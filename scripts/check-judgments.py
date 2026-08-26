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
# `case` is the name written as a lawyer would cite it; `source_title` is the
# raw title of the document it was verified against. Both are required, and they
# are separate on purpose: the clean name is editorial, and if it were the only
# name recorded there would be no way to check it back against the source.
REQUIRED = ('id', 'case', 'source_title', 'court', 'year', 'holding',
            'what_changed', 'status', 'themes', 'source_url', 'verified')

ID_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
URL_RE = re.compile(r'^https://')


def citation_numbers(text):
    """Petition/citation numbers in a string, normalised so "196 of 2001" and
    "196/2001" compare equal. These identify a case; party names do not."""
    out = set()
    for num, year in re.findall(r'(\d{1,5})\s*(?:of\s*|/)\s*((?:19|20)\d\d)', text):
        out.add('%s/%s' % (num.lstrip('0') or '0', year))
    return out


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

        # A scraper title in the `case` field means the clean-up was skipped.
        name = j.get('case', '')
        if ' vs ' in name or ' on ' in name.lower()[-24:] or '...' in name:
            failures.append('%-28s case name looks like raw scraper output: %s'
                            % (who, name[:60]))

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

    # The same judgment must not appear twice. It nearly did: three entries were
    # added under new ids for cases already in the docket under different names
    # ("CPIO, Supreme Court of India" vs "Central Public Information Officer,
    # Supreme Court of India"), so a name search found nothing and the id was
    # free. The source URL is the only stable identity a judgment has here.
    seen_url = {}
    for i, j in enumerate(entries):
        u = j.get('source_url')
        if not u:
            continue
        if u in seen_url:
            failures.append('%-28s same source_url as %s -- one judgment, two entries'
                            % ('#%d %s' % (i + 1, j.get('id', '?')), seen_url[u]))
        else:
            seen_url[u] = j.get('id', '#%d' % (i + 1))

    if not entries:
        failures.append('data/judgments.json holds no entries')

    # An "excluded" entry that names a case the docket actually publishes tells
    # a reader the opposite of the truth. That shipped: the right-to-food
    # litigation sat under "What is deliberately not here" while two of its
    # orders were live on the same page, because the note was written when the
    # docket had neither and never moved when they went in.
    #
    # Matched on the petition/citation number rather than party names, because
    # the party names in Indian public-interest litigation repeat endlessly
    # ("Union of India" is one side of most of this file) while "196 of 2001"
    # identifies exactly one petition. A caveat about what a published entry
    # stands for belongs in meta.coverage_notes, which the page renders under
    # coverage instead of under exclusions.
    published = set()
    for j in entries:
        published |= citation_numbers(' '.join(
            str(j.get(k, '')) for k in ('case', 'source_title', 'holding')))
    for i, e in enumerate(doc.get('meta', {}).get('excluded', []) or []):
        if not isinstance(e, dict) or not e.get('case') or not e.get('why'):
            failures.append('meta.excluded[%d]           needs both "case" and "why"' % i)
            continue
        clash = citation_numbers(e['case'] + ' ' + e['why']) & published
        if clash:
            failures.append(
                'meta.excluded[%d]           names %s, which the docket publishes -- '
                'a coverage caveat belongs in meta.coverage_notes'
                % (i, ', '.join(sorted(clash))))

    notes = doc.get('meta', {}).get('coverage_notes', [])
    if not isinstance(notes, list) or any(not isinstance(n, str) or not n.strip()
                                          for n in notes):
        failures.append('meta.coverage_notes         must be a list of non-empty strings')

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
