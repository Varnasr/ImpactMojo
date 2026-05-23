# Changelog

What's new on ImpactMojo. For the full technical changelog, see [CHANGELOG.md](https://github.com/ImpactMojo/ImpactMojo/blob/main/CHANGELOG.md) in the repository.

## v10.26.0 — May 23, 2026 (Practice Packs series launched)

A new content type on ImpactMojo: **Practice Packs**. Short, focused 3-hour sprints that take a practitioner from a job-to-be-done to a finished artefact. Sits between blog posts (read in 10 min) and flagship courses (multi-week commitment) — designed for the working practitioner with a real project waiting on a defensible artefact.

### For Learners

- **New section**: `/practice-packs/` — landing page listing the series (1 live, 9 upcoming)
- **First Practice Pack — SEL Evaluation: Design & Instruments** (PP01). 4 modules + capstone. Walk in with an SEL programme; walk out with a drafted evaluation design (research question, instruments, data plan, reporting outline). Includes 5 copy-to-clipboard templates.
- Nav link added to homepage; "New" badge.

### Roadmap (visible on landing page)

PP02 ToR Writing · PP03 Survey Instrument Design · PP04 Logframe Building · PP05 Activity-Based Costing · PP06 Focus Group Discussion · PP07 Critiquing Evidence Papers · PP08 Stakeholder Mapping · PP09 Donor Reporting · PP10 Building an MEL System from Scratch

## v10.25.5 — May 23, 2026 (Framework diversity propagated to SEL Course + Deep Dive)

After adding framework plurality to the SEL Simulation Game (v10.25.4), audited the SEL flagship course and the SEL Evaluation Deep Dive. Both had the same gaps. This release closes them.

### For Learners

- **SEL Course** now opens with an explicit "Frameworks We Draw From" section explaining how the course integrates CASEL, SEE Learning, WHO Life Skills, Delhi's Happiness Curriculum + EMC, Indian indigenous traditions (Tagore, Krishnamurti, Aurobindo, Nai Talim), and NEP 2020's full provisions (including teacher-side: NPST, 50-hr CPD, 4-yr B.Ed., teacher autonomy).
- **SEL Eval Deep Dive** expanded from 28 to 32 readings: added SEE Learning, NCERT AEP, Indian indigenous traditions, Delhi EMC; expanded NEP entry to surface teacher-side provisions.

## v10.25.4 — May 23, 2026 (SEL Simulation — Parent mode + framework diversity)

Addresses two cofounder feedback items: the game was missing a Parent perspective, and it framed NEP 2020 almost entirely from the child-facing side while leaning heavily on CASEL.

### For Learners

- **New Parent mode (5th lens)** in the SEL Simulation game. Six rounds covering: withdrawn child at dinner, teacher complaint, broken friendship, the day you snapped (modelling regulation), NEP school SEL outreach, and exam pressure + peer self-harm. Tracks Trust, Wellbeing, Connection, Modeling. India-specific adolescent helplines surfaced at end (iCall, Vandrevala, MANAS).
- **Framework plurality** — game now explicitly draws from CASEL, SEE Learning, WHO Life Skills, Delhi Happiness Curriculum + EMC, Indian indigenous traditions, and NEP 2020 (including its teacher-side provisions). Previous version was CASEL-heavy and child-focused on NEP.

## v10.25.3 — May 23, 2026 (ToR post — fix duplicate illustrations, all 4 napkin.ai)

The previous version rendered both the napkin.ai PNG and the inline SVG fallback simultaneously (the SVG's default style was set unconditionally, not only via the `onerror` handler), producing the impression of figures stacked back-to-back with no text between them. Fixed by removing all 4 SVG fallbacks now that real napkin.ai PNGs exist for every figure — including diagram 4 (research types), which previous attempts kept oversimplifying but a fresh prompt produced cleanly.

## v10.25.2 — May 23, 2026 (ToR post — research-types section + napkin.ai diagrams)

Expansion of the ToR blog post (v10.25.1) addressing a second common failure mode — clients asking for the wrong *type* of research — and upgrading three of the four diagrams to real napkin.ai-generated visuals.

### For Learners

- **New section: "What Kind of Research Do You Actually Need?"** — Covers three dimensions (question type: outcome vs process tracing vs theory-based; evidence type: quant vs qual vs mixed; time dimension: cross-sectional vs pre-post vs longitudinal vs retrospective) with the three common mismatches we see weekly.
- **Real napkin.ai diagrams** replace the inline SVG placeholders for the Anatomy of a ToR, Budget Tiers, and Pipeline diagrams. The research-types diagram still uses the inline SVG fallback because it shows all 9 sub-options + 3 mismatches, which napkin's summarisation can't preserve.

## v10.25.1 — May 23, 2026 (ToR-writing blog post)

Adds a single blog post answering one of the most common cofounder/client questions: how to write a Terms of Reference (or SoW, or RFP) that actually gets you useful research from an agency — and how to cost it honestly in India.

### For Learners

- **How to Write a ToR That Gets You Useful Research** — Practical, opinionated guide covering the nine ingredients of a good ToR, five common anti-patterns, India 2026 budget benchmarks (₹2L / ₹10L / ₹40L tiers with what each actually buys), and a pre-send checklist. Includes three inline diagrams (anatomy of a ToR, budget tiers, pipeline + failure points).

### Notes

- Diagrams are inline SVG in the napkin.ai style. PNG fallback paths exist at `assets/images/blog/writing-a-tor-for-research/illustration-{1,2,3}.png` — drop real napkin.ai exports there to swap.

## v10.25.0 — May 22, 2026 (Five-piece cofounder feature batch)

A five-deliverable release driven by cofounder feature requests — extending coverage of social-emotional learning, teacher evidence, livelihoods, and reflective practice. All evidence-grounded, India-context, practitioner-oriented.

### For Learners

- **SEL Simulation Game (4 modes)** — Step into Social-Emotional Learning from four chairs: teacher facing classroom dilemmas, program designer with a ₹40 lakh budget, evaluator deciding what can actually be known, or student (Anika, 12) navigating a school year. Each mode draws on NEP 2020, CASEL, and India-specific SEL research; scenarios are evidence-grounded with explicit "what the evidence shows" reflections after each choice.
- **Livelihoods in India: Rural, Urban, and Skills** (flagship course) — Comprehensive treatment across three modules: rural (NRLM/SHGs, MGNREGA, agriculture, financial inclusion); urban (informal sector, gig economy, vendors, domestic workers); skills (Skill India, apprenticeships, women's labour force participation, returns to training). Built for practitioners, evaluators, and policy actors who need both the policy landscape and the methodological rigour to read the field critically.
- **Teacher Evidence Lab** (interactive lab) — Filter 30+ teacher-effectiveness interventions by evidence quality, cost (per teacher per year), India relevance, type, and outcome. Built from rigorous evaluations 2000–2024: TaRL, contract teachers, pay-for-performance, mentoring, cascade training, multi-grade pedagogy, Mindspark, and more. Each card includes honest summary of what the evidence does and doesn't show.
- **SEL Evaluation in India** (deep dive) — Working syllabus on the methods that work and don't work for evaluating SEL in Indian school contexts. 28 readings across foundations, India evidence base, measurement, design choices, operational wisdom, and critiques. Includes opinionated "what works, what doesn't" summary.
- **Knowing What You Want** (blog) — A reflection on the quiet, hardest, most-skipped step in development work — actually knowing what you want, before you build the theory of change for it. Includes a 90-minute, 7-question exercise. Pairs naturally with the SEL course self-awareness material.

### Added

- `/Games/sel-simulation-game.html` (Game 17)
- `/Labs/teacher-evidence-lab.html` (Lab 12)
- `/DeepDives/sel-evaluation-india.html` (Deep Dive 6)
- `/blog/knowing-what-you-want.html` (Blog post)
- `/courses/livelihoods/` (Flagship 13)
- Entries added to `data/search-index.json` (5 entries), `catalog_data.json` (livelihoods), `data/deep-dives.json` (SEL eval), `sitemap.xml` (5 URLs)
- Blog card added to `blog.html`

### Changed

- Content counts updated sitewide: **53 courses (13 flagship + 40 foundational), 12 labs, 17 games, 6 deep dives** — was 52 / 11 / 16 / 5.

## v10.24.0 — May 20, 2026 (Flagship course chrome normalization)

Reader feedback was that the 12 flagship courses "looked different from each other" — mobile and desktop both. Over a session of audits, ran a line-by-line comparison against `devecon` (canonical) and closed the drift across 9 incremental PRs.

### For Learners

- **Consistent course experience** — all 12 flagship courses now share the same mobile and desktop chrome, so switching between Public Policy and Gender Studies (and the other 10) no longer feels like switching sites.
- **Mobile hamburger works on every course** — the menu button is in the same place on each course and tapping outside the open drawer closes it.
- **Accessibility widget present on every course** — the UserWay button is pinned right-middle on all 12, so font size / contrast / readability controls are one tap away regardless of course.

### Changed

- **Footer**: all 12 courses now render the same 3-column footer (Learn / Connect / Support / legal links / Docs link). Replaced 4 divergent footer patterns and removed a duplicate `<footer>` block in SEL.
- **Mobile (390px)**: body font 16px, sidebar drawer 280px, mobile-header height 56px, mobile-header top offset 0 — uniform across all 12. Was: body ranged 15–17px, drawer ranged 240–280px, header anchored 0–6px from top.
- **Desktop (1440px)**: sidebar width 260px, hero H1 `clamp(2.5rem, 5vw, 3.5rem)` (→ 56px) — uniform across all 12. Was: sidebars 260/280px split 8/4; H1 sizes ranged 38.4–56px.
- **Theme storage key**: unified `impactmojo-theme` localStorage key across all 12 (was: 6 different keys).
- **Sidebar drawer toggle class**: `.sidebar.active` across all 12 (was: 2 courses used `.sidebar.open`).

### Fixed

- **devai** — hamburger button was invisible because a broken UserWay script (`data-account="xxxx"` placeholder) rendered as a giant blue button covering the right side of the mobile-header. Replaced with canonical config.
- **devai** — mobile-header element order was reversed (LOGO → HAM). Reordered to canonical HAM → LOGO → THEME.
- **dataviz** — `.mobile-menu-btn` had `position: fixed; top: 12px; left: 12px;` taking it out of the flex flow and floating over the "ImpactMojo" logo. Moved back into the flex container.
- **dataviz, gandhi** — UserWay accessibility widget rendered as a dark/black box at the default top-right position because the positioning CSS (`.uwy.userway_p5`, `.uwy .uai`) was missing. Added.
- **gender, pubpol** — no UserWay accessibility widget at all. Added.
- **devai, dataviz** — tapping outside the open mobile sidebar didn't close it. Added the `<div class="sidebar-overlay">` element, the canonical backdrop CSS, and the click handler.
- **Mobile quiz options** — text was wrapping one word per line at narrow viewports because long words inside flex containers had no overflow control. Added `min-width: 0; overflow-wrap: anywhere` to quiz option containers.

### Out of scope (deliberately deferred)

- gender + SEL mobile-header use a 44px spacer instead of the canonical theme toggle. Each course uses a different theme system (`.im-theme-btn` with `data-imtheme`) which needs a small per-course glue layer to wire up properly.
- devai + SEL are missing the `.sidebar-collapse-btn` (the desktop chevron that shrinks the sidebar to icons).
- gender's mobile-header brand text is "Gender Studies" instead of "ImpactMojo" — may be intentional, awaiting decision.

## v10.23.10 — May 1, 2026 (Handouts emoji → SVG)

Closed the open finding from v10.23.9: replaced **all 1,317 emoji instances** across 63 handout files (144 unique characters) with inline Sargam-style stroke SVGs.

- Mapping: viewBox 0 0 24 24, stroke 1.5px, currentColor — visually consistent with the Sargam icon family already used in DeepDives and the homepage nav.
- Self-contained inline SVGs (no sprite/CDN dependency) so handouts remain print-portable.
- Each modified file got a one-time `.hi-emoji { width: 1em; height: 1em; vertical-align: -0.15em; display: inline-block; }` rule injected into its existing `<style>` block so SVG sizing follows surrounding `font-size`.
- Skipped emojis inside `<script>` and `<style>` blocks (3 instances) to avoid breaking JS data structures.

Verification: 0 body emojis remain in any handout. File count unchanged (84 HTML + 1 PDF).

## v10.23.9 — May 1, 2026 (Handouts audit)

Audited the 85 handouts (84 HTML + 1 PDF across 10 top-level Track directories).

### Render bug fixed: stale TRACK_MAPPING in handouts.html

The `TRACK_MAPPING` config in `handouts.html` had **5 of 6** keys that didn't match disk folder names. As a result, only "Policy and Economics Track" was being rendered with its proper colour/order/displayName — the other 5 tracks were silently being grouped into "Other Resources" (alphabetical fallback). Fixed:

| TRACK_MAPPING key was | Now (matches disk) |
|---|---|
| Data Analysis Track | Data and Technology Track |
| Gender Studies Track | Gender Equity and Inclusion Track |
| Research Methods Track | Monitoring Evaluation and Learning Track |
| Philosophy Law and Governance | Philosophy Law and Governance Track |
| Health Communication and Wellbeing | Health Communication and Wellbeing Track |

Also added 4 missing top-level mappings that exist on disk but weren't in TRACK_MAPPING: **Education and Pedagogy**, **Thematic Areas**, **Cross Cutting Resources**, **Quick Reference Cards**. All 4 will now render with proper display names, colours, and order rather than as "Other Resources".

### Typo fix

Renamed `Handouts/Thematic Areas/South Aisa Region/` → `South Asia Region/`.

### Count correction

Catalog and README claimed "400+ handouts" — actual count is 85. Updated catalog hd1 description (400+ → 85) and 3 README references.

### Open finding (not fixed): emojis in 62 of 84 handouts

Approximately **1,000+ emoji instances** across 62 print-optimised handout files (📊 🎯 💡 🔍 etc., used as visual scanning aids in reference cards). Replacing them with inline SVGs would be ~12× the work of the dt-companion replacement and risks regressions in 8.5×11" print layouts. Flagged for explicit decision before action.

## v10.23.8 — May 1, 2026 (Flagship modules audit)

Audited the 12 flagship courses for module-count drift between the actual `id="module-N"` anchors in each course's `index.html` and the counts claimed in catalog descriptions and homepage flagship cards. 5 drifts (catalog) and 3 drifts (homepage) found and fixed:

| Course | Actual | Was-catalog | Was-home | Fix |
|---|---|---|---|---|
| Gandhi | 13 | 13 ✓ | 12 ✗ | home → 13 |
| Devecon | 13 | 13 ✓ | 12 ✗ | home → 13 |
| Dataviz | 12 | 13 ✗ | 12 ✓ | catalog → 12 |
| DevAI | 12 | 13 ✗ | 12 ✓ | catalog → 12 |
| MEL | 14 | 13 ✗ | 13 ✗ | both → 14 |
| SEL | 13 | 12 ✗ | 13 ✓ | catalog → 13 |

7 of 12 flagships were already accurate (POA, Media, Law, PubPol, PubChoice, Gender, plus the 3 fixed-on-one-side above had a correct second source). Lexicon term counts (claimed 50–83 across courses) cannot be verified from the static HTML — terms are loaded dynamically (Supabase). Trusting existing claims.

## v10.23.7 — May 1, 2026 (BookSummaries deep-pass)

Brand audit on all 31 BookSummary companion pages:

- **30 of 31 clean** for viewport, meta description, OG, GA, Amaranth fonts, im-topbar with Browse, and no emojis.
- **dt-companion.html** (Design Thinking) had **54 emojis** across 24 unique characters (lightbulb, map, puzzle, magnifier, target, megaphone, etc.) used as decorative icons in tabs, author avatar, concept hero icons, and the toolkit cards. Replaced all 24 with inline Lucide-style stroke SVGs and added `svg { width: 1em; height: 1em }` rules so existing parent `font-size` continues to control the size.
- **Title cross-check**: all 31 catalog titles match the canonical title inside each BookSummary HTML file.

## v10.23.6 — May 1, 2026 (3 new 101-courses, 2 superseded)

### New courses

Three native slide-deck courses (1280×720 presentation format) shipped:

- **Work, Labour & Livelihoods 101** (12 sections) — SNA boundary, care economy, sustainable-livelihoods framework, agrarian question, migration, non-farm economy. **Replaces** the old `decent-work.html` and `livelihood-basics.html` (both Gamma-iframe pages absorbed into this comprehensive course).
- **Caste Studies 101** — varna and jati, Ambedkarite thought, the political economy of caste, anti-caste movements, the politics of measurement.
- **Public Finance & Budgeting 101** — fiscal architecture, Union and state budgets, finance commissions, budget transparency in India.

### Cross-references updated

- `catalog.html`: c28 retitled from "Decent Work For All 101" to "Work, Labour & Livelihoods 101" (URL repointed); 2 new entries appended (c40 caste-studies, c41 public-finance-budgeting). Filter chip 39 → 41. Hero copy 38 → 41 foundational courses.
- `index.html`: courses-modal entry for Livelihoods 101 retitled to Work, Labour & Livelihoods 101 with new URL + description; duplicate Decent Work modal item removed.
- `data/search-index.json`: 3 new entries appended.
- `sitemap.xml`: 2 old `<url>` entries removed; 3 new added.
- `_redirects`: 4 new 301 redirects so `/101-courses/decent-work` and `/101-courses/livelihood-basics` (both with and without `.html`) point at the replacement.
- Files deleted: `101-courses/decent-work.html`, `101-courses/livelihood-basics.html`.

## v10.23.5 — May 1, 2026 (Premium tools audit)

Audited the Premium tools surface against `premium.html` and `docs/faq.md` (both list 9 tools across two tiers).

- **Catalog dedup**: removed duplicate Code Converter entry — `p3` (Statistical Code Converter Pro) and `p5` (Code Converter Pro) both pointed at the same `code-converter-pro.html`. Kept the canonical title and merged the better description.
- **Catalog rename**: `p2` was titled "Qualitative Research Lab Pro" — actual product is "Qualitative Insights Lab Pro" (per premium.html marketing). Renamed in catalog and aligned the tool's own `<title>`/meta/h1 (8 occurrences) from the abbreviated "Qual Insights Lab Pro" to the full canonical name.
- **Catalog backfill**: added 4 missing premium tools — TOC Workbench Pro (live, was previously only in search-index), DevData Practice (coming soon), Visualization Cookbook (coming soon), DevEconomics Toolkit (coming soon). Catalog filter chip updated 7 → 9 to match catalog hero copy.
- **Search-index backfill**: added 2 missing tool entries (`code-converter-pro.html`, `qual-insights-lab.html`) so site search now resolves all premium tools.
- **Description rewrites**: tightened catalog descriptions for 4 entries to match the more specific copy on premium.html (Field Notes, RQ Builder, TOC Workbench, Code Converter).

All 3 tool files in `/premium-tools/` verified clean for viewport, meta description, OG, GA, Amaranth, im-topbar with Browse + Premium, no emojis.

## v10.23.4 — May 1, 2026 (Labs audit)

Audited all 11 labs for metadata, brand, and link consistency.

- **toc-lab.html**: was missing the Browse link (only lab without one). Injected into the existing `top-controls` div, styled to match its local `premium-link` pattern.
- **Search-index re-typing**: 2 entries (`/BookCompanionTools/budget-template-generator.html`, `/BookCompanionTools/sample-size-calculator.html`) were mistyped as `type: lab`. They are calculators that complement book summaries, not labs. Re-typed to `tool` with category `Book Companion Tools`. Lab count in search-index now matches the 11 files on disk.

All 11 labs verified clean: viewport meta, title, meta description, OG, GA, Amaranth/Inter fonts, im-topbar with Browse + Premium, no emojis.

## v10.23.3 — May 1, 2026 (Games audit)

### Brand alignment

Audited all 16 games for metadata, brand, and link consistency.

- **Emoji removal**: 14 emojis in `climate-action-game.html` (mitigation/adaptation actions + climate events) and 5 in `public-health-game.html` (cards + interventions) replaced with inline Lucide-style stroke SVGs. CSS updated so SVG sizing follows parent `font-size` via `width: 1em; height: 1em`. The platform brand standard is Sargam icons / inline SVGs only — no emojis.
- **Stale Netlify URLs in catalog**: `https://therealmiddle.netlify.app`, `https://risk-reward-be.netlify.app`, `https://cooperationparadox.netlify.app/` were pointing at external subdomains while the self-hosted versions exist at `/Games/real-middle-india.html`, `/Games/risk-reward-game.html`, `/Games/cooperation-paradox-game.html`. Catalog now points at the self-hosted files.
- **Missing topbar**: `externality-game.html` had the `.im-topbar` CSS but no rendered nav element. Injected the standard im-topbar with home/Browse/Premium links.

All 16 games verified for: viewport meta, title, meta description, OG tags, GA, Amaranth/Inter fonts, back-link to homepage, im-topbar with Browse + Premium buttons.

## v10.23.2 — May 1, 2026 (Reference Libraries audit)

### Count alignment across pages

Reference Library counts had drifted across landing cards, hero descriptions, and meta tags. Audited the 6 libraries and aligned every claim to the actual data:

| Library | Was | Now | Source |
|---|---|---|---|
| Dataverse hero + `<meta>` | 215+ | 270+ | `data/dataverse.json` (272 items) |
| Dataverse home card | 259 | 272 | – |
| NudgeKit hero + `<meta>` + ld-json | 200+ | 203 | `data/bct-repository.json` |
| NudgeKit home card | 16 Categories | 26 Categories | – |
| Flagship summary chip | 11 | 12 | Public Choice added in v10.23.0 |
| Dataverse meta `totalItems` | 271 | 272 | actual category sum |

ImpactLex (390 terms) and FieldCases (200 cases / 117 countries) verified accurate.

## v10.23.1 — May 1, 2026 (later same day)

### Catalog → complete content index

`/catalog.html` was advertising `Games (16)` while only listing 12 in its JS array, and was missing entire content types (BookSummaries, Reference Libraries, Handouts). Now indexes **128 items across 9 content types**:

| Type | Count | Filter chip |
|---|---|---|
| Flagship | 12 | `Flagship (12)` |
| Course | 39 | `Courses (39)` |
| Lab | 11 | `Labs (11)` (was advertised as 10) |
| Game | 16 | `Games (16)` (was 12 in array) |
| Premium | 7 | `Premium (7)` |
| Deep Dive | 5 | `Deep Dives (5)` |
| **Book Companion** | **31** | **NEW** |
| **Reference** | **6** | **NEW** |
| **Handouts** | **1 collective** | **NEW** |

- 4 missing games added: Algorithm's Dilemma, Epidemic Response, Climate Action, Care Economy.
- 1 missing lab added: Gender Analysis Lab.
- 31 BookSummaries added with hand-written descriptions (no SEO boilerplate).
- 6 Reference Libraries indexed: ImpactLex, DevDiscourses, FieldCases, PolicyDhara, Dataverse, NudgeKit.
- Handouts surfaced as a single collective entry → `/handouts.html` (didn't bloat with 400 individual entries).
- 3 new card-type pill colours (book-summary amber, reference indigo, handout teal) with light + dark variants.

### Browse access from inner pages

Inner pages (12 flagship courses, 31 BookSummaries, 5 DeepDives, 4 lexicons, 3 premium tools, climate-trace-india, 76 other utility pages — **132 total**) had only a minimal `im-topbar` with a logo and Premium button. Users on a course page couldn't reach the catalog or any reference library without going home first.

Injected an `Browse` link (4-square grid icon) into the `im-topbar` of every inner page, just left of the Premium button. Points at `/catalog.html`. Inline CSS so each page's topbar look is preserved.

The homepage was deliberately left untouched — it has the full nav with Specials dropdown.

## v10.23.0 — May 1, 2026

### Public Choice — 12th flagship course

- New flagship course at [/courses/pubchoice/](/courses/pubchoice/) — *Public Choice: Decisions, Incentives & Institutions*. 13 modules synthesising the Virginia school (rent-seeking), Bloomington school (commons), and New Institutional Economics, with cases from India, Bangladesh, Pakistan, Sri Lanka, and Nepal.
- 83-term interactive lexicon at [/courses/pubchoice/lexicon.html](/courses/pubchoice/lexicon.html).
- 13 modules imported to Supabase `course_content` table (matches the convention used by the other 11 flagships: module 1 is preview, 2–13 require auth).
- Wired into homepage flagship grid, catalog filter (`Flagship (12)`), JSON-LD ItemList, sitemap, and search-index.

### Performance — measurable wins shipped

- **Extracted 215 KB of inline `<style>` from index.html → `/css/imx-main.css`.** Browser now caches CSS across navigations and downloads it in parallel with HTML. Index.html dropped from 645 KB raw / 96 KB brotli → 431 KB raw / 64 KB brotli.
- **HTML edge caching** added in `netlify.toml` (`/*.html` and `/` → `public, max-age=300, must-revalidate`). Repeat-visit TTFB fell from ~1.4s to **175 ms** (8× faster). Netlify auto-purges on deploy so freshness is preserved.
- **Auth scripts deferred** at the bottom of body (`@supabase/supabase-js`, state-manager, config, auth) so the parser doesn't block on them.

### Specials nav — accordion subgroups

The Specials dropdown was a flat list of 13 items. Now organised into 4 collapsible subgroups (all closed by default):
- **Reference Libraries** — ImpactLex · DevDiscourses · FieldCases · PolicyDhara · Dataverse · NudgeKit
- **Long-form Reading** — Book Companions · Deep Dives
- **Practice & Programs** — Flagship Courses · ToC Workbench · Dojos · Challenges
- **Behind the Scenes** — Live Projects

Single-open accordion behaviour (opening one section closes others). On mobile the cap on dropdown height was lifted so accordion items aren't clipped.

### Navigation — fixes after we found a chain of subtle bugs

- All 13 Specials items now use absolute URLs (`/#flagship-courses` etc.). Previously several used bare anchors (`#flagship-courses`, `#case-studies`, `#dev-discourses`) or relative paths (`dataverse.html`, `challenges.html`) that only worked from the homepage.
- **`js/router.js` now respects hash fragments before path-based routes**. Earlier, navigating to `/#flagship-courses` would match the home route and scroll to top, overriding the hash. Now the hash always wins. (This was the actual cause of "clicking Flagship Courses does nothing.")
- Capture-phase click handler on accordion items as a belt-and-suspenders force-navigate.
- Mobile: tapping an accordion item now closes the menu so the user can see the page scroll.
- `js/faq-bank.js` line 167 had a string-literal syntax error (stray `""`) that was killing the whole file's parsing — fixed.

### Mobile — margin safety net + Public Choice hero text fix

- Sitewide mobile (≤768px) padding floor on top-level sections, hero blocks, and the named `imx-*` sections so cards stop bleeding into the viewport edge. Tightens to 1rem on screens ≤380px.
- Public Choice hero had two inline `color: rgba(255,255,255,...)` text elements with no dark background — invisible against the page bg. Switched to theme variables; the "Boundary with Politics of Aspiration" callout uses a new `.pubchoice-boundary-strong` class with proper light/dark amber.

### Reference libraries — eliminated `on-web.link`

- `/policydhara`, `/devdiscourses`, `/impactlex` (and `/dictionary`) all redirected through `on-web.link` shortlinks. PolicyDhara was already 404'ing.
- Replaced with **Netlify Edge Functions** that proxy directly from `varnasr.github.io/PolicyDhara` and `varnasr.github.io/development-discourses`, injecting a `<base href="...">` into the HTML so relative asset paths resolve.
- ImpactLex now points at the in-repo `/impactlex/` (was migrated locally in v10.20.0).
- Updated 4 pages that linked to `on-web.link/DevDiscourses` (`index.html`, `premium.html`, `updates.html`, `content-marketing-kit.html`).

### DevEcon CSS shim

- `courses/devecon/index.html` referenced `var(--indigo)`, `var(--cyan)`, `var(--orange)`, `var(--success)` in 17 places (quiz, phase, reflection, feedback components) but never defined them. Quiz number circles rendered faint, dashed reflection borders disappeared, correct/incorrect feedback bands lost colour. Defined the four aliases in each of the 4 `:root` / theme blocks.

### Misc polish

- Catalog `.track-filter.active` failed WCAG AA contrast (sky-500 text on sky-500-at-20% background). Fixed to amber-700 light / sky-300 dark — same WCAG-safe pattern used for `.card-type.course` two CSS blocks above.

## v10.22.0 — April 29, 2026

### Deep Dives — curated reading lists from named scholars

A new content type: themed annotated reading lists curated by named scholars and practitioners.

- **5 starter lists**, each with ~11 readings across 4 themed sections, curated by a rotating mix of Sukhmeet Bedi (Editor's Pick) and the ImpactMojo Editorial team (House Pick — open to invited curators):
  - Reading Indian Political Economy — *Sukhmeet Bedi*
  - Impact Measurement: Foundations and Frontiers — *ImpactMojo Editorial*
  - Climate and Just Transitions in South Asia — *Sukhmeet Bedi*
  - Caste, Identity, and Development — *ImpactMojo Editorial*
  - Data, Power, and the Global South — *ImpactMojo Editorial*
- **Mixed media**: each list draws on books, papers, podcasts, datasets, and articles — not just academic citations.
- **Annotated, not just cited**: every reading carries 2–4 sentences explaining why it matters and how it fits the syllabus.
- **Open call for curators**: practitioners and scholars who'd like to curate a Deep Dive can pitch via [/contact.html?topic=DeepDive](/contact.html?topic=DeepDive).
- **Live at**: [/DeepDives/](/DeepDives/) · also linked from the homepage and the Specials nav dropdown.

## v10.21.0 — April 28, 2026

### Infrastructure & Claude Code setup

- **New Supabase user**: `taranga.sriraman@gmail.com` added with organization tier (highest plan), learner role (non-admin). Password reset email sent.
- **Global Claude Code setup**: Promoted 16 reusable skills to `~/.claude/` (AI APIs, platform ops, content creation, research). Available across all projects.
- **Vendored best practices**: claude-code-synthesis guides synced to `~/.claude/vendor/` with `/sync-guides` command for updates.
- **Housekeeping skill upgraded**: Added Google Analytics verification (step 11) and comprehensive branding consistency checks (step 12) covering footer, fonts, language selector, theme toggle, UserWay accessibility widget, paper plane SVGs, blob decorations, cookie consent, speed dial FAB, and SVG icon sprite.
- **Dataverse**: Added "Awesome Open Source AI" catalog (271 total items).

## v10.20.0 — April 23, 2026

### ImpactLex — full upgrade + migration home

- **Brought ImpactLex into ImpactMojo** at `/impactlex/`. The external Varnasr/ImpactLex PWA becomes a legacy reference; the live glossary now deploys with the rest of the site.
- **Unified data source** — merged the external ImpactLex glossary (35 terms + 5 case studies + 10 formulas) with the 10 course-specific lexicons (MEL, Gender, DataViz, DevAI, DevEcon, Gandhi, Law, PoA, PubPol, SEL). Deduped by term, unioned course tags. **Total: 390 terms, 5 case studies, 10 formulae.**
- **New backend: InstantDB** (evaluated against Supabase; kept separate to isolate anonymous glossary traffic from learner data). App is snapshot-first with real-time enhancement — works fully offline against the local JSON snapshot, progressively hydrates from InstantDB when configured.
- **Refreshed look** — matches ImpactMojo V3 design system: Amaranth + Inter typography, sky-blue gradient, paper-plane decoration, 3-mode theme toggle, fixed topbar, full footer. PWA-installable with service worker.
- **New features**:
  - Instant fuzzy search across term, acronym, aliases, definition
  - Category + course filters (6 categories × 10 courses)
  - Term-of-the-Day (rotates daily)
  - Deep-linkable term pages at `/impactlex/term.html?id=<slug>`
  - Bookmarks (localStorage; cloud-ready when logged in)
  - Contribute-a-term form with offline queue + moderation workflow
  - Cross-reference chips (click related terms to jump)
- **AI rewrite pipeline** — `scripts/impactlex-ai-rewrite.mjs` drafts definitions in ImpactMojo voice (South Asia–grounded, practitioner-focused) via Gemini / Grok / DeepSeek fallback chain, with a review UI at `/impactlex/review.html`.
- **Course lexicon cross-links** — every course lexicon page now shows a banner linking into the filtered ImpactLex view with its term count.
- Updated `index.html` nav + resource card, `data/search-index.json`, `sitemap.xml`, `README.md`, `docs/impactlex-guide.md`.

## v10.19.0 — April 13, 2026

### Book Summaries
- **3 new book companions** added (28 → 31 total):
  - *Principles for Navigating Big Debt Crises* — Ray Dalio (2018) — debt cycles, deleveraging, and central bank policy across 48 historical cases
  - *Handbook for IPCC Authors: Climate Communications* — Corner, Shaw & Clarke (Climate Outreach, 2018) — six evidence-based principles for climate communication
  - *Storytelling to Accelerate Climate Solutions* — Coren & Wang (Springer, 2024) — 20 chapters on narrative approaches to climate action
- Updated BookSummaries index page: hero count 28→31, filter counts (dev-econ 5→6, leadership 7→9)
- Added entries to `data/search-index.json`, `sitemap.xml`, and docs

## v10.18.1 — April 12, 2026

### Fixed
- **README.md** — labs 19→11 (separated into Labs, Tools & Calculators, and Premium Tools sections), added 2 missing flagship courses (Gender Studies, Public Policy), added BookSummaries (28) and AI Study Companions (11) to content table, replaced Formspree with Netlify Forms in tech stack, updated version to 10.18.0 and date to April 12.
- **content-marketing-kit.html** — games 15→16, labs 10→11, flagship courses 9→11 across ~20 locations including social posts, carousel slides, brand guidelines, and content calendars. Fixed carousel counts (17 Labs→11, 27 Books→28).
- **ImpactMojo_PressKit.html** — foundational courses 39→38.
- **docs/roadmap.md** — moved Cohort-Based Learning, Notification System, Sample Size Calculator, Budget Template Generator, and full accessibility audit from "In Progress"/"Planned" to "Recently Completed". Added v10.13–v10.18 release entries. Added BookSummaries expansion and native deck migration to "In Progress".

### GitHub
- Closed Q1 2026 milestone (past due, all issues resolved).
- Replied to issue #361 (skill validation workflow proposal).
- Updated issue #272 (BookSummaries target raised from 5-8 to 40+).

## v10.18.0 — April 12, 2026

### Fixed
- **Sitemap coverage** — added 87 missing URLs to `sitemap.xml`: 2 flagship courses (gender, pubpol), 35 foundational 101-courses, 23 BookSummaries, 18 blog posts, and 9 public pages (transparency, dataverse, bct-repository, challenges, climate-trace-india, portfolio, live-projects, toc-builder, verify-certificate). Total URLs: 84 → 171.
- **Stale `101.impactmojo.in` links** — migrated ~100 legacy subdomain links to local paths across `js/faq-bank.js`, `js/bookmarks-compare.js`, `js/learning-tracks.js`, `js/game-agents.js`, and 4 docs files. All course links now point to `/101-courses/*.html`, all lab links to `/Labs/*.html`.
- **Search index phantom labs** — removed 6 duplicate/phantom lab entries from `data/search-index.json` (survey-design-lab, sampling-lab, logframe-builder, data-cleaning-lab, indicator-design-lab, toc-workbench); added missing entries for design-thinking-lab, mel-design-lab, and community-lab. Lab count: 17 → 13 (11 labs + 2 BookCompanionTools).
- **Content count drifts** — fixed `docs/content-guide.md` (flagship 9→11, labs 19→11, BookSummaries 27→28), `premium.html` ("47 foundational courses, labs & games" → "48 free courses, 11 labs & 16 games"), `catalog.html` JS comments (COURSES 39→38, LABS 10→11).
- **21 `.DS_Store` files** removed from git tracking (already in `.gitignore`).

## v10.17.0 — April 12, 2026

### Added
- **Formspree eliminated** — all 12 forms migrated to Netlify Forms with email notifications to info@impactmojo.in. Platform now runs on two services (Netlify + Supabase) instead of three.
- **Engagement email pipeline** — 5-email drip sequence for new users: welcome (Day 0), first course nudge (Day 3), content showcase (Day 7), re-engagement (Day 14), premium soft pitch (Day 21). Runs daily at 08:00 IST via Netlify Scheduled Function.
- **Streak tracking** — learning streaks now increment automatically on every login and reset after a missed day.
- **Post-certificate email** — congratulations email with shareable certificate link, sent automatically when a user completes a course. Includes a subtle premium mention for free-tier users.
- **Monthly newsletter** — automated content roundup on the 15th of every month, pulls highlights from the changelog and content counts from the search index. Includes premium and one-time support links.
- **Premium sales letter** at `/premium-letter.html` — long-form conversational page explaining Premium membership, tools, and pricing. Written as a personal letter, not a pricing table.
- **Practitioner Starter Kit** at `/starter-kit.html` — curated collection of 10 essential handouts for development practitioners.
- **Branded email template** — all platform emails now use a branded template with navy gradient header, ImpactMojo logo, amber accent bar, and dark footer.
- **Resend email integration** — domain verified (DKIM, SPF, DMARC) for transactional emails from notifications@impactmojo.in. Free tier: 3,000 emails/month.
- **Notifications infrastructure** — `notifications` and `notification_preferences` tables created in Supabase with RLS policies, indexes, and auto-preference creation for new signups.

### Changed
- **Netlify form detection** — enabled form processing (was previously disabled: `ignore_html_forms: true`) and configured email notifications for all 12 forms.
- **Supabase Edge Functions** — `send-notification` updated with engagement-drip and monthly-update endpoints; `issue-certificate` updated with congratulations email and premium upsell.

## v10.16.0 — April 8, 2026

### Added
- **Accessibility Statement page** at `/accessibility.html` — formal WCAG 2.1 Level AA conformance statement covering our commitment, how we test (axe-core + pa11y-ci on every PR), accessibility features, known limitations (Gamma iframes, canvas-based games, third-party widgets), and how to report a barrier. Linked from the footer Legal section, the About page, and the UserWay widget's statement link.
- **README badges** — new "Accessibility: WCAG 2.1 AA" shield and a live GitHub Actions status badge for the `accessibility.yml` workflow, so the repo README reflects current CI truth.
- **About page accessibility callout** — a brief paragraph in "What We Offer" announcing WCAG 2.1 AA conformance with a link to the full statement.

### Changed
- **UserWay widget** — the commented-out `data-statement_url` and `data-statement_text` config was wired up to point at the new `/accessibility.html` page. The UserWay button now surfaces "Our Accessibility Statement" as a direct link.

## v10.15.0 — April 8, 2026

### Fixed
- **Content-count drift sitewide** — `about.html`, `catalog.html` (hero + meta + filter chip), `transparency.html`, `org-dashboard.html`, `404.html`, `podcast.html`, Supabase signup/invite email templates, and four `docs/` files all now show the canonical counts: **48 courses (11 flagship + 38 foundational), 11 labs, 16 games**. Previously several of these still read 39 / 10 / 12.
- **`index.html` flagship stat line** — corrected "10 Flagship Courses" → "11 Flagship Courses" in the "What's Included" strip above the flagship course cards.
- **`catalog.html` missing flagship cards** — added Constitution & Law, Public Policy, and Gender Studies to the catalog JS data (they existed on the homepage but weren't in the catalog's searchable/filterable collection). Flagship filter chip now reflects the real 11.

### Changed
- **Learning Track Quiz promoted** — the "Not sure where to start?" quiz CTA has moved from section #6 of the homepage (below Learning Pathways) to directly under the hero area, right after the Daily Tip + Surprise Me buttons. First-time visitors now see the 5-question recommender before any content library listings.
- **New hero quiz shortcut** — added a tertiary "Not sure? Take the 5-question quiz →" link in the hero CTA block for visitors who want to jump straight to the quiz without scrolling.

## v10.14.0 — April 7, 2026

### Added
- **Device-mode default theme** on 70 pages — pages now follow your OS dark/light preference on first paint, and the 3-button theme toggle still wins if you pick explicitly
- **Underlined inline links** in body paragraphs across 74 content pages — meets WCAG 2.1 AA §1.4.1 (Use of Color)
- **CC BY-NC-SA 4.0 attribution** backfilled into 17 handouts that were missing it — all 84 handouts are now uniform
- **Premium topbar link** added to 11 main-site pages
- **Language translation widget** on `climate-trace-india` and `transparency`
- **Paper plane decoration** on `courses/gender/lexicon` and `courses/pubpol/lexicon`; footer landmark on `courses/pubpol/lexicon`

### Changed
- **WCAG AA muted-text contrast** bumped across 115 files (light and dark modes both)
- **`catalog.html` card colours** (ratings + track labels) darker to pass WCAG AA
- **Theme system unified** on a single `im-theme` localStorage key — picks now carry across games, account page, main site, and handouts consistently
- **Brand fonts** — two BookSummaries pages migrated back to the canonical Inter / Amaranth / JetBrains Mono stack
- **10 unbuilt course cards** marked "Coming Soon" with a disabled amber-pill card style
- **39 pictographic emoji → Sargam line icons** across 10 pages

### Fixed
- **Handout 404s** — self-hosted with URL-encoded paths (was linking to a stale mirror)
- **Duplicate headers** on 28 pages where the `im-topbar` was hiding the main site navigation
- **121 stale `101.impactmojo.in` course links** rewritten to self-hosted equivalents

## v10.13.0 — April 5, 2026

**What changed for you:** Three 101 foundational course decks — Development Economics, MEL, and Climate Essentials — are now native HTML slide decks replacing the old Gamma.app embeds. Full 100-slide presentations with light/dark theme, keyboard/touch navigation, interactive Chart.js charts, and content that fills the screen properly.

### Native 101 Slide Decks
- **Development Economics 101** — 100 slides, 12 sections, 17 interactive charts covering poverty, growth, agriculture, human capital, finance, trade, evidence, South Asia, and contemporary challenges
- **MEL 101** — 100 slides covering theory of change, indicators, data collection, evaluation methods, learning systems, and MEL failures
- **Climate Essentials 101** — 100 slides covering climate science, adaptation, mitigation, policy, finance, and South Asian climate vulnerability

### Design System
- Shared CSS/JS template for all future native 101 decks
- Light/dark/system theme toggle
- Keyboard arrows, touch swipe, and fullscreen navigation
- Responsive viewport scaling (1280×720 base, scales to any screen)
- Proportionally sized components that fill the slide area

## v10.12.0 — March 31, 2026

**What changed for you:** Repository moved to the ImpactMojo GitHub org, and documentation is now self-hosted (no more GitBook). Translation support expanded to 14 South Asian languages.

### Organization Migration
- Repository moved from `Varnasr/ImpactMojo` to `ImpactMojo/ImpactMojo` — all site links updated
- GitHub org configured with avatar, description, topics, and profile README
- Netlify reconnected to the new org

### Documentation
- **Self-hosted Docsify** replaces GitBook at `impactmojo.in/docs/`
- Dark/light/system theme toggle, full-text search, code copy buttons, prev/next navigation
- **Google Translate** with 14 languages: Hindi, Bengali, Marathi, Tamil, Telugu, Kannada, Malayalam, Gujarati, Punjabi, Odia, Assamese, Urdu, Nepali, Sinhala
- ImpactMojo branded design (Inter + Amaranth fonts, brand gradient, responsive)

### Infrastructure
- MCP server package scope: `@varnasr` → `@impactmojo`
- `_redirects` updated for self-hosted docs and new GitHub Pages URLs

## v10.11.0 — March 28, 2026

**What changed for you:** Two new blog posts with napkin.ai-generated illustrations, and a significantly expanded Content Marketing Kit with 5 new LinkedIn posts covering all 6 learning tracks.

### Blog
- **Introducing the ImpactMojo MCP Server** — Full blog post explaining what MCP is, what our server offers (11 tools, 3 resources), how to connect it, and example prompts
- **Open source blog illustrations** — Real napkin.ai infographics replacing placeholder images on the GitHub open dev ecosystem post
- Both posts include 2 professionally generated infographics via Napkin.ai API

### Content Marketing Kit
- **5 new LinkedIn posts** (LI-11–LI-15): Climate & Sustainability, Gender & Inclusion, AI in Development, Book Companions, MCP Server Launch
- **Broadened scope** — Renamed "Economics Games" to "Interactive Learning Games" across assets; ImpactMojo covers 6 tracks, not just economics
- **Corrected counts** throughout (9 courses, 16 games, 270 dataverse tools)
- **Redesigned brochure thumbnails** with content previews
- Total assets: 25 → 30

## v10.10.0 — March 27, 2026

**What changed for you:** ImpactMojo now has its own MCP server — connect any AI assistant (Claude Desktop, Claude Code, Cursor, etc.) to search our entire knowledge base: 700+ content items, 203 BCT techniques with South Asian context, 270 dataverse tools, India climate data, 16 economics games, and practice challenges.

### MCP Server (`/mcp-server/`)
- 11 tools: search_content, lookup_bct, search_bcts, list_bct_categories, browse_dataverse, search_dataverse, list_challenges, get_challenge, list_courses, get_game_info, query_climate_data
- 3 resources: platform overview, content catalog, learning tracks
- TypeScript + `@modelcontextprotocol/sdk`, stdio transport
- Published as `@impactmojo/impactmojo-mcp-server` on GitHub Packages
- Added to Dataverse catalog as `impactmojo-mcp`
- Auto-publishes on `mcp-server/v*` tags via GitHub Actions

## v10.9.1 — March 26, 2026

**What changed for you:** Housekeeping release — corrected lab counts across all documentation, added 13 missing games to sitemap for better search discoverability, and cleaned up stale branches.

### Documentation Consistency Sweep
- Fixed **lab count** from 19 → 11 across 12 files (faq, why-impactmojo, mojini-guide, learning-design, getting-started, transparency, premium, platform-overview, content-catalog, welcome, catalog.html, README)
- Fixed **foundational courses count** from 47 → 39 in platform-overview.md
- Fixed **docs/README.md version** from 10.1.0 → 10.9.0
- Fixed **Dataverse count** from 215 → 247 in docs/README.md and welcome.md
- Fixed **BookSummaries count** from 1 → 5 in content-catalog.md summary table
- Added 4 missing games (Climate Action, Gender Equity, Public Health, Digital Ethics) to content-catalog.md games table
- Added Gender Studies Lab to content-catalog.md labs table

### Sitemap
- Added 13 missing games to sitemap.xml (was 3, now all 16 games listed)

### Repository Cleanup
- Pruned stale remote tracking refs
- Identified 9 stale branches for deletion (no open PRs)
- Created pre-housekeeping backup of index.html

## v10.9.0 — March 24, 2026

**What changed for you:** Every page on ImpactMojo now has a consistent look and feel — unified fonts, mobile-responsive design, 3-mode theme toggle (System/Light/Dark), floating paper plane, standardized footer, and a sticky navigation bar with a home link and Premium button.

### Design System — Sitewide Audit & Fix (242 pages)
- Applied **ImpactMojo font stack** (Amaranth body, Inter headings, JetBrains Mono code) with `!important` global overrides across all 242 inner pages
- Added **3-mode theme toggle** (System / Light / Dark) with `localStorage` persistence and device-default loading
- Added **floating paper plane SVG** matching the homepage design to every page
- Added **sticky top bar** with ImpactMojo home link and Premium button on all inner pages
- Added **full 4-section footer** (About, Legal, Quick Links, Resources) to all pages missing it
- Fixed **mobile viewport meta tag** on BookSummary React pages that were missing it
- Added **dark mode CSS variables** and light/dark theme support across the entire site
- Added **GitBook documentation** link to the footer (Resources section) across all pages

### Documentation
- Updated typography docs to reflect 242-page coverage
- Updated roadmap: moved sitewide font/theme audit to Recently Completed
- Added GitBook docs link to index.html footer and all inner page footers

## v10.8.5 — March 22, 2026

**What changed for you:** Two new econometrics book companions added, press kit page linked in site navigation and footer, and book summary counts updated to 5 books / 100+ chapters.

### Book Summaries
- Added **Basic Econometrics** (Gujarati & Porter, McGraw-Hill) — 22-chapter interactive companion covering regression, hypothesis testing, multicollinearity, and more
- Added **Econometrics by Example** (Gujarati, Palgrave Macmillan) — 20-chapter hands-on companion with real-world examples
- Updated BookSummaries landing page: 3→5 books, 55+→100+ chapters

### Press Kit
- Added Press Kit link to About Us navigation dropdown
- Added Press Kit link to footer (About ImpactMojo section)
- Added Press Kit to search index and sitemap

### Documentation
- Added Press Kit page to GitBook navigation (About section)
- Updated content-catalog, platform-overview, and book-summaries-guide with new book entries

## v10.8.4 — March 22, 2026

**What changed for you:** Two new interactive book companions added — Debraj Ray's *Development Economics* and Andrew Pressman's *Design Thinking*. BookSummaries page now matches site-wide theming.

### Book Summaries
- Added **Development Economics** (Debraj Ray, Princeton 1998) — 18-chapter interactive companion with models, concepts, and exercises
- Added **Design Thinking** (Andrew Pressman, Routledge 2019) — 10-chapter interactive companion covering creative problem-solving methodology
- Updated BookSummaries landing page: 1→3 books, 30+→55+ chapters
- Applied ImpactMojo theming: floating paper airplane SVG, standard 4-section footer with social links, responsive + reduced-motion support

## v10.8.3 — March 22, 2026

**What changed for you:** Documentation consistency sweep — fixed stale content counts across all GitBook docs and added API key management template.

### GitBook Documentation Fixes
- Fixed stale lab counts (10→19) in 6 docs: why-impactmojo, getting-started, premium, transparency-and-commitments, mojini-guide, learning-design
- Fixed stale game counts (12→16) in 3 docs: getting-started, premium, learning-design
- Fixed stale Dataverse counts (215→247) in 3 docs: why-impactmojo, premium, dataverse-guide

### Developer Experience
- Added `.claude/.env.keys.example` template documenting all 6 API keys (GitHub, Supabase, Netlify, Gamma, Gemini, Napkin)

## v10.8.2 — March 21, 2026

**What changed for you:** Housekeeping release — updated counts, fixed stale references, and refreshed documentation.

### Documentation & Consistency
- Updated README version to 10.8.1 and date
- Fixed stale content counts across admin dashboard, analytics, transparency, and catalog pages (courses: 41→48, games: 11→16, labs: 15→19)
- Updated Dataverse count from 215 to 247 in index.html and transparency page
- Updated catalog.html header to reflect 11 flagship courses and 19 labs
- Refreshed sitemap.xml lastmod dates to 2026-03-21
- Created pre-housekeeping backup of index.html

## v10.8.1 — March 21, 2026

**What changed for you:** All blog posts now display napkin.ai illustrations, and blog card thumbnails on the blog index page are fixed.

### Blog Illustrations
- Generated 10 napkin.ai illustrations (2 per post) for the 5 blog posts that were missing them: from-learner-to-leader, learning-by-doing, meal-demystified, sample-size-matters, theory-of-change-pitfalls
- Fixed 4 mismatched thumbnail paths in blog.html (smart-vs-spiced → meal-demystified, toc-pitfalls → theory-of-change-pitfalls, qualitative-data → learning-by-doing, why-free → why-impactmojo-exists)

## v10.8.0 — March 20, 2026

**What changed for you:** Two major new features — **cohort-based learning** and **notifications** — plus auth reliability improvements.

### Cohort-Based Learning (#144)
- Organization admins can now create training cohorts with start/end dates, member enrollment, and deadline tracking
- Cohorts show per-member progress bars, average cohort progress, and a color-coded deadline countdown
- **Discussion threads** within each cohort — members can post, view, and delete messages
- Cohort status automatically updates (Upcoming → Active → Completed) based on dates
- Database tables: `cohorts`, `cohort_members`, `cohort_discussions` with full row-level security

### Notification System (#145)
- **In-app notifications** on the account page with unread badges and mark-as-read
- **Email notifications** via Resend (free 3K/month) with branded HTML templates
- **Streak reminders** — automatic email when users with active streaks go inactive for 2+ days
- **Cohort deadline alerts** — notifies enrolled members when cohorts end within 3 days
- **Notification preferences** — per-user opt-in/out for 6 notification categories (course updates, streaks, cohort deadlines, cohort discussions, assignments, certificates) plus digest frequency (daily/weekly/never)
- New Edge Function: `send-notification` with streak-reminders, cohort-deadlines, and manual notification endpoints

### Auth & Login Fixes
- Faster session recovery (1.5s + 4s safety nets, reduced from 3s)
- Increased SIGNED_OUT debounce to 1000ms to handle slow token refresh
- Aggressive session recovery from localStorage when in-memory state is lost
- Window `load` event recovery for `defer` script timing on homepage

### Other Fixes
- Gender equity game: SVG viewBox expanded to prevent Madhubani art head clipping
- Info asymmetry game: Pattachitra frame images now full-width on mobile
- API token documentation added for Gemini, DeepSeek, Grok, Sarvan.ai, Gamma
- Git standards verified across all 29 repos (29/29 compliant, dependabot active)
- 3 stale Claude Code branches cleaned up

## v10.7.0 — March 20, 2026

**What changed for you:** A brand new content type — **BookSummaries** — is now available under Specials. Developer tooling also improved with Claude Code skills and API key management built into the repo.

### BookSummaries
- New `BookSummaries/` directory for self-contained interactive book companions
- First entry: The Handbook of Social Protection — 24 chapters, 17 evidence findings, 5 learning pathways, 40+ glossary concepts
- Interactive data tools: SP Spending Explorer, Targeting Simulator, Transfer Size Calculator, Cost-Effectiveness chart
- Added to Specials dropdown navigation, content catalog, sitemap, and search index

### Claude Code Integration
- 6 repo-level skills for Claude Code (github-ops, netlify-ops, supabase-ops, gemini-ai, gamma-ops, housekeeping)
- SessionStart hook auto-loads API keys for Gemini, Gamma, DeepSeek, Grok, and Sarvan.ai
- All API tokens documented in project config

## v10.6.0 — March 19, 2026

**What changed for you:** ImpactMojo courses are being converted to Gamma presentation decks for visual delivery.

### Gamma API Integration
- 23 of 38 course decks synced as Gamma presentations
- Automated sync pipeline via `scripts/gamma-sync.js`
- Premium tools (Field Notes Pro, Workshop Pro) launched with server-side auth-gate

## v10.5.1 — March 19, 2026

**What changed for you:** Admin accounts are now protected from accidental tier downgrades, and premium resource access is more reliable.

### Premium Resource Gating
- All premium tools now use server-side JWT auth-gate on Netlify Edge Functions
- 7 new interactive workshop templates (ToC, Logframe, Chart Selector, Stakeholder Mapping, Empathy Canvas, Policy Canvas, AI Canvas) added to the premium listing
- Field Notes Pro — 70 curated development economics field notes, now a premium tool

### Admin Fixes
- Admin tier protection: database trigger prevents client-side downgrades
- Profile fetch timeout increased and auto-retry added for slow connections
- Fixed JS syntax errors that broke the org dashboard

### Labs & Design
- 7 new interactive labs (Design Thinking, Impact Partnerships, Resource Sustainability, Policy Advocacy, MEL Design, MEL Plan Builder, Gender Analysis)
- All 19 labs aligned to ImpactMojo standard design (theme selector, floating decorations, sargamicon badges)
- Lab count updated from 12 to 19 across the platform

### Housekeeping
- Removed `mobile-index.html` — `index.html` is now fully responsive
- Updated all documentation counts (labs 10→19, games 12→16, Dataverse 215→247)

## v10.1.0 — March 16, 2026

**What changed for you:** The documentation you're reading right now was completely restructured to be useful for educators, not just developers. We also standardized code quality practices across all 29 ImpactMojo repositories.

### Documentation Overhaul
- New educator-friendly docs: Welcome, Platform Overview, Getting Started, Learning Design, Workshops & Facilitation, Certificates & Progress, FAQ
- New guides: Handouts Guide (how to use and print), Dataverse Guide (all categories explained), Glossary (plain-language tech terms)
- Existing docs rewritten with clearer, more accessible language

### Dataverse Page Update
- Added explanations for all 7 resource types (datasets, tools, platforms, APIs, MCP servers, resources, skills)
- Previously only 3 types were explained

### Git Standards (29 repos)
- Consistent code quality standards across all ImpactMojo repositories
- Automated security checks prevent accidental commits of sensitive files

### GitBook Docs Fix
- Fixed broken sidebar links in the documentation

## v10.1.0 — March 16, 2026

### Git Standards (29 repos)
- Propagated `.gitattributes`, `.editorconfig`, `.githooks/`, `.gitmessage`, `CODEOWNERS`, `SECURITY.md`, `dependabot.yml`, PR & issue templates across all 29 ImpactMojo repos
- Pre-commit hook blocks secrets, debugger, conflict markers; warns on console.log and large files
- Commit-msg hook enforces prefix convention (Add/Fix/Update/Translate/Docs/Refactor/Test/CI/Chore)
- Dependabot auto-configured per ecosystem (npm, pip, github-actions)

### GitBook Docs Fix
- Fixed broken sidebar links — added `/impactmojo/*` → `/docs/*` Netlify redirects

## v10.0.0 — March 16, 2026

**What changed for you:** The site looks more consistent — fonts are unified across all 80+ pages. Mobile experience is significantly improved with new content sections and fixed navigation.

### Visual Consistency
- Standardized fonts across all pages: Amaranth (body text), Inter (headings), JetBrains Mono (code)
- Previously, different pages used different fonts, creating an inconsistent experience

### Mobile Experience
- New "What's New" section on mobile homepage — see the latest courses and features at a glance
- New "Wall of Love" testimonials section on mobile — real feedback from learners in 6 languages
- Fixed hamburger menu and logo display issues on mobile

### Dashboard Improvements
- Smoother charts on admin and transparency pages
- Fixed a bug where dashboard tabs sometimes showed the wrong membership tier
- Polished the "Create Learning Path" modal for organizations

### Transparency
- New revenue model section showing how ImpactMojo sustains itself
- Clearer methodology for usage statistics

## v9.5.0 — March 15, 2026

**What changed for you:** You can now navigate between your account, organization, admin, and analytics dashboards from a single tab bar. Organizations can set up team training packages.

- Unified dashboard navigation across all dashboard pages
- Team training packages for organizations (pre-built paths, facilitator guides, assessment rubrics)
- Full-text search, offline access, and course assessments

## v9.1.0 — March 7, 2026

**What changed for you:** PolicyDhara (policy research resource) was added as the 4th free resource accessible from the homepage. Organization dashboards got a getting-started guide.

- PolicyDhara integration on homepage and navigation
- Organization dashboard: welcome guide, feature grid, roadmap preview
- Login improvements — faster and more reliable

## v9.0.0 — March 6, 2026

**What changed for you:** Premium tools are now properly secured — only subscribers with the right tier can access them. Community features launched.

- Secure access control for premium tools (VaniScribe, Qual Lab Pro, etc.)
- GitHub Wiki with 7 documentation pages
- GitHub Discussions with 12 seed conversations
- Automated quality checks for links and accessibility

## v8.0.0 — February 28, 2026

**What changed for you:** The homepage loads much faster — we moved 160KB of code out of the main page. The site now works better offline.

- Major performance improvement — homepage loads significantly faster
- Improved offline support with smarter caching
- Community channels added to the premium registration flow

## v7.0.0 — February 15, 2026

**What changed for you:** This is when ImpactMojo launched as a full platform with accounts, certificates, and premium features.

- Premium membership tiers (Explorer, Practitioner, Professional, Organization)
- User accounts with Google login and magic links
- 38 foundational courses across 6 learning tracks
- 12 economics simulation games
- 10 interactive labs
- ImpactLex dictionary (500+ terms)
- Dev Case Studies (200 cases from 117 countries)
- DevDiscourses (500+ curated papers and books)
- Multilingual support (English, Hindi, Tamil, Bengali, Telugu, Marathi)
- Coaching, workshop booking, and Dojos skill sessions
- Blog (Learning Loops) and Podcast (Between the Logframes)
