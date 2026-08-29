#!/usr/bin/env python3
"""Reshape the NCRB disposal tables into one table for crime.html.

The same total-row trap as the prisons data: every NCRB table carries
'Total (States)', 'Total (UTs)' and 'Total (All India)', so summing a column
returns exactly three times the real figure. Totals are read from the total
row, the parts are summed separately, and the build refuses to write if the
two disagree.

The column names are long and positional -- 'chargesheeting_rate__col_18_19__
100______col__23_' -- so they are mapped by prefix rather than by exact name.
The mapping is asserted: a source that renames or reorders a column fails here
instead of producing a page of blanks.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "crime-india.json"
OUT = ROOT / "data" / "crime-explorer.json"
PAGE = ROOT / "crime.html"

SLOT = re.compile(
    r'(<script id="crime-data" type="application/json">)(.*?)(</script>)', re.S)

# Column names are matched on their letters alone. The same column is named
# 'charge_sheets_submitted___cases_charge_sheeted__col_16_col_17______col__18_'
# in one table and 'chargesheets_submitted___cases_chargesheeted__col_16_col_17
# ___col_18_' in the next: the underscore runs and the word split differ per
# table, and an exact-name mapping quietly matched nothing for IPC while
# working for crime against women. Stripping to letters makes the two
# identical, and the count assert below still catches a real rename.
POLICE_FIELDS = {
    "casesreportedduringtheyear": "reported",
    "totalcasesforinvestigation": "for_investigation",
    # 'col' after 'chargesheeted' distinguishes the total from the two
    # sub-rows, which continue 'outofcases...'.
    "chargesheetssubmittedcaseschargesheetedcol": "chargesheeted",
    "casespendinginvsgnatendoftheyear": "pending_police",
    "chargesheetingrate": "chargesheeting_rate",
    "pendencypercentage": "police_pendency",
}
COURT_FIELDS = {
    "totalcasesfortrial": "for_trial",
    "casesconvictedcol": "convicted",
    "casesacquitted": "acquitted",
    "casesinwhichtrialswerecompleted": "trials_completed",
    "casespendingtrialatendoftheyear": "pending_court",
    "convictionrate": "conviction_rate",
    "pendencypercentage": "court_pendency",
}


def letters(s):
    return re.sub(r"[^a-z]+", "", str(s).lower())

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
    s = re.sub(r"\but\b|\bstate\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def key(s):
    k = norm(s)
    return ALIAS.get(k, k)


def num(x):
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


def is_total(name):
    return "total" in str(name).lower()


def resolve(fields, mapping, label):
    """prefix -> real column name, asserting each one is found exactly once."""
    out = {}
    for prefix, short in mapping.items():
        hits = [f for f in fields if letters(f).startswith(prefix)]
        if len(hits) != 1:
            print(f"FAIL - {label}: expected exactly one column starting "
                  f"'{prefix}', found {len(hits)}: {hits[:3]}. The source has "
                  "changed shape; the mapping has to be updated rather than "
                  "silently producing blanks.")
            return None
        out[short] = hits[0]
    return out


def read_stage(block, mapping, label):
    if not block:
        return None, None
    rows = block["rows"]
    fields = list(rows[0].keys())
    cols = resolve(fields, mapping, label)
    if cols is None:
        return False, None
    # Even the state column is named differently per table -- 'state_ut',
    # 'state_ut__col_2_', 'state_ut___col__2__'. A hardcoded 'state_ut' read
    # None for five of the eight tables, which looked exactly like a source
    # with no total row.
    namecol = [f for f in fields if letters(f).startswith("stateut")]
    if len(namecol) != 1:
        print(f"FAIL - {label}: expected one state column, found {namecol}")
        return False, None
    namecol = namecol[0]
    real, total = {}, None
    for r in rows:
        name = r.get(namecol)
        vals = {short: num(r.get(col)) for short, col in cols.items()}
        if is_total(name):
            if "all india" in str(name).lower():
                total = vals
            continue
        real[key(name)] = dict(vals, name=(name or "").strip())
    return real, total


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
        print(f'FAIL - no <script id="crime-data"> block in {PAGE.name}')
        return 1
    if m.group(2) == js:
        print(f"  {PAGE.name} data is current")
        return 0
    if check_only:
        print(f"FAIL - {PAGE.name} carries stale data. Run "
              "`python3 scripts/build-crime-explorer-data.py`.")
        return 1
    PAGE.write_text(html[:m.start(2)] + js + html[m.end(2):], encoding="utf-8")
    print(f"  injected {len(js):,} bytes into {PAGE.name}")
    return 0


def main():
    check_only = "--check" in sys.argv
    raw = json.loads(SRC.read_text(encoding="utf-8"))

    pop = {}
    for r in raw["series"]["population"]["rows"]:
        p = num(r.get("population_2011"))
        k = key(r["india___state__union_territory"])
        if p and k != "india":
            pop[k] = pop.get(k, 0) + p

    tracks = {}
    for name, t in raw["tracks"].items():
        pol, pol_tot = read_stage(t["police"], POLICE_FIELDS, f"{name}/police")
        crt, crt_tot = read_stage(t["court"], COURT_FIELDS, f"{name}/court")
        if pol is False or crt is False:
            return 1

        # The double-count guard, per stage. Summing a column that contains
        # Total (States), Total (UTs) and Total (All India) returns 3x.
        for stage, real, total, field in (("police", pol, pol_tot, "reported"),
                                          ("court", crt, crt_tot, "for_trial")):
            if real is None:
                continue
            if total is None:
                print(f"FAIL - {name}/{stage}: no 'Total (All India)' row, so the "
                      "double-count guard cannot be trusted. Check the source.")
                return 1
            parts = sum(v.get(field) or 0 for v in real.values())
            whole = total.get(field)
            if whole is None or abs(parts - whole) > max(1.0, whole * 0.005):
                print(f"FAIL - {name}/{stage}: states sum to {parts:,.0f} on "
                      f"'{field}' but the source's own total says "
                      f"{(whole or 0):,.0f}.")
                return 1

        states = []
        for k in sorted(set(list(pol or {}) + list(crt or {}))):
            p = (pol or {}).get(k, {})
            c = (crt or {}).get(k, {})
            row = {"name": p.get("name") or c.get("name"),
                   "population_2011": pop.get(k)}
            for f in POLICE_FIELDS.values():
                row[f] = p.get(f)
            for f in COURT_FIELDS.values():
                row[f] = c.get(f)
            states.append(row)

        national = {}
        for f in POLICE_FIELDS.values():
            national[f] = (pol_tot or {}).get(f)
        for f in COURT_FIELDS.values():
            national[f] = (crt_tot or {}).get(f)

        tracks[name] = {
            "label": t["label"],
            "has_court": crt is not None,
            "national": national,
            "states": sorted(states, key=lambda s: s["name"] or ""),
        }

    out = {
        "_source": raw["_source"],
        "_licence": raw["_licence"],
        "_fetched": raw["_fetched"],
        "_built_by": "scripts/build-crime-explorer-data.py",
        "_caveats": [
            "Registered crime measures reporting as much as it measures crime. "
            "Whether an incident becomes a case depends on whether the person "
            "harmed goes to a police station and whether that station writes it "
            "down, and both vary enormously between states. A state with more "
            "registered cases may be a state where reporting works.",
            "This page therefore ranks states on what happened to the cases they "
            "did register -- chargesheeting, conviction, how much is still "
            "pending -- rather than on how much crime they have.",
            "Conviction rate here is convictions as a share of trials completed "
            "in the year, which is how NCRB defines it. It is not the share of "
            "reported cases that end in a conviction: most cases are still "
            "pending, and they are counted in the pendency figures instead.",
            "Cases pending at the end of the year include cases carried over "
            "from previous years, so a state can charge-sheet everything it "
            "received and still show high pendency from an older backlog.",
            "NCRB publishes state-wise court disposal for some categories and "
            "not others. Where it does not, the court panels say so rather than "
            "showing an empty chart.",
        ],
        "tracks": tracks,
    }

    js = payload_for_page(out)
    serialised = json.dumps(out, ensure_ascii=False, indent=1)
    if check_only:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != serialised:
            print(f"FAIL - {OUT.name} is stale. Run "
                  "`python3 scripts/build-crime-explorer-data.py`.")
            return 1
        print(f"  {OUT.name} is current")
    else:
        OUT.write_text(serialised, encoding="utf-8")
    rc = sync_page(js, check_only)
    if rc:
        return rc

    print("PASS" if check_only else f"wrote {OUT.relative_to(ROOT)}")
    for name, t in tracks.items():
        n = t["national"]
        print(f"  {t['label']:36s} {len(t['states'])} states  "
              f"reported {(n.get('reported') or 0):>9,.0f}  "
              f"chargesheet {(n.get('chargesheeting_rate') or 0):5.1f}%  "
              + (f"conviction {(n.get('conviction_rate') or 0):5.1f}%"
                 if t["has_court"] else "no state-wise court data"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
