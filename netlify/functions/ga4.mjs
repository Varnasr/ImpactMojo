// GA4 live analytics — server-side, no per-admin sign-in.
//
// The admin dashboard can read live Google Analytics 4 data without asking each
// admin to sign in with Google, by authenticating here with a *service account*
// (its private key stays server-side, never in the browser).
//
// Setup (one time):
//   1. In Google Cloud, create a service account and download its JSON key.
//   2. In GA4 Admin → Property → Property Access Management, add the service
//      account's email as a Viewer.
//   3. In Netlify → Site settings → Environment variables, set:
//        GA4_SERVICE_ACCOUNT = <the full JSON key>  (or its base64)
//        GA4_PROPERTY_ID     = 514001382            (optional; this is the default)
//
// Until GA4_SERVICE_ACCOUNT is set, this endpoint returns {configured:false} and
// the admin page falls back to the existing one-click Google sign-in — so it's
// safe to ship before the key exists.

import crypto from "node:crypto";

const PROPERTY_ID = process.env.GA4_PROPERTY_ID || "514001382";
const TOKEN_URL = "https://oauth2.googleapis.com/token";
const SCOPE = "https://www.googleapis.com/auth/analytics.readonly";
const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

function json(obj, status = 200, cache = "no-store") {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", "Cache-Control": cache },
  });
}

// Preferred source (org has no service-account keys): a daily snapshot pushed by
// the Apps Script bridge into Supabase. Returns the stored report if present.
async function readSnapshot() {
  if (!SERVICE_KEY) return null;
  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/ga4_snapshot?id=eq.latest&select=data,updated_at`, {
      headers: { apikey: SERVICE_KEY, Authorization: "Bearer " + SERVICE_KEY },
    });
    if (!res.ok) return null;
    const rows = await res.json();
    if (Array.isArray(rows) && rows[0] && rows[0].data) {
      return { ...rows[0].data, updatedAt: rows[0].updated_at };
    }
  } catch (e) { /* fall through */ }
  return null;
}

function b64url(buf) {
  return Buffer.from(buf).toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function readServiceAccount() {
  const raw = process.env.GA4_SERVICE_ACCOUNT;
  if (!raw) return null;
  let text = raw.trim();
  // allow the key to be provided base64-encoded (avoids newline pitfalls in some UIs)
  if (!text.startsWith("{")) {
    try { text = Buffer.from(text, "base64").toString("utf8"); } catch (e) { /* fall through */ }
  }
  try {
    const sa = JSON.parse(text);
    if (sa.client_email && sa.private_key) return sa;
  } catch (e) { /* invalid */ }
  return null;
}

// Mint a Google OAuth access token from the service account (signed JWT bearer).
async function getAccessToken(sa) {
  const now = Math.floor(Date.now() / 1000);
  const header = b64url(JSON.stringify({ alg: "RS256", typ: "JWT" }));
  const claims = b64url(JSON.stringify({
    iss: sa.client_email,
    scope: SCOPE,
    aud: TOKEN_URL,
    iat: now,
    exp: now + 3600,
  }));
  const signingInput = header + "." + claims;
  const signer = crypto.createSign("RSA-SHA256");
  signer.update(signingInput);
  const signature = b64url(signer.sign(sa.private_key));
  const assertion = signingInput + "." + signature;

  const res = await fetch(TOKEN_URL, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer",
      assertion,
    }),
  });
  const data = await res.json();
  if (!res.ok || !data.access_token) {
    throw new Error("token exchange failed: " + (data.error_description || data.error || res.status));
  }
  return data.access_token;
}

async function runReport(token, body) {
  const url = `https://analyticsdata.googleapis.com/v1beta/properties/${PROPERTY_ID}:runReport`;
  const res = await fetch(url, {
    method: "POST",
    headers: { Authorization: "Bearer " + token, "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const data = await res.json();
  if (!res.ok) throw new Error("runReport failed: " + (data.error?.message || res.status));
  return data;
}

export default async (req) => {
  // 1. Preferred: the daily snapshot from the Apps Script bridge (no keys needed).
  const snap = await readSnapshot();
  if (snap && snap.overview && Object.keys(snap.overview).length) {
    return json({ configured: true, source: "snapshot", updatedAt: snap.updatedAt,
                  overview: snap.overview, geography: snap.geography || [] }, 200, "public, max-age=1800");
  }

  // 2. Optional fallback: a service account, if one is ever configured.
  const sa = readServiceAccount();
  if (!sa) return json({ configured: false, reason: "no snapshot yet and GA4_SERVICE_ACCOUNT not set" }, 200, "no-store");

  try {
    const token = await getAccessToken(sa);
    const [overview, geo] = await Promise.all([
      runReport(token, {
        dateRanges: [{ startDate: "30daysAgo", endDate: "today" }],
        metrics: [
          { name: "totalUsers" }, { name: "newUsers" }, { name: "sessions" },
          { name: "screenPageViews" }, { name: "averageSessionDuration" },
          { name: "bounceRate" }, { name: "engagedSessions" },
        ],
      }),
      runReport(token, {
        dateRanges: [{ startDate: "30daysAgo", endDate: "today" }],
        dimensions: [{ name: "country" }],
        metrics: [{ name: "totalUsers" }, { name: "sessions" }],
        orderBys: [{ metric: { metricName: "totalUsers" }, desc: true }],
        limit: 30,
      }),
    ]);

    const result = { configured: true, overview: {}, geography: [] };
    const metricNames = ["Total Users", "New Users", "Sessions", "Pageviews", "Avg Session Duration", "Bounce Rate", "Engaged Sessions"];
    if (overview.rows && overview.rows[0]) {
      overview.rows[0].metricValues.forEach((v, i) => { result.overview[metricNames[i]] = parseFloat(v.value); });
    }
    if (geo.rows) {
      result.geography = geo.rows.map((row) => ({
        country: row.dimensionValues[0].value,
        users: parseFloat(row.metricValues[0].value),
        sessions: parseFloat(row.metricValues[1].value),
      }));
    }
    // small CDN cache so repeated admin loads don't re-hit the API every time
    return json(result, 200, "public, max-age=1800");
  } catch (e) {
    return json({ configured: true, error: String(e.message || e) }, 502, "no-store");
  }
};

export const config = { path: "/api/ga4" };
