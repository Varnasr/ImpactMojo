# Roadmap

What's coming next for ImpactMojo. This is a living document — we'd love your input. Suggest ideas in [GitHub Discussions](https://github.com/ImpactMojo/ImpactMojo/discussions/categories/ideas).

## Currently In Progress

### Vernacular Content
Professional translations of courses in Hindi, Tamil, Bengali, and Marathi. ([#29](https://github.com/ImpactMojo/ImpactMojo/issues/29))

**What this means for you:** If you work with teams who are more comfortable in regional languages, full course translations (not just Google Translate) will be available soon. We're starting with the most-used flagship courses.

### BookSummaries Expansion
Growing from 28 to 40+ interactive book companions across development economics, statistics, leadership, and productivity. ([#272](https://github.com/ImpactMojo/ImpactMojo/issues/272))

### Native 101 Deck Migration
Migrating remaining 37 foundational course decks from Gamma iframes to self-hosted HTML with 100 slides each, interactive charts, and keyboard/touch navigation.

## Planned — Q2 2026 (April–June)

### For Learners & Educators
- **Analytics dashboard v2** — See completion funnels, time-on-task, and assessment scores for yourself or your team
- **Enhanced offline support** — Push notifications and background sync so the app stays updated even on intermittent connections
- **Video walkthroughs** for interactive labs — short guided videos showing how to use each lab
- **Practitioner interview series** — Real practitioners sharing how they apply concepts in the field

### Content
- Additional foundational courses across all 6 tracks
- Regional case study packs focusing on state-level India data
- **Survey Instrument Library** — Browse and adapt validated survey instruments

### Community
- **Peer review system** — Get feedback on your lab outputs from other practitioners
- **Alumni network directory** — Connect with other ImpactMojo learners

## Planned — Q3–Q4 2026

### For Organizations
- **Certificate marketplace** — An employer-facing portal to verify credentials
- **Partner API** — For organizations that want to integrate ImpactMojo content into their own training platforms

### For the Community
- **Community-contributed courses** — Verified practitioners can publish their own courses on the platform
- **Live workshop integration** — Book workshops directly through the platform with calendar integration

### Platform Quality
- **Impact measurement dashboard** — Track real-world outcomes from learners' projects and practice

## Recently Completed

### v10.18.0 — April 2026
- **Sitemap expansion** — 84 → 171 indexed URLs (all courses, BookSummaries, blog posts, and public pages)
- **Stale link cleanup** — ~100 legacy `101.impactmojo.in` links migrated to self-hosted paths
- **Search index cleanup** — Removed phantom entries, added missing labs
- **Count drift fixes** across marketing kit, press kit, README, and docs

### v10.17.0 — April 2026
- **Formspree eliminated** — All 12 forms migrated to Netlify Forms. Platform now runs on 2 services (Netlify + Supabase) instead of 3
- **Engagement email pipeline** — 5-email drip sequence (Day 0/3/7/14/21) with streak reminders and cohort deadlines. ([#144](https://github.com/ImpactMojo/ImpactMojo/issues/144), [#145](https://github.com/ImpactMojo/ImpactMojo/issues/145))
- **Monthly newsletter** — Automated content roundup on the 15th of every month
- **Premium sales letter** and **Practitioner Starter Kit** pages
- **Branded email template** — Consistent design across all platform emails via Resend

### v10.16.0 — April 2026
- **Accessibility Statement** at `/accessibility.html` — Formal WCAG 2.1 Level AA conformance statement
- **Full accessibility audit** — axe-core + pa11y-ci CI pipeline, UserWay widget integration

### v10.15.0 — April 2026
- **Content count corrections** sitewide — all files now show canonical 52 courses / 13 labs / 134 games

### v10.14.0 — April 2026
- **Device-mode default theme** on 70 pages — OS dark/light preference on first paint
- **WCAG AA link underlines** across 74 content pages
- **CC BY-NC-ND 4.0 attribution** backfilled into all 84 handouts

### v10.13.0 — April 2026
- **4 native 101 slide decks** — Dev Econ, MEL, Climate, Inequality migrated from Gamma to self-hosted HTML (100 slides each, interactive charts, light/dark theme)

### v10.10.0 — March 2026
- **ImpactMojo MCP Server** — 11 tools and 3 resources exposing the full knowledge base via Model Context Protocol. Works with Claude Desktop, Claude Code, Cursor, and any MCP client. npm-publishable.

### v10.9.0 — March 2026
- Sitewide design audit: 242 pages updated with ImpactMojo fonts, 3-mode theme toggle, paper plane SVG, sticky topbar, and footer
- Full mobile responsiveness across all BookSummaries, Games, Handouts, Blog, Courses, Labs, Templates, and Premium Tools
- GitBook documentation link added to footer across all pages

### v10.1.0 — March 2026
- Git best-practice standards across all 29 repos
- GitBook docs sidebar link fix

### v10.0.0 — March 2026
- Font standardization (Amaranth + Inter + JetBrains Mono) across 80 files
- Canvas line charts on admin and transparency dashboards
- Mobile navigation fixes across all pages
- What's New and Wall of Love sections on mobile homepage
- 4 new flagship courses

### v9.x — March 2026
- JWT-based premium access control
- Supabase authentication (Email, Google OAuth, Magic Links)
- W3C Open Badges 3.0 verifiable credentials
- Learning Pathways with milestone progression
- Interactive assessments for flagship courses
- Full-text search (Ctrl+K)
- Offline PWA support
- ImpactMojo Dataverse (215+ tools and datasets)
- BCT Repository (203 behaviour change techniques)
- 16 learning games, 11 interactive labs
- Dark mode and high-contrast theme
- Multilingual support (6 languages)

## How to Suggest Features

1. Check [existing discussions](https://github.com/ImpactMojo/ImpactMojo/discussions/categories/ideas) to see if someone has already suggested it
2. Open a new discussion in the **Ideas** category
3. Describe the problem you're trying to solve — not just the feature you want. For example: "My team struggles to track who has completed which training module" is more helpful than "Add a dashboard"
4. Include examples from your development practice if possible — it helps us prioritize

You can also email suggestions to hello@impactmojo.in.
