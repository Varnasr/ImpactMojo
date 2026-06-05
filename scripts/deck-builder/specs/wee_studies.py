# -*- coding: utf-8 -*-
"""
Women's Economic Empowerment 101 — ImpactMojo 101 Series (native deck spec)
Foundational WEE for gender & development practitioners in South Asia (India-centric).
Build: python3 scripts/deck-builder/build.py wee_studies
"""

DECK = {
    "slug": "wee-studies",
    "title": "Women's Economic Empowerment 101",
    "description": ("Women's Economic Empowerment 101 — a free foundational course for gender "
                    "and development practitioners in South Asia: resources, agency and "
                    "achievements; the unpaid care economy; women's labour force participation; "
                    "pay gaps; land, finance and enterprise; norms, rights and what works. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Women's<br>Economic<br>Empowerment 101",
         "sub": "Resources, Agency &amp; Achievements &mdash; a Foundational Course on "
                "Women's Economic Empowerment for Gender &amp; Development Practitioners "
                "in South Asia",
         "tags": ["Research-Backed", "India-Centric", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Is Women's Economic Empowerment?"},
             {"name": "Why WEE Matters"},
             {"name": "The Unpaid Care Economy"},
             {"name": "Women's Labour Force Participation"},
             {"name": "Pay Gaps &amp; Occupational Segregation"},
             {"name": "Assets, Land &amp; Property"},
             {"name": "Financial Inclusion"},
             {"name": "Entrepreneurship &amp; Enterprise"},
             {"name": "Agency, Norms &amp; Decision-Making"},
             {"name": "Legal Rights &amp; the Enabling Environment"},
             {"name": "Measuring WEE &amp; What Works"},
         ]},

        # ===================== SECTION 01 — WHAT IS WEE =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Is Women's Economic Empowerment?"},

        {"type": "content", "label": "Definition", "title": "More than a job and an income",
         "blocks": [
             {"t": "body", "html": "Women's economic empowerment (WEE) is not just whether a "
              "woman earns. It is whether she can <strong>make and act on economic decisions</strong> "
              "&mdash; about her own work, money, assets and time &mdash; and benefit from them. "
              "Income without agency is not empowerment."},
             {"t": "term", "word": "Women's economic empowerment",
              "def": "The process by which women gain the power to make and act on economic "
              "decisions, expand their economic choices, and benefit from the resulting "
              "achievements &mdash; on terms they value."},
             {"t": "hbox", "color": "cyan", "html": "Keep the question economic <em>and</em> "
              "relational: not only 'does she have resources?' but 'can she decide and act?'"},
         ]},

        {"type": "content", "label": "Kabeer's Framework", "title": "Resources, agency, achievements",
         "blocks": [
             {"t": "body", "html": "Naila Kabeer's influential framework defines empowerment as "
              "the expansion of the ability to make strategic life choices for those previously "
              "denied it. It has three interlocking dimensions."},
             {"t": "flow", "steps": [
                 "RESOURCES: pre-conditions &mdash; income, land, credit, skills, networks",
                 "AGENCY: the process &mdash; the power to define goals and act on them",
                 "ACHIEVEMENTS: the outcomes &mdash; what the woman is able to be and do"]},
             {"t": "hbox", "color": "indigo", "html": "Empowerment is a <em>process</em>, not a "
              "fixed state &mdash; and only meaningful where real choice was previously absent."},
         ]},

        {"type": "content", "label": "Kabeer on Choice", "title": "Choice is the heart of it",
         "blocks": [
             {"t": "quote",
              "text": "Empowerment entails a process of change. People who exercise a great deal "
              "of choice in their lives may be very powerful, but they are not empowered, because "
              "they were never disempowered in the first place.",
              "attr": "&mdash; Naila Kabeer, 1999"},
             {"t": "body", "html": "The test is not the presence of choice in the abstract, but a "
              "movement from <strong>denial</strong> to <strong>the ability to choose</strong> "
              "&mdash; including the right to refuse work, to keep one's earnings, to own land."},
         ]},

        {"type": "content", "label": "Agency", "title": "Agency: more than the power to choose",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Forms of agency", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Decision-making &mdash; visible choices",
                      "Bargaining &amp; negotiation within the household",
                      "Resistance &amp; everyday subversion",
                      "Collective action &mdash; groups, unions"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Agency can be&hellip;", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Effective: she gets what she values",
                      "Or constrained: she 'chooses' within narrow limits",
                      "'Power within' &mdash; self-worth, voice",
                      "'Power to', 'power with', not just 'power over'"]}]}],
              },
             {"t": "hbox", "color": "amber", "html": "Watch for adaptive preferences: women may "
              "report satisfaction within unjust constraints. Voiced consent is not always free choice."},
         ]},

        {"type": "content", "label": "Not the Same Thing", "title": "Employment, work, empowerment",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Term", "What it captures", "Why it is not enough"],
              "rows": [
                  ["Employment", "A paid job", "Pay may be low, coerced, or controlled by others"],
                  ["Work", "All labour, paid &amp; unpaid", "Much of women's work is unpaid &amp; invisible"],
                  ["Income", "Earnings received", "She may not control how it is spent"],
                  ["Empowerment", "Resources + agency + achievements", "The fuller, harder goal"]]},
             {"t": "hbox", "color": "red", "html": "A garment worker on poverty wages with no say "
              "over her hours or pay is employed &mdash; not necessarily empowered."},
         ]},

        {"type": "content", "label": "Dimensions", "title": "WEE is multidimensional",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Economic", "label": "Earnings, assets, control over income &amp; spending",
                  "color": "cyan"},
                 {"num": "Social", "label": "Mobility, voice, status, freedom from violence",
                  "color": "green"},
                 {"num": "Relational", "label": "Bargaining power within household &amp; community",
                  "color": "indigo"}]},
             {"t": "body", "html": "These dimensions reinforce each other. A woman who owns land "
              "(economic) often gains standing in the household (relational) and the confidence to "
              "move and speak (social) &mdash; but the links are not automatic."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The terrain", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Care, labour force, pay &amp; segregation",
                      "Assets, land, finance, enterprise"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "The levers", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Agency, norms, legal rights",
                      "Measurement and what actually works"]}]}],
              },
             {"t": "hbox", "color": "cyan", "html": "Throughout, examples and data are "
              "India-centric &mdash; the realities you meet in gender &amp; development practice."},
         ]},

        # ===================== SECTION 02 — WHY WEE MATTERS =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Why WEE Matters"},

        {"type": "content", "label": "Rights First", "title": "The case begins with rights",
         "blocks": [
             {"t": "body", "html": "Women are entitled to economic autonomy because they are "
              "<strong>equal human beings</strong> &mdash; not because empowering them yields "
              "returns. The rights case is primary; everything else is secondary."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Equality and non-discrimination are constitutional and human-rights guarantees",
                 "India ratified CEDAW (1993) &mdash; the women's rights convention",
                 "Decent work and equal pay are rights, not rewards for being useful"]},
             {"t": "hbox", "color": "indigo", "html": "Lead with justice. The instrumental "
              "arguments that follow strengthen the case &mdash; they do not replace it."},
         ]},

        {"type": "content", "label": "The Development Case", "title": "Why economies need women's work too",
         "blocks": [
             {"t": "body", "html": "Alongside rights, there is a real development case. When women "
              "earn and decide, evidence repeatedly suggests benefits flow to children, households "
              "and economies &mdash; though magnitudes are debated and context-dependent."},
             {"t": "bullets", "items": [
                 "Women tend to invest a larger share of income in food, health and schooling",
                 "Excluding half the workforce leaves output and skills on the table",
                 "Women's bargaining power is linked to lower child malnutrition in many studies"]},
         ]},

        {"type": "content", "label": "The Big Number", "title": "The cost of the participation gap",
         "blocks": [
             {"t": "chart", "canvas": "weeGdpChart",
              "title": "Estimated GDP gain from closing gender gaps in work (illustrative)",
              "source": "Illustrative, patterned on McKinsey Global Institute &amp; ILO estimates",
              "type": "bar",
              "data": {"labels": ["Current path", "Full-potential scenario"],
                       "datasets": [{"label": "Relative GDP (indexed)",
                                     "data": [100, 127],
                                     "backgroundColor": ["#94A3B8", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:140, title:{display:true,text:'Indexed GDP'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Figures vary widely by study and assumptions "
              "(this bar is <strong>illustrative</strong>). The direction is robust: closing gender "
              "gaps in work could add substantially to GDP. Treat the exact percentage with care."},
         ]},

        {"type": "content", "label": "The Framing", "title": "'Smart economics' &mdash; what it claims",
         "blocks": [
             {"t": "body", "html": "Since the late 2000s, much WEE advocacy has used a "
              "<strong>'smart economics'</strong> frame: invest in women because it pays &mdash; for "
              "growth, for children, for poverty reduction. It was strategically powerful in "
              "unlocking funding and political will."},
             {"t": "term", "word": "Smart economics",
              "def": "The argument that gender equality, and women's economic participation in "
              "particular, is an efficient means to development and growth &mdash; a 'good investment'."},
         ]},

        {"type": "content", "label": "The Critique", "title": "Why 'smart economics' is contested",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Instrumentalises women</strong> &mdash; valued for their returns to others, "
                 "not as rights-holders",
                 "Treats women as a means to development, especially as efficient mothers and savers",
                 "Can <strong>add to women's burdens</strong> &mdash; more paid work atop unchanged "
                 "unpaid care",
                 "Sidelines structural causes: norms, power, discrimination, men's behaviour"]},
             {"t": "hbox", "color": "amber", "html": "Use the economic case to persuade &mdash; but "
              "anchor programmes in rights, or you risk 'empowering' women into double work days."},
         ]},

        {"type": "content", "label": "Both/And", "title": "Holding rights and returns together",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Rights-based core", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Women's economic autonomy is an end in "
                   "itself. The goal is freedom and equality, whatever the 'return'."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Development dividend", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Where it exists, the dividend is a welcome "
                   "bonus and a useful advocacy tool &mdash; not the justification."}]}],
              },
             {"t": "hbox", "color": "indigo", "html": "The mature position: rights first, returns "
              "alongside. Never let the business case crowd out the justice case."},
         ]},

        {"type": "content", "label": "The Win-Win Trap", "title": "When 'good for everyone' hides trade-offs",
         "blocks": [
             {"t": "body", "html": "'Win-win' framing assumes empowering women threatens no one. "
              "But power is partly redistributive: more agency for women can mean <strong>less "
              "control for men</strong>, and backlash is real. Pretending otherwise leaves women "
              "exposed."},
             {"t": "hbox", "color": "red", "html": "Honest programming plans for resistance &mdash; "
              "in the household, the market and the institution &mdash; rather than assuming "
              "everyone gains painlessly."},
         ]},

        # ===================== SECTION 03 — UNPAID CARE =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The Unpaid Care Economy"},

        {"type": "content", "label": "The Invisible Economy", "title": "The work that holds everything up",
         "blocks": [
             {"t": "body", "html": "Cooking, cleaning, fetching water and fuel, caring for children, "
              "the sick and the elderly &mdash; this <strong>unpaid care and domestic work</strong> "
              "sustains every household and economy. It is real work, largely done by women, and "
              "mostly absent from GDP."},
             {"t": "term", "word": "Unpaid care economy",
              "def": "The provision of care and domestic services within households and communities "
              "without monetary payment &mdash; essential to social reproduction, yet excluded "
              "from standard economic measures."},
         ]},

        {"type": "content", "label": "The Gap", "title": "Who does the unpaid work?",
         "blocks": [
             {"t": "chart", "canvas": "careTimeChart",
              "title": "Average minutes per day on unpaid domestic &amp; care work, by sex",
              "source": "Illustrative, patterned on India Time Use Survey 2019 (NSO)",
              "type": "bar",
              "data": {"labels": ["Unpaid domestic work", "Unpaid caregiving"],
                       "datasets": [
                           {"label": "Women", "data": [300, 135], "backgroundColor": "#6366F1"},
                           {"label": "Men", "data": [98, 76], "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ scales:{ y:{ title:{display:true,text:'Minutes per day'} } } }"}},
             {"t": "hbox", "color": "red", "html": "Pattern from the Time Use Survey 2019: women "
              "spend several times as many minutes on unpaid domestic work as men. Exact minutes "
              "here are <strong>illustrative</strong>; the large gap is well-established."},
         ]},

        {"type": "content", "label": "The Constraint", "title": "How care work blocks paid work",
         "blocks": [
             {"t": "flow", "steps": [
                 "Heavy unpaid care load falls on women",
                 "Less time &amp; flexibility for paid work",
                 "Women take part-time, home-based or no paid work",
                 "Lower earnings, weaker bargaining power, repeat"]},
             {"t": "hbox", "color": "amber", "html": "The care burden is a central reason women's "
              "labour force participation stays low. You cannot fix participation without "
              "addressing care."},
         ]},

        {"type": "content", "label": "Triple Burden", "title": "Productive, reproductive, community work",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Productive", "label": "Paid work &mdash; in fields, factories, services",
                  "color": "cyan"},
                 {"num": "Reproductive", "label": "Unpaid care &amp; domestic work at home",
                  "color": "indigo"},
                 {"num": "Community", "label": "Unpaid collective work &mdash; events, water, "
                  "local institutions", "color": "amber"}]},
             {"t": "body", "html": "Caroline Moser's 'triple role' framework: women routinely "
              "juggle all three, while men's roles are often counted only in the first. Planning "
              "that ignores the other two overloads women."},
         ]},

        {"type": "content", "label": "The 4 Rs", "title": "Recognise, reduce, redistribute, represent",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["R", "What it means", "Example"],
              "rows": [
                  ["Recognise", "Count care as real work", "Time-use surveys; valuing it in policy"],
                  ["Reduce", "Cut the drudgery", "Piped water, LPG, electricity, creches"],
                  ["Redistribute", "Share within household &amp; with the state", "Paternity leave, public childcare"],
                  ["Represent", "Give carers voice", "Carers in policy design &amp; unions"]]},
             {"t": "hbox", "color": "green", "html": "Diane Elson's 'three Rs' (recognise, reduce, "
              "redistribute), later extended to four, is the standard toolkit for the care economy."},
         ]},

        {"type": "content", "label": "Infrastructure", "title": "Care is also an infrastructure problem",
         "blocks": [
             {"t": "body", "html": "Much of women's unpaid time is spent compensating for missing "
              "public services. A piped water connection, an LPG cylinder, reliable electricity or "
              "a functioning anganwadi can free hours every day."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Water &amp; fuel collection can consume hours of women's and girls' time",
                 "Anganwadi &amp; creche services enable mothers to take paid work",
                 "Time saved on drudgery is time available for paid work, rest or schooling"]},
         ]},

        {"type": "content", "label": "Links", "title": "Connect to the Care Economy 101 deck",
         "blocks": [
             {"t": "body", "html": "Care is a vast topic in its own right &mdash; valuation methods, "
              "the care diamond, care workers' rights, public provisioning. This section is a bridge."},
             {"t": "hbox", "color": "indigo", "html": "For depth on measurement, financing and the "
              "care workforce, pair this with ImpactMojo's <strong>Care Economy 101</strong> deck."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "No WEE without rebalancing care",
         "blocks": [
             {"t": "quote",
              "text": "You cannot empower women economically while leaving the unpaid care economy "
              "untouched. The two are one problem.",
              "attr": "&mdash; a guiding principle for WEE programming"},
             {"t": "body", "html": "Every labour-force, enterprise or finance intervention should "
              "ask: what does this do to women's time? Add paid work without reducing care, and you "
              "deepen exhaustion, not empowerment."},
         ]},

        # ===================== SECTION 04 — LFPR =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Women's Labour Force Participation"},

        {"type": "content", "label": "The Headline", "title": "India's puzzle: low and long falling",
         "blocks": [
             {"t": "body", "html": "India has one of the world's <strong>lowest female labour force "
              "participation rates (LFPR)</strong>, and for much of the 2000s and 2010s it "
              "<strong>fell</strong> even as the economy grew and girls' education rose &mdash; a "
              "puzzle that has occupied economists for years."},
             {"t": "term", "word": "Labour force participation rate (LFPR)",
              "def": "The share of the working-age population that is either employed or actively "
              "seeking work. For women in India it has long been strikingly low by global standards."},
             {"t": "hbox", "color": "amber", "html": "Note the recent twist: PLFS data show female "
              "LFPR rising again since around 2017&ndash;18. Definitions and measurement matter a "
              "great deal here."},
         ]},

        {"type": "content", "label": "The Trend", "title": "A falling line, then an uptick",
         "blocks": [
             {"t": "chart", "canvas": "lfprTrendChart",
              "title": "India female LFPR over time (schematic of the documented pattern)",
              "source": "Illustrative, patterned on NSS &amp; PLFS estimates (usual status)",
              "type": "line",
              "data": {"labels": ["2004", "2009", "2011", "2017", "2019", "2022"],
                       "datasets": [{"label": "Female LFPR (%)",
                                     "data": [29, 23, 22, 23, 30, 37],
                                     "borderColor": "#EF4444",
                                     "backgroundColor": "rgba(239,68,68,0.08)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:50, title:{display:true,text:'Per cent'} } } }"}},
             {"t": "hbox", "color": "red", "html": "Schematic only &mdash; exact values are "
              "<strong>illustrative</strong> and definition-sensitive. The shape is real: a long "
              "decline, then a recent rise in PLFS, partly from changed measurement of women's work."},
         ]},

        {"type": "content", "label": "The U-Shape", "title": "Why participation may dip with development",
         "blocks": [
             {"t": "body", "html": "The <strong>'U-shaped' hypothesis</strong>: as incomes rise, "
              "female participation first falls &mdash; women leave low-paid farm and manual work as "
              "households can afford for them to &mdash; then rises again as education and "
              "white-collar jobs open up. India may be near the bottom of the U."},
             {"t": "flow", "steps": [
                 "Low income: women work out of necessity (high participation)",
                 "Rising income: women withdraw from drudgery (the dip)",
                 "Higher education + good jobs: women re-enter (the rise)"]},
         ]},

        {"type": "content", "label": "Explanations", "title": "Why is it so low? Competing reasons",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Explanation", "Mechanism"],
              "rows": [
                  ["Income effect", "As men earn more, families withdraw women from manual work"],
                  ["Unpaid care", "Care &amp; domestic burden leaves little time for paid work"],
                  ["Norms &amp; status", "Seclusion; 'respectable' families keep women out of the market"],
                  ["Missing jobs", "Too few suitable, safe, nearby jobs for educated women"],
                  ["Safety &amp; mobility", "Harassment, unsafe transport, restricted movement"],
                  ["Measurement", "Women's work undercounted, esp. unpaid family labour"]]},
             {"t": "hbox", "color": "amber", "html": "No single cause. It is demand (few good jobs) "
              "<em>and</em> supply (care, norms, safety) <em>and</em> measurement, together."},
         ]},

        {"type": "content", "label": "Measurement", "title": "How you count changes the answer",
         "blocks": [
             {"t": "body", "html": "Much of women's work &mdash; on family farms, in home-based "
              "production, in family enterprises &mdash; is unpaid and easily missed by surveys. "
              "Whether a woman who 'helps on the farm' counts as 'working' depends on the question "
              "and reference period."},
             {"t": "hbox", "color": "red", "html": "Part of the recent PLFS rise reflects "
              "<strong>better capture</strong> of women's own-account and unpaid family work &mdash; "
              "a measurement shift, not only a real-world one. Always check the definition."},
         ]},

        {"type": "content", "label": "Informality", "title": "Most working women are informal",
         "blocks": [
             {"t": "body", "html": "The vast majority of women who do work in India are in the "
              "<strong>informal economy</strong> &mdash; agriculture, domestic work, home-based "
              "production, petty trade, construction &mdash; without contracts, social security or "
              "stable pay."},
             {"t": "bullets", "color": "indigo", "items": [
                 "No written contract, no provident fund, no paid leave",
                 "Highly vulnerable to shocks &mdash; illness, drought, lockdowns",
                 "Often invisible in official employment statistics",
                 "Organisations like SEWA exist precisely to organise these workers"]},
         ]},

        {"type": "content", "label": "The Rural-Urban Split", "title": "Different stories by location",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Rural", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Higher participation, largely in agriculture "
                   "&amp; allied work &mdash; much of it unpaid family labour. MGNREGA provides a "
                   "rare source of paid, rights-based rural work for women."}]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Urban", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Lower participation; jobs concentrated in "
                   "domestic work, garments, and a small professional segment. Safety, commuting "
                   "and 'respectability' loom large."}]}],
              },
             {"t": "hbox", "color": "amber", "html": "Average national figures hide these very "
              "different realities. Always disaggregate by rural/urban and by social group."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "The puzzle, in one breath",
         "blocks": [
             {"t": "body", "html": "India's female LFPR is low and was long falling &mdash; driven "
              "by rising household incomes, the care burden, restrictive norms, a shortage of "
              "suitable safe jobs, and undercounting. The recent PLFS rise is partly real, partly "
              "better measurement."},
             {"t": "hbox", "color": "cyan", "html": "Hold all of it together: this is a labour-"
              "demand problem, a care problem, a norms problem and a measurement problem at once."},
         ]},

        # ===================== SECTION 05 — PAY GAP & SEGREGATION =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Pay Gaps &amp; Occupational Segregation"},

        {"type": "content", "label": "The Gap", "title": "Women earn less &mdash; even at the same work",
         "blocks": [
             {"t": "term", "word": "Gender pay gap",
              "def": "The difference between men's and women's earnings, usually expressed as a "
              "percentage of men's earnings. It reflects both different jobs and unequal pay for "
              "similar jobs."},
             {"t": "body", "html": "Part of the gap comes from women being concentrated in lower-"
              "paid work; part is unequal pay for the <em>same</em> work; and part is unexplained "
              "&mdash; the residue economists often read as discrimination."},
         ]},

        {"type": "content", "label": "Two Cuts", "title": "Explained and unexplained gaps",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "'Explained'", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Differences in measured factors &mdash; "
                   "education, experience, occupation, hours. Reducible in principle."}]}],
              "right": [{"t": "panel", "color": "red", "title": "'Unexplained'", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The portion left after accounting for those "
                   "factors &mdash; often interpreted as discrimination and unmeasured constraints."}]}],
              },
             {"t": "hbox", "color": "amber", "html": "Even the 'explained' part is not innocent: "
              "why are women in lower-paid occupations and working fewer paid hours in the first "
              "place? The constraints are themselves gendered."},
         ]},

        {"type": "content", "label": "Horizontal Segregation", "title": "Different jobs for women and men",
         "blocks": [
             {"t": "term", "word": "Horizontal segregation",
              "def": "The clustering of women and men into different occupations and sectors "
              "&mdash; e.g. women in nursing, teaching, domestic work, garments; men in "
              "construction, transport, engineering."},
             {"t": "body", "html": "'Women's work' is systematically valued and paid less &mdash; "
              "care and service roles in particular &mdash; even when it requires comparable skill. "
              "The label of femininity itself depresses the wage."},
         ]},

        {"type": "content", "label": "Vertical Segregation", "title": "The ceiling and the sticky floor",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Glass ceiling", "label": "Women under-represented at the top &mdash; "
                  "boards, senior management, leadership", "color": "indigo"},
                 {"num": "Sticky floor", "label": "Women over-represented at the bottom &mdash; "
                  "lowest grades, no progression", "color": "red"}]},
             {"t": "body", "html": "<strong>Vertical segregation</strong>: even within the same "
              "sector, women cluster in lower ranks. Boardrooms and senior posts remain heavily "
              "male despite women entering at the base."},
         ]},

        {"type": "content", "label": "Visualising", "title": "Where the gap shows up",
         "blocks": [
             {"t": "chart", "canvas": "payGapChart",
              "title": "Illustrative gender pay gap across job tiers",
              "source": "Illustrative &mdash; for teaching the pattern, not actual figures",
              "type": "bar",
              "data": {"labels": ["Casual labour", "Salaried entry", "Mid management", "Senior leadership"],
                       "datasets": [
                           {"label": "Men's earnings (indexed)", "data": [100, 100, 100, 100],
                            "backgroundColor": "#0EA5E9"},
                           {"label": "Women's earnings (indexed)", "data": [70, 80, 75, 65],
                            "backgroundColor": "#EF4444"}]},
              "options": {"__js__": "{ scales:{ y:{ min:0, max:110, title:{display:true,text:'Earnings (men = 100)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Numbers are <strong>illustrative</strong>. "
              "The teaching point: gaps persist across tiers and can <em>widen</em> at the top."},
         ]},

        {"type": "content", "label": "Motherhood Penalty", "title": "The penalty for becoming a mother",
         "blocks": [
             {"t": "term", "word": "Motherhood penalty",
              "def": "The earnings and employment loss women experience after having children "
              "&mdash; through dropping out, reduced hours, missed promotions and employer bias "
              "&mdash; with no equivalent 'fatherhood penalty'."},
             {"t": "body", "html": "Fathers often see a <em>premium</em>; mothers a penalty. The "
              "asymmetry tracks who is assumed to do the unpaid care &mdash; tying this section "
              "straight back to the care economy."},
         ]},

        {"type": "content", "label": "The Law", "title": "Equal remuneration is a legal right",
         "blocks": [
             {"t": "body", "html": "India's <strong>Equal Remuneration Act, 1976</strong> mandated "
              "equal pay for equal work and barred discrimination in recruitment. Its provisions "
              "are now subsumed within the <strong>Code on Wages, 2019</strong>."},
             {"t": "hbox", "color": "red", "html": "Law on paper is not pay in hand. Enforcement is "
              "weak, the informal sector is largely beyond reach, and proving 'equal work' is hard. "
              "Rights need teeth and awareness to bite."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "The gap is structural, not personal",
         "blocks": [
             {"t": "body", "html": "The pay gap is not mainly about women's choices or 'lower "
              "ambition'. It is built from segregation, the devaluation of care work, the "
              "motherhood penalty and outright discrimination &mdash; all structural."},
             {"t": "hbox", "color": "cyan", "html": "Close it by valuing care work, breaking "
              "occupational silos, sharing unpaid work, and enforcing equal-pay law &mdash; not by "
              "telling women to 'lean in'."},
         ]},

        # ===================== SECTION 06 — ASSETS, LAND & PROPERTY =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Assets, Land &amp; Property"},

        {"type": "content", "label": "Why Assets", "title": "Assets, not just income, change power",
         "blocks": [
             {"t": "body", "html": "Income can be spent or controlled by others; <strong>assets</strong> "
              "&mdash; land, a house, livestock, savings &mdash; provide security, collateral, "
              "status and a fallback. Asset ownership is among the strongest correlates of women's "
              "bargaining power."},
             {"t": "quote",
              "text": "The single most important economic factor affecting women's situation is "
              "the gender gap in command over property.",
              "attr": "&mdash; Bina Agarwal, <em>A Field of One's Own</em>"},
         ]},

        {"type": "content", "label": "The Asset Gap", "title": "Women own far less than men",
         "blocks": [
             {"t": "chart", "canvas": "assetGapChart",
              "title": "Illustrative ownership gap, women vs men",
              "source": "Illustrative, patterned on agricultural census &amp; NFHS land/house data",
              "type": "bar",
              "data": {"labels": ["Own agricultural land", "Own a house (sole/joint)", "Operate a landholding"],
                       "datasets": [
                           {"label": "Women", "data": [14, 42, 14], "backgroundColor": "#6366F1"},
                           {"label": "Men", "data": [55, 70, 86], "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ scales:{ y:{ min:0, max:100, title:{display:true,text:'Per cent'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Bars are <strong>illustrative</strong>. The "
              "well-documented reality: women operate only a small share of agricultural land "
              "despite doing much of the farm work."},
         ]},

        {"type": "content", "label": "The Paradox", "title": "Women farm the land they don't own",
         "blocks": [
             {"t": "body", "html": "Agriculture in India is increasingly <strong>feminised</strong> "
              "&mdash; as men migrate, women do more of the field labour and management. Yet land "
              "titles, and the credit, subsidies and schemes tied to them, remain overwhelmingly "
              "in men's names."},
             {"t": "hbox", "color": "red", "html": "Without title, women farmers are often invisible "
              "to extension services, crop loans and insurance &mdash; doing the work, denied the "
              "tools."},
         ]},

        {"type": "content", "label": "Inheritance", "title": "Inheritance: where the gap is made",
         "blocks": [
             {"t": "body", "html": "Most women's potential route to land is <strong>inheritance</strong>, "
              "yet custom long favoured sons. Daughters were expected to receive dowry instead of a "
              "share of ancestral property &mdash; trading a one-off transfer for a lasting asset."},
             {"t": "bullets", "color": "indigo", "items": [
                 "Sons inherit ancestral land; daughters 'marry out'",
                 "Dowry treated as a substitute for inheritance",
                 "Family pressure on daughters to relinquish claims to keep peace"]},
         ]},

        {"type": "content", "label": "The 2005 Reform", "title": "Hindu Succession (Amendment) Act, 2005",
         "blocks": [
             {"t": "body", "html": "The <strong>Hindu Succession (Amendment) Act, 2005</strong> was "
              "a landmark: it made <strong>daughters equal coparceners</strong> by birth in "
              "ancestral (joint family) property, on the same footing as sons."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Equal coparcener", "label": "Daughters get the same birthright in "
                  "ancestral property as sons", "color": "green",
                  "source": "Hindu Succession (Amendment) Act, 2005"},
                 {"num": "By birth", "label": "The right vests at birth &mdash; later clarified "
                  "to apply regardless of when father died", "color": "cyan"}]},
         ]},

        {"type": "content", "label": "Law vs Practice", "title": "A strong law, slow to reach the field",
         "blocks": [
             {"t": "body", "html": "Studies find the 2005 amendment improved some daughters' access "
              "to land &mdash; but change has been uneven. Awareness is low, land records lag, and "
              "social pressure to forgo claims persists."},
             {"t": "hbox", "color": "amber", "html": "Personal laws differ across communities, and "
              "the Act covers Hindus, Buddhists, Jains and Sikhs. Legal reform is necessary but far "
              "from sufficient &mdash; norms and records must move too."},
         ]},

        {"type": "content", "label": "Joint Titling", "title": "Putting women's names on the paper",
         "blocks": [
             {"t": "body", "html": "Beyond inheritance, programmes promote <strong>joint or "
              "individual titling</strong> &mdash; adding women's names to land patta, house "
              "allotments and resettlement deeds. Many housing schemes now require or favour "
              "women's ownership."},
             {"t": "bullets", "color": "green", "items": [
                 "Women's names on house/land titles in welfare schemes",
                 "Joint patta in land distribution programmes",
                 "Asset ownership linked to lower domestic violence in several studies"]},
         ]},

        {"type": "content", "label": "Takeaway", "title": "A field of one's own",
         "blocks": [
             {"t": "body", "html": "Land and assets in a woman's own name shift power more durably "
              "than income alone. The 2005 reform opened the legal door; closing the gap needs "
              "awareness, clean records, and norms that accept daughters as owners."},
             {"t": "hbox", "color": "cyan", "html": "When you design any asset transfer &mdash; "
              "house, land, livestock &mdash; ask whose name is on it. That choice is the "
              "intervention."},
         ]},

        # ===================== SECTION 07 — FINANCIAL INCLUSION =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Financial Inclusion"},

        {"type": "content", "label": "The Idea", "title": "An account of her own",
         "blocks": [
             {"t": "body", "html": "<strong>Financial inclusion</strong> &mdash; access to a bank "
              "account, savings, credit, insurance and payments &mdash; gives a woman a place to "
              "keep money out of others' reach, a way to receive wages and benefits directly, and "
              "a foothold for enterprise."},
             {"t": "hbox", "color": "cyan", "html": "But an account is a tool, not empowerment "
              "itself. The question is whether she <em>uses</em> and <em>controls</em> it &mdash; "
              "not just whether it exists."},
         ]},

        {"type": "content", "label": "Self-Help Groups", "title": "The SHG: India's signature model",
         "blocks": [
             {"t": "term", "word": "Self-help group (SHG)",
              "def": "A small group, typically 10&ndash;20 women, who pool regular savings, lend "
              "to each other, and over time link to a bank for larger loans &mdash; building "
              "credit, solidarity and collective voice."},
             {"t": "body", "html": "SHGs combine thrift, micro-credit and a regular meeting that "
              "doubles as a platform for information, training and collective action &mdash; one "
              "of the largest women's movements in the world by membership."},
         ]},

        {"type": "content", "label": "SHG-Bank Linkage", "title": "How the SHG-bank linkage works",
         "blocks": [
             {"t": "flow", "steps": [
                 "Women form a group &amp; save regularly",
                 "Group lends internally from the pooled fund",
                 "Group opens a bank account &amp; builds a track record",
                 "Bank lends to the group (linkage) at scale"]},
             {"t": "hbox", "color": "green", "html": "Pioneered with NABARD support, the "
              "SHG-Bank Linkage Programme connects millions of groups to formal banking &mdash; "
              "credit without individual collateral, backed by group guarantee."},
         ]},

        {"type": "content", "label": "Scale", "title": "From groups to a national mission",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "DAY-NRLM", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The Deendayal Antyodaya Yojana &mdash; "
                   "National Rural Livelihoods Mission federates SHGs into village and cluster "
                   "organisations across India, layering on livelihoods support."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Kudumbashree", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Kerala's celebrated women's network &mdash; "
                   "neighbourhood groups linked to local government, running enterprises and "
                   "anti-poverty work at massive scale."}]}],
              },
             {"t": "hbox", "color": "amber", "html": "These models show SHGs can be more than "
              "credit &mdash; a base for livelihoods, governance and collective bargaining."},
         ]},

        {"type": "content", "label": "JAM", "title": "Jan Dhan, Aadhaar, Mobile",
         "blocks": [
             {"t": "body", "html": "<strong>PM Jan Dhan Yojana</strong> opened hundreds of millions "
              "of basic bank accounts &mdash; a large share for women. Linked with Aadhaar identity "
              "and Mobile phones (the <strong>'JAM' trinity</strong>), it enables direct benefit "
              "transfers into women's own accounts."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Direct transfer", "label": "Wages &amp; benefits paid into her account, "
                  "bypassing intermediaries", "color": "green"},
                 {"num": "Dormancy risk", "label": "Many accounts opened; fewer actively used or "
                  "controlled by the woman", "color": "red"}]},
         ]},

        {"type": "content", "label": "Mobile Money", "title": "Phones, the digital gender gap",
         "blocks": [
             {"t": "body", "html": "Mobile money and digital payments can extend finance to remote "
              "women &mdash; but only if they own and control a phone. India has a real "
              "<strong>digital gender gap</strong>: women are less likely to own a phone, have data, "
              "or use it independently."},
             {"t": "hbox", "color": "amber", "html": "Digitisation can include or exclude. If the "
              "phone is the husband's and the PIN is shared, 'her' account may not be hers in "
              "practice."},
         ]},

        {"type": "content", "label": "Microfinance", "title": "Microcredit: promise and peril",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Promise", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Small loans without collateral",
                      "Smoothing consumption &amp; shocks",
                      "Seed capital for tiny enterprises"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Peril", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Over-indebtedness &amp; multiple loans",
                      "Coercive collection; high effective rates",
                      "Loans used by men, repaid by women"]}]}],
              },
             {"t": "hbox", "color": "amber", "html": "The Andhra Pradesh microfinance crisis (2010) "
              "was a warning: credit pushed without livelihoods or protection can trap, not "
              "empower."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Access is the start, control is the goal",
         "blocks": [
             {"t": "body", "html": "India has made huge strides in financial access &mdash; SHGs, "
              "Jan Dhan, DBT. The frontier now is <strong>usage and control</strong>: an account "
              "she operates, credit she chooses, debt she can carry."},
             {"t": "hbox", "color": "cyan", "html": "Measure inclusion by active, independent use "
              "&mdash; not by accounts opened. And watch debt: empowerment is not a heavier loan."},
         ]},

        # ===================== SECTION 08 — ENTREPRENEURSHIP =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Entrepreneurship &amp; Enterprise"},

        {"type": "content", "label": "The Landscape", "title": "Women-led enterprise in India",
         "blocks": [
             {"t": "body", "html": "Women own a minority of India's enterprises, and women-led "
              "firms are concentrated among the smallest <strong>micro and own-account</strong> "
              "units &mdash; tailoring, food, beauty, petty trade &mdash; with limited capital and "
              "few employees."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Mostly micro", "label": "Women-led firms cluster at the smallest, "
                  "lowest-capital end", "color": "cyan"},
                 {"num": "Often survivalist", "label": "Necessity-driven self-employment, not "
                  "high-growth ambition", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Necessity vs Opportunity", "title": "Two very different entrepreneurs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Necessity-driven", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Starts a tiny venture because no wage job is "
                   "available or suitable. Low margins, survival mode, home-based to manage care."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Opportunity-driven", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Spots a market gap and chooses to build a "
                   "growth business. Far rarer for women, and where most policy attention goes."}]}],
              },
             {"t": "hbox", "color": "indigo", "html": "Most women entrepreneurs in India are "
              "nearer the necessity end. Policy designed for the opportunity end can miss them "
              "entirely."},
         ]},

        {"type": "content", "label": "Barriers", "title": "The wall women entrepreneurs hit",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Barrier", "How it bites"],
              "rows": [
                  ["Credit", "Banks want collateral &amp; titles women rarely hold"],
                  ["Mobility", "Restricted travel limits markets, suppliers, training"],
                  ["Networks", "Business networks are male; women lack mentors &amp; contacts"],
                  ["Markets", "Harder to reach buyers, negotiate, scale beyond the local"],
                  ["Care &amp; time", "Enterprise squeezed around unpaid domestic work"],
                  ["Skills &amp; confidence", "Less access to training; norms dampen ambition"]]},
             {"t": "hbox", "color": "red", "html": "These barriers compound. Easing credit alone, "
              "without mobility, markets and care, rarely moves women's firms up."},
         ]},

        {"type": "content", "label": "Credit Gap", "title": "The missing collateral",
         "blocks": [
             {"t": "body", "html": "Because women own little land or property, they struggle to "
              "offer the collateral banks expect &mdash; tying enterprise straight back to the "
              "asset gap of Section Six. Schemes like <strong>MUDRA</strong> and "
              "<strong>Stand-Up India</strong> aim to widen collateral-light lending to women."},
             {"t": "hbox", "color": "amber", "html": "Loan schemes help, but a loan is not a "
              "market. Many women-led units fail for lack of demand and linkages, not just "
              "capital."},
         ]},

        {"type": "content", "label": "Value Chains", "title": "Where women sit in the value chain",
         "blocks": [
             {"t": "flow", "steps": [
                 "Women cluster in low-value nodes: raw production, processing, piece-work",
                 "Higher-value nodes &mdash; aggregation, branding, retail &mdash; are male-dominated",
                 "Value &amp; margin concentrate downstream, away from women",
                 "Upgrading women's position in the chain raises their returns"]},
             {"t": "hbox", "color": "cyan", "html": "Producer collectives and women-led FPOs "
              "(farmer producer organisations) help women capture more of the chain &mdash; "
              "aggregating, processing and selling collectively."},
         ]},

        {"type": "content", "label": "Collectives", "title": "Doing business together",
         "blocks": [
             {"t": "body", "html": "Collective enterprise &mdash; SHG federations, producer "
              "companies, cooperatives &mdash; lets women pool capital, share risk, reach bigger "
              "markets and bargain. SEWA's cooperatives and Lijjat's papad network are iconic "
              "examples."},
             {"t": "bullets", "color": "green", "items": [
                 "Aggregation gives scale and bargaining power",
                 "Shared assets &amp; services lower individual cost",
                 "Solidarity buffers shocks and builds voice"]},
         ]},

        {"type": "content", "label": "Beyond Capital", "title": "What women's enterprise really needs",
         "blocks": [
             {"t": "body", "html": "Evidence suggests that for many women, a one-off cash grant or "
              "loan does little on its own. Bundling capital with <strong>skills, mentoring, market "
              "links and confidence-building</strong> &mdash; and easing the care load &mdash; works "
              "far better."},
             {"t": "hbox", "color": "indigo", "html": "Design for the woman's whole reality: her "
              "time, mobility and household, not just her balance sheet."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Enterprise is embedded, not isolated",
         "blocks": [
             {"t": "body", "html": "Women's enterprise cannot be lifted by credit alone. It sits "
              "inside the same web &mdash; assets, mobility, norms, care, networks &mdash; that "
              "shapes everything else in this course."},
             {"t": "hbox", "color": "cyan", "html": "The most effective enterprise programmes are "
              "really WEE programmes: they address the constraints around the business, not only "
              "the business."},
         ]},

        # ===================== SECTION 09 — AGENCY, NORMS, DECISION-MAKING =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Agency, Norms &amp; Decision-Making"},

        {"type": "content", "label": "The Household", "title": "The household is not a single mind",
         "blocks": [
             {"t": "body", "html": "Economics long modelled the household as one decision-maker "
              "pooling everything. In reality, members have <strong>different preferences and "
              "unequal power</strong>. Who earns, who owns and who decides shapes how resources "
              "are actually shared."},
             {"t": "term", "word": "Intra-household bargaining",
              "def": "The negotiation between household members over how to allocate resources, "
              "labour and consumption &mdash; in which a person's 'fallback position' (what they "
              "could get outside the household) shapes their power within it."},
         ]},

        {"type": "content", "label": "Bargaining Power", "title": "What strengthens her hand",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Own income</strong> &mdash; especially if she controls it",
                 "<strong>Assets in her name</strong> &mdash; land, house, savings",
                 "<strong>A credible outside option</strong> &mdash; natal family support, ability to leave",
                 "<strong>Social networks</strong> &mdash; SHGs, friends, collective backing"]},
             {"t": "hbox", "color": "cyan", "html": "This is why <em>control</em>, not just access, "
              "matters: an asset she can credibly fall back on changes her voice at home."},
         ]},

        {"type": "content", "label": "Measuring Decisions", "title": "Decision-making as an indicator",
         "blocks": [
             {"t": "body", "html": "Surveys like NFHS ask who decides on health care, large "
              "purchases, visits to family, and use of the woman's own earnings &mdash; a common "
              "proxy for agency."},
             {"t": "hbox", "color": "amber", "html": "Read it carefully: 'joint' decisions can mask "
              "male dominance, and 'she decides' on a trivial matter is not the same as power over "
              "big ones. The indicator is a clue, not the whole story."},
         ]},

        {"type": "content", "label": "Social Norms", "title": "The invisible rulebook",
         "blocks": [
             {"t": "term", "word": "Social norm",
              "def": "An unwritten rule about what people in a group are expected to do, sustained "
              "by social approval and sanction &mdash; e.g. that 'good' women stay home, or that "
              "wage work for women shames the family."},
             {"t": "body", "html": "Norms operate even without a law or a locked door. Women may "
              "restrict themselves because they anticipate gossip, disapproval or worse. Changing "
              "norms means changing what people believe <em>others</em> expect."},
         ]},

        {"type": "content", "label": "Backlash", "title": "When empowerment provokes resistance",
         "blocks": [
             {"t": "body", "html": "Gains in women's earning or autonomy can trigger "
              "<strong>backlash</strong> &mdash; from partners, families or communities &mdash; "
              "including controlling behaviour and, in some cases, violence. Some studies link "
              "rising women's income to short-term increases in conflict."},
             {"t": "hbox", "color": "red", "html": "Do no harm: WEE programming must anticipate "
              "backlash, engage men and families, and never leave a woman more exposed for having "
              "taken part."},
         ]},

        {"type": "content", "label": "Mobility & Safety", "title": "Freedom of movement is economic",
         "blocks": [
             {"t": "body", "html": "If a woman cannot travel safely to a job, a market, a bank or "
              "training, her economic options shrink to whatever is within walking distance of "
              "home. <strong>Mobility and safety are economic infrastructure</strong> for women."},
             {"t": "bullets", "color": "indigo", "items": [
                 "Harassment on transport &amp; in public space deters participation",
                 "Curfews and 'permission' regimes limit hours and distance",
                 "Safe transport &amp; workplaces expand the real choice set"]},
         ]},

        {"type": "content", "label": "Engaging Men", "title": "Norms change is everyone's work",
         "blocks": [
             {"t": "body", "html": "Because norms and unpaid care are held collectively, lasting "
              "change needs <strong>men and boys, families and communities</strong> &mdash; not "
              "women-only interventions. Redistributing care and respecting women's choices is a "
              "household project."},
             {"t": "hbox", "color": "green", "html": "Effective programmes work with husbands, "
              "in-laws and male leaders &mdash; reframing women's work and shared care as normal "
              "and respectable."},
         ]},

        {"type": "content", "label": "Unpaid to Paid", "title": "The fraught transition to paid work",
         "blocks": [
             {"t": "body", "html": "Moving women from unpaid family labour into recognised, paid "
              "work is a core WEE goal &mdash; but it is not automatic empowerment. It can mean "
              "longer total work days, contested earnings and renegotiated roles."},
             {"t": "hbox", "color": "cyan", "html": "The transition empowers only when care is "
              "shared, earnings are hers to control, and the work itself is decent. Track all "
              "three."},
         ]},

        # ===================== SECTION 10 — LEGAL RIGHTS & ENABLING ENVIRONMENT =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Legal Rights &amp; the Enabling Environment"},

        {"type": "content", "label": "The Frame", "title": "Rights make empowerment durable",
         "blocks": [
             {"t": "body", "html": "Individual gains can be reversed; <strong>rights and "
              "institutions</strong> make them durable. The enabling environment &mdash; laws, "
              "social protection, public services &mdash; sets the floor beneath women's economic "
              "lives."},
             {"t": "hbox", "color": "cyan", "html": "This section maps the key Indian legal "
              "guarantees and what they do &mdash; and where they fall short in practice."},
         ]},

        {"type": "content", "label": "Maternity", "title": "Maternity Benefit (Amendment) Act, 2017",
         "blocks": [
             {"t": "body", "html": "The <strong>Maternity Benefit (Amendment) Act, 2017</strong> "
              "extended paid maternity leave from 12 to <strong>26 weeks</strong> for eligible "
              "women, and mandated creche facilities in larger establishments."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "26 weeks", "label": "paid maternity leave for eligible women", "color": "green",
                  "source": "Maternity Benefit (Amendment) Act, 2017"},
                 {"num": "Creche", "label": "mandatory in establishments above a size threshold",
                  "color": "cyan"}]},
             {"t": "hbox", "color": "amber", "html": "Reach is the catch: it covers the small "
              "formal sector. The vast informal workforce is largely outside it &mdash; and some "
              "employers may avoid hiring women to dodge the cost."},
         ]},

        {"type": "content", "label": "Workplace Safety", "title": "The PoSH Act, 2013",
         "blocks": [
             {"t": "body", "html": "The <strong>Sexual Harassment of Women at Workplace "
              "(Prevention, Prohibition and Redressal) Act, 2013</strong> &mdash; the 'PoSH Act' "
              "&mdash; requires employers to prevent and redress sexual harassment, including "
              "<strong>Internal Committees</strong> in workplaces above a size threshold."},
             {"t": "bullets", "color": "indigo", "items": [
                 "Grew out of the Supreme Court's Vishaka Guidelines (1997)",
                 "Defines harassment and a formal complaints process",
                 "Extends, in principle, to the unorganised sector via Local Committees"]},
             {"t": "hbox", "color": "red", "html": "Implementation is patchy &mdash; many "
              "workplaces lack functioning committees, and informal workers rarely access redress."},
         ]},

        {"type": "content", "label": "MGNREGA", "title": "MGNREGA's quiet gender provisions",
         "blocks": [
             {"t": "body", "html": "The <strong>Mahatma Gandhi National Rural Employment Guarantee "
              "Act, 2005</strong> guarantees wage work and builds in gender provisions: at least a "
              "third of work for women, <strong>equal wages</strong> for women and men, worksite "
              "creches, and work close to home."},
             {"t": "hbox", "color": "green", "html": "For many rural women MGNREGA is a rare source "
              "of paid, equal-wage, rights-based work &mdash; paid into their own accounts &mdash; "
              "and a meaningful lift to bargaining power."},
         ]},

        {"type": "content", "label": "Social Protection", "title": "The safety net and its holes",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Instrument", "What it offers women"],
              "rows": [
                  ["MGNREGA", "Guaranteed rural wage work at equal wages"],
                  ["Maternity benefits / PMMVY", "Cash support around childbirth"],
                  ["Pensions (widow, old-age)", "Income floor for vulnerable women"],
                  ["PDS / nutrition schemes", "Food security; ICDS for mothers &amp; children"],
                  ["E-Shram / informal worker registries", "A route towards covering informal workers"]]},
             {"t": "hbox", "color": "amber", "html": "The biggest hole: most women work informally "
              "and fall outside employment-linked protections. Universal, portable schemes matter "
              "most for them."},
         ]},

        {"type": "content", "label": "The Gap", "title": "Rights on paper, rights in practice",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "On paper", "blocks": [
                  {"t": "body", "cls": "sm", "html": "India has a strong scaffolding of laws: "
                   "equal pay, maternity, PoSH, inheritance, work guarantee."}]}],
              "right": [{"t": "panel", "color": "red", "title": "In practice", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Weak enforcement, low awareness, informal-"
                   "sector exclusion, and norms that deter women from claiming what is theirs."}]}],
              },
             {"t": "hbox", "color": "indigo", "html": "Legal literacy and accessible redress are "
              "as important as the laws themselves. A right unknown or unenforced is no right at "
              "all."},
         ]},

        {"type": "content", "label": "The Double Edge", "title": "Protection that can backfire",
         "blocks": [
             {"t": "body", "html": "Some protective provisions can, perversely, discourage hiring "
              "women if employers see them as costs &mdash; the maternity-cost worry is the "
              "classic case. The answer is usually to <strong>socialise the cost</strong> (state-"
              "funded benefits, shared parental leave), not to weaken the right."},
             {"t": "hbox", "color": "amber", "html": "Design matters: who pays for a protection "
              "decides whether it protects women or prices them out."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Build the floor, then enforce it",
         "blocks": [
             {"t": "body", "html": "An enabling environment &mdash; equal pay, maternity, PoSH, "
              "work guarantees, social protection &mdash; turns individual gains into durable "
              "rights. The frontier is coverage of the informal majority and real enforcement."},
             {"t": "hbox", "color": "cyan", "html": "Ask of any WEE programme: does it help women "
              "claim existing rights, and does it push to extend them to the uncovered?"},
         ]},

        # ===================== SECTION 11 — MEASURING WEE & WHAT WORKS =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Measuring WEE &amp; What Works"},

        {"type": "content", "label": "The Challenge", "title": "How do you measure empowerment?",
         "blocks": [
             {"t": "body", "html": "Empowerment is a process inside people's lives &mdash; agency, "
              "power, choice. Measuring it means choosing observable indicators that stand in for "
              "something inherently hard to see, without flattening it into 'has a job'."},
             {"t": "hbox", "color": "amber", "html": "Bad measurement drives bad programmes: count "
              "only loans or jobs and you will fund loans and jobs, even where agency does not "
              "follow."},
         ]},

        {"type": "content", "label": "What to Measure", "title": "Indicators across the dimensions",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Dimension", "Example indicators"],
              "rows": [
                  ["Resources", "Owns land/house; has an account she controls; earns income"],
                  ["Agency", "Decides on own health, large purchases, use of her earnings; mobility"],
                  ["Achievements", "Nutrition, schooling of children, freedom from violence"],
                  ["Control", "Whether she &mdash; not others &mdash; decides how her income is used"]]},
             {"t": "hbox", "color": "cyan", "html": "Triangulate: combine 'hard' economic measures "
              "with agency and control questions, and with qualitative voice. No single number "
              "captures WEE."},
         ]},

        {"type": "content", "label": "An Index", "title": "WEAI: the Women's Empowerment in Agriculture Index",
         "blocks": [
             {"t": "term", "word": "WEAI",
              "def": "The Women's Empowerment in Agriculture Index &mdash; developed by IFPRI, "
              "USAID and OPHI &mdash; measures women's empowerment across domains such as "
              "production decisions, resources, income, leadership and time use, and compares it "
              "with men in the same household."},
             {"t": "body", "html": "WEAI was a milestone: a survey-based, multidimensional measure "
              "that takes agency seriously and benchmarks women against men in their own "
              "households &mdash; widely used and adapted (e.g. pro-WEAI)."},
         ]},

        {"type": "content", "label": "What Works", "title": "Cash, assets, or bundles?",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Approach", "What it does", "Evidence signal"],
              "rows": [
                  ["Cash transfers", "Give money, often to women", "Helps consumption; agency gains vary"],
                  ["Assets", "Transfer productive assets in her name", "Stronger, more durable power shifts"],
                  ["Credit alone", "Microloans", "Mixed; can over-indebt without support"],
                  ["'Graduation' bundles", "Asset + cash + coaching + savings", "Among the most robust gains"]]},
             {"t": "hbox", "color": "green", "html": "The 'graduation' approach &mdash; pioneered "
              "by BRAC and tested across countries &mdash; bundles an asset, a stipend, training "
              "and savings, with some of the strongest evidence for lasting impact."},
         ]},

        {"type": "content", "label": "Bundles Win", "title": "Why bundled programmes outperform",
         "blocks": [
             {"t": "chart", "canvas": "whatWorksChart",
              "title": "Illustrative relative impact on women's agency, by approach",
              "source": "Illustrative &mdash; schematic of the direction of evidence, not exact effects",
              "type": "bar",
              "data": {"labels": ["Credit only", "Cash only", "Asset transfer", "Graduation bundle"],
                       "datasets": [{"label": "Relative agency gain (illustrative)",
                                     "data": [25, 40, 60, 85],
                                     "backgroundColor": ["#94A3B8", "#0EA5E9", "#6366F1", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'Relative gain (illustrative)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Heights are <strong>illustrative</strong>. "
              "The robust message: addressing several constraints at once beats any single lever."},
         ]},

        {"type": "content", "label": "Intersectionality", "title": "Not all women face the same walls",
         "blocks": [
             {"t": "body", "html": "'Women' is not one group. Caste, class, religion, disability, "
              "age, marital status and location shape opportunity together. A Dalit or Adivasi "
              "woman, a single woman, a disabled woman faces compounded constraints."},
             {"t": "hbox", "color": "red", "html": "Always disaggregate. A programme that raises "
              "the average can still bypass the most marginalised &mdash; or even widen gaps "
              "between women."},
         ]},

        {"type": "content", "label": "Principles", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Rights first</strong> &mdash; the case for WEE is justice, not just returns",
                 "<strong>Resources + agency + achievements</strong> &mdash; income alone is not empowerment",
                 "<strong>Fix care</strong> &mdash; no WEE without rebalancing unpaid work",
                 "<strong>Control, not just access</strong> &mdash; whose name, whose decision?",
                 "<strong>Bundle &amp; disaggregate</strong> &mdash; address many constraints, for all women"]},
         ]},

        {"type": "content", "label": "Reading List", "title": "Where to go next",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Naila Kabeer &mdash; <em>Resources, Agency, Achievements</em> (on measuring empowerment)",
                 "Bina Agarwal &mdash; <em>A Field of One's Own</em> (land &amp; gender)",
                 "Diane Elson &mdash; on recognising, reducing, redistributing care",
                 "IFPRI / USAID &mdash; the WEAI and pro-WEAI resources",
                 "NSO &mdash; India Time Use Survey 2019; PLFS reports (labour data)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Care Economy 101</strong>, <strong>Gender &amp; Development</strong> and "
              "<strong>Data Literacy 101</strong> courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Women's Economic Empowerment 101 &middot; Complete",
         "headline": "Empowerment is<br>resources, agency,<br>and achievements.",
         "byline": "Not just a job and an income, but the power to make and act on economic "
                   "decisions &mdash; on terms she values. Lead with rights, rebalance care, and "
                   "measure control, not just access. Explore the rest of the ImpactMojo 101 "
                   "Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
