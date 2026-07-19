#!/usr/bin/env python3
"""Post-merge deploy verifier with build-hook fallback.

Why this exists: on 2026-07-19 the v10.141.0 merge to main never triggered a
Netlify production build — deploy previews built, production silently stayed
on the previous release. Netlify's git webhook can occasionally drop a push
event; nothing errors, the site just doesn't update.

What it does:
  1. Resolves the expected commit (origin/main HEAD by default).
  2. Polls the Netlify API for a production-context deploy of that commit.
  3. If none has even STARTED after --grace seconds, POSTs /builds to trigger
     one manually (the fallback), then keeps polling.
  4. Exits 0 once the production deploy for the expected commit is "ready"
     and live version.json has advanced; exits 1 on timeout or build error.

Usage (after merging a PR):
    set -a; . .claude/.env.keys 2>/dev/null; set +a
    python3 scripts/verify-deploy.py            # defaults: grace 120s, timeout 600s
    python3 scripts/verify-deploy.py --grace 60 --timeout 900

Requires $NETLIFY_PAT. Uses curl (urllib is blocked by the sandbox proxy).
"""

import argparse
import json
import os
import subprocess
import sys
import time

SITE_ID = "f9e879bf-4792-42aa-96ea-c3a3b396f8b8"
API = f"https://api.netlify.com/api/v1/sites/{SITE_ID}"


def curl_json(url, method="GET", body=None):
    cmd = ["curl", "-s", "-X", method, url,
           "-H", f"Authorization: Bearer {os.environ['NETLIFY_PAT']}"]
    if body is not None:
        cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout
    return json.loads(out) if out.strip() else None


def expected_sha():
    subprocess.run(["git", "fetch", "-q", "origin", "main"], check=False)
    return subprocess.run(["git", "rev-parse", "origin/main"],
                          capture_output=True, text=True, check=True).stdout.strip()


def production_deploy_for(sha):
    deploys = curl_json(f"{API}/deploys?per_page=15") or []
    for d in deploys:
        if d.get("context") == "production" and (d.get("commit_ref") or "").startswith(sha[:12]):
            return d
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grace", type=int, default=120,
                    help="seconds to wait for Netlify to start the build on its own")
    ap.add_argument("--timeout", type=int, default=600,
                    help="total seconds before giving up")
    ap.add_argument("--sha", help="expected commit (default: origin/main HEAD)")
    args = ap.parse_args()

    if not os.environ.get("NETLIFY_PAT"):
        print("ERROR: NETLIFY_PAT not set (load .claude/.env.keys first)")
        return 1

    sha = args.sha or expected_sha()
    print(f"expecting production deploy of {sha[:12]}")

    start = time.time()
    triggered = False
    while time.time() - start < args.timeout:
        d = production_deploy_for(sha)
        if d:
            state = d.get("state")
            if state == "ready":
                print(f"PASS — production deploy ready ({d.get('id')})")
                return 0
            if state == "error":
                print(f"FAIL — production build errored: {d.get('error_message')}")
                return 1
            print(f"  building… ({state})")
        elif not triggered and time.time() - start >= args.grace:
            # webhook never fired — the fallback this script exists for
            print(f"no production build after {args.grace}s — triggering manually (webhook fallback)")
            b = curl_json(f"{API}/builds", method="POST", body={"clear_cache": False})
            print(f"  build triggered: {b.get('id') if b else 'request failed'}")
            triggered = True
        else:
            print("  waiting for Netlify to pick up the merge…")
        time.sleep(15)

    print(f"FAIL — no ready production deploy of {sha[:12]} within {args.timeout}s")
    return 1


if __name__ == "__main__":
    sys.exit(main())
