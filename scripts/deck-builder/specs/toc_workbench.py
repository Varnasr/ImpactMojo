# -*- coding: utf-8 -*-
"""
Theory of Change 101 — ImpactMojo 101 Series (native deck spec)
A practical workbench for development practitioners in programme design and M&E.
Build: python3 scripts/deck-builder/build.py toc_workbench
"""

DECK = {
    "slug": "toc-workbench",
    "title": "Theory of Change 101",
    "description": ("Theory of Change 101 — a free, practical course for development "
                    "practitioners in programme design and M&E across South Asia: build a "
                    "causal map from activities to long-term change, surface assumptions, "
                    "choose indicators, draw the outcome pathway, dodge the common pitfalls "
                    "and use a ToC across the whole programme cycle. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Theory of<br>Change<br>101",
         "sub": "Mapping the Causal Path from Activities to Long-Term Change &mdash; a "
                "Practical Workbench for Programme Design &amp; M&amp;E in South Asia",
         "tags": ["Methods &amp; Diagrams", "Design &amp; MEL", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What a Theory of Change Is"},
             {"name": "Why ToC Matters"},
             {"name": "ToC vs Logframe vs Results Chain"},
             {"name": "The Building Blocks"},
             {"name": "Backwards Mapping"},
             {"name": "Assumptions &amp; Rationale"},
             {"name": "Indicators &amp; Evidence"},
             {"name": "Drawing the ToC"},
             {"name": "Common Pitfalls"},
             {"name": "Using ToC Across the Cycle"},
             {"name": "Worked Example &amp; Further Reading"},
         ]},

        # ===================== SECTION 01 — What a ToC is (8) =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What a Theory of Change Is"},

        {"type": "content", "label": "Definition", "title": "A theory of change is a causal map",
         "blocks": [
             {"t": "body", "html": "A <strong>theory of change (ToC)</strong> is an explicit, "
              "testable account of how and why a set of activities is expected to lead to "
              "long-term change. It connects what you do to the change you seek &mdash; and "
              "names the assumptions that have to hold for that chain to work."},
             {"t": "term", "word": "Theory of change",
              "def": "A comprehensive description of how and why a desired change is expected to "
              "happen in a particular context &mdash; mapping the pathway from activities through "
              "outcomes to a long-term goal, with the assumptions made explicit."},
             {"t": "hbox", "color": "cyan", "html": "It is not a wish list. It is an "
              "<em>argument</em> about cause and effect that you can examine, test and revise."},
         ]},

        {"type": "content", "label": "The Shape", "title": "From activities to long-term change",
         "blocks": [
             {"t": "flow", "steps": [
                 "ACTIVITIES: what we do &mdash; train, equip, convene",
                 "OUTPUTS: what we deliver &mdash; teachers trained",
                 "OUTCOMES: what changes in others &mdash; better teaching, more learning",
                 "IMPACT: the long-term change &mdash; an educated generation"]},
             {"t": "hbox", "color": "amber", "html": "The arrows are the heart of a ToC. Each "
              "one is a claim: <em>because</em> this happened, that becomes possible."},
         ]},

        {"type": "content", "label": "What It Is Not", "title": "A ToC is not just a list of activities",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Not this", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "A list of things the project will do",
                      "A budget or a workplan",
                      "A logframe filled in after the fact",
                      "A diagram drawn to please a donor"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "But this", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "A causal account of how change happens",
                      "An explicit set of assumptions",
                      "A shared, testable hypothesis",
                      "A living tool you revisit and revise"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "If your ToC could be redrawn from the "
              "activity list alone, it is not yet a theory of change &mdash; it is a plan."},
         ]},

        {"type": "content", "label": "Origins", "title": "Where the idea comes from",
         "blocks": [
             {"t": "body", "html": "The ToC approach grew out of <strong>programme evaluation</strong>. "
              "Carol Weiss argued in 1995 that complex community initiatives kept failing "
              "evaluation because their underlying theories &mdash; the assumptions about how and "
              "why they would work &mdash; were left unstated and untested."},
             {"t": "quote",
              "text": "The concept of grounding evaluation in theories of change takes for "
              "granted that social programs are based on explicit or implicit theories about how "
              "and why the program will work.",
              "attr": "&mdash; Carol H. Weiss, 1995"},
         ]},

        {"type": "content", "label": "The Field Grew", "title": "From evaluation idea to design tool",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Who", "Contribution", "Era"],
              "rows": [
                  ["Carol Weiss", "Named theory-based evaluation of complex initiatives", "1995"],
                  ["Aspen Institute Roundtable", "Popularised ToC for community initiatives", "1990s"],
                  ["ActKnowledge", "Built the backwards-mapping &amp; outcomes-framework method", "2000s"],
                  ["Comic Relief", "Embedded ToC in grant-making practice", "2000s&ndash;10s"],
                  ["Isabel Vogel (for DFID)", "Reviewed ToC use in international development", "2012"]]},
             {"t": "hbox", "color": "amber", "html": "ToC migrated from a way to <em>evaluate</em> "
              "programmes to a way to <em>design</em> them &mdash; and now does both."},
         ]},

        {"type": "content", "label": "Two Faces", "title": "A diagram and a narrative",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The diagram", "blocks": [
                  {"t": "body", "cls": "sm", "html": "An <strong>outcomes map</strong> &mdash; "
                   "boxes for changes, arrows for causal links, working back from the goal."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "The narrative", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A written <strong>story</strong> that "
                   "explains each pathway, spells out the assumptions, and justifies the logic "
                   "with evidence and rationale."}]}]},
             {"t": "hbox", "color": "green", "html": "You need both. A diagram without a narrative "
              "is decoration; a narrative without a diagram is hard to test."},
         ]},

        {"type": "content", "label": "Context", "title": "Change happens in a context, not a vacuum",
         "blocks": [
             {"t": "body", "html": "A ToC is always anchored in a specific <strong>context</strong> "
              "&mdash; the place, the people, the politics, the existing services. The same "
              "activity can produce different outcomes in different settings, so a ToC that "
              "travels well names the context it assumes."},
             {"t": "hbox", "color": "amber", "html": "Ask early: what about <em>this</em> district, "
              "this community, this moment makes our causal story plausible &mdash; or fragile?"},
         ]},

        {"type": "content", "label": "Why Bother", "title": "Making the implicit explicit",
         "blocks": [
             {"t": "body", "html": "Every programme already has a theory of change &mdash; in "
              "someone's head. The discipline of a ToC is to drag it into the open where the "
              "whole team can see it, argue with it, and improve it before the money is spent."},
             {"t": "quote",
              "text": "Theory of change is essentially a comprehensive description of how and why "
              "a desired change is expected to happen in a particular context.",
              "attr": "&mdash; widely used working definition (after ActKnowledge / Aspen)"},
         ]},

        # ===================== SECTION 02 — Why ToC matters (8) =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Why ToC Matters"},

        {"type": "content", "label": "Four Jobs", "title": "What a ToC actually does for you",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Shared understanding", "label": "A whole team agrees on how change happens", "color": "cyan"},
                 {"num": "Better design", "label": "Gaps and leaps surface before delivery", "color": "green"},
                 {"num": "Sharper evaluation", "label": "You know what to measure and why", "color": "indigo"},
                 {"num": "Faster learning", "label": "Surprises become tests of the theory", "color": "amber"}]},
             {"t": "hbox", "color": "cyan", "html": "These four pay-offs &mdash; design, "
              "alignment, evaluation and learning &mdash; are why funders increasingly ask for a "
              "ToC, not just a logframe."},
         ]},

        {"type": "content", "label": "Where Effort Goes", "title": "A ToC shifts attention up the chain",
         "blocks": [
             {"t": "chart", "canvas": "tocFocusChart",
              "title": "Where a logframe vs a ToC tends to concentrate thinking (illustrative)",
              "source": "Illustrative &mdash; for teaching only",
              "type": "bar",
              "data": {"labels": ["Activities", "Outputs", "Outcomes", "Assumptions", "Impact"],
                       "datasets": [
                           {"label": "Logframe focus",
                            "data": [35, 30, 20, 10, 5], "backgroundColor": "#6366F1"},
                           {"label": "Theory of change focus",
                            "data": [10, 15, 30, 30, 15], "backgroundColor": "#10B981"}]},
              "options": {"__js__": "{ scales:{ y:{ min:0, max:40, title:{display:true,text:'relative attention (%)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative, not measured &mdash; the point "
              "is direction: a ToC pulls effort toward outcomes and the assumptions behind them."},
         ]},

        {"type": "content", "label": "ToC vs Plan", "title": "A theory, not a plan",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "A plan", "A theory of change"],
              "rows": [
                  ["Asks", "What will we do, by when?", "How &amp; why does change happen?"],
                  ["Direction", "Forward from activities", "Backward from the goal"],
                  ["Centre of gravity", "Activities &amp; milestones", "Outcomes &amp; assumptions"],
                  ["Tests", "Did we do it on time?", "Did the causal logic hold?"],
                  ["When wrong", "We were late", "Our theory was wrong &mdash; we learn"]]},
             {"t": "hbox", "color": "amber", "html": "A plan can be delivered perfectly and still "
              "change nothing. A ToC asks whether doing it should change anything at all."},
         ]},

        {"type": "content", "label": "Alignment", "title": "One picture the whole team can argue with",
         "blocks": [
             {"t": "body", "html": "Programme staff, finance, M&amp;E, partners and the community "
              "often hold different, unspoken theories of how the work will help. A shared ToC "
              "surfaces those differences early &mdash; while they are cheap to resolve."},
             {"t": "hbox", "color": "green", "html": "The argument you have over a draft ToC in a "
              "workshop is far cheaper than the argument you have over a failed evaluation."},
         ]},

        {"type": "content", "label": "Design", "title": "It exposes the weak links",
         "blocks": [
             {"t": "body", "html": "Laying out the pathway makes <strong>missing steps</strong> "
              "and <strong>leaps of logic</strong> visible. If training teachers is supposed to "
              "improve learning, the ToC forces you to show every link in between &mdash; and to "
              "notice where one is missing."},
             {"t": "flow", "steps": [
                 "Train teachers",
                 "??? do they change practice ???",
                 "??? do students engage more ???",
                 "Learning improves"]},
             {"t": "hbox", "color": "red", "html": "Those question marks are exactly the "
              "conversations a good ToC forces you to have <em>before</em> you commit funds."},
         ]},

        {"type": "content", "label": "Evaluation", "title": "It tells the evaluator what to measure",
         "blocks": [
             {"t": "body", "html": "A ToC is the backbone of <strong>theory-based evaluation</strong>. "
              "Each outcome on the map is something to measure; each assumption is something to "
              "test. Evaluation stops being a verdict and becomes an inquiry into <em>which links "
              "held and which broke</em>."},
             {"t": "hbox", "color": "indigo", "html": "When a programme underperforms, a ToC lets "
              "you ask the useful question: did we fail to deliver, or was the theory wrong?"},
         ]},

        {"type": "content", "label": "Learning", "title": "Surprises become evidence",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Without a ToC", "blocks": [
                  {"t": "body", "cls": "sm", "html": "An unexpected result is just bad news to "
                   "explain away or bury in the annual report."}]}],
              "right": [{"t": "panel", "color": "green", "title": "With a ToC", "blocks": [
                  {"t": "body", "cls": "sm", "html": "An unexpected result tells you precisely "
                   "which assumption was wrong &mdash; and where to adapt next."}]}]},
             {"t": "hbox", "color": "cyan", "html": "A ToC turns &lsquo;it didn't work&rsquo; into "
              "&lsquo;here is the link that broke, and here is what we now believe instead.&rsquo;"},
         ]},

        {"type": "content", "label": "Accountability", "title": "Honest about what you can claim",
         "blocks": [
             {"t": "body", "html": "A ToC clarifies your <strong>sphere of control</strong> "
              "(activities and outputs), your <strong>sphere of influence</strong> (outcomes you "
              "contribute to), and the <strong>sphere of interest</strong> (impact shaped by many "
              "actors). It keeps you from over-claiming credit."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Control", "label": "Activities &amp; outputs you own", "color": "cyan"},
                 {"num": "Influence", "label": "Outcomes you contribute to", "color": "amber"},
                 {"num": "Interest", "label": "Impact shaped by many", "color": "red"}]},
         ]},

        # ===================== SECTION 03 — ToC vs logframe vs results chain (8) =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "ToC vs Logframe vs Results Chain"},

        {"type": "content", "label": "Three Cousins", "title": "Related tools, different jobs",
         "blocks": [
             {"t": "body", "html": "ToC, the <strong>logframe</strong> and the <strong>results "
              "chain</strong> are cousins, not rivals. They share the activities&ndash;to&ndash;impact "
              "logic but differ in form, richness and what they make visible."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Results chain", "label": "The linear backbone: inputs &rarr; impact", "color": "cyan"},
                 {"num": "Logframe", "label": "A 4&times;4 matrix for management &amp; M&amp;E", "color": "indigo"},
                 {"num": "Theory of change", "label": "A richer causal model with assumptions", "color": "green"}]},
         ]},

        {"type": "content", "label": "The Logframe", "title": "A logframe is a 4&times;4 matrix",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "The <strong>logical framework</strong> arranges a programme "
              "into a four-by-four grid: four levels of result down the side, four columns across."},
             {"t": "table",
              "head": ["Level", "Indicator", "Means of verification", "Assumptions"],
              "rows": [
                  ["Impact / goal", "&hellip;", "&hellip;", "&hellip;"],
                  ["Outcome / purpose", "&hellip;", "&hellip;", "&hellip;"],
                  ["Outputs", "&hellip;", "&hellip;", "&hellip;"],
                  ["Activities", "&hellip;", "&hellip;", "&hellip;"]]},
             {"t": "hbox", "color": "cyan", "html": "Compact and management-friendly &mdash; but "
              "the grid hides the causal arrows <em>between</em> the rows."},
         ]},

        {"type": "content", "label": "Strengths", "title": "What the logframe does well",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Strengths", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Compact, standard, donor-familiar",
                      "Forces indicators &amp; verification",
                      "Good for management &amp; reporting",
                      "Lists assumptions per level"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Limits", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Linear &mdash; no branching pathways",
                      "Hides the &lsquo;because&rsquo; between rows",
                      "Often filled in to satisfy a form",
                      "Weak for complex, multi-actor change"]}]}]},
         ]},

        {"type": "content", "label": "Richer Model", "title": "How a ToC is richer",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Branching pathways</strong>, not a single straight line",
                 "<strong>Explicit assumptions</strong> on every causal arrow",
                 "A <strong>rationale</strong> &mdash; evidence for why each link should hold",
                 "Room for <strong>context, actors and feedback loops</strong>",
                 "A <strong>narrative</strong> alongside the diagram"]},
             {"t": "hbox", "color": "indigo", "html": "A logframe answers &lsquo;what will we "
              "track?&rsquo;. A ToC answers &lsquo;why do we believe this will work?&rsquo;"},
         ]},

        {"type": "content", "label": "How They Relate", "title": "They nest, they don't compete",
         "blocks": [
             {"t": "flow", "steps": [
                 "THEORY OF CHANGE: the full causal model + assumptions",
                 "RESULTS CHAIN: the linear spine drawn out of it",
                 "LOGFRAME: a matrix summarising it for management",
                 "INDICATORS: the measures hung on each level"]},
             {"t": "hbox", "color": "green", "html": "Best practice: develop the ToC first, then "
              "derive the logframe from it &mdash; not the other way round."},
         ]},

        {"type": "content", "label": "Side by Side", "title": "Choosing the right tool",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Results chain", "Logframe", "Theory of change"],
              "rows": [
                  ["Form", "Linear arrow", "4&times;4 matrix", "Causal map + narrative"],
                  ["Shows arrows?", "Yes, one line", "No (implied)", "Yes, branching"],
                  ["Assumptions", "Rarely", "One column", "Central, explicit"],
                  ["Best for", "Quick framing", "Management &amp; M&amp;E", "Design &amp; learning"]]},
             {"t": "hbox", "color": "amber", "html": "Use all three in sequence: a ToC to think, "
              "a results chain to communicate, a logframe to manage."},
         ]},

        {"type": "content", "label": "Common Confusion", "title": "&lsquo;We have a logframe, so we have a ToC&rsquo;",
         "blocks": [
             {"t": "body", "html": "A filled-in logframe is <em>not</em> a theory of change. The "
              "matrix can be complete while the causal reasoning &mdash; the &lsquo;because&rsquo; "
              "arrows and the assumptions that connect the rows &mdash; remains entirely unstated."},
             {"t": "hbox", "color": "red", "html": "If you cannot explain, out loud, why each "
              "logframe row should produce the row above it, you have a matrix but not a theory."},
         ]},

        {"type": "content", "label": "Outcome Mapping", "title": "A note on related methods",
         "blocks": [
             {"t": "body", "html": "<strong>Outcome Mapping</strong> (IDRC) and "
              "<strong>Outcome Harvesting</strong> are kindred approaches that focus on changes "
              "in the behaviour of actors a programme influences. They pair well with a ToC, "
              "especially for advocacy and systems change where impact is hard to attribute."},
             {"t": "hbox", "color": "cyan", "html": "Different vocabulary, same spirit: be honest "
              "about influence rather than control, and track behaviour change in others."},
         ]},

        # ===================== SECTION 04 — The building blocks (8) =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "The Building Blocks"},

        {"type": "content", "label": "The Chain", "title": "Inputs &rarr; activities &rarr; outputs &rarr; outcomes &rarr; impact",
         "blocks": [
             {"t": "flow", "steps": [
                 "INPUTS: resources &mdash; funds, staff, materials",
                 "ACTIVITIES: what we do with them",
                 "OUTPUTS: what we directly produce",
                 "OUTCOMES: changes in others' lives &amp; behaviour",
                 "IMPACT: durable, long-term change"]},
             {"t": "hbox", "color": "cyan", "html": "This <strong>results chain</strong> is the "
              "shared vocabulary of M&amp;E. Getting each box right is half the battle."},
         ]},

        {"type": "content", "label": "Inputs", "title": "Inputs: what you put in",
         "blocks": [
             {"t": "term", "word": "Inputs",
              "def": "The financial, human and material resources a programme uses &mdash; budget, "
              "staff time, training materials, vehicles, partner relationships."},
             {"t": "hbox", "color": "amber", "html": "Inputs are the easiest thing to count and "
              "the least interesting to a funder. Spending money is an activity, not a result."},
         ]},

        {"type": "content", "label": "Activities &amp; Outputs", "title": "Outputs are what you deliver",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Activities", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The actions you take: run trainings, build "
                   "toilets, hold meetings, distribute kits. Verbs you control."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Outputs", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The direct, countable products: 200 teachers "
                   "trained, 50 toilets built, 1,000 kits delivered. Still within your control."}]}]},
             {"t": "hbox", "color": "green", "html": "Outputs are necessary but never sufficient. "
              "Delivering them proves effort, not change."},
         ]},

        {"type": "content", "label": "The Big Leap", "title": "Outcomes: changes in <em>others</em>",
         "blocks": [
             {"t": "term", "word": "Outcome",
              "def": "A change in the knowledge, attitudes, behaviour, condition or status of the "
              "people, institutions or systems a programme works with. Outcomes happen in others "
              "&mdash; which is why they are outside your direct control."},
             {"t": "hbox", "color": "red", "html": "The single most common ToC error is calling an "
              "output an outcome. &lsquo;Teachers trained&rsquo; is an output; &lsquo;teachers "
              "teach differently&rsquo; is an outcome."},
         ]},

        {"type": "content", "label": "The Distinction", "title": "Outputs vs outcomes vs impact",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Output", "Outcome", "Impact"],
              "rows": [
                  ["What", "What you deliver", "Change in others", "Long-term change"],
                  ["Who changes", "Nobody yet", "Beneficiaries / systems", "Society / population"],
                  ["Control", "High &mdash; you own it", "Influence only", "Shared with many"],
                  ["Example", "Teachers trained", "Better teaching, more learning", "Educated generation"],
                  ["Timeframe", "During delivery", "Months&ndash;years", "Years&ndash;decades"]]},
             {"t": "hbox", "color": "cyan", "html": "Memorise this row: <strong>output = what you "
              "deliver, outcome = what changes in others, impact = the long-term change.</strong>"},
         ]},

        {"type": "content", "label": "Outcome Levels", "title": "Short, medium and long-term outcomes",
         "blocks": [
             {"t": "flow", "steps": [
                 "SHORT-TERM: knowledge &amp; attitudes shift (teachers learn new methods)",
                 "MEDIUM-TERM: behaviour &amp; practice change (they use the methods)",
                 "LONG-TERM: conditions improve (students learn more)"]},
             {"t": "hbox", "color": "indigo", "html": "Outcomes form a ladder. The early rungs "
              "(knowledge, attitude) are preconditions for the later rungs (behaviour, condition)."},
         ]},

        {"type": "content", "label": "Impact", "title": "Impact: durable change, shared credit",
         "blocks": [
             {"t": "body", "html": "<strong>Impact</strong> is the long-term, often population-level "
              "change a programme contributes to &mdash; reduced child stunting, an educated "
              "generation, safer cities. It usually unfolds after the project ends and is shaped "
              "by many actors beyond you."},
             {"t": "hbox", "color": "amber", "html": "Because so many forces shape impact, honest "
              "ToCs speak of <em>contribution</em>, not sole <em>attribution</em>, at this level."},
         ]},

        {"type": "content", "label": "Test Yourself", "title": "Output or outcome? A quick drill",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Statement", "It is an&hellip;", "Why"],
              "rows": [
                  ["1,000 SHG members trained on banking", "Output", "You delivered it"],
                  ["SHG members open &amp; use bank accounts", "Outcome", "Their behaviour changed"],
                  ["20 wells constructed", "Output", "You built them"],
                  ["Households drink safe water year-round", "Outcome", "Their condition changed"],
                  ["District anaemia prevalence falls", "Impact", "Long-term, population-level"]]},
             {"t": "hbox", "color": "green", "html": "The test: did <em>you</em> do it, or did "
              "<em>someone else change</em> because of what you did?"},
         ]},

        # ===================== SECTION 05 — Backwards mapping (8) =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Backwards Mapping"},

        {"type": "content", "label": "The Core Move", "title": "Start from the long-term goal",
         "blocks": [
             {"t": "body", "html": "The signature technique of ToC, from ActKnowledge and the "
              "Aspen Roundtable, is <strong>backwards mapping</strong>: begin with the long-term "
              "change you want, then work backwards asking &lsquo;what must be true just before "
              "this, for it to happen?&rsquo;"},
             {"t": "hbox", "color": "cyan", "html": "Designing forwards from activities tempts you "
              "to justify what you already do. Mapping backwards from the goal keeps the change, "
              "not the activity, in charge."},
         ]},

        {"type": "content", "label": "The Question", "title": "&lsquo;What has to be in place first?&rsquo;",
         "blocks": [
             {"t": "flow", "steps": [
                 "GOAL: children in the block read at grade level",
                 "&larr; PRECONDITION: they attend &amp; engage in class",
                 "&larr; PRECONDITION: teachers use effective methods",
                 "&larr; PRECONDITION: teachers know those methods",
                 "&larr; ENTRY POINT: a teacher-training programme"]},
             {"t": "hbox", "color": "amber", "html": "Each backward step asks the same question, "
              "and the chain stops when you reach something you can actually act on."},
         ]},

        {"type": "content", "label": "Preconditions", "title": "Outcomes are preconditions for the goal",
         "blocks": [
             {"t": "term", "word": "Precondition",
              "def": "An outcome that must be achieved before a higher-level outcome becomes "
              "possible. In a ToC, the chain of preconditions <em>is</em> the pathway of change."},
             {"t": "body", "html": "Backwards mapping produces a stack of preconditions. Read top "
              "to bottom it is a wish; read bottom to top it becomes a <strong>causal pathway</strong>."},
         ]},

        {"type": "content", "label": "The Diagram", "title": "An outcome pathway, drawn",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 720 380" width="720" style="max-width:100%;font-family:inherit;">'
                 '<defs><marker id="atocp" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto">'
                 '<path d="M0,0 L8,3 L0,6 Z" fill="#94a3b8"/></marker></defs>'
                 '<text x="360" y="22" text-anchor="middle" fill="#cbd5e1" font-size="14" font-weight="700">'
                 'Backwards from the goal &mdash; arrows show the causal direction</text>'
                 # goal at top
                 '<rect x="220" y="40" width="280" height="50" rx="10" fill="rgba(16,185,129,.15)" stroke="#10B981" stroke-width="2"/>'
                 '<text x="360" y="62" text-anchor="middle" fill="#10B981" font-size="14" font-weight="700">IMPACT</text>'
                 '<text x="360" y="80" text-anchor="middle" fill="#cbd5e1" font-size="12">children read at grade level</text>'
                 # precondition 1
                 '<rect x="220" y="130" width="280" height="46" rx="10" fill="rgba(99,102,241,.13)" stroke="#6366F1" stroke-width="1.8"/>'
                 '<text x="360" y="158" text-anchor="middle" fill="#a5b4fc" font-size="12.5">children attend &amp; engage in class</text>'
                 # precondition 2
                 '<rect x="220" y="216" width="280" height="46" rx="10" fill="rgba(99,102,241,.13)" stroke="#6366F1" stroke-width="1.8"/>'
                 '<text x="360" y="244" text-anchor="middle" fill="#a5b4fc" font-size="12.5">teachers use effective methods</text>'
                 # entry point
                 '<rect x="220" y="302" width="280" height="50" rx="10" fill="rgba(14,165,233,.15)" stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="360" y="324" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="700">ACTIVITY</text>'
                 '<text x="360" y="342" text-anchor="middle" fill="#cbd5e1" font-size="12">train teachers in proven methods</text>'
                 # upward arrows
                 '<line x1="360" y1="302" x2="360" y2="264" stroke="#94a3b8" stroke-width="2" marker-end="url(#atocp)"/>'
                 '<line x1="360" y1="216" x2="360" y2="178" stroke="#94a3b8" stroke-width="2" marker-end="url(#atocp)"/>'
                 '<line x1="360" y1="130" x2="360" y2="92" stroke="#94a3b8" stroke-width="2" marker-end="url(#atocp)"/>'
                 # design direction note
                 '<text x="600" y="70" fill="#f59e0b" font-size="12" font-weight="700">design</text>'
                 '<text x="600" y="86" fill="#f59e0b" font-size="12" font-weight="700">downward</text>'
                 '<line x1="600" y1="96" x2="600" y2="330" stroke="#F59E0B" stroke-width="1.5" stroke-dasharray="5,4" marker-end="url(#atocp)"/>'
                 '<text x="120" y="330" fill="#38bdf8" font-size="12" font-weight="700">deliver</text>'
                 '<text x="120" y="346" fill="#38bdf8" font-size="12" font-weight="700">upward</text>'
                 '<line x1="120" y1="320" x2="120" y2="90" stroke="#0EA5E9" stroke-width="1.5" stroke-dasharray="5,4" marker-end="url(#atocp)"/>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "Pathways", "title": "Change rarely runs in a single line",
         "blocks": [
             {"t": "body", "html": "Real pathways <strong>branch</strong>. Reaching grade-level "
              "reading may need three parallel pathways &mdash; better teaching, regular "
              "attendance, and a literate home environment &mdash; that converge on the goal."},
             {"t": "hbox", "color": "indigo", "html": "Map each pathway separately, then show "
              "where they meet. A single straight line usually means you have over-simplified."},
         ]},

        {"type": "content", "label": "Where to Stop", "title": "How far back do you go?",
         "blocks": [
             {"t": "body", "html": "Keep mapping backwards until you reach outcomes your "
              "programme can plausibly <strong>act on</strong> with its activities. Below that "
              "line are your entry points; above it are the changes you are trying to set off."},
             {"t": "hbox", "color": "amber", "html": "Draw the line honestly. If the lowest "
              "outcome is still far beyond your reach, your activities may be too thin for the "
              "goal you have set."},
         ]},

        {"type": "content", "label": "Necessary &amp; Sufficient", "title": "Are these preconditions enough?",
         "blocks": [
             {"t": "body", "html": "At each step, ask two questions: are these preconditions "
              "<strong>necessary</strong> (must they all be true?) and are they "
              "<strong>sufficient</strong> (if all are true, does the next outcome follow?)."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Necessary", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Drop one &mdash; does the chain still hold? "
                   "If yes, it may not have been needed."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Sufficient", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Have them all &mdash; is the next step "
                   "guaranteed, or is something still missing? The gap is an assumption."}]}]},
         ]},

        {"type": "content", "label": "Backwards in Practice", "title": "A facilitation sequence",
         "blocks": [
             {"t": "flow", "steps": [
                 "1. Agree the long-term goal &amp; who benefits",
                 "2. Ask: what must change just before that?",
                 "3. Repeat down to actionable outcomes",
                 "4. Identify entry-point activities",
                 "5. Surface the assumptions on each arrow"]},
             {"t": "hbox", "color": "green", "html": "Run steps 1&ndash;3 with sticky notes on a "
              "wall. The physical re-ordering is where teams discover their hidden disagreements."},
         ]},

        # ===================== SECTION 06 — Assumptions & rationale (8) =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Assumptions &amp; Rationale"},

        {"type": "content", "label": "The Heart", "title": "Assumptions are the &lsquo;because&rsquo; in the arrows",
         "blocks": [
             {"t": "body", "html": "Every arrow in a ToC hides an <strong>assumption</strong>: a "
              "belief about why one outcome will lead to the next. Make those beliefs explicit and "
              "the ToC becomes testable; leave them buried and it becomes a leap of faith."},
             {"t": "term", "word": "Assumption",
              "def": "A condition or belief that must hold for one step in the causal pathway to "
              "lead to the next. If an assumption fails, the link breaks &mdash; however well you "
              "deliver."},
         ]},

        {"type": "content", "label": "Three Kinds", "title": "Not all assumptions are the same",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Type", "About", "Example"],
              "rows": [
                  ["Causal-link", "Why one step leads to the next", "Trained teachers will actually change practice"],
                  ["Rationale / evidence", "Why we believe the link at all", "Studies show method X raises reading"],
                  ["External condition", "Context beyond our control", "Schools stay open; no major disruption"]]},
             {"t": "hbox", "color": "amber", "html": "Label each. Causal-link assumptions you can "
              "design around; external conditions you can only monitor and hope for."},
         ]},

        {"type": "content", "label": "Rationale", "title": "The rationale: evidence for the link",
         "blocks": [
             {"t": "body", "html": "A ToC arrow is stronger when backed by a <strong>rationale</strong> "
              "&mdash; evidence, theory or experience that the link tends to hold. Cite research, "
              "prior evaluations, or the lived knowledge of the community."},
             {"t": "hbox", "color": "indigo", "html": "Ask of every arrow: what is our evidence "
              "this works? &lsquo;It is obvious&rsquo; is not a rationale &mdash; it is a warning sign."},
         ]},

        {"type": "content", "label": "Surfacing Them", "title": "The &lsquo;if&ndash;then&ndash;because&rsquo; sentence",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 760 230" width="760" style="max-width:100%;font-family:inherit;">'
                 '<rect x="30" y="40" width="200" height="60" rx="10" fill="rgba(14,165,233,.14)" stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="130" y="66" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="700">IF</text>'
                 '<text x="130" y="86" text-anchor="middle" fill="#cbd5e1" font-size="11.5">teachers are trained</text>'
                 '<rect x="285" y="40" width="200" height="60" rx="10" fill="rgba(16,185,129,.14)" stroke="#10B981" stroke-width="2"/>'
                 '<text x="385" y="66" text-anchor="middle" fill="#34d399" font-size="13" font-weight="700">THEN</text>'
                 '<text x="385" y="86" text-anchor="middle" fill="#cbd5e1" font-size="11.5">practice improves</text>'
                 '<rect x="540" y="40" width="200" height="60" rx="10" fill="rgba(245,158,11,.14)" stroke="#F59E0B" stroke-width="2"/>'
                 '<text x="640" y="66" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="700">BECAUSE</text>'
                 '<text x="640" y="86" text-anchor="middle" fill="#cbd5e1" font-size="11.5">they apply what they learn</text>'
                 '<line x1="230" y1="70" x2="283" y2="70" stroke="#94a3b8" stroke-width="2"/>'
                 '<line x1="485" y1="70" x2="538" y2="70" stroke="#94a3b8" stroke-width="2"/>'
                 '<text x="385" y="150" text-anchor="middle" fill="#ef4444" font-size="13" font-weight="700">'
                 'The BECAUSE is the assumption &mdash; and the thing most likely to fail.</text>'
                 '<rect x="180" y="170" width="400" height="40" rx="8" fill="rgba(239,68,68,.10)" stroke="#EF4444" stroke-width="1.5"/>'
                 '<text x="380" y="195" text-anchor="middle" fill="#fca5a5" font-size="12">'
                 '&hellip; only if class sizes, materials &amp; supervision allow it</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "Risk", "title": "Assumptions are where risk lives",
         "blocks": [
             {"t": "body", "html": "A failed assumption is a <strong>risk</strong> by another "
              "name. Listing assumptions doubles as a risk register: plot each by how likely it "
              "is to fail and how badly the pathway breaks if it does."},
             {"t": "chart", "canvas": "tocRiskChart",
              "title": "Assumption risk &mdash; likelihood vs consequence (illustrative)",
              "source": "Illustrative example",
              "type": "scatter",
              "data": {"datasets": [{"label": "Assumptions",
                       "data": [{"x": 8, "y": 9}, {"x": 3, "y": 8}, {"x": 6, "y": 4},
                                {"x": 2, "y": 3}, {"x": 7, "y": 7}, {"x": 4, "y": 2}],
                       "backgroundColor": "#EF4444", "pointRadius": 8}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:10, title:{display:true,text:'likelihood it fails'} }, y:{ min:0, max:10, title:{display:true,text:'consequence if it fails'} } } }"}},
             {"t": "hbox", "color": "red", "html": "Watch the top-right corner: high likelihood "
              "<em>and</em> high consequence. Those are the load-bearing assumptions to design "
              "around and monitor first."},
         ]},

        {"type": "content", "label": "Killer Assumptions", "title": "Find the load-bearing one",
         "blocks": [
             {"t": "body", "html": "Some assumptions are <strong>load-bearing</strong>: if they "
              "fail, the whole theory collapses. A women's-livelihood ToC may rest on the "
              "assumption that <em>households will let women keep their earnings</em> &mdash; the "
              "quiet hinge on which everything turns."},
             {"t": "hbox", "color": "red", "html": "Hunt for the killer assumption deliberately. "
              "It is often social or political, rarely technical, and frequently unspoken."},
         ]},

        {"type": "content", "label": "External Conditions", "title": "Conditions you cannot control",
         "blocks": [
             {"t": "bullets", "items": [
                 "Markets, prices and the wider economy stay broadly stable",
                 "Policy and political backing do not reverse mid-programme",
                 "No major shock &mdash; flood, drought, pandemic, conflict",
                 "Other actors deliver the parts you depend on"]},
             {"t": "hbox", "color": "amber", "html": "You cannot remove external conditions, but "
              "you must name them &mdash; and monitor the ones most likely to move."},
         ]},

        {"type": "content", "label": "Test Them", "title": "Treat each assumption as a hypothesis",
         "blocks": [
             {"t": "body", "html": "An explicit assumption is a question you can answer with "
              "evidence. Build a small check for the riskiest ones into your monitoring, so you "
              "learn early whether the theory is holding &mdash; not at the final evaluation."},
             {"t": "hbox", "color": "green", "html": "Good practice: for every load-bearing "
              "assumption, write down what you would observe if it were false."},
         ]},

        # ===================== SECTION 07 — Indicators & evidence (8) =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Indicators &amp; Evidence"},

        {"type": "content", "label": "The Question", "title": "How will you know it happened?",
         "blocks": [
             {"t": "body", "html": "Every outcome on the map needs an answer to one question: "
              "<strong>how will we know this change occurred?</strong> The answer is an "
              "<strong>indicator</strong> &mdash; an observable marker that the outcome is real."},
             {"t": "term", "word": "Indicator",
              "def": "A measurable marker that signals whether, and how far, an outcome has been "
              "achieved. A good indicator is a faithful, observable proxy for the change."},
         ]},

        {"type": "content", "label": "SMART", "title": "What makes a usable indicator",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Letter", "Means", "Test"],
              "rows": [
                  ["Specific", "Clearly defined", "Would two people measure it the same way?"],
                  ["Measurable", "Quantifiable / observable", "Can we actually collect it?"],
                  ["Achievable", "Realistic to move", "Could the programme plausibly shift it?"],
                  ["Relevant", "Tied to the outcome", "Does it really reflect the change?"],
                  ["Time-bound", "Has a timeframe", "By when do we expect the change?"]]},
             {"t": "hbox", "color": "cyan", "html": "SMART is a checklist, not a straitjacket. The "
              "deeper test is whether the indicator faithfully reflects the outcome it sits under."},
         ]},

        {"type": "content", "label": "Match the Level", "title": "Different results need different indicators",
         "blocks": [
             {"t": "flow", "steps": [
                 "OUTPUT indicators: count what you delivered (# trained)",
                 "OUTCOME indicators: measure change in others (% changing practice)",
                 "IMPACT indicators: track long-term condition (reading levels)"]},
             {"t": "hbox", "color": "red", "html": "A frequent mistake: hanging only output "
              "indicators on outcome rows. Counting activities tells you nothing about change."},
         ]},

        {"type": "content", "label": "Quant &amp; Qual", "title": "Numbers and stories, together",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Quantitative", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Tells you <em>how much</em> changed &mdash; "
                   "scores, rates, counts. Good for scale and comparison."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Qualitative", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Tells you <em>how and why</em> &mdash; "
                   "stories, observation, interviews. Good for mechanism and meaning."}]}]},
             {"t": "hbox", "color": "green", "html": "The best ToCs use both: a number to detect "
              "change, a narrative to understand it. Each covers the other's blind spot."},
         ]},

        {"type": "content", "label": "Baseline &amp; Target", "title": "An indicator needs a before and an after",
         "blocks": [
             {"t": "body", "html": "An indicator is only meaningful against a <strong>baseline</strong> "
              "(where you started) and a <strong>target</strong> (where you aim to reach). Without "
              "a baseline you cannot show change; without a target you cannot judge whether it was "
              "enough."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Baseline", "label": "The starting value, measured before you act", "color": "cyan"},
                 {"num": "Target", "label": "The value you aim to reach, by when", "color": "green"},
                 {"num": "Endline", "label": "The value you actually measure later", "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Means of Verification", "title": "Where will the data come from?",
         "blocks": [
             {"t": "body", "html": "For each indicator, name the <strong>means of verification</strong> "
              "&mdash; the data source and method. An indicator with no realistic source is a wish, "
              "not a measure."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Programme data:</strong> attendance, training records, registers",
                 "<strong>Surveys:</strong> baseline / endline, sample-based outcome tracking",
                 "<strong>Secondary data:</strong> NFHS, UDISE+, HMIS, district statistics",
                 "<strong>Qualitative:</strong> interviews, observation, case stories"]},
         ]},

        {"type": "content", "label": "Don't Over-Measure", "title": "A few good indicators beat many weak ones",
         "blocks": [
             {"t": "body", "html": "It is tempting to attach three indicators to every box. Resist. "
              "Each indicator costs time, money and respondent goodwill to collect. Choose the few "
              "that genuinely move decisions."},
             {"t": "hbox", "color": "amber", "html": "Ask of each candidate: if this number "
              "changed, would we <em>do</em> anything differently? If not, drop it."},
         ]},

        {"type": "content", "label": "Worked Indicators", "title": "Indicators down one pathway",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Step", "Indicator", "Source"],
              "rows": [
                  ["Activity", "# teachers completing training", "Training records"],
                  ["Output", "% teachers passing the post-test", "Assessment data"],
                  ["Short outcome", "% using new methods in class", "Classroom observation"],
                  ["Med. outcome", "% students engaged in lessons", "Spot checks / survey"],
                  ["Impact", "% reading at grade level", "Learning assessment"]]},
             {"t": "hbox", "color": "cyan", "html": "Read top to bottom, the indicators track the "
              "change moving up the pathway &mdash; from your control into the world."},
         ]},

        # ===================== SECTION 08 — Drawing the ToC (8) =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Drawing the ToC"},

        {"type": "content", "label": "The Outcome Map", "title": "Boxes for changes, arrows for causes",
         "blocks": [
             {"t": "body", "html": "The visual heart of a ToC is the <strong>outcomes map</strong>: "
              "each box is an outcome (a change), each arrow a causal claim, read upward from "
              "entry-point activities to the long-term goal."},
             {"t": "bullets", "sm": True, "items": [
                 "Boxes hold <strong>outcomes</strong>, phrased as changes that have happened",
                 "Arrows show <strong>causal direction</strong>, never just sequence",
                 "Branches show <strong>parallel pathways</strong> converging on the goal",
                 "Notes on arrows carry the <strong>assumptions</strong>"]},
         ]},

        {"type": "content", "label": "A Worked Map", "title": "A two-pathway outcome map",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:4px 0;">'
                 '<svg viewBox="0 0 760 380" width="760" style="max-width:100%;font-family:inherit;">'
                 '<defs><marker id="atocm" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
                 '<path d="M0,0 L8,3 L0,6 Z" fill="#94a3b8"/></marker></defs>'
                 # goal
                 '<rect x="260" y="30" width="240" height="50" rx="10" fill="rgba(16,185,129,.16)" stroke="#10B981" stroke-width="2"/>'
                 '<text x="380" y="52" text-anchor="middle" fill="#34d399" font-size="13" font-weight="700">GOAL</text>'
                 '<text x="380" y="70" text-anchor="middle" fill="#cbd5e1" font-size="11.5">children read at grade level</text>'
                 # mid outcomes (two)
                 '<rect x="90" y="150" width="240" height="48" rx="10" fill="rgba(99,102,241,.13)" stroke="#6366F1" stroke-width="1.8"/>'
                 '<text x="210" y="178" text-anchor="middle" fill="#a5b4fc" font-size="11.5">children attend regularly</text>'
                 '<rect x="430" y="150" width="240" height="48" rx="10" fill="rgba(99,102,241,.13)" stroke="#6366F1" stroke-width="1.8"/>'
                 '<text x="550" y="178" text-anchor="middle" fill="#a5b4fc" font-size="11.5">teachers teach effectively</text>'
                 # entry activities (two)
                 '<rect x="90" y="280" width="240" height="48" rx="10" fill="rgba(14,165,233,.15)" stroke="#0EA5E9" stroke-width="1.8"/>'
                 '<text x="210" y="308" text-anchor="middle" fill="#38bdf8" font-size="11.5">community attendance drive</text>'
                 '<rect x="430" y="280" width="240" height="48" rx="10" fill="rgba(14,165,233,.15)" stroke="#0EA5E9" stroke-width="1.8"/>'
                 '<text x="550" y="308" text-anchor="middle" fill="#38bdf8" font-size="11.5">teacher training programme</text>'
                 # arrows up
                 '<line x1="210" y1="280" x2="210" y2="200" stroke="#94a3b8" stroke-width="2" marker-end="url(#atocm)"/>'
                 '<line x1="550" y1="280" x2="550" y2="200" stroke="#94a3b8" stroke-width="2" marker-end="url(#atocm)"/>'
                 '<line x1="230" y1="150" x2="345" y2="82" stroke="#94a3b8" stroke-width="2" marker-end="url(#atocm)"/>'
                 '<line x1="530" y1="150" x2="415" y2="82" stroke="#94a3b8" stroke-width="2" marker-end="url(#atocm)"/>'
                 # assumption note
                 '<text x="380" y="120" text-anchor="middle" fill="#f59e0b" font-size="11" font-style="italic">'
                 'assumes: attendance + good teaching together suffice</text>'
                 '<text x="380" y="358" text-anchor="middle" fill="#64748b" font-size="11">'
                 'Two pathways converge on one goal &mdash; read the arrows upward</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "Phrasing", "title": "Write outcomes as changes, not actions",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Weak (activity)", "Strong (outcome / change)"],
              "rows": [
                  ["Conduct hygiene sessions", "Families practise safe hygiene"],
                  ["Form farmer groups", "Farmers adopt improved practices"],
                  ["Distribute textbooks", "Children use textbooks to study"],
                  ["Hold awareness camps", "Women know &amp; claim their entitlements"]]},
             {"t": "hbox", "color": "green", "html": "Test each box: could you photograph the "
              "<em>change</em>? If you can only photograph the <em>event</em>, rewrite it."},
         ]},

        {"type": "content", "label": "The Narrative", "title": "Write the story beside the map",
         "blocks": [
             {"t": "body", "html": "The diagram needs a <strong>narrative</strong> that walks "
              "through each pathway: what changes, why we believe it will, what evidence supports "
              "the link, and what assumptions must hold. The narrative is where nuance lives."},
             {"t": "hbox", "color": "indigo", "html": "A good narrative makes the ToC legible to "
              "someone who was not in the room &mdash; including the funder and the evaluator."},
         ]},

        {"type": "content", "label": "Facilitation", "title": "Build it <em>with</em> stakeholders",
         "blocks": [
             {"t": "body", "html": "A ToC drawn alone is a document; a ToC drawn with the team, "
              "partners and community is a shared belief. The workshop &mdash; arguing, "
              "re-ordering, disagreeing &mdash; is where the real value is created."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Start from the goal, work backwards on the wall",
                 "Welcome disagreement &mdash; it reveals hidden theories",
                 "Capture every assumption as it surfaces",
                 "Leave with a rough map, not a polished one"]},
         ]},

        {"type": "content", "label": "Whose Theory", "title": "Include the people the change is for",
         "blocks": [
             {"t": "body", "html": "Communities hold knowledge about what actually drives change "
              "in their lives &mdash; knowledge no logframe captures. Involving them improves the "
              "theory and grounds it in lived reality, not assumption."},
             {"t": "hbox", "color": "amber", "html": "Ask: whose theory is this? If only "
              "outsiders shaped it, the most important assumptions may never have been questioned."},
         ]},

        {"type": "content", "label": "Iterate", "title": "First draft, not final word",
         "blocks": [
             {"t": "body", "html": "A ToC is never finished. Draft it quickly, use it, and revise "
              "as you learn. An over-polished first version signals false confidence; a rough, "
              "living one invites the questioning that makes it strong."},
             {"t": "quote",
              "text": "A theory of change is a work in progress, not a one-off product &mdash; "
              "its value lies in the thinking it provokes, not the diagram it produces.",
              "attr": "&mdash; after Isabel Vogel, ToC review for DFID, 2012"},
         ]},

        {"type": "content", "label": "Keep It Legible", "title": "Resist the urge to draw everything",
         "blocks": [
             {"t": "body", "html": "A map with sixty boxes and a hundred arrows communicates "
              "nothing. The discipline is to show the <strong>main pathways</strong> clearly and "
              "push the detail into the narrative and the indicator table."},
             {"t": "hbox", "color": "red", "html": "If a colleague cannot trace one path from "
              "activity to goal in under a minute, the diagram is too crowded. Simplify."},
         ]},

        # ===================== SECTION 09 — Common pitfalls (8) =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Common Pitfalls"},

        {"type": "content", "label": "Pitfall Map", "title": "The five classic failures",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Activity-itis", "label": "Activities masquerading as outcomes", "color": "red"},
                 {"num": "Missing assumptions", "label": "Arrows with no stated &lsquo;because&rsquo;", "color": "amber"},
                 {"num": "Leaps of logic", "label": "Big gaps between adjacent boxes", "color": "indigo"},
                 {"num": "Over-complexity", "label": "A map too tangled to read", "color": "cyan"}]},
             {"t": "hbox", "color": "red", "html": "And the fifth, underlying them all: confusing "
              "what you <em>do</em> with the change you <em>cause</em>."},
         ]},

        {"type": "content", "label": "Pitfall 1", "title": "Activity-itis: doing mistaken for changing",
         "blocks": [
             {"t": "body", "html": "<strong>Activity-itis</strong> is the most common disease of "
              "ToCs: the map fills with things the programme will <em>do</em> &mdash; train, build, "
              "convene &mdash; and never reaches the changes those activities are meant to cause."},
             {"t": "hbox", "color": "red", "html": "The cure: for every activity, ask &lsquo;so "
              "that what?&rsquo; until you reach a genuine change in someone's life or behaviour."},
         ]},

        {"type": "content", "label": "Pitfall 2", "title": "Results vs activities &mdash; the core confusion",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["What you wrote", "What it really is", "Fix"],
              "rows": [
                  ["&lsquo;500 women trained&rsquo;", "Activity / output", "&hellip; so they start enterprises"],
                  ["&lsquo;10 wells built&rsquo;", "Output", "&hellip; so households drink safe water"],
                  ["&lsquo;Held 30 meetings&rsquo;", "Activity", "&hellip; so the panchayat acts on it"],
                  ["&lsquo;Printed 5,000 leaflets&rsquo;", "Output", "&hellip; so people know their rights"]]},
             {"t": "hbox", "color": "amber", "html": "The &lsquo;so that&rsquo; clause is where "
              "the outcome hides. Chase it until you reach real change."},
         ]},

        {"type": "content", "label": "Pitfall 3", "title": "Missing assumptions: silent arrows",
         "blocks": [
             {"t": "body", "html": "An arrow with no stated assumption is a claim nobody has "
              "examined. The link &lsquo;women earn income &rarr; women are empowered&rsquo; hides "
              "a huge assumption: that they control how the income is spent."},
             {"t": "hbox", "color": "indigo", "html": "Audit every arrow. If it has no &lsquo;this "
              "works because&hellip; and only if&hellip;&rsquo; note, you have found a blind spot."},
         ]},

        {"type": "content", "label": "Pitfall 4", "title": "Leaps of logic: the missing middle",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0;">'
                 '<svg viewBox="0 0 760 220" width="760" style="max-width:100%;font-family:inherit;">'
                 '<rect x="40" y="80" width="210" height="60" rx="10" fill="rgba(14,165,233,.14)" stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="145" y="106" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="700">Train health workers</text>'
                 '<text x="145" y="126" text-anchor="middle" fill="#cbd5e1" font-size="11">(what we do)</text>'
                 '<rect x="510" y="80" width="210" height="60" rx="10" fill="rgba(16,185,129,.14)" stroke="#10B981" stroke-width="2"/>'
                 '<text x="615" y="106" text-anchor="middle" fill="#34d399" font-size="12" font-weight="700">Child deaths fall</text>'
                 '<text x="615" y="126" text-anchor="middle" fill="#cbd5e1" font-size="11">(long-term impact)</text>'
                 '<line x1="250" y1="110" x2="505" y2="110" stroke="#EF4444" stroke-width="2.5" stroke-dasharray="8,6" marker-end="url(#aleap)"/>'
                 '<defs><marker id="aleap" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto">'
                 '<path d="M0,0 L8,3 L0,6 Z" fill="#EF4444"/></marker></defs>'
                 '<text x="378" y="60" text-anchor="middle" fill="#ef4444" font-size="13" font-weight="700">'
                 'The missing middle</text>'
                 '<text x="378" y="170" text-anchor="middle" fill="#94a3b8" font-size="11.5">'
                 'Where are: workers practise correctly &rarr; mothers seek care &rarr; sick children treated?</text>'
                 '</svg></div>')},
             {"t": "hbox", "color": "red", "html": "A leap of logic skips the outcomes in "
              "between. Fill the gap with the real intermediate changes &mdash; or admit the link "
              "is hope, not theory."},
         ]},

        {"type": "content", "label": "Pitfall 5", "title": "Over-complexity: the spaghetti diagram",
         "blocks": [
             {"t": "body", "html": "The opposite failure: a map so dense with boxes and crossing "
              "arrows that no one can follow a single pathway. Complexity is not rigour &mdash; "
              "often it hides muddled thinking behind a busy picture."},
             {"t": "hbox", "color": "amber", "html": "If you cannot explain your ToC in two "
              "minutes with the diagram in hand, it is too complex to be useful. Prune it."},
         ]},

        {"type": "content", "label": "More Traps", "title": "Three quieter mistakes",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Reverse-engineering:</strong> writing the ToC after deciding the "
                 "activities, to justify them",
                 "<strong>Single-pathway tunnel vision:</strong> ignoring the other ways the goal "
                 "could be reached &mdash; or blocked",
                 "<strong>Set-and-forget:</strong> drawing it once for the proposal and never "
                 "looking at it again"]},
             {"t": "hbox", "color": "amber", "html": "Each of these turns a living theory into a "
              "dead document. The fix is the same: keep using it."},
         ]},

        {"type": "content", "label": "Quality Check", "title": "A pre-flight checklist for any ToC",
         "compact": True,
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Does every box describe a <em>change</em>, not an activity?",
                 "Can you read a clear path from activity to goal?",
                 "Does every arrow carry a stated assumption?",
                 "Have you named the load-bearing &amp; external assumptions?",
                 "Is there a rationale &mdash; evidence &mdash; for the key links?",
                 "Is it simple enough to explain in two minutes?",
                 "Did the people it serves help shape it?"]},
         ]},

        # ===================== SECTION 10 — Using ToC across the cycle (8) =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Using ToC Across the Cycle"},

        {"type": "content", "label": "Not Just Design", "title": "A ToC works the whole cycle",
         "blocks": [
             {"t": "flow", "steps": [
                 "DESIGN: shape the programme &amp; test the logic",
                 "MEL: derive indicators &amp; evaluation questions",
                 "ADAPT: revise as assumptions are tested",
                 "REPORT: tell a credible contribution story"]},
             {"t": "hbox", "color": "cyan", "html": "A ToC filed away after the proposal wastes "
              "most of its value. Its real life is across delivery, learning and reporting."},
         ]},

        {"type": "content", "label": "In Design", "title": "Designing with a ToC",
         "blocks": [
             {"t": "body", "html": "At design, the ToC stress-tests the programme before money is "
              "spent: are the pathways plausible? Are activities matched to the change sought? "
              "Where are the riskiest assumptions, and can the design strengthen them?"},
             {"t": "hbox", "color": "green", "html": "A ToC can save a programme by revealing, on "
              "paper, that the activities could never reach the goal &mdash; the cheapest failure "
              "you will ever have."},
         ]},

        {"type": "content", "label": "In MEL", "title": "The backbone of monitoring &amp; evaluation",
         "blocks": [
             {"t": "body", "html": "In <strong>MEL</strong>, the ToC turns into a measurement "
              "plan: each outcome becomes an indicator, each assumption a monitoring question, "
              "each pathway an evaluation hypothesis to confirm or revise."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Outcomes", "label": "become indicators to track", "color": "cyan"},
                 {"num": "Assumptions", "label": "become questions to monitor", "color": "amber"},
                 {"num": "Pathways", "label": "become hypotheses to test", "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Contribution", "title": "Contribution analysis: did the theory hold?",
         "blocks": [
             {"t": "body", "html": "Where you cannot run a controlled experiment, "
              "<strong>contribution analysis</strong> uses the ToC as its spine: gather evidence "
              "on each link, check whether the pathway played out as theorised, and rule out "
              "alternative explanations."},
             {"t": "hbox", "color": "indigo", "html": "The verdict is not &lsquo;did it "
              "work?&rsquo; but &lsquo;is it reasonable to conclude the programme made a "
              "difference, given how the theory held up?&rsquo;"},
         ]},

        {"type": "content", "label": "Adaptive Mgmt", "title": "Adaptive management: revise as you learn",
         "blocks": [
             {"t": "body", "html": "When monitoring shows an assumption failing, the response is "
              "not to bury it &mdash; it is to <strong>adapt</strong>. The ToC becomes the place "
              "where learning is recorded and the programme's direction is consciously adjusted."},
             {"t": "flow", "steps": [
                 "Monitor a key assumption",
                 "Find it is not holding",
                 "Revise the pathway &amp; activities",
                 "Update the ToC &amp; explain why"]},
         ]},

        {"type": "content", "label": "In Reporting", "title": "Telling an honest results story",
         "blocks": [
             {"t": "body", "html": "A ToC structures reporting around <strong>change</strong>, not "
              "activity. Instead of &lsquo;we trained 500 people&rsquo;, you can say &lsquo;here is "
              "the change we contributed to, here is the evidence, and here is where the theory "
              "did and did not hold.&rsquo;"},
             {"t": "hbox", "color": "green", "html": "Funders increasingly trust the programme "
              "that reports honestly on a broken link over the one that reports only success."},
         ]},

        {"type": "content", "label": "Living Document", "title": "Keep it on the wall, not in the drawer",
         "blocks": [
             {"t": "bullets", "items": [
                 "Revisit the ToC at every major review &mdash; not just at the start",
                 "Date each version and note <em>what changed and why</em>",
                 "Pin the current map where the team can see it",
                 "Use it to onboard new staff and partners quickly"]},
             {"t": "hbox", "color": "cyan", "html": "A ToC you update is a record of your "
              "learning. A ToC you never touch is just a relic of the proposal."},
         ]},

        # ===================== SECTION 11 — Worked example & further reading (7) =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Worked Example &amp; Further Reading"},

        {"type": "content", "label": "The Programme", "title": "A worked example: maternal nutrition",
         "blocks": [
             {"t": "body", "html": "Imagine a district programme aiming to reduce <strong>low "
              "birth weight</strong> by improving maternal nutrition. Let us build its theory of "
              "change end to end &mdash; goal, pathway, assumptions and indicators."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Goal", "label": "Fewer low-birth-weight babies in the district", "color": "green"},
                 {"num": "Levers", "label": "Counselling, supplements, ANC linkage", "color": "cyan"},
                 {"num": "Actors", "label": "Frontline workers, families, health system", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Note: figures and the pathway here are "
              "<strong>illustrative</strong>, built to feel real &mdash; not drawn from a specific "
              "evaluation."},
         ]},

        {"type": "content", "label": "The Pathway", "title": "Backwards from the goal",
         "blocks": [
             {"t": "flow", "steps": [
                 "GOAL: fewer low-birth-weight babies",
                 "&larr; mothers gain adequate weight in pregnancy",
                 "&larr; mothers eat better &amp; take supplements",
                 "&larr; mothers know what to eat &amp; have access",
                 "&larr; ACTIVITY: counselling + supplement supply + ANC linkage"]},
             {"t": "hbox", "color": "cyan", "html": "Five rungs, each a precondition for the one "
              "above. The lowest is where the programme acts; the top is the change it seeks."},
         ]},

        {"type": "content", "label": "Assumptions", "title": "What has to hold &mdash; and the indicators",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Link", "Key assumption", "Indicator"],
              "rows": [
                  ["Activity &rarr; knowledge", "Counselling reaches &amp; persuades mothers", "% mothers counselled / aware"],
                  ["Knowledge &rarr; intake", "Food &amp; supplements are available at home", "% taking supplements"],
                  ["Intake &rarr; weight gain", "Diet change is enough to shift weight", "Avg. gestational weight gain"],
                  ["Weight &rarr; birth weight", "No countervailing risk (illness, anaemia)", "% low-birth-weight births"]]},
             {"t": "hbox", "color": "red", "html": "The load-bearing assumption here is the second "
              "row: knowing is useless if the household cannot afford or access the food. "
              "(Illustrative.)"},
         ]},

        {"type": "content", "label": "Illustrative Targets", "title": "An illustrative results curve",
         "blocks": [
             {"t": "chart", "canvas": "tocLbwChart",
              "title": "Low-birth-weight rate &mdash; baseline, target &amp; illustrative trajectory",
              "source": "Illustrative &mdash; not from a specific evaluation",
              "type": "line",
              "data": {"labels": ["Baseline", "Yr 1", "Yr 2", "Yr 3", "Target"],
                       "datasets": [{"label": "Low-birth-weight rate (%)",
                                     "data": [22, 20, 18, 16, 15],
                                     "borderColor": "#10B981",
                                     "backgroundColor": "rgba(16,185,129,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 5}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:10, max:25, title:{display:true,text:'% of births'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "The numbers are invented for teaching. The "
              "shape is the point: a baseline, a credible trajectory, and a dated target."},
         ]},

        {"type": "content", "label": "Risk Check", "title": "Where could this theory break?",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Supplement supply chains fail &mdash; the second link snaps",
                 "Households deprioritise the mother's diet &mdash; a social assumption",
                 "Untreated anaemia or infection overrides nutrition gains",
                 "Frontline workers are overloaded &mdash; counselling never lands"]},
             {"t": "hbox", "color": "amber", "html": "Every bullet is an assumption from the "
              "table, turned into a monitoring question. That is the ToC earning its keep."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "The canon, briefly",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<strong>Carol Weiss (1995)</strong> &mdash; the founding essay on theory-based "
                 "evaluation of community initiatives",
                 "<strong>ActKnowledge &amp; Aspen Institute</strong> &mdash; the backwards-mapping "
                 "method (theoryofchange.org)",
                 "<strong>Isabel Vogel (2012)</strong> &mdash; &lsquo;Review of the use of Theory "
                 "of Change in international development&rsquo;, for DFID",
                 "<strong>Comic Relief</strong> &mdash; practical ToC guidance for grantees",
                 "<strong>Funnell &amp; Rogers</strong> &mdash; <em>Purposeful Program Theory</em> "
                 "(programme theory &amp; logic models)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Monitoring &amp; Evaluation</strong>, <strong>Logframes</strong> and "
              "<strong>Programme Design</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>A ToC is a causal argument</strong>, not an activity list or a plan",
                 "<strong>Map backwards</strong> from the long-term goal, not forwards from what you do",
                 "<strong>Outputs &ne; outcomes &ne; impact</strong> &mdash; know which is which",
                 "<strong>Make assumptions explicit</strong> &mdash; that is where risk and learning live",
                 "<strong>Keep it living</strong> &mdash; use it across design, MEL, adaptation and reporting"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Theory of Change 101 &middot; Complete",
         "headline": "Now go map<br>the change.",
         "byline": "A theory of change is only as good as the thinking it provokes. Draw it "
                   "backwards, name your assumptions, and keep it on the wall. Explore the rest "
                   "of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
