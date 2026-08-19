#!/usr/bin/env python3
"""Guard: an invisible full-screen overlay must not swallow taps.

Why this exists
---------------
blog.html, about.html and 404.html each carried this pair:

    .mobile-menu-overlay { display: none; opacity: 0; z-index: 998;
                           position: fixed; width: 100%; height: 100% }
    @media (max-width: 768px) { .mobile-menu-overlay { display: block } }

The media query turned the menu backdrop on for every phone, open menu or not.
opacity: 0 made it invisible — and an opacity-0 element still receives pointer
events, so on a phone every tap landed on a full-viewport div wired to
closeMobileMenu(). No blog post could be opened on mobile. Nothing rendered
wrong, no console error, and both accessibility audits passed: they test the
desktop DOM and never tap anything.

The rule this enforces: if an element is positioned fixed/absolute, covers
effectively the whole viewport, and is transparent via opacity: 0 in its
resting state (visibility: hidden and display: none already remove it from
hit-testing, so those are not traps), it must also declare
pointer-events: none there. Add `contrast-ignore`-style opt-out with
`tap-ok` on the rule if an overlay really is meant to catch taps while
invisible.

Run: python3 scripts/check-tap-traps.py
"""

import glob
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = ("Backups/", "node_modules/", "tests/")

RULE = re.compile(r"([^{}]+)\{([^{}]*)\}")
STYLE = re.compile(r"<style[^>]*>(.*?)</style>", re.S | re.I)


def decl(body, prop):
    m = re.search(r"(?:^|[;{\s])" + prop + r"\s*:\s*([^;]+)", body, re.I)
    return m.group(1).strip().lower() if m else None


def covers_viewport(body):
    pos = decl(body, "position")
    if pos not in ("fixed", "absolute"):
        return False
    w, h = decl(body, "width"), decl(body, "height")
    if w and h and re.match(r"100(%|vw)", w) and re.match(r"100(%|vh)", h):
        return True
    inset = all(decl(body, p) is not None for p in ("top", "left", "right", "bottom"))
    return inset or decl(body, "inset") is not None


def opacity_zero(body):
    """opacity: 0 keeps an element in hit-testing; visibility: hidden does not.

    A first version conflated the two and flagged two modals in
    bct-repository.html that rest at visibility: hidden and are correct.
    """
    o = decl(body, "opacity")
    try:
        return o is not None and float(o) == 0
    except ValueError:
        return False


def match_brace(text, i):
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return j
    return -1


def media_shown(chunk):
    """Selectors a media query switches on with display: block/flex/grid.

    Brace-matched rather than regex-bounded: the overlay rule that caused this
    sits inside a long mobile media query, and a non-greedy match to the first
    closing brace never reached it — the first version of this check passed
    with the bug reintroduced, which is worse than not having it.
    """
    out = set()
    for m in re.finditer(r"@media[^{]*\{", chunk):
        end = match_brace(chunk, m.end() - 1)
        if end == -1:
            continue
        for sel, body in RULE.findall(chunk[m.end():end]):
            if decl(body, "display") in ("block", "flex", "grid"):
                out.add(" ".join(sel.split()))
    return out


def main() -> int:
    findings = []
    files = [f for f in glob.glob("**/*.html", recursive=True) if not f.startswith(SKIP)]
    files += [f for f in glob.glob("css/*.css") if not f.endswith(".min.css")]
    checked = 0

    for f in sorted(files):
        src = Path(ROOT / f).read_text(encoding="utf-8", errors="replace")
        chunks = STYLE.findall(src) if f.endswith(".html") else [src]
        for chunk in chunks:
            chunk = re.sub(r"/\*.*?\*/", "", chunk, flags=re.S)
            shown = media_shown(chunk)
            for sel, body in RULE.findall(chunk):
                s = " ".join(sel.split())
                if "tap-ok" in sel or "tap-ok" in body:
                    continue
                if any(k in s for k in (".active", ":hover", ".open", ".is-on", ".show")):
                    continue
                if not covers_viewport(body) or not opacity_zero(body):
                    continue
                # The resting rule may say display: none while a media query
                # turns it on for phones. That combination is the bug: visible
                # to hit-testing, invisible to the eye.
                turned_on = s in shown or decl(body, "display") in ("block", "flex", "grid")
                if not turned_on:
                    continue
                if decl(body, "visibility") == "hidden":
                    continue
                checked += 1
                if decl(body, "pointer-events") == "none":
                    continue
                findings.append((f, s))

    if findings:
        print(f"FAIL - {len(findings)} invisible full-screen overlay(s) still take taps.")
        print("       Nothing looks wrong and nothing errors; the page just stops")
        print("       responding to touch underneath them.\n")
        for f, s in findings:
            print(f"    {f}")
            print(f"        {s}  — opacity 0, covers the viewport, displayed, "
                  f"no pointer-events: none")
        return 1

    print(f"PASS - all {checked} invisible full-screen overlays are inert "
          f"across {len(files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
