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
- [x] Offline PWA support for flagship courses
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
- [x] **Count-consistency pass** — canonical counts (54 courses · 13 labs · 69 book companions · 16 Deep Dives · 134 Game Library) propagated across site, README, and press kit
- [ ] **Migrate remaining 35 foundational decks** — Convert all Gamma iframe wrappers to native HTML using Claude Chat + Claude Code workflow
- [ ] **Vernacular Content** — Full courses in Hindi and Tamil (#29)
- [ ] **Analytics dashboard v2** — Learner analytics with completion funnels, time-on-task, assessment scores
- [ ] **Mobile app (PWA)** — Enhanced PWA with push notifications and background sync
- [ ] **Games/climate-action-game.html device-mode** — single remaining dark-only page; needs designer-authored light tokens for earth-tone palette (`#F5F0EB`)

## Q3 2026 (Jul-Sep) — Planned

- [ ] **Peer review system** — Learners review each other's assignments and case analyses
- [ ] **Certificate marketplace** — Employer-facing verification portal
- [ ] **API for partners** — REST API for organizations to integrate ImpactMojo content

## Q4 2026 (Oct-Dec) — Exploratory

- [ ] **Community-contributed courses** — Allow verified practitioners to publish courses
- [ ] **Live workshops integration** — Calendar-based booking with Zoom/Meet integration
- [ ] **Impact measurement dashboard** — Track real-world outcomes from learners' projects

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Feature requests and roadmap suggestions are welcome via [GitHub Issues](https://github.com/ImpactMojo/ImpactMojo/issues) or [Discussions](https://github.com/ImpactMojo/ImpactMojo/discussions).
