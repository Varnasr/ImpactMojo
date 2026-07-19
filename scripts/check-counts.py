#!/usr/bin/env python3
"""Content-count drift guard.

Canonical counts live in data/counts.json (single source of truth).
This script scans the user-facing files where counts have historically
drifted and fails if any "<number> <content type>" phrase disagrees with
the canonical value.

Workflow when adding content:
  1. Update the number in data/counts.json
  2. Run `python3 scripts/check-counts.py` — every stale occurrence is
     listed as file:line with the expected value
  3. Fix them, re-run until PASS

False-positive guards:
  - Lines containing an arrow (historical "15 → 28" changelog prose) are skipped
  - Lines containing "count-ignore" are skipped (inline opt-out)
  - "101 courses/Course" (the brand) never matches
  - Longer phrases match first ("flagship courses" before "courses"), and each
    line position is consumed once, so "51 foundational courses" is checked
    against foundational-courses, not courses

Exit 0 + "PASS" when clean; exit 1 with a drift listing otherwise.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COUNTS_FILE = ROOT / "data" / "counts.json"

# User-facing files where count drift has historically occurred.
# (docs/changelog.md and CHANGELOG.md are deliberately absent — historical.)
FILES = [
    "index.html",
    "catalog.html",
    "about.html",
    "404.html",
    "podcast.html",
    "transparency.html",
    "ImpactMojo_PressKit.html",
    "README.md",
    "docs/platform-overview.md",
    "docs/faq.md",
    "docs/content-catalog.md",
    "docs/games-guide.md",
    "docs/labs-guide.md",
    "js/tours.js",
]

# Ordered: longer/more specific phrases first. Each maps a phrase regex to a
# key in counts.json. Matching is case-insensitive.
TERMS = [
    (r"flagship\s+courses?", "flagship-courses"),
    (r"foundational\s+courses?", "foundational-courses"),
    (r"courses", "courses"),
    (r"interactive\s+simulations?", "game-simulations"),
    (r"simulations", "game-simulations"),
    (r"game\s+library", "games"),
    (r"games", "games"),
    (r"interactive\s+labs", "labs"),
    (r"labs", "labs"),
    (r"interactive\s+studios", "labs"),
    (r"studios", "labs"),
    (r"reading\s+companions", "reading-companions"),
    (r"deep\s+dives", "deep-dives"),
    (r"handouts", "handouts"),
    (r"timelines", "timelines"),
    (r"practice\s+packs", "practice-packs"),
    (r"live\s+case\s+challenges", "challenges"),
]

SKIP_LINE = re.compile(r"→|->|count-ignore")

# Homepage tile markup puts the number AFTER the label:
#   <span class="tp-n">Courses <span class="tp-cnt tp-mono">69</span></span>
TILE_TERMS = {
    "courses": "courses",
    "games": "games",
    "labs": "labs",
    "studios": "labs",
    "reading companions": "reading-companions",
    "deep dives": "deep-dives",
    "handouts": "handouts",
    "timelines": "timelines",
    "practice packs": "practice-packs",
}
TILE_RE = re.compile(
    r"(" + "|".join(re.escape(t) for t in TILE_TERMS) + r")\s*"
    r"<span class=\"tp-cnt[^\"]*\">(\d+)",
    re.IGNORECASE,
)


def build_pattern():
    alts = "|".join(f"(?P<t{i}>{rx})" for i, (rx, _) in enumerate(TERMS))
    # number not part of a larger number/word and not the end of a range
    # ("2–3 games"); phrase not followed by a letter ("35 labscape")
    return re.compile(rf"(?<![\d\w\-–—])(\d+)\+?\s+({alts})(?![a-z])", re.IGNORECASE)


def main():
    counts = {
        k: v for k, v in json.loads(COUNTS_FILE.read_text()).items()
        if not k.startswith("_")
    }
    pattern = build_pattern()
    failures = []
    scanned = 0

    for rel in FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        scanned += 1
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if SKIP_LINE.search(line):
                continue
            for m in pattern.finditer(line):
                number = int(m.group(1))
                if number == 101:  # "101 Courses" brand naming, never a count
                    continue
                term_idx = next(
                    i for i in range(len(TERMS)) if m.group(f"t{i}") is not None
                )
                key = TERMS[term_idx][1]
                expected = counts.get(key)
                if expected is not None and number != expected:
                    failures.append(
                        f"{rel}:{lineno}: found \"{m.group(0).strip()}\" "
                        f"but canonical {key} = {expected}"
                    )
            for m in TILE_RE.finditer(line):
                key = TILE_TERMS[m.group(1).lower()]
                number = int(m.group(2))
                expected = counts.get(key)
                if expected is not None and number != expected:
                    failures.append(
                        f"{rel}:{lineno}: tile \"{m.group(1)} … {number}\" "
                        f"but canonical {key} = {expected}"
                    )

    if failures:
        print(f"FAIL — {len(failures)} count drift(s) vs data/counts.json:\n")
        for f in failures:
            print(f"  {f}")
        print("\nFix the occurrences above (or update data/counts.json if the "
              "canonical value changed).")
        return 1

    print(f"PASS — counts consistent with data/counts.json across {scanned} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
