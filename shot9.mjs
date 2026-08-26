import { chromium } from 'playwright-core';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
for (const url of ['/dojos.html','/updates.html','/login.html','/upgrade.html','/org-dashboard.html','/grievance.html','/climate-trace-india.html','/404.html','/content-marketing-kit.html','/signup.html','/forgot-password.html','/reset-password.html','/ImpactMojo_PressKit.html','/offline.html']) {
  const p = await b.newPage();
  await p.setViewportSize({ width: 1100, height: 900 });
  await p.emulateMedia({ colorScheme: 'dark' });
  try {
    await p.goto('http://localhost:8199'+url, { waitUntil:'domcontentloaded' });
    await p.waitForTimeout(1200);
    const r = await p.evaluate(() => {
      // find every element whose background came from the --im-surface fallback
      const bad = [];
      for (const el of document.querySelectorAll('*')) {
        const cs = getComputedStyle(el);
        if (cs.backgroundColor === 'rgb(255, 255, 255)' && el.offsetParent) {
          const c = cs.color.match(/\d+/g).map(Number);
          const lum = (0.2126*c[0] + 0.7152*c[1] + 0.0722*c[2]) / 255;
          if (lum > 0.7) bad.push(el.className || el.tagName);
        }
      }
      return { theme: document.documentElement.getAttribute('data-theme'), badCount: bad.length, sample: bad.slice(0,3) };
    });
    console.log(url.padEnd(30), JSON.stringify(r));
  } catch(e) { console.log(url, 'ERR', e.message.slice(0,60)); }
  await p.close();
}
await b.close();
