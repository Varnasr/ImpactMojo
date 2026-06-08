/**
 * Netlify Function — sub-admin (admin reconciliation for subscriptions)
 *
 *   GET  /api/sub-admin            (header x-admin-key) -> overview JSON
 *   POST /api/sub-admin {reference}(header x-admin-key) -> mark that invoice
 *        paid, set its subscription active + last_paid=today.
 *
 * Env: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, ADMIN_KEY
 */
const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const ADMIN_KEY = process.env.ADMIN_KEY;

const j = (o, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" } });
const sb = (path, opts = {}) => fetch(`${SUPABASE_URL}/rest/v1/${path}`, {
  ...opts, headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json", ...(opts.headers || {}) },
});

export default async (req) => {
  if (!ADMIN_KEY) return j({ error: "ADMIN_KEY not configured" }, 503);
  if (!SERVICE_KEY) return j({ error: "service key missing" }, 500);
  if ((req.headers.get("x-admin-key") || new URL(req.url).searchParams.get("key") || "") !== ADMIN_KEY) return j({ error: "unauthorized" }, 401);

  if (req.method === "GET") {
    const subs = await (await sb("subscriptions?select=*&order=created_at.desc")).json();
    const inv = await (await sb("subscription_payments?status=eq.invoiced&select=*&order=created_at.desc")).json();
    return j({ subscriptions: subs, awaiting_payment: inv });
  }
  if (req.method === "POST") {
    let b; try { b = await req.json(); } catch { return j({ error: "bad json" }, 400); }
    const ref = (b.reference || "").trim();
    if (!ref) return j({ error: "reference required" }, 400);
    const today = new Date().toISOString().slice(0, 10);
    const payRes = await sb(`subscription_payments?reference=eq.${encodeURIComponent(ref)}`, { method: "PATCH", headers: { Prefer: "return=representation" }, body: JSON.stringify({ status: "paid" }) });
    const rows = await payRes.json();
    if (!rows.length) return j({ error: "reference not found" }, 404);
    await sb(`subscriptions?id=eq.${rows[0].subscription_id}`, { method: "PATCH", body: JSON.stringify({ status: "active", last_paid: today }) });
    return j({ ok: true, reference: ref, marked: "paid" });
  }
  return j({ error: "GET or POST" }, 405);
};

export const config = { path: "/api/sub-admin" };
