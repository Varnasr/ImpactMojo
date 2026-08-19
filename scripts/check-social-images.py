#!/usr/bin/env python3
"""Guard: every og:image and twitter:image must point at a file that exists.

Why this exists
---------------
A social preview image is the one part of a page nobody on the team ever sees.
It renders on somebody else's timeline, in somebody else's app, and when the
file is missing the post simply shares without a picture. Nothing errors, no
test fails, and the page itself looks perfect.

Found by accident while building a blog post: the p-value post shipped that same
morning pointed at `assets/images/blog/p-values-and-confidence-intervals-og.png`,
which was never created. `ai-policy.html` pointed at `og-image.png`, where the
file is `og-card.png`. Both had been live and neither had a preview.

This is the same class as the 69 form handlers that reported success on a
rejected submission: a failure with no signal attached to it.

Note on URL-encoding: a path like `ImpactMojo%20Logo.png` is a real file with a
space in its name, not a broken link. A first pass at this check reported it as
missing, so the decode below is doing real work rather than being defensive.

Run: python3 scripts/check-social-images.py
"""

import glob
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.impactmojo.in"

META = re.compile(
    r'<meta\s+(?:property|name)="((?:og|twitter):image(?::secure_url)?)"\s+content="([^"]+)"',
    re.I,
)

SKIP_DIRS = ("Backups/", "node_modules/", "tests/")


def main() -> int:
    files = [f for f in glob.glob("**/*.html", recursive=True)
             if not f.startswith(SKIP_DIRS)]

    checked = 0
    missing = []

    for rel in sorted(files):
        try:
            src = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for prop, url in META.findall(src):
            # Only our own assets can be checked from here; a CDN or a remote
            # host is somebody else's problem and is left alone.
            if url.startswith("http") and not url.startswith(SITE):
                continue
            path = urlparse(url).path if url.startswith("http") else url
            # A space in a filename arrives as %20 and is a real file.
            path = unquote(path).lstrip("/")
            if not path:
                continue
            checked += 1
            if not (ROOT / path).exists():
                missing.append((rel, prop, path))

    if missing:
        print(f"FAIL - {len(missing)} social preview image(s) point at a file that does not exist.")
        print("       These pages share with no picture, and nothing else reports it.\n")
        for rel, prop, path in missing:
            print(f"    {rel}")
            print(f"        {prop} -> {path}")
        return 1

    print(f"PASS - all {checked} social preview images resolve to a real file "
          f"across {len(files)} pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
