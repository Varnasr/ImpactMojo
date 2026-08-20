#!/usr/bin/env python3
"""Every page a browser renders must declare a viewport.

Without `<meta name="viewport">` a phone lays the page out at desktop width and
zooms out, so the text arrives too small to read. Nothing errors, the page looks
right on the machine it was built on, and only a visitor on a phone ever sees
it. `.claude/rules/testing.md` has required this since the file existed; it was
a manual step, so two live reading companions
(`history-economic-thought-interactive.html`, `beyond-developmentality-deb-interactive.html`)
shipped without one.

Attribute order is not fixed: `index.html` writes
`<meta content="..." name="viewport"/>`, which a naive `name="viewport"` scan
misses and reports as a false failure. The check tolerates either order, single
or double quotes, and any attribute spacing.

EXEMPT holds the files that are deliberately not browser pages, each with the
reason. A stale exemption fails too, so the list cannot rot.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = ("Backups", "node_modules", ".git", "tests")

EXEMPT = {
    "supabase/email-templates/confirm-signup.html": "email body, not a browser page; mail clients ignore viewport",
    "supabase/email-templates/reset-password.html": "email body, not a browser page",
    "supabase/email-templates/magic-link.html": "email body, not a browser page",
    "supabase/email-templates/invite-user.html": "email body, not a browser page",
    "supabase/email-templates/change-email.html": "email body, not a browser page",
}

# <meta ... name=viewport ...> with the attributes in either order.
VIEWPORT = re.compile(
    r"""<meta\b[^>]*\bname\s*=\s*["']?viewport["']?[^>]*>""",
    re.IGNORECASE,
)


def pages():
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        yield rel, path


def main():
    missing, checked = [], 0
    seen = set()

    for rel, path in pages():
        seen.add(rel)
        if rel in EXEMPT:
            continue
        checked += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        if not VIEWPORT.search(text):
            missing.append(rel)

    # An exemption for a file that is gone, or that now declares a viewport,
    # is stale -- report it so the list stays honest.
    stale = []
    for rel in sorted(EXEMPT):
        if rel not in seen:
            stale.append((rel, "no longer exists"))
            continue
        text = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
        if VIEWPORT.search(text):
            stale.append((rel, "now declares a viewport"))

    if missing:
        print(f"FAIL - {len(missing)} page(s) have no viewport meta:")
        for m in missing:
            print(f"    {m}")
        print("\nAdd <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        print("or list the file in EXEMPT in scripts/check-viewport.py with the reason.")
        return 1

    if stale:
        print(f"FAIL - {len(stale)} EXEMPT entr(ies) are stale:")
        for rel, why in stale:
            print(f"    {rel}  ({why})")
        return 1

    print(f"PASS - all {checked} pages declare a viewport "
          f"({len(EXEMPT)} exempted on purpose).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
