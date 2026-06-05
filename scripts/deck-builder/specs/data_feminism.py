# -*- coding: utf-8 -*-
"""
Data Feminism 101 — ImpactMojo 101 Series (native deck spec)
Power, data and justice — D'Ignazio & Klein's seven principles for South Asia.
Build: python3 scripts/deck-builder/build.py data_feminism
"""

DECK = {
    "slug": "data-feminism",
    "title": "Data Feminism 101",
    "description": ("Data Feminism 101 — a free foundational course for development "
                    "practitioners and researchers in South Asia. Power and data, "
                    "intersectionality and the seven principles of Catherine D'Ignazio "
                    "and Lauren Klein, with India-centric examples on gender data gaps, "
                    "the matrix of domination and counting for justice. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Data<br>Feminism<br>101",
         "sub": "Power, Justice &amp; the Seven Principles of D'Ignazio &amp; Klein "
                "&mdash; a Foundational Course for Development Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Data Feminism Is"},
             {"name": "Examine Power"},
             {"name": "Challenge Power"},
             {"name": "Rethink Binaries &amp; Hierarchies"},
             {"name": "Elevate Emotion &amp; Embodiment"},
             {"name": "Consider Context"},
             {"name": "Make Labour Visible"},
             {"name": "Embrace Pluralism"},
             {"name": "The Matrix of Domination"},
             {"name": "Gender Data Gaps in South Asia"},
             {"name": "Practice &amp; Tools"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Data Feminism Is"},

        {"type": "content", "label": "The Book", "title": "Data Feminism, D'Ignazio &amp; Klein (2020)",
         "blocks": [
             {"t": "body", "html": "<strong>Data Feminism</strong>, by Catherine D'Ignazio and "
              "Lauren F. Klein (MIT Press, 2020), is a way of thinking about data &mdash; its "
              "collection, analysis and communication &mdash; informed by intersectional feminist "
              "thought. It is not only about gender; it is about <strong>power</strong>."},
             {"t": "hbox", "color": "cyan", "html": "Its core question is not 'what does the data "
              "say?' but 'who made this data, about whom, for whom, and who benefits?'"},
         ]},

        {"type": "content", "label": "Core Claim", "title": "Data is never neutral",
         "blocks": [
             {"t": "body", "html": "Numbers feel objective. But every dataset embeds human "
              "choices &mdash; what to measure, which categories to use, whom to ask, what to "
              "ignore. Those choices carry the values and the power of the people who made them."},
             {"t": "quote",
              "text": "Data are not neutral or objective. They are the products of unequal social "
              "relations, and this context is essential for analysis.",
              "attr": "&mdash; Catherine D'Ignazio &amp; Lauren Klein, Data Feminism"},
         ]},

        {"type": "content", "label": "Definition", "title": "Data feminism, defined",
         "blocks": [
             {"t": "term", "word": "Data feminism",
              "def": "A way of thinking about data and its power that is informed by the "
              "tradition of intersectional feminism. It begins from the conviction that power "
              "is not distributed equally in the world &mdash; and that data both reflects and "
              "can reshape that distribution."},
             {"t": "hbox", "color": "amber", "html": "Feminism here is a lens on power and "
              "justice, applied to data &mdash; useful far beyond questions of gender alone."},
         ]},

        {"type": "content", "label": "Intersectionality", "title": "Why 'intersectional' feminism",
         "blocks": [
             {"t": "body", "html": "Legal scholar <strong>Kimberl&eacute; Crenshaw</strong> coined "
              "<strong>intersectionality</strong> in 1989 to show that a Black woman's experience "
              "is not simply 'racism plus sexism' &mdash; the forms of oppression intersect to "
              "create something distinct that neither alone captures."},
             {"t": "hbox", "color": "indigo", "html": "In South Asia, a Dalit woman's exclusion is "
              "not caste discrimination and gender discrimination added separately &mdash; it is a "
              "specific, compounded reality. Data that measures only one axis at a time misses her."},
         ]},

        {"type": "content", "label": "Power &amp; Data", "title": "Data reflects who holds power",
         "blocks": [
             {"t": "body", "html": "Those with power decide what counts as worth counting. "
              "Historically, that has meant data <em>about</em> the powerful is rich and data "
              "about the marginalised is thin, distorted, or absent altogether."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Who", "label": "Who collects the data &mdash; the institutions and "
                  "their interests", "color": "cyan"},
                 {"num": "Whom", "label": "Whom it is about &mdash; and whom it leaves out", "color": "indigo"},
                 {"num": "Why", "label": "For whose benefit it is collected and used", "color": "amber"}]},
         ]},

        {"type": "content", "label": "The Seven Principles", "title": "Seven principles of data feminism",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["#", "Principle", "In short"],
              "rows": [
                  ["1", "Examine power", "Name how power operates in data"],
                  ["2", "Challenge power", "Use data to contest inequity"],
                  ["3", "Elevate emotion &amp; embodiment", "Value feeling and lived bodies"],
                  ["4", "Rethink binaries &amp; hierarchies", "Question how we classify and count"],
                  ["5", "Embrace pluralism", "Centre many voices and forms of knowledge"],
                  ["6", "Consider context", "Refuse decontextualised data"],
                  ["7", "Make labour visible", "Credit the work behind data"]]},
             {"t": "hbox", "color": "green", "html": "This course works through all seven, framed "
              "for the data you meet in South Asian development practice."},
         ]},

        {"type": "content", "label": "Not Anti-Data", "title": "A feminist critique is pro-data",
         "blocks": [
             {"t": "body", "html": "Data feminism does not reject data &mdash; it demands "
              "<em>better</em> data: more representative, more accountable, more honest about its "
              "limits. The goal is data that serves justice, not data abandoned."},
             {"t": "hbox", "color": "cyan", "html": "Counting can be an act of care. The "
              "feminist move is to count well, count fairly, and count the people power forgets."},
         ]},

        {"type": "content", "label": "Lineage", "title": "Standing on feminist thought",
         "blocks": [
             {"t": "body", "html": "Data feminism is not new theory invented for the data age "
              "&mdash; it applies a long tradition. Its foundations sit in <strong>standpoint "
              "theory</strong>, Black feminist thought, and intersectional scholarship that "
              "asked, long before 'big data', whose knowledge counts."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Standpoint theory:</strong> knowledge is situated, never view-from-nowhere",
                 "<strong>Black feminism:</strong> Collins, hooks, the Combahee River Collective",
                 "<strong>Intersectionality:</strong> Crenshaw's account of compounded oppression"]},
         ]},

        {"type": "content", "label": "Why It Matters Here", "title": "Why South Asia needs this lens",
         "blocks": [
             {"t": "body", "html": "South Asia runs some of the world's largest data systems "
              "&mdash; the Census, NFHS, Aadhaar, welfare rolls &mdash; touching over a billion "
              "lives. The bigger the system, the higher the stakes of who it counts well and "
              "who it counts badly."},
             {"t": "hbox", "color": "indigo", "html": "When data decides rations, pensions and "
              "scheme eligibility for hundreds of millions, a flaw in the count is not academic "
              "&mdash; it is hunger, exclusion, and denied entitlement."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Examine Power"},

        {"type": "content", "label": "Principle One", "title": "Examine power: name how it works",
         "blocks": [
             {"t": "body", "html": "The first principle is to <strong>examine power</strong> "
              "&mdash; to analyse how power operates in the world, and how it shapes the data "
              "we have. You cannot challenge what you have not first named."},
             {"t": "term", "word": "Power (in data)",
              "def": "The current configuration of structural privilege and oppression that "
              "decides who collects data, about whom, for what purpose, and who gets to decide "
              "what the numbers mean."},
         ]},

        {"type": "content", "label": "The Data Setting", "title": "Read the whole 'data setting'",
         "blocks": [
             {"t": "body", "html": "D'Ignazio and Klein urge us to study not just the dataset but "
              "the <strong>data setting</strong>: the people, institutions, incentives and "
              "histories that produced it. A number is the visible tip of a social process."},
             {"t": "flow", "steps": [
                 "WHO funded and commissioned it",
                 "WHO designed the categories",
                 "WHO collected it, under what pressures",
                 "WHO is counted &mdash; and who is absent"]},
         ]},

        {"type": "content", "label": "Three Questions", "title": "Who, about whom, for whom",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Ask of any dataset", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Who collected this, and why?",
                      "Whose categories shaped it?",
                      "Who is the intended user?",
                      "Who is missing from it?"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Then ask", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Who benefits from this framing?",
                      "Who could be harmed by it?",
                      "Whose voice is absent from the design?",
                      "What would the counted say if asked?"]}]}]},
         ]},

        {"type": "content", "label": "The Privilege Hazard", "title": "The privilege hazard",
         "blocks": [
             {"t": "term", "word": "Privilege hazard",
              "def": "D'Ignazio and Klein's term for the danger that arises when the people who "
              "design data systems are drawn from a narrow, privileged group &mdash; they cannot "
              "see the problems and exclusions their position renders invisible to them."},
             {"t": "hbox", "color": "red", "html": "If everyone designing a survey is urban, "
              "upper-caste and male, the gaps that hurt rural Dalit women may simply never "
              "occur to them. Whose blind spots are baked into your data?"},
         ]},

        {"type": "content", "label": "Who Builds Data", "title": "Who is in the room matters",
         "blocks": [
             {"t": "chart", "canvas": "dfWomenDataChart",
              "title": "Women's share of the data &amp; tech workforce (illustrative pattern)",
              "source": "Illustrative, patterned on NASSCOM &amp; industry estimates",
              "type": "bar",
              "data": {"labels": ["Entry-level tech", "Data &amp; analytics roles",
                                   "Senior data roles", "Data leadership"],
                       "datasets": [{"label": "Women (%)",
                                     "data": [35, 26, 18, 11],
                                     "backgroundColor": ["#0EA5E9", "#6366F1", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:50, title:{display:true,text:'% women'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative pattern. The shape is the "
              "point: women thin out as you climb toward the people who decide what data systems "
              "measure. The privilege hazard is structural, not personal."},
         ]},

        {"type": "content", "label": "Default Settings", "title": "Power hides in the defaults",
         "blocks": [
             {"t": "body", "html": "Power is most effective when it is invisible &mdash; encoded "
              "in a 'standard' form, a 'normal' category, a 'default' user. Examining power means "
              "making those defaults visible and asking who they were built around."},
             {"t": "hbox", "color": "cyan", "html": "A form with only 'Male / Female', a survey "
              "in only the dominant language, a 'head of household' assumed to be a man &mdash; "
              "each default is a quiet exercise of power."},
         ]},

        {"type": "content", "label": "Head of Household", "title": "A worked example: 'head of household'",
         "blocks": [
             {"t": "body", "html": "Surveys often record the 'head of household' &mdash; "
              "frequently assumed, and recorded, as the oldest man. His characteristics then "
              "stand in for the whole family, and the women's circumstances are read through him."},
             {"t": "hbox", "color": "red", "html": "A 'male-headed household' classified as "
              "non-poor may still contain a daughter-in-law with no income, no assets and no "
              "say. The category renders her invisible inside her own home."},
         ]},

        {"type": "content", "label": "Power Is Relational", "title": "Power is not held; it is exercised",
         "blocks": [
             {"t": "body", "html": "Examining power is not about finding a villain. Power works "
              "through routine, well-meaning processes &mdash; a standard form, a default field, "
              "a 'best-practice' indicator &mdash; that quietly advantage some and disadvantage "
              "others."},
             {"t": "hbox", "color": "cyan", "html": "The data-feminist habit is to make the "
              "ordinary strange: to ask of every taken-for-granted choice, 'who does this serve, "
              "and who does it cost?'"},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Challenge Power"},

        {"type": "content", "label": "Principle Two", "title": "Challenge power: data for justice",
         "blocks": [
             {"t": "body", "html": "Examining power is diagnosis; <strong>challenging power</strong> "
              "is action. The second principle commits data work to contesting unequal power and "
              "working toward justice &mdash; not merely describing the world, but changing it."},
             {"t": "quote", "text": "Data feminism is about using data to make change in the "
              "world, while being mindful of how power and privilege shape its production.",
              "attr": "&mdash; D'Ignazio &amp; Klein, Data Feminism"},
         ]},

        {"type": "content", "label": "Counterdata", "title": "Counterdata: count what power ignores",
         "blocks": [
             {"t": "term", "word": "Counterdata",
              "def": "Data produced by communities or activists to document a harm that official "
              "systems fail to record &mdash; making the invisible countable, and so contestable."},
             {"t": "body", "html": "When institutions will not count a problem, people build the "
              "count themselves &mdash; mapping sexual harassment, logging manual-scavenging "
              "deaths, recording missing toilets &mdash; to force the issue onto the agenda."},
         ]},

        {"type": "content", "label": "Counterdata in Action", "title": "Citizen counts that moved policy",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Examples", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Community mapping of unsafe public spaces for women",
                      "Activist registers of sanitation-worker deaths",
                      "Crowd-sourced maps of harassment hotspots",
                      "People's audits of MGNREGA wage payments"]}]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Why it works", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Counterdata turns lived experience into "
                   "evidence the system must answer. A number is harder to dismiss than a "
                   "single story &mdash; and a map of many is harder still."}]}]},
         ]},

        {"type": "content", "label": "Auditing Bias", "title": "Audit systems for bias",
         "blocks": [
             {"t": "body", "html": "Challenging power includes <strong>auditing</strong> the "
              "algorithms and datasets that increasingly decide who gets a benefit, a loan, a "
              "ration card or a welfare flag. Biased data produces biased decisions at scale."},
             {"t": "hbox", "color": "red", "html": "A targeting algorithm trained on data that "
              "under-counts women or excludes the undocumented will systematically deny them "
              "&mdash; and do so with an appearance of objectivity."},
         ]},

        {"type": "content", "label": "Reported vs Real", "title": "Challenge the official count itself",
         "blocks": [
             {"t": "chart", "canvas": "dfGbvChart",
              "title": "Gender-based violence: reported vs estimated actual (illustrative)",
              "source": "Illustrative, pattern reflects survey-vs-FIR underreporting gap",
              "type": "bar",
              "data": {"labels": ["Officially reported", "Estimated actual"],
                       "datasets": [{"label": "Relative scale",
                                     "data": [100, 360],
                                     "backgroundColor": ["#6366F1", "#EF4444"]}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{min:0, title:{display:true,text:'Relative scale (reported = 100)'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative scale. Most gender-based "
              "violence never reaches a police record. Reading only reported cases mistakes the "
              "visible fraction for the whole &mdash; and treats silence as safety."},
         ]},

        {"type": "content", "label": "From Number to Change", "title": "Data is a means, not an end",
         "blocks": [
             {"t": "flow", "steps": [
                 "DOCUMENT the harm with data",
                 "AMPLIFY through the affected community",
                 "DEMAND accountability from power",
                 "CHANGE the policy or system"]},
             {"t": "hbox", "color": "green", "html": "The point of the count is the change. "
              "Data that stays in a report changes nothing; data placed in the hands of those it "
              "concerns can shift power."},
         ]},

        {"type": "content", "label": "Social Audits", "title": "Social audits: challenging power with its own data",
         "blocks": [
             {"t": "body", "html": "India's <strong>MGNREGA social audits</strong> turn the "
              "scheme's own administrative records back on it: villagers read out muster rolls "
              "and payments in a public hearing, and those present testify whether the work and "
              "wages were real."},
             {"t": "hbox", "color": "cyan", "html": "It is data feminism in action &mdash; the "
              "people in the data interpret the data, in public, to hold power to account. The "
              "official record meets the community's knowledge."},
         ]},

        {"type": "content", "label": "Reframe the Deficit", "title": "Challenge the framing, not just the figure",
         "blocks": [
             {"t": "body", "html": "Power lives in framing. 'Women's low workforce participation' "
              "frames women as the problem; 'an economy that does not count or reward women's "
              "work' frames the system as the problem. Same data, opposite politics."},
             {"t": "hbox", "color": "amber", "html": "Challenging power often means refusing the "
              "deficit framing &mdash; asking what the data reveals about structures, not just "
              "about the marginalised who appear in its margins."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Rethink Binaries &amp; Hierarchies"},

        {"type": "content", "label": "Principle Four", "title": "Rethink binaries &amp; hierarchies",
         "blocks": [
             {"t": "body", "html": "The fourth principle asks us to <strong>question the "
              "categories</strong> we count with. Binaries (male/female, formal/informal, "
              "literate/illiterate) and hierarchies are not facts of nature &mdash; they are "
              "choices that include some realities and erase others."},
             {"t": "hbox", "color": "cyan", "html": "Every classification is a decision about "
              "what counts as the same and what counts as different. Those decisions have "
              "winners and losers."},
         ]},

        {"type": "content", "label": "Counting Includes &amp; Excludes", "title": "To count is to decide who exists",
         "blocks": [
             {"t": "body", "html": "When a form offers only two gender boxes, anyone outside them "
              "is forced to misreport or vanish. The category does not just record reality &mdash; "
              "it constructs the official version of it."},
             {"t": "quote", "text": "What gets counted counts. To make something legible to the "
              "state, you must first fit it into the state's categories.",
              "attr": "&mdash; a recurring theme in critical data studies"},
         ]},

        {"type": "content", "label": "Gender Beyond Binary", "title": "Gender is not two boxes",
         "blocks": [
             {"t": "body", "html": "India legally recognises a <strong>third gender</strong> "
              "(Supreme Court, NALSA judgment, 2014), and the Census has counted "
              "'<strong>Others</strong>' since 2011. Yet many forms, schemes and datasets still "
              "offer only male/female &mdash; rendering trans and non-binary people invisible."},
             {"t": "hbox", "color": "indigo", "html": "When data has no box for you, policy has "
              "no plan for you. Recognition in the category is the first step to recognition in "
              "the budget."},
         ]},

        {"type": "content", "label": "The Missing Women", "title": "Amartya Sen's 'missing women'",
         "blocks": [
             {"t": "body", "html": "In 1990, economist <strong>Amartya Sen</strong> asked a "
              "feminist data question: given normal sex ratios at birth and survival, how many "
              "women <em>should</em> be alive in Asia &mdash; and how many are not? His answer: "
              "<strong>over 100 million 'missing women'</strong>, lost to neglect, discrimination "
              "and sex-selective practices."},
             {"t": "hbox", "color": "red", "html": "It is a count of an <em>absence</em> &mdash; "
              "made visible only by asking who should be in the data and is not. That is exactly "
              "the data-feminist move."},
         ]},

        {"type": "content", "label": "The Sex Ratio", "title": "An imbalance you can see in the data",
         "blocks": [
             {"t": "chart", "canvas": "dfSexRatioChart",
              "title": "Child sex ratio, India (girls per 1,000 boys, age 0&ndash;6)",
              "source": "Census of India, child sex ratio (age 0&ndash;6)",
              "type": "line",
              "data": {"labels": ["1991", "2001", "2011"],
                       "datasets": [{"label": "Girls per 1,000 boys (0&ndash;6)",
                                     "data": [945, 927, 919],
                                     "borderColor": "#EF4444",
                                     "backgroundColor": "rgba(239,68,68,0.08)",
                                     "fill": True, "tension": 0.3, "pointRadius": 5}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:900,max:960, title:{display:true,text:'girls per 1,000 boys'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "A biologically normal ratio is roughly "
              "952 girls per 1,000 boys. The deficit is Sen's 'missing women' as they appear in "
              "the youngest cohort &mdash; a hierarchy of value, written in the count."},
         ]},

        {"type": "content", "label": "False Binaries", "title": "Beyond gender: other false binaries",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Formal / informal work</strong> &mdash; most South Asian labour is a "
                 "blurred middle, badly served by either box",
                 "<strong>Urban / rural</strong> &mdash; peri-urban and circular migrants fall "
                 "between, counted twice or not at all",
                 "<strong>Employed / unemployed</strong> &mdash; erases the vast unpaid and "
                 "underemployed",
                 "<strong>Literate / illiterate</strong> &mdash; a single threshold flattens a "
                 "spectrum of skill"]},
         ]},

        {"type": "content", "label": "Hierarchies of Value", "title": "Categories rank as well as sort",
         "blocks": [
             {"t": "body", "html": "Classifications often smuggle in a hierarchy: 'head of "
              "household' above other members, 'skilled' above 'unskilled', 'productive' work "
              "above 'reproductive' work. The ranking shapes whose contribution shows up &mdash; "
              "and whose disappears."},
             {"t": "hbox", "color": "cyan", "html": "Rethinking binaries does not mean abandoning "
              "categories &mdash; it means choosing them consciously, naming what they exclude, "
              "and revising them when reality outgrows them."},
         ]},

        {"type": "content", "label": "Who Counts the Missing", "title": "Counting an absence",
         "blocks": [
             {"t": "body", "html": "Sen's insight is methodological as well as moral: some of the "
              "most important data is about people who are <em>not there</em>. The missing women, "
              "the out-of-school girl, the unregistered birth &mdash; absences that only a "
              "deliberate question can reveal."},
             {"t": "flow", "steps": [
                 "Model who SHOULD be present",
                 "Count who IS present",
                 "The gap is the finding",
                 "Ask why they are missing"]},
         ]},

        {"type": "content", "label": "Categories Evolve", "title": "Good categories change over time",
         "blocks": [
             {"t": "body", "html": "Categories are not eternal. India's recognition of a third "
              "gender, the slow inclusion of disability in the Census, the debate over a caste "
              "census &mdash; each shows classification responding to demands for visibility."},
             {"t": "hbox", "color": "indigo", "html": "If a category no longer fits the people it "
              "is meant to describe, the data-feminist response is to revise the category, not to "
              "force the people to fit."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Elevate Emotion &amp; Embodiment"},

        {"type": "content", "label": "Principle Three", "title": "Elevate emotion &amp; embodiment",
         "blocks": [
             {"t": "body", "html": "The third principle challenges the idea that good data work "
              "must be cold and detached. <strong>Emotion and embodiment</strong> &mdash; "
              "feeling, lived experience, the body &mdash; are valid sources of knowledge, not "
              "contaminants to be scrubbed out."},
             {"t": "hbox", "color": "indigo", "html": "The myth of the dispassionate analyst is "
              "itself a position of power &mdash; usually available only to those the data does "
              "not hurt."},
         ]},

        {"type": "content", "label": "Data Are People", "title": "Behind every row is a person",
         "blocks": [
             {"t": "body", "html": "In development data, a row is rarely an abstraction &mdash; "
              "it is a woman who walked three kilometres for water, a child weighed at an "
              "anganwadi, a worker whose wages went unpaid. The data-feminist asks us never to "
              "forget the body behind the number."},
             {"t": "quote", "text": "Data are people, and to ignore that is to risk doing harm.",
              "attr": "&mdash; a principle of feminist data practice"},
         ]},

        {"type": "content", "label": "Visceralisation", "title": "From visualisation to visceralisation",
         "blocks": [
             {"t": "term", "word": "Data visceralisation",
              "def": "D'Ignazio and Klein's term for representations of data that are experienced "
              "through the body and the emotions &mdash; not only seen, but felt. A way of "
              "communicating that moves people to understand and to act."},
             {"t": "body", "html": "A bar chart of maternal deaths informs. A memorial that gives "
              "each death a name, a place, a face &mdash; that <em>moves</em>. Both are data; only "
              "one reaches the heart."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "Emotion is not the enemy of rigour",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The old view", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Strip out feeling. Numbers should be "
                   "'objective', emotion-free, neutral. Charts as austere as possible."}]}],
              "right": [{"t": "panel", "color": "green", "title": "The feminist view", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Acknowledge that all data carries values. "
                   "Use emotion responsibly to communicate truth and prompt just action &mdash; "
                   "without manipulating."}]}]},
             {"t": "hbox", "color": "amber", "html": "The goal is not to inflame, but to restore "
              "the human stakes that decontextualised numbers strip away."},
         ]},

        {"type": "content", "label": "Caution", "title": "Use emotion ethically",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Do not exploit suffering for shock value or 'poverty porn'",
                 "Do not strip dignity from the people in the data",
                 "Centre the perspective of the affected, not the donor",
                 "Let communities choose how their story is told"]},
             {"t": "hbox", "color": "cyan", "html": "Elevating emotion is about restoring humanity "
              "to data &mdash; with the consent and dignity of the people it represents."},
         ]},

        {"type": "content", "label": "Embodiment", "title": "Knowledge lives in bodies too",
         "blocks": [
             {"t": "body", "html": "Embodiment means recognising that knowledge is held in "
              "bodies and lived experience, not only in spreadsheets. A community health worker "
              "'knows' which hamlet is hungry before any indicator confirms it &mdash; that "
              "embodied knowledge is real data."},
             {"t": "hbox", "color": "indigo", "html": "Discounting embodied knowledge as 'merely "
              "anecdotal' is itself a power move &mdash; it privileges the abstraction of those "
              "far from the problem over the certainty of those living it."},
         ]},

        {"type": "content", "label": "Design Choices", "title": "Communicate so people feel the stakes",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Use names, places and faces &mdash; with consent &mdash; not just totals",
                 "Choose units a reader can feel ('one classroom of children' vs '40')",
                 "Show the human scale behind the aggregate",
                 "Pair the chart with the testimony of someone inside it"]},
             {"t": "hbox", "color": "cyan", "html": "The aim is honest resonance: help people "
              "grasp what the number means for a life, without distorting what the number says."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Consider Context"},

        {"type": "content", "label": "Principle Six", "title": "Consider context: numbers don't speak",
         "blocks": [
             {"t": "body", "html": "The sixth principle insists that <strong>numbers do not "
              "speak for themselves</strong>. A figure ripped from its context can mislead "
              "more than it informs. Context is not optional background &mdash; it is part of "
              "the data's meaning."},
             {"t": "quote", "text": "Refusing to take data at face value, and putting it back "
              "into context, is a core act of data feminism.",
              "attr": "&mdash; D'Ignazio &amp; Klein, Data Feminism"},
         ]},

        {"type": "content", "label": "Raw vs Cooked", "title": "There is no such thing as raw data",
         "blocks": [
             {"t": "body", "html": "D'Ignazio and Klein echo Lisa Gitelman: '<strong>raw data is "
              "an oxymoron</strong>.' Data is always already 'cooked' &mdash; cleaned, classified, "
              "shaped by choices &mdash; before anyone analyses it. Pretending it is raw hides "
              "those choices."},
             {"t": "flow", "steps": [
                 "A measurement is chosen, not found",
                 "A category is imposed",
                 "Values are cleaned and recoded",
                 "So 'raw' data is already cooked"]},
         ]},

        {"type": "content", "label": "Context Changes Meaning", "title": "The same number, two truths",
         "blocks": [
             {"t": "body", "html": "A district reporting '90% institutional deliveries' looks like "
              "success &mdash; until you learn the facilities lack blood banks, the 10% missing "
              "are the remotest women, and the count includes a referral that ended in death "
              "elsewhere. Context flips the story."},
             {"t": "hbox", "color": "red", "html": "Decontextualised data is a favourite tool of "
              "those who would rather you not look closer. Always ask: out of what whole, under "
              "what conditions, with what missing?"},
         ]},

        {"type": "content", "label": "Refuse Decontextualisation", "title": "Some comparisons should be refused",
         "blocks": [
             {"t": "body", "html": "Sometimes the ethical act is to <strong>refuse</strong> a "
              "comparison the data invites. Ranking communities by 'crime rate' without noting "
              "differential reporting and policing can stigmatise the over-policed and exonerate "
              "the powerful."},
             {"t": "hbox", "color": "amber", "html": "Refusing decontextualised data is not "
              "censorship &mdash; it is responsibility. Provide the context, or do not publish "
              "the number."},
         ]},

        {"type": "content", "label": "Practice", "title": "Contextualise before you conclude",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "State who is in the denominator &mdash; and who is excluded",
                 "Note how the data was collected and by whom",
                 "Flag reporting and measurement gaps that shape the number",
                 "Give the historical and social conditions behind the figure"]},
         ]},

        {"type": "content", "label": "Provenance", "title": "Context includes where data comes from",
         "blocks": [
             {"t": "body", "html": "Part of considering context is tracing <strong>provenance</strong>: "
              "a crime statistic reflects policing as much as crime; a complaint count reflects "
              "access to grievance systems as much as grievances. The data measures the system, "
              "not only the phenomenon."},
             {"t": "hbox", "color": "amber", "html": "Higher reported numbers can mean a worse "
              "problem &mdash; or a better reporting system. Without provenance, you cannot tell "
              "which, and you will often guess wrong."},
         ]},

        {"type": "content", "label": "Aggregation Hides", "title": "Aggregation strips context by design",
         "blocks": [
             {"t": "body", "html": "Every aggregation is a loss of context. A national average "
              "dissolves the district; a district average dissolves the village; a household "
              "figure dissolves the woman inside it. Each step up the ladder erases someone."},
             {"t": "hbox", "color": "red", "html": "When a headline number looks reassuring, ask "
              "what context the aggregation discarded to produce it. The reassurance may live "
              "entirely in the averaging."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Make Labour Visible"},

        {"type": "content", "label": "Principle Seven", "title": "Make labour visible",
         "blocks": [
             {"t": "body", "html": "The seventh principle credits the <strong>work behind the "
              "data</strong>. Every dataset rests on labour &mdash; the surveyor in the field, "
              "the data-entry clerk, the cleaner, the respondent who gave an hour of their day "
              "&mdash; and most of it goes uncredited and unseen."},
             {"t": "hbox", "color": "cyan", "html": "Making labour visible is a matter of both "
              "justice and accuracy: invisible work is undervalued work, and undervalued work is "
              "where errors and exploitation hide."},
         ]},

        {"type": "content", "label": "The Hidden Pipeline", "title": "Who actually makes a dataset",
         "blocks": [
             {"t": "flow", "steps": [
                 "RESPONDENTS give their time and trust",
                 "FIELD STAFF walk, ask, record",
                 "CLERKS enter, clean, reconcile",
                 "ANALYSTS get the credit and the byline"]},
             {"t": "hbox", "color": "amber", "html": "The further down this chain, the more likely "
              "the worker is a woman, low-paid, and absent from the acknowledgements. Visibility "
              "is the first step to fair credit."},
         ]},

        {"type": "content", "label": "Care &amp; Data Work", "title": "Data work is often care work",
         "blocks": [
             {"t": "body", "html": "An ASHA worker filling registers, an anganwadi worker weighing "
              "children, a frontline enumerator building rapport &mdash; their data work is "
              "inseparable from <strong>care work</strong>, and like care work it is feminised, "
              "underpaid, and treated as 'natural' rather than skilled."},
             {"t": "hbox", "color": "indigo", "html": "India's million-plus ASHA workers generate "
              "vast health data as 'volunteers' on honoraria &mdash; the labour that powers the "
              "dashboards is itself rendered invisible."},
         ]},

        {"type": "content", "label": "Invisible Unpaid Work", "title": "The biggest invisible dataset: unpaid care",
         "blocks": [
             {"t": "body", "html": "Beyond the data pipeline lies the largest invisible labour of "
              "all: <strong>unpaid domestic and care work</strong>, done overwhelmingly by women, "
              "and historically excluded from GDP and from most statistics &mdash; until surveys "
              "deliberately chose to count it."},
             {"t": "hbox", "color": "green", "html": "India's Time Use Survey 2019 was a "
              "data-feminist act: it made visible the hours of unpaid work that the System of "
              "National Accounts had long ignored."},
         ]},

        {"type": "content", "label": "Credit &amp; Fair Work", "title": "From visibility to fairness",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Name and credit data collectors and entry staff in outputs",
                 "Pay fairly for data labour &mdash; 'volunteer' is not a wage",
                 "Acknowledge respondents' time as a real contribution",
                 "Count unpaid care work in the statistics that drive policy"]},
         ]},

        {"type": "content", "label": "Respondent Burden", "title": "The respondent's labour counts too",
         "blocks": [
             {"t": "body", "html": "An hour given to a survey is an hour not spent earning, "
              "cooking or resting &mdash; a real cost borne disproportionately by women, who are "
              "surveyed about the household yet rarely see anything return to them."},
             {"t": "hbox", "color": "amber", "html": "'Survey fatigue' in over-studied communities "
              "is not laziness &mdash; it is the rational response of people whose unpaid data "
              "labour has, time and again, bought them nothing."},
         ]},

        {"type": "content", "label": "Visible Infrastructure", "title": "Data infrastructure is built by hands",
         "blocks": [
             {"t": "body", "html": "Behind every clean dashboard is invisible infrastructure "
              "labour: the engineer who maintains the database, the moderator who reviews "
              "content, the annotator who labels training data &mdash; work that is often "
              "outsourced, precarious and unnamed."},
             {"t": "hbox", "color": "cyan", "html": "Making labour visible scales from the "
              "village enumerator to the global gig worker labelling data for AI. The chain of "
              "hidden hands is long &mdash; and gendered at every link."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Embrace Pluralism"},

        {"type": "content", "label": "Principle Five", "title": "Embrace pluralism &amp; many voices",
         "blocks": [
             {"t": "body", "html": "The fifth principle calls for <strong>many voices and forms "
              "of knowledge</strong>. The most complete picture comes not from a single expert "
              "viewpoint but from synthesising multiple perspectives &mdash; especially those of "
              "the people closest to the issue."},
             {"t": "quote", "text": "The people closest to the problem are closest to the "
              "solution &mdash; and often closest to the missing data.",
              "attr": "&mdash; a principle of participatory practice"},
         ]},

        {"type": "content", "label": "Whose Knowledge Counts", "title": "Expert is not the only valid voice",
         "blocks": [
             {"t": "body", "html": "Local and experiential knowledge &mdash; a midwife's, a "
              "fisherwoman's, a sanitation worker's &mdash; is data too. Privileging only "
              "credentialed expertise discards the knowledge of those who live the problem daily."},
             {"t": "hbox", "color": "indigo", "html": "Ask not only 'what does the survey say?' "
              "but 'what do the people in the survey know that the survey never asked?'"},
         ]},

        {"type": "content", "label": "Participatory Data", "title": "Data with, not just about",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Extractive", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Outsiders arrive, survey, leave. The "
                   "community is a source of raw material; the value flows outward."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Participatory", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The community helps define what is "
                   "measured, collects and interprets it, and keeps the findings to act on."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Participatory mapping, community scorecards "
              "and social audits put people in the room where the data is defined."},
         ]},

        {"type": "content", "label": "Many Forms", "title": "Honour many forms of knowing",
         "blocks": [
             {"t": "bullets", "items": [
                 "Quantitative <em>and</em> qualitative, treated as partners",
                 "Oral histories and testimony alongside survey rows",
                 "Indigenous and local classifications, not only official ones",
                 "Maps, stories and art as legitimate data forms"]},
         ]},

        {"type": "content", "label": "Caution", "title": "Pluralism without tokenism",
         "blocks": [
             {"t": "body", "html": "Inviting many voices is not the same as listening to them. "
              "Token consultation &mdash; gathering views you have already decided to ignore "
              "&mdash; can be worse than none, extracting time while changing nothing."},
             {"t": "hbox", "color": "amber", "html": "Real pluralism shares <em>power</em> over "
              "the data, not just access to the meeting. Who decides what the findings mean?"},
         ]},

        {"type": "content", "label": "Situated Knowledge", "title": "Every viewpoint is partial",
         "blocks": [
             {"t": "body", "html": "Feminist philosopher Donna Haraway argued that all knowledge "
              "is <strong>situated</strong> &mdash; seen from somewhere, by someone, with a "
              "particular stake. There is no 'view from nowhere'. Embracing pluralism means "
              "combining many situated views into a fuller picture."},
             {"t": "hbox", "color": "indigo", "html": "Objectivity is not achieved by pretending "
              "to have no standpoint &mdash; it is approached by naming standpoints and bringing "
              "many of them honestly together."},
         ]},

        {"type": "content", "label": "Co-Design", "title": "Co-designing what gets measured",
         "blocks": [
             {"t": "body", "html": "The deepest form of pluralism is letting communities help "
              "decide the <em>questions</em>, not just answer them. When women define what "
              "'safety' or 'wellbeing' means in their own terms, the resulting indicators "
              "measure something that matters to them."},
             {"t": "hbox", "color": "green", "html": "Indicators co-designed with the people they "
              "describe are more valid, more legitimate, and more likely to drive action the "
              "community actually wants."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "The Matrix of Domination"},

        {"type": "content", "label": "The Frame", "title": "How power is organised: the matrix",
         "blocks": [
             {"t": "term", "word": "Matrix of domination",
              "def": "Sociologist Patricia Hill Collins' framework for how systems of power "
              "&mdash; race, class, gender and more &mdash; interlock and operate across four "
              "domains: structural, disciplinary, hegemonic and interpersonal."},
             {"t": "body", "html": "D'Ignazio and Klein use it as the analytic backbone of data "
              "feminism: a way to see how oppression is organised, and where data work can "
              "intervene."},
         ]},

        {"type": "content", "label": "Four Domains", "title": "Where power operates",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Domain", "How it works", "Data example"],
              "rows": [
                  ["Structural", "Laws &amp; institutions that organise oppression",
                   "Who the census is designed to count"],
                  ["Disciplinary", "Bureaucratic rules that enforce it unevenly",
                   "Whose claims get verified vs waved through"],
                  ["Hegemonic", "Culture &amp; ideas that make it seem natural",
                   "'Head of household' assumed to be male"],
                  ["Interpersonal", "Everyday lived experience of it",
                   "An enumerator skipping the women's answers"]]},
             {"t": "hbox", "color": "cyan", "html": "Data injustice lives in all four domains "
              "&mdash; and so can data justice."},
         ]},

        {"type": "content", "label": "Intersectionality", "title": "Crenshaw: oppression intersects",
         "blocks": [
             {"t": "body", "html": "<strong>Kimberl&eacute; Crenshaw (1989)</strong> showed that "
              "Black women fell through the gaps of laws that treated race and sex as separate "
              "&mdash; they were neither the typical 'woman' (white) nor the typical 'Black "
              "person' (male) the categories imagined."},
             {"t": "hbox", "color": "indigo", "html": "Data that disaggregates by gender OR caste "
              "but never <em>both at once</em> reproduces exactly this erasure. Intersectional "
              "questions need intersectional tables."},
         ]},

        {"type": "content", "label": "Caste &amp; Gender", "title": "Caste-gender in India",
         "blocks": [
             {"t": "body", "html": "In South Asia the most important intersection is often "
              "<strong>caste and gender</strong>. A Dalit woman faces a compounded exclusion that "
              "neither 'women's' data nor 'Dalit' data, read separately, can reveal."},
             {"t": "chart", "canvas": "dfCasteGenderChart",
              "title": "Female literacy by group &mdash; the intersection deepens the gap (illustrative)",
              "source": "Illustrative, patterned on Census &amp; NFHS literacy gradients",
              "type": "bar",
              "data": {"labels": ["Upper-caste men", "Upper-caste women",
                                   "Dalit men", "Dalit women"],
                       "datasets": [{"label": "Literacy (%)",
                                     "data": [85, 72, 66, 49],
                                     "backgroundColor": ["#0EA5E9", "#6366F1", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100, title:{display:true,text:'literacy %'}} } }"}},
         ]},

        {"type": "content", "label": "Reading the Gap", "title": "Why one axis is never enough",
         "blocks": [
             {"t": "body", "html": "Report only the gender gap and you miss caste; report only "
              "the caste gap and you miss gender. The Dalit woman sits at the bottom of the "
              "previous chart not by coincidence but by the <em>compounding</em> the matrix of "
              "domination predicts."},
             {"t": "hbox", "color": "amber", "html": "Illustrative figures &mdash; but the "
              "<em>gradient</em> is real and well documented. Always cross-tabulate the axes that "
              "matter, even when it shrinks your cell sizes."},
         ]},

        {"type": "content", "label": "From Frame to Practice", "title": "Using the matrix in your work",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Map which domain a data injustice lives in &mdash; then target it there",
                 "Disaggregate by more than one axis whenever sample size allows",
                 "Name the intersection your programme most affects",
                 "Design data collection so the most marginalised are visible, not residual"]},
         ]},

        {"type": "content", "label": "Privilege &amp; Oppression", "title": "Everyone sits on the matrix",
         "blocks": [
             {"t": "body", "html": "The matrix of domination is not a list of 'oppressed groups' "
              "&mdash; it is a structure everyone occupies. A person can be privileged on one "
              "axis (caste) and oppressed on another (gender), advantaged here and disadvantaged "
              "there."},
             {"t": "hbox", "color": "cyan", "html": "This guards against a single 'victim' or "
              "'villain' story. It also reminds analysts to examine their own position in the "
              "matrix &mdash; the privilege hazard begins at home."},
         ]},

        {"type": "content", "label": "Beyond Two Axes", "title": "The intersections multiply",
         "blocks": [
             {"t": "body", "html": "Caste and gender are central in South Asia, but the matrix "
              "has many axes: religion, disability, sexuality, language, region, age and "
              "migration status all intersect. A disabled Muslim trans woman migrant sits at an "
              "intersection almost no dataset captures."},
             {"t": "hbox", "color": "amber", "html": "You cannot disaggregate by everything at "
              "once &mdash; sample sizes forbid it. But you can name which intersection your work "
              "most affects, and design to see <em>that</em> one clearly."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Gender Data Gaps in South Asia"},

        {"type": "content", "label": "The Gap", "title": "The gender data gap",
         "blocks": [
             {"t": "term", "word": "Gender data gap",
              "def": "The systematic absence of sex-disaggregated and gender-relevant data, which "
              "renders women's and gender-diverse people's lives, work and needs invisible to "
              "policy."},
             {"t": "body", "html": "What is not counted is not budgeted for. The gender data gap "
              "is not a technical oversight &mdash; it is the privilege hazard at the scale of a "
              "whole statistical system."},
         ]},

        {"type": "content", "label": "Default Male", "title": "Caroline Criado Perez: the 'default male'",
         "blocks": [
             {"t": "body", "html": "In <strong><em>Invisible Women</em> (2019)</strong>, "
              "<strong>Caroline Criado Perez</strong> documents how a world built on data that "
              "treats the average man as the default harms women &mdash; from car-crash dummies "
              "to drug doses to phone sizes designed for men's hands."},
             {"t": "hbox", "color": "red", "html": "The 'default male' is not malice; it is a gap. "
              "Data that forgot to ask about women produces a world that does not fit them &mdash; "
              "and calls the misfit 'normal'."},
         ]},

        {"type": "content", "label": "Time-Use", "title": "The unpaid-work gap, made visible",
         "blocks": [
             {"t": "chart", "canvas": "dfTimeUseChart",
              "title": "Average minutes/day on unpaid domestic &amp; care work, by sex",
              "source": "Pattern based on India Time Use Survey 2019 (illustrative values)",
              "type": "bar",
              "data": {"labels": ["Unpaid domestic work", "Unpaid caregiving", "Paid work"],
                       "datasets": [
                           {"label": "Women", "data": [240, 134, 90],
                            "backgroundColor": "#EF4444"},
                           {"label": "Men", "data": [55, 38, 230],
                            "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ plugins:{legend:{position:'bottom'}}, scales:{ y:{min:0, title:{display:true,text:'minutes per day'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative values patterned on the Time "
              "Use Survey 2019, which found women spend far more time on unpaid work and men far "
              "more on paid work. Counting it was the first step to valuing it."},
         ]},

        {"type": "content", "label": "Why TUS Matters", "title": "Time Use Survey 2019: a data-feminist landmark",
         "blocks": [
             {"t": "body", "html": "India's <strong>Time Use Survey 2019</strong> (NSO) was the "
              "first nationwide TUS in nearly two decades. By measuring how people spend their "
              "24 hours, it rendered the unpaid care economy &mdash; overwhelmingly women's work "
              "&mdash; statistically visible."},
             {"t": "hbox", "color": "green", "html": "You cannot value, redistribute or reduce a "
              "burden you do not measure. The TUS turned 'women's work' from an assumption into "
              "an official number."},
         ]},

        {"type": "content", "label": "NFHS-5", "title": "What NFHS-5 reveals &mdash; and asks well",
         "blocks": [
             {"t": "body", "html": "<strong>NFHS-5 (2019&ndash;21)</strong> is a gender-data "
              "powerhouse: it measures women's anaemia, age at marriage, decision-making, "
              "experience of spousal violence, account ownership and mobile-phone access &mdash; "
              "asked directly of women."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Women's status", "label": "Decision-making, mobility, asset ownership",
                  "color": "cyan", "source": "NFHS-5, 2019&ndash;21"},
                 {"num": "GBV module", "label": "Spousal violence asked privately, with consent",
                  "color": "indigo", "source": "NFHS-5"},
                 {"num": "Disaggregated", "label": "By caste, wealth, residence and education",
                  "color": "green", "source": "NFHS-5"}]},
         ]},

        {"type": "content", "label": "GBV Underreporting", "title": "Even good surveys hit the silence",
         "blocks": [
             {"t": "body", "html": "NFHS asks about violence carefully and privately &mdash; yet "
              "even then, <strong>under-reporting</strong> is severe: shame, fear and "
              "normalisation keep many women from disclosing. The survey number is a floor, never "
              "a ceiling."},
             {"t": "hbox", "color": "red", "html": "When you read a GBV statistic, read it as 'at "
              "least this many'. The gap between reported and real is itself evidence of the "
              "power that enforces silence."},
         ]},

        {"type": "content", "label": "Closing the Gap", "title": "What closing the gap looks like",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Disaggregate <em>every</em> indicator by sex &mdash; as a default, not a request",
                 "Interview women directly, not via the 'head of household'",
                 "Add a third-gender category and ask about it meaningfully",
                 "Measure unpaid work, mobility, safety and time, not only income",
                 "Fund the surveys &mdash; gender data costs money the budget often skips"]},
         ]},

        {"type": "content", "label": "Who Holds the Phone", "title": "The digital gender gap",
         "blocks": [
             {"t": "body", "html": "As services move online, a new gap opens: women in South "
              "Asia are markedly less likely to own a phone or use mobile internet. Data "
              "collected through digital channels then over-represents men &mdash; the privilege "
              "hazard, upgraded for the digital age."},
             {"t": "hbox", "color": "red", "html": "A 'digital-first' survey or grievance system "
              "can silently exclude the very women it claims to reach. Who holds the phone shapes "
              "who appears in the data."},
         ]},

        {"type": "content", "label": "Visible &ne; Helped", "title": "Counting is necessary, not sufficient",
         "blocks": [
             {"t": "body", "html": "Closing the data gap is essential &mdash; but being counted "
              "is not the same as being served. Surveillance counts the marginalised closely "
              "while denying them rights. The feminist test is not just visibility, but "
              "visibility that <em>benefits</em> the counted."},
             {"t": "hbox", "color": "amber", "html": "Ask of any new data effort: does this count "
              "people in order to help them, or in order to watch and control them? The "
              "difference is everything."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Practice &amp; Tools"},

        {"type": "content", "label": "Bringing It Together", "title": "The seven principles, as practice",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Principle", "Ask of your own work"],
              "rows": [
                  ["Examine power", "Who made this data, about whom, for whom?"],
                  ["Challenge power", "Could this data contest an injustice?"],
                  ["Elevate emotion", "Have I kept the people behind the rows?"],
                  ["Rethink binaries", "What do my categories exclude?"],
                  ["Embrace pluralism", "Whose knowledge did I leave out?"],
                  ["Consider context", "Am I publishing a number without its context?"],
                  ["Make labour visible", "Did I credit the work behind the data?"]]},
         ]},

        {"type": "content", "label": "The Checklist", "title": "A data-feminist checklist",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Have I asked who is <strong>missing</strong> from this dataset?",
                 "Have I <strong>disaggregated</strong> by gender &mdash; and a second axis?",
                 "Did the people in the data have a say in its design?",
                 "Have I named the data's <strong>limits</strong> and exclusions?",
                 "Have I credited the <strong>labour</strong> that produced it?",
                 "Does this data shift power &mdash; or just describe it?"]},
         ]},

        {"type": "content", "label": "Disaggregation", "title": "Disaggregation is the everyday tool",
         "blocks": [
             {"t": "body", "html": "If data feminism had one operational habit, it would be "
              "<strong>disaggregation</strong>: never settle for the average. Break every "
              "headline number down by sex, then by caste, disability, region and wealth &mdash; "
              "and watch the hidden inequities appear."},
             {"t": "hbox", "color": "cyan", "html": "An average is a place to start asking "
              "questions, never a place to stop. What you do not disaggregate, you cannot see."},
         ]},

        {"type": "content", "label": "Guarding Against Harm", "title": "Disaggregate &mdash; but protect",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Do", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Cross-tabulate the axes that matter",
                      "Report cell sizes and uncertainty",
                      "Centre the most marginalised group"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "But beware", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Small cells can re-identify individuals",
                      "Categories can stigmatise as well as reveal",
                      "Consent and privacy still apply"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Visibility is power &mdash; and power can "
              "protect or expose. Disaggregate to include, with care not to endanger."},
         ]},

        {"type": "content", "label": "Common Pitfalls", "title": "Mistakes to avoid",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Reporting an average and calling the analysis done",
                 "Disaggregating by one axis and ignoring the intersection",
                 "Treating survey numbers as ceilings rather than floors",
                 "Mistaking 'more data' for 'more justice'",
                 "Counting people without ever returning value to them"]},
             {"t": "hbox", "color": "cyan", "html": "Each pitfall has the same root: forgetting "
              "that data is about people, and that power shaped how they came to be counted."},
         ]},

        {"type": "content", "label": "Reading List", "title": "Read further",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Data Feminism</em> &mdash; Catherine D'Ignazio &amp; Lauren Klein (2020)",
                 "<em>Invisible Women</em> &mdash; Caroline Criado Perez (2019)",
                 "<em>Black Feminist Thought</em> &mdash; Patricia Hill Collins (matrix of domination)",
                 "Crenshaw (1989), '<em>Demarginalizing the Intersection of Race and Sex</em>'",
                 "Sen (1990), '<em>More Than 100 Million Women Are Missing</em>'"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Gender &amp; Development</strong> and "
              "<strong>Research Ethics</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Data is never neutral</strong> &mdash; it carries power and choices",
                 "<strong>Ask who is missing</strong> &mdash; the uncounted are usually the marginalised",
                 "<strong>Disaggregate</strong> &mdash; by gender, and by a second axis like caste",
                 "<strong>Context and labour matter</strong> &mdash; numbers don't speak; people make them",
                 "<strong>Count for justice</strong> &mdash; let data shift power, not just describe it"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Data Feminism 101 &middot; Complete",
         "headline": "Now ask: who made<br>this data, and for whom?",
         "byline": "Data is never neutral. Examine power, challenge it, count the people the "
                   "numbers forget &mdash; and let your data work toward justice. Explore the "
                   "rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
