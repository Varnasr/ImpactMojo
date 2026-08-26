#!/usr/bin/env python3
"""Fail when a judgment's source_url does not actually resolve.

Why this exists
---------------
Entries sourced from the AWS Open Data Registry carry a path built from the
Supreme Court's own metadata index (year, volume, page range). That path is
easy to get *nearly* right: on 2026-08-26 an entry shipped pointing at
2009_5_913_927 when the real document is 2009_5_913_936, because the range end
was guessed from a neighbouring record instead of read from the index. The
link 404s, and a docket whose whole promise is "check it yourself" had a
citation that could not be checked.

Network-dependent, so it runs on the daily schedule and on demand rather than
on every pull request -- a contributor cannot act on somebody else's S3 being
slow, and this is the same reasoning the supabase-anon guard uses.
"""
import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / 'data' / 'judgments.json'
TIMEOUT = 60


def head(url):
    req = urllib.request.Request(url, method='HEAD',
                                 headers={'User-Agent': 'ImpactMojo docket link check'})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:                      # noqa: BLE001 - report, do not raise
        return 'ERR %s' % type(e).__name__


def main():
    doc = json.loads(DATA.read_text(encoding='utf-8'))
    # Only the machine-addressable sources. indiankanoon.org rate-limits and
    # sometimes serves a soft 200 for a missing doc, so a HEAD there proves
    # nothing; those entries are verified by their recorded checks instead.
    targets = [j for j in doc['judgments'] if 'amazonaws.com' in j.get('source_url', '')]
    if not targets:
        print('PASS - no machine-addressable judgment sources to check.')
        return 0

    failures = []
    for j in targets:
        status = head(j['source_url'])
        if status != 200:
            failures.append('%-30s %s  %s' % (j['id'], status, j['source_url']))

    if failures:
        print('FAIL - %d judgment source_url(s) did not resolve:\n' % len(failures))
        for f in failures:
            print('  ' + f)
        print('\n       Read the real path from the court metadata index rather than')
        print('       inferring it: the page range in the key is not guessable.')
        return 1

    print('PASS - all %d judgment source PDF(s) resolve.' % len(targets))
    return 0


if __name__ == '__main__':
    sys.exit(main())
