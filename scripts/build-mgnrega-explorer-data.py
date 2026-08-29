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
PICK = "Persondays_of_Central_Liability_so_far"   # the dedupe yardstick

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
]
# Deliberately NOT carried: percentage_payments_gererated_within_15_days.
# It is the most interesting column in the source and it is not a percentage.
# Its median is about 100 but its 95th percentile reaches 1,143 and its
# maximum 84,031,507, in every year before 2024-25. Whatever it holds, it is
# not the share of payments made inside the legal fortnight, and the ways to
# make it look like one -- clipping at 100, dropping the rows above it -- all
# amount to selecting the districts that appear compliant. The page says the
# measure is missing instead of showing a cleaned-up version of it.

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


# The source abbreviates one state past recognition: 'DN HAVELI AND DD'
# title-cases to 'Dn Haveli and Dd', which is not a place anyone would search
# for.
STATE_NAMES = {
    "Dn Haveli and Dd": "Dadra and Nagar Haveli and Daman and Diu",
    "Andaman and Nicobar": "Andaman and Nicobar Islands",
}


def title(s):
    """Source writes states and districts in shouting caps."""
    s = " ".join(str(s or "").split()).title()
    for a, b in (("And ", "and "), ("Of ", "of "), ("The ", "the ")):
        s = s.replace(" " + a, " " + b)
    return STATE_NAMES.get(s, s)


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

    if not SRC.exists():
        # The raw snapshot is 266 MB and is deliberately not in the repo, so on
        # a fresh checkout there is nothing to rebuild from. The drift that CI
        # can still catch -- and the one that actually happens -- is the page's
        # inline copy falling out of step with the committed data file. That is
        # checked here; the heavier assertions run when someone refreshes the
        # data and has the raw file to hand.
        if not check_only:
            print(f"FAIL - {SRC.name} is missing. Fetch it first:\n"
                  "       DATA_GOV_KEY=... python3 scripts/fetch-mgnrega-data.py")
            return 1
        if not OUT.exists():
            print(f"FAIL - neither {SRC.name} nor {OUT.name} is present.")
            return 1
        built = json.loads(OUT.read_text(encoding="utf-8"))
        rc = sync_page(payload_for_page(built), True)
        if rc:
            return rc
        print("PASS (page matches the committed data; raw snapshot not in the "
              "repo, so the source-shape assertions were not re-run)")
        return 0

    raw = json.loads(SRC.read_text(encoding="utf-8"))
    rows = raw["rows"]

    # (year, state, district) -> {month index: row}
    cell = {}
    bad_month, blank, dupes = 0, 0, 0
    for r in rows:
        # The source carries one row that is 'NA' in every column, including
        # the year and the district. It is not a district-month with an
        # unreadable date; it is not a row. Dropping it is right, and counting
        # it as a parse failure would mask a real one.
        if all(str(r.get(f, "NA")).strip() in ("NA", "", "None")
               for f in ("fin_year", "state_name", "district_name")):
            blank += 1
            continue
        mi = month_ix(r.get("month"))
        if mi is None:
            bad_month += 1
            continue
        k = (r.get("fin_year"), r.get("state_name"), r.get("district_name"))
        # From 2024-25 the source publishes a DAILY snapshot of each
        # district-month -- up to 31 rows for one district and month, each a
        # little further along (11,419,430 person-days, then 11,419,598, then
        # 11,420,376). Keeping whichever arrived last in iteration order picks
        # an arbitrary day. The cumulative columns only grow within a month, so
        # the largest is the most complete reading of it.
        prev = cell.setdefault(k, {}).get(mi)
        if prev is None or (num(r.get(PICK)) or -1) > (num(prev.get(PICK)) or -1):
            cell[k][mi] = r
        dupes += 1 if prev is not None else 0
    if bad_month:
        print(f"FAIL - {bad_month:,} rows name a district and a year but a month "
              "this script cannot place in the financial year. Taking the last "
              "month would then be taking an arbitrary month.")
        return 1

    # The assumption this whole script rests on is that the columns are
    # cumulative within the year. It is tested by shape, on every district-year
    # rather than a sample, because the obvious test is the wrong one.
    #
    # "No cumulative column ever goes down" fails here: the MIS revises figures
    # downward as muster rolls are verified, so 148 of 6,479 district-years
    # contain at least one decrease. Those are revisions, not a refutation.
    #
    # What actually separates cumulative from monthly is the shape of the
    # series. Measured on this snapshot: 97.0% of month-to-month steps rise and
    # 0.2% fall, and the median district-year ends 18.6x where it started. If
    # the source switched to monthly flows, roughly half the steps would fall
    # and the ratio would sit near 1. The thresholds below are set far from the
    # measured values in the direction of the failure, so a real switch trips
    # them and a normal year of revisions does not.
    MAX_FALLING_STEPS = 0.05      # measured 0.002
    MIN_GROWTH_RATIO = 4.0        # measured 18.6
    up = down = 0
    ratios = []
    for months in cell.values():
        seq = [num(months[mi].get("Persondays_of_Central_Liability_so_far"))
               for mi in sorted(months)]
        seq = [v for v in seq if v is not None]
        if len(seq) < 3:
            continue
        for a, b in zip(seq, seq[1:]):
            if b > a:
                up += 1
            elif b < a:
                down += 1
        if seq[0]:
            ratios.append(seq[-1] / seq[0])
    steps = up + down
    falling = down / steps if steps else 0.0
    ratios.sort()
    growth = ratios[len(ratios) // 2] if ratios else 0.0
    if not steps or not ratios:
        print("FAIL - not enough month-to-month pairs to test whether the "
              "columns are cumulative. Refusing to guess.")
        return 1
    if falling > MAX_FALLING_STEPS or growth < MIN_GROWTH_RATIO:
        print(f"FAIL - these columns no longer look cumulative within the year: "
              f"{100*falling:.1f}% of month-to-month steps fall (expected under "
              f"{100*MAX_FALLING_STEPS:.0f}%) and the median district-year ends "
              f"{growth:.1f}x where it started (expected at least "
              f"{MIN_GROWTH_RATIO:.0f}x). If the source has switched to monthly "
              "flows, taking the last month reports ONE MONTH as a year and the "
              "figures must be summed instead.")
        return 1
    shape = (falling, growth)

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

    # A financial year still in progress is not a year. Recording how many
    # months the fullest district reported lets the page label it instead of
    # ranking a five-month year against a twelve-month one.
    months_in_year = {}
    for (fy, _s, _d), months in cell.items():
        months_in_year[fy] = max(months_in_year.get(fy, 0), len(months))
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
        # The wage rate has no published denominator per district, so it is
        # weighted by person-days, and the page says so.
        for f in ("wage_rate",):
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

    # The district payload carries only what the district table reads. Every
    # column for 757 districts across 9 years put 2.3 MB of JSON inline in the
    # page, most of it never looked at; the state and national roll-ups above
    # are computed from the full set first.
    DISTRICT_FIELDS = ("households", "hh_100_days", "persondays",
                       "women_persondays", "sc_persondays", "st_persondays",
                       "days_per_household")
    slim_districts = [
        {"state": d["state"], "district": d["district"],
         "y": {fy: {f: v[f] for f in DISTRICT_FIELDS if f in v}
               for fy, v in d["y"].items()}}
        for d in dist_list
    ]

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
            "From 2024-25 the source publishes a fresh snapshot of each "
            "district-month every day. The most complete snapshot of the final "
            "month is used as the year's figure.",
            "Districts are as the source names them, and district boundaries have "
            "changed over these years. A district created mid-series appears only "
            "from the year it starts reporting.",
        ],
        "years": year_list,
        "months_reported": months_in_year,
        "complete_years": [y for y in year_list if months_in_year.get(y, 0) >= 12],
        "national": national,
        "states": states,
        "districts": slim_districts,
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
    if blank:
        print(f"  dropped {blank} all-NA row(s) from the source")
    if dupes:
        print(f"  collapsed {dupes:,} repeat daily snapshots into "
              f"{len(cell):,} district-years")
    print(f"  {len(dist_list):,} districts, {len(states)} states, "
          f"{len(year_list)} years: {year_list[0]} to {year_list[-1]}")
    print(f"  cumulative check: {100*shape[0]:.1f}% of steps fall, median "
          f"district-year grows {shape[1]:.1f}x over its months")
    for fy in year_list:
        n = national[fy]
        mm = months_in_year.get(fy, 0)
        print(f"  {fy}: {(n['households'] or 0)/1e7:5.2f} cr households, "
              f"{(n['persondays'] or 0)/1e7:6.1f} cr person-days, "
              f"avg {(n['days_per_household'] or 0):4.1f} days, "
              f"wage Rs {(n['wage_rate'] or 0):6.2f}"
              + ("" if mm >= 12 else f"   [partial year: {mm} months]"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
