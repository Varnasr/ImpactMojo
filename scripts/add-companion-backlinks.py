#!/usr/bin/env python3
"""Add a minimal back-link footer bar to every BookSummaries companion page.

Each companion is a dead end: no way back to the library index or the catalog.
This script inserts, right before </body>, a small self-contained footer with
two links ("All Reading Companions" -> /BookSummaries/, "Browse everything"
-> /catalog.html). Styling is scoped under the class prefix `imx-companion-foot`
and respects dark mode via prefers-color-scheme plus the site theme toggle
(html.dark / html[data-theme]).

Idempotent: files that already contain `imx-companion-foot` are skipped, so
re-running never duplicates the footer. Files without a </body> tag are
reported and left untouched.

Usage: python3 scripts/add-companion-backlinks.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "BookSummaries"

MARKER = "imx-companion-foot"

FOOTER = """<!-- imx-companion-foot: back-links to the BookSummaries library -->
<style>
.imx-companion-foot{text-align:center;padding:1.25rem 1rem;margin-top:2rem;border-top:1px solid #E2E8F0;background:#F8FAFC;font-family:'Inter',system-ui,sans-serif;font-size:0.9rem;line-height:1.5;}
.imx-companion-foot a{color:#0369A1;text-decoration:none;font-weight:600;margin:0 0.75rem;display:inline-block;}
.imx-companion-foot a:hover{text-decoration:underline;}
@media (prefers-color-scheme: dark){
.imx-companion-foot{border-top-color:#2E3345;background:#14161F;}
.imx-companion-foot a{color:#38BDF8;}
}
html.dark .imx-companion-foot,html[data-theme="dark"] .imx-companion-foot{border-top-color:#2E3345;background:#14161F;}
html.dark .imx-companion-foot a,html[data-theme="dark"] .imx-companion-foot a{color:#38BDF8;}
html[data-theme="light"] .imx-companion-foot{border-top-color:#E2E8F0;background:#F8FAFC;}
html[data-theme="light"] .imx-companion-foot a{color:#0369A1;}
</style>
<div class="imx-companion-foot">
  <a href="/BookSummaries/">&#8592; All Reading Companions</a>
  <a href="/catalog.html">Browse everything</a>
</div>
"""


def main() -> int:
    added, skipped_present, skipped_nobody, errors = [], [], [], []

    for path in sorted(BOOK_DIR.glob("*.html")):
        if path.name == "index.html":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path.name}: not valid UTF-8 ({exc})")
            continue

        if MARKER in text:
            skipped_present.append(path.name)
            continue

        idx = text.rfind("</body>")
        if idx == -1:
            skipped_nobody.append(path.name)
            continue

        path.write_text(text[:idx] + FOOTER + text[idx:], encoding="utf-8")
        added.append(path.name)

    print(f"Added footer:      {len(added)}")
    print(f"Already present:   {len(skipped_present)}")
    if skipped_nobody:
        print(f"No </body> (skipped): {len(skipped_nobody)}")
        for name in skipped_nobody:
            print(f"  - {name}")
    if errors:
        print("Errors:")
        for err in errors:
            print(f"  - {err}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
