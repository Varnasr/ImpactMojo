# ImpactMojo — Working Backlog (live)

Tracking the review-driven work. Shipped items pruned as they merge. Priority is top-to-bottom within each phase.

## Phase 0 — Standing requirement: COUNT CONSISTENCY
Whenever content is added/removed, keep ALL counts correct and synced site-wide — Games (17), Deep Dives (16), blog posts, courses (flagship/foundational), Labs, Book companions, Game Library formats — across `index.html`, `catalog.html`, `README.md`, `docs/`, `sitemap.xml`, nav, hero, cards, sidebar, search-index. Run a count audit after every content change.

## Phase 1 — Consistency & polish (active bugs first)
- [x] **Header-offset sweep** — 9 trapped pages fixed (catalog/faq/accessibility/live-projects/contact/coaching 70px; transparency/challenges/dataverse 64px). workshops/handouts left (already clear via 60px padding).
- [x] **Nav/header standardisation** — updates + dojos now use the standard ImpactMojo nav. VERIFIED (#509): the earlier transplant was incomplete — both had duplicate stacked navbars, 3 conflicting theme scripts, and NO nav CSS (header not actually fixed, mobile menu dead). Fixed: single header, one canonical theme block (sets data-theme attr + body.dark-mode), injected nav CSS, 70px mobile offset.
- [x] **Light/dark mode consistency (mechanism)** — audited all 48 top-level pages for theme-JS↔CSS mechanism mismatch (#509). Clean — the one genuinely broken page (dojos) fixed above. Key fragmentation (im-theme/theme/impactmojo-theme) is reconciled by `js/cookie-ui.js` (writes all keys + migrates legacy). Per-element COLOUR contrast left to CI axe-core/pa11y (blanket inline-color rescue unsafe: same hex is invisible-on-dark as plain text but correct on inline light badges).
- [x] **Pre-existing contrast fails (CI) — FIXED (#513)** — axe-core/pa11y were RED on every commit since #502. Root cause: WCAG AA color-contrast (Today's Spotlight, Learning Pathways titles via `var(--pw-color)`, catalog active nav link). Darkened to AA on white + dark-mode overrides. Verified: axe 5/5, pa11y 13/13. CI now GREEN.
- [ ] **Design consistency** — hero treatment, spacing, fonts, card styles across main pages (visual; needs preview / named pages).
- [x] **Orphan-row / grid tuning** — community page grids fixed (auto-fill + centered).

## Phase 2 — Blog quality (defensible-citation bar)
- [x] **Napkin.ai illustrations** — cash-transfers post done (key now works); writing-a-tor & knowing-what-you-want already had them.
- [x] Blog citation upgrades — Batch 1 (6): meal-demystified, theory-of-change-pitfalls, sample-size-matters, indicators-that-matter, mixed-methods-evaluation, quasi-experimental-designs.
- [x] Blog citation upgrades — Batch 2 (6): assumption-testing, adaptive-management-toc, building-mel-culture, participatory-mel, toc-vs-logframe, ethical-research-south-asia.
- [x] Blog citation upgrades — Batch 3 (6): history-of-mel, data-driven-decisions, data-quality-field, community-feedback-loops, south-asia-development-landscape, toc-for-complex-programmes.
- [x] Blog citation upgrades — Batch 4: open-education-matters, multilingual-learning, learning-by-doing, writing-a-tor (verified citations; learning-pyramid myth removed). Manifesto/story posts left as-is (citations not warranted).

## Phase 3 — Content expansion (ADD more + update)
- [x] **Timelines** — all 5 extended to 2026 + node-count fixes (#502/#503).
- [x] **Dataverse** — +14 verified open-data sources → 296 (#501).
- [x] **Game Library** — 17 simulations merged in as a filterable type (134 games). (i18n + other-page footers still TODO.)
- [x] **Updates / Roadmap page** — standard nav (#504) + What's New refreshed with the recent major work (Game Library, 16 Deep Dives, Impact Bold, blog citations, Daily Spotlight, Dataverse/Timelines).
- [x] **Press kit** — refreshed to canonical counts (#498).

## Phase 4 — Repo program
- [x] README.md refreshed to canonical counts (#498).
- [x] GitHub repo description + 20 topics refreshed (via API).
- [~] All-language docs (`i18n/` bn·hi·mr·ta + ~40 `docs/` guides). **UI layer done (#509):** filled the 41 missing curated `data-i18n` keys (Press Kit + nav) × 4 langs → 0 missing site-wide; flagged `_meta.pending_native_review`. **Deferred:** translating the 57 `docs/` guides (needs native reviewers + translation budget; not a headless task).
- [x] ROADMAP.md refreshed (Q2 2026) (#499). Gantt = optional.
- [x] CI workflows audited — current; checkout@v4→v6 (#499).
- [ ] GitHub Issues + Discussions seeding.

## Done this session (PRs #464–#479)
Premium redesign · 32-page bold restyle + shared impact-bold.css · 10 Deep Dives (→16) · certificate consistency · GitBook→Documentation · testimonials Daily Spotlight · cash-transfers blog post · blog citation Batch 1 · founder photo (cache-fixed) · anchor-scroll fix · Game Library rename · gender box · dark-mode text · podcast "Soon" badge · paper-plane · INR copy · FAQ rebalance · modal mobile overflow · about-header offset.
