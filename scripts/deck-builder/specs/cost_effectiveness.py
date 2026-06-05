# -*- coding: utf-8 -*-
"""
Cost Effectiveness 101 — ImpactMojo 101 Series (native deck spec)
How to compare interventions on cost per outcome, for South Asian practitioners & funders.
Build: python3 scripts/deck-builder/build.py cost_effectiveness
"""

DECK = {
    "slug": "cost-effectiveness",
    "title": "Cost Effectiveness 101",
    "description": ("Cost Effectiveness 101 — a free foundational course for development "
                    "practitioners and funders in South Asia. Learn to compare interventions "
                    "by cost per outcome: cost-effectiveness, cost-benefit and cost-utility "
                    "analysis, the ICER, DALYs, discounting, league tables, sensitivity "
                    "analysis and the limits of efficiency. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Cost<br>Effectiveness<br>101",
         "sub": "Getting the Most Good per Rupee &mdash; Comparing Interventions on Cost "
                "per Outcome, a Foundational Course for Practitioners &amp; Funders in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "Why Cost-Effectiveness?"},
             {"name": "The Family of Methods"},
             {"name": "Measuring Costs"},
             {"name": "Measuring Effects"},
             {"name": "The Cost-Effectiveness Ratio"},
             {"name": "Cost-Utility &amp; DALYs"},
             {"name": "Time &amp; Discounting"},
             {"name": "Comparing Interventions"},
             {"name": "Uncertainty &amp; Sensitivity"},
             {"name": "Limits &amp; Equity"},
             {"name": "Practice &amp; Tools"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why Cost-Effectiveness?"},

        {"type": "content", "label": "The Core Reality", "title": "Budgets are finite; needs are not",
         "blocks": [
             {"t": "body", "html": "Every development organisation, ministry and funder faces the "
              "same wall: there is never enough money to do everything worth doing. "
              "<strong>Cost-effectiveness</strong> is the discipline of choosing well when you "
              "cannot fund it all &mdash; doing the most good with the resources you have."},
             {"t": "hbox", "color": "cyan", "html": "The question is not 'Does this programme "
              "work?' but 'Does it do <em>more good per rupee</em> than the alternatives we could "
              "fund instead?'"},
         ]},

        {"type": "content", "label": "Opportunity Cost", "title": "Every rupee spent is a rupee not spent elsewhere",
         "blocks": [
             {"t": "term", "word": "Opportunity cost",
              "def": "The value of the best alternative you give up when you choose one option. "
              "The true cost of funding programme A is the good you could have done with programme "
              "B instead."},
             {"t": "body", "html": "A health budget spent on a costly tertiary procedure is a "
              "budget <em>not</em> spent on the immunisations or bed nets it could have bought. "
              "Opportunity cost makes that trade-off visible."},
         ]},

        {"type": "content", "label": "The Most Good", "title": "'The most good per rupee'",
         "blocks": [
             {"t": "body", "html": "Two programmes can both be genuinely good and still differ "
              "enormously in how much good they buy per rupee. Cost-effectiveness analysis "
              "surfaces those differences so scarce funds flow where they help most."},
             {"t": "flow", "steps": [
                 "MONEY: a fixed budget",
                 "CHOICE: many worthy programmes compete",
                 "EVIDENCE: cost per outcome for each",
                 "DECISION: fund the most outcomes per rupee"]},
         ]},

        {"type": "content", "label": "A Worked Intuition", "title": "Same budget, very different impact",
         "blocks": [
             {"t": "body", "html": "Imagine &#8377;10 lakh to spend on reducing child illness. "
              "Programme A averts one case for &#8377;5,000; programme B averts one for &#8377;500. "
              "The same money buys 200 averted cases instead of 20 &mdash; a tenfold difference in "
              "good done."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "200 vs 20", "label": "cases averted for the same &#8377;10 lakh", "color": "green",
                  "source": "Illustrative"},
                 {"num": "10&times;", "label": "more impact from the cheaper-per-outcome option", "color": "cyan"}]},
             {"t": "hbox", "color": "amber", "html": "Illustrative figures &mdash; but the logic is "
              "real: differences between interventions are often this large, not marginal."},
         ]},

        {"type": "content", "label": "Not About Being Cheap", "title": "Cost-effective is not the same as cheap",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Cheapest", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Lowest total cost &mdash; but may deliver "
                   "almost nothing. A programme that does little for very little money is not a bargain."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Cost-effective", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Most outcome per rupee. A more expensive "
                   "programme can be <em>more</em> cost-effective if it delivers far more good."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Cost-effectiveness always holds cost and "
              "outcome together. Neither number means much alone."},
         ]},

        {"type": "content", "label": "Who Uses It", "title": "Where cost-effectiveness shapes decisions",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Health ministries</strong> deciding which treatments a public scheme covers",
                 "<strong>Funders</strong> allocating limited grants across many strong applicants",
                 "<strong>NGOs</strong> choosing between programme designs for the same goal",
                 "<strong>Global bodies</strong> (WHO, World Bank) ranking interventions across diseases"]},
             {"t": "hbox", "color": "indigo", "html": "From a panchayat health post to a national "
              "budget, the underlying question is identical: where does each rupee do the most?"},
         ]},

        {"type": "content", "label": "A Tool, Not a Verdict", "title": "Cost-effectiveness informs; it does not decide",
         "blocks": [
             {"t": "body", "html": "Cost-effectiveness analysis is one input into a decision, not "
              "the whole decision. Equity, rights, feasibility and politics all matter too &mdash; "
              "themes we return to in Section 10."},
             {"t": "quote", "text": "The aim is not to put a price on a life, but to be honest "
              "about the lives a fixed budget can and cannot save.",
              "attr": "&mdash; a working principle of health economics"},
         ]},

        {"type": "content", "label": "South Asia Stakes", "title": "Why this matters acutely in South Asia",
         "blocks": [
             {"t": "body", "html": "Public health spending per person in much of South Asia is among "
              "the lowest in the world relative to need, while disease and deprivation burdens are "
              "high. The gap between resources and need makes every allocation choice consequential."},
             {"t": "hbox", "color": "indigo", "html": "When budgets are tight and needs vast, "
              "choosing well is not an academic nicety &mdash; it is the difference between reaching "
              "many more people or far fewer with the same money."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Family of Methods"},

        {"type": "content", "label": "Three Cousins", "title": "CEA, CBA and CUA: one family, different units",
         "blocks": [
             {"t": "body", "html": "Economic evaluation comes in three main forms. All compare "
              "cost against benefit &mdash; they differ in <strong>how they measure the benefit</strong>, "
              "and that choice shapes what you can compare."},
             {"t": "flow", "steps": [
                 "CEA: benefit in natural units (cases averted)",
                 "CUA: benefit in DALYs / QALYs",
                 "CBA: benefit converted into money"]},
         ]},

        {"type": "content", "label": "Method 1", "title": "Cost-Effectiveness Analysis (CEA)",
         "blocks": [
             {"t": "term", "word": "Cost-Effectiveness Analysis",
              "def": "Compares the cost of interventions per unit of a single natural outcome "
              "&mdash; e.g. cost per case of malaria averted, per child immunised, per additional "
              "year of schooling."},
             {"t": "hbox", "color": "cyan", "html": "Strength: the outcome stays in real, "
              "intuitive units. Limit: you can only compare programmes that share the <em>same</em> "
              "outcome. Cost per case averted cannot be set against cost per child enrolled."},
         ]},

        {"type": "content", "label": "Method 2", "title": "Cost-Utility Analysis (CUA)",
         "blocks": [
             {"t": "term", "word": "Cost-Utility Analysis",
              "def": "A special form of CEA that measures benefit in a common health-and-quality "
              "unit &mdash; the DALY or QALY &mdash; so that very different health programmes can be "
              "compared on one scale."},
             {"t": "body", "html": "Because a DALY captures both length and quality of life, CUA "
              "lets you ask whether a rupee does more against blindness, diarrhoea or heart disease "
              "&mdash; comparisons CEA cannot make. We devote Section 6 to it."},
         ]},

        {"type": "content", "label": "Method 3", "title": "Cost-Benefit Analysis (CBA)",
         "blocks": [
             {"t": "term", "word": "Cost-Benefit Analysis",
              "def": "Converts <em>all</em> benefits into money, so cost and benefit share the "
              "same unit. The result is a net benefit (benefits &minus; costs) or a benefit-cost "
              "ratio."},
             {"t": "hbox", "color": "amber", "html": "Power: you can compare a road, a school and "
              "a clinic on one ledger. Danger: putting a rupee value on health, education or a "
              "life forces uncomfortable &mdash; and contested &mdash; assumptions."},
         ]},

        {"type": "content", "label": "Side by Side", "title": "Which method measures what?",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Method", "Benefit measured in", "Lets you compare"],
              "rows": [
                  ["CEA", "Natural units (cases, children, years)", "Programmes with the same outcome"],
                  ["CUA", "DALYs or QALYs", "Any health programmes, across diseases"],
                  ["CBA", "Money (&#8377;)", "Anything &mdash; health, roads, schools"],
                  ["CMA*", "(costs only; outcomes assumed equal)", "Options with identical effect"]]},
             {"t": "hbox", "color": "indigo", "html": "*Cost-minimisation analysis is the special "
              "case where two options give the <em>same</em> outcome, so you simply pick the cheaper."},
         ]},

        {"type": "content", "label": "Choosing", "title": "Pick the method that fits the question",
         "blocks": [
             {"t": "bullets", "items": [
                 "Comparing designs for <strong>one</strong> outcome? &rarr; CEA",
                 "Comparing across <strong>different</strong> health conditions? &rarr; CUA",
                 "Comparing across <strong>sectors</strong> (health vs infrastructure)? &rarr; CBA",
                 "Outcomes already known to be <strong>identical</strong>? &rarr; cost-minimisation"]},
             {"t": "hbox", "color": "cyan", "html": "The method is not a matter of taste; it follows "
              "from what you need to compare and what you are willing to monetise."},
         ]},

        {"type": "content", "label": "A Shared Logic", "title": "All four share one ratio at heart",
         "blocks": [
             {"t": "body", "html": "Despite the different units, every method asks a version of the "
              "same thing: <strong>how much do we pay for how much good?</strong> The numerator is "
              "always cost; only the denominator &mdash; the outcome &mdash; changes."},
             {"t": "raw", "html": "<div style='text-align:center;font-size:1.6rem;margin:0.5rem 0;'>"
              "value&nbsp;=&nbsp;<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>cost</span>"
              "&nbsp;/&nbsp;<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>outcome</span></div>"},
         ]},

        {"type": "content", "label": "A Caution", "title": "Different methods, different answers",
         "blocks": [
             {"t": "body", "html": "The same programme can look excellent under one method and "
              "mediocre under another, because each weighs outcomes differently. The method is a "
              "lens, and lenses shape what you see."},
             {"t": "hbox", "color": "red", "html": "Always report which method you used, and never "
              "compare a CEA result for one programme against a CBA result for another. Units must match."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Measuring Costs"},

        {"type": "content", "label": "Start Here", "title": "Costs are harder to measure than they look",
         "blocks": [
             {"t": "body", "html": "The 'cost' of a programme is rarely the figure on the grant "
              "agreement. Real cost includes staff time, volunteers, donated goods, shared "
              "overheads and the time of the people you serve. Miss these and you flatter the "
              "programme."},
             {"t": "hbox", "color": "cyan", "html": "A good cost estimate is a careful inventory, "
              "not a glance at the budget line."},
         ]},

        {"type": "content", "label": "The Method", "title": "The ingredients (or inventory) method",
         "blocks": [
             {"t": "term", "word": "Ingredients method",
              "def": "Cost estimation that lists every resource an intervention uses &mdash; the "
              "'ingredients' &mdash; values each at its real price, and adds them up. Also called "
              "the inventory method."},
             {"t": "flow", "steps": [
                 "LIST every resource used (the ingredients)",
                 "QUANTIFY how much of each",
                 "PRICE each at its true value",
                 "SUM to a total programme cost"]},
         ]},

        {"type": "content", "label": "Direct vs Indirect", "title": "Direct and indirect costs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Direct costs", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Tied straight to delivery: medicines, field "
                   "staff salaries, training materials, transport to villages."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Indirect costs", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Shared support that enables delivery: head-office "
                   "rent, accounts, IT, management. Must be apportioned, not ignored."}]}]},
             {"t": "hbox", "color": "red", "html": "Leaving out indirect costs is the most common way "
              "a programme is made to look cheaper than it really is."},
         ]},

        {"type": "content", "label": "Fixed vs Variable", "title": "Fixed and variable costs",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Fixed costs</strong> do not change with scale &mdash; a training centre, a "
                 "vehicle, the management team",
                 "<strong>Variable costs</strong> rise with each unit served &mdash; vaccines, "
                 "stipends, per-child materials",
                 "Together they shape how cost-per-outcome changes as a programme grows"]},
             {"t": "hbox", "color": "amber", "html": "This is why pilots look expensive: fixed costs "
              "are spread over few beneficiaries. Cost per outcome usually falls as you scale &mdash; "
              "up to a point."},
         ]},

        {"type": "content", "label": "Economies of Scale", "title": "Why cost per outcome falls with scale",
         "blocks": [
             {"t": "chart", "canvas": "scaleChart",
              "title": "Cost per beneficiary as a programme scales (illustrative)",
              "source": "Illustrative",
              "type": "line",
              "data": {"labels": ["100", "500", "1k", "2.5k", "5k", "10k", "20k"],
                       "datasets": [{"label": "Cost per beneficiary (&#8377;)",
                                     "data": [1800, 620, 410, 290, 240, 215, 205],
                                     "borderColor": "#0EA5E9", "backgroundColor": "rgba(14,165,233,0.08)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'\\u20B9 per beneficiary'} }, x:{ title:{display:true,text:'Number reached'} } } }"}},
             {"t": "hbox", "color": "green", "html": "Fixed costs spread over more people, so the "
              "curve falls steeply then flattens. Illustrative numbers, but a near-universal shape."},
         ]},

        {"type": "content", "label": "Whose Costs?", "title": "The perspective decides what counts",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Perspective", "Counts costs to&hellip;", "Often misses"],
              "rows": [
                  ["Provider", "The implementing organisation", "Costs borne by participants"],
                  ["Participant", "The beneficiary &mdash; travel, time, fees", "Provider overheads"],
                  ["Societal", "Everyone affected &mdash; the fullest view", "Hardest to measure fully"]]},
             {"t": "hbox", "color": "indigo", "html": "State the perspective up front. A programme "
              "that is cheap for the provider may be costly for a poor participant who loses a day's "
              "wage to attend."},
         ]},

        {"type": "content", "label": "Hidden to the Poor", "title": "Participant costs are real costs",
         "blocks": [
             {"t": "body", "html": "For a daily-wage worker, attending a 'free' health camp can mean "
              "lost income, bus fare and childcare. From a <strong>societal perspective</strong> those "
              "are genuine programme costs &mdash; and a reason people drop out."},
             {"t": "hbox", "color": "amber", "html": "Designs that lower participant costs &mdash; "
              "doorstep delivery, evening timings, compensation &mdash; can improve cost-effectiveness "
              "by lifting uptake, not just by spending less."},
         ]},

        {"type": "content", "label": "Where the Money Goes", "title": "A typical programme cost breakdown",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [{"t": "chart", "canvas": "costBreakdownChart",
                        "title": "Illustrative share of total cost by ingredient",
                        "source": "Illustrative",
                        "type": "doughnut",
                        "data": {"labels": ["Field staff", "Supplies / commodities", "Training",
                                            "Overheads / management", "Transport", "Participant time"],
                                 "datasets": [{"data": [38, 22, 9, 16, 8, 7],
                                               "backgroundColor": ["#0EA5E9", "#10B981", "#22C55E",
                                                                   "#6366F1", "#F59E0B", "#EF4444"]}]},
                        "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}}],
              "right": [
                  {"t": "body", "cls": "sm", "html": "Notice overheads and participant time together "
                   "are nearly a quarter of cost &mdash; the very items most often left out."},
                  {"t": "hbox", "color": "red", "html": "Drop those slices and the programme looks ~23% "
                   "cheaper than it really is. Illustrative shares."}]},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Measuring Effects"},

        {"type": "content", "label": "The Denominator", "title": "Effects: the 'good' you are buying",
         "blocks": [
             {"t": "body", "html": "If cost is the numerator, the <strong>effect</strong> is the "
              "denominator &mdash; the outcome the programme produces. Getting it right matters as "
              "much as costing, and is often harder."},
             {"t": "hbox", "color": "cyan", "html": "In CEA the effect stays in its natural unit: a "
              "case averted, a child immunised, a TB patient cured, a year of schooling added."},
         ]},

        {"type": "content", "label": "Natural Units", "title": "Outcomes in their own real units",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Health:</strong> cases averted, deaths prevented, patients cured",
                 "<strong>Education:</strong> additional years of schooling, test-score gains",
                 "<strong>Nutrition:</strong> children moved out of stunting",
                 "<strong>WASH:</strong> people with sustained access to safe water"]},
             {"t": "hbox", "color": "indigo", "html": "Natural units are intuitive and trusted by "
              "practitioners &mdash; but they only allow comparison <em>within</em> the same outcome."},
         ]},

        {"type": "content", "label": "A Chain", "title": "Intermediate vs final outcomes",
         "blocks": [
             {"t": "term", "word": "Intermediate outcome",
              "def": "A step on the causal path &mdash; bed nets distributed, children dewormed, "
              "people trained. Easy to measure, but not yet the thing you ultimately care about."},
             {"t": "term", "word": "Final outcome",
              "def": "The end goal &mdash; malaria cases averted, lives saved, income raised. "
              "Harder to measure, but it is what actually matters."},
         ]},

        {"type": "content", "label": "The Results Chain", "title": "From inputs to impact",
         "blocks": [
             {"t": "flow", "steps": [
                 "INPUTS: money, staff, nets",
                 "OUTPUTS: nets distributed",
                 "OUTCOMES: nets used nightly",
                 "IMPACT: malaria cases averted"]},
             {"t": "hbox", "color": "amber", "html": "Costing per <em>output</em> (nets distributed) "
              "is cheap to measure but can mislead &mdash; a net unused averts nothing. Push toward "
              "outcomes and impact where you can."},
         ]},

        {"type": "content", "label": "Attribution", "title": "Did the programme really cause the effect?",
         "blocks": [
             {"t": "body", "html": "Cost-effectiveness needs the effect <em>caused by</em> the "
              "programme &mdash; not the total change, some of which would have happened anyway. "
              "That requires a credible counterfactual: what would have occurred without it."},
             {"t": "hbox", "color": "red", "html": "Crediting a programme with outcomes it did not "
              "cause overstates its cost-effectiveness. This is why rigorous evaluation (RCTs, "
              "quasi-experiments) underpins the best cost-effectiveness estimates."},
         ]},

        {"type": "content", "label": "Cost per Outcome", "title": "Putting cost and effect together",
         "blocks": [
             {"t": "body", "html": "Divide total cost by total effect and you have the headline "
              "number: <strong>cost per outcome</strong>. &#8377;6 lakh spent to avert 300 cases is "
              "&#8377;2,000 per case averted."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "&#8377;6,00,000", "label": "total programme cost", "color": "cyan",
                  "source": "Illustrative"},
                 {"num": "&#8377;2,000", "label": "per case averted (cost &divide; 300 cases)", "color": "green"}]},
         ]},

        {"type": "content", "label": "Measuring Effect", "title": "Where effect estimates come from",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Source", "Strength", "Caution"],
              "rows": [
                  ["RCT / trial", "Strong causal estimate", "May not transfer to your context"],
                  ["Quasi-experiment", "Real-world, plausible counterfactual", "Assumptions can fail"],
                  ["Programme monitoring", "Cheap, available", "No counterfactual"],
                  ["Published meta-analysis", "Pools many studies", "Settings differ from yours"]]},
             {"t": "hbox", "color": "indigo", "html": "An effect estimate is only as good as the "
              "evidence behind it. Borrowed effect sizes need a sanity check against your reality."},
         ]},

        {"type": "content", "label": "A Warning", "title": "Cheap outputs can buy nothing",
         "blocks": [
             {"t": "quote", "text": "It is easy to be cost-effective at producing outputs nobody "
              "uses. The discipline is to cost what changes lives, not what is easy to count.",
              "attr": "&mdash; a programme-evaluation maxim"},
             {"t": "hbox", "color": "amber", "html": "Always ask whether your denominator is a real "
              "outcome or a convenient proxy. The choice can swing the ratio by an order of magnitude."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "The Cost-Effectiveness Ratio"},

        {"type": "content", "label": "The Headline Number", "title": "The cost-effectiveness ratio",
         "blocks": [
             {"t": "term", "word": "Cost-effectiveness ratio (CER)",
              "def": "Total cost divided by total effect &mdash; the average cost of one unit of "
              "outcome. Lower is better: less money for the same good."},
             {"t": "raw", "html": "<div style='text-align:center;font-size:1.5rem;margin:0.5rem 0;'>"
              "CER&nbsp;=&nbsp;<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>total cost</span>"
              "&nbsp;/&nbsp;<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>total effect</span></div>"},
         ]},

        {"type": "content", "label": "Average CER", "title": "The average ratio compares to doing nothing",
         "blocks": [
             {"t": "body", "html": "The <strong>average CER</strong> compares a programme against a "
              "baseline of doing nothing. It answers: across everyone reached, what did each unit of "
              "outcome cost on average?"},
             {"t": "hbox", "color": "cyan", "html": "Useful for a first sense of a programme &mdash; "
              "but real decisions usually compare options against <em>each other</em>, not against "
              "nothing. That needs the incremental ratio."},
         ]},

        {"type": "content", "label": "The Key Concept", "title": "The Incremental Cost-Effectiveness Ratio (ICER)",
         "blocks": [
             {"t": "term", "word": "ICER",
              "def": "The extra cost of switching from option B to option A, divided by the extra "
              "effect gained. It measures the cost-effectiveness of the <em>upgrade</em>, not the "
              "whole programme."},
             {"t": "raw", "html": "<div style='text-align:center;font-size:1.4rem;margin:0.5rem 0;'>"
              "ICER&nbsp;=&nbsp;<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>cost<sub>A</sub> &minus; cost<sub>B</sub></span>"
              "&nbsp;/&nbsp;<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>effect<sub>A</sub> &minus; effect<sub>B</sub></span></div>"},
             {"t": "hbox", "color": "red", "html": "The ICER is <strong>incremental</strong>, not "
              "average. It is the single most important &mdash; and most misread &mdash; number in "
              "the field."},
         ]},

        {"type": "content", "label": "Why Incremental", "title": "Why the increment, not the average, matters",
         "blocks": [
             {"t": "body", "html": "You are rarely choosing between a programme and nothing. You are "
              "choosing whether the <em>extra</em> spend on a better option is worth the <em>extra</em> "
              "good it buys. The ICER isolates exactly that trade-off."},
             {"t": "hbox", "color": "amber", "html": "A new treatment may be excellent on average yet "
              "a poor upgrade &mdash; if it costs far more than the current one for only a little extra "
              "benefit. The ICER catches what the average hides."},
         ]},

        {"type": "content", "label": "A Worked ICER", "title": "Comparing two TB-screening strategies",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Strategy", "Cost", "Cases detected"],
              "rows": [
                  ["B: standard screening", "&#8377;5,00,000", "200"],
                  ["A: enhanced screening", "&#8377;8,00,000", "260"],
                  ["Difference (A &minus; B)", "&#8377;3,00,000", "60 extra"]]},
             {"t": "hbox", "color": "green", "html": "ICER = &#8377;3,00,000 &divide; 60 = "
              "<strong>&#8377;5,000 per extra case detected</strong>. The question for the funder: is "
              "an extra case worth &#8377;5,000? Illustrative figures."},
         ]},

        {"type": "content", "label": "Reading the ICER", "title": "Is the ICER 'worth it'?",
         "blocks": [
             {"t": "body", "html": "An ICER only means something against a <strong>threshold</strong> "
              "&mdash; the most you are willing to pay for one unit of outcome. Below the threshold, "
              "the upgrade is judged worthwhile; above it, not."},
             {"t": "hbox", "color": "indigo", "html": "Thresholds are themselves value judgements, "
              "often tied to a country's income. We return to this in Sections 6 and 10 &mdash; there "
              "is no neutral 'correct' threshold."},
         ]},

        {"type": "content", "label": "Dominance", "title": "When the choice is obvious",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Dominant", "blocks": [
                  {"t": "body", "cls": "sm", "html": "An option that costs <em>less</em> and does "
                   "<em>more</em> dominates &mdash; always choose it. No ICER needed."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Dominated", "blocks": [
                  {"t": "body", "cls": "sm", "html": "An option that costs <em>more</em> and does "
                   "<em>less</em> is dominated &mdash; drop it from the comparison entirely."}]}]},
             {"t": "hbox", "color": "cyan", "html": "ICERs only matter for the hard middle cases: more "
              "cost <em>and</em> more effect, where you must weigh the trade-off."},
         ]},

        {"type": "content", "label": "A Common Slip", "title": "Don't confuse average with incremental",
         "blocks": [
             {"t": "body", "html": "Reporting a programme's average cost per outcome when the decision "
              "is about an upgrade is a frequent and serious error. It can make a poor-value addition "
              "look like a bargain."},
             {"t": "hbox", "color": "red", "html": "Rule: if you are comparing two options, you need "
              "the <strong>ICER</strong> between them &mdash; the difference in cost over the "
              "difference in effect. Never the two averages."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Cost-Utility &amp; DALYs"},

        {"type": "content", "label": "The Problem", "title": "How do you compare blindness with diarrhoea?",
         "blocks": [
             {"t": "body", "html": "CEA cannot compare a programme that prevents blindness with one "
              "that prevents child deaths &mdash; the outcomes are in different units. To choose "
              "across <em>all</em> of health, you need a common currency of health itself."},
             {"t": "hbox", "color": "cyan", "html": "That common currency combines two things people "
              "care about: <strong>how long</strong> you live and <strong>how well</strong> you live. "
              "Enter the DALY and the QALY."},
         ]},

        {"type": "content", "label": "Two Measures", "title": "QALYs and DALYs: length &times; quality of life",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "QALY", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Quality-Adjusted Life Year &mdash; a year of "
                   "<em>healthy</em> life. Higher is better; programmes aim to <em>gain</em> QALYs."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "DALY", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Disability-Adjusted Life Year &mdash; a year of "
                   "<em>healthy life lost</em>. Higher is worse; programmes aim to <em>avert</em> DALYs."}]}]},
             {"t": "hbox", "color": "indigo", "html": "QALYs count health <em>gained</em>; DALYs count "
              "health <em>lost</em>. They are mirror images &mdash; do not mix them in one calculation."},
         ]},

        {"type": "content", "label": "The DALY", "title": "What a DALY actually is",
         "blocks": [
             {"t": "term", "word": "DALY",
              "def": "Disability-Adjusted Life Year = Years of Life Lost to early death (YLL) + Years "
              "Lived with Disability (YLD). One DALY is one lost year of full health."},
             {"t": "raw", "html": "<div style='text-align:center;font-size:1.4rem;margin:0.5rem 0;'>"
              "DALY&nbsp;=&nbsp;YLL&nbsp;<span style='color:#94a3b8;'>(years of life lost)</span>"
              "&nbsp;+&nbsp;YLD&nbsp;<span style='color:#94a3b8;'>(years lived with disability)</span></div>"},
             {"t": "hbox", "color": "red", "html": "Because a DALY is a <em>loss</em>, lower is "
              "better and interventions seek to <strong>avert</strong> DALYs &mdash; not accumulate them."},
         ]},

        {"type": "content", "label": "The Two Halves", "title": "Dying early, and living unwell",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "YLL", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Years of Life Lost: a death at 30 against a life "
                   "expectancy of 70 loses 40 years. Captures the burden of dying early."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "YLD", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Years Lived with Disability: years spent in "
                   "ill-health, each weighted by how disabling the condition is. Captures suffering, "
                   "not just death."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Together they let a single number reflect both a "
              "fatal disease and a chronic, disabling but non-fatal one."},
         ]},

        {"type": "content", "label": "Disability Weights", "title": "Not all years of illness weigh the same",
         "blocks": [
             {"t": "body", "html": "Each condition carries a <strong>disability weight</strong> from 0 "
              "(full health) to 1 (equivalent to death). A year with a mild condition counts as a small "
              "fraction of a DALY; a year with a severe one counts as much more."},
             {"t": "hbox", "color": "amber", "html": "These weights come from surveys of how people "
              "value health states &mdash; they are useful, standardised, and genuinely contested. "
              "Whose values, and whose lives, the weights reflect is a real ethical question."},
         ]},

        {"type": "content", "label": "The CUA Ratio", "title": "Cost per DALY averted",
         "blocks": [
             {"t": "body", "html": "Cost-utility analysis divides cost by DALYs averted: "
              "<strong>cost per DALY averted</strong>. Lower means more health bought per rupee, and "
              "it works across completely different diseases."},
             {"t": "raw", "html": "<div style='text-align:center;font-size:1.45rem;margin:0.5rem 0;'>"
              "<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>cost</span>&nbsp;/&nbsp;"
              "<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>DALYs averted</span>"
              "&nbsp;=&nbsp;cost per DALY averted</div>"},
         ]},

        {"type": "content", "label": "Orders of Magnitude", "title": "Some interventions avert DALYs very cheaply",
         "blocks": [
             {"t": "chart", "canvas": "dalyLeagueChart",
              "title": "Cost per DALY averted &mdash; illustrative ranking (lower = better)",
              "source": "Illustrative; relative ordering only, not exact figures",
              "type": "bar",
              "data": {"labels": ["Insecticidal nets", "Childhood vaccines", "ORS for diarrhoea",
                                  "TB treatment", "Hypertension care", "Some tertiary surgery"],
                       "datasets": [{"label": "Relative cost per DALY averted",
                                     "data": [1, 1.5, 2, 4, 9, 40],
                                     "backgroundColor": ["#10B981", "#10B981", "#22C55E", "#F59E0B", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'relative cost per DALY (illustrative scale)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Bars show <em>relative</em> ordering only. Bed "
              "nets and basic vaccines are <strong>commonly cited</strong> as among the most "
              "cost-effective health buys &mdash; but treat any precise '&#36; per DALY' figure with care."},
         ]},

        {"type": "content", "label": "Thresholds", "title": "When is a cost per DALY 'good value'?",
         "blocks": [
             {"t": "body", "html": "A widely used rule of thumb judged an intervention cost-effective "
              "if its cost per DALY averted was below one to three times a country's GDP per capita. "
              "It is convenient &mdash; and increasingly criticised as arbitrary."},
             {"t": "hbox", "color": "red", "html": "WHO has moved away from blanket GDP-based "
              "thresholds toward context-specific judgement. A threshold is a value choice dressed as "
              "a number &mdash; treat it as one input, never a verdict."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Time &amp; Discounting"},

        {"type": "content", "label": "Money Has Timing", "title": "A rupee today is worth more than a rupee next year",
         "blocks": [
             {"t": "body", "html": "Costs and benefits arrive at different times. A rupee in hand "
              "today can be invested, can meet an urgent need, and is certain &mdash; so we value it "
              "more than the same rupee a decade away. <strong>Discounting</strong> makes future and "
              "present values comparable."},
             {"t": "hbox", "color": "cyan", "html": "This is not about inflation. Even with stable "
              "prices, sooner is worth more than later."},
         ]},

        {"type": "content", "label": "Why Discount", "title": "Time preference and opportunity cost",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Time preference:</strong> people generally prefer benefits now to benefits later",
                 "<strong>Opportunity cost of capital:</strong> money tied up could have earned a return",
                 "<strong>Uncertainty:</strong> the further ahead, the less sure the benefit will arrive"]},
             {"t": "hbox", "color": "indigo", "html": "Discounting is how we honour all three &mdash; "
              "putting flows that occur at different times on one comparable footing."},
         ]},

        {"type": "content", "label": "Present Value", "title": "Bringing the future into today's terms",
         "blocks": [
             {"t": "term", "word": "Present value (PV)",
              "def": "What a future cost or benefit is worth today, after discounting. A benefit of X "
              "in year t is worth X &divide; (1 + r)^t now, where r is the discount rate."},
             {"t": "raw", "html": "<div style='text-align:center;font-size:1.4rem;margin:0.5rem 0;'>"
              "PV&nbsp;=&nbsp;<span style='border-bottom:2px solid #475569;padding:0 .4rem;'>future value</span>"
              "&nbsp;/&nbsp;(1&nbsp;+&nbsp;r)<sup>t</sup></div>"},
         ]},

        {"type": "content", "label": "See the Decay", "title": "How a discount rate erodes future value",
         "blocks": [
             {"t": "chart", "canvas": "discountChart",
              "title": "Present value of &#8377;1,000 received in year t (at 3% and 8%)",
              "source": "Illustrative, standard discounting",
              "type": "line",
              "data": {"labels": ["0", "5", "10", "15", "20", "25", "30"],
                       "datasets": [
                           {"label": "Discount rate 3%",
                            "data": [1000, 863, 744, 642, 554, 478, 412],
                            "borderColor": "#10B981", "tension": 0.3, "pointRadius": 3, "fill": False},
                           {"label": "Discount rate 8%",
                            "data": [1000, 681, 463, 315, 215, 146, 99],
                            "borderColor": "#EF4444", "tension": 0.3, "pointRadius": 3, "fill": False}]},
              "options": {"__js__": "{ scales:{ y:{ title:{display:true,text:'present value (\\u20B9)'} }, x:{ title:{display:true,text:'years from now'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "At 8%, &#8377;1,000 in 30 years is worth under "
              "&#8377;100 today. The rate you pick dramatically changes how much the future counts."},
         ]},

        {"type": "content", "label": "The Rate", "title": "Choosing the discount rate",
         "blocks": [
             {"t": "body", "html": "Common rates in health and development run around 3% per year, "
              "though some analyses use higher. The choice is consequential and partly ethical: a high "
              "rate makes long-term benefits almost vanish."},
             {"t": "hbox", "color": "red", "html": "This matters acutely for the climate, for "
              "children, and for prevention &mdash; programmes whose payoffs land decades away look far "
              "worse under a high discount rate. The rate encodes how much we value the future."},
         ]},

        {"type": "content", "label": "Discount Effects Too?", "title": "Should we discount health, not just money?",
         "blocks": [
             {"t": "body", "html": "Convention often discounts <em>both</em> costs and health effects "
              "(DALYs, QALYs) &mdash; otherwise a calculation could justify delaying every benefit "
              "forever. But discounting future lives is philosophically uncomfortable."},
             {"t": "hbox", "color": "indigo", "html": "Whatever you choose, be explicit and "
              "consistent, and test how sensitive your result is to the rate &mdash; which is exactly "
              "what Section 9 is about."},
         ]},

        {"type": "content", "label": "Time Horizon", "title": "How far ahead do you count?",
         "blocks": [
             {"t": "body", "html": "Alongside the rate, you must choose a <strong>time horizon</strong> "
              "&mdash; how many years of costs and benefits to include. A prevention programme whose "
              "payoffs land over a lifetime looks worthless on a three-year horizon."},
             {"t": "hbox", "color": "amber", "html": "Cut the horizon too short and you systematically "
              "undervalue prevention and anything slow-burning. State the horizon, and match it to when "
              "the real effects actually occur."},
         ]},

        {"type": "content", "label": "A Caution", "title": "Discounting is an assumption, not a fact",
         "blocks": [
             {"t": "quote", "text": "The discount rate is the most powerful, least visible "
              "assumption in any long-horizon analysis &mdash; small changes swing the conclusion.",
              "attr": "&mdash; a maxim of cost-benefit practice"},
             {"t": "hbox", "color": "amber", "html": "Always report your discount rate, justify it, "
              "and show the result at alternative rates. Hiding it is a red flag in any analysis you read."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Comparing Interventions"},

        {"type": "content", "label": "The Pay-Off", "title": "Why we did all this: to compare",
         "blocks": [
             {"t": "body", "html": "The whole point of standardising costs and effects is to lay "
              "interventions side by side and ask where each rupee does most good. Done honestly, the "
              "comparison can redirect funding to far higher impact."},
             {"t": "hbox", "color": "cyan", "html": "But comparison is only as trustworthy as the "
              "consistency behind it &mdash; same method, same units, same perspective, same discount "
              "rate. Compare like with like, or not at all."},
         ]},

        {"type": "content", "label": "League Tables", "title": "Ranking interventions by cost per outcome",
         "blocks": [
             {"t": "term", "word": "League table",
              "def": "A ranked list of interventions by their cost-effectiveness ratio &mdash; "
              "cheapest per unit of outcome at the top &mdash; used to guide where to spend next."},
             {"t": "hbox", "color": "amber", "html": "League tables are powerful and seductive. Their "
              "honesty depends entirely on whether the entries were estimated the same way. A table "
              "mixing methods is worse than no table."},
         ]},

        {"type": "content", "label": "$ per Outcome", "title": "GiveWell-style 'cost per outcome' comparison",
         "blocks": [
             {"t": "chart", "canvas": "perOutcomeChart",
              "title": "Illustrative cost per equivalent outcome across programmes",
              "source": "Illustrative; relative comparison only",
              "type": "bar",
              "data": {"labels": ["Programme A", "Programme B", "Programme C", "Programme D", "Programme E"],
                       "datasets": [{"label": "Cost per outcome (&#8377;, illustrative)",
                                     "data": [400, 950, 1800, 3200, 7500],
                                     "backgroundColor": ["#10B981", "#22C55E", "#F59E0B", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'\\u20B9 per outcome (illustrative)'} } } }"}},
             {"t": "hbox", "color": "indigo", "html": "Funders like GiveWell rank charities by cost "
              "per comparable outcome and direct money to the top. The same logic scales from a global "
              "fund to a single grant committee. Figures here are illustrative."},
         ]},

        {"type": "content", "label": "Reallocation", "title": "Moving money up the league table",
         "blocks": [
             {"t": "body", "html": "If programme A averts an outcome for &#8377;400 and programme E "
              "for &#8377;7,500, shifting funds from E toward A &mdash; where appropriate and feasible "
              "&mdash; can multiply total impact for the same budget."},
             {"t": "hbox", "color": "amber", "html": "But 'shift the money' is rarely so simple: "
              "programmes serve different people, places and needs. Cost-effectiveness tells you where "
              "to <em>look</em> harder, not always where to cut."},
         ]},

        {"type": "content", "label": "A Cautionary Tale", "title": "The deworming debate",
         "blocks": [
             {"t": "body", "html": "Mass school deworming became a famous 'best buy' &mdash; cheap "
              "pills, and one influential study linked treatment to better schooling and later "
              "earnings. It topped cost-effectiveness league tables for years."},
             {"t": "hbox", "color": "red", "html": "Then re-analyses and replications questioned the "
              "size and durability of those long-run effects. The pills are cheap and safe; the "
              "<em>magnitude</em> of the benefit &mdash; the denominator &mdash; turned out far more "
              "uncertain than the rankings implied."},
         ]},

        {"type": "content", "label": "The Lesson", "title": "What deworming teaches about league tables",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "A ranking is only as solid as the effect estimate beneath it",
                 "A single influential study can move millions &mdash; and may not replicate",
                 "Cheap cost (numerator) cannot rescue an uncertain effect (denominator)",
                 "Precise-looking ratios can hide enormous uncertainty"]},
             {"t": "hbox", "color": "amber", "html": "The deworming story is not 'CEA is useless' "
              "&mdash; it is 'never read a league-table rank without its uncertainty'. Which is "
              "Section 9."},
         ]},

        {"type": "content", "label": "Transferability", "title": "A ratio from elsewhere may not hold here",
         "blocks": [
             {"t": "body", "html": "Costs, wages, disease burden and delivery systems differ across "
              "districts and countries. A cost-effectiveness ratio estimated in Kenya or Bihar will "
              "not automatically hold in Odisha or Sindh."},
             {"t": "hbox", "color": "indigo", "html": "Before borrowing a ratio, ask what would change "
              "in your context: input prices, baseline burden, uptake, capacity. Adapt, don't copy."},
         ]},

        {"type": "content", "label": "Diminishing Returns", "title": "The best buy changes as you scale",
         "blocks": [
             {"t": "body", "html": "A top-ranked intervention does not stay top-ranked forever. As you "
              "fund the easiest-to-reach first, the cost of reaching each additional person tends to "
              "rise &mdash; so even the best buy eventually becomes less cost-effective at the margin."},
             {"t": "hbox", "color": "amber", "html": "This is why portfolios beat single 'winners': "
              "the right answer is usually to fund the best buy <em>up to a point</em>, then move down "
              "the table &mdash; not to pour everything into one line."},
         ]},

        {"type": "content", "label": "Good Practice", "title": "Comparing interventions honestly",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Use the same method, units, perspective and discount rate for every entry",
                 "Show the uncertainty around each ratio, not just the point estimate",
                 "State the context each estimate came from",
                 "Pair the ranking with equity and feasibility, never efficiency alone"]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Uncertainty &amp; Sensitivity"},

        {"type": "content", "label": "The Honest Truth", "title": "Every ratio is an estimate, not a fact",
         "blocks": [
             {"t": "body", "html": "A cost-effectiveness ratio is built from uncertain inputs &mdash; "
              "uncertain costs, uncertain effects, an assumed discount rate. The single number that "
              "results looks precise but is not. <strong>Sensitivity analysis</strong> asks how much "
              "it could move."},
             {"t": "hbox", "color": "red", "html": "A point estimate with no uncertainty attached is "
              "not a finding &mdash; it is an illusion of precision. Demand the range."},
         ]},

        {"type": "content", "label": "One-Way", "title": "One-way sensitivity analysis",
         "blocks": [
             {"t": "term", "word": "One-way sensitivity analysis",
              "def": "Vary one input at a time across a plausible range, holding the rest fixed, and "
              "watch how the result moves. It reveals which assumptions the answer hinges on."},
             {"t": "hbox", "color": "cyan", "html": "If halving the assumed effect doubles the cost "
              "per outcome and flips your decision, you have found the input that deserves the most "
              "scrutiny &mdash; and better data."},
         ]},

        {"type": "content", "label": "The Tornado", "title": "Tornado diagram: what moves the answer most",
         "blocks": [
             {"t": "chart", "canvas": "tornadoChart",
              "title": "One-way sensitivity: swing in cost per outcome by input (illustrative)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["Effect size", "Discount rate", "Staff cost", "Uptake rate", "Overheads"],
                       "datasets": [{"label": "Range of cost per outcome (&#8377;)",
                                     "data": [2600, 1500, 900, 700, 350],
                                     "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'width of swing in \\u20B9 per outcome'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Sorted widest-to-narrowest, the bars form a "
              "'tornado'. Here the <strong>effect size</strong> dominates &mdash; so that is where to "
              "invest in better evidence. Illustrative."},
         ]},

        {"type": "content", "label": "Probabilistic", "title": "Probabilistic sensitivity analysis (PSA)",
         "blocks": [
             {"t": "term", "word": "Probabilistic sensitivity analysis",
              "def": "Assign each uncertain input a probability distribution, then simulate the model "
              "thousands of times to produce a <em>distribution</em> of cost-effectiveness results, "
              "not a single number."},
             {"t": "hbox", "color": "indigo", "html": "PSA answers the question decision-makers really "
              "have: not 'what is the ratio?' but 'how likely is this option to be the best buy, given "
              "everything we don't know?'"},
         ]},

        {"type": "content", "label": "The CE Plane", "title": "The cost-effectiveness plane",
         "blocks": [
             {"t": "body", "html": "Plot extra cost (vertical) against extra effect (horizontal) "
              "relative to the comparator. The origin is the comparator; an option's position decides "
              "whether it is an easy yes, an easy no, or a trade-off."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Lower-right", "blocks": [
                  {"t": "body", "cls": "sm", "html": "More effect, less cost &mdash; <strong>dominant</strong>. "
                   "Adopt it."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Upper-left", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Less effect, more cost &mdash; <strong>dominated</strong>. "
                   "Reject it."}]}]},
         ]},

        {"type": "content", "label": "See the Plane", "title": "An ICER on the cost-effectiveness plane",
         "blocks": [
             {"t": "chart", "canvas": "cePlaneChart",
              "title": "Simulated results vs a comparator (origin = comparator)",
              "source": "Illustrative PSA cloud",
              "type": "scatter",
              "data": {"datasets": [
                  {"label": "Simulations",
                   "data": [{"x": 30, "y": 90000}, {"x": 45, "y": 140000}, {"x": 55, "y": 120000},
                            {"x": 60, "y": 180000}, {"x": 70, "y": 160000}, {"x": 75, "y": 220000},
                            {"x": 50, "y": 70000}, {"x": 40, "y": 110000}, {"x": 65, "y": 130000},
                            {"x": 35, "y": 60000}, {"x": 80, "y": 200000}, {"x": 58, "y": 150000},
                            {"x": 48, "y": 95000}, {"x": 72, "y": 175000}, {"x": 62, "y": 145000}],
                   "backgroundColor": "rgba(99,102,241,0.6)", "pointRadius": 5}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'extra effect (outcomes gained)'}, min:0 }, y:{ title:{display:true,text:'extra cost (\\u20B9)'}, min:0 } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The scatter (one dot per simulation) shows how "
              "wide the uncertainty is. A line from the origin is the willingness-to-pay threshold: "
              "dots below it are 'worth it'. Illustrative."},
         ]},

        {"type": "content", "label": "The Takeaway", "title": "Why point estimates mislead",
         "blocks": [
             {"t": "body", "html": "Two interventions can have the same headline ratio while one is a "
              "near-certain good buy and the other a coin-toss. The point estimate alone cannot tell "
              "them apart; the spread can."},
             {"t": "hbox", "color": "red", "html": "Treat any single '&#8377;X per outcome' as the "
              "<em>centre</em> of a range, never the truth. The width of that range is often the most "
              "decision-relevant fact in the whole analysis."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Limits &amp; Equity"},

        {"type": "content", "label": "Not the Whole Story", "title": "Efficiency is one value among several",
         "blocks": [
             {"t": "body", "html": "Cost-effectiveness measures efficiency &mdash; outcomes per "
              "rupee. But societies also care about fairness, rights, dignity and reaching the worst-off. "
              "A perfectly efficient choice can be deeply unjust."},
             {"t": "quote", "text": "Not everything that counts can be counted, and not everything "
              "that can be counted counts.",
              "attr": "&mdash; commonly attributed to William Bruce Cameron"},
         ]},

        {"type": "content", "label": "What CEA Ignores", "title": "The blind spots of cost per outcome",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Distribution:</strong> a total of outcomes hides <em>who</em> gets them",
                 "<strong>Rights &amp; dignity:</strong> some things are owed regardless of efficiency",
                 "<strong>Process:</strong> how people are treated, not just the result",
                 "<strong>The hard-to-reach:</strong> serving them is costlier &mdash; and easily deprioritised"]},
         ]},

        {"type": "content", "label": "The Equity Trap", "title": "Cheapest-to-reach is not the same as fairest",
         "blocks": [
             {"t": "body", "html": "Reaching a remote Adivasi hamlet or a person with disability often "
              "costs far more per outcome than reaching an accessible town. Pure cost-effectiveness "
              "quietly pushes resources <em>away</em> from exactly those who need them most."},
             {"t": "hbox", "color": "amber", "html": "Left unchecked, 'value for money' can entrench "
              "the very inequities development is meant to undo. This is the central ethical tension of "
              "the whole field."},
         ]},

        {"type": "content", "label": "Equity Weighting", "title": "Building fairness into the numbers",
         "blocks": [
             {"t": "body", "html": "One response is <strong>equity weighting</strong>: counting an "
              "outcome for a worse-off person as worth more than the same outcome for someone "
              "advantaged, so the analysis rewards reaching the marginalised."},
             {"t": "hbox", "color": "indigo", "html": "It makes the value judgement explicit rather "
              "than pretending efficiency is neutral &mdash; but choosing the weights is itself a "
              "political and ethical act, not a technical one."},
         ]},

        {"type": "content", "label": "Whose Values?", "title": "Numbers carry hidden value judgements",
         "blocks": [
             {"t": "bullets", "items": [
                 "Disability weights embed whose view of a 'good life'",
                 "Discount rates embed how much we value future generations",
                 "Thresholds embed what a life or a healthy year is 'worth'",
                 "The choice of outcome embeds what we decided to count at all"]},
             {"t": "hbox", "color": "red", "html": "Every one of these is a values choice wearing the "
              "costume of arithmetic. Data-literate practice means reading the choices, not just the digits."},
         ]},

        {"type": "content", "label": "The Counted &amp; the Counted-Out", "title": "What gets measured gets funded",
         "blocks": [
             {"t": "body", "html": "Cost-effectiveness can only weigh outcomes that someone chose to "
              "measure. Benefits that are hard to quantify &mdash; dignity, social cohesion, women's "
              "voice, ecological resilience &mdash; risk being treated as if they were worth zero."},
             {"t": "hbox", "color": "red", "html": "'Not measured' is not the same as 'not valuable'. "
              "An analysis that silently drops the unmeasurable will systematically under-fund it. Name "
              "what your ratio leaves out."},
         ]},

        {"type": "content", "label": "Use It Well", "title": "A servant, not a master",
         "blocks": [
             {"t": "body", "html": "Cost-effectiveness is most useful as a <em>discipline of "
              "attention</em> &mdash; forcing you to be explicit about costs, outcomes and trade-offs "
              "&mdash; and most dangerous when it becomes the sole arbiter of who gets help."},
             {"t": "hbox", "color": "green", "html": "Best practice: present cost-effectiveness "
              "<em>alongside</em> equity, rights and feasibility, and let deliberation &mdash; not a "
              "single ratio &mdash; make the final call."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Practice &amp; Tools"},

        {"type": "content", "label": "What You Need", "title": "The data a cost-effectiveness study needs",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Cost data:</strong> a full ingredients inventory, including overheads and participant costs",
                 "<strong>Effect data:</strong> a credible, causal estimate of the outcome",
                 "<strong>The comparator:</strong> what you are measuring against",
                 "<strong>Assumptions:</strong> discount rate, time horizon, perspective &mdash; stated openly"]},
             {"t": "hbox", "color": "cyan", "html": "Most disputes over a result trace back to one of "
              "these four. Pin them down before you compute anything."},
         ]},

        {"type": "content", "label": "Build the Model", "title": "Spreadsheets are enough to start",
         "blocks": [
             {"t": "body", "html": "Most cost-effectiveness analyses begin life in a spreadsheet: "
              "costs in one sheet, effects in another, the ratio computed transparently, and a tab for "
              "sensitivity analysis. Clarity beats sophistication."},
             {"t": "hbox", "color": "green", "html": "Keep every assumption in a labelled, single cell "
              "so a reviewer can change it and watch the result move. An auditable spreadsheet is worth "
              "more than a black-box model."},
         ]},

        {"type": "content", "label": "Good Practice", "title": "Habits of a trustworthy analysis",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "State the perspective, comparator, horizon and discount rate explicitly",
                 "Use the ingredients method &mdash; cost everything, including the hidden",
                 "Report the ICER for choices between options, not just averages",
                 "Always run sensitivity analysis and show the range",
                 "Present equity alongside efficiency"]},
         ]},

        {"type": "content", "label": "Watch-Outs", "title": "Red flags when you read a CEA",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "A single ratio with no uncertainty or sensitivity analysis",
                 "An average ratio where an incremental one was needed",
                 "No stated perspective or discount rate",
                 "An effect size from one study, treated as settled",
                 "A ranking that ignores who is reached and who is missed"]},
         ]},

        {"type": "content", "label": "Reading List", "title": "Where to go deeper",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Resource", "What it offers"],
              "rows": [
                  ["Drummond et al., <em>Methods for the Economic Evaluation of Health Care Programmes</em>",
                   "The standard textbook of the field"],
                  ["WHO-CHOICE", "WHO's database and tools for comparing health interventions"],
                  ["Disease Control Priorities (DCP3)", "Cost-effectiveness evidence across diseases for low/middle-income settings"],
                  ["GiveWell &amp; the Disease Control Priorities reviews", "Worked 'cost per outcome' analyses you can learn from"],
                  ["iDSI Reference Case", "A shared standard for credible economic evaluation"]]},
         ]},

        {"type": "content", "label": "Connect the Course", "title": "Pair this with the rest of the 101 Series",
         "blocks": [
             {"t": "body", "html": "Cost-effectiveness sits inside a wider toolkit. It is strongest "
              "when fed by good measurement, sound evaluation and honest data."},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Impact Evaluation</strong> and "
              "<strong>Theory of Change</strong> 101 courses for the full picture."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Most good per rupee</strong> &mdash; because budgets are finite and choices have opportunity costs",
                 "<strong>Match the method</strong> &mdash; CEA (natural units), CUA (DALYs), CBA (money)",
                 "<strong>Use the ICER</strong> &mdash; the incremental, not average, ratio when comparing options",
                 "<strong>Show the uncertainty</strong> &mdash; a point estimate alone is an illusion of precision",
                 "<strong>Efficiency is not the only value</strong> &mdash; weigh equity, rights and dignity too"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Cost Effectiveness 101 &middot; Complete",
         "headline": "Now ask: the most<br>good per rupee?",
         "byline": "You don't need to be a health economist &mdash; you need to hold cost and "
                   "outcome together, demand the increment and the uncertainty, and never let a "
                   "ratio outrank equity. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
