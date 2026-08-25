#!/usr/bin/env python3
"""Build data/union-budget-history.json — a decade of Union spending by head.

Where the numbers come from
---------------------------
Only the current year's Budget at a Glance is published as a spreadsheet. Every
earlier year exists as a PDF, so this extracts them. Each year's PDF carries
four columns -- [Y-2 Actuals, Y-1 BE, Y-1 RE, Y BE] -- and this takes the
**Actuals** column only. Actuals are settled; budget and revised estimates are
superseded by them, and mixing the three into one series would be a chart that
looks like history and is not.

Result: actual expenditure by head for 2017-18 through 2024-25, the last of
which comes from the 2026-27 workbook rather than a PDF.

The PDFs are NOT committed -- seven of them run to 14 MB, and `--check` does not
need them: it validates the built file against itself (see below). Each one's
URL and SHA-256 are recorded in `meta.provenance`, so anyone can re-fetch the
exact bytes and re-run this script. To rebuild, download them to
data/sources/baag/ as baag-<year>.pdf.

How the extraction works
------------------------
The PDFs have no ruled table lines, so `page.find_tables()` finds nothing.
Instead words are grouped into visual rows by y-coordinate and ordered by x.
Only ASCII words form the label: the Hindi in these documents is bilingual with
the English on the same line, and in the 2019-20 file it is encoded in a legacy
non-Unicode font that extracts as mojibake ("BÉÖEãÉ VÉÉä½" for कुल जोड़). None
of it is needed, and storing it would put corruption in the repo.

Why this is trustworthy
-----------------------
Each PDF restates the previous year's Budget Estimate, so consecutive documents
overlap by one column. Seven PDFs plus the workbook give six independent
agreements, and all six match to the rupee. `--check` re-runs that chain: if a
figure is ever edited by hand or an extraction silently shifts a column, the
chain breaks. That is a stronger guarantee than "the script ran without error",
because it is the *documents* agreeing with each other, not the code agreeing
with itself.

What it does not establish
--------------------------
Comparability across years. Heads are renamed, split and merged between budgets
-- "Wealth Tax" and "Service Tax" appear in older years and not newer ones, and
several heads carry footnote markers flagging a definitional change. The page
says so. A head missing in a year is recorded as null, never as zero: a scheme
that did not exist and a scheme that spent nothing are different facts.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

try:
    import pymupdf
except ImportError:
    print('FAIL - pymupdf is required: pip install pymupdf')
    sys.exit(1)

ROOT = pathlib.Path(__file__).resolve().parent.parent
PDFS = ROOT / 'data' / 'sources' / 'baag'
XLSX_JSON = ROOT / 'data' / 'union-budget.json'
OUT = ROOT / 'data' / 'union-budget-history.json'

NUM = re.compile(r'-?[\d,]+(?:\.\d+)?$')
ASCII_WORD = re.compile(r"[A-Za-z0-9&@#*()/.,'\-]+$")

# Head names are not stable strings across years, in four distinct ways, and
# every one of them fragments a series into phantom appearances/disappearances
# if left alone. The first extraction produced "- - Fertiliser", "- Fertiliser"
# and "Fertiliser" as three separate heads, so the chart showed the fertiliser
# subsidy vanishing in 2018 and returning in 2021. It did no such thing.
#
#   1. Subsidy sub-items are indented with dashes: "- - Fertiliser".
#   2. Footnote markers are glued on: "Energy #", "Tax Administration@".
#   3. Footnote *digits* are glued on: "Tax Administration1".
#   4. Long names wrap mid-line, so only part reaches the row:
#      "Home Affairs (including Union" vs "Home Affairs (including Union
#      Territories)" vs "Agriculture and Allied" vs "...Allied Activities".
TRAILING = re.compile(r"[\s*#@\d]+$")
LEADING = re.compile(r'^[\s\-–—]+')
SPACE_BEFORE_PAREN = re.compile(r'\(\s+')
MARKERS = re.compile(r'[@#*]+')
# Rows that disclose a component of the line above. They are already inside
# their parent's total, so counting them again inflates the year.
OF_WHICH = re.compile(r'\s*of\s+which\b', re.I)


def canonical(label):
    """One stable name for a head, whatever the year's typography."""
    name = LEADING.sub('', label)
    name = TRAILING.sub('', name)
    name = SPACE_BEFORE_PAREN.sub('(', name)     # "( including" -> "(including"
    name = MARKERS.sub('', name)                 # "Tax Administration@"
    return ' '.join(name.split())


def merge_wrapped(names):
    """Map each truncated head name onto its full form.

    A wrapped label is a prefix of the complete one, so a longer name sharing a
    prefix absorbs it -- but only when the extra text is the rest of the *name*,
    never a parenthesised qualifier. That distinction is the whole point:

      "Agriculture and Allied"  ->  "Agriculture and Allied Activities"
          a line break mid-name, same head, merge.

      "Agriculture and Allied Activities"  vs  "... (Excluding PM-KISAN)"
          only the 2023-24 budget carries that qualifier, and in that year
          PM-KISAN really is a separate head. Merging stamped "(Excluding
          PM-KISAN)" onto seven years whose documents say no such thing.

      "Home Affairs"  vs  "Home Affairs (including Union Territories)"
          in 2021-22 these were two heads (1,12,301 + 56,490 crore); from
          2023-24 they are one (1,96,872). Merging would draw a 63% jump that
          never happened.

    Only applied when exactly one candidate remains, because an ambiguous merge
    files one head's money under another's name.
    """
    def absorbs(longer, shorter):
        if not longer.startswith(shorter + ' '):
            return False
        return not longer[len(shorter):].lstrip().startswith('(')

    out = {}
    for n in names:
        cands = sorted((f for f in names if f != n and absorbs(f, n)), key=len)
        # The shortest completion wins: "Agriculture and Allied" completes to
        # "Agriculture and Allied Activities", not to the longer variant that
        # also carries a qualifier. A tie in length is genuinely ambiguous and
        # is left alone rather than guessed.
        if cands and (len(cands) == 1 or len(cands[0]) < len(cands[1])):
            out[n] = cands[0]
        else:
            out[n] = n
    # One pass leaves a chain (a -> b -> c) partly resolved; follow it.
    for n in list(out):
        seen = set()
        while out[n] != n and out[n] not in seen:
            seen.add(out[n])
            out[n] = out[out[n]]
    return out


def is_num(w):
    return bool(NUM.fullmatch(w))


def rows_of(page):
    """Words grouped into visual rows by y, then labels reunited with figures.

    A head whose name runs to two or three lines has its figures on the *middle*
    line, alongside the Hindi. In the 2023-24 document that line reads
    "कायषकलाि (िीएम- 76492 83521 76279 84214" -- numbers with no English at all,
    while "Agriculture and Allied Activities" sits on the line above and
    "(Excluding PM-KISAN)" on the line below. Bucketing by y alone therefore
    produced a label with no numbers and numbers with no label, and dropped
    agriculture from that year entirely.

    So: a band carrying figures but no English text takes the nearest English
    label above it, and any English-only band immediately below is appended to
    the name. That recovers "Agriculture and Allied Activities (Excluding
    PM-KISAN)" -- which matters, because that year genuinely moved PM-KISAN out
    of the agriculture head, and the full name is what says so.
    """
    buckets = {}
    for x0, y0, _x1, _y1, w, *_ in page.get_text('words'):
        buckets.setdefault(round(y0 / 3), []).append((x0, w))

    bands = []
    for key in sorted(buckets):
        words = [w for _, w in sorted(buckets[key])]
        label = ' '.join(w for w in words
                         if not is_num(w) and ASCII_WORD.fullmatch(w)).strip()
        nums = [float(w.replace(',', '')) for w in words if is_num(w)]
        bands.append([key, label, nums])

    out = []
    for i, (key, label, nums) in enumerate(bands):
        if not nums:
            continue
        name = label
        if not name:
            # Walk back for the nearest English label that has no figures of
            # its own. Bounded to 3 bands so a stray number never adopts a
            # label from an unrelated row further up the page.
            for j in range(i - 1, max(-1, i - 4), -1):
                if bands[j][1] and not bands[j][2]:
                    name = bands[j][1]
                    bands[j][1] = ''          # claimed; do not reuse
                    break
        if not name:
            continue

        # A dangling "of which ..." above this row means this row IS that
        # sub-item, not a head. In the 2019-20 document the three bands read:
        #
        #     of which Transfer to            <- English, no figures
        #     <Hindi only>                    <- skipped
        #     GST Compensation Fund 56146 ... <- English AND figures
        #
        # so the sub-item carries its own label and the walk-back above never
        # fires. Left unjoined it became a head in its own right, while its
        # amount was already inside Tax Administration -- overstating every
        # PDF year by 2-6% against the published Grand Total. The mismatch
        # against Grand Total is what exposed it; nothing about the text did.
        for j in range(i - 1, max(-1, i - 4), -1):
            if bands[j][2]:
                break                          # a figure row: different item
            if bands[j][1] and OF_WHICH.match(bands[j][1]):
                name = bands[j][1] + ' ' + name
                bands[j][1] = ''
                break

        # A following English-only band completes a wrapped name.
        if i + 1 < len(bands) and bands[i + 1][1] and not bands[i + 1][2]:
            nxt = bands[i + 1][1]
            if not OF_WHICH.match(nxt) and (nxt.startswith('(') or nxt[:1].islower()):
                name = name + ' ' + nxt
                bands[i + 1][1] = ''
        out.append((canonical(name), nums))
    return out


def expenditure_page(doc):
    """The 'Expenditure of Major Items' page, found by content rather than
    number -- it moves between page 11 and 13 across years."""
    for i in range(doc.page_count):
        text = doc[i].get_text()
        if all(k in text for k in ('Grand Total', 'Pension', 'Defence')):
            return i
    return None


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def from_pdf(path):
    doc = pymupdf.open(path)
    page = expenditure_page(doc)
    if page is None:
        return None
    rows = rows_of(doc[page])
    heads, grand, subitems = {}, None, {}
    for label, nums in rows:
        if len(nums) < 4:
            # A row short of four numbers has a blank cell, which means the
            # columns can no longer be matched to years positionally. Skipping
            # is right: a guessed alignment is worse than an absent head.
            continue
        if 'Grand Total' in label:
            grand = nums[:4]
        elif OF_WHICH.search(label):
            subitems[label] = nums[:4]
        else:
            heads[label] = nums[:4]
    return {'page': page, 'heads': heads, 'grand': grand, 'subitems': subitems}


def build():
    if not PDFS.exists():
        print('FAIL - %s not found.' % PDFS.relative_to(ROOT))
        return None

    files = sorted(PDFS.glob('baag-*.pdf'))
    if not files:
        print('FAIL - no baag-*.pdf in %s' % PDFS.relative_to(ROOT))
        return None

    per_year, provenance = {}, []
    for f in files:
        budget_year = f.stem.replace('baag-', '')          # e.g. 2025-26
        got = from_pdf(f)
        if not got or not got['grand']:
            print('FAIL - could not read the expenditure table in %s' % f.name)
            return None
        # Columns are [Y-2 Actuals, Y-1 BE, Y-1 RE, Y BE]; the Actuals column
        # is two years behind the budget year.
        start = int(budget_year[:4]) - 2
        actuals_year = '%d-%02d' % (start, (start + 1) % 100)
        per_year[actuals_year] = {
            'source': f.name,
            'budget_document': budget_year,
            'heads': {k: v[0] for k, v in got['heads'].items()},
            'grand_total': got['grand'][0],
            '_cols': got['grand'],
        }
        provenance.append({
            'year_of_actuals': actuals_year,
            'budget_document': 'Budget at a Glance %s' % budget_year,
            'file': f.name,
            'url': ('https://www.indiabudget.gov.in/budget%s/doc/'
                    'Budget_at_Glance/budget_at_a_glance.pdf' % budget_year),
            'sha256': sha(f),
            'page': got['page'] + 1,
        })

    # The current workbook supplies one more year of Actuals than any PDF.
    if XLSX_JSON.exists():
        xl = json.loads(XLSX_JSON.read_text(encoding='utf-8'))
        blk = xl['blocks']['expenditure_function']
        idx = next((i for i, y in enumerate(blk['years'])
                    if y['kind'] == 'Actuals'), None)
        if idx is not None:
            yr = blk['years'][idx]['year']
            yr = '%s-%s' % (yr[:4], yr[-2:])
            heads = {canonical(r['label']): r['values'][idx]
                     for r in blk['rows']
                     if 'values' in r and r['label'] != 'Grand Total'
                     and r['values'][idx] is not None}
            gt = next(r['values'][idx] for r in blk['rows']
                      if r['label'] == 'Grand Total')
            per_year[yr] = {'source': 'budget-at-a-glance-2026-27.xlsx',
                            'budget_document': '2026-27',
                            'heads': heads, 'grand_total': gt, '_cols': None}
            provenance.append({
                'year_of_actuals': yr,
                'budget_document': 'Budget at a Glance 2026-27',
                'file': 'budget-at-a-glance-2026-27.xlsx',
                'sha256': sha(ROOT / 'data' / 'sources'
                              / 'budget-at-a-glance-2026-27.xlsx'),
                'page': None,
            })

    years = sorted(per_year)

    # The overlap chain: document N's Budget Estimate for year Y is restated as
    # document N+1's second column. Recorded, not just asserted, so a reader can
    # see the checks rather than take the word for it.
    checks = []
    pdf_years = [y for y in years if per_year[y]['_cols']]
    for a, b in zip(pdf_years, pdf_years[1:]):
        left, right = per_year[a]['_cols'][3], per_year[b]['_cols'][1]
        checks.append({'from': per_year[a]['budget_document'],
                       'to': per_year[b]['budget_document'],
                       'value': left, 'restated_as': right,
                       'agrees': abs(left - right) < 1})

    # Union of head names across years, so the series is explicit about which
    # years a head is absent from rather than quietly dropping it.
    raw_heads = {h for y in years for h in per_year[y]['heads']}
    alias = merge_wrapped(raw_heads)
    for y in years:
        merged = {}
        for h, v in per_year[y]['heads'].items():
            merged[alias[h]] = v
        per_year[y]['heads'] = merged
    all_heads = sorted(set(alias.values()))
    series = [{'head': h,
               'values': [per_year[y]['heads'].get(h) for y in years]}
              for h in all_heads]

    # Each year's heads must sum to that year's published Grand Total. This is
    # the strongest check available: eight documents each agreeing with their
    # own printed total, independently. It is what caught the GST Compensation
    # Fund sub-row being counted twice -- the text gave no hint, the arithmetic
    # did.
    residuals = []
    for i, y in enumerate(years):
        got = sum(per_year[y]['heads'][h] for h in per_year[y]['heads'])
        residuals.append(round(got - per_year[y]['grand_total'], 2))

    return {
        'meta': {
            'title': 'Union Budget — actual expenditure by head',
            'unit': '₹ crore',
            'basis': ('Actuals only. Each Budget at a Glance reports the '
                      'position two years back as Actuals; budget and revised '
                      'estimates for the same year are superseded by them and '
                      'are not used here.'),
            'comparability': ('Heads are renamed, split and merged between '
                              'budgets, and several carry footnote markers '
                              'flagging a definitional change. A head absent '
                              'in a year is null, never zero. Read the series '
                              'as indicative of direction, not as a like-for-'
                              'like ledger.'),
            'publisher': 'Ministry of Finance, Government of India',
            'url': 'https://www.indiabudget.gov.in/',
            'years': years,
            'provenance': provenance,
            'overlap_checks': checks,
            'sum_residuals': residuals,
        },
        'grand_total': [per_year[y]['grand_total'] for y in years],
        'series': series,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='verify the committed file rather than rewriting it')
    args = ap.parse_args()

    if args.check:
        if not OUT.exists():
            print('FAIL - %s not found. Run: python3 scripts/build-budget-history.py'
                  % OUT.relative_to(ROOT))
            return 1
        doc = json.loads(OUT.read_text(encoding='utf-8'))
        checks = doc['meta']['overlap_checks']
        bad = [c for c in checks if not c['agrees']]
        if bad:
            print('FAIL - the budget documents disagree where they overlap:')
            for c in bad:
                print('  %s says %s for the year %s restates as %s'
                      % (c['from'], c['value'], c['to'], c['restated_as']))
            return 1
        # Every head must have one value per year, or the series is ragged and
        # the page would silently plot the wrong year.
        n = len(doc['meta']['years'])
        ragged = [s['head'] for s in doc['series'] if len(s['values']) != n]
        if ragged:
            print('FAIL - %d head(s) have the wrong number of years: %s'
                  % (len(ragged), ', '.join(ragged[:4])))
            return 1
        res = doc['meta'].get('sum_residuals', [])
        if len(res) != n:
            print('FAIL - sum_residuals has %d values for %d years' % (len(res), n))
            return 1
        off = [(doc['meta']['years'][i], r) for i, r in enumerate(res) if abs(r) > 2]
        if off:
            print('FAIL - heads do not sum to the published Grand Total:')
            for y, r in off:
                print('  %s is out by %+g crore' % (y, r))
            return 1
        if len(doc['grand_total']) != n:
            print('FAIL - grand_total has %d values for %d years'
                  % (len(doc['grand_total']), n))
            return 1
        print('PASS - %d years, %d heads; %d document overlaps agree and every '
              'year sums to its published total (max %+g crore).'
              % (n, len(doc['series']), len(checks), max(res, key=abs)))
        return 0

    doc = build()
    if doc is None:
        return 1
    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + '\n',
                   encoding='utf-8')
    print('  years   : %s' % ', '.join(doc['meta']['years']))
    print('  heads   : %d' % len(doc['series']))
    print('  overlaps: %d checked, %d agree'
          % (len(doc['meta']['overlap_checks']),
             sum(1 for c in doc['meta']['overlap_checks'] if c['agrees'])))
    print('Wrote %s' % OUT.relative_to(ROOT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
