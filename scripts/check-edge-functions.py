#!/usr/bin/env python3
"""Every deployed Edge Function still boots and runs its own code.

The six functions import `@supabase/supabase-js` from esm.sh at cold start. If
that import breaks -- a bad version pin, an esm.sh outage, a dependency the new
version needs and Deno cannot resolve -- the function does not fail at deploy
time. It fails on the first request after the next cold start, as a 500, and
only the caller sees it.

The probes below are chosen so that a **successful** run proves the function
body executed: each expected response is text the function itself writes, not
something the platform gateway produces. `POST {}` with no auth to a
`verify_jwt: true` function is answered by the gateway before the code runs, so
those three are probed with the public anon key instead -- a valid JWT that
gets past the gateway and lands in the function, which then rejects it in its
own words.

`status-alert` is the control: it imports no supabase-js, so it must keep
answering whatever the others do.

No secrets: the URL and anon key come from js/config.js, the same pair every
browser already receives.
"""
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "js" / "config.js"
TIMEOUT = 25
RETRIES = 3

# slug -> (use_anon_jwt, expected_status, snippet the function itself writes)
PROBES = {
    "serve-course-content": (True, 400, "Missing course_id"),
    "issue-certificate": (True, 401, "Invalid session"),
    "send-notification": (True, 401, "Invalid session"),
    "mint-resource-token": (False, 401, "Missing or malformed Authorization header"),
    "send-push": (False, 401, "Missing Authorization"),
    "status-alert": (False, 401, "unauthorized"),
}


def read_config():
    text = CONFIG.read_text(encoding="utf-8")
    url = re.search(r"https://[a-z0-9]+\.supabase\.co", text)
    key = re.search(r"eyJ[A-Za-z0-9_.-]{40,}", text)
    if not url or not key:
        print(f"FAIL - could not read the Supabase URL/anon key from {CONFIG}")
        sys.exit(1)
    return url.group(0), key.group(0)


def probe(base, anon, slug, use_jwt):
    req = urllib.request.Request(
        f"{base}/functions/v1/{slug}",
        data=b"{}",
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    if use_jwt:
        req.add_header("Authorization", f"Bearer {anon}")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def main():
    base, anon = read_config()
    failures = []

    for slug, (use_jwt, want_status, want_text) in PROBES.items():
        status = body = None
        for attempt in range(RETRIES):
            try:
                status, body = probe(base, anon, slug, use_jwt)
                break
            except Exception as e:  # transient network/DNS blip
                if attempt == RETRIES - 1:
                    failures.append((slug, f"unreachable after {RETRIES} tries: {e}"))
                    status = None
                else:
                    time.sleep(2 * (attempt + 1))

        if status is None:
            continue
        if status != want_status or want_text not in body:
            failures.append((
                slug,
                f"expected {want_status} containing {want_text!r}, "
                f"got {status} {body[:120]!r}",
            ))

    if failures:
        print(f"FAIL - {len(failures)} of {len(PROBES)} Edge Functions did not answer as expected:")
        for slug, why in failures:
            print(f"    {slug}: {why}")
        print("\nA 500 here usually means the esm.sh import failed at cold start.")
        print("Check the pinned @supabase/supabase-js version in supabase/functions/<slug>/index.ts.")
        return 1

    print(f"PASS - all {len(PROBES)} Edge Functions boot and answer in their own words.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
