/**
 * Deep, real-browser validation of every BookSummaries page.
 *
 * Renders each page in headless Chromium and confirms it paints substantial
 * visible content with no JavaScript errors. Complements the fast static guard
 * (scripts/check-book-companions.py) which runs in CI; this one is heavier
 * (needs a browser) so it's a manual / optional deep check.
 *
 * Usage:
 *   npm install playwright-core
 *   npx playwright install chromium         # or point EXE at an existing Chromium
 *   python3 -m http.server 8199 &           # serve the repo root so /js/* resolves
 *   CHROMIUM=/path/to/chromium node scripts/validate-companions.mjs
 *
 * Exit 0 = every page rendered content with no real JS errors; exit 1 otherwise.
 * The Supabase CDN error is ignored when the CDN is unreachable (offline sandbox);
 * it loads fine in production.
 */
import { chromium } from 'playwright-core';
import { readdirSync } from 'fs';

const EXE = process.env.CHROMIUM || undefined; // undefined => playwright-managed chromium
const PORT = process.env.PORT || 8199;
const BASE = `http://localhost:${PORT}/BookSummaries/`;
const MIN_CHARS = 500;

const files = readdirSync('BookSummaries').filter(f => f.endsWith('.html') && f !== 'index.html').sort();
const browser = await chromium.launch({ executablePath: EXE, args: ['--no-sandbox'] });
const ctx = await browser.newContext();
// Abort external requests (blocked CDNs) so the run is fast and offline-safe.
await ctx.route('**', r => {
  const u = r.request().url();
  return (u.includes(`localhost:${PORT}`) || u.startsWith('data:')) ? r.continue() : r.abort();
});

let pass = 0;
const bad = [];
for (const f of files) {
  const p = await ctx.newPage();
  const errors = [];
  p.on('pageerror', e => errors.push(e.message.split('\n')[0]));
  try {
    await p.goto(BASE + f, { waitUntil: 'domcontentloaded', timeout: 20000 });
  } catch (e) {
    errors.push('NAV: ' + e.message.slice(0, 60));
  }
  await p.waitForTimeout(700);
  const len = await p.evaluate(() => (document.body.innerText || '').replace(/\s+/g, ' ').trim().length).catch(() => 0);
  // Ignore the Supabase CDN error (sandbox-only; loads in production).
  const real = errors.filter(e => !e.includes('createClient'));
  if (len < MIN_CHARS || real.length) bad.push({ f, len, real: real.map(e => e.slice(0, 80)) });
  else pass++;
  await p.close();
}
await browser.close();

console.log(`\n===== BookSummaries render validation =====`);
console.log(`Total pages: ${files.length}`);
console.log(`PASS (>= ${MIN_CHARS} chars, no real JS errors): ${pass}`);
console.log(`FLAGGED: ${bad.length}`);
for (const x of bad) console.log(`  ${x.f}: len=${x.len} errors=${JSON.stringify(x.real)}`);
process.exit(bad.length ? 1 : 0);
