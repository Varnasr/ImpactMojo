# ImpactLex Guide

## What Is ImpactLex?

ImpactLex is ImpactMojo's **searchable glossary of development terms** — acronyms, concepts, formulas, frameworks, case studies, and institutions that development professionals encounter daily.

It lives at [impactmojo.in/impactlex](https://www.impactmojo.in/impactlex/), installs as a Progressive Web App (PWA) for offline use, and draws on the same term pool as the 17 flagship ImpactMojo course lexicons — so what you learn in the MEL course shows up consistently wherever that term appears.

**Access:** Free — [Open ImpactLex](https://www.impactmojo.in/impactlex/)

---

## What ImpactLex Covers

| Category | Examples |
|----------|----------|
| **Acronyms** | DALY, WASH, NREGA, SDG, GBV, FGD, KII, ToC, MEL, BCC |
| **Concepts** | Adverse selection, moral hazard, intersectionality, Pareto efficiency, social capital |
| **Formulas** | Gini coefficient, cost-effectiveness ratio, Average Treatment Effect, HDI |
| **Frameworks** | Theory of Change, Logical Framework, Results-Based Management, GESI analysis |
| **Methods** | RCT, difference-in-differences, propensity score matching, most significant change |
| **Institutions** | World Bank, UNDP, 3ie, J-PAL, NITI Aayog, NSSO, Grameen, BRAC |
| **Case Studies** | Progresa, Graduation Approach, PROGRESA, BRAC, Janani Suraksha Yojana |

Each entry is written for practitioners, not academics. Definitions explain not just what a term means but when and why you'd use it. Examples are South Asia–grounded by default.

---

## Features

- **Instant search** across terms, acronyms, aliases, definitions
- **Category filters** — browse by acronym, concept, formula, framework, method, or institution
- **Course filters** — see only terms used in MEL, Gender, DataViz, DevAI, DevEcon, Gandhi, Law, PoA, PubPol, or SEL
- **Term of the Day** — rotating featured term to build vocabulary over time
- **Cross-references** — click a related term to jump, no re-searching
- **Bookmarks** — save favourites in your browser; syncs to your account when you log in
- **Offline access** — install as a PWA on mobile for field use without internet
- **Deep-linkable terms** — every term has its own URL (`/impactlex/term.html?id=theory-of-change`), shareable and search-indexed
- **Community contributions** — suggest new terms or corrections; reviewed before publishing

---

## Using ImpactLex

### As a workshop reference

Project ImpactLex during sessions so participants can look up unfamiliar terms in real time. Development jargon is a real barrier — having a searchable reference reduces the "I don't want to ask what that means" problem.

### As a study aid

Ask participants to learn 5–10 new terms per week. The contextual definitions help them build vocabulary that connects to their actual work, not just to textbooks.

### Alongside courses

Each ImpactMojo flagship course has its own interactive lexicon. ImpactLex is the cross-cutting view — the same term pool, filtered by course when you want that, unified when you don't. If you're studying MEL, use the course lexicon or filter ImpactLex to `MEL`. If you're writing a proposal that spans MEL + Gender + Public Policy, use ImpactLex directly.

### For report writing

When participants are writing proposals or reports, ImpactLex helps them use terminology correctly. Misusing terms like "output" vs. "outcome" or "monitoring" vs. "evaluation" is common — ImpactLex provides clear definitions with practitioner context.

---

## Contributing

Find a missing term? Spot a definition that needs fixing? Click **Suggest a term** on any ImpactLex page. Submissions go to the moderation queue and appear once reviewed.

We especially welcome:
- South Asian schemes, institutions, and acronyms that don't exist elsewhere
- Practitioner-flagged cases where donor language differs from field reality
- Formulas with worked examples
- Contested terms — if "resilience" or "empowerment" means different things to different funders, we want to explain that

---

## Under the hood

ImpactLex is a static Progressive Web App hosted on Netlify with ImpactMojo. Data lives in InstantDB; a snapshot JSON file provides the offline fallback, so the app works even when InstantDB is unreachable. Content is drafted with AI assistance (Gemini/Grok/DeepSeek) and reviewed by a human editor before publishing.

Source: `/impactlex/` in the [ImpactMojo repo](https://github.com/ImpactMojo/ImpactMojo). Legacy repo (pre-2026): [Varnasr/ImpactLex](https://github.com/Varnasr/ImpactLex).

---

## Tips

- **Install the PWA** for offline access — especially useful for field-based staff.
- **Deep-link specific terms** — every entry has a shareable URL, good for WhatsApp handoffs and workshop handouts.
- **Combine filters** — e.g., "category: method" + "course: MEL" to focus on evaluation methods only.
- **Can't find a term?** Submit it. The glossary grows from practitioner use, not desk research.
