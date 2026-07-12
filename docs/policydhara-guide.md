# PolicyDhara Guide

## What Is PolicyDhara?

PolicyDhara is a **curated collection of Indian public policy documents, government schemes, and legislative frameworks**, built for development practitioners and researchers. It gathers the source material of Indian policy — the schemes, laws, and frameworks that shape development work — into one browsable, **open-access** place.

PolicyDhara is **free and browser-based**. It opens directly on the page at [/policydhara](/policydhara) — no login, no download.

---

## What's in the Collection

PolicyDhara is organised around the documents practitioners actually reach for:

- **Policy documents** — the frameworks and official texts that set the direction of Indian public policy.
- **Government schemes** — the programmes through which policy is delivered on the ground.
- **Legislative frameworks** — the laws and statutory instruments that underpin it all.

Browse the collection at [/policydhara](/policydhara).

---

## How It Works

PolicyDhara is a standalone **Astro application**, built and published separately, that ImpactMojo surfaces at [/policydhara](/policydhara) so it lives under the impactmojo.in domain alongside the rest of the platform.

Behind the scenes, a **Netlify Edge Function** (`netlify/edge-functions/policydhara.ts`) proxies the PolicyDhara app onto the site. When you request `/policydhara`, the edge function fetches the upstream app and returns it in place — the pages, styling, and assets all load as if they were native to impactmojo.in. You never leave the site or see the upstream address.

---

## Why It's Served This Way

Serving PolicyDhara through the edge function keeps two things true at once:

- **One home.** The tool sits at a clean `/policydhara` URL under the main domain, so it is bookmarkable and shareable like any other ImpactMojo page.
- **Fast, fresh updates.** The proxy sets a short browser cache with stale-while-revalidate, so PolicyDhara loads quickly but still picks up upstream edits within about a minute of a new deploy — rather than waiting on the upstream host's longer cache.

Static assets (CSS, JavaScript, images) ship with content-hashed filenames, so they pass straight through with their long cache intact.

---

## Who It's For

PolicyDhara is aimed at **development practitioners and researchers** who need to ground their work in primary policy sources — anyone building a course, writing a brief, designing a programme, or checking what a scheme or framework actually says. It complements ImpactMojo's other reference tools by covering the Indian public-policy landscape specifically.

---

## Related

- [BCT Repository Guide](bct-repository-guide.md) — behaviour-change technique reference for practitioners.
- [Reading Companions Guide](book-summaries-guide.md) — interactive companions to key development texts.
- [Deep Dives Guide](deep-dives-guide.md) — long-form research explainers.
