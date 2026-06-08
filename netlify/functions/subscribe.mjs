/**
 * Netlify Function — subscribe (HTTP POST /api/subscribe)
 *
 * Free, gateway-less subscriptions. Creates a subscription row + the first
 * invoice in Supabase, emails the subscriber a UPI pay link, and returns a
 * payUrl the signup page redirects to. Renewals are handled monthly by
 * subscription-billing.mjs (a fresh QR/link each cycle).
 *
 * Env (Netlify): SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, URL
 */
const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const SITE = (process.env.URL || "https://www.impactmojo.in").replace(/\/$/, "");

const j = (o, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" } });
const sb = (path, opts = {}) => fetch(`${SUPABASE_URL}/rest/v1/${path}`, {
  ...opts,
  headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json", ...(opts.headers || {}) },
});
function addInterval(d, cadence) { const x = new Date(d); cadence === "annual" ? x.setFullYear(x.getFullYear() + 1) : x.setMonth(x.getMonth() + 1); return x.toISOString().slice(0, 10); }

export const payLink = (ref, amount, plan, period) =>
  `${SITE}/subscribe/pay/?ref=${encodeURIComponent(ref)}&amt=${amount}&plan=${encodeURIComponent(plan)}${period ? `&period=${encodeURIComponent(period)}` : ""}`;

export async function emailInvoice(to, name, plan, amount, link, period) {
  if (!SERVICE_KEY) return;
  const html = `<p>Hi ${name || "there"},</p>
    <p>Thanks for subscribing to <strong>ImpactMojo ${plan}</strong>${period ? ` — ${period}` : ""}.</p>
    <p>Please complete your payment of <strong>₹${amount}</strong> by UPI:</p>
    <p style="margin:20px 0"><a href="${link}" style="background:#0369A1;color:#fff;text-decoration:none;padding:12px 22px;border-radius:8px;font-weight:700;font-family:Inter,Arial">Pay ₹${amount} by UPI →</a></p>
    <p>Scan the QR on that page, or pay to <strong>impactmojo@ibl</strong> and add the reference shown. We activate within 24 hours of payment.</p>`;
  try {
    await fetch(`${SUPABASE_URL}/functions/v1/status-alert`, {
      method: "POST",
      headers: { Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({ to, subject: `Your ImpactMojo ${plan} subscription — pay ₹${amount}`, html }),
      signal: AbortSignal.timeout(8000),
    });
  } catch (e) { console.log("[subscribe] email failed:", e.message); }
}

export default async (req) => {
  if (req.method !== "POST") return j({ error: "POST only" }, 405);
  if (!SERVICE_KEY) return j({ error: "not configured" }, 503);
  let b; try { b = await req.json(); } catch { return j({ error: "bad json" }, 400); }
  const name = (b.name || "").trim(), email = (b.email || "").trim();
  const plan = (b.plan || "").trim(), cadence = b.cadence === "annual" ? "annual" : "monthly";
  const amount = parseInt(b.amount, 10);
  if (!email || !plan || !amount) return j({ error: "name, email, plan, amount required" }, 400);

  const today = new Date().toISOString().slice(0, 10);
  const period = today.slice(0, 7);
  try {
    const res = await sb("subscriptions", {
      method: "POST", headers: { Prefer: "return=representation" },
      body: JSON.stringify({ name, email, plan, cadence, amount, status: "pending", next_due: addInterval(today, cadence) }),
    });
    if (!res.ok) return j({ error: "insert failed", detail: await res.text() }, 502);
    const row = (await res.json())[0];
    const ref = `IMX-${plan.slice(0, 4).toUpperCase()}-${period.replace("-", "")}-${row.id.slice(0, 6).toUpperCase()}`;
    await sb("subscription_payments", { method: "POST", body: JSON.stringify({ subscription_id: row.id, period, amount, reference: ref, status: "invoiced" }) });
    const link = payLink(ref, amount, plan, period);
    await emailInvoice(email, name, plan, amount, link, period);
    return j({ ok: true, payUrl: link });
  } catch (e) {
    return j({ error: String(e) }, 500);
  }
};

export const config = { path: "/api/subscribe" };
