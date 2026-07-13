# Competitor Analysis — LFA Shala

**Competitor:** LFA Shala — <https://lfashala.sasocialimpact.workers.dev/>
**Analyzed:** 2026-07-13
**Analyst:** Claude Code (branch `claude/competitor-analysis-2arme2`)
**Scope:** How LFA Shala positions against ImpactMojo's MEL / Theory of Change / LogFrame offerings, what it does well, and where ImpactMojo has a genuine gap.

---

## 1. What LFA Shala is

A free, independent, single-purpose education platform by Shashidhar SA that teaches **one thing** — the **Logical Framework Approach (LFA)** — and teaches it deeply. It is deliberately narrow: no accounts, no payment, no sprawling catalog. Part of a small "Shala family" (also *SamplingShala* for statistics).

**Core value proposition:** take a practitioner from zero ("results ladders") to a complete, printable **LogFrame Matrix** through guided, self-paced, no-friction practice.

### Standout features

| # | Feature | Why it works |
|---|---------|--------------|
| 1 | **Guided 5-step LogFrame Builder** (Problem → Scale → Stakeholders → Logic → Matrix) ending in a **printable matrix** | The whole product is one focused *doing* tool, not a reading course. The user leaves with an artifact. |
| 2 | **No account, local-device progress** | Zero signup friction; privacy-friendly; works for field practitioners on shared/low-trust devices. |
| 3 | **"Learn in any order" lesson map + personalized route** | Respects that adult learners arrive with different gaps; non-linear but still guided. |
| 4 | **Basic → advanced progression** ("results ladder" → "cascading frameworks") | Clear pedagogical spine for a genuinely hard, jargon-heavy topic. |
| 5 | **Honest scope disclaimer** ("not a substitute for a qualified MEL specialist") | Builds trust; matches ImpactMojo's own disclaimer ethos. |
| 6 | **Minimalist UI, dark mode, offline-first** | Fast, distraction-free, field-appropriate. |

### Weaknesses / limits

- **Extremely narrow** — LogFrame only. No ToC, no indicators-in-depth, no data collection, no evaluation, no South Asia framing, no community, no certification.
- **Single-author, small brand** — no ecosystem, no ongoing content cadence, limited discoverability.
- **No localization** — English only; no Indic-language support.

---

## 2. Where ImpactMojo already overlaps (and wins)

ImpactMojo is **broader and deeper** across the whole MEL lifecycle. Direct comparisons:

| Capability | LFA Shala | ImpactMojo |
|------------|-----------|------------|
| Theory of Change builder | ❌ none | ✅ `toc-builder.html` + `toc-workbench.html` (interactive, save/export/print) + `Labs/toc-lab.html` |
| Full MEL framework tool | ❌ | ✅ `Labs/mel-lab.html` — MEL Framework, Indicator Development, Data Collection, Analysis & Use, **Indicator Matrix**, MEL Calendar & Budget, Reporting & Learning (export/print/localStorage) |
| LogFrame guided practice | ⚠️ builder-only | ✅ `practice-packs/logframe-building/` — "Building a Logframe That Actually Tracks" (4 modules, ~100 min, DAC-compatible) |
| Impact evaluation | ❌ | ✅ `Labs/impact-evaluation-lab.html`, `DeepDives/impact-measurement-foundations.html` |
| No-account local progress | ✅ | ✅ (PWA + `localStorage` across tools) |
| Offline | ✅ | ✅ (service worker, downloadable courses) |
| South Asia framing | ❌ | ✅ platform-wide |
| Localization | ❌ | ✅ i18n (hi/bn/mr/ta/…) |
| Community / certification / breadth | ❌ | ✅ extensive |

**Takeaway:** ImpactMojo is not out-competed on scope, depth, localization, or ecosystem. LFA Shala beats us on exactly one axis: a **single-purpose, guided, artifact-producing LogFrame *Matrix* builder**.

---

## 3. The one real gap — ToC Builder ≠ LogFrame Builder

This is the crux, and it's a genuine gap, not a duplicate:

- ImpactMojo's **ToC Builder** produces a **Theory of Change** — the upstream narrative of *why/how* change happens (pathways, assumptions, preconditions). Excellent, and we own this.
- LFA Shala produces a **LogFrame Matrix** — the downstream **4×4 donor grid**: `Goal / Outcomes / Outputs / Activities` × `Indicators / Means of Verification / Assumptions`, with explicit *vertical logic* and the *assumptions column*. This is the mechanical, "fill-the-grid," donor-required artifact.
- **ToC and LogFrame are cousins, not twins.** Most funders (EU, DFID/FCDO-lineage, UN, many INGOs) ask for the **LogFrame matrix specifically**. ImpactMojo currently teaches LogFrame as a *practice pack (guided reading)* and touches an *Indicator Matrix* inside `mel-lab`, but has **no dedicated interactive tool that walks a novice through building the classic 4×4 LogFrame and exports it in donor format.**

So the accurate statement is: **ImpactMojo has a ToC Builder, but not a LogFrame Builder.** That's the whitespace LFA Shala occupies.

---

## 4. Recommendations (prioritized)

### R1 — Build a **LogFrame Builder** lab *(highest value, non-duplicative)*
A self-contained interactive tool (`Labs/logframe-builder-lab.html`, matching existing lab conventions) that:
- Walks the vertical logic **Goal → Outcomes → Outputs → Activities**, then adds **Indicators → Means of Verification → Assumptions** per row.
- **Imports from the existing ToC Builder** output — position it as the natural *ToC → LogFrame* next step so it *complements* our ToC tool rather than competing with it. This is our structural advantage LFA Shala can't match.
- Outputs a **clean, printable/exportable 4×4 matrix** in donor-recognizable format (DAC-compatible, consistent with the practice pack).
- No account, `localStorage` progress, offline via the existing service worker — table-stakes we already have infra for.
- Cross-link with `practice-packs/logframe-building/` (the "why/how-to-think" reading) and `Labs/mel-lab.html` (indicators/data downstream).

### R2 — Tighten the LogFrame learning path
Surface a single **"LogFrame" learning route** that stitches: ToC Builder → LogFrame Builder → MEL Lab (indicators/data/reporting). LFA Shala's edge is *focus*; we can match the focus with a curated path while keeping our breadth.

### R3 — Borrow the "no-jargon, basic→advanced spine"
LFA Shala's "results ladder → cascading frameworks" progression is good pedagogy for a jargon-heavy topic. Adopt a similar plain-language on-ramp inside the new builder (glossary tooltips already exist via ImpactLex — reuse them).

### R4 — Don't chase their narrowness
Their weaknesses (English-only, no ToC, no community, no localization, single-author cadence) are our moat. No action needed except to keep leaning into breadth + South Asia framing + Indic languages.

---

## 5. One-line verdict

> LFA Shala does one thing we don't: a guided, artifact-producing **LogFrame Matrix builder**. We already own the harder upstream piece (Theory of Change) and the entire surrounding MEL lifecycle. Closing the gap = one focused **LogFrame Builder lab that starts from our ToC output** — turning their whole product into a single downstream step of ours.
