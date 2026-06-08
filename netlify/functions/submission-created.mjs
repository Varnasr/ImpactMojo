/**
 * Netlify event function — fires automatically on every Netlify Form submission.
 *
 * Turns each "I've paid" submission into a one-click action email to the admin:
 * you glance at your UPI app, click "Confirm & deliver", and /api/confirm does
 * the rest (emails the file / activates the subscription). UPI itself can't be
 * auto-verified, so this keeps the human "did the money arrive?" check while
 * removing all manual steps.
 *
 * Env: ADMIN_KEY, STATUS_ALERT_EMAIL, SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, URL
 */
import crypto from "node:crypto";

const SITE = (process.env.URL || "https://www.impactmojo.in").replace(/\/$/, "");
const SUPABASE_URL = (process.env.SUPABASE_URL || "https://ddyszmfffyedolkcugld.supabase.co").replace(/\/$/, "");
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const ADMIN_KEY = process.env.ADMIN_KEY || "";
const ADMIN_EMAIL = process.env.STATUS_ALERT_EMAIL || "hello@impactmojo.in";

// product title (without the " (₹…)" suffix) -> file in the private bucket
const FILES = {
  "ToR Template": "ImpactMojo-ToR-Template.docx",
  "Logframe Template": "ImpactMojo-Logframe-Template.xlsx",
  "Activity Budget & Costing Template": "ImpactMojo-Budget-Template.xlsx",
  "MEL Plan Template": "ImpactMojo-MEL-Plan-Template.docx",
  "Proposal Scoring Rubric": "ImpactMojo-Proposal-Scoring-Rubric.xlsx",
  "Survey Instrument Template": "ImpactMojo-Survey-Instrument-Template.docx",
  "FGD Facilitator's Guide": "ImpactMojo-FGD-Facilitator-Guide.docx",
  "Donor Report Template": "ImpactMojo-Donor-Report-Template.docx",
  "Stakeholder Mapping Template": "ImpactMojo-Stakeholder-Map-Template.xlsx",
  "Theory of Change Canvas": "ImpactMojo-Theory-of-Change-Canvas.docx",
  "Results Framework & Indicator Bank": "ImpactMojo-Results-Framework-Indicator-Bank.xlsx",
  "Data Management & Consent Pack": "ImpactMojo-Data-Management-Consent-Pack.docx",
  "Commissioning Research — Workbook": "ImpactMojo-Commissioning-Workbook.docx",
  "Introduction to MEL — Trainer Deck": "ImpactMojo-Intro-to-MEL-Deck.pptx",
  "Theory of Change — Trainer Deck": "ImpactMojo-Theory-of-Change-Trainer-Deck.pptx",
  "Evaluation Essentials Kit": "ImpactMojo-Evaluation-Essentials-Kit.zip",
};

const sign = (parts) => crypto.createHmac("sha256", ADMIN_KEY).update(parts.join("|")).digest("hex").slice(0, 32);

async function sendMail(to, subject, html) {
  if (!SERVICE_KEY) return;
  try {
    await fetch(`${SUPABASE_URL}/functions/v1/status-alert`, {
      method: "POST",
      headers: { Authorization: `Bearer ${SERVICE_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({ to, subject, html }),
    });
  } catch (e) { console.log("[submission] mail failed:", e.message); }
}

export const handler = async (event) => {
  let data, form;
  try { const b = JSON.parse(event.body); data = b.payload.data || {}; form = b.payload.form_name; }
  catch { return { statusCode: 200 }; }
  if (!ADMIN_KEY) { console.log("[submission] ADMIN_KEY unset"); return { statusCode: 200 }; }

  const email = (data.email || "").trim();
  const upiRef = (data.upi_ref || "").trim();

  let type, key, label;
  if (form === "product-order") {
    const title = (data.product || "").replace(/\s*\(₹.*$/, "").trim();
    const file = FILES[title];
    if (!file) { await sendMail(ADMIN_EMAIL, `Order needs manual handling: ${data.product}`, `<p>Unknown product "${data.product}" from ${email} (UPI ref ${upiRef}). Deliver manually.</p>`); return { statusCode: 200 }; }
    type = "product"; key = file; label = data.product;
  } else if (form === "subscription-payment") {
    type = "sub"; key = (data.reference || "").trim(); label = `${data.plan || "Subscription"} (${key})`;
  } else {
    return { statusCode: 200 }; // not a payment form
  }

  const sig = sign([type, email, key]);
  const url = `${SITE}/api/confirm?type=${type}&email=${encodeURIComponent(email)}&key=${encodeURIComponent(key)}&sig=${sig}`;
  const html = `<p><strong>${label}</strong></p>
    <p>From: ${email}<br>UPI reference quoted: <strong>${upiRef || "—"}</strong></p>
    <p>Check this payment landed in your UPI app, then:</p>
    <p style="margin:22px 0"><a href="${url}" style="background:#16A34A;color:#fff;text-decoration:none;padding:14px 26px;border-radius:8px;font-weight:700;font-family:Inter,Arial;font-size:15px">✓ Confirm &amp; deliver</a></p>
    <p style="font-size:12px;color:#94A3B8">Clicking ${type === "product" ? "emails the file to the buyer" : "activates the subscription"}. Ignore if the payment didn't arrive.</p>`;
  await sendMail(ADMIN_EMAIL, `Confirm payment: ${label}`, html);
  return { statusCode: 200 };
};
