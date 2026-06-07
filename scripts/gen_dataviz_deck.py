#!/usr/bin/env python3
"""Generate 101-courses/data-viz.html - Data Visualization 101.

Reuses the exact CSS / sprite / nav-JS chrome from data-lit.html so the new
deck is visually and behaviourally identical to the rest of the 101 series.
Only the slide content, title-slide, meta tags and chart code are new.
"""
import re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, '101-courses', 'data-lit.html')
OUT = os.path.join(ROOT, '101-courses', 'data-viz.html')

src = open(TPL).read()
CSS = src[src.index('<style>'):src.index('</style>') + len('</style>')]
sp = src.index('<svg class="sprites"')
spend = src.index('</svg>\n\n<div id="progress-bar"')
SPRITE = src[sp:spend + len('</svg>')]
mj0 = src.index('<script>\nconst SLIDE_IDS')
mj1 = src.index('</script>', mj0)
MAINJS = src[mj0 + len('<script>'):mj1]
pj0 = src.index('<script>', mj1)
pj1 = src.index('</script>', pj0)
POLISHJS = src[pj0 + len('<script>'):pj1]

COURSE = "Data Visualization 101"
LOGO = ('<svg class="logo-plane" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">'
        '<path d="M50,150 L150,50 L50,100 L80,130 Z" fill="none" stroke="#0EA5E9" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M80,130 L150,50" stroke="#6366F1" stroke-width="2" stroke-dasharray="4,4"/>'
        '<circle cx="150" cy="50" r="4" fill="#10B981"/></svg>')


def header():
    return ('<div class="slide-header"><a href="https://www.impactmojo.in/101-courses/" class="logo-mark" '
            'target="_blank">' + LOGO + '<span class="logo-wordmark">ImpactMojo</span></a>'
            '<span class="header-center">' + COURSE + '</span>'
            '<span class="header-url">www.impactmojo.in</span></div>')


def footer(n):
    return ('<div class="slide-footer"><span class="footer-left">CC BY-NC-ND 4.0 &middot; ImpactMojo 101 Series'
            '</span><span class="slide-number">' + ('%02d' % n) + '</span>'
            '<span class="footer-right">www.impactmojo.in</span></div>')


slides = []  # list of (kind, payload)


def content(inner):
    slides.append(('content', inner))


def divider(num, label, title):
    slides.append(('divider', (num, label, title)))


# ---- s1 TITLE ----
slides.append(('title', None))
# ---- s2 TOC ----
TOC = [
    ("What a Chart Is For", "3&ndash;9"),
    ("Marks &amp; Channels", "10&ndash;18"),
    ("Choosing a Chart", "19&ndash;29"),
    ("Honest Charts", "30&ndash;40"),
    ("Colour", "41&ndash;49"),
    ("Words on Charts", "50&ndash;57"),
    ("Tables &amp; Numbers", "58&ndash;64"),
    ("Spread &amp; Uncertainty", "65&ndash;73"),
    ("Maps", "74&ndash;81"),
    ("Audience &amp; Access", "82&ndash;89"),
    ("Workflow &amp; Tools", "90&ndash;98"),
]
slides.append(('toc', TOC))

# ===================== SECTION 1 =====================
divider(1, "Section One", "What a Chart Is For")

content('<div class="section-label">The job of a chart</div>'
        '<div class="slide-title md">A chart is an argument, not decoration</div>'
        '<div class="slide-body">Every chart you make is making a point: <em>this went up</em>, <em>this group '
        'is worse off</em>, <em>these two things move together</em>. A good chart helps a reader see that point '
        'faster than a paragraph could. A bad one hides it, or worse, makes a point the data does not support.</div>'
        '<div class="hbox"><div class="hbox-text">If you cannot say in one sentence what your chart is for, '
        'the reader will not be able to either. Write that sentence first &mdash; it usually becomes your title.</div></div>')

content('<div class="section-label">Why pictures work</div>'
        '<div class="slide-title md">The eye finds patterns the table hides</div>'
        '<div class="two-col half"><div><div class="slide-body sm">The classic demonstration is '
        '<strong>Anscombe&rsquo;s quartet</strong>: four datasets with almost identical means, variances and '
        'correlation. In a table they look the same. Plotted, they are obviously different &mdash; one is a clean line, '
        'one is curved, one has a single outlier dragging the trend.</div>'
        '<div class="hbox amber"><div class="hbox-text">Summary statistics can agree while the data disagree. '
        'Always look at the shape before you trust the number.</div></div></div>'
        '<div class="col-panel indigo"><div class="col-panel-title">The point</div>'
        '<div class="slide-body sm">We are very good at spotting lines, clusters, gaps and outliers by eye. '
        'We are bad at reading those same things out of a grid of numbers. Visualisation borrows the strength '
        'of the visual system to do statistics.</div></div></div>')

content('<div class="section-label">Picture vs. number</div>'
        '<div class="slide-title md">When a picture beats a sentence &mdash; and when it doesn&rsquo;t</div>'
        '<table class="ctable"><thead><tr><th>Reach for a chart when&hellip;</th><th>Reach for a number when&hellip;</th></tr></thead>'
        '<tbody>'
        '<tr><td>You are comparing many values at once</td><td>There is only one value that matters</td></tr>'
        '<tr><td>The shape or trend is the message</td><td>The precise figure is the message</td></tr>'
        '<tr><td>You want the reader to explore</td><td>You want the reader to remember one fact</td></tr>'
        '<tr><td>Patterns, gaps and outliers carry meaning</td><td>The audience needs to quote the exact value</td></tr>'
        '</tbody></table>'
        '<div class="hbox green"><div class="hbox-text">&ldquo;63% of rural households have piped water&rdquo; is one '
        'number &mdash; a sentence is fine. The change across 28 states over 20 years is a chart.</div></div>')

content('<div class="section-label">Knowing when to stop</div>'
        '<div class="slide-title md">When <em>not</em> to make a chart</div>'
        '<ul class="bullet-list red">'
        '<li><strong>Two or three numbers.</strong> A small table or a sentence is clearer than a tiny bar chart.</li>'
        '<li><strong>No real variation.</strong> If every bar is the same height, the chart says nothing.</li>'
        '<li><strong>The data is too thin.</strong> A trend drawn from three data points invites over-reading.</li>'
        '<li><strong>You are decorating a slide.</strong> A chart with no question behind it is just visual noise.</li>'
        '</ul>'
        '<div class="hbox"><div class="hbox-text">A chart is a cost &mdash; it asks the reader to learn its axes and '
        'colours. Only spend that cost when the payoff (a pattern they could not otherwise see) is real.</div></div>')

content('<div class="section-label">Three readers</div>'
        '<div class="slide-title md">Who is the chart for?</div>'
        '<div class="stat-grid c3">'
        '<div class="stat-card"><div class="stat-number">You</div><div class="stat-label">'
        '<strong>Exploring.</strong> Rough, fast, many charts. Ugly is fine &mdash; you are looking for what is there.</div></div>'
        '<div class="stat-card indigo"><div class="stat-number">A team</div><div class="stat-label">'
        '<strong>Explaining.</strong> One clear point per chart, labelled, in a report or deck.</div></div>'
        '<div class="stat-card green"><div class="stat-number">The public</div><div class="stat-label">'
        '<strong>Persuading.</strong> Self-contained, titled with the finding, works without you in the room.</div></div>'
        '</div>'
        '<div class="hbox amber"><div class="hbox-text">The same data needs three different charts for these three '
        'readers. Most mistakes come from showing an <em>exploration</em> chart to <em>the public</em>.</div></div>')

content('<div class="section-label">The standard</div>'
        '<div class="slide-title md">What makes a chart good</div>'
        '<ul class="bullet-list green">'
        '<li><strong>Honest</strong> &mdash; the visual proportions match the numbers. This is non-negotiable.</li>'
        '<li><strong>Clear</strong> &mdash; a reader gets the main point in a few seconds, without a manual.</li>'
        '<li><strong>Sourced</strong> &mdash; the data, the date and the source are on the chart, not lost.</li>'
        '<li><strong>Focused</strong> &mdash; one chart makes one point; if it makes three, split it into three.</li>'
        '</ul>'
        '<div class="hbox"><div class="hbox-text">Notice what is <em>not</em> on this list: &ldquo;beautiful&rdquo;. '
        'Beauty helps a chart get read, but it never rescues a chart that is dishonest or unclear.</div></div>')

# ===================== SECTION 2 =====================
divider(2, "Section Two", "Marks &amp; Channels")

content('<div class="section-label">The building blocks</div>'
        '<div class="term-box"><div class="term-word">Marks &amp; channels</div>'
        '<div class="term-def">A <strong>mark</strong> is the thing you draw &mdash; a dot, a line, a bar, an area. '
        'A <strong>channel</strong> is the property of that mark you use to carry data &mdash; its position, length, '
        'angle, area, colour or shape. Every chart is just data mapped onto marks through channels.</div></div>'
        '<div class="slide-body">Once you see charts this way, &ldquo;what chart should I use?&rdquo; becomes a sharper '
        'question: <em>which channel will carry my most important variable?</em></div>')

content('<div class="section-label">The hierarchy</div>'
        '<div class="slide-title md">Some channels are read more accurately than others</div>'
        '<div class="slide-body sm">From the work of Cleveland &amp; McGill (1984), channels ranked by how '
        'accurately people read quantities from them &mdash; most accurate at the top:</div>'
        '<ul class="bullet-list">'
        '<li><strong>1. Position</strong> on a common scale (scatter, dot plot)</li>'
        '<li><strong>2. Position</strong> on unaligned scales (small multiples)</li>'
        '<li><strong>3. Length</strong> (bars)</li>'
        '<li><strong>4. Angle / slope</strong> (pie slices, line steepness)</li>'
        '<li><strong>5. Area</strong> (bubbles, treemaps)</li>'
        '<li><strong>6. Colour intensity / shade</strong> (heatmaps, choropleths)</li>'
        '</ul>'
        '<div class="hbox green"><div class="hbox-text">Put your most important variable on the most accurate '
        'channel you can afford. That single habit fixes most weak charts.</div></div>')

content('<div class="section-label">Position</div>'
        '<div class="slide-title md">Why position wins</div>'
        '<div class="two-col half"><div><div class="slide-body sm">When two marks sit on the same axis, the reader '
        'compares them directly &mdash; no mental arithmetic, no guessing at areas. That is why a <strong>dot plot</strong> '
        'or <strong>scatter</strong> lets people read values to within a few percent, while a pie chart leaves them '
        'guessing.</div></div>'
        '<div class="col-panel"><div class="col-panel-title">Practical rule</div>'
        '<div class="slide-body sm">If precise comparison matters, get your values onto a shared horizontal or '
        'vertical scale. Bars and dot plots do this; pies, bubbles and 3D do not.</div></div></div>')

content('<div class="section-label">Length</div>'
        '<div class="slide-title md">Length needs a zero baseline</div>'
        '<div class="slide-body">A bar encodes a value with its <strong>length</strong>. A reader judges a bar twice '
        'as long as carrying twice the value &mdash; so the bar must start at zero. Cut the baseline and a 2% difference '
        'can look like a doubling. This is the single most common way charts mislead.</div>'
        '<div class="hbox red"><div class="hbox-text"><strong>Bars start at zero. Always.</strong> '
        'If zero is irrelevant to your story (say, a stock index that never goes near it), use a line, not a bar &mdash; '
        'lines encode <em>change</em>, not magnitude, and may omit zero.</div></div>')

content('<div class="section-label">Area</div>'
        '<div class="slide-title md">Area is honest but hard to read</div>'
        '<div class="two-col half"><div><div class="slide-body sm">We badly underestimate area. Double a circle&rsquo;s '
        '<em>radius</em> and its area quadruples &mdash; a common bubble-chart error makes big values look four times too '
        'big. Even done correctly, readers cannot compare areas precisely.</div></div>'
        '<div class="col-panel amber"><div class="col-panel-title">Use area when&hellip;</div>'
        '<div class="slide-body sm">A rough sense of magnitude is enough (a treemap of budget shares), or area is a '
        'secondary channel (bubble size on a scatter). Never when readers must rank close values. '
        'And always scale by area, never by radius.</div></div></div>')

content('<div class="section-label">Colour</div>'
        '<div class="slide-title md">Colour: powerful, easily overused</div>'
        '<div class="slide-body">Colour is great for showing <em>categories</em> (which line is which) and rough '
        '<em>intensity</em> (a heatmap). It is poor for precise quantities &mdash; nobody can read &ldquo;47&rdquo; off a '
        'shade of blue. Colour gets its own section later; for now, two rules:</div>'
        '<ul class="bullet-list">'
        '<li>Use colour to <strong>group or highlight</strong>, not to carry numbers people must read off.</li>'
        '<li>Keep the number of colours small &mdash; the eye loses track past about seven.</li>'
        '</ul>')

content('<div class="section-label">One variable, done well</div>'
        '<div class="slide-title md">Encode the important thing strongly</div>'
        '<div class="slide-body">Suppose you are comparing female literacy across 12 states. The states are the '
        'categories; literacy is the number that matters. Put literacy on <strong>position or length</strong> '
        '(a sorted bar or dot plot), and use colour only to flag the one state you want to talk about.</div>'
        '<div class="hbox indigo"><div class="hbox-text">A frequent mistake is to spend the strongest channel '
        '(position) on something unimportant (alphabetical order) and push the real variable onto a weak one '
        '(colour shade). Sort by the value instead.</div></div>')

content('<div class="section-label">Worked example</div>'
        '<div class="slide-title md">Same data, three encodings</div>'
        '<table class="ctable"><thead><tr><th>Encoding</th><th>Channel</th><th>How well it reads</th></tr></thead>'
        '<tbody>'
        '<tr><td>Pie chart of 6 shares</td><td>Angle / area</td><td>Hard &mdash; can&rsquo;t rank similar slices</td></tr>'
        '<tr><td>Stacked bar of 6 shares</td><td>Length (unaligned)</td><td>Better for the bottom segment only</td></tr>'
        '<tr><td>Sorted bar / dot plot</td><td>Position + length</td><td>Best &mdash; every value is comparable</td></tr>'
        '</tbody></table>'
        '<div class="hbox green"><div class="hbox-text">Three ways to show the same six numbers. The data did not '
        'change &mdash; only how accurately the reader can recover it. That choice is yours to make on purpose.</div></div>')

# ===================== SECTION 3 =====================
divider(3, "Section Three", "Choosing a Chart")

content('<div class="section-label">Start here</div>'
        '<div class="slide-title md">Pick the question before the chart</div>'
        '<div class="slide-body">Do not start from &ldquo;I want a chart.&rdquo; Start from the question your reader has. '
        'Almost every question is one of five kinds, and each kind has a natural chart family.</div>'
        '<div class="flow">'
        '<div class="flow-step"><div class="flow-num">Q</div><div class="flow-label">What&rsquo;s the question?</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">TYPE</div><div class="flow-label">Comparison? Trend? Part? Spread? Link?</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">CHART</div><div class="flow-label">The family that fits</div></div>'
        '</div>')

content('<div class="section-label">Comparison</div>'
        '<div class="slide-title md">&ldquo;Who is bigger / more / worse off?&rdquo; &rarr; bars</div>'
        '<div class="two-col half"><div><div class="slide-body sm">For comparing values across categories, a '
        '<strong>bar chart</strong> is the workhorse. Sort the bars by value (not alphabetically) so the ranking is '
        'instant. Horizontal bars when labels are long.</div>'
        '<div class="hbox"><div class="hbox-text">A <strong>dot plot</strong> does the same job with less ink and '
        'handles two series (e.g. men vs women) cleanly as a dumbbell.</div></div></div>'
        '<div class="col-panel"><div class="col-panel-title">Watch out</div>'
        '<div class="slide-body sm">Bars must start at zero. Too many bars (40+) become a wall &mdash; switch to a dot '
        'plot or a sorted table.</div></div></div>')

content('<div class="section-label">Change over time</div>'
        '<div class="slide-title md">&ldquo;Is it rising or falling?&rdquo; &rarr; lines</div>'
        '<div class="slide-body">Time goes on the horizontal axis, left to right. A <strong>line</strong> connects '
        'points to show the trend; the slope <em>is</em> the message. Use a line for continuous time, a bar only when '
        'the periods are few and discrete.</div>'
        '<ul class="bullet-list sm">'
        '<li>One to four lines: label each line directly at its end &mdash; skip the legend.</li>'
        '<li>Many series: use <strong>small multiples</strong> (one mini-chart each) instead of a tangle.</li>'
        '<li>Lines may omit zero &mdash; they encode change, not magnitude.</li>'
        '</ul>')

content('<div class="section-label">Part of a whole</div>'
        '<div class="slide-title md">&ldquo;What share is each part?&rdquo; &rarr; handle with care</div>'
        '<table class="ctable"><thead><tr><th>Option</th><th>Verdict</th></tr></thead><tbody>'
        '<tr><td>Pie chart</td><td>Fine for 2&ndash;3 slices that are very different; poor beyond that</td></tr>'
        '<tr><td>100% stacked bar</td><td>Good for comparing the same parts across a few groups</td></tr>'
        '<tr><td>Sorted bar of the shares</td><td>Usually clearest &mdash; reader can rank every part</td></tr>'
        '<tr><td>Treemap</td><td>Many nested parts where rough size is enough</td></tr>'
        '</tbody></table>'
        '<div class="hbox red"><div class="hbox-text">The infamous pie of 12 near-equal slices tells the reader '
        'nothing. When in doubt, a sorted bar of the percentages beats a pie.</div></div>')

content('<div class="section-label">Distribution</div>'
        '<div class="slide-title md">&ldquo;How is it spread out?&rdquo; &rarr; histogram, box, strip</div>'
        '<div class="two-col half"><div><div class="slide-body sm">When you care about the <em>range</em> and '
        '<em>shape</em> of values &mdash; not a single average &mdash; show the distribution. A <strong>histogram</strong> '
        'bins the values; a <strong>box plot</strong> summarises quartiles; a <strong>strip / beeswarm</strong> shows '
        'every point.</div></div>'
        '<div class="col-panel green"><div class="col-panel-title">Why it matters</div>'
        '<div class="slide-body sm">&ldquo;Average income &#8377;15,000&rdquo; can hide a few rich households and many poor '
        'ones. The distribution reveals the inequality the mean conceals.</div></div></div>')

content('<div class="section-label">Relationship</div>'
        '<div class="slide-title md">&ldquo;Do these two move together?&rdquo; &rarr; scatter</div>'
        '<div class="slide-body">A <strong>scatter plot</strong> puts one variable on each axis and one dot per '
        'observation. Clusters, lines and outliers jump out. Add a trend line only if it genuinely helps &mdash; and '
        'never let it imply causation (more on that soon).</div>'
        '<ul class="bullet-list sm">'
        '<li>Add a third variable with dot <strong>colour</strong> (category) or <strong>size</strong> (quantity).</li>'
        '<li>A <strong>connected scatter</strong> traces two variables over time as a path.</li>'
        '</ul>')

content('<div class="section-label">Scales</div>'
        '<div class="slide-title md">Linear or log? The axis is a choice too</div>'
        '<div class="slide-body">Most charts use a <strong>linear</strong> scale, where equal distances mean equal '
        'amounts. A <strong>log</strong> scale makes equal distances mean equal <em>multiples</em> (10, 100, 1,000) '
        '&mdash; useful when values span many orders of magnitude, or when the rate of growth is the story.</div>'
        '<ul class="bullet-list sm">'
        '<li>Linear: most data, most audiences &mdash; the safe default.</li>'
        '<li>Log: incomes from poor to billionaire, exponential growth, anything spanning 100&times; or more.</li>'
        '<li>Always <strong>label a log axis clearly</strong> &mdash; many readers misread it as linear and '
        'underestimate the spread.</li>'
        '</ul>')

content('<div class="section-label">Ranking &amp; flow</div>'
        '<div class="slide-title md">Two more families worth knowing</div>'
        '<div class="two-col half">'
        '<div class="col-panel indigo"><div class="col-panel-title">Ranking</div>'
        '<div class="slide-body sm">When the order itself is the story (league tables, top-10 lists), use an '
        '<strong>ordered bar</strong> or <strong>dot plot</strong>. A <strong>slope chart</strong> shows how ranks '
        'change between two points in time.</div></div>'
        '<div class="col-panel"><div class="col-panel-title">Flow &amp; networks</div>'
        '<div class="slide-body sm">For quantities moving between categories &mdash; budget &rarr; sector, source &rarr; '
        'use &mdash; a <strong>Sankey</strong> shows volume as ribbon width. A <strong>chord</strong> diagram shows '
        'two-way flows (trade, migration between regions).</div></div></div>')

content('<div class="section-label">The cheat sheet</div>'
        '<div class="slide-title md">The chart chooser</div>'
        '<table class="ctable"><thead><tr><th>Your question</th><th>First choice</th><th>Also consider</th></tr></thead>'
        '<tbody>'
        '<tr><td>Compare categories</td><td>Sorted bar</td><td>Dot plot, dumbbell</td></tr>'
        '<tr><td>Trend over time</td><td>Line</td><td>Area, small multiples</td></tr>'
        '<tr><td>Part of a whole</td><td>Sorted bar of shares</td><td>Stacked bar, treemap</td></tr>'
        '<tr><td>Distribution</td><td>Histogram</td><td>Box, strip, beeswarm</td></tr>'
        '<tr><td>Relationship</td><td>Scatter</td><td>Bubble, connected scatter</td></tr>'
        '<tr><td>Flow between groups</td><td>Sankey</td><td>Chord</td></tr>'
        '</tbody></table>')

content('<div class="section-label">Worked example</div>'
        '<div class="slide-title md">From question to chart</div>'
        '<div class="slide-body sm">Question: <em>&ldquo;Which of these countries has the highest under-five '
        'mortality?&rdquo;</em> That is a <strong>comparison</strong> &mdash; so a sorted bar, starting at zero, '
        'one country per bar, ordered worst to best.</div>'
        '<div class="chart-wrap"><div class="chart-title">Under-five mortality, deaths per 1,000 live births (latest)</div>'
        '<canvas id="u5mChart"></canvas>'
        '<div class="chart-source">Source: World Bank / UN IGME, indicator SH.DYN.MORT. Illustrative recent values.</div></div>')

# ===================== SECTION 4 =====================
divider(4, "Section Four", "Honest Charts")

content('<div class="section-label">The core duty</div>'
        '<div class="slide-title md">A chart can lie while every number is true</div>'
        '<div class="slide-body">You can plot accurate data and still mislead &mdash; through the axis, the scale, the '
        'time window or the framing. Because charts are read fast and trusted instinctively, a misleading chart does '
        'more damage than a misleading sentence. This section is the most important in the course.</div>'
        '<div class="hbox red"><div class="hbox-text">The test: would a careful reader come away believing something '
        'the data does not actually support? If yes, the chart is dishonest &mdash; even if no single value is wrong.</div></div>')

content('<div class="section-label">Mislead #1</div>'
        '<div class="slide-title md">The truncated axis</div>'
        '<div class="two-col half">'
        '<div class="chart-wrap"><div class="chart-title">Misleading &mdash; axis starts at 90</div>'
        '<canvas id="truncChart"></canvas></div>'
        '<div class="chart-wrap"><div class="chart-title">Honest &mdash; axis starts at 0</div>'
        '<canvas id="honestChart"></canvas></div>'
        '</div>'
        '<div class="hbox red"><div class="hbox-text">Same three numbers (92, 94, 96%). On the left the change looks '
        'enormous; on the right, modest &mdash; which is the truth. Bars must start at zero.</div></div>')

content('<div class="section-label">The exception</div>'
        '<div class="slide-title md">When zero is <em>not</em> required</div>'
        '<div class="slide-body">The zero rule is about <strong>bars</strong>, where length carries the value. '
        '<strong>Lines</strong> encode change, so they may start where the data lives &mdash; forcing a stock index or '
        'a temperature series to include zero can flatten a real, meaningful change.</div>'
        '<ul class="bullet-list sm">'
        '<li><strong>Bar / area</strong> &rarr; must include zero.</li>'
        '<li><strong>Line / scatter</strong> &rarr; zero optional; choose a range that shows the real variation '
        'without exaggerating it.</li>'
        '<li>When you omit zero on a line, make the axis range obvious so nobody is fooled.</li>'
        '</ul>')

content('<div class="section-label">Mislead #2</div>'
        '<div class="slide-title md">The dual-axis trap</div>'
        '<div class="slide-body">Two lines, two different y-axes, scaled so they appear to track each other &mdash; the '
        'reader infers a relationship that the analyst manufactured by choosing the scales. By sliding the axes you '
        'can make almost any two series look correlated.</div>'
        '<div class="hbox amber"><div class="hbox-text">Prefer two small charts side by side, or index both series to '
        '100 at a common start year and plot them on one honest axis. Avoid the second y-axis unless the two units are '
        'genuinely linked.</div></div>')

content('<div class="section-label">Mislead #3</div>'
        '<div class="slide-title md">The cherry-picked window</div>'
        '<div class="slide-body">Start the time axis at an unusually low year and the trend looks like a boom; start '
        'at a peak and the same series looks like a collapse. The data is real; the <em>window</em> is the lie.</div>'
        '<ul class="bullet-list sm">'
        '<li>Show the longest honest period you have, not the slice that flatters your point.</li>'
        '<li>If you must zoom in, say so, and show the full series somewhere nearby.</li>'
        '<li>Beware comparisons to a single unusual base year (a drought, a pandemic, an election).</li>'
        '</ul>')

content('<div class="section-label">Mislead #4</div>'
        '<div class="slide-title md">3D and perspective</div>'
        '<div class="slide-body">3D bars and pies tilt the geometry so that nearer slices look bigger and the back of '
        'the chart shrinks. They add no information and distort the one channel that mattered. The same goes for '
        'drop shadows and &ldquo;glossy&rdquo; effects.</div>'
        '<div class="hbox red"><div class="hbox-text">There is no honest reason to make a statistical chart 3D. '
        'Flat, plain and accurate beats impressive every time.</div></div>')

content('<div class="section-label">Mislead #5</div>'
        '<div class="slide-title md">Sizing by radius, not area</div>'
        '<div class="slide-body">When a value is shown as a circle or icon, the reader judges it by <strong>area</strong>. '
        'If you set the radius proportional to the value, a figure twice as large draws a circle <em>four</em> times as '
        'big. Pictographs (&ldquo;one person = 1 million&rdquo;) that scale a single stretched icon make the same error.</div>'
        '<div class="hbox amber"><div class="hbox-text">Scale circles by area (radius &prop; &radic;value). Better still, '
        'for icon charts, repeat a fixed-size icon &mdash; a waffle or isotype grid &mdash; so each unit is equal.</div></div>')

content('<div class="section-label">Mislead #6</div>'
        '<div class="slide-title md">Correlation drawn as causation</div>'
        '<div class="slide-body">A scatter with a trend line, or two lines rising together, strongly <em>suggests</em> '
        'that one causes the other. The chart cannot show causation &mdash; only association. Ice-cream sales and '
        'drownings both rise in summer; neither causes the other.</div>'
        '<ul class="bullet-list sm">'
        '<li>Word the title as association (&ldquo;moves with&rdquo;), not cause (&ldquo;drives&rdquo;), unless you have '
        'evidence for cause.</li>'
        '<li>Watch for a hidden third variable (here, heat) driving both.</li>'
        '</ul>')

content('<div class="section-label">Mislead #7</div>'
        '<div class="slide-title md">Aggregation that hides the truth</div>'
        '<div class="term-box"><div class="term-word">Simpson&rsquo;s paradox</div>'
        '<div class="term-def">A trend that holds in the overall data can reverse when you split it by group. A '
        'treatment can look worse on average yet be better for <em>every</em> subgroup, because the groups differ in '
        'size and baseline risk.</div></div>'
        '<div class="hbox"><div class="hbox-text">Always ask whether a headline average survives disaggregation by '
        'sex, caste, region or income. If the picture flips, the disaggregated chart is the honest one.</div></div>')

content('<div class="section-label">The checklist</div>'
        '<div class="slide-title md">Before you publish: an integrity check</div>'
        '<ul class="bullet-list green">'
        '<li>Do bars start at zero, and are areas scaled correctly?</li>'
        '<li>Is the time window the full, fair period &mdash; not a flattering slice?</li>'
        '<li>Does the title claim only what the data supports (association vs cause)?</li>'
        '<li>Would the picture survive being split by the obvious subgroups?</li>'
        '<li>Are the source, date and units on the chart?</li>'
        '</ul>'
        '<div class="hbox"><div class="hbox-text">If a figure is approximate or modelled, say so on the chart. '
        'Never present an estimate as if it were a measured fact.</div></div>')

# ===================== SECTION 5 =====================
divider(5, "Section Five", "Colour")

content('<div class="section-label">Three jobs</div>'
        '<div class="slide-title md">Colour does exactly three jobs</div>'
        '<div class="stat-grid c3">'
        '<div class="stat-card"><div class="stat-number">Qual.</div><div class="stat-label">'
        '<strong>Qualitative</strong> &mdash; distinct hues for unordered categories (regions, parties).</div></div>'
        '<div class="stat-card indigo"><div class="stat-number">Seq.</div><div class="stat-label">'
        '<strong>Sequential</strong> &mdash; light-to-dark of one hue for low-to-high values.</div></div>'
        '<div class="stat-card amber"><div class="stat-number">Div.</div><div class="stat-label">'
        '<strong>Diverging</strong> &mdash; two hues from a meaningful middle (e.g. surplus vs deficit).</div></div>'
        '</div>'
        '<div class="hbox red"><div class="hbox-text">Most colour mistakes are using the wrong family &mdash; a rainbow '
        '(qualitative) for ordered data, or a sequential ramp for categories. Match the palette to the data type.</div></div>')

content('<div class="section-label">Sequential</div>'
        '<div class="slide-title md">Light to dark for ordered values</div>'
        '<div class="slide-body">For a quantity that runs low to high &mdash; poverty rate, temperature, density &mdash; '
        'use a single hue from pale to deep. Darker reads as &ldquo;more&rdquo; intuitively. Keep the steps evenly spaced '
        'in perceived lightness so equal jumps look equal.</div>'
        '<div class="hbox"><div class="hbox-text">Tested ramps (ColorBrewer&rsquo;s Blues, Viridis) are designed to be '
        'perceptually even and colour-blind safe. Borrow them rather than inventing your own.</div></div>')

content('<div class="section-label">Diverging</div>'
        '<div class="slide-title md">Two directions from a meaningful middle</div>'
        '<div class="slide-body">When values spread both ways from a natural centre &mdash; above/below average, '
        'gain/loss, agree/disagree &mdash; a diverging scale puts a neutral colour at the midpoint and two contrasting '
        'hues at the ends. The midpoint must be the <em>real</em> zero or mean, not an arbitrary value.</div>'
        '<div class="hbox amber"><div class="hbox-text">Set the colour midpoint to where the meaning flips. Centring '
        'it on the data&rsquo;s median instead can paint a struggling region as &ldquo;average&rdquo;.</div></div>')

content('<div class="section-label">Qualitative</div>'
        '<div class="slide-title md">Distinct hues &mdash; and not too many</div>'
        '<div class="slide-body">For categories with no order, pick hues that are easy to tell apart and roughly '
        'equal in weight (so none shouts). Past about <strong>seven</strong> colours, readers lose track and the '
        'legend becomes a memory test.</div>'
        '<ul class="bullet-list sm">'
        '<li>Too many categories? Group the small ones into &ldquo;other&rdquo;, or use small multiples.</li>'
        '<li>Give a fixed colour to a category that recurs across charts (e.g. always green for &ldquo;rural&rdquo;).</li>'
        '</ul>')

content('<div class="section-label">Accessibility</div>'
        '<div class="slide-title md">About 1 in 12 men can&rsquo;t tell red from green</div>'
        '<div class="slide-body">Roughly <strong>8% of men and 0.5% of women</strong> have some colour-vision '
        'deficiency, most commonly red&ndash;green. A chart that relies on red-vs-green to make its point fails for '
        'millions of readers.</div>'
        '<ul class="bullet-list green">'
        '<li>Use colour-blind-safe palettes (Viridis, Okabe&ndash;Ito, ColorBrewer &ldquo;colorblind safe&rdquo; sets).</li>'
        '<li>Check your chart in a simulator before publishing.</li>'
        '<li>Pair colour with a second cue &mdash; label, shape or pattern (next slide).</li>'
        '</ul>')

content('<div class="section-label">Don&rsquo;t</div>'
        '<div class="slide-title md">Retire the rainbow</div>'
        '<div class="slide-body">The classic &ldquo;jet&rdquo; rainbow ramp (blue&ndash;green&ndash;yellow&ndash;red) looks '
        'lively but lies: it has bright bands that invent boundaries where the data is smooth, and dark ones that hide '
        'real differences. It is also poor for colour-blind readers.</div>'
        '<div class="hbox red"><div class="hbox-text">Replace rainbow heatmaps and maps with a perceptually uniform '
        'ramp like Viridis. The pattern in the data will change &mdash; because the rainbow was distorting it.</div></div>')

content('<div class="section-label">Meaning</div>'
        '<div class="slide-title md">Colour carries meaning &mdash; use it deliberately</div>'
        '<ul class="bullet-list sm">'
        '<li>Red reads as <em>bad / hot / loss / stop</em>; green as <em>good / go</em>. Do not colour a good outcome '
        'red by accident.</li>'
        '<li>Convention matters: don&rsquo;t recolour a party, a flag or a brand against what readers expect.</li>'
        '<li>Meaning is cultural &mdash; white, red and saffron carry different associations across South Asia. Know '
        'your audience.</li>'
        '<li>Reserve a bold colour for the <strong>one</strong> thing you want noticed; grey the rest.</li>'
        '</ul>')

content('<div class="section-label">Worked example</div>'
        '<div class="slide-title md">Recolouring a noisy chart</div>'
        '<table class="ctable"><thead><tr><th>Before</th><th>After</th></tr></thead><tbody>'
        '<tr><td>12 bars, 12 different bright colours</td><td>11 grey bars, 1 coloured &mdash; the one you discuss</td></tr>'
        '<tr><td>Rainbow choropleth</td><td>Single-hue sequential ramp</td></tr>'
        '<tr><td>Red = our product (the &ldquo;good&rdquo; one)</td><td>Green for the favourable series</td></tr>'
        '<tr><td>Legend with 12 swatches</td><td>Direct labels on the bars that matter</td></tr>'
        '</tbody></table>'
        '<div class="hbox green"><div class="hbox-text">Less colour, more meaning. Colour should guide attention, '
        'not compete for it.</div></div>')

# ===================== SECTION 6 =====================
divider(6, "Section Six", "Words on Charts")

content('<div class="section-label">Text matters</div>'
        '<div class="slide-title md">A chart without words is half a chart</div>'
        '<div class="slide-body">Marks show the pattern; words tell the reader what it means and what to trust. '
        'Titles, labels, annotations, units and sources do as much work as the geometry. A beautiful chart with no '
        'words is a puzzle.</div>'
        '<div class="hbox"><div class="hbox-text">Budget your effort roughly half on the picture and half on the '
        'words around it. Most weak charts are under-written, not under-designed.</div></div>')

content('<div class="section-label">The title</div>'
        '<div class="slide-title md">Make the title state the finding</div>'
        '<div class="two-col half">'
        '<div class="col-panel red"><div class="col-panel-title">Weak (topic)</div>'
        '<div class="slide-body sm">&ldquo;Under-five mortality by country, 2000&ndash;2022&rdquo;</div></div>'
        '<div class="col-panel green"><div class="col-panel-title">Strong (finding)</div>'
        '<div class="slide-body sm">&ldquo;Child deaths have more than halved in every country since 2000&rdquo;</div></div>'
        '</div>'
        '<div class="hbox"><div class="hbox-text">A topic title makes the reader do the work. A finding title hands '
        'them the point, then lets the chart prove it. Keep the descriptive version as a subtitle if you like.</div></div>')

content('<div class="section-label">Labels</div>'
        '<div class="slide-title md">Label directly; kill the legend</div>'
        '<div class="slide-body">A separate legend forces the reader&rsquo;s eye to bounce between the key and the '
        'chart, matching colours from memory. Where you can, write the label next to the thing it names &mdash; at the '
        'end of each line, beside each bar.</div>'
        '<ul class="bullet-list sm">'
        '<li>One to four series: direct labels almost always win.</li>'
        '<li>Many series: a legend is unavoidable &mdash; order it to match the chart (top line = top legend entry).</li>'
        '<li>Rotate axis labels as little as possible; switch to horizontal bars if names are long.</li>'
        '</ul>')

content('<div class="section-label">Annotation</div>'
        '<div class="slide-title md">Point at the one thing that matters</div>'
        '<div class="slide-body">An annotation &mdash; a short note with an arrow or a marked point &mdash; turns a chart '
        'from &ldquo;here is some data&rdquo; into &ldquo;here is what happened.&rdquo; Mark the spike, name the policy, flag '
        'the outlier. It is the cheapest way to make a chart memorable.</div>'
        '<div class="hbox amber"><div class="hbox-text">One or two annotations, not ten. Annotate the moment that '
        'carries your argument and leave the rest of the chart quiet.</div></div>')

content('<div class="section-label">The fine print</div>'
        '<div class="slide-title md">Units, source, date &mdash; every time</div>'
        '<ul class="bullet-list">'
        '<li><strong>Units</strong> on the axis: &#8377;, %, per 1,000, thousands &mdash; never make the reader guess.</li>'
        '<li><strong>Source</strong> line: who collected the data, which dataset, which year.</li>'
        '<li><strong>Date</strong>: when the data is from, and when the chart was made if it differs.</li>'
        '<li><strong>Notes</strong>: definitions, exclusions, &ldquo;provisional&rdquo; or &ldquo;approximate&rdquo; flags.</li>'
        '</ul>'
        '<div class="hbox green"><div class="hbox-text">A sourced chart can travel on its own and be trusted. An '
        'unsourced one is just a claim.</div></div>')

content('<div class="section-label">Numbers in words</div>'
        '<div class="slide-title md">Round to the precision that matters</div>'
        '<div class="slide-body">&ldquo;63.7%&rdquo; implies you know the figure to a tenth of a percent; often you do '
        'not. Round to the precision your data and your reader actually need &mdash; usually whole numbers for a public '
        'audience.</div>'
        '<ul class="bullet-list sm">'
        '<li>Match precision to the margin of error: don&rsquo;t quote decimals a survey can&rsquo;t support.</li>'
        '<li>Use thousands separators and consistent units across a chart.</li>'
        '<li>Indian readers: lakh/crore for domestic figures, millions/billions for international comparison &mdash; '
        'pick one and stay consistent.</li>'
        '</ul>')

content('<div class="section-label">Worked example</div>'
        '<div class="slide-title md">Annotating a line</div>'
        '<div class="slide-body sm">A flat line of full-immunisation coverage suddenly climbs after 2014. The raw '
        'chart shows the rise; the <em>annotated</em> chart explains it:</div>'
        '<div class="flow">'
        '<div class="flow-step"><div class="flow-num">1</div><div class="flow-label">Finding title: &ldquo;Coverage rose after the 2014 mission&rdquo;</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">2</div><div class="flow-label">Marker + note at the 2014 inflection</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">3</div><div class="flow-label">Source + &ldquo;latest data 2021&rdquo;</div></div>'
        '</div>'
        '<div class="hbox"><div class="hbox-text">Same line, three small additions &mdash; now it argues a point '
        'instead of just plotting one.</div></div>')

# ===================== SECTION 7 =====================
divider(7, "Section Seven", "Tables &amp; Numbers")

content('<div class="section-label">Not everything is a chart</div>'
        '<div class="slide-title md">Sometimes the table is the answer</div>'
        '<div class="slide-body">When readers need exact figures, when there are only a handful of numbers, or when '
        'they will look up specific rows, a well-set <strong>table</strong> beats a chart. Tufte&rsquo;s rule of thumb: '
        'for a small dataset that will be read closely, a table often communicates better.</div>'
        '<div class="hbox"><div class="hbox-text">Don&rsquo;t force a chart onto data that wants to be a table &mdash; '
        'and don&rsquo;t bury 200 rows in a table that wants to be a chart.</div></div>')

content('<div class="section-label">Table design</div>'
        '<div class="slide-title md">A table is a designed object too</div>'
        '<ul class="bullet-list">'
        '<li><strong>Order rows meaningfully</strong> &mdash; by value, not alphabetically, unless lookup is the point.</li>'
        '<li><strong>Light rules, not heavy grids</strong> &mdash; a line under the header and at the foot is usually '
        'enough.</li>'
        '<li><strong>Group and indent</strong> to show hierarchy instead of repeating labels.</li>'
        '<li><strong>One idea per column</strong>; put units in the header, not every cell.</li>'
        '</ul>')

content('<div class="section-label">Numbers in tables</div>'
        '<div class="slide-title md">Align numbers so the eye can compare</div>'
        '<div class="two-col half">'
        '<div class="col-panel green"><div class="col-panel-title">Do</div>'
        '<div class="slide-body sm">Right-align numbers, fix the decimal places, use a mono/tabular figure so digits '
        'line up in columns. Then magnitudes are visible at a glance &mdash; longer number, bigger value.</div></div>'
        '<div class="col-panel red"><div class="col-panel-title">Don&rsquo;t</div>'
        '<div class="slide-body sm">Centre numbers, mix &ldquo;1,200&rdquo; with &ldquo;1200.0&rdquo;, or vary decimal '
        'places down a column. The digits stop lining up and comparison breaks.</div></div></div>'
        '<div class="hbox"><div class="hbox-text">Left-align text, right-align numbers. This one habit makes any '
        'table more readable.</div></div>')

content('<div class="section-label">Tiny charts in tables</div>'
        '<div class="slide-title md">Sparklines: a chart the size of a word</div>'
        '<div class="slide-body">A <strong>sparkline</strong> is a small, axis-free line drawn inline &mdash; enough to '
        'show a trend right next to the number it describes. Add a column of sparklines to a table and readers get the '
        'exact value <em>and</em> the shape of its history together.</div>'
        '<div class="hbox indigo"><div class="hbox-text">Sparklines, in-cell bars and up/down arrows let a table carry '
        'pattern as well as precision &mdash; the best of both worlds for a dashboard or report.</div></div>')

content('<div class="section-label">Big numbers</div>'
        '<div class="slide-title md">The KPI card: one number, well dressed</div>'
        '<div class="slide-body">Sometimes the most effective &ldquo;visualisation&rdquo; is a single large figure with '
        'a label and a tiny bit of context. Used on dashboards and report covers, these <strong>big-number cards</strong> '
        'make the headline impossible to miss.</div>'
        '<div class="stat-grid c3">'
        '<div class="stat-card"><div class="stat-number">63%</div><div class="stat-label">rural households with piped water</div><div class="stat-source">illustrative</div></div>'
        '<div class="stat-card green"><div class="stat-number">&minus;2.1pp</div><div class="stat-label">vs last year</div></div>'
        '<div class="stat-card amber"><div class="stat-number">28</div><div class="stat-label">states &amp; UTs covered</div></div>'
        '</div>')

content('<div class="section-label">Worked example</div>'
        '<div class="slide-title md">A clean comparison table</div>'
        '<table class="ctable"><thead><tr><th style="text-align:left">Indicator</th><th style="text-align:right">2015</th>'
        '<th style="text-align:right">2021</th><th style="text-align:right">Change</th></tr></thead><tbody>'
        '<tr><td>Full immunisation (%)</td><td style="text-align:right">62</td><td style="text-align:right">76</td><td style="text-align:right">+14</td></tr>'
        '<tr><td>Institutional births (%)</td><td style="text-align:right">79</td><td style="text-align:right">89</td><td style="text-align:right">+10</td></tr>'
        '<tr><td>Stunting, under-5 (%)</td><td style="text-align:right">38</td><td style="text-align:right">36</td><td style="text-align:right">&minus;2</td></tr>'
        '</tbody></table>'
        '<div class="hbox"><div class="hbox-text">Numbers right-aligned, units in the header, a change column to do '
        'the arithmetic for the reader. Source: NFHS-4 and NFHS-5, all-India (illustrative selection).</div></div>')

# ===================== SECTION 8 =====================
divider(8, "Section Eight", "Spread &amp; Uncertainty")

content('<div class="section-label">Beyond the average</div>'
        '<div class="slide-title md">The average hides the spread</div>'
        '<div class="two-col half"><div><div class="slide-body sm">Two districts can share an average income while one '
        'is broadly comfortable and the other has a few rich households among many poor ones. The mean is the same; the '
        '<strong>distribution</strong> is not. Development data is often skewed, so the average can mislead.</div></div>'
        '<div class="chart-wrap"><div class="chart-title">Same mean, different shape</div>'
        '<canvas id="skewChart"></canvas>'
        '<div class="chart-source">Illustrative distributions with equal means.</div></div></div>')

content('<div class="section-label">Histograms</div>'
        '<div class="slide-title md">Histograms, and the bin problem</div>'
        '<div class="slide-body">A histogram groups values into bins and shows how many fall in each. It reveals shape '
        '&mdash; symmetric, skewed, bimodal. But the <strong>bin width</strong> changes the story: too wide hides '
        'structure, too narrow turns signal into noise.</div>'
        '<div class="hbox amber"><div class="hbox-text">Try a few bin widths before settling. If the shape changes '
        'wildly with small changes in bins, say so &mdash; your data may be thinner than it looks.</div></div>')

content('<div class="section-label">Box plots</div>'
        '<div class="slide-title md">Box plots summarise &mdash; and conceal</div>'
        '<div class="slide-body">A box plot compresses a distribution into median, quartiles and whiskers &mdash; great '
        'for comparing many groups at once. The cost: it hides the actual shape. Two very different distributions can '
        'produce identical boxes.</div>'
        '<ul class="bullet-list sm">'
        '<li>Use boxes to compare spread across many categories quickly.</li>'
        '<li>When the shape matters (or n is small), overlay or switch to the points themselves.</li>'
        '</ul>')

content('<div class="section-label">Showing every point</div>'
        '<div class="slide-title md">Strip, jitter and beeswarm plots</div>'
        '<div class="slide-body">When you have room and not too many observations, plot <strong>every point</strong>. '
        'A strip plot lines them up; jittering spreads overlaps apart; a <strong>beeswarm</strong> packs them into a '
        'shape that doubles as a density. Readers see the spread, the clusters and the outliers &mdash; nothing is '
        'hidden behind a summary.</div>'
        '<div class="hbox green"><div class="hbox-text">For small datasets, showing the raw points is almost always '
        'more honest than summarising them.</div></div>')

content('<div class="section-label">Uncertainty</div>'
        '<div class="slide-title md">Show what you don&rsquo;t know</div>'
        '<div class="slide-body">Most development figures are estimates from samples or models. A point drawn without '
        'its uncertainty looks more certain than it is. Error bars, confidence bands and ranges tell the reader how '
        'much to trust the dot.</div>'
        '<ul class="bullet-list sm">'
        '<li>Add 95% confidence intervals to survey estimates where you have them.</li>'
        '<li>For two bars whose error bars overlap heavily, resist saying one is &ldquo;higher&rdquo;.</li>'
        '<li>Label what the bar or band represents &mdash; SE, 95% CI, min&ndash;max are not the same.</li>'
        '</ul>')

content('<div class="section-label">Margin of error</div>'
        '<div class="slide-title md">Bigger samples, smaller error &mdash; with diminishing returns</div>'
        '<div class="chart-wrap"><div class="chart-title">Approximate margin of error vs. sample size (50/50 proportion)</div>'
        '<canvas id="moeChart"></canvas>'
        '<div class="chart-source">&plusmn;1.96&middot;&radic;(p(1&minus;p)/n) at p=0.5; standard sampling formula.</div></div>'
        '<div class="hbox"><div class="hbox-text">Going from 400 to 1,000 respondents roughly halves the error; going '
        'from 2,400 to 4,000 barely moves it. This is why national surveys cluster around a few thousand.</div></div>')

content('<div class="section-label">Forecasts</div>'
        '<div class="slide-title md">Projections are fans, not lines</div>'
        '<div class="slide-body">A forecast drawn as a single confident line invites the reader to believe a precision '
        'that does not exist. Show projections as a <strong>fan</strong> &mdash; a widening band &mdash; so the growing '
        'uncertainty is visible. Mark clearly where measured data ends and the projection begins.</div>'
        '<div class="hbox red"><div class="hbox-text">A solid line into the future, with no band and no &ldquo;projected&rdquo; '
        'label, is one of the easiest ways to overstate what you know.</div></div>')

content('<div class="section-label">Worked example</div>'
        '<div class="slide-title md">Showing an income distribution honestly</div>'
        '<div class="flow">'
        '<div class="flow-step"><div class="flow-num">1</div><div class="flow-label">Report the median, not just the mean</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">2</div><div class="flow-label">Plot the histogram so the skew shows</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">3</div><div class="flow-label">Mark mean &amp; median on it</div></div>'
        '</div>'
        '<div class="hbox green"><div class="hbox-text">When mean and median sit far apart on the chart, the reader '
        'sees the inequality directly &mdash; no statistics lecture required.</div></div>')

# ===================== SECTION 9 =====================
divider(9, "Section Nine", "Maps")

content('<div class="section-label">Handle with care</div>'
        '<div class="slide-title md">Maps are seductive &mdash; and often the wrong choice</div>'
        '<div class="slide-body">A map feels authoritative and is genuinely useful when <em>location</em> is the '
        'story. But a lot of data plotted on a map would be clearer as a bar chart &mdash; the geography adds beauty '
        'while making values harder to compare.</div>'
        '<div class="hbox amber"><div class="hbox-text">Ask: does the spatial pattern matter, or am I mapping this '
        'because maps look impressive? If the latter, a sorted bar will serve the reader better.</div></div>')

content('<div class="section-label">Choropleths</div>'
        '<div class="slide-title md">The shaded-region map, and its trap</div>'
        '<div class="slide-body">A <strong>choropleth</strong> shades each region by a value. Its biggest trap: '
        'shading by a <em>count</em> rather than a <em>rate</em>. A map of &ldquo;total cases&rdquo; mostly shows where '
        'the people are &mdash; big, populous states light up regardless of how bad things actually are there.</div>'
        '<div class="hbox red"><div class="hbox-text">Map rates, shares and per-capita figures &mdash; not raw totals '
        '&mdash; unless &ldquo;how many&rdquo; really is the question.</div></div>')

content('<div class="section-label">Normalise</div>'
        '<div class="slide-title md">Per capita, per area, per household</div>'
        '<div class="slide-body">Normalising turns a map of population into a map of the thing you care about. '
        'Deaths &rarr; deaths per 100,000. Spending &rarr; spending per person. Schools &rarr; schools per 1,000 '
        'children. The denominator is a design decision &mdash; choose the one that matches the question.</div>'
        '<div class="hbox"><div class="hbox-text">State the denominator on the chart. &ldquo;Per 100,000&rdquo; and '
        '&ldquo;per 100,000 women aged 15&ndash;49&rdquo; can tell very different stories.</div></div>')

content('<div class="section-label">Area bias</div>'
        '<div class="slide-title md">Big empty regions shout; dense small ones whisper</div>'
        '<div class="slide-body">On a normal map, area equals visual weight. A huge, sparsely populated state '
        '(Rajasthan, Ladakh) dominates the eye, while a tiny, densely populated one (Delhi, Kerala&rsquo;s coast) all '
        'but disappears &mdash; even when far more people live there. The map over-weights land and under-weights '
        'people.</div>'
        '<div class="hbox amber"><div class="hbox-text">If your subject is people, a land-area map systematically '
        'mis-weights them. That is the problem cartograms solve.</div></div>')

content('<div class="section-label">Cartograms</div>'
        '<div class="slide-title md">Resize geography to match the data</div>'
        '<div class="slide-body">A <strong>cartogram</strong> distorts regions so their size reflects a value '
        '(population, electorate) instead of land area. A <strong>hex cartogram</strong> gives every region an equal '
        'tile &mdash; useful when you want each state read equally, regardless of size.</div>'
        '<ul class="bullet-list sm">'
        '<li>Population cartogram: each state&rsquo;s area &prop; its population &mdash; honest weighting for people-based data.</li>'
        '<li>Hex/tile grid: every state an equal cell &mdash; clear, if geographically loose.</li>'
        '<li>Trade-off: cartograms are less recognisable, so label generously.</li>'
        '</ul>')

content('<div class="section-label">Classification</div>'
        '<div class="slide-title md">How you cut the colour scale changes the map</div>'
        '<div class="slide-body">A choropleth groups values into colour bins, and the cut-points are a choice. '
        '<strong>Equal-interval</strong> bins split the range evenly; <strong>quantile</strong> bins put equal numbers '
        'of regions in each colour. The same data can look alarming or calm depending on the scheme.</div>'
        '<div class="hbox red"><div class="hbox-text">Don&rsquo;t tune the bins until the map says what you want. Pick '
        'a defensible scheme, state it, and keep it consistent across related maps.</div></div>')

content('<div class="section-label">Worked example</div>'
        '<div class="slide-title md">A map of Indian states, done honestly</div>'
        '<div class="flow">'
        '<div class="flow-step"><div class="flow-num">1</div><div class="flow-label">Use a rate (female literacy %), not a count</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">2</div><div class="flow-label">Hex tiles so small states read equally</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">3</div><div class="flow-label">Sequential ramp + stated bins</div></div>'
        '</div>'
        '<div class="hbox green"><div class="hbox-text">See this exact chart built from Census data on '
        '<strong>The Long View</strong> &mdash; ImpactMojo&rsquo;s data-visualisation showcase.</div></div>')

# ===================== SECTION 10 =====================
divider(10, "Section Ten", "Audience &amp; Access")

content('<div class="section-label">Know your reader</div>'
        '<div class="slide-title md">Who is this for, and where will they see it?</div>'
        '<div class="slide-body">A chart for a statistics-literate panel can carry more complexity than one for the '
        'general public. A chart for a printed report is read slowly and closely; one on a projector has three seconds '
        'from the back row. Design for the actual reader and the actual medium.</div>'
        '<div class="hbox"><div class="hbox-text">The most common failure is showing an analyst&rsquo;s working chart '
        '&mdash; dense, unlabelled, six series &mdash; to a public audience who needed one clear line.</div></div>')

content('<div class="section-label">Medium</div>'
        '<div class="slide-title md">Print, screen, mobile, projector</div>'
        '<table class="ctable"><thead><tr><th>Medium</th><th>Design for&hellip;</th></tr></thead><tbody>'
        '<tr><td>Print report</td><td>High detail, small fonts OK, must work in greyscale</td></tr>'
        '<tr><td>Web / screen</td><td>Interaction possible, but make it readable static-first</td></tr>'
        '<tr><td>Mobile</td><td>One idea, large text, vertical, few categories</td></tr>'
        '<tr><td>Projector / room</td><td>Big marks, high contrast, 3-second readability</td></tr>'
        '</tbody></table>'
        '<div class="hbox amber"><div class="hbox-text">A chart that works on a laptop can be unreadable on a phone or '
        'a projector. Test it where it will actually be seen.</div></div>')

content('<div class="section-label">Accessibility</div>'
        '<div class="slide-title md">Make charts readable by everyone</div>'
        '<ul class="bullet-list green">'
        '<li><strong>Contrast</strong>: dark text on light, light on dark &mdash; meet WCAG contrast ratios.</li>'
        '<li><strong>Font size</strong>: nothing smaller than the reader can comfortably read in the medium.</li>'
        '<li><strong>Alt text</strong>: describe the chart&rsquo;s point in words for screen-reader users.</li>'
        '<li><strong>Data table</strong>: offer the underlying numbers for those who can&rsquo;t use the visual.</li>'
        '</ul>'
        '<div class="hbox"><div class="hbox-text">Accessibility is not an add-on for a few users &mdash; high contrast '
        'and large type make a chart clearer for <em>everyone</em>.</div></div>')

content('<div class="section-label">Redundant coding</div>'
        '<div class="slide-title md">Never rely on colour alone</div>'
        '<div class="slide-body">Because some readers cannot distinguish certain colours &mdash; and because charts get '
        'printed in greyscale and photographed badly &mdash; pair every colour with a second cue. Then the chart still '
        'works when the colour is lost.</div>'
        '<ul class="bullet-list sm">'
        '<li>Lines: different dash patterns or direct labels as well as colour.</li>'
        '<li>Points: different shapes (circle, triangle, square) as well as colour.</li>'
        '<li>Categories on bars: direct labels so colour is a bonus, not the only key.</li>'
        '</ul>')

content('<div class="section-label">Data-ink</div>'
        '<div class="term-box"><div class="term-word">Data-ink ratio</div>'
        '<div class="term-def">Tufte&rsquo;s idea: of all the ink on a chart, what share actually encodes data? '
        'Maximise it. Every gridline, border, shadow and background that isn&rsquo;t carrying information is competing '
        'with the part that is.</div></div>'
        '<div class="hbox"><div class="hbox-text">Erase to improve: drop heavy gridlines, boxes and backgrounds, and '
        'the data stands out more. But don&rsquo;t strip away helpful labels in the name of minimalism &mdash; words are '
        'data-ink too.</div></div>')

content('<div class="section-label">Chartjunk</div>'
        '<div class="slide-title md">Cut the junk</div>'
        '<div class="slide-body"><strong>Chartjunk</strong> is decoration that adds no information and often subtracts '
        'clarity: 3D effects, gradients, clip-art, busy backgrounds, needless gridlines, redundant legends. It makes a '
        'chart look &ldquo;designed&rdquo; while making it harder to read.</div>'
        '<div class="hbox red"><div class="hbox-text">The test for any element: if removing it loses no information, '
        'remove it. What remains is the chart.</div></div>')

content('<div class="section-label">Motion &amp; interaction</div>'
        '<div class="slide-title md">Animate and interact &mdash; only when it helps</div>'
        '<div class="slide-body">Interaction (hover, filter, zoom) and animation (transitions between states) are '
        'powerful for <em>exploration</em> and for <em>showing change</em>. But a static reader sees none of it, and a '
        'gratuitous animation just delays the point. Always make the chart work as a still image first.</div>'
        '<ul class="bullet-list sm">'
        '<li>Good: animate a transition so the reader can follow what moved.</li>'
        '<li>Good: let users filter a big dataset to their own region.</li>'
        '<li>Bad: spinning, bouncing or fading that carries no meaning.</li>'
        '</ul>')

# ===================== SECTION 11 =====================
divider(11, "Section Eleven", "Workflow &amp; Tools")

content('<div class="section-label">The process</div>'
        '<div class="slide-title md">From data to finished chart</div>'
        '<div class="flow">'
        '<div class="flow-step"><div class="flow-num">1</div><div class="flow-label">Question</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">2</div><div class="flow-label">Get &amp; clean data</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">3</div><div class="flow-label">Explore (rough charts)</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">4</div><div class="flow-label">Choose &amp; refine</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">5</div><div class="flow-label">Annotate &amp; source</div></div>'
        '</div>'
        '<div class="hbox"><div class="hbox-text">Most of the work is steps 2 and 3 &mdash; cleaning the data and '
        'looking at it. The pretty final chart is the last 10%.</div></div>')

content('<div class="section-label">Sketch first</div>'
        '<div class="slide-title md">Pencil before pixels</div>'
        '<div class="slide-body">Before opening any tool, sketch the chart on paper. It costs seconds, forces you to '
        'decide what goes on each axis, and surfaces a better idea than the software&rsquo;s default. The tool should '
        'execute your decision, not make it for you.</div>'
        '<div class="hbox green"><div class="hbox-text">A rough sketch you can show a colleague in 30 seconds will '
        'save you an hour of polishing the wrong chart.</div></div>')

content('<div class="section-label">No-code tools</div>'
        '<div class="slide-title md">Tools: spreadsheets and chart builders</div>'
        '<ul class="bullet-list sm">'
        '<li><strong>Spreadsheets</strong> (Excel, Google Sheets, LibreOffice) &mdash; fine for quick exploration; '
        'fight their ugly defaults.</li>'
        '<li><strong>Datawrapper</strong> &mdash; free, makes honest, clean, responsive charts and maps fast; the '
        'newsroom standard.</li>'
        '<li><strong>Flourish</strong> &mdash; interactive and animated charts and stories, no code.</li>'
        '<li><strong>RAWGraphs</strong> &mdash; free, good for less common chart types (Sankey, beeswarm).</li>'
        '</ul>'
        '<div class="hbox"><div class="hbox-text">For most practitioners, Datawrapper covers 80% of needs and is hard '
        'to make ugly. Start there.</div></div>')

content('<div class="section-label">Code tools</div>'
        '<div class="slide-title md">Tools: when you want full control</div>'
        '<table class="ctable"><thead><tr><th>Tool</th><th>Good for</th></tr></thead><tbody>'
        '<tr><td>Python (matplotlib, seaborn, plotly)</td><td>Analysis-to-chart in one place; reproducible</td></tr>'
        '<tr><td>R (ggplot2)</td><td>Statistical graphics; the grammar of graphics done well</td></tr>'
        '<tr><td>D3.js / Observable</td><td>Bespoke, interactive web visuals; full control</td></tr>'
        '<tr><td>Vega-Lite</td><td>Declarative charts from a JSON spec</td></tr>'
        '</tbody></table>'
        '<div class="hbox indigo"><div class="hbox-text">Code wins when you need reproducibility, automation, or a '
        'chart no tool offers. The charts on The Long View are hand-built in SVG for exactly this reason.</div></div>')

content('<div class="section-label">Finding data</div>'
        '<div class="slide-title md">Where to find good data (South Asia)</div>'
        '<ul class="bullet-list sm">'
        '<li><strong>India</strong>: NFHS, Census, NSS, PLFS, data.gov.in, RBI, budget documents.</li>'
        '<li><strong>Global</strong>: World Bank, UN agencies (WHO, UNICEF, UN DESA), Our World in Data.</li>'
        '<li><strong>Climate</strong>: IPCC, EDGAR, Global Carbon Project, national communications.</li>'
        '<li><strong>Always</strong>: read the methodology, note the year, check the definition before you plot.</li>'
        '</ul>'
        '<div class="hbox"><div class="hbox-text">ImpactMojo&rsquo;s <strong>Dataverse</strong> collects vetted '
        'development datasets for South Asia in one place.</div></div>')

content('<div class="section-label">Learn from</div>'
        '<div class="slide-title md">People and places to learn from</div>'
        '<ul class="bullet-list sm">'
        '<li><strong>Our World in Data</strong> &mdash; a master-class in clear, sourced development charts.</li>'
        '<li><strong>The Financial Times &amp; The Economist</strong> visual teams &mdash; and the FT&rsquo;s public '
        '&ldquo;Visual Vocabulary&rdquo;.</li>'
        '<li><strong>VizChitra</strong> &mdash; India&rsquo;s data-visualisation community and conference.</li>'
        '<li><strong>The Pudding, Reuters Graphics, IndiaSpend</strong> for data journalism in context.</li>'
        '</ul>'
        '<div class="hbox green"><div class="hbox-text">The fastest way to improve: find a chart you admire and work '
        'out, element by element, why it works.</div></div>')

content('<div class="section-label">Read</div>'
        '<div class="slide-title md">Further reading</div>'
        '<ul class="bullet-list sm">'
        '<li>Edward Tufte &mdash; <em>The Visual Display of Quantitative Information</em></li>'
        '<li>Alberto Cairo &mdash; <em>The Truthful Art</em> and <em>How Charts Lie</em></li>'
        '<li>Cole Nussbaumer Knaflic &mdash; <em>Storytelling with Data</em></li>'
        '<li>Tamara Munzner &mdash; <em>Visualization Analysis &amp; Design</em> (the marks-and-channels theory)</li>'
        '<li>Catherine D&rsquo;Ignazio &amp; Lauren Klein &mdash; <em>Data Feminism</em> (power and data)</li>'
        '</ul>')

content('<div class="section-label">Practice</div>'
        '<div class="slide-title md">Get better by redrawing</div>'
        '<div class="slide-body">Theory only takes you so far. Pick one chart a week &mdash; from a newspaper, a report, '
        'your own work &mdash; and redraw it better. Decide what it is for, fix the encoding, cut the junk, write a '
        'finding title, add the source. Keep the before-and-after.</div>'
        '<div class="hbox indigo"><div class="hbox-text">Then explore ImpactMojo&rsquo;s <strong>The Long View</strong> '
        '&mdash; every chart there is built from real, cited data, with notes on why that chart type and what to look '
        'for. It is this course, made concrete.</div></div>')

# ---- s99 recap ----
content('<div class="section-label">In one slide</div>'
        '<div class="slide-title md">The whole course as a checklist</div>'
        '<div class="two-col half">'
        '<div class="col-panel green"><div class="col-panel-title">Before you draw</div>'
        '<div class="slide-body sm">&bull; What is the one question?<br>&bull; Comparison, trend, part, spread or link?<br>'
        '&bull; Which channel carries the key variable?<br>&bull; Who reads it, and where?</div></div>'
        '<div class="col-panel"><div class="col-panel-title">Before you publish</div>'
        '<div class="slide-body sm">&bull; Bars from zero; areas by area<br>&bull; Full, fair time window<br>'
        '&bull; Title states the finding, honestly<br>&bull; Colour-blind safe, not colour-only<br>'
        '&bull; Units, source, date on the chart</div></div>'
        '</div>'
        '<div class="hbox"><div class="hbox-text">Honest first, clear second, beautiful third &mdash; in that order, '
        'always.</div></div>')

# ---- s100 end ----
slides.append(('end', None))

assert len(slides) == 100, "Expected 100 slides, got %d" % len(slides)

# ----------------- build slide HTML -----------------
parts = []
TITLE_GEO = ('<div class="title-geo"><svg viewBox="0 0 300 620" xmlns="http://www.w3.org/2000/svg" '
             'style="width:100%;height:100%"><defs><pattern id="hex" x="0" y="0" width="40" height="46" '
             'patternUnits="userSpaceOnUse"><polygon points="20,2 38,12 38,34 20,44 2,34 2,12" fill="none" '
             'stroke="white" stroke-width="1"/></pattern></defs><rect width="300" height="620" fill="url(#hex)"/>'
             '</svg></div>')

for i, (kind, payload) in enumerate(slides):
    n = i + 1
    sid = 's%d' % n
    active = ' active' if n == 1 else ''
    if kind == 'title':
        body = ('<div class="title-screen"><div class="title-bg"></div><div class="title-bar"></div>'
                '<div class="title-content"><div class="title-series">ImpactMojo 101 Series &middot; Free Forever</div>'
                '<div class="title-main">Data<br>Visualization<br>101</div>'
                '<div class="title-sub">How to turn numbers into honest, clear pictures &mdash; a foundational course '
                'for development practitioners in South Asia, and the companion to ImpactMojo&rsquo;s '
                '<em>The Long View</em>.</div>'
                '<div class="title-tags"><span class="title-tag">Practical</span>'
                '<span class="title-tag">South Asia Focus</span><span class="title-tag">100 Slides</span>'
                '<span class="title-tag">Free Access</span></div></div>' + TITLE_GEO + '</div>')
    elif kind == 'toc':
        items = ''
        for j, (name, rng) in enumerate(payload):
            items += ('<div class="toc-item"><div class="toc-num">%02d</div><div class="toc-name">%s</div>'
                      '<div class="toc-slides">Slides %s</div></div>' % (j + 1, name, rng))
        body = ('<div class="slide-content"><div class="section-label">Agenda</div>'
                '<div class="slide-title md" style="margin-bottom:8px">What We Cover</div>'
                '<div class="toc-grid">' + items + '</div></div>')
    elif kind == 'divider':
        num, label, title = payload
        body = ('<div class="section-divider"><div class="div-num">%02d</div>'
                '<div class="div-label">%s</div><div class="div-title">%s</div>'
                '<div class="div-accent"></div></div>' % (num, label, title))
    elif kind == 'end':
        body = ('<div class="end-screen"><div class="end-bar"></div><div class="end-pattern"></div>'
                '<div class="end-glow"></div><div class="end-content">'
                '<div class="end-eyebrow">ImpactMojo 101 Series</div>'
                '<div class="end-headline">Now go<br>draw it.</div>'
                '<div class="end-byline">You now have the questions to ask, the chart families to choose from, and '
                'the integrity checks to pass. The rest is practice &mdash; one chart at a time.</div>'
                '<div class="end-cta">'
                '<a class="end-btn end-btn-primary" href="https://www.impactmojo.in/the-long-view.html" target="_blank">Explore The Long View</a>'
                '<a class="end-btn end-btn-secondary" href="https://www.impactmojo.in/101-courses/" target="_blank">More 101 Courses</a>'
                '<a class="end-btn end-btn-tertiary" href="https://www.impactmojo.in/101-courses/data-lit.html" target="_blank">Data Literacy 101</a>'
                '</div>'
                '<div class="end-meta"><span>Free Forever</span><span class="end-meta-divider">&middot;</span>'
                '<span>CC BY-NC-ND 4.0</span><span class="end-meta-divider">&middot;</span>'
                '<span>www.impactmojo.in</span></div></div></div>')
    else:  # content
        body = '<div class="slide-content">' + payload + '</div>'

    parts.append('<div class="slide%s" id="%s">%s%s%s</div>' % (active, sid, header(), body, footer(n)))

slides_html = '\n\n'.join(parts)

# ----------------- main JS: swap SLIDE_IDS + chart block -----------------
ids = "['" + "','".join('s%d' % k for k in range(1, 101)) + "']"
mainjs = re.sub(r"const SLIDE_IDS = \[[^\]]*\];", "const SLIDE_IDS = " + ids + ";", MAINJS, count=1)

head = mainjs[:mainjs.index('// Charts')]
tail = mainjs[mainjs.index('// Theme'):]

CHARTS = """// Charts
const CHART_DEFAULTS = {
  responsive: true, maintainAspectRatio: false,
  plugins: { legend: { labels: { font: { family: 'JetBrains Mono', size: 10 }, color: '#78716C' } } },
  scales: {
    x: { ticks: { font: { family: 'JetBrains Mono', size: 9 }, color: '#78716C' }, grid: { color: 'rgba(0,0,0,0.05)' } },
    y: { ticks: { font: { family: 'JetBrains Mono', size: 9 }, color: '#78716C' }, grid: { color: 'rgba(0,0,0,0.05)' } }
  }
};

function initChart(slideIdx) {
  const id = SLIDE_IDS[slideIdx];
  const mk = (cid, type, data, opts) => {
    const el = document.getElementById(cid);
    if (!el) return;
    new Chart(el, { type, data, options: { ...CHART_DEFAULTS, ...opts } });
  };

  if (id === 's29') {
    mk('u5mChart', 'bar', {labels:['Pakistan','India','Nepal','Bangladesh','Bhutan','Maldives','Sri Lanka'],
      datasets:[{label:'Deaths per 1,000 live births', data:[63,31,28,27,25,7,7], backgroundColor:'#EF4444'}]},
      { indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, beginAtZero:true } } });
  }
  if (id === 's32') {
    mk('truncChart', 'bar', {labels:['2019','2021','2023'],
      datasets:[{label:'Coverage %', data:[92,94,96], backgroundColor:'#EF4444'}]},
      { plugins:{legend:{display:false}}, scales:{ y:{ min:90, max:97 } } });
    mk('honestChart', 'bar', {labels:['2019','2021','2023'],
      datasets:[{label:'Coverage %', data:[92,94,96], backgroundColor:'#10B981'}]},
      { plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100 } } });
  }
  if (id === 's66') {
    mk('skewChart', 'line', {labels:['0','1','2','3','4','5','6','7','8','9','10'],
      datasets:[
        {label:'Symmetric', data:[1,3,8,16,24,28,24,16,8,3,1], borderColor:'#10B981', tension:0.4, pointRadius:0, fill:false},
        {label:'Right-skewed (e.g. income)', data:[2,18,28,24,16,10,6,4,2,1,0.5], borderColor:'#EF4444', tension:0.4, pointRadius:0, fill:false}
      ]}, {});
  }
  if (id === 's71') {
    mk('moeChart', 'line', {labels:['100','200','400','600','1000','1500','2400','4000'],
      datasets:[{label:'Margin of error (±%)', data:[9.8,6.9,4.9,4.0,3.1,2.5,2.0,1.5],
        borderColor:'#0EA5E9', backgroundColor:'rgba(14,165,233,0.08)', fill:true, tension:0.3, pointRadius:4}]},
      { plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'± percentage points'} } } });
  }
}


"""

mainjs = head + CHARTS + tail

# ----------------- assemble file -----------------
META_DESC = ("Data Visualization 101 - a free foundational course for development practitioners in South Asia. "
             "How to turn numbers into honest, clear charts: marks and channels, choosing a chart type, avoiding "
             "misleading visuals, colour, annotation, tables, distributions, maps and accessibility. ImpactMojo, "
             "CC BY-NC-ND.")

HEAD = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>Data Visualization 101 | ImpactMojo</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Amaranth:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">\n'
        '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>\n'
        + CSS + '\n'
        '<!-- Google Analytics -->\n'
        '<script async src="https://www.googletagmanager.com/gtag/js?id=G-JRCMEB9TBW"></script>\n'
        "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-JRCMEB9TBW');</script>\n"
        '<!-- SEO meta -->\n'
        '<meta name="description" content="' + META_DESC + '">\n'
        '<meta name="robots" content="index, follow">\n'
        '<link rel="canonical" href="https://www.impactmojo.in/101-courses/data-viz.html">\n'
        '<meta property="og:title" content="Data Visualization 101">\n'
        '<meta property="og:description" content="' + META_DESC + '">\n'
        '<meta property="og:image" content="https://www.impactmojo.in/assets/images/ImpactMojo%20Logo.png">\n'
        '<meta property="og:url" content="https://www.impactmojo.in/101-courses/data-viz.html">\n'
        '<meta property="og:type" content="website">\n'
        '<meta property="og:site_name" content="ImpactMojo">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<meta name="twitter:title" content="Data Visualization 101">\n'
        '<meta name="twitter:description" content="' + META_DESC + '">\n'
        '<meta name="twitter:image" content="https://www.impactmojo.in/assets/images/ImpactMojo%20Logo.png">\n'
        '<link rel="icon" type="image/png" href="/assets/images/favicon.png">\n'
        '<link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">\n'
        '</head>\n<body>\n\n')

THEMEBAR = ('<div id="theme-bar">\n <button class="theme-btn" onclick="setTheme(\'system\')">System</button>\n'
            ' <button class="theme-btn active" onclick="setTheme(\'light\')">Light</button>\n'
            ' <button class="theme-btn" onclick="setTheme(\'dark\')">Dark</button>\n</div>\n\n')

NAV = ('<div id="nav">\n <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)">&#8249;</button>\n'
       ' <span id="prog-text">1 / 100</span>\n'
       ' <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)">&#8250;</button>\n</div>\n\n')

doc = (HEAD + THEMEBAR + SPRITE + '\n\n'
       '<div id="progress-bar"></div>\n<div id="fs-hint" onclick="toggleFS()">fullscreen</div>\n'
       '<div id="deck">\n <div class="slide-viewport" id="viewport">\n\n'
       + slides_html +
       '\n\n </div>\n</div><!-- /deck -->\n\n'
       + NAV +
       '<script>\n' + mainjs + '</script>\n\n'
       '<script>\n' + POLISHJS + '</script>\n\n'
       '<script src="/js/translate-sarvam.js" defer></script>\n</body>\n</html>\n')

open(OUT, 'w').write(doc)
print('Wrote', OUT, '-', len(doc), 'bytes,', len(slides), 'slides')
