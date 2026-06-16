#!/usr/bin/env python3
"""Glossary-enforcement detector for the i18n page dictionaries.

For every string whose ENGLISH key contains a protected term (a keep-verbatim
brand/software/acronym/journal/programme, an author surname, or a stat badge
like 8M+), check that the term survives VERBATIM in the translated value. If it
doesn't, the machine pass probably translated or dropped it — flag it.

Deterministic and exhaustive (not sampled), unlike the review agents. Prints
candidates per language; review and fix the real ones.
"""
import json, os, glob, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G = json.load(open(os.path.join(ROOT, "data", "i18n-glossary.json"), encoding="utf-8"))

kv = G["keep_verbatim"]
TERMS = (kv["brands_products"] + kv["software_tools"] + kv["acronyms"] +
         kv["journals"] + kv["programmes"] + G["authors_keep_transliterated"]["names"])
# drop terms too short/ambiguous to detect reliably as substrings
TERMS = sorted({t for t in TERMS if len(t) >= 3 and t not in
                ("AI", "RISE", "SEE", "ODI", "Sen", "GST", "PIL")}, key=len, reverse=True)
BADGE = re.compile(r"\b\d+(?:\.\d+)?[MK]\+?")


def tok_in_key(term, key):
    return re.search(r"(?<![A-Za-z])" + re.escape(term) + r"(?![A-Za-z])", key) is not None


def main():
    for lang in ["hi", "ta", "bn", "mr"]:
        flagged = []
        for f in sorted(glob.glob(os.path.join(ROOT, "i18n", "pages", lang, "*.json"))):
            d = json.load(open(f, encoding="utf-8"))
            for k, v in d.items():
                if not isinstance(v, str):
                    continue
                for t in TERMS:
                    if tok_in_key(t, k) and t not in v:
                        flagged.append((os.path.basename(f), t, k[:32], v[:46]))
                        break
                else:
                    for m in BADGE.findall(k):
                        if m not in v:
                            flagged.append((os.path.basename(f), m, k[:32], v[:46]))
                            break
        print(f"\n===== {lang}: {len(flagged)} candidate protected-term issues =====")
        for fn, t, k, v in flagged[:40]:
            print(f"  [{t}] {fn} | {k!r} -> {v!r}")


if __name__ == "__main__":
    main()
