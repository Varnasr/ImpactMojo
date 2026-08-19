/**
 * Render the next monthly newsletter from the real changelog, search index and
 * counts, and write it to a file. Nothing is sent.
 *
 * Run: node scripts/preview-newsletter.mjs [outfile]
 */
import fs from "node:fs";
import path from "node:path";

const root = new URL("..", import.meta.url).pathname;
const nl = await import(new URL("../netlify/functions/monthly-newsletter.mjs", import.meta.url));

const index = JSON.parse(fs.readFileSync(path.join(root, "data/search-index.json"), "utf8"));
const counts = JSON.parse(fs.readFileSync(path.join(root, "data/counts.json"), "utf8"));
const changelog = fs.readFileSync(path.join(root, "docs/changelog.md"), "utf8");

const highlights = nl.parseChangelog(changelog);
const items = nl.buildItems(highlights, index);
const sections = nl.groupItems(items);
const month = new Date().toLocaleString("en-IN", { month: "long", year: "numeric" });
const lede = sections.length > 1
  ? `${items.length} new things went up on ImpactMojo this month, across ${sections.length} kinds of work. Everything is linked below.`
  : `${items.length} new things went up on ImpactMojo this month.`;

const subject = nl.buildSubject(items, month);
const body = nl.composeBody("Varna", lede, sections, counts);

// Mirror of wrapEmail() in supabase/functions/send-notification/index.ts.
const html = `<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>${subject}</title></head>
<body style="font-family:'Amaranth',Georgia,serif;background:#F1F5F9;margin:0;padding:0">
<div style="max-width:600px;margin:0 auto">
<div style="background:linear-gradient(135deg,#0F172A 0%,#075985 100%);padding:32px 32px 24px;text-align:center">
<p style="font-family:Inter,Helvetica,sans-serif;font-weight:700;font-size:20px;color:#FFFFFF;letter-spacing:-0.02em;margin:12px 0 0">ImpactMojo</p>
</div>
<div style="background:#075985;padding:14px 32px;text-align:center">
<h2 style="font-family:Inter,Helvetica,sans-serif;color:#FFFFFF;margin:0;font-size:17px;font-weight:600;line-height:1.4">${subject}</h2>
</div>
<div style="background:#FFFFFF;padding:32px;color:#334155;line-height:1.7;font-size:15px">
${body}
</div>
<div style="height:4px;background:linear-gradient(90deg,#F59E0B 0%,#EF4444 50%,#F59E0B 100%)"></div>
<div style="background:#0F172A;padding:24px 32px;text-align:center">
<p style="color:#94A3B8;font-family:Inter,Helvetica,sans-serif;font-size:12px;margin:0;line-height:1.6">
<strong style="color:#CBD5E1">ImpactMojo</strong> &middot; Free Development Education for South Asia<br>
<a href="https://www.impactmojo.in" style="color:#F59E0B;text-decoration:none">impactmojo.in</a></p>
</div>
</div></body></html>`;

const out = process.argv[2] || path.join(root, "newsletter-preview.html");
fs.writeFileSync(out, html);

console.log(`eligible in window : ${highlights.length}`);
console.log(`shipped            : ${items.length}`);
console.log(`resolved to a page : ${items.filter((i) => i.resolved).length}`);
console.log(`sections           : ${sections.map((s) => s.label + " (" + s.items.length + ")").join(", ")}`);
console.log(`subject            : ${subject}`);
const unresolved = items.filter((i) => !i.resolved);
if (unresolved.length) console.log(`routed by topic    : ${unresolved.map((i) => i.title + " -> " + i.url).join("; ")}`);
console.log(`\nwrote ${out}`);
