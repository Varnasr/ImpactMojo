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
//   BASE_URL=http://localhost:8080 npx playwright test                       # compare
//   BASE_URL=http://localhost:8080 npx playwright test --update-snapshots    # (re)baseline
//
// Point BASE_URL at a local server (e.g. python3 -m http.server 8080) to test
// un-merged work.
//
// DETERMINISM — this spec neutralises every source of run-to-run variance:
//   1. ALL external hosts are blocked via routing (fonts.googleapis.com,
//      cdn.jsdelivr.net, cdnjs, userway, googletagmanager, Supabase, …).
//      Only the BASE_URL origin is allowed. This is applied identically to
//      baseline and comparison runs, so blocked web-fonts / widgets can never
//      cause a diff — and hanging third-party requests can no longer stall
//      `networkidle` (the original cause of the home/catalog/course-mel
//      timeouts: those pages reference CDNs that hang behind the sandbox
//      proxy, so networkidle never fired and the 30 s test timeout hit).
//   2. Date is frozen (Date.now / new Date() → fixed instant) so date-seeded
//      content (js/daily-spotlight.js rotation, auto-refresh cache-busters,
//      "today" strings) renders identically every run and every day.
//   3. Math.random is replaced with a seeded PRNG — any randomised ordering
//      or shuffled content is the same on every run.
//   4. prefers-reduced-motion is emulated and a kill-switch stylesheet
//      disables all animations/transitions and hides the text caret.
//   5. Web-font readiness is awaited (document.fonts.ready) and a scripted
//      scroll pass triggers lazy-loaded content before the screenshot.
// No mask regions are needed — everything dynamic is frozen at the source.

import { test, expect } from '@playwright/test';

const BASE_URL = process.env.BASE_URL || 'http://localhost:8080';
const BASE_HOST = new URL(BASE_URL).host;

// Fixed instant for all frozen clocks: 2026-01-15T12:00:00Z (arbitrary but
// stable — never change it or date-seeded content will legitimately shift
// and baselines must be regenerated).
const FROZEN_NOW = Date.UTC(2026, 0, 15, 12, 0, 0);

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

const FREEZE_CSS = `
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
    caret-color: transparent !important;
  }
`;

for (const theme of THEMES) {
  for (const page of PAGES) {
    test(`${page.name} — ${theme}`, async ({ page: pw }) => {
      // (1) Block every request that isn't same-origin with BASE_URL.
      // Applied before navigation so baseline and test runs are identical.
      await pw.route('**/*', (route) => {
        const host = new URL(route.request().url()).host;
        return host === BASE_HOST ? route.continue() : route.abort();
      });

      // (4) Kill motion at the media-query level too.
      await pw.emulateMedia({ reducedMotion: 'reduce' });

      // Force the theme before any script runs (matches js/theme.js
      // conventions), and (2)+(3) freeze time and randomness.
      await pw.addInitScript(({ t, now }) => {
        try {
          localStorage.setItem('im-theme', t);
          localStorage.setItem('theme', t);
        } catch (e) { /* ignore */ }

        // Freeze the clock: no-arg Date and Date.now always return FROZEN_NOW.
        const OrigDate = Date;
        class FrozenDate extends OrigDate {
          constructor(...args) {
            if (args.length === 0) super(now); else super(...args);
          }
          static now() { return now; }
        }
        FrozenDate.parse = OrigDate.parse.bind(OrigDate);
        FrozenDate.UTC = OrigDate.UTC.bind(OrigDate);
        // eslint-disable-next-line no-global-assign
        window.Date = FrozenDate;
        if (typeof performance !== 'undefined' && performance.now) {
          let tick = 0;
          performance.now = () => (tick += 16); // monotonic but deterministic
        }

        // Seeded PRNG replaces Math.random (same LCG as daily-spotlight.js).
        let seed = 42;
        Math.random = () => {
          seed = (seed * 9301 + 49297) % 233280;
          return seed / 233280;
        };
      }, { t: theme, now: FROZEN_NOW });

      // With external hosts aborted instantly, networkidle settles fast.
      await pw.goto(BASE_URL + page.path, { waitUntil: 'networkidle' });

      // (4) Belt-and-braces stylesheet kill-switch for animations/carets.
      await pw.addStyleTag({ content: FREEZE_CSS });

      // Course pages (js/course-loader.js) fetch module content from a
      // Supabase edge function. That host is blocked above, so the loader
      // fails fast, retries once after 1.5 s, then settles on its error
      // state. Wait for the transient "Loading course content..." spinners
      // to disappear so we always screenshot the settled state (no-op on
      // pages without the loader).
      await pw.waitForFunction(
        () => !document.querySelector('.content-loading'),
        null,
        { timeout: 30_000 }
      );

      // (5) Wait for fonts, then walk the page to flush lazy-loaded content,
      // return to the top, and let layout settle.
      await pw.evaluate(() => document.fonts.ready);
      await pw.evaluate(async () => {
        await new Promise((resolve) => {
          let y = 0;
          const step = () => {
            y += 900;
            window.scrollTo(0, y);
            if (y < document.documentElement.scrollHeight) {
              setTimeout(step, 40);
            } else {
              window.scrollTo(0, 0);
              setTimeout(resolve, 120);
            }
          };
          step();
        });
      });
      await pw.waitForLoadState('networkidle');
      await pw.waitForTimeout(400);

      await expect(pw).toHaveScreenshot(`${page.name}-${theme}.png`, {
        fullPage: true,
        maxDiffPixelRatio: 0.01, // tolerate sub-pixel AA noise, catch real layout shifts
        animations: 'disabled',
      });
    });
  }
}
