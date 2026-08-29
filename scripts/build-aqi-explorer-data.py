#!/usr/bin/env python3
"""Reshape the CPCB station readings into one table for aqi.html.

Three things this handles that would otherwise go quietly wrong:

  1. A station that reports no value for a pollutant sends the string 'NA',
     not a zero. 330 of 3,514 rows are like that. Averaged as zero, a city
     with two working sensors and one dead one reads a third cleaner than it
     is.
  2. Readings are per station, and cities have between one and a dozen. A
     city figure is the mean of its stations, so a city is never ranked on a
     single sensor without saying how many it has.
  3. 'Real time' means the hour the snapshot was taken. Every reading in the
     file carries the same timestamp, and the build asserts that: a file
     mixing hours would be averaging across time without saying so.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "aqi-india.json"
OUT = ROOT / "data" / "aqi-explorer.json"
PAGE = ROOT / "aqi.html"

SLOT = re.compile(
    r'(<script id="aqi-data" type="application/json">)(.*?)(</script>)', re.S)

# The order the page offers them in: the two that drive health guidance first.
POLLUTANTS = ["PM2.5", "PM10", "NO2", "SO2", "OZONE", "CO", "NH3"]

ALIAS = {"nct of delhi": "delhi", "orissa": "odisha", "pondicherry": "puducherry",
         "uttaranchal": "uttarakhand", "a n island": "andaman nicobar island",
         "dadra nagar haveli": "dadra nagar haveli daman diu",
         "daman diu": "dadra nagar haveli daman diu"}


def norm(s):
    s = (s or "").lower().strip().replace("&", " and ")
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z]+", " ", s).strip()
    s = re.sub(r"\band\b", " ", s)
    s = re.sub(r"\bislands?\b", "island", s)
    return re.sub(r"\s+", " ", s).strip()


def key(s):
    k = norm(s)
    return ALIAS.get(k, k)


def num(x):
    """'NA' is a station that did not report, and is not a zero."""
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    t = str(x).strip().replace(",", "")
    if t in ("", "NA", "N/A", "-", "--"):
        return None
    try:
        return float(t)
    except ValueError:
        return None


def mean(vals):
    v = [x for x in vals if x is not None]
    return sum(v) / len(v) if v else None


def payload_for_page(d):
    js = json.dumps(d, ensure_ascii=True, separators=(",", ":"))
    assert "</" not in js, "data contains a tag close; would end the script block"
    return js


def sync_page(js, check_only):
    if not PAGE.exists():
        print(f"FAIL - {PAGE.name} is missing")
        return 1
    html = PAGE.read_text(encoding="utf-8")
    m = SLOT.search(html)
    if not m:
        print(f'FAIL - no <script id="aqi-data"> block in {PAGE.name}')
        return 1
    if m.group(2) == js:
        print(f"  {PAGE.name} data is current")
        return 0
    if check_only:
        print(f"FAIL - {PAGE.name} carries stale data. Run "
              "`python3 scripts/build-aqi-explorer-data.py`.")
        return 1
    PAGE.write_text(html[:m.start(2)] + js + html[m.end(2):], encoding="utf-8")
    print(f"  injected {len(js):,} bytes into {PAGE.name}")
    return 0


def main():
    check_only = "--check" in sys.argv
    raw = json.loads(SRC.read_text(encoding="utf-8"))
    rows = raw["series"]["readings"]["rows"]

    stamps = {r.get("last_update") for r in rows if r.get("last_update")}
    if len(stamps) != 1:
        print("FAIL - the snapshot mixes "
              f"{len(stamps)} reading times: {sorted(stamps)[:4]}. Averaging "
              "across them would blend hours without saying so.")
        return 1
    reading_time = stamps.pop()

    pop = {}
    for r in raw["series"]["population"]["rows"]:
        p = num(r.get("population_2011"))
        k = key(r["india___state__union_territory"])
        if p and k != "india":
            pop[k] = pop.get(k, 0) + p

    # station -> its readings, keeping the identity of the place
    stations = {}
    for r in rows:
        sid = r.get("station")
        s = stations.setdefault(sid, {
            "station": sid, "city": (r.get("city") or "").strip(),
            "state": (r.get("state") or "").strip(),
            "lat": num(r.get("latitude")), "lon": num(r.get("longitude")),
            "v": {}})
        v = num(r.get("avg_value"))
        if v is not None:
            s["v"][r.get("pollutant_id")] = v

    cities = {}
    for s in stations.values():
        c = cities.setdefault((s["state"], s["city"]),
                              {"city": s["city"], "state": s["state"],
                               "stations": 0, "vals": {p: [] for p in POLLUTANTS}})
        c["stations"] += 1
        for p in POLLUTANTS:
            if p in s["v"]:
                c["vals"][p].append(s["v"][p])

    city_rows = []
    for c in cities.values():
        row = {"city": c["city"], "state": c["state"], "stations": c["stations"],
               "reporting": {}, "v": {}}
        for p in POLLUTANTS:
            row["v"][p] = mean(c["vals"][p])
            row["reporting"][p] = len(c["vals"][p])
        city_rows.append(row)

    state_rows = []
    for st in sorted({s["state"] for s in stations.values()}):
        k = key(st)
        n = sum(1 for s in stations.values() if s["state"] == st)
        ncity = len({s["city"] for s in stations.values() if s["state"] == st})
        p = pop.get(k)
        state_rows.append({
            "state": st, "stations": n, "cities": ncity, "population_2011": p,
            "per_10m": 1e7 * n / p if p else None,
            "v": {q: mean([s["v"].get(q) for s in stations.values() if s["state"] == st])
                  for q in POLLUTANTS},
        })

    missing = sum(1 for r in rows if num(r.get("avg_value")) is None)
    out = {
        "_source": raw["_source"],
        "_licence": raw["_licence"],
        "_fetched": raw["_fetched"],
        "_built_by": "scripts/build-aqi-explorer-data.py",
        "reading_time": reading_time,
        "_caveats": [
            "These are readings from one hour, not an average over a day or a "
            "year. Air quality swings with the time of day, the weather and the "
            "season, so a single hour ranks the hour, not the city.",
            "A station that did not report a pollutant is left out of the "
            "average rather than counted as zero. Each figure shows how many of "
            "the city's stations reported it.",
            "Values are concentrations in micrograms per cubic metre (milligrams "
            "for CO), not the composite Air Quality Index number. The AQI is "
            "derived from the worst pollutant at a station over a longer window.",
            "Stations sit where they were installed, usually in larger cities. "
            "A state with no station is not a state with clean air; it is a "
            "state with no measurement.",
            "Population is Census 2011, the most recent enumerated count India "
            "has, so people per station uses a 2011 denominator.",
        ],
        "pollutants": POLLUTANTS,
        "totals": {
            "stations": len(stations), "cities": len(cities),
            "states": len({s["state"] for s in stations.values()}),
            "readings": len(rows), "not_reported": missing,
        },
        "cities": sorted(city_rows, key=lambda c: (c["state"], c["city"])),
        "states": sorted(state_rows, key=lambda s: s["state"]),
    }

    js = payload_for_page(out)
    serialised = json.dumps(out, ensure_ascii=False, indent=1)
    if check_only:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != serialised:
            print(f"FAIL - {OUT.name} is stale. Run "
                  "`python3 scripts/build-aqi-explorer-data.py`.")
            return 1
        print(f"  {OUT.name} is current")
    else:
        OUT.write_text(serialised, encoding="utf-8")
    rc = sync_page(js, check_only)
    if rc:
        return rc

    print("PASS" if check_only else f"wrote {OUT.relative_to(ROOT)}")
    t = out["totals"]
    print(f"  {t['stations']} stations, {t['cities']} cities, {t['states']} states")
    print(f"  reading time {reading_time}; {missing:,} of {t['readings']:,} "
          f"station-pollutant readings not reported")
    joined = sum(1 for s in state_rows if s["per_10m"])
    print(f"  {joined}/{len(state_rows)} states have a population figure")
    return 0


if __name__ == "__main__":
    sys.exit(main())
