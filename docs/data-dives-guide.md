# Data Dives Guide

## What Are Data Dives?

Data Dives are **independent data investigations**. Each one takes a single public dataset, interrogates it with original charts, builds a clear argument — and, just as importantly, spells out what the numbers *can't* show. They are ImpactMojo's data-journalism format: closer to an investigative brief than a lesson or a reading list.

All Data Dives are **free, browser-based, and require no login**. Every chart is drawn on the page (no external services), carries a data table behind it, and names its source.

### How a Data Dive Differs from a Deep Dive

- **A Deep Dive** curates the *literature* on a question — an annotated reading list with a point of view. Many authors, sequenced and annotated.
- **A Data Dive** interrogates the *data* on a question — original analysis of one dataset, with charts we build and an argument we make. One dataset, dug into.

If you want to know *what to read* on a topic, use a [Deep Dive](deep-dives-guide.md). If you want to know *what the numbers say*, use a Data Dive.

---

## The Data Dives

| Data Dive | Topic | Dataset | Charts | Link |
|-----------|-------|---------|--------|------|
| **The Welfare Spending Paradox** | Public Finance | RBI State Finances 2025-26 | 3 | [Open](/DataDives/state-welfare-budgets.html) |

Browse all Data Dives at [/DataDives/](/DataDives/).

---

## How a Data Dive Is Built

Each Data Dive follows the same honest structure:

1. **The finding** — a one-sentence headline of what the data shows, stated up front.
2. **Stat tiles** — the three or four numbers that anchor the story.
3. **Chart-led sections** — two to four sections, each pairing narrative with a chart we drew ourselves. Every chart has a title, a plain-English note on what higher/lower means, a data table, and a source line.
4. **"What this data can and can't tell you"** — a mandatory methodology block. Stocks vs flows, allocation vs delivery, association vs causation, coverage caveats. This is the part that separates a data dive from a hot take.
5. **Sources & data** — every source linked so readers can check our working.
6. **Go deeper** — links to the matching Deep Dives and courses.

### Editorial principles

- **Charts are honest by construction.** Single-hue magnitude bars, reference lines for averages, direct value labels, and explicit "associational, not causal" language on any scatter. No dual axes, no truncated baselines that exaggerate a gap, no chartjunk.
- **Show the working.** Every chart ships a data table; every number is sourced.
- **State the limits.** A Data Dive that doesn't tell you what it *can't* prove isn't finished.
- **Accessible and theme-aware.** Charts render in light and dark, carry an `aria-label` description, and degrade to a table.

---

## For Educators

- **As a data-literacy teaching case.** Walk students through the "What this data can and can't tell you" block — stocks vs flows, allocation vs delivery — as a live lesson in reading official statistics critically.
- **To pair with courses and Deep Dives.** The Welfare Spending Paradox pairs with the [Politics of Targeting](/DeepDives/politics-of-targeting.html) and [Health Systems and UHC in South Asia](/DeepDives/health-systems-uhc-south-asia.html) Deep Dives, and with development-economics and MEL courses.
- **As a prompt for replication.** Point research assistants at the source dataset and ask them to reproduce a chart, then extend it (per-capita spending, trends over time) — the natural next questions each dive leaves open.

---

## Authoring a New Data Dive

1. Copy `/DataDives/state-welfare-budgets.html` (the reference implementation) to `/DataDives/<slug>.html` and rewrite the content. Keep the `<style>` block and the chart-renderer `<script>` — they are self-contained, theme-aware, and accessible.
2. Edit only the data arrays at the bottom of the chart script. The chart API is:
   - `barChart(mountId, { data:[{label,value,hl?}], max, ticks, avg:{value,label}, suffix?, tipLabel? })`
   - `scatterChart(mountId, { data:[{label,x,y}], xMin, xMax, yMax, xTicks, yTicks })`
3. Add an entry to `data/data-dives.json`.
4. Wire cross-references: `index.html` (Data Dives section + footer explore list), `data/search-index.json`, `sitemap.xml`, this guide's table, and a `### For Learners` bullet in `docs/changelog.md`.
5. Validate: `python3 -m json.tool data/data-dives.json` and `python3 -m json.tool data/search-index.json`, plus `python3 scripts/check-mojibake.py`.

See `/DataDives/_template.html` for the annotated skeleton.

---

## Related

- [Deep Dives Guide](deep-dives-guide.md) — the reading-list companion format
- Skill `tufte-viz` and `dataviz` — the visualization principles behind the charts
- Skill `deep-research` — for sourcing and verifying the underlying data
