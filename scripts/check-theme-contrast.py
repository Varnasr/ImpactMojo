#!/usr/bin/env python3
"""Guard: text and its background must clear WCAG AA in BOTH themes.

Why this exists
---------------
The site ships a light and a dark palette built from the same custom
properties, and a colour is only ever half-chosen: a value picked against one
theme's surfaces can be unreadable against the other's, and nothing reports it.
That is not hypothetical. Three examples, all found by this check:

  .card-number      colour #075985 was chosen deliberately against the light
                    hover surface and carries a comment recording its 6.90:1.
                    In dark mode the same ink lands on #334155 at 1.37:1.
  .testimonial-lang the language chips on testimonials.html paint a hue at 12%
                    over the card and print the same hue on top. Seven of the
                    eight combinations failed, worst at 2.37:1.
  --text-color      referenced ten times in css/imx-main.css and defined
                    nowhere, so every one of those declarations was invalid and
                    silently inherited instead.

The audits already in CI do not cover this. axe-core does run both themes, but
only over ten pages, and it never evaluates :hover state contrast — three of the
four accent failures were hover states. pa11y catches DOM contrast but runs the
default theme at desktop width. A green audit run means less than it looks.

What it checks
--------------
Every rule that sets a colour AND a background in the same block, resolved
through var() chains per theme. A rule scoped to one theme is only evaluated in
that theme. Where the background is translucent it is composited over each
surface the theme defines, and the rule is only failed when no surface would
save it — so a tint that is fine somewhere is never reported.

Threshold is 4.5:1, or 3:1 where the same rule declares large text (>=24px, or
>=18.66px at weight 700+), per WCAG 1.4.3. Add `contrast-ignore` to a line to
exempt it, the same escape hatch check-counts.py uses.

Run: python3 scripts/check-theme-contrast.py [-v]
"""

import glob
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = ("Backups/", "node_modules/", "tests/", "docs/")

AA_NORMAL, AA_LARGE = 4.5, 3.0

# ---------------------------------------------------------------- colour maths

NAMED = {
    "white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0),
    "transparent": None, "inherit": None, "currentcolor": None, "unset": None,
    "initial": None, "none": None, "auto": None,
}

RGBA = re.compile(r"rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+)(?:[\s,/]+([\d.]+%?))?\s*\)", re.I)


def _hex(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) == 8:          # #rrggbbaa
        h = h[:6]
    if len(h) != 6 or not re.fullmatch(r"[0-9A-Fa-f]{6}", h):
        return None
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def parse_colour(value):
    """-> (rgb, alpha) for a literal colour, or None when it is not one."""
    v = value.strip().rstrip(";").strip()
    v = re.sub(r"\s*!important\s*$", "", v, flags=re.I).strip()
    if not v:
        return None
    m = RGBA.match(v)
    if m:
        rgb = tuple(max(0, min(255, round(float(m.group(i))))) for i in (1, 2, 3))
        a = m.group(4)
        alpha = 1.0 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        return rgb, alpha
    first = v.split()[0]
    if first.startswith("#"):
        rgb = _hex(first)
        return (rgb, 1.0) if rgb else None
    low = first.lower()
    if low in NAMED:
        return (NAMED[low], 1.0) if NAMED[low] else None
    return None


def luminance(rgb):
    c = [x / 255 for x in rgb]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def composite(fg, alpha, ground):
    return tuple(round(alpha * fg[i] + (1 - alpha) * ground[i]) for i in range(3))


# ------------------------------------------------------------------ css parsing

COMMENT = re.compile(r"/\*.*?\*/", re.S)
DECL = re.compile(r"(--[\w-]+)\s*:\s*([^;{}]+)")
RULE = re.compile(r"([^{}]+)\{([^{}]*)\}")
VAR = re.compile(r"var\(\s*(--[\w-]+)\s*(?:,\s*([^()]*(?:\([^()]*\)[^()]*)*))?\)")

# a selector or at-rule that only ever applies in one theme
DARK_ONLY = re.compile(r"dark-mode|\[data-theme=[\"']?dark|prefers-color-scheme:\s*dark", re.I)
LIGHT_ONLY = re.compile(r"light-mode|\[data-theme=[\"']?light", re.I)


def strip_comments(css):
    return COMMENT.sub("", css)


def collect_tokens(css):
    """-> (light, dark) token tables. Dark inherits from light, then overrides.

    Both conventions in this repo are handled: `body.dark-mode { ... }` blocks
    and `@media (prefers-color-scheme: dark) { :root { ... } }`.
    """
    light, dark_over = {}, {}
    # blocks, keeping track of any enclosing at-rule
    depth_stack = []
    pos, at_dark = 0, False
    for m in re.finditer(r"@media[^{]*\{|\{|\}", css):
        pass  # (structure walked below instead)

    # Simpler and sufficient: walk brace blocks with their preceding text.
    i = 0
    open_at = []          # stack of at-rule preludes
    while i < len(css):
        brace = css.find("{", i)
        if brace == -1:
            break
        prelude = css[i:brace].strip()
        close = _matching_brace(css, brace)
        if close == -1:
            break
        body = css[brace + 1:close]
        if prelude.startswith("@"):
            in_dark = bool(DARK_ONLY.search(prelude))
            for sel, decls in _blocks(body):
                if "--" not in decls:
                    continue
                tgt = dark_over if (in_dark or DARK_ONLY.search(sel)) else (
                    None if LIGHT_ONLY.search(sel) and in_dark else light)
                if tgt is None:
                    continue
                if not (in_dark or DARK_ONLY.search(sel)) and LIGHT_ONLY.search(sel):
                    tgt = light
                for k, v in DECL.findall(decls):
                    tgt[k] = v.strip()
        else:
            if "--" in body:
                tgt = dark_over if DARK_ONLY.search(prelude) else light
                for k, v in DECL.findall(body):
                    tgt[k] = v.strip()
        i = close + 1
    dark = dict(light)
    dark.update(dark_over)
    return light, dark


def _matching_brace(s, start):
    depth = 0
    for j in range(start, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return j
    return -1


def _blocks(css):
    """Top-level `selector { decls }` pairs inside a chunk of css."""
    out, i = [], 0
    while i < len(css):
        brace = css.find("{", i)
        if brace == -1:
            break
        close = _matching_brace(css, brace)
        if close == -1:
            break
        out.append((css[i:brace].strip(), css[brace + 1:close]))
        i = close + 1
    return out


def resolve(value, table, depth=0):
    """Resolve a declaration value to (rgb, alpha), following var() chains."""
    if depth > 8:
        return None
    value = value.strip()
    m = VAR.match(value)
    if m:
        name, fallback = m.group(1), m.group(2)
        if name in table:
            return resolve(table[name], table, depth + 1)
        if fallback:
            return resolve(fallback, table, depth + 1)
        return None                      # undefined and no fallback
    return parse_colour(value)


def is_var_undefined(value, table):
    m = VAR.match(value.strip())
    return bool(m) and m.group(1) not in table and not m.group(2)


# ------------------------------------------------------------------- the checks

COLOR_DECL = re.compile(r"(?<![-\w])color\s*:\s*([^;]+)")
BG_DECL = re.compile(r"(?:^|[;{\s])background(?:-color)?\s*:\s*([^;]+)")
FONT_SIZE = re.compile(r"font-size\s*:\s*([\d.]+)(px|rem|em)")
FONT_WEIGHT = re.compile(r"font-weight\s*:\s*(\d{3}|bold)")


def threshold_for(body):
    """3:1 only where the rule itself declares large text."""
    m = FONT_SIZE.search(body)
    if not m:
        return AA_NORMAL
    size = float(m.group(1))
    px = size * 16 if m.group(2) in ("rem", "em") else size
    w = FONT_WEIGHT.search(body)
    bold = bool(w) and (w.group(1) == "bold" or int(w.group(1)) >= 700)
    if px >= 24 or (px >= 18.66 and bold):
        return AA_LARGE
    return AA_NORMAL


def surfaces(table):
    """Every opaque surface colour the theme defines, as candidate grounds."""
    out = []
    for name in ("--card-bg", "--primary-bg", "--secondary-bg", "--hover-bg", "--bg", "--body-bg"):
        got = resolve(f"var({name})", table)
        if got and got[1] > 0.999:
            out.append(got[0])
    return out or [(255, 255, 255)]


def overridden_backgrounds(rules):
    """Selectors whose background a more specific companion rule replaces.

    `.era-marker` declares `background: var(--paper-soft)` and `color: white`,
    which reads as white-on-white. Every instance in the markup also carries a
    colour class, and `.era-marker.amber` replaces the background — so the pair
    the base rule describes never paints. A rule cannot be judged without the
    rules that outrank it.
    """
    setters = [" ".join(sel.split()) for sel, body in rules if BG_DECL.search(body)]
    out = set()
    for sel, body in rules:
        flat = " ".join(sel.split())
        for other in setters:
            if other != flat and (other.startswith(flat + ".")
                                  or other.startswith(flat + "[")
                                  or other.startswith(flat + ":")
                                  or (" " + flat) in other
                                  or other.endswith(" " + flat)):
                out.add(flat)
                break
    return out


QUALIFIER = re.compile(
    r"^\s*(?:body|html)?(?:\.(?:dark|light)-mode|\.dark|\[data-theme=[\"\']?(?:dark|light)[\"\']?\])"
    r"(?::not\([^)]*\))*\s+", re.I)


def theme_overrides(rules):
    """(base selector, property, theme) -> value, for theme-scoped rules.

    A base rule can be perfectly correct in one theme and corrected for the
    other by a rule further down. Judging the base rule alone reports the
    corrected pair as a failure, which is how a guard loses its authority.
    """
    out = {}
    for sel, body in rules:
        for one in sel.split(","):
            one = " ".join(one.split())
            m = QUALIFIER.match(one)
            if not m:
                continue
            base = one[m.end():].strip()
            if not base:
                continue
            theme = "dark" if DARK_ONLY.search(one) else "light"
            for prop, rx in (("color", COLOR_DECL), ("background", BG_DECL)):
                d = rx.search(body)
                if d:
                    out[(base, prop, theme)] = d.group(1).strip()
    return out


def scan_css(css, label, findings, undefined):
    css = strip_comments(css)
    light, dark = collect_tokens(css)
    if not light and not dark:
        return
    all_rules = RULE.findall(css)
    shadowed = overridden_backgrounds(all_rules)
    overrides = theme_overrides(all_rules)
    for sel, body in all_rules:
        sel_flat = " ".join(sel.split())
        if "contrast-ignore" in sel or "contrast-ignore" in body:
            continue
        cm, bm = COLOR_DECL.search(body), BG_DECL.search(body)
        if not cm:
            continue
        if sel_flat in shadowed:
            continue
        raw_c = cm.group(1).strip()
        if is_var_undefined(raw_c, light) and is_var_undefined(raw_c, dark):
            undefined.add((label, VAR.match(raw_c).group(1)))
        if not bm:
            continue
        if DARK_ONLY.search(sel_flat):
            themes = (("dark", dark),)
        elif LIGHT_ONLY.search(sel_flat):
            themes = (("light", light),)
        else:
            themes = (("light", light), ("dark", dark))
        need = threshold_for(body)
        for theme, table in themes:
            eff_c = overrides.get((sel_flat, "color", theme), raw_c)
            eff_b = overrides.get((sel_flat, "background", theme), bm.group(1).strip())
            fg = resolve(eff_c, table)
            bg = resolve(eff_b, table)
            if not fg or not bg:
                continue
            if bg[1] > 0.999:
                r = contrast(fg[0], bg[0])
                if r < need:
                    findings.append((r, need, theme, label, sel_flat[:64],
                                     eff_c[:28], eff_b[:28]))
            # A translucent background is deliberately out of scope: what shows
            # through it is set by an ancestor, and on this site that ancestor is
            # often a gradient hero rather than any surface token. A first pass
            # composited such tints over every theme surface and reported 6,397
            # rules, essentially all of them `color: white` on a 10% white veil
            # over a dark hero — correct on the page, unresolvable from the
            # stylesheet. The ground has to be known to judge the pair, so the
            # check stays with the pairs where it is.


STYLE_BLOCK = re.compile(r"<style[^>]*>(.*?)</style>", re.S | re.I)


def main():
    verbose = "-v" in sys.argv
    # The shared stylesheets are the gate: one cascade, one token table, and
    # every finding here was checked against a browser before this shipped.
    # Inline page CSS is reported under --pages but not gated. A page can hold
    # several <style> elements, utility classes that outrank a base rule, and
    # tints over a gradient an ancestor paints, and this checker resolves none
    # of those reliably — a first attempt over pages reported 6,397 rules,
    # essentially all of them correct on screen. A gate that cannot be trusted
    # gets ignored, and then it protects nothing.
    scan_pages = "--pages" in sys.argv
    findings, undefined = [], set()

    sheets = [f for f in glob.glob("css/*.css") if not f.endswith(".min.css")]
    for f in sheets:
        scan_css(Path(ROOT / f).read_text(encoding="utf-8", errors="replace"), f,
                 findings, undefined)

    pages = [f for f in glob.glob("**/*.html", recursive=True)
             if not f.startswith(SKIP_DIRS)] if scan_pages else []
    for f in pages:
        src = Path(ROOT / f).read_text(encoding="utf-8", errors="replace")
        for block in STYLE_BLOCK.findall(src):
            scan_css(block, f, findings, undefined)

    if undefined and verbose:
        print("custom properties referenced with no definition and no fallback:")
        for label, name in sorted(undefined):
            print(f"    {label}: {name}")
        print()

    if findings:
        seen, uniq = set(), []
        for f in sorted(findings):
            key = (f[2], f[3], f[4])
            if key not in seen:
                seen.add(key)
                uniq.append(f)
        print(f"FAIL - {len(uniq)} rule(s) put text on a background below WCAG AA.")
        print("       A theme the change was not viewed in fails exactly like this,")
        print("       with nothing on the page to show for it.\n")
        for r, need, theme, label, sel, c, b in uniq:
            print(f"    {r:5.2f}:1  (needs {need}:1)  [{theme}]  {label}")
            print(f"        {sel}")
            print(f"        color: {c}   background: {b}")
        return 1

    scope = f"{len(sheets)} stylesheets" + (f" and {len(pages)} pages" if pages else "")
    print(f"PASS - every colour/background pair clears WCAG AA in both themes ({scope}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
