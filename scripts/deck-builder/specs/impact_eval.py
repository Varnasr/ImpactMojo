# -*- coding: utf-8 -*-
"""
Impact Evaluation 101 — ImpactMojo 101 Series (native deck spec)
Designing and commissioning credible impact evaluations for South Asian
development programmes. Applied, practitioner-facing companion to Econometrics 101.
Build: python3 scripts/deck-builder/build.py impact_eval
"""

DECK = {
    "slug": "impact-eval",
    "title": "Impact Evaluation 101",
    "description": ("Impact Evaluation 101 — a free foundational course for development "
                    "programme and MEL practitioners in South Asia on designing, "
                    "commissioning and using credible impact evaluations: the "
                    "counterfactual, theory of change, RCTs, quasi-experimental designs, "
                    "power, measurement, interpretation, cost and ethics, with "
                    "India-centric examples. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Impact<br>Evaluation<br>101",
         "sub": "Designing &amp; Commissioning Credible Evaluations &mdash; a Foundational "
                "Course for Development Programme &amp; MEL Practitioners in South Asia",
         "tags": ["Practice-Focused", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Impact Evaluation Is"},
             {"name": "The Counterfactual &amp; Causal Inference"},
             {"name": "Theory of Change &amp; Evaluation Questions"},
             {"name": "Randomised Experiments (RCTs)"},
             {"name": "Quasi-Experimental Designs"},
             {"name": "Choosing a Method"},
             {"name": "Sampling &amp; Statistical Power"},
             {"name": "Measurement &amp; Data Collection"},
             {"name": "Analysis &amp; Interpreting Results"},
             {"name": "External Validity, Cost &amp; Ethics"},
             {"name": "Using IE for Decisions &amp; Further Reading"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Impact Evaluation Is"},

        {"type": "content", "label": "Definition", "title": "Measuring the change a programme caused",
         "blocks": [
             {"t": "body", "html": "An <strong>impact evaluation</strong> answers one demanding "
              "question: how much of the change we observe was actually <em>caused</em> by our "
              "programme &mdash; and not by everything else happening at the same time?"},
             {"t": "term", "word": "Impact evaluation",
              "def": "A study that estimates the causal effect of a programme, policy or "
              "intervention on an outcome &mdash; the difference between what happened with the "
              "programme and what would have happened without it."},
             {"t": "hbox", "color": "cyan", "html": "Every other M&amp;E question can be useful. "
              "This one tells you whether the programme is worth running at all."},
         ]},

        {"type": "content", "label": "The Distinction", "title": "Impact is not the same as monitoring",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Monitoring", "Impact evaluation"],
              "rows": [
                  ["Asks", "Are we doing what we planned?", "Did it cause the change?"],
                  ["Tracks", "Inputs, activities, outputs", "Outcomes vs a counterfactual"],
                  ["Timing", "Continuous, routine", "Periodic, designed in advance"],
                  ["Example", "1,200 toilets built", "Did diarrhoea actually fall because of them?"],
                  ["Answers", "Implementation", "Attribution"]]},
             {"t": "hbox", "color": "amber", "html": "Monitoring tells you the programme ran. "
              "Impact evaluation tells you whether it <em>worked</em>. You need both &mdash; they "
              "answer different questions."},
         ]},

        {"type": "content", "label": "The Results Chain", "title": "Where impact sits in the results chain",
         "blocks": [
             {"t": "flow", "steps": [
                 "INPUTS: budget, staff, training",
                 "ACTIVITIES: deliver the programme",
                 "OUTPUTS: toilets built, classes held",
                 "OUTCOMES: behaviour, take-up",
                 "IMPACT: the caused change in wellbeing"]},
             {"t": "hbox", "color": "cyan", "html": "Monitoring lives on the left of this chain; "
              "impact evaluation targets the far right &mdash; and insists on attribution, not "
              "just association."},
         ]},

        {"type": "content", "label": "The Attribution Question", "title": "Compared to what?",
         "blocks": [
             {"t": "body", "html": "A village had the programme; outcomes improved. Tempting to "
              "claim success &mdash; but outcomes might have improved anyway, through a good "
              "monsoon, rising incomes, or other schemes. The honest question is always: "
              "<strong>compared to what?</strong>"},
             {"t": "quote",
              "text": "The fundamental question of impact evaluation is not 'did things get "
              "better?' but 'did things get better because of us?'",
              "attr": "&mdash; a working principle of evaluation practice"},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "What credible evidence buys you",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "When you have it", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Scale what genuinely works",
                      "Stop what does not, and free up budget",
                      "Defend funding with real evidence",
                      "Learn why, not just whether"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "When you don't", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Scale failures by mistake",
                      "Credit yourself for trends you didn't cause",
                      "Cut effective programmes blindly",
                      "Repeat the same expensive errors"]}]}]},
         ]},

        {"type": "content", "label": "A Caution", "title": "Impact evaluation is not always the answer",
         "blocks": [
             {"t": "body", "html": "Impact evaluation is powerful but costly and slow. It is one "
              "tool in the MEL toolkit &mdash; not a stamp of legitimacy to apply to everything. "
              "Much of the time, good monitoring and process evaluation serve you better."},
             {"t": "hbox", "color": "amber", "html": "This course is as much about knowing "
              "<em>when</em> to commission an impact evaluation as about how to design one."},
         ]},

        {"type": "content", "label": "Your Role", "title": "You don't have to run it to commission it well",
         "blocks": [
             {"t": "body", "html": "Most practitioners will <strong>commission</strong> an impact "
              "evaluation rather than estimate it themselves. That still demands real literacy: "
              "framing the question, choosing a design, judging a proposal, and reading the "
              "findings critically."},
             {"t": "hbox", "color": "cyan", "html": "This deck is written for the commissioner and "
              "the manager &mdash; the person who must ask hard questions of an evaluator, not "
              "necessarily write the regression."},
         ]},

        {"type": "content", "label": "The Family of M&amp;E", "title": "Impact evaluation among its cousins",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Activity", "Question it answers"],
              "rows": [
                  ["Needs assessment", "What is the problem, and for whom?"],
                  ["Process evaluation", "Was the programme delivered as designed?"],
                  ["Monitoring", "Are we on track against the plan?"],
                  ["Impact evaluation", "Did the programme cause the change?"],
                  ["Cost-effectiveness analysis", "Was the impact worth the cost?"]]},
             {"t": "hbox", "color": "cyan", "html": "Impact evaluation is one row in this table, "
              "not the whole table. It shines only when paired with the others &mdash; especially "
              "process evaluation, which tells you whether a null means the idea or the delivery "
              "failed."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Counterfactual &amp; Causal Inference"},

        {"type": "content", "label": "The Big Idea", "title": "The counterfactual: the road not taken",
         "blocks": [
             {"t": "term", "word": "Counterfactual",
              "def": "What would have happened to the very same people, in the same period, had "
              "the programme not existed. It is the benchmark against which impact is measured."},
             {"t": "body", "html": "Impact = outcome <em>with</em> the programme &minus; outcome "
              "<em>without</em> it, for the same group. The first we observe; the second we never "
              "can. Everything in this course is a strategy to estimate that missing half."},
         ]},

        {"type": "content", "label": "The Core Problem", "title": "The fundamental problem of causal inference",
         "blocks": [
             {"t": "body", "html": "A person is either treated or not. We can never observe the "
              "<em>same</em> person in both states at once, so the true individual counterfactual "
              "is permanently missing. This is the <strong>fundamental problem of causal "
              "inference</strong>."},
             {"t": "hbox", "color": "indigo", "html": "The solution is not to find each person's "
              "missing twin, but to build a <strong>comparison group</strong> that, on average, "
              "stands in for what the treated group would have looked like untreated."},
         ]},

        {"type": "content", "label": "The Wrong Counterfactuals", "title": "Two tempting comparisons that mislead",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Before vs after", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Compare the same group before and after. "
                   "But the world moved on too &mdash; you confuse the programme with everything "
                   "else that changed (the monsoon, prices, other schemes)."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Participants vs non-participants", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Compare those who joined to those who didn't. "
                   "But joiners often differ &mdash; more motivated, better placed. That difference "
                   "is selection bias, not impact."}]}]},
             {"t": "hbox", "color": "amber", "html": "Both are easy, cheap and wrong. A credible "
              "counterfactual is the whole game."},
         ]},

        {"type": "content", "label": "The Central Threat", "title": "Selection bias, defined",
         "blocks": [
             {"t": "term", "word": "Selection bias",
              "def": "When the people who receive a programme differ systematically from those "
              "who don't &mdash; in ways that also affect the outcome &mdash; so a naive "
              "comparison mixes the programme's effect with those pre-existing differences."},
             {"t": "body", "html": "If a skills programme enrols the most motivated youth, their "
              "later success partly reflects motivation, not training. Selection bias is the "
              "single biggest reason naive evaluations overstate impact."},
         ]},

        {"type": "content", "label": "See It", "title": "Why volunteers make a misleading comparison",
         "blocks": [
             {"t": "chart", "canvas": "selbiasChart",
              "title": "Illustrative: who self-selects into a training programme",
              "source": "Illustrative example, not real data",
              "type": "bar",
              "data": {"labels": ["Prior schooling (yrs)", "Baseline income (₹000)",
                                  "Motivation score"],
                       "datasets": [
                           {"label": "Joiners", "data": [9.2, 6.8, 7.5],
                            "backgroundColor": "#0EA5E9"},
                           {"label": "Non-joiners", "data": [6.1, 5.2, 4.3],
                            "backgroundColor": "#94A3B8"}]},
              "options": {"__js__": "{ scales:{ y:{ beginAtZero:true } } }"}},
             {"t": "hbox", "color": "red", "html": "Joiners already differ <em>before</em> the "
              "programme. Comparing their later outcomes to non-joiners' measures who they were, "
              "not what the programme did."},
         ]},

        {"type": "content", "label": "The Goal", "title": "What a good comparison group must satisfy",
         "blocks": [
             {"t": "bullets", "items": [
                 "It looks like the treatment group <strong>before</strong> the programme &mdash; "
                 "same characteristics, same trajectory",
                 "It is exposed to the <strong>same outside forces</strong> &mdash; weather, "
                 "prices, other schemes",
                 "The <strong>only</strong> systematic difference is the programme itself"]},
             {"t": "hbox", "color": "green", "html": "Get this right and the comparison group's "
              "outcomes are a credible estimate of the treatment group's counterfactual. Every "
              "method that follows is a different way to build such a group."},
         ]},

        {"type": "content", "label": "Two Estimands", "title": "ATE and ATT: effect on whom?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "ATE", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>Average Treatment Effect</strong> "
                   "&mdash; the effect if <em>everyone</em> in the population were treated."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "ATT", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>Average Treatment effect on the "
                   "Treated</strong> &mdash; the effect among those who <em>actually</em> received "
                   "the programme. Often the policy-relevant one."}]}]},
             {"t": "hbox", "color": "amber", "html": "They differ when the programme works "
              "differently for participants than for everyone. Always ask which one a study "
              "reports &mdash; and which one your decision needs."},
         ]},

        {"type": "content", "label": "The Logic in One Line", "title": "Every method, one promise",
         "blocks": [
             {"t": "body", "html": "Strip away the jargon and every design in this course makes "
              "the same promise: <strong>my comparison group is a credible stand-in for the "
              "treatment group's counterfactual.</strong> Methods differ only in <em>how</em> "
              "they make that promise believable."},
             {"t": "flow", "steps": [
                 "RCT: a lottery makes the groups alike",
                 "RD: the cutoff makes near-neighbours alike",
                 "DiD: a shared trend makes changes comparable",
                 "Matching: observed traits make pairs alike"]},
             {"t": "hbox", "color": "green", "html": "Judge any study by asking: how believable is "
              "<em>its</em> version of that promise &mdash; and what would break it?"},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Theory of Change &amp; Evaluation Questions"},

        {"type": "content", "label": "Start Here", "title": "No theory of change, no evaluation",
         "blocks": [
             {"t": "term", "word": "Theory of change",
              "def": "An explicit map of how and why a programme's activities are expected to "
              "lead to its intended outcomes &mdash; the chain of cause and effect, plus the "
              "assumptions at each link."},
             {"t": "body", "html": "Before measuring impact, you must state what impact you "
              "expect and through what pathway. A vague programme cannot be rigorously evaluated."},
         ]},

        {"type": "content", "label": "The Causal Chain", "title": "Map the pathway, link by link",
         "blocks": [
             {"t": "flow", "steps": [
                 "Cash transfer to mothers",
                 "more household income",
                 "more spent on food &amp; care",
                 "better child nutrition",
                 "lower stunting"]},
             {"t": "hbox", "color": "amber", "html": "Each arrow is an <strong>assumption</strong> "
              "that can fail. If transfers are spent elsewhere, or food prices rise, the chain "
              "breaks &mdash; and that is exactly what evaluation should test."},
         ]},

        {"type": "content", "label": "Assumptions", "title": "The arrows are where programmes fail",
         "blocks": [
             {"t": "body", "html": "A theory of change makes assumptions visible so you can check "
              "them. Most programmes that 'fail' did not fail because the idea was wrong &mdash; "
              "they failed at a specific, checkable link."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Implementation failure", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The chain was never delivered &mdash; "
                   "training didn't happen, transfers didn't arrive. The theory is untested."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Theory failure", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Everything was delivered, but an assumed "
                   "link did not hold &mdash; the idea itself was wrong."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Impact evaluation paired with monitoring lets "
              "you tell these two apart &mdash; a null result means little if the programme never "
              "actually reached people."},
         ]},

        {"type": "content", "label": "Framing", "title": "Turn the theory into evaluation questions",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Impact question:</strong> did the programme change the outcome, by how "
                 "much, for whom?",
                 "<strong>Mechanism question:</strong> through which link in the chain?",
                 "<strong>Process question:</strong> was it delivered as designed?",
                 "<strong>Cost question:</strong> was the impact worth what it cost?"]},
             {"t": "hbox", "color": "amber", "html": "Only the first is strictly an impact "
              "question &mdash; but a good evaluation usually answers several, because 'did it "
              "work?' is rarely enough to act on."},
         ]},

        {"type": "content", "label": "A Good Question", "title": "What a sharp evaluation question looks like",
         "blocks": [
             {"t": "body", "html": "A usable impact question names the <strong>intervention</strong>, "
              "the <strong>population</strong>, the <strong>outcome</strong>, the "
              "<strong>comparison</strong> and the <strong>timeframe</strong>."},
             {"t": "hbox", "color": "green", "html": "<em>Weak:</em> 'Does our programme help?' "
              "<em>Strong:</em> 'Does 18 months of monthly cash transfers to mothers of under-2s "
              "in Koraput reduce child stunting, relative to comparable villages without "
              "transfers?'"},
         ]},

        {"type": "content", "label": "Scope", "title": "Choose the right question, not every question",
         "blocks": [
             {"t": "body", "html": "You cannot evaluate everything. A focused evaluation that "
              "answers one decision well beats a sprawling one that answers many vaguely. Let the "
              "<strong>decision you face</strong> dictate the question."},
             {"t": "hbox", "color": "cyan", "html": "Ask up front: what would we <em>do</em> "
              "differently if the answer were yes, versus no? If nothing changes either way, the "
              "evaluation may not be worth running."},
         ]},

        {"type": "content", "label": "When NOT to do it", "title": "When an impact evaluation is the wrong call",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "The programme is still changing weekly &mdash; there is nothing stable to evaluate",
                 "The intervention is already proven and the question is purely operational",
                 "No credible comparison group is possible (e.g. a universal, simultaneous rollout)",
                 "The budget and timeline cannot support a rigorous design &mdash; a weak IE is worse than none",
                 "The decision is already made and evidence will not change it"]},
             {"t": "hbox", "color": "amber", "html": "A badly underpowered or poorly identified "
              "impact evaluation can mislead more than no evaluation at all. Knowing when to walk "
              "away is a skill."},
         ]},

        {"type": "content", "label": "Evaluability", "title": "Run an evaluability check first",
         "blocks": [
             {"t": "body", "html": "An <strong>evaluability assessment</strong> asks, before you "
              "commit: is this programme well-defined, stable and measurable enough to evaluate "
              "credibly &mdash; and will anyone act on the result?"},
             {"t": "flow", "steps": [
                 "Clear theory of change?",
                 "Measurable outcomes?",
                 "A feasible counterfactual?",
                 "A decision waiting on the answer?"]},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Randomised Experiments (RCTs)"},

        {"type": "content", "label": "The Gold Standard", "title": "Randomisation: let the lottery build the counterfactual",
         "blocks": [
             {"t": "term", "word": "Randomised controlled trial (RCT)",
              "def": "A study in which eligible units are assigned to treatment or control "
              "<em>by chance</em>, so the two groups are comparable in expectation and the "
              "difference in their outcomes estimates the causal effect."},
             {"t": "body", "html": "If a coin flip decides who gets the programme, the treatment "
              "and control groups have no systematic reason to differ &mdash; so any later "
              "difference in outcomes can be attributed to the programme."},
         ]},

        {"type": "content", "label": "Why It Works", "title": "Chance balances what you can and cannot see",
         "blocks": [
             {"t": "body", "html": "This is the deep power of randomisation: with enough units, "
              "it balances the two groups on <strong>observed</strong> characteristics (age, "
              "caste, income) <em>and</em> on <strong>unobserved</strong> ones (motivation, "
              "ability, family support) &mdash; in expectation."},
             {"t": "hbox", "color": "green", "html": "No other method can claim to balance the "
              "<em>unobservable</em> factors. That is why a well-run RCT has the strongest claim "
              "to internal validity."},
         ]},

        {"type": "content", "label": "Check Balance", "title": "Show the groups started alike",
         "blocks": [
             {"t": "chart", "canvas": "balanceChart",
              "title": "Illustrative baseline balance: treatment vs control",
              "source": "Illustrative example, not real data",
              "type": "bar",
              "data": {"labels": ["% female", "Mean age", "Yrs schooling", "% below poverty line"],
                       "datasets": [
                           {"label": "Treatment", "data": [51, 34, 6.2, 42],
                            "backgroundColor": "#10B981"},
                           {"label": "Control", "data": [50, 33, 6.4, 41],
                            "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ scales:{ y:{ beginAtZero:true } } }"}},
             {"t": "hbox", "color": "cyan", "html": "A <strong>balance table</strong> like this is "
              "the first thing to check in any RCT: if randomisation worked, the groups look alike "
              "at baseline on every measured characteristic."},
         ]},

        {"type": "content", "label": "J-PAL", "title": "Who champions the RCT in development",
         "blocks": [
             {"t": "body", "html": "The <strong>Abdul Latif Jameel Poverty Action Lab (J-PAL)</strong>, "
              "based at MIT, has run hundreds of randomised evaluations of anti-poverty programmes "
              "worldwide, including across South Asia. Its founders, Abhijit Banerjee and Esther "
              "Duflo, shared the 2019 Nobel Prize in Economics (with Michael Kremer) for this "
              "experimental approach."},
             {"t": "hbox", "color": "cyan", "html": "Its sister network <strong>3ie</strong> (the "
              "International Initiative for Impact Evaluation) funds and synthesises impact "
              "evaluations across the Global South."},
         ]},

        {"type": "content", "label": "Growth", "title": "How randomised evaluations took off",
         "blocks": [
             {"t": "chart", "canvas": "rctGrowthChart",
              "title": "Illustrative: the rise of randomised evaluations in development",
              "source": "Illustrative trend, schematic only",
              "type": "line",
              "data": {"labels": ["2000", "2004", "2008", "2012", "2016", "2020", "2024"],
                       "datasets": [{"label": "Published randomised evaluations (index)",
                                     "data": [5, 20, 60, 140, 280, 480, 720],
                                     "borderColor": "#0EA5E9",
                                     "backgroundColor": "rgba(14,165,233,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true, title:{display:true,text:'Cumulative index (schematic)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Schematic, not a precise count &mdash; but "
              "the direction is real: randomised impact evaluation went from rare to mainstream in "
              "development over two decades."},
         ]},

        {"type": "content", "label": "Unit of Randomisation", "title": "Randomise individuals, or whole clusters?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Individual", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Each person assigned separately. Most "
                   "statistically efficient, but risky when treated and control people mix and "
                   "influence each other."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Cluster", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Whole villages, schools or clinics assigned "
                   "together. Needed when the programme operates at group level or spillovers are "
                   "likely &mdash; but you need <em>many</em> clusters."}]}]},
             {"t": "hbox", "color": "red", "html": "Cluster designs cost statistical power: 40 "
              "villages of 50 people is far weaker than 2,000 individually randomised people. "
              "Power is driven by the number of clusters, not just total people."},
         ]},

        {"type": "content", "label": "Spillovers", "title": "When treatment leaks to the control group",
         "blocks": [
             {"t": "body", "html": "If treated and control units interact, the programme can "
              "<strong>spill over</strong> &mdash; a dewormed child stops infecting an untreated "
              "neighbour. The control group is no longer a clean counterfactual, and the effect "
              "is understated."},
             {"t": "hbox", "color": "amber", "html": "Cluster randomisation &mdash; treating "
              "whole villages &mdash; is the usual defence, keeping treated and control units far "
              "enough apart that they don't contaminate each other."},
         ]},

        {"type": "content", "label": "Ethics", "title": "Equipoise: the ethics of the lottery",
         "blocks": [
             {"t": "term", "word": "Equipoise",
              "def": "Genuine uncertainty about whether the programme works. When we honestly do "
              "not know, randomly choosing who gets it first is defensible &mdash; and the "
              "evaluation resolves the uncertainty for everyone."},
             {"t": "bullets", "sm": True, "items": [
                 "Random <strong>phase-in</strong>: everyone gets it eventually; the lottery just sets the order",
                 "Randomise only when demand <strong>exceeds</strong> supply &mdash; a lottery is already fair",
                 "Never withhold a known, effective, life-saving intervention to run a trial"]},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Quasi-Experimental Designs"},

        {"type": "content", "label": "When You Can't Randomise", "title": "Finding a counterfactual in the real world",
         "blocks": [
             {"t": "body", "html": "Often you cannot randomise &mdash; the programme is already "
              "running, or rolled out to everyone, or randomisation is infeasible. "
              "<strong>Quasi-experimental</strong> designs exploit natural variation to "
              "approximate a control group."},
             {"t": "hbox", "color": "amber", "html": "They can be highly credible &mdash; but "
              "each rests on an <strong>assumption</strong> you must argue for, not just an "
              "untouchable coin flip. Know the assumption behind every design."},
         ]},

        {"type": "content", "label": "Diff-in-Diff", "title": "Difference-in-differences: subtract the trend",
         "blocks": [
             {"t": "body", "html": "<strong>Difference-in-differences (DiD)</strong> compares the "
              "<em>change</em> in a treated group with the <em>change</em> in a comparison group "
              "over the same period. Subtracting the comparison group's change removes whatever "
              "trend would have happened anyway."},
             {"t": "flow", "steps": [
                 "Treated: before &rarr; after",
                 "Comparison: before &rarr; after",
                 "Impact = (treated change) &minus; (comparison change)"]},
         ]},

        {"type": "content", "label": "See It", "title": "DiD: the gap that opens up",
         "blocks": [
             {"t": "chart", "canvas": "didChart",
              "title": "Illustrative DiD: outcome before and after, treated vs comparison",
              "source": "Illustrative example, not real data",
              "type": "line",
              "data": {"labels": ["Baseline", "Intervention", "Endline"],
                       "datasets": [
                           {"label": "Treated", "data": [40, None, 62],
                            "borderColor": "#10B981", "backgroundColor": "#10B981",
                            "tension": 0, "spanGaps": True, "borderWidth": 3},
                           {"label": "Comparison", "data": [42, None, 50],
                            "borderColor": "#6366F1", "backgroundColor": "#6366F1",
                            "tension": 0, "spanGaps": True, "borderWidth": 3},
                           {"label": "Counterfactual for treated", "data": [40, None, 48],
                            "borderColor": "#94A3B8", "backgroundColor": "#94A3B8",
                            "borderDash": [6, 4], "tension": 0, "spanGaps": True, "borderWidth": 2}]},
              "options": {"__js__": "{ scales:{ y:{ beginAtZero:false, title:{display:true,text:'Outcome (%)'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The grey dashed line is the assumed "
              "counterfactual: where the treated group <em>would</em> have gone, tracking the "
              "comparison group's trend. The estimated impact is the gap above it (~14 points)."},
         ]},

        {"type": "content", "label": "The Key Assumption", "title": "DiD identifies only under parallel trends",
         "blocks": [
             {"t": "term", "word": "Parallel trends",
              "def": "The assumption that, absent the programme, the treated and comparison groups "
              "would have moved in parallel &mdash; the same trend over time. DiD is only valid "
              "if this holds."},
             {"t": "hbox", "color": "red", "html": "If the groups were already diverging before "
              "the programme, DiD attributes that pre-existing divergence to the programme &mdash; "
              "and overstates impact. Always check trends in the <em>pre-period</em> first."},
         ]},

        {"type": "content", "label": "Regression Discontinuity", "title": "RD: compare just either side of a cutoff",
         "blocks": [
             {"t": "body", "html": "Many programmes use a sharp <strong>eligibility cutoff</strong> "
              "&mdash; a poverty score below 0.33, a test mark above 60. People just <em>above</em> "
              "and just <em>below</em> the line are nearly identical, except one gets the programme. "
              "That tiny band is a natural experiment."},
             {"t": "term", "word": "Regression discontinuity (RD)",
              "def": "A design that estimates impact from the jump in outcomes exactly at an "
              "eligibility threshold, comparing units narrowly above and below the cutoff."},
         ]},

        {"type": "content", "label": "See It", "title": "RD: read the jump at the cutoff",
         "blocks": [
             {"t": "chart", "canvas": "rdChart",
              "title": "Illustrative RD: outcome jumps at the eligibility threshold",
              "source": "Illustrative example, not real data",
              "type": "scatter",
              "data": {"datasets": [
                  {"label": "Below cutoff (ineligible)",
                   "data": [{"x": 10, "y": 31}, {"x": 20, "y": 35}, {"x": 30, "y": 38},
                            {"x": 40, "y": 42}, {"x": 49, "y": 46}],
                   "backgroundColor": "#94A3B8", "pointRadius": 5},
                  {"label": "Above cutoff (eligible / treated)",
                   "data": [{"x": 51, "y": 60}, {"x": 60, "y": 63}, {"x": 70, "y": 66},
                            {"x": 80, "y": 70}, {"x": 90, "y": 73}],
                   "backgroundColor": "#0EA5E9", "pointRadius": 5}]},
              "options": {"__js__": "{ scales:{ x:{ title:{display:true,text:'Eligibility score (cutoff = 50)'} }, y:{ title:{display:true,text:'Outcome'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "The vertical jump at the cutoff (~14 points) "
              "is the estimated effect. Crucially, RD gives a <strong>local</strong> effect &mdash; "
              "valid for units <em>near the threshold</em>, not for everyone."},
         ]},

        {"type": "content", "label": "Matching / PSM", "title": "Matching: build a statistical twin",
         "blocks": [
             {"t": "body", "html": "<strong>Matching</strong> pairs each treated unit with one or "
              "more untreated units that look alike on observed characteristics. "
              "<strong>Propensity-score matching (PSM)</strong> matches on a single number: the "
              "estimated probability of being treated, given those characteristics."},
             {"t": "hbox", "color": "red", "html": "The fatal limit: matching can only balance "
              "what you <em>measured</em>. If treated and untreated differ on something unobserved "
              "&mdash; motivation, hidden need &mdash; matching cannot fix it. Weaker than an RCT."},
         ]},

        {"type": "content", "label": "Instrumental Variables", "title": "IV: borrow some random-like variation",
         "blocks": [
             {"t": "body", "html": "An <strong>instrumental variable</strong> is an outside factor "
              "that nudges people into the programme but has no other path to the outcome. It "
              "isolates the slice of programme take-up that behaves as if random &mdash; e.g. "
              "distance to a facility shifting who enrols."},
             {"t": "hbox", "color": "red", "html": "A valid instrument needs <strong>two</strong> "
              "things: <em>relevance</em> (it genuinely shifts take-up) <em>and</em> the "
              "<strong>exclusion restriction</strong> (it affects the outcome <em>only</em> "
              "through take-up). The second can never be fully proven &mdash; only argued."},
         ]},

        {"type": "content", "label": "Compare", "title": "The quasi-experimental toolkit at a glance",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Design", "Exploits", "Key assumption"],
              "rows": [
                  ["Diff-in-differences", "Before/after &times; treated/comparison", "Parallel trends"],
                  ["Regression discontinuity", "A sharp eligibility cutoff", "Units similar across the cutoff"],
                  ["Matching / PSM", "Observed similarity", "No unobserved confounders"],
                  ["Instrumental variables", "An external nudge into take-up", "Relevance + exclusion restriction"]]},
             {"t": "hbox", "color": "cyan", "html": "Each is only as credible as its assumption. "
              "A commissioner's job is to ask: <em>what must be true for this to identify the "
              "effect &mdash; and is it?</em>"},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Choosing a Method"},

        {"type": "content", "label": "The Trade-Off", "title": "There is no single best method",
         "blocks": [
             {"t": "body", "html": "The 'best' design is the most credible one that is "
              "<strong>feasible</strong> and <strong>ethical</strong> for your situation. Method "
              "choice is a negotiation between three forces, not a ranking to memorise."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Validity", "label": "How credible is the causal claim?", "color": "cyan"},
                 {"num": "Feasibility", "label": "Can you actually do it, in time and budget?", "color": "amber"},
                 {"num": "Ethics", "label": "Is it fair to those involved?", "color": "green"}]},
         ]},

        {"type": "content", "label": "Internal Validity", "title": "Internal validity: is the answer right here?",
         "blocks": [
             {"t": "term", "word": "Internal validity",
              "def": "The degree to which a study correctly identifies the causal effect for the "
              "people and place it studied &mdash; free of selection bias and confounding."},
             {"t": "body", "html": "A well-run RCT typically has the strongest internal validity; "
              "a before-after comparison the weakest. Internal validity is the first hurdle: an "
              "answer that is wrong <em>here</em> is useless everywhere."},
         ]},

        {"type": "content", "label": "The Credibility Ladder", "title": "Designs ranked by credibility",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Design", "Counterfactual quality", "Credibility"],
              "rows": [
                  ["Randomised controlled trial", "Strongest &mdash; balances unobservables", "Highest"],
                  ["Regression discontinuity", "Strong, but local to the cutoff", "High"],
                  ["Difference-in-differences", "Good if parallel trends hold", "Medium-high"],
                  ["Instrumental variables", "Depends on a defensible instrument", "Conditional"],
                  ["Matching / PSM", "Only as good as observed variables", "Medium"],
                  ["Before-after / naive comparison", "No real counterfactual", "Lowest"]]},
             {"t": "hbox", "color": "amber", "html": "Climb as high as feasibility and ethics "
              "allow &mdash; but a credible quasi-experiment beats a badly run RCT. Execution "
              "matters as much as the rung."},
         ]},

        {"type": "content", "label": "Feasibility", "title": "What makes a design practical",
         "blocks": [
             {"t": "bullets", "items": [
                 "Is there a stage of rollout where you can still assign or compare?",
                 "Are baseline data and a comparison group available?",
                 "Do you have the sample size, budget and time the design needs?",
                 "Will the result arrive in time to inform the decision?"]},
             {"t": "hbox", "color": "cyan", "html": "The single biggest feasibility lever is "
              "<strong>timing</strong>: the best designs are built in <em>before</em> a programme "
              "starts, not retrofitted afterwards."},
         ]},

        {"type": "content", "label": "Design In Early", "title": "Plan the evaluation before the programme rolls out",
         "blocks": [
             {"t": "body", "html": "A staggered or phased rollout &mdash; which most large "
              "programmes need anyway &mdash; is a gift to evaluators. It creates a natural "
              "comparison group (those not yet reached) at no extra cost."},
             {"t": "hbox", "color": "green", "html": "Lesson for commissioners: involve the "
              "evaluator at the <em>design</em> stage. Retrofitting rigour onto a finished "
              "programme is the hardest and least credible path."},
         ]},

        {"type": "content", "label": "Mixed Methods", "title": "Quantitative tells you whether; qualitative tells you why",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Quantitative IE", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Estimates the size of the effect and how "
                   "sure we are. Answers <em>did it work, and by how much?</em>"}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Qualitative work", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Explains the mechanism, the surprises, the "
                   "implementation. Answers <em>why, how, and for whom?</em>"}]}]},
             {"t": "hbox", "color": "amber", "html": "The strongest evaluations combine both: a "
              "number you can trust, and a story that explains it. Neither alone is enough to act."},
         ]},

        {"type": "content", "label": "Decision Guide", "title": "A rough rule for choosing",
         "blocks": [
             {"t": "flow", "steps": [
                 "Can you assign at random, ethically? &rarr; RCT",
                 "Is there a sharp eligibility cutoff? &rarr; RD",
                 "Phased rollout with baseline data? &rarr; DiD",
                 "Only an external nudge into take-up? &rarr; IV",
                 "None of the above? &rarr; reconsider whether to run an IE"]},
         ]},

        {"type": "content", "label": "Execution Beats Elegance", "title": "A well-run simple design beats a botched fancy one",
         "blocks": [
             {"t": "body", "html": "The credibility ladder ranks <em>designs</em>, but in the "
              "field, <strong>execution</strong> decides everything. An RCT wrecked by attrition, "
              "spillovers and broken randomisation can be less trustworthy than a careful "
              "difference-in-differences."},
             {"t": "hbox", "color": "amber", "html": "So weigh the design <em>and</em> the team, "
              "the timeline and the field conditions together. Ambition you cannot execute is "
              "worse than modesty you can."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Sampling &amp; Statistical Power"},

        {"type": "content", "label": "The Stakes", "title": "Why an underpowered evaluation misleads",
         "blocks": [
             {"t": "body", "html": "If your sample is too small, even a real, useful effect can "
              "fail to reach statistical significance. You then conclude 'no impact' &mdash; when "
              "the truth is you simply could not <em>detect</em> it. This is the curse of the "
              "<strong>underpowered</strong> study."},
             {"t": "hbox", "color": "red", "html": "An underpowered evaluation wastes money and "
              "can kill a programme that actually works. Power must be planned <em>before</em> "
              "data collection &mdash; it cannot be fixed afterwards."},
         ]},

        {"type": "content", "label": "Definition", "title": "Statistical power, defined",
         "blocks": [
             {"t": "term", "word": "Statistical power",
              "def": "The probability that a study will detect a real effect of a given size, if "
              "one truly exists. By convention, evaluations aim for 80% power or more."},
             {"t": "body", "html": "Power of 80% means that if the programme really has the effect "
              "you assumed, you have an 80% chance of finding a statistically significant result "
              "&mdash; and a 20% chance of missing it."},
         ]},

        {"type": "content", "label": "MDE", "title": "Minimum detectable effect: what can you even see?",
         "blocks": [
             {"t": "term", "word": "Minimum detectable effect (MDE)",
              "def": "The smallest true effect a study is reliably able to detect, given its "
              "sample size, the outcome's variability and the desired power."},
             {"t": "hbox", "color": "amber", "html": "Flip the question round: with this sample, "
              "what is the smallest impact I could detect? If your MDE is a 10-point gain but the "
              "programme can realistically deliver 3, the study is doomed before it starts."},
         ]},

        {"type": "content", "label": "Drivers", "title": "What determines how big a sample you need",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Factor", "Effect on required sample"],
              "rows": [
                  ["Smaller expected effect", "Much larger sample needed"],
                  ["Higher outcome variability", "Larger sample needed"],
                  ["Higher power target (e.g. 90%)", "Larger sample needed"],
                  ["Clustered design", "Larger sample &mdash; driven by number of clusters"],
                  ["A good baseline to control for", "Smaller sample needed"]]},
             {"t": "hbox", "color": "cyan", "html": "The headline driver is effect size: detecting "
              "small effects is expensive. Be honest about how big an impact is plausible."},
         ]},

        {"type": "content", "label": "See It", "title": "How power rises with sample size",
         "blocks": [
             {"t": "chart", "canvas": "powerChart",
              "title": "Illustrative power curve: power vs sample size",
              "source": "Illustrative, schematic shape only",
              "type": "line",
              "data": {"labels": ["100", "300", "600", "1000", "1500", "2400", "4000"],
                       "datasets": [{"label": "Statistical power",
                                     "data": [0.22, 0.45, 0.63, 0.78, 0.86, 0.93, 0.98],
                                     "borderColor": "#6366F1",
                                     "backgroundColor": "rgba(99,102,241,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:1, title:{display:true,text:'Power'} }, x:{ title:{display:true,text:'Sample size per arm'} } } }"}},
             {"t": "hbox", "color": "green", "html": "Power climbs steeply at first, then flattens "
              "as it approaches 1. The dashed convention of 80% (~1,000 per arm here) is where "
              "most evaluations aim &mdash; beyond it, extra sample buys little."},
         ]},

        {"type": "content", "label": "Clustering", "title": "Why clusters cost you power",
         "blocks": [
             {"t": "body", "html": "When you randomise whole villages, people <em>within</em> a "
              "village resemble each other &mdash; they share the same school, water, weather. "
              "These correlated responses carry less independent information than the same number "
              "of unrelated individuals."},
             {"t": "hbox", "color": "red", "html": "So power is driven by the <strong>number of "
              "clusters</strong>, not the total headcount. Forty large villages can be weaker "
              "than a hundred small ones. Add clusters, not just people."},
         ]},

        {"type": "content", "label": "In Practice", "title": "Run a power calculation before you commit",
         "blocks": [
             {"t": "bullets", "items": [
                 "State the smallest effect worth detecting (your MDE)",
                 "Estimate outcome variability from prior data or a pilot",
                 "Account for clustering, attrition and partial take-up",
                 "Solve for the sample size that gives at least 80% power"]},
             {"t": "hbox", "color": "amber", "html": "Tools like J-PAL's resources and free "
              "software make this routine. Insist on seeing the power calculation in any "
              "evaluation proposal &mdash; a design without one is a red flag."},
         ]},

        {"type": "content", "label": "Two Errors", "title": "False positives and false negatives",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Type I (false positive)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Concluding the programme worked when it "
                   "didn't. Controlled by the significance level &mdash; conventionally a 5% risk."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Type II (false negative)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Missing a real effect. Its risk is "
                   "1 &minus; power &mdash; the very thing a good sample size guards against."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Underpowered studies are dominated by Type II "
              "error: they scream 'no effect' when they simply could not see one. Power is how you "
              "buy down that risk."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Measurement &amp; Data Collection"},

        {"type": "content", "label": "Outcomes First", "title": "Decide what to measure before how",
         "blocks": [
             {"t": "body", "html": "The outcome indicators flow straight from the theory of "
              "change. Choose them <strong>before</strong> the evaluation starts, define them "
              "precisely, and commit to them &mdash; so you cannot fish for whichever outcome "
              "happens to look good afterwards."},
             {"t": "hbox", "color": "cyan", "html": "Distinguish <strong>primary</strong> "
              "outcomes (the one or two you will judge success on) from <strong>secondary</strong> "
              "ones. Pre-specifying the primary outcome is a core discipline of credible IE."},
         ]},

        {"type": "content", "label": "Good Indicators", "title": "What makes an outcome indicator usable",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Valid", "label": "Captures the concept you actually care about", "color": "cyan"},
                 {"num": "Reliable", "label": "Gives the same reading on repeat measurement", "color": "green"},
                 {"num": "Sensitive", "label": "Moves when the real outcome moves", "color": "indigo"},
                 {"num": "Feasible", "label": "Can be measured affordably in the field", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Baseline / Endline", "title": "Measure before, measure after",
         "blocks": [
             {"t": "flow", "steps": [
                 "BASELINE: measure outcomes before the programme",
                 "RANDOMISE / ASSIGN: form treatment &amp; comparison",
                 "DELIVER: run the programme",
                 "ENDLINE: re-measure the same outcomes"]},
             {"t": "hbox", "color": "green", "html": "A baseline does double duty: it confirms the "
              "groups started balanced, and it sharpens power by letting you control for "
              "starting levels. Skip it only if you must."},
         ]},

        {"type": "content", "label": "Data Sources", "title": "Surveys and administrative data",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Survey data", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Collected for the evaluation &mdash; exactly "
                   "the outcomes you need, but costly, and prone to recall and reporting error."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Administrative data", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Already generated by the system &mdash; "
                   "school registers, HMIS, MGNREGA records. Cheap and continuous, but may not "
                   "measure quite what you want."}]}]},
             {"t": "hbox", "color": "amber", "html": "Linking your evaluation to existing "
              "administrative systems can slash cost and enable long-term follow-up &mdash; where "
              "the data quality is good enough to trust."},
         ]},

        {"type": "content", "label": "Measurement Bias", "title": "How measurement quietly corrupts a finding",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Social desirability:</strong> people report what they think you want to hear",
                 "<strong>Recall error:</strong> hazy memory of past income, illness, spending",
                 "<strong>Surveyor effects:</strong> who asks, and how, shifts the answer",
                 "<strong>Differential measurement:</strong> measuring treatment and control groups differently"]},
             {"t": "hbox", "color": "amber", "html": "The last is the most dangerous: if treated "
              "respondents are surveyed more enthusiastically than controls, you manufacture an "
              "effect out of thin air. Measure both groups identically."},
         ]},

        {"type": "content", "label": "Good Instruments", "title": "Build the survey to avoid bias",
         "blocks": [
             {"t": "bullets", "items": [
                 "Pilot every instrument before the real round &mdash; without exception",
                 "Use neutral wording; avoid leading and double-barrelled questions",
                 "Blind enumerators to treatment status where you possibly can",
                 "Use the same instrument, timing and team for both groups"]},
             {"t": "hbox", "color": "cyan", "html": "Where feasible, prefer objective measures "
              "(test scores, anthropometry, biomarkers, admin records) over self-report &mdash; "
              "they are harder to bias."},
         ]},

        {"type": "content", "label": "Attrition", "title": "When people drop out of the study",
         "blocks": [
             {"t": "term", "word": "Attrition",
              "def": "The loss of study participants between baseline and endline &mdash; through "
              "migration, refusal or death &mdash; who cannot be measured at follow-up."},
             {"t": "hbox", "color": "red", "html": "Attrition is dangerous when it differs between "
              "groups, or relates to the outcome &mdash; if the worst-off in the treatment group "
              "leave, the survivors look artificially good. Track it, report it, and test whether "
              "it is balanced."},
         ]},

        {"type": "content", "label": "Timing", "title": "When you measure shapes what you find",
         "blocks": [
             {"t": "body", "html": "Measure too <strong>early</strong> and the effect has not yet "
              "appeared &mdash; a nutrition programme needs months to move stunting. Measure too "
              "<strong>late</strong> and a real effect may have faded, or comparison villages may "
              "have caught up."},
             {"t": "hbox", "color": "amber", "html": "Let the theory of change set the clock: when "
              "should this outcome plausibly respond? Endline timing is a design choice, not an "
              "afterthought &mdash; and a second follow-up tells you whether effects last."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Analysis &amp; Interpreting Results"},

        {"type": "content", "label": "Effect Size", "title": "How big, not just whether",
         "blocks": [
             {"t": "body", "html": "The first thing to read is the <strong>effect size</strong>: "
              "how much did the outcome change? Report it in units a decision-maker understands "
              "&mdash; percentage points, rupees, days of schooling &mdash; not just a coefficient."},
             {"t": "hbox", "color": "amber", "html": "Then ask the practical question: is an effect "
              "of <em>this</em> size worth the programme's cost? A real but tiny effect may not "
              "justify the spend."},
         ]},

        {"type": "content", "label": "Significance", "title": "Significant is not the same as important",
         "blocks": [
             {"t": "term", "word": "Statistical significance",
              "def": "A result unlikely to have arisen by chance alone if the programme truly had "
              "no effect. It speaks to confidence, not to the size or importance of the effect."},
             {"t": "hbox", "color": "red", "html": "With a huge sample, a trivially small effect "
              "can be 'statistically significant'. With a small sample, a large, real effect can "
              "miss significance. Always read the effect size <em>and</em> the uncertainty &mdash; "
              "never the p-value alone."},
         ]},

        {"type": "content", "label": "Confidence Intervals", "title": "Report the range, not just the point",
         "blocks": [
             {"t": "body", "html": "An estimated impact of '6 percentage points' is shorthand for "
              "a <strong>range</strong> &mdash; say 2 to 10 &mdash; the confidence interval. The "
              "width of that range tells you how precisely the effect was estimated."},
             {"t": "hbox", "color": "cyan", "html": "If the interval comfortably excludes zero, "
              "the effect is reasonably firm. If it straddles zero, the evaluation cannot rule "
              "out 'no effect'. Read intervals, not just stars."},
         ]},

        {"type": "content", "label": "ITT vs ToT", "title": "Intention-to-treat vs treatment-on-the-treated",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Intention-to-treat (ITT)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The effect of being <em>offered</em> the "
                   "programme &mdash; everyone assigned to treatment, whether or not they took it "
                   "up. Reflects real-world rollout, where take-up is never 100%."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Treatment-on-treated (ToT)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The effect on those who <em>actually</em> "
                   "took up the programme. Usually larger than ITT, since it strips out the "
                   "non-participants."}]}]},
             {"t": "hbox", "color": "amber", "html": "Keep groups by <em>original assignment</em> "
              "to preserve the randomisation. For a policy that can only offer (not force) a "
              "programme, ITT is often the more honest, decision-relevant number."},
         ]},

        {"type": "content", "label": "Heterogeneity", "title": "Did it work differently for different people?",
         "blocks": [
             {"t": "body", "html": "An average effect can hide wide variation. A programme might "
              "help women but not men, or the poorest but not the better-off. "
              "<strong>Heterogeneity analysis</strong> looks for these differences &mdash; and is "
              "often where the most useful learning lives."},
             {"t": "hbox", "color": "red", "html": "But beware: test enough subgroups and one will "
              "look 'significant' by chance. Pre-specify the subgroups you care about, and treat "
              "surprising ones as hypotheses to test next time, not conclusions."},
         ]},

        {"type": "content", "label": "Null Results", "title": "A null result is not a failure",
         "blocks": [
             {"t": "body", "html": "Finding <em>no</em> significant impact is genuine, valuable "
              "knowledge &mdash; it can stop a wasteful programme or redirect resources. But "
              "distinguish a true zero from an inconclusive one."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "A real null", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Well-powered study, tight interval around "
                   "zero: the programme genuinely did little. Act on it."}]}],
              "right": [{"t": "panel", "color": "red", "title": "An empty null", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Underpowered, wide interval: you simply "
                   "couldn't detect an effect. This tells you almost nothing."}]}]},
         ]},

        {"type": "content", "label": "Honesty", "title": "Read against the threats you learned",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Was the design well identified &mdash; did the key assumption hold?",
                 "Were the groups balanced at baseline?",
                 "Was attrition low and balanced across groups?",
                 "Is the primary outcome the pre-specified one, or a convenient substitute?",
                 "Is the effect size practically meaningful, not just significant?"]},
         ]},

        {"type": "content", "label": "Mind the Multiple", "title": "Test twenty outcomes and one will 'work'",
         "blocks": [
             {"t": "body", "html": "Measure enough outcomes and subgroups and, by chance alone, "
              "roughly one in twenty will look 'significant' at the usual threshold. Reporting "
              "only the winners &mdash; <strong>p-hacking</strong> &mdash; manufactures findings "
              "that will not replicate."},
             {"t": "hbox", "color": "cyan", "html": "Defences: pre-specify the primary outcome, "
              "limit the number of tests, and adjust for multiple comparisons. Treat a lone "
              "surprising result as a hypothesis for the next study, not a conclusion."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "External Validity, Cost &amp; Ethics"},

        {"type": "content", "label": "Will It Travel?", "title": "External validity: will it work elsewhere?",
         "blocks": [
             {"t": "term", "word": "External validity",
              "def": "The degree to which a result found in one place, time and population holds "
              "in another. A programme that worked in Bihar may not work the same way in Tamil "
              "Nadu &mdash; or at national scale."},
             {"t": "body", "html": "Internal validity asks 'is the answer right <em>here</em>?'; "
              "external validity asks 'does it transfer <em>there</em>?' A perfectly identified "
              "RCT can still mislead if you scale it into a different context."},
         ]},

        {"type": "content", "label": "What Breaks Transfer", "title": "Why results don't always generalise",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Context:</strong> different markets, culture, institutions",
                 "<strong>Implementation:</strong> a research-grade pilot run far better than a government scale-up",
                 "<strong>Scale effects:</strong> general-equilibrium changes once everyone is treated",
                 "<strong>Population:</strong> the studied group differs from the target group"]},
             {"t": "hbox", "color": "amber", "html": "Don't ask only 'did it work?' Ask 'why did "
              "it work, and are those conditions present where I want to use it?' Mechanism "
              "travels better than a headline number."},
         ]},

        {"type": "content", "label": "Cost-Effectiveness", "title": "Impact per rupee, not impact alone",
         "blocks": [
             {"t": "body", "html": "Impact is only half the decision. <strong>Cost-effectiveness</strong> "
              "asks how much outcome you buy per rupee &mdash; letting you compare very different "
              "programmes chasing the same goal."},
             {"t": "hbox", "color": "green", "html": "A smaller-impact programme that costs a "
              "tenth as much may be the better buy. Always pair the effect size with a credible "
              "cost figure &mdash; the question is impact <em>per rupee</em>, not impact alone."},
         ]},

        {"type": "content", "label": "Do No Harm", "title": "Ethics: the programme and the study both",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Informed consent:</strong> participants understand and may refuse, without penalty",
                 "<strong>Do no harm:</strong> the study itself must not worsen anyone's situation",
                 "<strong>Privacy:</strong> protect respondents' data, especially the marginalised",
                 "<strong>Ethics review:</strong> an independent board (IRB) approves the design"]},
             {"t": "hbox", "color": "amber", "html": "Recall equipoise: random assignment is "
              "ethical only when we genuinely do not know what works &mdash; never withhold a "
              "proven, essential intervention to run a trial."},
         ]},

        {"type": "content", "label": "Transparency", "title": "Pre-registration and open evidence",
         "blocks": [
             {"t": "term", "word": "Pre-registration",
              "def": "Publicly recording your hypotheses, primary outcome and analysis plan "
              "<em>before</em> collecting or seeing the data &mdash; so you cannot quietly change "
              "the goalposts to fit the result."},
             {"t": "hbox", "color": "cyan", "html": "Registries like the AEA RCT Registry and "
              "3ie's records make evaluation honest and cumulative. Pre-registration is the main "
              "defence against cherry-picking and p-hacking."},
         ]},

        {"type": "content", "label": "Publication Bias", "title": "The file-drawer problem",
         "blocks": [
             {"t": "body", "html": "Studies that find big, positive effects get published and "
              "shared; null results often languish in a file drawer. So the published record can "
              "<strong>overstate</strong> what works &mdash; you see the hits, not the misses."},
             {"t": "hbox", "color": "green", "html": "Trust <strong>systematic reviews</strong> "
              "and replications over any single splashy study. Bodies like 3ie and the Campbell "
              "Collaboration synthesise across studies precisely to correct this bias."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Using IE for Decisions &amp; Further Reading"},

        {"type": "content", "label": "Commissioning", "title": "How to commission an impact evaluation well",
         "blocks": [
             {"t": "flow", "steps": [
                 "Define the decision the evidence will inform",
                 "Write a sharp evaluation question",
                 "Bring the evaluator in at design stage",
                 "Demand a power calculation &amp; identification strategy",
                 "Pre-register; plan to act on whatever you find"]},
             {"t": "hbox", "color": "cyan", "html": "Your leverage as commissioner is greatest "
              "<em>before</em> the contract is signed. Ask the hard questions then, not when the "
              "report lands."},
         ]},

        {"type": "content", "label": "Reading a Proposal", "title": "Questions to ask any evaluator",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "What is the counterfactual, and how credible is it?",
                 "What must be true for this design to identify the effect?",
                 "What is the MDE, and is it smaller than a plausible impact?",
                 "How will you handle attrition, spillovers and partial take-up?",
                 "Is the primary outcome pre-specified, and will you pre-register?"]},
         ]},

        {"type": "content", "label": "The Limits", "title": "The limits of 'what works'",
         "blocks": [
             {"t": "body", "html": "Impact evaluation tells you whether a specific programme "
              "worked in a specific place. It cannot, by itself, tell you what to value, how to "
              "navigate trade-offs, or whether the result will hold at scale."},
             {"t": "quote",
              "text": "Evidence informs judgement; it does not replace it. The number is an "
              "input to a decision, never the decision itself.",
              "attr": "&mdash; a working principle for evidence use"},
         ]},

        {"type": "content", "label": "Evidence Into Action", "title": "Why good evidence still goes unused",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Findings arrive after the decision was already made",
                 "Results are framed for academics, not for managers",
                 "No one owns turning the finding into a change in practice",
                 "Inconvenient nulls are quietly shelved"]},
             {"t": "hbox", "color": "green", "html": "Plan use from the start: agree who decides "
              "what, by when, and commit to act on the answer &mdash; including if it is "
              "disappointing."},
         ]},

        {"type": "content", "label": "The Cornerstone", "title": "The one book to read: Gertler et al.",
         "blocks": [
             {"t": "body", "html": "<strong><em>Impact Evaluation in Practice</em></strong> by "
              "Paul Gertler, Sebastian Martinez, Patrick Premand, Laura Rawlings and Christel "
              "Vermeersch (World Bank) is the standard, free, practitioner-friendly handbook "
              "&mdash; the natural next step after this deck."},
             {"t": "hbox", "color": "cyan", "html": "It walks through counterfactuals, every "
              "design in this course, and a worked case study, in plain language. Download it "
              "free from the World Bank's Open Knowledge Repository."},
         ]},

        {"type": "content", "label": "Where to Learn More", "title": "Trusted sources and resources",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Source", "What it offers", "Note"],
              "rows": [
                  ["J-PAL", "Randomised evaluations, training, evidence reviews", "MIT-based; strong South Asia office"],
                  ["3ie", "Impact evaluations &amp; systematic reviews of the Global South", "Searchable evidence portal"],
                  ["World Bank DIME", "Methods, guidance, the Gertler et al. handbook", "Free handbook &amp; toolkits"],
                  ["Campbell Collaboration", "Systematic reviews of social interventions", "Synthesis across studies"],
                  ["AEA RCT Registry", "Pre-registered trial protocols", "Check what was promised"]]},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Always ask 'compared to what?'</strong> &mdash; the counterfactual is everything",
                 "<strong>Randomisation balances the unobservable</strong>, in expectation &mdash; no other method can claim that",
                 "<strong>Every quasi-experiment rests on an assumption</strong> &mdash; name it and test it",
                 "<strong>Plan power before, read effect size after</strong> &mdash; significance is not importance",
                 "<strong>Know when NOT to run an IE</strong> &mdash; and pre-register when you do"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Econometrics</strong>, <strong>Data Literacy</strong> and "
              "<strong>Research Ethics</strong> 101 courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Impact Evaluation 101 &middot; Complete",
         "headline": "Now go ask:<br>compared to what?",
         "byline": "You don't have to run the regression to commission an evaluation well "
                   "&mdash; you need to frame the question, choose a credible counterfactual, "
                   "and read the findings honestly. Explore the rest of the ImpactMojo 101 "
                   "Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
