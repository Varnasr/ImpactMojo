# 101 Deck Spec Schema

A spec is a Python module under `scripts/deck-builder/specs/<slug>.py` exporting a
`DECK` dict. Build with:

```bash
python3 scripts/deck-builder/build.py <module_name>     # writes 101-courses/<slug>.html
python3 scripts/deck-builder/build.py <module_name> --check   # dry run, prints counts
```

The builder slices the proven shell (CSS + runtime JS) out of
`101-courses/dev-economics.html` and injects the generated slides, so every deck
inherits the gold-standard styling, theming, deep-linking and auto-fit for free.

## Top level

```python
DECK = {
  "slug": "data-lit",            # output filename (101-courses/data-lit.html)
  "title": "Data Literacy 101",  # appears in <title>, headers, SEO
  "description": "...",          # meta description / OG / Twitter
  "slides": [ ...slide dicts... ],
}
```

## Slide types

- **title** — `{type:"title", main:"A<br>B", sub:"...", tags:["..."]}`
- **toc** — `{type:"toc", title:"...", items:[{name, slides}]}`
- **divider** — `{type:"divider", num:"01", label:"Section One", title:"..."}`
- **content** (default) — `{label, title, titleSize:"xl|lg|md|sm", blocks:[...],
  compact|spacious|ultra-compact: True}`
- **end** — `{type:"end", eyebrow, headline, byline, ctas:[{label,href}], meta:[...]}`

## Content blocks (inside `blocks: [...]`)

| `t` | fields |
|-----|--------|
| `body` | `html`, optional `cls:"sm"` |
| `label` | `text` |
| `title` | `html`, `size`, optional `style` |
| `bullets` | `items:[...]`, optional `color`, `sm` |
| `stats` | `cols`, `cards:[{num,label,color,source}]` |
| `twocol` | `ratio:"half|a32|a23"`, `left:[blocks]`, `right:[blocks]` |
| `panel` | `color`, `title`, `html` or `blocks:[...]` |
| `hbox` | `color`, `html` |
| `term` | `word`, `def` |
| `quote` | `text`, `attr` |
| `table` | `head:[...]`, `rows:[[...]]` |
| `flow` | `steps:[...]` |
| `darkcard` | `label`, `title`, `body` |
| `chart` | `canvas`, `type`, `data`, optional `options`, `title`, `source` |
| `raw` | `html` (escape hatch for bespoke SVG diagrams) |

Colors: `cyan` (default), `green`, `amber`, `indigo`, `red`.

### Charts

`data`/`options` are JSON by default. To pass raw JavaScript (e.g. a color
callback) wrap it: `{"__js__": "{ plugins:{legend:{display:false}} }"}`.
For ECharts, use `{"lib":"echarts", "canvas":"id", "echarts":"<raw JS that inits on that id>"}`
plus a `{t:"raw", html:'<div class="chart-canvas" id="id"></div>'}` block.

## Authoring guidance (quality bar)

- **EXACTLY 100 slides.** This is enforced: `build.py` refuses to write (and
  `--check` exits non-zero) unless the deck has exactly 100 navigable slides,
  counting the title, TOC, every `divider`, every content slide and the `end`
  slide. Tune section depth until the total is 100.
- Structure: `title` (s1), `toc` (s2), then ~10–12 sections each opened by a
  `divider`, then an `end` slide.
- **Do not write the TOC `slides` labels by hand** — the builder computes each
  section's "Slides X–Y" range from the divider positions and fills them in.
  Just give each TOC item a `name` (in the same order as the dividers).
- Lead with South Asian data, examples and sources; cite real datasets
  (Census, NFHS, PLFS/NSS, World Bank) and label approximations "Illustrative".
- Keep each slide to one idea; the runtime auto-fit shrinks overflow but slides
  should be designed to fit ~1280×720 without crowding or empty space.
- Mix component types — avoid 10 bullet slides in a row. Use stats, tables,
  charts, quotes, term boxes, flows and two-column layouts for rhythm.
