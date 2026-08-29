#!/usr/bin/env python3
"""Snapshot the CPCB station-level air quality readings into data/aqi-india.json.

This is the one live series among the explorers: the CPCB publishes a fresh
reading for every station every hour. The page still ships a snapshot rather
than calling the API in the browser, for the same reasons as the others -- the
key would have to be in the page, the API is rate-limited, and a visitor
cannot act on a failed fetch. The trade is that the readings age, so the page
states the reading time at the top rather than implying it is current.

Re-run to refresh. Roughly 3,500 rows, so a few seconds on a registered key.

Sources, via data.gov.in:
  Central Pollution Control Board, real-time station readings
  Census 2011 population, as the denominator for network coverage
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import datagov  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "aqi-india.json"

RESOURCES = {
    "readings": ("3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69",
                 "Real time Air Quality Index from various locations (CPCB)"),
    # How many people each monitoring station covers is a fact about the
    # network, not about the air, and it is the part that varies most.
    "population": ("cd3f9ecd-0bc3-406a-bb7d-8562ffb75083",
                   "State/UT-wise Population, Decadal Growth Rate and Density, Census 2011"),
}


def main():
    out = {
        "_source": ("Central Pollution Control Board and the Office of the Registrar General "
                    "of India, via data.gov.in (Open Government Data Platform)"),
        "_licence": "Government Open Data Licence - India",
        "_note": ("Station readings are hourly and this file is a snapshot of one hour. "
                  "Refresh with scripts/fetch-aqi-data.py."),
        "_fetched": time.strftime("%Y-%m-%d %H:%M"),
        "series": {},
    }
    for name, (rid, title) in RESOURCES.items():
        print(f"  {name}: {title[:70]}")
        rows = datagov.fetch_all(rid, quiet=True)
        print(f"    {len(rows):,} rows")
        out["series"][name] = {"resource_id": rid, "title": title, "rows": rows}

    OUT.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
