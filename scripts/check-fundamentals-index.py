#!/usr/bin/env python3
"""Guard: the Fundamentals landing page must count and link what actually ships.

Why this exists
---------------
The landing page said "Four so far" while listing five cards, for as long as the
fifth framework had been live. Nothing caught it: the number is prose on a page
under fundamentals/, and check-counts.py deliberately scans only root-level
pages for platform totals. It was found by a person reading the page.

That is the class of bug worth a guard — a number stated in one place and the
thing it counts maintained in another. This checks three of them:

  * the "N so far" heading matches the number of framework cards listed
  * every fundamentals/*.html page except the index is linked from the index
  * every card links to a file that exists

Run: python3 scripts/check-fundamentals-index.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "fundamentals" / "index.html"

WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
         "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}


def main() -> int:
    if not INDEX.exists():
        print(f"FAIL - {INDEX} is missing.")
        return 1
    src = INDEX.read_text(encoding="utf-8")
    problems = []

    cards = re.findall(r'<div class="credit-card">\s*<h3><a href="(/fundamentals/[^"]+)"', src)
    n_cards = len(cards)

    m = re.search(r"<h2>\s*(\w+)\s+so far\s*</h2>", src, re.I)
    if not m:
        problems.append('no "<N> so far" heading found — has the section been renamed?')
    else:
        word = m.group(1).lower()
        stated = WORDS.get(word, int(word) if word.isdigit() else None)
        if stated is None:
            problems.append(f'heading count "{m.group(1)}" is not a number this check knows')
        elif stated != n_cards:
            problems.append(f'the heading says "{m.group(1)}" ({stated}) '
                            f"but {n_cards} framework cards are listed")

    for href in cards:
        if not (ROOT / href.lstrip("/")).exists():
            problems.append(f"card links to {href}, which does not exist")

    shipped = sorted(p.name for p in (ROOT / "fundamentals").glob("*.html")
                     if p.name != "index.html")
    linked = {Path(h).name for h in cards}
    for name in shipped:
        if name not in linked:
            problems.append(f"fundamentals/{name} ships but the index does not link it")

    if problems:
        print("FAIL - the Fundamentals index does not describe what ships.\n")
        for p in problems:
            print(f"    {p}")
        return 1

    print(f"PASS - the Fundamentals index counts, links and resolves all "
          f"{n_cards} frameworks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
