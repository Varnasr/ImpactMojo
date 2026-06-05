# -*- coding: utf-8 -*-
"""
Data Literacy 101 — ImpactMojo 101 Series (native deck spec)
Foundational data literacy for South Asian development practitioners.
Build: python3 scripts/deck-builder/build.py data_lit
"""

DECK = {
    "slug": "data-lit",
    "title": "Data Literacy 101",
    "description": ("Data Literacy 101 — a free foundational course for development "
                    "practitioners in South Asia. Read, question, visualise and use data "
                    "responsibly: from India's data ecosystem to sampling, distributions, "
                    "correlation, data quality and ethics. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Data<br>Literacy<br>101",
         "sub": "Reading, Questioning &amp; Using Data Responsibly &mdash; a Foundational "
                "Course for Development Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Is Data Literacy?", "slides": "Slides 3&ndash;9"},
             {"name": "Types &amp; Sources of Data", "slides": "Slides 10&ndash;19"},
             {"name": "From Concept to Indicator", "slides": "Slides 20&ndash;28"},
             {"name": "Describing Data", "slides": "Slides 29&ndash;38"},
             {"name": "Visualising Data", "slides": "Slides 39&ndash;49"},
             {"name": "Relationships &amp; Correlation", "slides": "Slides 50&ndash;58"},
             {"name": "Sampling &amp; Surveys", "slides": "Slides 59&ndash;67"},
             {"name": "Data Quality &amp; Cleaning", "slides": "Slides 68&ndash;75"},
             {"name": "Reading Data Critically", "slides": "Slides 76&ndash;84"},
             {"name": "Data Ethics, Privacy &amp; Equity", "slides": "Slides 85&ndash;91"},
             {"name": "Tools &amp; Further Reading", "slides": "Slides 92&ndash;94"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Is Data Literacy?"},

        {"type": "content", "label": "Definition", "title": "Data literacy is a survival skill",
         "blocks": [
             {"t": "body", "html": "Development work runs on numbers &mdash; targets, indicators, "
              "budgets, surveys, dashboards. <strong>Data literacy</strong> is the ability to "
              "read, question, interpret and communicate data, and to use it to make better "
              "decisions. It is not statistics for its own sake; it is judgement."},
             {"t": "term", "word": "Data literacy",
              "def": "The capacity to find, read, interpret, critically evaluate and "
              "communicate with data &mdash; and to recognise when data is being misused. "
              "It sits between raw numbers and good decisions."},
             {"t": "hbox", "color": "cyan", "html": "You do not need to be a statistician. "
              "You need to ask the right questions of any number that lands on your desk."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "Decisions you already make with data",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Programme decisions", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Which blocks or wards to prioritise",
                      "Whether an intervention is working",
                      "How to set a realistic target",
                      "Where the budget actually goes"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Daily judgement calls", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Is this survey finding trustworthy?",
                      "Does this chart mislead?",
                      "Is the sample like our population?",
                      "Who is missing from this count?"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Every one of these is a data-literacy "
              "question before it is a technical one."},
         ]},

        {"type": "content", "label": "The Ladder", "title": "Data &rarr; Information &rarr; Knowledge &rarr; Decision",
         "blocks": [
             {"t": "flow", "steps": [
                 "DATA: raw records &mdash; 1,240 children weighed",
                 "INFORMATION: 18% are underweight",
                 "KNOWLEDGE: underweight is concentrated in 3 hamlets",
                 "DECISION: target supplementary feeding there"]},
             {"t": "hbox", "color": "green", "html": "Data literacy is what moves you up the "
              "ladder without slipping &mdash; each step adds interpretation, and each step "
              "can introduce error."},
         ]},

        {"type": "content", "label": "Mindset", "title": "Five habits of a data-literate practitioner",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Ask where it came from.</strong> Who collected it, when, how, and why?",
                 "<strong>Ask what it measures.</strong> Is the indicator really capturing the concept?",
                 "<strong>Ask who is missing.</strong> Whom does this number leave out?",
                 "<strong>Ask how sure we are.</strong> What is the uncertainty, the sample, the error?",
                 "<strong>Ask what decision it serves.</strong> Data without a question is noise."]},
         ]},

        {"type": "content", "label": "Caution", "title": "Numbers feel objective. They are not neutral.",
         "blocks": [
             {"t": "quote",
              "text": "Not everything that counts can be counted, and not everything that "
              "can be counted counts.",
              "attr": "&mdash; commonly attributed to William Bruce Cameron"},
             {"t": "body", "html": "Every dataset embeds choices: what to measure, what category "
              "to use, whom to ask, what to ignore. Those choices carry power. A data-literate "
              "practitioner reads the choices, not just the digits."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Foundations", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Types and sources of data",
                      "Turning concepts into indicators",
                      "Describing and visualising data"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Judgement", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Correlation, sampling and surveys",
                      "Data quality and critical reading",
                      "Ethics, privacy and equity"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Throughout, examples come from India and "
              "the wider region &mdash; the data you will actually meet at work."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Types &amp; Sources of Data"},

        {"type": "content", "label": "Two Families", "title": "Quantitative and qualitative",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Quantitative", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Numbers and counts &mdash; how many, how "
                   "much, how often. Strong for measuring scale, comparing groups, tracking change."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Qualitative", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Words, meanings, experiences &mdash; why, "
                   "how, in what context. Strong for understanding process, mechanism and lived reality."}]}]},
             {"t": "hbox", "color": "amber", "html": "They are partners, not rivals. Numbers tell "
              "you <em>that</em> something changed; stories tell you <em>why</em>. The best "
              "evidence usually uses both."},
         ]},

        {"type": "content", "label": "Provenance", "title": "Primary vs secondary data",
         "blocks": [
             {"t": "table",
              "head": ["", "Primary", "Secondary"],
              "rows": [
                  ["Source", "You collect it", "Someone else collected it"],
                  ["Example", "Your baseline survey, FGDs", "Census, NFHS, district HMIS"],
                  ["Control", "High &mdash; you design it", "Low &mdash; you take it as given"],
                  ["Cost / time", "High", "Usually low"],
                  ["Risk", "Fieldwork error, bias", "May not fit your question"]]},
             {"t": "hbox", "color": "cyan", "html": "Rule of thumb: <strong>exhaust good "
              "secondary data before collecting primary data.</strong> Much of what you need "
              "already exists &mdash; and re-collecting it wastes respondents' time."},
         ]},

        {"type": "content", "label": "Structure", "title": "Structured, semi-structured, unstructured",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Structured", "label": "Neat rows &amp; columns &mdash; survey tables, "
                  "registers, spreadsheets", "color": "cyan"},
                 {"num": "Semi", "label": "Some structure &mdash; forms with open text, tagged "
                  "records, JSON", "color": "indigo"},
                 {"num": "Unstructured", "label": "Free text, audio, images, video, field notes",
                  "color": "amber"}]},
             {"t": "body", "html": "Most development M&amp;E lives in structured data, but a "
              "growing share &mdash; call-centre logs, photos, social media, satellite imagery "
              "&mdash; is unstructured and needs different tools."},
         ]},

        {"type": "content", "label": "Forms of Data", "title": "Cross-section, time series, panel",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [
                  {"t": "bullets", "items": [
                      "<strong>Cross-section:</strong> many units at one time (one NFHS round)",
                      "<strong>Time series:</strong> one unit over time (national TFR, 1990&ndash;2024)",
                      "<strong>Panel / longitudinal:</strong> same units tracked over time "
                      "(a cohort re-surveyed every year)"]}],
              "right": [
                  {"t": "hbox", "color": "green", "html": "Panel data is powerful &mdash; it can "
                   "follow the <em>same</em> household as it changes, separating real change from "
                   "differences between households."}]},
         ]},

        {"type": "content", "label": "India's Backbone", "title": "India's official data ecosystem",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Source", "What it covers", "Frequency"],
              "rows": [
                  ["Census of India", "Every person &mdash; population, literacy, housing, migration", "Decennial (2011 latest)"],
                  ["NFHS", "Health, nutrition, fertility, anaemia, women's status", "~5 years (NFHS-5: 2019&ndash;21)"],
                  ["NSS / PLFS", "Consumption, employment, unemployment", "PLFS annual since 2017&ndash;18"],
                  ["SRS", "Birth &amp; death rates, infant mortality, life expectancy", "Annual"],
                  ["HMIS", "Facility-level health service delivery", "Monthly"],
                  ["SECC 2011", "Socio-economic &amp; caste deprivation indicators", "One-off (2011)"]]},
             {"t": "hbox", "color": "amber", "html": "Know these by name. Most of your "
              "secondary-data needs are met by one of them &mdash; free and downloadable."},
         ]},

        {"type": "content", "label": "Sample vs Census", "title": "NFHS, NSS and the Census do different jobs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Census = everyone", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Counts <em>every</em> person. Best for small-area "
                   "detail (a village, a ward). Expensive, so it is rare."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Surveys = a sample", "blocks": [
                  {"t": "body", "cls": "sm", "html": "NFHS &amp; NSS interview a carefully chosen "
                   "<em>sample</em> and infer the whole. Cheaper, frequent &mdash; but only reliable "
                   "down to the level they were designed for (usually state or district)."}]}]},
             {"t": "hbox", "color": "red", "html": "Common error: using a state-level survey "
              "estimate to make claims about a single block. The sample was never designed to "
              "say anything that local."},
         ]},

        {"type": "content", "label": "Scale", "title": "How big are these datasets?",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "1.21 bn", "label": "people enumerated in Census 2011", "color": "cyan",
                  "source": "Census of India 2011"},
                 {"num": "~636,000", "label": "households interviewed in NFHS-5", "color": "green",
                  "source": "NFHS-5, 2019&ndash;21"},
                 {"num": "707", "label": "districts covered by NFHS-5", "color": "indigo",
                  "source": "IIPS / MoHFW"}]},
             {"t": "body", "html": "These are among the largest demographic and health surveys in "
              "the world. Their size is what lets them speak reliably about districts &mdash; but "
              "not about your single panchayat."},
         ]},

        {"type": "content", "label": "Administrative Data", "title": "The data your programme already generates",
         "blocks": [
             {"t": "body", "html": "Every scheme produces <strong>administrative data</strong> as "
              "a by-product of delivery: MGNREGA muster rolls, school enrolment (UDISE+), health "
              "records (HMIS), ration transactions, immunisation registers."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Strengths", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Continuous, cheap, already collected",
                      "Universal coverage of beneficiaries",
                      "Real-time-ish monitoring"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Watch-outs", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Records who is served, not who is missed",
                      "Incentives to over- or under-report",
                      "Gaps, duplicates, stale entries"]}]}]},
         ]},

        {"type": "content", "label": "New Frontiers", "title": "Big data and digital traces",
         "blocks": [
             {"t": "body", "html": "Mobile-phone records, satellite night-lights, transaction "
              "logs and remote sensing increasingly supplement official statistics &mdash; "
              "useful where surveys are slow or coverage is thin."},
             {"t": "hbox", "color": "amber", "html": "But digital traces over-represent the "
              "connected and under-represent the poor, women, the elderly and remote areas. "
              "Big data can deepen exclusion if read uncritically."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "From Concept to Indicator"},

        {"type": "content", "label": "The Core Problem", "title": "You cannot measure 'wellbeing' directly",
         "blocks": [
             {"t": "body", "html": "Most things we care about &mdash; poverty, empowerment, "
              "health, learning &mdash; are <strong>concepts</strong>, not numbers. Measurement "
              "is the bridge from an abstract concept to an observable indicator."},
             {"t": "flow", "steps": [
                 "CONCEPT: women's empowerment",
                 "DIMENSIONS: mobility, decision-making, assets",
                 "INDICATORS: % who can visit a health centre alone",
                 "DATA: survey responses"]},
         ]},

        {"type": "content", "label": "Definition", "title": "Indicators, defined",
         "blocks": [
             {"t": "term", "word": "Indicator",
              "def": "An observable, measurable marker that stands in for something we cannot "
              "observe directly. A good indicator is a faithful proxy for the concept &mdash; "
              "no more, no less."},
             {"t": "term", "word": "Operationalisation",
              "def": "The precise rule that turns a concept into a measurement: exactly what "
              "to count, for whom, over what period, in what units."},
         ]},

        {"type": "content", "label": "Levels of Measurement", "title": "Four kinds of variable",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Level", "Meaning", "Example", "Valid maths"],
              "rows": [
                  ["Nominal", "Labels, no order", "District, caste, religion", "Counts, mode"],
                  ["Ordinal", "Ordered, unequal gaps", "Wealth quintile, Likert scale", "Median, rank"],
                  ["Interval", "Equal gaps, no true zero", "Temperature (&deg;C), calendar year", "Mean, difference"],
                  ["Ratio", "Equal gaps, true zero", "Income, age, children ever born", "All, ratios"]]},
             {"t": "hbox", "color": "red", "html": "Why it matters: you cannot take a meaningful "
              "<em>average</em> of caste categories, and a wealth quintile is a rank, not a rupee "
              "amount. The level decides which statistics are legal."},
         ]},

        {"type": "content", "label": "Good Indicators", "title": "What makes an indicator trustworthy?",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Valid", "label": "Measures what it claims to measure", "color": "cyan"},
                 {"num": "Reliable", "label": "Gives the same answer on repeat measurement", "color": "green"},
                 {"num": "Sensitive", "label": "Moves when the real thing moves", "color": "indigo"},
                 {"num": "Feasible", "label": "Can actually be collected, affordably", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Validity vs Reliability", "title": "Accurate is not the same as consistent",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Reliable, not valid", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A miscalibrated weighing scale: it reads "
                   "2&nbsp;kg high <em>every</em> time. Perfectly consistent &mdash; consistently wrong."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Valid and reliable", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A calibrated scale: same answer each time, "
                   "and the right answer. This is the target."}]}]},
             {"t": "hbox", "color": "amber", "html": "You can have reliability without validity, "
              "but never validity without reliability. Check both."},
         ]},

        {"type": "content", "label": "Proxies", "title": "When you measure A to learn about B",
         "blocks": [
             {"t": "body", "html": "A <strong>proxy</strong> stands in for something hard to "
              "measure. Household assets proxy for wealth; night-light intensity proxies for "
              "economic activity; mid-upper-arm circumference proxies for acute malnutrition."},
             {"t": "hbox", "color": "red", "html": "Every proxy leaks. Asset indices miss debt; "
              "night-lights miss the informal economy. Name the gap between your proxy and the "
              "concept &mdash; and report it."},
         ]},

        {"type": "content", "label": "Composite Indices", "title": "Bundling many indicators into one number",
         "blocks": [
             {"t": "body", "html": "Indices like the <strong>Human Development Index</strong> or "
              "the <strong>Multidimensional Poverty Index (MPI)</strong> combine several "
              "indicators into a single score for easy comparison."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Upside", "blocks": [
                  {"t": "body", "cls": "sm", "html": "One memorable number; ranks and headlines; "
                   "captures several dimensions at once."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Downside", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Weights are value judgements; aggregation "
                   "hides trade-offs; a good score can mask a terrible component."}]}]},
         ]},

        {"type": "content", "label": "Worked Example", "title": "India's National MPI",
         "blocks": [
             {"t": "body", "html": "NITI Aayog's National MPI bundles 12 indicators across "
              "<strong>health, education and standard of living</strong> &mdash; nutrition, child "
              "mortality, schooling, cooking fuel, sanitation, housing, assets and more."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "12", "label": "indicators in 3 dimensions", "color": "cyan",
                  "source": "NITI Aayog National MPI"},
                 {"num": "Headcount &times; Intensity", "label": "MPI = share who are poor &times; "
                  "how deeply poor they are", "color": "indigo"}]},
             {"t": "hbox", "color": "cyan", "html": "Notice the design choice: a household is "
              "'MPI poor' if deprived in a weighted third or more of indicators. Change that "
              "threshold and the poverty rate changes."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Describing Data"},

        {"type": "content", "label": "First Question", "title": "Where is the centre? How spread out?",
         "blocks": [
             {"t": "body", "html": "Before any fancy analysis, describe the data. Two questions "
              "answer most of it: <strong>what is typical</strong> (central tendency) and "
              "<strong>how much do values vary</strong> (dispersion)."},
             {"t": "flow", "steps": [
                 "CENTRE: mean, median, mode",
                 "SPREAD: range, IQR, standard deviation",
                 "SHAPE: skew, peaks, outliers"]},
         ]},

        {"type": "content", "label": "Central Tendency", "title": "Mean, median and mode",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Measure", "What it is", "Best when"],
              "rows": [
                  ["Mean", "Arithmetic average", "Roughly symmetric data, no wild outliers"],
                  ["Median", "Middle value when sorted", "Skewed data &mdash; income, land, wealth"],
                  ["Mode", "Most frequent value", "Categories &mdash; commonest crop, caste, response"]]},
             {"t": "hbox", "color": "amber", "html": "For money &mdash; income, consumption, "
              "landholding &mdash; prefer the <strong>median</strong>. A few crorepatis drag the "
              "mean far above what a typical household actually has."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "Mean vs median: the same village, two stories",
         "blocks": [
             {"t": "chart", "canvas": "meanMedianChart", "title": "Monthly income, 11 households (₹000s)",
              "source": "Illustrative example",
              "type": "bar",
              "data": {"labels": ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11"],
                       "datasets": [{"label": "Income (₹000/month)",
                                     "data": [8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 220],
                                     "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ plugins:{ legend:{ display:false } } }"}},
             {"t": "hbox", "color": "red", "html": "<strong>Median = ₹12k</strong> (typical "
              "household). <strong>Mean = ₹31k</strong>, pulled up by one rich household. Report "
              "the mean here and you describe a village that does not exist."},
         ]},

        {"type": "content", "label": "Dispersion", "title": "Spread: range, IQR and standard deviation",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Range:</strong> max &minus; min. Simple, but one outlier wrecks it.",
                 "<strong>IQR (interquartile range):</strong> the middle 50% &mdash; robust to outliers.",
                 "<strong>Standard deviation:</strong> typical distance from the mean. The "
                 "everyday measure of variability."]},
             {"t": "hbox", "color": "cyan", "html": "Two districts can share the same average "
              "income yet feel completely different &mdash; one equal, one polarised. The mean "
              "hides that; the spread reveals it."},
         ]},

        {"type": "content", "label": "Percentiles", "title": "Percentiles, quartiles and quintiles",
         "blocks": [
             {"t": "body", "html": "A <strong>percentile</strong> is the value below which a given "
              "share of cases fall. The 25th percentile (Q1) has a quarter of households below it. "
              "Wealth <strong>quintiles</strong> &mdash; five 20% bands &mdash; are how NFHS and "
              "NSS routinely report inequality."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Q1&ndash;Q5", "label": "Quintiles: five equal-size groups", "color": "cyan"},
                 {"num": "p50", "label": "The 50th percentile is the median", "color": "green"},
                 {"num": "p90/p10", "label": "A common inequality ratio", "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Distributions", "title": "The shape of the data matters",
         "blocks": [
             {"t": "chart", "canvas": "distShapeChart", "title": "Symmetric vs right-skewed distributions",
              "source": "Illustrative",
              "type": "line",
              "data": {"labels": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                       "datasets": [
                           {"label": "Symmetric (e.g. height)",
                            "data": [1, 3, 8, 16, 24, 28, 24, 16, 8, 3, 1],
                            "borderColor": "#10B981", "tension": 0.4, "pointRadius": 0, "fill": False},
                           {"label": "Right-skewed (e.g. income)",
                            "data": [2, 18, 28, 24, 16, 10, 6, 4, 2, 1, 0.5],
                            "borderColor": "#EF4444", "tension": 0.4, "pointRadius": 0, "fill": False}]}},
             {"t": "hbox", "color": "amber", "html": "Income, landholding and firm size are "
              "almost always <strong>right-skewed</strong> &mdash; a long tail of large values. "
              "That is exactly when the mean misleads."},
         ]},

        {"type": "content", "label": "The Normal Curve", "title": "The bell curve and the 68&ndash;95&ndash;99.7 rule",
         "blocks": [
             {"t": "body", "html": "Many natural measurements (height, birth weight, "
              "measurement error) follow a roughly <strong>normal</strong> distribution &mdash; "
              "symmetric, bell-shaped, defined by its mean and standard deviation (SD)."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "68%", "label": "of values fall within 1 SD of the mean", "color": "cyan"},
                 {"num": "95%", "label": "fall within 2 SD", "color": "green"},
                 {"num": "99.7%", "label": "fall within 3 SD", "color": "indigo"}]},
             {"t": "hbox", "color": "red", "html": "But do not assume normality. Development data "
              "&mdash; income, expenditure, programme size &mdash; is usually skewed, so the rule "
              "does not apply. Always look at the shape first."},
         ]},

        {"type": "content", "label": "Outliers", "title": "Outliers: error, or the most important case?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Could be an error", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A 9-foot-tall respondent, a household of 80, "
                   "an income of ₹0 &mdash; check for data-entry slips before analysing."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Could be the story", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The one block with triple the dropout rate "
                   "may be precisely where the programme is needed. Do not delete it &mdash; "
                   "investigate it."}]}]},
             {"t": "hbox", "color": "amber", "html": "Never silently drop outliers. Flag them, "
              "explain them, and decide transparently."},
         ]},

        {"type": "content", "label": "Rates vs Counts", "title": "Always ask: out of how many?",
         "blocks": [
             {"t": "body", "html": "A raw <strong>count</strong> without its denominator is "
              "almost meaningless. '500 dropouts' could be a crisis or a triumph depending on "
              "whether the base is 600 or 60,000."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Count", "label": "How many? (numerator alone)", "color": "amber"},
                 {"num": "Rate", "label": "How many out of how many? (numerator &divide; "
                  "denominator)", "color": "green"}]},
             {"t": "hbox", "color": "cyan", "html": "The denominator is where most honest "
              "comparison lives &mdash; per 1,000 people, per eligible child, per year. Demand it."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Visualising Data"},

        {"type": "content", "label": "Why Visualise", "title": "A good chart is an argument you can see",
         "blocks": [
             {"t": "body", "html": "Visualisation is not decoration. A well-made chart reveals "
              "patterns the table hides &mdash; trends, gaps, outliers, relationships &mdash; and "
              "lets a busy decision-maker grasp them in seconds."},
             {"t": "quote", "text": "The greatest value of a picture is when it forces us to "
              "notice what we never expected to see.",
              "attr": "&mdash; John Tukey, pioneer of exploratory data analysis"},
         ]},

        {"type": "content", "label": "Match Chart to Job", "title": "Pick the chart for the question",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["You want to show&hellip;", "Use", "Avoid"],
              "rows": [
                  ["Change over time", "Line chart", "Pie chart"],
                  ["Comparison across categories", "Bar chart", "3-D anything"],
                  ["Composition / shares of a whole", "Stacked bar (or 1 pie, few slices)", "Many pies"],
                  ["Relationship between two variables", "Scatter plot", "Dual-axis tricks"],
                  ["Distribution of one variable", "Histogram / box plot", "Single average"],
                  ["Geographic pattern", "Choropleth map", "Map coloured by raw counts"]]},
         ]},

        {"type": "content", "label": "Anatomy", "title": "What every honest chart needs",
         "blocks": [
             {"t": "bullets", "items": [
                 "A clear <strong>title</strong> that states the takeaway, not just the topic",
                 "Labelled <strong>axes</strong> with units",
                 "An honest <strong>baseline</strong> &mdash; usually zero for bar charts",
                 "A <strong>source</strong> and a date",
                 "A note on the <strong>denominator</strong> and any exclusions"]},
         ]},

        {"type": "content", "label": "The Big Lie", "title": "The truncated axis",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "truncChart", "title": "Y-axis starts at 90 (misleading)",
                        "source": "Illustrative",
                        "type": "bar",
                        "data": {"labels": ["2019", "2021", "2023"],
                                 "datasets": [{"label": "Coverage %", "data": [92, 94, 96],
                                               "backgroundColor": "#EF4444"}]},
                        "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:90, max:97 } } }"}}],
              "right": [{"t": "chart", "canvas": "honestChart", "title": "Y-axis starts at 0 (honest)",
                         "source": "Illustrative",
                         "type": "bar",
                         "data": {"labels": ["2019", "2021", "2023"],
                                  "datasets": [{"label": "Coverage %", "data": [92, 94, 96],
                                                "backgroundColor": "#10B981"}]},
                         "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100 } } }"}}]},
             {"t": "hbox", "color": "red", "html": "Same data. The left chart makes a 4-point "
              "rise look like a tripling. Truncating the axis is the most common way charts lie."},
         ]},

        {"type": "content", "label": "Chartjunk", "title": "More ink is not more information",
         "blocks": [
             {"t": "body", "html": "Edward Tufte's principle: maximise the <strong>data-ink "
              "ratio</strong>. Every gradient, shadow, 3-D effect and clip-art icon competes "
              "with the data for attention &mdash; and usually wins."},
             {"t": "bullets", "color": "red", "items": [
                 "No 3-D bars &mdash; they distort the very lengths you are comparing",
                 "No pie charts with 8 slices &mdash; the eye cannot rank angles",
                 "No rainbow palettes &mdash; colour should carry meaning, not noise"]},
         ]},

        {"type": "content", "label": "Colour", "title": "Use colour with intent &mdash; and for everyone",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Good colour", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Sequential for ordered data (light&rarr;dark)",
                      "One accent colour to highlight the point",
                      "Consistent meaning across charts"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Accessibility", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "~8% of men have colour-vision deficiency",
                      "Never rely on red-vs-green alone",
                      "Add labels, patterns or direct text"]}]}]},
         ]},

        {"type": "content", "label": "Small Multiples", "title": "Repeat a small chart to compare many",
         "blocks": [
             {"t": "body", "html": "Instead of cramming ten states into one tangled line chart, "
              "draw ten tiny identical charts side by side &mdash; <strong>small multiples</strong>. "
              "The eye compares shapes effortlessly when scale and layout are shared."},
             {"t": "hbox", "color": "green", "html": "Rule: when a single chart gets crowded, "
              "split it into a grid of small, identical ones rather than adding more colours."},
         ]},

        {"type": "content", "label": "Tables Too", "title": "Sometimes a table beats a chart",
         "blocks": [
             {"t": "bullets", "items": [
                 "Use a <strong>table</strong> for exact values people will look up or quote",
                 "Use a <strong>chart</strong> for pattern, trend and comparison",
                 "Right-align numbers, fix decimal places, and add row/column totals",
                 "A heat-shaded table can do both &mdash; precise <em>and</em> patterned"]},
         ]},

        {"type": "content", "label": "Checklist", "title": "Before you publish a chart, ask&hellip;",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Does the title state the finding?",
                 "Is the baseline honest (zero where it should be)?",
                 "Are axes, units and the denominator labelled?",
                 "Could a colour-blind reader read it?",
                 "Is the source and date on the chart?",
                 "Have I removed everything that is not data?"]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Relationships &amp; Correlation"},

        {"type": "content", "label": "The Idea", "title": "Do two things move together?",
         "blocks": [
             {"t": "term", "word": "Correlation",
              "def": "A measure of how strongly two variables move together. Positive: both rise "
              "together. Negative: one rises as the other falls. Zero: no linear relationship."},
             {"t": "body", "html": "The correlation coefficient <em>r</em> runs from "
              "&minus;1 (perfect negative) through 0 (none) to +1 (perfect positive)."},
         ]},

        {"type": "content", "label": "See It", "title": "Female literacy and fertility across Indian states",
         "blocks": [
             {"t": "chart", "canvas": "litFertChart",
              "title": "Female literacy (%) vs total fertility rate, major states",
              "source": "Illustrative, patterned on Census 2011 &amp; NFHS-5",
              "type": "scatter",
              "data": {"datasets": [{"label": "States",
                       "data": [{"x": 92, "y": 1.8}, {"x": 84, "y": 1.7}, {"x": 76, "y": 1.8},
                                {"x": 73, "y": 2.1}, {"x": 70, "y": 2.0}, {"x": 66, "y": 2.1},
                                {"x": 64, "y": 2.4}, {"x": 60, "y": 2.5}, {"x": 59, "y": 2.7},
                                {"x": 53, "y": 3.0}, {"x": 50, "y": 3.0}, {"x": 57, "y": 2.6}],
                       "backgroundColor": "#6366F1", "pointRadius": 6}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Female literacy %'} }, y:{ title:{display:true,text:'Total fertility rate'}, min:1.5, max:3.2 } } }"}},
             {"t": "hbox", "color": "cyan", "html": "A clear negative correlation: states with "
              "higher female literacy tend to have lower fertility. But does literacy <em>cause</em> "
              "lower fertility? Hold that thought."},
         ]},

        {"type": "content", "label": "The Golden Rule", "title": "Correlation is not causation",
         "blocks": [
             {"t": "body", "html": "Two variables can move together for several reasons, only one "
              "of which is 'A causes B'."},
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Reverse causation:</strong> B might cause A",
                 "<strong>Confounding:</strong> a third factor C drives both",
                 "<strong>Selection:</strong> the sample was chosen in a way that creates the link",
                 "<strong>Chance:</strong> with enough variables, some correlate by luck"]},
         ]},

        {"type": "content", "label": "Confounding", "title": "The lurking third variable",
         "blocks": [
             {"t": "body", "html": "Ice-cream sales correlate with drowning deaths. Ice cream "
              "does not cause drowning &mdash; <strong>summer heat</strong> drives both. The "
              "confounder is the real story."},
             {"t": "flow", "steps": [
                 "Hot weather (confounder C)",
                 "drives ice-cream sales (A)",
                 "AND drives swimming &amp; drowning (B)",
                 "so A and B correlate &mdash; with no causal link"]},
         ]},

        {"type": "content", "label": "Spurious", "title": "Patterns appear in pure noise",
         "blocks": [
             {"t": "body", "html": "Test enough pairs of unrelated variables and some will "
              "correlate strongly by sheer chance. A tight correlation is a <em>clue</em>, never "
              "a <em>proof</em>."},
             {"t": "hbox", "color": "amber", "html": "Before believing a correlation, ask: is "
              "there a plausible mechanism? Could a confounder explain it? Does it survive in "
              "other data?"},
         ]},

        {"type": "content", "label": "Anscombe", "title": "Never trust the number without the picture",
         "blocks": [
             {"t": "body", "html": "Anscombe's quartet is four datasets with <strong>identical</strong> "
              "means, variances and correlation (r = 0.82) &mdash; yet utterly different shapes: one "
              "linear, one curved, one a single outlier driving everything."},
             {"t": "hbox", "color": "cyan", "html": "The lesson, proven in 1973 and true today: "
              "<strong>always plot your data.</strong> Summary statistics alone can hide the truth."},
         ]},

        {"type": "content", "label": "Ecological Fallacy", "title": "Group patterns &ne; individual truths",
         "blocks": [
             {"t": "term", "word": "Ecological fallacy",
              "def": "Wrongly inferring something about individuals from a pattern seen only at "
              "the group level."},
             {"t": "body", "html": "A district with higher average income may have higher literacy "
              "<em>on average</em> &mdash; that does not mean the richer <em>individuals</em> within "
              "it are the literate ones. What holds for districts need not hold for people."},
         ]},

        {"type": "content", "label": "Simpson's Paradox", "title": "A trend can reverse when you split the data",
         "blocks": [
             {"t": "body", "html": "<strong>Simpson's paradox:</strong> a relationship visible in "
              "the whole dataset can flip when you break it into subgroups. A scheme can look "
              "worse overall yet be better in <em>every</em> region &mdash; if the regions differ "
              "in size and baseline."},
             {"t": "hbox", "color": "red", "html": "Always disaggregate before concluding. The "
              "aggregate can point the opposite way to the truth."},
         ]},

        {"type": "content", "label": "Regression to the Mean", "title": "Extreme results drift back to average",
         "blocks": [
             {"t": "body", "html": "When you pick the <em>worst-performing</em> districts and "
              "re-measure them later, they usually look better &mdash; even with no intervention. "
              "Extreme values contain extra luck that does not repeat. This is "
              "<strong>regression to the mean</strong>."},
             {"t": "hbox", "color": "amber", "html": "It is a notorious trap in evaluation: target "
              "the bottom 10% of schools, see them improve, and credit your programme &mdash; when "
              "much of the gain would have happened anyway. A comparison group is the cure."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Sampling &amp; Surveys"},

        {"type": "content", "label": "Why Sample", "title": "You rarely need to ask everyone",
         "blocks": [
             {"t": "body", "html": "A well-chosen <strong>sample</strong> of a few thousand can "
              "describe a population of millions &mdash; the principle behind NFHS, NSS and every "
              "opinion poll. The magic is not size; it is <strong>representativeness</strong>."},
             {"t": "term", "word": "Representative sample",
              "def": "A sample whose composition mirrors the population on the characteristics "
              "that matter, so findings can be generalised back to the whole."},
         ]},

        {"type": "content", "label": "Population vs Sample", "title": "Define the population first",
         "blocks": [
             {"t": "flow", "steps": [
                 "TARGET POPULATION: whom you want to learn about",
                 "SAMPLING FRAME: the list you can actually draw from",
                 "SAMPLE: who you end up measuring",
                 "RESPONDENTS: who actually answers"]},
             {"t": "hbox", "color": "amber", "html": "Each gap &mdash; frame missing people, "
              "non-response, refusals &mdash; is a place bias creeps in. The frame is often the "
              "weakest link: a list of phone owners is not a list of citizens."},
         ]},

        {"type": "content", "label": "Probability Sampling", "title": "Let chance choose &mdash; it removes bias",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Method", "How", "Use when"],
              "rows": [
                  ["Simple random", "Every unit equal chance", "You have a full list"],
                  ["Systematic", "Every k-th unit from a list", "Ordered list, no hidden cycle"],
                  ["Stratified", "Split into groups, sample each", "You must represent subgroups"],
                  ["Cluster", "Sample whole groups (villages)", "People are geographically spread"],
                  ["Multistage", "Clusters, then units within", "Large national surveys (NFHS)"]]},
             {"t": "hbox", "color": "cyan", "html": "Only probability sampling lets you calculate "
              "a margin of error and generalise honestly."},
         ]},

        {"type": "content", "label": "Non-Probability", "title": "Convenient, but you cannot generalise",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Convenience:</strong> whoever is easy to reach &mdash; the people at the camp",
                 "<strong>Purposive:</strong> hand-picked for a reason &mdash; key informants",
                 "<strong>Snowball:</strong> respondents refer others &mdash; hidden populations",
                 "<strong>Quota:</strong> fill fixed counts per group, but non-randomly"]},
             {"t": "hbox", "color": "amber", "html": "These are legitimate for qualitative depth "
              "and hard-to-reach groups &mdash; but you cannot attach a margin of error or claim "
              "population-level numbers from them."},
         ]},

        {"type": "content", "label": "Sample Size", "title": "How many do I actually need?",
         "blocks": [
             {"t": "chart", "canvas": "moeChart",
              "title": "Margin of error vs sample size (95% confidence, p=0.5)",
              "source": "Standard sampling theory",
              "type": "line",
              "data": {"labels": ["100", "200", "400", "600", "1000", "1500", "2400", "4000"],
                       "datasets": [{"label": "Margin of error (±%)",
                                     "data": [9.8, 6.9, 4.9, 4.0, 3.1, 2.5, 2.0, 1.5],
                                     "borderColor": "#0EA5E9", "backgroundColor": "rgba(14,165,233,0.08)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'± percentage points'} } } }"}},
             {"t": "hbox", "color": "green", "html": "Note the curve flattens: ~<strong>1,067</strong> "
              "gives ±3%, but halving the error to ±1.5% needs ~4,000. Precision gets expensive fast."},
         ]},

        {"type": "content", "label": "Key Insight", "title": "It's the sample size, not the fraction",
         "blocks": [
             {"t": "body", "html": "A counter-intuitive truth: for a large population, accuracy "
              "depends on the <strong>absolute</strong> sample size, not the share of the "
              "population sampled. 1,500 people describe a state and a country about equally well."},
             {"t": "hbox", "color": "cyan", "html": "This is why a national survey of ~600,000 "
              "households can speak about all of India &mdash; and why your block of 2,000 "
              "households still needs a few hundred interviews, not twenty."},
         ]},

        {"type": "content", "label": "Bias", "title": "The errors that size cannot fix",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Selection bias:</strong> the frame or method systematically misses people",
                 "<strong>Non-response bias:</strong> those who refuse differ from those who answer",
                 "<strong>Survivorship bias:</strong> you only see who remained (drop-outs vanish)",
                 "<strong>Social-desirability bias:</strong> people answer how they think they should"]},
             {"t": "hbox", "color": "amber", "html": "A bigger biased sample is just a more "
              "confident wrong answer. Size fixes <em>noise</em>, never <em>bias</em>."},
         ]},

        {"type": "content", "label": "Weights", "title": "Why survey results come 'weighted'",
         "blocks": [
             {"t": "body", "html": "When some groups are deliberately over-sampled (to study them "
              "reliably) or respond less, surveys apply <strong>weights</strong> so each respondent "
              "represents the right number of real people."},
             {"t": "hbox", "color": "red", "html": "Practical warning: using NFHS or PLFS unit "
              "data <em>without</em> the survey weights gives wrong totals. Always weight when the "
              "documentation says to."},
         ]},

        {"type": "content", "label": "Good Questions", "title": "A survey is only as good as its questions",
         "blocks": [
             {"t": "bullets", "items": [
                 "Avoid <strong>leading</strong> questions ('Don't you agree that&hellip;?')",
                 "Avoid <strong>double-barrelled</strong> ones ('clean and safe?' &mdash; which one?)",
                 "Use language and units respondents actually use locally",
                 "Pilot every instrument before the real round &mdash; always"]},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Data Quality &amp; Cleaning"},

        {"type": "content", "label": "Reality Check", "title": "Most data work is cleaning",
         "blocks": [
             {"t": "body", "html": "Analysts often spend the majority of a project just preparing "
              "data &mdash; finding errors, reconciling formats, handling gaps. Glamorous "
              "analysis sits on a large, unglamorous foundation of cleaning."},
             {"t": "quote", "text": "Garbage in, garbage out. No model rescues bad data.",
              "attr": "&mdash; computing proverb, truer than ever"},
         ]},

        {"type": "content", "label": "Dirty Data", "title": "What 'dirty' data looks like",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Problem", "Example", "Risk"],
              "rows": [
                  ["Missing values", "Blank income field", "Biased averages if not random"],
                  ["Duplicates", "Same beneficiary twice", "Inflated counts"],
                  ["Inconsistent codes", "'F' / 'Female' / '2'", "Broken grouping"],
                  ["Outliers / impossible", "Age = 200, &minus;5 children", "Distorted statistics"],
                  ["Format drift", "DD/MM vs MM/DD dates", "Silent miscalculation"],
                  ["Typos in keys", "Misspelt village name", "Failed merges"]]},
         ]},

        {"type": "content", "label": "Missing Data", "title": "Why values are missing matters more than how many",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Missing at random:</strong> gaps unrelated to the value &mdash; least harmful",
                 "<strong>Missing not at random:</strong> the richest refuse to state income &mdash; "
                 "this <em>biases</em> results",
                 "Dropping rows with gaps can quietly delete the very people you care about"]},
             {"t": "hbox", "color": "red", "html": "Before deleting or filling missing values, ask "
              "<em>why</em> they are missing. The pattern of absence is itself data."},
         ]},

        {"type": "content", "label": "The Pipeline", "title": "A repeatable cleaning workflow",
         "blocks": [
             {"t": "flow", "steps": [
                 "INSPECT: look at every column's range &amp; uniques",
                 "VALIDATE: rules (age 0&ndash;120, % in 0&ndash;100)",
                 "FIX: standardise codes, dates, units",
                 "DOCUMENT: log every change",
                 "FREEZE: keep raw data untouched"]},
             {"t": "hbox", "color": "green", "html": "Golden rule: <strong>never edit the raw "
              "file.</strong> Clean in a script or a copy so every change is reversible and visible."},
         ]},

        {"type": "content", "label": "Reproducibility", "title": "If you can't redo it, you can't trust it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Fragile", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Manual edits in a spreadsheet, no record of "
                   "what changed. Next month, nobody can reproduce the number &mdash; including you."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Robust", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A documented script from raw to result. "
                   "Re-run it any time, audit every step, hand it to a colleague."}]}]},
         ]},

        {"type": "content", "label": "Validation", "title": "Build checks in, don't hope",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "<strong>Range checks:</strong> can this value exist at all?",
                 "<strong>Logic checks:</strong> a 6-year-old cannot be married with children",
                 "<strong>Cross-checks:</strong> do parts sum to the reported total?",
                 "<strong>Sense checks:</strong> does the headline number pass the smell test?"]},
         ]},

        {"type": "content", "label": "Metadata", "title": "Document so future-you can understand",
         "blocks": [
             {"t": "body", "html": "<strong>Metadata</strong> is data about your data: what each "
              "variable means, its units, allowed values, how and when it was collected, and what "
              "you changed."},
             {"t": "hbox", "color": "amber", "html": "A dataset without a data dictionary is a "
              "puzzle with no key. The six months it takes to forget your own coding is shorter "
              "than you think."},
         ]},

        {"type": "content", "label": "Versioning", "title": "Keep the trail",
         "blocks": [
             {"t": "bullets", "items": [
                 "Keep the <strong>raw</strong> extract read-only and dated",
                 "Name files with versions and dates, not 'final_FINAL_v3'",
                 "Record the source, download date and any filters applied",
                 "Save the cleaning script alongside the data"]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Reading Data Critically"},

        {"type": "content", "label": "Uncertainty", "title": "Every estimate has a range",
         "blocks": [
             {"t": "body", "html": "A survey figure of 42% is shorthand for 'about 42%, give or "
              "take'. The <strong>confidence interval</strong> &mdash; say 39&ndash;45% &mdash; is "
              "the honest version. A point estimate without its range overstates certainty."},
             {"t": "hbox", "color": "cyan", "html": "If two groups' confidence intervals overlap "
              "heavily, a difference between them may be noise, not signal. Look for the range, "
              "not just the dot."},
         ]},

        {"type": "content", "label": "Significance", "title": "'Significant' has a narrow technical meaning",
         "blocks": [
             {"t": "term", "word": "Statistical significance",
              "def": "A result unlikely to have arisen by chance alone if there were truly no "
              "effect. It says nothing about whether the effect is large or important."},
             {"t": "hbox", "color": "red", "html": "Statistically significant &ne; practically "
              "important. With a huge sample, a trivially small difference can be 'significant'. "
              "Always ask: how <em>big</em> is the effect, and does it matter?"},
         ]},

        {"type": "content", "label": "Base Rates", "title": "The base-rate trap",
         "blocks": [
             {"t": "body", "html": "Even a 99%-accurate test for a rare condition produces mostly "
              "<strong>false positives</strong> &mdash; because the healthy vastly outnumber the "
              "sick. Ignoring the underlying rate is one of the commonest reasoning errors."},
             {"t": "hbox", "color": "amber", "html": "Whenever you read 'X% accurate', ask how "
              "common the thing is to begin with. The base rate changes everything."},
         ]},

        {"type": "content", "label": "Percentages", "title": "Percent vs percentage points",
         "blocks": [
             {"t": "body", "html": "If coverage rises from 40% to 50%, that is a <strong>10 "
              "percentage-point</strong> increase &mdash; but a <strong>25 percent</strong> "
              "increase. Mixing the two is a classic way to exaggerate or hide change."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "+10 pp", "label": "percentage-point change (50 &minus; 40)", "color": "cyan"},
                 {"num": "+25%", "label": "relative change (10 &divide; 40)", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Relative vs Absolute", "title": "'Doubled' can hide tiny numbers",
         "blocks": [
             {"t": "body", "html": "'Cases doubled!' sounds alarming &mdash; but a rise from 2 to "
              "4 is a doubling of almost nothing. Relative change without the absolute base is "
              "designed to impress, not inform."},
             {"t": "hbox", "color": "red", "html": "Always pair the relative figure with the raw "
              "counts. '100% increase, from 2 to 4 cases' tells the honest story."},
         ]},

        {"type": "content", "label": "Cherry-Picking", "title": "Beware the chosen baseline",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Start the time axis at a low year to exaggerate growth",
                 "Quote the one indicator that improved, ignore the rest",
                 "Compare to an unusual reference period (a drought, a peak)",
                 "Report only the subgroup that helps the argument"]},
             {"t": "hbox", "color": "amber", "html": "Ask: why <em>this</em> start date, "
              "<em>this</em> indicator, <em>this</em> comparison? What is left out?"},
         ]},

        {"type": "content", "label": "Garden of Forking Paths", "title": "Test enough things and something 'works'",
         "blocks": [
             {"t": "body", "html": "If you slice the data twenty ways, roughly one slice will show "
              "a 'significant' result by chance. Reporting only that slice &mdash; "
              "<strong>p-hacking</strong> &mdash; manufactures false findings."},
             {"t": "hbox", "color": "cyan", "html": "Trust analyses that were specified "
              "<em>before</em> seeing the data, and findings that replicate. Be wary of a single "
              "surprising subgroup result."},
         ]},

        {"type": "content", "label": "A Reader's Checklist", "title": "Eight questions for any statistic",
         "compact": True,
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Who produced it, and what is their interest?",
                 "How was it measured &mdash; and what is the denominator?",
                 "Is it a sample? How big, how chosen?",
                 "What is the uncertainty / margin of error?",
                 "Percent or percentage points? Relative or absolute?",
                 "Who is missing from the count?",
                 "Correlation, or genuine causation?",
                 "Does it pass the common-sense smell test?"]},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Data Ethics, Privacy &amp; Equity"},

        {"type": "content", "label": "Behind Every Row", "title": "Every data point is a person",
         "blocks": [
             {"t": "body", "html": "In development data, rows are people &mdash; often poor, "
              "often without power over how their information is used. Data ethics is not "
              "paperwork; it is respect made operational."},
             {"t": "quote", "text": "Data are not just numbers; they are people reduced to "
              "numbers. The reduction is never neutral.",
              "attr": "&mdash; a principle of feminist data practice"},
         ]},

        {"type": "content", "label": "Consent", "title": "Informed consent is the floor",
         "blocks": [
             {"t": "bullets", "items": [
                 "People should know <strong>what</strong> is collected and <strong>why</strong>",
                 "How it will be used, stored and shared &mdash; and for how long",
                 "That they can <strong>refuse</strong> or stop, with no penalty",
                 "Consent must be in a language and form they genuinely understand"]},
             {"t": "hbox", "color": "amber", "html": "A thumbprint on a form nobody explained is "
              "not consent. For children and other vulnerable groups, extra safeguards apply."},
         ]},

        {"type": "content", "label": "Privacy", "title": "Anonymisation is harder than deleting names",
         "blocks": [
             {"t": "body", "html": "Removing names is not enough. A combination of village + age "
              "+ caste + occupation can <strong>re-identify</strong> one person &mdash; especially "
              "in small areas where few people share those traits."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Direct IDs", "label": "Name, Aadhaar, phone &mdash; remove", "color": "red"},
                 {"num": "Quasi-IDs", "label": "Age + place + caste can re-identify &mdash; "
                  "aggregate or coarsen", "color": "amber"}]},
         ]},

        {"type": "content", "label": "The Law", "title": "India's Digital Personal Data Protection Act, 2023",
         "blocks": [
             {"t": "body", "html": "The <strong>DPDP Act, 2023</strong> is India's first "
              "comprehensive data-protection law. It sets duties for anyone handling personal "
              "digital data &mdash; including NGOs and researchers."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Collect only what you need, for a stated purpose (purpose limitation)",
                 "Obtain free, informed, specific consent",
                 "Protect data with reasonable security safeguards",
                 "Stronger protections for children's data"]},
             {"t": "hbox", "color": "amber", "html": "Know your obligations before you collect. "
              "'We're a small NGO' is not an exemption."},
         ]},

        {"type": "content", "label": "Equity in Counting", "title": "What you don't disaggregate, you can't see",
         "blocks": [
             {"t": "body", "html": "An average hides the people behind it. A programme can report "
              "good overall numbers while failing Dalit, Adivasi, disabled, or women "
              "beneficiaries. <strong>Disaggregation</strong> is how inequity becomes visible."},
             {"t": "chart", "canvas": "disaggChart",
              "title": "An overall average can mask large gaps between groups",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["Overall", "Group A", "Group B", "Group C", "Group D"],
                       "datasets": [{"label": "Outcome (%)", "data": [62, 78, 70, 55, 38],
                                     "backgroundColor": ["#6366F1", "#10B981", "#10B981", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100} } }"}},
         ]},

        {"type": "content", "label": "The Missing", "title": "Count the people the data forgets",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Homeless and pavement-dwellers absent from household frames",
                 "Migrants counted nowhere &mdash; neither origin nor destination",
                 "Informal workers invisible to formal employment statistics",
                 "Trans and non-binary people erased by binary-only forms"]},
             {"t": "hbox", "color": "amber", "html": "'Missing data' is rarely random. The "
              "uncounted are usually the most marginalised &mdash; and policy built on the count "
              "leaves them out twice."},
         ]},

        {"type": "content", "label": "Data Power", "title": "Data colonialism and who benefits",
         "blocks": [
             {"t": "body", "html": "Communities are often <em>extracted</em> from &mdash; surveyed "
              "repeatedly, with the knowledge and value flowing to outside institutions while "
              "respondents see nothing back."},
             {"t": "bullets", "color": "green", "items": [
                 "Give findings <strong>back</strong> to the community in usable form",
                 "Involve people in defining what gets measured",
                 "Ask: who owns this data, and who profits from it?"]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Tools &amp; Further Reading"},

        {"type": "content", "label": "Getting Hands-On", "title": "Tools to grow into",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Good for", "Note"],
              "rows": [
                  ["Spreadsheets (Excel, Google Sheets)", "Most everyday analysis", "Start here; learn pivot tables"],
                  ["R", "Statistics, reproducible analysis, graphics", "Free, powerful, steeper curve"],
                  ["Python (pandas)", "Cleaning, large data, automation", "Free, general-purpose"],
                  ["KoboToolbox / ODK", "Mobile survey data collection", "Free, offline-capable"],
                  ["QGIS", "Maps and spatial data", "Free, open-source GIS"],
                  ["Power BI / Looker Studio", "Dashboards", "Quick visual reporting"]]},
             {"t": "hbox", "color": "cyan", "html": "Tools matter less than habits. A clear "
              "spreadsheet beats a confused script. Master the thinking first."},
         ]},

        {"type": "content", "label": "Where to Get Data", "title": "Open data you can use today",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>data.gov.in</strong> &mdash; India's open government data portal",
                 "<strong>censusindia.gov.in</strong> &mdash; Census tables &amp; maps",
                 "<strong>NFHS / DHS Program</strong> &mdash; health &amp; demographic data",
                 "<strong>MoSPI</strong> &mdash; NSS, PLFS, national accounts",
                 "<strong>World Bank Open Data</strong> &amp; <strong>Our World in Data</strong> &mdash; global comparisons"]},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>How to Lie with Statistics</em> &mdash; Darrell Huff (still the classic primer)",
                 "<em>The Visual Display of Quantitative Information</em> &mdash; Edward Tufte",
                 "<em>Data Feminism</em> &mdash; D'Ignazio &amp; Klein (power and data)",
                 "<em>Factfulness</em> &mdash; Hans Rosling (reading global data well)",
                 "<em>Poor Economics</em> &mdash; Banerjee &amp; Duflo (evidence in development)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Exploratory Data Analysis</strong>, <strong>Qualitative Methods</strong> and "
              "<strong>Research Ethics</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Always ask where the data came from</strong> &mdash; and who is missing",
                 "<strong>Plot it</strong> before you trust any summary number",
                 "<strong>Median over mean</strong> for skewed things like money",
                 "<strong>Correlation is not causation</strong> &mdash; look for the confounder",
                 "<strong>Behind every row is a person</strong> &mdash; handle with care"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Data Literacy 101 &middot; Complete",
         "headline": "Now go question<br>the next number.",
         "byline": "You don't need to be a statistician &mdash; you need to ask the right "
                   "questions of every chart, survey and dashboard that crosses your desk. "
                   "Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
