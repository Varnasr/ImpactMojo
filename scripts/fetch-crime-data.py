#!/usr/bin/env python3
"""Snapshot the NCRB case-disposal tables into data/crime-india.json.

This explorer deliberately covers what happens to a case after it is
registered, not how much crime a state has. Registered crime is a measure of
how willing people are to go to a police station and how willing that station
is to write it down, and comparing states on it says more about reporting than
about safety. Chargesheeting, conviction and pendency describe the machinery
handling the cases it did receive, which is a question the data can answer.

NCRB publishes police disposal for more categories than court disposal. Where a
category has no state-wise court table, the page says so rather than leaving a
blank chart.

Source: National Crime Records Bureau, Crime in India 2023, via data.gov.in.
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datagov  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "crime-india.json"

# (police disposal, court disposal or None) for each track the page offers.
TRACKS = {
    "ipc": {
        "label": "All IPC crime",
        "police": ("43d43e29-3a62-4b40-9b07-7716b2a87548",
                   "State/UT-wise Police Disposal of Indian Penal Code (IPC) Crime Cases during 2023"),
        "court": ("a050617c-9d8a-477f-b189-87e37b543b62",
                  "State/UT-wise Court Disposal of Indian Penal Code (IPC) Crime Cases during 2023"),
    },
    "women": {
        "label": "Crime against women",
        "police": ("a9fec274-b9f0-45fa-af87-48dfd6c377d5",
                   "State/UT-wise Police Disposal of Crime against Women during 2023"),
        "court": None,   # NCRB publishes no state-wise court table for this
    },
    "sc": {
        "label": "Atrocities against Scheduled Castes",
        "police": ("c989a134-78f8-46ec-a695-19c54d95db90",
                   "State/UT-wise Police Disposal of Crime/Atrocities against Scheduled Caste(s) during 2023"),
        "court": ("f4fbc445-056f-4826-80b5-da1cb782e49f",
                  "State/UT-wise Court Disposal of Crime/Atrocities against Scheduled Caste(s) during 2023"),
    },
    "st": {
        "label": "Atrocities against Scheduled Tribes",
        "police": ("c0acddde-9366-4efe-a0c9-2aa29d5c4ba9",
                   "State/UT-wise Police Disposal of Crime/Atrocities against Scheduled Tribe(s) during 2023"),
        "court": None,
    },
    "cyber": {
        "label": "Cyber crime",
        "police": ("9abd80f3-8269-40a5-93e8-26d7c5fdb006",
                   "State/UT-wise Police Disposal of Cyber Crime Cases during 2023"),
        "court": ("407d0480-2b94-42f3-aaab-4db42a0207f0",
                  "State/UT-wise Court Disposal of Cyber Crime Cases during 2023"),
    },
    "senior": {
        "label": "Crime against senior citizens",
        "police": ("1c4acfa1-f7ae-4e87-a71b-7c20eb8905d2",
                   "State/UT-wise Police Disposal of Crime against Senior Citizen during 2023"),
        "court": ("2659bbfb-4fdf-40e6-98c8-c9869d8e05c8",
                  "State/UT-wise Court Disposal of Crime against Senior Citizen during 2023"),
    },
}

POPULATION = ("cd3f9ecd-0bc3-406a-bb7d-8562ffb75083",
              "State/UT-wise Population, Decadal Growth Rate and Density, Census 2011")


def main():
    out = {
        "_source": ("National Crime Records Bureau, Crime in India 2023, and the Office of the "
                    "Registrar General of India, via data.gov.in (Open Government Data Platform)"),
        "_licence": "Government Open Data Licence - India",
        "_note": ("Case disposal by police and by courts, 2023. Snapshot -- refresh with "
                  "scripts/fetch-crime-data.py."),
        "_fetched": time.strftime("%Y-%m-%d"),
        "tracks": {},
        "series": {},
    }
    for name, t in TRACKS.items():
        entry = {"label": t["label"], "police": None, "court": None}
        for stage in ("police", "court"):
            if not t[stage]:
                continue
            rid, title = t[stage]
            print(f"  {name}/{stage}: {title[:66]}")
            rows = datagov.fetch_all(rid, quiet=True)
            print(f"    {len(rows)} rows")
            entry[stage] = {"resource_id": rid, "title": title, "rows": rows}
        out["tracks"][name] = entry

    rid, title = POPULATION
    print(f"  population: {title[:66]}")
    out["series"]["population"] = {
        "resource_id": rid, "title": title,
        "rows": datagov.fetch_all(rid, quiet=True)}

    OUT.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
