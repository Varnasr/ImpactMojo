#!/usr/bin/env python3
"""Join the raw CSR snapshot into one clean table for csr.html.

The joins are done here, not in the browser, because they are the part most
likely to go quietly wrong: three sources spell states differently ("Daman &
Diu" vs "Daman and Diu"), one of them predates two of the UTs, and the CSR
table mixes real states with four rows that are not places at all.

Two traps this handles explicitly, either of which silently corrupts every
figure on the page:

  1. Both CSR series carry a "Total" ROW. Summing the column double-counts
     exactly -- 59,976 instead of the real 29,988 Cr for 2022-23.
  2. "PAN India", "PAN India (Other Centralized Funds)" and "NEC/Not
     Mentioned" are CSR that is not attributable to any state. Together they
     are a fifth of all spending. Dropping them silently would inflate every
     state's share; folding them into a state would be a lie.

Output keeps them as a separate `unattributed` block so the page can show
them rather than pretend they do not exist.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "csr-india.json"
OUT = ROOT / "data" / "csr-explorer.json"
PAGE = ROOT / "csr.html"

# The page reads its data from an inline <script type="application/json">
# rather than fetching the JSON file. One request instead of two, and the
# numbers cannot render half-loaded. Injected here so the file and the page
# cannot drift apart; `--check` fails CI if they have.
SLOT = re.compile(
    r'(<script id="csr-data" type="application/json">)(.*?)(</script>)', re.S)

YEARS = ["2018_19", "2019_20", "2020_21", "2021_22", "2022_23"]

# Rows in the CSR state table that are not places.
NON_GEO = {
    "total",
    "pan india",
    "pan india other centralized funds",
    "nec not mentioned",
}

ALIAS = {
    "leh ladakh": "ladakh",
    "nct of delhi": "delhi",
    "orissa": "odisha",
    "pondicherry": "puducherry",
    "uttaranchal": "uttarakhand",
}


def norm(s):
    s = (s or "").lower().strip().replace("&", " and ")
    s = re.sub(r"[^a-z]+", " ", s).strip()
    s = re.sub(r"\band\b", " ", s)          # "A and B" == "A & B"
    s = re.sub(r"\bislands?\b", "island", s)
    return re.sub(r"\s+", " ", s).strip()


def key(s):
    k = norm(s)
    return ALIAS.get(k, k)


def num(x):
    """Values arrive as numbers, numeric strings, or the literal 'NA'."""
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


def payload_for_page(d):
    """Compact copy of the explorer data, safe to inline in a <script> block.

    Two characters end that block early and blank the page: a literal
    `</script>` inside a string, and U+2028/U+2029, which are line
    terminators in JS source. `ensure_ascii` escapes the latter; the former
    cannot occur in this data, and the assert says so out loud rather than
    trusting it.
    """
    js = json.dumps(d, ensure_ascii=True, separators=(",", ":"))
    assert "</" not in js, "data contains a tag close; would end the script block"
    return js


def sync_page(js, check):
    if not PAGE.exists():
        print(f"FAIL - {PAGE.name} is missing")
        return 1
    html = PAGE.read_text(encoding="utf-8")
    m = SLOT.search(html)
    if not m:
        print(f"FAIL - no <script id=\"csr-data\"> block in {PAGE.name}")
        return 1
    if m.group(2) == js:
        print(f"  {PAGE.name} data is current")
        return 0
    if check:
        print(f"FAIL - {PAGE.name} carries stale data. Run "
              "`python3 scripts/build-csr-explorer-data.py`.")
        return 1
    PAGE.write_text(html[:m.start(2)] + js + html[m.end(2):], encoding="utf-8")
    print(f"  injected {len(js):,} bytes into {PAGE.name}")
    return 0


def main():
    check = "--check" in sys.argv
    raw = json.loads(SRC.read_text(encoding="utf-8"))
    S = raw["series"]

    pop = {}
    for r in S["population"]["rows"]:
        p = num(r.get("population_2011"))
        if p:
            pop[key(r["india___state__union_territory"])] = p

    nsdp = {}
    for r in S["nsdp"]["rows"]:
        nsdp[key(r["state_ut"])] = {
            y: num(r.get("_" + y)) for y in YEARS if ("_" + y) in r
        }

    states, unattributed, total_row = [], [], None
    for r in S["state"]["rows"]:
        name = (r["state_ut"] or "").strip()
        vals = {y: num(r.get(f"csr_expenditure_{y}")) for y in YEARS}
        n = norm(name)
        if n == "total":
            total_row = vals
            continue
        if n in NON_GEO:
            unattributed.append({"name": name, "csr": vals})
            continue
        k = key(name)
        states.append({
            "name": name,
            "csr": vals,
            "population_2011": pop.get(k),
            "nsdp_per_capita": nsdp.get(k, {}),
        })

    sectors = []
    sector_total = None
    for r in S["sector"]["rows"]:
        name = (r["development_sector"] or "").strip()
        vals = {y: num(r.get(f"csr_expenditure_{y}")) for y in YEARS}
        if norm(name) == "total":
            sector_total = vals
            continue
        sectors.append({"name": name, "csr": vals})

    if total_row is None or sector_total is None:
        print("FAIL - the source no longer carries a 'Total' row; the "
              "double-count guard below cannot be trusted. Check the source.")
        return 1

    # The two series must agree on the national total, and the parts must sum
    # to it. If either check fails the snapshot is malformed and the page
    # would render confidently wrong numbers.
    for y in YEARS:
        a, b = total_row.get(y), sector_total.get(y)
        if a is None or b is None or abs(a - b) > 1:
            print(f"FAIL - {y}: state total {a} != sector total {b}")
            return 1
        parts = sum(s["csr"][y] or 0 for s in states) \
            + sum(u["csr"][y] or 0 for u in unattributed)
        if abs(parts - a) > max(1.0, a * 0.005):
            print(f"FAIL - {y}: rows sum to {parts:,.0f} but Total says {a:,.0f}")
            return 1

    joined = sum(1 for s in states if s["population_2011"])
    out = {
        "_source": raw["_source"],
        "_licence": raw["_licence"],
        "_fetched": raw["_fetched"],
        "_built_by": "scripts/build-csr-explorer-data.py",
        "_caveats": [
            "CSR expenditure in rupees crore, financial years.",
            "Population is Census 2011 -- the most recent enumerated count "
            "India has, since the 2021 census was not held. Per-person figures "
            "are therefore CSR now over people counted then.",
            "'PAN India', 'PAN India (Other Centralized Funds)' and 'NEC/Not "
            "Mentioned' are CSR not attributable to any state. They are kept "
            "separate, not distributed across states.",
        ],
        "years": [y.replace("_", "-") for y in YEARS],
        "year_keys": YEARS,
        "national_total": total_row,
        "states": sorted(states, key=lambda s: s["name"]),
        "unattributed": unattributed,
        "sectors": sorted(sectors, key=lambda s: s["name"]),
    }
    js = payload_for_page(out)
    if check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != json.dumps(out, ensure_ascii=False, indent=1):
            print(f"FAIL - {OUT.name} is stale. Run "
                  "`python3 scripts/build-csr-explorer-data.py`.")
            return 1
        print(f"  {OUT.name} is current")
    else:
        OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    rc = sync_page(js, check)
    if rc:
        return rc

    t = total_row["2022_23"]
    una = sum(u["csr"]["2022_23"] or 0 for u in unattributed)
    print("PASS" if check else f"wrote {OUT.relative_to(ROOT)}")
    print(f"  {len(states)} states, {len(sectors)} sectors, "
          f"{len(unattributed)} unattributed rows")
    print(f"  {joined}/{len(states)} states have a population figure")
    print(f"  2022-23 total {t:,.0f} Cr, of which unattributed "
          f"{una:,.0f} Cr ({100*una/t:.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
