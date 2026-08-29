#!/usr/bin/env python3
"""Reshape the district-month MGNREGA series into one table for mgnrega.html.

The trap here is different from the other explorers, and worse, because the
result of getting it wrong looks entirely plausible.

Most columns in this source are CUMULATIVE WITHIN THE FINANCIAL YEAR. The
March row for a district is that district's whole year; the December row is
April to December. Summing the twelve months -- the obvious thing to do --
returns roughly six times the real figure and a number that is still the right
order of magnitude, still ranks states in about the right order, and is wrong
everywhere. So the year's value is the LAST MONTH PRESENT, not the sum, and the
build asserts the series is non-decreasing before it believes that.

The check matters both ways: if the source ever switches to monthly flows, the
assertion fails and this script stops, rather than silently reporting one
month as a year.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "mgnrega-india.json"
OUT = ROOT / "data" / "mgnrega-explorer.json"
PAGE = ROOT / "mgnrega.html"

SLOT = re.compile(
    r'(<script id="mgnrega-data" type="application/json">)(.*?)(</script>)', re.S)

# Financial year order. The source writes months inconsistently -- 'Sep' and
# 'September', 'July' and 'Jul' -- so the first three letters are the key.
FY_MONTHS = ["apr", "may", "jun", "jul", "aug", "sep",
             "oct", "nov", "dec", "jan", "feb", "mar"]
MONTH_IX = {m: i for i, m in enumerate(FY_MONTHS)}

# The cumulative counters. These must never be summed across months.
CUMULATIVE = [
    "Total_Households_Worked", "Total_Individuals_Worked",
    "Total_No_of_Active_Workers",
    "Total_No_of_HHs_completed_100_Days_of_Wage_Employment",
    "Persondays_of_Central_Liability_so_far",
    "Women_Persondays", "SC_persondays", "ST_persondays",
    "Total_Exp", "Wages",
]
# Rates and averages, also year-to-date rather than monthly.
RATES = [
    "Average_Wage_rate_per_day_per_person",
    "Average_days_of_employment_provided_per_Household",
    "percentage_payments_gererated_within_15_days",
]

SHORT = {
    "Total_Households_Worked": "households",
    "Total_Individuals_Worked": "individuals",
    "Total_No_of_Active_Workers": "active_workers",
    "Total_No_of_HHs_completed_100_Days_of_Wage_Employment": "hh_100_days",
    "Persondays_of_Central_Liability_so_far": "persondays",
    "Women_Persondays": "women_persondays",
    "SC_persondays": "sc_persondays",
    "ST_persondays": "st_persondays",
    "Total_Exp": "expenditure",
    "Wages": "wages",
    "Average_Wage_rate_per_day_per_person": "wage_rate",
    "Average_days_of_employment_provided_per_Household": "days_per_household",
    "percentage_payments_gererated_within_15_days": "paid_in_15_days",
}


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


def month_ix(m):
    return MONTH_IX.get(str(m).strip().lower()[:3])


def title(s):
    """Source writes states and districts in shouting caps."""
    s = " ".join(str(s or "").split()).title()
    for a, b in (("And ", "and "), ("Of ", "of "), ("The ", "the ")):
        s = s.replace(" " + a, " " + b)
    return s


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
        print(f'FAIL - no <script id="mgnrega-data"> block in {PAGE.name}')
        return 1
    if m.group(2) == js:
        print(f"  {PAGE.name} data is current")
        return 0
    if check_only:
        print(f"FAIL - {PAGE.name} carries stale data. Run "
              "`python3 scripts/build-mgnrega-explorer-data.py`.")
        return 1
    PAGE.write_text(html[:m.start(2)] + js + html[m.end(2):], encoding="utf-8")
    print(f"  injected {len(js):,} bytes into {PAGE.name}")
    return 0


def main():
    check_only = "--check" in sys.argv
    raw = json.loads(SRC.read_text(encoding="utf-8"))
    rows = raw["rows"]

    # (year, state, district) -> {month index: row}
    cell = {}
    bad_month = 0
    for r in rows:
        mi = month_ix(r.get("month"))
        if mi is None:
            bad_month += 1
            continue
        k = (r.get("fin_year"), r.get("state_name"), r.get("district_name"))
        cell.setdefault(k, {})[mi] = r
    if bad_month:
        print(f"FAIL - {bad_month:,} rows have a month this script cannot place "
              "in the financial year. Taking the last month would then be "
              "taking an arbitrary month.")
        return 1

    # The assumption this whole script rests on: within a year, a cumulative
    # column never goes down. Checked on every district-year, not a sample.
    violations = []
    for k, months in cell.items():
        order = sorted(months)
        for col in ("Persondays_of_Central_Liability_so_far",
                    "Total_Households_Worked"):
            prev = None
            for mi in order:
                v = num(months[mi].get(col))
                if v is None:
                    continue
                if prev is not None and v < prev * 0.999:
                    violations.append((k, col, prev, v))
                    break
                prev = v
    if len(violations) > len(cell) * 0.02:
        print(f"FAIL - {len(violations):,} of {len(cell):,} district-years have a "
              "cumulative column that goes DOWN during the year. The columns are "
              "not year-to-date after all, and taking the last month would report "
              "one month as a year. First few:")
        for k, col, a, b in violations[:5]:
            print(f"    {k} {col}: {a:,.0f} -> {b:,.0f}")
        return 1

    districts = {}
    years = set()
    for (fy, state, district), months in cell.items():
        last = months[max(months)]
        years.add(fy)
        d = districts.setdefault((state, district),
                                 {"state": title(state), "district": title(district),
                                  "y": {}})
        vals = {}
        for src in CUMULATIVE + RATES:
            vals[SHORT[src]] = num(last.get(src))
        vals["months_reported"] = len(months)
        d["y"][fy] = vals

    year_list = sorted(years)
    dist_list = sorted(districts.values(), key=lambda d: (d["state"], d["district"]))

    # State and national roll-ups. Counts add across districts; rates have to
    # be re-derived from their own numerator and denominator, because a mean of
    # district percentages weights a district of 40,000 like one of 4 million.
    def rollup(members, fy):
        out = {}
        for f in ("households", "individuals", "active_workers", "hh_100_days",
                  "persondays", "women_persondays", "sc_persondays",
                  "st_persondays", "expenditure", "wages"):
            vals = [m["y"].get(fy, {}).get(f) for m in members]
            vals = [v for v in vals if v is not None]
            out[f] = sum(vals) if vals else None
        # Average days per household = person-days / households, not the mean
        # of the district averages.
        out["days_per_household"] = (out["persondays"] / out["households"]
                                     if out["persondays"] and out["households"] else None)
        # The wage rate and the 15-day share have no published denominator per
        # district, so these are weighted by person-days, and the page says so.
        for f in ("wage_rate", "paid_in_15_days"):
            num_, den = 0.0, 0.0
            for m in members:
                v = m["y"].get(fy, {}).get(f)
                w = m["y"].get(fy, {}).get("persondays")
                if v is not None and w:
                    num_ += v * w
                    den += w
            out[f] = num_ / den if den else None
        out["districts"] = len(members)
        return out

    by_state = {}
    for d in dist_list:
        by_state.setdefault(d["state"], []).append(d)
    states = [{"state": st, "y": {fy: rollup(ms, fy) for fy in year_list}}
              for st, ms in sorted(by_state.items())]
    national = {fy: rollup(dist_list, fy) for fy in year_list}

    out = {
        "_source": raw["_source"],
        "_licence": raw["_licence"],
        "_fetched": raw["_fetched"],
        "_built_by": "scripts/build-mgnrega-explorer-data.py",
        "_caveats": [
            "The Act guarantees 100 days of wage employment per rural household "
            "in a financial year, on demand. Days provided is what was actually "
            "worked, which is not the same as what was demanded and not the same "
            "as what was needed.",
            "Figures in this source are cumulative within the financial year, so "
            "each year's value is its last reported month rather than a sum of "
            "the months. A district that stopped reporting in December shows the "
            "year to December.",
            "The wage rate and the share of payments generated within 15 days are "
            "averaged across districts weighted by person-days, because the "
            "source publishes no denominator for them. A simple mean would let a "
            "district of forty thousand outweigh one of four million.",
            "'Payments generated within 15 days' is when the payment order was "
            "raised, not when money reached the worker's account. The gap between "
            "the two is not in this data.",
            "Districts are as the source names them, and district boundaries have "
            "changed over these years. A district created mid-series appears only "
            "from the year it starts reporting.",
        ],
        "years": year_list,
        "national": national,
        "states": states,
        "districts": dist_list,
    }

    js = payload_for_page(out)
    serialised = json.dumps(out, ensure_ascii=False, indent=1)
    if check_only:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != serialised:
            print(f"FAIL - {OUT.name} is stale. Run "
                  "`python3 scripts/build-mgnrega-explorer-data.py`.")
            return 1
        print(f"  {OUT.name} is current")
    else:
        OUT.write_text(serialised, encoding="utf-8")
    rc = sync_page(js, check_only)
    if rc:
        return rc

    print("PASS" if check_only else f"wrote {OUT.relative_to(ROOT)}")
    print(f"  {len(dist_list):,} districts, {len(states)} states, "
          f"{len(year_list)} years: {year_list[0]} to {year_list[-1]}")
    print(f"  {len(violations):,} district-years with a non-monotonic cumulative "
          f"column ({100*len(violations)/max(1,len(cell)):.2f}%, tolerated below 2%)")
    for fy in year_list:
        n = national[fy]
        print(f"  {fy}: {(n['households'] or 0)/1e7:5.2f} cr households, "
              f"{(n['persondays'] or 0)/1e7:6.1f} cr person-days, "
              f"avg {(n['days_per_household'] or 0):4.1f} days, "
              f"{(n['paid_in_15_days'] or 0):4.1f}% paid in 15 days")
    return 0


if __name__ == "__main__":
    sys.exit(main())
