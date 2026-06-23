# Visual-regression harness (#563 gate)

Issue #563 (migrate `css/imx-main.css` off load-bearing `!important` to CSS
`@layer`) is **explicitly gated** on a visual-regression harness: the `!important`
rules are mostly responsive/redesign overrides, so the only safe way to refactor
them is to prove the rendered pages don't change. This is that harness.

It screenshots representative pages across **viewport × theme** and fails on any
unintended visual diff.

## What it covers

- **Pages:** home, a flagship course, a lab, premium, catalog, account, cookies,
  BookSummaries, and the Climate Action game (one of each template the stylesheet
  touches). Edit the `PAGES` array in `visual-regression.spec.js` to add more.
- **Viewports:** desktop (1280×900) and mobile (Pixel 7) — the two `projects` in
  `playwright.config.js`.
- **Themes:** light and dark, forced via `localStorage['im-theme']` before scripts run.

That's 9 pages × 2 themes × 2 viewports = **36 snapshots**.

## Run it

> Needs a real browser, so run locally or in CI — not in the Claude Code sandbox
> (no Chromium there).

```bash
cd tests/visual
npm install
npx playwright install chromium

# 1. Create baselines on a known-good build (e.g. main):
BASE_URL=https://www.impactmojo.in npm run baseline

# 2. Do the @layer refactor on a branch.

# 3. Compare — any layout/colour shift fails with a pixel diff:
BASE_URL=https://www.impactmojo.in npm test
npm run report   # open the visual diff report
```

Set `BASE_URL` to a local server (`npx http-server -p 8080` from the repo root)
to test un-merged work before deploy.

## Workflow for #563

1. On `main`, run `npm run baseline` and commit `__screenshots__/`.
2. Branch, wrap the stylesheet in `@layer base, components, redesign, responsive, overrides;`
   and drop `!important` tier by tier (start with base-level redesign overrides).
3. After each tier, run `npm test`. Green = the cascade still resolves identically.
   Red = that `!important` was load-bearing; keep it (or scope it into a higher layer).
4. Only merge when the suite is green across all 36 snapshots.

Baselines are environment-sensitive (font rendering differs per OS). Generate and
compare on the **same** runner — pin it to the CI image used for the comparison run.
