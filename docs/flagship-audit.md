# Flagship Audit — Gap Matrix (2026-07)

Measured directly from the production `course_content` DB and the course shells, against `flagship-specification.md`. Regenerate with the audit script.

| course | mods | kB/mod | diagrams | excerpts | coach (Vandana/Varna) | reflect | worked | formulae | prog-bar | Conn-Res | hero-Papers | KaTeX |
|---|--:|--:|--:|--:|--|--:|--:|--:|:--:|--:|:--:|:--:|
| devecon | 13 | 21.1 | 13 | 0 | 13: 13/13 | 0 | 0 | 5 | yes | 7 | yes | — |
| pubpol | 16 | 10.1 | **1** | 0 | **16: 0/8 (no alt)** | 0 | 0 | 0 | yes | 7 | yes | — |
| pubchoice | 13 | 32.8 | **0** | 0 | **13: 0/6 (no alt)** | 0 | 0 | 0 | yes | 7 | yes | — |
| livelihoods | 17 | 3.6 | **3** | 0 | 0: 0/0 | 0 | 0 | 0 | yes | 6 | **no** | — |
| mel | 14 | 15.5 | 14 | 0 | 10: 6/7 | 0 | 0 | 0 | yes | 7 | yes | — |
| causal | 13 | 10.5 | 13 | 0 | 5: 2/3 | 0 | 13 | 9 | yes | 7 | yes | yes |
| dataviz | 12 | 14.9 | 12 | 0 | 12: 10/11 | 0 | 0 | 0 | **MISSING** | 7 | yes | — |
| powerBI | 8 | 27.0 | 8 | 0 | **8: 0/8 (no alt)** | 0 | 0 | 0 | yes | **0** | yes | — |
| devai | 12 | 12.5 | **0** | 0 | 12: 12/12 | 0 | 0 | 0 | **MISSING** | 7 | yes | — |
| gender | 16 | 6.1 | **0** | 0 | **16: 0/8 (no alt)** | 0 | 0 | 0 | yes | 7 | yes | — |
| sel | 13 | 12.8 | **0** | 0 | 13: 13/13 | 0 | 0 | 0 | **MISSING** | 7 | yes | — |
| law | 13 | 18.6 | **0** | 0 | 13: 6/7 | 0 | 0 | 1 | yes | 7 | yes | — |
| poa | 13 | 17.5 | 13 | 0 | 13: 6/7 | 0 | 0 | 1 | yes | 7 | yes | — |
| media | 12 | 14.1 | **1** | 0 | 12: 11/12 | 0 | 0 | 0 | yes | 7 | yes | — |
| gandhi | 13 | 14.2 | 13 | 0 | 13: 7/7 | 0 | 0 | 0 | yes | 7 | yes | — |
| intervention | 14 | 15.6 | 14 | 1 | 0: 0/0 | 14 | 13 | 4 | yes | 7 | yes | yes |
| nvc-rj | 12 | 12.3 | 12 | 0 | **5: 0/5 (no alt)** | 12 | 12 | 0 | yes | 7 | yes | — |

## Reading the matrix
- **coach (Vandana/Varna):** `N: v/r` = N coach-callouts, v mention Vandana, r mention Varna. Gold courses alternate (both > 0). **Bold '(no alt)'** = Varna-only, fails C3: **pubpol, pubchoice, gender, nvc-rj**. `0:0/0` = no coach-callouts at all: **intervention, livelihoods**.
- **diagrams (bold = short):** missing/thin in **pubchoice, livelihoods, devai, gender, sel, law, pubpol, media**.
- **excerpts:** only intervention has one; **all 17 need open-access excerpts (C7)**.
- **prog-bar MISSING:** dataviz, devai, sel (reading-progress element absent).
- **Conn-Res 0/6:** powerBI (0, special powerbi.html), livelihoods (6).
- **hero-Papers no:** livelihoods.
- **reflect/worked** only appear in causal/intervention/nvc-rj — a newer-course vocabulary, not the gold standard (which relies on alternating coach call-outs).

## Priority fix waves
1. **Diagram legibility (B5)** — global CSS fix + relabel overflowing network diagrams. Affects every diagram already shipped.
2. **Coach alternation (C3)** — rework Varna-only courses (nvc-rj, pubpol, pubchoice, gender) and add woven coach-callouts to intervention/livelihoods.
3. **Diagrams** — author for the 8 lacking courses.
4. **Open-access excerpts (C7)** — one per module, all courses.
5. **Chrome** — add reading-progress element to dataviz/devai/sel; Connected Resources to powerBI; hero Papers to livelihoods.
6. **Per-course count/SEO audit** (E1).
