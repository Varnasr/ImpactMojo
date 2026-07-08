# Content Guide

This page documents how educational content is structured in ImpactMojo, for contributors who want to add or improve courses, labs, games, and resources.

## Content Types

| Type | Count | Format | Access |
|------|-------|--------|--------|
| Flagship Courses | 16 | Multi-module (12–13 modules each) | Free |
| Foundational Courses | 47 | Single-page or multi-section | Free |
| Interactive Labs | 28 | HTML/JS workbenches | Free |
| Learning Games | 135 | 18 simulations + 117 puzzles | Free |
| Premium Tools | 9 | Separate Netlify sites | Paid tiers |
| ImpactLex | 390+ terms | PWA dictionary | Free |
| Dev Case Studies | 200 | Curated library | Free |
| DevDiscourses | 500+ | Curated papers/books | Free |
| Handouts | 84 | HTML pages | Free |
| BookSummaries | 55 | Interactive reading companions | Free (Specials) |
| Deep Dives | 21 | Curated annotated reading lists | Free (Specials) |
| 101 Course Decks | 47 | Native HTML (~100 slides), fully self-hosted | Free |
| Blog posts | Ongoing | HTML articles | Free |
| Podcast | Episodes | Audio (Spotify) | Free |

## Learning Tracks

Content is organized into 6 tracks:

1. **MEL & Research** — Monitoring, evaluation, qualitative/quantitative methods
2. **Economics & Policy** — Development economics, political economy, fundraising
3. **Gender & Equity** — Gender studies, WEE, care economy, data feminism
4. **Governance & Society** — Constitution, decolonization, community development
5. **Health & Wellbeing** — Public health, climate, SEL, livelihoods
6. **Communication & Data** — Data literacy, visual ethnography, BCC, advocacy

## Flagship Course Structure

Each flagship course follows a consistent structure:

- **13 modules** (approximately)
- **Lexicon** of 50–65 key terms
- **South Asian context** — examples from India, Bangladesh, Nepal, Sri Lanka
- **Case studies** — real development programs and evaluations
- **Reflection prompts** — for practitioners to connect to their work
- **Further reading** — curated from DevDiscourses

### Example: MEL for Development
```
Module 1:  What is MEL?
Module 2:  Theories of Change
Module 3:  Indicators & Frameworks
Module 4:  Data Collection Methods
...
Module 13: MEL for Learning & Adaptation
Lexicon:   65 terms with definitions
```

## Interactive Labs

Labs are HTML/JS workbenches that let practitioners apply concepts. Each lab:

- Has a guided workflow (step-by-step)
- Produces an output (framework, plan, analysis)
- Can export results (PDF/PNG in premium versions)
- Requires no server — runs entirely in the browser

## Learning Games

Games are economics simulations built as single HTML pages:

- **Self-contained** — each game is one HTML file
- **Data-driven** — real economic parameters where possible
- **Debriefable** — designed for classroom or workshop use
- **Mobile-friendly** — responsive layouts

## Adding New Content

### Adding a new foundational course

1. Create a new HTML file following the existing course pattern
2. Add the course to the catalog in `catalog.html`
3. Add it to the main site's course listing in `index.html`
4. Update the README content inventory

### Adding a new game

1. Create a single HTML file with the game logic
2. Host it in the appropriate directory or as a separate Netlify site
3. Add it to the games section in `index.html` and `catalog.html`

### Adding handouts

Handouts are loaded dynamically from the repo. Add HTML files to the handouts collection and they will appear automatically.

## Multilingual Content

Content is available in 6 languages:
- English (primary)
- Hindi
- Tamil
- Bengali
- Telugu
- Marathi

Translation contributions are welcome. See [Contributing](Contributing) for guidelines.

## Style Guide

- **Tone:** Accessible but rigorous. Write for a practitioner with 2–3 years of experience.
- **Examples:** Prefer South Asian context (India, Bangladesh, Nepal, Sri Lanka).
- **Jargon:** Define terms on first use. Add to ImpactLex if they're sector-standard.
- **Attribution:** Cite sources. Link to DevDiscourses where possible.
- **Accessibility:** Use semantic HTML, alt text for images, sufficient color contrast.

## How to Write a Deep Dive

Deep Dives are curated annotated reading lists. Each list is an editorial artifact with a named curator's voice, not a neutral bibliography — closer to a long-form essay-as-syllabus than to a stand-alone references page.

### Anatomy of a Deep Dive

1. **Hero** — title, one-line tagline, topic chip, count of readings.
2. **Curator card** — name, role, 2–3 sentence bio. Mark as `Editor's Pick` (in-house) or `Invited Curator`.
3. **Editor's Note** — 2–4 paragraph framing essay in the curator's voice. This is the substance; the list is the receipt.
4. **3–6 themed sections** — e.g. "Foundations", "Recent Debates", "Voices from the Field". Don't make a flat list.
5. **Reading items** — for each: a type badge (📘 Book / 📄 Paper / 🎙 Podcast / 🎬 Film / 📊 Dataset / 📰 Article / 🌐 Web), a full citation with outbound link, and a 2–4 sentence annotation that says why the work matters and how it fits the syllabus.
6. **Related ImpactMojo content** — cross-link 2–4 courses, labs, games, or reading companions.
7. **Suggested citation** — APA-style citation block.
8. **Contribute CTA** — link to the pitch form.

### Files to create / update

To add a new Deep Dive:

1. Copy `/DeepDives/_template.html` → `/DeepDives/{slug}.html`. Fill in title, tagline, topic, curator, editor's note, sections, readings.
2. Add an entry to `/data/deep-dives.json` (id, title, tagline, topic, url, curator, sections, tags, reading_count, published).
3. Add an entry to `/data/search-index.json` with `"type": "deep-dive"` and `"category": "Deep Dives"`.
4. Add a `<url>` entry to `/sitemap.xml`.
5. Add a card to `catalog.html` `allContent` array (`type: 'deep-dive'`, pick a track).
6. (Optional) Feature on the homepage by editing the Deep Dives section in `/index.html` if it's flagship-quality.
7. Update count text everywhere — grep for `(5 Deep Dives|5 readings)` and bump the number.

### Editorial guidelines

- **Curator voice over neutrality.** A list without a point of view is just a bibliography. Tell the reader what you would press into their hands and why.
- **Mixed media is encouraged.** A good Deep Dive has at least one podcast, one dataset, and one practitioner-facing source alongside the academic core.
- **Annotate, don't summarise.** Two to four sentences. Why this work, why now, who should read it.
- **Cross-link generously.** Use the "Related ImpactMojo Content" block to send readers to courses, labs, and reading companions that build on the list.
- **Stay in scope.** Each Deep Dive is one coherent topic — don't try to cover a whole field.
