#!/usr/bin/env python3
"""Pass 8: clear the residuals the i18n-quality guard surfaced.

1. Hindi brand leftovers: इम्पैक्टमोज़… / इम्पाक्टमोज़… ("ImpactMojo Labs",
   "Why We Built ImpactMojo") -> ImpactMojo.
2. Cross-script corruption: drop any value containing letters from a foreign
   Indic script (incl. Malayalam, which the first cleanup pass never scanned,
   and Devanagari/Bengali/Tamil cross-contamination) -> clean English fallback.
   Shared Indic punctuation (danda ।) is excluded.
3. Strip runs of zero-width spaces (U+200B) — invisible cruft from the machine
   pass. (ZWNJ/ZWJ, which Indic scripts use legitimately, are left alone.)
"""
import json, os, glob, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# "इम्पैक्ट…"/"इम्पाक्ट…" (impact transliterated) only ever appears as the
# brand; match the prefix + the rest of the token to dodge nukta-encoding
# variants in "मोज़".
HI_BRAND_RE = re.compile(r"इम्प[ैा]क्ट\S*")

DEVANAGARI = (0x900, 0x97F); BENGALI = (0x980, 0x9FF); TAMIL = (0xB80, 0xBFF)
OTHER = [(0xA00, 0xA7F), (0xA80, 0xAFF), (0xB00, 0xB7F),
         (0xC00, 0xC7F), (0xC80, 0xCFF), (0xD00, 0xD7F)]
OWN = {"hi": DEVANAGARI, "mr": DEVANAGARI, "bn": BENGALI, "ta": TAMIL}
SHARED = {0x964, 0x965, 0x970}


def foreign(lang, v):
    own = OWN[lang]
    blocks = [b for b in [DEVANAGARI, BENGALI, TAMIL] + OTHER if b != own]
    return any(ord(c) not in SHARED and any(lo <= ord(c) <= hi for lo, hi in blocks)
               for c in v)


def main():
    brand_fixed = dropped = zwsp = 0
    for lang in ["hi", "ta", "bn", "mr"]:
        for path in sorted(glob.glob(os.path.join(ROOT, "i18n", "pages", lang, "*.json"))):
            d = json.load(open(path, encoding="utf-8"))
            changed = False
            for k in list(d.keys()):
                v = d[k]
                if not isinstance(v, str):
                    continue
                if lang == "hi" and HI_BRAND_RE.search(v):
                    nv = HI_BRAND_RE.sub("ImpactMojo", v)
                    if nv != v:
                        d[k] = v = nv; brand_fixed += 1; changed = True
                if "​" in v:
                    nv = v.replace("​", "")
                    if nv != v:
                        d[k] = v = nv; zwsp += 1; changed = True
                if foreign(lang, v):
                    del d[k]; dropped += 1; changed = True
            if changed:
                json.dump(d, open(path, "w", encoding="utf-8"),
                          ensure_ascii=False, separators=(",", ":"))
    print(f"brand leftovers fixed: {brand_fixed}")
    print(f"cross-script entries dropped: {dropped}")
    print(f"zero-width-space runs stripped: {zwsp}")


if __name__ == "__main__":
    main()
