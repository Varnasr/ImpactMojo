#!/usr/bin/env python3
"""Pass 5: systematic sweeps found in round-2 review.

1. "text:" placeholder artifact the machine pass prepended (like Hindi's "पाठ:"
   handled in pass 4): Marathi "मजकूर:" / bare "मजकूर", Bengali "টেক্সট:".
   Strip the leading artifact; if the value was only the placeholder, leave it
   empty so the runtime falls back to clean English.
2. Bengali "Causal" → কারসাজি ("manipulation/trickery") throughout the causal
   inference course. Replace কারসাজি → কার্যকারণ ONLY in strings whose English
   source mentions "causal" (so the legitimate "manipulation" sense elsewhere
   is untouched).
"""
import json, os, glob, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARTIFACT = {
    "mr": re.compile(r"^\s*मजकूर[:ःं]?\s*"),
    "bn": re.compile(r"^\s*টেক্সট[:ঃ]?\s*"),
}


def main():
    total = 0
    # 1. placeholder artifacts
    for lang, pat in ARTIFACT.items():
        for path in sorted(glob.glob(os.path.join(ROOT, "i18n", "pages", lang, "*.json"))):
            d = json.load(open(path, encoding="utf-8"))
            ch = 0
            for k, v in list(d.items()):
                if isinstance(v, str) and pat.match(v):
                    nv = pat.sub("", v)
                    if nv != v:
                        d[k] = nv
                        ch += 1
            if ch:
                json.dump(d, open(path, "w", encoding="utf-8"),
                          ensure_ascii=False, separators=(",", ":"))
                total += ch
                print(f"  artifact {lang}/{os.path.basename(path):38s} {ch:3d}")

    # 2. Bengali causal -> কারসাজি, only where source mentions "causal"
    ch = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "i18n", "pages", "bn", "*.json"))):
        d = json.load(open(path, encoding="utf-8"))
        local = 0
        for k, v in list(d.items()):
            if isinstance(v, str) and "কারসাজি" in v and "causal" in k.lower():
                d[k] = v.replace("কারসাজি", "কার্যকারণ")
                local += 1
        if local:
            json.dump(d, open(path, "w", encoding="utf-8"),
                      ensure_ascii=False, separators=(",", ":"))
            ch += local
            print(f"  causal   bn/{os.path.basename(path):38s} {local:3d}")
    total += ch
    print(f"\nTotal pass-5 fixes: {total}")


if __name__ == "__main__":
    main()
