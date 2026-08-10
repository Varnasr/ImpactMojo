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

The `tests/visual/` Playwright harness gates issue #563. It can't run in the agent sandbox (no browser); run it locally/CI: `cd tests/visual && npm install && npx playwright install chromium`, baseline on `main` with `npm run baseline`, then `npm test` after the refactor — any layout/colour shift fails as a snapshot diff. See `tests/visual/README.md`.

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
