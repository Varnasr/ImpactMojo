# -*- coding: utf-8 -*-
"""
Gender Mainstreaming 101 — ImpactMojo 101 Series (native deck spec)
Foundational gender mainstreaming for South Asian development practitioners.
Build: python3 scripts/deck-builder/build.py gender_mainstreaming
"""

DECK = {
    "slug": "gender-mainstreaming",
    "title": "Gender Mainstreaming 101",
    "description": ("Gender Mainstreaming 101 — a free foundational course for development "
                    "practitioners and programme managers in South Asia: from the Beijing "
                    "Platform and ECOSOC definition to gender analysis, the programme cycle, "
                    "gender-responsive budgeting, the twin-track approach, institutionalisation "
                    "and the critiques that keep it honest. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Gender<br>Mainstreaming<br>101",
         "sub": "Making Gender Integral to Every Policy &amp; Programme &mdash; a Foundational "
                "Course for Development Practitioners &amp; Programme Managers in South Asia",
         "tags": ["Beijing 1995", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Gender Mainstreaming Is"},
             {"name": "Key Concepts"},
             {"name": "Analytical Frameworks"},
             {"name": "Doing Gender Analysis"},
             {"name": "Gender Across the Programme Cycle"},
             {"name": "Gender-Responsive Budgeting"},
             {"name": "Indicators &amp; Measuring Change"},
             {"name": "The Twin-Track Approach"},
             {"name": "Institutionalising Gender"},
             {"name": "Challenges &amp; Critiques"},
             {"name": "The India Context &amp; Practice"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Gender Mainstreaming Is"},

        {"type": "content", "label": "The Definition", "title": "Gender mainstreaming, in the words that coined it",
         "blocks": [
             {"t": "quote",
              "text": "Mainstreaming a gender perspective is the process of assessing the "
              "implications for women and men of any planned action &mdash; including legislation, "
              "policies or programmes, in all areas and at all levels.",
              "attr": "&mdash; UN ECOSOC Agreed Conclusions, 1997"},
             {"t": "hbox", "color": "cyan", "html": "The aim is equality as the <em>goal</em>; "
              "mainstreaming is the <em>strategy</em> for reaching it. Note: it is a process, not "
              "a one-off activity."},
         ]},

        {"type": "content", "label": "Where It Came From", "title": "Beijing, 1995: the global turning point",
         "blocks": [
             {"t": "body", "html": "The <strong>Beijing Platform for Action</strong> &mdash; "
              "adopted by 189 governments at the Fourth World Conference on Women, 1995 &mdash; "
              "made gender mainstreaming the agreed strategy of choice for advancing gender "
              "equality across all 12 critical areas of concern."},
             {"t": "flow", "steps": [
                 "1975 Mexico City: First World Conference on Women",
                 "1985 Nairobi: forward-looking strategies",
                 "1995 BEIJING: mainstreaming adopted as strategy",
                 "1997 ECOSOC: the working definition"]},
         ]},

        {"type": "content", "label": "Not an Add-On", "title": "Integral, not an afterthought",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Add-on thinking", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "'Let's also do something for women'",
                      "A separate gender component or annex",
                      "A line in the budget at the end",
                      "Counted, then forgotten"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Mainstreamed thinking", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Gender shapes the core design",
                      "Asked at every stage and every level",
                      "Resourced from the start",
                      "Owned by everyone, not the 'gender person'"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Mainstreaming means gender is "
              "<strong>everybody's business</strong> and built into the main work &mdash; not "
              "outsourced to a single specialist or a separate project."},
         ]},

        {"type": "content", "label": "Why Bother", "title": "Why neutral is rarely neutral",
         "blocks": [
             {"t": "body", "html": "A 'gender-blind' programme is not neutral &mdash; it quietly "
              "assumes the user is a man with a man's time, mobility and assets. The default "
              "excludes whoever does not fit it."},
             {"t": "term", "word": "Gender-blind",
              "def": "Ignoring gender as a variable &mdash; treating women and men as if their "
              "needs, constraints and opportunities were identical. Usually reinforces existing "
              "inequality by default."},
             {"t": "hbox", "color": "cyan", "html": "Example: a toilet block with no separate, "
              "lockable facilities for women is technically 'sanitation for all' &mdash; and used "
              "by almost no women."},
         ]},

        {"type": "content", "label": "A Spectrum", "title": "From harmful to transformative",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Approach", "What it does", "Stance on norms"],
              "rows": [
                  ["Gender-exploitative", "Uses or worsens inequality", "Reinforces"],
                  ["Gender-blind", "Ignores gender entirely", "Default reinforces"],
                  ["Gender-aware / sensitive", "Recognises differences, adapts", "Works within"],
                  ["Gender-responsive", "Addresses different needs", "Accommodates"],
                  ["Gender-transformative", "Changes unequal norms &amp; power", "Challenges"]]},
             {"t": "hbox", "color": "amber", "html": "Mainstreaming aims to move programmes "
              "<strong>up</strong> this ladder &mdash; ultimately toward the transformative end, "
              "where unequal power itself is the target."},
         ]},

        {"type": "content", "label": "Two Goals", "title": "Equality of treatment and of outcome",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Equality (sameness)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Treating everyone the same. Fair in "
                   "principle, but identical inputs on an unequal starting line preserve the gap."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Equity (fairness)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Allocating according to need to reach a fair "
                   "outcome. Different inputs where starting points differ &mdash; the route to "
                   "real equality."}]}]},
             {"t": "hbox", "color": "green", "html": "Mainstreaming uses <strong>equity</strong> "
              "(treating differently when needed) to achieve <strong>equality</strong> (a fair "
              "result for all)."},
         ]},

        {"type": "content", "label": "Mandate", "title": "It is policy, not charity",
         "blocks": [
             {"t": "body", "html": "Gender mainstreaming is a binding commitment under CEDAW, the "
              "SDGs (Goal 5 and gender targets across all goals), and most national gender "
              "policies in South Asia. It is an obligation, not an optional kindness."},
             {"t": "bullets", "sm": True, "color": "indigo", "items": [
                 "<strong>CEDAW</strong> &mdash; the women's rights treaty (ratified across the region)",
                 "<strong>SDG 5</strong> &mdash; gender equality, with gender data cutting across all 17 goals",
                 "<strong>Beijing+ reviews</strong> &mdash; periodic national progress reporting"]},
         ]},

        {"type": "content", "label": "Common Myths", "title": "What gender mainstreaming is not",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Not</strong> just 'adding women' or counting female heads",
                 "<strong>Not</strong> a separate women's project run on the side",
                 "<strong>Not</strong> the job of one focal point while others opt out",
                 "<strong>Not</strong> anti-men &mdash; it analyses relations, and engages men too",
                 "<strong>Not</strong> a one-time activity &mdash; it is an ongoing process"]},
             {"t": "hbox", "color": "green", "html": "Clearing these myths early saves years of "
              "well-meaning effort spent on the wrong thing. Mainstreaming changes the "
              "<em>mainstream</em> &mdash; that is the whole point."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Key Concepts"},

        {"type": "content", "label": "The Foundational Distinction", "title": "Sex is biological; gender is social",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Sex", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Biological characteristics &mdash; "
                   "chromosomes, anatomy, reproductive function. Largely universal and "
                   "relatively fixed."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Gender", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Socially constructed roles, behaviours and "
                   "expectations a society assigns to women, men and others. Varies by culture and "
                   "changes over time."}]}]},
             {"t": "hbox", "color": "amber", "html": "Because gender is <strong>learned</strong>, "
              "not given, it can be <strong>unlearned and changed</strong>. That possibility is "
              "the whole premise of mainstreaming."},
         ]},

        {"type": "content", "label": "Roles", "title": "Gender roles and the gendered division of labour",
         "blocks": [
             {"t": "body", "html": "Societies assign different work to women and men &mdash; the "
              "<strong>gendered division of labour</strong>. Caroline Moser's framework names "
              "three kinds of work women routinely do, often simultaneously."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Productive", "label": "Paid or income-generating work &mdash; farming, "
                  "wages, enterprise", "color": "cyan"},
                 {"num": "Reproductive", "label": "Unpaid care &amp; domestic work &mdash; "
                  "cooking, water, childcare", "color": "green"},
                 {"num": "Community", "label": "Collective work &mdash; organising, ceremonies, "
                  "local services", "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Moser's Triple Role", "title": "The triple burden",
         "blocks": [
             {"t": "body", "html": "Moser's insight: women typically carry a <strong>triple "
              "role</strong> &mdash; productive, reproductive and community work at once &mdash; "
              "while men's roles are more often single and sequential. Reproductive work is "
              "unpaid, unmeasured and assumed."},
             {"t": "hbox", "color": "red", "html": "A 'time-neutral' programme that adds a "
              "meeting, a training or a worksite to a woman's day stacks it on top of an already "
              "full reproductive load. Mainstreaming asks: whose time are we spending?"},
         ]},

        {"type": "content", "label": "Needs", "title": "Practical vs strategic gender needs",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Practical gender needs", "Strategic gender needs"],
              "rows": [
                  ["What they are", "Immediate, day-to-day needs", "Needs to change unequal position"],
                  ["Arise from", "Existing roles &amp; division of labour", "Subordinate status in society"],
                  ["Examples", "Water, fuel, health post, income", "Land rights, voice, ending violence"],
                  ["Effect", "Eases the condition", "Transforms the position"],
                  ["Challenge norms?", "No &mdash; works within them", "Yes &mdash; reshapes power"]]},
             {"t": "hbox", "color": "cyan", "html": "Moser's distinction: meeting practical needs "
              "improves daily life; meeting strategic needs shifts the underlying power balance. "
              "Good programmes do both."},
         ]},

        {"type": "content", "label": "Condition vs Position", "title": "Improving lives vs shifting power",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Condition", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A woman's material state &mdash; her "
                   "workload, income, health, access to services. A new handpump improves her "
                   "<em>condition</em>."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Position", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Her social and economic standing relative to "
                   "men &mdash; rights, status, decision-making power. Land in her name shifts her "
                   "<em>position</em>."}]}]},
             {"t": "hbox", "color": "amber", "html": "You can improve condition without touching "
              "position. Lasting equality needs both &mdash; or the gains evaporate when the "
              "project ends."},
         ]},

        {"type": "content", "label": "Empowerment", "title": "Empowerment is about power, not just access",
         "blocks": [
             {"t": "term", "word": "Empowerment (Kabeer)",
              "def": "The expansion of people's ability to make strategic life choices in a "
              "context where this ability was previously denied to them &mdash; the process of "
              "gaining power to define and act on one's own goals."},
             {"t": "body", "html": "Naila Kabeer frames empowerment as <strong>resources &rarr; "
              "agency &rarr; achievements</strong>: not just having things, but the capacity to "
              "use them to act, and the outcomes that follow."},
         ]},

        {"type": "content", "label": "Intersectionality", "title": "Gender never travels alone",
         "blocks": [
             {"t": "body", "html": "A woman is never <em>only</em> a woman. Caste, class, "
              "religion, disability, age, region and sexuality intersect to shape very different "
              "experiences. A Dalit woman farm-labourer faces compounded, not merely additive, "
              "disadvantage."},
             {"t": "hbox", "color": "red", "html": "Treating 'women' as one uniform group hides "
              "the women most excluded. Mainstreaming must disaggregate <em>within</em> gender, "
              "not only across it."},
         ]},

        {"type": "content", "label": "Beyond the Binary", "title": "Gender is not only women",
         "blocks": [
             {"t": "body", "html": "Mainstreaming examines relations between women, men and "
              "gender-diverse people. It engages men and boys as stakeholders and allies, and "
              "recognises transgender and non-binary people &mdash; legally affirmed in India by "
              "the NALSA judgment (2014)."},
             {"t": "hbox", "color": "cyan", "html": "'Gender' is relational. Changing women's "
              "lives requires engaging the norms that govern <em>everyone's</em> behaviour."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Analytical Frameworks"},

        {"type": "content", "label": "Why Frameworks", "title": "A framework is a set of questions",
         "blocks": [
             {"t": "body", "html": "Gender frameworks are structured ways of asking 'who does "
              "what, who has what, who decides, and who benefits?' They turn good intentions into "
              "systematic analysis. Each has a different focus &mdash; pick to fit the task."},
             {"t": "flow", "steps": [
                 "HARVARD: maps roles, access &amp; control",
                 "MOSER: needs &amp; the triple role",
                 "KABEER: social relations &amp; institutions",
                 "GAM: participatory impact at four levels"]},
         ]},

        {"type": "content", "label": "Harvard", "title": "The Harvard / Gender Roles Framework",
         "blocks": [
             {"t": "body", "html": "One of the earliest (1985), the <strong>Harvard Analytical "
              "Framework</strong> is efficiency-oriented and data-driven. It maps activities by "
              "gender and the access to, and control over, resources and benefits."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Activity profile:</strong> who does what (productive / reproductive)",
                 "<strong>Access &amp; control profile:</strong> who uses, who decides over resources",
                 "<strong>Influencing factors:</strong> what shapes these patterns"]},
             {"t": "hbox", "color": "amber", "html": "Strength: concrete and visible. Limit: it "
              "describes the division of labour but says little about <em>why</em> power is "
              "unequal."},
         ]},

        {"type": "content", "label": "Moser", "title": "The Moser Framework",
         "blocks": [
             {"t": "body", "html": "Caroline Moser's framework is explicitly "
              "<strong>transformative</strong>. It builds on the triple role and the practical / "
              "strategic needs distinction to ask whether a programme merely eases life or "
              "reshapes power."},
             {"t": "bullets", "sm": True, "color": "indigo", "items": [
                 "Identifies the <strong>triple role</strong> in a given context",
                 "Distinguishes <strong>practical vs strategic</strong> needs",
                 "Assesses how policy approaches address (or ignore) each",
                 "Examines who controls resources and decisions in the household"]},
         ]},

        {"type": "content", "label": "Kabeer", "title": "Kabeer's Social Relations Approach",
         "blocks": [
             {"t": "body", "html": "Naila Kabeer's <strong>Social Relations Approach</strong> "
              "shifts the lens from women alone to the <em>institutions</em> that produce "
              "inequality &mdash; and how they reproduce it across the household, market, state "
              "and community."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "4 institutions", "label": "Household, market, state, community "
                  "&mdash; each carries gendered rules", "color": "cyan"},
                 {"num": "5 dimensions", "label": "Rules, resources, people, activities, power "
                  "&mdash; analysed in each institution", "color": "indigo"}]},
             {"t": "hbox", "color": "green", "html": "Its power: inequality is not a women's "
              "deficit to fix but an institutional pattern to change."},
         ]},

        {"type": "content", "label": "GAM", "title": "The Gender Analysis Matrix",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "Rani Parker's <strong>Gender Analysis Matrix (GAM)</strong> "
              "is participatory and community-led. It maps a programme's likely effects across "
              "four levels and four dimensions of impact."},
             {"t": "table",
              "head": ["Level &darr; / Impact &rarr;", "Labour", "Time", "Resources", "Culture"],
              "rows": [
                  ["Women", "&hellip;", "&hellip;", "&hellip;", "&hellip;"],
                  ["Men", "&hellip;", "&hellip;", "&hellip;", "&hellip;"],
                  ["Household", "&hellip;", "&hellip;", "&hellip;", "&hellip;"],
                  ["Community", "&hellip;", "&hellip;", "&hellip;", "&hellip;"]]},
             {"t": "hbox", "color": "cyan", "html": "Communities fill the cells themselves &mdash; "
              "surfacing impacts (and unintended harms) the planners never anticipated."},
         ]},

        {"type": "content", "label": "Compared", "title": "Choosing a framework for the job",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Framework", "Focus", "Best for"],
              "rows": [
                  ["Harvard", "Roles, access &amp; control", "Rapid baseline mapping"],
                  ["Moser", "Needs &amp; the triple role", "Planning for transformation"],
                  ["Kabeer (SRA)", "Institutions &amp; power", "Root-cause &amp; policy analysis"],
                  ["GAM", "Community impact, 4 levels", "Participatory appraisal"]]},
             {"t": "hbox", "color": "amber", "html": "No framework is 'best'. Efficiency-minded "
              "tools map; transformative tools probe power. Combine them &mdash; map first, then "
              "interrogate why."},
         ]},

        {"type": "content", "label": "What They Share", "title": "Four questions every framework asks",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Who does what?</strong> &mdash; the gendered division of labour",
                 "<strong>Who has what?</strong> &mdash; access to resources and services",
                 "<strong>Who decides?</strong> &mdash; control over resources and choices",
                 "<strong>Who benefits?</strong> &mdash; who gains from the activity or programme"]},
             {"t": "hbox", "color": "green", "html": "Memorise these four. They are the portable "
              "core of gender analysis &mdash; usable even without a formal framework in hand."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Doing Gender Analysis"},

        {"type": "content", "label": "Definition", "title": "What gender analysis actually is",
         "blocks": [
             {"t": "term", "word": "Gender analysis",
              "def": "The systematic examination of the different roles, needs, constraints, "
              "opportunities and power relations of women, men and gender-diverse people in a "
              "given context &mdash; and what a policy or programme will do to them."},
             {"t": "hbox", "color": "cyan", "html": "It is the first step of mainstreaming, not a "
              "specialist luxury. Without it, 'gender-sensitive design' is a guess."},
         ]},

        {"type": "content", "label": "Step Zero", "title": "Sex-disaggregated data: see the gap",
         "blocks": [
             {"t": "body", "html": "You cannot manage what you cannot see. "
              "<strong>Sex-disaggregated data</strong> &mdash; every indicator split by sex "
              "&mdash; is the bedrock. An average of '70% covered' can hide men at 85% and women "
              "at 55%."},
             {"t": "chart", "canvas": "gmDisaggChart",
              "title": "An overall figure can hide a wide gender gap (illustrative)",
              "source": "Illustrative example",
              "type": "bar",
              "data": {"labels": ["Overall", "Men", "Women"],
                       "datasets": [{"label": "Coverage (%)", "data": [70, 85, 55],
                                     "backgroundColor": ["#6366F1", "#0EA5E9", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100,title:{display:true,text:'%'}} } }"}},
         ]},

        {"type": "content", "label": "Beyond Sex", "title": "Gender data is more than a column for sex",
         "blocks": [
             {"t": "body", "html": "True gender data captures issues that disproportionately "
              "affect one gender (unpaid care, violence), reflects women's own realities, and is "
              "collected by methods that reach women &mdash; not just a tick-box added to a male "
              "respondent's form."},
             {"t": "bullets", "sm": True, "color": "indigo", "items": [
                 "Disaggregate by sex <em>and</em> by caste, disability, age",
                 "Measure unpaid work, mobility, voice &mdash; not only income",
                 "Interview women directly, in private, in their language"]},
         ]},

        {"type": "content", "label": "The Four Questions", "title": "Who does, who has, who decides, who benefits",
         "blocks": [
             {"t": "flow", "steps": [
                 "WHO DOES WHAT: the division of labour, paid &amp; unpaid",
                 "WHO HAS WHAT: access to land, credit, services, time",
                 "WHO DECIDES: control over resources &amp; choices",
                 "WHO BENEFITS: who gains from the activity"]},
             {"t": "hbox", "color": "amber", "html": "Run any intervention through these four. "
              "The answers reveal where it will help, where it will miss, and where it might "
              "backfire."},
         ]},

        {"type": "content", "label": "The Crucial Distinction", "title": "Access is not control",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Access", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The opportunity to <em>use</em> a resource. "
                   "A woman may farm the land, draw from the well, attend the clinic."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Control", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The power to <em>decide</em> over the "
                   "resource &mdash; to sell, lease, mortgage, or keep the income. Often the "
                   "man's, even when she does the work."}]}]},
             {"t": "hbox", "color": "amber", "html": "Women frequently have access without "
              "control. A scheme that boosts access but ignores control can leave power exactly "
              "where it was &mdash; or hand the gains to men."},
         ]},

        {"type": "content", "label": "Access vs Control", "title": "Mapping access against control",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 560 300" width="560" height="290" xmlns="http://www.w3.org/2000/svg" '
                 'style="max-width:100%;height:auto;font-family:inherit">'
                 # axes
                 '<line x1="90" y1="250" x2="540" y2="250" stroke="#64748B" stroke-width="2"/>'
                 '<line x1="90" y1="40" x2="90" y2="250" stroke="#64748B" stroke-width="2"/>'
                 '<text x="315" y="285" text-anchor="middle" fill="#94A3B8" font-size="14">CONTROL (power to decide) &rarr;</text>'
                 '<text x="40" y="150" text-anchor="middle" fill="#94A3B8" font-size="14" transform="rotate(-90 40 150)">ACCESS (use) &rarr;</text>'
                 # midlines
                 '<line x1="315" y1="40" x2="315" y2="250" stroke="#334155" stroke-width="1" stroke-dasharray="4 4"/>'
                 '<line x1="90" y1="145" x2="540" y2="145" stroke="#334155" stroke-width="1" stroke-dasharray="4 4"/>'
                 # quadrant boxes
                 '<rect x="100" y="55" width="200" height="80" rx="6" fill="#0EA5E915" stroke="#0EA5E9" stroke-width="1.5"/>'
                 '<text x="200" y="88" text-anchor="middle" fill="#0EA5E9" font-size="13" font-weight="bold">Access, no control</text>'
                 '<text x="200" y="110" text-anchor="middle" fill="#94A3B8" font-size="11">She farms the land</text>'
                 '<text x="200" y="126" text-anchor="middle" fill="#94A3B8" font-size="11">but cannot sell it</text>'
                 '<rect x="330" y="55" width="200" height="80" rx="6" fill="#10B98115" stroke="#10B981" stroke-width="1.5"/>'
                 '<text x="430" y="88" text-anchor="middle" fill="#10B981" font-size="13" font-weight="bold">Access &amp; control</text>'
                 '<text x="430" y="110" text-anchor="middle" fill="#94A3B8" font-size="11">Land in her name;</text>'
                 '<text x="430" y="126" text-anchor="middle" fill="#94A3B8" font-size="11">she decides &mdash; the goal</text>'
                 '<rect x="100" y="160" width="200" height="80" rx="6" fill="#EF444415" stroke="#EF4444" stroke-width="1.5"/>'
                 '<text x="200" y="193" text-anchor="middle" fill="#EF4444" font-size="13" font-weight="bold">Neither</text>'
                 '<text x="200" y="215" text-anchor="middle" fill="#94A3B8" font-size="11">Excluded from the</text>'
                 '<text x="200" y="231" text-anchor="middle" fill="#94A3B8" font-size="11">resource entirely</text>'
                 '<rect x="330" y="160" width="200" height="80" rx="6" fill="#F59E0B15" stroke="#F59E0B" stroke-width="1.5"/>'
                 '<text x="430" y="193" text-anchor="middle" fill="#F59E0B" font-size="13" font-weight="bold">Control, no access</text>'
                 '<text x="430" y="215" text-anchor="middle" fill="#94A3B8" font-size="11">Owns on paper but</text>'
                 '<text x="430" y="231" text-anchor="middle" fill="#94A3B8" font-size="11">others use it (rare)</text>'
                 '</svg></div>'
             )},
             {"t": "hbox", "color": "green", "html": "Mainstreaming pushes resources toward the "
              "top-right quadrant: women with both access <em>and</em> control."},
         ]},

        {"type": "content", "label": "How To Do It", "title": "A lightweight gender analysis, in practice",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Collect or find sex-disaggregated baseline data",
                 "Map roles, access and control with the community (not for it)",
                 "Identify practical and strategic needs separately",
                 "Test the design against the four questions",
                 "Name likely risks &mdash; backlash, added workload, exclusion",
                 "Feed findings straight into objectives, activities and indicators"]},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Gender Across the Programme Cycle"},

        {"type": "content", "label": "The Whole Cycle", "title": "Gender belongs at every stage",
         "blocks": [
             {"t": "body", "html": "Mainstreaming is not a single step bolted on at design. "
              "Gender questions run through the entire programme cycle &mdash; and a gap at any "
              "stage leaks the gains made in the others."},
             {"t": "flow", "steps": [
                 "ANALYSE: gender analysis &amp; sex-disaggregated baseline",
                 "DESIGN: gendered objectives, activities, indicators",
                 "IMPLEMENT: equitable access, safe participation",
                 "MONITOR &amp; EVALUATE: track gendered results"]},
         ]},

        {"type": "content", "label": "Design", "title": "Gender-sensitive design",
         "blocks": [
             {"t": "bullets", "items": [
                 "Set <strong>explicit gender objectives</strong>, not just an aspiration",
                 "Design activities around women's time, mobility and safety constraints",
                 "Build in measures for access <em>and</em> control",
                 "Budget for the gender work from the start (see Section 6)",
                 "Plan to engage men so as to reduce backlash"]},
             {"t": "hbox", "color": "amber", "html": "If gender objectives are absent at design, "
              "no amount of monitoring will conjure them later. Design is where mainstreaming is "
              "won or lost."},
         ]},

        {"type": "content", "label": "Implementation", "title": "Equitable implementation",
         "blocks": [
             {"t": "body", "html": "Even a well-designed programme can exclude women in delivery: "
              "wrong timing, unsafe locations, male-only staff, information that never reaches "
              "women. Implementation is where good design meets hard reality."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Barriers in delivery", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Meetings timed against the care load",
                      "Distant or unsafe venues",
                      "All-male field teams",
                      "Information shared only with men"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Fixes", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Flexible timing, childcare on site",
                      "Local, safe, accessible venues",
                      "Women field staff &amp; mobilisers",
                      "Reach women through their own channels"]}]}]},
         ]},

        {"type": "content", "label": "M&amp;E", "title": "Gender-responsive monitoring &amp; evaluation",
         "blocks": [
             {"t": "body", "html": "If results are not disaggregated, the programme is flying "
              "blind on equity. Gender-responsive M&amp;E tracks <em>who</em> participated, "
              "<em>who</em> benefited, and whether power relations shifted &mdash; not just totals."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Disaggregate every output and outcome indicator by sex",
                 "Include indicators on control, voice and workload, not only access",
                 "Collect qualitative evidence on changing norms",
                 "Ask women themselves to judge what changed"]},
         ]},

        {"type": "content", "label": "Tools", "title": "Gender markers: scoring the cycle",
         "blocks": [
             {"t": "term", "word": "Gender marker",
              "def": "A coding system that rates how strongly a project or budget line is "
              "designed to advance gender equality &mdash; e.g. 0 (gender-blind) to 2 or 3 "
              "(gender as a principal objective)."},
             {"t": "body", "html": "Markers (used by the OECD-DAC, UN agencies and many donors) "
              "turn 'is this gender-sensitive?' into a trackable score across a whole portfolio, "
              "exposing how much funding is genuinely gendered."},
         ]},

        {"type": "content", "label": "Marker Scale", "title": "Reading a gender marker score",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Score", "Meaning", "Example"],
              "rows": [
                  ["0", "Gender-blind / no attention", "Road built with no gender analysis"],
                  ["1", "Gender a significant objective", "Road plus safe transport for women"],
                  ["2", "Gender the principal objective", "Programme to end gender-based violence"]]},
             {"t": "hbox", "color": "amber", "html": "A common red flag at portfolio level: lots "
              "of '1's, almost no '2's, and a quiet pile of un-scored '0's. The markers reveal "
              "where mainstreaming is real versus rhetorical."},
         ]},

        {"type": "content", "label": "Participation", "title": "Counting heads is not participation",
         "blocks": [
             {"t": "body", "html": "'50% of attendees were women' can still mean women sat "
              "silent at the back. Mainstreaming asks about the <strong>quality</strong> of "
              "participation: who spoke, who was heard, who shaped the decision."},
             {"t": "hbox", "color": "red", "html": "Beware 'nominal' inclusion &mdash; a quota "
              "met on paper while real influence stays with men. Measure voice, not just "
              "attendance."},
         ]},

        {"type": "content", "label": "Do No Harm", "title": "Watch for unintended backlash",
         "blocks": [
             {"t": "body", "html": "Shifting gender roles can provoke resistance &mdash; "
              "increased domestic tension or even violence when women gain income or visibility. "
              "Mainstreaming includes a <strong>do-no-harm</strong> lens."},
             {"t": "bullets", "sm": True, "color": "amber", "items": [
                 "Engage men and family early to reduce threat",
                 "Avoid adding unsupported workload to women",
                 "Have referral pathways for violence in place",
                 "Monitor for backlash as a real programme risk"]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Gender-Responsive Budgeting"},

        {"type": "content", "label": "Definition", "title": "Following the money through a gender lens",
         "blocks": [
             {"t": "term", "word": "Gender-responsive budgeting (GRB)",
              "def": "Not a separate budget for women, but the analysis and restructuring of "
              "<em>the whole</em> budget &mdash; revenue and expenditure &mdash; to assess and "
              "advance its impact on gender equality."},
             {"t": "hbox", "color": "cyan", "html": "GRB asks: does this 'gender-neutral' road, "
              "subsidy or salary line actually serve women and men equally? Budgets are policy "
              "stated in money."},
         ]},

        {"type": "content", "label": "Why Budgets", "title": "A budget is a moral document",
         "blocks": [
             {"t": "body", "html": "Policies promise; budgets deliver. A gender policy with no "
              "money behind it is a wish. GRB is how mainstreaming reaches the one stage that "
              "decides what actually happens &mdash; the allocation of resources."},
             {"t": "quote",
              "text": "Show me your budget and I will tell you what you truly value.",
              "attr": "&mdash; a principle of gender budgeting practice"},
         ]},

        {"type": "content", "label": "How GRB Works", "title": "Three buckets of spending",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Category", "What it covers", "Example"],
              "rows": [
                  ["Women-specific", "Targeted at women / girls", "Maternity benefit, girls' scholarships"],
                  ["Pro-equality within general", "Mainstream schemes with gender focus", "Toilets for girls in schools"],
                  ["General / mainstream", "Everything else &mdash; assessed for impact", "Roads, power, salaries"]]},
             {"t": "hbox", "color": "amber", "html": "The radical step is the third bucket: "
              "examining the supposedly 'neutral' 95% of the budget for its hidden gendered "
              "effects, not just the small targeted slice."},
         ]},

        {"type": "content", "label": "India's Tool", "title": "India's Gender Budget Statement",
         "blocks": [
             {"t": "body", "html": "Since 2005&ndash;06, India's Union Budget has included a "
              "<strong>Gender Budget Statement (GBS)</strong> &mdash; Statement 13 in the Budget "
              "documents &mdash; reporting allocations to schemes that benefit women, across "
              "central ministries."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Part A", "label": "Schemes with 100% allocation for women &amp; girls",
                  "color": "cyan"},
                 {"num": "Part B", "label": "Schemes with at least 30% allocation for women",
                  "color": "indigo"}]},
             {"t": "hbox", "color": "green", "html": "The GBS made gender spending visible and "
              "trackable year on year &mdash; a genuine institutional advance, and a model copied "
              "across the region."},
         ]},

        {"type": "content", "label": "Illustrative", "title": "What a gender budget share looks like",
         "blocks": [
             {"t": "chart", "canvas": "gmGbShareChart",
              "title": "Gender budget as a share of total expenditure (illustrative pattern)",
              "source": "Illustrative &mdash; not actual figures",
              "type": "line",
              "data": {"labels": ["Yr 1", "Yr 2", "Yr 3", "Yr 4", "Yr 5", "Yr 6"],
                       "datasets": [{"label": "Gender budget share (%)",
                                     "data": [4.8, 5.1, 5.0, 4.6, 5.3, 5.5],
                                     "borderColor": "#10B981",
                                     "backgroundColor": "rgba(16,185,129,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:8,title:{display:true,text:'% of total'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative shape only. The recurring "
              "real-world finding: the gender share hovers at a small single-digit percentage and "
              "barely grows &mdash; ambition outruns allocation."},
         ]},

        {"type": "content", "label": "Sub-National", "title": "GRB below the centre",
         "blocks": [
             {"t": "body", "html": "Several Indian states and many local bodies run their own "
              "gender budgeting &mdash; gender budget cells in departments, and gender-tagged "
              "allocations in panchayat and municipal plans. This is where money meets women's "
              "daily lives most directly."},
             {"t": "hbox", "color": "cyan", "html": "Local gender budgeting lets women themselves "
              "weigh in on what gets funded &mdash; a handpump, a lit bus stop, a creche &mdash; "
              "in the gram sabha."},
         ]},

        {"type": "content", "label": "Doing GRB", "title": "Five steps to a gender-responsive budget",
         "blocks": [
             {"t": "flow", "steps": [
                 "1. Profile women's &amp; men's situation in the sector",
                 "2. Assess if policy responds to gendered needs",
                 "3. Check whether the budget matches the policy",
                 "4. Track spending &amp; outputs by gender",
                 "5. Reassess &amp; reallocate for the next cycle"]},
             {"t": "hbox", "color": "amber", "html": "Adapted from Diane Elson's widely used "
              "GRB framework &mdash; the analytical backbone of gender budgeting worldwide."},
         ]},

        {"type": "content", "label": "Watch-Outs", "title": "Where gender budgeting goes wrong",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Reporting, not budgeting:</strong> a statement compiled after the fact, "
                 "changing no allocation",
                 "<strong>Mislabelling:</strong> general schemes tagged 'for women' to inflate "
                 "the figure",
                 "<strong>Allocation &ne; spending:</strong> funds budgeted but never released "
                 "or utilised",
                 "<strong>No outcome link:</strong> rupees counted, results for women never measured"]},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Indicators &amp; Measuring Change"},

        {"type": "content", "label": "The Challenge", "title": "Measuring what matters most",
         "blocks": [
             {"t": "body", "html": "The deepest changes &mdash; agency, voice, freedom from "
              "fear &mdash; are the hardest to count. Yet what goes unmeasured goes unfunded. "
              "Good gender indicators make the invisible visible without flattening it."},
             {"t": "hbox", "color": "cyan", "html": "Pair <strong>quantitative</strong> "
              "indicators (how many, how much) with <strong>qualitative</strong> evidence (what "
              "changed, in whose judgement). Numbers alone miss empowerment."},
         ]},

        {"type": "content", "label": "Types", "title": "Three layers of gender indicators",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Layer", "Captures", "Example"],
              "rows": [
                  ["Access / condition", "Resources &amp; services reached", "% women with bank accounts"],
                  ["Agency", "Decision-making &amp; voice", "% women deciding own healthcare"],
                  ["Position / norms", "Status &amp; underlying norms", "Acceptance of women in leadership"]]},
             {"t": "hbox", "color": "amber", "html": "Most programmes measure only the first row. "
              "Empowerment lives in the second and third &mdash; harder to measure, but the point "
              "of the exercise."},
         ]},

        {"type": "content", "label": "Agency Indicators", "title": "Measuring decision-making and voice",
         "blocks": [
             {"t": "body", "html": "Surveys like NFHS already ask agency questions &mdash; who "
              "decides on a woman's healthcare, major purchases, or visits to family; whether she "
              "owns a phone or operates a bank account; whether she can move freely."},
             {"t": "bullets", "sm": True, "color": "indigo", "items": [
                 "Sole or joint say in household decisions",
                 "Mobility &mdash; can she travel alone to key places?",
                 "Control over own and household income",
                 "Ownership of assets &mdash; land, house, account, phone"]},
         ]},

        {"type": "content", "label": "A Persistent Gap", "title": "Where gendered gaps show up",
         "blocks": [
             {"t": "chart", "canvas": "gmGapChart",
              "title": "Illustrative gender gaps across indicators (women vs men, %)",
              "source": "Illustrative &mdash; patterned on the kinds of gaps seen in regional data",
              "type": "bar",
              "data": {"labels": ["Labour-force participation", "Asset ownership",
                                   "Account use", "Phone ownership"],
                       "datasets": [
                           {"label": "Women", "data": [25, 30, 55, 60], "backgroundColor": "#EF4444"},
                           {"label": "Men", "data": [70, 60, 78, 85], "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ scales:{ y:{min:0,max:100,title:{display:true,text:'%'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative bars, not exact statistics. "
              "The <em>pattern</em> is real and well-documented: women trail on participation, "
              "assets and control across South Asia."},
         ]},

        {"type": "content", "label": "GBV-Sensitivity", "title": "Measuring violence with care",
         "blocks": [
             {"t": "body", "html": "Gender-based violence is widespread and badly under-reported. "
              "Measuring it demands <strong>GBV-sensitive</strong> methods &mdash; safety and "
              "ethics first &mdash; or the data itself can endanger respondents."},
             {"t": "bullets", "sm": True, "color": "red", "items": [
                 "Interview in private, by trained women interviewers",
                 "Guarantee confidentiality; never interview with the partner present",
                 "Have referral and support pathways ready before you ask",
                 "Read rising reports as better disclosure, not always rising violence"]},
         ]},

        {"type": "content", "label": "Composite Indices", "title": "Global gender indices, and their limits",
         "blocks": [
             {"t": "body", "html": "Indices like the UNDP's <strong>Gender Inequality Index "
              "(GII)</strong> and the WEF's <strong>Global Gender Gap Index</strong> bundle "
              "health, education, economic and political indicators into one comparable score."},
             {"t": "hbox", "color": "amber", "html": "Useful for advocacy and ranking, but a "
              "single number hides which dimension is failing. Always open the index back up "
              "before drawing a programme conclusion from a rank."},
         ]},

        {"type": "content", "label": "Good Indicators", "title": "What makes a gender indicator useful",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Disaggregable", "label": "Splits by sex &mdash; and by caste, "
                  "disability, age", "color": "cyan"},
                 {"num": "Relevant", "label": "Tracks the change that matters, not just what is "
                  "easy", "color": "green"},
                 {"num": "Sensitive", "label": "Moves when women's real situation moves",
                  "color": "indigo"},
                 {"num": "Ethical", "label": "Safe to collect, especially on violence",
                  "color": "amber"}]},
         ]},

        {"type": "content", "label": "Mixed Methods", "title": "Numbers plus narratives",
         "blocks": [
             {"t": "body", "html": "A figure tells you <em>that</em> women's account use rose; a "
              "woman's story tells you whether <em>she</em> controls the account or her husband "
              "operates it. The most honest gender M&amp;E weaves both together."},
             {"t": "hbox", "color": "cyan", "html": "Tools like the 'most significant change' "
              "technique and participatory scoring let women define and rate change in their own "
              "terms &mdash; capturing empowerment a survey would miss."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "The Twin-Track Approach"},

        {"type": "content", "label": "The Core Strategy", "title": "Two tracks, run together",
         "blocks": [
             {"t": "body", "html": "Experience showed that mainstreaming <em>alone</em> can "
              "dilute into nothing, while women-only projects <em>alone</em> stay marginal. The "
              "<strong>twin-track approach</strong> runs both at once &mdash; and is now standard "
              "in EU, UN and most donor policy."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Track 1: Mainstream", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Integrate gender into <em>every</em> policy, "
                   "programme and budget &mdash; everywhere, by everyone."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Track 2: Target", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Run dedicated women's-empowerment "
                   "interventions to close specific gaps and build agency."}]}]},
         ]},

        {"type": "content", "label": "The Diagram", "title": "How the twin tracks work together",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 600 290" width="600" height="280" xmlns="http://www.w3.org/2000/svg" '
                 'style="max-width:100%;height:auto;font-family:inherit">'
                 # track 1 bar
                 '<rect x="40" y="55" width="380" height="60" rx="8" fill="#0EA5E915" stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="230" y="80" text-anchor="middle" fill="#0EA5E9" font-size="14" font-weight="bold">TRACK 1 &mdash; Gender mainstreaming</text>'
                 '<text x="230" y="100" text-anchor="middle" fill="#94A3B8" font-size="11">gender built into all policies, programmes &amp; budgets</text>'
                 # track 2 bar
                 '<rect x="40" y="135" width="380" height="60" rx="8" fill="#10B98115" stroke="#10B981" stroke-width="2"/>'
                 '<text x="230" y="160" text-anchor="middle" fill="#10B981" font-size="14" font-weight="bold">TRACK 2 &mdash; Targeted empowerment</text>'
                 '<text x="230" y="180" text-anchor="middle" fill="#94A3B8" font-size="11">dedicated women-specific interventions</text>'
                 # arrows converging
                 '<line x1="420" y1="85" x2="495" y2="120" stroke="#64748B" stroke-width="2" marker-end="url(#gmArrow)"/>'
                 '<line x1="420" y1="165" x2="495" y2="130" stroke="#64748B" stroke-width="2" marker-end="url(#gmArrow)"/>'
                 '<defs><marker id="gmArrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">'
                 '<path d="M0,0 L6,3 L0,6 Z" fill="#64748B"/></marker></defs>'
                 # goal box
                 '<rect x="500" y="95" width="90" height="60" rx="8" fill="#6366F120" stroke="#6366F1" stroke-width="2"/>'
                 '<text x="545" y="120" text-anchor="middle" fill="#6366F1" font-size="13" font-weight="bold">GENDER</text>'
                 '<text x="545" y="138" text-anchor="middle" fill="#6366F1" font-size="13" font-weight="bold">EQUALITY</text>'
                 # caption
                 '<text x="300" y="240" text-anchor="middle" fill="#94A3B8" font-size="12">Mainstreaming spreads the lens everywhere; targeting closes the gaps mainstreaming alone leaves.</text>'
                 '</svg></div>'
             )},
         ]},

        {"type": "content", "label": "Why Both", "title": "Each track covers the other's blind spot",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Mainstreaming alone fails when&hellip;", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Gender becomes 'everyone's job, so no one's'",
                      "It dilutes to a checkbox",
                      "Deep, specific gaps go unaddressed"]}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Targeting alone fails when&hellip;", "blocks": [
                  {"t": "bullets", "sm": True, "color": "amber", "items": [
                      "It stays a small, marginal silo",
                      "The mainstream 95% stays gender-blind",
                      "It is the first thing cut in a squeeze"]}]}]},
             {"t": "hbox", "color": "green", "html": "Run together, each track guards against the "
              "other's failure mode. That is the whole logic of the twin track."},
         ]},

        {"type": "content", "label": "Track 2 Examples", "title": "What targeted empowerment looks like",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Women's self-help groups and federations (e.g. India's NRLM / DAY-NRLM)",
                 "Girls' scholarships and conditional transfers",
                 "Women-only skilling, enterprise and credit programmes",
                 "Leadership quotas &mdash; one-third reservation in panchayats",
                 "Dedicated services on violence, health and legal aid"]},
         ]},

        {"type": "content", "label": "A Caution", "title": "Targeting is not 'doing gender'",
         "blocks": [
             {"t": "body", "html": "A common error: running one women's project and declaring "
              "gender 'done' &mdash; while every other programme stays blind. Track 2 is "
              "necessary but never sufficient. Both tracks, always."},
             {"t": "hbox", "color": "red", "html": "If your only gender work is a separate "
              "women's component, you are doing Track 2, not mainstreaming. The mainstream itself "
              "must change."},
         ]},

        {"type": "content", "label": "Balancing", "title": "Getting the mix right",
         "blocks": [
             {"t": "body", "html": "The balance shifts by context. Where gaps are wide and "
              "women's voice is weak, Track 2 may need to lead at first &mdash; building the "
              "agency that lets women claim space in the mainstream Track 1 then opens."},
             {"t": "hbox", "color": "cyan", "html": "Think of Track 2 as building capability and "
              "Track 1 as opening opportunity. Empowerment without opportunity frustrates; "
              "opportunity without capability excludes."},
         ]},

        {"type": "content", "label": "Engaging Men", "title": "A third strand: men and boys",
         "blocks": [
             {"t": "body", "html": "Increasingly, twin-track practice adds work with men and "
              "boys &mdash; on shared care, respectful relationships and challenging harmful "
              "masculinities &mdash; because women's gains stick only when norms around men "
              "shift too."},
             {"t": "hbox", "color": "amber", "html": "Engaging men is an ally strategy, not a "
              "diversion of resources from women. Done badly it re-centres men; done well it "
              "removes the backlash that undoes Track 2."},
         ]},

        {"type": "content", "label": "Summary", "title": "The twin-track, in one line",
         "blocks": [
             {"t": "quote",
              "text": "Mainstream gender into everything you do &mdash; and keep doing the "
              "targeted things that only women's empowerment can achieve.",
              "attr": "&mdash; the twin-track principle"},
             {"t": "hbox", "color": "green", "html": "Neither track replaces the other. Mainstreaming "
              "without targeting drifts; targeting without mainstreaming stalls."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Institutionalising Gender"},

        {"type": "content", "label": "The Real Test", "title": "From a project to a way of working",
         "blocks": [
             {"t": "body", "html": "Mainstreaming succeeds only when it survives the departure of "
              "the committed individual. <strong>Institutionalisation</strong> embeds gender into "
              "an organisation's policies, systems, skills, budgets and culture &mdash; so it "
              "becomes the default."},
             {"t": "flow", "steps": [
                 "POLICY: a clear gender policy &amp; commitment",
                 "CAPACITY: skills, staff, focal points",
                 "ACCOUNTABILITY: targets, reporting, incentives",
                 "CULTURE: norms &amp; leadership that live it"]},
         ]},

        {"type": "content", "label": "Policy", "title": "Start with an explicit gender policy",
         "blocks": [
             {"t": "bullets", "items": [
                 "A written <strong>gender policy</strong> with goals, not vague aspirations",
                 "Mandatory gender analysis built into project approval",
                 "Gender criteria in procurement, partnerships and grants",
                 "Senior leadership visibly accountable for it"]},
             {"t": "hbox", "color": "amber", "html": "A policy on the shelf changes nothing. It "
              "must be wired into the gateways &mdash; no gender analysis, no approval."},
         ]},

        {"type": "content", "label": "Capacity", "title": "Skills and people to make it real",
         "blocks": [
             {"t": "body", "html": "Mainstreaming demands capability across <em>all</em> staff, "
              "not just specialists. That means training, tools, time, and budget &mdash; and "
              "someone responsible for keeping gender on the agenda."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Build basic gender-analysis skills in every team",
                 "Provide checklists, frameworks and ready data tools",
                 "Fund the work &mdash; capacity without budget is a slogan",
                 "Recruit and retain women in technical and leadership roles"]},
         ]},

        {"type": "content", "label": "Gender Focal Points", "title": "The promise and trap of focal points",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "What they should do", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Champion, advise, build capacity and keep "
                   "gender visible &mdash; while the work stays everyone's responsibility."}]}],
              "right": [{"t": "panel", "color": "red", "title": "The trap", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Becoming the dumping ground &mdash; usually "
                   "a junior woman, given the title but no authority, time or budget, while others "
                   "opt out."}]}]},
             {"t": "hbox", "color": "amber", "html": "A focal point needs seniority, a mandate "
              "and resources &mdash; otherwise the role <em>de</em>-mainstreams gender by making "
              "it one person's burden."},
         ]},

        {"type": "content", "label": "Accountability", "title": "What gets measured gets done",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Gender targets in organisational and staff performance plans",
                 "Mandatory disaggregated reporting on every programme",
                 "Gender markers tracked across the whole portfolio",
                 "Consequences and incentives tied to gender results",
                 "Periodic gender audits of the organisation itself"]},
             {"t": "hbox", "color": "amber", "html": "Without accountability, mainstreaming "
              "relies on goodwill &mdash; and goodwill evaporates under deadline pressure."},
         ]},

        {"type": "content", "label": "Gender Audit", "title": "Holding the organisation to its own mirror",
         "blocks": [
             {"t": "term", "word": "Gender audit",
              "def": "A participatory self-assessment of how well an organisation has "
              "mainstreamed gender &mdash; in its policies, programmes, staffing, budget and "
              "culture &mdash; pioneered in the ILO's participatory model."},
             {"t": "body", "html": "An audit turns the gender lens inward. An NGO preaching "
              "equality with an all-male senior team and no childcare has an internal gap to "
              "close before it can credibly mainstream outward."},
         ]},

        {"type": "content", "label": "Culture", "title": "The hardest layer to change",
         "blocks": [
             {"t": "body", "html": "Policies and structures are the easy part. Organisational "
              "<strong>culture</strong> &mdash; whose ideas get heard, who gets promoted, whether "
              "meetings respect care responsibilities, whether harassment is tolerated &mdash; is "
              "where mainstreaming is truly tested."},
             {"t": "hbox", "color": "red", "html": "An organisation cannot transform gender "
              "relations in communities while reproducing them in its own corridors. Walk the "
              "talk, or the talk rings hollow."},
         ]},

        {"type": "content", "label": "Leadership", "title": "It rises or falls on leadership",
         "blocks": [
             {"t": "body", "html": "Where leaders own gender as core business &mdash; not a side "
              "issue delegated to a focal point &mdash; mainstreaming takes root. Where they "
              "treat it as compliance, it withers into reporting."},
             {"t": "quote",
              "text": "Mainstreaming is everyone's responsibility &mdash; which means leadership "
              "must make it no one's option to opt out.",
              "attr": "&mdash; a lesson from two decades of practice"},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Challenges &amp; Critiques"},

        {"type": "content", "label": "An Honest Reckoning", "title": "A good idea, unevenly delivered",
         "blocks": [
             {"t": "body", "html": "Three decades on, mainstreaming is near-universal in policy "
              "language and patchy in practice. Taking the critiques seriously is not betrayal of "
              "the agenda &mdash; it is how the agenda gets better."},
             {"t": "hbox", "color": "cyan", "html": "The recurring problem is not the concept but "
              "the gap between the rhetoric of mainstreaming and the reality of programmes."},
         ]},

        {"type": "content", "label": "Policy Evaporation", "title": "The classic critique: policy evaporation",
         "blocks": [
             {"t": "term", "word": "Policy evaporation",
              "def": "Coined by Sara Hlupekile Longwe: good gender-equality commitments made at "
              "the top 'evaporate' as they pass down through the bureaucracy, so little survives "
              "into actual implementation."},
             {"t": "hbox", "color": "red", "html": "Strong policy at headquarters; almost nothing "
              "on the ground. Longwe's image &mdash; commitment evaporating like water in heat "
              "&mdash; remains the sharpest indictment of weak mainstreaming."},
         ]},

        {"type": "content", "label": "Dilution", "title": "Tokenism and the checkbox",
         "blocks": [
             {"t": "body", "html": "When 'mainstreaming' becomes a box to tick &mdash; a "
              "paragraph in a proposal, a women's photo in a report, a quota met on paper &mdash; "
              "the form survives but the substance drains away."},
             {"t": "bullets", "sm": True, "color": "amber", "items": [
                 "Gender 'addressed' by one line in the logframe",
                 "A women's activity bolted on, core design untouched",
                 "Disaggregated data collected but never acted upon",
                 "'Gender' invoked, power never mentioned"]},
         ]},

        {"type": "content", "label": "Technical vs Transformative", "title": "The depoliticisation critique",
         "blocks": [
             {"t": "body", "html": "The deepest critique: mainstreaming has been turned into a "
              "<strong>technical</strong> exercise &mdash; tools, checklists, markers &mdash; "
              "that quietly strips out its <strong>political</strong> core. Gender equality is "
              "about power; bureaucratising it can defang it."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Technical (thin)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Apply the tool, count the women, file the "
                   "report. Comfortable, measurable &mdash; and toothless."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Transformative (thick)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Confront unequal power and challenge the "
                   "norms that hold it. Uncomfortable, contested &mdash; and the actual point."}]}]},
         ]},

        {"type": "content", "label": "Whose Agenda", "title": "Co-option and the loss of the feminist edge",
         "blocks": [
             {"t": "body", "html": "Critics note that as 'gender' entered mainstream institutions, "
              "it was sometimes drained of its feminist politics &mdash; 'gender' replacing "
              "'women', 'efficiency' replacing 'rights', the radical demand softened into "
              "managerial routine."},
             {"t": "hbox", "color": "red", "html": "The question to keep asking: is this "
              "mainstreaming changing power, or just making existing systems look gender-friendly "
              "while leaving them intact?"},
         ]},

        {"type": "content", "label": "Capacity Gaps", "title": "The practical failures on the ground",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Staff told to 'mainstream gender' with no training or tools",
                 "Gender work unfunded, unstaffed and unrewarded",
                 "Sex-disaggregated data missing, so gaps stay invisible",
                 "Focal points junior, overloaded and powerless",
                 "Leadership treating it as compliance, not commitment"]},
         ]},

        {"type": "content", "label": "The Backlash", "title": "Resistance is real &mdash; and rising",
         "blocks": [
             {"t": "body", "html": "Mainstreaming faces open and quiet resistance: 'gender is "
              "Western', 'our women are content', 'this divides the family'. At household level, "
              "women's gains can trigger backlash; at policy level, hard-won space can be rolled "
              "back."},
             {"t": "hbox", "color": "amber", "html": "Resistance is a sign the work is touching "
              "real power &mdash; not a reason to retreat. But it must be anticipated, navigated "
              "and managed, not wished away."},
         ]},

        {"type": "content", "label": "Holding the Line", "title": "Keeping mainstreaming honest",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Keep <strong>power</strong> in the frame &mdash; not just tools and counts",
                 "Resource and staff the work properly, or admit it is rhetoric",
                 "Track outcomes for women, not just activities done",
                 "Keep women's movements and feminist analysis at the centre",
                 "Treat critique as course-correction, not as the enemy"]},
             {"t": "hbox", "color": "cyan", "html": "The goal was never the tool. The goal is a "
              "fairer distribution of power. Keep the tool in service of the goal."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "The India Context &amp; Practice"},

        {"type": "content", "label": "The Architecture", "title": "India's gender-equality machinery",
         "blocks": [
             {"t": "body", "html": "India mainstreams gender through a dense institutional fabric "
              "&mdash; constitutional guarantees, a dedicated ministry, the gender budget, "
              "schemes and reservations &mdash; even as outcomes remain deeply uneven."},
             {"t": "bullets", "sm": True, "color": "indigo", "items": [
                 "Constitutional equality (Arts. 14, 15, 15(3), 16) &amp; directive principles",
                 "Ministry of Women &amp; Child Development at the centre",
                 "Gender Budget Statement since 2005&ndash;06",
                 "73rd / 74th Amendments: one-third reservation in local bodies"]},
         ]},

        {"type": "content", "label": "Schemes", "title": "Mainstreaming through flagship schemes",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Scheme / measure", "What it targets", "Track"],
              "rows": [
                  ["Beti Bachao Beti Padhao", "Child sex ratio, girls' education", "Targeted"],
                  ["DAY-NRLM / SHGs", "Women's collectives &amp; livelihoods", "Targeted"],
                  ["MGNREGA (33% for women)", "Wage work with gender quota", "Mainstream + quota"],
                  ["PM Ujjwala (LPG)", "Reducing women's fuel burden", "Practical needs"],
                  ["Maternity benefits", "Income support around childbirth", "Targeted"]]},
             {"t": "hbox", "color": "amber", "html": "Note the mix: some ease practical needs "
              "(fuel, wages), some build agency (SHGs). The gap is usually in strategic needs "
              "&mdash; land, voice, safety."},
         ]},

        {"type": "content", "label": "Law &amp; Reform", "title": "NEP, labour codes and recent shifts",
         "blocks": [
             {"t": "body", "html": "Mainstreaming shows up in major reforms &mdash; the "
              "<strong>National Education Policy 2020</strong> includes a Gender Inclusion Fund; "
              "the consolidated <strong>labour codes</strong> address maternity, equal "
              "remuneration and (contested) provisions on women's night work."},
             {"t": "hbox", "color": "red", "html": "The test of every reform: does it shift "
              "women's <em>position</em>, or only adjust their <em>condition</em> &mdash; and who "
              "was at the table when it was drafted?"},
         ]},

        {"type": "content", "label": "The Sharpest Gap", "title": "The women's workforce puzzle",
         "blocks": [
             {"t": "body", "html": "India's most-discussed gender gap is women's low and long-"
              "stagnant labour-force participation &mdash; with a recent reported uptick driven "
              "largely by rural self-employment. PLFS now tracks this annually."},
             {"t": "chart", "canvas": "gmLfprChart",
              "title": "The gender gap in labour-force participation (illustrative shape)",
              "source": "Illustrative &mdash; pattern only, not exact PLFS figures",
              "type": "bar",
              "data": {"labels": ["Period 1", "Period 2", "Period 3", "Period 4"],
                       "datasets": [
                           {"label": "Women", "data": [24, 26, 30, 33], "backgroundColor": "#EF4444"},
                           {"label": "Men", "data": [76, 76, 77, 78], "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ scales:{ y:{min:0,max:100,title:{display:true,text:'LFPR %'}} } }"}},
         ]},

        {"type": "content", "label": "Local Practice", "title": "Mainstreaming in the panchayat",
         "blocks": [
             {"t": "body", "html": "The 73rd Amendment's one-third (now half, in many states) "
              "reservation put over a million women into local government &mdash; the world's "
              "largest experiment in women's political representation, with real and contested "
              "results."},
             {"t": "hbox", "color": "amber", "html": "Watch for the <em>sarpanch pati</em> "
              "problem &mdash; husbands ruling in their elected wives' names. A seat is access; "
              "real decision-making is control. The gap recurs."},
         ]},

        {"type": "content", "label": "A Practitioner Checklist", "title": "Twelve questions for your next programme",
         "compact": True,
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Do I have sex-disaggregated baseline data?",
                 "Have I run the four questions &mdash; does, has, decides, benefits?",
                 "Did I separate practical from strategic needs?",
                 "Does the design touch control, not just access?",
                 "Are gender objectives explicit, with indicators and budget?",
                 "Will delivery actually reach women (time, place, staff)?",
                 "Have I engaged men to reduce backlash?",
                 "Is there a do-no-harm / GBV pathway?",
                 "Will I disaggregate every result?",
                 "Is gender someone senior's accountability, not a junior's burden?",
                 "Am I running both tracks &mdash; mainstream and targeted?",
                 "Am I changing power, or just ticking a box?"]},
         ]},

        {"type": "content", "label": "Further Reading", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Caroline Moser, <em>Gender Planning and Development</em> (1993) &mdash; triple "
                 "role, practical vs strategic needs",
                 "Naila Kabeer, <em>Reversed Realities</em> (1994) &amp; the Social Relations "
                 "Approach &mdash; empowerment and institutions",
                 "Beijing Platform for Action (1995) &amp; UN ECOSOC Agreed Conclusions (1997)",
                 "Sara Longwe on 'policy evaporation' &mdash; the enduring critique",
                 "UN Women, OECD-DAC &amp; ILO gender-audit and gender-marker toolkits"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Care Economy</strong>, <strong>Women's Economic Empowerment</strong> and "
              "<strong>Data Feminism</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Gender is everywhere</strong> &mdash; mainstreaming, not an add-on",
                 "<strong>Access is not control</strong> &mdash; aim for both",
                 "<strong>Practical eases life; strategic shifts power</strong> &mdash; do both",
                 "<strong>Run both tracks</strong> &mdash; mainstream <em>and</em> target",
                 "<strong>Keep power in the frame</strong> &mdash; or it evaporates into a checkbox"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Gender Mainstreaming 101 &middot; Complete",
         "headline": "Now make gender<br>everybody's business.",
         "byline": "Mainstreaming is not a checkbox or a separate project &mdash; it is asking, "
                   "at every stage and every level, who does what, who decides, and who benefits. "
                   "Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
