#!/usr/bin/env python3
"""Pass 4: strip stray machine-translation artifacts and char corruption (Hindi).

- "पाठ:" / "पाठः" ("lesson:") was prepended by the machine pass to many Hindi
  strings, sometimes replacing the real opening words entirely.
- "Module 9" -> "नौं" followed by a long run of anusvaras (corruption).

Only safe, unambiguous Hindi cleanups here. Cross-script leakage (Odia letters
inside Bengali, etc.) is corruption that needs per-string retranslation and is
reported separately, not patched blindly.
"""
import json, os, glob, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# keys whose value collapsed to just the artifact — restore real translation
EMPTY_FIX = {
    "(18 terms)": "(18 शब्द)",
    "(25 terms)": "(25 शब्द)",
    "(7 readings, 6 essential)": "(7 पठन, 6 अनिवार्य)",
}
EXACT = {
    "Module 9": "मॉड्यूल 9",
}


def main():
    changed_total = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "i18n", "pages", "hi", "*.json"))):
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        changed = 0
        for k, v in list(d.items()):
            if not isinstance(v, str):
                continue
            nv = v
            if k in EXACT:
                nv = EXACT[k]
            elif re.match(r"^\s*पाठ[:ः]", nv):
                stripped = re.sub(r"^\s*पाठ[:ः]\s*", "", nv)
                if stripped.strip():
                    nv = stripped
                elif k in EMPTY_FIX:
                    nv = EMPTY_FIX[k]
                else:
                    nv = stripped  # leave empty -> runtime falls back to English
            # collapse any pathological repeated-char run (>=5 identical) to one
            nv = re.sub(r"(.)\1{4,}", r"\1", nv)
            if nv != v:
                d[k] = nv
                changed += 1
        if changed:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False, separators=(",", ":"))
            changed_total += changed
            print(f"  hi/{os.path.basename(path):42s} {changed:3d} fixed")
    print(f"\nTotal pass-4 fixes: {changed_total}")


if __name__ == "__main__":
    main()
