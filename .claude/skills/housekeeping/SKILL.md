---
description: "Post-feature housekeeping for ImpactMojo — fix count drifts, update CHANGELOG + docs + ROADMAP, verify Google Analytics + SEO meta + brand template coverage, clean merged branches, backup index.html, sync memory + wiki + issues. Use when the user says 'housekeeping', 'clean up', 'after shipping', 'enliven the repo', 'we're done with this feature', or after merging a major batch of PRs. Includes SEO audit, a11y guidance, topbar layout safety check, duplicate-header detection with false-positive avoidance, emoji-to-Sargam replacement, and living-documentation sync."
---

# Post-Change Housekeeping — ImpactMojo

Run this checklist after any batch of changes lands on `main`. The checklist
is ordered roughly by how cheap the check is and how painful the failure
mode if missed. Skip nothing — but learn each section's **false-positive
traps** so you don't waste cycles chasing phantoms.

This skill is loaded from whichever location wins precedence first:
1. `.claude/skills/housekeeping/SKILL.md` in the repo (canonical, repo-specific)
2. `~/.claude/skills/housekeeping/SKILL.md` in the user's home (fallback, globally available)

Keep them in sync — when you update the repo copy, copy it to the home copy
so the skill stays available across any session on this machine.

---

## 0. Quick health dashboard

Before diving in, run this one-liner to see the current state of the repo:

```bash
python3 - <<'PY'
import os, re
root = '.'
counts = {
  'flagship': sum(1 for p in os.listdir('courses') if os.path.isdir(f'courses/{p}') and os.path.exists(f'courses/{p}/index.html')),
  'foundational_101': len([f for f in os.listdir('101-courses') if f.endswith('.html')]),
  'labs': len([f for f in os.listdir('Labs') if f.endswith('-lab.html')]),
  'games': len([f for f in os.listdir('Games') if f.endswith('.html')]),
  'book_summaries': len([f for f in os.listdir('BookSummaries') if f.endswith('-companion.html')]),
  'handouts': sum(1 for dp,_,fs in os.walk('Handouts') for f in fs if f.endswith('.html') and f != 'index.html'),
  'blog_posts': len([f for f in os.listdir('blog') if f.endswith('.html')]),
}
for k, v in counts.items():
    print(f'  {v:4d}  {k}')
PY
```

These are the ground-truth counts every doc, page, and marketing asset must
match. If you only do one check on a casual visit, do this one — it catches
drift instantly.

---

## 1. Git cleanup

```bash
git branch -vv | grep gone                # stale branches (merged + deleted upstream)
git branch -d <branch>                     # delete merged local branches
git fetch --prune                          # prune remote refs
git status                                 # confirm clean
```

Never use `git branch -D` (force delete) unless you've explicitly confirmed
the branch was merged.

---

## 2. Count-drift audit (CRITICAL — highest-ROI check)

Hard-coded content counts appear in dozens of places: README, CLAUDE.md,
catalog.html, index.html hero stats, premium.html, upgrade.html,
content-marketing-kit.html, org-dashboard.html, verify-certificate.html,
updates.html, press kit, admin dashboards, all 13 `docs/*.md` files,
transparency pages, and sometimes blog posts. Every time content is added
or removed, drift is near-guaranteed.

**Run a mode-aware grep that catches both word-form and parenthetical form:**

```bash
python3 - <<'PY'
import os, re
patterns = [
    (r'\b9\s*[Ff]lagship',            '9 flagship  (should match ground truth)'),
    (r'\b10\s*[Ff]lagship',           '10 flagship'),
    (r'Flagship Courses \(\d+\)',     'Flagship Courses (N)'),
    (r'\b39\s*[Ff]oundational',       '39 foundational'),
    (r'Foundational Courses \(\d+\)', 'Foundational Courses (N)'),
    (r'\b10\s*[Ll]abs?\b',            '10 labs'),
    (r'\b15\s*[Gg]ames?\b',           '15 games'),
    (r'\b25\s*[Bb]ook',               '25 book'),
]
hits = []
for dp, dirs, fns in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in {'Backups','node_modules','.git','Handouts'}]
    for fn in fns:
        if not (fn.endswith('.html') or fn.endswith('.md') or fn.endswith('.json')): continue
        path = os.path.join(dp, fn)
        try:
            with open(path, encoding='utf-8', errors='ignore') as f: text = f.read()
        except: continue
        for pat, desc in patterns:
            for m in re.finditer(pat, text):
                hits.append((path, text[:m.start()].count('\n')+1, desc, m.group(0)))
for p, line, desc, match in hits:
    print(f'  {p}:{line}  "{match}" — {desc}')
print(f'Total: {len(hits)} drift hits')
PY
```

**Replacements must be case-preserving.** Use a regex with capture groups:

```python
(re.compile(r'\b9(\s*)([Ff]lagship)'),    r'11\1\2'),
(re.compile(r'\b39(\s*)([Ff]oundational)'), r'38\1\2'),
(re.compile(r'\b10(\s*)([Ll]abs?\b)'),    r'11\1\2'),
(re.compile(r'\b15(\s*)([Gg]ames?\b)'),   r'16\1\2'),
```

**Also catch the parenthetical form** — the word-form regex above does NOT
match `Flagship Courses (9)` because "9" isn't adjacent to "flagship". Fix
these manually in: `docs/platform-overview.md`, `docs/content-catalog.md`,
`docs/faq.md`, `README.md` — or extend the regex.

**Other places counts hide:**
- `content-marketing-kit.html` stat-row cards, LinkedIn/Instagram captions, carousel text, sidebar badge "Content Kit · N Assets"
- `upgrade.html` stats banner + intro paragraph
- `index.html` hero stats + nav-stats + social-proof counter
- `premium.html` intro + comparison table
- `admin/index.html` and `admin/analytics.html` dashboard cards
- `data/search-index.json` top-level count field if present
- `.claude/memory.md` session-log entries

---

## 3. CHANGELOG + docs/changelog

**Two separate files to update:**
1. `CHANGELOG.md` — technical, detailed, engineer audience, Keep-a-Changelog format
2. `docs/changelog.md` — user-facing, plain English, shorter

Both should get an entry for every batch of user-visible changes. Version
bump: use semver — patch for fixes, minor for additions, major for breaking
changes. Date in `YYYY-MM-DD` format in `CHANGELOG.md`, friendlier format in
`docs/changelog.md` (e.g. "April 7, 2026").

Structure of a `CHANGELOG.md` entry:

```markdown
## [10.14.0] - 2026-04-07

### Added
- **Feature X** — one-liner on what shipped, scoped enough to debug later

### Changed
- **Token / token set Y** — before → after with measurable delta (e.g. contrast 2.56:1 → 6.20:1)

### Fixed
- **Specific bug** — root cause + blast radius + what was left untouched

### Removed
- **Deprecated thing** — why it's gone
```

---

## 4. Backup `index.html`

```bash
cp index.html "Backups/index-backup-$(date +%Y%m%d-%H%M)-<short-reason>.html"
```

`index.html` is ~620KB — a careless edit can silently break hundreds of
hand-written links. Always backup before major edits.

Clean up superseded backups in `Backups/` periodically (keep last ~10 named
backups). Never delete without reading at least one line to confirm the
file you're deleting is really an older copy of the current `index.html`.

---

## 5. Search index & sitemap

```bash
# Validate JSON first — a broken search index kills the Ctrl+K search
python3 -m json.tool data/search-index.json > /dev/null
python3 -m json.tool catalog_data.json > /dev/null

# Validate sitemap XML
python3 -c "import xml.etree.ElementTree as ET; ET.parse('sitemap.xml'); print('sitemap OK')"

# Count sitemap URLs vs actual files
python3 -c "
import xml.etree.ElementTree as ET
tree = ET.parse('sitemap.xml')
ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = tree.getroot().findall('s:url', ns)
print(f'Sitemap URLs: {len(urls)}')
"
```

New content (games, labs, courses, book summaries, blog posts) must be added
to BOTH `data/search-index.json` (schema: `{id, title, description, type,
category, url, tags}`) and `sitemap.xml` (with appropriate priority and
changefreq per the SEO section below).

---

## 6. Google Analytics coverage

Every user-facing HTML page must include the GA snippet with ID
`G-JRCMEB9TBW`.

**Audit:**

```bash
grep -rL "G-JRCMEB9TBW" *.html courses/*/*.html 101-courses/*.html Games/*.html \
    Labs/*.html blog/*.html BookSummaries/*.html 2>/dev/null | \
    grep -Ev '(offline|PressKit|content-marketing-kit|linkedin-claude|PAGE-TEMPLATE|404)\.html'
```

**Required snippet** (insert just before `</head>`):

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-JRCMEB9TBW"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-JRCMEB9TBW');</script>
```

**Intentional exemptions** (do not add GA):
- `offline.html` — service worker offline fallback
- `ImpactMojo_PressKit.html` — press kit / static marketing
- `content-marketing-kit.html` — internal marketing tool
- `linkedin-claude-code-visual.html` — one-off visual asset
- `PAGE-TEMPLATE.html` — skeleton
- `404.html` — debatable, currently exempt

Pages without a `</head>` closing tag (Parcel-bundled React book summaries)
need GA inserted via a different anchor — see §15 for the pattern.

---

## 7. SEO baseline (critical)

Every content page needs the full SEO meta stack. This is a 12-category
audit — run the baseline scan first, then fix gaps in bulk via a Python
script that derives values from `<title>` and the file path.

### 7a. Audit

```bash
python3 - <<'PY'
import os, re
from collections import defaultdict
ROOT = '.'
SKIP = {'Backups','node_modules','.git','mcp-server','scripts','supabase',
        'netlify-env-files','docs','tests','assets','Handouts','templates',
        'admin','SupportGifts','BookCompanionTools','community','.github'}
EXEMPT = {'offline.html','PAGE-TEMPLATE.html','linkedin-claude-code-visual.html','404.html'}

checks = {
    'description':  re.compile(r'<meta\s+name="description"', re.I),
    'canonical':    re.compile(r'<link\s+rel="canonical"', re.I),
    'og_title':     re.compile(r'<meta\s+property="og:title"', re.I),
    'og_image':     re.compile(r'<meta\s+property="og:image"', re.I),
    'twitter_card': re.compile(r'<meta\s+name="twitter:card"', re.I),
    'robots':       re.compile(r'<meta\s+name="robots"', re.I),
    'viewport':     re.compile(r'<meta\s+name="viewport"', re.I),
    'json_ld':      re.compile(r'application/ld\+json', re.I),
}
missing = defaultdict(int); total = 0
for dp, dirs, fns in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in SKIP]
    for fn in fns:
        if not fn.endswith('.html') or fn in EXEMPT: continue
        total += 1
        with open(os.path.join(dp, fn), encoding='utf-8', errors='ignore') as f:
            text = f.read()
        for k, pat in checks.items():
            if not pat.search(text): missing[k] += 1
print(f'Audited: {total}')
for k in checks: print(f'  {missing[k]:4d}  missing {k}')
PY
```

### 7b. Required baseline (every content page)

```html
<!-- SEO meta (autogenerated is fine for baseline) -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{Page Title} | ImpactMojo</title>
<meta name="description" content="{150-160 char description with primary keyword}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.impactmojo.in/{path}">

<!-- Open Graph -->
<meta property="og:title" content="{Title}">
<meta property="og:description" content="{Description}">
<meta property="og:image" content="https://www.impactmojo.in/assets/images/ImpactMojo%20Logo.png">
<meta property="og:url" content="https://www.impactmojo.in/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ImpactMojo">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{Title}">
<meta name="twitter:description" content="{Description}">
<meta name="twitter:image" content="https://www.impactmojo.in/assets/images/ImpactMojo%20Logo.png">
```

### 7c. Structured data (JSON-LD, rich-result bonus)

- **Homepage**: `EducationalOrganization` schema
- **Courses**: `Course` schema with provider, isAccessibleForFree, inLanguage
- **Games/Labs**: `LearningResource` schema with interactivityType: active
- **Book summaries**: `Book` + `Review` schema
- **Blog posts**: `Article` or `BlogPosting` schema

Full templates in `.claude/skills/seo/SKILL.md`.

### 7d. Sitemap priorities

| Content type | Priority | changefreq |
|---|---|---|
| Homepage | `1.0` | weekly |
| Flagship courses | `0.8` | monthly |
| Catalog, blog index | `0.8` | weekly |
| 101 courses | `0.7` | monthly |
| Book summaries | `0.7` | monthly |
| Games, Labs | `0.6` | monthly |
| Blog posts | `0.6` | monthly |
| Handouts | `0.5` | monthly |
| Legal pages | `0.4` | yearly |

### 7e. Core Web Vitals targets

- **LCP** < 2.5s — inline critical CSS, preload Google Fonts
- **FID** < 100ms — defer non-critical JS
- **CLS** < 0.1 — set explicit `width`/`height` on images
- **Set alt text** on every image (SEO + a11y)

---

## 8. Brand identity audit

Every user-facing content page must carry the full ImpactMojo brand stack.
Skills knows the canonical pattern from the 84 handouts.

### 8a. Required elements

| Element | Canonical | Audit pattern |
|---|---|---|
| Fonts | Inter (headings) + Amaranth (body) + JetBrains Mono (code) | `grep -L 'Amaranth:wght.*Inter:wght.*JetBrains' *.html` |
| Paper plane SVG | `.v3-paper-plane` or `.im-paper-plane` | `grep -L 'v3-paper-plane\|im-paper-plane' *.html` |
| Home link in topbar | `.im-topbar-home` or `href="index.html"` | `grep -L 'im-topbar-home\|href="index.html"\|href="/"' *.html` |
| Premium link | `href="premium.html"` OR `href="/premium"` OR `im-premium-btn` | |
| 3-button theme toggle | `data-theme="system"` + `"light"` + `"dark"` | `grep -L 'data-theme="system"' *.html` |
| Language dropdown | `js/translate.js` | `grep -L 'translate\.js' *.html` |
| Footer landmark | `<footer>` with site-footer / footer / im-footer | `grep -L '<footer\b' *.html` |
| CC BY-NC-ND | On all handouts | `grep -L 'CC BY-NC-ND' Handouts/**/*.html` |
| Google Analytics | `G-JRCMEB9TBW` | see §6 |

### 8b. Canonical `localStorage` key for theme

The whole platform now uses `im-theme` as the canonical key. Legacy keys
(`theme`, `impactmojo-theme`, `imx_theme`) are read as a one-shot migration
fallback and mirrored on every write. Never add a new theme key.

### 8c. Brand fonts stack

Canonical Google Fonts URL:

```
https://fonts.googleapis.com/css2?family=Amaranth:wght@400;700&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap
```

`docs/typography.md` documents the stack. Historical fonts removed in
v10.0.0 (Source Serif 4, Merriweather, Fraunces, Poppins, Cormorant,
Source Sans 3) must never reappear outside `Backups/`.

### 8d. Known drift paths

- **BookSummaries** pages are Parcel-bundled and may drift silently when
  the bundle is regenerated. Grep every BookSummary for the canonical
  Google Fonts URL after any bundle refresh.
- **101-courses native decks** have their own minimalist CSS that uses
  `--font-head`/`--font-body`/`--font-mono` instead of the standard names.
  This is intentional — do not normalize them.

---

## 9. Duplicate header / `im-topbar` layering

The `im-topbar` is `position: fixed; top: 0; z-index: 9999`. If a page
ALSO has a legacy `<header class="header">` or `<header class="site-header">`
that's fixed at top:0 with lower z-index, the legacy main nav is completely
invisible behind the im-topbar. Users can't reach the site navigation.

### 9a. The critical direct-bug check

```bash
# .im-topbar itself with position:sticky — this has broken 30+ pages before. Should be ZERO.
grep -rl 'position:\s*sticky' --include="*.html" . | xargs grep -l 'im-topbar' 2>/dev/null | grep -v Backups
```

If found: change the `.im-topbar { position: sticky }` to
`position: fixed; top: 0; left: 0; right: 0`.

### 9b. Layered conflict detection (higher false-positive rate)

A page has a layered conflict if BOTH:
1. It contains `<div class="im-topbar">` HTML
2. It has a **navigation** element fixed at top:0 with a known-nav class

**Tight nav selector allowlist** (do NOT remove based on anything else):

```python
NAV_SELECTORS = {
    'header', '.header', '.site-header', '.im-header', '.app-header',
    '.navbar', '.nav', '.nav-bar', 'nav', '.app-nav', '.top-nav',
    '.topbar', '.top-bar', '.site-nav', '.main-nav',
}
```

**False-positive traps** — these selectors ARE fixed at top:0 but are NOT
navigation and must NOT trigger im-topbar removal:
- `.v3-decoration-container`, `.v3-organic-bg`, `.floating-planes` — decorations
- `.reading-progress`, `.gradient-bar`, `.tricolor-bar`, `#prog` — progress bars
- `.result-flash`, `.story-screen` — game HUD elements
- `th` — table header element (CSS selector matches `th { position: sticky }`)
- `.controls`, `.top-bar-inner` — in-page control panels, not nav
- `.mobile-header` — `display: none` on desktop, no conflict

### 9c. The correct removal pattern

Use depth-counted `<div>` matching (not regex) to find the closing `</div>`
of `<div class="im-topbar">`:

```python
def find_matching_close(text, open_end_pos):
    depth = 1; i = open_end_pos
    open_re = re.compile(r'<div\b', re.I)
    close_re = re.compile(r'</div\s*>', re.I)
    while i < len(text) and depth > 0:
        m_o = open_re.search(text, i); m_c = close_re.search(text, i)
        if not m_c: return -1
        if m_o and m_o.start() < m_c.start():
            depth += 1; i = m_o.end()
        else:
            depth -= 1; i = m_c.end()
    return i if depth == 0 else -1
```

### 9d. When removing im-topbar, also add Premium link

If a page's only Premium link lives inside the im-topbar (the
`<a class="im-premium-btn" href="/premium.html">`), removing the topbar
strips the only Premium entry point. Re-add a Premium link to the legacy
header's `.theme-selector` (insert right before it) using an inline-styled
gradient button. See `.claude/skills/housekeeping/lib/premium-link-snippet.html`
for the canonical snippet.

---

## 10. Accessibility (WCAG 2.1 AA)

### 10a. Color contrast — canonical tokens

The site uses mode-aware muted-text tokens. After v10.14.0 the canonical
values that pass WCAG AA are:

| Token | Light mode | Dark mode | Notes |
|---|---|---|---|
| `--text-primary` | `#0F172A` | `#F1F5F9` | Always high contrast |
| `--text-secondary` | `#475569` | `#CBD5E1` | 7.58:1 / 12.02:1 |
| `--text-muted` | `#52627A` | `#94A3B8` | 6.20:1 / 6.96:1 |

**Never use:**
- `#94A3B8` for `--text-muted` in light mode (2.56:1 — fails AA)
- `#64748B` for `--text-muted` in dark mode (3.75:1 — fails AA)
- `#0EA5E9` (sky-500) as text on white — 2.77:1 fails; use `#0369A1` (5.93:1)
- `#F59E0B` (amber-500) as text on white — 2.15:1 fails; use `#B45309` (5.02:1)

### 10b. Link-in-text-block (WCAG §1.4.1)

Every content page with a `<main>` element should have this rule in its
inline CSS:

```css
main p  a[href]:not([class*="btn"]):not([class*="button"]):not([role="button"]),
main li a[href]:not([class*="btn"]):not([class*="button"]):not([role="button"]) {
    text-decoration: underline;
    text-underline-offset: 0.15em;
}
```

Audit: `grep -rL 'WCAG 2.1 AA (1.4.1 Use of Color)' *.html courses/*/*.html blog/*.html`

### 10c. Device-mode default theme

Every page's `:root` should default to LIGHT tokens. Dark mode goes inside
`@media (prefers-color-scheme: dark) { :root { } }`. Explicit class
overrides (`body.dark-mode`, `[data-theme="dark"]`) win over the media
query via specificity.

**Anti-pattern:** `:root { --primary-bg: #0F172A; ... }` with only a
`body.light-mode` override. This hardcodes dark mode regardless of OS.

**Known exception:** `Games/climate-action-game.html` uses a custom
earth-tone palette (`#F5F0EB`) and needs a designer-authored light-mode
token set before conversion.

### 10d. Running the audit

Two CI checks run on every PR: `axe-core WCAG 2.1 AA audit` and
`Accessibility audit (pa11y-ci)`. Both post results as sticky PR comments
via `marocchino/sticky-pull-request-comment@v3`. The job needs
`permissions: pull-requests: write` — if you see "Resource not accessible
by integration", that's missing from the workflow file.

---

## 11. Stale external links

```bash
# Should point to self-hosted resources, not the legacy mirror
grep -rln "101\.impactmojo\.in" --include="*.html" --include="*.json" \
    --include="*.md" . | grep -v Backups
```

Known mapping for stale slugs → self-hosted paths:

| Stale slug | Self-hosted |
|---|---|
| `decolonial-dev` | `/101-courses/decolonize-dev.html` |
| `code-convert-pro` | `/premium-tools/code-converter-pro.html` |
| `qual-insights` | `/premium-tools/qual-insights-lab.html` |
| `impact-partnerships` | `/Labs/impact-partnerships-lab.html` |
| `gender-studies` | `/Labs/gender-studies-lab.html` |
| `real-middle-india` | `/Games/real-middle-india.html` |
| `mel-basics-101` | `/101-courses/mel-basics.html` |
| `toc-basics-101` | `/Labs/toc-lab.html` |
| `data-literacy` | `/101-courses/data-lit.html` |
| `development-economics` | `/101-courses/dev-economics.html` |
| `public-health` | `/101-courses/pub-health-basics.html` |
| `visual-ethnography` | `/101-courses/visual-eth.html` |
| `sexual-health` | `/101-courses/SRHR-basics.html` |
| `researchQ-pro` | `/premium-tools/rq-builder.html` |

**Unresolvable slugs** (placeholders for courses that were announced but
never built) — do NOT silently remap these, mark them `comingSoon: true`
instead:

`economics-101`, `vaniscribe`, `child-development`, `feminist-research`,
`gender-mainstreaming`, `impact-eval`, `maternal-health`, `mixed-methods`,
`survey-design`.

---

## 12. Emoji → Sargam line icons

Replace pictographic emoji with inline `<img>` tags pointing at
`https://cdn.jsdelivr.net/npm/sargam-icons@1.6.6/Icons/Line/si_*.svg`.

### 12a. Canonical mapping

| Emoji | Sargam icon | Emoji | Sargam icon |
|---|---|---|---|
| 📊 | `si_ChartBar` | 🌐 | `si_Globe_detailed` |
| 🎯 | `si_Target` | 👥 | `si_UsersGroup` |
| 🔍 | `si_Search` | 🤝 | `si_Handshake` |
| 📚 | `si_Library_books` | 💡 | `si_Lightbulb` |
| 📋 | `si_Clipboard` | ⚡ | `si_Lightning` |
| 📧 | `si_Mail` | ❌ | `si_Close_circle` |
| 💬 | `si_Chat` | ♥ | `si_Heart` |
| 🔄 | `si_Direction` | ★ | `si_Star` |

### 12b. Leave as-is (typographic, not pictographic)

`✓ ✔ ✦ ✧ ⚠ ☰` — these are styled bullets, decorative sparkles
(`.v3-sparkle-1` etc.), and functional icons (hamburger menu). Replacing
them with SVG icons makes the layout noisier, not cleaner.

### 12c. Known unmapped pictographic (no clean Sargam equivalent)

`👋 🗓 🎓 🏆 📏` — left alone. Revisit if Sargam releases matching icons.

### 12d. Replacement template

```html
<img src="https://cdn.jsdelivr.net/npm/sargam-icons@1.6.6/Icons/Line/si_ChartBar.svg"
     alt="" style="width:1em;height:1em;vertical-align:-0.15em;display:inline-block;"
     aria-hidden="true">
```

### 12e. Do NOT replace emoji inside:
- `<!-- comments -->` (internal documentation)
- `<script>` / `<style>` blocks
- `<svg>` inline SVGs
- CSS class names, IDs, or selectors

---

## 13. False-positive avoidance — general principles

When you write a script to find/fix something across many files, the biggest
risk is **false positives** that silently break unrelated code. Rules:

1. **Start with a narrow allowlist, not a broad denylist.**
   - Example: to find nav elements, use a known list of nav-related class
     names, not "any element with `position: fixed`".

2. **Test on ONE file first, then verify the diff makes sense.**
   - Never run a 100-file sed across the repo without a dry-run on one file.

3. **Look for negative signals that mean "don't touch this".**
   - Presence of inline React/Parcel bundle? → unusual `<head>` structure.
   - Presence of `@media (prefers-color-scheme)` already? → already converted.
   - Presence of a `WCAG 2.1 AA` marker comment? → rule already added.

4. **Idempotency is non-negotiable.**
   - Every fix script should detect its own marker and skip already-fixed
     files. Re-running the script should be a no-op on a clean repo.

5. **Classify your matches before acting.**
   - When you find 200 matches for pattern X, don't immediately run replace.
     First: how many are in comments, scripts, styles, SVGs, test data,
     backups? Filter those out, THEN count what's actually actionable.

6. **Prefer surgical HTML edits over regex replace for structural changes.**
   - Use depth-counted brace matching for nested elements.
   - Use proper XML/HTML parsers when touching structure.

7. **Always verify tag balance after structural changes.**

   ```python
   # Post-edit sanity check
   for f in modified:
       text = open(f).read()
       for tag in ('div','head','header','footer','style','script'):
           opens = len(re.findall(rf'<{tag}\b', text, re.I))
           closes = len(re.findall(rf'</{tag}\s*>', text, re.I))
           assert opens == closes, f'{f}: {tag} imbalance {opens}/{closes}'
   ```

8. **Compare against HEAD, not just absolute balance.**
   - Some files have pre-existing imbalances in HEAD. Check that YOUR
     changes didn't introduce new imbalance (delta = 0), not that the
     final state is perfect.

9. **Known false-positive catalog** (learned from experience):
   - `<th>` — table header element — matches `th { position: sticky }`
     queries if you search for "sticky at top:0"
   - `.reading-progress`, `#prog`, `.gradient-bar` — progress bars, not nav
   - `.v3-organic-bg`, `.floating-planes`, `.v3-decoration-container` — decoration
   - `.mobile-header` — `display: none` on desktop, not a conflict
   - `.result-flash`, `.story-screen`, `.top-bar-inner` — game HUD elements
   - `code, pre, kbd, samp` — code elements, not brand fonts
   - Emoji inside `<!-- -->` comments at the top of `faq.html`, etc.
   - Stale mirror URLs in `CHANGELOG.md` — those are historical records,
     don't rewrite them.

10. **When in doubt, skip and flag.**
    - If a fix is ambiguous, leave the file untouched and report it in the
      commit message so a human can review. Better to leave 5% unfixed than
      to break 5% trying to fix 100%.

---

## 14. "Enliven the repo" — living documentation sync

After every major batch of changes, update the living documentation so
future sessions (and future humans) know what's current.

### 14a. `.claude/memory.md`

Append a session-log entry:

```markdown
## YYYY-MM-DD — {Session title}

**What shipped:**
- PR #N — one-liner
- PR #N+1 — one-liner

**Key learnings:**
- Pattern X is the canonical way to do Y
- Z is a known false-positive trap

**Known gaps flagged for follow-up:**
- Gap 1 (blocker: needs designer input)
- Gap 2 (easy win, next session)
```

Then run `/memory` to re-read and confirm.

### 14b. GitHub Wiki (`ImpactMojo/ImpactMojo.wiki.git`)

```bash
git clone https://github.com/ImpactMojo/ImpactMojo.wiki.git /tmp/imwiki
cd /tmp/imwiki
# Update affected pages:
#  - Home.md (high-level summary)
#  - Content-Guide.md (counts, new content)
#  - Changelog.md (mirror of docs/changelog.md)
#  - Roadmap.md (mirror of ROADMAP.md)
#  - Architecture.md (if structure changed)
git add -A && git commit -m "Sync wiki after v10.X.X" && git push
```

### 14c. GitHub Issues

- Close resolved issues with a commit/PR reference:
  `Fixes #N via commit <sha> in PR #M`
- Update long-running tracking issues (like #272 BookSummaries).
- Open new tracking issues for follow-up items flagged in the audit.

### 14d. GitHub Discussions

For user-visible additions, post an announcement in the Announcements
category. Not required for bug fixes or refactors.

### 14e. GitHub profile README

If the session landed something high-visibility, update
`.github/profile/README.md` with the new feature highlight.

---

## 15. Parcel-bundled pages (BookSummaries)

A subset of `BookSummaries/*.html` are Parcel React bundles with
non-standard head structure:

```html
<!DOCTYPE html>
<link href="https://fonts.googleapis.com/..." rel="stylesheet">
<html lang=en><style>...
```

No `<head>` tag, no separation between link/style/body. This means:
- `grep -L '</head>' BookSummaries/*.html` finds 17 files (known set)
- `<title>` is just the filename stem, not a real title
- Inserting meta tags requires a different anchor

**Insertion strategy for bundled pages:**

```python
# For files with <!DOCTYPE html> on its own line:
re.sub(r'(<!DOCTYPE html>)\s*\n', r'\1\n' + seo_block, text, count=1, flags=re.I)

# For files with <!DOCTYPE html><html lang=en> on the same line:
re.sub(r'(<html\s+lang=[^>]*>)', r'\1' + seo_block, text, count=1, flags=re.I)
```

Known bundled files (as of v10.14):
`eat-frog-companion`, `gog-companion`, `ultralearning-companion`,
`atomic-habits-companion`, `handbook-social-protection`, `rsoe-companion`,
`naked-stats-companion`, `info-we-trust-companion`, `tufte-companion`,
`swd-companion`, `deep-work-companion`, `basic-econometrics-companion`,
`ted-talks-companion`, `ipcc-climate-communication-companion`,
`damned-lies-companion`, `truthful-art-companion`,
`econometrics-by-example-companion`.

---

## 16. Quality checks (final pass)

Run these before calling housekeeping complete:

```bash
# 1. No broken JSON
for f in data/*.json catalog_data.json; do
    python3 -m json.tool "$f" > /dev/null && echo "OK: $f" || echo "FAIL: $f"
done

# 2. All HTML tag balance
python3 - <<'PY'
import os, re
broken = []
for dp, dirs, fns in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in {'Backups','node_modules','.git'}]
    for fn in fns:
        if not fn.endswith('.html'): continue
        with open(os.path.join(dp, fn), encoding='utf-8', errors='ignore') as f:
            text = f.read()
        for tag in ('div','head','header','footer','style','script','section','article'):
            opens = len(re.findall(rf'<{tag}\b', text, re.I))
            closes = len(re.findall(rf'</{tag}\s*>', text, re.I))
            if opens != closes:
                broken.append((os.path.relpath(os.path.join(dp, fn), '.'), tag, opens, closes))
for f, tag, o, c in broken[:20]:
    print(f'  {f}: <{tag}> {o}/{c}')
print(f'Imbalanced: {len(broken)}')
PY

# 3. Form attribute consistency (all forms → Netlify Forms)
grep -rln '<form' --include="*.html" . | grep -v Backups | xargs \
    grep '<form' | grep -v 'data-netlify' | grep -v 'onsubmit' | grep -v 'hidden' | grep -v 'trackQuiz'

# 4. No localhost / 127.0.0.1 / stale dev URLs
grep -rln 'localhost\|127\.0\.0\.1\|\.ngrok\.' --include="*.html" . | grep -v Backups

# 5. Responsive meta on new pages
grep -rL 'name="viewport"' --include="*.html" . | grep -v Backups | head
```

---

## 17. Content-type-specific add checklists

### 17a. New game

- [ ] Self-contained `Games/<slug>.html` (inline CSS + JS)
- [ ] Sargam icons only (no emoji)
- [ ] Indian folk art illustration if decorative
- [ ] `data/search-index.json` entry with type:"game"
- [ ] `sitemap.xml` entry with priority 0.6
- [ ] Game card in `index.html` Games section
- [ ] Game listed in `docs/games-guide.md`
- [ ] `docs/changelog.md` + `CHANGELOG.md` entry
- [ ] Count bump everywhere (see §2)
- [ ] `G-JRCMEB9TBW` snippet in `<head>`

### 17b. New lab

- [ ] `Labs/<slug>-lab.html`
- [ ] All checklist items from 17a, substituting "lab" for "game"
- [ ] Lab listed in `docs/labs-guide.md`
- [ ] Lab linked from the supporting course's index.html

### 17c. New course (101 or flagship)

- [ ] 101: `101-courses/<slug>.html` (or native deck at `101-courses/native/<slug>.html`)
- [ ] Flagship: `courses/<slug>/index.html` with lexicon, modules
- [ ] `catalog_data.json` entry with type, track, level
- [ ] `catalog.html` card in the `allContent` array
- [ ] `data/search-index.json` entry
- [ ] `sitemap.xml` entry
- [ ] `docs/content-catalog.md` + `docs/platform-overview.md`
- [ ] Count bump (see §2)

### 17d. New handout

- [ ] HTML file under `Handouts/<Track>/<topic>/<name>.html`
- [ ] Must carry the full brand template (see §8a)
- [ ] CC BY-NC-ND attribution block
- [ ] `data/search-index.json` + `sitemap.xml` entries
- [ ] `docs/handouts-guide.md` update if new track

### 17e. New blog post

- [ ] `blog/<slug>.html` with brand fonts + theme toggle
- [ ] `blog.html` card (summary + date)
- [ ] `data/search-index.json` entry
- [ ] `sitemap.xml` with priority 0.6
- [ ] SEO meta (description, canonical, OG, Twitter — see §7)
- [ ] Thread post on Threads if it's a substantial piece

### 17f. New book summary

- [ ] `BookSummaries/<slug>-companion.html`
- [ ] `BookSummaries/index.html` card
- [ ] `docs/book-summaries-guide.md` entry
- [ ] Count bump (see §2)

---

## 18. Efficient execution order

When a big batch has just landed, run sections in this order for max
efficiency:

1. **§0 health dashboard** — 5 seconds, tells you what counts are correct
2. **§2 count drift** — the #1 highest-ROI check, run even for trivial sessions
3. **§9a direct topbar-sticky check** — 2 seconds, critical safety check
4. **§1 git cleanup** — delete merged branches before they accumulate
5. **§3 CHANGELOG + docs/changelog** — write while the changes are fresh
6. **§6 GA coverage** — catch new pages missing GA
7. **§7 SEO audit** — catch pages missing meta stack
8. **§10 a11y audit** — only if you made UI changes
9. **§11 stale external links** — catches recent content additions
10. **§5 search index + sitemap** — must reflect all new content
11. **§4 backup index.html** — do this AFTER all edits to index.html are done
12. **§14 enliven (memory + wiki + issues)** — close the loop for future sessions
13. **§16 quality final pass** — last sanity check before committing
14. **git commit + push + merge**

For a **minimal drive-by housekeeping** (no new content, just a polish
session), skip everything except §2, §9a, §3, §14a.

---

## 19. Updating this skill

This file lives in two places:
1. `.claude/skills/housekeeping/SKILL.md` — repo-specific canonical
2. `~/.claude/skills/housekeeping/SKILL.md` — globally available fallback

When you improve this skill, update both. The repo copy is source of
truth; copy it to home after every change:

```bash
mkdir -p ~/.claude/skills/housekeeping
cp .claude/skills/housekeeping/SKILL.md ~/.claude/skills/housekeeping/SKILL.md
```

Also update `.claude/memory.md` with a session log entry noting the skill
update, so future sessions know to check the latest version.

**Things worth adding in future:**
- New false-positive patterns as they're discovered
- New brand elements if the template evolves
- New count sources as marketing creates them
- New SEO schema types (currently just the 4 core types)
- Specific CI check results that need manual follow-up

---

## 20. Related skills

- `seo` — deeper SEO audit + structured data templates
- `brand-guidelines` — canonical brand identity enforcement  
- `content-auditor` (agent) — automated consistency checks
- `debugging` — systematic debugging for ImpactMojo-specific issues
- `add-files` — full matrix for adding new content types
