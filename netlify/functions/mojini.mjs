// Mojini — ImpactMojo's platform assistant, now AI-backed.
//
// Public endpoint (no login): the client at js/faq-bank.js answers known
// questions instantly from its local FAQ bank, and only calls this function
// when nothing matched. We proxy to a FREE LLM (Groq → Gemini → DeepSeek,
// whichever key is configured) so the API key never touches the browser.
//
// Grounding: the system prompt carries a compact, verified snapshot of the
// platform so answers stay accurate and point to real pages. Kept intentionally
// short + on-topic; declines anything that isn't about ImpactMojo or the
// development sector.

const MAX_Q = 600;          // reject over-long questions (abuse guard)
const MAX_TOKENS = 320;     // keep replies short + costs near-zero

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
  });
}

// ---- Grounding: a compact, verified snapshot of the platform ---------------
const KNOWLEDGE = `
ImpactMojo is a free, open development-education platform for South Asia (site: www.impactmojo.in).
Almost everything is free forever, no login. Content under CC BY-NC-ND 4.0; code MIT. Contact: hello@impactmojo.in.

WHAT'S FREE (no sign-in):
- 17 flagship courses (/courses/) and 51 foundational "101" courses (/101-courses/)
- 30 labs (/Labs/) and 135 games (/game-library.html) — 18 simulations + 117 puzzles
- 105 reading companions (/BookSummaries/), 22 deep dives (/DeepDives/), 6 data dives (/DataDives/)
- Field Radio — community voice notes (/field-radio.html)
- 89 handouts (/handouts.html), 296 curated datasets in the Dataverse (/dataverse.html)
- BCT behaviour-change repository (/bct-repository.html), ImpactLex glossary (/impactlex/)
- 13 libraries hub (/libraries.html); 56-session Dojo practice programme (/dojos.html)
- Five pro tools that are FREE TO USE (Research Question Builder, ToR Builder, Qualitative Insights Lab, Code Converter, Sampling Studio) — only EXPORT + advanced modes are Premium.

FREEMIUM MODEL: "free to build, pay to export." The paywall never blocks learning or doing the work — only exporting a polished deliverable, advanced modes, the full Practice Packs, the AI Advisory Board, VaniScribe, DevData, certificates, and priority coaching.
PLANS (see /premium.html): Explorer (free) · Practitioner ₹399/mo or ₹3,990/yr · Professional ₹999/mo or ₹9,990/yr · Team (custom). Practice Packs also à la carte.

COMMUNITY (/community): WhatsApp PLC, "Research Rundown" (a Substack newsletter at varna.substack.com), Discord, Telegram. Coaching (/coaching). Peer review (/peer-review.html). Webinars are small (10 seats) — request a seat at /events.html.
ABOUT: Founded by Dr. Varna Sri Raman and Vandana Soni. Supported by PinPoint Ventures.`;

const SYSTEM = `You are Mojini, the friendly assistant for ImpactMojo, a free development-education platform for South Asia.
Answer ONLY using the facts below (plus general, well-established development-sector knowledge). Never invent courses, prices, tools, counts, or URLs that are not listed here.

${KNOWLEDGE}

RULES:
- Be warm, concise and practical — 2 to 4 sentences. No headings or long lists unless the user asks.
- When a page is relevant, point to it with its root-relative path (e.g. "/premium.html"). Only use paths listed above.
- If asked about pricing or what's free, use the plan facts exactly; don't guess numbers.
- If you don't know or it's outside ImpactMojo / the development sector, say so briefly and suggest the catalog (/catalog.html) or search — don't make things up.
- Never claim to perform actions (signing someone up, sending email). You only give information.`;

// ---- Providers (server-side keys only; pick the first free one available) --
async function callOpenAICompat({ baseURL, key, model, system, user }) {
  for (let attempt = 0; attempt < 3; attempt++) {
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
          temperature: 0.4,
          max_tokens: MAX_TOKENS,
        }),
      });
      if (r.status === 429 || r.status >= 500) { await sleep(400 * (attempt + 1)); continue; }
      if (!r.ok) return null;
      const d = await r.json();
      const t = d?.choices?.[0]?.message?.content?.trim();
      // some open models leak <think> chains; strip them
      return t ? t.replace(/<think>[\s\S]*?<\/think>/gi, "").trim() : null;
    } catch { await sleep(400 * (attempt + 1)); }
  }
  return null;
}

async function callGemini({ key, model, system, user }) {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${key}`;
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      const r = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          system_instruction: { parts: [{ text: system }] },
          contents: [{ role: "user", parts: [{ text: user }] }],
          generationConfig: { temperature: 0.4, maxOutputTokens: MAX_TOKENS },
        }),
      });
      if (r.status === 429 || r.status >= 500) { await sleep(400 * (attempt + 1)); continue; }
      if (!r.ok) return null;
      const d = await r.json();
      return d?.candidates?.[0]?.content?.parts?.map((p) => p.text).join("").trim() || null;
    } catch { await sleep(400 * (attempt + 1)); }
  }
  return null;
}

// Free-tier friendly providers, tried in order of what's configured.
async function answer(system, user) {
  if (process.env.GROQ_API_KEY) {
    const t = await callOpenAICompat({
      baseURL: "https://api.groq.com/openai/v1",
      key: process.env.GROQ_API_KEY,
      model: "llama-3.3-70b-versatile",
      system, user,
    });
    if (t) return { text: t, model: "groq/llama-3.3-70b" };
  }
  if (process.env.GEMINI_API_KEY) {
    const t = await callGemini({
      key: process.env.GEMINI_API_KEY,
      model: "gemini-2.0-flash",
      system, user,
    });
    if (t) return { text: t, model: "gemini-2.0-flash" };
  }
  if (process.env.DEEPSEEK_API_KEY) {
    const t = await callOpenAICompat({
      baseURL: "https://api.deepseek.com/v1",
      key: process.env.DEEPSEEK_API_KEY,
      model: "deepseek-chat",
      system, user,
    });
    if (t) return { text: t, model: "deepseek-chat" };
  }
  return { text: null, model: null };
}

// ---- Handler ---------------------------------------------------------------
export default async (req) => {
  if (req.method !== "POST") return json({ error: "POST only" }, 405);

  let body;
  try { body = await req.json(); } catch { return json({ error: "bad json" }, 400); }

  const question = String(body?.question || "").trim();
  const page = String(body?.page || "").slice(0, 200);
  if (!question) return json({ error: "question required" }, 400);
  if (question.length > MAX_Q) return json({ error: "That's a long one — try a shorter question." }, 400);

  const user = page
    ? `The visitor is on the page "${page}".\n\nTheir question: ${question}`
    : question;

  const { text, model } = await answer(SYSTEM, user);
  if (!text) {
    return json({
      answer: "I can't reach my assistant right now. Meanwhile, the catalog (/catalog.html) and search cover almost everything — or email hello@impactmojo.in.",
      model: null,
      degraded: true,
    });
  }
  return json({ answer: text, model });
};

export const config = { path: "/api/mojini" };
