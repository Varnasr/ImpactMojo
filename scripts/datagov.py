#!/usr/bin/env python3
"""Shared client for the data.gov.in Open Government Data API.

Every explorer built on data.gov.in ships a snapshot in the repo rather than
calling the API at render time: the API is rate-limited, needs a key we would
have to put in the page, and would make each explorer fail in a way the
visitor cannot act on. This module is the one place that talks to it.

Set DATA_GOV_KEY to your own key (free registration at data.gov.in). Without
one it falls back to the shared public demo key, which is capped at 10 records
a request -- fine for a small table, unusable for anything district-level.
"""
import json
import os
import subprocess
import time

DEMO_KEY = "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b"
BASE = "https://api.data.gov.in/resource/"


def key():
    return os.environ.get("DATA_GOV_KEY", DEMO_KEY)


def page_size():
    """The demo key rejects anything above 10; a registered key allows 1000."""
    return 10 if key() == DEMO_KEY else 1000


def get(url, tries=6):
    """One request, with backoff on the rate limiter.

    Shells out to curl deliberately: this environment routes outbound HTTPS
    through an agent proxy that curl is configured for and urllib is not, so
    urllib times out where curl succeeds.
    """
    delay = 5
    for attempt in range(tries):
        try:
            out = subprocess.run(
                ["curl", "-s", "--max-time", "90", url],
                capture_output=True, text=True, check=True,
            ).stdout
            body = json.loads(out)
        except Exception:
            if attempt == tries - 1:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 60)
            continue
        if isinstance(body, dict) and body.get("error"):
            if attempt == tries - 1:
                raise RuntimeError(body["error"])
            time.sleep(delay)
            delay = min(delay * 2, 60)
            continue
        return body
    raise RuntimeError("unreachable")


def fetch_all(resource_id, quiet=False, pause=0.6):
    """Every row of a resource, paged.

    Refuses to return a short read. A truncated fetch is the failure that does
    not look like one: the file is valid JSON, the page renders, and a tenth of
    India is quietly missing from it.
    """
    per, rows, offset, total = page_size(), [], 0, None
    while True:
        body = get(f"{BASE}{resource_id}?api-key={key()}&format=json"
                   f"&limit={per}&offset={offset}")
        total = body.get("total", 0)
        batch = body.get("records", [])
        rows.extend(batch)
        if not quiet:
            print(f"    {len(rows):,}/{total:,}", flush=True)
        if not batch or len(rows) >= total:
            break
        offset += per
        time.sleep(pause)
    if total is not None and len(rows) != total:
        raise RuntimeError(
            f"{resource_id}: expected {total:,} rows, got {len(rows):,}")
    return rows


def describe(resource_id):
    body = get(f"{BASE}{resource_id}?api-key={key()}&format=json&limit=1")
    return {"total": body.get("total"), "title": body.get("title"),
            "fields": list((body.get("records") or [{}])[0].keys())}
