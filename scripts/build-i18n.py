#!/usr/bin/env python3
"""Build the shipped static translation dictionaries for ImpactMojo.

Layers (later wins):
  1. i18n/machine/<lang>.json   — optional bulk machine pass (not required)
  2. i18n/overrides/<lang>.json — hand-authored / reviewed translations

Output:
  i18n/<lang>.json  — flat { "English source": "translation" } map that the
  client (js/translate-sarvam.js) fetches and applies. Source-text keyed, so a
  string is translated once and reused everywhere it appears.

Usage:
  python3 scripts/build-i18n.py            # merge layers -> shipped dicts
  python3 scripts/build-i18n.py --report   # also print site-wide coverage
"""
import json, os, sys, glob, re
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["hi", "ta", "bn", "mr", "te"]


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def build():
    for lang in LANGS:
        machine = load(os.path.join(ROOT, "i18n", "machine", lang + ".json"))
        override = load(os.path.join(ROOT, "i18n", "overrides", lang + ".json"))
        merged = {}
        merged.update(machine)
        merged.update(override)  # overrides win
        out = os.path.join(ROOT, "i18n", lang + ".json")
        with open(out, "w", encoding="utf-8") as f:
            json.dump(merged, f, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        print(f"built i18n/{lang}.json  ({len(merged)} strings; "
              f"{len(machine)} machine + {len(override)} override)")


# --- coverage report (mirrors the client's isTranslatable / skip rules) -------
SKIP_TAGS = {"script", "style", "noscript", "svg", "code", "pre", "kbd", "samp",
             "canvas", "textarea", "option"}
KEEP = {"ImpactMojo", "ImpactLex", "VaniScribe", "Mojini", "PinPoint Ventures",
        "DevDiscourses", "Dataverse", "Bulbul", "Mayura", "Saaras"}


class Ex(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.out = []

    def handle_starttag(self, t, a):
        if t in SKIP_TAGS:
            self.skip += 1
        d = dict(a)
        if d.get("data-no-translate") is not None or d.get("translate") == "no":
            self.skip += 1

    def handle_endtag(self, t):
        if t in SKIP_TAGS and self.skip > 0:
            self.skip -= 1

    def handle_data(self, d):
        if self.skip > 0:
            return
        x = d.strip()
        if len(x) < 2 or x in KEEP or not re.search(r"[A-Za-z]", x) \
                or re.match(r"^(https?://|www\.|\S+@)", x):
            return
        self.out.append(x)


def report():
    uniq = set()
    for fp in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        if "/Backups/" in fp:
            continue
        p = Ex()
        try:
            p.feed(open(fp, encoding="utf-8", errors="ignore").read())
        except Exception:
            pass
        uniq.update(p.out)
    total = len(uniq)
    print(f"\nSite-wide unique translatable strings: {total:,}")
    for lang in LANGS:
        d = load(os.path.join(ROOT, "i18n", lang + ".json"))
        covered = sum(1 for s in uniq if s in d)
        print(f"  {lang}: {len(d):,} in dict, {covered:,} on-site covered "
              f"({100*covered/total:.1f}%)")


if __name__ == "__main__":
    build()
    if "--report" in sys.argv:
        report()
