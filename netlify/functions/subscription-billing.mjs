/**
 * Netlify Scheduled Function — subscription-billing
 *
 * Runs on the 1st of each month. For every subscription that's due
 * (next_due <= today and not cancelled), it raises a fresh invoice with a new
 * UPI reference, emails the subscriber a pay link (a fresh QR each cycle), and
 * advances next_due by the plan's cadence. No payment gateway, no fees.
 *
 * Reconciliation is manual: when a payment lands, mark the latest
 * subscription_payments row status='paid' and the subscription status='active'
 * / last_paid=today (see /api/sub-admin or do it in the Supabase table editor).
 *
 * Env (Netlify): SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, URL
 */
import { payLink, emailInvoice } from "./subscribe.mjs";

const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

const sb = (path, opts = {}) => fetch(`${SUPABASE_URL}/rest/v1/${path}`, {
  ...opts,
  headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json", ...(opts.headers || {}) },
});
function addInterval(d, cadence) { const x = new Date(d); cadence === "annual" ? x.setFullYear(x.getFullYear() + 1) : x.setMonth(x.getMonth() + 1); return x.toISOString().slice(0, 10); }

export default async () => {
  if (!SERVICE_KEY) return new Response("not configured", { status: 503 });
  const today = new Date().toISOString().slice(0, 10);
  const period = today.slice(0, 7);
  const res = await sb(`subscriptions?status=neq.cancelled&next_due=lte.${today}&select=*`);
  if (!res.ok) return new Response("query failed: " + (await res.text()), { status: 502 });
  const due = await res.json();
  let billed = 0;
  for (const s of due) {
    const ref = `IMX-${(s.plan || "SUB").slice(0, 4).toUpperCase()}-${period.replace("-", "")}-${s.id.slice(0, 6).toUpperCase()}`;
    await sb("subscription_payments", { method: "POST", body: JSON.stringify({ subscription_id: s.id, period, amount: s.amount, reference: ref, status: "invoiced" }) });
    await emailInvoice(s.email, s.name, s.plan, s.amount, payLink(ref, s.amount, s.plan, period), period);
    await sb(`subscriptions?id=eq.${s.id}`, { method: "PATCH", body: JSON.stringify({ next_due: addInterval(today, s.cadence) }) });
    billed++;
  }
  console.log(`[billing] ${period}: invoiced ${billed} of ${due.length} due subscriptions`);
  return new Response(JSON.stringify({ ok: true, period, billed }), { headers: { "Content-Type": "application/json" } });
};

// 04:00 UTC on the 1st of every month
export const config = { schedule: "0 4 1 * *" };
