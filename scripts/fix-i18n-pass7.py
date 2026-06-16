#!/usr/bin/env python3
"""Pass 7: strip the Tamil "உரை:" ("Text:") placeholder artifact.

Round-3 review found Tamil has the same placeholder-artifact class already
handled for Hindi (पाठ:), Marathi (मजकूर:) and Bengali (টেক্সট:) — the machine
pass prepended "உரை:" / "உரைநிலை" to many strings, sometimes replacing the
real opening words. Strip the leading artifact; if the value was only the
placeholder, leave it empty so the runtime falls back to clean English.
"""
import json, os, glob, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAT = re.compile(r"^\s*உரை(?:நிலை)?\s*[:：]?\s*")


def main():
    total = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "i18n", "pages", "ta", "*.json"))):
        d = json.load(open(path, encoding="utf-8"))
        ch = 0
        for k, v in list(d.items()):
            if isinstance(v, str) and PAT.match(v):
                nv = PAT.sub("", v)
                if nv != v:
                    d[k] = nv
                    ch += 1
        if ch:
            json.dump(d, open(path, "w", encoding="utf-8"),
                      ensure_ascii=False, separators=(",", ":"))
            total += ch
            print(f"  ta/{os.path.basename(path):42s} {ch:3d}")
    print(f"\nTotal pass-7 (ta உரை: artifact) strips: {total}")


if __name__ == "__main__":
    main()
