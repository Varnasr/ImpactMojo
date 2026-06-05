# -*- coding: utf-8 -*-
"""
Political Economy 101 — ImpactMojo 101 Series (native deck spec)
Foundational political economy for South Asian development practitioners & analysts.
Build: python3 scripts/deck-builder/build.py pol_economy
"""

DECK = {
    "slug": "pol-economy",
    "title": "Political Economy 101",
    "description": ("Political Economy 101 — a free foundational course for development "
                    "practitioners and analysts in South Asia. From Smith, Ricardo and Marx "
                    "through institutions, collective action, rents and political settlements "
                    "to Political Economy Analysis in practice and the Indian state. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Political<br>Economy<br>101",
         "sub": "Who Gets What, When &amp; How &mdash; a Foundational Course on Power, "
                "Institutions &amp; Reform for Development Practitioners in South Asia",
         "tags": ["Theory-to-Practice", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Is Political Economy?"},
             {"name": "Classical Roots"},
             {"name": "The State &amp; the Market"},
             {"name": "Institutions Matter"},
             {"name": "Collective Action &amp; Public Goods"},
             {"name": "Rents, Corruption &amp; State Capture"},
             {"name": "The Political Economy of Development"},
             {"name": "Political Settlements &amp; Power"},
             {"name": "Political Economy Analysis in Practice"},
             {"name": "Applying PEA"},
             {"name": "India / South Asia &amp; Further Reading"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Is Political Economy?"},

        {"type": "content", "label": "Definition", "title": "Politics and economics are one system",
         "blocks": [
             {"t": "body", "html": "Economics asks how scarce resources are allocated. Politics "
              "asks who holds power and how it is used. <strong>Political economy</strong> insists "
              "the two cannot be separated: markets are shaped by rules, and rules are shaped by "
              "power. For a practitioner, it is the study of why policies live or die."},
             {"t": "term", "word": "Political economy",
              "def": "The study of how political power and economic forces interact to determine "
              "the production and distribution of resources &mdash; who gets what, who decides, "
              "and who is left out."},
         ]},

        {"type": "content", "label": "The Classic Question", "title": "Who gets what, when, and how?",
         "blocks": [
             {"t": "quote",
              "text": "Politics is who gets what, when, how.",
              "attr": "&mdash; Harold Lasswell, 1936"},
             {"t": "body", "html": "Lasswell's phrase is the whole field in one line. Every "
              "budget, subsidy, tariff and posting is an answer to it. Political economy reads "
              "the <em>distribution</em> behind the policy &mdash; and the power behind the "
              "distribution."},
         ]},

        {"type": "content", "label": "Why 'Good Policy' Stalls", "title": "Good economics is not enough",
         "blocks": [
             {"t": "body", "html": "Practitioners are puzzled when a technically sound reform "
              "&mdash; a cleaner subsidy, a better tariff, an honest procurement rule &mdash; is "
              "never adopted, or is adopted and quietly reversed. The reason is rarely ignorance. "
              "It is that the reform reshuffles winners and losers."},
             {"t": "hbox", "color": "amber", "html": "A reform is not just a technical proposal. "
              "It is a redistribution &mdash; and someone always stands to lose. They tend to be "
              "organised, and they tend to fight."},
         ]},

        {"type": "content", "label": "Winners &amp; Losers", "title": "Concentrated losses, diffuse gains",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "The losers", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Few, identifiable, well-resourced",
                      "Lose a lot each &mdash; worth fighting for",
                      "Already organised to defend the status quo"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "The winners", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Many, dispersed, often poor",
                      "Each gains a little &mdash; not worth organising",
                      "Rarely mobilised before the reform happens"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "When losses are concentrated and gains "
              "diffuse, the losers usually win the politics &mdash; even when the public would "
              "gain. This single asymmetry explains a great deal of policy."},
         ]},

        {"type": "content", "label": "Positive vs Normative", "title": "Explain the world, then judge it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Positive", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<em>What is</em> and <em>why</em>: why a "
                   "subsidy persists, how a cartel forms, who captures a regulator. Analytical, "
                   "testable."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Normative", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<em>What ought to be</em>: which "
                   "distribution is fair, which policy is just. Value-laden, contestable."}]}]},
             {"t": "hbox", "color": "amber", "html": "Political economy is mostly positive &mdash; "
              "it explains why bad equilibria persist. But the questions it asks are driven by "
              "normative concern for who is left out."},
         ]},

        {"type": "content", "label": "Levels", "title": "From households to the global order",
         "blocks": [
             {"t": "flow", "steps": [
                 "MICRO: a household, a firm, a village commons",
                 "MESO: a sector, a regulator, a value chain",
                 "MACRO: the national state, fiscal &amp; trade policy",
                 "GLOBAL: aid, debt, trade rules, capital flows"]},
             {"t": "hbox", "color": "cyan", "html": "Power operates at every level. A "
              "well-designed scheme can still fail because of incentives three levels up."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "Political economy is a practitioner's tool",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Diagnose</strong> why a reform you favour keeps stalling",
                 "<strong>Map</strong> who wins, who loses and who can block",
                 "<strong>Find</strong> feasible entry points instead of ideal ones",
                 "<strong>Avoid</strong> designs that ignore the incentives that will undo them"]},
             {"t": "hbox", "color": "green", "html": "This course moves from theory (Sections "
              "1&ndash;8) to practice (Sections 9&ndash;11). The theory exists to make you a "
              "sharper reader of power."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Classical Roots"},

        {"type": "content", "label": "Origins", "title": "Economics began as 'political economy'",
         "blocks": [
             {"t": "body", "html": "Until the late 19th century, the discipline was called "
              "<strong>political economy</strong> &mdash; the study of how nations produce and "
              "distribute wealth, inseparable from the state. Smith, Ricardo, Malthus, Mill and "
              "Marx all wrote in this tradition before 'economics' narrowed the lens."},
             {"t": "hbox", "color": "cyan", "html": "Today's revival of political economy is, in "
              "part, a return to those founders' broader question: not just how much is produced, "
              "but for whom, and under what rules."},
         ]},

        {"type": "content", "label": "Adam Smith", "title": "Adam Smith and the invisible hand",
         "blocks": [
             {"t": "body", "html": "In <em>The Wealth of Nations</em> (1776), <strong>Adam "
              "Smith</strong> argued that individuals pursuing their own interest in competitive "
              "markets are led, as if by an <strong>invisible hand</strong>, to outcomes that "
              "serve society &mdash; without intending to."},
             {"t": "quote",
              "text": "It is not from the benevolence of the butcher, the brewer, or the baker "
              "that we expect our dinner, but from their regard to their own interest.",
              "attr": "&mdash; Adam Smith, The Wealth of Nations, 1776"},
         ]},

        {"type": "content", "label": "Smith Misread", "title": "The Smith most people forget",
         "blocks": [
             {"t": "body", "html": "Smith is caricatured as a prophet of greed. In fact he "
              "distrusted merchants' conspiracies, warned against monopoly, supported public "
              "goods and education, and in <em>The Theory of Moral Sentiments</em> grounded "
              "markets in sympathy and justice."},
             {"t": "hbox", "color": "amber", "html": "The invisible hand works only under "
              "competition and fair rules. Smith knew the businessmen of his day would rig both "
              "if allowed. The qualification matters as much as the metaphor."},
         ]},

        {"type": "content", "label": "David Ricardo", "title": "Ricardo and comparative advantage",
         "blocks": [
             {"t": "term", "word": "Comparative advantage",
              "def": "David Ricardo's insight (1817): even a country worse at producing "
              "everything still gains from trade by specialising in what it produces "
              "<em>relatively</em> best, and trading for the rest."},
             {"t": "body", "html": "It is the strongest case in economics for trade &mdash; both "
              "parties can gain. But Ricardo says nothing about <em>how the gains are shared</em>, "
              "or who bears the losses when an industry is wiped out. That silence is where "
              "political economy enters."},
         ]},

        {"type": "content", "label": "Karl Marx", "title": "Marx: class, capital and critique",
         "blocks": [
             {"t": "body", "html": "<strong>Karl Marx</strong> turned political economy into a "
              "critique of capitalism. He argued that profit comes from <strong>surplus value</strong> "
              "&mdash; the gap between the value workers produce and the wages they are paid &mdash; "
              "making class conflict structural, not accidental."},
             {"t": "term", "word": "Surplus value",
              "def": "In Marx, the value created by labour beyond what is paid in wages, "
              "appropriated by the owners of capital. The source of profit &mdash; and, in Marx's "
              "view, of exploitation."},
         ]},

        {"type": "content", "label": "Marx's Tools", "title": "What survives of Marx for analysts",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Material interests</strong> shape ideas and institutions, not the reverse",
                 "<strong>Class</strong> &mdash; who owns, who labours &mdash; structures conflict",
                 "<strong>Capital accumulation</strong> drives crisis, concentration and change",
                 "<strong>Ideology</strong> can make a particular interest look like the common good"]},
             {"t": "hbox", "color": "amber", "html": "You need not be a Marxist to use Marx. The "
              "habit of asking <em>whose material interest does this serve?</em> is core to any "
              "political-economy analysis."},
         ]},

        {"type": "content", "label": "Three Lenses", "title": "Smith, Ricardo, Marx side by side",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Smith", "Ricardo", "Marx"],
              "rows": [
                  ["Core idea", "Markets coordinate", "Gains from trade", "Class &amp; exploitation"],
                  ["The market", "Mostly benign", "Mutually beneficial", "Site of conflict"],
                  ["Key concept", "Invisible hand", "Comparative advantage", "Surplus value"],
                  ["Distribution", "Secondary", "Central (rent)", "The whole question"],
                  ["The state", "Rules &amp; public goods", "Free trade", "Instrument of class"]]},
             {"t": "hbox", "color": "cyan", "html": "All three are alive in today's debates. "
              "Most policy arguments are, at root, arguments between these three."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The State &amp; the Market"},

        {"type": "content", "label": "The Big Tension", "title": "Markets and states need each other",
         "blocks": [
             {"t": "body", "html": "The lazy debate pits 'free market' against 'big state'. The "
              "real question is the <strong>division of labour</strong> between them: markets are "
              "powerful coordinators, but they fail in predictable ways, and only collective "
              "authority can fix those failures."},
             {"t": "hbox", "color": "cyan", "html": "There is no market without a state to define "
              "property, enforce contracts and issue money. The choice is never market <em>or</em> "
              "state &mdash; it is which mix, designed how."},
         ]},

        {"type": "content", "label": "Market Failure", "title": "When markets get it wrong",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Failure", "What happens", "Example"],
              "rows": [
                  ["Public goods", "Under-supplied &mdash; can't exclude free-riders", "Clean air, rural roads, defence"],
                  ["Externalities", "Costs/benefits spill onto others", "Pollution, vaccination"],
                  ["Information gaps", "One side knows more", "Insurance, used goods, credit"],
                  ["Monopoly power", "Few sellers set prices", "Utilities, platforms"],
                  ["Missing markets", "No market exists at all", "Insurance for the very poor"]]},
             {"t": "hbox", "color": "amber", "html": "Each failure is a <em>reason</em> for state "
              "action &mdash; but not a guarantee the state will do better. Government failure is "
              "real too."},
         ]},

        {"type": "content", "label": "Roles of the State", "title": "What the state is for",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Set the rules:</strong> property rights, contracts, courts, money",
                 "<strong>Provide public goods:</strong> infrastructure, defence, basic research",
                 "<strong>Correct externalities:</strong> tax the bad, subsidise the good",
                 "<strong>Redistribute:</strong> taxes and transfers for equity",
                 "<strong>Stabilise:</strong> manage the macroeconomy and crises"]},
             {"t": "hbox", "color": "green", "html": "Every one of these can be done well or "
              "badly &mdash; and who captures the state decides which."},
         ]},

        {"type": "content", "label": "Government Failure", "title": "The state can fail too",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Why states fail", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Capture by organised interests",
                      "Information the centre cannot have",
                      "Weak capacity to implement",
                      "Officials' own incentives diverge"]}]}],
              "right": [{"t": "panel", "color": "cyan", "title": "The honest balance", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The mature question is not 'market or "
                   "state?' but 'given that <em>both</em> fail, which failure is cheaper to fix "
                   "here, for this problem?'"}]}]},
         ]},

        {"type": "content", "label": "Karl Polanyi", "title": "Polanyi: the great transformation",
         "blocks": [
             {"t": "body", "html": "In <em>The Great Transformation</em> (1944), <strong>Karl "
              "Polanyi</strong> argued that the 19th-century attempt to create a "
              "<strong>self-regulating market</strong> &mdash; treating land, labour and money as "
              "ordinary commodities &mdash; was a radical, destabilising experiment, not a natural "
              "order."},
             {"t": "quote",
              "text": "To allow the market mechanism to be sole director of the fate of human "
              "beings would result in the demolition of society.",
              "attr": "&mdash; Karl Polanyi, The Great Transformation, 1944"},
         ]},

        {"type": "content", "label": "Embeddedness", "title": "Markets are embedded in society",
         "blocks": [
             {"t": "term", "word": "Embeddedness",
              "def": "Polanyi's claim that economic activity is always enmeshed in social "
              "relations, norms and institutions. The 'free market' disembedded from society is "
              "an artificial &mdash; and unsustainable &mdash; construction."},
             {"t": "body", "html": "Land is not just an asset; it is a place people belong to. "
              "Labour is not just a commodity; it is human lives. Pretending otherwise provokes a "
              "reaction."},
         ]},

        {"type": "content", "label": "Double Movement", "title": "The double movement",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:10px 0;">'
                 '<svg viewBox="0 0 560 250" width="560" height="240" xmlns="http://www.w3.org/2000/svg" '
                 'style="max-width:100%;height:auto;font-family:inherit">'
                 # market expansion arrow (right)
                 '<rect x="20" y="40" width="220" height="56" rx="8" fill="#0EA5E9" fill-opacity="0.12" '
                 'stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="130" y="64" text-anchor="middle" fill="#0EA5E9" font-size="13">Market expansion</text>'
                 '<text x="130" y="84" text-anchor="middle" fill="#94A3B8" font-size="11">commodify land, labour, money</text>'
                 '<path d="M250,68 L330,68" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#pmh)"/>'
                 # society protects (left, counter)
                 '<rect x="340" y="40" width="200" height="56" rx="8" fill="#F59E0B" fill-opacity="0.12" '
                 'stroke="#F59E0B" stroke-width="2"/>'
                 '<text x="440" y="64" text-anchor="middle" fill="#F59E0B" font-size="13">Social protection</text>'
                 '<text x="440" y="84" text-anchor="middle" fill="#94A3B8" font-size="11">demands to re-embed</text>'
                 # return arrow
                 '<path d="M440,100 Q440,170 290,170 Q140,170 130,102" fill="none" stroke="#334155" '
                 'stroke-width="2" stroke-dasharray="5,4" marker-end="url(#pmh)"/>'
                 '<text x="285" y="195" text-anchor="middle" fill="#10B981" font-size="13">'
                 'the &quot;double movement&quot;: expansion provokes counter-movement</text>'
                 '<defs><marker id="pmh" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
                 '<path d="M0,0 L7,3 L0,6 Z" fill="#334155"/></marker></defs>'
                 '</svg></div>')},
             {"t": "hbox", "color": "cyan", "html": "Polanyi's pattern recurs: each push to "
              "marketise provokes demands for protection &mdash; from labour laws to farm-loan "
              "waivers to MGNREGA. Read backlash as a double movement, not just 'populism'."},
         ]},

        {"type": "content", "label": "South Asia", "title": "The double movement in South Asia",
         "blocks": [
             {"t": "body", "html": "India's 1991 liberalisation expanded markets; the subsequent "
              "decades brought a counter-movement of rights-based guarantees &mdash; "
              "<strong>NREGA, the Right to Food, the Forest Rights Act</strong>. The 2020&ndash;21 "
              "farm-law repeal was a vivid double movement in real time."},
             {"t": "hbox", "color": "amber", "html": "Practitioner lesson: a reform that "
              "disembeds too fast &mdash; removing protections faster than society will bear "
              "&mdash; generates the very backlash that reverses it."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Institutions Matter"},

        {"type": "content", "label": "The Turn", "title": "Why are some countries rich?",
         "blocks": [
             {"t": "body", "html": "Not geography, not culture, not natural resources alone. The "
              "dominant modern answer is <strong>institutions</strong> &mdash; the rules, written "
              "and unwritten, that shape incentives to invest, innovate and cooperate. Get the "
              "rules wrong and no amount of aid or advice sticks."},
             {"t": "hbox", "color": "cyan", "html": "This is the most influential idea in "
              "development economics of the last forty years &mdash; and the most useful for a "
              "practitioner diagnosing why a programme underperforms."},
         ]},

        {"type": "content", "label": "Douglass North", "title": "North: institutions as the rules of the game",
         "blocks": [
             {"t": "term", "word": "Institutions",
              "def": "Douglass North: the humanly devised constraints that structure political, "
              "economic and social interaction &mdash; the 'rules of the game' in a society. "
              "Both formal (laws, constitutions) and informal (norms, conventions)."},
             {"t": "body", "html": "North founded <strong>New Institutional Economics</strong>. "
              "His insight: institutions reduce <em>uncertainty</em> and <em>transaction costs</em>. "
              "Where property is secure and contracts enforced, people invest for the long run."},
         ]},

        {"type": "content", "label": "Rules vs Players", "title": "The rules, the players, the referee",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Institutions", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The <em>rules</em> of the game: laws, "
                   "property rights, electoral systems, norms. Slow to change, deeply consequential."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Organisations", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The <em>players</em>: firms, parties, "
                   "agencies, NGOs. They form to exploit the rules &mdash; and lobby to change them."}]}]},
             {"t": "hbox", "color": "amber", "html": "Confusing the two is a common error. "
              "Building a new agency (a player) rarely fixes a problem rooted in the rules."},
         ]},

        {"type": "content", "label": "Acemoglu &amp; Robinson", "title": "Inclusive vs extractive institutions",
         "blocks": [
             {"t": "body", "html": "In <em>Why Nations Fail</em> (2012), <strong>Daron Acemoglu "
              "&amp; James Robinson</strong> argue prosperity turns on whether institutions are "
              "<strong>inclusive</strong> &mdash; broad rights, level playing field &mdash; or "
              "<strong>extractive</strong> &mdash; designed to funnel wealth and power to a "
              "narrow elite."},
             {"t": "hbox", "color": "cyan", "html": "Acemoglu, Robinson and Simon Johnson shared "
              "the 2024 Nobel Prize in Economics for this body of work on institutions and "
              "prosperity."},
         ]},

        {"type": "content", "label": "The Contrast", "title": "Inclusive vs extractive, compared",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Inclusive", "Extractive"],
              "rows": [
                  ["Who participates", "Broad mass of people", "A narrow elite"],
                  ["Property rights", "Secure for many", "Secure only for the elite"],
                  ["Entry &amp; competition", "Open", "Blocked to protect incumbents"],
                  ["Incentive to invest", "Strong, widespread", "Weak for outsiders"],
                  ["Political power", "Pluralist, constrained", "Concentrated, absolutist"],
                  ["Long-run result", "Innovation &amp; growth", "Stagnation &amp; capture"]]},
             {"t": "hbox", "color": "amber", "html": "Their claim: economic and political "
              "institutions reinforce each other. Extractive politics protects extractive "
              "economics &mdash; a trap that is hard to escape."},
         ]},

        {"type": "content", "label": "The Evidence", "title": "Institutions track with prosperity",
         "blocks": [
             {"t": "chart", "canvas": "instIncomeChart",
              "title": "Institutional quality vs income per person, across countries",
              "source": "Illustrative scatter, patterned on cross-country evidence",
              "type": "scatter",
              "data": {"datasets": [{"label": "Countries",
                       "data": [{"x": 2.0, "y": 1.5}, {"x": 2.6, "y": 2.2}, {"x": 3.1, "y": 2.0},
                                {"x": 3.4, "y": 3.5}, {"x": 4.0, "y": 4.2}, {"x": 4.3, "y": 3.8},
                                {"x": 5.0, "y": 6.0}, {"x": 5.5, "y": 7.5}, {"x": 6.2, "y": 9.0},
                                {"x": 6.8, "y": 11.0}, {"x": 7.5, "y": 12.5}, {"x": 8.2, "y": 13.0},
                                {"x": 3.0, "y": 5.5}, {"x": 7.0, "y": 8.0}],
                       "backgroundColor": "#6366F1", "pointRadius": 6}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Institutional quality (index, low→high)'} }, y:{ title:{display:true,text:'Income per person (relative)'} } } }"}},
             {"t": "hbox", "color": "red", "html": "A strong positive pattern &mdash; but "
              "<em>illustrative</em>. And correlation is not causation: do good institutions cause "
              "wealth, or does wealth buy good institutions? The debate is live."},
         ]},

        {"type": "content", "label": "Critique", "title": "Where the institutions story strains",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Tautology risk:</strong> 'good institutions' can be defined by the "
                 "outcomes they're meant to explain",
                 "<strong>How to change them?</strong> The theory explains traps better than exits",
                 "<strong>China &amp; East Asia:</strong> grew fast with 'extractive'-looking politics",
                 "<strong>Informal rules</strong> often matter more than the formal ones measured"]},
             {"t": "hbox", "color": "amber", "html": "Institutions matter &mdash; but 'just fix "
              "the institutions' is advice, not a plan. The next sections ask <em>how</em> rules "
              "actually change."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Collective Action &amp; Public Goods"},

        {"type": "content", "label": "The Puzzle", "title": "Why don't people who share an interest act?",
         "blocks": [
             {"t": "body", "html": "Millions of consumers would gain from cheaper, cleaner "
              "policy; a handful of producers gain from the status quo. Yet the producers win. "
              "Why do large groups with a common interest so often fail to act on it? This is the "
              "<strong>collective action problem</strong>."},
             {"t": "hbox", "color": "cyan", "html": "It is one of the most useful ideas a "
              "practitioner can hold. It explains why the many are out-organised by the few "
              "&mdash; again and again."},
         ]},

        {"type": "content", "label": "Mancur Olson", "title": "Olson: the logic of collective action",
         "blocks": [
             {"t": "body", "html": "In <em>The Logic of Collective Action</em> (1965), "
              "<strong>Mancur Olson</strong> showed that rational individuals will "
              "<strong>free-ride</strong> on a shared benefit rather than pay to provide it "
              "&mdash; so large groups under-provide their own collective goods unless specially "
              "organised."},
             {"t": "term", "word": "Free-riding",
              "def": "Enjoying a collective benefit without contributing to its cost. Because one "
              "can benefit whether or not one pays, the individually rational choice is to let "
              "others bear the burden &mdash; so the good is under-supplied."},
         ]},

        {"type": "content", "label": "Small Beats Large", "title": "Why small groups out-organise large ones",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Small group", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Each member's share is large",
                      "Free-riders are visible &amp; shamed",
                      "Easy to coordinate and monitor"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Large group", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Each member's share is tiny",
                      "One defector goes unnoticed",
                      "Coordination is costly &mdash; so few try"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Olson's paradox: a small group of "
              "industrialists will reliably lobby; millions of dispersed taxpayers or consumers "
              "rarely will. Concentrated interests beat diffuse ones."},
         ]},

        {"type": "content", "label": "Selective Incentives", "title": "How collective action is solved",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Selective incentives:</strong> private rewards for members only "
                 "(union benefits, a co-op's services)",
                 "<strong>Coercion:</strong> compulsory dues, mandatory membership",
                 "<strong>Small size or federation:</strong> nest large groups inside small ones",
                 "<strong>Leadership &amp; identity:</strong> entrepreneurs who supply organisation"]},
             {"t": "hbox", "color": "green", "html": "Effective movements &mdash; trade unions, "
              "SEWA, farmer associations &mdash; succeed by giving members something <em>only "
              "members</em> get, not by appeals to the common good alone."},
         ]},

        {"type": "content", "label": "The Commons", "title": "The tragedy of the commons",
         "blocks": [
             {"t": "body", "html": "A shared, finite resource &mdash; a grazing pasture, a "
              "groundwater aquifer, a fishery &mdash; tends to be over-used when each user gains "
              "the full benefit of taking more but shares the cost of depletion. Garrett Hardin "
              "called this the <strong>tragedy of the commons</strong> (1968)."},
             {"t": "hbox", "color": "red", "html": "South Asia's falling water tables are a "
              "textbook commons tragedy: each farmer's borewell is rational; the collapsing "
              "aquifer is catastrophic for all."},
         ]},

        {"type": "content", "label": "Elinor Ostrom", "title": "Ostrom: governing the commons",
         "blocks": [
             {"t": "body", "html": "<strong>Elinor Ostrom</strong> showed Hardin was not "
              "destiny. Across forests, fisheries and irrigation systems worldwide, communities "
              "<em>do</em> govern commons sustainably &mdash; without either privatisation or "
              "top-down state control. She won the <strong>2009 Nobel Prize in Economics</strong>."},
             {"t": "quote",
              "text": "There is no reason to believe that bureaucrats and politicians... are "
              "any more motivated to achieve the public interest than are... ordinary citizens.",
              "attr": "&mdash; Elinor Ostrom"},
         ]},

        {"type": "content", "label": "Ostrom's Principles", "title": "Eight design principles for the commons",
         "compact": True,
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "bullets", "sm": True, "items": [
                  "Clear boundaries &mdash; who may use it",
                  "Rules fit local conditions",
                  "Users help make the rules",
                  "Monitoring by accountable monitors"]}],
              "right": [{"t": "bullets", "sm": True, "color": "green", "items": [
                  "Graduated sanctions for breaches",
                  "Cheap, accessible conflict resolution",
                  "Right to self-organise is recognised",
                  "Nested governance for large systems"]}]},
             {"t": "hbox", "color": "cyan", "html": "Notice: these are <em>institutional</em> "
              "design rules. Ostrom's commons work and North's institutions are the same insight "
              "from two directions &mdash; rules shape cooperation."},
         ]},

        {"type": "content", "label": "Application", "title": "Commons governance in South Asia",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Joint Forest Management</strong> and community forest rights under the FRA",
                 "<strong>Pani panchayats</strong> and water-user associations for irrigation",
                 "<strong>Fishery cooperatives</strong> managing access and seasons",
                 "<strong>Self-help groups</strong> pooling savings and enforcing repayment"]},
             {"t": "hbox", "color": "amber", "html": "Ostrom's lesson for practitioners: don't "
              "assume the only options are privatise or nationalise. Well-designed "
              "<em>collective</em> institutions are often the durable answer."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Rents, Corruption &amp; State Capture"},

        {"type": "content", "label": "Rents", "title": "What economists mean by 'rent'",
         "blocks": [
             {"t": "term", "word": "Economic rent",
              "def": "Income earned above what is needed to keep a resource in its current use "
              "&mdash; a surplus created not by adding value but by scarcity, position or "
              "privilege (a licence, a monopoly, a connection)."},
             {"t": "body", "html": "Not all rent is bad: a temporary innovation rent rewards "
              "risk. The danger is rent created by <em>artificial</em> scarcity &mdash; a permit "
              "you must bribe for, a quota only insiders get."},
         ]},

        {"type": "content", "label": "Rent-Seeking", "title": "Spending resources to capture rents",
         "blocks": [
             {"t": "term", "word": "Rent-seeking",
              "def": "Using resources to obtain an unearned share of existing wealth &mdash; "
              "lobbying for a licence, a tariff, a subsidy &mdash; rather than creating new "
              "wealth. The effort is pure social waste."},
             {"t": "body", "html": "When the most profitable activity is capturing favours rather "
              "than serving customers, talent and capital flow to lobbying, not production. The "
              "whole economy is poorer for it."},
         ]},

        {"type": "content", "label": "License Raj", "title": "A South Asian case: the Licence Raj",
         "blocks": [
             {"t": "body", "html": "India's pre-1991 <strong>Licence Raj</strong> required "
              "permits for capacity, imports and expansion. The system created vast rents: a "
              "licence was worth a fortune, so firms competed to <em>win permits</em> rather than "
              "<em>win markets</em>."},
             {"t": "hbox", "color": "red", "html": "Classic rent-seeking equilibrium: scarce "
              "permits + discretionary officials = bribery, delay, and entrepreneurs who "
              "succeeded by working the ministry, not the market."},
         ]},

        {"type": "content", "label": "Corruption", "title": "Corruption: types and logics",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Type", "What it is", "Example"],
              "rows": [
                  ["Petty", "Small bribes for routine service", "Speed money for a certificate"],
                  ["Grand", "Large-scale theft at the top", "Rigged mega-contracts"],
                  ["Bureaucratic", "Officials extract from citizens", "Inspector demands a cut"],
                  ["Political", "Funds &amp; favours for power", "Donations for policy"],
                  ["State capture", "Rules themselves bought", "Laws written for one firm"]]},
             {"t": "hbox", "color": "amber", "html": "Corruption is not random vice &mdash; it is "
              "a <em>system</em> of incentives. Anti-corruption that ignores the incentives just "
              "moves the bribe."},
         ]},

        {"type": "content", "label": "State Capture", "title": "When the rules themselves are captured",
         "blocks": [
             {"t": "term", "word": "State capture",
              "def": "When private interests so dominate the making of laws, regulations and "
              "appointments that the state's rules are shaped to serve them &mdash; corruption "
              "moved upstream, into the design of the system itself."},
             {"t": "body", "html": "This is the most dangerous form: not breaking the rules, but "
              "<em>writing</em> them. Once captured, a state can look clean on paper while "
              "serving a narrow elite by design."},
         ]},

        {"type": "content", "label": "Elite Capture", "title": "Elite capture of programmes",
         "blocks": [
             {"t": "body", "html": "Even well-meant programmes are vulnerable. "
              "<strong>Elite capture</strong> occurs when local powerful groups divert benefits "
              "&mdash; subsidised inputs, scheme funds, the best plots &mdash; meant for the poor."},
             {"t": "hbox", "color": "red", "html": "A targeting scheme can have flawless rules "
              "and still fail if the village elite control the list. Always ask: <em>who "
              "administers this, and what stops them capturing it?</em>"},
         ]},

        {"type": "content", "label": "Patronage", "title": "Patronage and clientelism",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Patronage", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Jobs, contracts and transfers handed out as "
                   "<em>favours</em> to supporters, not by rule. Loyalty is rewarded; rules bend."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Clientelism", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A standing exchange: politicians deliver "
                   "targeted goods (a road, a ration card) for reliable votes. Benefits are "
                   "<em>contingent</em> on support."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Clientelism is not simply 'bad' &mdash; for "
              "many poor voters it is the only credible way to get the state to deliver. "
              "Understand its logic before trying to replace it."},
         ]},

        {"type": "content", "label": "Breaking Out", "title": "What actually reduces rents",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Remove the scarcity:</strong> abolish needless permits &amp; discretion",
                 "<strong>Transparency:</strong> open data, RTI, social audits, beneficiary lists",
                 "<strong>Rules over discretion:</strong> auctions, lotteries, automatic entitlement",
                 "<strong>Competition:</strong> let entrants erode incumbents' rents",
                 "<strong>Direct delivery:</strong> bypass intermediaries who capture (DBT)"]},
             {"t": "hbox", "color": "cyan", "html": "India's shift to <strong>Direct Benefit "
              "Transfers</strong> is, in political-economy terms, an attack on the intermediaries "
              "who lived off the leakage."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "The Political Economy of Development"},

        {"type": "content", "label": "Big Question", "title": "Why do some late developers catch up?",
         "blocks": [
             {"t": "body", "html": "After 1945, a few economies &mdash; Japan, South Korea, "
              "Taiwan, later China &mdash; transformed from poor to rich in a generation, while "
              "others stagnated. The political economy of development asks what kind of "
              "<strong>state</strong> made the difference."},
             {"t": "hbox", "color": "cyan", "html": "The answer was not simply 'free markets'. It "
              "was a particular relationship between state and capital &mdash; the "
              "<em>developmental state</em>."},
         ]},

        {"type": "content", "label": "Developmental State", "title": "The East Asian developmental state",
         "blocks": [
             {"t": "term", "word": "Developmental state",
              "def": "A state that actively steers economic transformation &mdash; disciplining "
              "and supporting industry, picking sectors, tying subsidies to performance &mdash; "
              "through a capable, relatively autonomous bureaucracy."},
             {"t": "body", "html": "Chalmers Johnson (Japan) and later Alice Amsden (Korea) and "
              "Robert Wade (Taiwan) documented states that did not just fix market failures but "
              "<em>governed</em> the market toward industrialisation."},
         ]},

        {"type": "content", "label": "The Discipline", "title": "Subsidies with strings: reciprocity",
         "blocks": [
             {"t": "body", "html": "The key was <strong>reciprocal control</strong>: the state "
              "gave firms cheap credit and protection, but <em>only</em> if they hit hard export "
              "targets. Underperformers lost support. Subsidy was a contract, not a gift."},
             {"t": "hbox", "color": "amber", "html": "Contrast with rent-seeking: same tools "
              "(subsidy, protection), opposite outcome. The difference is whether the state can "
              "<em>discipline</em> the recipients &mdash; or is captured by them."},
         ]},

        {"type": "content", "label": "Embedded Autonomy", "title": "Embedded autonomy",
         "blocks": [
             {"t": "term", "word": "Embedded autonomy",
              "def": "Peter Evans's term for the developmental state's balance: bureaucrats are "
              "<em>connected</em> to business enough to gather information and coordinate, yet "
              "<em>autonomous</em> enough not to be captured by it."},
             {"t": "hbox", "color": "red", "html": "Too autonomous and the state is blind; too "
              "embedded and it is captured. South Asia's challenge has often been the wrong mix "
              "&mdash; close ties without the autonomy to discipline."},
         ]},

        {"type": "content", "label": "The Resource Curse", "title": "The paradox of plenty",
         "blocks": [
             {"t": "body", "html": "Counter-intuitively, resource-rich countries often grow "
              "<em>slower</em> and govern <em>worse</em>. Oil, gas and minerals generate huge "
              "rents that detach rulers from citizens, fuel conflict, and crowd out other "
              "industry. This is the <strong>resource curse</strong>."},
             {"t": "bullets", "sm": True, "color": "red", "items": [
                 "Rents finance the state without taxing citizens &rarr; less accountability",
                 "A currency boom makes other exports uncompetitive (Dutch disease)",
                 "The prize of capturing rents fuels conflict and corruption"]},
         ]},

        {"type": "content", "label": "Curse Illustrated", "title": "Rents can crowd out accountability",
         "blocks": [
             {"t": "chart", "canvas": "resourceChart",
              "title": "Resource rents (% of GDP) vs governance quality &mdash; illustrative pattern",
              "source": "Illustrative &mdash; schematic of the resource-curse argument",
              "type": "scatter",
              "data": {"datasets": [{"label": "Countries",
                       "data": [{"x": 2, "y": 7.5}, {"x": 4, "y": 7.0}, {"x": 6, "y": 6.2},
                                {"x": 10, "y": 5.5}, {"x": 15, "y": 4.8}, {"x": 20, "y": 4.0},
                                {"x": 28, "y": 3.2}, {"x": 35, "y": 2.6}, {"x": 42, "y": 2.2},
                                {"x": 12, "y": 6.5}, {"x": 30, "y": 4.5}, {"x": 5, "y": 8.0}],
                       "backgroundColor": "#F59E0B", "pointRadius": 6}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Resource rents, % of GDP'} }, y:{ title:{display:true,text:'Governance quality (index)'}, min:0, max:9 } } }"}},
             {"t": "hbox", "color": "amber", "html": "The downward pattern is the resource-curse "
              "claim &mdash; <em>illustrative, not real data</em>. Note the exceptions (Norway, "
              "Botswana): institutions can break the curse."},
         ]},

        {"type": "content", "label": "Premature Deindustrialisation", "title": "Running out of road too soon",
         "blocks": [
             {"t": "term", "word": "Premature deindustrialisation",
              "def": "Dani Rodrik's observation that today's developing countries see "
              "manufacturing's share of jobs and output peak at a much lower income than earlier "
              "industrialisers &mdash; then decline before the country is rich."},
             {"t": "body", "html": "This is acute for South Asia: services and informal work "
              "absorb labour leaving farms, but the high-productivity manufacturing path that "
              "lifted East Asia is narrowing. The escalator is shorter than it used to be."},
         ]},

        {"type": "content", "label": "South Asia's Path", "title": "South Asia's distinctive trajectory",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Services-led growth</strong> (IT, finance) without a mass factory phase",
                 "A vast <strong>informal sector</strong> &mdash; most workers, little protection",
                 "Strong democracy, but a state often <em>embedded</em> without <em>autonomy</em>",
                 "Welfare politics filling the gap manufacturing jobs did not fill"]},
             {"t": "hbox", "color": "cyan", "html": "South Asia is neither East Asia nor a "
              "resource-curse case. Its political economy is its own &mdash; democratic, "
              "informal, and fiercely contested. The later sections turn to it directly."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Political Settlements &amp; Power"},

        {"type": "content", "label": "The Gap", "title": "Why 'best-practice' reforms keep failing",
         "blocks": [
             {"t": "body", "html": "Donors export the institutions of rich countries &mdash; "
              "independent regulators, merit bureaucracies, anti-corruption agencies &mdash; and "
              "watch them wither. The institutions are real on paper but powerless in practice. "
              "Why?"},
             {"t": "hbox", "color": "amber", "html": "Because institutions sit on top of an "
              "underlying <em>distribution of power</em>. Graft a new rule onto an unchanged "
              "balance of power and the power, not the rule, prevails."},
         ]},

        {"type": "content", "label": "Mushtaq Khan", "title": "Khan: the political settlement",
         "blocks": [
             {"t": "term", "word": "Political settlement",
              "def": "Mushtaq Khan: the underlying balance or distribution of power between "
              "contending groups in a society, and the institutions that are compatible with it. "
              "Institutions survive only if they are consistent with this balance."},
             {"t": "body", "html": "Khan's key move: stop asking 'are these the right "
              "institutions?' and start asking 'are these institutions <em>compatible</em> with "
              "how power is actually distributed here?'"},
         ]},

        {"type": "content", "label": "Holding Power", "title": "Holding power decides what sticks",
         "blocks": [
             {"t": "term", "word": "Holding power",
              "def": "A group's capacity to benefit itself in conflicts &mdash; its ability to "
              "fight, disrupt, withhold cooperation or impose costs. It comes from organisation, "
              "wealth, numbers or violence, and need not match formal authority."},
             {"t": "hbox", "color": "red", "html": "A reform that hurts a group with strong "
              "holding power will be blocked, diluted or reversed &mdash; whatever the law says. "
              "Map holding power before you map the law."},
         ]},

        {"type": "content", "label": "The Diagram", "title": "Power, institutions and outcomes",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:8px 0;">'
                 '<svg viewBox="0 0 560 270" width="560" height="250" xmlns="http://www.w3.org/2000/svg" '
                 'style="max-width:100%;height:auto;font-family:inherit">'
                 '<rect x="20" y="100" width="150" height="58" rx="8" fill="#EF4444" fill-opacity="0.12" '
                 'stroke="#EF4444" stroke-width="2"/>'
                 '<text x="95" y="126" text-anchor="middle" fill="#EF4444" font-size="13">Distribution</text>'
                 '<text x="95" y="144" text-anchor="middle" fill="#EF4444" font-size="13">of power</text>'
                 '<rect x="205" y="100" width="150" height="58" rx="8" fill="#0EA5E9" fill-opacity="0.12" '
                 'stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="280" y="126" text-anchor="middle" fill="#0EA5E9" font-size="13">Institutions</text>'
                 '<text x="280" y="144" text-anchor="middle" fill="#94A3B8" font-size="11">(formal &amp; informal)</text>'
                 '<rect x="390" y="100" width="150" height="58" rx="8" fill="#10B981" fill-opacity="0.12" '
                 'stroke="#10B981" stroke-width="2"/>'
                 '<text x="465" y="126" text-anchor="middle" fill="#10B981" font-size="13">Economic</text>'
                 '<text x="465" y="144" text-anchor="middle" fill="#10B981" font-size="13">outcomes</text>'
                 '<path d="M170,129 L203,129" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#psh)"/>'
                 '<path d="M355,129 L388,129" fill="none" stroke="#334155" stroke-width="2" marker-end="url(#psh)"/>'
                 # feedback loop
                 '<path d="M465,160 Q465,225 280,225 Q95,225 95,160" fill="none" stroke="#6366F1" '
                 'stroke-width="2" stroke-dasharray="5,4" marker-end="url(#psh2)"/>'
                 '<text x="280" y="248" text-anchor="middle" fill="#6366F1" font-size="12">'
                 'outcomes reshape power &mdash; the settlement evolves</text>'
                 '<text x="280" y="50" text-anchor="middle" fill="#94A3B8" font-size="12">'
                 'institutions stick only if compatible with the power below them</text>'
                 '<defs><marker id="psh" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
                 '<path d="M0,0 L7,3 L0,6 Z" fill="#334155"/></marker>'
                 '<marker id="psh2" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
                 '<path d="M0,0 L7,3 L0,6 Z" fill="#6366F1"/></marker></defs>'
                 '</svg></div>')},
             {"t": "hbox", "color": "cyan", "html": "Read left to right, then the feedback loop: "
              "power shapes institutions, institutions shape outcomes, and outcomes feed back to "
              "reshape power. Reform enters this loop &mdash; it does not float above it."},
         ]},

        {"type": "content", "label": "Informal Institutions", "title": "The unwritten rules that really bind",
         "blocks": [
             {"t": "body", "html": "<strong>Informal institutions</strong> &mdash; norms, "
              "conventions, networks of caste, kin and patronage &mdash; often govern behaviour "
              "more powerfully than the formal law. A bribe norm, a caste hierarchy, an "
              "understanding about 'whose turn' it is can override any statute."},
             {"t": "hbox", "color": "amber", "html": "Practitioners who design only for the "
              "formal rules are repeatedly ambushed by the informal ones. Map both."},
         ]},

        {"type": "content", "label": "Why Reforms Stall", "title": "The anatomy of a stalled reform",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["The reform aims to&hellip;", "But the settlement&hellip;", "So&hellip;"],
              "rows": [
                  ["Remove a subsidy", "Empowers those who capture it", "It is restored after protests"],
                  ["Build merit hiring", "Rests on patronage networks", "Postings stay political"],
                  ["Empower a regulator", "Favours the firms regulated", "The regulator is captured"],
                  ["Target the poor", "Runs through local elites", "Benefits leak upward"]]},
             {"t": "hbox", "color": "red", "html": "In each case the reform is technically fine "
              "and politically dead. The settlement, not the design, is the binding constraint."},
         ]},

        {"type": "content", "label": "Productive Use", "title": "Working with the settlement, not against it",
         "blocks": [
             {"t": "body", "html": "Khan's framework is not counsel of despair. It directs effort "
              "to reforms that are <em>compatible</em> with the existing balance &mdash; or that "
              "shift it gradually &mdash; rather than ideal reforms that the powerful will simply "
              "kill."},
             {"t": "hbox", "color": "green", "html": "Sometimes the win is to channel rents "
              "toward productive ends (as East Asia did), not to abolish them frontally. Feasible "
              "and second-best can beat ideal and dead."},
         ]},

        {"type": "content", "label": "Settlements Compared", "title": "Types of political settlement",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "More inclusive / stable", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Power broadly shared, ruling coalition "
                   "wide, longer horizons. Easier to make credible long-term commitments and "
                   "discipline rent recipients."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Narrow / contested", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Power concentrated or fiercely fought "
                   "over, short horizons, weak commitment. Reforms are fragile; rents buy "
                   "short-term loyalty."}]}]},
             {"t": "hbox", "color": "amber", "html": "Diagnosing <em>which</em> settlement you "
              "are in tells you which reforms are even possible. This is the bridge to PEA."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Political Economy Analysis in Practice"},

        {"type": "content", "label": "From Theory to Tool", "title": "What is Political Economy Analysis?",
         "blocks": [
             {"t": "term", "word": "Political Economy Analysis (PEA)",
              "def": "A structured way to understand how power, interests and institutions shape "
              "a development problem &mdash; so that programmes are designed for the world as it "
              "is, not as it should be."},
             {"t": "body", "html": "PEA took the theory of Sections 1&ndash;8 and turned it into "
              "a practical diagnostic now used across DFID/FCDO, the World Bank, USAID and many "
              "NGOs. It is the working analyst's main political-economy tool."},
         ]},

        {"type": "content", "label": "Problem-Driven", "title": "Problem-driven, not country-wide",
         "blocks": [
             {"t": "body", "html": "Early PEA produced sweeping country studies that sat on "
              "shelves. The influential shift &mdash; led by analysts like David Booth &mdash; was "
              "to <strong>problem-driven PEA</strong>: start from a specific, concrete problem "
              "your programme faces, not the whole nation."},
             {"t": "hbox", "color": "cyan", "html": "Ask 'why does this school have teachers who "
              "don't show up?' &mdash; not 'analyse the political economy of education in "
              "country X'. Specific questions get usable answers."},
         ]},

        {"type": "content", "label": "The SIA Frame", "title": "Structures, institutions, actors",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 460 300" width="460" height="280" xmlns="http://www.w3.org/2000/svg" '
                 'style="max-width:100%;height:auto;font-family:inherit">'
                 # triangle outline
                 '<polygon points="230,30 60,260 400,260" fill="none" stroke="#334155" stroke-width="2"/>'
                 # structures (top)
                 '<circle cx="230" cy="30" r="6" fill="#6366F1"/>'
                 '<text x="230" y="20" text-anchor="middle" fill="#6366F1" font-size="14">STRUCTURES</text>'
                 '<text x="230" y="52" text-anchor="middle" fill="#94A3B8" font-size="11">deep, slow:</text>'
                 '<text x="230" y="68" text-anchor="middle" fill="#94A3B8" font-size="11">history, geography, economy</text>'
                 # institutions (bottom-left)
                 '<circle cx="60" cy="260" r="6" fill="#0EA5E9"/>'
                 '<text x="60" y="284" text-anchor="middle" fill="#0EA5E9" font-size="14">INSTITUTIONS</text>'
                 '<text x="60" y="246" text-anchor="middle" fill="#94A3B8" font-size="11">rules,</text>'
                 '<text x="60" y="230" text-anchor="middle" fill="#94A3B8" font-size="11">norms</text>'
                 # actors (bottom-right)
                 '<circle cx="400" cy="260" r="6" fill="#10B981"/>'
                 '<text x="400" y="284" text-anchor="middle" fill="#10B981" font-size="14">ACTORS</text>'
                 '<text x="400" y="246" text-anchor="middle" fill="#94A3B8" font-size="11">interests,</text>'
                 '<text x="400" y="230" text-anchor="middle" fill="#94A3B8" font-size="11">incentives, power</text>'
                 '<text x="230" y="160" text-anchor="middle" fill="#F59E0B" font-size="12">a problem sits</text>'
                 '<text x="230" y="178" text-anchor="middle" fill="#F59E0B" font-size="12">inside all three</text>'
                 '</svg></div>')},
             {"t": "hbox", "color": "cyan", "html": "The standard PEA frame: deep "
              "<strong>structures</strong> set the stage, <strong>institutions</strong> set the "
              "rules, and <strong>actors</strong> pursue interests within them. Diagnose all three."},
         ]},

        {"type": "content", "label": "Structures", "title": "Structures: the slow-moving stage",
         "blocks": [
             {"t": "body", "html": "<strong>Structures</strong> are the deep, slow-changing "
              "features that constrain everyone: economic geography, demography, the resource "
              "base, history, the global position, social structure (caste, class, ethnicity)."},
             {"t": "hbox", "color": "amber", "html": "You cannot change structures in a project "
              "cycle &mdash; but ignoring them guarantees failure. They define the space of the "
              "possible."},
         ]},

        {"type": "content", "label": "Institutions", "title": "Institutions: formal and informal rules",
         "blocks": [
             {"t": "body", "html": "Within structures sit <strong>institutions</strong> &mdash; "
              "the formal rules (laws, mandates, budgets, electoral systems) and the informal "
              "ones (norms, patronage, 'how things are really done')."},
             {"t": "hbox", "color": "red", "html": "The recurring PEA finding: the informal "
              "rules usually dominate. Map the gap between the rules on paper and the rules in "
              "practice &mdash; that gap is where your problem lives."},
         ]},

        {"type": "content", "label": "Actors", "title": "Actors: interests, incentives, power",
         "blocks": [
             {"t": "body", "html": "Finally the <strong>actors</strong>: who has a stake, what "
              "they want, what they stand to gain or lose, and how much power they have to act on "
              "it. This is the most operational layer &mdash; the one you can actually engage."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Interests:</strong> what does each actor materially want?",
                 "<strong>Incentives:</strong> what is the system rewarding them to do?",
                 "<strong>Power:</strong> how able are they to get it &mdash; or to block you?"]},
         ]},

        {"type": "content", "label": "TWP", "title": "Thinking and working politically",
         "blocks": [
             {"t": "body", "html": "<strong>Thinking and Working Politically (TWP)</strong> turns "
              "PEA from a one-off report into a way of operating: read the politics continuously, "
              "back local reformers, stay flexible, and adapt as the situation shifts."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Politics is the main event, not a risk in the margins",
                 "Back locally legitimate change &mdash; don't impose blueprints",
                 "Adapt iteratively: small bets, fast learning, course-correct"]},
         ]},

        {"type": "content", "label": "Caution", "title": "PEA is a lens, not a crystal ball",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "It can rationalise inaction &mdash; 'too political, do nothing'",
                 "It can be used to justify whatever the funder already wanted",
                 "Power maps date fast &mdash; yesterday's analysis misleads tomorrow",
                 "Analysts have interests too &mdash; PEA needs PEA"]},
             {"t": "hbox", "color": "amber", "html": "Use PEA to find <em>feasible action</em>, "
              "not as an excuse for paralysis or as cover for a predetermined plan."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Applying PEA"},

        {"type": "content", "label": "Step One", "title": "Start from a concrete problem",
         "blocks": [
             {"t": "body", "html": "Good applied PEA begins by naming the problem sharply: not "
              "'weak governance' but 'frontline health workers are absent three days a week in "
              "this district'. The sharper the problem, the more usable the analysis."},
             {"t": "flow", "steps": [
                 "NAME the problem precisely",
                 "MAP the actors around it",
                 "TRACE their interests &amp; incentives",
                 "FIND a feasible entry point"]},
         ]},

        {"type": "content", "label": "Stakeholder Mapping", "title": "Map interests against power",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 460 300" width="460" height="280" xmlns="http://www.w3.org/2000/svg" '
                 'style="max-width:100%;height:auto;font-family:inherit">'
                 # axes
                 '<line x1="60" y1="250" x2="430" y2="250" stroke="#334155" stroke-width="2"/>'
                 '<line x1="60" y1="250" x2="60" y2="20" stroke="#334155" stroke-width="2"/>'
                 '<text x="245" y="280" text-anchor="middle" fill="#94A3B8" font-size="12">Support for reform &rarr;</text>'
                 '<text x="20" y="135" text-anchor="middle" fill="#94A3B8" font-size="12" transform="rotate(-90 20 135)">Power &rarr;</text>'
                 # quadrant guides
                 '<line x1="245" y1="20" x2="245" y2="250" stroke="#1E293B" stroke-width="1" stroke-dasharray="4,4"/>'
                 '<line x1="60" y1="135" x2="430" y2="135" stroke="#1E293B" stroke-width="1" stroke-dasharray="4,4"/>'
                 # quadrant labels
                 '<text x="150" y="50" text-anchor="middle" fill="#EF4444" font-size="12">BLOCKERS</text>'
                 '<text x="150" y="66" text-anchor="middle" fill="#94A3B8" font-size="10">powerful, opposed</text>'
                 '<text x="345" y="50" text-anchor="middle" fill="#10B981" font-size="12">CHAMPIONS</text>'
                 '<text x="345" y="66" text-anchor="middle" fill="#94A3B8" font-size="10">powerful, supportive</text>'
                 '<text x="150" y="210" text-anchor="middle" fill="#F59E0B" font-size="12">LATENT FOES</text>'
                 '<text x="345" y="210" text-anchor="middle" fill="#0EA5E9" font-size="12">ALLIES TO BUILD</text>'
                 # sample dots
                 '<circle cx="160" cy="80" r="7" fill="#EF4444"/>'
                 '<circle cx="350" cy="90" r="7" fill="#10B981"/>'
                 '<circle cx="320" cy="200" r="7" fill="#0EA5E9"/>'
                 '<circle cx="140" cy="195" r="7" fill="#F59E0B"/>'
                 '</svg></div>')},
             {"t": "hbox", "color": "cyan", "html": "Plot each actor by power and stance. Your "
              "strategy: empower champions, build up allies, neutralise or split blockers, watch "
              "latent foes. Position dictates tactic."},
         ]},

        {"type": "content", "label": "Incentives", "title": "Follow the incentives, not the org chart",
         "blocks": [
             {"t": "body", "html": "An official's <em>job description</em> says one thing; the "
              "<em>incentives</em> they actually face &mdash; transfers, postings, side-income, "
              "political loyalty &mdash; often say another. PEA asks what behaviour the system is "
              "really rewarding."},
             {"t": "hbox", "color": "amber", "html": "If absent teachers are never sanctioned and "
              "present ones are not rewarded, absence is the rational response. Fix the incentive, "
              "not just the rule."},
         ]},

        {"type": "content", "label": "Entry Points", "title": "Finding a feasible entry point",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Where interests align:</strong> a reform that also serves a powerful actor",
                 "<strong>A reform champion:</strong> an insider with power and will to act",
                 "<strong>A window:</strong> a crisis, election or scandal that shifts the balance",
                 "<strong>A small win:</strong> a feasible first step that builds a coalition"]},
             {"t": "hbox", "color": "green", "html": "You rarely move the whole settlement. You "
              "look for the seam &mdash; the place where a feasible push meets a willing ally and "
              "an open window."},
         ]},

        {"type": "content", "label": "Coalitions", "title": "Build the coalition the reform needs",
         "blocks": [
             {"t": "body", "html": "Recall Section 1: reforms have concentrated losers and "
              "diffuse winners. The political-economy task is to <strong>organise the winners</strong> "
              "&mdash; give the diffuse beneficiaries a champion, a voice, and a stake worth "
              "defending."},
             {"t": "hbox", "color": "cyan", "html": "Transparency tools &mdash; social audits, "
              "published beneficiary lists, RTI &mdash; work partly because they help the diffuse "
              "many see and defend their stake."},
         ]},

        {"type": "content", "label": "Limits of Best Practice", "title": "Why 'best practice' travels badly",
         "blocks": [
             {"t": "body", "html": "What worked in Rwanda or Korea rests on <em>that</em> "
              "settlement, <em>that</em> capacity, <em>that</em> history. Transplanted whole, "
              "'best practice' becomes <strong>isomorphic mimicry</strong> &mdash; the form "
              "copied, the function absent."},
             {"t": "term", "word": "Isomorphic mimicry",
              "def": "Pritchett, Woolcock &amp; Andrews: when states adopt the <em>appearance</em> "
              "of capable institutions (the law, the agency, the policy) to gain legitimacy, "
              "while the underlying function never actually works."},
         ]},

        {"type": "content", "label": "PDIA", "title": "Problem-driven iterative adaptation",
         "blocks": [
             {"t": "body", "html": "The constructive response is <strong>PDIA</strong> &mdash; "
              "Problem-Driven Iterative Adaptation: start from a locally-felt problem, take small "
              "steps, learn fast from what works, and let solutions emerge rather than importing "
              "them."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Solve <em>local</em> problems, not imported templates",
                 "Create space for iteration &mdash; permission to experiment and fail",
                 "Build capability by doing, not by passing a law that mimics one"]},
         ]},

        {"type": "content", "label": "Case", "title": "A worked example: cleaning up a transfer scheme",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["PEA question", "Finding (illustrative)", "Implication"],
              "rows": [
                  ["What's the problem?", "Pensions don't reach the elderly poor", "Define narrowly, by district"],
                  ["Who are the actors?", "Officials, middlemen, local leaders, elders", "Map power vs stance"],
                  ["What are the incentives?", "Middlemen profit from the leakage", "They will block reform"],
                  ["Where's the entry point?", "Digital payments + public lists", "Cut the middleman, arm the poor"],
                  ["Who's the champion?", "A reformist district officer", "Back them; protect them"]]},
             {"t": "hbox", "color": "cyan", "html": "Notice the whole course at work: rents, "
              "capture, collective action, incentives, settlement &mdash; converging on one "
              "feasible move."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "India / South Asia &amp; Further Reading"},

        {"type": "content", "label": "The Indian State", "title": "What kind of state is India's?",
         "blocks": [
             {"t": "body", "html": "India is a paradox: a durable democracy with a vast, "
              "ambitious state that often delivers poorly. Its political economy is shaped by "
              "democratic competition, deep social cleavages, and a powerful but unevenly "
              "capable bureaucracy."},
             {"t": "hbox", "color": "cyan", "html": "Understanding it means holding several "
              "things at once: electoral democracy, caste, class, federalism and a still-large "
              "informal economy."},
         ]},

        {"type": "content", "label": "Bardhan", "title": "Bardhan: the dominant proprietary classes",
         "blocks": [
             {"t": "body", "html": "<strong>Pranab Bardhan</strong>, in <em>The Political Economy "
              "of Development in India</em> (1984), argued that India's slow growth reflected a "
              "stand-off between three <strong>dominant proprietary classes</strong> &mdash; "
              "industrial capitalists, rich farmers, and the professional/bureaucratic elite."},
             {"t": "hbox", "color": "amber", "html": "None could dominate; each could veto. The "
              "result was a state that spread subsidies across all three rather than investing "
              "decisively &mdash; a settlement of mutual blocking."},
         ]},

        {"type": "content", "label": "Kohli", "title": "Kohli: states and industrialisation",
         "blocks": [
             {"t": "body", "html": "<strong>Atul Kohli</strong> compared how different states "
              "drive (or fail to drive) industrial transformation. In the Indian case he traced "
              "the shift toward a closer <strong>state&ndash;business alliance</strong> and a "
              "more pro-business (not always pro-market) tilt from the 1980s."},
             {"t": "hbox", "color": "cyan", "html": "Kohli's distinction matters: "
              "<em>pro-business</em> (favouring existing firms and their profits) is not the same "
              "as <em>pro-market</em> (favouring competition and entry). India often chose the "
              "former."},
         ]},

        {"type": "content", "label": "Federal Bargains", "title": "Federalism: the bargaining state",
         "blocks": [
             {"t": "body", "html": "India's federalism is a continuous bargain between the Centre "
              "and the states over taxes, transfers and authority &mdash; mediated by the Finance "
              "Commission, the GST Council and party competition. Much of India's political "
              "economy is this Centre&ndash;state negotiation."},
             {"t": "hbox", "color": "amber", "html": "For practitioners: which tier holds the "
              "money, the mandate and the staff for <em>your</em> issue is a first-order "
              "question. The bargain shapes what is implementable."},
         ]},

        {"type": "content", "label": "Caste &amp; Capital", "title": "Caste, class and capital",
         "blocks": [
             {"t": "body", "html": "Caste is not a residue of the past but an active force in "
              "India's political economy &mdash; structuring access to land, credit, networks, "
              "education and the state itself. Class and caste overlap and cross-cut in ways no "
              "purely economic analysis captures."},
             {"t": "hbox", "color": "red", "html": "Any PEA in India that treats actors as "
              "caste-blind will misread both interests and power. Who benefits is rarely "
              "separable from who belongs."},
         ]},

        {"type": "content", "label": "Welfare Politics", "title": "The new welfare politics",
         "blocks": [
             {"t": "body", "html": "Recent decades brought a wave of rights and transfers &mdash; "
              "<strong>MGNREGA, the food security and forest rights acts, DBT, free rations and "
              "cash schemes</strong>. This welfare expansion is itself a political-economy "
              "phenomenon: competitive democracy delivering to the poor as voters."},
             {"t": "hbox", "color": "green", "html": "Read these as the double movement and "
              "clientelism at once &mdash; protection against markets <em>and</em> a currency of "
              "electoral exchange. Both readings are true."},
         ]},

        {"type": "content", "label": "South Asia", "title": "The wider region",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Pakistan &amp; Bangladesh:</strong> Mushtaq Khan's settlements work "
                 "draws heavily on them",
                 "<strong>Bangladesh:</strong> NGO-led delivery (BRAC, Grameen) reshaping the state's role",
                 "<strong>Sri Lanka &amp; Nepal:</strong> how ethnic &amp; regional cleavages shape settlements",
                 "<strong>Common threads:</strong> informality, patronage, contested federalism, agrarian power"]},
             {"t": "hbox", "color": "cyan", "html": "The frameworks travel; the settlements "
              "differ. Always ground the theory in the specific country's distribution of power."},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "A short reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Why Nations Fail</em> &mdash; Acemoglu &amp; Robinson (institutions)",
                 "<em>The Great Transformation</em> &mdash; Karl Polanyi (markets &amp; society)",
                 "<em>Governing the Commons</em> &mdash; Elinor Ostrom (collective action)",
                 "<em>The Political Economy of Development in India</em> &mdash; Pranab Bardhan",
                 "<em>Political Settlements</em> &amp; PEA toolkits &mdash; Mushtaq Khan; ODI / DLP"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Development Economics</strong>, <strong>Indian Constitution</strong> and "
              "<strong>Decolonising Development</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Politics and economics are one system</strong> &mdash; who gets what, how",
                 "<strong>Institutions are the rules of the game</strong> &mdash; and they shape incentives",
                 "<strong>Concentrated interests beat diffuse ones</strong> &mdash; organise the winners",
                 "<strong>Reforms stick only if compatible with power</strong> &mdash; read the settlement",
                 "<strong>Design for the world as it is</strong> &mdash; find feasible entry points"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Political Economy 101 &middot; Complete",
         "headline": "Now read the power<br>behind the policy.",
         "byline": "Good economics is rarely enough. The reforms that last are the ones designed "
                   "for the real distribution of power &mdash; so map the interests, find the "
                   "feasible entry point, and organise the winners. Explore the rest of the "
                   "ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
