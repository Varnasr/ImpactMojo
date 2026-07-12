# The Long View Guide

## What Is The Long View?

The Long View is **ImpactMojo's data-visualization studio** — a page of original charts built by hand from real, cited evidence on the things we teach: poverty, child survival, caste, climate, gender and women's work. It is not a slideshow of stock graphics. Every chart is drawn live in your browser from a named dataset, with the source printed underneath so you can check it.

The Long View is **free, browser-based, and requires no login**. There is nothing to install and no build step: the charts are hand-coded SVG that render on the page and adapt to your light or dark theme.

Open the studio at [/the-long-view.html](/the-long-view.html).

---

## What's in the Studio

The page is organised into two "wings", with a gallery of classics and modern greats one click further on.

### The Data Wing — 25 original charts

Twenty-five charts, each built from a public dataset and captioned with its source. They deliberately use a wide range of chart forms so the shape fits the question — among them:

- **Trends over time** — line and area charts (extreme poverty falling, India's under-five mortality, women re-entering the workforce).
- **Comparisons and gaps** — a **dumbbell** of gender gaps, a **horizontal bar** of poverty by social group, a **beeswarm** of per-capita carbon.
- **Parts of a whole** — a **donut** of the electricity mix, **waffle** grids ("if India were 100 people"), a **funnel** of the leaky education pipeline.
- **Flows and structure** — **Sankey** diagrams (two-stage and three-stage) of India's greenhouse gases, a **chord** diagram of migration between world regions.
- **Distributions and change** — a **bubble chart** of wealth vs. health, a **connected scatterplot** of the demographic transition, a **bump chart** of population rank, **small multiples** of child-mortality decline.
- **Population and place** — a **population pyramid** (1990 vs. 2050), a **stream graph** of the world's shifting weight, a **radial** chart of the monsoon, and a **hex cartogram** of female literacy by state.

A twenty-sixth panel, **"How to read a chart honestly,"** is a method note rather than a data chart: it shows the same three numbers on a truncated axis and a zero axis to demonstrate Tufte's "lie factor." Every chart in the studio starts its axis at zero.

### The Frameworks Wing — the ideas behind the numbers

Five hand-drawn diagrams of the models we use in teaching — **Arnstein's Ladder of Participation**, the **Results Chain** and its attribution gap, the **Poverty Trap** loop, **Intersectionality**, and the **Systems Iceberg** — plus a closing **"Build your own"** prompt.

### The classics & the greats (gallery)

A separate gallery at [/the-long-view/gallery.html](/the-long-view/gallery.html) holds **4 famous charts rebuilt in code** — Florence Nightingale's rose, Minard's Napoleon march, John Snow's cholera map, and a W.E.B. Du Bois spiral — alongside a curated shelf of **18 modern data-visualization masterworks** by others (Gapminder, Our World in Data, The Pudding, Warming Stripes and more), filterable by theme, each linking out to the original.

---

## How to Read and Use It

Each Data Wing chart is a card with three parts: the **chart** itself, a plain-language **insight** ("what to take away"), and a **source** line naming the dataset. Click any chart to open a dedicated page ([/the-long-view/chart.html](/the-long-view/chart.html)) with a fuller breakdown — the takeaway, the source, *why this chart form was chosen*, *how it was built*, and *what to look for*.

The studio is meant to be read as much as browsed. Use it to:

- **Teach with honest evidence** — every figure is cited and every axis starts at zero.
- **Learn chart craft** — the "why this form" and "how it's built" notes make each chart a small lesson in matching a visualization to its data.
- **Check the numbers** — the closing "Where the numbers come from" section lists the dataset behind each chart in one place.

---

## How It's Built

The Long View has no data file of its own — it is **self-contained code**. All the charts, their data, sources and captions live in `js/longview-charts.js`, which draws every visualization as plain SVG (no charting library). Styling is in `css/longview.css`, and the page shell is `the-long-view.html`.

Because the charts read theme colours from CSS variables, they redraw automatically when you switch between light and dark mode, and they respect `prefers-reduced-motion` (animations are skipped for readers who ask for less motion). A few series are pulled from figures originally sourced via the World Bank API; the values are baked into the code so the page works offline.

---

## Related

- [Numbers in the News](/the-long-view/numbers-in-the-news.html) — a reader's field guide to statistics that mislead.
- [The Evidence Map](/the-long-view/evidence-map.html) — how to read an evidence gap map.
- [Data Visualization 101](/101-courses/data-viz.html) — building charts that are clear and honest.
- [Dataverse](/dataverse.html) — the datasets and tools we draw on, in one place.
