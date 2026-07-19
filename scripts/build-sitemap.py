#!/usr/bin/env python3
"""Regenerate sitemap.xml from the tracked HTML files.

The hand-maintained sitemap had drifted 194 pages behind reality (whole
families missing: Handouts, challenges, some companions). This walks
`git ls-files '*.html'`, applies an explicit exclusion list, folds
index.html to its directory URL, and stamps lastmod from each file's last
git commit. Run after adding content; CI-friendly (deterministic).
"""

import subprocess
import sys
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.impactmojo.in"

EXCLUDE_PREFIXES = (
    "Backups/", "node_modules/", "tests/", "ops/", "admin/", "supabase/",
    "netlify/", "scripts/", "docs/", "netlify-resource-template/",
    "netlify-env-files/",
)
EXCLUDE_FILES = {
    "404.html", "offline.html", "login.html", "signup.html",
    "forgot-password.html", "reset-password.html", "account.html",
    "org-dashboard.html", "PAGE-TEMPLATE.html",
}
EXCLUDE_SUBSTRINGS = ("_template", "template.html", "-TEMPLATE")


def tracked_html():
    out = subprocess.run(["git", "ls-files", "*.html"], capture_output=True,
                         text=True, cwd=ROOT, check=True).stdout.splitlines()
    return out


def last_commit_dates():
    """One pass over history: path -> ISO date of most recent commit."""
    out = subprocess.run(
        ["git", "log", "--format=%x01%cs", "--name-only"],
        capture_output=True, text=True, cwd=ROOT, check=True).stdout
    dates = {}
    current = None
    for line in out.splitlines():
        if line.startswith("\x01"):
            current = line[1:]
        elif line and current and line not in dates:
            dates[line] = current
    return dates


def include(path):
    if path.startswith(EXCLUDE_PREFIXES):
        return False
    name = path.rsplit("/", 1)[-1]
    if name in EXCLUDE_FILES or path in EXCLUDE_FILES:
        return False
    if any(s in path for s in EXCLUDE_SUBSTRINGS):
        return False
    # respect per-page noindex
    try:
        head = (ROOT / path).read_text(encoding="utf-8", errors="ignore")[:4000]
        if "noindex" in head:
            return False
    except OSError:
        return False
    return True


def to_url(path):
    if path == "index.html":
        return SITE + "/"
    if path.endswith("/index.html"):
        return SITE + "/" + path[: -len("index.html")]
    return SITE + "/" + path


def main():
    dates = last_commit_dates()
    urls = []
    for p in tracked_html():
        if include(p):
            urls.append((to_url(p), dates.get(p, "")))
    urls.sort()

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, lastmod in urls:
        entry = f"  <url><loc>{escape(url)}</loc>"
        if lastmod:
            entry += f"<lastmod>{lastmod}</lastmod>"
        entry += "</url>"
        lines.append(entry)
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"sitemap.xml written: {len(urls)} URLs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
