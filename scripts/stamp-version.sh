#!/usr/bin/env bash
#
# Deploy-time version stamping — run by Netlify's build command (see netlify.toml).
#
# Two things go stale between deploys, and this stamps BOTH so returning
# visitors reliably get the latest site:
#
#   1. version.json          — polled every 60s by js/auto-refresh.js; when the
#                              string changes the open page reloads itself.
#   2. service-worker.js     — its `const VERSION` names the runtime cache. The
#      VERSION                 SW purges every non-matching cache on `activate`,
#                              so rotating VERSION on each deploy forces the old
#                              stale-while-revalidate assets (JS/CSS) to be
#                              dropped. Without this, a reload alone keeps
#                              serving cached assets from the prior deploy.
#
# Both are stamped with the same deploy identifier: the immutable commit SHA
# when Netlify provides it ($COMMIT_REF), otherwise a UTC timestamp. This runs
# against Netlify's ephemeral build checkout, so it never commits back to git —
# the committed VERSION in the repo is just a sensible default for local/preview.
#
set -euo pipefail

TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Prefer the commit SHA (unique + immutable per deploy); fall back to a timestamp.
if [ -n "${COMMIT_REF:-}" ]; then
  STAMP="${COMMIT_REF:0:12}"
else
  STAMP="$(date -u +%Y%m%d%H%M%S)"
fi

# 1) version.json — drives the in-page auto-refresh notifier.
printf '{"v":"%s"}\n' "$TS" > version.json
echo "stamp-version: version.json -> $TS"

# 2) service-worker.js VERSION — rotates the runtime cache (auto cache-bust).
if [ -f service-worker.js ]; then
  if grep -q "const VERSION = '" service-worker.js; then
    sed -i "s/const VERSION = '[^']*';/const VERSION = 'v2-${STAMP}';/" service-worker.js
    echo "stamp-version: service-worker.js VERSION -> v2-${STAMP}"
  else
    echo "stamp-version: WARN — 'const VERSION' not found in service-worker.js; skipped" >&2
  fi
fi
