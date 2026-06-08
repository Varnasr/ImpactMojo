/**
 * Netlify Scheduled Function — Server-side Status Probe
 *
 * Runs every 15 minutes, probes every ImpactMojo component from the server
 * (no CORS limits, real HTTP status codes), and persists results to a
 * Netlify Blobs store ("status") so the public /status.html page can show a
 * TRUE cross-visitor 90-day uptime history (not just per-browser localStorage).
 *
 * It is also the alerting brain:
 *   - Flap-resistant: a component is only declared "down" after 2 consecutive
 *     failed probes (~30 min), and "recovered" after 1 clean probe.
 *   - On a confirmed outage it auto-opens a GitHub issue (which emails repo
 *     watchers) and sends an email alert via the Supabase `status-alert`
 *     function; on recovery it auto-closes the issue and sends an all-clear.
 *   - Light auto-remediation: if Supabase looks down it fires a keepalive
 *     ping (the #1 real cause is the free-tier project pausing).
 *
 * Storage keys in the "status" blob store:
 *   history → { "YYYY-MM-DD": { overall, components: {id: level} } }   (~120d)
 *   state   → { components: {id: {level, fails, since, issue}}, updatedAt }
 *
 * Optional environment variables (set in the Netlify dashboard):
 *   URL / SITE_URL              — deploy URL (Netlify sets URL automatically)
 *   SUPABASE_URL               — Supabase project URL
 *   SUPABASE_ANON_KEY          — public anon key (for the auth health probe)
 *   SUPABASE_SERVICE_ROLE_KEY  — for the Supabase auto-wake remediation
 *   GITHUB_TOKEN               — repo-scoped PAT to auto-open/close issues
 *   STATUS_ALERT_EMAIL         — where outage emails go (default below)
 *
 * Every alerting/remediation step degrades gracefully: a missing token just
 * logs a notice and skips, it never breaks the probe loop.
 */

const SITE_URL = (process.env.URL || process.env.SITE_URL || "https://www.impactmojo.in").replace(/\/$/, "");
const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SUPABASE_ANON = process.env.SUPABASE_ANON_KEY ||
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRkeXN6bWZmZnllZG9sa2N1Z2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ3MzMxMzEsImV4cCI6MjA4MDMwOTEzMX0.vPLlFkC3pqOBtofZ8B6_FBLbRfOKwlyv3DzLvJBS16w";
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const GITHUB_TOKEN = process.env.GITHUB_TOKEN || process.env.GITHUB_PAT;
const ALERT_EMAIL = process.env.STATUS_ALERT_EMAIL || "hello@impactmojo.in";
const REPO = "ImpactMojo/ImpactMojo";

const SLOW_MS = 2000;     // slower than this = degraded
const TIMEOUT_MS = 10000; // no response by this = down
const DOWN_AFTER = 2;     // consecutive fails before declaring an outage
const HISTORY_DAYS = 120; // keep ~4 months, page renders last 90

const RANK = { up: 0, degraded: 1, down: 2 };
const RANK_REV = ["up", "degraded", "down"];
const LABELS = { up: "Operational", degraded: "Degraded", down: "Down" };

const COMPONENTS = [
  { id: "home",      name: "Website",            url: SITE_URL + "/",                          type: "page" },
  { id: "catalog",   name: "Course Catalog",     url: SITE_URL + "/catalog.html",              type: "page" },
  { id: "games",     name: "Game Library",       url: SITE_URL + "/game-library.html",         type: "page" },
  { id: "handouts",  name: "Resource Library",   url: SITE_URL + "/handouts.html",             type: "page" },
  { id: "blog",      name: "Blog",               url: SITE_URL + "/blog.html",                 type: "page" },
  { id: "docs",      name: "Documentation",      url: SITE_URL + "/docs/",                     type: "page" },
  { id: "search",    name: "Search Index",       url: SITE_URL + "/data/search-index.json",    type: "json" },
  { id: "deploy",    name: "Hosting & CDN",      url: SITE_URL + "/version.json",              type: "json" },
  { id: "translate", name: "Translation Service",url: SITE_URL + "/.netlify/functions/translate", type: "fn" },
  { id: "supabase",  name: "Accounts & Backend", url: SUPABASE_URL + "/auth/v1/health",        type: "fn", headers: { apikey: SUPABASE_ANON } },
  { id: "github",    name: "Source & Content",   url: "https://api.github.com/repos/" + REPO,  type: "fn",
    headers: { "User-Agent": "impactmojo-status", ...(GITHUB_TOKEN ? { Authorization: `Bearer ${GITHUB_TOKEN}` } : {}) } },
];

const today = () => new Date().toISOString().slice(0, 10);

async function probe(c) {
  const start = Date.now();
  const headers = c.headers || {};
  try {
    let res, level;
    const opts = { headers, signal: AbortSignal.timeout(TIMEOUT_MS), redirect: "follow" };
    if (c.type === "page") {
      res = await fetch(c.url, { ...opts, method: "HEAD" });
      level = res.ok ? "up" : "down";
    } else if (c.type === "json") {
      res = await fetch(c.url, { ...opts, method: "GET" });
      if (res.ok) { await res.json(); level = "up"; } else { level = "down"; }
    } else { // fn — any non-5xx response means reachable
      res = await fetch(c.url, { ...opts, method: "GET" });
      level = res.status >= 500 ? "down" : "up";
    }
    const ms = Date.now() - start;
    if (level === "up" && ms > SLOW_MS) level = "degraded";
    return { level, ms, code: res.status };
  } catch (e) {
    return { level: "down", ms: Date.now() - start, code: e.name === "TimeoutError" ? "timeout" : "error" };
  }
}

/* ---- Light auto-remediation (only for tractable, known failure modes) ---- */
async function remediate(id) {
  if (id === "supabase" && SERVICE_KEY) {
    // The overwhelmingly common cause of a Supabase free-tier outage is the
    // project auto-pausing after inactivity. A REST + auth ping counts as
    // activity and nudges it back awake (same mechanism as supabase-keepalive).
    try {
      await fetch(`${SUPABASE_URL}/rest/v1/?select=1`, {
        headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}` },
        signal: AbortSignal.timeout(8000),
      });
      await fetch(`${SUPABASE_URL}/auth/v1/settings`, {
        headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}` },
        signal: AbortSignal.timeout(8000),
      });
      return "fired supabase keepalive (auto-wake)";
    } catch (e) {
      return "supabase auto-wake failed: " + e.message;
    }
  }
  return null;
}

/* ---- GitHub issue alerting (emails repo watchers automatically) ---- */
async function githubRequest(method, path, body) {
  if (!GITHUB_TOKEN) return null;
  const res = await fetch(`https://api.github.com${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${GITHUB_TOKEN}`,
      Accept: "application/vnd.github+json",
      "User-Agent": "impactmojo-status",
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) { console.log(`[status] GitHub ${method} ${path} -> ${res.status}`); return null; }
  return res.json();
}
async function openIssue(c, r, note) {
  const data = await githubRequest("POST", `/repos/${REPO}/issues`, {
    title: `🔴 Status: ${c.name} is down`,
    body: `Automated alert from the status monitor.\n\n` +
          `- **Component:** ${c.name} (\`${c.id}\`)\n` +
          `- **URL:** ${c.url}\n` +
          `- **Result:** ${LABELS[r.level]} (code: ${r.code}, ${r.ms} ms)\n` +
          `- **Detected:** ${new Date().toISOString()}\n` +
          (note ? `- **Auto-remediation:** ${note}\n` : "") +
          `\nThis issue will auto-close when the component recovers. ` +
          `Live status: ${SITE_URL}/status.html`,
    labels: ["status", "incident"],
  });
  return data ? data.number : null;
}
async function closeIssue(num, c) {
  if (!num) return;
  await githubRequest("POST", `/repos/${REPO}/issues/${num}/comments`, {
    body: `✅ Recovered — ${c.name} is responding normally again as of ${new Date().toISOString()}. Auto-closing.`,
  });
  await githubRequest("PATCH", `/repos/${REPO}/issues/${num}`, { state: "closed" });
}

/* ---- Email alert via the Supabase status-alert function (uses Resend) ---- */
async function sendAlertEmail(subject, html) {
  if (!SERVICE_KEY) { console.log("[status] no service key — skipping email"); return; }
  try {
    const res = await fetch(`${SUPABASE_URL}/functions/v1/status-alert`, {
      method: "POST",
      headers: { Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({ to: ALERT_EMAIL, subject, html }),
      signal: AbortSignal.timeout(8000),
    });
    console.log(`[status] alert email -> ${res.status}`);
  } catch (e) {
    console.log("[status] alert email failed:", e.message);
  }
}

export default async () => {
  const { getStore } = await import("@netlify/blobs");
  const store = getStore("status");

  const history = (await store.get("history", { type: "json" })) || {};
  const state = (await store.get("state", { type: "json" })) || { components: {} };
  const day = today();
  history[day] = history[day] || { overall: 0, components: {} };

  const results = await Promise.all(COMPONENTS.map(async (c) => ({ c, r: await probe(c) })));

  for (const { c, r } of results) {
    // roll today's worst observation per component + overall
    history[day].components[c.id] = Math.max(history[day].components[c.id] ?? 0, RANK[r.level]);
    history[day].overall = Math.max(history[day].overall, RANK[r.level]);

    const prev = state.components[c.id] || { level: "up", fails: 0, since: null, issue: null };
    const failing = r.level === "down";
    const fails = failing ? prev.fails + 1 : 0;
    const next = { level: r.level, fails, since: prev.since, issue: prev.issue, code: r.code, ms: r.ms };

    // transition: healthy -> confirmed outage
    if (failing && fails >= DOWN_AFTER && prev.level !== "down") {
      const note = await remediate(c.id);
      next.level = "down";
      next.since = new Date().toISOString();
      console.log(`[status] OUTAGE: ${c.name} (${r.code}) ${note || ""}`);
      next.issue = await openIssue(c, r, note);
      await sendAlertEmail(
        `🔴 ImpactMojo status: ${c.name} is down`,
        `<p><strong>${c.name}</strong> failed ${fails} consecutive checks (code ${r.code}, ${r.ms} ms).</strong></p>` +
        (note ? `<p>Auto-remediation: ${note}.</p>` : "") +
        `<p>Live status: <a href="${SITE_URL}/status.html">${SITE_URL}/status.html</a></p>`
      );
    } else if (failing && prev.level !== "down") {
      next.level = prev.level; // not yet confirmed — hold previous level
    }

    // transition: was down -> recovered
    if (!failing && prev.level === "down") {
      console.log(`[status] RECOVERED: ${c.name}`);
      await closeIssue(prev.issue, c);
      await sendAlertEmail(
        `✅ ImpactMojo status: ${c.name} recovered`,
        `<p><strong>${c.name}</strong> is responding normally again (code ${r.code}, ${r.ms} ms).</p>`
      );
      next.issue = null;
      next.since = null;
    }

    state.components[c.id] = next;
  }

  // prune history to HISTORY_DAYS
  const cutoff = new Date(Date.now() - HISTORY_DAYS * 864e5).toISOString().slice(0, 10);
  for (const k of Object.keys(history)) if (k < cutoff) delete history[k];

  state.updatedAt = new Date().toISOString();
  await store.setJSON("history", history);
  await store.setJSON("state", state);

  const summary = results.map(({ c, r }) => `${c.id}:${r.level}`).join(" ");
  console.log(`[status] probed ${results.length} components — ${summary}`);
  return new Response(JSON.stringify({ ok: true, updatedAt: state.updatedAt }), {
    headers: { "Content-Type": "application/json" },
  });
};

// Every 15 minutes
export const config = { schedule: "*/15 * * * *" };
