#!/usr/bin/env python3
"""
Supabase anon-exposure guard.

Replaces the daily "Supabase health" Claude routine with something that lives in
the repo and runs in CI. It re-probes, with the *public* anon key, the exact
contract established by the 2026-08-03 remediation (PR #895):

  - the four tables that once had a blanket anon GRANT must stay anon-denied
  - the deliberately public reads must keep working, so an over-correction that
    breaks certificate verification or the public profile fields is caught too
  - the sensitive profile columns must stay denied

No secrets. The URL and anon key are read from js/config.js, which is the same
pair every browser already receives, so this file never duplicates them and can
never drift from what the site actually ships.

Exit 0 = contract holds. Exit 1 = a probe returned something other than the
contract (either a regression, or a change that needs this file updated).

Usage:  python3 scripts/check-supabase-anon.py [--verbose]
"""

import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

CONFIG = Path(__file__).resolve().parent.parent / "js" / "config.js"
TIMEOUT = 20
ATTEMPTS = 3

# (label, path, expected_status, why)
PROBES = [
    # Revoked from anon on 2026-08-03 — a 200 here is a real exposure.
    ("push_subscriptions",    "push_subscriptions?select=*&limit=1",    401,
     "revoked from anon in 20260803_revoke_anon_grants_flagged_tables.sql"),
    ("challenge_submissions", "challenge_submissions?select=*&limit=1", 401,
     "revoked from anon in 20260803_revoke_anon_grants_flagged_tables.sql"),
    ("organizations",         "organizations?select=*&limit=1",         401,
     "revoked from anon in 20260803_revoke_anon_grants_flagged_tables.sql"),
    ("organization_members",  "organization_members?select=*&limit=1",  401,
     "revoked from anon in 20260803_revoke_anon_grants_flagged_tables.sql"),

    # Sensitive columns must stay denied even though the table is readable.
    ("profiles(phone,address,email,bio)",
     "profiles?select=phone,address,email,bio&limit=1", 401,
     "profiles is column-limited for anon; these columns are not granted"),

    # Intentionally public — a 401 here means we broke a live feature.
    ("certificates(select=*)", "certificates?select=*&limit=1", 200,
     "public certificate verification depends on this staying readable"),
    ("profiles(id,full_name,display_name)",
     "profiles?select=id,full_name,display_name&limit=1", 200,
     "the granted anon columns power public profile display"),
]


def read_config():
    """Pull the URL + anon key out of js/config.js."""
    try:
        src = CONFIG.read_text(encoding="utf-8")
    except OSError as exc:
        sys.exit(f"FAIL — cannot read {CONFIG}: {exc}")
    url = re.search(r"SUPABASE_URL:\s*'([^']+)'", src)
    key = re.search(r"SUPABASE_ANON_KEY:\s*'([^']+)'", src)
    if not url or not key:
        sys.exit(f"FAIL — could not find SUPABASE_URL / SUPABASE_ANON_KEY in {CONFIG}")
    return url.group(1).rstrip("/"), key.group(1)


def probe(base, key, path):
    """Return the HTTP status, retrying so a blip is not reported as a breach."""
    req = urllib.request.Request(
        f"{base}/rest/v1/{path}",
        headers={"apikey": key, "Authorization": f"Bearer {key}"},
    )
    last = None
    for attempt in range(ATTEMPTS):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return resp.status
        except urllib.error.HTTPError as exc:
            return exc.code  # a status is an answer, not a failure
        except Exception as exc:  # noqa: BLE001 — network flake, retry
            last = exc
            if attempt < ATTEMPTS - 1:
                time.sleep(2 * (attempt + 1))
    return f"unreachable ({last})"


def main():
    verbose = "--verbose" in sys.argv
    base, key = read_config()
    print(f"Supabase anon-exposure guard — {base}")
    print(f"Probes: {len(PROBES)} (public anon key, no secrets)\n")

    failures = []
    for label, path, expected, why in PROBES:
        got = probe(base, key, path)
        ok = got == expected
        print(f"  {'ok  ' if ok else 'FAIL'}  {label:<40} expected {expected}, got {got}")
        if verbose and ok:
            print(f"          ({why})")
        if not ok:
            failures.append((label, expected, got, why))

    print()
    if failures:
        print(f"FAIL — {len(failures)} probe(s) did not match the expected contract:\n")
        for label, expected, got, why in failures:
            print(f"  {label}")
            print(f"    expected {expected}, got {got}")
            print(f"    {why}")
            if expected == 401 and got == 200:
                print("    >> anon can now read this table. Check for a re-added GRANT or a")
                print("       policy scoped to {public} instead of {authenticated}.")
            elif expected == 200 and got == 401:
                print("    >> a public read broke. This is a live feature regression, not a leak.")
            print()
        print("If a change here was deliberate, update PROBES in this file to match.")
        return 1

    print("PASS — anon exposure matches the expected contract.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
