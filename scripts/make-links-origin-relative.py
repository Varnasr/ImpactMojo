#!/usr/bin/env python3
"""Rewrite in-site absolute links to root-relative ones.

Why this exists
---------------
The site was written with `href="https://www.impactmojo.in/..."` in its own
navigation -- about 6,300 times across 248 pages. On the custom domain that
works, so nothing ever looked wrong. It means the site can only be browsed on
that one hostname: on impactmojo.netlify.app, on a deploy preview, or on
localhost, every one of those links leaves for the canonical domain. When DNS
for that domain failed on 2026-08-29 the whole site became unusable even
though Netlify was serving it perfectly, and every page reported the visitor
as offline, because for those requests they were.

A root-relative `/courses/mel/` resolves identically on the custom domain and
works everywhere else too, so this is strictly a widening.

What is deliberately NOT rewritten
----------------------------------
Absolute URLs that are consumed off-site and must name the canonical host:

  <link rel="canonical">, og:url, og:image, twitter:*   crawlers and unfurlers
  JSON-LD blocks (application/ld+json)                  structured data
  <loc> in sitemap.xml                                  the sitemap contract
  supabase/email-templates/                             an email has no origin
  Open Badges credential ids (js/open-badges.js)        permanent identifiers

Run with --check to fail when any in-site absolute link has come back.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = ("Backups", "node_modules", ".git", "tests", "supabase")

ORIGIN = re.compile(r'https://(?:www\.)?impactmojo\.in')
# <link>/<meta> carry canonical + og/twitter; ld+json carries structured data.
TAG_SKIP = re.compile(r'<\s*(?:link|meta)\b[^>]*>', re.I)
LDJSON = re.compile(r'<script[^>]*application/ld\+json[^>]*>.*?</script>', re.I | re.S)
ATTR = re.compile(r'\b(href|src)=(["\'])https://(?:www\.)?impactmojo\.in([^"\']*)\2')


def rewrite(text):
    """Rewrite outside the regions that must keep an absolute URL."""
    keep = []
    for pat in (LDJSON, TAG_SKIP):
        for m in pat.finditer(text):
            keep.append((m.start(), m.end()))
    keep.sort()

    def protected(pos):
        for a, b in keep:
            if a <= pos < b:
                return True
            if a > pos:
                break
        return False

    out, last, n = [], 0, 0
    for m in ATTR.finditer(text):
        if protected(m.start()):
            continue
        path = m.group(3)
        out.append(text[last:m.start()])
        out.append(f'{m.group(1)}={m.group(2)}{path or "/"}{m.group(2)}')
        last = m.end()
        n += 1
    out.append(text[last:])
    return "".join(out), n


def targets():
    for p in sorted(ROOT.rglob("*.html")):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        yield p


def main():
    check = "--check" in sys.argv
    total, touched, offenders = 0, 0, []
    for p in targets():
        text = p.read_text(encoding="utf-8", errors="surrogateescape")
        if not ORIGIN.search(text):
            continue
        new, n = rewrite(text)
        if not n:
            continue
        total += n
        touched += 1
        if check:
            offenders.append((p.relative_to(ROOT), n))
        else:
            p.write_text(new, encoding="utf-8", errors="surrogateescape")

    if check:
        if offenders:
            print(f"FAIL - {total:,} in-site absolute link(s) in "
                  f"{len(offenders)} file(s) name the canonical host, so they "
                  "break on every other origin (netlify.app, deploy previews, "
                  "localhost).\n       Run: python3 "
                  "scripts/make-links-origin-relative.py")
            for f, n in offenders[:10]:
                print(f"    {n:5d}  {f}")
            if len(offenders) > 10:
                print(f"    … and {len(offenders)-10} more")
            return 1
        print("PASS - no in-site link hard-codes the canonical host.")
        return 0

    print(f"rewrote {total:,} link(s) across {touched} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
