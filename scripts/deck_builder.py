#!/usr/bin/env python3
"""Reusable builder for ImpactMojo 101-series slide decks.

Extracts the CSS / sprite / nav-JS chrome from an existing deck
(101-courses/data-lit.html) so every generated deck is visually and
behaviourally identical to the rest of the series. Per-deck scripts supply
only content, meta, the title/end screens and (optionally) chart code.
"""
import re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, '101-courses', 'data-lit.html')

_src = open(TPL).read()
CSS = _src[_src.index('<style>'):_src.index('</style>') + len('</style>')]
_sp = _src.index('<svg class="sprites"')
_spend = _src.index('</svg>\n\n<div id="progress-bar"')
SPRITE = _src[_sp:_spend + len('</svg>')]
_mj0 = _src.index('<script>\nconst SLIDE_IDS')
_mj1 = _src.index('</script>', _mj0)
MAINJS = _src[_mj0 + len('<script>'):_mj1]
_pj0 = _src.index('<script>', _mj1)
_pj1 = _src.index('</script>', _pj0)
POLISHJS = _src[_pj0 + len('<script>'):_pj1]

LOGO = ('<svg class="logo-plane" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">'
        '<path d="M50,150 L150,50 L50,100 L80,130 Z" fill="none" stroke="#0EA5E9" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M80,130 L150,50" stroke="#6366F1" stroke-width="2" stroke-dasharray="4,4"/>'
        '<circle cx="150" cy="50" r="4" fill="#10B981"/></svg>')

TITLE_GEO = ('<div class="title-geo"><svg viewBox="0 0 300 620" xmlns="http://www.w3.org/2000/svg" '
             'style="width:100%;height:100%"><defs><pattern id="hex" x="0" y="0" width="40" height="46" '
             'patternUnits="userSpaceOnUse"><polygon points="20,2 38,12 38,34 20,44 2,34 2,12" fill="none" '
             'stroke="white" stroke-width="1"/></pattern></defs><rect width="300" height="620" fill="url(#hex)"/>'
             '</svg></div>')

NO_CHARTS = """// Charts
function initChart(slideIdx) {}

"""


def _header(course):
    return ('<div class="slide-header"><a href="https://www.impactmojo.in/101-courses/" class="logo-mark" '
            'target="_blank">' + LOGO + '<span class="logo-wordmark">ImpactMojo</span></a>'
            '<span class="header-center">' + course + '</span>'
            '<span class="header-url">www.impactmojo.in</span></div>')


def _footer(n):
    return ('<div class="slide-footer"><span class="footer-left">CC BY-NC-ND 4.0 &middot; ImpactMojo 101 Series'
            '</span><span class="slide-number">' + ('%02d' % n) + '</span>'
            '<span class="footer-right">www.impactmojo.in</span></div>')


def build(course, out_name, meta_desc, title_main_html, title_sub_html, title_tags,
          toc, slides, end_headline_html, end_byline, charts_js=NO_CHARTS,
          extra_head_scripts=''):
    """slides: list of (kind, payload). kinds: 'title','toc','divider','content','end'.
    The caller supplies the list already containing title/toc/dividers/end placeholders
    in order; payloads: title->None, toc->list[(name,range)], divider->(num,label,title),
    content->inner_html, end->None.
    """
    parts = []
    for i, (kind, payload) in enumerate(slides):
        n = i + 1
        sid = 's%d' % n
        active = ' active' if n == 1 else ''
        if kind == 'title':
            tags = ''.join('<span class="title-tag">%s</span>' % t for t in title_tags)
            body = ('<div class="title-screen"><div class="title-bg"></div><div class="title-bar"></div>'
                    '<div class="title-content"><div class="title-series">ImpactMojo 101 Series &middot; Free Forever</div>'
                    '<div class="title-main">' + title_main_html + '</div>'
                    '<div class="title-sub">' + title_sub_html + '</div>'
                    '<div class="title-tags">' + tags + '</div></div>' + TITLE_GEO + '</div>')
        elif kind == 'toc':
            items = ''
            for j, (name, rng) in enumerate(payload):
                items += ('<div class="toc-item"><div class="toc-num">%02d</div><div class="toc-name">%s</div>'
                          '<div class="toc-slides">Slides %s</div></div>' % (j + 1, name, rng))
            body = ('<div class="slide-content"><div class="section-label">Agenda</div>'
                    '<div class="slide-title md" style="margin-bottom:8px">What We Cover</div>'
                    '<div class="toc-grid">' + items + '</div></div>')
        elif kind == 'divider':
            num, label, title = payload
            body = ('<div class="section-divider"><div class="div-num">%02d</div>'
                    '<div class="div-label">%s</div><div class="div-title">%s</div>'
                    '<div class="div-accent"></div></div>' % (num, label, title))
        elif kind == 'end':
            body = ('<div class="end-screen"><div class="end-bar"></div><div class="end-pattern"></div>'
                    '<div class="end-glow"></div><div class="end-content">'
                    '<div class="end-eyebrow">ImpactMojo 101 Series</div>'
                    '<div class="end-headline">' + end_headline_html + '</div>'
                    '<div class="end-byline">' + end_byline + '</div>'
                    '<div class="end-cta">'
                    '<a class="end-btn end-btn-primary" href="https://www.impactmojo.in/101-courses/" target="_blank">More 101 Courses</a>'
                    '<a class="end-btn end-btn-secondary" href="https://www.impactmojo.in/" target="_blank">ImpactMojo Home</a>'
                    '<a class="end-btn end-btn-tertiary" href="https://www.impactmojo.in/catalog.html" target="_blank">Full Catalog</a>'
                    '</div>'
                    '<div class="end-meta"><span>Free Forever</span><span class="end-meta-divider">&middot;</span>'
                    '<span>CC BY-NC-ND 4.0</span><span class="end-meta-divider">&middot;</span>'
                    '<span>www.impactmojo.in</span></div></div></div>')
        else:
            body = '<div class="slide-content">' + payload + '</div>'
        parts.append('<div class="slide%s" id="%s">%s%s%s</div>' % (active, sid, _header(course), body, _footer(n)))

    slides_html = '\n\n'.join(parts)
    total = len(slides)

    ids = "['" + "','".join('s%d' % k for k in range(1, total + 1)) + "']"
    mainjs = re.sub(r"const SLIDE_IDS = \[[^\]]*\];", "const SLIDE_IDS = " + ids + ";", MAINJS, count=1)
    head = mainjs[:mainjs.index('// Charts')]
    tail = mainjs[mainjs.index('// Theme'):]
    mainjs = head + charts_js + '\n' + tail

    title_short = course
    HEAD = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>' + course + ' | ImpactMojo</title>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Amaranth:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">\n'
            '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>\n'
            + CSS + '\n'
            '<!-- Google Analytics -->\n'
            '<script async src="https://www.googletagmanager.com/gtag/js?id=G-JRCMEB9TBW"></script>\n'
            "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-JRCMEB9TBW');</script>\n"
            '<!-- SEO meta -->\n'
            '<meta name="description" content="' + meta_desc + '">\n'
            '<meta name="robots" content="index, follow">\n'
            '<link rel="canonical" href="https://www.impactmojo.in/101-courses/' + out_name + '">\n'
            '<meta property="og:title" content="' + title_short + '">\n'
            '<meta property="og:description" content="' + meta_desc + '">\n'
            '<meta property="og:image" content="https://www.impactmojo.in/assets/images/ImpactMojo%20Logo.png">\n'
            '<meta property="og:url" content="https://www.impactmojo.in/101-courses/' + out_name + '">\n'
            '<meta property="og:type" content="website">\n'
            '<meta property="og:site_name" content="ImpactMojo">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="twitter:title" content="' + title_short + '">\n'
            '<meta name="twitter:description" content="' + meta_desc + '">\n'
            '<meta name="twitter:image" content="https://www.impactmojo.in/assets/images/ImpactMojo%20Logo.png">\n'
            '<link rel="icon" type="image/png" href="/assets/images/favicon.png">\n'
            '<link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">\n'
            + extra_head_scripts +
            '</head>\n<body>\n\n')

    THEMEBAR = ('<div id="theme-bar">\n <button class="theme-btn" onclick="setTheme(\'system\')">System</button>\n'
                ' <button class="theme-btn active" onclick="setTheme(\'light\')">Light</button>\n'
                ' <button class="theme-btn" onclick="setTheme(\'dark\')">Dark</button>\n</div>\n\n')

    NAV = ('<div id="nav">\n <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)">&#8249;</button>\n'
           ' <span id="prog-text">1 / ' + str(total) + '</span>\n'
           ' <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)">&#8250;</button>\n</div>\n\n')

    doc = (HEAD + THEMEBAR + SPRITE + '\n\n'
           '<div id="progress-bar"></div>\n<div id="fs-hint" onclick="toggleFS()">fullscreen</div>\n'
           '<div id="deck">\n <div class="slide-viewport" id="viewport">\n\n'
           + slides_html +
           '\n\n </div>\n</div><!-- /deck -->\n\n'
           + NAV +
           '<script>\n' + mainjs + '</script>\n\n'
           '<script>\n' + POLISHJS + '</script>\n\n'
           '<script src="/js/translate-sarvam.js" defer></script>\n</body>\n</html>\n')

    out_path = os.path.join(ROOT, '101-courses', out_name)
    open(out_path, 'w').write(doc)
    return out_path, len(doc), total
