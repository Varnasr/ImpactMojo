# The 101 Deck Standard

What a foundational course deck has to contain before it counts as finished.
Companion to `flagship-course-standard.md`, which governs the twenty flagship
courses and does not apply here — decks have no modules, so they carry no
excerpts, worked examples or reflection prompts.

Enforced by `scripts/check-decks.py` (CI job `decks`).

## Why this file exists

The flagship standard was written down, and the flagships drifted anyway until
someone measured them. The decks had the opposite problem: **nothing was written
down at all**, so nobody could tell a thin deck from a dense one without opening
it, and no drift was ever reported because there was no bar to drift from.

Measured 2026-08-22 across all 52 decks. The result is not a gradient:

| | decks | words/slide | words |
|---|---|---|---|
| Thin | **41** | 67–81 | 6,691–8,057 |
| *(nothing in between)* | 0 | 82–139 | — |
| Dense | **11** | 140–227 | 14,426–23,585 |

Every deck has ~100 slides and ~102 SVG figures, so the shell is uniform and
the *content* varies **3.4×**. `sel-basics` gives a reader 67 words a slide;
`inequality-basics` gives 227. Both present as a hundred-slide course.

The cliff between 81 and 140 is two generations of deck, not a spectrum. That
is what makes a floor defensible: it is not an aesthetic preference, it is the
line the newer decks already clear and the older ones do not approach.

## The bar

### 1. Density — **≥140 words per slide**

Roughly 14,000 words across a 100-slide deck. This is the floor the twelve
dense decks already meet, not an aspiration.

A deck below it is not "concise". At 67 words a slide a concept gets a heading,
a sentence and a diagram, which is enough to name an idea and not enough to
teach it — the "over the surface" failure. Density is a proxy for whether the
deck explains *why*, not only *what*.

### 2. Structure — density has to come from teaching, not padding

The dense decks differ from the thin ones structurally, not just in word count:

| | `mel-basics` (220 w/slide) | `sel-basics` (67 w/slide) |
|---|---|---|
| Tables | **33** (floor of the dense group: 7) | 1 |
| Two-column layouts | **76** (floor: 28) | 8 |
| List items | 223 | 89 |
| Stat elements | 75 | 38 |

So the requirement is not "write more words". It is — with each threshold set
at the **floor of the dense group, not its ceiling**, because `mel-basics`
carries 33 tables and 76 two-column slides and setting the bar there fails four
decks that are demonstrably fine:

- **≥7 tables** — comparisons, frameworks side by side, before/after. A table
  forces a claim to be specific in a way a paragraph lets you avoid.
- **≥28 two-column slides** — the format that carries "here is the idea, here
  is what it looks like in practice".
- **≥1 SVG figure per slide** (all decks already meet this).

### 3. Sources

Every statistic carries its source inline — survey, year, publisher. A number
without provenance is decoration, and in a teaching deck it is worse than
omitting the number.

### 4. Register

The same rule as everywhere else on the platform: no epigrams, no
"in today's rapidly evolving landscape", no sentence that could open any deck
on any subject. If a paragraph would survive being moved into a different
course unchanged, it is not teaching that course.

## The backlog is part of the standard

41 decks are below the floor. They are listed in `DECK_BACKLOG` in
`scripts/check-decks.py`, with their measured density, and the guard prints
the list and its size on every run.

Two properties keep that list from becoming a blindfold, matching the `EXEMPT`
convention in the other guards:

- A deck **not** on the list that falls below the floor **fails**. New thin
  decks cannot be added.
- A deck **on** the list that now clears the floor **also fails**, so it must
  be removed. The backlog can only shrink.

## Related

- `docs/flagship-course-standard.md` — the twenty flagship courses
- `docs/101-decks-guide.md` — the deck format, slugs and LMS embedding
- `scripts/check-decks.py` — the guard
