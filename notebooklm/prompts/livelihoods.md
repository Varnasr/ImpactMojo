# Livelihoods in India — NotebookLM study-companion prompt

**Course:** Livelihoods in India (ImpactMojo flagship, 17 modules). South Asia-first development education for practitioners, students and educators.

## 1. Sources to load
Upload `notebooklm/packs/livelihoods-source-pack.md` and add the cited readings in `notebooklm/readings/livelihoods.md`.

## 2. Audio Overview steering prompt (paste into NotebookLM's "Customise")
> Create a ~12-minute study-companion overview for a practitioner audience. Ground every concept in the course's South Asian examples and cited evidence — do not invent statistics or cases. Move module by module across: Framing the Field; Why Rural Still Dominates Indian Livelihoods Policy; NRLM and the SHG Federation Architecture; Agriculture and Diversification: The Smallholder Question; MGNREGA: India's Largest Public Employment Programme; Financial Inclusion: From Microcredit to UPI; The Urbanisation Reality; Informal Sector Work and Street Vendor Policy; The Gig and Platform Economy; Domestic Workers: The Largest Invisible Workforce; Urban Policy Tools: SVAMITVA, DAY-NULM, and the Missing Layers; Skill India: Promise vs Evidence. For each, give the core idea, one concrete South Asian example from the sources, and one "use it in your work" takeaway. Close with the capstone challenge. Keep the tone rigorous but accessible; define jargon on first use.

## 3. Suggested questions to seed the notebook
- What is the single most important idea in this course, and what evidence supports it?
- Summarise each module in two sentences: the concept and its South Asian application.
- Which cited readings should I go to first, and why?
- Turn the capstone into a step-by-step plan I can apply to my own work.
- Quiz me with 10 questions across the whole course, then mark my answers.
- Where do the sources disagree or leave open questions?

## 4. Wire-up (maintainer)
After creating the notebook, register it: add `livelihoods` -> notebook-id to `data/notebooklm-registry.json`,
put the share URL in the course shell's AI Study Companion button, then optionally
`python3 scripts/notebooklm-manage.py generate-audio livelihoods`.
