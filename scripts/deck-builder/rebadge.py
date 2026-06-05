#!/usr/bin/env python3
"""
Re-badge a 101-courses card from Gamma "Slide Deck" to native, and recompute the
hero-stat and filter counts from the actual badges present in index.html.

Usage:  python3 scripts/deck-builder/rebadge.py <slug> [<slug> ...]
Idempotent: a card already native is left as-is; counts are always recomputed.
"""
import re
import sys
from pathlib import Path

INDEX = Path(__file__).resolve().parents[2] / "101-courses" / "index.html"
DECK_BADGE = '<span class="card-badge card-badge-deck">Slide Deck</span>'
NATIVE_BADGE = '<span class="card-badge card-badge-native">Native HTML &middot; 100 slides</span>'


def rebadge_one(s, slug):
    anchor = f'<a class="course-card" href="/101-courses/{slug}.html">'
    i = s.find(anchor)
    if i == -1:
        print(f"  [skip] card not found: {slug}")
        return s
    j = s.find(DECK_BADGE, i)
    if j != -1 and j < i + 400:
        return s[:j] + NATIVE_BADGE + s[j + len(DECK_BADGE):]
    if s.find('card-badge-native', i) != -1 and s.find('card-badge-native', i) < i + 400:
        print(f"  [ok] already native: {slug}")
    else:
        print(f"  [warn] no deck badge near card: {slug}")
    return s


def recompute_counts(s):
    # Count only the badge spans on actual cards (class="card-badge card-badge-*"),
    # NOT the CSS rule and JS classify() occurrences of the bare class name.
    native = s.count('class="card-badge card-badge-native"')
    deck = s.count('class="card-badge card-badge-deck"')
    coming = s.count('class="card-badge card-badge-coming"')
    total = native + deck + coming
    s = re.sub(r'(<div class="hero-stat-num">)\d+(</div>\s*<div class="hero-stat-lbl">Native HTML Decks</div>)',
               rf'\g<1>{native}\g<2>', s)
    s = re.sub(r'(<div class="hero-stat-num">)\d+(</div>\s*<div class="hero-stat-lbl">Slide Deck Courses</div>)',
               rf'\g<1>{deck}\g<2>', s)
    s = re.sub(r'(data-filter="native">Native HTML \()\d+(\)</button>)', rf'\g<1>{native}\g<2>', s)
    s = re.sub(r'(data-filter="deck">Slide Deck \()\d+(\)</button>)', rf'\g<1>{deck}\g<2>', s)
    return s, native, deck, coming, total


def main():
    s = INDEX.read_text(encoding="utf-8")
    for slug in sys.argv[1:]:
        s = rebadge_one(s, slug)
        print(f"  rebadged {slug}")
    s, native, deck, coming, total = recompute_counts(s)
    INDEX.write_text(s, encoding="utf-8")
    print(f"counts -> Native {native} / Slide Deck {deck} / Coming {coming} = {total}")


if __name__ == "__main__":
    main()
