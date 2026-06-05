/**
 * Netlify Function — Sarvam-backed translation proxy with persistent cache.
 *
 * The browser language switcher (js/translate-sarvam.js) POSTs a batch of
 * English strings + a target language; this function returns their
 * translations. Each unique (string, language) pair is sent to Sarvam (Mayura)
 * exactly once — thereafter it is served from a Netlify Blobs cache — so cost
 * is bounded by the number of unique strings, not by traffic.
 *
 * The SARVAM_API_KEY lives only in the Netlify environment (never shipped to
 * the browser).
 *
 * Request:  POST { "lang": "hi", "q": ["Text one", "Text two", ...] }
 * Response: { "t": { "Text one": "...", "Text two": "..." } }
 */
const SARVAM_URL = "https://api.sarvam.ai/translate";
const KEY = process.env.SARVAM_API_KEY;
const LANG = { hi: "hi-IN", ta: "ta-IN", bn: "bn-IN", mr: "mr-IN" };
const MAX_BATCH = 12;     // strings per request (keep cold calls under Netlify ~10s fn timeout)
const CONCURRENCY = 6;    // parallel Sarvam calls
const MAX_LEN = 900;      // Mayura input guard

const json = (obj, status = 200) => new Response(JSON.stringify(obj), {
  status,
  headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
});

async function sarvam(text, code) {
  for (let attempt = 0; attempt < 4; attempt++) {
    try {
      const r = await fetch(SARVAM_URL, {
        method: "POST",
        headers: { "api-subscription-key": KEY, "Content-Type": "application/json" },
        body: JSON.stringify({
          input: text.slice(0, MAX_LEN),
          source_language_code: "en-IN",
          target_language_code: code,
          model: "mayura:v1",
        }),
      });
      if (r.status === 429 || r.status >= 500) { await sleep(400 * (attempt + 1)); continue; }
      if (!r.ok) return null;
      const d = await r.json();
      return d.translated_text ?? null;
    } catch { await sleep(400 * (attempt + 1)); }
  }
  return null;
}
const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

export default async (req) => {
  if (req.method !== "POST") return json({ error: "POST only" }, 405);
  if (!KEY) return json({ error: "translation unavailable" }, 503);

  let body;
  try { body = await req.json(); } catch { return json({ error: "bad json" }, 400); }
  const { lang, q } = body || {};
  const code = LANG[lang];
  if (!code || !Array.isArray(q)) return json({ error: "lang + q[] required" }, 400);

  const items = [...new Set(q.map((s) => (s || "").trim()).filter(Boolean))].slice(0, MAX_BATCH);
  let store = null;
  try { const { getStore } = await import("@netlify/blobs"); store = getStore("translations"); }
  catch { /* Blobs unavailable — translate live without server cache */ }

  const out = {};
  const misses = [];

  // 1) cache read
  await Promise.all(items.map(async (s) => {
    if (!store) { misses.push(s); return; }
    const k = `${lang}:${s}`;
    try {
      const hit = await store.get(k);
      if (hit != null) out[s] = hit; else misses.push(s);
    } catch { misses.push(s); }
  }));

  // 2) translate misses (bounded concurrency) + cache write
  for (let i = 0; i < misses.length; i += CONCURRENCY) {
    const chunk = misses.slice(i, i + CONCURRENCY);
    await Promise.all(chunk.map(async (s) => {
      const t = await sarvam(s, code);
      const val = t || s; // fall back to original on failure
      out[s] = val;
      if (store && t) { try { await store.set(`${lang}:${s}`, val); } catch { /* ignore */ } }
    }));
  }

  return json({ t: out });
};

export const config = { path: "/api/translate" };
