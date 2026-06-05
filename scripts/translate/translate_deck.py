#!/usr/bin/env python3
"""
Translate an ImpactMojo native 101 deck into an Indian language via Sarvam
(Mayura). Preserves all HTML structure, CSS, JS and charts; translates only
human-readable text nodes. Injects the right Noto script font, sets lang, and
adds a language switcher. Writes 101-courses/<lang>/<slug>.html.

Usage:
  . .claude/.env.keys
  python3 scripts/translate/translate_deck.py <slug> <lang>     # lang: hi|ta|bn|mr
  python3 scripts/translate/translate_deck.py data-lit hi

A persistent per-language cache (scripts/translate/cache/<lang>.json) is a
translation memory so repeated strings (and re-runs) cost no API calls.
"""
import os, sys, json, time, re, html
from pathlib import Path
import urllib.request
from bs4 import BeautifulSoup, NavigableString, Comment

ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = Path(__file__).resolve().parent / "cache"
CACHE_DIR.mkdir(exist_ok=True)
API = "https://api.sarvam.ai/translate"
KEY = os.environ.get("SARVAM_API_KEY", "")

LANG = {  # code -> (sarvam code, English name, native name, Noto font family, font css url)
    "hi": ("hi-IN", "Hindi", "हिन्दी", "Noto Sans Devanagari", "Noto+Sans+Devanagari:wght@400;500;700;800"),
    "mr": ("mr-IN", "Marathi", "मराठी", "Noto Sans Devanagari", "Noto+Sans+Devanagari:wght@400;500;700;800"),
    "ta": ("ta-IN", "Tamil", "தமிழ்", "Noto Sans Tamil", "Noto+Sans+Tamil:wght@400;500;700;800"),
    "bn": ("bn-IN", "Bengali", "বাংলা", "Noto Sans Bengali", "Noto+Sans+Bengali:wght@400;500;700;800"),
}
SKIP_PARENTS = {"script", "style", "svg", "path", "symbol", "defs", "canvas", "noscript"}
# Don't translate: pure numbers/symbols, URLs, the wordmark, mono code-ish bits.
SKIP_RE = re.compile(r"^[\s\d\W]*$")
URL_RE = re.compile(r"(https?://|www\.|\.html|\.in\b|@)", re.I)
KEEP_VERBATIM = {"ImpactMojo", "CC BY-NC-ND 4.0", "www.impactmojo.in", "Chart.js", "101"}


def load_cache(lang):
    p = CACHE_DIR / f"{lang}.json"
    return json.loads(p.read_text()) if p.exists() else {}


def save_cache(lang, cache):
    (CACHE_DIR / f"{lang}.json").write_text(json.dumps(cache, ensure_ascii=False, indent=0))


def translate(text, sarvam_code, cache):
    key = text.strip()
    if key in cache:
        return cache[key]
    body = json.dumps({"input": key, "source_language_code": "en-IN",
                       "target_language_code": sarvam_code, "model": "mayura:v1"}).encode()
    req = urllib.request.Request(API, data=body, method="POST", headers={
        "api-subscription-key": KEY, "Content-Type": "application/json"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                out = json.loads(r.read())
                t = out.get("translated_text", key)
                cache[key] = t
                return t
        except Exception as e:
            wait = 2 ** attempt
            code = getattr(e, "code", None)
            if code == 429 or code is None:
                time.sleep(wait); continue
            if code and 400 <= code < 500 and code != 429:
                cache[key] = key  # don't retry hard client errors; keep original
                return key
            time.sleep(wait)
    cache[key] = key
    return key


def translatable(node):
    if not isinstance(node, NavigableString) or isinstance(node, Comment):
        return False
    s = str(node).strip()
    if not s or SKIP_RE.match(s) or URL_RE.search(s) or s in KEEP_VERBATIM:
        return False
    for p in node.parents:
        if p.name in SKIP_PARENTS:
            return False
    return any(c.isalpha() for c in s)


def lang_switcher_html(slug, cur):
    links = ['<a href="/101-courses/%s.html"%s>EN</a>' % (slug, ' class="active"' if cur == "en" else "")]
    for code, (_, _, native, _, _) in LANG.items():
        active = ' class="active"' if cur == code else ""
        links.append('<a href="/101-courses/%s/%s.html"%s>%s</a>' % (code, slug, active, native))
    return ('<div id="lang-bar" style="position:fixed;top:58px;left:14px;z-index:2000;display:flex;gap:4px;'
            'background:rgba(0,0,0,0.6);backdrop-filter:blur(8px);border-radius:20px;padding:4px 6px;'
            'font-family:sans-serif;font-size:11px">'
            + "".join(l.replace("<a ", '<a style="color:rgba(255,255,255,0.7);text-decoration:none;padding:3px 8px;border-radius:12px"')
                      for l in links) + "</div>")


def build(slug, lang):
    sarvam_code, en_name, native, font_fam, font_url = LANG[lang]
    src = ROOT / "101-courses" / f"{slug}.html"
    html_text = src.read_text(encoding="utf-8")
    soup = BeautifulSoup(html_text, "html.parser")
    cache = load_cache(lang)

    nodes = [n for n in soup.find_all(string=True) if translatable(n)]
    uniq = []
    seen = set()
    for n in nodes:
        s = str(n).strip()
        if s not in seen:
            seen.add(s); uniq.append(s)
    n_new = sum(1 for s in uniq if s not in cache)
    print(f"  {slug}/{lang}: {len(nodes)} text nodes, {len(uniq)} unique, {n_new} need API")
    for i, s in enumerate(uniq):
        translate(s, sarvam_code, cache)
        if i % 25 == 0:
            save_cache(lang, cache)
            time.sleep(0.2)
    save_cache(lang, cache)

    # replace text nodes preserving leading/trailing whitespace
    for n in nodes:
        raw = str(n)
        s = raw.strip()
        t = cache.get(s, s)
        lead = raw[:len(raw) - len(raw.lstrip())]
        trail = raw[len(raw.rstrip()):]
        n.replace_with(NavigableString(lead + t + trail))

    out = str(soup)
    # lang attribute
    out = out.replace('<html lang="en">', f'<html lang="{lang}">', 1)
    # inject Noto font + apply to deck + language switcher, just before </head>
    inject = (f'<link href="https://fonts.googleapis.com/css2?family={font_url}&display=swap" rel="stylesheet">'
              f'<style>:root{{--font-head:\'{font_fam}\',\'Inter\',sans-serif;'
              f'--font-body:\'{font_fam}\',\'Amaranth\',sans-serif}}'
              f'.slide-title,.slide-body,.bullet-list li,.div-title,.title-main,.title-sub,'
              f'.stat-label,.col-panel-title,.hbox-text,.term-word,.term-def,.quote-text,'
              f'.ctable td,.ctable th,.toc-name,.section-label,.chart-title{{font-family:\'{font_fam}\',sans-serif}}</style>')
    out = out.replace("</head>", inject + "\n</head>", 1)
    # language switcher
    out = out.replace('<div id="deck">', lang_switcher_html(slug, lang) + '\n<div id="deck">', 1)

    target_dir = ROOT / "101-courses" / lang
    target_dir.mkdir(exist_ok=True)
    (target_dir / f"{slug}.html").write_text(out, encoding="utf-8")
    print(f"  -> wrote 101-courses/{lang}/{slug}.html ({len(out)//1024}KB)")


if __name__ == "__main__":
    if not KEY:
        print("SARVAM_API_KEY not set — run: . .claude/.env.keys"); sys.exit(1)
    if len(sys.argv) < 3:
        print("usage: translate_deck.py <slug> <lang>"); sys.exit(1)
    build(sys.argv[1], sys.argv[2])
