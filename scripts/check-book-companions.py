#!/usr/bin/env python3
"""
Blank-page regression guard for BookSummaries/ companions.

The interactive companions render their content client-side from an inline
`const DATA = {...}` object. A handful of deterministic mistakes cause a page to
render BLANK (no content) in the browser even though the file looks fine:

  1. DATA is not valid JSON            → the <script> throws, nothing renders.
  2. `</script>` inside DATA           → the HTML parser ends the <script> early.
  3. U+2028 / U+2029 inside DATA        → illegal in a JS string literal (older engines).
  4. raw C0 control chars inside DATA   → JS syntax error.
  5. empty title or empty sections      → the app paints an empty shell.

This guard catches exactly those, and nothing else — it is intentionally lenient
about schema variations (older companions omit `southAsia`, use `summary` instead
of `ideas`, or ship as a compiled bundle with no `const DATA`) so it has zero
false positives on the existing library. Run in CI on every push/PR.

Exit 0 = PASS, exit 1 = one or more companions would render blank.
For a deeper, real-browser check, see scripts/validate-companions.mjs.
"""
import glob
import json
import os
import re
import sys

BROKEN_SCRIPT = re.compile(r'</script', re.IGNORECASE)
BAD_CTRL = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f]')


def extract_data(s):
    """Return (data_obj, raw_str) or (None, error_message)."""
    i = s.find('const DATA')
    if i < 0:
        return None, None  # not a data-driven companion
    eq = s.find('=', i)
    b = s.find('{', eq)
    if b < 0:
        return None, "const DATA present but no object literal found"
    depth = 0; j = b; instr = False; esc = False; q = ''
    while j < len(s):
        c = s[j]
        if instr:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == q: instr = False
        else:
            if c in '"\'': instr = True; q = c
            elif c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    break
        j += 1
    raw = s[b:j + 1]
    try:
        return json.loads(raw), raw
    except Exception as e:
        return None, f"DATA is not valid JSON: {e}"


def check(path):
    """Return list of FAIL messages for one file (empty = ok)."""
    s = open(path, encoding='utf-8').read()
    fails = []

    if 'const DATA' in s:
        data, raw = extract_data(s)
        if data is None:
            fails.append(raw or "could not extract DATA")
            return fails
        # 2-4: browser-breaking sequences inside the DATA script block
        if BROKEN_SCRIPT.search(raw):
            fails.append("DATA contains '</script>' — breaks the <script> block (blank page)")
        if ' ' in raw or ' ' in raw:
            fails.append("DATA contains U+2028/U+2029 — illegal in a JS string literal")
        if BAD_CTRL.search(raw):
            fails.append("DATA contains a raw C0 control character — JS syntax error")
        # 5: empty title / sections
        if not isinstance(data.get('title'), str) or not data['title'].strip():
            fails.append("DATA.title is empty")
        secs = data.get('sections')
        if not isinstance(secs, list) or len(secs) == 0:
            fails.append("DATA.sections is empty — nothing to render")
        else:
            titled = [x for x in secs if isinstance(x, dict) and str(x.get('title', '')).strip()]
            if len(titled) == 0:
                fails.append("no section has a title — sections panel would be blank")
    else:
        # compiled-bundle / legacy companion: sanity-check it isn't an empty stub
        if len(s) < 3000:
            fails.append("no `const DATA` and file is < 3KB — likely an empty/broken stub")
        if '<title' not in s.lower():
            fails.append("no <title> tag")
    return fails


def main():
    files = sorted(glob.glob('BookSummaries/*-companion.html'))
    if not files:
        print("check-book-companions: no companion files found", file=sys.stderr)
        return 1
    problems = {}
    for f in files:
        fails = check(f)
        if fails:
            problems[f] = fails
    print(f"Checked {len(files)} book companions.")
    if problems:
        print(f"\nFAIL — {len(problems)} companion(s) would render blank:\n")
        for f, fails in sorted(problems.items()):
            print(f"  {f}")
            for m in fails:
                print(f"      - {m}")
        print("\nFix the DATA object(s) above (see scripts/check-book-companions.py header).")
        return 1
    print("PASS — every companion has parseable DATA, a title, sections, and no "
          "browser-breaking characters.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
