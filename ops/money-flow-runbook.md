# ImpactMojo — Money-Flow Runbook (internal)

> **Private/internal.** This file is **not** part of the public `/docs/` site and is
> blocked from web access via a `netlify.toml` redirect (`/ops/*` → 404). Do **not**
> put the `ADMIN_KEY` or any secret in this file — secrets live in Netlify env only.

Last updated: 2026-06-08.

## What we sell

| Type | Where | Price | Delivery |
|------|-------|-------|----------|
| 27 one-time products (templates, workbooks, decks, refreshers, posters, checklists) | `/products/<slug>/` | ₹99 / ₹149 / ₹199 / ₹499 | Signed download link emailed after payment |
| Bundle — Evaluation Essentials Kit (all 27) | `/products/evaluation-essentials-kit/` | ₹2,499 | Same |
| Premium subscriptions (Practitioner / Organisation) | `/subscribe/` | ₹399–₹9,990 | Activation + monthly UPI QR |

**Payments:** UPI to `impactmojo@ibl` · **WhatsApp:** +91 9871777110. No payment gateway (by choice — no fees).

## Where the files live (never on the public site)

- **Delivery source:** private Supabase Storage bucket **`products`** (all 27 + bundle + 2 calculators). Links are 7-day signed URLs.
- **Your master copies:** Google Drive → **"ImpactMojo — Product Masters"**.
- **Public site only holds:** watermarked samples (`/downloads/samples/`), UPI QR images (`/assets/images/upi/`), and the landing pages.
- The full files are git-ignored from the repo, so they can't leak via the website.

## The fulfilment loop (one-click)

1. Customer pays by UPI and submits the **"I've paid"** form on the product/pay page.
2. `netlify/functions/submission-created.mjs` fires and emails **you** (`STATUS_ALERT_EMAIL`) a
   **"Confirm payment"** message with the buyer's email + their UPI reference and a single
   **✓ Confirm & deliver** button (an HMAC-signed `/api/confirm` link — no secret in the URL).
3. Check the payment actually landed in your UPI app, then click the button:
   - **Product** → buyer is auto-emailed a 7-day signed download link.
   - **Subscription** → invoice marked paid, subscription set `active`, buyer emailed confirmation.

UPI has no webhook, so the one human step is confirming the money arrived; everything else is automatic.

## Subscriptions

- Tables (Supabase): `subscriptions`, `subscription_payments`.
- Signup `/subscribe/` → `/api/subscribe` inserts the subscription + first invoice and emails a pay link.
- Pay page `/subscribe/pay/` generates the cycle's UPI QR in the browser (unique reference per cycle).
- `netlify/functions/subscription-billing.mjs` runs **1st of each month (04:00 UTC)**: raises a fresh
  invoice + reference for every due subscription, emails the pay link, advances `next_due`.
- No auto-debit — subscribers renew by paying the new QR; lapsed = they just don't pay.

## Admin endpoints (fallbacks — normally you just click the email button)

All require header `x-admin-key: <ADMIN_KEY>` (or `?key=`). The key is in **Netlify env → `ADMIN_KEY`**.

| Action | Call |
|--------|------|
| List subs + awaiting payments | `GET /api/sub-admin` |
| Mark a subscription invoice paid | `POST /api/sub-admin` body `{"reference":"IMX-…"}` |
| Mint a product download link | `GET /api/mint-download?file=ImpactMojo-ToR-Template.docx` |

## Status / health (separate system)

- `/status.html` — live status page. `status-probe.mjs` (every 15 min) writes 90-day history to
  Netlify Blobs and, on a confirmed outage, opens a GitHub issue + emails via `status-alert`.

## Netlify env vars (set in dashboard — do not commit)

`ADMIN_KEY` · `STATUS_ALERT_EMAIL` · `GITHUB_TOKEN` · `SUPABASE_URL` · `SUPABASE_SERVICE_ROLE_KEY`
(`RESEND_API_KEY` lives in Supabase env, used by the `status-alert` function for all outbound email.)

## Common tasks

- **Change a price:** edit the product's `/products/<slug>/index.html` (price + the `upi-<slug>-<price>.png` QR ref) and the card on `/products.html`. Regenerate the QR if the amount changes.
- **Add a product:** add the file to the Supabase `products` bucket, add a landing page under `/products/<slug>/`, a sample + QR, a card on `/products.html`, and the title→file map in `submission-created.mjs`.
- **Refund/revoke:** signed links expire in 7 days on their own; for subscriptions set `status` back in the Supabase table editor.
