/**
 * Netlify Function — challenge-submit (HTTP POST /api/challenge-submit)
 *
 * A second, spam-filter-proof path for challenge submissions.
 *
 * Netlify Forms was the only path, and it loses work silently: Akismet
 * classified 3 of the first 5 challenge submissions as spam (all used
 * disposable-email domains), and a spam-classified submission is still accepted
 * with HTTP 200. The browser cannot tell it apart from a delivered one, so the
 * learner saw "Submitted" and nobody ever received it.
 *
 * This writes straight to Supabase with the service role, so nothing sits behind
 * a spam classifier. The Netlify Forms POST is kept alongside it -- it is what
 * sends the notification email -- but the database row is now the record of
 * truth.
 *
 * Anon is deliberately NOT granted write access to challenge_submissions; the
 * table keeps the anon-denied contract asserted by scripts/check-supabase-anon.py.
 * Writes only ever arrive here, where they can be validated first.
 *
 * Env (Netlify): SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
 */
const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

const MIN_TEXT = 200;
const MAX_TEXT = 60000;
const MAX_FIELD = 300;

const j = (o, s = 200) => new Response(JSON.stringify(o), {
  status: s,
  headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
});

const clip = (v, n = MAX_FIELD) => (typeof v === "string" ? v.trim().slice(0, n) : null);
const looksLikeEmail = (v) => typeof v === "string" && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim());

export default async function handler(req) {
  if (req.method !== "POST") return j({ error: "method_not_allowed" }, 405);
  if (!SERVICE_KEY) {
    console.log("[challenge-submit] SUPABASE_SERVICE_ROLE_KEY missing");
    return j({ error: "not_configured" }, 500);
  }

  let body;
  try { body = await req.json(); }
  catch (e) { return j({ error: "invalid_json" }, 400); }

  const challengeId = clip(body.challenge_id, 120);
  const text = typeof body.submission_text === "string" ? body.submission_text.trim() : "";
  const email = clip(body.email);
  const userId = clip(body.user_id, 64);

  if (!challengeId) return j({ error: "missing_challenge_id" }, 400);
  if (text.length < MIN_TEXT) return j({ error: "too_short", min: MIN_TEXT }, 400);
  if (text.length > MAX_TEXT) return j({ error: "too_long", max: MAX_TEXT }, 400);
  // Without an account, email is the only way to send feedback back, so it is
  // required for anonymous submissions and validated rather than trusted.
  if (!userId && !looksLikeEmail(email)) return j({ error: "email_required" }, 400);

  const row = {
    challenge_id: challengeId,
    challenge_title: clip(body.challenge_title),
    submission_text: text,
    submission_status: "pending",
    submitted_at: new Date().toISOString(),
    email: looksLikeEmail(email) ? email : null,
    attachment_name: clip(body.attachment_name),
    source: "web",
  };
  if (userId) row.user_id = userId;

  // A signed-in learner resubmitting the same challenge should replace their
  // row, which the (challenge_id, user_id) unique constraint supports. An
  // anonymous row has a NULL user_id, which never conflicts, so it inserts.
  const url = `${SUPABASE_URL}/rest/v1/challenge_submissions` +
    (userId ? "?on_conflict=challenge_id,user_id" : "");

  try {
    const res = await fetch(url, {
      method: "POST",
      headers: {
        apikey: SERVICE_KEY,
        Authorization: `Bearer ${SERVICE_KEY}`,
        "Content-Type": "application/json",
        Prefer: userId ? "resolution=merge-duplicates,return=representation" : "return=representation",
      },
      body: JSON.stringify(row),
      signal: AbortSignal.timeout(10000),
    });

    if (!res.ok) {
      const detail = await res.text();
      console.log("[challenge-submit] supabase rejected:", res.status, detail.slice(0, 400));
      return j({ error: "store_failed", status: res.status }, 502);
    }

    const saved = await res.json();
    return j({ ok: true, id: Array.isArray(saved) && saved[0] ? saved[0].id : null });
  } catch (e) {
    console.log("[challenge-submit] failed:", e.message);
    return j({ error: "store_failed" }, 502);
  }
}

export const config = { path: "/api/challenge-submit" };
