# -*- coding: utf-8 -*-
"""
Care Economy 101 — ImpactMojo 101 Series (native deck spec)
Foundational care economy literacy for South Asian development practitioners.
Build: python3 scripts/deck-builder/build.py care_economy_101
"""

DECK = {
    "slug": "care-economy-101",
    "title": "Care Economy 101",
    "description": ("Care Economy 101 — a free foundational course for development "
                    "practitioners and policy folk in South Asia. Understand paid and "
                    "unpaid care work, why GDP hides it, how India's Time Use Survey "
                    "measures it, the 5 Rs framework, care policies and the case for "
                    "investing in care. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Care<br>Economy<br>101",
         "sub": "Recognising, Valuing &amp; Investing in the Work That Holds Everything "
                "Else Up &mdash; a Foundational Course for Development Practitioners in "
                "South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What the Care Economy Is"},
             {"name": "The Invisibility of Care"},
             {"name": "Measuring Care: Time-Use Surveys"},
             {"name": "The Value of Unpaid Care"},
             {"name": "The Gendered Division of Care"},
             {"name": "Care &amp; the Macroeconomy"},
             {"name": "The 5 Rs Framework"},
             {"name": "Care Policies"},
             {"name": "Paid Care Work"},
             {"name": "Care in South Asia"},
             {"name": "Practice &amp; Policy"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What the Care Economy Is"},

        {"type": "content", "label": "Definition", "title": "Care is the economy beneath the economy",
         "blocks": [
             {"t": "body", "html": "Every market, factory and office runs on people who were "
              "fed, raised, nursed and kept well by someone. The <strong>care economy</strong> "
              "is the whole system of activities &mdash; paid and unpaid &mdash; that sustain "
              "human beings day to day and across generations."},
             {"t": "term", "word": "Care economy",
              "def": "The sector of activity, paid and unpaid, that meets the physical, "
              "emotional and developmental needs of people &mdash; children, the sick, the "
              "elderly, persons with disabilities, and able adults &mdash; so that life and "
              "the wider economy can continue."},
             {"t": "hbox", "color": "cyan", "html": "No worker arrives at a job site without "
              "first being cared for. Care is the precondition of all other production."},
         ]},

        {"type": "content", "label": "Two Halves", "title": "Care work comes paid and unpaid",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Unpaid care work", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Cooking, cleaning, fetching water and "
                   "fuel, childcare, caring for the sick and elderly &mdash; done within the "
                   "household for no wage. Overwhelmingly done by women and girls."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Paid care work", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Domestic workers, nurses, ASHAs, "
                   "anganwadi workers, teachers, eldercare staff &mdash; care provided for a "
                   "wage, in homes, clinics, schools and institutions."}]}]},
             {"t": "hbox", "color": "amber", "html": "The two are connected: when unpaid care "
              "is squeezed, demand for paid care rises &mdash; and vice versa."},
         ]},

        {"type": "content", "label": "What Counts", "title": "Direct care and the work that enables it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Direct (person) care", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Feeding and bathing a child",
                      "Nursing a sick relative",
                      "Supervising an elderly parent",
                      "Helping a child with schoolwork"]}]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Indirect (housework) care", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Cooking and washing up",
                      "Cleaning the home",
                      "Fetching water and firewood",
                      "Shopping and household management"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Both are care work. Indirect care &mdash; "
              "the cooking and fetching &mdash; is what makes direct care possible."},
         ]},

        {"type": "content", "label": "The Foundation", "title": "Why care is the foundation of every other economy",
         "blocks": [
             {"t": "flow", "steps": [
                 "UNPAID CARE produces &amp; maintains people",
                 "PEOPLE supply labour to markets",
                 "MARKETS generate paid output (GDP)",
                 "GDP funds public services &amp; more care"]},
             {"t": "hbox", "color": "cyan", "html": "Economists call this the <em>circuit of "
              "social reproduction</em>: the market economy could not function for a single day "
              "without the care economy replenishing its workforce."},
         ]},

        {"type": "content", "label": "Scale", "title": "Care work is colossal &mdash; if you count it",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "16.4 bn", "label": "hours of unpaid care work performed worldwide "
                  "every day", "color": "cyan", "source": "ILO, <em>Care Work and Care Jobs</em> (2018)"},
                 {"num": "76%", "label": "of all unpaid care hours worldwide are done by women",
                  "color": "indigo", "source": "ILO (2018)"},
                 {"num": "2 billion+", "label": "equivalent full-time jobs that daily unpaid care "
                  "would represent at minimum wage", "color": "amber", "source": "ILO (2018)"}]},
             {"t": "hbox", "color": "green", "html": "These are established global estimates from "
              "the ILO &mdash; care is not a marginal activity but one of the largest 'sectors' "
              "in the world economy."},
         ]},

        {"type": "content", "label": "Reframe", "title": "From cost to investment",
         "blocks": [
             {"t": "body", "html": "Conventional accounting treats care &mdash; childcare leave, "
              "anganwadis, eldercare &mdash; as <strong>spending</strong> to be minimised. The "
              "care-economy lens reframes it as <strong>investment</strong> in the people on whom "
              "all future output depends."},
             {"t": "quote",
              "text": "The care economy is not a drain on the 'real' economy. It is the "
              "infrastructure that makes the real economy possible.",
              "attr": "&mdash; a core insight of feminist economics"},
         ]},

        {"type": "content", "label": "A Working Day", "title": "A day in two economies",
         "blocks": [
             {"t": "body", "html": "Picture a rural morning. A woman rises before dawn, fetches "
              "water, lights the stove, cooks, feeds children, sees the older ones to school, "
              "tends an ailing parent &mdash; all before any 'work' the economy recognises has "
              "begun."},
             {"t": "hbox", "color": "amber", "html": "Hours of essential labour, all of it "
              "uncounted. The care economy is not abstract &mdash; it is the texture of daily "
              "life, mostly women's."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Seeing &amp; measuring", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Why GDP makes care invisible",
                      "Time-use surveys and the gender gap",
                      "Valuing unpaid care work"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Acting on it", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "The gendered division and the 5 Rs",
                      "Care policies and paid care work",
                      "Care in South Asia, and what to do"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Examples are India-centric throughout "
              "&mdash; the care realities you meet in policy and practice."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Invisibility of Care"},

        {"type": "content", "label": "The Blind Spot", "title": "GDP measures the market, not the home",
         "blocks": [
             {"t": "body", "html": "Gross Domestic Product counts goods and services bought and "
              "sold. The meal cooked at home for free does not count; the identical meal bought "
              "at a restaurant does. The work is the same &mdash; only the price tag differs."},
             {"t": "hbox", "color": "red", "html": "Result: a vast share of the labour that keeps "
              "society alive is statistically invisible. What we do not measure, we do not value, "
              "and do not fund."},
         ]},

        {"type": "content", "label": "The Rule", "title": "The SNA 'production boundary'",
         "blocks": [
             {"t": "term", "word": "Production boundary (SNA)",
              "def": "The line drawn by the System of National Accounts &mdash; the UN rulebook "
              "for GDP &mdash; that decides which activities count as economic 'production'. "
              "Unpaid domestic and care services for one's own household sit <em>outside</em> it."},
             {"t": "body", "html": "Crucially, the SNA does count unpaid <em>production of goods</em> "
              "for own use (e.g. subsistence farming, fetching water), but excludes unpaid "
              "<em>services</em> &mdash; cooking, cleaning, caring &mdash; from GDP."},
         ]},

        {"type": "content", "label": "The Paradox", "title": "The classic paradox of national accounting",
         "blocks": [
             {"t": "body", "html": "A famous illustration: if a man marries his housekeeper and "
              "stops paying her, but she does the same work, <strong>GDP falls</strong> &mdash; "
              "even though nothing about the actual work has changed."},
             {"t": "hbox", "color": "amber", "html": "The example, debated since the early days of "
              "national accounting, exposes the arbitrariness of the boundary: the <em>same task</em> "
              "is 'production' when paid and 'nothing' when unpaid."},
         ]},

        {"type": "content", "label": "'Women's Work'", "title": "How care became 'not work'",
         "blocks": [
             {"t": "body", "html": "The exclusion is not a neutral technicality. Care was "
              "naturalised as something women do out of love &mdash; an instinct, not labour. "
              "Calling it <strong>'women's work'</strong> made it both invisible and unpaid."},
             {"t": "quote",
              "text": "When work is done out of love, or expected of one's gender, it is rarely "
              "counted as work at all.",
              "attr": "&mdash; a recurring theme in feminist economics"},
         ]},

        {"type": "content", "label": "Who Saw It First", "title": "Feminist economists named the gap",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Marilyn Waring</strong> &mdash; <em>If Women Counted</em> (1988) exposed "
                 "how the SNA renders women's work invisible",
                 "<strong>Nancy Folbre</strong> &mdash; theorised the economics of care and 'the "
                 "invisible heart'",
                 "<strong>Diane Elson</strong> &mdash; built the policy framework (the Rs) for "
                 "acting on unpaid care",
                 "<strong>Shahra Razavi</strong> &mdash; mapped how care is provided across state, "
                 "market, family and community"]},
             {"t": "hbox", "color": "cyan", "html": "We will meet each of these thinkers again "
              "&mdash; they built the toolkit this course uses."},
         ]},

        {"type": "content", "label": "Consequences", "title": "What invisibility costs",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Care receives little public investment &mdash; it 'isn't economic'",
                 "Women's economic contribution is systematically understated",
                 "Time spent caring is mistaken for 'not working' or 'inactivity'",
                 "Policy is designed as if care happens for free, forever, automatically"]},
             {"t": "hbox", "color": "amber", "html": "Making care visible is the first step "
              "&mdash; you cannot redistribute or invest in what the data refuses to see."},
         ]},

        {"type": "content", "label": "The Iceberg", "title": "What the headline number leaves under water",
         "blocks": [
             {"t": "chart", "canvas": "icebergChart",
              "title": "Total socially useful work: what GDP counts vs what it omits (illustrative)",
              "source": "Illustrative, patterned on time-use-based estimates",
              "type": "doughnut",
              "data": {"labels": ["Counted in GDP (paid work)", "Omitted: unpaid care work"],
                       "datasets": [{"data": [55, 45],
                                     "backgroundColor": ["#6366F1", "#0EA5E9"]}]},
              "options": {"__js__": "{ plugins:{ legend:{ position:'bottom' } } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative split: a large share of all "
              "socially useful work is unpaid care that never enters GDP. The visible economy "
              "sits on a vast invisible one."},
         ]},

        {"type": "content", "label": "Shifting Ground", "title": "The boundary is being challenged",
         "blocks": [
             {"t": "body", "html": "The SNA still excludes unpaid care from headline GDP, but "
              "statisticians now build <strong>satellite accounts</strong> &mdash; parallel "
              "estimates that value household production alongside GDP without changing the "
              "core measure."},
             {"t": "hbox", "color": "green", "html": "Time-use surveys, which we turn to next, "
              "are the raw material for these satellite accounts &mdash; the way care finally "
              "gets counted."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Measuring Care: Time-Use Surveys"},

        {"type": "content", "label": "The Instrument", "title": "Time-use surveys make care visible",
         "blocks": [
             {"t": "term", "word": "Time-use survey",
              "def": "A survey that asks people to account for how they spent a full day &mdash; "
              "typically in fixed time slots &mdash; capturing paid work, unpaid care, learning, "
              "leisure and rest. It is the standard tool for measuring unpaid work."},
             {"t": "body", "html": "Because it records <em>activities</em> rather than only "
              "earnings, the time-use survey can see the cooking, cleaning and caring that GDP "
              "ignores &mdash; and reveal who does it."},
         ]},

        {"type": "content", "label": "India's Survey", "title": "The India Time Use Survey, 2019",
         "blocks": [
             {"t": "body", "html": "India's first national <strong>Time Use Survey (TUS)</strong> "
              "was conducted by the <strong>National Statistical Office (NSO)</strong> from "
              "January to December 2019. It is the authoritative source on how Indians &mdash; "
              "women and men &mdash; spend their time."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "2019", "label": "first all-India TUS, conducted by NSO over a full year",
                  "color": "cyan", "source": "MoSPI / NSO Time Use Survey 2019"},
                 {"num": "~1.39 lakh", "label": "households surveyed across India", "color": "green",
                  "source": "NSO TUS 2019"},
                 {"num": "24 hrs", "label": "of each respondent's day recorded in 30-minute slots",
                  "color": "indigo", "source": "NSO TUS 2019"}]},
         ]},

        {"type": "content", "label": "How It Works", "title": "Recording a day, slot by slot",
         "blocks": [
             {"t": "flow", "steps": [
                 "SAMPLE households across rural &amp; urban India",
                 "ASK each member to recount the previous day",
                 "CODE activities in 30-minute slots",
                 "CLASSIFY into paid work, unpaid care, learning, leisure, rest"]},
             {"t": "hbox", "color": "cyan", "html": "The survey also captures <em>simultaneous</em> "
              "activities &mdash; minding a child while cooking &mdash; a reality that single-task "
              "measures miss entirely."},
         ]},

        {"type": "content", "label": "The Headline", "title": "The gendered gap in unpaid work",
         "blocks": [
             {"t": "body", "html": "The TUS 2019 confirmed what was long suspected: Indian women "
              "spend many times more of their day on unpaid domestic and caregiving services than "
              "men do &mdash; one of the widest such gaps measured anywhere."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "~5 hrs", "label": "average daily time women (15&ndash;59) spend on unpaid "
                  "domestic &amp; care work", "color": "indigo", "source": "Illustrative, patterned on NSO TUS 2019"},
                 {"num": "~30 min", "label": "average daily time men (15&ndash;59) spend on the same",
                  "color": "amber", "source": "Illustrative, patterned on NSO TUS 2019"}]},
             {"t": "hbox", "color": "red", "html": "The participation gap is just as stark: a large "
              "majority of women do unpaid domestic work on any given day; only a minority of men do."},
         ]},

        {"type": "content", "label": "See It", "title": "Unpaid work hours by sex (illustrative)",
         "blocks": [
             {"t": "chart", "canvas": "tusGapChart",
              "title": "Average minutes per day on unpaid domestic &amp; care work, by sex",
              "source": "Illustrative, patterned on NSO Time Use Survey 2019",
              "type": "bar",
              "data": {"labels": ["Unpaid domestic services", "Unpaid caregiving", "Total unpaid care work"],
                       "datasets": [
                           {"label": "Women", "data": [240, 60, 300], "backgroundColor": "#6366F1"},
                           {"label": "Men", "data": [25, 12, 37], "backgroundColor": "#F59E0B"}]},
              "options": {"__js__": "{ scales:{ y:{ title:{display:true,text:'Minutes per day'}, min:0 } } }"}},
             {"t": "hbox", "color": "amber", "html": "Bars are illustrative and patterned on the "
              "TUS 2019 pattern; the magnitude of the gap &mdash; women doing the large majority "
              "of unpaid care &mdash; is well established."},
         ]},

        {"type": "content", "label": "Reading It Well", "title": "What the numbers do and don't say",
         "blocks": [
             {"t": "bullets", "items": [
                 "Time-use data shows <strong>how much</strong> care is done, and <strong>by "
                 "whom</strong> &mdash; powerfully",
                 "It captures simultaneous and unpaid work that GDP misses",
                 "But recall and social desirability can <em>under</em>-report men's small share "
                 "or women's leisure",
                 "And a minute of childcare and a minute of leisure are not equivalent in wellbeing"]},
             {"t": "hbox", "color": "cyan", "html": "Use time-use data to size the problem and "
              "target policy &mdash; but read it like any survey, with its limits in view."},
         ]},

        {"type": "content", "label": "Rural &amp; Urban", "title": "The gap is everywhere &mdash; with variations",
         "blocks": [
             {"t": "body", "html": "The unpaid-care gender gap shows up in <em>every</em> setting "
              "the TUS measured &mdash; rural and urban, across states, rich and poor. Where "
              "infrastructure is thin, women's unpaid hours climb further; men's barely move."},
             {"t": "hbox", "color": "cyan", "html": "This consistency is the point: the gap is "
              "structural, not the quirk of one region. It is built into how society assigns care."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "From a survey to a budget line",
         "blocks": [
             {"t": "body", "html": "Time-use data is not an academic curiosity. It is the evidence "
              "base for childcare investment, for measuring women's true workload, for designing "
              "leave policy, and for valuing unpaid care in national accounts."},
             {"t": "hbox", "color": "green", "html": "Once you can <em>count</em> the hours, you "
              "can begin to <em>value</em> them &mdash; the question we turn to next."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "The Value of Unpaid Care"},

        {"type": "content", "label": "The Question", "title": "What is unpaid care worth?",
         "blocks": [
             {"t": "body", "html": "If unpaid care were a paid sector, how large would it be? "
              "Answering this means assigning a money value to hours that, by definition, command "
              "no wage. Economists call this <strong>imputation</strong>."},
             {"t": "term", "word": "Imputation",
              "def": "Estimating a monetary value for an activity that has no market price &mdash; "
              "here, by asking what the equivalent work would cost if it had to be bought."},
         ]},

        {"type": "content", "label": "Methods", "title": "Three ways to put a price on care",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Method", "How it values an hour of care", "Tends to give"],
              "rows": [
                  ["Replacement cost (generalist)", "Wage of a domestic worker who could do it",
                   "Lower estimate"],
                  ["Replacement cost (specialist)", "Wage of a nurse, cook, tutor for each task",
                   "Higher estimate"],
                  ["Opportunity cost", "The wage the carer forgoes by doing care instead",
                   "Varies by the carer's own wage"]]},
             {"t": "hbox", "color": "amber", "html": "The method chosen can change the headline "
              "value several-fold &mdash; so always ask which one a figure uses."},
         ]},

        {"type": "content", "label": "The Estimates", "title": "Unpaid care as a share of GDP",
         "blocks": [
             {"t": "body", "html": "Across countries, valuations of unpaid care work typically land "
              "between roughly <strong>10% and 60% of GDP</strong>, depending on the method and the "
              "country. For India, leading estimates put women's unpaid work alone at a very large "
              "share of GDP &mdash; tens of percent."},
             {"t": "chart", "canvas": "gdpValueChart",
              "title": "Unpaid care valued as % of GDP, under different methods (illustrative)",
              "source": "Illustrative, patterned on ranges in ILO &amp; OECD valuation studies",
              "type": "bar",
              "data": {"labels": ["Replacement (generalist)", "Replacement (specialist)", "Opportunity cost"],
                       "datasets": [{"label": "Estimated value (% of GDP)",
                                     "data": [15, 32, 24],
                                     "backgroundColor": ["#0EA5E9", "#10B981", "#6366F1"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'% of GDP'}, min:0, max:60 } } }"}},
             {"t": "hbox", "color": "amber", "html": "Values are illustrative; the <em>order of "
              "magnitude</em> &mdash; care is worth a double-digit share of GDP &mdash; is robust "
              "across studies."},
         ]},

        {"type": "content", "label": "A Concrete Sense", "title": "Bigger than most named industries",
         "blocks": [
             {"t": "body", "html": "Put the share in perspective: when valued, unpaid care work "
              "would typically dwarf sectors we treat as economically central &mdash; larger than "
              "manufacturing or transport in many national exercises."},
             {"t": "hbox", "color": "cyan", "html": "The point is not the exact percentage. It is "
              "that the single largest 'industry' in most economies is one we have chosen not to "
              "count or fund."},
         ]},

        {"type": "content", "label": "Why Value It", "title": "What monetising care achieves",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Makes the invisible <strong>visible</strong> to ministries that speak in money",
                 "Justifies public investment in childcare, eldercare and leave",
                 "Reveals the true scale of women's economic contribution",
                 "Lets us track whether care burdens are rising or being shared"]},
         ]},

        {"type": "content", "label": "The Limits", "title": "Why monetising care is also dangerous",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "A money value can <strong>flatten</strong> the relational, emotional core of care",
                 "Replacement-wage methods anchor care to <em>already low</em> care wages &mdash; "
                 "circular undervaluation",
                 "A single number invites cost-cutting once care 'has a price'",
                 "Valuing is not the same as <em>paying</em> &mdash; the carer still earns nothing"]},
             {"t": "hbox", "color": "amber", "html": "Value care to argue for investment &mdash; "
              "but never let the price tag become the whole story of why care matters."},
         ]},

        {"type": "content", "label": "The Balance", "title": "Count it, but don't reduce it",
         "blocks": [
             {"t": "quote",
              "text": "Care is both an economic activity worth measuring and a human relationship "
              "that resists being priced. Hold both truths at once.",
              "attr": "&mdash; a guiding principle for care valuation"},
             {"t": "body", "html": "The practical stance: use valuation to win recognition and "
              "resources, while insisting that care's worth is not exhausted by its monetary "
              "estimate."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "The Gendered Division of Care"},

        {"type": "content", "label": "The Pattern", "title": "Care falls on women and girls",
         "blocks": [
             {"t": "body", "html": "Across cultures and income levels, unpaid care is not shared "
              "equally. It is assigned to women and girls by social norm, and reinforced by every "
              "institution from the family to the labour market."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "3&ndash;10x", "label": "more time women spend on unpaid care than men, "
                  "depending on the country", "color": "indigo", "source": "ILO (2018); TUS-type surveys"},
                 {"num": "Girls", "label": "are drawn into fetching, cooking and sibling care "
                  "earlier than boys", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Learned Early", "title": "Care roles are taught, not innate",
         "blocks": [
             {"t": "body", "html": "Girls are socialised into care from childhood &mdash; helping "
              "in the kitchen, minding younger siblings, fetching water. This is not biology; it is "
              "a <strong>gendered division of labour</strong> learned and enforced over time."},
             {"t": "hbox", "color": "red", "html": "The cost is direct: care duties pull girls out "
              "of school and away from play, narrowing their futures before they choose them."},
         ]},

        {"type": "content", "label": "Time Poverty", "title": "Care and time poverty",
         "blocks": [
             {"t": "term", "word": "Time poverty",
              "def": "Having too little time left for rest, learning, paid work or leisure after "
              "unavoidable unpaid work is done. A person can be income-poor and time-poor at once "
              "&mdash; and care is the main driver of women's time poverty."},
             {"t": "body", "html": "Where water and fuel are far, infrastructure thin, and "
              "appliances absent, the unpaid-care day stretches longest &mdash; and falls hardest "
              "on the poorest women."},
         ]},

        {"type": "content", "label": "The Second Shift", "title": "The 'second shift'",
         "blocks": [
             {"t": "body", "html": "When women take paid work, they rarely shed unpaid care. They "
              "return home to a <strong>second shift</strong> of cooking, cleaning and caring "
              "&mdash; a phrase coined by sociologist Arlie Hochschild."},
             {"t": "hbox", "color": "amber", "html": "The result is a 'double burden': paid work "
              "added on top of unpaid work, rather than in place of it. Leisure and sleep are what "
              "get squeezed."},
         ]},

        {"type": "content", "label": "The Trade-off", "title": "Care burden vs joining the workforce",
         "blocks": [
             {"t": "chart", "canvas": "lfpCareChart",
              "title": "Female labour-force participation vs unpaid-care hours, by group (illustrative)",
              "source": "Illustrative, patterned on PLFS &amp; TUS-type relationships",
              "type": "scatter",
              "data": {"datasets": [{"label": "Groups",
                       "data": [{"x": 360, "y": 18}, {"x": 320, "y": 22}, {"x": 300, "y": 24},
                                {"x": 270, "y": 28}, {"x": 240, "y": 33}, {"x": 210, "y": 38},
                                {"x": 180, "y": 44}, {"x": 150, "y": 52}, {"x": 120, "y": 58}],
                       "backgroundColor": "#6366F1", "pointRadius": 6}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Unpaid care minutes/day'} }, y:{ title:{display:true,text:'Female LFP (%)'}, min:0, max:65 } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Illustrative pattern: the heavier the unpaid-care "
              "load, the lower women's labour-force participation tends to be. Care is a key reason "
              "India's female LFP is low."},
         ]},

        {"type": "content", "label": "Intersecting", "title": "Care burdens stack with other inequalities",
         "blocks": [
             {"t": "body", "html": "The care load is not the same for all women. It is heaviest "
              "where poverty, caste, rurality and lack of infrastructure intersect &mdash; the "
              "Dalit or Adivasi woman in a village without piped water carries far more than the "
              "salaried urban professional."},
             {"t": "hbox", "color": "red", "html": "Care inequality is gendered <em>and</em> "
              "classed and casted. Policy that ignores this serves the already-advantaged first."},
         ]},

        {"type": "content", "label": "Not Just Time", "title": "The mental load of care",
         "blocks": [
             {"t": "body", "html": "Beyond the visible hours lies the <strong>mental load</strong> "
              "&mdash; the invisible work of planning, remembering and worrying: noticing the "
              "medicine is finished, that a child is unwell, that the elder needs a check-up. It "
              "rarely shows up in any survey."},
             {"t": "hbox", "color": "amber", "html": "This managerial burden of care falls almost "
              "entirely on women too &mdash; and unlike a task, it never clocks off."},
         ]},

        {"type": "content", "label": "The Stakes", "title": "Why the division matters for development",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Women's unequal care load is a root cause of low female workforce participation",
                 "It drives girls' school dropout and limits their attainment",
                 "It undermines women's health, rest and economic independence",
                 "Redistributing care is therefore central to gender equality &mdash; not a side issue"]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Care &amp; the Macroeconomy"},

        {"type": "content", "label": "The Engine", "title": "Social reproduction keeps the economy running",
         "blocks": [
             {"t": "term", "word": "Social reproduction",
              "def": "The daily and generational work of producing and maintaining people &mdash; "
              "birthing, feeding, raising, healing, sustaining &mdash; that replenishes the labour "
              "force the market economy depends on."},
             {"t": "body", "html": "The paid economy and the care economy are not separate. The "
              "first continuously draws on the second for its workers &mdash; yet rarely pays back "
              "into it."},
         ]},

        {"type": "content", "label": "The Warning", "title": "Depletion: when care runs down",
         "blocks": [
             {"t": "term", "word": "Depletion",
              "def": "The harm that accumulates when the demands of care work outstrip the "
              "resources &mdash; time, energy, health, support &mdash; available to carers. Care "
              "extracted without replenishment exhausts the people who provide it."},
             {"t": "hbox", "color": "red", "html": "Just as soil erodes if farmed without rest, "
              "carers deplete if society draws on their labour without investing back. Depletion "
              "is an economic risk, not only a personal one."},
         ]},

        {"type": "content", "label": "The Reframe", "title": "Care as investment, not cost",
         "blocks": [
             {"t": "body", "html": "Spending on childcare, health and eldercare is routinely "
              "booked as <strong>current consumption</strong> &mdash; a cost to contain. But care "
              "builds <strong>human capital</strong>: healthy, educated, well-raised people who "
              "power future growth."},
             {"t": "hbox", "color": "green", "html": "Treat care as social infrastructure &mdash; "
              "as much an investment as a road or a power line, and arguably with higher returns."},
         ]},

        {"type": "content", "label": "Who Provides", "title": "The care diamond",
         "blocks": [
             {"t": "body", "html": "Care is provided through four institutions &mdash; the "
              "<strong>care diamond</strong>, a framework from Shahra Razavi (UNRISD, 2007). How "
              "much each corner does, and who carries the rest, is a core policy question."},
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:10px 0;">'
                 '<svg viewBox="0 0 520 320" width="520" height="300" xmlns="http://www.w3.org/2000/svg" '
                 'style="max-width:100%;height:auto;font-family:inherit">'
                 # diamond connecting lines
                 '<line x1="260" y1="40" x2="470" y2="160" stroke="#334155" stroke-width="1.5"/>'
                 '<line x1="470" y1="160" x2="260" y2="280" stroke="#334155" stroke-width="1.5"/>'
                 '<line x1="260" y1="280" x2="50" y2="160" stroke="#334155" stroke-width="1.5"/>'
                 '<line x1="50" y1="160" x2="260" y2="40" stroke="#334155" stroke-width="1.5"/>'
                 # centre
                 '<circle cx="260" cy="160" r="46" fill="#0EA5E9" fill-opacity="0.12" stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="260" y="156" text-anchor="middle" fill="#0EA5E9" font-size="15" font-weight="700">CARE</text>'
                 '<text x="260" y="174" text-anchor="middle" fill="#0EA5E9" font-size="13">provision</text>'
                 # top - state
                 '<rect x="205" y="14" width="110" height="48" rx="8" fill="#10B981" fill-opacity="0.15" stroke="#10B981" stroke-width="2"/>'
                 '<text x="260" y="44" text-anchor="middle" fill="#10B981" font-size="14" font-weight="700">STATE</text>'
                 # right - market
                 '<rect x="400" y="136" width="110" height="48" rx="8" fill="#6366F1" fill-opacity="0.15" stroke="#6366F1" stroke-width="2"/>'
                 '<text x="455" y="166" text-anchor="middle" fill="#6366F1" font-size="14" font-weight="700">MARKET</text>'
                 # bottom - family
                 '<rect x="205" y="258" width="110" height="48" rx="8" fill="#F59E0B" fill-opacity="0.15" stroke="#F59E0B" stroke-width="2"/>'
                 '<text x="260" y="288" text-anchor="middle" fill="#F59E0B" font-size="14" font-weight="700">FAMILY</text>'
                 # left - community
                 '<rect x="10" y="136" width="110" height="48" rx="8" fill="#EF4444" fill-opacity="0.15" stroke="#EF4444" stroke-width="2"/>'
                 '<text x="65" y="166" text-anchor="middle" fill="#EF4444" font-size="13" font-weight="700">COMMUNITY</text>'
                 '</svg></div>')},
             {"t": "hbox", "color": "amber", "html": "When the state and market do little, the "
              "<strong>family</strong> corner &mdash; in practice, women &mdash; absorbs the rest."},
         ]},

        {"type": "content", "label": "Each Corner", "title": "The four providers of care",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Corner", "How it provides care", "Example in India"],
              "rows": [
                  ["State", "Public services, transfers, regulation", "Anganwadis, ASHAs, public health, maternity benefit"],
                  ["Market", "Paid services bought by households", "Cr&egrave;ches, private nurses, domestic workers"],
                  ["Family", "Unpaid care within the household", "Mothers, daughters, daughters-in-law"],
                  ["Community", "Informal mutual support", "Neighbours, kin networks, SHGs, faith groups"]]},
         ]},

        {"type": "content", "label": "Policy Choice", "title": "The diamond is a policy lever",
         "blocks": [
             {"t": "body", "html": "Where care sits in the diamond is a <em>choice</em>, not a "
              "given. Investing in the state and supporting the market corner shifts care off the "
              "family &mdash; off women &mdash; and into shared, paid provision."},
             {"t": "hbox", "color": "green", "html": "Rebalancing the diamond is exactly what the "
              "5 Rs framework, next, is designed to do."},
         ]},

        {"type": "content", "label": "The Multiplier", "title": "Care investment pays the economy back",
         "blocks": [
             {"t": "body", "html": "Investing in care is not only fair &mdash; it is effective "
              "stimulus. Care services are labour-intensive, so spending creates many jobs per "
              "rupee, much of it for women, while also freeing other women to work."},
             {"t": "hbox", "color": "cyan", "html": "Studies by the ILO and others find that "
              "investing in the care economy generates <em>more</em> jobs per unit of spending "
              "than equivalent investment in, say, construction."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "The 5 Rs Framework"},

        {"type": "content", "label": "The Toolkit", "title": "From analysis to action: the Rs",
         "blocks": [
             {"t": "body", "html": "The most influential policy framework for unpaid care began as "
              "Diane Elson's <strong>3 Rs &mdash; Recognise, Reduce, Redistribute</strong>. The "
              "ILO later extended it with two more: <strong>Represent</strong> and "
              "<strong>Reward</strong>."},
             {"t": "hbox", "color": "cyan", "html": "Together the 5 Rs turn the diagnosis &mdash; "
              "care is invisible and unequal &mdash; into a concrete agenda for policy and "
              "practice."},
         ]},

        {"type": "content", "label": "The Five", "title": "The 5 Rs at a glance",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["R", "Means", "Who proposed"],
              "rows": [
                  ["Recognise", "Make unpaid care visible &amp; count it", "Elson (3 Rs)"],
                  ["Reduce", "Cut the drudgery via infrastructure &amp; tech", "Elson (3 Rs)"],
                  ["Redistribute", "Shift care from women to men &amp; to the state", "Elson (3 Rs)"],
                  ["Represent", "Give carers &amp; care workers voice", "ILO addition"],
                  ["Reward", "Pay &amp; protect paid care workers decently", "ILO addition"]]},
             {"t": "hbox", "color": "amber", "html": "Attribution matters: Recognise&ndash;Reduce&ndash;"
              "Redistribute are Diane Elson's; Represent and Reward were added by the ILO."},
         ]},

        {"type": "content", "label": "R1", "title": "Recognise",
         "blocks": [
             {"t": "body", "html": "<strong>Recognise</strong> unpaid care as work &mdash; real, "
              "skilled, economically essential labour. This means measuring it (time-use surveys), "
              "naming it in policy, and valuing it in satellite accounts."},
             {"t": "hbox", "color": "cyan", "html": "Recognition is the precondition for everything "
              "else: you cannot reduce, redistribute or reward what you refuse to see."},
         ]},

        {"type": "content", "label": "R2", "title": "Reduce",
         "blocks": [
             {"t": "body", "html": "<strong>Reduce</strong> the sheer drudgery of care through "
              "infrastructure and technology &mdash; piped water, clean cooking fuel (LPG), "
              "electricity, sanitation, better transport."},
             {"t": "hbox", "color": "green", "html": "A tap in the home and an LPG stove can return "
              "hours a day to a woman. Schemes like Jal Jeevan Mission and Ujjwala are, in effect, "
              "care-reduction policies &mdash; even if rarely framed that way."},
         ]},

        {"type": "content", "label": "R3", "title": "Redistribute",
         "blocks": [
             {"t": "body", "html": "<strong>Redistribute</strong> the care that remains &mdash; "
              "from women to men within the household, and from families to the state and market. "
              "This is the hardest R, because it confronts gender norms head-on."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Within the home", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Men sharing cooking, cleaning, childcare; "
                   "paternity leave; changing norms about whose job care is."}]}],
              "right": [{"t": "panel", "color": "green", "title": "To state &amp; market", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Public cr&egrave;ches, eldercare, school "
                   "meals, anganwadis &mdash; care moved out of the household entirely."}]}]},
         ]},

        {"type": "content", "label": "R4", "title": "Represent",
         "blocks": [
             {"t": "body", "html": "<strong>Represent</strong> means giving carers and paid care "
              "workers a <em>voice</em> &mdash; in unions, collectives and policy-making &mdash; "
              "so that those who do care work help shape the rules that govern it."},
             {"t": "hbox", "color": "cyan", "html": "Domestic-worker unions and ASHA/anganwadi "
              "collectives bargaining for pay and protection are 'Represent' in action."},
         ]},

        {"type": "content", "label": "R5", "title": "Reward",
         "blocks": [
             {"t": "body", "html": "<strong>Reward</strong> paid care work properly &mdash; decent "
              "wages, social protection, safe conditions and recognition of skill. Today, care jobs "
              "are among the lowest-paid and least-protected, precisely because care is "
              "undervalued."},
             {"t": "hbox", "color": "amber", "html": "Reward closes the loop: it insists that the "
              "people society relies on to provide care are not themselves pushed into poverty by "
              "doing it."},
         ]},

        {"type": "content", "label": "Sequence", "title": "The Rs build on one another",
         "blocks": [
             {"t": "flow", "steps": [
                 "RECOGNISE: see &amp; count the care",
                 "REDUCE: cut the drudgery",
                 "REDISTRIBUTE: share what remains",
                 "REPRESENT &amp; REWARD: voice &amp; pay for carers"]},
             {"t": "hbox", "color": "cyan", "html": "They are not a menu to pick from but a "
              "sequence &mdash; recognition unlocks the rest, and reward without representation "
              "rarely sticks."},
         ]},

        {"type": "content", "label": "Using It", "title": "The 5 Rs as a programme checklist",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Recognise:</strong> does our data even capture unpaid care?",
                 "<strong>Reduce:</strong> are we cutting drudgery (water, fuel, transport)?",
                 "<strong>Redistribute:</strong> who carries the care our programme assumes?",
                 "<strong>Represent:</strong> do carers have a say in the design?",
                 "<strong>Reward:</strong> are the care workers we rely on paid and protected?"]},
             {"t": "hbox", "color": "cyan", "html": "Run any care-relevant intervention through "
              "the five Rs &mdash; gaps jump out fast."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Care Policies"},

        {"type": "content", "label": "The Levers", "title": "What care policy looks like",
         "blocks": [
             {"t": "body", "html": "Care policy is the set of public actions that recognise, "
              "reduce, redistribute, represent and reward care. Its main instruments cluster "
              "around children, the elderly, leave, and income support."},
             {"t": "flow", "steps": [
                 "SERVICES: childcare, eldercare, health",
                 "LEAVE: maternity, paternity, parental",
                 "TRANSFERS: maternity benefit, pensions",
                 "REGULATION: rights for care workers"]},
         ]},

        {"type": "content", "label": "Early Childhood", "title": "Childcare &amp; ECCE",
         "blocks": [
             {"t": "body", "html": "<strong>Early Childhood Care and Education (ECCE)</strong> "
              "&mdash; quality care and learning for children under six &mdash; does double duty: "
              "it nurtures children <em>and</em> frees mothers' time for paid work, study or rest."},
             {"t": "hbox", "color": "green", "html": "India's National Education Policy 2020 makes "
              "ECCE for all children up to age six a priority &mdash; a major care-policy commitment "
              "if resourced and delivered."},
         ]},

        {"type": "content", "label": "India's Backbone", "title": "Anganwadis and the ICDS",
         "blocks": [
             {"t": "body", "html": "The <strong>Integrated Child Development Services (ICDS)</strong>, "
              "delivered through <strong>anganwadi centres</strong>, is one of the world's largest "
              "care programmes &mdash; offering nutrition, pre-school and health services to young "
              "children and mothers."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "~14 lakh", "label": "anganwadi centres operating across India", "color": "cyan",
                  "source": "Ministry of Women &amp; Child Development"},
                 {"num": "Under 6", "label": "the age group ICDS is designed to reach, plus pregnant "
                  "&amp; nursing mothers", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Anganwadis are care infrastructure already in "
              "place &mdash; strengthening them is among the highest-leverage care investments India "
              "can make."},
         ]},

        {"type": "content", "label": "Time to Care", "title": "Parental leave",
         "blocks": [
             {"t": "body", "html": "Paid leave lets parents care for a new child without losing "
              "income. India's <strong>Maternity Benefit (Amendment) Act, 2017</strong> raised paid "
              "maternity leave to 26 weeks for eligible women in the organised sector."},
             {"t": "hbox", "color": "red", "html": "But two gaps remain: it covers mainly the "
              "<em>formal</em> sector &mdash; a small minority of working women &mdash; and offers "
              "little statutory <strong>paternity</strong> leave, leaving care 'her' job by default."},
         ]},

        {"type": "content", "label": "The Other End", "title": "Eldercare",
         "blocks": [
             {"t": "body", "html": "India is ageing fast. As elders multiply and joint families "
              "shrink, <strong>eldercare</strong> is becoming a major unmet need &mdash; today "
              "carried almost entirely by families, again mostly by women."},
             {"t": "hbox", "color": "amber", "html": "Old-age pensions, geriatric health services "
              "and supported eldercare are an emerging frontier of care policy &mdash; one most "
              "South Asian states are barely beginning to address."},
         ]},

        {"type": "content", "label": "The Safety Net", "title": "Social protection as care policy",
         "blocks": [
             {"t": "body", "html": "Pensions, maternity benefits, disability support and child "
              "grants are care policy by another name &mdash; they put resources behind the people "
              "doing or receiving care, reducing the unpaid burden."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Maternity benefit schemes (e.g. PMMVY) support new mothers",
                 "Old-age and widow pensions support elder and survivor care",
                 "Disability allowances recognise the cost of caring for and as disabled people"]},
         ]},

        {"type": "content", "label": "Models Abroad", "title": "What strong care systems look like",
         "blocks": [
             {"t": "body", "html": "Some countries treat care as core infrastructure: universal "
              "childcare, generous and shared parental leave, public eldercare, and decently paid "
              "care workers. The Nordic countries are the best-known example."},
             {"t": "hbox", "color": "cyan", "html": "The lesson for South Asia is not to copy a "
              "rich-country model wholesale, but to see that a high-care, high-participation "
              "equilibrium is a <em>policy choice</em>, not an accident of wealth."},
         ]},

        {"type": "content", "label": "Design Lens", "title": "Reading a policy through the care lens",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Does it <strong>reduce</strong> unpaid drudgery, or merely add to women's day?",
                 "Does it <strong>redistribute</strong> care, or assume women will absorb it?",
                 "Is it tied to formal employment &mdash; thereby excluding most women?",
                 "Does it fund the <strong>care workers</strong> who actually deliver it?"]},
             {"t": "hbox", "color": "cyan", "html": "A 'good' scheme that quietly relies on unpaid "
              "female time is shifting cost onto women, not solving the problem."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Paid Care Work"},

        {"type": "content", "label": "The Workforce", "title": "Who does paid care work?",
         "blocks": [
             {"t": "body", "html": "Paid care work spans the home, the clinic and the classroom: "
              "domestic workers, nurses and midwives, teachers, child- and eldercare staff, and "
              "India's vast army of frontline community health and nutrition workers."},
             {"t": "hbox", "color": "indigo", "html": "It is a heavily feminised workforce &mdash; "
              "women dominate paid care globally &mdash; which is one reason it is so persistently "
              "underpaid."},
         ]},

        {"type": "content", "label": "In the Home", "title": "Domestic workers",
         "blocks": [
             {"t": "body", "html": "Millions of women in India work as paid <strong>domestic "
              "workers</strong> &mdash; cooking, cleaning and caring in others' homes. Largely "
              "informal, the work is often unregulated, low-paid and without social protection."},
             {"t": "hbox", "color": "red", "html": "Because it happens in private homes and is seen "
              "as 'women's work', domestic labour is among the least protected forms of employment "
              "&mdash; despite the ILO's Domestic Workers Convention (C189) setting standards for it."},
         ]},

        {"type": "content", "label": "The Frontline", "title": "ASHA, anganwadi &amp; ANM workers",
         "blocks": [
             {"t": "body", "html": "India's public health and nutrition system runs on frontline "
              "women workers: <strong>ASHAs</strong> (community health), <strong>anganwadi "
              "workers</strong> (child development) and <strong>ANMs</strong> (auxiliary nurse "
              "midwives)."},
             {"t": "hbox", "color": "amber", "html": "ASHAs are formally 'volunteers' paid through "
              "task-based incentives rather than a salary &mdash; a vivid example of essential care "
              "labour kept cheap by being classed as something other than work."},
         ]},

        {"type": "content", "label": "The Penalty", "title": "The 'care penalty'",
         "blocks": [
             {"t": "term", "word": "Care penalty",
              "def": "The wage discount attached to care jobs: even after accounting for skill and "
              "education, work involving care for people tends to pay less than comparable work "
              "&mdash; a pattern documented by Nancy Folbre and others."},
             {"t": "body", "html": "The penalty is self-reinforcing: care is assumed to be a "
              "natural female trait rather than a skill, so it is paid as if anyone could do it for "
              "love &mdash; which keeps wages low and the workforce female."},
         ]},

        {"type": "content", "label": "Why It Persists", "title": "Why care work stays cheap",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Care is seen as an extension of women's 'natural' unpaid role &mdash; so 'worth less'",
                 "Its quality is hard to measure, so it is poorly rewarded",
                 "Much of it is informal, isolated, and hard to organise",
                 "Those who need care often cannot pay much, squeezing wages further"]},
             {"t": "hbox", "color": "amber", "html": "None of these is a law of nature. Each is a "
              "policy and norm choice that can be changed."},
         ]},

        {"type": "content", "label": "The Goal", "title": "Decent work for care workers",
         "blocks": [
             {"t": "body", "html": "The ILO's <strong>decent work</strong> agenda sets the standard "
              "for paid care: fair wages, social protection, safety, reasonable hours, and the "
              "right to organise &mdash; the 'Reward' and 'Represent' Rs in practice."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Minimum-wage coverage and timely pay",
                 "Social security: pensions, health, maternity",
                 "Recognition of skill and formal status",
                 "The right to unionise and bargain collectively"]},
         ]},

        {"type": "content", "label": "The Pay Gap", "title": "Care wages sit at the bottom",
         "blocks": [
             {"t": "chart", "canvas": "carePayChart",
              "title": "Average monthly earnings by occupation, relative to all workers (illustrative)",
              "source": "Illustrative, patterned on care-penalty wage research",
              "type": "bar",
              "data": {"labels": ["All workers", "Domestic workers", "Anganwadi / ASHA", "Private nurse"],
                       "datasets": [{"label": "Relative earnings (all workers = 100)",
                                     "data": [100, 48, 42, 70],
                                     "backgroundColor": ["#6366F1", "#EF4444", "#EF4444", "#F59E0B"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Earnings index (all=100)'}, min:0 } } }"}},
             {"t": "hbox", "color": "red", "html": "Illustrative pattern: paid care occupations "
              "cluster well below average earnings &mdash; the care penalty made visible."},
         ]},

        {"type": "content", "label": "The Stakes", "title": "Why decent care jobs matter twice over",
         "blocks": [
             {"t": "body", "html": "Improving paid care work is a <strong>double dividend</strong>: "
              "it lifts a large, female workforce out of low-wage precarity, <em>and</em> it raises "
              "the quality of the care that children, patients and elders receive."},
             {"t": "hbox", "color": "cyan", "html": "Underpaid, exhausted carers cannot give good "
              "care. Rewarding care workers is also a way of caring for everyone they serve."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Care in South Asia"},

        {"type": "content", "label": "The Context", "title": "Care in a region in transition",
         "blocks": [
             {"t": "body", "html": "South Asia carries a distinctive care profile: very high "
              "unpaid-care gender gaps, low female labour-force participation, thin public care "
              "services, and rapid demographic and social change all at once."},
             {"t": "hbox", "color": "indigo", "html": "Understanding care here means reading these "
              "forces together &mdash; family structure, migration, ageing and informality."},
         ]},

        {"type": "content", "label": "Family in Flux", "title": "Joint families and migration",
         "blocks": [
             {"t": "body", "html": "The <strong>joint family</strong> once spread care across many "
              "hands. As families nuclearise and working-age members migrate for work, that informal "
              "care network frays &mdash; leaving fewer people to care for children and elders."},
             {"t": "hbox", "color": "amber", "html": "Migration adds a twist: women left behind may "
              "gain autonomy but also absorb <em>all</em> the care once shared, while migrant women "
              "may leave their own families to care for others'."},
         ]},

        {"type": "content", "label": "The Crunch", "title": "The care crisis",
         "blocks": [
             {"t": "body", "html": "A <strong>care crisis</strong> emerges when care demand rises "
              "(more elders, more young children needing ECCE) while supply falls (smaller families, "
              "more women in paid work, weak public services) &mdash; with no one filling the gap."},
             {"t": "hbox", "color": "red", "html": "South Asia risks resolving this crisis the old "
              "way &mdash; by quietly loading still more unpaid work onto women &mdash; unless the "
              "state and market step in."},
         ]},

        {"type": "content", "label": "Greying", "title": "Ageing populations",
         "blocks": [
             {"t": "body", "html": "South Asian populations are ageing rapidly. India's share of "
              "people aged 60+ is projected to roughly <strong>double</strong> in the coming "
              "decades, sharply increasing the need for eldercare."},
             {"t": "hbox", "color": "amber", "html": "With pensions thin and eldercare services "
              "scarce, this demand will land first on families &mdash; and within families, on "
              "women &mdash; unless care policy gets ahead of it."},
         ]},

        {"type": "content", "label": "A Window", "title": "NEP, ECCE and the young",
         "blocks": [
             {"t": "body", "html": "At the other end of life, the region's still-large child "
              "population means early-childhood care is a present, not future, priority. India's "
              "<strong>NEP 2020</strong> and its push on <strong>ECCE</strong> offer a real "
              "opportunity to build care infrastructure for the young."},
             {"t": "hbox", "color": "green", "html": "Anganwadis upgraded into genuine ECCE centres "
              "could simultaneously support children's development and women's employment &mdash; a "
              "classic care 'double dividend'."},
         ]},

        {"type": "content", "label": "The Reality", "title": "Informality shapes everything",
         "blocks": [
             {"t": "body", "html": "The defining feature of South Asian care is <strong>informality</strong>: "
              "the vast majority of workers &mdash; and almost all care workers &mdash; are outside "
              "formal employment, beyond the reach of leave laws, social security and labour "
              "protection."},
             {"t": "hbox", "color": "red", "html": "Policies pegged to formal jobs &mdash; like "
              "26-week maternity leave &mdash; therefore miss most women. Care policy here must be "
              "designed for the informal majority, not the formal minority."},
         ]},

        {"type": "content", "label": "The Paradox", "title": "South Asia's care paradox",
         "blocks": [
             {"t": "body", "html": "South Asia presents a striking puzzle: women's education and "
              "household incomes have risen, yet female labour-force participation has stayed low "
              "&mdash; even fallen. The unequal, unsupported care burden is a leading explanation."},
             {"t": "hbox", "color": "red", "html": "Growth alone has not freed women's time. "
              "Without care services and shared care at home, rising prosperity leaves the unpaid "
              "burden intact &mdash; and women out of the paid workforce."},
         ]},

        {"type": "content", "label": "Bright Spots", "title": "What works in the region",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>SHGs &amp; collectives</strong> &mdash; SEWA, self-help groups organising "
                 "care and domestic workers",
                 "<strong>Cr&egrave;ches at worksites</strong> &mdash; e.g. mobile cr&egrave;ches "
                 "for construction workers' children",
                 "<strong>Community kitchens &amp; school meals</strong> &mdash; reducing the daily "
                 "cooking burden",
                 "<strong>Water &amp; LPG schemes</strong> &mdash; Jal Jeevan, Ujjwala cutting "
                 "fetching and fuel time"]},
             {"t": "hbox", "color": "cyan", "html": "The building blocks of a care system already "
              "exist in the region &mdash; the task is to fund, connect and scale them."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Practice &amp; Policy"},

        {"type": "content", "label": "The Case", "title": "Investing in the care economy",
         "blocks": [
             {"t": "body", "html": "The closing argument is simple: investing in care is one of the "
              "highest-return, most equitable investments a developing economy can make &mdash; for "
              "children, for women, for elders, and for growth itself."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Double dividend", "label": "care jobs created + other women freed to work",
                  "color": "green"},
                 {"num": "Human capital", "label": "healthier, better-raised, better-educated "
                  "future workers", "color": "cyan"}]},
         ]},

        {"type": "content", "label": "Jobs", "title": "Care investment as a jobs engine",
         "blocks": [
             {"t": "chart", "canvas": "careJobsChart",
              "title": "Jobs created per unit of public investment, by sector (illustrative)",
              "source": "Illustrative, patterned on ILO care-economy investment studies",
              "type": "bar",
              "data": {"labels": ["Care services", "Construction", "Manufacturing"],
                       "datasets": [{"label": "Relative jobs per unit invested",
                                     "data": [100, 55, 45],
                                     "backgroundColor": ["#10B981", "#F59E0B", "#6366F1"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Jobs per unit (care=100)'}, min:0 } } }"}},
             {"t": "hbox", "color": "green", "html": "Illustrative pattern, robust in direction: "
              "because care is labour-intensive, a rupee invested in care typically creates more "
              "jobs &mdash; many for women &mdash; than the same rupee in construction."},
         ]},

        {"type": "content", "label": "The Returns", "title": "What care investment buys",
         "blocks": [
             {"t": "table",
              "head": ["Invest in&hellip;", "Immediate effect", "Longer-run return"],
              "rows": [
                  ["Childcare / ECCE", "Frees mothers' time; care jobs", "Child development; women's earnings"],
                  ["Eldercare", "Relieves family carers", "Dignity for elders; women re-enter work"],
                  ["Water / fuel / sanitation", "Cuts unpaid drudgery hours", "Girls in school; women's health"],
                  ["Decent pay for care workers", "Lifts a feminised workforce", "Better-quality care for all"]]},
             {"t": "hbox", "color": "green", "html": "Every row delivers a care <em>and</em> an "
              "economic return &mdash; the heart of the 'care as investment' case."},
         ]},

        {"type": "content", "label": "For Practitioners", "title": "What this means for your work",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "<strong>Count care</strong> &mdash; build unpaid-care questions into your baselines",
                 "<strong>Don't free-ride on women</strong> &mdash; check whose unpaid time your "
                 "programme assumes",
                 "<strong>Reduce drudgery</strong> &mdash; water, fuel and childcare are care policy",
                 "<strong>Reward care workers</strong> &mdash; the ASHAs and anganwadi staff you "
                 "rely on deserve decent pay"]},
         ]},

        {"type": "content", "label": "For Policy", "title": "An agenda for care",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Fund ECCE and anganwadis as genuine care infrastructure",
                 "Extend leave and maternity benefits to informal workers",
                 "Build eldercare ahead of the ageing wave",
                 "Formalise, pay and protect the paid-care workforce",
                 "Invest in water, fuel and sanitation to cut unpaid hours"]},
             {"t": "hbox", "color": "cyan", "html": "Every item maps to an R &mdash; the framework "
              "doubles as a policy to-do list."},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "A short reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>The Invisible Heart: Economics and Family Values</em> &mdash; Nancy Folbre",
                 "<em>Who Pays for the Kids?</em> &mdash; Nancy Folbre (the economics of care)",
                 "Diane Elson &mdash; the 'Recognise, Reduce, Redistribute' framework",
                 "<em>Care Work and Care Jobs for the Future of Decent Work</em> &mdash; ILO (2018)",
                 "Shahra Razavi &mdash; the 'care diamond' (UNRISD, 2007)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Feminist Economics</strong>, <strong>Gender &amp; Development</strong> and "
              "<strong>Social Protection</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Care is the economy beneath the economy</strong> &mdash; everything rests on it",
                 "<strong>GDP hides unpaid care</strong> &mdash; the SNA boundary leaves it out",
                 "<strong>Care falls on women and girls</strong> &mdash; unequally, and at a cost",
                 "<strong>The 5 Rs are the toolkit</strong> &mdash; Recognise, Reduce, Redistribute, "
                 "Represent, Reward",
                 "<strong>Care is investment, not cost</strong> &mdash; and a powerful jobs engine"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Care Economy 101 &middot; Complete",
         "headline": "Now go make<br>care count.",
         "byline": "The work that holds everything else up has been invisible for too long. "
                   "Recognise it, reduce it, redistribute it, represent and reward those who do "
                   "it &mdash; and build the care economy your community already depends on. "
                   "Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
