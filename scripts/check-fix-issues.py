#!/usr/bin/env python3
"""Fail when a changelog `### Fixed` entry names no issue.

Why this exists
---------------
On 2026-08-22 the public Known Issues page was found showing nothing. The page
was correct: it reads bug-labelled issues live from GitHub, and in the whole
history of the repository three had ever been filed. Meanwhile the changelog
carried ninety-two `### Fixed` entries -- ninety-two real defects, found, fixed,
written up for readers, and never recorded anywhere a reader could search.

Nothing had gone wrong that anyone would notice. The workflow was simply
find-it-and-fix-it-in-the-same-commit, which is fast, and leaves no trace. A
page that can only show what the workflow files will show nothing, forever,
without ever failing.

So the requirement is: if a fix is worth telling readers about in the release
notes, it is worth a filed issue. This guard enforces exactly that and nothing
more -- it does not ask for an issue per commit, which would be noise, and it
does not read git history, which squash-merges rewrite.

What it checks
--------------
Every bullet under `### Fixed` in a release dated on or after ENFORCE_FROM must
reference an issue as `#NNN`. Earlier releases are grandfathered: they are the
backlog this guard was written because of, and they are published instead via
scripts/build-fix-history.py, which dates them from the release rather than
inventing a close date.

The grandfathering has an expiry in the same sense as the other guards here: it
is a fixed date, not a moving window, so it can only ever cover less.
"""
import datetime
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHANGELOG = ROOT / 'docs' / 'changelog.md'

# Releases from this date forward must cite an issue for every Fixed entry.
# Set to the day the guard was written; everything before it is the backlog.
ENFORCE_FROM = datetime.date(2026, 8, 23)

RELEASE_RE = re.compile(r'^(?P<version>v[\d.]+)\s+—\s+(?P<date>\w+ \d+, \d{4})')
FIXED_RE = re.compile(r'^### Fixed\n(.*?)(?=^###|\Z)', re.M | re.S)
BULLET_RE = re.compile(r'^- (.+?)(?=\n- |\Z)', re.M | re.S)
ISSUE_RE = re.compile(r'#\d+')


def main():
    if not CHANGELOG.exists():
        print('FAIL - %s not found.' % CHANGELOG.relative_to(ROOT))
        return 1

    src = CHANGELOG.read_text(encoding='utf-8')
    failures = []
    checked = grandfathered = 0

    for chunk in re.split(r'^## ', src, flags=re.M)[1:]:
        head = chunk.split('\n', 1)[0]
        m = RELEASE_RE.match(head)
        if not m:
            continue
        try:
            when = datetime.datetime.strptime(m.group('date'), '%B %d, %Y').date()
        except ValueError:
            failures.append('%-12s release date "%s" is not parseable'
                            % (m.group('version'), m.group('date')))
            continue

        for section in FIXED_RE.findall(chunk):
            for bullet in BULLET_RE.findall(section):
                flat = ' '.join(bullet.split())
                if when < ENFORCE_FROM:
                    grandfathered += 1
                    continue
                checked += 1
                if not ISSUE_RE.search(flat):
                    failures.append('%-12s no issue reference: %s'
                                    % (m.group('version'), flat[:96]))

    if failures:
        print('FAIL')
        for f in failures:
            print('  ' + f)
        print('\nEvery "### Fixed" entry in a release dated %s or later must cite the'
              % ENFORCE_FROM.strftime('%-d %B %Y'))
        print('issue it closed, as (#NNN). File the bug, fix it, close it citing the')
        print('commit, and reference it here -- so the public Known Issues page can')
        print('show it. See docs/bug-reporting.md.')
        return 1

    print('PASS - %d Fixed entr%s cite an issue (%d grandfathered before %s).'
          % (checked, 'y' if checked == 1 else 'ies', grandfathered,
             ENFORCE_FROM.isoformat()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
