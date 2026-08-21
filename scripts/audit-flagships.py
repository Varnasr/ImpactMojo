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
    ('coach',      'coach-callout',     0.20, 'coach callout'), # "~1 in 3", floor at 1 in 5
]

SHELL_CHECKS = [
    ('hero buttons (4)',   lambda s: len(re.findall(r'class="hero-resource-btn', s)), 4),
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
    row['missing CSS'] = ([c for c in REQUIRED_CSS if not re.search(r'\.%s\b' % re.escape(c), src)], [])
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
]


def count_terms(path):
    if not path.exists():
        return 0
    src = path.read_text(encoding='utf-8')
    return max(len(re.findall(rx, src)) for rx in TERM_SHAPES)


def main(argv):
    shell_only = '--shell-only' in argv
    by_course = {}
    if not shell_only:
        try:
            rows = json.load(sys.stdin)
        except Exception as exc:                    # no stdin / bad JSON
            print('could not read module JSON on stdin (%s); use --shell-only' % exc)
            return 2
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
