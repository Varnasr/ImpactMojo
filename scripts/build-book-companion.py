#!/usr/bin/env python3
"""
Build an interactive book-companion page for BookSummaries/ from a content spec.

The modern ImpactMojo companion (e.g. debraj-ray-companion.html) is a single,
self-contained data-driven app: one `const DATA = {...}` object feeds tabs for
Overview / Sections / Concepts / Toolkit / Context / Ask-AI. This script injects
a spec's DATA object into the shared template and writes {slug}-companion.html.

Usage:
    python3 scripts/build-book-companion.py path/to/spec.json
    python3 scripts/build-book-companion.py path/to/spec.json --out BookSummaries

A spec is JSON with two top-level keys:
    "meta": { "slug", "page_title", "meta_desc" }
    "data": { ...the DATA object (schema below)... }

DATA schema (all keys required; lists may be empty):
    title, dayBadge, author, tagline,
    pills:[str], stats:[{n,l}], argument:[str],
    accent, accent_light,
    pathways:[...], sections:[{title,subtitle,summary,ideas:[str],quotes:[str],devEcon}],
    concepts:[{term,definition,practitionerNote}],
    tools:[{label,intro,html}], connections:[...], southAsia:[...],
    critiques:[...], suggested:[...], systemPrompt
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "templates", "book-companion.template.html")

REQUIRED_META = ("slug", "page_title", "meta_desc")
REQUIRED_DATA = (
    "title", "dayBadge", "author", "tagline", "pills", "stats", "argument",
    "accent", "accent_light", "pathways", "sections", "concepts", "tools",
    "connections", "southAsia", "critiques", "suggested", "systemPrompt",
)


def build(spec_path, out_dir):
    with open(spec_path, encoding="utf-8") as f:
        spec = json.load(f)

    meta = spec.get("meta", {})
    data = spec.get("data", {})

    missing_meta = [k for k in REQUIRED_META if not meta.get(k)]
    if missing_meta:
        sys.exit(f"spec.meta missing keys: {missing_meta}")
    missing_data = [k for k in REQUIRED_DATA if k not in data]
    if missing_data:
        sys.exit(f"spec.data missing keys: {missing_data}")

    slug = meta["slug"]
    if slug.endswith("-companion"):
        slug = slug[: -len("-companion")]

    with open(TEMPLATE, encoding="utf-8") as f:
        tmpl = f.read()

    # DATA is injected as compact JSON so the app's JSON.parse-equivalent works.
    data_json = json.dumps(data, ensure_ascii=False)

    html = (
        tmpl.replace("{{PAGE_TITLE}}", meta["page_title"])
        .replace("{{META_DESC}}", meta["meta_desc"])
        .replace("{{SLUG}}", slug)
        .replace("{{DATA}}", data_json)
    )

    out_path = os.path.join(out_dir, f"{slug}-companion.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {out_path} ({len(html):,} bytes, {len(data['sections'])} sections, "
          f"{len(data['concepts'])} concepts)")
    return out_path


def main():
    ap = argparse.ArgumentParser(description="Build a BookSummaries companion page from a spec.")
    ap.add_argument("spec", help="Path to the spec JSON file")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(HERE), "BookSummaries"),
                    help="Output directory (default: BookSummaries/)")
    args = ap.parse_args()
    build(args.spec, args.out)


if __name__ == "__main__":
    main()
