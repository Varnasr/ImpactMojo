#!/usr/bin/env python3
"""Snapshot the MCA CSR series from data.gov.in into data/csr-india.json.

Why a snapshot and not a live call: data.gov.in caps the shared public key at
10 records per request and rate-limits it hard, so a page calling the API at
render time would be slow, flaky, and dependent on a key we do not control.
Every other explorer on the site ships its data in the repo; this does the same.

Re-run to refresh. Set DATA_GOV_KEY to use your own key (free registration at
data.gov.in) instead of the shared demo key.

Sources, all Ministry of Corporate Affairs via data.gov.in:
  state  — State/UT-wise CSR Expenditure, 2018-19 to 2022-23
  sector — Development Sector-wise CSR Expenditure, 2018-19 to 2022-23
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "csr-india.json"
KEY = os.environ.get(
    "DATA_GOV_KEY",
    "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b",  # public demo key
)

RESOURCES = {
    "state": ("80f3abf8-7c91-4966-a37f-8c7b0aae92e9",
              "State/UT-wise Details of CSR Expenditure from 2018-19 to 2022-23"),
    "sector": ("40ca3289-b33c-4f60-b8fe-c5050d8e27fa",
               "Development Sector-wise Details of CSR Expenditure from 2018-19 to 2022-23"),
    # Denominator for the per-person view. Census 2011 is the most recent
    # enumerated population India has -- the 2021 census has not been held --
    # so per-person figures are CSR now over people counted then, and the page
    # says so rather than burying it.
    "population": ("cd3f9ecd-0bc3-406a-bb7d-8562ffb75083",
                   "State/UT-wise Population, Decadal Growth Rate and Density, Census 2011"),
    # The wealth axis. Per-capita NSDP covers 33 states and reaches 2022-23,
    # matching the CSR series; the per-capita GSDP table covers only 28.
    # Carries literal "NA" strings for unpublished cells -- not zero.
    "nsdp": ("c9bfd3c0-b9de-4a5b-8752-f72a4f2932ad",
             "State/UT-wise Per Capita Net State Domestic Product at Current Prices"),
}

PAGE = 10          # the shared key's hard cap
MAX_TRIES = 6


def get(url):
    """One request, with backoff on the rate limiter.

    Shells out to curl deliberately: this environment routes outbound HTTPS
    through an agent proxy that curl is configured for and urllib is not, so
    urllib times out where curl succeeds.
    """
    delay = 5
    for attempt in range(MAX_TRIES):
        try:
            out = subprocess.run(
                ["curl", "-s", "--max-time", "45", url],
                capture_output=True, text=True, check=True,
            ).stdout
            body = json.loads(out)
        except Exception:
            if attempt == MAX_TRIES - 1:
                raise
            time.sleep(delay)
            delay *= 2
            continue
        if isinstance(body, dict) and body.get("error"):
            if attempt == MAX_TRIES - 1:
                raise RuntimeError(body["error"])
            time.sleep(delay)
            delay *= 2
            continue
        return body
    raise RuntimeError("unreachable")


def fetch_all(rid):
    rows, offset, total = [], 0, None
    while True:
        url = (f"https://api.data.gov.in/resource/{rid}"
               f"?api-key={KEY}&format=json&limit={PAGE}&offset={offset}")
        body = get(url)
        total = body.get("total", 0)
        batch = body.get("records", [])
        rows.extend(batch)
        print(f"    {len(rows)}/{total}", flush=True)
        if not batch or len(rows) >= total:
            break
        offset += PAGE
        time.sleep(2)          # stay under the limiter
    if total is not None and len(rows) != total:
        raise RuntimeError(f"expected {total} rows, got {len(rows)}")
    return rows


def main():
    out = {
        "_source": "Ministry of Corporate Affairs, via data.gov.in (Open Government Data Platform)",
        "_licence": "Government Open Data Licence - India",
        "_note": ("CSR expenditure in rupees crore. Snapshot -- refresh with "
                  "scripts/fetch-csr-data.py. The 2021-22 and 2022-23 columns are the "
                  "most recent the MCA series publishes at State/UT level."),
        "_fetched": time.strftime("%Y-%m-%d"),
        "series": {},
    }
    for name, (rid, title) in RESOURCES.items():
        print(f"  {name}: {title}")
        rows = fetch_all(rid)
        out["series"][name] = {"resource_id": rid, "title": title, "rows": rows}

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nwrote {OUT.relative_to(ROOT)}")
    for k, v in out["series"].items():
        print(f"  {k:12s} {len(v['rows']):>4} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
