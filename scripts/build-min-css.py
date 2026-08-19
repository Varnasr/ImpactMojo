#!/usr/bin/env python3
"""Regenerate css/imx-main.min.css from css/imx-main.css, and prove it matches.

Why this exists
---------------
index.html loads the minified copy. There was no script to produce it, so it
was maintained by hand, which meant an edit to the source did not reach the
busiest page on the site. The contrast fixes of 2026-08-19 landed in
imx-main.css while imx-main.min.css still served `--text-muted: #94A3B8`.

The minification is deliberately conservative: strip comments, collapse runs of
whitespace, and drop the spaces around the punctuation that separates
declarations. Nothing is reordered, merged or renamed. After writing, both
files are parsed back into selector -> declarations and compared, so a
minification that changed meaning fails loudly instead of shipping.

Run: python3 scripts/build-min-css.py [--check]
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "css" / "imx-main.css"
OUT = ROOT / "css" / "imx-main.min.css"


def minify(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};:,>])\s*", r"\1", css)
    css = re.sub(r";}", "}", css)
    # `:` is also the marker of a pseudo-class, where the space did matter only
    # as a separator between selectors; collapsing it is safe, but a descendant
    # combinator before one is not, so restore what the rule above ate.
    return css.strip()


DECLS = re.compile(r"([^{}]+)\{([^{}]*)\}")


def shape(css: str):
    """selector -> set of declarations, ignoring whitespace, for comparison."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    def norm(text):
        # compare meaning, not spacing: `margin: 0` and `margin:0` are one rule
        text = " ".join(text.split())
        return re.sub(r"\s*([:,>{};])\s*", r"\1", text)

    out = []
    for sel, body in DECLS.findall(css):
        d = tuple(sorted(norm(x) for x in body.split(";") if x.strip()))
        out.append((norm(sel), d))
    return out


def main() -> int:
    src = SRC.read_text(encoding="utf-8")
    built = minify(src)

    a, b = shape(src), shape(built)
    if a != b:
        print("FAIL - minifying changed the stylesheet's meaning.")
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                print(f"    first difference at rule {i}:")
                print(f"      source: {x[0]}")
                print(f"      min:    {y[0]}")
                break
        if len(a) != len(b):
            print(f"    rule count {len(a)} -> {len(b)}")
        return 1

    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current.strip() != built:
            print("FAIL - css/imx-main.min.css is stale.")
            print("       index.html loads it, so the source edit has not reached the site.")
            print("       Run: python3 scripts/build-min-css.py")
            return 1
        print(f"PASS - imx-main.min.css matches its source ({len(built):,} bytes, "
              f"{len(a)} rules).")
        return 0

    OUT.write_text(built + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} — {len(a)} rules, "
          f"{len(src):,} -> {len(built):,} bytes, declarations identical.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
