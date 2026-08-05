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
  "Logframe Template": "ImpactMojo-Logframe-Template.zip",
  "Activity Budget & Costing Template": "ImpactMojo-Budget-Template.zip",
  "MEL Plan Template": "ImpactMojo-MEL-Plan-Template.docx",
  "Proposal Scoring Rubric": "ImpactMojo-Proposal-Scoring-Rubric.zip",
  "Survey Instrument Template": "ImpactMojo-Survey-Instrument-Template.docx",
  "FGD Facilitator's Guide": "ImpactMojo-FGD-Facilitator-Guide.docx",
  "Donor Report Template": "ImpactMojo-Donor-Report-Template.docx",
  "Stakeholder Mapping Template": "ImpactMojo-Stakeholder-Map-Template.zip",
  "Theory of Change Canvas": "ImpactMojo-Theory-of-Change-Canvas.docx",
  "Results Framework & Indicator Bank": "ImpactMojo-Results-Framework-Indicator-Bank.zip",
  "Data Management & Consent Pack": "ImpactMojo-Data-Management-Consent-Pack.docx",
  "Commissioning Research — Workbook": "ImpactMojo-Commissioning-Workbook.docx",
  "Introduction to MEL — Trainer Deck": "ImpactMojo-Intro-to-MEL-Deck.pptx",
  "Theory of Change — Trainer Deck": "ImpactMojo-Theory-of-Change-Trainer-Deck.pptx",
  "MEL from Scratch — 90-Day Workbook": "ImpactMojo-MEL-from-Scratch-Workbook.docx",
  "Theory of Change — Workshop Workbook": "ImpactMojo-Theory-of-Change-Workshop-Workbook.docx",
  "Survey Design Workbook": "ImpactMojo-Survey-Design-Workbook.docx",
  "Sampling & Sample Size — Refresher": "ImpactMojo-Refresher-Sampling.pdf",
  "Causal Designs — Refresher": "ImpactMojo-Refresher-Causal-Designs.pdf",
  "OECD-DAC Criteria — Refresher": "ImpactMojo-Refresher-OECD-DAC.pdf",
  "Quant vs Qual vs Mixed — Refresher": "ImpactMojo-Refresher-Quant-Qual-Mixed.pdf",
  "MEL & Statistics Formulae Poster": "ImpactMojo-Poster-MEL-Statistics-Formulae.pdf",
  "Econometrics Formulae Poster": "ImpactMojo-Poster-Econometrics-Formulae.pdf",
  "Field Data-Collection Readiness Checklist": "ImpactMojo-Checklist-Field-Readiness.pdf",
  "Ethics & DPDP Consent Checklist": "ImpactMojo-Checklist-Ethics-DPDP.pdf",
  "Proposal Review Checklist": "ImpactMojo-Checklist-Proposal-Review.pdf",
  "Evaluation & Research Costing Calculator": "ImpactMojo-Calculator-Evaluation-Costing.zip",
  "Programme Unit Economics & Pricing Calculator": "ImpactMojo-Calculator-Unit-Economics-Pricing.zip",
  "Evaluation Essentials Kit": "ImpactMojo-Evaluation-Essentials-Kit.zip",
  // Flagship Course Notes (PDF) — ₹350 each
  "Gandhi's Political Thought: Philosophy for Praxis — Course Notes": "ImpactMojo-Notes-gandhi.pdf",
  "Understanding Development: An Economics Perspective — Course Notes": "ImpactMojo-Notes-devecon.pdf",
  "Seeing Data: Visualization for Impact — Course Notes": "ImpactMojo-Notes-dataviz.pdf",
  "AI for Impact: Data Monitoring & Evaluation — Course Notes": "ImpactMojo-Notes-devai.pdf",
  "MEL for Development: Monitoring, Evaluation & Learning — Course Notes": "ImpactMojo-Notes-mel.pdf",
  "Politics of Aspiration: Rights, Insurance & Social Mobility — Course Notes": "ImpactMojo-Notes-poa.pdf",
  "Media for Development: Communication, Power & Practice — Course Notes": "ImpactMojo-Notes-media.pdf",
  "Social-Emotional Learning for Development — Course Notes": "ImpactMojo-Notes-sel.pdf",
  "Constitution & Law for Development Practice — Course Notes": "ImpactMojo-Notes-law.pdf",
  "Public Policy: Process, Design & Governance — Course Notes": "ImpactMojo-Notes-pubpol.pdf",
  "Gender Studies: Feminisms, Power & Social Change — Course Notes": "ImpactMojo-Notes-gender.pdf",
  "Public Choice: Decisions, Incentives & Institutions — Course Notes": "ImpactMojo-Notes-pubchoice.pdf",
  "Livelihoods in India: Rural, Urban & Skills — Course Notes": "ImpactMojo-Notes-livelihoods.pdf",
  "Power BI for Practitioners — Course Notes": "ImpactMojo-Notes-powerBI.pdf",
  "Causal Inference for Development — Course Notes": "ImpactMojo-Notes-causal.pdf",
  "Designing What Works: Development Interventions from Model to Scale — Course Notes": "ImpactMojo-Notes-intervention.pdf",
  "Nonviolence in Practice: NVC, NVR & Restorative Justice — Course Notes": "ImpactMojo-Notes-nvc-rj.pdf",
  "Nothing About Us Without Us: Disability, Justice & Development — Course Notes": "ImpactMojo-Notes-nothing-about-us.pdf",
  // Assessment Series — 500-MCQ question banks with answer keys (PDF)
  "MEL Assessment — 500-Question Bank": "assessments/mel-500-assessment.pdf",
  "Data & Technology Assessment — 500-Question Bank": "assessments/data-tech-500-assessment.pdf",
  "Policy & Economics Assessment — 500-Question Bank": "assessments/policy-econ-500-assessment.pdf",
  "AI for M&E Assessment — 500-Question Bank": "assessments/ai-for-me-500-assessment.pdf",
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

  // Email-first gate: a product-order with no UPI reference is a pre-payment
  // lead (the buyer entered their email before paying). It's recorded in
  // Netlify so we can reach them, but there is nothing to confirm or deliver
  // yet — skip the action email. The real "I've paid" submission carries a
  // upi_ref and flows through normally below.
  if (form === "product-order" && !upiRef) {
    return { statusCode: 200 };
  }

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
