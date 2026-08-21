# 101 Course Decks Guide

## What the 101 decks are

ImpactMojo's **52 foundational courses** are slide decks you read in a browser. Each is a single self-hosted HTML page of roughly 100 slides, with a light/dark/system theme, keyboard and touch navigation, fullscreen, and interactive Chart.js figures where the argument needs a chart rather than a sentence.

They are not summaries of the flagship courses. A 101 deck is the shortest honest route into a subject: what the thing is, who it binds, what the numbers are, and what a practitioner is expected to know before walking into a meeting about it. A flagship course is the long version, with modules, readings, a lexicon and an assessment.

Every deck lives at `https://www.impactmojo.in/101-courses/{slug}.html`, needs no login, works offline once loaded, and prints.

### No third-party embeds

Earlier versions of this guide described decks generated through Gamma and displayed in an iframe. **That is no longer how any of them work.** All 52 decks were migrated to self-hosted native HTML; zero Gamma iframes remain. The practical consequences: nothing is served from a third-party domain, nothing breaks when an external service changes its embed, the decks are indexed by search engines, they render on a bad connection, and they can be packaged for an LMS (see [For educators](#for-educators)).

---

## What's in a deck

Every deck follows the same shape:

1. **Title card** — course name, track identity, ImpactMojo branding
2. **What this covers** — the agenda, stated as questions rather than headings
3. **Ten to twelve content sections** — concepts, tables, diagrams, and South Asian cases
4. **Charts where they earn their place** — each with the context above it and the reading below it, not a decorative graphic
5. **Check-your-understanding** — questions embedded in the deck
6. **Key takeaways and further reading** — including primary sources and where to find them

### Companion material

47 of the 52 decks also ship two companions:

- **Course Outline poster** — `/101-courses/poster/{slug}.html`, a one-page map of the deck, designed to print
- **Practice Workbook** — `/101-courses/practice/{slug}.html`, exercises that apply the deck to the reader's own work

The five most recent decks — **CSR & ESG**, **Data Protection & the DPDP Act**, **Disability Inclusion**, **GenAI for Practitioners** and **Safeguarding & PSEA** — do not yet have a poster or a workbook. That is a known gap, not a design decision.

---

## The 52 decks by track

### MEL, Research & Data Methods (14)

| Deck | Slug |
|------|------|
| MEL Basics 101 | `mel-basics` |
| Theory of Change 101 | `toc-workbench` |
| Logframe 101 | `logframe-101` |
| Impact Evaluation 101 | `impact-eval` |
| Cost Effectiveness 101 | `cost-effectiveness` |
| Survey Design 101 | `survey-design` |
| Qualitative Methods 101 | `qual-methods` |
| Mixed Methods 101 | `mixed-methods` |
| Research Ethics 101 | `research-ethics` |
| Observation to Insight 101 | `obs2insight` |
| Exploratory Data Analysis 101 | `eda-hhs` |
| Bivariate Analysis 101 | `bi-analysis` |
| Multivariate Analysis 101 | `multivariate-basics` |
| Item Response Theory 101 | `irt-basics` |

### Economics & Policy (7)

| Deck | Slug |
|------|------|
| Development Economics 101 | `dev-economics` |
| Political Economy 101 | `pol-economy` |
| Econometrics 101 | `econometrics-101` |
| Inequality Basics 101 | `inequality-basics` |
| Global Development Governance 101 | `dev-architecture` |
| Public Finance & Budgeting 101 | `public-finance-budgeting` |
| Fundraising Basics 101 | `fundraising-basics` |

### Gender & Equity (7)

| Deck | Slug |
|------|------|
| Gender Mainstreaming 101 | `gender-mainstreaming` |
| Women's Economic Empowerment 101 | `wee-studies` |
| Feminist Research 101 | `feminist-research` |
| Care Economy 101 | `care-economy-101` |
| Sexual Health 101 | `SRHR-basics` |
| Social Margins 101 | `social-margins` |
| Data Feminism 101 | `data-feminism` |

### Governance, Rights & Society (8)

| Deck | Slug |
|------|------|
| Indian Constitution 101 | `ind-constitution` |
| Post-Truth Politics 101 | `post-truth-101` |
| Decolonial Development 101 | `decolonize-dev` |
| Community Development 101 | `community-dev` |
| Environmental Justice 101 | `env-justice` |
| Disability Inclusion 101 | `disability-inclusion` |
| Safeguarding & PSEA 101 | `safeguarding-psea` |
| CSR & ESG 101 | `csr-esg` |

### Health, Climate & Wellbeing (6)

| Deck | Slug |
|------|------|
| Public Health 101 | `pub-health-basics` |
| Maternal Health 101 | `maternal-health` |
| Child Development 101 | `child-development` |
| Climate Essentials 101 | `climate-essentials` |
| SEL Basics 101 | `sel-basics` |
| Work, Labour & Livelihoods 101 | `work-labour-livelihoods` |

### Communication, Data & Digital (10)

| Deck | Slug |
|------|------|
| English for Development 101 | `eng-dev` |
| Visual Ethnography 101 | `visual-eth` |
| Data Literacy 101 | `data-lit` |
| Data Visualization 101 | `data-viz` |
| Behaviour Change Communication 101 | `bcc-comms` |
| Advocacy Basics 101 | `advocacy-basics` |
| Education and Pedagogy 101 | `edu-pedagogy` |
| Digital Ethics 101 | `digital-ethics` |
| GenAI for Practitioners 101 | `genai-practitioners` |
| Data Protection & the DPDP Act 101 | `data-protection-dpdp` |

Browse them all at [/101-courses/](https://www.impactmojo.in/101-courses/).

---

## How to read one

- **Navigate** with the arrow keys, `Space`, or by swiping. `F` toggles fullscreen.
- **Theme** follows your device by default; the three-button toggle overrides it.
- **Deep link** to a slide with `#s42` — the slide IDs are stable, so a link you put in a syllabus will still land in the right place next year.
- **Offline**: once a deck has loaded, it stays available. Flagship courses can also be downloaded explicitly from the course page.

---

## For educators

### A deck as a workshop

The ~100-slide format maps to a **90-minute session** if you are selective, or a half-day if you stop at every case:

1. **Frame it** (10 min) — the title card and the "what this covers" slides
2. **Work the content** (50 min) — pause at the case studies and let people argue
3. **Check understanding** (15 min) — run the embedded questions as a group activity, not a test
4. **Reflect** (15 min) — ask each participant to name one thing they will do differently

### Pair with handouts and games

- **Data Literacy** deck + the Data & Technology handouts for a full day
- **MEL Basics** handouts as pre-reading, deck as the session
- **Development Economics** deck after the **Public Good Game** or **Externality Game**
- **Climate Essentials** deck after the **Climate Action Challenge**
- **Political Economy** deck after **Cooperation Paradox** or **Prisoners' Dilemma**

Play the game first to create the experience, then use the deck to name what happened.

### Put a deck in your LMS

[LMS Export](https://www.impactmojo.in/lms-export) packages any 101 deck as **SCORM 1.2**, **SCORM 2004**, **IMS Common Cartridge 1.3**, or one self-contained HTML file. The package is built in your browser from the live deck, so it is never a stale copy. Our analytics, sign-in, database and translation code are stripped out before packaging and everything else is inlined, so the imported deck runs with no network and reports nothing back to us. SCORM marks the course complete when the learner reaches the final slide.

### Adapt it

The decks are licensed **CC BY-NC-ND 4.0**. You may share them, distribute them to participants, and post them on your organisation's LMS. Credit ImpactMojo and keep the non-commercial terms. If you want to remix or translate a deck for a specific context, [get in touch](mailto:hello@impactmojo.in) — we would rather help than have a bad copy circulate.

---

## Technical details

### How a deck is built

Decks are generated from Python, not by hand:

- **`scripts/deck_builder.py`** — the shared builder. `build()` assembles the page; helpers (`sec`, `divider`, `bullets`, `table`, `stats`, `twocol`, `flow`, `hbox`, `quote`, `terms`, `SRC`) emit the house components so every deck looks the same.
- **`scripts/gen_{slug}_deck.py`** — one generator per deck, holding that deck's content.
- **Charts** use Chart.js in the house `chart-slide-frame` pattern: context above the chart, the chart, and the reading below it. A deck degrades gracefully if Chart.js fails to load.

To regenerate a deck, edit its generator and run it; do not hand-edit the output HTML, or the next run will overwrite you.

### After adding or changing a deck

Follow the checklist in `.claude/rules/content-management.md`. In short: update `data/counts.json` first, then run `python3 scripts/check-counts.py`, add the page to `data/search-index.json` and `sitemap.xml`, wire it into `catalog.html` and `101-courses/index.html`, and record it in `docs/changelog.md`.

---

## Tips

- **Read it yourself first.** Note which cases land with your audience and which slides you will skip.
- **Don't rush the cases.** The South Asian examples are where the abstraction becomes real. Budget time to argue about them.
- **Sequence within a track.** For a multi-day training, run two or three decks from the same track — Data Literacy, then Bivariate Analysis, then Multivariate Analysis.
- **Print the poster.** For the 47 decks that have one, the Course Outline poster is the handout you want on the table.
- **Give people the deep link, not the deck.** `#s42` gets a reader to the slide you meant instead of the first one.
