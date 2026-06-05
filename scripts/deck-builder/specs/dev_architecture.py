# -*- coding: utf-8 -*-
"""
Global Development Governance 101 — ImpactMojo 101 Series (native deck spec)
The actors, rules and money of the global aid architecture, for South Asian
development practitioners.
Build: python3 scripts/deck-builder/build.py dev_architecture
"""

DECK = {
    "slug": "dev-architecture",
    "title": "Global Development Governance 101",
    "description": ("Global Development Governance 101 — a free foundational course for "
                    "development practitioners in South Asia. Understand the global aid "
                    "architecture: the UN system, the World Bank and IMF, ODA and the OECD-DAC, "
                    "the SDGs, financing for development, new actors, aid effectiveness, the "
                    "critiques of aid, and India's shift from recipient to donor. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Global<br>Development<br>Governance 101",
         "sub": "The Actors, Rules &amp; Money of the Global Aid Architecture &mdash; a "
                "Foundational Course for Development Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "The Aid Architecture", "slides": "auto"},
             {"name": "A Short History", "slides": "auto"},
             {"name": "The UN Development System", "slides": "auto"},
             {"name": "The Financial Institutions", "slides": "auto"},
             {"name": "Bilateral &amp; Multilateral Aid", "slides": "auto"},
             {"name": "The SDGs &amp; 2030 Agenda", "slides": "auto"},
             {"name": "Financing for Development", "slides": "auto"},
             {"name": "New &amp; Shifting Actors", "slides": "auto"},
             {"name": "Aid Effectiveness &amp; Localisation", "slides": "auto"},
             {"name": "Critiques &amp; Power", "slides": "auto"},
             {"name": "India in the System", "slides": "auto"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "The Aid Architecture"},

        {"type": "content", "label": "Definition", "title": "What 'development governance' means",
         "blocks": [
             {"t": "body", "html": "Every grant, loan, target and treaty that shapes development "
              "flows through a vast, layered system of institutions. <strong>Global development "
              "governance</strong> is the ecosystem of actors, rules and money that decides who "
              "gets resources, on what terms, to do what."},
             {"t": "term", "word": "Aid architecture",
              "def": "The web of organisations, agreements, funding channels and norms through "
              "which development assistance is decided, delivered and accounted for &mdash; from "
              "the UN and the World Bank down to a single project in a single district."},
             {"t": "hbox", "color": "cyan", "html": "You do not need to run these institutions. "
              "You need to know who holds the money, who makes the rules, and where your work "
              "sits in the chain."},
         ]},

        {"type": "content", "label": "Three Things", "title": "Actors, rules and money",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Actors", "label": "UN agencies, banks, donor governments, NGOs, "
                  "foundations, the private sector", "color": "cyan"},
                 {"num": "Rules", "label": "Treaties, declarations, conditionalities, reporting "
                  "standards, the SDGs", "color": "green"},
                 {"num": "Money", "label": "Grants, concessional loans, equity, philanthropy, "
                  "domestic taxes", "color": "amber"}]},
             {"t": "hbox", "color": "indigo", "html": "Follow any development outcome backwards "
              "and you pass through all three. They rarely pull in the same direction."},
         ]},

        {"type": "content", "label": "Who's Who", "title": "The main families of actors",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Family", "Examples", "Primary role"],
              "rows": [
                  ["UN system", "UNDP, UNICEF, WHO, UN Women, FAO", "Norms, technical support, grants"],
                  ["IFIs", "World Bank, IMF, ADB, AIIB", "Loans, finance, policy advice"],
                  ["Bilateral donors", "USAID, FCDO, JICA, GIZ", "Country-to-country aid"],
                  ["Philanthropy", "Gates, Ford, Rockefeller", "Private grants, agenda-setting"],
                  ["Civil society", "INGOs, NGOs, networks", "Delivery, advocacy, accountability"],
                  ["Recipient states", "Governments &amp; ministries", "Set priorities, deliver, report"]]},
             {"t": "hbox", "color": "amber", "html": "Learn these six families by name. Almost "
              "every development dollar passes through one or more of them."},
         ]},

        {"type": "content", "label": "How Money Moves", "title": "The funding chain, simplified",
         "blocks": [
             {"t": "flow", "steps": [
                 "SOURCE: taxpayers, donors, lenders, foundations",
                 "CHANNEL: UN agency, bank, bilateral agency",
                 "INTERMEDIARY: government, INGO, contractor",
                 "DELIVERY: project, programme, community"]},
             {"t": "hbox", "color": "green", "html": "Every link takes a cut, adds a rule, and "
              "loses a little of the original intent. The longer the chain, the less of each "
              "rupee reaches the ground &mdash; and the harder it is to trace."},
         ]},

        {"type": "content", "label": "Grants vs Loans", "title": "Not all 'aid' is a gift",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Grants", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Money given that need not be repaid. The "
                   "purest form of aid &mdash; but a small and shrinking share of total flows."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Loans", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Money lent, to be repaid &mdash; often at "
                   "below-market 'concessional' rates. Most development finance is debt, not gift."}]}]},
             {"t": "hbox", "color": "red", "html": "A loan still counts as 'aid' in many ledgers. "
              "Always ask whether a flow is a grant or a debt the country must one day repay."},
         ]},

        {"type": "content", "label": "Scale", "title": "How big is the system?",
         "blocks": [
             {"t": "body", "html": "Official development assistance (ODA) from the wealthy donor "
              "club runs into the <strong>hundreds of billions of dollars a year</strong> "
              "&mdash; large in absolute terms, yet small next to global trade, remittances or "
              "what developing countries raise in their own taxes."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Hundreds of $bn/yr", "label": "ODA from OECD-DAC donors (order of "
                  "magnitude)", "color": "cyan", "source": "OECD-DAC, qualitative"},
                 {"num": "&lt; tax &amp; remittances", "label": "Aid is dwarfed by domestic "
                  "revenue and money migrants send home", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Aid is influential out of proportion to its "
              "size &mdash; it sets norms and unlocks other money &mdash; but it is never the "
              "main resource for development."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "Why a practitioner should care",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Your funder sits inside this system</strong> &mdash; its rules become "
                 "your rules",
                 "<strong>Targets cascade down</strong> &mdash; the SDGs end up in your logframe",
                 "<strong>Power is unequal</strong> &mdash; knowing who decides helps you "
                 "advocate",
                 "<strong>The system is shifting</strong> &mdash; new donors and debt change "
                 "what is possible"]},
             {"t": "hbox", "color": "cyan", "html": "This course maps the architecture so you can "
              "navigate it &mdash; and question it &mdash; rather than simply receive its "
              "instructions."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "A Short History"},

        {"type": "content", "label": "Origins", "title": "Bretton Woods, 1944",
         "blocks": [
             {"t": "body", "html": "In July 1944, with the Second World War still raging, "
              "delegates from 44 nations met at <strong>Bretton Woods</strong>, New Hampshire, to "
              "design the post-war economic order. They created two institutions that still "
              "dominate development finance."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "IMF", "label": "International Monetary Fund &mdash; monetary stability "
                  "&amp; balance-of-payments support", "color": "cyan", "source": "Founded 1944"},
                 {"num": "World Bank", "label": "Originally to rebuild Europe, then to finance "
                  "development", "color": "green", "source": "Founded 1944"}]},
             {"t": "hbox", "color": "amber", "html": "The system was designed by the victors of "
              "1945 &mdash; a fact that still shapes who holds the votes today."},
         ]},

        {"type": "content", "label": "Decolonisation", "title": "Independence remakes the map",
         "blocks": [
             {"t": "body", "html": "From the late 1940s, dozens of nations &mdash; India in 1947, "
              "then much of Asia and Africa &mdash; won independence. A world of empires became a "
              "world of <strong>sovereign developing states</strong>, each needing to build an "
              "economy and a public sector almost from scratch."},
             {"t": "hbox", "color": "cyan", "html": "'Development' as an international project was "
              "born here: newly independent nations seeking to catch up, and former colonial "
              "powers offering 'assistance' &mdash; with mixed motives."},
         ]},

        {"type": "content", "label": "The UN", "title": "A forum for all nations, 1945",
         "blocks": [
             {"t": "body", "html": "The <strong>United Nations</strong>, founded in 1945, gave "
              "every state &mdash; large or small, rich or poor &mdash; a seat in the General "
              "Assembly. Over time it grew a sprawling family of agencies to tackle health, "
              "children, food, labour and development."},
             {"t": "hbox", "color": "indigo", "html": "Note the tension built in from the start: "
              "the General Assembly is one-nation-one-vote, but the financial institutions are "
              "one-dollar-one-vote. Two very different ideas of fairness."},
         ]},

        {"type": "content", "label": "Cold War Aid", "title": "Aid as a weapon, 1947&ndash;1991",
         "blocks": [
             {"t": "body", "html": "For four decades, much aid was an instrument of "
              "superpower rivalry. Washington and Moscow funded dams, factories and armies to "
              "win allies. The Marshall Plan rebuilt Europe; later, aid flowed to keep nations "
              "inside one camp or the other."},
             {"t": "hbox", "color": "red", "html": "A lasting lesson: aid has rarely been "
              "charity alone. Strategic interest &mdash; security, trade, influence &mdash; has "
              "always shaped where the money goes."},
         ]},

        {"type": "content", "label": "The Turn", "title": "The Washington Consensus, 1980s&ndash;90s",
         "blocks": [
             {"t": "body", "html": "By the 1980s a new orthodoxy took hold: the "
              "<strong>Washington Consensus</strong>. Loans came with conditions &mdash; cut "
              "deficits, privatise, deregulate, open to trade. 'Structural adjustment' reshaped "
              "economies across the Global South."},
             {"t": "bullets", "sm": True, "color": "amber", "items": [
                 "Fiscal discipline and reduced public spending",
                 "Privatisation of state enterprises",
                 "Trade and financial liberalisation",
                 "Deregulation and secure property rights"]},
             {"t": "hbox", "color": "red", "html": "The results were bitterly contested: growth "
              "in some places, austerity, lost services and a 'lost decade' in others."},
         ]},

        {"type": "content", "label": "Course Correction", "title": "From adjustment to goals",
         "blocks": [
             {"t": "body", "html": "Backlash against structural adjustment pushed the system "
              "toward an explicit focus on <strong>poverty</strong> and measurable human "
              "outcomes. The result, in 2000, was a shared global scorecard: the Millennium "
              "Development Goals."},
             {"t": "flow", "steps": [
                 "1980s&ndash;90s: structural adjustment &amp; conditionality",
                 "Late 1990s: debt relief &amp; poverty focus",
                 "2000: Millennium Development Goals (MDGs)",
                 "2015: Sustainable Development Goals (SDGs)"]},
         ]},

        {"type": "content", "label": "MDGs to SDGs", "title": "From 8 goals to 17",
         "blocks": [
             {"t": "chart", "canvas": "mdgSdgChart",
              "title": "Goal count: MDGs (2000&ndash;2015) vs SDGs (2015&ndash;2030)",
              "source": "United Nations",
              "type": "bar",
              "data": {"labels": ["MDGs (8 goals)", "SDGs (17 goals)"],
                       "datasets": [{"label": "Number of goals",
                                     "data": [8, 17],
                                     "backgroundColor": ["#0EA5E9", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:20, title:{display:true,text:'Goals'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The MDGs (2000&ndash;2015) had 8 goals "
              "aimed mainly at poor countries. The SDGs (2015&ndash;2030) have 17 goals and "
              "<strong>169 targets</strong> &mdash; and apply to every nation, rich and poor."},
         ]},

        {"type": "content", "label": "The Pattern", "title": "Each era left a residue",
         "blocks": [
             {"t": "body", "html": "Today's architecture is a sediment of every past era: "
              "Bretton Woods institutions, a post-colonial donor relationship, Cold War "
              "habits, market orthodoxy, and a goals-based global agenda &mdash; all layered on "
              "top of one another."},
             {"t": "hbox", "color": "amber", "html": "Nothing in this system is natural or "
              "inevitable. Each rule was made by someone, for a reason, at a moment in history "
              "&mdash; and can be remade."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The UN Development System"},

        {"type": "content", "label": "The Family", "title": "A federation, not a single body",
         "blocks": [
             {"t": "body", "html": "The 'UN' is not one organisation but a <strong>family of "
              "agencies</strong>, funds and programmes, each with its own mandate, budget and "
              "governing board. They cooperate &mdash; and sometimes compete &mdash; under the "
              "broad UN umbrella."},
             {"t": "hbox", "color": "cyan", "html": "When someone says 'the UN is doing X', ask "
              "<em>which</em> UN body. UNDP, UNICEF and WHO are as different from one another as "
              "separate ministries."},
         ]},

        {"type": "content", "label": "Who Does What", "title": "The major development agencies",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Agency", "Focus", "Note"],
              "rows": [
                  ["UNDP", "Development coordination, governance, poverty", "Hosts the HDI &amp; resident coordinators"],
                  ["UNICEF", "Children &mdash; health, nutrition, education", "Large field presence, own fundraising"],
                  ["WHO", "Global health &amp; disease", "Sets health norms &amp; standards"],
                  ["UN Women", "Gender equality &amp; women's rights", "Newest of the big agencies (2010)"],
                  ["FAO", "Food, agriculture &amp; rural livelihoods", "Rome-based, with WFP &amp; IFAD"]]},
             {"t": "hbox", "color": "amber", "html": "Each agency competes for the same donor "
              "money &mdash; which both drives energy and fuels duplication."},
         ]},

        {"type": "content", "label": "Governance", "title": "The General Assembly vs the agencies",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "General Assembly", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Every member state, one vote. Sets broad "
                   "agendas and adopts declarations &mdash; but cannot compel."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Agency boards", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Each agency has its own executive board of "
                   "member states that approves its budget and programmes."}]}]},
             {"t": "hbox", "color": "amber", "html": "Power is diffuse. No single body commands "
              "the UN development system; it is steered by many hands, often pulling differently."},
         ]},

        {"type": "content", "label": "The Money", "title": "Core vs earmarked funding",
         "blocks": [
             {"t": "term", "word": "Core (unearmarked) funding",
              "def": "Flexible money agencies can allocate to their own priorities. Predictable "
              "and strategic &mdash; but a shrinking share of the total."},
             {"t": "term", "word": "Earmarked (non-core) funding",
              "def": "Money tied by the donor to a specific country, theme or project. The agency "
              "becomes, in effect, a contractor delivering the donor's choices."},
         ]},

        {"type": "content", "label": "The Squeeze", "title": "Earmarking is taking over",
         "blocks": [
             {"t": "chart", "canvas": "coreEarmarkChart",
              "title": "Illustrative shift from core to earmarked UN funding",
              "source": "Illustrative, patterned on UN funding trends",
              "type": "bar",
              "data": {"labels": ["Earlier", "Recent"],
                       "datasets": [
                           {"label": "Core %", "data": [40, 20], "backgroundColor": "#10B981"},
                           {"label": "Earmarked %", "data": [60, 80], "backgroundColor": "#F59E0B"}]},
              "options": {"__js__": "{ plugins:{legend:{display:true}}, scales:{ x:{stacked:true}, y:{stacked:true, min:0, max:100, title:{display:true,text:'% of funding'}} } }"}},
             {"t": "hbox", "color": "red", "html": "As earmarking grows, agencies lose room to "
              "fund the unglamorous, the long-term and the politically awkward. Donors gain "
              "control; agencies lose strategy. (Shares above are illustrative.)"},
         ]},

        {"type": "content", "label": "On the Ground", "title": "How the UN shows up in a country",
         "blocks": [
             {"t": "flow", "steps": [
                 "RESIDENT COORDINATOR leads the UN country team",
                 "COUNTRY FRAMEWORK agreed with the government",
                 "AGENCIES deliver programmes in their mandates",
                 "PARTNERS: ministries, NGOs, communities"]},
             {"t": "hbox", "color": "cyan", "html": "For a practitioner, the UN is most visible "
              "as a convenor and a source of grants, technical guidance and global norms &mdash; "
              "less often as a direct funder of frontline delivery."},
         ]},

        {"type": "content", "label": "Strengths", "title": "What the UN system does well",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Legitimacy:</strong> nearly every nation is a member",
                 "<strong>Norm-setting:</strong> conventions on rights, health, children, women",
                 "<strong>Convening:</strong> brings rivals to one table",
                 "<strong>Neutral-ish technical advice</strong> not tied to one donor's interest"]},
         ]},

        {"type": "content", "label": "Limits", "title": "What the UN system struggles with",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Underfunded core budgets</strong> and reliance on earmarking",
                 "<strong>Fragmentation</strong> across dozens of overlapping agencies",
                 "<strong>Slow, consensus-bound</strong> decision-making",
                 "<strong>Limited enforcement</strong> &mdash; it can recommend, rarely compel"]},
             {"t": "hbox", "color": "amber", "html": "Its strength &mdash; including everyone "
              "&mdash; is also its weakness: consensus is slow, and no one is fully in charge."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "The Financial Institutions"},

        {"type": "content", "label": "The IFIs", "title": "Banks that lend for development",
         "blocks": [
             {"t": "body", "html": "The <strong>International Financial Institutions (IFIs)</strong> "
              "are the heavyweights of development finance. Unlike UN agencies, they lend at "
              "scale, attach policy conditions, and shape national economic decisions."},
             {"t": "hbox", "color": "cyan", "html": "Where the UN sets norms, the IFIs move "
              "money &mdash; and money, with conditions attached, is leverage."},
         ]},

        {"type": "content", "label": "World Bank Group", "title": "Five institutions under one roof",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Arm", "What it does", "Clients"],
              "rows": [
                  ["IBRD", "Loans to middle-income governments", "Creditworthy states"],
                  ["IDA", "Grants &amp; cheap loans to the poorest", "Low-income states"],
                  ["IFC", "Invests in the private sector", "Companies"],
                  ["MIGA", "Political-risk guarantees", "Investors"],
                  ["ICSID", "Settles investment disputes", "States &amp; investors"]]},
             {"t": "hbox", "color": "amber", "html": "For South Asia, <strong>IDA</strong> "
              "(concessional finance for the poorest) and <strong>IBRD</strong> matter most. "
              "India has been one of the largest IDA borrowers in history."},
         ]},

        {"type": "content", "label": "The IMF", "title": "Lender of last resort",
         "blocks": [
             {"t": "body", "html": "The <strong>IMF</strong> is not primarily a development bank. "
              "It lends to countries in <strong>balance-of-payments crisis</strong> &mdash; when "
              "they cannot pay for imports or service debt &mdash; in exchange for policy "
              "reforms."},
             {"t": "hbox", "color": "red", "html": "IMF programmes are powerful and "
              "controversial: they can stabilise a currency, but their austerity conditions have "
              "repeatedly squeezed public spending on health, food and jobs."},
         ]},

        {"type": "content", "label": "Regional Banks", "title": "ADB, AIIB and the NDB",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "ADB", "label": "Asian Development Bank (1966), Manila &mdash; "
                  "Japan/US-led", "color": "cyan"},
                 {"num": "AIIB", "label": "Asian Infrastructure Investment Bank (2016), Beijing "
                  "&mdash; China-led", "color": "amber"},
                 {"num": "NDB", "label": "New Development Bank (2015) &mdash; the BRICS bank, "
                  "Shanghai", "color": "indigo"}]},
             {"t": "hbox", "color": "green", "html": "The AIIB and NDB are recent additions, "
              "launched partly because emerging economies wanted alternatives to "
              "Western-dominated institutions. The architecture is no longer monopolised."},
         ]},

        {"type": "content", "label": "Who Decides", "title": "One dollar, one vote",
         "blocks": [
             {"t": "body", "html": "Unlike the UN General Assembly, the World Bank and IMF "
              "allocate votes by <strong>financial shareholding</strong>. The more capital you "
              "contribute, the more votes you hold &mdash; so the richest nations decide."},
             {"t": "chart", "canvas": "wbVoteChart",
              "title": "Illustrative World Bank (IBRD) voting-share distribution",
              "source": "Illustrative, patterned on World Bank shareholding",
              "type": "doughnut",
              "data": {"labels": ["United States", "Japan", "China", "Germany", "Other members"],
                       "datasets": [{"data": [16, 7, 6, 4, 67],
                                     "backgroundColor": ["#0EA5E9", "#10B981", "#F59E0B", "#6366F1", "#94A3B8"]}]},
              "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
             {"t": "hbox", "color": "red", "html": "The US has historically held a large enough "
              "share to veto major changes single-handedly. (Shares above are illustrative.)"},
         ]},

        {"type": "content", "label": "The Convention", "title": "An unwritten leadership pact",
         "blocks": [
             {"t": "body", "html": "By long-standing convention, the World Bank's president is an "
              "American and the IMF's managing director a European. No developing-country "
              "national has ever led either institution."},
             {"t": "hbox", "color": "amber", "html": "This is not written in any statute &mdash; "
              "it is a power arrangement from 1944 that has simply never been broken. A recurring "
              "demand of the Global South is to end it."},
         ]},

        {"type": "content", "label": "Conditionality", "title": "Money with strings",
         "blocks": [
             {"t": "term", "word": "Conditionality",
              "def": "The policy conditions attached to a loan &mdash; for example, cutting "
              "subsidies, raising tariffs, or reforming a sector &mdash; that a borrowing "
              "government must meet to receive or keep the money."},
             {"t": "hbox", "color": "red", "html": "Conditionality is where finance becomes "
              "politics. It can push useful reform &mdash; or override democratic choices made by "
              "the borrowing country's own citizens."},
         ]},

        {"type": "content", "label": "Reform Debate", "title": "Calls to rebalance the IFIs",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Re-weight votes</strong> toward emerging and developing economies",
                 "<strong>Open leadership</strong> to nationals of any country",
                 "<strong>Lend more, on softer terms</strong> for climate and development",
                 "<strong>Lighten conditionality</strong> and respect country ownership"]},
             {"t": "hbox", "color": "cyan", "html": "Reform is slow precisely because those who "
              "hold the votes must agree to dilute their own power."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Bilateral &amp; Multilateral Aid"},

        {"type": "content", "label": "Two Channels", "title": "Bilateral vs multilateral aid",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Bilateral", "blocks": [
                  {"t": "body", "cls": "sm", "html": "One government gives directly to another "
                   "&mdash; e.g. Japan's JICA, the UK's FCDO, Germany's GIZ. Donor keeps the most "
                   "control and visibility."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Multilateral", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Many governments pool funds through an "
                   "institution &mdash; the UN, World Bank, Global Fund &mdash; which decides "
                   "allocation. More neutral, less donor control."}]}]},
             {"t": "hbox", "color": "amber", "html": "Donors balance the two: bilateral for "
              "visibility and influence, multilateral for reach and shared burden."},
         ]},

        {"type": "content", "label": "The Donor Club", "title": "The OECD-DAC",
         "blocks": [
             {"t": "body", "html": "The <strong>Development Assistance Committee (DAC)</strong> of "
              "the OECD is the club of traditional Western donors. It defines what counts as aid, "
              "collects the statistics, and reviews members' performance."},
             {"t": "hbox", "color": "cyan", "html": "When you read 'global aid totals', they "
              "usually mean DAC members' ODA. Major donors like China are <em>not</em> in the "
              "DAC &mdash; so a lot of real flows sit outside the headline numbers."},
         ]},

        {"type": "content", "label": "The Definition", "title": "What counts as ODA?",
         "blocks": [
             {"t": "term", "word": "Official Development Assistance (ODA)",
              "def": "Government aid that promotes the economic development and welfare of "
              "developing countries. To count, a flow must be official, concessional (with a "
              "grant element), and developmental in purpose."},
             {"t": "hbox", "color": "red", "html": "The definition is contested. Donors have "
              "counted refugee costs at home, debt relief and security spending as 'aid' &mdash; "
              "inflating totals without a dollar reaching a developing country."},
         ]},

        {"type": "content", "label": "The Benchmark", "title": "The 0.7% target",
         "blocks": [
             {"t": "body", "html": "In 1970 the UN General Assembly set a target: wealthy nations "
              "should give <strong>0.7% of their gross national income (GNI)</strong> as ODA. "
              "More than fifty years on, most donors have never reached it."},
             {"t": "chart", "canvas": "odaTargetChart",
              "title": "ODA as % of GNI vs the 0.7% UN target (illustrative donors)",
              "source": "0.7% target is the real UN goal (1970); donor values illustrative",
              "type": "bar",
              "data": {"labels": ["Donor A", "Donor B", "Donor C", "Donor D", "DAC average"],
                       "datasets": [{"label": "ODA % of GNI",
                                     "data": [0.9, 0.7, 0.5, 0.3, 0.37],
                                     "backgroundColor": ["#10B981", "#10B981", "#F59E0B", "#EF4444", "#6366F1"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}, annotation:{}}, scales:{ y:{min:0, max:1.1, title:{display:true,text:'% of GNI'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "The 0.7% line is the real, agreed "
              "benchmark. Only a handful of countries consistently meet it; the DAC average sits "
              "well below. (Individual donor bars above are illustrative.)"},
         ]},

        {"type": "content", "label": "Grants vs Loans", "title": "Concessional loans count too",
         "blocks": [
             {"t": "body", "html": "ODA includes both grants and <strong>concessional "
              "loans</strong> &mdash; loans at softer-than-market terms. A loan's 'grant element' "
              "is the discount it carries versus a commercial loan."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Grant", "label": "100% grant element &mdash; nothing to repay", "color": "green"},
                 {"num": "Concessional loan", "label": "Part gift, part debt &mdash; only the "
                  "gift part is 'aid'", "color": "amber"}]},
             {"t": "hbox", "color": "red", "html": "Counting a whole loan as aid overstates "
              "generosity. Modern rules count only the grant equivalent &mdash; but the borrower "
              "still repays the rest."},
         ]},

        {"type": "content", "label": "Tied Aid", "title": "Aid that must be spent at home",
         "blocks": [
             {"t": "term", "word": "Tied aid",
              "def": "Aid that the recipient must spend on goods, services or contractors from "
              "the donor country &mdash; rather than buying the best value anywhere."},
             {"t": "hbox", "color": "red", "html": "Tying aid can return a large share of the "
              "money to the donor's own firms and consultants, and raises costs for the "
              "recipient. The DAC discourages it &mdash; but it persists in many forms."},
         ]},

        {"type": "content", "label": "Where It Goes", "title": "Aid is unevenly distributed",
         "blocks": [
             {"t": "chart", "canvas": "aidRegionChart",
              "title": "Illustrative shares of bilateral ODA by recipient region",
              "source": "Illustrative",
              "type": "doughnut",
              "data": {"labels": ["Sub-Saharan Africa", "Asia", "Middle East &amp; N. Africa", "Latin America", "Other"],
                       "datasets": [{"data": [35, 28, 18, 9, 10],
                                     "backgroundColor": ["#0EA5E9", "#10B981", "#F59E0B", "#6366F1", "#94A3B8"]}]},
              "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
             {"t": "hbox", "color": "amber", "html": "Allocation follows need <em>and</em> "
              "interest &mdash; geopolitics, history and security all tilt the map. (Shares above "
              "are illustrative.)"},
         ]},

        {"type": "content", "label": "Reading Aid Data", "title": "Questions for any aid figure",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Is it grant or loan &mdash; and net of repayments?",
                 "Is it committed (promised) or disbursed (actually paid)?",
                 "Does it include items that never reach the recipient?",
                 "Is it bilateral or channelled through a multilateral?"]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "The SDGs &amp; 2030 Agenda"},

        {"type": "content", "label": "The Agenda", "title": "Agenda 2030, adopted 2015",
         "blocks": [
             {"t": "body", "html": "In September 2015, all UN member states adopted "
              "<strong>Transforming Our World: the 2030 Agenda for Sustainable Development</strong> "
              "&mdash; a shared plan built around 17 Sustainable Development Goals."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "17", "label": "Sustainable Development Goals", "color": "cyan",
                  "source": "UN, 2015"},
                 {"num": "169", "label": "targets beneath the goals", "color": "green"},
                 {"num": "2030", "label": "the deadline", "color": "amber"}]},
         ]},

        {"type": "content", "label": "From the MDGs", "title": "What changed from the MDGs",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "MDGs (2000&ndash;15)", "SDGs (2015&ndash;30)"],
              "rows": [
                  ["Goals", "8", "17"],
                  ["Applies to", "Mainly poor countries", "Every country, universally"],
                  ["Origin", "Drafted by experts", "Negotiated by all states"],
                  ["Scope", "Poverty, health, education", "Adds climate, inequality, justice, jobs"],
                  ["Environment", "One goal", "Woven throughout"]]},
             {"t": "hbox", "color": "cyan", "html": "The biggest shift is "
              "<strong>universality</strong>: the SDGs ask Norway and Nepal alike to act &mdash; "
              "development is no longer something rich countries 'do to' poor ones."},
         ]},

        {"type": "content", "label": "The Promise", "title": "'Leave no one behind'",
         "blocks": [
             {"t": "body", "html": "The 2030 Agenda's central pledge is to <strong>leave no one "
              "behind</strong> &mdash; to reach the poorest and most marginalised first, not "
              "just to lift national averages."},
             {"t": "hbox", "color": "green", "html": "This is a direct response to the MDG-era "
              "lesson that you can hit a national target while entirely missing the people "
              "furthest from the mean. Averages can hide the abandoned."},
         ]},

        {"type": "content", "label": "Universality", "title": "Every country has homework",
         "blocks": [
             {"t": "body", "html": "Because the goals are universal, every country &mdash; rich "
              "or poor &mdash; reports its progress through <strong>Voluntary National Reviews "
              "(VNRs)</strong> at the UN. Sweden has SDG gaps too: inequality, consumption, "
              "emissions."},
             {"t": "hbox", "color": "indigo", "html": "Universality is powerful rhetoric and "
              "weak enforcement: reviews are voluntary, and no one is penalised for missing a "
              "target."},
         ]},

        {"type": "content", "label": "Measuring It", "title": "The data challenge",
         "blocks": [
             {"t": "body", "html": "169 targets need hundreds of <strong>indicators</strong> "
              "&mdash; and for many of them, especially in the poorest countries, the data simply "
              "does not exist, is out of date, or cannot be disaggregated by group."},
             {"t": "chart", "canvas": "sdgDataChart",
              "title": "Illustrative: share of SDG indicators with usable data",
              "source": "Illustrative, patterned on UN SDG data-gap discussions",
              "type": "doughnut",
              "data": {"labels": ["Good data", "Partial / outdated", "Little or no data"],
                       "datasets": [{"data": [45, 30, 25],
                                     "backgroundColor": ["#10B981", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
             {"t": "hbox", "color": "red", "html": "You cannot leave no one behind if you cannot "
              "count them. The data gap is a justice problem, not just a technical one. "
              "(Shares above are illustrative.)"},
         ]},

        {"type": "content", "label": "Interlinked", "title": "The goals pull on each other",
         "blocks": [
             {"t": "body", "html": "The 17 goals are not a menu to pick from; they are a system. "
              "Progress on one can drive &mdash; or undermine &mdash; another."},
             {"t": "flow", "steps": [
                 "Educate girls (SDG 4)",
                 "&rarr; later marriage &amp; fewer children (SDG 3, 5)",
                 "&rarr; higher household income (SDG 1, 8)",
                 "&rarr; but rising consumption can strain SDG 12, 13"]},
         ]},

        {"type": "content", "label": "South Asia", "title": "The SDGs in South Asia",
         "blocks": [
             {"t": "bullets", "items": [
                 "Home to a large share of the world's poor &mdash; SDG 1 is central",
                 "Strong gains in some health and poverty indicators",
                 "Persistent gaps in nutrition, gender, sanitation and air quality",
                 "India tracks progress via NITI Aayog's <strong>SDG India Index</strong>"]},
             {"t": "hbox", "color": "cyan", "html": "For a regional practitioner, the SDGs are "
              "not abstract: they likely already structure your funder's targets and your own "
              "reporting."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Financing for Development"},

        {"type": "content", "label": "The Big Question", "title": "Who pays for the SDGs?",
         "blocks": [
             {"t": "body", "html": "Reaching the SDGs needs <strong>trillions, not "
              "billions</strong> &mdash; far beyond what aid can supply. 'Financing for "
              "development' is the global conversation about where that money comes from."},
             {"t": "chart", "canvas": "financingGapChart",
              "title": "Illustrative SDG financing: need vs available sources",
              "source": "Illustrative, patterned on the 'billions to trillions' debate",
              "type": "bar",
              "data": {"labels": ["Estimated need", "Current financing"],
                       "datasets": [{"label": "Relative scale",
                                     "data": [100, 60],
                                     "backgroundColor": ["#EF4444", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0, max:110, title:{display:true,text:'Relative scale'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "The gap between what the goals need and "
              "what is financed is large and persistent. (Scale above is illustrative, not a "
              "dollar figure.)"},
         ]},

        {"type": "content", "label": "The Agenda", "title": "Monterrey to Addis Ababa",
         "blocks": [
             {"t": "flow", "steps": [
                 "2002 Monterrey Consensus &mdash; first big FfD framework",
                 "2008 Doha &mdash; review amid financial crisis",
                 "2015 Addis Ababa Action Agenda &mdash; financing the SDGs",
                 "Ongoing: debt, tax &amp; reform debates"]},
             {"t": "hbox", "color": "cyan", "html": "The <strong>Addis Ababa Action Agenda "
              "(2015)</strong> is the financing companion to the SDGs &mdash; it shifted the "
              "emphasis from aid alone to all sources of finance."},
         ]},

        {"type": "content", "label": "The First Source", "title": "Domestic resource mobilisation",
         "blocks": [
             {"t": "body", "html": "The largest and most sustainable source of development "
              "finance is a country's own <strong>tax revenue</strong>. Building the capacity to "
              "tax fairly and efficiently &mdash; 'domestic resource mobilisation' &mdash; "
              "matters more than any aid flow."},
             {"t": "hbox", "color": "green", "html": "A few percentage points more of GDP "
              "collected in tax can dwarf a country's entire aid receipts &mdash; and comes "
              "without conditions or repayment."},
         ]},

        {"type": "content", "label": "The Leak", "title": "Illicit flows and tax avoidance",
         "blocks": [
             {"t": "body", "html": "Developing countries lose vast sums to "
              "<strong>illicit financial flows</strong> &mdash; corporate profit-shifting, "
              "trade mis-invoicing, tax evasion &mdash; money that flows <em>out</em> to tax "
              "havens, often exceeding what flows in as aid."},
             {"t": "hbox", "color": "red", "html": "This reframes the aid debate: for many "
              "countries, stopping the leakage out would do more than increasing the trickle in. "
              "Tax justice is a development issue."},
         ]},

        {"type": "content", "label": "The Debt Trap", "title": "Debt sustainability",
         "blocks": [
             {"t": "term", "word": "Debt sustainability",
              "def": "Whether a country can service its debts without compromising its ability to "
              "fund essential public services or jeopardising future growth."},
             {"t": "hbox", "color": "red", "html": "When debt service swallows the budget, "
              "spending on health, education and food gets squeezed first. A growing number of "
              "low-income countries are in or near <strong>debt distress</strong>."},
         ]},

        {"type": "content", "label": "Debt Dynamics", "title": "How countries fall into distress",
         "blocks": [
             {"t": "flow", "steps": [
                 "Borrow for infrastructure &amp; budgets",
                 "Shock: pandemic, prices, currency fall",
                 "Repayments rise, revenue falls",
                 "Service debt OR fund services &mdash; not both"]},
             {"t": "hbox", "color": "amber", "html": "Debt is not inherently bad &mdash; it can "
              "finance growth. The danger is borrowing on hard terms for projects that do not "
              "generate the returns to repay them."},
         ]},

        {"type": "content", "label": "Blended Finance", "title": "Using aid to pull in private money",
         "blocks": [
             {"t": "term", "word": "Blended finance",
              "def": "Using public or philanthropic money to reduce the risk of an investment so "
              "that private capital, which would otherwise stay away, comes in alongside it."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "The hope", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Each aid dollar 'leverages' several private "
                   "dollars, multiplying impact."}]}],
              "right": [{"t": "panel", "color": "red", "title": "The caution", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Leverage ratios are often modest, and "
                   "private money avoids the poorest places that need it most."}]}]},
         ]},

        {"type": "content", "label": "All Sources", "title": "The financing toolbox",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Domestic taxes</strong> &mdash; largest, most sustainable",
                 "<strong>ODA</strong> &mdash; catalytic but limited",
                 "<strong>Private investment</strong> &mdash; large but risk-averse",
                 "<strong>Remittances</strong> &mdash; huge, direct to households",
                 "<strong>Borrowing</strong> &mdash; useful, but watch sustainability"]},
             {"t": "hbox", "color": "cyan", "html": "The Addis lesson: no single source is "
              "enough. Development financing is a portfolio, and aid is only one slice of it."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "New &amp; Shifting Actors"},

        {"type": "content", "label": "A Crowded Field", "title": "The system is no longer just states",
         "blocks": [
             {"t": "body", "html": "For decades, development was governments and the UN. Today the "
              "field is crowded with <strong>foundations, emerging-economy donors, companies and "
              "global networks</strong> &mdash; each bringing money, agendas and influence."},
             {"t": "hbox", "color": "cyan", "html": "This pluralism brings more resources and "
              "ideas &mdash; but also more fragmentation, and new questions about who is "
              "accountable to whom."},
         ]},

        {"type": "content", "label": "Big Philanthropy", "title": "Private foundations as power players",
         "blocks": [
             {"t": "body", "html": "Large foundations &mdash; the <strong>Gates Foundation</strong> "
              "above all, alongside Ford, Rockefeller and others &mdash; now fund development at a "
              "scale that rivals mid-sized donor governments, especially in global health."},
             {"t": "hbox", "color": "amber", "html": "Their money is fast and flexible &mdash; "
              "but it is unelected. A handful of private donors can tilt a whole field's "
              "priorities, with no voters to answer to."},
         ]},

        {"type": "content", "label": "South-South", "title": "South&ndash;South cooperation",
         "blocks": [
             {"t": "term", "word": "South&ndash;South cooperation",
              "def": "Development cooperation between developing countries themselves &mdash; "
              "sharing finance, technology and expertise as partners, framed as solidarity "
              "rather than charity."},
             {"t": "hbox", "color": "green", "html": "India, Brazil, China and others position "
              "their assistance as <em>partnership between equals</em> &mdash; explicitly "
              "rejecting the donor-recipient hierarchy of traditional North&ndash;South aid."},
         ]},

        {"type": "content", "label": "China", "title": "China &amp; the Belt and Road Initiative",
         "blocks": [
             {"t": "body", "html": "China has become a major development financier, much of it "
              "through the <strong>Belt and Road Initiative (BRI)</strong> &mdash; large "
              "infrastructure loans for ports, roads, rail and power across Asia and Africa."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Appeal", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Fast, large-scale, few governance "
                   "conditions, builds visible infrastructure."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Concern", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Mostly loans, opaque terms, and debt-"
                   "sustainability worries for some borrowers."}]}]},
         ]},

        {"type": "content", "label": "Beyond the DAC", "title": "Why this breaks the old map",
         "blocks": [
             {"t": "body", "html": "These new donors sit <strong>outside the OECD-DAC</strong>. "
              "They do not report to its rules, do not use its ODA definition, and do not accept "
              "its aid-effectiveness commitments as binding."},
             {"t": "hbox", "color": "amber", "html": "So the official 'global aid' statistics now "
              "miss a large and fast-growing slice of real flows. The map is older than the "
              "territory."},
         ]},

        {"type": "content", "label": "The Private Sector", "title": "Business as a development actor",
         "blocks": [
             {"t": "body", "html": "Companies are courted as financiers, partners and "
              "implementers &mdash; through CSR, impact investing, public-private partnerships "
              "and corporate foundations."},
             {"t": "hbox", "color": "red", "html": "Promise: scale, efficiency, jobs. Risk: "
              "profit motives may not align with the poorest, and 'partnership' can become "
              "privatised public services with weak accountability."},
         ]},

        {"type": "content", "label": "INGOs", "title": "International NGOs",
         "blocks": [
             {"t": "body", "html": "Large international NGOs &mdash; Oxfam, Save the Children, "
              "CARE, BRAC and many more &mdash; deliver programmes, channel donor money, and "
              "advocate. They are both implementers and a check on power."},
             {"t": "hbox", "color": "cyan", "html": "But INGOs face their own reckoning: critics "
              "ask why Northern organisations still capture so much funding meant for Southern "
              "communities. (More on this in the next section.)"},
         ]},

        {"type": "content", "label": "Net Effect", "title": "A multipolar, contested system",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>More money</strong> and more choice for recipient countries",
                 "<strong>More fragmentation</strong> &mdash; harder to coordinate",
                 "<strong>Eroded Western monopoly</strong> on rules and finance",
                 "<strong>New accountability gaps</strong> as unelected actors grow"]},
             {"t": "hbox", "color": "green", "html": "For practitioners, this means more "
              "potential partners &mdash; and a sharper need to ask what each one really wants."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Aid Effectiveness &amp; Localisation"},

        {"type": "content", "label": "The Problem", "title": "More aid is not enough",
         "blocks": [
             {"t": "body", "html": "By the early 2000s it was clear that the <em>quality</em> of "
              "aid mattered as much as the quantity. Fragmented projects, duplicated reporting "
              "and donor-driven priorities were wasting effort and overwhelming governments."},
             {"t": "hbox", "color": "amber", "html": "A poor country might host dozens of donors, "
              "each with its own forms, missions and audits &mdash; a crushing burden on the very "
              "ministries meant to be delivering."},
         ]},

        {"type": "content", "label": "Paris 2005", "title": "The Paris Declaration",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "The <strong>Paris Declaration on Aid Effectiveness "
              "(2005)</strong> set out principles donors and recipients agreed to live by."},
             {"t": "table",
              "head": ["Principle", "Meaning"],
              "rows": [
                  ["Ownership", "Countries lead their own development plans"],
                  ["Alignment", "Donors back those plans &amp; use country systems"],
                  ["Harmonisation", "Donors coordinate to reduce duplication"],
                  ["Results", "Focus on outcomes, not just inputs"],
                  ["Mutual accountability", "Both sides answerable for results"]]},
         ]},

        {"type": "content", "label": "The Sequence", "title": "Paris &rarr; Accra &rarr; Busan",
         "blocks": [
             {"t": "flow", "steps": [
                 "2005 Paris Declaration &mdash; five principles",
                 "2008 Accra Agenda for Action &mdash; deepen ownership",
                 "2011 Busan &mdash; widen to new donors, CSOs, business",
                 "Today: localisation &amp; the Grand Bargain"]},
             {"t": "hbox", "color": "cyan", "html": "<strong>Busan (2011)</strong> mattered "
              "because it tried to bring China, the private sector and civil society into a "
              "shared 'partnership' &mdash; with limited success."},
         ]},

        {"type": "content", "label": "Ownership", "title": "The most important principle",
         "blocks": [
             {"t": "body", "html": "<strong>Country ownership</strong> &mdash; the idea that "
              "recipients, not donors, should set priorities and lead &mdash; is the heart of the "
              "agenda, and the hardest to honour in practice."},
             {"t": "hbox", "color": "red", "html": "Ownership and conditionality are in tension: "
              "you cannot truly own a plan that a lender requires you to follow. The principle is "
              "easy to sign and hard to mean."},
         ]},

        {"type": "content", "label": "Localisation", "title": "Shifting power and money local",
         "blocks": [
             {"t": "term", "word": "Localisation",
              "def": "Shifting funding, decision-making and leadership from international actors "
              "to local and national organisations &mdash; on the principle that those closest to "
              "a problem should lead the response."},
             {"t": "hbox", "color": "green", "html": "The aim: more money <em>direct</em> to "
              "local organisations, and less passing through layers of international "
              "intermediaries that each take a cut."},
         ]},

        {"type": "content", "label": "Grand Bargain", "title": "The Grand Bargain, 2016",
         "blocks": [
             {"t": "body", "html": "At the 2016 World Humanitarian Summit, major donors and "
              "agencies struck the <strong>Grand Bargain</strong>: a set of commitments to make "
              "aid more efficient, including channelling more funding 'as directly as possible' "
              "to local responders."},
             {"t": "chart", "canvas": "localisationChart",
              "title": "Illustrative: aid reaching local actors vs an aspirational target",
              "source": "Illustrative, patterned on Grand Bargain localisation debates",
              "type": "bar",
              "data": {"labels": ["Reaching local actors", "Aspirational target"],
                       "datasets": [{"label": "% of funding",
                                     "data": [3, 25],
                                     "backgroundColor": ["#EF4444", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0, max:30, title:{display:true,text:'% direct to local actors'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "Progress has been slow: the share reaching "
              "local actors directly remains far below the aspiration. (Values above are "
              "illustrative.)"},
         ]},

        {"type": "content", "label": "Decolonising Aid", "title": "A deeper challenge to power",
         "blocks": [
             {"t": "body", "html": "The <strong>decolonising-aid</strong> movement goes further "
              "than logistics. It questions whose knowledge counts, who sits in leadership, whose "
              "language sets the terms, and who is treated as expert versus beneficiary."},
             {"t": "hbox", "color": "indigo", "html": "It asks the system to confront the "
              "colonial patterns embedded in its everyday habits &mdash; not just to move money "
              "faster, but to share power."},
         ]},

        {"type": "content", "label": "Why It's Hard", "title": "Good intentions, slow change",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Donors fear losing control and visibility",
                 "Risk and compliance rules favour large intermediaries",
                 "'Capacity' is used to justify keeping power at the top",
                 "Incentives reward those who already hold the money"]},
             {"t": "hbox", "color": "cyan", "html": "The agenda is widely endorsed and slowly "
              "implemented &mdash; a reminder that in this system, declarations are easy and "
              "redistributing power is not."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Critiques &amp; Power"},

        {"type": "content", "label": "The Hard Questions", "title": "Does aid even work?",
         "blocks": [
             {"t": "body", "html": "After decades and trillions of dollars, the question still "
              "divides experts: has aid driven development, held it back, or merely been a "
              "sideshow? A data-literate practitioner holds the critiques and the defences "
              "together."},
             {"t": "hbox", "color": "amber", "html": "The honest answer is 'it depends' &mdash; "
              "on the type of aid, the context, the conditions and who controls it. Blanket "
              "praise and blanket condemnation are both lazy."},
         ]},

        {"type": "content", "label": "Dependency", "title": "Does aid create dependence?",
         "blocks": [
             {"t": "body", "html": "Critics argue that sustained aid can <strong>weaken "
              "accountability</strong>: governments answer to donors rather than citizens, local "
              "markets are undercut, and a parallel aid economy supplants domestic capacity."},
             {"t": "hbox", "color": "red", "html": "If a government's revenue comes from donors "
              "rather than taxpayers, the pressure to serve its own people can weaken. Aid can "
              "quietly bypass the social contract."},
         ]},

        {"type": "content", "label": "The Dead Aid Debate", "title": "Dambisa Moyo's challenge",
         "blocks": [
             {"t": "body", "html": "In <em>Dead Aid</em> (2009), economist <strong>Dambisa "
              "Moyo</strong> argued that decades of aid to Africa had fostered dependency and "
              "corruption, and that trade, investment and markets would do more than grants ever "
              "could."},
             {"t": "hbox", "color": "amber", "html": "Critics counter that her case generalises "
              "and that targeted aid &mdash; vaccines, schooling, cash &mdash; has saved and "
              "improved millions of lives. The debate remains unresolved &mdash; and worth "
              "knowing by name."},
         ]},

        {"type": "content", "label": "Paternalism", "title": "Who decides what people need?",
         "blocks": [
             {"t": "body", "html": "Aid has a long habit of deciding <em>for</em> people: outside "
              "experts designing solutions for communities they barely know, treating recipients "
              "as problems to be managed rather than agents with their own priorities."},
             {"t": "quote",
              "text": "The poor are not the problem; they are the solution. Treat them as "
              "partners, not as beneficiaries.",
              "attr": "&mdash; a recurring theme in participatory development"},
         ]},

        {"type": "content", "label": "Conditionality, Again", "title": "Aid and sovereignty",
         "blocks": [
             {"t": "body", "html": "When loans require privatisation, austerity or specific "
              "reforms, unelected outsiders are effectively setting the policies of a sovereign "
              "country &mdash; sometimes against the express wishes of its voters."},
             {"t": "hbox", "color": "red", "html": "This is the sharpest critique of "
              "conditionality: it can hollow out democracy, making governments accountable "
              "upward to lenders rather than downward to citizens."},
         ]},

        {"type": "content", "label": "Whose Knowledge", "title": "Power runs through measurement",
         "blocks": [
             {"t": "body", "html": "Power is not only in the money. It is in <strong>who defines "
              "success</strong>: which outcomes get measured, whose indicators count, which "
              "languages and frameworks dominate the proposals and reports."},
             {"t": "hbox", "color": "indigo", "html": "Recall from data literacy: every choice of "
              "what to measure is a choice about what matters. In aid, those choices are usually "
              "made far from the communities affected."},
         ]},

        {"type": "content", "label": "Accountability", "title": "Accountable to whom?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Upward", "blocks": [
                  {"t": "body", "cls": "sm", "html": "To donors and headquarters &mdash; audits, "
                   "logframes, results frameworks. Well-developed and heavily enforced."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Downward", "blocks": [
                  {"t": "body", "cls": "sm", "html": "To the communities served &mdash; their "
                   "voice, feedback, redress. Often weak, optional or tokenistic."}]}]},
             {"t": "hbox", "color": "red", "html": "The system is wired to answer to those who "
              "<em>pay</em>, not to those who are <em>served</em>. Rebalancing that is the "
              "unfinished work of accountability."},
         ]},

        {"type": "content", "label": "A Balanced View", "title": "Critique without cynicism",
         "blocks": [
             {"t": "bullets", "items": [
                 "Aid has demonstrably <strong>saved lives</strong> &mdash; vaccines, "
                 "treatment, cash, disaster relief",
                 "It has also <strong>distorted incentives</strong> and entrenched power",
                 "The goal is not to abolish or worship aid, but to "
                 "<strong>reform</strong> it",
                 "Better aid means more local power, less conditionality, real accountability"]},
             {"t": "hbox", "color": "cyan", "html": "Hold both truths. Naive faith and total "
              "dismissal each fail the people the system is meant to serve."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "India in the System"},

        {"type": "content", "label": "The Journey", "title": "From major recipient to emerging donor",
         "blocks": [
             {"t": "body", "html": "India's place in the architecture has flipped within a "
              "lifetime. Once among the world's largest aid recipients, it is now also a "
              "<strong>provider of development cooperation</strong> to other countries."},
             {"t": "flow", "steps": [
                 "1950s&ndash;90s: major recipient (food aid, IDA loans)",
                 "2000s: graduates from many donor programmes",
                 "Today: both receives selectively AND gives",
                 "Positions itself as voice of the Global South"]},
         ]},

        {"type": "content", "label": "How India Gives", "title": "DPA, lines of credit &amp; the MEA",
         "blocks": [
             {"t": "body", "html": "India's cooperation is run largely through the "
              "<strong>Ministry of External Affairs (MEA)</strong> and its Development "
              "Partnership Administration (DPA), delivered mainly via concessional "
              "<strong>lines of credit</strong>, grants, training and projects."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Lines of credit", "label": "Concessional loans for partner-country "
                  "projects", "color": "cyan"},
                 {"num": "Grants &amp; projects", "label": "Especially to neighbours &amp; "
                  "Africa", "color": "green"},
                 {"num": "Training", "label": "Scholarships &amp; technical cooperation (ITEC)",
                  "color": "indigo"}]},
         ]},

        {"type": "content", "label": "The Framing", "title": "Partnership, not charity",
         "blocks": [
             {"t": "body", "html": "India frames its assistance as <strong>South&ndash;South "
              "cooperation</strong> &mdash; solidarity between developing nations, free of the "
              "conditionalities and lectures it associates with traditional Western donors."},
             {"t": "hbox", "color": "amber", "html": "Critics note India's cooperation also "
              "serves its strategic and commercial interests &mdash; as all donors' aid does. "
              "'Partnership' is a framing, not a guarantee of selflessness."},
         ]},

        {"type": "content", "label": "The G20", "title": "India's G20 presidency",
         "blocks": [
             {"t": "body", "html": "Holding the <strong>G20 presidency in 2023</strong>, India "
              "pushed development up the agenda &mdash; debt, climate finance, digital public "
              "infrastructure &mdash; and championed the inclusion of the "
              "<strong>African Union</strong> as a permanent G20 member."},
             {"t": "hbox", "color": "green", "html": "The presidency was a stage to argue that "
              "the global architecture, designed in 1944, no longer reflects today's world "
              "&mdash; and must be reformed."},
         ]},

        {"type": "content", "label": "Voice of the South", "title": "Speaking for the Global South",
         "blocks": [
             {"t": "body", "html": "India increasingly casts itself as a "
              "<strong>spokesperson for the Global South</strong> &mdash; convening the 'Voice of "
              "the Global South' summits and pressing for fairer representation in the UN, the "
              "IMF and the World Bank."},
             {"t": "hbox", "color": "cyan", "html": "Its core demands echo the reform agenda of "
              "this whole course: re-weight the votes, end the leadership conventions, ease "
              "conditionality, and treat developing nations as partners."},
         ]},

        {"type": "content", "label": "Tensions", "title": "An honest look at India's role",
         "blocks": [
             {"t": "bullets", "color": "amber", "items": [
                 "Champions the South abroad while facing deep inequities at home",
                 "Gives aid yet still hosts a vast share of global poverty",
                 "Seeks more votes in IFIs it also benefits from",
                 "Balances rivalry with China against shared 'Southern' interests"]},
             {"t": "hbox", "color": "indigo", "html": "These tensions are not hypocrisy so much "
              "as the reality of a large, unequal, fast-changing country negotiating a system in "
              "flux."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "Where to learn more",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Dead Aid</em> &mdash; Dambisa Moyo (the critique of aid)",
                 "<em>The End of Poverty</em> &mdash; Jeffrey Sachs (the case for big aid)",
                 "<em>The White Man's Burden</em> &mdash; William Easterly (the sceptic's reply)",
                 "<em>Poor Economics</em> &mdash; Banerjee &amp; Duflo (evidence over ideology)",
                 "OECD-DAC, UN SDG and World Bank Open Data portals for the numbers"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Development Economics</strong>, <strong>Data Literacy</strong> and "
              "<strong>Aid &amp; Philanthropy</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>The architecture was built in 1944</strong> &mdash; and still favours "
                 "its founders",
                 "<strong>Most 'aid' is debt</strong> &mdash; always ask grant or loan",
                 "<strong>The 0.7% target is real</strong> &mdash; and mostly unmet",
                 "<strong>The SDGs are a shared map</strong>, not a funded guarantee",
                 "<strong>Follow the power</strong> &mdash; who decides, and who is accountable "
                 "to whom"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Global Development Governance 101 &middot; Complete",
         "headline": "Now follow the<br>money and the power.",
         "byline": "You don't need to run the UN or the World Bank &mdash; you need to know who "
                   "holds the money, who makes the rules, and where your work sits in the chain. "
                   "Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
