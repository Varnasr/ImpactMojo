#!/usr/bin/env python3
"""Every page that loads site-chrome.js must still have an <h1> after the chrome runs.

js/site-chrome.js removes, at runtime, any <header>/<nav> that is a direct child of
<body> (plus .nav-container/.masthead/.mobile-header/footer/.foot/.site-footer/
.im-footer anywhere). That is deliberate — it strips legacy per-page nav bars so the
shared top bar can be injected. But a page whose only <h1> lives inside that
body-level <header> ships a heading that no visitor and no screen reader ever sees.

This has bitten three times: ASER's methodology section (class="foot", July),
NFHS's sources block (<footer class="nf-foot">, July), and eleven root pages whose
hero <h1> vanished — found 2026-08-21, fixed by swapping <header class="hero"> for
<section class="hero">.

Neither accessibility job catches it: axe-core tests 10 hardcoded pages and pa11y-ci
19, and none of the eleven were in either list. A page can be added at any time
without being added to those lists, so the check has to be structural and sitewide.

The parser is deliberately crude but conservative: it only treats a <header> as
body-level when no <main>/<section>/<article>/<div> is open at that point, so a
nested <header> inside a card or article is never counted.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Pages that legitimately have no <h1> at all (nothing for the chrome to eat).
EXEMPT = {
    # add "path.html": "reason" here
}

def opts_out(src: str, rel: str) -> bool:
    """True when site-chrome.js loads but deliberately leaves the page's chrome alone.

    site-chrome.js treats these as "the homepage" and skips build() entirely
    (see its isHome check): data-im-home on <html> or <body>, a
    <meta name="im-chrome" content="off">, or the site root path. Pages that
    opt out keep their own <header>, so nothing is stripped and this guard must
    not report them. Missing this made two ImpactLex pages look broken when
    they were fine -- the same false-positive shape that made an earlier ad-hoc
    viewport check untrustworthy.
    """
    if re.search(r'<meta\s+name="im-chrome"\s+content="off"', src, re.I):
        return True
    if re.search(r'<(html|body)\b[^>]*\bdata-im-home\b', src, re.I):
        return True
    return rel == 'index.html'


CONTAINERS = re.compile(r'<(main|section|article|div)\b', re.I)
CONTAINERS_CLOSE = re.compile(r'</(main|section|article|div)>', re.I)

# The class tokens site-chrome.js kills ANYWHERE in the document, taken verbatim
# from its `sel` string. The earlier version of this guard modelled only the
# body-level <header>/<nav> rule and reported PASS while 13 course lexicons were
# shipping with no <h1> in the browser: their heading sits in
# <header class="header"> nested inside .container, which `header.header` in that
# selector removes regardless of depth. Measured in Chromium, not inferred.
KILL_CLASSES = {
    'im-topbar', 'top-nav', 'site-header', 'navbar', 'site-nav', 'main-nav',
    'nav-container', 'masthead', 'mobile-header',
    'footer', 'foot', 'site-footer', 'im-footer',
}
# <header class="header"> and <header class="mobile-header"> are killed by tag+class.
KILL_TAG_CLASS = {('header', 'header'), ('header', 'mobile-header')}
KILL_IDS = {'imtopbar'}
# The <footer> tag itself is in the selector.
KILL_TAGS = {'footer'}

OPEN_TAG = re.compile(r'<(header|nav|div|section|footer|aside)\b([^>]*)>', re.I)
ATTR_CLASS = re.compile(r'\bclass\s*=\s*["\']([^"\']*)["\']', re.I)
ATTR_ID = re.compile(r'\bid\s*=\s*["\']([^"\']*)["\']', re.I)


def _is_killed(tag: str, attrs: str) -> bool:
    tag = tag.lower()
    if tag in KILL_TAGS:
        return True
    cm = ATTR_CLASS.search(attrs)
    classes = set(cm.group(1).split()) if cm else set()
    if classes & KILL_CLASSES:
        return True
    if any((tag, c) in KILL_TAG_CLASS for c in classes):
        return True
    im = ATTR_ID.search(attrs)
    if im and im.group(1).strip().lower() in KILL_IDS:
        return True
    return False


def _element_end(src: str, tag: str, open_end: int) -> int:
    """Index just past the matching close tag, by depth counting. -1 if unclosed."""
    depth = 1
    pat = re.compile(r'<(/?)%s\b[^>]*>' % re.escape(tag), re.I)
    pos = open_end
    while True:
        m = pat.search(src, pos)
        if not m:
            return -1
        depth += -1 if m.group(1) else 1
        pos = m.end()
        if depth == 0:
            return m.end()


def body_level_headers(body: str):
    """Yield (start, end_of_open_tag) for each <header> at body level."""
    for m in re.finditer(r'<header\b[^>]*>', body, re.I):
        pre = body[:m.start()]
        if len(CONTAINERS.findall(pre)) - len(CONTAINERS_CLOSE.findall(pre)) == 0:
            yield m.start(), m.end()


def strip_chrome(body: str) -> str:
    """Remove what site-chrome.js removes, so we see what the visitor sees.

    Two rules, both from the real source: any element matching the kill selector
    at any depth, and any <header>/<nav> that is a direct child of <body>.
    Removal is outermost-first so a nested match inside an already-removed block
    is not double-counted.
    """
    spans = []
    for m in OPEN_TAG.finditer(body):
        tag, attrs = m.group(1), m.group(2)
        if not _is_killed(tag, attrs):
            continue
        end = _element_end(body, tag, m.end())
        if end > 0:
            spans.append((m.start(), end))
    for start, open_end in body_level_headers(body):
        end = _element_end(body, 'header', open_end)
        if end > 0:
            spans.append((start, end))

    # keep only outermost spans, then cut right-to-left
    spans.sort(key=lambda sp: (sp[0], -sp[1]))
    outer, last_end = [], -1
    for a, b in spans:
        if a >= last_end:
            outer.append((a, b))
            last_end = b
    out = body
    for a, b in reversed(outer):
        out = out[:a] + out[b:]
    return out


def main() -> int:
    failures, checked = [], 0
    for path in sorted(ROOT.rglob('*.html')):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(('Backups/', 'node_modules/', 'tests/')):
            continue
        try:
            src = path.read_text(encoding='utf-8', errors='replace')
        except OSError:
            continue
        if 'site-chrome.js' not in src:
            continue          # page does not run the chrome; nothing is stripped
        if opts_out(src, rel):
            continue          # chrome is loaded but skips build(); the header stays
        checked += 1
        if rel in EXEMPT:
            continue
        b = src.find('<body')
        if b < 0:
            continue
        body = src[b:]
        if '<h1' not in body:
            continue          # no h1 to lose — a different concern, not this guard's
        if '<h1' not in strip_chrome(body):
            failures.append(rel)

    stale = sorted(set(EXEMPT) - {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.html')})
    for rel in stale:
        failures.append(f'{rel} (stale EXEMPT entry — file no longer exists)')

    if failures:
        print('FAIL - these pages lose their only <h1> when site-chrome.js runs.')
        print('       The heading sits in a body-level <header>, which is removed at')
        print('       runtime. Use <section class="hero"> instead (same CSS class,')
        print('       so styling is unchanged).\n')
        for f in failures:
            print(f'  {f}')
        return 1

    print(f'PASS - <h1> survives site-chrome on all {checked} pages that load it.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
