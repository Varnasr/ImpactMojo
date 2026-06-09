/**
 * Netlify Function — Advisory Board Pro orchestrator.
 *
 * Powers the Advisory Board Pro tool (/premium-tools/advisory-board-pro.html).
 * The browser asks for ONE advisor's contribution at a time, passing the topic
 * and the discussion-so-far; this function routes that persona's turn to its
 * assigned LLM provider and returns the contribution. The browser appends it to
 * the transcript and requests the next turn — so every call stays short (well
 * under Netlify's ~10s function budget) and the panel reveals progressively.
 *
 * Why multi-provider: each persona is voiced by a different model so the
 * "advisors" genuinely sound distinct, e.g. the Development Economist runs on
 * DeepSeek while the Behavioural Scientist runs on Grok. Provider keys live
 * ONLY in the Netlify environment.
 *
 * GATING (Professional tier):
 *   This is a paid tool with real per-call LLM cost. A client-side AuthGate
 *   hides the page, but THIS function is the authoritative guard: every request
 *   must carry the caller's Supabase access token (Authorization: Bearer …).
 *   We validate it against Supabase Auth, look up the user's profile, and only
 *   proceed if their subscription_tier is professional/organization (or they
 *   hold an explicit resource grant). A per-user daily quota bounds spend as
 *   defence in depth. Uses the SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY env
 *   vars the other functions already rely on — no new credentials needed.
 *
 * Request:  POST {
 *             topic: string,
 *             transcript: [{ name, lens, text }],
 *             advisorId: string,
 *             isOpening?: bool,        // first turn of the discussion
 *             isSynthesis?: bool,      // closing synthesis turn
 *             steer?: string           // user-injected discussion point
 *           }
 *           Header: Authorization: Bearer <supabase access_token>
 * Response: { name, lens, text, model }
 */

const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const RESOURCE_ID = "advisory-board-pro";
const ALLOWED_TIERS = ["professional", "organization"];

const json = (obj, status = 200) =>
  new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
  });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ---- Caps ---------------------------------------------------------------
const MAX_TOPIC = 600; // chars
const MAX_STEER = 300; // chars
const MAX_TRANSCRIPT = 40; // entries (≈ 8 rounds of a 5-seat panel)
const MAX_TURNS_PER_DAY = 150; // per user — ≈ 6–7 full discussions/day

// ---- The panel ----------------------------------------------------------
// provider ∈ deepseek | gemini | grok. Models kept here so they're easy to
// retune without touching the call logic below.
const PANEL = {
  moderator: {
    name: "Moderator",
    lens: "Framing & synthesis",
    provider: "gemini",
    persona:
      "You are the Moderator of a panel of development-sector experts. You are even-handed and never take a side. You frame questions sharply and, when asked to synthesise, you fairly summarise where the panel agreed, where it disagreed, and what a practitioner should weigh.",
  },
  economist: {
    name: "Development Economist",
    lens: "Cost-effectiveness & evidence",
    provider: "deepseek",
    persona:
      "You are a Development Economist. You reason from incentives, cost-effectiveness, the strength of the evidence base (RCTs, quasi-experimental work), and whether an intervention can scale affordably. You are rigorous and a little sceptical of claims that lack evidence, but you respect that evidence is incomplete.",
  },
  practitioner: {
    name: "Field Practitioner",
    lens: "Implementation reality",
    provider: "gemini",
    persona:
      "You are a Field Practitioner who has implemented programmes on the ground in South Asia. You speak to operational reality — staffing, last-mile delivery, community trust, what actually happens versus what the design assumes. You respect evidence but insist it survive contact with the field.",
  },
  behavioral: {
    name: "Behavioural Scientist",
    lens: "Take-up & behaviour",
    provider: "grok",
    persona:
      "You are a Behavioural Scientist. You focus on why people do or don't take up an intervention — friction, defaults, salience, social norms, trust — and how design choices change behaviour. You bring concrete behavioural mechanisms, not just 'add a nudge'.",
  },
  critic: {
    name: "Critic / Equity Lens",
    lens: "Power, equity, unintended consequences",
    provider: "deepseek",
    persona:
      "You are the panel's Critic, arguing from a power and equity lens. You ask who is excluded, who bears the cost, whose voice is missing, and what could go wrong. You challenge the other advisors' assumptions directly but in good faith — you are a sharp critic, not a cynic.",
  },
};

const SHARED_RULES =
  "This is a panel discussion for a development-education audience. Stay strictly on the development-sector topic at hand. Keep your contribution to 2–4 sentences: make ONE substantive point, and where natural, explicitly build on or push back against a specific advisor by name. Do not repeat what others already said. No headings, no bullet lists, no preamble like 'As the X...' — just speak. If the topic is off-topic, harmful, or not a genuine development question, briefly decline and steer back.";

// ---- Providers (server-side keys only) ----------------------------------
async function callOpenAICompat({ baseURL, key, model, system, user }) {
  for (let attempt = 0; attempt < 4; attempt++) {
    try {
      const r = await fetch(`${baseURL}/chat/completions`, {
        method: "POST",
        headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
        body: JSON.stringify({
          model,
          messages: [
            { role: "system", content: system },
            { role: "user", content: user },
          ],
          temperature: 0.8,
          max_tokens: 320,
        }),
      });
      if (r.status === 429 || r.status >= 500) { await sleep(500 * (attempt + 1)); continue; }
      if (!r.ok) return null;
      const d = await r.json();
      return d?.choices?.[0]?.message?.content?.trim() ?? null;
    } catch { await sleep(500 * (attempt + 1)); }
  }
  return null;
}

async function callGemini({ key, model, system, user }) {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${key}`;
  for (let attempt = 0; attempt < 4; attempt++) {
    try {
      const r = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          system_instruction: { parts: [{ text: system }] },
          contents: [{ role: "user", parts: [{ text: user }] }],
          generationConfig: { temperature: 0.8, maxOutputTokens: 320 },
        }),
      });
      if (r.status === 429 || r.status >= 500) { await sleep(500 * (attempt + 1)); continue; }
      if (!r.ok) return null;
      const d = await r.json();
      return d?.candidates?.[0]?.content?.parts?.map((p) => p.text).join("").trim() ?? null;
    } catch { await sleep(500 * (attempt + 1)); }
  }
  return null;
}

function runProvider(provider, system, user) {
  switch (provider) {
    case "deepseek":
      if (!process.env.DEEPSEEK_API_KEY) return Promise.resolve({ text: null, model: "deepseek" });
      return callOpenAICompat({
        baseURL: "https://api.deepseek.com/v1",
        key: process.env.DEEPSEEK_API_KEY,
        model: "deepseek-chat",
        system, user,
      }).then((t) => ({ text: t, model: "deepseek-chat" }));
    case "grok":
      if (!process.env.GROK_API_KEY) return Promise.resolve({ text: null, model: "grok" });
      return callOpenAICompat({
        baseURL: "https://api.x.ai/v1",
        key: process.env.GROK_API_KEY,
        model: "grok-3-mini",
        system, user,
      }).then((t) => ({ text: t, model: "grok-3-mini" }));
    case "gemini":
    default:
      if (!process.env.GEMINI_API_KEY) return Promise.resolve({ text: null, model: "gemini" });
      return callGemini({
        key: process.env.GEMINI_API_KEY,
        model: "gemini-2.0-flash",
        system, user,
      }).then((t) => ({ text: t, model: "gemini-2.0-flash" }));
  }
}

// ---- Supabase: verify session + Professional entitlement ----------------
async function authorize(req) {
  if (!SERVICE_KEY) return { ok: false, status: 503, error: "auth unavailable" };
  const authz = req.headers.get("authorization") || "";
  const token = authz.toLowerCase().startsWith("bearer ") ? authz.slice(7).trim() : "";
  if (!token) return { ok: false, status: 401, error: "sign in to use Advisory Board Pro" };

  // 1) Validate the access token → user id
  let uid;
  try {
    const r = await fetch(`${SUPABASE_URL}/auth/v1/user`, {
      headers: { Authorization: `Bearer ${token}`, apikey: SERVICE_KEY },
    });
    if (!r.ok) return { ok: false, status: 401, error: "session expired — sign in again" };
    const u = await r.json();
    uid = u?.id;
    if (!uid) return { ok: false, status: 401, error: "invalid session" };
  } catch {
    return { ok: false, status: 502, error: "auth check failed — try again" };
  }

  // 2) Look up tier / status / grants
  try {
    const r = await fetch(
      `${SUPABASE_URL}/rest/v1/profiles?id=eq.${uid}&select=subscription_tier,subscription_status,resource_grants`,
      { headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}` } }
    );
    const rows = r.ok ? await r.json() : [];
    const p = Array.isArray(rows) ? rows[0] : null;
    const tier = (p?.subscription_tier || "explorer").toLowerCase();
    const status = (p?.subscription_status || "").toLowerCase();
    const grants = Array.isArray(p?.resource_grants) ? p.resource_grants : [];
    const inactive = ["canceled", "cancelled", "expired", "inactive", "past_due"].includes(status);

    const tierOk = ALLOWED_TIERS.includes(tier) && !inactive;
    const grantOk = grants.includes(RESOURCE_ID);
    if (!tierOk && !grantOk) {
      return { ok: false, status: 403, error: "Advisory Board Pro requires a Professional subscription" };
    }
    return { ok: true, uid };
  } catch {
    return { ok: false, status: 502, error: "entitlement check failed — try again" };
  }
}

// ---- Per-user daily quota via Netlify Blobs -----------------------------
async function checkQuota(uid) {
  let store;
  try {
    const { getStore } = await import("@netlify/blobs");
    store = getStore("advisory-board-quota");
  } catch {
    return { ok: true }; // Blobs unavailable → don't block
  }
  const day = new Date().toISOString().slice(0, 10);
  const key = `${day}:${uid}`;
  try {
    const used = parseInt((await store.get(key)) || "0", 10);
    if (used >= MAX_TURNS_PER_DAY) return { ok: false };
    await store.set(key, String(used + 1));
    return { ok: true };
  } catch {
    return { ok: true };
  }
}

// ---- Handler ------------------------------------------------------------
export default async (req) => {
  if (req.method !== "POST") return json({ error: "POST only" }, 405);

  // Gate FIRST — never touch a paid LLM for an unauthorised caller.
  const auth = await authorize(req);
  if (!auth.ok) return json({ error: auth.error }, auth.status);

  let body;
  try { body = await req.json(); } catch { return json({ error: "bad json" }, 400); }

  const { topic, transcript, advisorId, isOpening, isSynthesis, steer } = body || {};
  const advisor = PANEL[advisorId];
  if (!advisor) return json({ error: "unknown advisor" }, 400);
  if (typeof topic !== "string" || !topic.trim()) return json({ error: "topic required" }, 400);
  if (topic.length > MAX_TOPIC) return json({ error: `topic too long (max ${MAX_TOPIC})` }, 400);
  if (!Array.isArray(transcript)) return json({ error: "transcript[] required" }, 400);
  if (transcript.length > MAX_TRANSCRIPT) return json({ error: "discussion limit reached" }, 429);
  if (steer && steer.length > MAX_STEER) return json({ error: "steer too long" }, 400);

  const quota = await checkQuota(auth.uid);
  if (!quota.ok) return json({ error: "daily limit reached — please come back tomorrow" }, 429);

  // Build the discussion context for this persona's turn.
  const history = transcript.length
    ? transcript.map((t) => `${t.name} (${t.lens}): ${t.text}`).join("\n\n")
    : "(You are opening the discussion.)";

  let task;
  if (isSynthesis) {
    task = `As the Moderator, close the panel. In 3–5 sentences, synthesise where the advisors agreed, where they disagreed, and what a practitioner should weigh when deciding. Do not introduce new arguments.`;
  } else if (isOpening) {
    task = `As the ${advisor.name}, open the panel: in 2–3 sentences frame why this is a genuine tension worth debating and name the key question the panel should resolve. Do not answer it yet.`;
  } else {
    task = `As the ${advisor.name}, give your contribution now.`;
  }

  const steerLine = steer && steer.trim()
    ? `\n\nThe user has added a point to steer the discussion — address it directly:\n"${steer.trim()}"`
    : "";

  const system = `${advisor.persona}\n\n${SHARED_RULES}`;
  const user = `TOPIC FOR THE PANEL:\n${topic.trim()}\n\nDISCUSSION SO FAR:\n${history}${steerLine}\n\n${task}`;

  const { text, model } = await runProvider(advisor.provider, system, user);
  if (!text) return json({ error: "advisor unavailable — try again" }, 502);

  return json({ name: advisor.name, lens: advisor.lens, text, model });
};

export const config = { path: "/api/advisor-panel" };
