#!/usr/bin/env python3
"""Guard the readable-ink contract behind the Fundamentals diagrams.

Why this exists
---------------
The four diagrams paint text directly onto a coloured shape, so the ink has to
be chosen per colour at render time. That choice has now been got wrong twice,
the same way both times: a fixed luminance cutoff.

  * cube.js picked white on #d97706 (3.19:1) because the cutoff sat at 0.32.
  * fundamentals-wheel.js kept a 0.42 cutoff and put white on all twelve
    outer-ring fills, which are the base mixed 42% with white and land just
    under it. Every rim label on the wheel read at 2.3-3.2:1, on desktop, in
    the default theme.

A cutoff cannot be right: it approximates a comparison instead of making it.
Comparing the two candidate inks and keeping the better one is self-correcting
for any colour, so this script checks both halves of that:

  1. every colour a diagram paints text on has an ink that clears 4.5:1, and
  2. each diagram actually picks its ink by comparing the two ratios, rather
     than by testing luminance against a constant.

Check 2 matters because check 1 alone passes even when the code picks the
worse of the two inks -- which is exactly what shipped.

Usage
-----
    python3 scripts/check-diagram-contrast.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (data file, renderer, the dark ink that renderer pairs against white)
DIAGRAMS = [
    ("js/cube-data.js", "js/cube.js", "#1a1420"),
    ("js/ladder-data.js", "js/ladder.js", "#1a1420"),
    ("js/whocounts-data.js", "js/whocounts.js", "#1a1420"),
    ("js/fundamentals-data.js", "js/fundamentals-wheel.js", "#241a20"),
    ("js/capabilities-data.js", "js/capabilities.js", "#241a20"),
    ("js/gender-needs-data.js", "js/gender-needs.js", "#241a20"),
]

# The wheel does not paint on the base colour: each ring is a mix of it.
# Mirrors ringFill() in js/fundamentals-wheel.js.
RING_MIX = {"power": ("#000000", 0.30), "middle": None, "margin": ("#ffffff", 0.42)}

# Face titles sit on the cube panel, not on a slice, so they are picked by hand
# in css/fundamentals.css. Both themes have to clear the bar.
FACE_TITLES = [
    ("light", "#fbf8f3", ["#6d28d9", "#115e59", "#92400e"]),
    ("dark", "#1b2333", ["#c4b5fd", "#5eead4", "#fbbf24"]),
]

# The gender-needs quadrant labels print on a 7% wash of their own colour over
# the page ground, not on a solid fill, so the fill's own ink chooser does not
# apply. Written out as (theme, page ground, quadrant colour, label ink), and
# the ground each label really sits on is computed as the wash.
#
# This entry exists because the first version inherited the quadrant colour as
# the label ink: all four failed AA in dark and two in light, on a page whose
# whole subject is checking both themes.
QUAD_WASH = 0.07
QUAD_LABELS = [
    ("light", "#f7fafc", [("#0369a1", "#075985"), ("#6d28d9", "#5b21b6"),
                          ("#15803d", "#166534"), ("#b45309", "#92400e")]),
    ("dark", "#141a26", [("#0369a1", "#7dd3fc"), ("#6d28d9", "#c4b5fd"),
                         ("#15803d", "#6ee7b7"), ("#b45309", "#fcd34d")]),
]

AA_NORMAL = 4.5

# The shape check 2 looks for, e.g.
#   return ratio("#1a1420", hex) > ratio("#ffffff", hex) ? "#1a1420" : "#ffffff";
PICKS_BY_RATIO = re.compile(
    r'return\s+(\w+)\("#[0-9a-fA-F]{6}",\s*hex\)\s*>\s*\1\("#ffffff",\s*hex\)'
)
# The shape it must NOT have: a luminance value tested against a constant.
PICKS_BY_CUTOFF = re.compile(r'return\s+L\s*[<>]=?\s*0?\.\d+\s*\?')


def rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def hexa(c):
    return "#%02x%02x%02x" % tuple(int(round(max(0, min(255, v)))) for v in c)


def mix(a, b, t):
    A, B = rgb(a), rgb(b)
    return hexa([A[i] + (B[i] - A[i]) * t for i in range(3)])


def luminance(h):
    out = []
    for v in rgb(h):
        v /= 255
        out.append(v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def contrast(a, b):
    x, y = luminance(a), luminance(b)
    hi, lo = max(x, y), min(x, y)
    return (hi + 0.05) / (lo + 0.05)


def colours_in(path):
    src = (ROOT / path).read_text(encoding="utf-8")
    return sorted(set(re.findall(r'color:\s*"(#[0-9a-fA-F]{6})"', src)))


def main():
    problems = []

    for data, renderer, dark_ink in DIAGRAMS:
        for f in (data, renderer):
            if not (ROOT / f).is_file():
                problems.append("%s is missing" % f)
        if problems:
            break

        src = (ROOT / renderer).read_text(encoding="utf-8")
        if PICKS_BY_CUTOFF.search(src):
            problems.append(
                "%s picks its ink from a luminance cutoff. Compare the two "
                "candidate inks instead: whichever gives the higher contrast "
                "ratio against the fill is the right one." % renderer
            )
        elif not PICKS_BY_RATIO.search(src):
            problems.append(
                "%s has no ink chooser of the form "
                'return f("%s", hex) > f("#ffffff", hex) ? ... — so this guard '
                "cannot tell which ink it paints." % (renderer, dark_ink)
            )

        fills = []
        for base in colours_in(data):
            if "wheel" in renderer:
                for ring, m in RING_MIX.items():
                    fills.append(("%s %s" % (base, ring),
                                  base if m is None else mix(base, m[0], m[1])))
            else:
                fills.append((base, base))

        for label, fill in fills:
            best = max(contrast(dark_ink, fill), contrast("#ffffff", fill))
            if best < AA_NORMAL:
                problems.append(
                    "%s: no readable ink for %s (fill %s) — best is %.2f:1, "
                    "needs %.1f:1. Darken or lighten the colour."
                    % (data, label, fill, best, AA_NORMAL)
                )

    for theme, panel, inks in FACE_TITLES:
        for c in inks:
            got = contrast(c, panel)
            if got < AA_NORMAL:
                problems.append(
                    "css/fundamentals.css: face title %s on the %s cube panel "
                    "(%s) is %.2f:1, needs %.1f:1."
                    % (c, theme, panel, got, AA_NORMAL)
                )

    for theme, ground, pairs in QUAD_LABELS:
        for base, ink in pairs:
            wash = mix(base, ground, 1 - QUAD_WASH)
            got = contrast(ink, wash)
            if got < AA_NORMAL:
                problems.append(
                    "gender-needs quadrant label %s on its %s wash (%s) is "
                    "%.2f:1, below %.1f" % (ink, theme, wash, got, AA_NORMAL)
                )

    if problems:
        print("FAIL - diagram text would fall below WCAG AA:")
        for p in problems:
            print("   ", p)
        return 1

    checked = sum(len(colours_in(d)) * (3 if "wheel" in r else 1)
                  for d, r, _ in DIAGRAMS)
    print("PASS - %d diagram fills have a readable ink, and all %d renderers "
          "pick it by contrast ratio." % (checked, len(DIAGRAMS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
