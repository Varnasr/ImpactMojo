#!/usr/bin/env python3
"""Fail when a stylesheet reads a custom property nothing defines.

Why this exists
---------------
An undefined `var(--x)` does not error and does not fall back -- it makes the
declaration invalid at computed-value time. For a `background` that means
transparent; inside a shorthand it drops the WHOLE declaration. Both are
invisible in review and neither shows up red anywhere.

Measured 2026-08-21, before this guard existed:

  * Eleven flagship shells wrote `.callout-blue { background: var(--callout-blue) }`
    and never defined the token. Every callout in those eleven courses painted
    transparent -- live.
  * `law` wrote `border: 1px dashed var(--cyan)` on its reflection prompts with
    no --cyan. The prompts had no border at all.

axe, pa11y and the contrast guard all passed throughout: a transparent callout
has no contrast problem, it simply is not there.

Scope: course shells plus the shared component sheet they load. A var() WITH a
fallback -- var(--x, #fff) -- is fine by construction and is not flagged.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHARED = ROOT / 'css' / 'course-components.css'
DEF_RE = re.compile(r'(--[a-zA-Z0-9_-]+)\s*:')
USE_RE = re.compile(r'var\(\s*(--[a-zA-Z0-9_-]+)\s*\)')      # no-fallback uses only

# Properties supplied by the browser or by site-wide CSS loaded on every page.
EXEMPT = {
    '--im-accent',      # set by js/site-chrome.js on the injected top bar
}


def shells():
    for d in sorted((ROOT / 'courses').iterdir()):
        if not d.is_dir():
            continue
        f = d / 'index.html'
        if not f.exists():                       # powerBI ships powerbi.html
            f = d / (d.name.lower() + '.html')
        if f.exists():
            yield d.name, f


def main():
    shared_defs = set(DEF_RE.findall(SHARED.read_text(encoding='utf-8'))) if SHARED.exists() else set()
    bad = 0
    for name, f in shells():
        src = f.read_text(encoding='utf-8', errors='replace')
        defined = set(DEF_RE.findall(src)) | shared_defs | EXEMPT
        missing = sorted(set(USE_RE.findall(src)) - defined)
        if missing:
            bad += 1
            print('FAIL %-18s uses undefined: %s' % (name, ', '.join(missing)))
    if bad:
        print('\n%d shell(s) read a custom property nothing defines.' % bad)
        print('Define it in css/course-components.css, or give the var() a fallback.')
        return 1
    print('PASS - every var() in %d course shells resolves.' % len(list(shells())))
    return 0


if __name__ == '__main__':
    sys.exit(main())
