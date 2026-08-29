#!/usr/bin/env python3
"""Snapshot the district-month MGNREGA series into data/mgnrega-india.json.

One resource, ~416,000 rows: every district, every month, FY2019-20 onward.
That is a 20-minute fetch, so it is a separate script from the build step --
you re-run this to refresh the data and the build step every time you change
how it is read.

Source: Ministry of Rural Development, via data.gov.in.
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datagov  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "mgnrega-india.json"
RESOURCE = "ee03643a-ee4c-48c2-ac30-9f2ff26ab722"

# The columns the explorer uses. The source carries 35; carrying all of them
# would quadruple the file for fields nothing reads.
KEEP = [
    "fin_year", "month", "state_name", "district_name",
    "Average_Wage_rate_per_day_per_person",
    "Average_days_of_employment_provided_per_Household",
    "Total_Households_Worked", "Total_Individuals_Worked",
    "Total_No_of_Active_Workers",
    "Total_No_of_HHs_completed_100_Days_of_Wage_Employment",
    "Persondays_of_Central_Liability_so_far",
    "Women_Persondays", "SC_persondays", "ST_persondays",
    "Total_Exp", "Wages",
    "percentage_payments_gererated_within_15_days",
]


def main():
    if datagov.page_size() == 10:
        print("FAIL - this needs a registered key; the demo key's 10-row cap\n"
              "       would make this a 41,000-request fetch. Set DATA_GOV_KEY.")
        return 1
    print(f"  MGNREGA district-month series ({RESOURCE})")
    rows = datagov.fetch_all(RESOURCE)
    slim = [{k: r.get(k) for k in KEEP} for r in rows]
    out = {
        "_source": "Ministry of Rural Development, via data.gov.in (Open Government Data Platform)",
        "_licence": "Government Open Data Licence - India",
        "_note": ("District-by-month MGNREGA physical and financial progress. "
                  "Snapshot -- refresh with scripts/fetch-mgnrega-data.py."),
        "_fetched": time.strftime("%Y-%m-%d"),
        "_resource_id": RESOURCE,
        "columns": KEEP,
        "rows": slim,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)}  {len(slim):,} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
