# Roadmap

ImpactMojo development priorities for 2026. Items are roughly ordered by priority within each quarter.

## Q1 2026 (Jan-Mar) — Completed

- [x] JWT-based premium access control for resource sites
- [x] Supabase authentication (Email, Google OAuth, Magic Links)
- [x] W3C Open Badges 3.0 verifiable credentials
- [x] Learning Pathways with milestone progression
- [x] Interactive assessments for flagship courses
- [x] Team training packages for organizations
- [x] Full-text search (Ctrl+K) via Fuse.js
- [x] Offline PWA support for flagship courses — _rebuilt 2026-06-19: a network-first (HTML) + stale-while-revalidate (assets) service worker that purges non-current caches on activate, so offline works without the stale-file bug that retired the previous SW. Backs the course-download + offline-status UI in `js/offline.js`._
- [x] Unified dashboard architecture (account, org, admin, analytics)
- [x] Canvas line charts on admin & transparency dashboards
- [x] Font standardization (Amaranth + Inter + JetBrains Mono)
- [x] Mobile nav fixes across all pages
- [x] 4 new flagship courses (Politics of Aspiration, Media for Development, Constitution & Law, SEL)
- [x] Git best-practice standards propagated across all 29 repos (hooks, templates, dependabot, CODEOWNERS, SECURITY)
- [x] GitBook docs sidebar link fix (`/impactmojo/*` → `/docs/*` redirects)
- [x] **Self-hosted interactive games** with MiroFish AI agents — replacing Netlify-hosted apps
- [x] **MiroFish AI agent engine** — Supabase Edge Function with multi-provider LLM fallback (Groq/Gemini/DeepSeek)
- [x] **30+ AI agent personas** — South Asian development practitioners across 10 games
- [x] **3 new games** beyond economics — Climate Action, Gender Equity, Public Health (Digital Ethics in progress)
- [x] **Indian folk art story illustrations** — across all games in 6 styles
- [x] **Card text contrast fixes** — WCAG AA compliance across 8 games
- [x] **Sample Size Calculator** — survey planning lab with 4 calculation modes
- [x] **Budget Template Generator** — project budget lab with smart templates and CSV export
- [x] **Admin dashboard** — User Management and Site Settings panels
- [x] **Accessibility improvements** — skip-nav, ARIA landmarks, focus styles on key pages
- [x] **Old Netlify game sites deleted** — freed 12 slots
- [x] **PolicyDhara workflow fix** — commit-msg prefix causing build failures
- [x] **Gender Studies flagship course** — in progress
- [x] **7 interactive workshop templates** — ToC, Logframe, Chart Selector, Stakeholder, Empathy Canvas, Policy Canvas, AI Canvas (premium)
- [x] **Field Notes Pro** — 70 curated development economics field notes (premium)
- [x] **Server-side auth-gate** on all premium Netlify resource sites
- [x] **Removed mobile-index.html** — index.html is now fully responsive
- [x] **Admin tier protection** — database trigger prevents client-side downgrades
- [x] **BookSummaries** — new content type under Specials with interactive reading companions
- [x] **Handbook of Social Protection** — first interactive book summary (Hanna & Olken, MIT Press 2026)
- [x] **Gamma API integration** — 23/38 course decks synced as Gamma presentations
- [x] **Claude Code skills & hooks** — 6 global skills, SessionStart hook for API key bootstrap, multi-provider AI token support
- [x] **Cohort-based learning** — Supabase-backed cohorts with discussion threads, deadlines, and progress tracking (#144)
- [x] **Notification system** — Edge Function for email notifications (streak reminders, cohort deadlines), in-app notification feed, per-user preferences (#145)
- [x] **Git standards verified** — all 29 repos confirmed compliant, dependabot PRs arriving (#162)
- [x] **Auth persistence fixes** — faster session recovery, aggressive SIGNED_OUT debounce, window.load recovery
- [x] **Game visual fixes** — gender equity SVG clipping, info asymmetry image sizing
- [x] **API token documentation** — Gemini, DeepSeek, Grok, Sarvan.ai, Gamma added to CLAUDE.md and .env.example
- [x] **BookSummaries landing page** — browsable index at `/BookSummaries/` replacing direct-to-book navigation
- [x] **Development Economics companion** — Debraj Ray (Princeton 1998), 18 chapters with models, concepts, exercises
- [x] **Design Thinking companion** — Andrew Pressman (Routledge 2019), 10 chapters on creative problem-solving
- [x] **Premium design consistency** — premium.html and premium-tools pages aligned with main site design standards (fonts, borders, shadows)
- [x] **RQ Premium redirect fix** — race condition in resource-launch.js preventing upgrade modal from showing

## Q2 2026 (Apr-Jun) — In Progress

### Content and integration gaps (raised 2026-08-21 by an instructor-kit request)

An instructor at a school of social work asked for a kit covering Sustainability, ESG, CSR and M&E. Mapping the M&E half was straightforward. The other half does not exist here, and mapping it exposed the integration gaps below. One request is not a mandate — these are recorded because they were found, and should be weighed against demand rather than built on the strength of a single enquiry.

- [x] **CSR & ESG 101 course** — **Shipped 2026-08-21** as `/101-courses/csr-esg.html` (88 slides). Section 135, Schedule VII, the two per cent, unspent-money rules, CSR-1, impact assessment, then BRSR and the global frameworks. Previously: no dedicated ESG material existed; CSR appeared only in passing inside a handful of 101 decks. ESG reporting, CSR obligations under the Companies Act, and sustainability frameworks are core teaching for institutional and corporate-adjacent audiences. A 101 deck is the cheapest format to close this.
- [ ] **Sustainability / ESG flagship** — The heavier version of the above: a full ~13-module flagship with South Asian cases, a lexicon and an assessment. Worth building only if ESG proves a durable teaching market rather than one syllabus.
- [~] **LMS-friendly exports** — **Gradebook CSV shipped 2026-08-21**; per-module deep links partly there. `js/studio-submit.js` wraps any Studio's existing export in an envelope carrying the student's name, the Studio, a timestamp and a digest — the missing piece, since Studio exports carried no identity at all (`logframe-builder` exported bare `JSON.stringify(state)`), so an instructor with thirty files could not tell whose was whose. `/gradebook.html` reads a folder of them and emits one CSV, entirely in the browser: student work is never uploaded. **Wired into one Studio so far** (LogFrame Builder, as the reference); the other 32 need the same two-line adoption. **Deep links**: every deck slide already has a stable `id` and `#s42` navigates, so an instructor can link a specific slide today — what is still missing is a published section→slide map and an LMS export that emits one SCO per section rather than one for the whole course.
- [x] **SCORM / xAPI package** — **Shipped 2026-08-21** at `/lms-export.html`. Builds SCORM 1.2, SCORM 2004, IMS Common Cartridge 1.3 and a single self-contained HTML file, for any of the 71 courses and 47 practice workbooks, in the instructor's browser. No zip is committed: a package per course would be 118 artifacts rebuilt on every content edit and stale the moment one drifted, so the export fetches the live page instead and is always current. The payload drops our analytics, sign-in, Supabase and translation code before packaging — none of it belongs in someone else's LMS — and inlines what remains, so an imported course runs with no network. SCORM reports completion when the learner reaches the final slide, hooked to the deck's own navigation. xAPI is **not** included: it needs an LRS endpoint to post to, which we do not run.

- [x] **Native 101 slide decks** — Replaced Gamma iframes with self-hosted HTML decks for Dev Econ, MEL, and Climate (100 slides each, Chart.js, light/dark theme, keyboard/touch nav)
- [x] **Handout 404s + same-origin serving** — `getHandoutURL` now serves from `/Handouts/` with URL-encoded path segments (previously pointed at a stale mirror)
- [x] **Brand theme unification** — single `im-theme` localStorage key across main site, handouts, games, account page; seamless legacy-key migration
- [x] **WCAG 2.1 AA contrast baseline** — muted-text token bumps across 115 files, `link-in-text-block` underline rule on 74 content pages, `id="home"` anchor fix, card-colour overrides
- [x] **Device-mode default theme resolution** on 70 pages — follows OS `prefers-color-scheme` on first paint, explicit class overrides keep the 3-button toggle dominant
- [x] **Duplicate header cleanup** — removed `im-topbar` overlay from 28 pages where it was hiding the legacy main navigation
- [x] **Emoji → Sargam line icons** — 39 pictographic emoji replaced with `si_*` icons across 10 content pages
- [x] **"Coming Soon" course cards** — 10 unbuilt placeholder cards marked with disabled state instead of dead mirror links
- [x] **Brand identity audit complete** — every content page has correct fonts, paper plane, theme toggle, home link, Premium link, footer landmark, CC BY-NC-ND attribution, language dropdown
- [x] **FieldCases + DevDiscourses theme toggle** (sister sites on `varnasr.github.io`) — 3-button system/light/dark selector shipped on both
- [x] **"Impact Bold" visual refresh** — 32-page bold restyle on a shared `impact-bold.css`, plus a full premium-page redesign
- [x] **Deep Dives library (→16)** — 10 new curated, fully web-cited reading lists (cash transfers, India's FLFP, politics of targeting, the RCT debate, climate adaptation finance, measuring empowerment, informality, the learning crisis, health systems & UHC, decolonising development knowledge)
- [x] **Game Library** — unified the 18 simulations + 117 puzzles into one filterable library (135 games) at `/game-library`, with a 301 from the old `/puzzle-library`
- [x] **Blog citation program** — ~22 methods/evidence posts upgraded to verified inline citations; corrected the debunked "learning pyramid" retention myth
- [x] **Daily Spotlight** — date-seeded "of the day" rotation engine (testimonials "featured voice" + homepage Today's Spotlight across courses/labs/deep dives/games/timelines)
- [x] **Certificate policy consistency** — reconciled to "free completion + Premium verified" site-wide
- [x] **Contact-email consolidation** — 11 scattered addresses folded into a single `hello@`
- [x] **Header-offset + anchor-scroll fixes** — heroes no longer trapped under the fixed header (10 pages); in-page `#section` links land correctly
- [x] **Count-consistency pass** — canonical counts (62 courses · 30 labs · 55 reading companions · 20 Deep Dives · 135 Game Library) propagated across site, README, and press kit
- [x] **Migrate all 47 foundational decks to native HTML** — every `/101-courses/*` deck is now a self-hosted ~100-slide native HTML deck (Chart.js, light/dark, keyboard/touch nav). Zero Gamma iframes remain across the 101 series; verified live on impactmojo.in.
- [~] **Vernacular Content** — *Partially shipped; the remaining gap is the teaching content itself, not the site.* **Live:** all **19 flagship course pages and their 13 lexicons**, plus the homepage — **33 page-dictionaries per language** — in **5 languages** (Hindi, Tamil, Bengali, Marathi, Telugu), behind a **439-string** common UI dictionary each, a protected-terms glossary and the `check-i18n-quality` CI guard. Telugu (2026-06) came from a glossary-aware Gemini pass (`scripts/gemini-translate.py`) as a Sarvam fallback. The strategy is high-quality machine translation refined toward human quality. **Not translated:** the **52 foundational 101 decks** (0 of 52), the Studios, Games, Deep Dives and Book Companions — 33 of ~178 site pages in total. So a learner can browse a flagship course in Hindi and then hit English the moment they open a deck. Closing it means translating slide decks, which is a different and much larger job than page dictionaries: ~100 slides each, and the glossary guard has to hold across all of them. *(Corrected 2026-08-21: the previous entry read as wholly unstarted, and undercounted at "30 page-dictionaries" and a "409-string" UI dictionary. Measured: 33 and 439.)*
- [x] **Analytics dashboard v2** — Learner analytics with completion funnels, time-on-task, and assessment scores (`admin/learner-analytics.html`)
- [x] **Mobile app (PWA)** — Enhanced PWA: offline support + background sync of learner progress (service worker), and **web push notifications** (VAPID, per-device opt-in on the account page; streak & cohort reminders delivered via the `send-push` Edge Function). Backend is live on Supabase (table, secrets, functions deployed + smoke-tested); the front-end opt-in ships on the next deploy to `main`.
- [x] **Games/climate-action-game.html device-mode** — designer-authored light earth-tone palette (warm sand surfaces + espresso-brown folk-art ink), replacing the cold filter-invert fallback. All games now support the 3-button system/light/dark toggle.

## Q3 2026 (Jul-Sep) — Shipped early

- [x] **12 new Interactive Labs** — Budget & Fiscal Analysis, Climate Risk & Adaptation, Conflict-Sensitive Programming, Data Feminism & Intersectional Analysis, Digital Public Infrastructure, Ethics & Research Integrity, Grant Writing & Proposal, Participatory Methods, Policy Brief Writing, Stakeholder Mapping & Power Analysis, Survey Design, and Systems Thinking & Complexity — drafted labs re-skinned to the standard lab template (cyan/indigo, 3-mode theme, floating SVG, footer), fact-checked, and wired across `/labs/`, catalog, search index and sitemap. Labs collection **15 → 28** (incl. the R/Python course) with 3 new tracks: Research & Methods, Governance & Digital, Climate & Environment. (#643–#648)
- [x] **R & Python for Development** — interactive course teaching R and Python from zero with real code running in the browser via WebR + Pyodide (no install). _All 7 modules live (real NFHS/ASER/PLFS/Budget data, wrangling, visualisation, impact evaluation)._

- [x] **Peer review system** — Learners review each other's submissions; Supabase-backed (`peer-review.html`, `peer_reviews` + `challenge_submissions` tables with RLS)
- [x] **Certificate marketplace** — Employer-facing verification portal (`verify.html`)
- [x] **API for partners** — REST API for organizations to integrate ImpactMojo content (`api-docs.html` + `netlify/functions/partner-api.mjs`)

### Shipped so far (Q3)

- **Jul 2** — 12 new Interactive Labs (15 → 28, three new tracks) + the full **R & Python for Development** live-code course (7 modules, WebR + Pyodide)
- **Jul 5 (v10.80.0)** — *Counterfactual: The Evaluation Game* (game #18; Game Library 135), six new Live Case Challenges (9 → 15, every flagship covered), the *Gender & Work in India* timeline (6th timeline; 113 nodes / 44 eras), and search-index completeness (26 blog posts + 4 reading companions added to site search)
- **Jul 6 (v10.82.0–82.2)** — **Build Circles** (4-week AI build cohorts) and the **AI for M&E Certificate Track** (₹2,499) + the free **AI Agents for Evaluators** module; and **interactive assessments on every flagship** — all 16 flagship courses now end with a six-question auto-graded "Assess Yourself" self-check (90 questions total), surfaced across catalog, homepage, nav, footer, updates, README and docs
- **Jul 9–10 (v10.86–10.87)** — **Flagship parity across all 17**: a theme-aware concept diagram and a verified open-access key reading in every one of the 224 modules; standard thin top-bar + footer and rich gradient heroes site-wide; a content-freshness pass (incl. a GenAI refresh of *AI for Impact*). **Printable Course Notes** — one print-ready PDF per flagship (₹350), delivered by UPI. **Four new 101 courses** — GenAI for Practitioners, Data Protection & the DPDP Act, Safeguarding & PSEA, Disability Inclusion (foundational library **47 → 51**, total courses **64 → 68**). **Full anti-fork cleanup** — all 17 flagships now served exclusively from the database.

## Q4 2026 (Oct-Dec) — Shipped early

- [x] **Community-contributed courses** — Verified practitioners can submit courses ("Teach with Us", `contribute.html`, Netlify Forms)
- [x] **Live workshops integration** — Webinar listings + registration with `.ics` calendar export (`events.html`, `data/events.json`). _Operational follow-up: replace placeholder `join_url`s with real Zoom/Meet links._
- [x] **Impact measurement dashboard** — Public community outcomes view + login-gated outcome logging (`impact-dashboard.html`, `impact_outcomes` table with RLS)

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Feature requests and roadmap suggestions are welcome via [GitHub Issues](https://github.com/ImpactMojo/ImpactMojo/issues) or [Discussions](https://github.com/ImpactMojo/ImpactMojo/discussions).
