/**
 * Netlify Function — monthly newsletter (scheduled, 10:00 IST on the 15th)
 *
 * Reads the `### For Learners` entries from docs/changelog.md, resolves each one
 * to the page it is actually about, groups them by kind and composes the email.
 *
 * What this replaces, and why
 * ---------------------------
 * The previous version gave every highlight `url: "/docs/#/changelog"`, so an
 * email announcing a new reading companion sent the reader to a changelog page
 * rather than the companion. It also cut every description at 150 characters
 * mid-word, and kept only 5 items — against 72 eligible ones in a recent
 * 35-day window. The result was an email that could not link to the work it was
 * announcing and showed a fourteenth of it.
 *
 * Titles are matched against data/search-index.json, which already holds the
 * canonical URL for every piece of content. Items with no index entry are
 * feature announcements rather than content ("the documentation is now in
 * Telugu"), and get the section they belong to instead of a dead changelog link.
 *
 * Env (Netlify): SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, URL
 */
const SITE_URL = (process.env.URL || "https://www.impactmojo.in").replace(/\/$/, "");
const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

const WINDOW_DAYS = 35;
const MAX_ITEMS = 14;

/* ------------------------------------------------------------------ matching */

export function norm(s) {
  return String(s)
    .toLowerCase()
    .replace(/['‘’]/g, "")
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

/** Exact normalised title, then prefix, then containment. */
export function resolveEntry(title, index) {
  const t = norm(title);
  if (!t) return null;
  const exact = index.find((e) => norm(e.title) === t);
  if (exact) return exact;
  const prefix = index.find((e) => {
    const n = norm(e.title);
    return n.length > 8 && (t.startsWith(n) || n.startsWith(t));
  });
  if (prefix) return prefix;
  const contains = index.find((e) => {
    const n = norm(e.title);
    return n.length > 12 && (t.includes(n) || n.includes(t));
  });
  if (contains) return contains;
  // A changelog heading often qualifies the thing it names -- "Energy Explorer,
  // expanded" -- which no whole-string comparison matches against the index
  // title. Retry on the part before the qualifier.
  const head = String(title).split(/[,(]/)[0];
  if (norm(head) !== t && norm(head).length > 8) return resolveEntry(head, index);
  return null;
}

/* A feature announcement has no index entry of its own, so send the reader to
   the part of the site it changed rather than to a changelog. */
const TOPIC_ROUTES = [
  [/\bchallenge/i, "/challenges.html", "challenge"],
  [/\bdocumentation|guides?\b|\btranslat/i, "/docs/", "other"],
  [/\bcompanion|book\b/i, "/BookSummaries/", "book-summary"],
  [/\bdeep dive/i, "/DeepDives/", "deep-dive"],
  [/\blab\b|\bstudio/i, "/Labs/", "lab"],
  [/\bgame/i, "/game-library.html", "game"],
  [/\bcourse|certificate/i, "/catalog.html", "course"],
  [/\bexplorer|dataverse|dataset/i, "/explorers.html", "showcase"],
  [/\bhandout/i, "/handouts.html", "handout"],
  [/\blong view\b|\bgallery\b|\bchart\b/i, "/the-long-view/gallery.html", "tool"],
  [/\bblog|post\b/i, "/blog.html", "blog"],
];

function routeFor(title, description) {
  const hay = `${title} ${description}`;
  for (const [re, url, kind] of TOPIC_ROUTES) if (re.test(hay)) return { url, kind };
  return { url: "/catalog.html", kind: "other" };
}

/* ------------------------------------------------------------------- shaping */

/** Trim at a sentence boundary rather than mid-word. */
export function tidy(desc, max = 260) {
  // Changelog descriptions are written as continuations of the title ("a new
  // Deep Dive on ..."), so they arrive lowercase and read oddly once the title
  // is a heading above them.
  let raw = String(desc).trim().replace(/\s+/g, " ").replace(/[.,;:\s]+$/, "");
  raw = raw.charAt(0).toUpperCase() + raw.slice(1);
  const d = raw;
  if (d.length <= max) return d + ".";
  const cut = d.slice(0, max);
  const stop = Math.max(cut.lastIndexOf(". "), cut.lastIndexOf("; "));
  if (stop > max * 0.5) return cut.slice(0, stop + 1);
  return cut.replace(/\s+\S*$/, "") + "…";
}

export const GROUPS = [
  ["book-summary", "New reading companions"],
  ["blog", "From the blog"],
  ["deep-dive", "New Deep Dives"],
  ["lab", "New labs"],
  ["showcase", "New data explorers"],
  ["tool", "New explorers and tools"],
  ["special", "Long reads"],
  ["game", "New games"],
  ["course", "New courses"],
  ["challenge", "Challenges"],
  ["handout", "New handouts"],
  ["other", "Also new"],
];

export function groupItems(items) {
  const known = new Set(GROUPS.map(([k]) => k));
  const byKind = new Map();
  for (const it of items) {
    const k = known.has(it.kind) ? it.kind : "other";
    if (!byKind.has(k)) byKind.set(k, []);
    byKind.get(k).push(it);
  }
  return GROUPS.filter(([k]) => byKind.get(k) && byKind.get(k).length)
    .map(([k, label]) => ({ kind: k, label, items: byKind.get(k) }));
}

/* ------------------------------------------------------------------ changelog */

export function parseChangelog(text, now = new Date()) {
  const cutoff = new Date(now);
  cutoff.setDate(cutoff.getDate() - WINDOW_DAYS);

  const out = [];
  let currentDate = null;
  let inSection = false;

  for (const line of text.split("\n")) {
    const version = line.match(/^## .+?[—–-]\s*(.+)$/);
    if (version) {
      const dateStr = version[1].trim().replace(/\s*\(.*\)\s*$/, "");
      const parsed = new Date(dateStr);
      currentDate = isNaN(parsed.getTime()) ? null : parsed;
      inSection = false;
      continue;
    }
    if (/^### For Learners\b/i.test(line)) { inSection = true; continue; }
    if (/^### /.test(line)) { inSection = false; continue; }

    if (inSection && currentDate && currentDate >= cutoff) {
      const m = line.match(/^-\s+\*\*(.+?)\*\*\s*[—–-]\s*(.+)/);
      if (m) out.push({ title: m[1].replace(/[`*]/g, "").trim(), description: m[2].replace(/[`*]/g, "").trim() });
    }
  }
  return out;
}

/* Even a curated section can pick up infrastructure language; strip it rather
   than ship it to a learner. */
const BLOCK = /\b(Formspree|drip|streak[ -]?tracking|RLS|Edge Function|migration|SUPABASE|cron|webhook|infrastructure|Netlify Function|API key|service.role|localStorage|endpoint)\b/i;

/** Index titles sometimes carry a full explanatory clause; a heading needs the name. */
export function shortTitle(t) {
  let s = String(t).replace(/\s*[—–-]\s*$/, "").trim();
  if (s.length <= 72) return s;
  const dash = s.search(/\s[—–]\s/);
  if (dash > 12 && dash <= 72) return s.slice(0, dash).trim();
  return s.slice(0, 69).replace(/\s+\S*$/, "") + "…";
}

export function buildItems(highlights, index) {
  const seen = new Set();
  const items = [];
  for (const h of highlights) {
    if (BLOCK.test(`${h.title} ${h.description}`)) continue;
    const entry = resolveEntry(h.title, index);
    const routed = entry ? { url: entry.url, kind: (entry.type || "other").toLowerCase() } : routeFor(h.title, h.description);
    // Two changelog lines can name the same page ("Energy Explorer" and
    // "Energy Explorer, expanded"); keep the first and drop the repeat.
    if (seen.has(routed.url)) continue;
    seen.add(routed.url);
    items.push({
      title: shortTitle(h.title),
      description: tidy(h.description),
      url: routed.url,
      kind: routed.kind,
      resolved: Boolean(entry),
    });
    if (items.length >= MAX_ITEMS) break;
  }
  return items;
}

/* ---------------------------------------------------------------------- email */

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

/**
 * The body is composed here rather than in the Supabase function so the whole
 * design lives in one file that can be rendered and reviewed before it ships.
 * Table-based layout and inline styles, because Outlook ignores most else.
 */
export function composeBody(name, lede, sections, counts) {
  const sectionHtml = sections.map((sec) => {
    const rows = sec.items.map((it) => `
      <tr><td style="padding:0 0 18px">
        <a href="${SITE_URL}${it.url}" style="color:#075985;text-decoration:none;font-family:Inter,Helvetica,Arial,sans-serif;font-weight:700;font-size:16px;line-height:1.35">${esc(it.title)}</a>
        <div style="color:#475569;font-size:14.5px;line-height:1.6;margin-top:5px">${esc(it.description)}</div>
      </td></tr>`).join("");
    return `
      <tr><td style="padding:26px 0 10px">
        <span style="font-family:Inter,Helvetica,Arial,sans-serif;font-size:11px;font-weight:700;letter-spacing:0.09em;text-transform:uppercase;color:#B45309">${esc(sec.label)}</span>
        <div style="height:2px;background:#FDE68A;margin-top:7px;width:44px"></div>
      </td></tr>
      <tr><td><table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:14px">${rows}</table></td></tr>`;
  }).join("");

  const tally = [
    counts.courses && `${counts.courses} courses`,
    counts["reading-companions"] && `${counts["reading-companions"]} reading companions`,
    counts.labs && `${counts.labs} labs`,
    counts.games && `${counts.games} games`,
  ].filter(Boolean).join(" &middot; ");

  return `<p style="margin:0 0 16px">Hi ${esc(name)},</p>
<p style="margin:0 0 4px;font-size:15.5px;line-height:1.65">${lede}</p>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0">${sectionHtml}</table>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-top:30px">
  <tr><td style="background:#F8FAFC;border-left:3px solid #F59E0B;padding:14px 18px">
    <div style="font-family:Inter,Helvetica,Arial,sans-serif;font-size:13px;color:#475569;line-height:1.6">
      Everything above is free to read, with no account needed.<br><span style="color:#94A3B8">${tally}</span>
    </div>
  </td></tr>
</table>`;
}

/** Name the best thing in the issue instead of the month. */
export function buildSubject(items, month) {
  const lead = items.find((i) => i.resolved) || items[0];
  if (!lead) return `What's new on ImpactMojo — ${month}`;
  const t = lead.title.length > 58 ? lead.title.slice(0, 55).replace(/\s+\S*$/, "") + "…" : lead.title;
  return items.length > 1 ? `${t} — and ${items.length - 1} more from ImpactMojo` : t;
}

function monthName(d = new Date()) {
  return d.toLocaleString("en-IN", { month: "long", year: "numeric" });
}

/* ------------------------------------------------------------------- handler */

async function getJson(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`${url} -> ${r.status}`);
  return r.json();
}

export default async () => {
  if (!SERVICE_KEY) {
    console.log("[newsletter] SUPABASE_SERVICE_ROLE_KEY not set — skipping");
    return new Response(JSON.stringify({ error: "Missing service key" }), { status: 500 });
  }

  const month = monthName();
  let index = [], counts = {}, changelog = "";
  try {
    [index, counts, changelog] = await Promise.all([
      getJson(`${SITE_URL}/data/search-index.json`),
      getJson(`${SITE_URL}/data/counts.json`),
      fetch(`${SITE_URL}/docs/changelog.md`).then((r) => (r.ok ? r.text() : "")),
    ]);
  } catch (e) {
    console.log("[newsletter] source fetch failed:", e.message);
  }

  const items = buildItems(parseChangelog(changelog), index);
  if (!items.length) {
    // Better to send nothing than to send the generic filler the previous
    // version fell back to; a quiet month is not worth an email.
    console.log("[newsletter] nothing new in the window — not sending");
    return new Response(JSON.stringify({ message: "No new items; newsletter skipped" }), {
      headers: { "Content-Type": "application/json" },
    });
  }

  const sections = groupItems(items);
  const lede = sections.length > 1
    ? `${items.length} new things went up on ImpactMojo this month, across ${sections.length} kinds of work. Everything is linked below.`
    : `${items.length} new ${items.length === 1 ? "thing" : "things"} went up on ImpactMojo this month.`;

  const subject = buildSubject(items, month);

  try {
    const resp = await fetch(`${SUPABASE_URL}/functions/v1/send-notification/monthly-update`, {
      method: "POST",
      headers: { Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        subject,
        // body_html is honoured by send-notification when present; intro and
        // highlights remain for backward compatibility with older deploys.
        body_html_template: composeBody("__NAME__", lede, sections, counts),
        intro: lede,
        highlights: items.map((i) => ({ title: i.title, description: i.description, url: i.url })),
      }),
    });
    const data = await resp.json();
    console.log("[newsletter]", JSON.stringify(data));
    return new Response(JSON.stringify(data), { headers: { "Content-Type": "application/json" } });
  } catch (err) {
    console.log("[newsletter] send failed:", err.message);
    return new Response(JSON.stringify({ error: err.message }), { status: 500 });
  }
};

// 04:30 UTC on the 15th = 10:00 IST
export const config = { schedule: "30 4 15 * *" };
