#!/usr/bin/env python3
"""Join the prison and court tables into one clean table for justice.html.

The same trap the CSR data set: every NCRB table carries THREE total rows --
'Total (States)', 'Total (UTs)' and 'Total (All India)' -- so summing a column
returns exactly three times the real figure. 1,590,999 prisoners instead of
530,333. The court tables carry one 'Total' row and double instead.

Nothing about that is visible in the output: the file is valid, the page
renders, and every number on it is wrong by a clean multiple. So the totals are
read from the Total row, the parts are summed separately, and the two are
required to agree before anything is written.

Population and SC/ST shares are Census 2011, the most recent enumerated count
India has. Prison figures are a single-day census as on 31-12-2023, so a
per-100,000 rate is 2023 prisoners over 2011 people, and the page says so.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "justice-india.json"
OUT = ROOT / "data" / "justice-explorer.json"
PAGE = ROOT / "justice.html"

SLOT = re.compile(
    r'(<script id="justice-data" type="application/json">)(.*?)(</script>)', re.S)

ALIAS = {
    "nct of delhi": "delhi", "delhi ut": "delhi", "orissa": "odisha",
    "pondicherry": "puducherry", "uttaranchal": "uttarakhand",
    "leh ladakh": "ladakh",
    "a n island": "andaman nicobar island",
    "chhatisgarh": "chhattisgarh",          # misspelt in the SC/ST source
    # Dadra & Nagar Haveli and Daman & Diu were merged into one UT in 2020.
    # Census 2011 counted them separately, so both halves are folded together
    # to match the prison tables, which use the merged name.
    "dadra nagar haveli": "dadra nagar haveli daman diu",
    "daman diu": "dadra nagar haveli daman diu",
}

# Duration-of-confinement bands, in the order the source publishes them.
BANDS = [("upto_3_months", "Up to 3 months"), ("_3_to_6_months", "3 to 6 months"),
         ("_6_to_12_months", "6 to 12 months"), ("_1_to_2_years", "1 to 2 years"),
         ("_2_to_3_years", "2 to 3 years"), ("_3_to_5_years", "3 to 5 years"),
         ("above_5_years", "Over 5 years")]


def norm(s):
    s = (s or "").lower().strip().replace("&", " and ")
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z]+", " ", s).strip()
    s = re.sub(r"\band\b", " ", s)
    s = re.sub(r"\bislands?\b", "island", s)
    s = re.sub(r"\but\b|\bstate\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def key(s):
    k = norm(s)
    return ALIAS.get(k, k)


def num(x):
    if x is None:
        return None
    if isinstance(x, (int, float)):
        return float(x)
    t = str(x).strip().replace(",", "")
    if t in ("", "NA", "N/A", "-", "--"):
        return None
    try:
        return float(t)
    except ValueError:
        return None


def is_total(name):
    return "total" in str(name).lower() or norm(name) == "india"


def split(rows, field):
    """(real rows, the all-India total row) for a table carrying total rows."""
    real, allindia = [], None
    for r in rows:
        n = r.get(field)
        if not is_total(n):
            real.append(r)
        elif "all india" in str(n).lower() or norm(n) == "india":
            allindia = r
        elif str(n).strip().lower() == "total":
            allindia = r
    return real, allindia


def check(label, parts, whole, tol=0.005):
    if whole is None:
        print(f"FAIL - {label}: the source no longer carries a total row, so the "
              "double-count guard cannot be trusted. Check the source.")
        return False
    if abs(parts - whole) > max(1.0, whole * tol):
        print(f"FAIL - {label}: rows sum to {parts:,.0f} but the source's own "
              f"total says {whole:,.0f}.")
        return False
    return True


def payload_for_page(d):
    js = json.dumps(d, ensure_ascii=True, separators=(",", ":"))
    assert "</" not in js, "data contains a tag close; would end the script block"
    return js


def sync_page(js, check_only):
    if not PAGE.exists():
        print(f"FAIL - {PAGE.name} is missing")
        return 1
    html = PAGE.read_text(encoding="utf-8")
    m = SLOT.search(html)
    if not m:
        print(f'FAIL - no <script id="justice-data"> block in {PAGE.name}')
        return 1
    if m.group(2) == js:
        print(f"  {PAGE.name} data is current")
        return 0
    if check_only:
        print(f"FAIL - {PAGE.name} carries stale data. Run "
              "`python3 scripts/build-justice-explorer-data.py`.")
        return 1
    PAGE.write_text(html[:m.start(2)] + js + html[m.end(2):], encoding="utf-8")
    print(f"  injected {len(js):,} bytes into {PAGE.name}")
    return 0


def main():
    check_only = "--check" in sys.argv
    raw = json.loads(SRC.read_text(encoding="utf-8"))
    S = raw["series"]

    pop = {}
    for r in S["population"]["rows"]:
        p = num(r.get("population_2011"))
        k = key(r["india___state__union_territory"])
        if p:
            pop[k] = pop.get(k, 0) + p          # the two halves of DNH & DD

    # SC and ST population shares, recomputed from counts because two Census
    # 2011 units have to be merged to match 2020 UT boundaries and percentages
    # cannot be added.
    #
    # The two counts come from different tables on purpose. The ST column of
    # the combined SC/ST table is scrambled across rows: Kerala's row carries
    # Madhya Pradesh's ST population AND its percentage, so the row is
    # internally consistent and externally wrong, and the column still sums to
    # the correct national total. Nothing about it looks broken. Plotted, it
    # put Kerala at 46% Scheduled Tribe against a real 1.5%.
    #
    # So ST is taken from the Ministry of Tribal Affairs table instead, and a
    # state is only used if the count it implies agrees with a published
    # percentage. A state that fails is dropped and named on the page rather
    # than shown with a number nobody has checked.
    sc_raw, st_raw, sc_pub, st_pub = {}, {}, {}, {}
    for r in S["sc_st"]["rows"]:
        k = key(r["state_union_territory"])
        sc_raw[k] = (sc_raw.get(k) or 0) + (num(r.get("scheduled_castes_persons")) or 0)
        if num(r.get("percentage_to_population_of_state_union_territory")) is not None:
            sc_pub.setdefault(k, num(r["percentage_to_population_of_state_union_territory"]))
    for r in S["st_mota"]["rows"]:
        k = key(r["name_of_the_states_uts"])
        st_raw[k] = (st_raw.get(k) or 0) + (num(r.get("st_population")) or 0)

    # The two ST sources must agree nationally before either is used at all.
    st_a = sum(num(r.get("scheduled_tribes_persons")) or 0
               for r in S["sc_st"]["rows"] if not is_total(r["state_union_territory"]))
    st_b = sum(v for k, v in st_raw.items() if k != "india")
    if abs(st_a - st_b) > st_b * 0.01:
        print(f"FAIL - the two Scheduled Tribe sources disagree nationally: "
              f"{st_a:,.0f} vs {st_b:,.0f}. One of them has changed shape; "
              f"check before trusting either.")
        return 1

    scst, rejected = {}, []
    for k in set(list(sc_raw) + list(st_raw)):
        if k == "india":
            continue
        base = pop.get(k)
        if not base:
            continue
        sc, st = sc_raw.get(k), st_raw.get(k)
        e = {"sc_pct": 100 * sc / base if sc is not None else None,
             "st_pct": 100 * st / base if st is not None else None}
        # Cross-check against the source's own published SC percentage. A gap
        # wider than a point means the row is describing a different place --
        # which is what a Census-2011 count over a post-2014 boundary looks
        # like, and what a scrambled row looks like too.
        pub = sc_pub.get(k)
        if e["sc_pct"] is not None and pub is not None and abs(e["sc_pct"] - pub) > 1.0:
            rejected.append(k)
            continue
        scst[k] = e
    india_pop = pop.get("india")
    india_scst = {
        "sc_pct": 100 * sc_raw.get("india", 0) / india_pop if india_pop else None,
        "st_pct": 100 * st_raw.get("india", 0) / india_pop if india_pop else None,
    }

    occ_rows, occ_tot = split(S["occupancy"]["rows"], "state_ut")
    typ_rows, typ_tot = split(S["types"]["rows"], "state_ut__col_2_")
    dur_rows, dur_tot = split(S["duration"]["rows"], "state_ut")
    cst_rows, cst_tot = split(S["caste"]["rows"], "state_ut")
    edu_rows, edu_tot = split(S["education"]["rows"], "state_ut")
    rel_rows, rel_tot = split(S["religion"]["rows"], "state_ut")
    s436_rows, s436_tot = split(S["s436a"]["rows"], "state_ut")
    dc_rows, dc_tot = split(S["district_courts"]["rows"], "state_ut")
    hc_rows, hc_tot = split(S["high_courts"]["rows"], "high_court")

    ok = True
    ok &= check("prison population",
                sum(num(r["inmate_population___total"]) or 0 for r in occ_rows),
                num(occ_tot and occ_tot["inmate_population___total"]))
    ok &= check("prison capacity",
                sum(num(r["available_capacity___total"]) or 0 for r in occ_rows),
                num(occ_tot and occ_tot["available_capacity___total"]))
    ok &= check("undertrials",
                sum(num(r["undertrials___total__col_10_"]) or 0 for r in typ_rows),
                num(typ_tot and typ_tot["undertrials___total__col_10_"]))
    ok &= check("district-court pendency",
                sum(num(r["_total"]) or 0 for r in dc_rows),
                num(dc_tot and dc_tot["_total"]))
    ok &= check("high-court pendency",
                sum(num(r["_total"]) or 0 for r in hc_rows),
                num(hc_tot and hc_tot["_total"]))
    if not ok:
        return 1

    def by_state(rows, field):
        return {key(r[field]): r for r in rows}

    T, D, C, E, R, A = (by_state(typ_rows, "state_ut__col_2_"),
                        by_state(dur_rows, "state_ut"),
                        by_state(cst_rows, "state_ut"),
                        by_state(edu_rows, "state_ut"),
                        by_state(rel_rows, "state_ut"),
                        by_state(s436_rows, "state_ut"))
    DC = by_state(dc_rows, "state_ut")

    states = []
    for r in occ_rows:
        name = (r["state_ut"] or "").strip()
        k = key(name)
        t, d, c, e, rel, a = T.get(k), D.get(k), C.get(k), E.get(k), R.get(k), A.get(k)
        dc = DC.get(k)
        states.append({
            "name": name,
            "capacity": num(r["available_capacity___total"]),
            "inmates": num(r["inmate_population___total"]),
            "occupancy": num(r["occupancy_rate_in_percentage____total"]),
            "women_inmates": num(r["inmate_population___female"]),
            "convicts": t and num(t["convicts___total__col_6_"]),
            "undertrials": t and num(t["undertrials___total__col_10_"]),
            "detenues": t and num(t["detenues___total__col_14_"]),
            "wait": d and {b: num(d.get(b + "___total")) for b, _ in BANDS},
            "caste": c and {
                "sc": num(c["scheduled_castes__sc_"]), "st": num(c["scheduled_tribes__st_"]),
                "obc": num(c["other_backward_classes__obc_"]), "other": num(c["others"])},
            "education": e and {
                "illiterate": num(e["educational_standard___illiterate"]),
                "below_x": num(e["educational_standard___below_class_x"]),
                "x_to_grad": num(e["educational_standard___class_x_and_above_but_below_graduation"]),
                "graduate": num(e["educational_standard___graduate"]),
                "technical": num(e["educational_standard___holding_tech__degree_diploma"]),
                "post_graduate": num(e["educational_standard___post_graduate"])},
            "religion": rel and {
                "hindu": num(rel["hindu"]), "muslim": num(rel["muslim"]),
                "sikh": num(rel["sikh"]), "christian": num(rel["christian"]),
                "other": num(rel["others"])},
            "s436a_eligible": a and num(a[
                "number_of_inmates_eligible_for_pre__mature_release_under_section_436a___total"]),
            "s436a_released": a and num(a[
                "number_of_inmates_released_under_section_436a_of_cr_p_c____total"]),
            "district_court_pending": dc and num(dc["_total"]),
            "population_2011": pop.get(k),
            "sc_pct": (scst.get(k) or {}).get("sc_pct"),
            "st_pct": (scst.get(k) or {}).get("st_pct"),
        })

    national = {
        "inmates": num(occ_tot["inmate_population___total"]),
        "capacity": num(occ_tot["available_capacity___total"]),
        "occupancy": num(occ_tot["occupancy_rate_in_percentage____total"]),
        "convicts": num(typ_tot["convicts___total__col_6_"]),
        "undertrials": num(typ_tot["undertrials___total__col_10_"]),
        "detenues": num(typ_tot["detenues___total__col_14_"]),
        "wait": {b: num(dur_tot.get(b + "___total")) for b, _ in BANDS},
        "caste": {"sc": num(cst_tot["scheduled_castes__sc_"]),
                  "st": num(cst_tot["scheduled_tribes__st_"]),
                  "obc": num(cst_tot["other_backward_classes__obc_"]),
                  "other": num(cst_tot["others"])},
        "religion": {"hindu": num(rel_tot["hindu"]), "muslim": num(rel_tot["muslim"]),
                     "sikh": num(rel_tot["sikh"]), "christian": num(rel_tot["christian"]),
                     "other": num(rel_tot["others"])},
        "education": {
            "illiterate": num(edu_tot["educational_standard___illiterate"]),
            "below_x": num(edu_tot["educational_standard___below_class_x"]),
            "x_to_grad": num(edu_tot["educational_standard___class_x_and_above_but_below_graduation"]),
            "graduate": num(edu_tot["educational_standard___graduate"]),
            "technical": num(edu_tot["educational_standard___holding_tech__degree_diploma"]),
            "post_graduate": num(edu_tot["educational_standard___post_graduate"])},
        "s436a_eligible": num(s436_tot[
            "number_of_inmates_eligible_for_pre__mature_release_under_section_436a___total"]),
        "s436a_released": num(s436_tot[
            "number_of_inmates_released_under_section_436a_of_cr_p_c____total"]),
        "district_court_pending": num(dc_tot["_total"]),
        "high_court_pending": num(hc_tot["_total"]),
        "sc_pct": india_scst.get("sc_pct"),
        "st_pct": india_scst.get("st_pct"),
    }

    pend_age = [{"band": r["age_wise_particulars"],
                 "civil": num(r["civil_cases"]), "criminal": num(r["criminal_cases"]),
                 "total": num(r["_total"])}
                for r in S["pendency_age"]["rows"] if not is_total(r["age_wise_particulars"])]

    high_courts = sorted(
        ({"name": (r["high_court"] or "").strip(), "pending": num(r["_total"])}
         for r in hc_rows), key=lambda x: -(x["pending"] or 0))

    out = {
        "_source": raw["_source"],
        "_licence": raw["_licence"],
        "_fetched": raw["_fetched"],
        "_built_by": "scripts/build-justice-explorer-data.py",
        "_caveats": [
            "Prison figures are a single-day census as on 31 December 2023, not a "
            "count of everyone held during the year. A person released in November "
            "does not appear.",
            "Population and SC/ST shares are Census 2011, the most recent enumerated "
            "count India has, since the 2021 census was not held. A rate per 100,000 "
            "is therefore 2023 prisoners over people counted in 2011.",
            "'Undertrial' means a person in custody whose trial has not concluded. "
            "They have not been convicted of the offence they are held for.",
            "Court pendency counts cases, not people, and one person can be party to "
            "several. District and high court figures are as reported to Parliament "
            "on the dates given in the source titles, not the same day as the prison "
            "census.",
        ],
        "bands": [{"key": b, "label": lab} for b, lab in BANDS],
        "caste_excluded": sorted(rejected),
        "national": national,
        "states": sorted(states, key=lambda s: s["name"]),
        "pendency_age": pend_age,
        "high_courts": high_courts,
    }

    js = payload_for_page(out)
    serialised = json.dumps(out, ensure_ascii=False, indent=1)
    if check_only:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != serialised:
            print(f"FAIL - {OUT.name} is stale. Run "
                  "`python3 scripts/build-justice-explorer-data.py`.")
            return 1
        print(f"  {OUT.name} is current")
    else:
        OUT.write_text(serialised, encoding="utf-8")
    rc = sync_page(js, check_only)
    if rc:
        return rc

    ut = national["undertrials"]
    print("PASS" if check_only else f"wrote {OUT.relative_to(ROOT)}")
    print(f"  {len(states)} states/UTs, {len(high_courts)} high courts")
    print(f"  {national['inmates']:,.0f} prisoners at {national['occupancy']:.1f}% "
          f"of capacity; {ut:,.0f} undertrials "
          f"({100*ut/national['inmates']:.1f}%)")
    print(f"  {national['district_court_pending']:,.0f} cases pending in district "
          f"courts, {national['high_court_pending']:,.0f} in high courts")
    with_caste = sum(1 for s in states if s["sc_pct"] is not None and s["caste"]
                     and s["caste"]["sc"] is not None)
    print(f"  {with_caste}/{len(states)} states have a caste comparison "
          f"({len(rejected)} population rows rejected as inconsistent)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
