# Changelog

All notable changes to ImpactMojo are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [10.79.6] - 2026-06-23

### Added

- **Research to Action — poster series** (`/research-to-action/`). A new visual section with a wide central spotlight/lightbox album: a large featured poster, prev/next + keyboard navigation, a thumbnail filmstrip, click-to-zoom fullscreen lightbox, per-poster download, and `#n` deep-links. **Series 1** ships with 10 posters — What is Research to Action?, Start with the Right Question, Choosing the Right Research Design, Sample Size, Indicators That Measure What Matters, Five Common Biases, Correlation/Causation/Credibility, How to Read Findings Without Being Misled, From Findings to Decisions, and Communicating Research So People Use It. Source PNGs (~21 MB) were re-encoded to optimized JPEGs + thumbnails (~2 MB total). Brand shell (topbar, theme toggle, footer), search index (`RTA001`), sitemap, and homepage footer link added.

### For Learners

- **New "Research to Action" poster series** — a visual walk through turning research into decisions and impact, from asking the right question to communicating findings people actually use. Browse the spotlight album, open any poster full-size, or download them for your own workshops and classrooms.

## [10.79.5] - 2026-06-19

### Added

- **Web push notifications.** Learners can opt in (per device) on the account page to receive browser push notifications for streak and cohort-deadline reminders, extending the existing email + in-app notification system (#145). New pieces: a `push_subscriptions` table + `notification_preferences.push_enabled` column (migration `20260621_push_subscriptions.sql`); a `send-push` Supabase Edge Function (save/delete subscription + VAPID-signed delivery via `web-push`, dead-subscription pruning); `push`/`notificationclick` handlers in the service worker; a `js/push-notifications.js` opt-in module (VAPID public key, permission + subscribe flow); and a toggle in the account-page Notifications card. The `send-notification` function now also fires a best-effort push (wrapped so it never blocks email/in-app) on streak and cohort events. Backend (table, VAPID secrets, both functions) is deployed and smoke-tested on Supabase; the front-end opt-in goes live on the next `main` deploy.

## [10.79.4] - 2026-06-19

### Added

- **Rebuilt service worker — offline support without stale files.** The previous SW had been reduced to a self-unregistering stub (`js/pwa.js` actively cleared registrations) after a stale-cache bug. The new `service-worker.js` is **network-first for HTML/navigations** (always fresh online, cached fallback or `/offline.html` only when the network fails) and **stale-while-revalidate for static assets** (CSS/JS/images/fonts/JSON), with versioned caches purged on `activate` so a deploy can never serve stale files. It also wires up the previously-dead `js/offline.js` features: on-demand course download (`CACHE_COURSE`) and **background sync** of queued learner progress (`sync-progress`). User-downloaded course caches persist across SW versions. `js/pwa.js` now registers the SW (with prompt-free skip-waiting on update) instead of unregistering it.

### Fixed

- **Deep Dives count corrected to 20** on `premium.html` (3 places said "17") — matches `data/deep-dives.json` and the homepage. (Site-wide audit: courses 60, labs 13, games 134, book companions 54, handouts 84 all consistent.)

## [10.79.3] - 2026-06-19

### Fixed

- **Climate Action Challenge game now has a real light theme** — it was the last dark-only page, relying on a global filter-invert fallback that turned its warm Warli earth-tones cold and muddy in light mode. Replaced with a designer-authored light palette (warm sand surfaces, espresso-brown folk-art ink) wired to the existing 3-button system/light/dark toggle. The folk-art SVG line illustrations (hard-coded cream `#F5F0EB` ink) now flip to brown on the sand background, the literal-dark gauge track lightens, and the page no longer loads `light-mode-fallback.css`. All games now have a genuine light theme.

### For Learners

- **The Climate Action game looks right in light mode** — warm, readable sand-and-brown colours that match the rest of the site, instead of the previous washed-out inverted look.

## [10.79.0] - 2026-06-11

### Added

- **Case packets for all 9 Live Case Challenges** — each challenge in `data/challenges.json` now points at real downloadable resources under `/challenges/<id>/` instead of `#` placeholders. 24 new brand-styled, `noindex`, print-friendly HTML documents plus 6 datasets (CSV), built to be internally consistent with each challenge's case context (e.g. the flawed logframe contains its 5 documented flaws; the AI-targeting dataset exhibits the four described biases; the two nutrition interventions' cost breakdowns reconcile to their per-child figures). The `challenges.js` renderer already shows a real link when a resource URL is present, and the placeholder "coming soon" rendering remains as the fallback.

## [10.78.0] - 2026-06-11

### Added

- **Five new interactive book companions** — Poor Economics (Banerjee & Duflo), Why Nations Fail (Acemoglu & Robinson), Development as Freedom (Sen), Capital in the Twenty-First Century (Piketty), and India After Gandhi (Guha). Each mirrors the data-driven `debraj-ray-companion.html` template (chapter accordions, concept cards, practitioner takeaways, South Asia lens, Gemini Q&A). Cross-referenced into `BookSummaries/index.html`, `data/search-index.json` (BS46–BS50), `sitemap.xml`, `catalog.html` (bs46–bs50), and the docs.

### Changed

- **Theory of Change Workbench relabelled free** — the self-hosted `/toc-workbench.html` was mislabelled "Premium"/"TOC Workbench Pro" in `catalog.html`, `catalog_data.json`, and `data/search-index.json` despite being fully open. The genuine paid Pro tool is the external workshop-pro app; the catalog premium card now points there.
- **Book-companion counts corrected** to 54 across `premium.html`, `README.md`, `upgrade.html`, `content-marketing-kit.html`; catalog filter to 50; BookSummaries index category chips corrected to true card counts (pre-existing drift).

### Fixed

- **Gated four ungated Pro tools** — `rq-builder` and `tor-builder` (→ Practitioner), `qual-insights-lab` and `code-converter-pro` (→ Professional) were fully usable signed-out via direct URL while only the homepage cards were locked. Added the `advisory-board-pro.html` gate pattern (`#lockGate`/`#liveTool` + `hasTierAccess`).
- **~20 broken internal links** — challenge resources and Dataverse skill items no longer render dead `#` links; capitalized `/Labs` & `/Games` directory links now redirect; corrected wrong BookSummary filenames (gog/dt/info-we-trust/storytelling-with-data), course-link case mismatches (`/courses/Gender`, `/courses/MEL`), the `course-catalog.html` back-link, five dead practice-pack flagship-course links, a missing ToC lab path, and a wrong-case SEL redirect target.

## [10.64.0] - 2026-06-05

### Added — Site-wide multilingual support (Hindi, Tamil, Bengali, Marathi)

### For Learners

- **Every page is now available in हिन्दी, தமிழ், বাংলা and मराठी** — a language
  switcher on all 377 pages translates the whole site (courses, 101 decks,
  blogs, deep dives, book summaries, essays) on demand, with the proper Indian
  script fonts. Switch back to English instantly. Powered by Sarvam (Mayura).

### Added

- **`netlify/functions/translate.mjs`** (`/api/translate`) — Sarvam translation
  proxy with a Netlify Blobs cache (each unique string translated once per
  language, then served from cache; API key server-side only).
- **`js/translate-sarvam.js`** — the client switcher: progressive batch-by-batch
  DOM translation with per-user `localStorage` cache, Noto script fonts, a
  MutationObserver for dynamically-loaded content (flagship modules), a
  brand-name keep-list, and a "translating…" indicator.
- **`scripts/translate/`** — the translation pipeline + a paced cache pre-warm
  tool.

### Fixed

- Translation reliability on heavy/cold pages — small batches (fit the Netlify
  function timeout) + progressive apply (render as you go, not all-at-once).

## [10.63.0] - 2026-06-05

### Added — Marginalia essay 3 + 101 hub completion + count reconciliation

### For Learners

- **The Indicator Ate the Village** — the third Marginalia cartoon essay: ten
  drawings on monitoring & evaluation (the baseline that learns nothing, the
  dashboard at 87% beside an empty clinic, real-time-data-for-whom, the endline
  that never saw the year after exit, accountability that only points up), each
  with cited, evidence-based paragraphs.
  `/specials/the-indicator-ate-the-village/`
- **Climate Essentials 101** and **Inequality Basics 101** now appear in the
  101 Series hub (they were native decks sitting outside the grid).

### Changed

- **101 hub** now lists **45 native course decks** — added Climate Essentials +
  Inequality Basics and removed the duplicate "Economics for Policy
  Practitioners" card (it pointed at the Development Economics deck), so the hub
  matches the Deck Library gallery exactly.
- **Site-wide counts reconciled** to 15 flagship · 45 foundational · 60 total ·
  134 games · 13 labs · 49 book summaries · 17 deep dives · 84 handouts ·
  18 practice packs — across English pages, the Supabase signup/invite emails,
  the GitHub profile README, and the bn/mr/hi/ta documentation.

## [10.62.0] - 2026-06-05

### Fixed — Mobile rendering

### For Learners

- **101 course decks now display correctly on phones** — slides previously
  collapsed to a tiny portrait sliver on mobile; they now fill the screen width.

### Fixed

- **All 45 native 101 decks + the `build.py` donor** — `.slide-viewport` was a
  `flex-shrink:1` child of the `display:flex` `#deck`, so on any screen narrower
  than 1280px it shrank its width while height stayed fixed, collapsing the 16:9
  stage into a scaled-down portrait sliver. Added `flex-shrink:0`. Verified in
  headless Chromium (viewport 412px: stage width 412→1280, slide aspect
  0.57→1.78).
- **`faq.html`** — mobile breakpoint hid `.nav-links` but not the `.nav-buttons`
  theme/auth cluster, causing a 73px horizontal overflow; hidden on mobile +
  `overflow-x:hidden` safety net.

### Added

- **`scripts/mobile/audit.py`** — headless-Chromium harness that flags
  horizontal overflow across key pages (exit 1 = CI-gateable). Audit: 24/25 key
  pages already pass at 390px.

## [10.61.0] - 2026-06-05

### Added — 101 Series: 5 more native decks; ZERO Gamma embeds remain

Migrates the last 5 Gamma-embedded 101 decks to native 100-slide HTML and
surfaces 4 catalog-only courses in the 101 hub (40 → 44 listed courses; 37
native, 0 Gamma anywhere in the series).

### For Learners

- **Theory of Change 101** — causal maps from activities to impact: ToC vs
  logframe, the results chain, backwards mapping, assumptions, indicators, and
  common pitfalls. 100 slides. (Fixes a card that was labelled native but was
  still a Gamma embed.)
- **Advocacy Basics 101** — influencing policy and power: types of advocacy,
  power analysis, stakeholder mapping, policy windows, tactics, and ethics.
  100 slides.
- **Behaviour Change Communication 101** — moving from awareness to action:
  behaviour-change theory, audience segmentation, formative research, message
  design, channels, and campaigns. 100 slides.
- **Political Economy 101** — how politics and economics interact: institutions,
  collective action, rent-seeking, the developmental state, and political-economy
  analysis for reform. 100 slides.
- **Women's Economic Empowerment 101** — resources, agency and achievements: the
  care economy, labour-force participation, assets and finance, social norms,
  legal rights, and what works. 100 slides.

### Changed

- **`101-courses/index.html`** — 4 new hub cards (Advocacy, BCC, Political
  Economy, WEE); counts now Native 37 / Slide Deck 0; series total 40 → 44;
  hero stat "3,700 Slides of Learning".
- **`data/search-index.json`** — `course` entries for the 5 additional decks.

## [10.60.0] - 2026-06-05

### Added — 101 Series native migration COMPLETE: Governance & Economy (4 decks)

The final cluster lands. **All 26 ImpactMojo 101 courses that were embedded
Gamma decks are now self-hosted native 100-slide HTML decks** — joining the 7
pre-existing native decks for **33 native decks, 0 Gamma embeds**.

### For Learners

- **Indian Constitution 101** — the making of the Constitution, the Preamble,
  Fundamental Rights and Duties, Directive Principles, the union and federal
  structure, the judiciary and the basic-structure doctrine, local
  self-government, and constitutionalism in practice. 100 slides.
- **Global Development Governance 101** — the aid architecture: Bretton Woods,
  the UN system and IFIs, ODA and the 0.7% target, the SDGs, financing for
  development, new actors, aid effectiveness and localisation, and India's
  shift from recipient to emerging donor. 100 slides.
- **Public Health 101** — population health and prevention: social determinants,
  epidemiology, measuring health, communicable disease and immunisation, NCDs,
  maternal and child health, the WHO building blocks and Universal Health
  Coverage, and India's health system. 100 slides.
- **Fundraising Basics 101** — resource mobilisation for nonprofits: the funding
  landscape, donor relationships, proposal writing and budgets, CSR (Companies
  Act s.135) and compliance (FCRA, 12A/80G), diversification, and the ethics of
  fundraising. 100 slides.

### Changed

- **`101-courses/index.html`** — the last four cards re-badged Native HTML;
  counts now Native HTML 33, Slide Deck 0.
- **`data/search-index.json`** — `course` entries added for all 26 migrated
  decks so they surface in site search.

## [10.59.0] - 2026-06-05

### Added — 101 Series native migration: Critical & Digital cluster (5 decks)

Five more 100-slide native decks (plus English for Development, shipped
separately); 22 of 26 Gamma courses now migrated.

### For Learners

- **Decolonial Development 101** — the colonial roots of "development" and how to
  decolonise it: Said, Escobar, Quijano and the dependency/coloniality
  critiques, epistemic injustice, decolonising aid and research, and
  post-development alternatives. 100 slides.
- **Digital Ethics 101** — data privacy and the DPDP Act 2023, algorithmic bias,
  AI in development, digital ID (Aadhaar) inclusion and exclusion, surveillance,
  the digital divide, data colonialism, and responsible design. 100 slides.
- **Environmental Justice 101** — the unequal distribution of environmental harm:
  distributive/procedural/recognition justice, climate justice, the Forest
  Rights Act, pollution and health, just transition, and India's environmental
  movements. 100 slides.
- **Post-Truth Politics 101** — mis/dis/mal-information, how falsehoods spread,
  filter bubbles, cognitive biases, propaganda, the attention economy,
  deepfakes, polarisation, and building resilience. 100 slides.
- **Visual Ethnography 101** — studying culture through images: photo-elicitation,
  photovoice, video methods, visual analysis, the ethics of the image and the
  gaze, and dignity in representation. 100 slides.
- **English for Development 101** — clear professional communication for the
  sector: plain language, de-jargoning, writing for different audiences,
  reports and briefs, and ethical storytelling. 100 slides.

### Changed

- **`101-courses/index.html`** — six more cards re-badged Native HTML · 100
  slides; counts updated (Slide Deck down to 4, Native HTML up to 29).

## [10.58.0] - 2026-06-05

### Added — 101 Series native migration: Gender & Social cluster (6 decks)

Six more 100-slide native decks (16 of 26 Gamma courses now migrated).

### For Learners

- **Data Feminism 101** — power and data through D'Ignazio & Klein's seven
  principles: examining and challenging power, rethinking who gets counted,
  intersectionality, and South Asia's gender data gaps. 100 slides.
- **Care Economy 101** — the unpaid and paid care that holds up every economy:
  the SNA boundary, time-use data, the gendered care burden, the 5 Rs, and
  care policy. 100 slides.
- **SEL Basics 101** — social and emotional learning: CASEL's five
  competencies, the evidence base, classroom implementation, and SEL in the
  Indian context (NEP 2020). 100 slides.
- **Sexual Health 101** — a rights-based, medically accurate primer on sexual
  and reproductive health and rights: contraception, maternal health, safe
  abortion law (MTP 2021), STIs/HIV, consent, and comprehensive sexuality
  education. 100 slides.
- **Community Development 101** — participation (Arnstein's ladder), asset-based
  development, organising, participatory tools, self-help groups and the
  commons, and panchayati raj. 100 slides.
- **Education and Pedagogy 101** — how learning works (Piaget, Vygotsky,
  Bloom, Freire), assessment, foundational literacy & numeracy and Teaching at
  the Right Level, inclusive pedagogy, and India's learning crisis. 100 slides.

### Changed

- **`101-courses/index.html`** — six cards re-badged Native HTML · 100 slides;
  counts updated (Native HTML 17 → 23, Slide Deck 16 → 10). Adds
  `scripts/deck-builder/rebadge.py` to keep card badges and counts in sync.

## [10.57.0] - 2026-06-05

### Added — 101 Series native migration: Data & Methods cluster complete (5 decks)

Five more 100-slide native decks finish the Data & Methods cluster (10 of the
26 Gamma courses now migrated).

### For Learners

- **Econometrics 101** — measuring causal effects, not just correlations:
  the counterfactual, OLS and omitted-variable bias, RCTs, instrumental
  variables, difference-in-differences, regression discontinuity, and panel
  fixed effects — with the assumptions each one rests on. 100 slides, 7 charts.
- **Multivariate Analysis 101** — multiple regression and beyond: partial
  effects, model fit and diagnostics, multicollinearity, interactions,
  logistic regression and odds ratios, and PCA/factor analysis (the wealth
  index). 100 slides, 8 charts.
- **Item Response Theory 101** — modern measurement: latent traits, item
  characteristic curves, difficulty and discrimination, the 1PL/2PL/3PL
  family, test information, and differential item functioning, applied to
  learning and empowerment scales. 100 slides, 12 charts.
- **Cost Effectiveness 101** — doing the most good per rupee: CEA/CBA/CUA,
  costing, the ICER, DALYs and QALYs, discounting, league tables and
  sensitivity analysis — and what cost-effectiveness leaves out. 100 slides.
- **Observation to Insight 101** — turning field observation into evidence:
  observation types, Spradley's framework, field notes, structured tools,
  sensemaking, triangulation, rigour and the ethics of watching. 100 slides.

### Changed

- **`101-courses/index.html`** — five cards re-badged Native HTML · 100 slides;
  counts updated (Native HTML 12 → 17, Slide Deck 21 → 16).

## [10.56.0] - 2026-06-05

### Added — 101 Series native migration: Data & Methods batch (4 decks)

Four more 101 Series courses move from Gamma embeds to native 100-slide decks,
built with the `scripts/deck-builder` pipeline.

### For Learners

- **Bivariate Analysis 101** — relationships between two variables: cross-tabs,
  scatterplots, correlation (Pearson & Spearman), comparing groups, chi-square,
  simple regression, and the classic pitfalls (confounding, ecological fallacy,
  Anscombe, Simpson's paradox). 100 slides, 8 charts.
- **Exploratory Data Analysis 101** — making sense of household survey data
  (NSS/PLFS, NFHS, CMIE): the EDA workflow, distributions, missingness and
  outliers, survey weights and design effects, and honest visual exploration.
  100 slides, 10 charts.
- **Qualitative Methods 101** — interviews, focus groups, observation and
  ethnography, participatory & visual methods, coding and thematic analysis
  (Braun & Clarke), and trustworthiness (Lincoln & Guba). 100 slides.
- **Research Ethics 101** — from Nuremberg, Helsinki and Belmont to India's
  ICMR 2017 guidelines and the DPDP Act 2023: consent, vulnerable populations,
  privacy, risk–benefit, ethics review, and giving findings back. 100 slides.

### Changed

- **`101-courses/index.html`** — the four cards re-badged Native HTML · 100
  slides; counts updated (Native HTML 8 → 12, Slide Deck 25 → 21).
- Every deck is now hard-enforced at exactly 100 slides, with TOC section
  ranges auto-computed by the builder.

## [10.55.0] - 2026-06-05

### Added — 101 Series native migration: Data Literacy 101 + deck builder

Begins migrating the ImpactMojo 101 Series from embedded Gamma slide decks to
self-hosted, native HTML decks. First deck shipped: **Data Literacy 101**.

### For Learners

- **Data Literacy 101** — a 99-slide native course on reading, questioning,
  visualising and using data responsibly: India's data ecosystem (Census,
  NFHS, PLFS/NSS), turning concepts into indicators, describing and visualising
  data, correlation vs causation, sampling and surveys, data cleaning, reading
  statistics critically, and data ethics, privacy & equity. Charts, tables and
  diagrams throughout; light/dark themes, keyboard & swipe navigation, free
  forever.

### Added

- **`101-courses/data-lit.html`** — native gold-standard deck (replaces the
  Gamma embed), 99 slides, 7 charts. Self-contained: inline theme switcher,
  viewport scaling, lazy chart init, deep-linking and auto-fit.
- **`scripts/deck-builder/`** — a reusable deck generator. Authors write a
  compact Python spec (`specs/<slug>.py`); the builder slices the proven shell
  (CSS + runtime JS) out of `dev-economics.html` and injects the generated
  slides, slide-IDs and chart code, so every deck inherits identical styling
  and behaviour. Includes `build.py`, `_schema.md` and the Data Literacy spec.

### Changed

- **`101-courses/index.html`** — Data Literacy card re-badged Native HTML ·
  99 slides; counts updated (Native HTML 7 → 8, Slide Deck 26 → 25).
## [10.54.0] - 2026-06-04

### Changed — Causal Inference flagship: gold-standard content rewrite (all 13 modules)

- Rewrote every module's `content_html` and deployed it to the production
  `course_content` table (course_id `causal`). Each module now has KaTeX math,
  an inline DAG/plot, a worked Indian-programme example with a results table,
  R + Stata code, a common-pitfalls callout, a problem set with collapsible
  solutions, and current references. Per-module content roughly doubled in
  depth (≈6 KB → 9–16 KB).
- `courses/causal/index.html`: KaTeX wired (earlier) + new styled components
  (`worked-example`, `problem-set`, `dag-figure`, `assumption-list`).
- `js/course-loader.js` (earlier): fetch timeout + retry so modules no longer
  hang on a slow edge-function response.
- Content pipeline: `supabase/seed-content/causal/` per-module source files;
  `scripts/build-causal-seed.py` rebuilds the seed migration; `scripts/
  deploy-causal.py` deploys to prod via the Supabase Management API.

## [10.53.0] - 2026-06-04

### Added — Marginalia series hub + second essay "The Fine Print"

- **`specials/the-fine-print/index.html`** (new) — second Marginalia cartoon
  essay, 10 panels with the "pitch / reply" device and two–three cited
  paragraphs each, plus a 19-item Notes & Sources list. Themes: co-creation/
  tokenism (Arnstein), ownership vs budget (participatory budgeting), disability
  access (RPwD Act 2016 / CRPD), youth tokenism (Hart), unpaid "volunteer"
  labour (WHO), lifestyle drift / commercial determinants (WHO), evidence vs
  budget (Cairney), dashboard vs service (Jal Jeevan Mission, Goodhart),
  maintenance vs innovation (Vinsel & Russell), resilience vs root causes
  (*At Risk*).
- **`specials/marginalia/index.html`** (new) — series landing hub with cards
  for both essays; BreadcrumbList + CollectionPage JSON-LD.
- **`assets/images/the-fine-print/`** — 10 cartoons optimised to progressive
  JPEG (~2.8 MB); **`assets/images/marginalia-cover.jpg`** series cover.
- **Cross-refs** — homepage Specials section now shows both essays and links
  to the hub; nav "Marginalia" repointed to `/specials/marginalia/`;
  `search-index.json` (+2), `catalog.html`/`catalog_data.json` (Specials → 2),
  `sitemap.xml`, and the podcast companion callout updated to the series.

## [10.52.0] - 2026-06-04

### Added — New Special: "Capacity for Irony" (Marginalia)

A new content type — **Specials** — debuts with its first entry, a
**Marginalia** piece (illustrated satire with cited evidence) at
`/specials/capacity-for-irony/`.

- **`specials/capacity-for-irony/index.html`** (new) — self-contained,
  brand-compliant page (fixed topbar, 3-mode theme toggle, 4-section footer,
  skip link, GA, paper-plane, Article JSON-LD). Ten cartoons laid out as
  alternating panels; each pairs the "pitch / reply" exchange with two–three
  evidence-based paragraphs and inline citations, plus a 17-item numbered
  Notes & Sources list. Notebook-paper palette with a blue-ink accent echoing
  the artwork.
- **`assets/images/capacity-for-irony/`** (new) — 10 cartoons optimised from
  ~24 MB PNG to ~2.5 MB progressive JPEG (1000px wide), lazy-loaded with full
  alt text.
- **Cross-references** — added to the homepage Specials → Long-form Reading
  menu (`index.html`), `data/search-index.json` (type `special`),
  `sitemap.xml`, and both changelogs.

## [10.34.0] - 2026-06-02

### Added — Practice Packs premium (freemium paywall)

Practice Packs move from fully free to a freemium model: the first two modules
of every pack remain a free preview; modules 3–4 plus the capstone builder
require access.

- **`js/practice-pack-gate.js`** (new) — reusable client-side freemium gate.
  Wraps the shared `goTab(idx)` entry point so every tab and nav button is
  gated with one drop-in. Themed paywall modal offers three paths: Practitioner
  subscription (₹399/mo, all 18 packs), standalone single pack (₹299), and an
  optional expert review (₹999). Config per pack via `window.IM_PACK`.
- **All 18 packs** wired with the gate (`freeModules: 2`).
- **Standalone purchase support** — `profiles.resource_grants TEXT[]` column
  (migration `20260602_add_resource_grants.sql`, GIN-indexed). `auth.js` selects
  it and exposes `ImpactMojoAuth.hasResourceAccess(slug)`; `state-manager.js`
  caches it; the gate unlocks a pack if the user's tier qualifies OR the slug is
  in `resource_grants`. Admin grants the slug after UPI, matching the existing
  manual registration flow.
- **`premium.html`** — Practice Packs added to the Practitioner tier card and
  detail; registration form gains "Practice Pack (single) – ₹299", "Practice
  Pack + Expert Review – ₹1,298", and "Practice Pack Expert Review – ₹999"
  options plus a conditional pack-name field; `?pack=<slug>` deep link
  preselects the standalone option and prefills the pack; new FAQ entry.
- **`upgrade.html`** — Practice Packs added to the Practitioner offer.
- **`practice-packs/index.html`** — reframed from "Free" to free-preview +
  premium; **search-index** landing description updated.

## [10.28.0] - 2026-05-23

### Added — Complete Practice Packs series (16 new) + blog rewrite

**16 new interactive Practice Packs** completing the full series (18 total):

Subject Packs (7 new):
- PP-S3 Gender Impact Assessment Design
- PP-S4 Education Programme Evaluation
- PP-S5 Health Intervention Evaluation
- PP-S6 Climate Adaptation Programme Evaluation
- PP-S7 Public Policy Evaluation
- PP-S8 Media Campaign Evaluation
- PP-S9 Governance Reform Evaluation

Method Packs (9 new):
- PP-M1 Writing a ToR That Gets You Useful Research
- PP-M2 Designing a Survey Instrument
- PP-M3 Building a Logframe That Actually Tracks
- PP-M4 Costing a Programme from Activities Up
- PP-M5 Running a Real Focus Group Discussion
- PP-M6 Reading & Critiquing an Evidence Paper
- PP-M7 Stakeholder Mapping for Influence
- PP-M8 Donor Reporting That Funders Read
- PP-M9 Building an MEL System from Scratch

All follow interactive pattern: localStorage auto-save, progress bar, MCQ self-checks, live capstone builder ("Build my brief" pulls module answers into compiled markdown), copy/print export. No emoji — Sargam SVG icons. India-context throughout. Dark mode support.

Landing page (`/practice-packs/`) updated with all 18 pack cards in Subject + Method tracks. `data/search-index.json` +16 entries (total 562). `sitemap.xml` +16 URLs.

### Fixed

- **Blog "Evidence-Based Pivots" rewritten with real named cases + citations** — reader (Ashwani, M&E practitioner) asked for sources. The three stories were composites. Rewrote with: (1) India's ICDS system (Gragnolati et al. 2005, World Bank); (2) JEEViKA Bihar (Datta 2015, *World Development*); (3) Pratham TaRL pivot (Banerjee et al. 2017, *JEP*). Same arcs, real names, inline source blocks.
- **All emoji removed from every new page** — replaced with Sargam-style inline SVGs across all 9 files from the session (186 emoji in SEL game alone). Practice Packs landing stripped of "v2 callout" and stub cards.

## [10.27.0] - 2026-05-23

### Practice Packs v2 — Interactive lab-features + Subject/Method tracks + PP02 Livelihoods Evaluation

Cofounder feedback: (1) the PP roadmap looked all-SEL because PP01 was the only live subject pack — felt narrow; (2) labs and handouts outperform courses because they're interactive — Practice Packs should work like labs, not like static reading. This release addresses both.

**Landing page (`/practice-packs/`) restructured into two tracks**:
- **Subject Packs** (9 — per-domain evaluation design): SEL ✓, Livelihoods ✓, Gender, Education, Health, Climate, Public Policy, Media, Governance
- **Method Packs** (9 — cross-cutting toolkit skills): ToR (Next), Survey, Logframe, Costing, FGD, Critiquing Evidence, Stakeholder, Donor Reporting, MEL from Scratch
- The SEL pack is now visibly one of 9 subject packs, not the lead identity

**PP01 SEL Evaluation — retrofitted with interactive lab-features**:
- In-browser form-based template editor (textareas + radios) replacing the static copy-to-clipboard `<pre>` blocks
- localStorage auto-save (no login; data stays in browser; explicit privacy claim)
- Progress bar shows % complete + per-module completion state
- 4 self-check MCQs (one per module) with reveal-the-answer + feedback
- Live capstone builder: click "Build my brief" → pulls all module answers into a compiled markdown brief
- Export: copy as markdown / print as PDF / contenteditable for in-place refinement
- Reset button (with confirmation) to clear progress

**PP02 Livelihoods Evaluation Design — new Subject pack, shipped with full interactive features**:
- Module 1: SLF + outcome dimension choice (income / asset / capability / vulnerability)
- Module 2: PLFS/NRLM/SECC-aligned instrument selection with India national-data comparability
- Module 3: Sampling + seasonal calendar + migration coding protocol
- Module 4: Disaggregated analysis + shock-attribution + the "Krishna question" framing
- Capstone: 1-page Livelihoods Evaluation Design Brief
- 4 self-check MCQs; same interactive pattern as PP01

**Cross-references**: search-index (PP01 updated, PP02 added — type `practice-pack`), sitemap (livelihoods URL added).

## [10.26.2] - 2026-05-23

### Added — napkin.ai diagrams for the accessibility blog post

`/blog/making-accessible-websites.html` was the last blog post on the site using only inline SVG figures rather than napkin.ai PNG diagrams (cofounder feedback called it out as the holdout). Brought it in line with the rest of the blog.

- **Illustration 1** — replaces the inline SVG bar chart of the 5-pass trajectory (393 → 77 → 21 → 14 → 1 → 0). Same data; cleaner napkin progress-tile design with both percentage reductions and absolute counts shown.
- **Illustration 2** — new diagram added at "Lesson 2: small number of root causes" section, illustrating the five common root causes (missing alt text, low colour contrast, improper form labels, missing skip links, missing ARIA attributes) that account for ~80% of WCAG violations across most sites.
- The two remaining inline SVGs (Brand colours vs WCAG comparison table; Six-step starter checklist) intentionally kept as inline SVG — they contain precise data (specific Tailwind colour codes, contrast ratios, numbered step actions) that napkin's summarisation would not preserve faithfully.

## [10.26.1] - 2026-05-23

### Added — napkin.ai diagrams for "Knowing What You Want" blog

The blog post shipped in v10.25.0 had no illustrations (platform convention is 2 per post). This PR fixes that gap.

- **Illustration 1** — Six substitutes for wanting, stacked precariously like a tower. The fragility-of-substitution metaphor.
- **Illustration 2** — Seven honest questions as stations on a winding path. The 90-minute exercise.
- Added `.napkin-figure` CSS (was missing).

## [10.26.0] - 2026-05-23

### Added — Practice Packs series launched

**New content type**: ImpactMojo Practice Packs — short, focused 3-hour sprints that take practitioners from a job-to-be-done to a finished artefact. Sits between blog posts (one-shot read) and flagship courses (multi-week commitment). The format contract:

- 4 modules, ~25 min each
- ~2 hours reading + 1 hour exercise = ~3 hour total commitment
- Each module: short read + worked example + exercise + downloadable template
- Capstone: produce one concrete artefact (a ToR, drafted survey, logframe, eval design, etc.)
- Take-home pack of all templates

**New section**: `/practice-packs/` — landing page lists all packs (1 live, 9 upcoming).

**First Practice Pack**: `/practice-packs/sel-evaluation/` — "SEL Evaluation: Design & Instruments" (PP01).
- Module 1: What kind of evaluation do you actually need? (3 dimensions)
- Module 2: Choosing your measurement approach (CASEL / SEE Learning / WHO Life Skills / NCERT AEP / ACER India / behavioural / direct assessment)
- Module 3: Designing the data collection (sample sizes, per-unit costs in 2026 ₹, consent architecture)
- Module 4: Analysis, reporting, and the honest framing
- Capstone: 1-page SEL Evaluation Design Brief
- 5 downloadable copy-to-clipboard templates throughout

**Upcoming Practice Packs** (listed on landing page):
PP02 ToR Writing · PP03 Survey Instrument · PP04 Logframe · PP05 Costing · PP06 FGD · PP07 Critiquing Evidence · PP08 Stakeholder Mapping · PP09 Donor Reporting · PP10 MEL from Scratch

**Cross-references**: `data/search-index.json` (PP-LANDING + PP01, new type `practice-pack`), `sitemap.xml` (2 URLs), `index.html` (nav link with "New" badge).

## [10.25.5] - 2026-05-23

### Added — Framework diversity propagated to SEL Course and SEL Eval Deep Dive

After bringing framework plurality to the SEL Simulation Game (#433), audited the SEL Course and SEL Evaluation Deep Dive — both had the same CASEL-heavy, NEP-child-only gaps. This PR fixes both.

**SEL Flagship Course (`/courses/SEL/`)**:
- Hero subtitle now names CASEL, SEE Learning, WHO Life Skills, Delhi Happiness Curriculum + EMC, Indian indigenous traditions (Tagore, Krishnamurti, Aurobindo, Nai Talim), and NEP 2020 teacher-side provisions (NPST, CPD, B.Ed., teacher autonomy)
- New static "Frameworks We Draw From" section inserted between hero and Module 1, explicitly mapping each framework's relevance with India-context notes
- Sidebar nav updated with link to the new section
- Meta description, keywords, OG description updated for SEO
- *Note*: Course module content itself is dynamically loaded from Supabase edge function; this PR updates only the static shell. Full integration of framework references into individual module bodies would require database updates outside this repo.

**SEL Evaluation in India Deep Dive (`/DeepDives/sel-evaluation-india.html`)**:
- Section 01 (Foundations) — added 4 new entries:
  - SEE Learning (Emory + Dalai Lama Centre)
  - NCERT Adolescence Education Programme (AEP) — the framework Indian government schools actually run
  - Indian indigenous educational traditions (Tagore, Krishnamurti, Aurobindo, Nai Talim)
  - Expanded NEP 2020 entry to explicitly include teacher-side provisions (NPST, 50-hr CPD, 4-yr integrated B.Ed., teacher autonomy)
- Section 02 (India Evidence Base) — added entry for Delhi's Entrepreneurship Mindset Curriculum (EMC) alongside the existing Happiness Curriculum entry; deepened the Happiness Curriculum annotation
- Reading count updated 28 → 32 (in HTML, `data/deep-dives.json`, and the homepage Deep Dives card)

## [10.25.4] - 2026-05-23

### Added

- **SEL Simulation Game: Parent mode (5th mode).** Replaces "Four Lenses" with "Five Lenses". Six new rounds drawn from Indian parenting + adolescent mental-health evidence:
  - The withdrawn child at dinner (early-warning response)
  - The teacher complaint about your son (parent-teacher partnership)
  - The friend who turned on your daughter (relational coaching)
  - The day you snapped (rupture-and-repair modelling)
  - The school SEL programme arrives (NEP-aligned parent engagement)
  - Boards + a peer self-harming (warm-handoff to professional support)
- Parent mode tracks 4 dimensions: Trust, Wellbeing, Connection, Modeling. 5 archetypes. End-screen summary including India-specific adolescent mental-health helplines (iCall, Vandrevala, MANAS).
- Welcome SVG updated with parent figures (violet).

### Changed

- **Framework diversity acknowledged.** Game was CASEL-heavy. Now explicitly references **SEE Learning** (Emory + Dalai Lama Centre, India-translated), **WHO Life Skills** (the framework actually under-girding most Indian state curricula), Delhi's **Happiness Curriculum** + **Entrepreneurship Mindset Curriculum (EMC)**, and Indian indigenous traditions (Tagore, Krishnamurti, Aurobindo, Nai Talim). Updated intro card, "Why X modes?" card, and several scenario insights to reflect this plurality.
- **NEP 2020 teacher-side provisions** woven into Teacher and Designer endEvidence summaries — NPST (National Professional Standards for Teachers), 50-hour annual CPD mandate, 4-year integrated B.Ed., teacher autonomy. Previous text framed NEP almost entirely from the child-facing side.
- Score dimensions, scenario card, choice grid all extended to support 5th mode (violet color tokens, m5 score card, b5 bar, scenario-card.parent, parent .btn-choice).
- Cross-references updated: search-index `GAME017`, index.html courses modal card, catalog.html g17 entry.

## [10.25.3] - 2026-05-23

### Fixed

- **ToR blog post: removed duplicate illustrations.** The inline SVG fallbacks were rendering alongside the napkin.ai PNGs (default `display: inline-block` was applied unconditionally, not only via `onerror`), producing the impression of figures back-to-back with no text in between. Removed all 4 inline SVG fallbacks now that real napkin.ai PNGs exist for every figure.
- **Diagram 4 (research types) is now a real napkin.ai PNG** — generated successfully on the third prompt attempt (clean mismatches list). Previous versions either collapsed the 3×3 matrix to 3 pills or used over-creative metaphors that lost the content.
- Removed dead `.napkin-figure svg` CSS rule.

### Changed

- Updated alt text on all 4 figures to reflect they are napkin.ai diagrams.
- Tightened figcaptions on figures 3 and 4 since the diagram now does more of the storytelling.

## [10.25.2] - 2026-05-23

### Added

- **New section in ToR blog post:** "What Kind of Research Do You Actually Need?" — addresses the second-most-common cause of failed research engagements (asking for the wrong *type* of research). Covers three dimensions:
  - **Question type**: outcome evaluation vs process tracing vs theory-based evaluation
  - **Evidence type**: quantitative vs qualitative vs mixed-methods (and why mixed is consistently under-budgeted)
  - **Time dimension**: cross-sectional vs pre-post vs longitudinal vs retrospective
- Includes 3 common mismatches we see weekly and a closing callout requiring a one-line statement of the design choice on all three dimensions before finalising the methods section.

### Changed

- **3 of 4 blog diagrams upgraded to real napkin.ai-generated PNGs** (illustration-1 Anatomy of ToR, illustration-2 Budget Tiers, illustration-3 Process Cycle). Inline SVG fallbacks remain via `onerror` handler.
- **Diagram 4 (research types) deliberately uses the inline SVG** rather than a napkin PNG — napkin's summarisation collapsed the 3 dimensions × 3-4 options + 3 mismatches structure into a 3-pill graphic each time it was re-prompted; the inline SVG preserves the full matrix.
- Updated blog-card excerpt and search-index description to reflect the expanded scope.

## [10.25.1] - 2026-05-23

### Added

- **Blog post: How to Write a ToR That Gets You Useful Research** at `/blog/writing-a-tor-for-research.html` — practical guide for development sector clients on writing Terms of Reference / Scope of Work / RFP documents to obtain research from agencies like ImpactMojo. Covers the 9 ingredients of a good ToR, 5 anti-patterns, India 2026 budget benchmarks (₹2L/₹10L/₹40L tiers, day rates by seniority, where the money actually goes), 5 common budgeting mistakes, and a pre-send checklist.
- 3 inline SVG napkin-style diagrams: (1) anatomy of a good ToR, (2) what ₹2L/₹10L/₹40L buys, (3) ToR-to-research pipeline with failure points. PNG fallback paths at `assets/images/blog/writing-a-tor-for-research/illustration-{1,2,3}.png`.
- Entries in `data/search-index.json` (BLOG031), `sitemap.xml`, `blog.html` card.

## [10.25.0] - 2026-05-22

### Added

- **SEL Simulation Game** at `/Games/sel-simulation-game.html` — four-mode game (teacher, program designer, evaluator, student) on Social-Emotional Learning in Indian schools. Evidence-grounded scenarios drawn from NEP 2020, CASEL, WHO life skills, and India-specific SEL research 2015–2024. ~24 evidence-backed scenarios across the four modes, each with explicit "what the evidence shows" reflection.
- **Teacher Evidence Lab** at `/Labs/teacher-evidence-lab.html` — filterable evidence base of 30+ teacher-effectiveness interventions (TaRL, contract teachers, mentoring, structured pedagogy, cascade training, multi-grade pedagogy, Mindspark, pay-for-performance, etc.). Filter by evidence quality, cost, type, outcome, and India relevance. Each card includes honest summary including weak/null findings.
- **SEL Evaluation in India — Deep Dive** at `/DeepDives/sel-evaluation-india.html` — 28-reading working syllabus across 7 sections: foundations, India evidence base, measurement, design choices, operational wisdom, critiques, and an opinionated "what works, what doesn't" summary.
- **Knowing What You Want — Blog Post** at `/blog/knowing-what-you-want.html` — reflection on the foundational step of knowing what you want before building theory of change. Includes 90-minute 7-question exercise.
- **Livelihoods in India: Rural, Urban, and Skills — Flagship Course** at `/courses/livelihoods/` — comprehensive 3-module flagship: rural livelihoods (NRLM, SHGs, MGNREGA, agriculture, financial inclusion), urban livelihoods (informal sector, vendors, gig economy, domestic workers, urban policy tools), skills (Skill India evidence, apprenticeships, women's labour force participation puzzle, job matching, returns to training). ~15,000 words. Practitioner-level, India-centred, evidence-driven.
- Entries in `data/search-index.json` (5), `catalog_data.json` (livelihoods), `data/deep-dives.json` (SEL eval), `sitemap.xml` (5 URLs).

### Changed

- Content counts sitewide:
  - Games: 16 → 17
  - Courses: 52 (12 flagship + 40 foundational) → 53 (13 flagship + 40 foundational)
  - Labs: 11 → 12
  - Deep Dives: 5 → 6

Updates made to `index.html`, `catalog.html`, `docs/changelog.md`. Other count references in `docs/` files may still show old numbers — to be swept in next housekeeping pass.

## [10.23.38] - 2026-05-03

### Fixed
- **Timeline era headers no longer overlap card content.** The original v10.23.35-36 design used `position: sticky` on `.era-header` which caused the "01 / 02 / 03" era numbers to sit on top of node cards as users scrolled. Removed sticky positioning; era headers are now inline section breaks.

### Changed
- **Timeline cards now use progressive disclosure** (matches reference site behaviour). Cards are collapsed by default showing year + title + author + chevron. Click anywhere on the card to expand the Argued / Mattered / Critique sections + cross-links. Click again to collapse. Reduces the wall-of-text feel that made timelines hard to scan.
- **Era jump-nav added** (sticky pill bar below topbar) — click an era name to smooth-scroll to that section. Replaces the old filter chips that hid eras (jump is more intuitive than filter for sequential reading).
- **Era headers redesigned** as inline flex (marker + title + years pill + blurb below) — cleaner than the previous stacked layout with the absolutely-positioned marker.
- **Vertical timeline rail removed** — no longer needed without sticky positioning; visual hierarchy now comes from the era headers + card grouping.
- Deep-link via `#n-...` still works AND auto-opens the target node when the page loads.

### Why
User: "the format of the timelines is not working. it's hard to read and understand. pls look at the original example shared and try to emulate just using our brand and fonts. also the sections 01 02 03 etc are overlapping the text content."

Applied to all 5 timelines (Development Thinking, Indian Policy, MEL & Methods, Climate Policy, Indian Rights) via single CSS+JS override block.

## [10.23.37] - 2026-05-03

### Added
- **Timelines added to main site navigation** under Specials → Long-form Reading (alongside Book Companions and Deep Dives). Single-line addition to `index.html`'s nav-specials dropdown — `/timelines/` now reachable from every page on the site without needing to know the URL.

## [10.23.36] - 2026-05-03

### Added
- **Four more timelines shipped — all 5 stubs from v10.23.35 now LIVE.** User: "do the stubs." Each is hand-curated, citation-backed, era-grouped, with cross-links to existing ImpactMojo content.
  - **Indian Policy & Welfare State, 1947–Today** (15 nodes, 7 eras): Independence/Partition · Constitution · First Five-Year Plan · 1956 Industrial Policy + Mahalanobis · Green Revolution · Bank Nationalisation 1969 · Garibi Hatao · Emergency · NABARD · Mandal · 1991 LPG · 73rd/74th amendments · Mid-Day Meal/PoA · RTI · MGNREGA · FRA · RTE · NFSA · Jan Dhan/JAM · GST · CAA-NRC + Article 370 · NEP 2020 · Farm Laws · Bihar Caste Survey 2023.
  - **MEL & Research Methods, 1969–Today** (18 nodes, 6 eras): USAID Logframe 1969 · OECD-DAC formed · DAC Evaluation Criteria 1991 · Theory of Change 1995 · Paris Declaration 2005 · UNEG Norms · J-PAL 2003 · 3ie · PDIA · MSC + Outcome Harvesting · DAC Coherence added 2019 · COVID Remote MEL · Generative AI for evaluation · Decolonial/Made-in-Africa Evaluation.
  - **Climate Policy & Justice, 1972–Today** (17 nodes, 6 eras): Stockholm 1972 · Limits to Growth · Brundtland · IPCC · Rio · Kyoto · USA Withdraws · Copenhagen failure · Paris Agreement · IPCC 1.5°C report · Greta · IPCC AR6 · COP27 Loss & Damage Fund · COP28 Dubai "transition away from fossil fuels".
  - **Indian Rights & Social Margins, 1950–Today** (18 nodes, 6 eras): Constitution Articles 14/15/16/17 · Untouchability Act · Mandal Commission · SC/ST PoA Act · Mandal Accepted · 73rd/74th · PESA · RTI/MGNREGS · FRA · NFSA + Koushal · NALSA third gender · RPWD Act · Section 377 read-down · Trans Persons Act + Triple Talaq + Article 370 · CAA · Janhit Abhiyan EWS · Supriyo marriage equality · Davinder Singh sub-categorisation 2024.
- **Total now: 5 LIVE timelines, 95 nodes, 38 eras** spanning ~250 years of development thinking, ~75-80 years of Indian state-building/rights, ~55 years of MEL practice, and ~52 years of climate diplomacy.
- Landing page `/timelines/` updated: all 5 cards now LIVE with node counts; hero stats updated to "5 Live · 95 Total nodes · 38 Eras covered".
- `sitemap.xml` updated with 4 new URLs (priority 0.8). 194 URLs total.
- `data/search-index.json` updated with 4 new entries (TIMELINE003-006). 537 entries total.

## [10.23.35] - 2026-05-03

### Added
- **New content type: ImpactMojo Timelines.** Curated, citation-backed visual histories at `/timelines/`. Each timeline carries: era-grouped nodes, original argument, why-it-mattered, the critique that came after, and cross-links to existing ImpactMojo decks/BookSummaries/handouts. Single-file HTML per timeline, brand-consistent styling, deep-link via `#node-id`, era filter chips, sticky era headers.
- **First timeline live: "Development Thinking, 1776–Today" — 25 nodes, 7 eras**. From Adam Smith and Marx through Truman's "underdeveloped," Lewis dual-sector, the Bandung Conference, Rostow's stages, Prebisch–Singer, Cardoso–Faletto, Wallerstein, the ILO Basic Needs approach, Sen's *Poverty and Famines* + *Development as Freedom*, the Washington Consensus, MDGs, Acemoglu–Robinson on institutions, J-PAL/RCTs, Easterly's *White Man's Burden*, Piketty's *Capital*, the SDGs, Hickel/degrowth, the polycrisis frame, COP27 Loss and Damage, and Bridgetown/BRICS+/decolonial turn 2023.
- **Landing page** at `/timelines/index.html` showcases the new content type with one card LIVE (Development Thinking) and four others marked "Soon" (Indian Policy & Welfare State; MEL & Research Methods; Climate Policy & Justice; Indian Rights & Social Margins).
- **Sitemap** updated with `/timelines/` and `/timelines/development-thinking.html` (priority 0.8).
- **Search-index** updated with two new entries (`TIMELINE001` landing, `TIMELINE002` Development Thinking).

## [10.23.34] - 2026-05-03

### Fixed
- **Auto-fit JS was truncated across all 7 native decks** during a prior merge conflict resolution — only the opening comment marker remained, with the entire `autoFit` IIFE body deleted. Re-injected the full `autoFit` function so proportional zoom-on-overflow works again. Lowered the floor from **0.85x → 0.78x** so genuinely overflowing slides scale further before "give up and overflow" — fonts can shrink to ~12px (still readable) before allowing visible cutoff.
- **Stale agenda count in social-margins s2**: "What We Cover in 110 Slides" → "What We Cover in 123 Slides" (deck has been at 121 then 123 slides for some time; agenda was never updated).

### Added — universal fit tightening (all 7 decks)
- Consistent slightly-tighter base spacing applied across every slide so most content fits naturally without needing zoom. **No font-size changes** — only padding, margins, and line-height adjustments. This is the "broad CSS rule" the user asked for.
  - `.slide-content` padding `24px 40px 20px` → `18px 36px 16px` (saves ~10px vertical, 8px horizontal)
  - `.slide-title.md/.sm` margin-bottom `10/8 → 6/4px` (saves ~4px each)
  - `.bullet-list` gap `10 → 7px`, line-height `1.55 → 1.5` (saves ~10px on long lists)
  - `.hbox` padding `14 → 11px`, hbox-text line-height `1.55 → 1.45` (saves ~6px each)
  - `.term-box` padding `18px 22px → 14px 18px`
  - `.dark-card` padding tightened (saves ~4-6px each)
  - `.col-panel`, `.stat-card` padding tightened
  - `.ctable td/th` padding `10→8px`, line-height `1.4` (saves ~4-8px per row across long tables)
- Net effect: every slide gets ~30-50px more usable vertical space than before, so most content fits naturally. Auto-fit zoom only kicks in for genuinely dense slides.

## [10.23.33] - 2026-05-03

### Added
- **Social Margins 101 — split overflowing s117 + s118 into 4 slides total**. User confirmed both reading list (s117, 26 items) and glossary (s118, 24 terms) overflow at full font size; user said "break for both."
  - **s117** now: "Where to Go Next — Primary Indian Sources & Data" — 10 items split into 2 columns (foundational documents | surveys & data).
  - **s118** (NEW): "Where to Go Next — Major Scholarly & Literary Works" — 16 items split into 2 columns (foundational thinkers | modern scholarship + literary voices).
  - **s119** (was s118): "Working Glossary I — Cross-cutting & Caste" — 12 terms (Intersectionality, Subaltern, Recognition vs Redistribution, Brahmanical patriarchy, Varna/Jati, Dalit, Adivasi/ST, Bahujan, Pasmanda, NALSA, Section 377, Hijra).
  - **s120** (NEW): "Working Glossary II — Identity Vectors & Acts" — 12 terms (Brahmanical patriarchy × sexuality, RPWD Act 2016, Social model, Communalism, Sub-nationalism, Untouchability, Endogamy, SC/ST/OBC/EWS, PoA Act 1989, Mandal, Manual scavenging, Honour killing).
  - **s121, s122, s123** — renumbered from s119/s120/s121 (MPI chart, Scavenging chart, End slide). Total slides now 123 (was 121).

## [10.23.32] - 2026-05-03

### Fixed
- **Social Margins 101 — duplicate s121 slide removed**. User flagged slides 119, 120, 121 all "blank". Investigation revealed s120 and s121 were duplicate "Manual Scavenging Deaths" chart slides (both with canvas `id="sm_scavenging_deaths"`) — likely from a merge resolution that didn't dedup properly. Since ECharts can only initialize one canvas per ID, the second instance was always blank. Removed s121, renumbered End slide s122 → s121, updated SLIDE_IDS array, fixed end-byline mention. Total slides now 121.
- **Chart slides showing blank on first view across all 7 native decks**. ECharts canvases initialize when the deck loads — but only the first slide is `display:flex`; all others are `display:none`. A canvas inside a hidden parent has 0 width at init time, so ECharts creates the chart but renders to a 0×0 canvas. When the user navigates to the chart slide, the canvas now has dimensions but no resize event fires, so the chart stays blank. Fix: added `MutationObserver` on `.slide.active` class changes that calls `echarts.getInstanceByDom(canvas).resize()` for every chart canvas in the newly-active slide. Initial pass at 400ms ensures even the deck's first chart slide (if active at load) renders properly.

### Known follow-ups (not in this PR)
- **Slides 117 + 118 in social-margins overflow** — s117 has 26 list items (Where to Go Next reading), s118 is a 4898-char working glossary table. Both need editorial trim or split. Will scope per slide.
- **Slides 2, 55, 113 reported as "mostly blank"** — these all have content in source (TOC, table, bullets respectively); user reporting them as blank may be a rendering issue separate from the chart fix above. Need user re-check post-deploy to confirm.

## [10.23.31] - 2026-05-03

### Added
- **Proportional auto-fit rule** across all 7 native decks. User asked: "No content exceeds the viewport dimensions without shrinking font too much and also without allowing overflow." Implementation: at slide-active change, JS measures `slide-content.scrollHeight` vs `clientHeight` — if natural content exceeds available space, applies CSS `zoom` to scale the entire slide-content down proportionally (fonts, padding, margins, and image dimensions all shrink together so visual hierarchy is preserved). Hard floor at **0.85x** (max 15% reduction) so fonts stay readable (~13px minimum on a 15px base). Below that scale, the slide is allowed to overflow rather than become unreadable — signal that the slide genuinely needs editorial trimming.
- **Compared to v10.23.22's auto-compact**: that approach used selective font-size reductions (only some elements got smaller, breaking visual hierarchy) and went all the way to 11px ultra-compact. The new auto-fit is proportional (everything scales together) and capped at a 15% reduction, so it never makes text unreadable.
- Deck behaviour: most slides need no scaling. A few slightly-overflowing slides scale to ~0.92-0.97x (visually almost identical to base). Heavily overflowing slides (those that needed `.compact` or `.ultra-compact` in v10.23.22) overflow visibly — flagging them for content trim.

## [10.23.30] - 2026-05-02

### Added
- **Slide deep-linking via URL hash** across all 7 native decks. The URL now updates as you navigate (`#s1` → `#s2` → ...). Pasting a deep-link URL like `https://www.impactmojo.in/101-courses/climate-essentials.html#s31` jumps directly to slide 31 on load. Browser back/forward buttons now traverse slide history. Implementation: `MutationObserver` watches `.slide.active` class changes and syncs `location.hash` via `history.replaceState` (no page reload). On load + on `hashchange` event, parses the hash and calls the deck's own `showSlide()`/`show()` function (tries multiple signatures), falling back to manual class swap + progress UI update if no API matches.

### Fixed
- **Climate-essentials slide 4 overflow** — removed the redundant Pakistan floods bullet (`<li>The 2022 Pakistan floods were made 50% more likely…</li>`) that was getting clipped at the bottom now that font-shrinking is disabled. Same data point appears in slide 9's "Attribution evidence" hbox with fuller context (one-third of country underwater, 1,700 deaths, $30B damage), so no information is lost.

## [10.23.29] - 2026-05-02

### Changed
- **No more font shrinking on slides**. User explicitly: "I dont want to shrink fonts. I want to make sure the content is proportionately and consistently fitting." Removed `class="slide compact"` from all 51 manually-marked slides across 7 native decks (climate 6 + dev-econ 7 + inequality 5 + mel 4 + pub-finance 18 + social-margins 3 + work-labour 8). Also disabled the runtime `ensureFit` auto-compact (introduced in v10.23.22) — JS no longer adds `.compact` or `.ultra-compact` classes on overflow detection. CSS rules for `.slide.compact` and `.slide.ultra-compact` remain in the stylesheets but become inert (no slides carry the class). Slides that previously got their fonts shrunk to fit now render at base font sizes.
- **Trade-off acknowledged**: slides that genuinely have too much content for the 1280×720 viewport will now overflow visibly (clipped at the bottom) rather than auto-shrink. This makes content overflow obvious so it can be addressed editorially (split into 2 slides, trim content) rather than masked by font reduction.

### Fixed (slide structure)
- **Slide 31 climate-essentials (Carbon Budget — Stern vs Nordhaus)** — `<div class="two-col half">` was closing too early before the right column, orphaning the right-column stat-grid + hbox outside the grid container. Right column now properly nested inside two-col.
- **Slides s4 climate, s4 + s63 dev-economics** — same orphaned-right-column malformation, fixed via Python regex pattern matcher.

## [10.23.28] - 2026-05-02

### Fixed
- **Bullet-list `<strong>` no longer breaks into a separate column**. Across all 7 native decks. The `.bullet-list li` rule used `display:flex; gap:12px; align-items:flex-start` with the bullet as a `::before` pseudo-element — but inline children of a flex container become flex items themselves, so each `<strong>...</strong>` was rendering as a separate flex item alongside the trailing text node. Result: the strong got its own narrow column and the body text got a wider one, so on slide 10 of climate-essentials (Carbon Budget) "Deep decarbonisation:" wrapped to its own column while the body "Energy systems, transport..." rendered in a parallel column. User flagged this as the "deep carbonisation misalignment".
- Replaced flex layout with `position:relative` + `padding-left:19px` on `<li>` and `position:absolute; left:0; top:9px` on `::before`. The bullet dot floats outside the text flow; strong + body text now wrap together as a single inline flow. Applied to all 7 decks (each had different default bullet colors — handled). Responsive override updated from `margin-top:7px` to `top:8px` to match the larger 8px bullet on bigger screens.

## [10.23.27] - 2026-05-02

### Fixed
- **Stat-grid cards now size to their own content** — across all 7 native decks. Changed `.stat-grid { align-items: stretch }` (default) to `align-items: start`. Previously cards in a row stretched to match the tallest sibling, leaving empty space at the bottom of cards with shorter labels. Now each card is just as tall as its own content; the row no longer shows uneven empty space below shorter labels. User flagged this pattern as the broader version of the v10.23.26 stat-card alignment issue.

## [10.23.26] - 2026-05-02

### Fixed
- **Stat-card label alignment** across all 7 native decks. The v10.23.21 "alignment hardening" added `.stat-card .stat-label{flex:1 1 auto; margin-top:auto}` which pushed the label to the BOTTOM edge of equal-height stat-cards in a grid — creating an awkward gap between the stat-number and the label whenever cards stretched to match the tallest sibling. User flagged climate-essentials slide 10 (Carbon Budget) where the 380 GtCO₂ + 10 years stat-cards showed the gap most clearly. Removed the offending flex rules so stat-cards revert to natural block layout: number on top, label right below, no forced bottom-anchoring. Cards still equal-height via grid `align-items:stretch` default; extra space (when any) sits at the bottom edge of the card, not in the middle.
- Also removed two over-broad rules from v10.23.21 that forced `display:flex; flex-direction:column` on every `<div>` child of inline `display:grid` containers (caused unintended layout shifts on hand-coded grids in some slides).

### Kept
- `.two-col, .two-col.half/.a32/.a23 { align-items:start }` — top-aligns side-by-side columns when content heights differ. Genuine improvement, retained.
- `.col-panel { display:flex; flex-direction:column }` + `.col-panel-title { flex:0 0 auto }` — keeps col-panel titles at top with body flowing below. Retained.

## [10.23.25] - 2026-05-02

### Added
- **Social Margins 101 Phase 2 vector expansion** — 7 new deeper data + practice slides inserted into Section 12 (slides 108-114), one per vector beyond the existing primer. Section 12 now carries 17 slides total (was 10).
  - **s108 — Adivasi Land Loss & Forest Rights**: FRA 2006 implementation gap (~13% of CFR claims granted), 50%+ of all displacement is tribal, Hasdeo/Niyamgiri/Pathalgadi flashpoints, Schedule V vs VI vs PESA. Practitioner FPIC translation.
  - **s109 — Religious Minorities — Sachar to Citizenship**: Sachar 2006 (Muslims worse than SCs), Misra 2007 + Ranganath Mishra (Dalit Christian/Muslim SC eligibility pending), CAA 2019 + NRC Assam (1.9M excluded), 12-state anti-conversion laws.
  - **s110 — Gender Beyond Caste**: care economy 297 vs 31 min/day (9.6× gap, widest in G20), FLFPR 33% recovery, MMR 97/100K (Kerala 19, Assam 195), SRHR access. Counter to "gender mainstreaming" as add-on.
  - **s111 — Queer & Trans Post-NALSA**: NALSA 2014, Section 377 read-down 2018, Trans Persons Act 2019 critique vs Pakistan 2018 Act, marriage equality 2023 verdict (Supriyo Chakraborty), hijra/khwaja sira historical recognition.
  - **s112 — Disability — The 4% Reservation Reality**: Census 2.21% vs WHO 15-20% (measurement politics), 4% PwD reservation only ~1.5% filled, 27% disabled children out of school, NMHS mental health gap (150M need care, <9k psychiatrists).
  - **s113 — Linguistic Federalism**: 22 Eighth Schedule + 800 unscheduled, Three-Language Formula NEP 2020, Tamil Nadu anti-Hindi politics since 1965, language as gatekeeper for state employment + judicial access.
  - **s114 — Class as a Vector**: Top 1% wealth share 40.6% (Oxfam 2023), 36% of BPL households are SC/ST, EWS 10% reservation (Janhit Abhiyan 2022), within-caste class differentiation. Why income-only and caste-only targeting both miss what the other captures.
- Each new slide carries: structural body paragraph, 4 bullet points with citations, and a colored callout box ("practitioner translation" / "for programme design" / etc.). Templates use the existing `.two-col.half`, `.bullet-list`, `.hbox` styles.

### Changed
- **Slide IDs renumbered** in social-margins: existing s108-s114 (Section 13 + appendix charts + End slide) shifted to s115-s121. SLIDE_IDS array extended; End slide footer `slide-number` updated to 121.
- **TOC entry** for Section 12 updated from "Slides 98-107" → "Slides 98-114".
- **Section 13 entry** in Reading the deck note updated from "108-110" → "115-117".
- **Section 12 divider subtitle** rewritten to mention the 8 primers + 7 deeper slides structure.

### Result
- Social Margins 101 deck now has **121 total slides** (was 114) with substantively expanded treatment of all 7 vectors beyond caste. Phase 2 closed.

## [10.23.24] - 2026-05-02

### Added
- **One more ECharts data slide per native deck** (7 new charts, total now 4 per deck), inserted just before the End slide:
  - **climate-essentials** — India's power mix 2010 vs 2024 (stacked bar). Coal still ~50% of installed capacity, but solar grew 0.2 GW → 90 GW. Source: CEA / Ministry of Power.
  - **dev-economics** — India MPI decline 2005-06 → 2019-21 (line+area). 55.1% → 16.4% headcount; 415M people exited multidimensional poverty. Source: NITI Aayog / OPHI.
  - **inequality-basics** — India consumption Gini 1983-2022 (line). Stable through 1990s; rose with liberalisation. Source: NSSO + PLFS.
  - **mel-basics** — RACI matrix heatmap (6 tasks × 5 roles, R/A/C/I codes). Programme Manager accountable; M&E officer responsible for indicator framework; Field Team responsible for data collection.
  - **public-finance-budgeting** — India fiscal deficit Centre + States + Combined 2010-2024 (multi-line). Combined deficit averaged ~6.5% pre-COVID, jumped to 13.3% in 2020-21, slow consolidation since. Source: RBI State Finances + Union Budget.
  - **social-margins** — Manual scavenging deaths in India 2013-2023 (bar). 39-117 deaths/year despite the 2013 Prohibition Act. Over 95% of victims are Dalits. Source: NCSK + Ministry of Social Justice.
  - **work-labour-livelihoods** — India labour share of GVA 1981-2022 (line+area). Fell from ~60% to ~50% — a 10pp shift from labour to capital, mirroring global middle-income trend. Source: Penn World Tables + RBI.
- End slide IDs renumbered s103 → s104 (s113 → s114 in social-margins) to make room.

### Updated (Wiki)
- **`101-Course-Decks.md`** — full rewrite reflecting the 40-course state with 7 native HTML decks + 31 Gamma + 2 coming soon. Documents native deck features (end slides, charts, runtime overflow detection, auto-spacious, table improvements, logo→landing, fullscreen pill).
- **`Changelog.md`** — condensed v10.23.13-23 summary entry covering 11 point releases.

## [10.23.23] - 2026-05-02

### Fixed
- **axe-core SERIOUS color-contrast violation resolved** on all 12 flagship Resources & Practice cards. Eyebrow text on `.lab` (#10B981 → #047857), `.notebooklm` (#6366F1 → #4338CA), `.course101` (#0EA5E9 → #0369A1), and `.dojo` (#EF4444 → #B91C1C) cards previously failed WCAG 2.1 AA at 2.54-4.47:1 contrast on white card backgrounds. New darker variants all clear ≥5.4:1 (PASS). Same hue family preserved — only brightness reduced. Affected: SEL, dataviz, devai, devecon, gandhi, gender, law, media, mel, poa, pubchoice, pubpol.
- **axe-core image-redundant-alt warning** on `.sidebar-logo-icon > img[alt="ImpactMojo"]` resolved across 7 flagship pages (mel, devecon, law, media, poa, pubchoice, pubpol). The img sits in the same `<a class="sidebar-logo">` as a `<span class="sidebar-logo-text">ImpactMojo</span>` — the alt was redundant. Set `alt=""` so the image is treated as decorative and the link is labelled by the visible text.
- **axe-core landmark-region warnings** resolved:
  - `index.html` practitioner trust strip: `<div class="practitioner-trust-strip">` → `<aside aria-label="Practitioner trust">`. The 8 social-proof spans (Multilateral Banks, UN Agencies, Research Institutes, etc.) are now inside an aside landmark.
  - `bct-repository.html` `#compareBar`: `<div>` → `<aside role="region">`.
  - All 12 flagship topbars: added `role="navigation" aria-label="Site navigation"` to `<div class="im-topbar" id="imTopbar">`. The browse/premium/theme-selector children are now inside a navigation landmark.

### Result
- axe-core CI check that has been failing on every commit since v10.23.16 should now pass.
- pa11y-ci, Validate HTML, Check broken links, and main CI workflow continue to pass.

## [10.23.22] - 2026-05-02

### Fixed
- **Real overflow detection replaces heuristic auto-compact** across all 7 native decks. The v10.23.19 heuristic (≥11 li / ≥2 tables / >1900 chars) missed slides that genuinely overflowed but didn't hit any of those thresholds — e.g. climate-essentials slide 4 (5 bullets + 1 hbox + 1 5-row component grid: cut off at the bottom). Replaced with a runtime check that observes `scrollHeight > clientHeight` on the active slide's `.slide-content` container and applies `.compact`. If the slide still overflows after compact is applied, an `.ultra-compact` class escalates further (smaller fonts, tighter padding, denser table cells/hboxes/term-boxes/col-panels). MutationObserver re-runs the check whenever a new slide becomes active and on window resize. Net effect: any slide that doesn't fit gets auto-tightened until it does, regardless of whether the overflow comes from bullets, tables, info-boxes, term-definitions, stat-cards, or grid-based component lists.

## [10.23.21] - 2026-05-02

### Fixed
- **Pseudo-table alignment hardening** across all 7 native decks. User reported "table block" layouts where text was misaligned because the layouts use div-grids rather than `<table>` elements. Without a specific slide reference, applied structural alignment fixes to the most common pseudo-table patterns:
  - `.stat-grid` cards now use flex column with `stat-label` pushed to bottom (`margin-top:auto`) so labels align across a row even when card heights differ from variable text wrapping.
  - `.col-panel` uses flex column with title fixed at top, body flowing below.
  - `.two-col` (and variants `.half`, `.a32`, `.a23`) get `align-items:start` so content top-aligns when column heights differ.
  - Inline `display:grid` divs inside `.slide-content`: cells now use flex column for predictable internal alignment.
- Speculative fix; awaiting specific slide URL for targeted treatment of remaining cases.

## [10.23.20] - 2026-05-02

### Fixed
- **Fullscreen button no longer covers `www.impactmojo.in`** in slide-header. Added `padding-right:120px` to `.slide-header` across all 7 native decks, pushing the right-hand `header-url` text leftward so the fs-hint pill (positioned `right:18px`) sits in clear space and no longer obscures the URL text.

### Added
- **Auto-spacious mode** for sparse slides — symmetric counterpart to v10.23.19's auto-compact. JS heuristic adds `.slide.spacious` to any non-compact, non-divider slide with under 420 characters of text content (excluding chart canvases and tables). Spacious mode bumps `slide-title.sm` from 24px → 30px, `slide-body` from 15px → 17px, `bullet-list li` from 15px → 16px, and adds 18px padding on `hbox` callouts. Slides that previously looked underfilled with small fonts now read with appropriate visual weight.
- **One new ECharts data slide per native deck** (7 charts total), inserted just before the End slide:
  - **climate-essentials** — CO₂ per capita 2023 by region (horizontal bar). Africa 1.0 / India 1.9 / EU 6.4 / China 7.7 / Russia 11.4 / USA 14.4 t/cap. Source: Global Carbon Project / Our World in Data.
  - **dev-economics** — India sectoral GDP composition 1950-2023 (stacked area). Agri 51%→17%, Industry 14%→27%, Services 35%→56%. Source: World Bank / RBI.
  - **inequality-basics** — Top 1% pre-tax income share, cross-country comparison (horizontal bar). Sweden 11.7% → South Africa 21.9%, with India at 21.7%, USA 20.5%. Source: WID 2024.
  - **mel-basics** — Theory of Change as a 5-node directed graph (Inputs → Activities → Outputs → Outcomes → Impact) with arrow-labelled link types (efficiency, effectiveness, attribution, contribution).
  - **public-finance-budgeting** — Tax-to-GDP ratio cross-country bar. Bangladesh 8% / Indonesia 12% / India 17.8% → Brazil 32.5% / OECD 33.8% / Norway 39.8%. Source: World Bank / OECD / IMF.
  - **social-margins** — Multidimensional Poverty headcount by social group (India 2023). ST 21.4% / Muslims 14.4% / SC 14.0% / OBC 11.5% / National 11.3% / Hindus 11.6% / Others 7.5%. Source: NITI Aayog National MPI 2023.
  - **work-labour-livelihoods** — India female LFPR (15+) 2017-18 → 2022-23 (line with area). 17.5% → 33.0% trajectory. Source: PLFS annual rounds.
- Each new chart slide carries: section label, contextual paragraph, full-width canvas, and "what to see" amber-callout takeaway.
- End slide IDs renumbered from `s102` → `s103` (and `s112` → `s113` in social-margins) to make room.

### Fixed (drive-by)
- Typo `www.impacctmojo.in` → `www.impactmojo.in` in dev-economics deck slide-footer (one slide).

## [10.23.19] - 2026-05-02

### Fixed
- **Native deck formatting polish — fullscreen button, nav overlap, content overflow** across all 7 native decks.
  - **Fullscreen button (`#fs-hint`)**: previously rendered at 9px font with 25% white opacity — barely visible, sometimes mistaken for being clipped/cut off. Repositioned with safer margins (top:14px, right:18px), bumped font to 10px, raised contrast to 85% white, added a translucent dark pill background (with dark-mode counterpart) and 14px border-radius. Now obviously a clickable element.
  - **Bottom navigation overlap**: `#nav` fixed at `bottom:16px` was sitting visually on top of slide content because the slide-viewport scales to fill the browser window. Added a fade-on-idle behaviour (drops to 18% opacity after 2.2s of no input; full opacity on hover or any mouse/keyboard/touch activity). Also increased `.slide-content` bottom padding from 20px to 46px so content doesn't crowd into the nav strip even when nav is fully visible.
  - **Content overflow auto-compact**: added a JS heuristic that runs at load and adds the existing `.slide.compact` modifier to any slide with ≥11 `<li>` items, ≥2 `<table>`s, or >1900 characters of text. Skips title screens, section dividers, end screens, and TOC slides. Existing `.slide.compact` rules already shrink fonts and padding on dense slides; auto-application means content-heavy slides no longer overflow the 1280×720 viewport. Also tightened `.slide.compact` rules for tables (`.ctable td` 12px / 6px padding), info-boxes (`.hbox` 10px padding, 12.5px text), and bottom-padding on the content area.

### Known follow-ups (not in this PR)
- Some slides have **too little content** with small fonts on otherwise-empty slides — opposite of overflow. Needs per-slide content audit and either copy expansion or font promotion (`slide-title sm` → `lg`). Out of scope for a structural CSS fix.
- **Charts/diagrams density**: most decks currently carry only 2 ECharts data slides each (the v10.23.15 batch). User asked for more diagrams across decks — that's substantive content work (research, data sourcing, ECharts authoring per slide) and warrants its own PR.

## [10.23.18] - 2026-05-02

### Fixed
- **Native 101 deck tables — added inside borders + vertical alignment** across all 7 native decks (climate-essentials, dev-economics, inequality-basics, mel-basics, public-finance-budgeting, social-margins, work-labour-livelihoods). The `.ctable` class previously had only `border-bottom` on `<td>`, no vertical separators between columns, and no `vertical-align` rule — multi-line cells looked misaligned and columns blurred together. Added: outer 1px border, vertical right-borders on every `<th>`/`<td>` (with `:last-child` cleared), `vertical-align: top` so wrapped text in one cell doesn't drag adjacent cells with it, and `tr:last-child td { border-bottom: none }` for a clean bottom edge. Dark-mode counterparts also added. Tables now read as proper grids rather than horizontal-stripe blocks.
- **Slide-header logo links → 101 Series landing page** across every slide in all 7 native decks (724 links updated total: 102 per deck × 6 + 112 in social-margins). Previously the logo on every slide pointed to `https://www.impactmojo.in` (homepage), which made it hard to jump back to the 101 Series landing without navigating up two levels. Now the logo on every slide (including the end slide) points to `https://www.impactmojo.in/101-courses/` — the real landing page for the 101 deck context. Single click from any slide → browse all 40 101 courses.

## [10.23.17] - 2026-05-02

### Fixed
- **Browse button redesign across 118 inner pages.** The previous Browse-link styling was a flat text link with muted colour — visually weak next to the gradient Premium button. Replaced site-wide with an outline button: 1.5px border, uppercase Inter 700, 0.5rem padding, hover state that fills with the cyan accent + lifts on translateY + adds soft shadow. Dark-mode variant uses translucent white background. Result: better visual balance with the Premium button, more inviting interaction state. Affected: all flagship course pages, all 101 deck landing pages, all DeepDives pages, all BookSummary pages, all top-level pages.

## [10.23.16] - 2026-05-02

### Added
- **Universal "Resources & Practice" cross-link section** added to all 12 flagship course pages (SEL, dataviz, devai, devecon, gandhi, gender, law, media, mel, poa, pubchoice, pubpol). Each section carries 7 colour-coded resource cards: Hands-on Lab (course-specific or generic), NotebookLM AI Companion (with course-specific URL where available — 11 of 12 flagships have one), Foundational 101 Decks (course-specific recommendations + browse-all), BookCompanion Field Companions (course-specific + browse-all), Print-Friendly Reference Handouts, Live Dojo Practice Sessions, Premium Tools & Coaching. Closes the long-running flagship parity ask: every flagship now has a consistent baseline of cross-linked resources, regardless of how rich its main content is.
- Per-flagship customisation: dataviz cross-links the dataviz lab + storytelling/info-we-trust books; mel cross-links TOC Lab + MEL Plan Lab; gender cross-links 3 thematically-related 101 courses (SRHR, care economy, data feminism); pubchoice cross-links Political Economy + Public Finance 101 + Indian Constitution 101; etc.
- Bespoke Sargam-style SVGs replace 21 remaining body emojis (📚 📧 💬 👋 ♥ 🌐 📩 ⚠ 📏 🏆 🎓 🗓) across 7 files (`accessibility.html`, `blog.html`, `blog/sample-size-matters.html`, `blog/whats-coming-in-2026.html`, `catalog.html`, `content-marketing-kit.html`, `forgot-password.html`). Body emojis platform-wide now at zero.

## [10.23.15] - 2026-05-02

### Added
- **14 substantive ECharts data slides** across all 7 native ImpactMojo-hosted 101 decks (2 per deck). Each slide carries: contextual paragraph above the chart, full-width visualisation in a bordered canvas, and a "what to see" amber-callout takeaway below. Charts use the requested fancy types (no pies):
  - **climate-essentials**: Sankey of global CO₂ emissions (energy carrier → sector, ~37 GtCO₂); area chart of NASA GISTEMP temperature anomaly 1880-2023.
  - **dev-economics**: Multi-series line panel of South Asia per-capita GDP (PPP) trajectories 1990-2023 — India, Bangladesh, Pakistan, Sri Lanka, Nepal; Sankey of India's structural transformation (workforce 1991→2011→2023, by sector).
  - **inequality-basics**: Area chart of India top-10% income share 1922-2022 (V-shape); Lorenz curve of India wealth distribution 2023 (WID).
  - **mel-basics**: Bubble panel of evaluation methods (rigour × feasibility × cost) — RCT, DiD/RDD, PSM, pre-post survey, contribution analysis, outcome harvesting, qualitative, MSC; circular graph linking indicator types (input/output/outcome/impact) to MEL methods.
  - **public-finance-budgeting**: Union Budget Sankey (tax revenue → expenditure heads, FY24); multi-country debt/GDP panel (India, Bangladesh, Pakistan, Brazil, China, USA, Japan).
  - **social-margins**: Identity-intersection chord (caste/tribe/religion/gender/sexuality/disability/region/class with edge-weights reflecting empirical co-incidence); SC/ST PoA Act atrocity cases bar+line panel 1995-2022 (cases + conviction rate).
  - **work-labour-livelihoods**: Stacked area of India workforce share by sector 1983-2023; Sankey of formal/informal decomposition of India's workforce (PLFS 2022-23).
- ECharts 5.5.0 added to all 7 native decks — supports sankey, chord, area, beeswarm, parallel coordinates, custom layouts.
- New `.slide.compact` modifier: tighter font/spacing for slides with 11+ list items (PFB) or 14+ li / 320+ words (others). 51 slides marked compact across the 7 decks (PFB 18, climate-essentials 6, dev-economics 7, inequality-basics 5, mel-basics 4, social-margins 3, work-labour-livelihoods 8).

### Fixed
- **Work, Labour & Livelihoods 101 slides 13-15 overflow** marked compact.
- **All 7 native deck SLIDE_IDS arrays** rebuilt to include new chart slides — total slide counts now: climate-essentials 102, dev-economics 102, inequality-basics 102, mel-basics 102, public-finance-budgeting 102, social-margins 112, work-labour-livelihoods 102. Progress text + TOTAL constants synchronised.
- All chart slide IDs renamed from temporary `sN_chart` form to plain sequential `sN` for navigation continuity.

## [10.23.14] - 2026-05-02

### Added
- **Social Margins 101 Section 12: The Other Vectors — A South Asian Survey** (10 net-new slides). Substantively expands the deck from 100 to 110 slides with vector-specific primers on tribal/Adivasi, religion, gender (broader), sexuality & queer/trans, disability, region & language, class, migration & statelessness, plus a closing practitioner toolkit. Each primer includes structural framing, foundational voices, key indicators, constitutional/statutory architecture, and intersectional cautions. Honest accounting: caste sections (02-11) retain their depth, but the deck now genuinely delivers on its broader name.
- **101-courses/index.html** — new landing page for the ImpactMojo 101 Series. 40 courses with native HTML / Slide Deck / Coming Soon filter chips, search, tracks, hero stats, full SEO + GA. Sitemap entry, /101 short-URL redirect.
- **Standardised end slide** across all 7 native ImpactMojo-hosted 101 decks (climate-essentials, dev-economics, inequality-basics, mel-basics, public-finance-budgeting, social-margins, work-labour-livelihoods). New `.end-screen` template with gradient background, dot pattern, glow effect, gradient bar, gradient-text "Thank You" headline, byline, 3 themed CTAs (primary gradient / secondary outline / tertiary ghost), meta footer with CC BY-NC-ND. Replaces 7 different bespoke ugly closing slides with one consistent beautiful template.

### Fixed
- **Public Finance & Budgeting 101 overflow**: 18 dense slides (11+ list items each) marked with new `.slide.compact` modifier. Reduced font-size, line-height, and padding within compact slides to fit content within the fixed 1280×720 viewport. Same compact treatment applied conservatively (14+ li or 320+ words threshold) to 30 dense slides across the other 6 native decks.
- **Stale 101.impactmojo.in references**: removed from native deck end slide CTAs; replaced with self-hosted `/101-courses/` URL throughout.
- **Slide 100 (thank-you) on Social Margins**: stale link fixed; CTAs swapped from devecon/poa/101.impactmojo.in to gender/poa/decolonize-dev which are thematically aligned with Social Margins; later replaced entirely by the new standardised end-slide template.

### Changed
- Social Margins TOC + agenda updated to reflect 110 slides + new Section 12 (slides 98-107) + renumbered Section 13 (Further Reading, Glossary, Thank You at slides 108-110). Reading-the-deck guide rewritten to describe the new structure.
- HTML balance: 1494 → 1656 open/close divs in social-margins.html (added 10 substantive slides + Section 12 divider + agenda expansion). All 7 native decks balance-checked.

## [10.23.13] - 2026-05-02

### Changed
- **Groups 9-14 audit batch.** Closed all six remaining content-type audits (101-courses, Deep Dives, Blog, Top-level pages, Flagship course pages, NotebookLM registry). 130 files scanned across 6 groups; 86 files patched in a single commit.
- **SEO baseline 100%** across all 130 audited files: 14 canonical links + 38 og:image + 70 og:site_name + 4 full twitter:card blocks added. Default og:image is the ImpactMojo logo at `/assets/images/ImpactMojo Logo.png`. Twitter cards include matching title/description/image. Inserted after the last existing `og:` tag where present, otherwise after meta description.
- **3 native 101 decks (PFB, social-margins, work-labour-livelihoods)** received full SEO + Google Analytics installation: meta description, robots, canonical, og:type/title/description/url/image/site_name, twitter:card block, and the GA G-JRCMEB9TBW snippet. Previously they had only `<title>` + viewport because the Claude-Chat-generated slide-deck template ships with minimal head metadata.
- **54 dingbat replacements** (✓ ✗ ✦ ✧) → inline Sargam-style stroke SVGs across 14 files: `101-courses/mel-basics.html` (10 ✗/✓ marks in pros/cons lists), `blog/learning-by-doing.html` (1), `blog/theory-of-change-pitfalls.html` (5 ✓ Strong labels), `content-marketing-kit.html` (8), and 10 flagship course pages (3 sparkles each in v3-hero decoration). SVGs sized via `width:1em; height:1em` with `vertical-align:-0.15em` to inherit text colour and baseline.
- **NotebookLM registry verified clean**: 11 entries, all with title + URL, JSON valid. No drift between registry and platform claims.

### Known drift (deferred)
- 21 real-emoji chars remain across 7 files (📚📧💬👋♥🌐📩⚠📏🏆🎓🗓): used as functional UI category icons (`accessibility.html`, `forgot-password.html` chatbot menus), friendly greetings (`👋` on `blog.html`, `catalog.html`), and content emphasis (3 in `whats-coming-in-2026.html`). Need bespoke 1:1 SVG mapping per use case rather than bulk substitution. Tracked for a dedicated emoji-to-Sargam pass.

## [10.23.12] - 2026-05-02

### Changed
- **Social Margins 101 — Phase A finish (lightweight cross-vector signposting).** Caste content in sections 02-11 retained as the deepest vector treatment in the deck; each section divider now carries an italic "Parallels" subtitle explicitly connecting the section's analytical frame to other vectors (tribe, religion, gender, sexuality, disability, region, language, class). Examples: section 04 (Colonialism & Census) parallels — Hindu/Muslim binary, Scheduled Tribes vs PVTGs, Hindi/Urdu wedge, criminalised hijra under CTA 1871; section 05 (Constitution) parallels — Schedules V/VI, Articles 25-30, NALSA, RPWD Act; section 11 (Contemporary Debates) parallels — caste census ↔ religion-based reservation, EWS ↔ poverty as vector, AI bias ↔ identity surveillance.
- Agenda note (slide 2) rewritten from "deep treatment of caste anchored by..." to a "Reading the deck" framing that names where each vector is treated and explicitly signposts the parallels mechanism.
- Added `.div-subtitle` CSS rule (italic 15px, 62%-opacity white, max-width 680px) to support cross-vector subtitles on section dividers.
- HTML balance preserved (1494 open / 1494 close divs, 100 slides). Phase A is considered complete for v10.23.x. Net-new vector sections (Tribal/Adivasi, Religion broader, Gender broader, Sexuality, Disability, Region/Language, Class) as their own slide modules are tracked for future releases under the broader Social Margins expansion.

## [10.23.11] - 2026-05-01

### Changed
- **Caste Studies 101 folded into expanded Social Margins 101.** User feedback: separate Caste Studies course was too narrow; Social Margins is the better umbrella name for a course covering all identity vectors (caste, tribe, religion, gender, sexuality, disability, region, language, class). Architectural switchover (`fd3c909`) shipped first; Phase A content expansion ongoing across releases.
- **Foundational course count: 41 → 40** (Caste Studies merged into expanded Social Margins). 4 native HTML decks now: social-margins, public-finance-budgeting, work-labour-livelihoods, plus 36 Gamma-hosted.
- `social-margins.html` (was the Gamma-only Marginalised Identities 101) now lives as a 100-slide native HTML deck:
  - Section 01 (slides 3-8) **fully rewritten** to be foundational across all identities — "What Are Social Margins?", "Vectors of Marginalisation", "Foundational Voices on Identity & Marginalisation" (Ambedkar, Crenshaw, Spivak, Iris Marion Young, Phule, Uma Chakravarti), "Categories That Shape Identity Analysis" (ascribed/achieved, visible/invisible, identity/structure, recognition/redistribution), "Intersectionality — How Identities Compound" (Crenshaw + South Asian translation).
  - Sections 02-11 (slides 9-97) currently retain the existing strong caste content (origins, anti-caste thought, colonialism/census, Article 17/reservations, economy, violence, education, gender×caste, diaspora, contemporary debates). Agenda transparently flags that broader sections (Tribal/Adivasi, Religion, Gender broader, Sexuality, Disability, Region, Language, Class) are "in expansion in upcoming releases".
  - Section 12 lexicon (slide 99) restructured to a 3-column table with **Vector** annotations — added Intersectionality, Subaltern, Recognition vs Redistribution, NALSA judgment, Section 377, Hijra, RPWD Act 2016, Social model of disability, Communalism, Sub-nationalism alongside existing caste terms.
- 301 redirects: `/101-courses/caste-studies` → `/101-courses/social-margins.html`.
- Catalog `c40` (Caste Studies) deleted; `c17` retitled "Marginalised Identities 101" → "Social Margins 101" with broader scope description. Filter chip 41 → 40.
- Homepage modal: Caste Studies item removed; Social Margins item swapped from Gamma fallback to direct native HTML link with new description. Heading "All Courses (53)" → 52. View-All-Courses button 53 → 52. C16 dropdown option label updated.
- `search-index.json`: `COURSE-CASTE-STUDIES` replaced by `COURSE-SOCIAL-MARGINS` with expanded tag set.
- `sitemap.xml`: caste-studies removed; social-margins lastmod 2026-04-05 → 2026-05-01, priority 0.7 → 0.8.
- 13 docs files updated to reflect 53 → 52 / 41 → 40 counts (README, catalog hero, 11 docs/*.md).

### Note
This is a **Phase B (architectural) commit + partial Phase A (content)**. The deck is correctly named, discoverable, and has rewritten foundational framing — but full deep treatment of non-caste identity vectors as their own sections is queued for upcoming releases. User explicitly authorised iterative refinement: "we can always revise A".

## [10.23.10] - 2026-05-01

### Added
- **Public Choice — 12th flagship course** at `/courses/pubchoice/` — *Decisions, Incentives & Institutions*. 13 modules synthesising the Virginia school (rent-seeking), Bloomington school (commons), and New Institutional Economics, with cases from India, Bangladesh, Pakistan, Sri Lanka, and Nepal. 83-term interactive lexicon. 12th NotebookLM AI Study Companion.
- **3 new 101-courses** — native slide-deck (1280×720, 12 sections) format: *Caste Studies 101* (varna/jati, Ambedkarite thought, anti-caste movements), *Public Finance & Budgeting 101* (Union/state budgets, finance commissions, budget transparency), *Work, Labour & Livelihoods 101* (SNA boundary, care economy, sustainable-livelihoods framework, agrarian question, migration, non-farm economy).
- **Deep Dives** — new content type at `/DeepDives/`: 5 curated annotated reading lists by Sukhmeet Bedi + ImpactMojo Editorial team (Indian Political Economy, Impact Measurement, Climate & Just Transitions in South Asia, Caste/Identity/Development, Data/Power/Global South). Mixed media (books, papers, podcasts, datasets), 2–4 sentence annotations per reading.

### Changed
- **Foundational course count: 38 → 41**. *Work, Labour & Livelihoods 101* supersedes both *Decent Work for All 101* and *Livelihoods 101* (deleted with 301 redirects). Net +3.
- **Performance wins on index.html**: extracted 215 KB inline `<style>` to `/css/imx-main.css` (cacheable, parallel-loadable). Index dropped from 645 KB raw / 96 KB brotli → 431 KB / 64 KB. Repeat-visit TTFB improved from ~1.4s to **175 ms** (8× faster) via Netlify edge caching (`max-age=300, must-revalidate`). Auth scripts deferred to bottom of body.
- **Specials nav restructured** into 4 collapsible accordion subgroups (Reference Libraries, Long-form Reading, Practice & Programs, Behind the Scenes) replacing a flat 13-item dropdown.
- **Reference library proxies cleaned up** — eliminated `on-web.link` shortlinks (one was already 404'ing). PolicyDhara, DevDiscourses now served via Netlify Edge Functions proxying directly from the upstream GitHub Pages repos with injected `<base href>` for asset resolution.

### Fixed (content audit batch — Group 1–8)
- **Reference Libraries**: ImpactLex term count drift (claimed 1,200 vs actual 1,055), DevDiscourses count, FieldCases count — all aligned to source-of-truth across catalog, homepage, FAQ.
- **Search-index**: backfilled 27 BookSummary/Reference/Handout entries that were on disk but missing from `data/search-index.json`. 3 catalog descriptions corrected (Hindi-shipping mojini-guide misclaim).
- **Games**: emoji → SVG migration for climate-action and public-health games (Lucide-style, viewBox 0 0 24 24, 1.5px stroke). Stale `101.impactmojo.in` links replaced with self-hosted paths. `im-topbar` injected into all 16 games.
- **Labs**: `toc-lab` Browse button added. 2 mistyped lab catalog entries corrected.
- **Premium tools**: removed duplicate Code Converter Pro entry. Renamed *Qualitative Research Lab Pro* → *Qualitative Insights Lab Pro* (8 occurrences in source file). 4 missing tools backfilled to catalog (TOC Workbench Pro live; DevData Practice / Visualization Cookbook / DevEconomics Toolkit coming soon). Filter chip 7 → 9. Search-index entries added for all live tools.
- **BookSummaries**: 30 of 31 companions verified clean (viewport, meta, OG, GA, Amaranth, im-topbar, no emojis). Replaced **54 emoji instances** in dt-companion.html (Design Thinking) with inline Sargam-style SVGs across 24 unique characters. All 31 catalog titles confirmed to match canonical `<title>` in source files.
- **Flagship modules**: 5 catalog drifts + 3 homepage drifts in module counts. After fixes, all 12 flagships have consistent counts across catalog, homepage cards, and `id="module-N"` anchors. Specifically: Gandhi 12→13 (home), Devecon 12→13 (home), Dataviz 13→12 (catalog), DevAI 13→12 (catalog), MEL 13→14 (both), SEL 12→13 (catalog).
- **Handouts render bug** in `handouts.html`: `TRACK_MAPPING` had 5 of 6 stale folder-name keys (`Data Analysis Track`, `Gender Studies Track`, `Research Methods Track`, etc.) that didn't match disk. Only Policy & Economics rendered with proper colour/order — the other 5 tracks fell into "Other Resources" alphabetical fallback. Fixed all 5 + added 4 missing mappings (Education and Pedagogy, Thematic Areas, Cross Cutting Resources, Quick Reference Cards).
- **Handouts emoji removal**: replaced **1,317 emoji instances** across 63 handout files (144 unique characters) with inline Sargam-style SVGs. Self-contained (no sprite/CDN dependency) so handouts stay print-portable.
- **Typo fix**: `Handouts/Thematic Areas/South Aisa Region/` → `South Asia Region/`.
- **Count corrections**: catalog + README "400+ handouts" was inflated marketing copy → 85 actual.
- **README + 18 docs files**: backfilled all stale counts (11→12 flagships, 38→41 foundational, 48→53 courses, 400+→85 handouts, 11→12 NotebookLM).
- **Mobile**: sitewide ≤768px padding floor on top-level sections so cards stop bleeding into viewport edge.
- **Specials nav**: all 13 items now use absolute URLs (`/#flagship-courses` etc.). `js/router.js` now respects hash fragments before path-based routes.
- **DevEcon CSS shim**: defined missing `--indigo`, `--cyan`, `--orange`, `--success` aliases in all 4 `:root` blocks of `courses/devecon/index.html` (17 components were referencing undefined vars).
- **Catalog accessibility**: `.track-filter.active` failed WCAG AA contrast (sky-500 on sky-500@20%). Fixed to amber-700 light / sky-300 dark.
- **`faq-bank.js` line 167**: stray `""` syntax error was killing the whole file's parsing — fixed.

## [10.20.0] - 2026-04-20

### Added
- **Book Summary: *Beyond Developmentality* — Debal Deb** (Earthscan, 2009). Deb's eco-socialist critique of the doctrine of development: eight neo-classical myths, "developmentality" as Foucauldian epistemic apparatus, inclusive freedom, strong sustainability grounded in the Basudha farm counter-evidence. 9 chapters + 4 learning pathways + 8 key concepts + 6 South Asia lenses. BookSummaries total: 31 → 32 (with interactive archive).
- **Archived interactive companion** at `/BookSummaries/beyond-developmentality-deb-interactive.html` (original React SPA preserved), linked from the new templated page via "Launch interactive companion".
- Landing card, search-index entry, sitemap entry for the new book.

### Changed
- **Brand refresh across all 31 book summaries.** Every BookSummary now passes the 14-item ImpactMojo brand checklist:
  - Floating paper plane SVG (decorative, 30 files gained it)
  - Skip-to-content link for WCAG 2.4.1 (30 files)
  - `translate.js` defer script (30 files)
  - Favicon + apple-touch-icon (28 files)
  - Full `im-topbar` with logo + Premium CTA + 3-mode theme selector (19 files)
  - Single-file fixes: theme selector for `handbook-social-protection.html`

### Fixed
- Book counters in `BookSummaries/index.html`: total 30 → 31, dev-econ filter 6 → 7.

## [10.19.0] - 2026-04-13

### Added
- **3 new Book Summaries** (28 → 31 total):
  - *Principles for Navigating Big Debt Crises* — Ray Dalio (2018)
  - *Handbook for IPCC Authors: Climate Communications* — Corner, Shaw & Clarke (2018)
  - *Storytelling to Accelerate Climate Solutions* — Coren & Wang (Springer, 2024)
- BookSummaries index cards, search index entries, sitemap URLs, docs updates

## [10.18.0] - 2026-04-12

### Fixed
- **Sitemap coverage** — 87 missing URLs added to `sitemap.xml` (2 courses, 35 foundational, 23 BookSummaries, 18 blog posts, 9 public pages). Total: 84 → 171.
- **Stale 101.impactmojo.in links** — ~100 legacy subdomain refs migrated to local paths in `js/faq-bank.js`, `js/bookmarks-compare.js`, `js/learning-tracks.js`, `js/game-agents.js`, and 4 docs files.
- **Search index phantom labs** — 6 duplicate/phantom lab entries removed, 3 missing labs added. Lab count: 17 → 13.
- **Content count drifts** — `docs/content-guide.md` (flagship 9→11, labs 19→11), `premium.html`, `catalog.html` JS comments corrected.
- **21 `.DS_Store` files** removed from git tracking.

## [10.17.0] - 2026-04-12

### Added
- **Netlify Forms migration** — 12 forms migrated from Formspree (`xpwdvgzp`) to Netlify Forms with `data-netlify="true"`, `netlify-honeypot="bot-field"`, and unique `name` attributes. Email notifications configured for all forms via Netlify hooks API.
- **Engagement drip pipeline** — 5-stage email sequence (Day 0/3/7/14/21) in `send-notification` Edge Function with deduplication via `notifications.metadata.drip_stage`. Day 21 pitches Premium for explorer-tier users with one-time support fallback.
- **Streak tracking** — `update_streak()` PL/pgSQL function increments `profiles.streak_days` on daily login, resets on miss. Called from `auth.js:fetchProfile()` as fire-and-forget RPC.
- **Post-certificate upsell** — `issue-certificate` Edge Function now sends branded congratulations email with certificate number, verification link, and subtle Premium mention for explorer-tier users.
- **Monthly newsletter** — `netlify/functions/monthly-newsletter.mjs` scheduled function (15th, 10:00 IST) parses `docs/changelog.md` for recent additions, pulls content counts from `search-index.json`, sends via `monthly-update` endpoint.
- **Premium sales letter** — `/premium-letter.html` (15KB, standalone, dark mode, mobile responsive). Conversational tone with concrete tool examples and honest pricing rationale.
- **Practitioner Starter Kit** — `/starter-kit.html` with 10 curated handouts across M&E, data, policy, and cross-cutting tracks.
- **Branded email template** — `wrapEmail()` rewritten with navy gradient header, stacked logo, blue title bar, amber-to-red accent bar, dark footer with preference management link.
- **Resend integration** — `RESEND_API_KEY` configured in Supabase secrets. Domain `impactmojo.in` verified with DKIM, SPF, DMARC DNS records added via Netlify DNS API.
- **Notifications tables** — `notifications` and `notification_preferences` tables applied to production Supabase (were defined in migration but never run). RLS policies, indexes, `notify_user()` function, auto-preference trigger, backfill for 14 existing users.
- **Daily engagement cron** — `netlify/functions/daily-engagement.mjs` (02:30 UTC / 08:00 IST) runs engagement-drip, streak-reminders, cohort-deadlines in parallel.
- **Netlify env vars** — `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` set for scheduled functions.

### Changed
- **Netlify form detection** — `processing_settings.ignore_html_forms` changed from `true` to `false` via Netlify API.
- **Documentation** — CLAUDE.md, 4 rules files, 2 agent definitions, 3 command files, 2 skill files updated to reference Netlify Forms instead of Formspree.
- **`auth.js`** — added `supabaseClient.rpc('update_streak')` call after successful profile fetch.

### Removed
- **Formspree dependency** — all references to `https://formspree.io/f/xpwdvgzp` removed from production HTML/JS files. Backups retain historical references.

## [10.14.0] - 2026-04-07

### Added
- **Device-mode default theme resolution** on 70 pages — `:root` now carries light tokens, `@media (prefers-color-scheme: dark) { :root {} }` drives dark, and explicit `body.{light,dark}-mode` + `[data-theme="*"]` overrides keep the theme toggle dominant. Applied to blog posts, Labs, course index + lexicon pages, admin pages, book companion tools, premium tools, `transparency`, `testimonials`, `challenges`, `bct-repository`, `dataverse`, `toc-builder`, `toc-workbench`.
- **Link-in-text-block underline rule** (WCAG 2.1 AA §1.4.1) on 74 content pages — inline `<a>` inside `<main> p` / `<main> li` now carries `text-decoration: underline`, scoped to exclude button-styled anchors.
- **CC BY-NC-ND 4.0 attribution** backfilled into 17 handouts — all 84 handout pages now uniform on every brand-default check.
- **Premium topbar link** added to 11 main-site pages whose only Premium button lived inside the removed duplicate `im-topbar`.
- **Language translation widget** (`js/translate.js`) on `climate-trace-india.html` and `transparency.html`.
- **`id="home"` anchor** on `index.html` hero section so `<a href="#home">` nav links resolve (fixes pa11y NoSuchID).
- **Paper plane SVG** on `courses/gender/lexicon.html` and `courses/pubpol/lexicon.html`.
- **`<footer>` landmark** with ImpactMojo attribution on `courses/pubpol/lexicon.html`.
- **PR-comment permissions** — `accessibility.yml` + `ci.yml` now grant `pull-requests: write` (scoped per job) so `marocchino/sticky-pull-request-comment@v3` stops failing.

### Changed
- **WCAG AA muted-text contrast** bumped across 115 files mode-aware: light `--text-muted #94A3B8→#52627A` (2.56:1→6.20:1), dark `--text-muted #64748B→#94A3B8` (3.75:1→6.96:1), dark `--text-secondary #94A3B8→#CBD5E1` (6.96:1→12.02:1).
- **`catalog.html` card colours** — scoped overrides for `.card-rating` (amber `#F59E0B`→`#B45309`/`#FBBF24`) and `.card-track` (sky `#0EA5E9`→`#0369A1`/`#38BDF8`), both now pass WCAG AA.
- **Theme system unified** on `im-theme` localStorage key — `js/cookie-ui.js`, `js/account.js`, `js/game-shell.js` all read canonical first then fall back to legacy keys (`theme`, `impactmojo-theme`, `imx_theme`) for seamless migration; all writes mirrored to legacy keys. Also set `data-theme` on `<html>`.
- **Brand fonts** — `BookSummaries/ultralearning-companion.html` (was Source Serif 4) and `BookSummaries/deep-work-companion.html` (was Merriweather) migrated to Inter / Amaranth / JetBrains Mono.
- **Content counts** aligned to ground truth across 26 files (11 flagship, 38 foundational, 11 Labs, 16 Games): `README.md`, `CLAUDE.md`, catalog, index, premium, upgrade, content-marketing-kit, org-dashboard, verify-certificate, updates, PressKit, blog post, and 13 `docs/*.md` files.
- **39 pictographic emoji → Sargam line icons** across 10 content pages. Typographic symbols (✓ ✔ ✦ ✧ ⚠) left as decorative characters.
- **10 unbuilt course cards** in `catalog.html` + `catalog_data.json` marked `comingSoon: true`, rendered as disabled cards with dashed border and amber "Coming Soon" pill badge: Survey Design 101, Gender Mainstreaming 101, Mixed Methods 101, Impact Evaluation 101, Maternal Health 101, Child Development 101, Feminist Research 101, Economics 101, VaniScribe (×2).

### Fixed
- **Handout 404s** — `getHandoutURL` in `handouts.html` now serves from same-origin `/Handouts/` with URL-encoded path segments (was pointing at a stale `varnasr.github.io/ImpactMojo/` mirror).
- **Duplicate `im-topbar` covering main site nav** on 28 pages — the overlay was hiding the legacy `<header class="header">` main navigation (including all dropdowns). Removed from pages where the legacy header is the real main nav; kept on handouts, blog posts, lexicons, games, and slide decks where it's the only topbar.
- **121 of 131 stale `101.impactmojo.in` links** rewritten to self-hosted equivalents via a Python migration with filesystem existence checks.

### Removed
- **PhD-level rigor marketing language** — reverted to actual tagline.

## [10.13.0] - 2026-04-05

### Added
- **Native 101 slide decks** — Replaced Gamma.app iframe wrappers with self-hosted HTML slide decks for 3 foundational courses: Development Economics 101, MEL 101, Climate Essentials 101
- **Shared deck template** — Reusable CSS (`101-courses/native/shared/deck.css`) and JS engine (`deck.js`) for all native 101 decks: light/dark/system theme, keyboard/touch/swipe nav, fullscreen, Chart.js integration, viewport scaling
- **17 Chart.js visualisations** in Dev Econ 101 (poverty trends, Lorenz curve, convergence trajectories, structural transformation, India GDP growth, rural credit, HCI comparison, UPI growth, global trade, FDI, RCT publications, caste income, urbanisation, SDG progress, jobless growth)

### Changed
- **101 deck CSS** — Proportionally larger fonts, padding, and gaps across all slide components to fill 1280×720 viewport: titles 32px/26px, body 16px, bullets 16px, stat numbers 36px, quotes 20px, charts 230px height
- **Inline style overrides** — Bumped 200+ hardcoded inline font sizes (11→13px, 12→14px, 13→15px) that CSS classes couldn't override
- **Dev Econ CTA** — "Explore the Full Course" → "Explore the Flagship Course"

### Fixed
- **Slide navigation** — Slides 51–100 were outside `slide-viewport` div in all Claude Chat-generated decks, making them unreachable by nav JS
- **JS syntax error** — Literal newlines inside Chart.js label strings broke entire script block
- **`chartsInit` declaration order** — Variable referenced before declaration in Dev Econ deck

## [10.12.0] - 2026-03-31

### Added
- **Self-hosted Docsify documentation** — Replaced GitBook with branded Docsify at `/docs/`, featuring dark/light/system theme, full-text search, code copy, prev/next pagination, Google Translate (14 South Asian languages), ImpactMojo branding (Inter + Amaranth + JetBrains Mono fonts, brand colors)
- **GitHub org profile README** — `.github/profile/README.md` visible at github.com/ImpactMojo

### Changed
- **Repository moved to ImpactMojo org** — All 200+ GitHub URLs updated from `Varnasr/ImpactMojo` to `ImpactMojo/ImpactMojo` across HTML, docs, config, and data files
- **MCP package scope** — `@varnasr/impactmojo-mcp-server` → `@impactmojo/impactmojo-mcp-server`
- **Netlify repo connection** — Updated from `Varnasr/ImpactMojo` to `ImpactMojo/ImpactMojo`
- **GitHub org settings** — Avatar, description, URL, email, location, and 16 repo topics configured
- **Sister repo links** — README and blog references to ImpactLex, PolicyDhara, dev-case-studies, etc. updated to org
- **`_redirects`** — Removed GitBook proxy, added Docsify SPA fallback; updated `varnasr.github.io` → `impactmojo.github.io`

### Removed
- **GitBook dependency** — No longer proxying to `impactmojo.gitbook.io`; all docs self-hosted

## [10.11.0] - 2026-03-28

### Added
- **Blog: Introducing the ImpactMojo MCP Server** — New blog post at `/blog/impactmojo-mcp-server.html` with 2 napkin.ai-generated illustrations, added card to `blog.html`
- **Napkin.ai blog illustrations** — Generated real infographics for the open source blog post (`github-open-dev-ecosystem`) replacing placeholder images, using the Napkin.ai API
- **CMK: 5 new LinkedIn posts** (LI-11 through LI-15) — Climate & Sustainability, Gender & Inclusion, AI in Development, Book Companions, MCP Server Launch. Total assets: 25 → 30
- **Housekeeping: CMK brochure update step** — Added Content Marketing Kit and brochure PDF to the counts/references checklist in `housekeeping/SKILL.md`

### Changed
- **CMK: Broadened scope beyond economics** — Renamed "Economics Games" to "Interactive Learning Games" across IG-04, LI-07, CR-03; updated headlines and hashtags
- **CMK: Corrected content counts** — 48 → 9 courses, 16 → 16 games, 247 → 270 dataverse throughout all captions and visuals
- **CMK: Redesigned brochure thumbnails** — Replaced plain colored boxes with content-preview thumbnails showing actual page content
- **CMK: Updated year** — "Content Kit 2025" → "Content Kit 2026"

## [10.10.0] - 2026-03-27

### Added
- **ImpactMojo MCP Server** — New `/mcp-server/` directory with a standalone TypeScript MCP server exposing the full knowledge base via Model Context Protocol. 11 tools (search_content, lookup_bct, search_bcts, list_bct_categories, browse_dataverse, search_dataverse, list_challenges, get_challenge, list_courses, get_game_info, query_climate_data) and 3 resources (overview, catalog, tracks). Compatible with Claude Desktop, Claude Code, Cursor, and any MCP client.
- **Dataverse entry** — Added `impactmojo-mcp` to Education & Learning category (269→270 items)
- **Search index entry** — Added MCP server to `data/search-index.json`
- **Published to GitHub Packages** — `@varnasr/impactmojo-mcp-server@1.0.0` with auto-publish GitHub Action on `mcp-server/v*` tags

## [10.8.1] - 2026-03-20

### Added
- **BookSummaries landing page** — `/BookSummaries/index.html` so navigation goes to a browsable landing page instead of directly to the Hanna book

### Fixed
- **RQ Premium redirect loop** — Race condition in `resource-launch.js` where clicking Research Question Builder before `premium.js` initializes redirected to login instead of showing the upgrade modal
- **Premium page design consistency** — Updated `premium.html` cards to use main site design standards (3px borders, 20px radius, offset box-shadows)
- **Premium tool fonts** — Updated `code-converter-pro.html` and `qual-insights-lab.html` to use ImpactMojo fonts (Amaranth/Inter/JetBrains Mono) and color palette instead of Segoe UI

## [10.8.0] - 2026-03-20

### Added
- **Cohort-based learning** — Supabase-backed cohorts with start/end dates, member enrollment, progress tracking, and deadline countdown (org dashboard Training tab)
- **Cohort discussion threads** — Real-time discussion within cohorts with post/delete support
- **Notification system** — `send-notification` Edge Function with streak reminders, cohort deadline alerts, and manual notification API
- **Notification preferences** — Per-user email opt-in/out (course updates, streak reminders, cohort deadlines, discussions, assignments, certificates) with digest frequency
- **In-app notification feed** — Recent notifications card on account page with unread badges and mark-as-read
- **Database migration** — `cohorts`, `cohort_members`, `cohort_discussions`, `notifications`, `notification_preferences` tables with full RLS policies, indexes, and triggers

### Changed
- **Auth session recovery** — Faster safety-net (1.5s + 4s fallback), increased SIGNED_OUT debounce to 1000ms, aggressive `_recoverSessionFromStorage()` for stored sessions, window.load recovery
- **API token documentation** — Added Gemini, DeepSeek, Grok, Sarvan.ai, Gamma to CLAUDE.md and .env.example

### Fixed
- **Gender equity game** — SVG viewBox too short, causing Madhubani art heads to be clipped
- **Info asymmetry game** — Pattachitra frame and end-story-art missing `width:100%`, appearing too small on mobile
- **Login persistence** — Session not surviving page navigation due to timing gaps in token refresh cycle

## [10.7.0] - 2026-03-20

### Added
- **BookSummaries** — New content type under Specials: interactive book summaries
- **The Handbook of Social Protection** (Hanna & Olken, MIT Press 2026) — first interactive book companion with chapter navigator, evidence explorer, data playground, programme compare, glossary, South Asia lens, and AI-powered Q&A
- BookSummaries entry added to Specials dropdown nav, catalog, sitemap, and search index
- **Claude Code global skills** — 6 repo-level skills (github-ops, netlify-ops, supabase-ops, gemini-ai, gamma-ops, housekeeping) for Claude Code on the web
- **SessionStart hook** — auto-loads API keys (Gemini, Gamma, DeepSeek, Grok, Sarvan.ai) from gitignored `.claude/.env.keys`
- **API token documentation** — CLAUDE.md updated with all 8 environment tokens

### Changed
- **`.env.example` updated** with Grok, Sarvan.ai, and Gamma API key placeholders
- **`.claude/settings.json`** now registers both SessionStart and Stop hooks
- **`.gitignore`** updated to protect `.claude/.env.keys` from commits

## [10.6.0] - 2026-03-19

### Added
- **Field Notes Pro** — 70 curated development economics field notes deployed as premium tool at `impactmojo-field-notes-pro.netlify.app`
- **Workshop Pro** — 7 interactive workshop templates (ToC, Logframe, Chart Selector, Stakeholder Mapping, Empathy Canvas, Policy Canvas, AI Canvas) deployed at `impactmojo-workshop-pro.netlify.app`
- **Field Notes JSON editor** link added to admin dashboard — edit `data/notes.json` directly from GitHub
- **Server-side auth-gate** on all new premium Netlify resource sites with `RESOURCE_TOKEN_SECRET` env vars configured

### Changed
- **Removed `mobile-index.html`** — `index.html` is now fully responsive, no separate mobile page needed
- **Updated all doc counts** — labs 10→19, games 12→16, Dataverse 215→247 across platform-overview, content-guide, architecture docs
- **Architecture docs updated** — full tier access control matrix with all 16 resource IDs
- **GitBook changelog updated** through v10.5.1
- **Sitemap timestamps refreshed** to 2026-03-19
- **ROADMAP.md updated** with Q1 2026 completions (workshop templates, field notes, auth-gate, mobile removal)
- **CLAUDE.md updated** — removed stale mobile-index.html checklist item
- **GitHub repo description updated** with current counts

## [10.5.1] - 2026-03-19

### Fixed
- **Admin tier reset bug** — admin accounts (varna.sr@gmail.com, varna@pinpointventures.in, vsoni.1986@gmail.com) were intermittently shown as free/explorer tier due to stale localStorage cache when profile fetch timed out
- **Profile fetch timeout** increased from 5s to 8s to reduce cache fallback on slow connections
- **Profile fetch retry** — failed fetches now auto-retry after 5 seconds so stale cached tier doesn't persist

### Added
- **Admin tier protection trigger** (`protect_admin_tier`) — database trigger prevents client-side downgrades of admin role, subscription tier, or subscription status
- **Idempotent profile creation** — `handle_new_user()` trigger now uses `ON CONFLICT DO NOTHING` to prevent overwriting existing profiles on re-authentication

## [10.5.0] - 2026-03-19

### Added
- **RQ Builder Pro** premium card — Practitioner tier, guided research question builder with PICO/SPIDER framing
- **TOC Workbench Pro** premium card — Practitioner tier, advanced Theory of Change building with assumption mapping and PDF/PNG export
- Both new tools added to premium modal, mobile-index.html, and search index

### Changed
- **Premium tool count updated from 7 → 9** across all pages and docs (catalog.html, content-catalog.md, faq.md, architecture.md, premium-tools-guide.md)
- **All 9 premium cards modernized with unique Sargam icons** — replaced generic si_Flare/imx-star badges with contextual icons (si_Search, si_Crosshair_detailed, si_Direction_alt, si_Library_books, si_Bar_chart, si_Database, si_Chat, si_Activity, si_Lightning)
- **Compact premium cards reformatted** to consistent expanded multi-line style matching the rest of the section
- **Tier access matrix updated** in architecture.md to include `toc-workbench-pro`

## [10.4.1] - 2026-03-19

### Changed
- **All 11 labs aligned to ImpactMojo standard design** — 3-button theme selector (System/Light/Dark), floating paper plane SVG decoration, sargamicon header badges
- **Theme persistence** — labs now share the `impactmojo-theme` localStorage key with system-preference awareness

## [10.4.0] - 2026-03-18

### Added
- **7 new self-hosted interactive labs** — Design Thinking, Impact Partnerships, Resource Sustainability, Policy Advocacy, MEL Design, MEL Plan Builder, Gender Analysis (all in `/courses/`)
- **Lab links updated** — all lab links in index.html now point to self-hosted files instead of `101.impactmojo.in`

### Changed
- **Lab count updated** from 12 to 19 across README and platform pages
- **Sitemap updated** with 7 new lab page entries
- **Search index updated** with entries for all new labs

## [10.3.0] - 2026-03-18

### Added
- **3 new games** beyond economics: Climate Action (Warli art), Gender Equity/Care Economy (Madhubani art), Public Health/Epidemic Response (Pattachitra art)
- **Indian folk art story illustrations** across all 12 existing games — intro screens, mid-game interludes, and adaptive ending art in 6 styles (Warli, Madhubani, Gond, Kalamkari, Pichwai, Pattachitra)
- **Sample Size Calculator** lab tool — 4 modes (proportion, mean, two-group, cluster sampling) with educational content
- **Budget Template Generator** lab tool — 7 budget categories, 5 smart templates, CSV/clipboard export
- **Admin dashboard panels** — User Management (search, filter, pagination) and Site Settings (feature flags, metadata, integrations, backups)
- **Accessibility improvements** — skip-nav links, ARIA landmarks, focus-visible styles, screen-reader labels on index, mobile-index, about, catalog
- **Claude Code project config** — `.claude/CLAUDE.md`, Stop hook for housekeeping, `/housekeeping` skill

### Changed
- **Renamed "Economics Games" → "Games"** across 14 files (now covers broader topics)
- **Fixed card text contrast** across 8 games — increased badge opacity, darkened text, added text-shadows (WCAG AA)
- **Fixed Dojos nav icon** — was duplicating Flagship Courses icon, now uses Activity icon
- **Fixed PolicyDhara workflow** — commit-msg prefix mismatch causing all scheduled runs to fail

### Removed
- **12 old Netlify game sites** deleted — all games now self-hosted in `/Games/`

## [10.2.0] - 2026-03-17

### Added
- **Self-hosted interactive games** in `/Games/` folder — replacing old Netlify-hosted apps at 101.impactmojo.in
- **MiroFish AI agent engine** (`supabase/functions/game-agent/`) — multi-provider LLM support with automatic fallback chain (DeepSeek → Groq → Gemini → Together → OpenAI)
- **30+ AI agent personas** (`data/game-agents.json`) — South Asian development practitioners with distinct personalities, backstories, and strategic behaviours
- **Game agents client library** (`js/game-agents.js`) — browser-side integration with Edge Function + local fallback engine
- **LLM provider secrets** configured: Groq, Google Gemini, DeepSeek API keys set as Supabase secrets

### Changed
- **Game links in index.html** — all 12 game links updated from `101.impactmojo.in/*` to `/Games/*.html`
- **game-agents.js Supabase URL** — corrected to actual project endpoint

### Games Built
- Public Good Game (free-rider problem, 4 AI agents)
- Prisoners' Dilemma (strategic interdependence, 4 AI agents)
- Commons Crisis (tragedy of the commons, 4 AI agents)
- Cooperation Paradox (Nash vs Pareto, 2 AI agents)
- Opportunity Cost (budget allocation, 2 AI agents)
- Risk & Reward Explorer (prospect theory, 3 AI agents)
- Bidding Wars (auction theory, 3 AI agents)
- Information Asymmetry (lemons problem, 3 AI agents)
- Network Effects (platform adoption, 3 AI agents)
- Externality Game (Pigouvian tax, 3 AI agents)
- The Real Middle (India income inequality)
- Econ Concepts Puzzle (12 brain-teasers)

## [10.1.0] - 2026-03-16

### Added
- **Git best-practice standards** propagated across all 29 ImpactMojo repos: `.gitattributes`, `.editorconfig`, `.githooks/pre-commit`, `.githooks/commit-msg`, `.gitmessage`, `.github/CODEOWNERS`, `.github/SECURITY.md`, `.github/dependabot.yml`, `.github/pull_request_template.md`, `.github/ISSUE_TEMPLATE/` (bug report, feature request, content issue)
- **Dependabot** configured per-repo (npm, pip, github-actions ecosystems auto-detected)
- **Pre-commit hook** blocks secrets (.env, .pem, .key), debugger statements, merge conflict markers; warns on console.log and files >500KB
- **Commit-msg hook** enforces prefix convention (Add/Fix/Update/Translate/Docs/Refactor/Test/CI/Chore)

### Fixed
- **Broken GitBook sidebar links**: Added `/impactmojo/*` → `/docs/*` Netlify redirects so sidebar navigation on impactmojo.in/docs works correctly

## [10.0.0] - 2026-03-16

### Added
- **What's New section** on mobile homepage — 8 feature cards highlighting new courses, DevData, Case Studies, DevDiscourses
- **Wall of Love section** on mobile homepage — horizontally scrollable testimonial cards in 6 languages (English, Hindi, Tamil, Bengali, Telugu, Marathi)
- **4 new course pages** linked: Politics of Aspiration, Media for Development, Constitution & Law, Social-Emotional Learning
- **Canvas line charts** on admin dashboard and transparency page — smooth Catmull-Rom spline rendering with gradient fills, replacing bar charts
- **Revenue model section** on transparency page — Explorer (free) vs Practitioner/Organisation (paid) tier cards

### Changed
- **Font standardization across 80 files**: Amaranth (body text) + Inter (headings) + JetBrains Mono (code). Removed Poppins, Fraunces, Merriweather, Source Serif 4, Source Sans 3, Cormorant Garamond. All fallback chains standardized
- **Google Fonts loading standardized**: Amaranth:400,700 + Inter:400-800 + JetBrains Mono:400,500. Consistent weight ranges across all pages
- **Transparency page redesigned**: renamed from "Transparency & Analytics", simplified data model (Legacy + GA4 = Totals), added methodology section
- **Admin dashboard redesigned**: removed one-time Supabase setup section, replaced bar charts with canvas line charts, games & tools charts in two-column layout
- **Org dashboard modal polished**: Create Learning Path modal — tighter padding, compact course rows, pill-shaped category buttons, proper light theme checkbox styling
- **Dashboard tabs** now accept profile parameter directly, fixing race condition where tabs showed wrong role/tier

### Fixed
- **Auth gate race condition**: `authStateChanged` event fired before profile fetch completed, causing premature access denial. Both `admin-gate.js` and `auth-gate.js` now await `fetchProfile()` before checking roles
- **Dashboard tabs wrong role**: `DashboardTabs.init()` relied on global `ImpactMojoAuth.profile` which wasn't set yet. Fixed by passing profile from auth callback
- **Mobile hamburger cutting off logo**: hidden desktop-only elements (theme selector, tour toggle, starburst badge, nav buttons) on mobile across `index.html`, `account.html`, `org-dashboard.html`, `mobile-index.html`
- **Mobile logo truncation**: removed `overflow:hidden` + `text-overflow:ellipsis` that was truncating "ImpactMojo" to "Impact..." on mobile-index.html

### Removed
- One-off fonts: Fraunces (dojos), Merriweather (about), Source Serif 4 (lexicons), Source Sans 3 (gandhi), Cormorant Garamond (gandhi)
- Supabase one-time setup section from admin dashboard
- Bar chart rendering code from admin and transparency pages

## [9.5.0] - 2026-03-15

### Added
- Unified dashboard tab navigation across account, org, admin, and analytics pages
- Team training packages for organizations (pre-built training paths, facilitator guides, assessment rubrics, cohort management)

## [9.1.0] - 2026-03-07

### Added
- **PolicyDhara** as 4th free resource (homepage, mobile, nav dropdown) linking to https://on-web.link/PolicyDhara
- Organization Dashboard content: welcome getting-started guide, "What's Included" feature grid, "Coming Soon for Teams" roadmap preview
- New roadmap items: Open Badges & Micro-credentials (#30), Live Case Challenges (#31)
- GitHub Issues for all roadmap features (#25-#31)

### Changed
- Org dashboard loads members and paths in parallel (`Promise.all`) for faster rendering
- Added `preconnect` hints for Supabase and CDN on org dashboard

### Fixed
- Org dashboard auth gate now waits for auth to fully resolve before checking tier access
- Google OAuth sign-in no longer triggers redundant profile fetch/sync on redirect

### Removed
- "Qualitative Data Lab" from roadmap (already live as Qual Insights Lab)
- "AI Learning Assistant" from roadmap (commoditized by general AI agents)

## [9.0.0] - 2026-03-06

### Added
- JWT-based premium access control for all resource sites
- Netlify Edge Functions (auth-gate) on 4 premium tool sites
- Supabase Edge Function for minting resource tokens
- `resource-launch.js` — client-side JWT launcher for premium tools
- `token-gate.js` — client-side token verification
- GitHub Wiki with 7 documentation pages
- GitHub Discussions with 12 seed conversations
- GitHub Actions CI for broken links and accessibility checks
- `.editorconfig` for consistent formatting
- `CHANGELOG.md` (this file)
- JSON-LD structured data for SEO

### Changed
- README rewritten with business models (Workshops, Coaching, Dojos, Premium tiers)
- README Netlify badge fixed (was using wrong site ID format)
- README version bumped to 9.0.0

### Fixed
- Broken Netlify deploy status badge in README
- `RESOURCE_SECRET_TOKEN` typo on premium resource site (renamed to `RESOURCE_TOKEN_SECRET`)

## [8.0.0] - 2026-02-28

### Added
- Performance optimization: extracted 160KB inline JS to deferred external files
- `js/bookmarks-compare.js` — bookmarks and course comparison logic
- `js/cookie-ui.js` — cookie consent banner
- `js/learning-tracks.js` — learning track navigation
- `js/mobile-ui.js` — mobile-specific UI logic
- Service worker upgraded with versioned cache and network-first strategy
- Font subsetting (Latin + Devanagari only)
- Community channels added to premium registration form

### Changed
- Inline JavaScript extracted from `index.html` (reduced from ~200KB to ~40KB)
- Service worker cache version bumped with proper invalidation

## [7.0.0] - 2026-02-15

### Added
- Premium membership tiers (Explorer, Practitioner, Professional, Organization)
- Supabase authentication (Email, Google OAuth, Magic Links)
- User profiles with progress tracking
- Bookmarks, personal notes, and reading lists
- Course comparison feature
- 38 foundational courses across 6 learning tracks
- 12 economics learning games
- 10 interactive labs
- ImpactLex PWA with 500+ terms
- Dev Case Studies library (200 cases, 117 countries)
- DevDiscourses (500+ curated papers and books)
- 400+ downloadable handouts
- Multilingual support (English, Hindi, Tamil, Bengali, Telugu, Marathi)
- Coaching and workshop booking pages
- Dojos skill session page
- Blog (Learning Loops) and podcast (Between the Logframes)

[10.7.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.6.0...v10.7.0
[10.6.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.5.1...v10.6.0
[10.5.1]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.5.0...v10.5.1
[10.5.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.4.1...v10.5.0
[10.4.1]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.4.0...v10.4.1
[10.4.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.3.0...v10.4.0
[10.3.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.2.0...v10.3.0
[10.2.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.1.0...v10.2.0
[10.1.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v10.0.0...v10.1.0
[10.0.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v9.5.0...v10.0.0
[9.5.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v9.1.0...v9.5.0
[9.1.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v9.0.0...v9.1.0
[9.0.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v8.0.0...v9.0.0
[8.0.0]: https://github.com/ImpactMojo/ImpactMojo/compare/v7.0.0...v8.0.0
[7.0.0]: https://github.com/ImpactMojo/ImpactMojo/releases/tag/v7.0.0
