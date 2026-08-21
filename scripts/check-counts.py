#!/usr/bin/env python3
"""Content-count drift guard — sitewide.

Canonical counts live in data/counts.json (single source of truth). This
script scans every CURRENT-CLAIM, user-facing surface and fails if any
"<number> <content type>" phrase disagrees with the canonical value.

Coverage (the point of the 2026-08 rewrite — no more per-file exceptions
for the live site):
  * ALL root-level *.html — the website's landing / marketing / legal /
    premium pages — are scanned automatically. New pages are covered the
    moment they're added; nobody has to remember to add them here.
  * The present-tense GitBook overview docs + README.
  * The Dataverse total is now tracked (key "dataverse") in all its prose
    and tile phrasings.

Deliberately EXCLUDED (their numbers are legitimately NOT the platform
totals — enforcing "current" here would corrupt real content):
  * Historical prose — changelogs, roadmaps, the blog, updates.html, the
    website-todo / flagship-specification working docs.
  * Per-item / contextual pages — course pages (courses/, 101-courses/),
    the practice tools (premium-tools/), book summaries, the Labs index,
    supabase e-mail templates.
  * Dynamic dashboards — org-dashboard.html (per-organisation learning-path
    sizes) and game-library.html (a "0 of 0 games" JS placeholder).
  * Translated docs (docs/bn|hi|mr|ta/…) — kept in sync manually.
  A line can also opt out inline with the token "count-ignore", and any
  line containing an arrow (→ / ->) is treated as historical prose.

The GitHub Wiki is a separate repository, so it is covered by the same
guard through --wiki: point it at a wiki clone and it scans that clone's
*.md the same way, minus Changelog.md and Roadmap.md (mirrors of the
repo's historical prose, excluded here for the same reason they are
excluded above). Before this existed, .github/workflows/sync-wiki.yml
refreshed exactly two hardcoded phrases on three of the eleven wiki
pages, so every other count on the wiki drifted silently: on 2026-08-19
the Book-Summaries and Premium pages were still claiming 163 reading
companions, 34 labs, 22 deep dives and 89 handouts.

Usage:
  python3 scripts/check-counts.py           # report drift, exit 1 if any
  python3 scripts/check-counts.py --fix     # rewrite drift to canonical
  python3 scripts/check-counts.py --wiki DIR [--fix]   # scan a wiki clone

Workflow when adding content:
  1. Update the number in data/counts.json
  2. Run with --fix (or fix by hand from the report)
  3. Re-run until PASS

Exit 0 + "PASS" when clean; exit 1 with a drift listing otherwise.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COUNTS_FILE = ROOT / "data" / "counts.json"

# Root-level HTML pages that are NOT current-claim platform surfaces.
EXCLUDE_HTML = {
    "updates.html",          # dated "what's new" cards — historical
    "PAGE-TEMPLATE.html",    # page skeleton
    "org-dashboard.html",    # per-organisation learning-path counts (dynamic)
    "game-library.html",     # "0 of 0 games" progress placeholder (JS)
    # Its <span class="cnt"> tallies count the links in each section of the
    # sitemap, not the platform totals -- "Games 18" is 18 listed links, not the
    # 135-game library. Verified: every section tally matches the links beneath
    # it. (That check also showed the sitemap is missing entries -- 17 of 19
    # flagship courses, 31 of 35 labs, 21 of 22 deep dives -- which is a content
    # gap to fix in the page, not a count to rewrite.)
    "sitemap.html",
}

# Present-tense docs that DO make current platform claims (changelogs,
# roadmaps, specs and translated docs are intentionally absent).
DOC_FILES = [
    "README.md",
    "docs/platform-overview.md",
    "docs/content-catalog.md",
    "docs/faq.md",
    "docs/games-guide.md",
    "docs/labs-guide.md",
    "docs/premium.md",
    "docs/welcome.md",
    "docs/why-impactmojo.md",
    "docs/getting-started.md",
    "docs/mcp-server-guide.md",
    "docs/mojini-guide.md",
    "docs/learning-design.md",
    "docs/terms-guide.md",
    "docs/team.md",
    "docs/transparency-and-commitments.md",
    "docs/freemium-and-premium-guide.md",
    "docs/teaching-and-lms-guide.md",
    "docs/101-decks-guide.md",
]

# Wiki pages that mirror historical prose from the repo, so their numbers are
# records of what was true then — the same exclusion the changelog and roadmap
# get above.
EXCLUDE_WIKI = {"Changelog.md", "Roadmap.md"}

# Non-HTML files whose *user-facing copy* quotes platform totals. The guard
# scanned only root-level HTML, so the homepage tour drifted unnoticed: it
# offered "34 studios", "163 reading companions" and "22 deep dives" while the
# canonical figures had moved to 35, 166 and 23. Copy is copy wherever it lives.
COPY_FILES = [
    "js/tours.js",
    # The 101 series landing page. Not root-level, so the HTML glob never saw
    # it, and its <title>, og:title and <h1> each carried a stale foundational
    # count -- the one page whose entire subject is that number.
    "101-courses/index.html",
]


def scanned_files(wiki_dir=None):
    if wiki_dir is not None:
        return sorted(
            p.name for p in wiki_dir.glob("*.md") if p.name not in EXCLUDE_WIKI
        )
    html = sorted(
        p.name for p in ROOT.glob("*.html") if p.name not in EXCLUDE_HTML
    )
    return html + [d for d in DOC_FILES if (ROOT / d).exists()] + [
        f for f in COPY_FILES if (ROOT / f).exists()
    ]


# Ordered: longer / more specific phrases first. Each maps a phrase regex to a
# key in counts.json. Matching is case-insensitive. The number precedes the
# phrase ("324 datasets").
TERMS = [
    (r"data\s+explorers?", "data-explorers"),
    (r"flagship\s+courses?", "flagship-courses"),
    (r"foundational\s+courses?", "foundational-courses"),
    # The site rarely writes the full phrase. "19 flagship + 51 foundational",
    # "51 foundational slide decks", "51 foundational primers", "51 foundational
    # 101 decks" and "51 Foundational Courses for South Asian Practitioners" all
    # appeared on live pages while `foundational courses` alone reported PASS --
    # so 52 in counts.json sat beside "71 courses (19 flagship + 51
    # foundational)" on the homepage, catalogue, FAQ, premium and teach pages,
    # a total that does not even add up. Match the bare word.
    (r"foundational\b", "foundational-courses"),
    (r"flagship\b", "flagship-courses"),
    (r"courses", "courses"),
    (r"interactive\s+simulations?", "game-simulations"),
    (r"simulations", "game-simulations"),
    (r"game\s+library", "games"),
    (r"games", "games"),
    (r"browser-based\s+labs", "labs"),
    (r"interactive\s+labs", "labs"),
    (r"labs", "labs"),
    (r"interactive\s+studios", "labs"),
    (r"studios", "labs"),
    (r"reading\s+companions", "reading-companions"),
    # The site's other name for the same library. Only reachable on
    # current-claim surfaces: every "<n> BookSummaries" in the repo sits
    # in a changelog or a translated doc, both already excluded.
    (r"booksummaries", "reading-companions"),
    (r"deep\s+dives", "deep-dives"),
    (r"law\s+guides", "law-guides"),
    (r"handouts", "handouts"),
    (r"timelines", "timelines"),
    (r"practice\s+packs", "practice-packs"),
    (r"live\s+case\s+challenges", "challenges"),
    # Dataverse total — its varied prose forms ("324 datasets", "324 curated
    # data tools", "324 Dataverse Tools", "324 tools, datasets, APIs …").
    (r"curated\s+data\s+tools", "dataverse"),
    (r"data\s+tools", "dataverse"),
    (r"datasets", "dataverse"),
    (r"dataverse\s+tools", "dataverse"),
    # README described the library as "296 curated tools" -- no "data", so
    # the `curated data tools` pattern never saw it, and the number sat 32
    # behind canonical.
    (r"curated\s+tools", "dataverse"),
    (r"tools,\s*datasets", "dataverse"),
]

# Dataverse phrasings where the number is NOT directly before a noun phrase.
# Each captures the number as group 1 and maps to "dataverse".
SPECIAL = [
    # explorers.html states the platform total as "<b>12</b> explorers"; the
    # per-group tallies on the same page ("4 explorers" in one theme group) are
    # legitimately smaller, so this is anchored to the <b> wrapper.
    (re.compile(r"<b>(\d+)</b>\s*(?:data\s+)?explorers?\b", re.I), "data-explorers"),
    (re.compile(r"Dataverse\s*\(\s*(\d+)\+?\s+(?:sources?|datasets?|data\s+tools?|tools?)", re.I), "dataverse"),
    (re.compile(r"(\d+)\+?[-\s]source\s+Dataverse", re.I), "dataverse"),
    (re.compile(r"Dataverse\s+Tools['\"]?\s*:\s*(\d+)", re.I), "dataverse"),
]

# Stat tiles put the number in one element and a label in the next, in varied
# markup and with adjective-prefixed labels:
#   <b>34</b><span>Interactive Labs</span>
#   <div class="stat-value">70</div><div class="stat-label">Free courses</div>
# Match the number + the following short label text, then resolve the label to
# a counts.json key by the content keyword it contains (longest first).
# Label keyword -> counts.json key, longest/most-specific first. Matched on
# WORD BOUNDARIES so "Discourses" never matches "courses" and "Premium tools"
# never matches (bare "tools" is intentionally not a key).
LABEL_KEYS = [
    ("data explorers", "data-explorers"),
    ("reading companions", "reading-companions"),
    ("book companions", "reading-companions"),
    ("live case challenges", "challenges"),
    ("flagship courses", "flagship-courses"),
    ("foundational courses", "foundational-courses"),
    ("interactive studios", "labs"),
    ("interactive labs", "labs"),
    ("game library", "games"),
    ("practice packs", "practice-packs"),
    ("deep dives", "deep-dives"),
    ("dataverse tools", "dataverse"),
    ("data tools", "dataverse"),
    ("law guides", "law-guides"),
    ("foundational", "foundational-courses"),
    ("explorers", "data-explorers"),
    ("simulations", "game-simulations"),
    ("datasets", "dataverse"),
    ("challenges", "challenges"),
    ("studios", "labs"),
    ("courses", "courses"),
    ("games", "games"),
    ("labs", "labs"),
    ("handouts", "handouts"),
    ("timelines", "timelines"),
]
LABEL_KEY_RES = [(re.compile(rf"\b{re.escape(kw)}\b", re.I), key) for kw, key in LABEL_KEYS]

# Stat/number tiles in any markup: a number that is the WHOLE content of its
# element, immediately followed by a label element. The leading ">" anchor
# means "WEEK 3</span><span>Games…" (number not alone) is NOT a match.
TILE_LABEL_RES = [
    re.compile(r">\s*(\d+)\+?\s*</[^>]+>\s*<[^>]+>\s*([A-Za-z][^<]{1,44})"),
]

# The same tile, written the other way round: the label element first and the
# number second. libraries.html does this
#   <span class="lib-n">Reading Companions</span><span class="lib-c">149</span>
# and it drifted to 149/89/321 against a canonical 163/90/328 without the guard
# noticing, because the only label-first rule here was hardcoded to the
# homepage's own "tp-cnt" class. Matching on shape rather than class name means
# a new page's markup is covered the day it lands. Safe against false positives
# because the label still has to resolve to a known key via label_to_key().
TILE_LABEL_FIRST_RES = [
    re.compile(r">\s*([A-Za-z][^<]{1,44}?)\s*</[^>]+>\s*<[^>]+>\s*(\d+)\+?\s*<"),
]


def label_to_key(text):
    for rx, key in LABEL_KEY_RES:
        if rx.search(text):
            return key
    return None

# A whole line opts out with the explicit token "count-ignore".
SKIP_LINE = re.compile(r"count-ignore")
# An arrow marks a historical range ("15 → 28 games") — but only when it sits
# right next to the number. A decorative arrow elsewhere on the line (e.g.
# "All free → impactmojo.in") must NOT suppress a real count claim, so this is
# checked per match against a small window around the number, not per line.
ARROW = re.compile(r"→|->")


def in_range(line, start, end):
    return bool(ARROW.search(line[max(0, start - 6):end + 6]))

# Homepage tile markup puts the number AFTER the label:
#   <span class="tp-n">Courses <span class="tp-cnt tp-mono">70</span></span>
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


def line_hits(line, pattern, counts):
    """Yield (num_start, num_end, key, found_number, expected) for a line."""
    for m in pattern.finditer(line):
        number = int(m.group(1))
        if number == 101:  # "101 Courses" brand naming, never a count
            continue
        term_idx = next(i for i in range(len(TERMS)) if m.group(f"t{i}") is not None)
        key = TERMS[term_idx][1]
        expected = counts.get(key)
        if expected is None:
            continue
        # A year is not a count: "the Q3 2026 BookSummaries expansion" read as
        # 2026 reading companions, and --fix would have written "Q3 166
        # BookSummaries" into the wiki. Only suppressed when the canonical
        # value is not itself year-shaped, so a library that really does reach
        # 1,900 items is still checked.
        if 1900 <= number <= 2099 and expected < 1000:
            continue
        yield (m.start(1), m.end(1), key, number, expected)
    for rx, key in SPECIAL:
        for m in rx.finditer(line):
            number = int(m.group(1))
            expected = counts.get(key)
            if expected is not None:
                yield (m.start(1), m.end(1), key, number, expected)
    for m in TILE_RE.finditer(line):
        key = TILE_TERMS[m.group(1).lower()]
        expected = counts.get(key)
        if expected is not None:
            yield (m.start(2), m.end(2), key, int(m.group(2)), expected)
    for rx in TILE_LABEL_FIRST_RES:
        for m in rx.finditer(line):
            key = label_to_key(m.group(1))
            if key is None:
                continue
            expected = counts.get(key)
            if expected is not None:
                yield (m.start(2), m.end(2), key, int(m.group(2)), expected)
    for rx in TILE_LABEL_RES:
        for m in rx.finditer(line):
            key = label_to_key(m.group(2))
            if key is None:
                continue
            expected = counts.get(key)
            if expected is not None:
                yield (m.start(1), m.end(1), key, int(m.group(1)), expected)


# Tiles split across lines. `line_hits` scans one line at a time, so a tile
# written as
#     <div class="stat-number">70</div>
#     <div class="stat-label">Courses</div>
# was invisible to it -- the number and its label never appeared in the same
# string. about.html writes every tile that way, and nine of them had drifted
# (70 courses, 163 reading companions, 89 handouts, 36 studios, 22 deep dives,
# 9 data explorers) against canonical values the guard was reporting PASS on.
# The same shape is one indent away in any hand-written page, so match the pair
# across a line boundary in both orders, yielding only spans that fall on the
# line being scanned.
def cross_line_tile_hits(prev, line, nxt, counts):
    if nxt and not SKIP_LINE.search(nxt):
        joined = line + "\n" + nxt
        for rx in TILE_LABEL_RES:
            for m in rx.finditer(joined):
                if m.end(1) > len(line):
                    continue
                key = label_to_key(m.group(2))
                if key is None:
                    continue
                expected = counts.get(key)
                if expected is not None:
                    yield (m.start(1), m.end(1), key, int(m.group(1)), expected)
    if prev and not SKIP_LINE.search(prev):
        joined = prev + "\n" + line
        off = len(prev) + 1
        for rx in TILE_LABEL_FIRST_RES:
            for m in rx.finditer(joined):
                if m.start(2) < off:
                    continue
                key = label_to_key(m.group(1))
                if key is None:
                    continue
                expected = counts.get(key)
                if expected is not None:
                    yield (m.start(2) - off, m.end(2) - off, key,
                           int(m.group(2)), expected)


def main(argv):
    fix = "--fix" in argv
    wiki_dir = None
    if "--wiki" in argv:
        wiki_dir = Path(argv[argv.index("--wiki") + 1]).resolve()
        if not wiki_dir.is_dir():
            print(f"FAIL - --wiki {wiki_dir} is not a directory")
            return 1
    base = wiki_dir or ROOT
    counts = {
        k: v for k, v in json.loads(COUNTS_FILE.read_text()).items()
        if not k.startswith("_")
    }
    pattern = build_pattern()
    failures = []
    fixed = 0
    scanned = 0

    for rel in scanned_files(wiki_dir):
        path = base / rel
        if not path.exists():
            continue
        scanned += 1
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        changed = False
        for i, raw in enumerate(lines):
            line = raw.rstrip("\n")
            newline_suffix = raw[len(line):]
            if SKIP_LINE.search(line):
                continue
            prev_line = lines[i - 1].rstrip("\n") if i else ""
            next_line = lines[i + 1].rstrip("\n") if i + 1 < len(lines) else ""
            raw_hits = list(line_hits(line, pattern, counts)) + list(
                cross_line_tile_hits(prev_line, line, next_line, counts)
            )
            hits = []
            spans = set()
            for h in raw_hits:
                if h[3] == h[4] or in_range(line, h[0], h[1]):
                    continue
                if (h[0], h[1]) in spans:
                    continue
                spans.add((h[0], h[1]))
                hits.append(h)
            if not hits:
                continue
            if fix:
                # apply right-to-left so spans stay valid
                for start, end, key, found, expected in sorted(hits, key=lambda h: -h[0]):
                    line = line[:start] + str(expected) + line[end:]
                    fixed += 1
                lines[i] = line + newline_suffix
                changed = True
            else:
                # de-dupe overlapping hits at the same number position
                seen = set()
                for start, end, key, found, expected in hits:
                    if start in seen:
                        continue
                    seen.add(start)
                    snippet = line[max(0, start - 24):end + 14].strip()
                    failures.append(
                        f"{rel}:{i + 1}: \"…{snippet}…\" "
                        f"({found} but canonical {key} = {expected})"
                    )
        if fix and changed:
            path.write_text("".join(lines), encoding="utf-8")

    if fix:
        print(f"--fix rewrote {fixed} drifted number(s) across {scanned} files. "
              f"Re-run without --fix to confirm PASS.")
        return 0

    if failures:
        print(f"FAIL — {len(failures)} count drift(s) vs data/counts.json:\n")
        for f in failures:
            print(f"  {f}")
        print("\nFix with `python3 scripts/check-counts.py --fix`, or update "
              "data/counts.json if the canonical value changed.")
        return 1

    where = f"the wiki at {wiki_dir}" if wiki_dir else "the site"
    print(f"PASS — counts consistent with data/counts.json across "
          f"{scanned} files ({where})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
