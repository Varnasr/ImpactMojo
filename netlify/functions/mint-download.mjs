/**
 * Netlify Function — mint-download (admin)
 *
 * Fast fulfilment for the product store: given a product file name, returns a
 * short-lived Supabase signed download URL you paste into the delivery email
 * after verifying a UPI payment. Files live in the PRIVATE Supabase "products"
 * bucket — never on the public site.
 *
 * Usage (admin only):
 *   GET /.netlify/functions/mint-download?file=ImpactMojo-ToR-Template.docx
 *   Header:  x-admin-key: <ADMIN_KEY>
 *
 * Environment (Netlify):
 *   SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY  — already set
 *   ADMIN_KEY                                — a secret you choose; without it
 *                                              the endpoint refuses to run.
 */
const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const ADMIN_KEY = process.env.ADMIN_KEY;
const EXPIRES = 7 * 24 * 3600; // 7 days

export default async (req) => {
  const json = (o, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { "Content-Type": "application/json", "Cache-Control": "no-store" } });

  if (!ADMIN_KEY) return json({ error: "ADMIN_KEY not configured" }, 503);
  if (!SERVICE_KEY) return json({ error: "service key missing" }, 500);
  if ((req.headers.get("x-admin-key") || "") !== ADMIN_KEY) return json({ error: "unauthorized" }, 401);

  const file = new URL(req.url).searchParams.get("file");
  if (!file) return json({ error: "?file= required" }, 400);

  try {
    const res = await fetch(`${SUPABASE_URL}/storage/v1/object/sign/products/${encodeURIComponent(file)}`, {
      method: "POST",
      headers: { Authorization: `Bearer ${SERVICE_KEY}`, apikey: SERVICE_KEY, "Content-Type": "application/json" },
      body: JSON.stringify({ expiresIn: EXPIRES }),
    });
    if (!res.ok) return json({ error: "sign failed", status: res.status, detail: await res.text() }, 502);
    const data = await res.json();
    return json({ file, url: `${SUPABASE_URL}/storage/v1${data.signedURL}`, expires_in_days: 7 });
  } catch (e) {
    return json({ error: String(e) }, 500);
  }
};

export const config = { path: "/api/mint-download" };
