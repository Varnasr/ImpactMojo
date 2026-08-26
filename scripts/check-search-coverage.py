#!/usr/bin/env python3
"""Every page in sitemap.xml must be findable in site search.

The sitemap is what we tell Google exists. `data/search-index.json` is what our
own visitors can find. They had drifted 127 pages apart -- 47 course posters, 19
reading companions, 17 course lexicons and 8 premium tools were live, crawlable
and advertised, and site search could not return any of them. Nothing failed:
adding a page updates the sitemap, and the index is a separate file nobody is
forced to touch.

Comparison is on the decoded, case-folded, fragment-stripped path, because the
index stores `%20` in handout paths and the sitemap does not -- comparing raw
strings reports 87 phantom gaps.

EXEMPT lists the pages deliberately left out, each with the reason. Adding to it
is a decision someone has to write down, which is the point.

It also asserts that `id` is unique across the index. That is here because
coverage is compared by url, so id collisions were invisible to every guard we
had: three ids were each carrying two different pages (#1031).
The cause is worth knowing, because it will recur otherwise -- the next id gets
chosen by reading the id of the *last* blog entry in the array, but the array is
not sorted by id, so the last blog entry was BLOG037 while the highest in the
file was BLOG061. Search still worked throughout, which is exactly why nobody
noticed.
"""
import json, re, sys, urllib.parse, xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITEMAP = ROOT / "sitemap.xml"
INDEX = ROOT / "data" / "search-index.json"
SM_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}loc"

EXEMPT = {
    "/": "the homepage; a search result pointing home is noise",
    "/handouts": "pretty-URL duplicate of /handouts.html, which is indexed",
    "/supportgifts/thankyou.html": "post-transaction page; a search hit on it is a dead end",
    "/linkedin-claude-code-visual.html": "a dev-setup artefact, not platform content",
    "/101-courses/native/dev-economics.html": "16KB alternate rendering of /101-courses/dev-economics.html, already indexed under the same title",
}


def norm(url):
    url = url.split("#")[0].split("?")[0]
    url = re.sub(r"^https?://(www\.)?impactmojo\.in", "", url)
    return urllib.parse.unquote(url).rstrip("/").lower() or "/"


def main():
    entries = json.loads(INDEX.read_text(encoding="utf-8"))
    indexed = {norm(e.get("url") or "") for e in entries}

    locs = [el.text.strip() for el in ET.parse(SITEMAP).getroot().iter(SM_NS) if el.text]
    if not locs:
        print("FAIL - sitemap.xml has no <loc> entries")
        return 1

    exempt = {norm(k) for k in EXEMPT}
    missing = sorted({norm(l) for l in locs} - indexed - exempt)

    # An exemption for a page that is now indexed, or gone from the sitemap, is
    # stale -- report it so the list does not rot into a permanent blindfold.
    sitemap_paths = {norm(l) for l in locs}
    stale = sorted(p for p in exempt if p in indexed or p not in sitemap_paths)

    if missing:
        print(f"FAIL - {len(missing)} page(s) in sitemap.xml are not in data/search-index.json:")
        for m in missing:
            print(f"    {m}")
        print("\nAdd an entry to data/search-index.json, or list the page in EXEMPT")
        print("in scripts/check-search-coverage.py with the reason it stays out.")
        return 1

    if stale:
        print(f"FAIL - {len(stale)} EXEMPT entr(ies) in this script are stale:")
        for s in stale:
            why = "now indexed" if s in indexed else "no longer in sitemap.xml"
            print(f"    {s}  ({why})")
        return 1

    # An id looks like a primary key, so anything downstream may treat it as
    # unique; nothing else in the repo reads the field at all, which is how
    # three collisions survived (#1031). Urls are deliberately NOT checked for
    # uniqueness: many entries point at the same page under different fragments
    # -- every judgment at the docket, every dataverse resource at dataverse.html
    # -- and norm() strips fragments, so a url check would fail on correct data.
    dup_id = sorted(k for k, n in Counter(
        e["id"] for e in entries if isinstance(e.get("id"), str)).items() if n > 1)
    if dup_id:
        print(f"FAIL - data/search-index.json has {len(dup_id)} duplicate id(s):")
        for d in dup_id:
            urls = [e.get("url") for e in entries if e.get("id") == d]
            print(f"    {d} -> {', '.join(str(u) for u in urls)}")
        print("\nGive each entry its own id. For a new blog post take max(id) over")
        print("the whole file, not the id of the last blog entry in the array --")
        print("the array is not sorted by id.")
        return 1

    print(f"PASS - all {len(sitemap_paths)} sitemap pages are in site search "
          f"({len(exempt)} exempted on purpose, {len(entries)} index entries).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
