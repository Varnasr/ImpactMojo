# ImpactMojo — Working Backlog (live)

Tracking the review-driven work. Shipped items pruned as they merge. Priority is top-to-bottom within each phase.

## Phase 0 — Standing requirement: COUNT CONSISTENCY
Whenever content is added/removed, keep ALL counts correct and synced site-wide — Games (17), Deep Dives (16), blog posts, courses (flagship/foundational), Labs, Book companions, Game Library formats — across `index.html`, `catalog.html`, `README.md`, `docs/`, `sitemap.xml`, nav, hero, cards, sidebar, search-index. Run a count audit after every content change.

## Phase 1 — Consistency & polish (active bugs first)
- [ ] **Header-offset sweep** — pages with a fixed header but NO body offset trap their hero/nav under the header (the about.html bug, generalised). Affected (verify each renders, avoid double-gap): catalog, faq, contact, workshops, coaching, handouts, transparency, accessibility, live-projects, challenges, dataverse.
- [ ] **Nav/header standardisation** — `updates` and `dojos` use the minimal `im-topbar` instead of the standard `.header`+nav; bring them onto the standard nav. (Reader pages — DeepDives, BookSummaries, Game Library — keep the clean topbar by design.)
- [ ] **Light/dark mode consistency** — audit every main page for dark-mode contrast (blue-on-dark, invisible text, tinted bands).
- [ ] **Design consistency** — hero treatment, spacing, fonts, card styles across main pages.
- [x] **Orphan-row / grid tuning** — community page grids fixed (auto-fill + centered).

## Phase 2 — Blog quality (defensible-citation bar)
- [x] **Napkin.ai illustrations** — cash-transfers post done (key now works); writing-a-tor & knowing-what-you-want already had them.
- [x] Blog citation upgrades — Batch 1 (6): meal-demystified, theory-of-change-pitfalls, sample-size-matters, indicators-that-matter, mixed-methods-evaluation, quasi-experimental-designs.
- [x] Blog citation upgrades — Batch 2 (6): assumption-testing, adaptive-management-toc, building-mel-culture, participatory-mel, toc-vs-logframe, ethical-research-south-asia.
- [x] Blog citation upgrades — Batch 3 (6): history-of-mel, data-driven-decisions, data-quality-field, community-feedback-loops, south-asia-development-landscape, toc-for-complex-programmes.
- [ ] Blog citation upgrades — Batch 4 (remaining): open-education-matters, multilingual-learning, learning-by-doing, writing-a-tor-for-research, + judgement-call on the manifesto/story posts (why-impactmojo-exists, knowing-what-you-want, from-learner-to-leader, tools-we-use, whats-coming-in-2026 — cite where claims warrant, don't force).

## Phase 3 — Content expansion (ADD more + update)
- [ ] **Timelines** — expand & refresh: add new timeline pages and update the 5 existing (climate-policy, development-thinking, indian-policy, indian-rights, mel-methods).
- [ ] **Dataverse** — add more data sources and refresh the catalogue (`data/dataverse.json`).
- [x] **Game Library** — 17 simulations merged in as a filterable type (134 games). (i18n + other-page footers still TODO.)
- [ ] **Updates / Roadmap page** — rewrite stale content (then it also gets the standard nav from Phase 1).
- [ ] **Press kit** — refresh stats, year, and copy.

## Phase 4 — Repo program
- [ ] README.md refresh (stale counts/structure).
- [ ] GitHub repo description + topics.
- [ ] All-language docs (`i18n/` bn·hi·mr·ta + ~40 `docs/` guides).
- [ ] ROADMAP.md + project plan / Gantt.
- [ ] CI workflows audit (ci.yml, accessibility.yml, static.yml, publish-mcp-server.yml) + dependabot/templates.
- [ ] GitHub Issues + Discussions seeding.

## Done this session (PRs #464–#479)
Premium redesign · 32-page bold restyle + shared impact-bold.css · 10 Deep Dives (→16) · certificate consistency · GitBook→Documentation · testimonials Daily Spotlight · cash-transfers blog post · blog citation Batch 1 · founder photo (cache-fixed) · anchor-scroll fix · Game Library rename · gender box · dark-mode text · podcast "Soon" badge · paper-plane · INR copy · FAQ rebalance · modal mobile overflow · about-header offset.
