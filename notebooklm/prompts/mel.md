# Monitoring, Evaluation & Learning (MEAL) — NotebookLM study-companion prompt

**Course:** Monitoring, Evaluation & Learning (MEAL) (ImpactMojo flagship, 14 modules). South Asia-first development education for practitioners, students and educators.

## 1. Sources to load
Upload `notebooklm/packs/mel-source-pack.md` and add the cited readings in `notebooklm/readings/mel.md`.

## 2. Audio Overview steering prompt (paste into NotebookLM's "Customise")
> Create a ~12-minute study-companion overview for a practitioner audience. Ground every concept in the course's South Asian examples and cited evidence — do not invent statistics or cases. Move module by module across: MEL—History, Variations & Foundations; Theory of Change & Logic Models; Indicator Design & Frameworks; Baselines, Targets & Benchmarks; Data Collection Methods; Data Quality Assurance; Quantitative Analysis; Qualitative Analysis; Evaluation Design & the OECD-DAC Framework; Learning Systems & Adaptive Management; MEL Technology & Data Systems; MEL Leadership & Sustainability. For each, give the core idea, one concrete South Asian example from the sources, and one "use it in your work" takeaway. Close with the capstone challenge. Keep the tone rigorous but accessible; define jargon on first use.

## 3. Suggested questions to seed the notebook
- What is the single most important idea in this course, and what evidence supports it?
- Summarise each module in two sentences: the concept and its South Asian application.
- Which cited readings should I go to first, and why?
- Turn the capstone into a step-by-step plan I can apply to my own work.
- Quiz me with 10 questions across the whole course, then mark my answers.
- Where do the sources disagree or leave open questions?

## 4. Wire-up (maintainer)
After creating the notebook, register it: add `mel` -> notebook-id to `data/notebooklm-registry.json`,
put the share URL in the course shell's AI Study Companion button, then optionally
`python3 scripts/notebooklm-manage.py generate-audio mel`.
