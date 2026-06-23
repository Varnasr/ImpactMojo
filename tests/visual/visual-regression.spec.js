// Visual-regression spec for the CSS @layer migration (issue #563).
//
// Captures screenshots of representative pages across viewport × theme and
// compares them to committed baselines. This is the gate the #563 issue
// requires before any !important → @layer refactor: run it on `main` to
// create baselines, do the refactor, run it again — any unintended visual
// change shows up as a failing snapshot diff.
//
// Usage (needs a browser, so run it locally / in CI, not the agent sandbox):
//   cd tests/visual
//   npm install
//   npx playwright install chromium
//   BASE_URL=https://www.impactmojo.in npx playwright test         # compare
//   BASE_URL=https://www.impactmojo.in npx playwright test --update-snapshots  # (re)baseline
//
// Point BASE_URL at a local server (e.g. npx http-server) to test un-merged work.

import { test, expect } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:8080';

// Representative pages — one of each major template the stylesheet touches.
const PAGES = [
  { name: 'home', path: '/' },
  { name: 'course-mel', path: '/courses/mel/' },
  { name: 'lab-toc', path: '/toc-workbench.html' },
  { name: 'premium', path: '/premium.html' },
  { name: 'catalog', path: '/catalog.html' },
  { name: 'account', path: '/account.html' },
  { name: 'cookies', path: '/cookies.html' },
  { name: 'booksummaries', path: '/BookSummaries/' },
  { name: 'game-climate', path: '/Games/climate-action-game.html' },
];

const THEMES = ['light', 'dark'];

for (const theme of THEMES) {
  for (const page of PAGES) {
    test(`${page.name} — ${theme}`, async ({ page: pw }) => {
      // Force the theme before any script runs (matches js/theme.js conventions).
      await pw.addInitScript((t) => {
        try {
          localStorage.setItem('im-theme', t);
          localStorage.setItem('theme', t);
        } catch (e) { /* ignore */ }
      }, theme);

      await pw.goto(BASE_URL + page.path, { waitUntil: 'networkidle' });
      // Settle fonts/animations.
      await pw.waitForTimeout(800);

      await expect(pw).toHaveScreenshot(`${page.name}-${theme}.png`, {
        fullPage: true,
        maxDiffPixelRatio: 0.01, // tolerate sub-pixel AA noise, catch real layout shifts
        animations: 'disabled',
      });
    });
  }
}
