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
- [x] **BookSummaries** — new content type under Specials with interactive book companions
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
- [x] **Game Library** — unified the 17 economics simulations + 117 puzzles into one filterable library (134 games) at `/game-library`, with a 301 from the old `/puzzle-library`
- [x] **Blog citation program** — ~22 methods/evidence posts upgraded to verified inline citations; corrected the debunked "learning pyramid" retention myth
- [x] **Daily Spotlight** — date-seeded "of the day" rotation engine (testimonials "featured voice" + homepage Today's Spotlight across courses/labs/deep dives/games/timelines)
- [x] **Certificate policy consistency** — reconciled to "free completion + Premium verified" site-wide
- [x] **Contact-email consolidation** — 11 scattered addresses folded into a single `hello@`
- [x] **Header-offset + anchor-scroll fixes** — heroes no longer trapped under the fixed header (10 pages); in-page `#section` links land correctly
- [x] **Count-consistency pass** — canonical counts (62 courses · 14 labs · 54 book companions · 20 Deep Dives · 134 Game Library) propagated across site, README, and press kit
- [x] **Migrate all 47 foundational decks to native HTML** — every `/101-courses/*` deck is now a self-hosted ~100-slide native HTML deck (Chart.js, light/dark, keyboard/touch nav). Zero Gamma iframes remain across the 101 series; verified live on impactmojo.in.
- [ ] **Vernacular Content** — Full courses in regional languages (#29). _Live: machine-translated + quality-audited per-page course content ships for **5 languages** — Hindi, Tamil, Bengali, Marathi and **Telugu** (30 page-dictionaries each) — plus a 409-string common UI dictionary per language, all behind a protected-terms glossary and the `check-i18n-quality` CI guard. Telugu (2026-06) was generated via a glossary-aware Gemini pass (`scripts/gemini-translate.py`) as a Sarvam fallback. The strategy is high-quality machine translation refined toward human quality (via the glossary + a community-correction override layer), not paid human localization._
- [x] **Analytics dashboard v2** — Learner analytics with completion funnels, time-on-task, and assessment scores (`admin/learner-analytics.html`)
- [x] **Mobile app (PWA)** — Enhanced PWA: offline support + background sync of learner progress (service worker), and **web push notifications** (VAPID, per-device opt-in on the account page; streak & cohort reminders delivered via the `send-push` Edge Function). Backend is live on Supabase (table, secrets, functions deployed + smoke-tested); the front-end opt-in ships on the next deploy to `main`.
- [x] **Games/climate-action-game.html device-mode** — designer-authored light earth-tone palette (warm sand surfaces + espresso-brown folk-art ink), replacing the cold filter-invert fallback. All games now support the 3-button system/light/dark toggle.

## Q3 2026 (Jul-Sep) — Shipped early

- [x] **Peer review system** — Learners review each other's submissions; Supabase-backed (`peer-review.html`, `peer_reviews` + `challenge_submissions` tables with RLS)
- [x] **Certificate marketplace** — Employer-facing verification portal (`verify.html`)
- [x] **API for partners** — REST API for organizations to integrate ImpactMojo content (`api-docs.html` + `netlify/functions/partner-api.mjs`)

## Q4 2026 (Oct-Dec) — Shipped early

- [x] **Community-contributed courses** — Verified practitioners can submit courses ("Teach with Us", `contribute.html`, Netlify Forms)
- [x] **Live workshops integration** — Webinar listings + registration with `.ics` calendar export (`events.html`, `data/events.json`). _Operational follow-up: replace placeholder `join_url`s with real Zoom/Meet links._
- [x] **Impact measurement dashboard** — Public community outcomes view + login-gated outcome logging (`impact-dashboard.html`, `impact_outcomes` table with RLS)

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Feature requests and roadmap suggestions are welcome via [GitHub Issues](https://github.com/ImpactMojo/ImpactMojo/issues) or [Discussions](https://github.com/ImpactMojo/ImpactMojo/discussions).
