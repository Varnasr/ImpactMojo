# Flagship Course — Master Specification

The single source of truth for what a flagship course **is** on ImpactMojo, across
five dimensions: **Tech template · Design · Content · Assessments · Marketing.**
A course is "flagship-grade" only when it passes the audit checklist in Part F.
This supersedes `flagship-course-standard.md` (kept as the short design-only
version); when the two disagree, this document wins.

> **How to use.** (1) Build/audit against Parts A–E. (2) Score each course in the
> Part F matrix. (3) Fix in priority order. Every value below is taken from the
> current gold-standard flagships (`mel`, `devecon`, `gandhi`, `causal`,
> `intervention`).

---

## Part A — Tech template / architecture

**A1. Shell + DB content (anti-fork).** A course is two files plus database rows:
- `courses/<slug>/index.html` — the **shell**: chrome + empty module placeholders
  `<section id="moduleN"><div id="moduleN-content" class="module-content-placeholder"></div></section>`. No teaching content.
- `courses/<slug>/lexicon.html` — the glossary (self-contained).
- **`course_content` table** (Supabase) — one row per module:
  `course_id, module_number, module_title, module_intro, content_html, quiz_html, is_preview, created_at, updated_at`.
  Served at runtime by `js/course-loader.js` → `serve-course-content` edge function,
  injected into the placeholders. Content lives **only in the DB** (fork-safe).

**A2. Course-id casing.** DB `course_id` is the URL slug except `sel→SEL`,
`powerbi→powerBI` (see `COURSE_ID_MAP` in `course-loader.js`). Match it exactly for
any DB write.

**A3. Module gating.** Module 1 is `is_preview = true` (open); modules 2+ are gated
behind sign-in. Anything a reviewer must see logged-out goes in module 1 or the shell.

**A4. Shared script bundle** (end of `<body>`, verbatim, in this order):
`theme.js` · supabase-js `2.49.1` · `state-manager.js` · `config.js` · `auth.js` ·
`../../js/course-loader.js` · `../../js/course-progress.js` · `js/search.js` ·
`js/pwa.js` · `js/offline.js` · `../../js/auto-refresh.js` · `js/translate-sarvam.js` ·
`js/paper-excerpt.js` · GA `G-JRCMEB9TBW`. Site utils use absolute `/js/…`; the three
course scripts use relative `../../js/…`.

**A5. Optional per-subject libraries.** KaTeX `0.16.11` (CSS+JS+auto-render) — load
**only** for quantitative courses that use formulae; re-typeset after content injects.

**A6. Head requirements.** Pre-paint theme-unify script; `manifest.json` + PWA metas;
Google Fonts preconnect + link; SEO meta (Part E); one JSON-LD `Course` schema block.

---

## Part B — Design system

**B1. Layout.** Content column centred, `--content-max-width: 900px`, `3rem` padding;
`--sidebar-width: 260px`; `.main-content{margin-left:var(--sidebar-width)}` (must equal
260px). Breakpoints at 900px (sidebar → drawer) and 768px (fluid headings, tables scroll).

**B2. Type.** Body **Amaranth** (`--font-sans`), headings **Inter**
(`--font-serif`/`--font-heading`), mono **JetBrains Mono**. One Google Fonts link with
those three families.

**B3. Colour + theme.** Full `:root` token set declared **four ways** (`:root`,
`@media (prefers-color-scheme:dark)`, `[data-theme="light"]`, `[data-theme="dark"]`).
Signature gradient `--gradient-primary: linear-gradient(135deg,#0EA5E9,#6366F1)`. A
course may re-skin the accent but must keep the token name + 135° form.

**B4. Required chrome, in `<body>` order.** `.im-topbar#imTopbar` · `.skip-link` ·
`.v3-paper-plane` · `.v3-organic-bg` **with four `.v3-blob` divs** · `.reading-progress`
**element (`id="reading-progress"`)** · `.mobile-header` + `.sidebar-overlay` ·
`.sidebar#sidebar` · `.hero#hero` · module sections · `#course-assessment` ·
`#resources-cross` · footer. (CSS without the markup renders nothing — both required.)

**B5. Diagram rendering standard (MANDATORY — this is where diagrams currently fail).**
Diagrams are hand-authored **theme-aware inline SVG** (`.dag-figure` + `.dag-caption`).
Rules:
- **Theme-aware:** every stroke/fill/text uses `currentColor` (or `fill="none"`). Never
  hard-code black/white/hex on content strokes or text.
- **Legibility floor:** text font-size ≥ 13 SVG user units; keep the viewBox tight so
  the natural render is close to 1:1 (a `520×200` viewBox renders ~legibly in a 700px
  column; a `900×160` one renders too small — split or stack instead).
- **No shrink-to-illegible on mobile.** The figure must NOT scale the whole SVG down to
  nothing. Required CSS:
  ```css
  .dag-figure{margin:2rem 0;overflow-x:auto;-webkit-overflow-scrolling:touch}
  .dag-figure svg{display:block;height:auto;width:100%;max-width:560px;min-width:min(100%,480px);margin:0 auto}
  .dag-caption{margin:.6rem auto 0;font-size:.85rem;color:var(--text-muted,#64748B);font-style:italic;max-width:640px}
  ```
  i.e. cap width for readability, keep a legible **min-width** and let the wrapper
  **scroll horizontally** on narrow screens rather than shrinking text away.
- **Labels stay inside their shapes.** Size each node box/circle to its text (measure:
  ~7px per char at 13u). Long labels wrap into two `<text>`/`tspan` lines or use a wider
  node — never let a label overflow its circle/rect or collide with an edge/arrow.
- **Arrowheads** via a `<marker>` with a **unique id per SVG** (`arr<course><mod><n>`).
  Dashed stroke = hypothetical/unobserved.
- **One diagram per module**, `role="img"` + descriptive `aria-label`, wrapped in
  `.dag-figure` with a one-sentence caption. **Verify every diagram rendered at 360px
  and 720px before shipping.**

**B6. Accessibility.** Must pass the repo axe audit (0 serious). Reduced-motion guard
(`@media (prefers-reduced-motion:reduce)`), 48px tap targets, contrast AA, `aria-*` on
interactive chrome, all content inside landmarks.

---

## Part C — Content components (per module unless noted)

**C1. Depth.** Substantive prose, target **≥10 KB/module** (thin courses sit ~4 KB and
fail). Intro `.section-intro > p.lead`, then `<h3>` sections.

**C2. Worked examples** — `.worked-example` with `.worked-example-header`; ≈1–2 per
module; a concrete, South-Asia-grounded case, usually contrasting two approaches.

**C3. Coach call-outs — Vandana ⇄ Varna alternation (MANDATORY, the core reflective
element).** Verified against the gold courses (devecon, SEL, devai, gandhi): **each
module carries 2–4 `coach-callout` blocks woven through the content, and they alternate
between the two coaches** — **Vandana** (`/assets/images/vandana-photo.jpg`) and **Varna**
(`/assets/images/varna-photo.jpg`). E.g. devecon m3 = Vandana → Varna; SEL m2 = Varna →
Vandana → Varna → Vandana. This alternating two-mentor voice **is** the flagship's
reflective/coaching device — it is NOT a single end-of-module box. (The
`.reflection-prompt` and standalone `.worked-example` classes used in the newer
causal/intervention/nvc-rj courses are acceptable *additions* but do **not** substitute
for the alternating coach call-outs, and a Varna-only course fails this check.) Markup:
```html
<div class="coach-callout">
  <img loading="lazy" src="https://www.impactmojo.in/assets/images/vandana-photo.jpg" alt="Coach Vandana" class="coach-photo">
  <div class="coach-content">
    <div class="coach-name">Vandana</div>
    <div class="coach-message">…a short, distinct-voice nudge tied to this module…</div>
    <div class="coach-links"><a href="/coaching" class="coach-link">Book a coaching session</a><a href="lexicon.html" class="coach-link secondary">Open the lexicon</a></div>
  </div>
</div>
```
Give the two coaches distinct voices (e.g. one more challenging, one more supportive);
keep them consistent within a course.

**C4. Reflection prompts (optional).** A single `.reflection-prompt` closing a module
(`<strong>Reflect.</strong> …`) is a fine *addition* used by the newer courses, but it
is **not** the standard and does not replace C3's alternating coach call-outs. Prefer C3.

**C5. Diagrams** — one per module, per the Part B5 standard.

**C6. Formulae** — `.equation-box > .equation (\[…\]) + .equation-caption`, rendered by
KaTeX. **Subject-gated**: quantitative courses only (causal, intervention, MEL,
public-choice-ish). Never force LaTeX into a non-quantitative course.

**C7. Paper excerpts (open-access popups)** — one per module. `.excerpt-btn[data-excerpt]`
trigger + hidden `.excerpt-source` block in the module content; opened by
`js/paper-excerpt.js`. **Open-access / CC / public-domain text ONLY**, verified against a
real source with a working URL — never fabricated. (See `flagship-course-standard.md §6b`
for the markup.)

**C8. Supporting blocks** — `.concept-box`, `.definition`/`.definition-term`,
`.key-insight`, `.callout callout-blue|amber|purple|green`, `.comparison-cards`,
`.table-wrapper > table`, `blockquote > cite`. A strong module mixes several.

**C9. Capstone** — final module: intro `.lead` → `.capstone-timeline` (numbered
`.capstone-phase`) → `.key-insight` → **Deliverables** `.callout`.

**C10. Lexicon** — `courses/<slug>/lexicon.html`: 40+ terms rendered from an inline JS
array, live search + category filter, each term `term/category/definition/example`.

---

## Part D — Assessments

**D1. "Assess Yourself"** — a `#course-assessment .quiz-section` in the **shell** with 6
auto-graded MCQs (`.quiz-question`, `data-correct`, `checkAnswer()`), covering the course.

**D2. Per-module quizzes** — optional `quiz_html` per module row, appended after content.

**D3. Capstone project** — the final module's deliverables (memo/plan/artefact) — the
applied assessment.

**D4. Certificates / badges** — completion drives certificates (`certificate_trigger`
migration) and Open Badges (`js/open-badges.js`, `open_badges` migration). A flagship
must be certificate-eligible (all modules present, quiz working).

---

## Part E — Marketing / growth / discoverability

**E1. SEO meta.** `<title>` (course name + hook), `meta description`, `canonical`,
`robots`, Open Graph (type/title/description/url/image/site_name), Twitter card. Counts
in copy must be **accurate and consistent** (a recurring bug — audit them).

**E2. Structured data.** One JSON-LD `Course` schema block (provider = ImpactMojo).

**E3. Hero resource buttons — 4 expected.** Course Papers (Dropbox folder), AI Study
Companion (NotebookLM), Interactive Lexicon (`lexicon.html`), Excel Lexicon (Dropbox
`.xlsx`). Honest `.hero-resource-btn.soon` stub allowed until a real URL exists, but a
course isn't "on par" until Papers + AI Companion are live.

**E4. Connected Resources block** — `#resources-cross` with 7 `.resource-card`s in order
`lab · notebooklm · course101 · book · handout · dojo · premium`, each with real,
course-relevant links. The `notebooklm` card carries a real NotebookLM URL.

**E5. Cross-linking** — into `/Labs/`, `/101-courses/`, `/BookSummaries/`,
`/handouts.html`, `/dojos.html`, `/premium.html`, and sibling flagships.

**E6. Platform registration.** Entry in `data/search-index.json`, `catalog_data.json` /
`catalog.html`, and a `<url>` in `sitemap.xml`. Learner-facing additions get a
`### For Learners` changelog bullet (parsed by the monthly newsletter).

**E7. Flagships landing card** (`courses/index.html`) — `.course-card[data-track]` with
badge, track (colour-coded), title, description, accurate `.card-meta` counts, a
`.card-outline-list` matching the real module list, `.card-cta`, and a `.card-lexicon`
link. Track accent colours: economics=indigo, mel=cyan, gender=pink, law=amber,
communication=teal, philosophy=violet, practice=emerald.

---

## Part F — Audit checklist (score every course)

For each of the 17 courses, mark ✓/✗/partial:

**Tech** — [ ] DB rows for all modules · [ ] correct course-id casing · [ ] module 1
preview · [ ] full script bundle · [ ] JSON-LD · [ ] KaTeX iff quantitative

**Design** — [ ] V3 tokens + 4-way theme · [ ] 900/260 layout · [ ] fonts + 135°
gradient · [ ] all chrome incl. blob divs + reading-progress element · [ ] **diagrams
pass B5 (legible at 360px & 720px, labels inside shapes)** · [ ] axe 0-serious

**Content** — [ ] ≥10 KB/module · [ ] 1–2 worked examples/module · [ ] **coach
call-outs alternate Vandana/Varna** · [ ] 1 reflection prompt/module · [ ] 1 diagram/module
· [ ] formulae iff quantitative · [ ] 1 open-access excerpt/module · [ ] capstone ·
[ ] lexicon 40+ terms

**Assessments** — [ ] Assess-Yourself 6-MCQ quiz · [ ] capstone deliverables ·
[ ] certificate-eligible

**Marketing** — [ ] accurate/consistent counts · [ ] SEO + OG + Twitter · [ ] 4 hero
buttons · [ ] 7-card Connected Resources w/ real links · [ ] search-index + catalog +
sitemap · [ ] landing-card correct

---

## Part G — Known live gaps (2026-07, pre-audit)

- **Coach call-outs do NOT alternate** — every NVC call-out is Varna; needs Vandana⇄Varna
  (C3). Applies to any course using call-outs.
- **Diagrams fail B5** — shrink to illegible on mobile; some network-diagram labels
  overflow their nodes. Needs the B5 CSS + label fixes across shells and existing SVGs.
- **Excerpts** — only intervention m02 has one; all courses need C7.
- **Diagrams** — present in 9 courses; missing in gender, devai, pubchoice, law, SEL,
  pubpol, media, livelihoods.
- **Connected Resources / hero buttons** — added to some; audit the rest.
- **Counts** — landing page fixed; audit each course shell's internal counts.
