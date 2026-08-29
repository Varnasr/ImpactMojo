#!/usr/bin/env python3
"""Snapshot the prison and court-pendency tables into data/justice-india.json.

Small tables -- one row per state, a dozen or so of them -- so this runs in
under a minute even on the shared demo key.

Sources, all via data.gov.in:
  National Crime Records Bureau, Prison Statistics India 2023
  Department of Justice / Supreme Court, pendency as reported to Parliament
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datagov  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "justice-india.json"

RESOURCES = {
    # --- prisons, as on 31-12-2023 -----------------------------------------
    "occupancy": ("7fceae29-0ae6-45d3-81ef-309d4f989799",
                  "State/UT-wise Capacity, Inmate Population and Occupancy Rate of Jails as on 31-12-2023"),
    "types": ("52b18256-7c08-4689-853e-fabfa8977d30",
              "State/UT-wise Types of Prison Inmates as on 31-12-2023"),
    # How long people who have not been convicted have already been inside.
    "duration": ("db4bb26f-f008-41a9-a05e-ee0e50434702",
                 "State/UT-wise Number of Undertrial Prisoners by Duration of Confinement as on 31-12-2023"),
    # Section 436A CrPC: an undertrial who has served half the maximum sentence
    # for the offence charged is entitled to release. This table is how often
    # that entitlement was acted on.
    "s436a": ("f1bc9e58-5eb6-439b-852b-3fb8b3aeda01",
              "State/UT-wise Status of Undertrial Inmates under Section 436A of Cr.P.C. during 2023"),
    "caste": ("6e069039-64bd-43da-8f5a-15cb697caf1b",
              "State/UT-wise Caste of Undertrial Prisoners as on 31-12-2023"),
    "religion": ("62bdc6b5-4147-47a9-82fa-a3fa36918cfb",
                 "State/UT-wise Religion of Undertrial Prisoners as on 31-12-2023"),
    "education": ("4a07d5ff-d12d-4de8-bfb4-18636178a725",
                  "State/UT-wise Education Profile of Undertrial Prisoners as on 31-12-2023"),
    "women_jails": ("10617167-ed89-4315-9501-ee46097eb6f7",
                    "State/UT-wise Capacity, Inmates Population and Occupancy Rate of Women Jails as on 31-12-2023"),
    # --- courts -------------------------------------------------------------
    "district_courts": ("a462752d-c47b-45ed-ae18-f172ed6ffbc8",
                        "State/UT-wise Pendency of Cases in District Courts as on 07-12-2023"),
    "high_courts": ("e5702dd4-9f39-4d32-9138-697b62aad854",
                    "High Court-wise Pendency of Cases as on 07-12-2023"),
    "pendency_age": ("3cdf56d6-0c30-4344-8d5c-9965feb53b1f",
                     "Age-wise Pendency of Civil and Criminal Cases in District and Subordinate Courts"),
    "pocso": ("1ef6fac8-8d4a-4747-bd14-5a3f8ab6d176",
              "State/UT-wise Pendency of Rape and POCSO Act Cases as on 31-10-2024"),
    # --- denominators -------------------------------------------------------
    # Pendency and prison numbers mean little without a population to divide
    # by, and the caste profile of undertrials means nothing without the caste
    # profile of the state they were arrested in.
    "population": ("cd3f9ecd-0bc3-406a-bb7d-8562ffb75083",
                   "State/UT-wise Population, Decadal Growth Rate and Density, Census 2011"),
    "sc_st": ("c1c221ef-324a-4715-bc02-58172107c162",
              "Population of Scheduled Castes and Scheduled Tribes (Census 2011)"),
    # A second, independent ST count. Needed because the ST columns of the
    # table above are scrambled across rows -- Kerala's row carries Madhya
    # Pradesh's ST population and percentage, Madhya Pradesh's carries
    # Chhattisgarh's, Jharkhand's carries Karnataka's. The column still sums to
    # the correct national total, so nothing about it looks wrong until you
    # check a state against the published census figure. This one matches the
    # published figure for every state tested, and the build step requires the
    # two to agree before it will use a state's numbers.
    "st_mota": ("a5cd7e55-2e13-4017-9f8c-410dad9cc518",
                "State/UT-wise Scheduled Tribe population as per Census 2011 (Ministry of Tribal Affairs)"),
}


def main():
    out = {
        "_source": ("National Crime Records Bureau (Prison Statistics India 2023) and the "
                    "Department of Justice, via data.gov.in (Open Government Data Platform)"),
        "_licence": "Government Open Data Licence - India",
        "_note": ("Prison figures are a single-day census as on 31-12-2023; court "
                  "pendency is as reported to Parliament on the date in each title. "
                  "Snapshot -- refresh with scripts/fetch-justice-data.py."),
        "_fetched": time.strftime("%Y-%m-%d"),
        "series": {},
    }
    for name, (rid, title) in RESOURCES.items():
        print(f"  {name}: {title[:70]}")
        rows = datagov.fetch_all(rid, quiet=True)
        print(f"    {len(rows)} rows")
        out["series"][name] = {"resource_id": rid, "title": title, "rows": rows}

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
