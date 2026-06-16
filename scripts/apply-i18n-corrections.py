#!/usr/bin/env python3
"""Apply reviewed translation corrections to the per-page i18n dictionaries.

Reads scripts/i18n-corrections.json — {lang: [{"en": <source>, "fix": <correct>}]}
— curated from a per-language native-speaker review pass. Each correction is
applied by EXACT English-source key across every page file for that language,
so a single entry cascades to all course pages that share the string, and a
correction never depends on the (broken) current value.

Reports, per language: how many corrections matched at least one key, how many
strings were rewritten, and any corrections whose `en` matched no key (so they
can be handled as substrings or dropped). Idempotent.
"""
import json, os, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def variants(en):
    """Key may be stored with or without HTML-entity encoding."""
    out = {en, html.escape(en), html.unescape(en),
           en.replace("&", "&amp;"), en.replace("&amp;", "&")}
    return {v for v in out if v}


def main():
    corr = json.load(open(os.path.join(ROOT, "scripts", "i18n-corrections.json"),
                           encoding="utf-8"))
    for lang, items in corr.items():
        files = sorted(glob.glob(os.path.join(ROOT, "i18n", "pages", lang, "*.json")))
        dicts = {f: json.load(open(f, encoding="utf-8")) for f in files}
        rewrites = 0
        unmatched = []
        for it in items:
            en, fix = it["en"], it["fix"]
            keys = variants(en)
            hit = False
            for f, d in dicts.items():
                for k in keys:
                    if k in d and d[k] != fix:
                        d[k] = fix; rewrites += 1; hit = True
                    elif k in d:
                        hit = True  # already correct
            if not hit:
                unmatched.append(en)
        for f, d in dicts.items():
            with open(f, "w", encoding="utf-8") as fh:
                json.dump(d, fh, ensure_ascii=False, separators=(",", ":"))
        print(f"{lang}: {len(items)} corrections, {rewrites} strings rewritten, "
              f"{len(unmatched)} unmatched")
        for u in unmatched:
            print(f"    UNMATCHED: {u!r}")


if __name__ == "__main__":
    main()
