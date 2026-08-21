# Flagship Course Standard

The definitive spec for what makes a course a *flagship* on ImpactMojo. Use it to
build a new flagship or to audit an existing one for parity. Every value below is
taken from the current gold-standard flagships (`mel`, `devecon`, `gender`,
`gandhi`, `law`, `causal`, `intervention`).

> **Architecture note (read first).** A course page is a **shell**, not content.
> Each module body is an empty placeholder — `<div id="moduleN-content"
> class="module-content-placeholder">` — that `js/course-loader.js` fills at
> runtime from the Supabase `serve-course-content` edge function. This is
> deliberate anti-fork protection. So:
> - **Shell/chrome components** (design tokens, top bar, sidebar, hero, hero
>   resource buttons, `resources-cross`, KaTeX wiring, lexicon) live in
>   `courses/<slug>/index.html`.
> - **Per-module pedagogy** (prose, worked examples, coach/reflection prompts,
>   diagrams, formulae, capstone body) lives **only in the Supabase
>   `course_content` table** and is injected at runtime by `js/course-loader.js`.
>   There are no in-repo content copies or seed migrations (removed for
>   anti-fork). Editing module depth means updating the `course_content` row
>   directly in the DB (via the Management API SQL endpoint), **not**
>   `index.html` and **not** any repo file. Keep an out-of-repo backup before
>   bulk DB edits.

---

## Part A — Design system (the shell)

| Aspect | Standard | Source token |
|---|---|---|
| Content column | Centered, **900px** max-width, `3rem` padding | `--content-max-width: 900px` on `.content-wrapper` |
| Sidebar | Fixed left, **260px** | `--sidebar-width: 260px` |
| Main offset | `margin-left: var(--sidebar-width)` (must equal 260px — `gandhi` has a 280px bug) | `.main-content` |
| Body font | **Amaranth** | `--font-sans` (note: misleadingly named) |
| Heading font | **Inter** | `--font-serif` / `--font-heading` |
| Mono font | **JetBrains Mono** | `--font-mono` |
| Google Fonts link | `Amaranth:wght@400;700` + `Inter:wght@400;500;600;700;800` + `JetBrains+Mono:wght@400;500` | one `<link>` in `<head>` |
| Signature gradient | `linear-gradient(135deg, #0EA5E9 0%, #6366F1 100%)` (sky→indigo) | `--gradient-primary` |
| Accent gradient | `linear-gradient(135deg, #0EA5E9 0%, #10B981 100%)` (blue→emerald) | `--gradient-accent` |
| Theme support | Four declarations: `:root`, `@media (prefers-color-scheme: dark)`, `[data-theme="light"]`, `[data-theme="dark"]` | — |

A course **may** re-skin `--gradient-primary` / `--accent-color` to its own identity
(gender = purple/magenta, gandhi = saffron/green), but must keep the **token
names** and the **135° form** so shared components stay coherent.

### Required chrome, in `<body>` order

1. `.im-topbar#imTopbar` — the **ImpactMojo Top Bar** (logo · Browse · Premium ·
   3-button theme selector). Byte-identical across all flagships; copy verbatim.
2. `.skip-link` (visually-hidden skip-to-content).
3. `.v3-paper-plane` SVG — floating decorative plane (page-level).
4. `.v3-organic-bg` wrapper containing four `.v3-blob v3-blob-1..4` — morphing
   background blobs. **The wrapper + 4 divs must exist** (CSS alone renders
   nothing).
5. `.reading-progress#reading-progress` — the scroll progress bar. **The element
   must exist** (`id="reading-progress"`), or the JS no-ops and the bar never
   shows.
6. `.mobile-header` (hamburger + theme toggle, ≤900px) and `.sidebar-overlay`.
7. `.sidebar#sidebar` — grouped nav (`.nav-section` → `.nav-section-title` →
   `.nav-link`, `.active` state with left border), gradient logo chip, collapse
   button.
8. `.hero#hero` — badge, title, `.hero-subtitle` (≤700px), `.hero-meta`,
   `.feature-tags`, and the **hero resource button row** (Part B).
9. Module placeholder sections, then `#course-assessment`, then
   `#resources-cross`.

### Shared script bundle (end of `<body>`, verbatim)

`theme.js` · supabase-js `2.49.1` · `state-manager.js` · `config.js` · `auth.js` ·
`../../js/course-loader.js` · `../../js/course-progress.js` · `search.js` ·
`pwa.js` · `offline.js` · `../../js/auto-refresh.js` · `translate-sarvam.js` ·
GA `G-JRCMEB9TBW` · a JSON-LD `Course` schema block. Site utilities use absolute
`/js/…`; the three course scripts use relative `../../js/…`.

---

## Part B — Component catalog (what each piece looks like)

### 1. Hero resource buttons (`.hero-resource-btn`) — **4 expected**

A gold-standard hero carries four buttons, in this spirit:

1. **Course Papers Collection** → a **Dropbox folder** link (`target="_blank"`,
   `title="Most readings included. For others, email hello@impactmojo.in…"`).
2. **AI Study Companion** → a **NotebookLM** notebook link (`target="_blank"`).
3. **Interactive Lexicon** → `lexicon.html`.
4. **Excel Lexicon** → the downloadable `.xlsx` (Dropbox).

A disabled `<span class="hero-resource-btn soon">…<span class="soon-badge">Soon</span></span>`
is the honest placeholder while a real URL doesn't exist yet — but a flagship is
not "on par" until buttons 1 and 2 are live links.

### 2. Related-resources block (`#resources-cross`) — **7 cards**

Fixed structure: `.resources-eyebrow` → `.resources-h2` → `.resources-lead` →
`.resources-grid` of seven `.resource-card` in this order:

```
lab · notebooklm · course101 · book · handout · dojo · premium
```

Each card = `.resource-card-eyebrow` + `.resource-card-title` +
`.resource-card-body` + a `<ul>` of links. The `notebooklm` card **must** carry a
real `notebooklm.google.com` URL (do not repurpose it for the lexicon).

### 3. Coach & reflection prompts — the "alternating" rhythm

Two distinct blocks, one of each per module:

- **`.reflection-prompt`** — the *pedagogical* one. Dashed-cyan box, italic
  secondary text, opens with `<strong>Reflect.</strong>`. **One per module**,
  closing the module. It asks the learner a question about their own work; it
  never sells anything.
- **`.coach-callout`** — a photo + "book a coaching session" CTA. **One per
  module, alternating between the two coaches**: Vandana on odd-numbered
  modules, Varna on even-numbered ones (or the reverse — what matters is that
  consecutive modules never show the same face).

**"Alternating" means alternating coaches, module by module.** It is not a
left/right CSS alternation (there is none), and it is not "a coach every third
module". A reader working through a course meets both coaches, in turn, all the
way down.

Two failure modes, both measured across the live courses in 2026-08:

- **Stacking.** `SEL` carried 52 coach callouts across 13 modules (4.0 per
  module) and `devai` 37 across 12 (3.1). Repeating the same CTA three or four
  times inside one module trains the reader to skip it, which costs the
  conversion the block exists for.
- **Same face twice.** Alternation is what keeps the block feeling like a person
  rather than an advertisement. Two Vandanas in a row reads as a banner.

The message must be **specific to that module** — a thing this coach has seen go
wrong in this subject — not a generic invitation to book a session. A callout
whose text would work equally well in any module of any course is doing nothing
that a footer link would not do.

Markup (the `.coach-photo` path is the tell for which coach it is):

```html
<div class="coach-callout">
  <img src="https://www.impactmojo.in/assets/images/vandana-photo.jpg"
       alt="Coach Vandana" class="coach-photo" loading="lazy">
  <div class="coach-content">
    <div class="coach-name">Vandana</div>
    <div class="coach-message"><p>…module-specific counsel…</p></div>
    <div class="coach-links">
      <a href="/coaching" class="coach-link">…Book 1:1 Coaching</a>
      <a href="…" class="coach-link secondary">…a relevant Studio or course</a>
    </div>
  </div>
</div>
```

### 4. Worked examples (`.worked-example`) — **≈1–2 per module**

`.worked-example` → `.worked-example-header` (a `sargam-icon` + a "Case —" title)
→ several `<p>`, typically contrasting **Response A** vs **Response B** on the same
problem, grounded in South Asian evidence (ASER/Pratham, J-PAL, etc.).

### 5. Diagrams (Excalidraw-style) — theme-aware inline SVG

The gold model is `causal`'s `.dag-figure`: a hand-authored inline `<svg>` that
uses `stroke="currentColor"` / `fill="currentColor"` (so it recolors with the
theme), `viewBox`, `role="img"`, and a descriptive `aria-label`, wrapped with a
`.dag-caption`. Nodes are `<circle>`/`<rect>` + `<text>`; edges are `<line>` with
an arrowhead `<marker>`; dashed stroke = unobserved/hypothetical.

```html
<div class="dag-figure">
  <svg viewBox="0 0 460 150" role="img" aria-label="…" xmlns="http://www.w3.org/2000/svg"
       fill="none" stroke="currentColor"> … </svg>
  <div class="dag-caption">…</div>
</div>
```

The lighter, non-drawn alternative is a **`.comparison-cards`** grid of numbered
`.comparison-card` (step/pipeline diagrams) — used heavily in `intervention`.
A flagship should carry **several drawn figures per course**, not zero.
(An Excalidraw MCP server is available for authoring these.)

### 6. Formulae (`.equation-box`) — **subject-gated**

Only for quantitative courses (`causal`, and appropriately `intervention` for
cost-effectiveness / targeting / cost-per-outcome). Markup:

```html
<div class="equation-box">
  <div class="equation">\[ \tau_i = Y_i(1) - Y_i(0) \]</div>
  <div class="equation-caption">…what it means, in one plain sentence.</div>
</div>
```

Inline math uses `\( … \)`. Rendered by **KaTeX 0.16.11** — the shell must load
`katex.min.css` + `katex.min.js` + `auto-render.min.js` and re-typeset **after**
`course-loader.js` injects DB content. **Do not** add formulae to non-quantitative
courses (e.g. NVC/nonviolence) — a flagship earns parity through diagrams and
worked examples there, not forced LaTeX.

### 6b. Paper excerpts in popups (`js/paper-excerpt.js`)

A flagship surfaces **real, detailed excerpts from key readings** in an accessible
modal — reproduced only from **open-access / Creative-Commons / public-domain**
text (never full copyrighted paper text). The feature is a self-contained script
(`/js/paper-excerpt.js`, wired into every course shell) that injects its own modal
+ styles and uses event delegation, so it works on DB-injected module content.

Authoring convention — a trigger button plus a hidden source block, both in the
module content (the DB):

```html
<button class="excerpt-btn" data-excerpt="ex-<course>-mNN">
  <svg …></svg> Read the passage &mdash; Author (Year) &rarr;</button>
<div class="excerpt-source" id="ex-<course>-mNN" hidden>
  <div class="excerpt-kicker">Key reading &middot; Open access (LICENSE)</div>
  <h3>Title (Year)</h3>
  <div class="excerpt-cite">Authors &middot; Publisher &middot; <a href="URL" target="_blank" rel="noopener">Source &rarr;</a></div>
  <blockquote class="excerpt-quote"><p>…the open-access passage…</p></blockquote>
  <p class="excerpt-note"><strong>Why it matters.</strong> Editorial gloss + which chapters to read.</p>
</div>
```

The button's `data-excerpt` must equal the source div's `id`. Target ≈1 excerpt per
module, always license-clean and attributed with a working source link.

### 7. Capstone (final module, `.capstone-timeline`)

The last module is the capstone: intro `.lead` → `.capstone-timeline` of numbered
`.capstone-phase` (`.phase-number` + `.phase-content` with `<h5>` + `<p>`) → a
`.key-insight` → a **Deliverables** `.callout` listing concrete submissions (e.g.
a 4–6 page memo). Every flagship ends this way.

### 8. Supporting blocks (use throughout)

`.concept-box` (definitions), `.key-insight` (the one-line takeaway),
`.callout callout-blue|…` (asides), `.definition` / `.definition-term`
(inline glossary), `.table-wrapper > table` (matrices). A strong module mixes
several of these; a thin module has only prose.

### 9. Lexicon (`courses/<slug>/lexicon.html`)

A separate, self-contained page: term cards rendered from an inline JS data array,
live search + category-pill filter, `40+` authored terms each with
`term / category / definition / example`. `gandhi` (142 KB) sets the depth
ceiling. Optionally ship a downloadable `.xlsx`.

---

## Part C — Per-course parity checklist

Tick every row before calling a course a flagship.

**Shell**
- [ ] V3 `:root` token set with all four theme declarations
- [ ] 900px content column, 260px sidebar, matching main offset
- [ ] Amaranth/Inter/JetBrains fonts loaded; `--gradient-primary` at 135°
- [ ] `.im-topbar`, skip-link, `.v3-paper-plane`, `.v3-organic-bg` **with 4 blob
      divs**, `.reading-progress` **element**, mobile header, sidebar
- [ ] Full shared script bundle + JSON-LD `Course` schema
- [ ] 4 hero resource buttons (Papers, AI Companion, Lexicon, Excel) — links live
- [ ] `#resources-cross` with all 7 cards; `notebooklm` card has a real URL

**Content depth** (per module, in the `course_content` DB rows)
- [ ] Substantive prose (target **≥10 KB/module**; thin courses sit near 4 KB)
- [ ] Exactly 1 `reflection-prompt` per module, closing it
- [ ] Exactly 1 `coach-callout` per module, **alternating coaches** so no two
      consecutive modules show the same face, each message specific to its module
- [ ] ≈1–2 `worked-example` per module
- [ ] Several theme-aware SVG diagrams (or `comparison-cards`) across the course
- [ ] Formulae **iff** the subject is quantitative
- [ ] A real capstone final module (`capstone-timeline` + Deliverables)
- [ ] A companion `lexicon.html` with 40+ terms

---

## Part D — Current gap snapshot (2026-08-21)

Measured, not remembered. Regenerate with `scripts/audit-flagships.py` rather
than editing this table by hand — the 2026-07 version of Part D was a two-course
table maintained manually and it was wrong in **both** directions within a
month: it recorded `intervention` as having 0 SVG diagrams (it has 14) and
`nvc-rj` at ~4 KB/module (it is 15.4). A hand-kept conformance table decays
faster than the thing it describes.

Content is in the `course_content` DB rows, not the repo, so the audit takes the
module bodies on stdin as JSON (see the script's docstring).

`yes` = present in every module. A fraction = how many modules have it.

| Course | Modules | KB/mod | reflect | worked | excerpt | diagrams | capstone |
|---|---|---|---|---|---|---|---|
| `esg` | 13 | 21.0 | yes | yes | yes | 13 | yes |
| `nvc-rj` | 12 | 15.4 | yes | yes | yes | 12 | yes |
| `intervention` | 14 | 19.6 | yes | 26/14 | yes | 14 | yes |
| `pubchoice` | 13 | 36.3 | 0/13 | 0/13 | yes | 13 | none |
| `powerBI` | 8 | 28.6 | 0/8 | 0/8 | yes | none | none |
| `law` | 13 | 23.6 | 0/13 | 0/13 | yes | 13 | yes |
| `devecon` | 13 | 22.4 | 0/13 | 0/13 | yes | none | yes |
| `poa` | 13 | 19.8 | 0/13 | 0/13 | yes | none | yes |
| `mel` | 14 | 17.7 | 0/14 | 0/14 | yes | none | none |
| `media` | 12 | 17.3 | 0/12 | 0/12 | yes | 12 | yes |
| `gandhi` | 13 | 16.5 | 0/13 | 0/13 | yes | none | none |
| `devai` | 12 | 14.9 | 0/12 | 0/12 | yes | 12 | none |
| `dataviz` | 12 | 14.7 | 0/12 | 0/12 | yes | none | none |
| `pubpol` | 16 | 14.6 | 0/16 | 0/16 | yes | 15 | none |
| `SEL` | 13 | 14.5 | 0/13 | 0/13 | yes | 13 | none |
| `causal` | 13 | 13.9 | 0/13 | yes | yes | 7 | none |
| `social-movements` | 13 | 11.3 | 0/13 | 0/13 | yes | none | none |
| `gender` | 16 | 10.7 | 0/16 | 0/16 | yes | 16 | none |
| `livelihoods` | 17 | 9.3 | 0/17 | 0/17 | yes | 17 | none |
| `nothing-about-us` | 9 | 5.0 | 0/9 | 0/9 | 0/9 | none | none |

**Three of twenty** meet Part C in full: `esg`, `nvc-rj`, `intervention`.

### Coach callouts — done (2026-08-21)

This is the one row no longer in the table, because all 20 courses now pass it:
**exactly one coach callout per module, alternating, no two consecutive modules
showing the same face**, across all 260 modules.

Getting there was mostly *deletion*. The failure was over-use, not absence —
`SEL` carried 52 callouts across 13 modules, `devai` 37 across 12, `dataviz` 30
across 12. In total **158 surplus blocks were removed**, 20 blocks were
re-attributed to the other coach (only where the message carried no first-person
claim, so nothing is now attributed to a person who did not say it), and 9 were
newly written for modules that had none.

`pubchoice` was a separate shape: 13 callouts that named a coach in text but
showed a generic quote icon instead of a face and carried **no coaching link at
all** — the CTA the block exists for. Its shell had always styled `.coach-photo`
as a 64px circle with `object-fit: cover`, i.e. for a photograph. All 13 were
re-emitted in canonical markup with the authored messages preserved.

A backup of every module body as it stood before this work is in
`course_content_backup_20260821` (259 rows).

### What is left, in the order worth doing it

1. **`nothing-about-us`** — 5.0 KB/module and the only course with no paper
   excerpts at all. It is not a thin flagship, it is a draft. Rewrite before
   adding components to it.
2. **Reflection prompts** — absent from 17 of 20 courses. Cheapest large win:
   one closing question per module, and the standard already fixes the shape.
3. **Worked examples** — absent from 16 of 20.
4. **Capstone timeline** — absent from 13 of 20. Several of those courses do
   have a capstone module; what they lack is the `capstone-timeline` component.
5. **SVG diagrams** — none in `dataviz`, `devecon`, `gandhi`, `mel`,
   `nothing-about-us`, `poa`, `powerBI`, `social-movements`. `dataviz` having
   no diagram is the odd one.
6. **Prose depth** — `livelihoods` (9.3 KB) and `social-movements` (11.3 KB)
   sit below the 10–12 KB the standard targets.

### Shell gaps (run `scripts/audit-flagships.py --shell-only`)

Distinct from content, and the reason to check before writing: `devai`,
`gender`, `gandhi`, `social-movements` and `pubpol` carry **no CSS** for
`stats-grid`, `key-insight` or the callout colours, so standard content written
into them renders unstyled. This is exactly how the ESG build went wrong first
time — it was drafted against `social-movements`, whose shell styles none of it.

### A note on malformed div nesting

35 modules across 9 courses have unbalanced `<div>` counts — `dataviz` m6 and
`devai` m2 literally begin with a stray `</div>`. **This is inert**, and worth
recording so nobody spends a day on it: `js/course-loader.js` injects via
`placeholder.innerHTML`, and the HTML fragment parser discards unmatched end
tags and auto-closes unclosed ones at the fragment boundary. Verified in
Chromium against all three malformation shapes — content stays inside the
placeholder in every case. Untidy, not broken.

**External dependencies** (block two components everywhere): a **NotebookLM
notebook** and a **Dropbox papers folder** per course. Create via
`scripts/notebooklm-manage.py` / Dropbox, or supply the URLs.
