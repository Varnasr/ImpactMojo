#!/usr/bin/env python3
"""
Sync data/search-index.json with the migrated native 101 decks.

The site convention: each *native* 101 deck has a `course` entry in
search-index.json (the pre-existing native decks already do). This adds/updates
one entry per Gamma→native migrated deck so they're discoverable in site search.

Idempotent: an existing entry for the same url is replaced, not duplicated.
Appends with the file's 2-space indentation without reflowing existing entries.

Usage:  python3 scripts/deck-builder/sync_search_index.py
"""
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPECS = Path(__file__).resolve().parent / "specs"
INDEX = ROOT / "data" / "search-index.json"

# (spec module, output slug) for the 26 Gamma→native migrated decks.
DECKS = [
    ("data_lit", "data-lit"), ("bi_analysis", "bi-analysis"),
    ("multivariate_basics", "multivariate-basics"), ("econometrics_101", "econometrics-101"),
    ("eda_hhs", "eda-hhs"), ("irt_basics", "irt-basics"),
    ("qual_methods", "qual-methods"), ("obs2insight", "obs2insight"),
    ("research_ethics", "research-ethics"), ("cost_effectiveness", "cost-effectiveness"),
    ("data_feminism", "data-feminism"), ("care_economy_101", "care-economy-101"),
    ("sel_basics", "sel-basics"), ("srhr_basics", "SRHR-basics"),
    ("community_dev", "community-dev"), ("edu_pedagogy", "edu-pedagogy"),
    ("eng_dev", "eng-dev"), ("decolonize_dev", "decolonize-dev"),
    ("digital_ethics", "digital-ethics"), ("env_justice", "env-justice"),
    ("post_truth_101", "post-truth-101"), ("visual_eth", "visual-eth"),
    ("ind_constitution", "ind-constitution"), ("dev_architecture", "dev-architecture"),
    ("pub_health_basics", "pub-health-basics"), ("fundraising_basics", "fundraising-basics"),
]

STOP = {"and", "the", "for", "of", "to", "in", "a", "an", "101", "amp"}


def load_deck(module):
    path = SPECS / f"{module}.py"
    spec = importlib.util.spec_from_file_location(f"ssi_{module}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.DECK


def make_tags(title):
    words = re.sub(r"&[a-z]+;", " ", title).lower()
    words = re.sub(r"[^a-z0-9 ]", " ", words).split()
    seen = []
    for w in words:
        if w not in STOP and w not in seen:
            seen.append(w)
    return seen[:5] + ["south asia", "101", "foundational course"]


def short_desc(deck):
    # Trim the spec description to a single clean sentence-ish blurb.
    d = re.sub(r"\s+", " ", deck["description"]).strip()
    return d


def build_entries():
    out = []
    for module, slug in DECKS:
        path = SPECS / f"{module}.py"
        if not path.exists():
            print(f"  [skip] spec not found: {module}")
            continue
        deck = load_deck(module)
        out.append({
            "id": f"101-{slug.lower()}",
            "title": deck["title"],
            "description": short_desc(deck),
            "url": f"/101-courses/{slug}.html",
            "tags": make_tags(deck["title"]),
            "type": "course",
            "category": "101 Foundational Courses",
        })
    return out


def main():
    text = INDEX.read_text(encoding="utf-8")
    data = json.loads(text)
    existing_urls = {(e.get("url") or e.get("link")) for e in data}
    new = [e for e in build_entries() if e["url"] not in existing_urls]
    if not new:
        print("search-index.json: already in sync, nothing to add")
        return
    # Serialise each new object at the array's 2-space indentation, leaving
    # every existing byte untouched (splice before the closing bracket).
    blocks = []
    for e in new:
        body = json.dumps(e, ensure_ascii=False, indent=2)
        blocks.append("\n".join("  " + ln for ln in body.splitlines()))
    insertion = ",\n" + ",\n".join(blocks)
    idx = text.rstrip().rfind("\n]")
    if idx == -1:
        raise SystemExit("could not find closing ] in search-index.json")
    out = text[:idx] + insertion + text[idx:]
    json.loads(out)  # validate before writing
    INDEX.write_text(out, encoding="utf-8")
    print(f"search-index.json: +{len(new)} native 101 course entries "
          f"({len(data)} -> {len(data) + len(new)})")


if __name__ == "__main__":
    main()
