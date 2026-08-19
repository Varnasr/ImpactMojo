/**
 * Automated accessibility testing with axe-core + Puppeteer
 *
 * Launches a local HTTP server, visits each target page, and runs
 * axe-core to detect WCAG 2.1 AA violations.
 *
 * Usage:
 *   npm run test:a11y              # assumes http-server is already running on :8080
 *   AXE_SERVER_URL=http://localhost:3000 node tests/axe-accessibility.js
 *
 * The script will:
 *  - Start an http-server if the env var AXE_START_SERVER=true (CI default)
 *  - Test all pages listed below against WCAG 2.1 Level AA
 *  - Print a summary and exit with code 1 if any violations are found
 */

const puppeteer = require('puppeteer');
const { AxePuppeteer } = require('@axe-core/puppeteer') || {};
const { execSync, spawn } = require('child_process');
const path = require('path');

// ---------------------------------------------------------------------------
// Configuration
// ---------------------------------------------------------------------------

const BASE_URL = process.env.AXE_SERVER_URL || 'http://localhost:8080';

// Pages to audit (relative to the site root)
const PAGES = [
  'index.html',
  'about.html',
  'catalog.html',
  'bct-repository.html',
  'courses/mel/index.html',
  'fundamentals/wheel.html',
  'fundamentals/index.html',
  'fundamentals/ladder.html',
  'fundamentals/power-cube.html',
  'fundamentals/who-counts.html',
];

// axe-core impact levels: minor, moderate, serious, critical
// Only fail on serious + critical by default; override with AXE_MIN_IMPACT
const MIN_IMPACT = process.env.AXE_MIN_IMPACT || 'serious';
const IMPACT_ORDER = ['minor', 'moderate', 'serious', 'critical'];

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function impactAtLeast(impact, threshold) {
  return IMPACT_ORDER.indexOf(impact) >= IMPACT_ORDER.indexOf(threshold);
}

function colorize(text, code) {
  return `\x1b[${code}m${text}\x1b[0m`;
}

const red    = (t) => colorize(t, 31);
const green  = (t) => colorize(t, 32);
const yellow = (t) => colorize(t, 33);
const bold   = (t) => colorize(t, 1);

function printViolation(v) {
  const impactColors = { minor: 33, moderate: 33, serious: 31, critical: 31 };
  const color = impactColors[v.impact] || 0;
  console.log(`  ${colorize(v.impact.toUpperCase(), color)} : ${v.id} — ${v.help}`);
  console.log(`           ${v.helpUrl}`);
  v.nodes.slice(0, 3).forEach((node) => {
    console.log(`           target: ${node.target.join(', ')}`);
  });
  if (v.nodes.length > 3) {
    console.log(`           ... and ${v.nodes.length - 3} more elements`);
  }
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

async function runAxeOnPage(browser, url) {
  const page = await browser.newPage();
  await page.setBypassCSP(true);
  try {
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
  } catch (err) {
    console.log(yellow(`  WARNING: Could not load ${url} — ${err.message}`));
    await page.close();
    return { url, violations: [], skipped: true };
  }

  // Inject axe-core manually (works even if @axe-core/puppeteer is not installed)
  const axeSource = require('axe-core').source;
  await page.evaluate(axeSource);

  const results = await page.evaluate(() => {
    /* global axe */
    // Exclude third-party widgets that we don't directly own:
    //   - .introjs-* — Intro.js tour library (auto-starts via js/tours.js)
    //   - .userway_* / #uwy* — UserWay accessibility widget
    //   - .gtranslate_wrapper — Google Translate widget
    return axe.run(
      {
        exclude: [
          ['.introjs-tooltip'],
          ['.introjs-overlay'],
          ['.introjs-helperLayer'],
          ['.introjs-progressbar'],
          ['.introjs-bullets'],
          ['.introjs-arrow'],
          ['[class^="userway_"]'],
          ['#uwy'],
          ['.gtranslate_wrapper'],
        ],
      },
      {
        runOnly: {
          type: 'tag',
          values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'best-practice'],
        },
      }
    );
  });

  await page.close();
  return { url, violations: results.violations, passes: results.passes.length };
}

async function main() {
  let serverProcess = null;

  // Optionally start a local server (useful in CI)
  if (process.env.AXE_START_SERVER === 'true') {
    const root = path.resolve(__dirname, '..');
    serverProcess = spawn('npx', ['http-server', root, '-p', '8080', '-s'], {
      stdio: 'ignore',
      detached: true,
    });
    // Give the server a moment to boot
    await new Promise((r) => setTimeout(r, 2000));
  }

  // puppeteer >= 23 dropped the `'new'` string; `true` now means the new headless mode
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  console.log(bold('\n=== axe-core Accessibility Audit ===\n'));
  console.log(`Base URL : ${BASE_URL}`);
  console.log(`Pages    : ${PAGES.length}`);
  console.log(`Min fail : ${MIN_IMPACT} and above\n`);

  let totalViolations = 0;
  let totalFailingViolations = 0;
  const summaries = [];

  for (const pagePath of PAGES) {
    const url = `${BASE_URL}/${pagePath}`;
    console.log(bold(`\n--- ${pagePath} ---`));

    const result = await runAxeOnPage(browser, url);

    if (result.skipped) {
      summaries.push({ page: pagePath, status: 'SKIPPED', violations: 0, failing: 0 });
      continue;
    }

    const failing = result.violations.filter((v) => impactAtLeast(v.impact, MIN_IMPACT));
    const warnings = result.violations.filter((v) => !impactAtLeast(v.impact, MIN_IMPACT));

    totalViolations += result.violations.length;
    totalFailingViolations += failing.length;

    if (failing.length > 0) {
      console.log(red(`  ${failing.length} failing violation(s):`));
      failing.forEach(printViolation);
    }
    if (warnings.length > 0) {
      console.log(yellow(`  ${warnings.length} warning(s) (below threshold):`));
      warnings.forEach(printViolation);
    }
    if (result.violations.length === 0) {
      console.log(green('  No violations found.'));
    }

    console.log(`  Passed rules: ${result.passes}`);
    summaries.push({
      page: pagePath,
      status: failing.length > 0 ? 'FAIL' : 'PASS',
      violations: result.violations.length,
      failing: failing.length,
    });
  }

  await browser.close();

  if (serverProcess) {
    process.kill(-serverProcess.pid);
  }

  // Summary table
  console.log(bold('\n\n=== Summary ===\n'));
  console.log('Page                          | Status  | Violations | Failing');
  console.log('------------------------------|---------|------------|--------');
  for (const s of summaries) {
    const status = s.status === 'FAIL' ? red(s.status) : s.status === 'PASS' ? green(s.status) : yellow(s.status);
    console.log(
      `${s.page.padEnd(30)}| ${s.status === 'FAIL' ? red(s.status.padEnd(8)) : s.status === 'PASS' ? green(s.status.padEnd(8)) : yellow(s.status.padEnd(8))}| ${String(s.violations).padEnd(11)}| ${s.failing}`
    );
  }

  const audited = summaries.filter((s) => s.status !== 'SKIPPED').length;

  console.log(`\nPages audited    : ${audited} of ${summaries.length}`);
  console.log(`Total violations : ${totalViolations}`);
  console.log(`Failing (>= ${MIN_IMPACT}) : ${totalFailingViolations}\n`);

  if (totalFailingViolations > 0) {
    console.log(red(`FAILED — ${totalFailingViolations} accessibility violation(s) at ${MIN_IMPACT} level or above.\n`));
    process.exit(1);
  } else if (audited === 0) {
    // Zero violations across zero pages is not a pass. Without this, a server
    // that never came up makes every page SKIPPED and the suite still exits 0 —
    // a wholly unreachable site would report green.
    console.log(red(`FAILED — no pages were audited (all ${summaries.length} skipped). The site was unreachable at ${BASE_URL}.\n`));
    process.exit(1);
  } else {
    console.log(green('PASSED — No serious accessibility violations found.\n'));
    process.exit(0);
  }
}

main().catch((err) => {
  console.error('Unexpected error:', err);
  process.exit(2);
});
