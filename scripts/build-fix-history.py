#!/usr/bin/env python3
"""Derive the public fix history from the changelog's `### Fixed` sections.

Why this exists
---------------
`known-issues.html` reads live from GitHub Issues, which is the right source for
what is *currently* broken: it cannot quietly fall behind what we are working on.
It is the wrong source for what we have *already* fixed, because this repository
did not file issues for defects. Ninety-two defects were found, fixed and written
up in `docs/changelog.md` between March and August 2026; three carried a
bug-labelled issue.

Backfilling those as closed GitHub issues was considered and rejected. The page
prints "Fixed N days ago" from the issue's `closed_at`, so seventy issues closed
in one afternoon would every one of them read "Fixed today" -- including defects
fixed in June. A page built to stop us overstating what we know would have
started overstating when we knew it.

The changelog already carries the true date: the release the fix shipped in. So
the history is derived from there, and the page renders it as a separate,
clearly-dated section rather than mixing it in with live issue data.

Usage
-----
    python3 scripts/build-fix-history.py            # rewrite data/fix-history.json
    python3 scripts/build-fix-history.py --check    # fail if it is out of date

The --check mode runs in CI, so an edit to the changelog's Fixed sections that
is not reflected in the JSON is caught rather than silently diverging.
"""
import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHANGELOG = ROOT / 'docs' / 'changelog.md'
OUT = ROOT / 'data' / 'fix-history.json'

# Entries older than this are still parsed and published; the cutoff only bounds
# how much the page shows by default. Kept here so the page and the guard agree.
MAX_ENTRIES = 120

RELEASE_RE = re.compile(r'^(?P<version>v[\d.]+)\s+—\s+(?P<date>\w+ \d+, \d{4})')
BULLET_RE = re.compile(r'^- (.+?)(?=\n- |\Z)', re.M | re.S)
FIXED_RE = re.compile(r'^### Fixed\n(.*?)(?=^###|\Z)', re.M | re.S)


def strip_markdown(text):
    """Flatten a changelog bullet into the plain sentence the page will show."""
    t = ' '.join(text.split())
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)   # links -> their text
    t = re.sub(r'\*\*([^*]+)\*\*', r'\1', t)          # bold
    t = re.sub(r'`([^`]+)`', r'\1', t)                # code spans
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'\1', t)  # italics
    return t.strip()


def split_headline(text):
    """Most bullets lead with a bolded headline; use it as the title when present.

    Falls back to the first sentence, then to a truncation, so a bullet written
    without the convention still produces something readable rather than nothing.
    """
    m = re.match(r'\s*\*\*(.+?)\*\*(.*)$', text.strip(), re.S)
    if m:
        return strip_markdown(m.group(1)).rstrip('.'), strip_markdown(m.group(2))
    flat = strip_markdown(text)
    m = re.match(r'(.{20,140}?[.!?])\s+(.*)$', flat, re.S)
    if m:
        return m.group(1).rstrip('.'), m.group(2)
    return (flat[:140].rstrip() + ('…' if len(flat) > 140 else '')), ''


def parse():
    src = CHANGELOG.read_text(encoding='utf-8')
    entries = []
    for chunk in re.split(r'^## ', src, flags=re.M)[1:]:
        head = chunk.split('\n', 1)[0]
        m = RELEASE_RE.match(head)
        if not m:
            continue
        try:
            when = datetime.datetime.strptime(m.group('date'), '%B %d, %Y').date()
        except ValueError:
            continue
        for section in FIXED_RE.findall(chunk):
            for bullet in BULLET_RE.findall(section):
                title, detail = split_headline(bullet)
                if not title:
                    continue
                issue = re.search(r'#(\d+)', bullet)
                entries.append({
                    'title': title,
                    'detail': detail,
                    'fixed_on': when.isoformat(),
                    'release': m.group('version'),
                    'issue': int(issue.group(1)) if issue else None,
                })
    entries.sort(key=lambda e: (e['fixed_on'], e['release']), reverse=True)
    return entries[:MAX_ENTRIES]


def payload(entries):
    return {
        'generated_from': 'docs/changelog.md',
        'note': ('Derived from the changelog, not from GitHub Issues. Dates are '
                 'the release the fix shipped in, which is what we actually know; '
                 'issue numbers appear only where one was filed.'),
        'count': len(entries),
        'entries': entries,
    }


def main():
    check = '--check' in sys.argv
    data = payload(parse())
    new = json.dumps(data, indent=2, ensure_ascii=False) + '\n'

    if check:
        if not OUT.exists():
            print('FAIL - %s does not exist. Run scripts/build-fix-history.py.' % OUT.relative_to(ROOT))
            return 1
        if OUT.read_text(encoding='utf-8') != new:
            print('FAIL - %s is out of date with docs/changelog.md.' % OUT.relative_to(ROOT))
            print('       Run: python3 scripts/build-fix-history.py')
            return 1
        print('PASS - fix history matches the changelog (%d entries).' % data['count'])
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(new, encoding='utf-8')
    print('Wrote %s (%d entries).' % (OUT.relative_to(ROOT), data['count']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
