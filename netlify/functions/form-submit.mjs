/**
 * Netlify Function — form-submit (HTTP POST /api/form-submit)
 *
 * Durable path for every consequential form on the site.
 *
 * Netlify Forms accepts a submission it classifies as spam with HTTP 200, so the
 * browser is shown success and the submission is never delivered. Six genuine
 * event registrations were lost that way -- two people each signing up for three
 * events in under a minute, where the burst rate alone was enough to trip the
 * filter. Anything whose loss actually costs something needs a second path that
 * is not behind a spam classifier.
 *
 * This writes to public.form_submissions with the service role. That table has
 * RLS on with no policies and no grants, so anon and authenticated can neither
 * read nor write it; the service role is the only writer, and it only gets here
 * after the checks below.
 *
 * Env (Netlify): SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
 */
const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

// Allowlist rather than free-form: an open endpoint writing arbitrary form_name
// values is a spam target in its own right. Forms not listed here keep using
// Netlify Forms alone, which is the right trade for low-stakes ones
// (chatbot-feedback, podcast-newsletter).
const ALLOWED_FORMS = new Set([
  "event-registration",
  "certificate-track-order",
  "product-order",
  "subscription-payment",
  "premium-subscription",
  "workshop-booking",
  "dojo-interest",
  "build-circle-waitlist",
  "partner-inquiry",
  "instructor-kit",
  "course-contribution",
  "testimonial",
  "contact",
  "contact-modal",
  "support",
  "grievance",
  "data-protection",
  "aor-petition",
]);

const MAX_FIELDS = 40;
const MAX_VALUE = 20000;
const MAX_TOTAL = 100000;
// Netlify adds these to every submission; they are noise in the stored payload.
const DROP_KEYS = new Set(["form-name", "bot-field"]);

const j = (o, s = 200) => new Response(JSON.stringify(o), {
  status: s,
  headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
});

const looksLikeEmail = (v) => typeof v === "string" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim());

export default async function handler(req) {
  if (req.method !== "POST") return j({ error: "method_not_allowed" }, 405);
  if (!SERVICE_KEY) {
    console.log("[form-submit] SUPABASE_SERVICE_ROLE_KEY missing");
    return j({ error: "not_configured" }, 500);
  }

  let body;
  try { body = await req.json(); }
  catch (e) { return j({ error: "invalid_json" }, 400); }

  const formName = typeof body.form_name === "string" ? body.form_name.trim() : "";
  if (!ALLOWED_FORMS.has(formName)) return j({ error: "unknown_form" }, 400);

  const raw = body.data && typeof body.data === "object" && !Array.isArray(body.data) ? body.data : null;
  if (!raw) return j({ error: "missing_data" }, 400);

  // The honeypot is the one signal worth acting on here: a real browser leaves it
  // empty because it is visually hidden, so a filled one is automation. Accepted
  // with a 200 rather than an error, so a bot learns nothing from the response.
  if (typeof raw["bot-field"] === "string" && raw["bot-field"].trim() !== "") {
    return j({ ok: true, id: null });
  }

  const entries = Object.entries(raw).filter(([k]) => !DROP_KEYS.has(k));
  if (entries.length === 0) return j({ error: "empty_submission" }, 400);
  if (entries.length > MAX_FIELDS) return j({ error: "too_many_fields", max: MAX_FIELDS }, 400);

  const data = {};
  let total = 0;
  for (const [k, v] of entries) {
    const key = String(k).slice(0, 120);
    const val = v == null ? "" : String(v).slice(0, MAX_VALUE);
    total += key.length + val.length;
    if (total > MAX_TOTAL) return j({ error: "payload_too_large" }, 413);
    data[key] = val;
  }

  const email = looksLikeEmail(data.email) ? data.email.trim() : null;

  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/form_submissions`, {
      method: "POST",
      headers: {
        apikey: SERVICE_KEY,
        Authorization: `Bearer ${SERVICE_KEY}`,
        "Content-Type": "application/json",
        Prefer: "return=representation",
      },
      body: JSON.stringify({ form_name: formName, data, email, source: "web" }),
      signal: AbortSignal.timeout(10000),
    });

    if (!res.ok) {
      const detail = await res.text();
      console.log("[form-submit] supabase rejected:", res.status, detail.slice(0, 400));
      return j({ error: "store_failed", status: res.status }, 502);
    }

    const saved = await res.json();
    return j({ ok: true, id: Array.isArray(saved) && saved[0] ? saved[0].id : null });
  } catch (e) {
    console.log("[form-submit] failed:", e.message);
    return j({ error: "store_failed" }, 502);
  }
}

export const config = { path: "/api/form-submit" };
