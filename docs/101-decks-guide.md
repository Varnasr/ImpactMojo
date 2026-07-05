# 101 Course Decks Guide

## What Are the 101 Course Decks?

ImpactMojo's **47 foundational courses** are available as visual presentation decks — 60-slide interactive decks generated via [Gamma](https://gamma.app) with Indian folk art illustrations, consistent branding, and South Asian context throughout.

These aren't typical slide decks. Each one is a structured learning journey designed for self-study or facilitated workshops, with case studies drawn from development practice in India and South Asia. They are free to view, share, and use in educational settings.

All decks are accessible at `https://www.impactmojo.in/101-courses/{course-slug}.html` and require no login or download.

### Native HTML Decks (New — April 2026)

Three decks have been migrated from Gamma iframe wrappers to **self-hosted native HTML slide decks** with 100 slides each:

| Deck | Slides | Charts | URL |
|------|--------|--------|-----|
| Development Economics 101 | 100 | 17 Chart.js | [View](https://www.impactmojo.in/101-courses/dev-economics.html) |
| MEL Fundamentals 101 | 100 | — | [View](https://www.impactmojo.in/101-courses/mel-basics.html) |
| Climate Essentials 101 | 100 | — | [View](https://www.impactmojo.in/101-courses/climate-essentials.html) |

Native decks feature: light/dark/system theme toggle, keyboard/touch/swipe navigation, fullscreen mode, responsive viewport scaling, and interactive Chart.js visualisations. The shared template (`101-courses/native/shared/deck.css` + `deck.js`) is ready for all future 101 deck conversions.

**Workflow for new native decks:**
1. Generate 100-slide HTML in Claude Chat using an existing native deck as format template
2. Save/paste the output to `101-courses/{slug}.html`
3. Fix JS bugs (viewport split after slide 50, newlines in chart labels) and push

The remaining 35 decks still use Gamma iframe wrappers and will be migrated incrementally.

---

## What's in Each Deck

Every 101 deck follows a consistent structure across approximately 60–100 slides:

1. **Title card** — Course name, ImpactMojo branding, track identity
2. **Agenda** — Overview of what the deck covers
3. **10--12 content sections** — Core concepts with explanations, diagrams, and South Asian case studies
4. **Quiz / Assessment** — Check-your-understanding questions embedded in the deck
5. **Key Takeaways** — Summary of the most important points
6. **Glossary** — Definitions of key terms used in the deck
7. **Further Reading** — Curated references for deeper exploration
8. **Thank You** — Closing slide with license and attribution

### Branding and Design

- **Fonts**: Inter (body) + Amaranth (headings)
- **Theme**: Cornflower (consistent across all decks)
- **Footer**: ImpactMojo branding on every slide
- **License**: CC BY-NC-ND 4.0 — free to share and adapt for non-commercial use with attribution

---

## Indian Folk Art Styles by Track

Each track uses a distinct Indian folk art tradition for its illustrations, grounding the learning content in South Asian visual culture.

| Track | Art Style | Origin |
|-------|-----------|--------|
| **MEL & Research** | Warli | Maharashtra — white line art on terracotta backgrounds |
| **Data & Technology** | Gond | Madhya Pradesh — dot patterns, vibrant nature-tech fusion |
| **Policy & Economics** | Kalamkari | Andhra Pradesh — pen-drawn narrative scrolls |
| **Gender & Equity** | Madhubani | Bihar — bold outlines, bright fills, nature motifs |
| **Health & Communication** | Pattachitra | Odisha — scrollwork narrative art, bold outlines |
| **Philosophy & Governance** | Pichwai | Rajasthan — devotional temple art, rich detail |

---

## Available Decks

As of April 2026, **3 native HTML decks** are live (Dev Econ, MEL, Climate) and **22 of 39** Gamma decks have been generated. The remaining courses are being migrated from Gamma iframes to native HTML.

### MEL & Research

| Course | Status | Access |
|--------|--------|--------|
| MEL Fundamentals | Available | [View deck](/101-courses/mel-basics.html) |
| Qualitative Research Methods | Available | [View deck](/101-courses/qual-methods.html) |
| Observation to Insight | Available | [View deck](/101-courses/obs2insight.html) |
| Visual Ethnography | Available | [View deck](/101-courses/visual-eth.html) |
| Research Ethics | Available | [View deck](/101-courses/research-ethics.html) |
| Item Response Theory and Qualitative Assessment | Available | [View deck](/101-courses/irt-basics.html) |
| BCC and Communications | Coming Soon | — |
| Theory of Change Workbench | Coming Soon | — |

### Data & Technology

| Course | Status | Access |
|--------|--------|--------|
| Data Literacy for Development | Available | [View deck](/101-courses/data-lit.html) |
| Data Feminism | Available | [View deck](/101-courses/data-feminism.html) |
| EDA for Humanitarian/Health/Social Data | Available | [View deck](/101-courses/eda-hhs.html) |
| Bivariate Analysis | Available | [View deck](/101-courses/bi-analysis.html) |
| Multivariate Analysis | Available | [View deck](/101-courses/multivariate-basics.html) |
| Econometrics 101 | Available | [View deck](/101-courses/econometrics-101.html) |
| Digital Development Ethics | Available | [View deck](/101-courses/digital-ethics.html) |
| Education and Pedagogy | Coming Soon | — |
| Social Emotional Learning | Coming Soon | — |
| Poverty and Inequality | Coming Soon | — |
| Marginalized Identities and Development | Coming Soon | — |
| Decent Work for All | Coming Soon | — |
| Community-Led Development | Coming Soon | — |
| Decolonizing Development | Coming Soon | — |
| Environmental Justice | Coming Soon | — |

### Policy & Economics

| Course | Status | Access |
|--------|--------|--------|
| Development Economics | Available | [View deck](/101-courses/dev-economics.html) |
| Political Economy | Available | [View deck](/101-courses/pol-economy.html) |
| Cost-Effectiveness Analysis | Available | [View deck](/101-courses/cost-effectiveness.html) |
| English for Development | Available | [View deck](/101-courses/eng-dev.html) |
| Advocacy Fundamentals | Available | [View deck](/101-courses/advocacy-basics.html) |
| Livelihoods Fundamentals | Available | [View deck](/101-courses/livelihood-basics.html) |
| Climate Essentials | Available | [View deck](/101-courses/climate-essentials.html) |
| Post-Truth Politics | Deck Ready (PDF pending) | [View on Gamma](https://gamma.app/docs/07twqrzjtsnf49j) |
| Fundraising Fundamentals | Deck Ready (PDF pending) | [View on Gamma](https://gamma.app/docs/0j6oy9d9f60xevo) |
| Global Development Architecture | Deck Ready (PDF pending) | [View on Gamma](https://gamma.app/docs/n6gze051jrfnllw) |
| Indian Constitution and Development | Coming Soon | — |

### Gender, Equity & Inclusion

| Course | Status | Access |
|--------|--------|--------|
| Women's Economic Empowerment | Coming Soon | — |
| Sexual Rights and Health Basics | Coming Soon | — |
| Care Economy and Unpaid Work | Coming Soon | — |

### Health & Communication

| Course | Status | Access |
|--------|--------|--------|
| Public Health 101 | Coming Soon | — |

---

## How to Access the Decks

### Primary access

Visit `/101-courses/{course-slug}.html` in any browser. For example:
- [/101-courses/data-lit.html](/101-courses/data-lit.html) — Data Literacy for Development
- [/101-courses/mel-basics.html](/101-courses/mel-basics.html) — MEL Fundamentals
- [/101-courses/dev-economics.html](/101-courses/dev-economics.html) — Development Economics

### Gamma fallback

For decks marked "Deck Ready (PDF pending)", use the Gamma link directly. These decks are fully viewable on Gamma's platform — the only difference is that a downloadable PDF has not yet been exported.

### PDF downloads

Completed decks have PDF exports available. These are useful for offline use, printing, or sharing in low-bandwidth contexts.

---

## For Educators

### Using Decks in Workshops

The 60-slide format maps well to a **90-minute workshop session**:

1. **Introduction** (10 min) — Use the title card and agenda slides to frame the session
2. **Content walk-through** (50 min) — Work through the content sections, pausing at case studies for group discussion
3. **Quiz and discussion** (15 min) — Use the embedded quiz as a group activity
4. **Takeaways and reflection** (15 min) — Review key takeaways, ask participants to identify one concept they will apply

### Combining with Handouts

ImpactMojo offers 84 handouts in `/Handouts/` that pair well with the decks. For example:

- Use the **Data Literacy deck** alongside the Data & Technology track handouts for a full-day workshop
- Distribute the **MEL Fundamentals handouts** as pre-reading before presenting the deck
- Assign **Further Reading** references from the deck as follow-up homework

### Combining with Games

Several 101 courses have companion interactive games on the platform:

- **Development Economics** deck + **Public Good Game** or **Externality Game**
- **Digital Development Ethics** deck + **Digital Ethics** scenarios
- **Climate Essentials** deck + **Climate Action Challenge**
- **Political Economy** deck + **Cooperation Paradox** or **Prisoners' Dilemma**

Play the game first to create an experiential hook, then use the deck to build the conceptual framework.

### Customizing for Local Context

The decks are licensed CC BY-NC-ND 4.0, which means you can:

- **Adapt** — Add local case studies, translate key terms, adjust examples for your state or region
- **Share** — Distribute to participants, post on your organization's LMS
- **Remix** — Combine slides from multiple decks for a custom workshop

Please credit ImpactMojo and maintain the non-commercial, share-alike terms.

---

## Technical Details

### How Decks Are Built

Decks are generated programmatically using the **Gamma API** through an automated pipeline:

1. **Course content** is structured into a prompt with section headings, case studies, and assessment items
2. **Gamma API** generates the 60-slide deck with the cornflower theme and specified art style
3. **PDF export** is triggered automatically after successful generation
4. **Sync results** are logged to `data/gamma-sync-results.json` for tracking

### Sync Pipeline

- **Script**: `scripts/gamma-sync.js` handles the full generation and export workflow
- **Recovery**: The pipeline supports recovery — if a generation succeeds but PDF export fails (e.g., due to credit limits), the Gamma URL is preserved and export can be retried later
- **Status tracking**: Each course has a status in `gamma-sync-results.json`: `completed` (with or without export URL) or `error` (generation not yet attempted/failed)

### Current Pipeline Status

- **18 decks**: Fully completed with PDF export
- **4 decks**: Generated on Gamma, PDF export pending (credit-limited)
- **14 decks**: Awaiting generation (credit-limited)
- **Recovery date**: 2026-03-19 — pipeline recovered previously generated decks that were missing from local tracking

---

## Tips

- **Preview before presenting.** Walk through a deck yourself before using it in a workshop. Note which case studies resonate with your audience and which slides you might skip or expand on.
- **Use the glossary.** Development jargon trips people up. Point participants to the glossary slide when introducing new terms.
- **Don't rush the case studies.** The South Asian case studies are where abstract concepts become concrete. Budget time for participants to discuss how the example connects to their own work.
- **Download PDFs for field settings.** If you are running a workshop in an area with unreliable internet, download the PDF in advance. The decks work well projected from a laptop without a live connection.
- **Pair decks from the same track.** Running a multi-day training? Sequence two or three decks from the same track for cumulative learning — for example, Data Literacy followed by Bivariate Analysis followed by Multivariate Analysis.
