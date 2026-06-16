#!/usr/bin/env python3
"""i18n quality guard — fails CI if a machine-translation 'horror' reappears.

Deterministic, zero-false-positive regression checks across the translated
dictionaries (i18n/<lang>.json and i18n/pages/<lang>/*.json) for the four
corruption classes the 2026-06 audit eliminated:

  1. CROSS-SCRIPT LEAKAGE — a value in one language containing letters from a
     different Indic script (e.g. Odia letters inside Bengali). Legitimate
     translations never mix Indic scripts, so any occurrence is corruption.
  2. PLACEHOLDER ARTIFACTS — a value starting with the machine pass's stray
     "text:" label: पाठ: (hi) · मजकूर: (mr) · টেক্সট: (bn) · உரை: (ta).
  3. TRANSLATED BRAND NAME — "ImpactMojo" rendered in native script
     (प्रभावमोज… / इम्पॅक्टमोज… / ইম্প্যাক্টমোজ… / இம்பேக்ட்மோஜ…). The brand
     must always stay Latin.
  4. CHARACTER-RUN CORRUPTION — the same non-trivial character repeated 6+
     times (e.g. नौंंंंंं…), a signature of the garbling seen in "Module 9".

Run: python3 scripts/check-i18n-quality.py   (exit 1 on any finding)
Wired into CI (.github/workflows/ci.yml, job `i18n-quality`) on every push/PR
and a daily schedule. Pairs with check-mojibake.py and the (advisory, noisier)
check-i18n-glossary.py.
"""
import json, os, glob, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["hi", "ta", "bn", "mr"]

# Unicode block (lo, hi) per script
DEVANAGARI = (0x900, 0x97F)
BENGALI = (0x980, 0x9FF)
TAMIL = (0xB80, 0xBFF)
OTHER_INDIC = {
    "Gurmukhi": (0xA00, 0xA7F), "Gujarati": (0xA80, 0xAFF),
    "Oriya": (0xB00, 0xB7F), "Telugu": (0xC00, 0xC7F),
    "Kannada": (0xC80, 0xCFF), "Malayalam": (0xD00, 0xD7F),
}
OWN = {"hi": DEVANAGARI, "mr": DEVANAGARI, "bn": BENGALI, "ta": TAMIL}

# Shared Indic punctuation that lives in the Devanagari block but is used by
# every Indic script (danda ।, double danda ॥, abbreviation sign ॰). Excluded
# from cross-script detection so a Bengali/Tamil sentence ending in । is fine.
SHARED_INDIC = {0x964, 0x965, 0x970}

# Foreign Indic ranges per language = all Indic blocks except the language's own.
def foreign_ranges(lang):
    own = OWN[lang]
    allblocks = [DEVANAGARI, BENGALI, TAMIL] + list(OTHER_INDIC.values())
    return [b for b in allblocks if b != own]

ARTIFACT = {
    "hi": re.compile(r"^\s*पाठ\s*[:ः]"),
    "mr": re.compile(r"^\s*मजकूर\s*[:ःं]"),
    "bn": re.compile(r"^\s*টেক্সট\s*[:ঃ]"),
    "ta": re.compile(r"^\s*உரை(?:நিলை)?\s*[:：]"),
}
# native-script ImpactMojo renderings (brand must stay Latin). Specific enough
# that no legitimate word matches (e.g. Marathi मोजमाप 'measure' is NOT matched).
BRAND = re.compile(
    r"इम्पैक्ट|इम्पॅक्ट|इम्पाक्ट|प्रभाव[ःक]?मोज|"          # Devanagari
    r"ইম্প্যাক্টমোজ|ইমপ্যাক্ট\s*মোজ|প্রভাবমোজ|প্রভাবমোজ|"  # Bengali
    r"இம்பேக்ட்மோஜ|இம்பாக்ஸ்ட்மோஜ|தாக்கமோஜோ"               # Tamil
)
RUN = re.compile(r"([^\d\s.\-—–_])\1{5,}")  # same non-trivial char 6+ times


def main():
    issues = []
    files = []
    for lang in LANGS:
        files.append((lang, os.path.join(ROOT, "i18n", lang + ".json")))
        for f in glob.glob(os.path.join(ROOT, "i18n", "pages", lang, "*.json")):
            files.append((lang, f))

    for lang, path in files:
        if not os.path.exists(path):
            continue
        try:
            d = json.load(open(path, encoding="utf-8"))
        except Exception as e:
            issues.append((path, "INVALID-JSON", str(e)))
            continue
        rel = os.path.relpath(path, ROOT)
        fr = foreign_ranges(lang)
        for k, v in d.items():
            if not isinstance(v, str):
                continue
            # 1. cross-script leakage (shared Indic punctuation excluded)
            bad = [c for c in v if ord(c) not in SHARED_INDIC
                   and any(lo <= ord(c) <= hi for lo, hi in fr)]
            if bad:
                names = sorted({unicodedata.name(c, "?").split()[0] for c in bad})
                issues.append((rel, "CROSS-SCRIPT(" + ",".join(names) + ")", repr(k[:40])))
                continue
            # 2. placeholder artifact
            if ARTIFACT[lang].match(v):
                issues.append((rel, "ARTIFACT", repr(k[:40])))
                continue
            # 3. translated brand name
            if BRAND.search(v):
                issues.append((rel, "BRAND-TRANSLATED", repr(k[:40])))
                continue
            # 4. character-run corruption
            if RUN.search(v):
                issues.append((rel, "CHAR-RUN", repr(k[:40])))
                continue

    if issues:
        print(f"FAIL — {len(issues)} i18n quality issue(s):\n")
        for rel, kind, key in issues[:200]:
            print(f"  [{kind}] {rel} | {key}")
        if len(issues) > 200:
            print(f"  … and {len(issues) - 200} more")
        sys.exit(1)
    print(f"PASS — no i18n corruption found "
          f"({len(files)} dictionaries across {len(LANGS)} languages).")


if __name__ == "__main__":
    main()
