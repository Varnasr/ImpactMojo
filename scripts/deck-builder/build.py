#!/usr/bin/env python3
"""
ImpactMojo 101 Series — Native Deck Builder
===========================================
Generates a self-contained, gold-standard native slide deck (the same format
as 101-courses/dev-economics.html) from a compact Python spec.

WHY a "shell donor":
  The gold-standard decks carry ~430 lines of evolved CSS and ~280 lines of
  runtime JS (theme switcher, viewport scaling, lazy chart init, deep-linking,
  auto-fit/compact modes, ECharts resize). Re-typing that risks drift. Instead
  we slice the proven shell out of a donor deck (dev-economics.html) and inject
  only the parts that vary per deck:
    - the slides HTML (between the viewport open/close markers)
    - the SLIDE_IDS array
    - the Chart.js initChart() body
    - the ECharts initECharts() body (optional)
    - the SEO / title strings in <head>

Usage:
    python3 scripts/deck-builder/build.py <spec_module> [--check]
    e.g.  python3 scripts/deck-builder/build.py data_lit

A spec module lives in scripts/deck-builder/specs/<name>.py and defines DECK.
See specs/_schema.md for the spec format.
"""
import json
import re
import sys
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DONOR = ROOT / "101-courses" / "dev-economics.html"
SPECS_DIR = Path(__file__).resolve().parent / "specs"
OUT_DIR = ROOT / "101-courses"

VIEWPORT_OPEN = '<div class="slide-viewport" id="viewport">'
VIEWPORT_CLOSE = '</div><!-- /slide-viewport -->'

LOGO_SVG = ('<svg class="logo-plane" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M50,150 L150,50 L50,100 L80,130 Z" fill="none" stroke="#0EA5E9" stroke-width="3" '
            'stroke-linecap="round" stroke-linejoin="round"/>'
            '<path d="M80,130 L150,50" stroke="#6366F1" stroke-width="2" stroke-dasharray="4,4"/>'
            '<circle cx="150" cy="50" r="4" fill="#10B981"/></svg>')

# Charts collected during slide rendering: { slide_id: [chart_spec, ...] }
_CHARTS = {}
_CUR_SLIDE_ID = None


# ----------------------------------------------------------------------------
# Component renderers — emit HTML that matches the gold-standard CSS classes.
# Spec authors supply trusted inline HTML (so light markup like <strong>/<br>
# is allowed inside text fields).
# ----------------------------------------------------------------------------
def _hdr(title):
    return ('<div class="slide-header">'
            f'<a href="https://www.impactmojo.in/101-courses/" class="logo-mark" target="_blank">{LOGO_SVG}'
            '<span class="logo-wordmark">ImpactMojo</span></a>'
            f'<span class="header-center">{title}</span>'
            '<span class="header-url">www.impactmojo.in</span></div>')


def _ftr(num):
    return ('<div class="slide-footer">'
            '<span class="footer-left">CC BY-NC-ND 4.0 &middot; ImpactMojo 101 Series</span>'
            f'<span class="slide-number">{num:02d}</span>'
            '<span class="footer-right">www.impactmojo.in</span></div>')


def render_blocks(blocks):
    return "\n".join(render_block(b) for b in blocks)


def render_block(b):
    t = b["t"]
    if t == "body":
        cls = (" " + b["cls"]) if b.get("cls") else ""
        return f'<div class="slide-body{cls}">{b["html"]}</div>'
    if t == "label":
        return f'<div class="section-label">{b["text"]}</div>'
    if t == "title":  # inline heading inside content
        size = b.get("size", "md")
        style = f' style="{b["style"]}"' if b.get("style") else ""
        return f'<div class="slide-title {size}"{style}>{b["html"]}</div>'
    if t == "bullets":
        color = b.get("color", "")
        sm = " sm" if b.get("sm") else ""
        items = "".join(f"<li>{i}</li>" for i in b["items"])
        return f'<ul class="bullet-list {color}{sm}">{items}</ul>'
    if t == "stats":
        cols = b.get("cols", len(b["cards"]))
        cards = ""
        for c in b["cards"]:
            color = (" " + c["color"]) if c.get("color") else ""
            src = f'<div class="stat-source">{c["source"]}</div>' if c.get("source") else ""
            cards += (f'<div class="stat-card{color}"><div class="stat-number">{c["num"]}</div>'
                      f'<div class="stat-label">{c["label"]}</div>{src}</div>')
        return f'<div class="stat-grid c{cols}">{cards}</div>'
    if t == "twocol":
        ratio = b.get("ratio", "half")
        left = render_blocks(b["left"])
        right = render_blocks(b["right"])
        return f'<div class="two-col {ratio}"><div>{left}</div><div>{right}</div></div>'
    if t == "panel":
        color = (" " + b["color"]) if b.get("color") else ""
        title = f'<div class="col-panel-title">{b["title"]}</div>' if b.get("title") else ""
        inner = b["html"] if "html" in b else render_blocks(b.get("blocks", []))
        return f'<div class="col-panel{color}">{title}{inner}</div>'
    if t == "hbox":
        color = (" " + b["color"]) if b.get("color") else ""
        return f'<div class="hbox{color}"><div class="hbox-text">{b["html"]}</div></div>'
    if t == "term":
        return f'<div class="term-box"><div class="term-word">{b["word"]}</div><div class="term-def">{b["def"]}</div></div>'
    if t == "quote":
        attr = f'<div class="quote-attr">{b["attr"]}</div>' if b.get("attr") else ""
        return f'<div class="quote-block"><div class="quote-text">{b["text"]}</div>{attr}</div>'
    if t == "table":
        head = "".join(f"<th>{h}</th>" for h in b["head"])
        rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in b["rows"])
        return f'<table class="ctable"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>'
    if t == "flow":
        steps = ""
        n = len(b["steps"])
        for i, s in enumerate(b["steps"]):
            steps += f'<div class="flow-step"><div class="flow-num">{i + 1:02d}</div><div class="flow-label">{s}</div></div>'
            if i < n - 1:
                steps += '<div class="flow-arrow">&rarr;</div>'
        return f'<div class="flow">{steps}</div>'
    if t == "darkcard":
        return (f'<div class="dark-card"><div class="dark-card-label">{b.get("label", "")}</div>'
                f'<div class="dark-card-title">{b.get("title", "")}</div>'
                f'<div class="dark-card-body">{b.get("body", "")}</div></div>')
    if t == "chart":
        _CHARTS.setdefault(_CUR_SLIDE_ID, []).append(b)
        title = f'<div class="chart-title">{b["title"]}</div>' if b.get("title") else ""
        src = f'<div class="chart-source">{b["source"]}</div>' if b.get("source") else ""
        return f'<div class="chart-wrap">{title}<canvas id="{b["canvas"]}"></canvas>{src}</div>'
    if t == "raw":
        return b["html"]
    raise ValueError(f"Unknown block type: {t}")


# ----------------------------------------------------------------------------
# Slide renderers
# ----------------------------------------------------------------------------
def render_slide(s, num, total, deck_title):
    global _CUR_SLIDE_ID
    sid = f"s{num}"
    _CUR_SLIDE_ID = sid
    active = " active" if num == 1 else ""
    typ = s.get("type", "content")

    if typ == "title":
        tags = "".join(f'<span class="title-tag">{tg}</span>' for tg in s.get("tags", []))
        body = (
            '<div class="title-screen"><div class="title-bg"></div><div class="title-bar"></div>'
            '<div class="title-content">'
            '<div class="title-series">ImpactMojo 101 Series &middot; Free Forever</div>'
            f'<div class="title-main">{s["main"]}</div>'
            f'<div class="title-sub">{s["sub"]}</div>'
            f'<div class="title-tags">{tags}</div></div>'
            '<div class="title-geo"><svg viewBox="0 0 300 620" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%">'
            '<defs><pattern id="hex" x="0" y="0" width="40" height="46" patternUnits="userSpaceOnUse">'
            '<polygon points="20,2 38,12 38,34 20,44 2,34 2,12" fill="none" stroke="white" stroke-width="1"/></pattern></defs>'
            '<rect width="300" height="620" fill="url(#hex)"/></svg></div></div>'
        )
        return f'<div class="slide{active}" id="{sid}">{_hdr(deck_title)}{body}{_ftr(num)}</div>'

    if typ == "toc":
        items = ""
        for i, it in enumerate(s["items"]):
            items += (f'<div class="toc-item"><div class="toc-num">{i + 1:02d}</div>'
                      f'<div class="toc-name">{it["name"]}</div>'
                      f'<div class="toc-slides">{it["slides"]}</div></div>')
        content = (f'<div class="slide-content"><div class="section-label">{s.get("label", "Agenda")}</div>'
                   f'<div class="slide-title md" style="margin-bottom:8px">{s.get("title", "What We Cover")}</div>'
                   f'<div class="toc-grid">{items}</div></div>')
        return f'<div class="slide{active}" id="{sid}">{_hdr(deck_title)}{content}{_ftr(num)}</div>'

    if typ == "divider":
        body = (f'<div class="section-divider"><div class="div-num">{s["num"]}</div>'
                f'<div class="div-label">{s.get("label", "")}</div>'
                f'<div class="div-title">{s["title"]}</div><div class="div-accent"></div></div>')
        return f'<div class="slide{active}" id="{sid}">{_hdr(deck_title)}{body}{_ftr(num)}</div>'

    if typ == "end":
        ctas = ""
        for i, c in enumerate(s.get("ctas", [])):
            kind = ["end-btn-primary", "end-btn-secondary", "end-btn-tertiary"][min(i, 2)]
            ctas += f'<a class="end-btn {kind}" href="{c["href"]}">{c["label"]}</a>'
        meta = '<span class="end-meta-divider">&middot;</span>'.join(
            f'<span>{m}</span>' for m in s.get("meta", ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]))
        body = ('<div class="end-screen"><div class="end-bar"></div><div class="end-pattern"></div>'
                '<div class="end-glow"></div><div class="end-content">'
                f'<div class="end-eyebrow">{s.get("eyebrow", "Thank You")}</div>'
                f'<div class="end-headline">{s["headline"]}</div>'
                f'<div class="end-byline">{s["byline"]}</div>'
                f'<div class="end-cta">{ctas}</div>'
                f'<div class="end-meta">{meta}</div></div></div>')
        return f'<div class="slide{active}" id="{sid}">{_hdr(deck_title)}{body}{_ftr(num)}</div>'

    # default: content slide
    cls = "slide"
    for mode in ("compact", "ultra-compact", "spacious"):
        if s.get(mode):
            cls += " " + mode
    parts = []
    if s.get("label"):
        parts.append(f'<div class="section-label">{s["label"]}</div>')
    if s.get("title"):
        size = s.get("titleSize", "md")
        parts.append(f'<div class="slide-title {size}">{s["title"]}</div>')
    parts.append(render_blocks(s.get("blocks", [])))
    content = f'<div class="slide-content">{"".join(parts)}</div>'
    return f'<div class="{cls}{active}" id="{sid}">{_hdr(deck_title)}{content}{_ftr(num)}</div>'


# ----------------------------------------------------------------------------
# Chart code generation
# ----------------------------------------------------------------------------
def _js_value(v):
    """Serialise chart data/options. Raw JS strings are passed through via a
    {"__js__": "..."} wrapper; everything else is JSON."""
    if isinstance(v, dict) and "__js__" in v:
        return v["__js__"]
    return json.dumps(v, ensure_ascii=False)


def build_chartjs_body():
    lines = []
    for sid, charts in _CHARTS.items():
        lines.append(f"  if (id === '{sid}') {{")
        for c in charts:
            if c.get("lib") == "echarts":
                continue  # handled separately
            data = _js_value(c["data"]) if "data" in c else "{}"
            if "options" in c:
                opts = _js_value(c["options"])
            else:
                opts = "{}"
            lines.append(f"    mk('{c['canvas']}', {json.dumps(c['type'])}, {data}, {opts});")
        lines.append("  }")
    return "\n".join(lines)


def build_echarts_body():
    blocks = []
    for sid, charts in _CHARTS.items():
        for c in charts:
            if c.get("lib") != "echarts":
                continue
            blocks.append(c["echarts"])  # raw JS that inits echarts on c['canvas']
    return "\n".join(blocks)


# ----------------------------------------------------------------------------
# Assembly
# ----------------------------------------------------------------------------
def load_spec(name):
    path = SPECS_DIR / f"{name}.py"
    spec = importlib.util.spec_from_file_location(f"deckspec_{name}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.DECK


def build(name):
    deck = load_spec(name)
    donor = DONOR.read_text(encoding="utf-8")

    head, rest = donor.split(VIEWPORT_OPEN, 1)
    _slides_region, tail = rest.split(VIEWPORT_CLOSE, 1)

    slides = deck["slides"]
    total = len(slides)
    title = deck["title"]

    # Render slides
    slide_html = []
    for i, s in enumerate(slides, start=1):
        slide_html.append(render_slide(s, i, total, title))
    slides_out = "\n\n".join(slide_html)

    # --- HEAD: swap SEO/title strings ---
    desc = deck["description"]
    slug = deck["slug"]
    head = head.replace("Development Economics 101 | ImpactMojo", f"{title} | ImpactMojo")
    head = head.replace(
        "Development Economics 101 — free development education from ImpactMojo. "
        "Browse courses, games, labs, and resources for practitioners across South Asia.",
        desc)
    head = head.replace("dev-economics.html", f"{slug}.html")
    # Remaining bare references (og:title / twitter:title / header none in head)
    head = head.replace(">Development Economics 101<", f">{title}<")
    head = head.replace('content="Development Economics 101"', f'content="{title}"')

    # --- TAIL: swap SLIDE_IDS, initChart body, initECharts body ---
    ids = ",".join(f"'s{i}'" for i in range(1, total + 1))
    tail = re.sub(r"const SLIDE_IDS = \[[\s\S]*?\];",
                  f"const SLIDE_IDS = [{ids}];", tail, count=1)

    chartjs_body = build_chartjs_body()
    tail = re.sub(
        r"(function initChart\(slideIdx\) \{\s*\n\s*const id = SLIDE_IDS\[slideIdx\];\s*\n\s*const mk = \(id, type, data, opts\) => \{\s*\n\s*const el = document\.getElementById\(id\);\s*\n\s*if \(!el\) return;\s*\n\s*new Chart\(el, \{ type, data, options: \{ \.\.\.CHART_DEFAULTS, \.\.\.opts \} \}\);\s*\n\s*\};\n)[\s\S]*?(\n\}\n\n\n// Theme)",
        lambda m: m.group(1) + "\n" + chartjs_body + m.group(2),
        tail, count=1)

    echarts_body = build_echarts_body()
    tail = re.sub(
        r"(const initECharts = \(\) => \{)[\s\S]*?(\n  \};\n  // Defer until DOM ready)",
        lambda m: m.group(1) + "\n" + echarts_body + m.group(2),
        tail, count=1)

    # progress text initial label
    tail = tail.replace("<span id=\"prog-text\">1 / 102</span>",
                        f"<span id=\"prog-text\">1 / {total}</span>")

    out = head + VIEWPORT_OPEN + "\n\n" + slides_out + "\n\n" + VIEWPORT_CLOSE + tail
    return out, total


def main():
    if len(sys.argv) < 2:
        print("usage: build.py <spec_module> [--check]")
        sys.exit(1)
    name = sys.argv[1]
    check = "--check" in sys.argv
    out, total = build(name)
    deck = load_spec(name)
    target = OUT_DIR / f"{deck['slug']}.html"
    if check:
        print(f"[check] {name}: {total} slides, {sum(len(v) for v in _CHARTS.values())} charts -> {target}")
        return
    target.write_text(out, encoding="utf-8")
    print(f"[built] {deck['slug']}.html — {total} slides, "
          f"{sum(len(v) for v in _CHARTS.values())} charts, {len(out)//1024}KB")


if __name__ == "__main__":
    main()
