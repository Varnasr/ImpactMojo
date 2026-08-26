import { chromium } from 'playwright-core';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
for (const [w,tag] of [[390,'mob'],[900,'desk']]) {
  for (const theme of ['light','dark']) {
    const p = await b.newPage();
    await p.setViewportSize({ width: w, height: 900 });
    await p.goto('http://localhost:8199/blog/dividing-good-by-money.html', { waitUntil: 'domcontentloaded' });
    await p.evaluate(t => document.documentElement.setAttribute('data-theme', t), theme);
    await p.waitForTimeout(800);
    const figs = await p.$$('.article-illustration');
    await figs[0].screenshot({ path: `f-${tag}-${theme}.png` });
    await p.close();
  }
}
await b.close();
