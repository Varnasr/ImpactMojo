#!/usr/bin/env python3
"""Keep the homepage nav's "Recently updated" dots honest.

The dots were two hardcoded `<span>`s, added 2026-07-29 to Libraries and Field
Radio and never revisited. Three weeks later they still claimed freshness while
the **blog** — which had the two newest items on the whole site — carried none.
A freshness marker with no expiry can only drift, and it drifts in the direction
that misleads: it keeps pointing at whatever was new the day someone typed it.

So the dots are derived now, from `data/nav-updated.json`:

  * `auto`   — a nav id whose date is read from the content itself. `nav-blog`
               takes the newest `article:published_time` across `blog/*.html`,
               so it is right without anyone maintaining it.
  * `manual` — a nav id with a hand-set date, for areas that carry no per-item
               dates. These expire.

Anything older than `window_days` loses its dot automatically. That is the whole
point: the failure mode being fixed is a dot that never goes away.

    python3 scripts/stamp-nav-dots.py            rewrite index.html
    python3 scripts/stamp-nav-dots.py --check    verify, exit 1 on drift
"""
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
CONFIG = ROOT / "data" / "nav-updated.json"
BLOG = ROOT / "blog"

DOT = (
    '<span title="Recently updated" aria-label="Recently updated" '
    'style="display:inline-block;width:6px;height:6px;border-radius:50%;'
    'background:#D97706;margin-left:4px;vertical-align:middle"></span>'
)
# The dot as it appears now, so an existing one can be found and removed.
DOT_RE = re.compile(
    r'<span title="Recently updated"[^>]*></span>'
)


def newest_blog_date():
    newest = None
    for post in BLOG.glob("*.html"):
        m = re.search(
            r'article:published_time"\s+content="(\d{4}-\d{2}-\d{2})', post.read_text(
                encoding="utf-8", errors="replace")[:4000]
        )
        if m:
            d = m.group(1)
            if newest is None or d > newest:
                newest = d
    return newest


def wanted(cfg, today):
    """nav ids that should carry a dot, with the date that justifies it."""
    window = timedelta(days=int(cfg.get("window_days", 30)))
    out = {}

    for nav_id in cfg.get("auto", {}):
        if nav_id == "nav-blog":
            d = newest_blog_date()
        else:
            d = None
        if d:
            out[nav_id] = d

    for nav_id, d in (cfg.get("manual") or {}).items():
        out[nav_id] = d

    fresh = {}
    for nav_id, d in out.items():
        try:
            when = datetime.strptime(d, "%Y-%m-%d").date()
        except ValueError:
            print(f"FAIL - {nav_id} has an unparseable date {d!r} in {CONFIG.name}")
            sys.exit(1)
        if today - when <= window:
            fresh[nav_id] = d
    return fresh


def li_span(html, nav_id):
    """Return (start, end) of the <li id="nav-x"> … </li> block, or None."""
    m = re.search(rf'<li id="{re.escape(nav_id)}">', html)
    if not m:
        return None
    end = html.find("</li>", m.end())
    return (m.start(), end) if end != -1 else None


def apply(html, fresh):
    """Add a dot to every fresh nav id and strip it from every other."""
    # Strip every existing dot first, so removals happen too.
    ids = set(re.findall(r'<li id="(nav-[a-z-]+)">', html))
    for nav_id in sorted(ids):
        span = li_span(html, nav_id)
        if not span:
            continue
        start, end = span
        block = html[start:end]
        cleaned = DOT_RE.sub("", block)
        if cleaned != block:
            html = html[:start] + cleaned + html[end:]

    # Then add one to each fresh id, immediately before its closing </a>.
    for nav_id in sorted(fresh):
        span = li_span(html, nav_id)
        if not span:
            print(f"  note: {nav_id} is not in index.html — skipped")
            continue
        start, end = span
        block = html[start:end]
        close = block.rfind("</a>")
        if close == -1:
            print(f"  note: {nav_id} has no </a> — skipped")
            continue
        html = html[:start] + block[:close] + DOT + block[close:] + html[end:]
    return html


def main():
    check = "--check" in sys.argv
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    html = INDEX.read_text(encoding="utf-8")
    fresh = wanted(cfg, date.today())
    updated = apply(html, fresh)

    if check:
        if updated != html:
            have = set(re.findall(r'<li id="(nav-[a-z-]+)">[^\0]*?</li>', html))
            print("FAIL - the nav dots in index.html do not match data/nav-updated.json")
            print(f"    should carry a dot: {', '.join(sorted(fresh)) or '(none)'}")
            print("\nRun: python3 scripts/stamp-nav-dots.py")
            return 1
        print(f"PASS - nav dots match ({len(fresh)} fresh: "
              f"{', '.join(sorted(fresh)) or 'none'}).")
        return 0

    if updated != html:
        INDEX.write_text(updated, encoding="utf-8")
        print(f"stamped {len(fresh)} dot(s): {', '.join(sorted(fresh)) or 'none'}")
    else:
        print(f"no change ({len(fresh)} fresh dot(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
