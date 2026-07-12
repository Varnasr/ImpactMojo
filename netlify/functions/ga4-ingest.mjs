// GA4 snapshot ingest — receives a daily GA4 report from the Apps Script bridge
// and stores it in Supabase (public.ga4_snapshot, single 'latest' row).
//
// Why this exists: the org disables downloadable service-account keys, so instead
// a Google Apps Script (running under the maintainer's own Google login, no key)
// pulls GA4 daily and POSTs the numbers here. This endpoint is guarded by a shared
// secret (GA4_INGEST_TOKEN) and writes with the Supabase service-role key, so the
// powerful key never leaves the server. The admin page then reads via /api/ga4.

const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const INGEST_TOKEN = process.env.GA4_INGEST_TOKEN;

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
  });
}

export default async (req) => {
  if (req.method !== "POST") return json({ error: "POST only" }, 405);
  if (!INGEST_TOKEN) return json({ error: "ingest not configured" }, 501);
  if (!SERVICE_KEY) return json({ error: "supabase not configured" }, 501);

  // auth: shared bearer token
  const auth = req.headers.get("authorization") || "";
  const token = auth.replace(/^Bearer\s+/i, "").trim();
  if (token !== INGEST_TOKEN) return json({ error: "unauthorized" }, 401);

  let body;
  try { body = await req.json(); } catch (e) { return json({ error: "invalid JSON" }, 400); }
  if (!body || typeof body !== "object" || !body.overview) {
    return json({ error: "expected { overview, geography }" }, 400);
  }

  const snapshot = {
    overview: body.overview || {},
    geography: Array.isArray(body.geography) ? body.geography : [],
  };

  // upsert the single 'latest' row
  const res = await fetch(`${SUPABASE_URL}/rest/v1/ga4_snapshot?on_conflict=id`, {
    method: "POST",
    headers: {
      apikey: SERVICE_KEY,
      Authorization: "Bearer " + SERVICE_KEY,
      "Content-Type": "application/json",
      Prefer: "resolution=merge-duplicates,return=minimal",
    },
    body: JSON.stringify({ id: "latest", data: snapshot, updated_at: new Date().toISOString() }),
  });
  if (!res.ok) {
    const t = await res.text();
    return json({ error: "store failed: " + t.slice(0, 200) }, 502);
  }
  return json({ ok: true, stored: Object.keys(snapshot.overview).length + " metrics, " + snapshot.geography.length + " countries" });
};

export const config = { path: "/api/ga4-ingest" };
