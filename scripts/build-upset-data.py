#!/usr/bin/env python3
"""Build the UpSet intersection data for The Long View, from NFHS districts.

An UpSet plot answers a question a bar chart cannot: not "how common is each
deprivation" but "which ones land on the same district". Six separate bars
reading 63%, 90%, 50%, 8%, 75%, 46% let a reader assume those are six different
sets of places. They are very largely the same places, and that is the whole
point of measuring poverty multidimensionally.

Two views are built:

  deprivation  NFHS-5 only. A district is "in" a set when it crosses a stated
               threshold on that dimension. Which combinations co-occur?
  backwards    NFHS-4 -> NFHS-5. A district is "in" a set when it moved the
               wrong way on that dimension. Which reversals travel together?

Run: python3 scripts/build-upset-data.py [--check]
"""

import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "nfhs" / "nfhs-districts.json"
OUT = ROOT / "data" / "upset-nfhs.json"
# Every other chart in The Long View carries its numbers inline, and these two
# describe a finished historical survey that will not change. So the figures are
# emitted as a script rather than fetched -- but generated, never hand-copied,
# so they cannot drift from the JSON the guard above protects.
JS = ROOT / "js" / "longview-upset-data.js"
TOP = 12          # columns drawn; the rest are counted in a footnote

# ---------------------------------------------------------------- the guard
#
# In this file each indicator is a two-element list. It is [NFHS-5, NFHS-4] --
# the LATER round first -- which is the reverse of the reading order of the
# name "NFHS-4 & NFHS-5" and the reverse of what anyone writing this script
# will assume. nfhs.html:631 is the authority: `{n5: p[0], n4: p[1]}`.
#
# Getting it backwards does not raise, does not produce nulls, and does not
# look wrong: every number stays inside its plausible range. It silently
# reports the 2015-16 survey as the 2019-21 one. On the first draft of this
# script it put district sanitation deprivation at 55% when the NFHS-5 figure
# is 7.9%, and turned a decade of near-universal sanitation gains into
# "went backwards in 96% of districts".
#
# So the order is asserted, not assumed -- but on the right property. The first
# version of this guard compared the median district value against the published
# all-India value and picked the nearer round. That is not the same statistic:
# the national figure is population-weighted, the median district is not, and for
# an indicator that splits on urban/rural the gap between them can be larger than
# the gap between the two rounds. Clean cooking fuel is exactly that case -- a
# median district of 50.5 against a national 58.6 -- so the guard failed on
# correctly-ordered data.
#
# What actually separates the two hypotheses is the DIRECTION each district
# moved. Every indicator below has a large, undisputed direction of travel
# between the rounds, and reversing the pair flips all of them at once, so
# unanimous agreement is conclusive. It is also a paired comparison -- each
# district against itself -- so the weighting problem cannot arise.
#
#   id: (name, published NFHS-4, published NFHS-5)
ORDER_PROBES = {
    8:  ("Improved sanitation", 48.4, 70.2),
    9:  ("Clean cooking fuel", 43.8, 58.6),
    41: ("Institutional births", 78.9, 88.6),
    72: ("Child stunting", 38.4, 35.5),
    83: ("Women anaemic", 53.1, 57.0),
}

N5, N4 = 0, 1        # index into the pair, per nfhs.html:631

# ------------------------------------------------------------ the two views
#
# Thresholds are stated on the page, not hidden here. Where an external body
# publishes one, it is used and named; the rest are round numbers chosen to be
# legible, and the page says so.
DEPRIVATION = [
    ("stunting",   72, "Child stunting",        "ge", 30,
     "30% or more of under-fives stunted — the WHO “very high” prevalence threshold"),
    ("anaemia",    83, "Women anaemic",         "ge", 40,
     "40% or more of women aged 15–49 anaemic — a “severe public health problem” by WHO's classification"),
    ("fuel",        9, "No clean cooking fuel", "lt", 50,
     "fewer than half of households cooking with clean fuel"),
    ("sanitation",  8, "No safe sanitation",    "lt", 50,
     "fewer than half of people using an improved sanitation facility"),
    ("schooling",  14, "Women under-schooled",  "lt", 50,
     "fewer than half of women with ten or more years of schooling"),
    ("marriage",   15, "Child marriage",        "ge", 20,
     "20% or more of women aged 20–24 married before 18"),
]

BACKWARDS = [
    ("wanaemia", 83, "Women's anaemia"),
    ("canaemia", 80, "Children's anaemia"),
    ("stunting", 72, "Child stunting"),
    ("marriage", 15, "Child marriage"),
    ("schooling", 14, "Women's schooling"),
    ("births",   41, "Institutional births"),
    ("sanitation", 8, "Sanitation"),
    ("fuel",       9, "Clean cooking fuel"),
]


def load():
    d = json.loads(SRC.read_text(encoding="utf-8"))
    return d, {c["id"]: c for c in d["catalog"]}


def median(xs):
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def check_pair_order(data):
    """Fail loudly if [NFHS-5, NFHS-4] is no longer the shape of the pair."""
    problems = []
    for cid, (name, pub4, pub5) in ORDER_PROBES.items():
        deltas = [r["v"][cid][N5] - r["v"][cid][N4] for r in data.values()
                  if r["v"][cid]
                  and r["v"][cid][N5] is not None and r["v"][cid][N4] is not None]
        if not deltas:
            problems.append(f"{name}: no district has both rounds")
            continue
        moved, expected = median(deltas), pub5 - pub4
        if (moved > 0) != (expected > 0):
            problems.append(
                f"{name}: districts moved {moved:+.1f} between v[1] and v[0], but "
                f"the published change from NFHS-4 to NFHS-5 is {expected:+.1f}")
    return problems


def sets_for(rec, spec):
    """Which deprivation sets this district belongs to, or None if incomplete."""
    out = []
    for key, cid, _label, op, thr, _rule in spec:
        pair = rec["v"][cid]
        if not pair or pair[N5] is None:
            return None
        v = pair[N5]
        if (v >= thr) if op == "ge" else (v < thr):
            out.append(key)
    return out


def worse_for(rec, spec, cat):
    """Which dimensions this district moved backwards on, or None if incomplete."""
    out = []
    for key, cid, _label in spec:
        pair = rec["v"][cid]
        if not pair or pair[N5] is None or pair[N4] is None:
            return None
        delta = pair[N5] - pair[N4]
        if cat[cid]["dir"] == -1:      # higher is worse -> flip so +ve is progress
            delta = -delta
        if delta < 0:
            out.append(key)
    return out


def tally(members, keys):
    """Set sizes and exact-intersection sizes, largest first."""
    sizes = {k: sum(1 for m in members if k in m) for k in keys}
    inter = Counter(tuple(sorted(m)) for m in members)
    rows = [{"sets": list(t), "n": n} for t, n in inter.most_common()]
    return sizes, rows


def build():
    d, cat = load()
    data = d["data"]

    problems = check_pair_order(data)
    if problems:
        print("FAIL - the NFHS value pairs are not [NFHS-5, NFHS-4] any more.")
        print("       Every figure built from this file would be the wrong survey")
        print("       round, in range and unremarkable. See nfhs.html:631.\n")
        for p in problems:
            print("    " + p)
        return None

    dep = [m for m in (sets_for(r, DEPRIVATION) for r in data.values()) if m is not None]
    bak = [m for m in (worse_for(r, BACKWARDS, cat) for r in data.values()) if m is not None]

    dep_sizes, dep_rows = tally(dep, [s[0] for s in DEPRIVATION])
    bak_sizes, bak_rows = tally(bak, [s[0] for s in BACKWARDS])

    return {
        "_source": d["meta"]["source"],
        "_boundaries": d["meta"]["geometry"],
        "_built_by": "scripts/build-upset-data.py",
        "_generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "_note": ("Value pairs in the source are [NFHS-5, NFHS-4] — later round "
                  "first. The build asserts this before using it."),
        "deprivation": {
            "round": "NFHS-5 (2019-21)",
            "universe": len(dep),
            "sets": [{"key": k, "label": lab, "n": dep_sizes[k], "rule": rule}
                     for k, _c, lab, _o, _t, rule in DEPRIVATION],
            "intersections": dep_rows,
        },
        "backwards": {
            "round": "NFHS-4 (2015-16) → NFHS-5 (2019-21)",
            "universe": len(bak),
            "sets": [{"key": k, "label": lab, "n": bak_sizes[k],
                      "rule": "moved the wrong way between the two rounds"}
                     for k, _c, lab in BACKWARDS],
            "intersections": bak_rows,
        },
    }


def render_js(built):
    """The drawable subset: top intersections, plus what was left out."""
    def view(v):
        shown = v["intersections"][:TOP]
        return {
            "round": v["round"],
            "universe": v["universe"],
            "sets": [{"key": s["key"], "label": s["label"], "n": s["n"]}
                     for s in v["sets"]],
            "shown": [{"sets": r["sets"], "n": r["n"]} for r in shown],
            "hiddenCombos": len(v["intersections"]) - len(shown),
            "hiddenDistricts": sum(r["n"] for r in v["intersections"][TOP:]),
        }
    payload = {"deprivation": view(built["deprivation"]),
               "backwards": view(built["backwards"])}
    return ("/* Generated by scripts/build-upset-data.py -- do not edit.\n"
            "   Source: " + built["_source"] + " */\n"
            "window.LV_UPSET = " + json.dumps(payload, ensure_ascii=False, indent=1)
            + ";\n")


def main():
    built = build()
    if built is None:
        return 1
    js = render_js(built)

    if "--check" in sys.argv:
        for path in (OUT, JS):
            if not path.exists():
                print(f"FAIL - {path.relative_to(ROOT)} is missing. "
                      f"Run without --check.")
                return 1
        have = json.loads(OUT.read_text(encoding="utf-8"))
        a = {k: v for k, v in have.items() if k != "_generated"}
        b = {k: v for k, v in built.items() if k != "_generated"}
        if a != b:
            print(f"FAIL - {OUT.relative_to(ROOT)} is out of date with the source.")
            print("       Run: python3 scripts/build-upset-data.py")
            return 1
        if JS.read_text(encoding="utf-8") != js:
            print(f"FAIL - {JS.relative_to(ROOT)} does not match {OUT.relative_to(ROOT)}.")
            print("       The chart would draw numbers the data file does not agree")
            print("       with. Run: python3 scripts/build-upset-data.py")
            return 1
        dep, bak = have["deprivation"], have["backwards"]
        print(f"PASS - UpSet data matches the source and the chart script "
              f"({dep['universe']} districts on {len(dep['sets'])} deprivations, "
              f"{bak['universe']} on {len(bak['sets'])} changes).")
        return 0

    OUT.write_text(json.dumps(built, ensure_ascii=False, indent=1) + "\n",
                   encoding="utf-8")
    JS.write_text(js, encoding="utf-8")
    print(f"Wrote {JS.relative_to(ROOT)}")
    dep, bak = built["deprivation"], built["backwards"]
    print(f"Wrote {OUT.relative_to(ROOT)}")
    print(f"  deprivation: {dep['universe']} districts, "
          f"{len(dep['intersections'])} distinct combinations")
    for s in dep["sets"]:
        print(f"      {s['label']:24s} {s['n']:4d}")
    print(f"  backwards:   {bak['universe']} districts, "
          f"{len(bak['intersections'])} distinct combinations")
    for s in bak["sets"]:
        print(f"      {s['label']:24s} {s['n']:4d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
