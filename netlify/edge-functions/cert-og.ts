// Netlify Edge Function: make shared certificate links unfurl properly.
//
// /verify-certificate.html?cert=IM-XXXX is a client-rendered page, so
// LinkedIn/WhatsApp scrapers only ever saw the generic "Verify Certificate"
// meta tags. When a cert param is present, this function looks the
// certificate up (same anon-key REST query the page itself makes) and
// rewrites og:/twitter: title + description so the share card names the
// course and recipient. No param, or lookup failure → page untouched.
//
// The anon key is the same public key shipped in js/config.js; RLS already
// permits this exact read (it is how verification works client-side).

import type { Context } from "https://edge.netlify.com";

const SUPABASE_URL = "https://ddyszmfffyedolkcugld.supabase.co";
const SUPABASE_ANON_KEY =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRkeXN6bWZmZnllZG9sa2N1Z2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ3MzMxMzEsImV4cCI6MjA4MDMwOTEzMX0.vPLlFkC3pqOBtofZ8B6_FBLbRfOKwlyv3DzLvJBS16w";

// Meta-attribute values: escape everything HTML-active, collapse whitespace.
function clean(s: string): string {
  return s
    .replace(/[<>"'&]/g, (c) =>
      ({ "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;", "&": "&amp;" }[c] as string)
    )
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 200);
}

export default async (request: Request, context: Context) => {
  const url = new URL(request.url);
  const certNum = url.searchParams.get("cert");
  if (!certNum || !/^[A-Za-z0-9-]{4,64}$/.test(certNum)) return context.next();

  const headers = {
    apikey: SUPABASE_ANON_KEY,
    Authorization: `Bearer ${SUPABASE_ANON_KEY}`,
  };

  let title = "";
  let desc = "";
  try {
    const certResp = await fetch(
      `${SUPABASE_URL}/rest/v1/certificates?certificate_number=eq.${encodeURIComponent(certNum)}&select=course_name,issued_at,user_id`,
      { headers },
    );
    if (!certResp.ok) return context.next();
    const certs = await certResp.json();
    if (!Array.isArray(certs) || certs.length === 0) return context.next();
    const cert = certs[0];

    let name = "";
    try {
      const profResp = await fetch(
        `${SUPABASE_URL}/rest/v1/profiles?id=eq.${encodeURIComponent(cert.user_id)}&select=full_name,display_name`,
        { headers },
      );
      if (profResp.ok) {
        const profs = await profResp.json();
        if (Array.isArray(profs) && profs.length > 0) {
          name = profs[0].full_name || profs[0].display_name || "";
        }
      }
    } catch (_) {
      /* name is best-effort */
    }

    const issued = cert.issued_at
      ? new Date(cert.issued_at).toLocaleDateString("en-IN", {
          year: "numeric",
          month: "long",
        })
      : "";
    title = clean(
      name
        ? `${name} — Certificate: ${cert.course_name}`
        : `Certificate: ${cert.course_name}`,
    );
    desc = clean(
      `Verified ImpactMojo certificate for ${cert.course_name}` +
        (issued ? `, issued ${issued}` : "") +
        ". Free development education for South Asia.",
    );
  } catch (_) {
    return context.next();
  }

  const response = await context.next();
  const contentType = response.headers.get("content-type") || "";
  if (!contentType.includes("text/html")) return response;

  let html = await response.text();
  html = html
    .replace(
      /<meta property="og:title" content="[^"]*">/,
      `<meta property="og:title" content="${title}">`,
    )
    .replace(
      /<meta property="og:description" content="[^"]*">/,
      `<meta property="og:description" content="${desc}">`,
    )
    .replace(
      /<meta name="twitter:title" content="[^"]*">/,
      `<meta name="twitter:title" content="${title}">`,
    )
    .replace(
      /<meta name="twitter:description" content="[^"]*">/,
      `<meta name="twitter:description" content="${desc}">`,
    )
    .replace(/<title>[^<]*<\/title>/, `<title>${title} | ImpactMojo</title>`)
    .replace(
      /<meta property="og:url" content="[^"]*">/,
      `<meta property="og:url" content="https://www.impactmojo.in/verify-certificate.html?cert=${encodeURIComponent(certNum)}">`,
    );

  return new Response(html, {
    status: response.status,
    headers: response.headers,
  });
};

export const config = {
  path: ["/verify-certificate", "/verify-certificate.html"],
};
