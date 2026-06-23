// Playwright config for the #563 visual-regression harness.
// Two projects = two viewports (desktop + mobile); the spec adds theme × page.
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: '.',
  // Baselines live next to the spec, keyed by project (viewport) + title.
  snapshotPathTemplate: '{testDir}/__screenshots__/{projectName}/{arg}{ext}',
  fullyParallel: true,
  retries: 0,
  reporter: [['list'], ['html', { open: 'never', outputFolder: 'report' }]],
  use: {
    ignoreHTTPSErrors: true,
    colorScheme: 'no-preference', // theme is forced via localStorage in the spec
  },
  projects: [
    { name: 'desktop', use: { ...devices['Desktop Chrome'], viewport: { width: 1280, height: 900 } } },
    { name: 'mobile', use: { ...devices['Pixel 7'] } },
  ],
});
