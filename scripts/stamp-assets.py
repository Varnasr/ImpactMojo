#!/usr/bin/env python3
"""Stamp local CSS/JS references with a content hash, so fresh HTML can never
pair with a stale cached asset.

Why this exists
---------------
service-worker.js serves HTML network-first and static assets
stale-while-revalidate. That is deliberate and good for offline, but it means
the first load after a deploy can pair *fresh* HTML with the *previous*
deploy's JS. On 2026-08-19 that shipped a Fundamentals page whose HTML had a
<svg id="cubeSvg"> and whose cached JS had no code to draw into it: an empty
box on the user's phone, with no error anywhere.

Appending ?v=<hash of the file> makes the URL change whenever the file does, so
new HTML always requests a URL that cannot already be in the cache.

Usage
-----
    python3 scripts/stamp-assets.py            # rewrite stamps in place
    python3 scripts/stamp-assets.py --check    # exit 1 if any stamp is stale
"""

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Every page that loads a shared /css/ or /js/ file. The stale-pairing risk is
# not specific to Fundamentals -- service-worker.js serves HTML network-first
# and assets stale-while-revalidate site-wide, so any page whose markup and
# script have to agree can pair fresh HTML with a previous deploy's JS. The
# Fundamentals cube is simply where it was noticed.
PAGE_GLOBS = [
    "*.html",
    "fundamentals/*.html",
    "Labs/*.html",
    "courses/*/index.html",
    "101-courses/*.html",
]
SKIP = {"PAGE-TEMPLATE.html"}
PAGES = sorted(
    p for g in PAGE_GLOBS for p in ROOT.glob(g) if p.name not in SKIP
)

REF = re.compile(r'(?P<attr>href|src)="(?P<path>/(?:css|js)/[A-Za-z0-9._-]+\.(?:css|js))(?:\?v=[0-9a-f]+)?"')


def digest(rel: str) -> str | None:
    f = ROOT / rel.lstrip("/")
    if not f.is_file():
        return None
    return hashlib.md5(f.read_bytes()).hexdigest()[:8]


def stamp(html: Path, check: bool):
    src = html.read_text(encoding="utf-8")

    def sub(m):
        h = digest(m.group("path"))
        if h is None:                      # not a local file we manage
            return m.group(0)
        return '%s="%s?v=%s"' % (m.group("attr"), m.group("path"), h)

    out = REF.sub(sub, src)
    if out == src:
        return True
    if check:
        return False
    html.write_text(out, encoding="utf-8")
    return True


def main():
    check = "--check" in sys.argv
    stale = [p for p in PAGES if not stamp(p, check)]
    if check and stale:
        print("FAIL - asset stamps are stale in:")
        for p in stale:
            print("   ", p.relative_to(ROOT))
        print("\nRun: python3 scripts/stamp-assets.py")
        return 1
    verb = "would update" if check else "stamped"
    print("PASS - asset stamps current across %d page(s)" % len(PAGES)
          if check else "%s %d page(s)" % (verb, len(PAGES)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
