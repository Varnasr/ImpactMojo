# ImpactMojo — Working Backlog (live)

Tracking the review-driven work. Shipped items pruned as they merge. Priority is top-to-bottom within each phase.

## Phase 0 — Standing requirement: COUNT CONSISTENCY
Whenever content is added/removed, keep ALL counts correct and synced site-wide — Games (17), Deep Dives (16), blog posts, courses (flagship/foundational), Labs, Book companions, Game Library formats — across `index.html`, `catalog.html`, `README.md`, `docs/`, `sitemap.xml`, nav, hero, cards, sidebar, search-index. Run a count audit after every content change.

## Phase 1 — Consistency & polish (active bugs first)
- [x] **Header-offset sweep** — 9 trapped pages fixed (catalog/faq/accessibility/live-projects/contact/coaching 70px; transparency/challenges/dataverse 64px). workshops/handouts left (already clear via 60px padding).
- [x] **Nav/header standardisation** — updates (#504) and dojos now use the standard ImpactMojo nav (transplanted; reader pages keep the clean topbar by design). VERIFY on preview.
- [ ] **Light/dark mode consistency** — audit every main page for dark-mode contrast (blue-on-dark, invisible text, tinted bands).
- [ ] **Design consistency** — hero treatment, spacing, fonts, card styles across main pages.
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
- [ ] All-language docs (`i18n/` bn·hi·mr·ta + ~40 `docs/` guides).
- [x] ROADMAP.md refreshed (Q2 2026) (#499). Gantt = optional.
- [x] CI workflows audited — current; checkout@v4→v6 (#499).
- [ ] GitHub Issues + Discussions seeding.

## Done this session (PRs #464–#479)
Premium redesign · 32-page bold restyle + shared impact-bold.css · 10 Deep Dives (→16) · certificate consistency · GitBook→Documentation · testimonials Daily Spotlight · cash-transfers blog post · blog citation Batch 1 · founder photo (cache-fixed) · anchor-scroll fix · Game Library rename · gender box · dark-mode text · podcast "Soon" badge · paper-plane · INR copy · FAQ rebalance · modal mobile overflow · about-header offset.
