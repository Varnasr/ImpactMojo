#!/usr/bin/env python3
"""Fail when a judgment entry makes a claim a reader cannot check.

Why this exists
---------------
A database of court judgments read by NGO staff will be used as legal
guidance whatever the disclaimer says. That makes two failure modes far
more expensive here than elsewhere on the platform.

The first is an unsourced holding. A case summary is exactly the kind of
content a language model produces fluently and wrongly, and a wrong
holding is indistinguishable from a right one at a glance. So every entry
must carry a link to the judgment text, and every entry must record that
someone checked the case name and year against that text -- `verified`
carries the date and the source it was checked against.

The second is a holding that was true and no longer is. Unni Krishnan was
substantially reworked by T.M.A. Pai. Section 66A was struck down in
Shreya Singhal and is still used to book people. Sabarimala sits before a
nine-judge bench. An entry that omits this reads authoritative and is
worse than no entry at all, so `status` is mandatory and constrained to a
vocabulary -- there is no "unknown" value, because "we did not check" is
not a thing this file may say silently.

Everything else here is ordinary referential integrity: statute tags must
name a law guide that exists, ids must be unique, no dangling cross-refs.
"""
import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / 'data' / 'judgments.json'
GUIDES = ROOT / 'law-guides'

# A holding is either still good law, or it is qualified. There is no third
# option and deliberately no "unknown": an entry whose status nobody
# established does not ship.
STATUS = {
    'good-law',              # stands, applied as decided
    'codified',              # Parliament enacted it; the statute now governs
    'modified',              # later bench narrowed or reworked it
    'overruled',             # no longer good law
    'under-reference',       # pending before a larger bench
    'partly-overruled',
}

# status_note is NOT here: it is required only when the status is qualified,
# which is checked separately below. A case that is simply good law has
# nothing to add, and demanding filler there would train people to write it.
REQUIRED = ('id', 'case', 'court', 'year', 'holding', 'what_changed',
            'status', 'themes', 'source_url', 'verified')

ID_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
URL_RE = re.compile(r'^https://')


def main():
    if not DATA.exists():
        print('FAIL - %s not found.' % DATA.relative_to(ROOT))
        return 1

    try:
        doc = json.loads(DATA.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        print('FAIL - %s is not valid JSON: %s' % (DATA.relative_to(ROOT), e))
        return 1

    entries = doc.get('judgments', [])
    guides = {p.stem for p in GUIDES.glob('*.html')} if GUIDES.exists() else set()
    failures, seen = [], {}

    for n, j in enumerate(entries, 1):
        who = j.get('id') or ('entry #%d' % n)

        for field in REQUIRED:
            if not j.get(field):
                failures.append('%-28s missing required field "%s"' % (who, field))

        if j.get('id'):
            if not ID_RE.match(j['id']):
                failures.append('%-28s id is not a slug' % who)
            if j['id'] in seen:
                failures.append('%-28s duplicate id (also entry #%d)' % (who, seen[j['id']]))
            seen[j['id']] = n

        st = j.get('status')
        if st and st not in STATUS:
            failures.append('%-28s status "%s" is not one of: %s'
                            % (who, st, ', '.join(sorted(STATUS))))

        # A qualified holding must say how it is qualified. "modified" with an
        # empty note is the exact silence this guard exists to prevent.
        if st and st != 'good-law' and len(str(j.get('status_note', ''))) < 25:
            failures.append('%-28s status "%s" needs a status_note explaining it' % (who, st))

        url = j.get('source_url', '')
        if url and not URL_RE.match(url):
            failures.append('%-28s source_url must be https' % who)

        v = j.get('verified') or {}
        if v:
            if not v.get('date') or not v.get('against'):
                failures.append('%-28s verified needs both "date" and "against"' % who)
            else:
                try:
                    datetime.date.fromisoformat(v['date'])
                except ValueError:
                    failures.append('%-28s verified.date is not ISO YYYY-MM-DD' % who)

        for s in j.get('statutes', []):
            if s not in guides:
                failures.append('%-28s statute tag "%s" names no law guide' % (who, s))

        if j.get('year') and not (1947 <= int(j['year']) <= datetime.date.today().year):
            failures.append('%-28s year %s is out of range' % (who, j['year']))

    if not entries:
        failures.append('data/judgments.json holds no entries')

    if failures:
        print('FAIL')
        for f in failures:
            print('  ' + f)
        print('\nSee docs/judgments-standard.md.')
        return 1

    landmarks = sum(1 for j in entries if j.get('landmark'))
    qualified = sum(1 for j in entries if j.get('status') != 'good-law')
    print('PASS - %d judgment(s): %d landmark, %d carrying a qualified status, '
          '%d verified against primary source.'
          % (len(entries), landmarks, qualified,
             sum(1 for j in entries if j.get('verified'))))
    return 0


if __name__ == '__main__':
    sys.exit(main())
