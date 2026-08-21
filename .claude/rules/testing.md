# Testing

No formal test framework — static HTML site with no build step.

## Ship checklist — post-merge deploy verification (MANDATORY)

Netlify's git webhook can silently drop a merge event: deploy previews build,
production stays on the previous release, nothing errors (this happened to
v10.141.0 on 2026-07-19). After EVERY merge to main:

```bash
set -a; . .claude/.env.keys 2>/dev/null; set +a
python3 scripts/verify-deploy.py        # polls production; auto-triggers a
                                        # manual build if the webhook was missed
```

Must print `PASS — production deploy ready`. Then spot-check 1-2 live markers
from the release (curl with -L; remember Netlify's lowercase/pretty-URL
redirects). Never announce a release as live on version.json age alone.

## Manual verification checklist

Before considering any change complete:

1. **JSON validity**: Run `python3 -m json.tool data/search-index.json > /dev/null` after any data file changes
2. **Link check**: Grep for the new file path in `index.html` — confirm it resolves to a real file
3. **Count consistency**: Canonical counts live in `data/counts.json` (incl. `dataverse`) — update the number there first, then run `python3 scripts/check-counts.py` — must print `PASS`. Use `python3 scripts/check-counts.py --fix` to rewrite drift to canonical automatically, then re-run to confirm. **Scope is sitewide**: it scans **every root-level `*.html`** (all landing/marketing/legal/premium pages — new pages are covered automatically) plus the present-tense GitBook overview docs + README. It matches prose (`"70 courses"`, `"324 datasets"`, `"324 curated data tools"`) **and** stat tiles in any markup (a number alone in one element followed by a labelled element — `<b>34</b><span>Interactive Labs</span>`, `stat-value`/`stat-label`, `chip`/`nm`, `sn`/`sl`, `tp-cnt`, …), resolving the label by keyword. Deliberately **excluded** (their numbers are legitimately not the platform totals): changelogs, roadmaps, the blog, `updates.html`, per-course pages, `premium-tools/`, book summaries, translated docs, and the dynamic dashboards (`org-dashboard.html`, `game-library.html`). A match is skipped if the number is adjacent to an arrow (`→`/`->`, a historical range) or the line contains `count-ignore`. Enforced in CI via the `counts` job in `ci.yml`.
4. **Form attributes**: Grep for `data-netlify="true"` in any new HTML files that contain forms — ensure forms have `name`, `data-netlify="true"`, and `netlify-honeypot="bot-field"`
5. **Responsive meta**: Every new HTML file must have `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
6. **Service worker** (after any change to `service-worker.js` or `js/pwa.js`): Run `node scripts/test-service-worker.mjs` — must print `PASS`. Loads the real SW source in a sandbox and asserts the offline-without-stale-files contract: HTML is network-first (fresh online, `/offline.html` fallback offline), assets are stale-while-revalidate, backend/API/non-GET requests bypass the SW, `activate` purges stale runtime caches but keeps `impactmojo-course-*` downloads, and `CACHE_COURSE` stores a course offline. Enforced in CI via the `service-worker` job in `ci.yml`. **Also smoke-test in a real browser before relying on it** (DevTools → Application → Service Workers): load a page online, go offline, reload a previously-visited page (should render), reload an unvisited page (should show `/offline.html`), then download a flagship course and confirm it opens offline.
7. **Encoding / mojibake**: Run `python3 scripts/check-mojibake.py` — must print `PASS`. Catches the encoding-corruption signatures that have historically broken scripts (e.g. `js/faq-bank.js`): classic UTF-8/CP1252 byte corruption, smart-punctuation collapse, the U+FFFD replacement char, and C1 control characters. Enforced in CI via the `encoding` job in `ci.yml`; it has zero false positives on legitimate Unicode (em-dash, ellipsis, rupee, copyright, section, middot, plus-minus, smart quotes, Indic i18n).
8. **Translation quality (i18n)**: After any change to `i18n/<lang>.json` or `i18n/pages/<lang>/*.json`, run `python3 scripts/check-i18n-quality.py` — must print `PASS`. Deterministic, zero-false-positive guard for the four machine-translation corruption classes the 2026-06 audit eliminated: cross-script leakage (foreign Indic letters in a value, e.g. Odia inside Bengali — shared danda `।` excluded), the "text:" placeholder artifact (पाठ: / मजकूर: / টেক্সট: / உரை:), the brand name "ImpactMojo" rendered in native script, and character-run corruption (same char repeated 6+ times). Enforced in CI via the `i18n-quality` job in `ci.yml` (every push/PR **and** a daily schedule). The companion `scripts/check-i18n-glossary.py` is an advisory (noisier) detector for protected-term drops; `data/i18n-glossary.json` is the protected-terms reference.
9. **Book-companion blank-page guard**: After adding or editing any `BookSummaries/*-companion.html`, run `python3 scripts/check-book-companions.py` — must print `PASS`. The interactive companions render client-side from an inline `const DATA = {...}` object; this guard catches the deterministic ways one renders BLANK in the browser — DATA that isn't valid JSON, a `</script>` / U+2028 / U+2029 / raw C0 control char inside DATA (ends the `<script>` block or breaks the JS literal), or an empty title/sections. Intentionally lenient about schema variation (older companions omit `southAsia`, use `summary` instead of `ideas`, or ship as a compiled bundle with no `const DATA`), so it has zero false positives on the existing library. Enforced in CI via the `book-companions` job in `ci.yml`. For a deeper, real-browser render check (visible-text length + JS errors across every page), run `node scripts/validate-companions.mjs` — needs `playwright-core` + Chromium + a local `python3 -m http.server 8199`; not in CI because a browser run is heavier/flakier than the static guard.

10. **Supabase anon-exposure guard**: Run `python3 scripts/check-supabase-anon.py` — must print `PASS`. Re-probes, with the *public* anon key, the access contract fixed by the 2026-08-03 remediation (PR #895): `push_subscriptions`, `challenge_submissions`, `organizations` and `organization_members` must stay anon-denied (401), the sensitive `profiles` columns (phone/address/email/bio) must stay denied, and the deliberately public reads — `certificates` and the granted `profiles` columns — must keep working, so an over-correction that breaks certificate verification is caught as well as a leak. **No secrets**: the URL and anon key are read from `js/config.js`, the same pair every browser already receives, so the guard can never drift from what the site ships. Network blips are retried 3×. Runs in CI as the `supabase-anon` job on the **daily schedule and `workflow_dispatch` only** — not on pull requests, since it hits a live third-party API where latency would add flake and a contributor could not act on the result. If a change is deliberate, update `PROBES` in the script to match.

11. **Asset-stamp freshness**: After changing any CSS/JS a Fundamentals page loads, run `python3 scripts/stamp-assets.py` — then `--check` must print `PASS`. Every `/css/*` and `/js/*` reference on those pages carries `?v=<content hash>`, so a URL changes whenever its file does. This exists because `service-worker.js` serves **HTML network-first and static assets stale-while-revalidate**: deliberate, and correct for offline, but it means the first load after a deploy can pair *fresh* HTML with the *previous* deploy's JS. On 2026-08-19 that shipped a Power Cube whose HTML had `<svg id="cubeSvg">` and whose cached JS had no code to draw into it — an empty box on the user's phone, no error anywhere, nothing red in CI. The stamp makes that pairing impossible: new HTML requests a URL that cannot already be cached. Enforced in CI via the `asset-stamps` job.

    **You do not need to bump `VERSION` in `service-worker.js` by hand.** This rule used to say you did. Netlify's build command is `bash scripts/stamp-version.sh` (see `netlify.toml`), which rewrites `const VERSION` to `v2-<commit sha>` on **every** deploy — so the runtime cache already rotates once per deploy and the committed value never reaches production. The script says so itself: the committed VERSION "is just a sensible default for local/preview". Verified 2026-08-20 against a live deploy, where the repo held `v18-2026-08-20` and production served `v2-772296480539`. Bump it if you like for local clarity; it changes nothing that ships.

12. **Diagram text contrast**: Run `python3 scripts/check-diagram-contrast.py` — must print `PASS`. The four Fundamentals diagrams paint text straight onto a coloured shape, so the ink is chosen per fill at render time, and that choice has been got wrong twice the same way — a fixed luminance cutoff. `cube.js` put white on `#d97706` (3.19:1); `fundamentals-wheel.js` kept a 0.42 cutoff and put white on all twelve outer-ring fills, which are the base mixed 42% with white and land just under it, so every rim label on the wheel read at 2.3–3.2:1 in the default theme, on desktop. The guard checks both halves: that every fill (including the wheel's three ring mixes) has an ink clearing 4.5:1, **and** that each renderer picks it by comparing the two candidate ratios rather than testing luminance against a constant. The second half is the one that matters — the first passes even when the code picks the worse ink, which is exactly what shipped. It also checks the cube's face-title colours, which sit on the panel rather than a slice and so are hand-picked in `css/fundamentals.css`, against both theme backgrounds. Enforced in CI via the `diagram-contrast` job.

    **Neither audit would have caught this.** axe-core does not evaluate SVG text contrast, so it reported 0 violations on the wheel with all twelve labels failing. pa11y (HTML_CodeSniffer) does catch DOM contrast — it is what found the 3.19:1 rung number axe missed — but both run only the **default light theme at desktop width**, so a dark-theme-only failure (the cube's face titles, 2.76–3.13:1) is invisible to them. When changing anything colour-bearing, check both themes explicitly; a green audit run means less than it looks.

13. **Site-search coverage**: After adding any page that goes into `sitemap.xml`, run `python3 scripts/check-search-coverage.py` — must print `PASS`. The sitemap is what we tell Google exists; `data/search-index.json` is what our own visitors can find, and they had drifted **127 pages apart** — 47 course posters, 19 reading companions, 17 course lexicons and 8 premium tools, all live and crawlable and unfindable in site search. Nothing failed to allow it: adding a page updates the sitemap, and the index is a separate file nobody is forced to touch. The guard compares **decoded, case-folded, fragment-stripped** paths, because comparing raw strings reports 87 phantom gaps (the index stores `%20` in handout paths, the sitemap does not). Deliberate exclusions live in `EXEMPT` in the script with a written reason, and a **stale exemption fails too** — an exempted page that later gets indexed, or leaves the sitemap, is reported, so the list cannot rot into a blindfold. Enforced in CI via the `search-coverage` job.

14. **Viewport meta**: Run `python3 scripts/check-viewport.py` — must print `PASS`. Item 5 above has required a viewport meta on every new HTML file since this file existed, and nothing checked it. Without one a phone lays the page out at desktop width and zooms out, so the text arrives too small to read; the page looks correct on the machine it was built on and only a visitor on a phone ever sees it. The guard tolerates **`name=viewport` unquoted** and **`content=` written before `name=`** — both shapes are in this repo (`index.html` uses the reversed order, the compiled reading companions use unquoted), and both defeat a naive `name="viewport"` scan. An ad-hoc check missing exactly those two shapes reported two companions as broken when they were fine, so the tolerance is the point of the guard, not a detail. Exemptions live in `EXEMPT` with a written reason (the five Supabase email templates, since a mail client ignores viewport), and a stale exemption fails too. Enforced in CI via the `viewport` job.

15. **Heading survives the chrome strip**: Run `python3 scripts/check-h1-survives-chrome.py` — must print `PASS`. `js/site-chrome.js` removes, at runtime, any `<header>`/`<nav>` that is a **direct child of `<body>`** (plus `.nav-container`/`.masthead`/`.mobile-header`/`footer`/`.foot`/`.site-footer`/`.im-footer` anywhere). That is deliberate — it strips legacy per-page nav bars so the shared top bar can be injected — and `rules/content-management.md` has warned about it since the ASER/NFHS incident. What nobody checked is the **collateral**: a page whose only `<h1>` sits inside that header ships a heading no visitor and no screen reader ever sees, and anything else in the block goes with it. On 2026-08-21 that was **24 pages**, and on three of them it was deleting working UI — the Gandhian Lexicon's search box and category filter (`#searchInput`, `#categoryFilter`), the LogFrame Builder's Import/Example/Reset buttons, and the Public Choice lexicon's term counter. The inline scripts bound their listeners at parse time and the deferred chrome removed the elements afterwards, so the handlers were live on detached nodes: **no console error, nothing red, the feature simply absent**.

    **The fix is a one-word change**: `<header class="hero">` → `<section class="hero">`. The class carries the styling, so nothing moves. Only two of the 24 needed more — `courses/gandhi/lexicon.html` and `premium-tools/vaniscribe.html` styled the bare `header` **tag**, so those got a real class (`.lx-head`, `.vs-head`) and the CSS selector updated with them. Check which you are dealing with (`grep -E '(^|[^.a-zA-Z_-])header\s*[,{]'`) before swapping, or you will silently drop the styling.

    **Neither accessibility job would have caught this.** axe-core tests **10** hardcoded pages and pa11y-ci **19**; none of the 24 appeared in either list, and a newly added page joins neither by default — which is exactly why this guard walks every page that loads the chrome instead of a fixed list. Enforced in CI via the `heading-survives-chrome` job.

### A note on the retired maintenance Routines

Between 2026-07-19 and 2026-08-04 this repo was maintained by ~12 scheduled Claude Routines (daily Supabase health, count drift, content wiring; weekly backend/i18n/link/forms/SEO; monthly fact-check). **They no longer exist**, and they left a mess worth remembering: each run pushed a `claude/routine-<name>-<date>` branch and never opened a PR, so 41 such branches accumulated carrying work that never reached `main`. The Supabase routine spent eleven days re-deriving its own history from unmerged branches and recording, in its own snapshot file, that "none of the 11 daily PRs 20260721-20260802 have ever been merged to main".

The lesson is in the design, not the tooling: **an automated check is only worth having if its failure is visible and its output lands somewhere.** Anything that can drift without a commit belongs in `ci.yml` on the `schedule:` trigger, where a red run notifies the owner. Most of what those Routines covered — counts, i18n, encoding, internal links, book companions — is already enforced there on every push *and* daily. What the schedule genuinely adds beyond a PR gate is the class of failure that needs no commit at all: external link rot and live-service drift, which is why `broken-links` now fails on the scheduled run (it is still `fail: false` on PRs) and why `supabase-anon` exists.

## Manual browser QA — push & offline (PWA)

These need a real browser (no headless Chromium in the agent sandbox). Run after any service-worker / push change, on the deployed site or a local `npx http-server`:

**Offline (service worker):**
1. Load a flagship course online (e.g. `/courses/mel/`). DevTools → Application → Service Workers shows the SW *activated*.
2. Go offline (DevTools → Network → Offline). Reload the same page → it still renders (network-first fell back to cache).
3. Navigate to a page you have NOT visited → shows `/offline.html` (not a browser error).
4. Back online, in `js/offline.js`-enabled pages, click "download course" → reload offline → the course opens.
5. Deploy check: after a deploy, a normal reload shows fresh content (network-first), and DevTools → Application → Cache Storage shows only the current `im-runtime-*` cache (old versions purged).

**Push notifications:**
1. Sign in → `/account.html` → Notifications card → **Browser Notifications** toggle.
2. Flip it on → browser permission prompt appears → Allow. The toggle stays on; `push_subscriptions` gets a row (check via Supabase).
3. Trigger a test push (service role): `POST {SUPABASE_URL}/functions/v1/send-push/send` with `{ "user_id": "<your id>", "title": "Test", "body": "hello", "link": "/account.html" }` → a notification banner appears; clicking it focuses/opens the link.
4. Flip the toggle off → the subscription is removed and no further pushes arrive.

## Visual regression — CSS @layer migration (#563)

The `tests/visual/` Playwright harness gates issue #563. **Chromium *is* installed in the agent sandbox** (`/opt/pw-browsers/chromium`, with `PLAYWRIGHT_BROWSERS_PATH` set) — the earlier "no browser" note was wrong, and a July comment on #563 claiming the harness "runs fine in remote agent sessions" was wrong in the other direction. What is actually true, measured 2026-08-20: the browser launches, but it **cannot reach the network** — every external navigation dies with `ERR_CONNECTION_RESET` through the agent proxy, including `example.com`, with or without `proxy: { server: $HTTPS_PROXY }`. So a sandbox run works against a **local server only** (which is exactly why the `axe-core` and `pa11y-ci` CI jobs pass — they serve `localhost:8080`), and anything needing a deploy preview or a CDN-loaded script has to run elsewhere. Locally/CI: `cd tests/visual && npm install && npx playwright install chromium`, baseline on `main` with `npm run baseline`, then `npm test` after the refactor — any layout/colour shift fails as a snapshot diff. See `tests/visual/README.md`.

## Useful grep commands

```bash
# Find all content count references (replace 16 with current game count)
grep -rn "16 Games\|16 games\|16 Interactive" index.html catalog.html docs/

# Validate all JSON data files
for f in data/*.json; do python3 -m json.tool "$f" > /dev/null && echo "OK: $f" || echo "FAIL: $f"; done

# Check for broken internal links in index.html
grep -oP 'href="(/[^"]+)"' index.html | sort -u
```

## Related

- Agent `content-auditor` automates consistency checks across the platform
- Skill `housekeeping` includes quality checks as step 10
- Command `/project:deploy-check` runs a pre-deploy verification
