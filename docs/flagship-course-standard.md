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
>   diagrams, formulae, capstone body) lives in
>   `supabase/seed-content/<slug>/content/mNN.html` and is bundled into a
>   migration `supabase/migrations/*_seed_<slug>_content.sql`. Editing module
>   depth means editing those seed files + re-seeding, **not** `index.html`.

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

Two distinct blocks, and the balance between them is the tell:

- **`.reflection-prompt`** — the *pedagogical* one. Dashed-cyan box, italic
  secondary text, opens with `<strong>Reflect.</strong>`. **Target: one per
  module**, closing the module.
- **`.coach-callout`** — a photo + "book a coaching session" CTA that pops in on
  scroll. Reserve for a **few** modules (≈1 in 3), not every one.

"Alternating coach prompts" = this per-module rhythm (reflect every module,
coach occasionally), **not** a left/right CSS alternation (there is none).

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

**Content depth** (per module, in the seed files)
- [ ] Substantive prose (target **≥10 KB/module**; thin courses sit near 4 KB)
- [ ] ≈1 `reflection-prompt` per module; `coach-callout` used sparingly
- [ ] ≈1–2 `worked-example` per module
- [ ] Several theme-aware SVG diagrams (or `comparison-cards`) across the course
- [ ] Formulae **iff** the subject is quantitative
- [ ] A real capstone final module (`capstone-timeline` + Deliverables)
- [ ] A companion `lexicon.html` with 40+ terms

---

## Part D — Current gap snapshot (2026-07)

Measured from the in-repo seed content.

| Component | Gold ref (intervention / causal) | intervention | nvc-rj |
|---|---|---|---|
| KB per module | ~10–12 KB | ~12 KB ✅ | **~4 KB** ✗ |
| worked-example | ~1/module | 13 ✅ | **0** ✗ |
| reflection-prompt (1/module) | 14 ✅ | 14 ✅ | **1** ✗ (over-uses coach CTA) |
| SVG diagrams (excali) | causal 72 ✅ | **0** ✗ | **0** ✗ |
| formulae (subject-gated) | causal 19 ✅ | **0** ✗ (KaTeX wired, unused) | n/a (non-quant) |
| comparison-cards | 37 | 37 ✅ | **0** ✗ |
| capstone | ✅ | ✅ | ✅ |
| hero Papers (Dropbox) btn | ✅ | "Soon" stub | **✗ absent** |
| hero AI Companion (NotebookLM) | ✅ | "Soon" stub | **✗ absent** |
| resources-cross notebooklm card | real URL | real block | **✗ repurposed to lexicon** |
| v3 blobs instantiated | ✅ | ✅ | **✗ CSS only, no markup** |
| reading-progress element | ✅ | ✅ | **✗ missing element** |

**To bring the two named courses on par**
- **NVC-RJ**: enrich modules (worked examples, 1 reflection-prompt/module, SVG
  diagrams, definitions) to ~10 KB/module; add the two hero buttons; restore the
  real NotebookLM resource card; instantiate the blob divs + progress-bar element.
  *No formulae* (non-quantitative subject).
- **Intervention**: prose is already strong — add **theme-aware SVG diagrams** and
  **formulae** (cost-effectiveness, targeting, cost-per-outcome; KaTeX is already
  wired); turn the two "Soon" hero stubs into live links once URLs exist.

**External dependencies** (needed before two components can be finished): a
**NotebookLM notebook** and a **Dropbox papers folder** for each course — neither
exists yet (verified: absent from `data/notebooklm-registry.json`, no Dropbox
folder in either hero). Create via `scripts/notebooklm-manage.py` / Dropbox, or
supply the URLs.
