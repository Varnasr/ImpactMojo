#!/usr/bin/env python3
"""Measure every flagship against docs/flagship-course-standard.md, Part C.

Why this exists
---------------
The standard is written down; conformance to it was not measured. Part D of the
standard is a hand-made gap snapshot from 2026-07 covering two courses, and it
went stale immediately. Building the ESG flagship in 2026-08 surfaced the cost:
`social-movements`' shell carries no CSS for `stats-grid`, `key-insight` or any
callout colour, so content written to the standard renders unstyled there --
and nothing reported that.

This script reads the live `course_content` rows (content is not in the repo)
and each course shell, and prints one row per flagship. It takes the module
bodies on stdin as JSON so it can run without database credentials:

    python3 scripts/audit-flagships.py < modules.json

where modules.json is [{"course_id":..,"module_number":..,"content_html":..}, ..].
Pass --shell-only to skip the content half and audit just the shells.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COURSES = ROOT / 'courses'

# Slug -> DB course_id where they differ (course-loader.js COURSE_ID_MAP).
DB_ID = {'sel': 'SEL'}

# Component -> how many the standard expects, expressed per module unless noted.
CONTENT_CHECKS = [
    ('excerpt',    'excerpt-btn',       1.0,  'paper excerpt'),
    ('reflect',    'reflection-prompt', 1.0,  'reflection prompt'),
    ('worked',     'worked-example',    1.0,  'worked example'),
    ('diagram',    'dag-figure',        0.25, 'SVG diagram'),   # "several per course"
]

# The coach block has its own rule, because a count alone cannot express it:
# exactly one per module, alternating between the two coaches so that no two
# consecutive modules show the same face. Stacking is the commoner failure --
# measured 2026-08, SEL carried 52 callouts across 13 modules and devai 37
# across 12, which trains a reader to skip the CTA the block exists for.
COACH_RE = re.compile(r'/assets/images/(vandana|varna)-photo\.jpg', re.I)


def coach_gaps(mods):
    """`mods` is each module's content_html, ordered by module_number."""
    gaps, seq, over, under = [], [], 0, 0
    for html in mods:
        found = COACH_RE.findall(html or '')
        seq.append(found[0].lower() if found else None)
        if len(found) > 1:
            over += 1
        elif not found:
            under += 1
    if under:
        gaps.append('no coach callout in %d module(s)' % under)
    if over:
        gaps.append('coach callout stacked in %d module(s)' % over)
    repeats = sum(1 for a, b in zip(seq, seq[1:]) if a and a == b)
    if repeats:
        gaps.append('same coach twice running in %d place(s)' % repeats)
    # A callout with no coaching link is the CTA-less shape `pubchoice` carried
    # until 2026-08: a coach's name and a paragraph, and nothing to click. The
    # photo check is deliberately strict about the canonical `<img class=
    # "coach-photo">`, because the variant it replaced sized a 32px quote icon
    # inside a 64px circle the shell CSS had always written for a face.
    noclick = sum(1 for h in mods
                  if COACH_RE.search(h or '') and 'coach-links' not in (h or ''))
    if noclick:
        gaps.append('coach callout has no CTA in %d module(s)' % noclick)
    return gaps

SHELL_CHECKS = [
    # Both class names are in use: most shells write hero-resource-btn, devai
    # and gender write hero-btn. Counting only the first reported those two as
    # 0/4 when they carry a full set, including real Dropbox and NotebookLM links.
    ('hero buttons (4)',   lambda s: len(re.findall(r'class="hero-(?:resource-)?btn\b', s)), 4),
    ('resource cards (7)', lambda s: len(re.findall(r'class="resource-card [a-z0-9]+"', s)), 7),
    ('v3 blob divs (4)',   lambda s: len(re.findall(r'class="v3-blob v3-blob-\d"', s)), 4),
    ('reading-progress',   lambda s: 1 if 'id="reading-progress"' in s else 0, 1),
    ('JSON-LD Course',     lambda s: 1 if '"@type": "Course"' in s else 0, 1),
]

# Classes a shell must style for standard content to render at all.
REQUIRED_CSS = ['stats-grid', 'stat-card', 'key-insight', 'callout-blue', 'callout-green',
                'callout-amber', 'callout-red', 'coach-callout', 'reflection-prompt',
                'worked-example', 'capstone-timeline', 'dag-figure', 'data-exercise']


def flagships():
    for d in sorted(COURSES.iterdir()):
        if not d.is_dir():
            continue
        if (d / 'index.html').exists() or (d / (d.name.lower() + '.html')).exists():
            yield d.name


def audit_shell(slug):
    shell = COURSES / slug / 'index.html'
    if not shell.exists():                      # powerBI ships as powerbi.html
        shell = COURSES / slug / (slug.lower() + '.html')
    src = shell.read_text(encoding='utf-8')
    row = {name: (fn(src), want) for name, fn, want in SHELL_CHECKS}
    # Component CSS moved to a shared sheet in 2026-08 (see the header of
    # css/course-components.css). Resolve it too, or every shell that correctly
    # relies on the shared sheet reports as missing all of it -- which turns
    # this column into a blindfold rather than a check.
    css = src
    for m in re.finditer(r'<link[^>]+href="(/css/[^"?]+)', src):
        extra = ROOT / m.group(1).lstrip('/')
        if extra.exists():
            css += extra.read_text(encoding='utf-8')
    row['missing CSS'] = ([c for c in REQUIRED_CSS if not re.search(r'\.%s\b' % re.escape(c), css)], [])
    row['lexicon terms (40+)'] = (count_terms(COURSES / slug / 'lexicon.html'), 40)
    return row


# Lexicons were authored at different times and use four different shapes for a
# term: a bare JS key, a quoted JSON key, an object with an id before the term,
# and (in `causal`) static markup with no data array at all. Counting only one
# shape reported 0 terms for most flagships -- a false gap that would have sent
# someone rewriting perfectly good lexicons. Take the largest plausible count.
TERM_SHAPES = [
    r'\{\s*term\s*:',            # {term:"..."
    r'"term"\s*:',               # "term": "..."
    r'\bterm\s*:\s*[\'"]',       # id: 1, term: '...'
    r'<h3 class="lex-t"',        # static cards (causal)
    r'class="term-name"',
    r'^\s*\["',                  # gender: const TERMS = [ ["Term","Cat",...], ...
    r'^\s+roman:\s*"',           # gandhi: {id: 1, devanagari: "...", roman: "..."}
]


def count_terms(path):
    if not path.exists():
        return 0
    src = path.read_text(encoding='utf-8')
    return max(len(re.findall(rx, src, re.M)) for rx in TERM_SHAPES)


def main(argv):
    shell_only = '--shell-only' in argv
    by_course = {}
    if not shell_only:
        try:
            rows = json.load(sys.stdin)
        except Exception as exc:                    # no stdin / bad JSON
            print('could not read module JSON on stdin (%s); use --shell-only' % exc)
            return 2
        rows.sort(key=lambda r: (r['course_id'], r['module_number']))
        for r in rows:
            by_course.setdefault(r['course_id'], []).append(r['content_html'] or '')

    failures = 0
    print('%-18s %5s %7s %s' % ('course', 'mods', 'KB/mod', 'gaps against the standard'))
    print('-' * 100)
    for slug in flagships():
        gaps = []
        shell = audit_shell(slug)
        for name, (got, want) in shell.items():
            if name == 'missing CSS':
                if got:
                    gaps.append('shell has no CSS for: ' + ', '.join(got))
            elif got < want:
                gaps.append('%s: %s/%s' % (name, got, want))

        mods = by_course.get(DB_ID.get(slug, slug), [])
        n = len(mods)
        kb = (sum(len(m) for m in mods) / n / 1024) if n else 0
        if n:
            if kb < 10:
                gaps.append('prose %.1f KB/module (want >=10)' % kb)
            for _key, cls, per_mod, label in CONTENT_CHECKS:
                got = sum(m.count('class="%s' % cls) for m in mods)
                want = max(1, int(round(per_mod * n)))
                if got < want:
                    gaps.append('%s: %d (want ~%d)' % (label, got, want))
            gaps.extend(coach_gaps(mods))
            if not any('capstone-timeline' in m for m in mods):
                gaps.append('no capstone-timeline')
        elif not shell_only:
            gaps.append('NO MODULES IN DB')

        failures += len(gaps)
        print('%-18s %5d %7.1f %s' % (slug, n, kb, '; '.join(gaps) if gaps else 'on standard'))

    print('-' * 100)
    print('%d gap(s) across %d flagships' % (failures, len(list(flagships()))))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
