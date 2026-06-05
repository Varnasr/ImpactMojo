# -*- coding: utf-8 -*-
"""
Econometrics 101 — ImpactMojo 101 Series (native deck spec)
Causal inference for South Asian development practitioners and researchers.
Build: python3 scripts/deck-builder/build.py econometrics_101
"""

DECK = {
    "slug": "econometrics-101",
    "title": "Econometrics 101",
    "description": ("Econometrics 101 — a free foundational course for development "
                    "practitioners and researchers in South Asia. From correlation to "
                    "credible causation: potential outcomes, OLS, endogeneity, RCTs, "
                    "instrumental variables, difference-in-differences, regression "
                    "discontinuity, panel fixed effects and how to read results "
                    "critically, with India-centric examples. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Econometrics<br>101",
         "sub": "From Correlation to Credible Causation &mdash; a Foundational Course on "
                "Estimating Causal Effects for Development Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Econometrics Is"},
             {"name": "The Causal Question &amp; the Counterfactual"},
             {"name": "OLS Regression, Properly Understood"},
             {"name": "Endogeneity &amp; Omitted-Variable Bias"},
             {"name": "Randomised Experiments / RCTs"},
             {"name": "Instrumental Variables"},
             {"name": "Difference-in-Differences"},
             {"name": "Regression Discontinuity"},
             {"name": "Panel Data &amp; Fixed Effects"},
             {"name": "Reading &amp; Critiquing Results"},
             {"name": "Tools &amp; Further Reading"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Econometrics Is"},

        {"type": "content", "label": "Definition", "title": "Econometrics, defined",
         "blocks": [
             {"t": "body", "html": "<strong>Econometrics</strong> is where economics, statistics "
              "and real-world data meet. Its central ambition is not just to <em>describe</em> the "
              "world but to estimate <strong>causal effects</strong> &mdash; what would happen if "
              "we changed something."},
             {"t": "term", "word": "Econometrics",
              "def": "The application of statistical methods to economic and social data in order "
              "to test theories and, above all, to measure the causal effect of a policy, "
              "programme or treatment on an outcome of interest."},
             {"t": "hbox", "color": "cyan", "html": "You do not need heavy mathematics to think "
              "like an econometrician. You need to ask, relentlessly: <em>compared to what?</em>"},
         ]},

        {"type": "content", "label": "Three Ingredients", "title": "Economics + statistics + data",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Economics", "label": "A theory of how people and markets behave &mdash; "
                  "what to look for and why", "color": "cyan"},
                 {"num": "Statistics", "label": "Tools to separate signal from noise and quantify "
                  "uncertainty", "color": "green"},
                 {"num": "Data", "label": "Surveys, censuses, admin records, experiments &mdash; "
                  "the evidence itself", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Take away any one ingredient and you get "
              "something less: theory without data is speculation; data without theory is "
              "pattern-hunting."},
         ]},

        {"type": "content", "label": "The Core Job", "title": "The question behind every study",
         "blocks": [
             {"t": "body", "html": "Almost every econometric study is, at heart, answering one "
              "policy question: <strong>does X cause Y, and by how much?</strong>"},
             {"t": "flow", "steps": [
                 "Does a cash transfer raise school attendance?",
                 "Does a new road increase farm incomes?",
                 "Does microcredit lift consumption?",
                 "Does a midday meal cut child anaemia?"]},
             {"t": "hbox", "color": "cyan", "html": "Each is a causal question. The whole "
              "discipline exists because answering it honestly is genuinely hard."},
         ]},

        {"type": "content", "label": "The Trap", "title": "Correlation is not causation",
         "blocks": [
             {"t": "body", "html": "Two things moving together &mdash; districts with more bank "
              "branches having higher incomes &mdash; does not mean one caused the other. The "
              "link could run the other way, or a third factor could drive both."},
             {"t": "quote", "text": "Whenever two variables are correlated, at least four "
              "explanations are possible &mdash; and only one of them is 'X causes Y'.",
              "attr": "&mdash; a working principle of causal inference"},
         ]},

        {"type": "content", "label": "Why Naive Comparisons Fail", "title": "The comparison that fools you",
         "blocks": [
             {"t": "body", "html": "Suppose villages with a microfinance branch have higher "
              "incomes than villages without one. Tempting conclusion: microfinance works. But "
              "branches were not placed at random &mdash; lenders chose <em>more promising</em> "
              "villages to begin with."},
             {"t": "hbox", "color": "red", "html": "The income gap mixes the <em>effect</em> of "
              "microfinance with the pre-existing differences between the two kinds of village. "
              "Econometrics exists to pull these apart."},
         ]},

        {"type": "content", "label": "Description vs Causation", "title": "Two very different goals",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Descriptive / predictive", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Who is poor? Where is dropout highest? What "
                   "will demand be next year? Correlations are enough here."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Causal", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Will <em>this</em> programme reduce dropout? "
                   "Here you must imagine a world without the programme &mdash; a counterfactual."}]}]},
             {"t": "hbox", "color": "amber", "html": "Most policy questions are causal. That is "
              "why this course spends most of its time on causal methods."},
         ]},

        {"type": "content", "label": "The Credibility Revolution", "title": "How the field changed",
         "blocks": [
             {"t": "body", "html": "From the 1990s onwards, econometrics shifted from elaborate "
              "models toward <strong>research designs</strong> that mimic experiments &mdash; "
              "the 'credibility revolution'. The 2019 and 2021 Nobel prizes recognised RCTs and "
              "natural-experiment methods used heavily in development."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "2019", "label": "Nobel: Banerjee, Duflo &amp; Kremer for the "
                  "experimental approach to poverty", "color": "green",
                  "source": "Sveriges Riksbank Prize"},
                 {"num": "2021", "label": "Nobel: Card, Angrist &amp; Imbens for natural "
                  "experiments &amp; causal methods", "color": "indigo",
                  "source": "Sveriges Riksbank Prize"}]},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Causal Question &amp; the Counterfactual"},

        {"type": "content", "label": "The Big Idea", "title": "Compared to what?",
         "blocks": [
             {"t": "body", "html": "A causal effect is always a <strong>comparison</strong>: the "
              "outcome <em>with</em> the treatment versus the outcome that <em>would have</em> "
              "occurred without it, for the very same unit, at the same time."},
             {"t": "term", "word": "Counterfactual",
              "def": "What would have happened to a treated unit had it <em>not</em> been treated. "
              "It is never observed &mdash; which is the whole difficulty of causal inference."},
         ]},

        {"type": "content", "label": "Potential Outcomes", "title": "Two possible futures for each unit",
         "blocks": [
             {"t": "body", "html": "The potential-outcomes framework imagines, for each person "
              "<em>i</em>, two outcomes:"},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Y&#8331;(1)", "label": "outcome if person i receives the treatment",
                  "color": "green"},
                 {"num": "Y&#8331;(0)", "label": "outcome if person i does NOT receive it",
                  "color": "amber"}]},
             {"t": "hbox", "color": "cyan", "html": "The individual causal effect is the "
              "difference Y&#8331;(1) &minus; Y&#8331;(0). It is exactly what we want &mdash; and "
              "exactly what we can never see."},
         ]},

        {"type": "content", "label": "The Core Obstacle", "title": "The fundamental problem of causal inference",
         "blocks": [
             {"t": "body", "html": "For any one person we observe <em>only one</em> outcome: either "
              "the treated state or the untreated state, never both. The other is forever "
              "counterfactual."},
             {"t": "hbox", "color": "red", "html": "<strong>The fundamental problem of causal "
              "inference:</strong> we can never observe both Y&#8331;(1) and Y&#8331;(0) for the "
              "same unit. Causal inference is, in essence, a missing-data problem."},
         ]},

        {"type": "content", "label": "The Workaround", "title": "We estimate averages, not individuals",
         "blocks": [
             {"t": "body", "html": "Since the individual effect is unknowable, we aim instead for "
              "the <strong>average treatment effect</strong> across a group &mdash; the mean of "
              "Y(1) minus the mean of Y(0) for a population."},
             {"t": "term", "word": "Average Treatment Effect (ATE)",
              "def": "The average of the individual causal effects across all units in a "
              "population: what the treatment does on average, even though no single person's "
              "effect is observed."},
             {"t": "hbox", "color": "cyan", "html": "The trick is finding a credible "
              "<em>stand-in</em> for the unobserved counterfactual outcome of the treated group."},
         ]},

        {"type": "content", "label": "The Naive Estimate", "title": "Why a simple group difference goes wrong",
         "blocks": [
             {"t": "body", "html": "We compare treated people's outcomes with untreated people's "
              "outcomes. But the untreated are different people &mdash; their average Y(0) need "
              "not equal the treated group's Y(0)."},
             {"t": "raw", "html": "<div style='font-family:monospace;font-size:1.05em;line-height:1.8;"
              "background:rgba(99,102,241,0.08);border:1px solid rgba(99,102,241,0.35);"
              "border-radius:10px;padding:18px 22px;'>"
              "Observed gap = <b>True effect (ATT)</b> + <b style='color:#EF4444'>Selection bias</b><br>"
              "<span style='font-size:0.85em;opacity:0.8'>"
              "Selection bias = how treated &amp; untreated differ in Y(0) <em>before</em> any treatment"
              "</span></div>"},
         ]},

        {"type": "content", "label": "Selection Bias", "title": "The villain of the whole course",
         "blocks": [
             {"t": "term", "word": "Selection bias",
              "def": "The systematic difference in (untreated) outcomes between those who get a "
              "treatment and those who do not, arising because they are not comparable to begin "
              "with."},
             {"t": "body", "html": "Healthier people exercise more; richer farmers adopt new "
              "seeds first; motivated students attend coaching. Compare them with everyone else "
              "and you measure who they <em>were</em>, not what the treatment <em>did</em>."},
         ]},

        {"type": "content", "label": "An Example", "title": "Do hospitals make people sicker?",
         "blocks": [
             {"t": "body", "html": "People who visited a hospital last year report worse health "
              "than people who did not. Does the hospital harm them? Of course not &mdash; "
              "<strong>sick people go to hospital</strong>. The comparison is contaminated by who "
              "selects in."},
             {"t": "hbox", "color": "amber", "html": "This cartoon example is the same logic that "
              "wrecks naive evaluations of training, microcredit and health camps. Selection is "
              "everywhere."},
         ]},

        {"type": "content", "label": "The Strategy", "title": "Every method is a counterfactual strategy",
         "blocks": [
             {"t": "body", "html": "The rest of this course is a toolkit of <strong>research "
              "designs</strong>, each a different way to construct a credible counterfactual &mdash; "
              "a comparison group that plausibly shows what would have happened anyway."},
             {"t": "flow", "steps": [
                 "RCTs: randomisation makes groups comparable",
                 "IV: an external nudge mimics random assignment",
                 "DiD: a comparison group tracks the trend",
                 "RD: units just above/below a cutoff are alike"]},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "OLS Regression, Properly Understood"},

        {"type": "content", "label": "The Workhorse", "title": "Regression: fitting a line through data",
         "blocks": [
             {"t": "body", "html": "<strong>Ordinary Least Squares (OLS)</strong> finds the "
              "straight line that minimises the sum of squared vertical distances between the line "
              "and the data points. It is the workhorse of applied economics."},
             {"t": "raw", "html": "<div style='font-family:monospace;font-size:1.15em;text-align:center;"
              "background:rgba(14,165,233,0.08);border:1px solid rgba(14,165,233,0.35);"
              "border-radius:10px;padding:20px;'>"
              "Y = &alpha; + &beta;X + &epsilon;<br>"
              "<span style='font-size:0.7em;opacity:0.8'>outcome = intercept + slope &times; "
              "predictor + error</span></div>"},
         ]},

        {"type": "content", "label": "See It", "title": "A fitted regression line",
         "blocks": [
             {"t": "chart", "canvas": "olsScatter",
              "title": "Years of schooling vs monthly wage &mdash; OLS line of best fit",
              "source": "Illustrative",
              "type": "scatter",
              "data": {"datasets": [
                  {"label": "Workers",
                   "data": [{"x": 0, "y": 6}, {"x": 2, "y": 7}, {"x": 4, "y": 9},
                            {"x": 5, "y": 8}, {"x": 6, "y": 11}, {"x": 8, "y": 12},
                            {"x": 8, "y": 10}, {"x": 10, "y": 14}, {"x": 12, "y": 15},
                            {"x": 12, "y": 17}, {"x": 14, "y": 18}, {"x": 16, "y": 22}],
                   "backgroundColor": "#0EA5E9", "pointRadius": 6},
                  {"label": "OLS fit", "type": "line",
                   "data": [{"x": 0, "y": 6.2}, {"x": 16, "y": 21.0}],
                   "borderColor": "#EF4444", "borderWidth": 3, "pointRadius": 0, "fill": False}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Years of schooling'} }, y:{ title:{display:true,text:'Monthly wage (₹000s)'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The slope says how much wage rises, on "
              "average, per extra year of schooling &mdash; <em>in this data</em>. Whether that "
              "slope is causal is a separate question entirely."},
         ]},

        {"type": "content", "label": "What Regression Really Is", "title": "The conditional expectation function",
         "blocks": [
             {"t": "term", "word": "Conditional Expectation Function (CEF)",
              "def": "E[Y | X] &mdash; the average value of the outcome Y for each value of the "
              "predictor X. OLS gives the best straight-line approximation to this function."},
             {"t": "body", "html": "Read a regression as a machine that answers: <em>for units "
              "with this value of X, what is the average Y?</em> Nothing more is guaranteed."},
         ]},

        {"type": "content", "label": "Reading a Coefficient", "title": "What a slope coefficient means",
         "blocks": [
             {"t": "body", "html": "A coefficient &beta; on X is the predicted change in Y "
              "associated with a <strong>one-unit increase in X</strong>, holding the other "
              "included variables fixed."},
             {"t": "hbox", "color": "amber", "html": "Two load-bearing words: "
              "<strong>'associated'</strong> (not necessarily caused) and <strong>'included'</strong> "
              "(only the variables you put in the model are held fixed &mdash; not the ones you "
              "left out)."},
         ]},

        {"type": "content", "label": "Multiple Regression", "title": "Controlling for other variables",
         "blocks": [
             {"t": "body", "html": "Adding controls &mdash; Y = &alpha; + &beta;X + &gamma;Z + "
              "&epsilon; &mdash; lets &beta; describe the X&ndash;Y link <em>among units with the "
              "same Z</em>. This is how we try to compare like with like."},
             {"t": "hbox", "color": "red", "html": "But you can only control for what you "
              "<em>measure</em>. The variables you cannot observe &mdash; ability, motivation, "
              "soil quality &mdash; are precisely the ones that cause trouble."},
         ]},

        {"type": "content", "label": "Units &amp; Interpretation", "title": "Levels, logs and dummies",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Form", "Coefficient reads as", "Common use"],
              "rows": [
                  ["Y on X (levels)", "&Delta;Y in Y-units per 1-unit &Delta;X", "Most variables"],
                  ["log Y on X", "approx. % change in Y per 1-unit &Delta;X", "Wages, income"],
                  ["log Y on log X", "elasticity: % &Delta;Y per 1% &Delta;X", "Demand, output"],
                  ["Y on a dummy (0/1)", "gap in mean Y between the two groups", "Treated vs control"]]},
             {"t": "hbox", "color": "cyan", "html": "Knowing the functional form tells you how to "
              "<em>translate</em> a coefficient into a sentence a programme officer understands."},
         ]},

        {"type": "content", "label": "When OLS Is Trustworthy", "title": "Gauss&ndash;Markov &amp; BLUE",
         "blocks": [
             {"t": "body", "html": "Under a set of assumptions &mdash; the <strong>Gauss&ndash;"
              "Markov</strong> conditions &mdash; OLS is <strong>BLUE</strong>: the Best Linear "
              "Unbiased Estimator. Among all linear unbiased methods, it has the smallest "
              "variance."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>B</strong>est: lowest variance among linear unbiased estimators",
                 "<strong>L</strong>inear: it is a linear function of the data",
                 "<strong>U</strong>nbiased: on average it hits the true value",
                 "<strong>E</strong>stimator: a recipe for guessing the parameter"]},
         ]},

        {"type": "content", "label": "The Crucial Caveat", "title": "Unbiased ≠ causal",
         "blocks": [
             {"t": "body", "html": "The key Gauss&ndash;Markov assumption is that the error term "
              "is <strong>uncorrelated with X</strong> (exogeneity). If something in the error "
              "&mdash; an omitted cause &mdash; correlates with X, OLS is biased and the "
              "coefficient is <em>not</em> the causal effect."},
             {"t": "hbox", "color": "red", "html": "This single assumption is where most of "
              "applied econometrics lives or dies. The next section is entirely about how it "
              "breaks."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Endogeneity &amp; Omitted-Variable Bias"},

        {"type": "content", "label": "The Central Threat", "title": "Endogeneity, defined",
         "blocks": [
             {"t": "term", "word": "Endogeneity",
              "def": "A situation where the explanatory variable X is correlated with the error "
              "term &mdash; that is, with something that also affects Y but is left out of the "
              "model. It makes the OLS coefficient biased and non-causal."},
             {"t": "body", "html": "When X is <strong>exogenous</strong>, OLS recovers the causal "
              "effect. When X is <strong>endogenous</strong>, it does not. Diagnosing endogeneity "
              "is the practitioner's core skill."},
         ]},

        {"type": "content", "label": "Three Sources", "title": "Where endogeneity comes from",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Omitted variables", "label": "A common cause of both X and Y is left "
                  "out", "color": "red"},
                 {"num": "Reverse causality", "label": "Y also affects X &mdash; the arrow runs "
                  "both ways", "color": "amber"},
                 {"num": "Measurement error", "label": "X is recorded with noise, biasing its "
                  "coefficient", "color": "indigo"}]},
             {"t": "hbox", "color": "cyan", "html": "All three break the exogeneity assumption. "
              "We take them one at a time."},
         ]},

        {"type": "content", "label": "OVB", "title": "Omitted-variable bias, illustrated",
         "blocks": [
             {"t": "chart", "canvas": "ovbChart",
              "title": "Wage vs schooling &mdash; the same data split by (omitted) ability",
              "source": "Illustrative",
              "type": "scatter",
              "data": {"datasets": [
                  {"label": "Lower ability",
                   "data": [{"x": 4, "y": 7}, {"x": 6, "y": 8}, {"x": 8, "y": 9},
                            {"x": 10, "y": 10}, {"x": 12, "y": 11}],
                   "backgroundColor": "#0EA5E9", "pointRadius": 7},
                  {"label": "Higher ability",
                   "data": [{"x": 8, "y": 13}, {"x": 10, "y": 14}, {"x": 12, "y": 15},
                            {"x": 14, "y": 16}, {"x": 16, "y": 17}],
                   "backgroundColor": "#10B981", "pointRadius": 7}]},
              "options": {"__js__": "{ plugins:{legend:{display:true,position:'bottom'}}, scales:{ x:{ title:{display:true,text:'Years of schooling'} }, y:{ title:{display:true,text:'Monthly wage (₹000s)'} } } }"}},
             {"t": "hbox", "color": "red", "html": "Within each ability group the schooling slope "
              "is gentle. Pooled, a steep line appears &mdash; because higher-ability people get "
              "<em>both</em> more schooling and higher wages. OLS credits schooling for ability's "
              "effect."},
         ]},

        {"type": "content", "label": "Sign of the Bias", "title": "Which way does OVB push?",
         "blocks": [
             {"t": "body", "html": "The direction of omitted-variable bias depends on two signs: "
              "how the omitted variable Z relates to X, and how Z relates to Y."},
             {"t": "table",
              "head": ["Z &rarr; X", "Z &rarr; Y", "Bias on &beta;"],
              "rows": [
                  ["+", "+", "Upward (too big)"],
                  ["&minus;", "&minus;", "Upward (too big)"],
                  ["+", "&minus;", "Downward (too small)"],
                  ["&minus;", "+", "Downward (too small)"]]},
             {"t": "hbox", "color": "amber", "html": "Even when you cannot fix OVB, you can often "
              "<em>reason about its direction</em> &mdash; and so bound how wrong your estimate "
              "might be."},
         ]},

        {"type": "content", "label": "Reverse Causality", "title": "When the arrow runs both ways",
         "blocks": [
             {"t": "body", "html": "Do more police <em>cause</em> more crime? Cross-section data "
              "often shows a positive correlation &mdash; because cities with more crime "
              "<strong>hire more police</strong>. Causation runs from Y to X."},
             {"t": "flow", "steps": [
                 "More crime (Y)",
                 "leads cities to hire more police (X)",
                 "so X and Y correlate positively",
                 "even if police actually reduce crime"]},
         ]},

        {"type": "content", "label": "Measurement Error", "title": "Noise in X biases toward zero",
         "blocks": [
             {"t": "body", "html": "When the predictor X is measured with random error &mdash; "
              "self-reported income, recalled expenditure &mdash; its coefficient is pulled "
              "<strong>toward zero</strong>. This is <strong>attenuation bias</strong>."},
             {"t": "hbox", "color": "indigo", "html": "Counter-intuitive but important: messy "
              "measurement of X usually makes a real effect look <em>smaller</em> than it is, not "
              "larger. Noise in Y, by contrast, mainly inflates uncertainty."},
         ]},

        {"type": "content", "label": "The False Comfort of Controls", "title": "More controls is not a cure",
         "blocks": [
             {"t": "body", "html": "It is tempting to believe that adding enough control variables "
              "removes bias. But you can only control for what you <strong>observe and measure</strong>. "
              "Unobservables &mdash; motivation, ability, local governance &mdash; remain in the error."},
             {"t": "hbox", "color": "red", "html": "Worse, controlling for the wrong variable &mdash; "
              "something <em>caused</em> by the treatment, or a collider &mdash; can <em>introduce</em> "
              "bias. Controls are a scalpel, not a sledgehammer."},
         ]},

        {"type": "content", "label": "The Way Out", "title": "Design beats adjustment",
         "blocks": [
             {"t": "body", "html": "Because we can never be sure we have controlled for every "
              "confounder, credible causal work relies on a <strong>research design</strong> that "
              "creates exogenous variation in X &mdash; variation unrelated to the unobservables."},
             {"t": "quote", "text": "The way to estimate a causal effect is not to control for "
              "everything, but to find variation in the treatment that is as good as random.",
              "attr": "&mdash; the design-based view of econometrics"},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Randomised Experiments / RCTs"},

        {"type": "content", "label": "The Gold Standard", "title": "Randomisation solves selection",
         "blocks": [
             {"t": "body", "html": "In a <strong>randomised controlled trial (RCT)</strong>, "
              "units are assigned to treatment or control <strong>by a coin flip</strong>. On "
              "average the two groups are identical in everything &mdash; observed and "
              "unobserved &mdash; except the treatment."},
             {"t": "hbox", "color": "green", "html": "Because assignment is independent of "
              "potential outcomes, the control group is a credible counterfactual. Selection bias "
              "is designed away."},
         ]},

        {"type": "content", "label": "Why It Works", "title": "Balance in expectation",
         "blocks": [
             {"t": "body", "html": "Randomisation does not make any two specific people identical. "
              "It makes the <em>groups</em> statistically equivalent, so their average Y(0) is "
              "the same. The control group's outcome stands in for the treated group's missing "
              "counterfactual."},
             {"t": "raw", "html": "<div style='font-family:monospace;font-size:1.05em;text-align:center;"
              "background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.35);"
              "border-radius:10px;padding:18px;'>"
              "Effect = mean Y(treated) &minus; mean Y(control)<br>"
              "<span style='font-size:0.8em;opacity:0.8'>and with randomisation, selection bias &asymp; 0</span></div>"},
         ]},

        {"type": "content", "label": "Check the Balance", "title": "A balance table",
         "blocks": [
             {"t": "chart", "canvas": "balanceChart",
              "title": "Baseline characteristics &mdash; treatment vs control (should be similar)",
              "source": "Illustrative balance check",
              "type": "bar",
              "data": {"labels": ["% female", "Mean age", "% literate", "Land (acres)", "HH size"],
                       "datasets": [
                           {"label": "Treatment", "data": [51, 34, 62, 1.8, 5.2],
                            "backgroundColor": "#10B981"},
                           {"label": "Control", "data": [49, 35, 61, 1.9, 5.1],
                            "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ plugins:{legend:{display:true,position:'bottom'}} }"}},
             {"t": "hbox", "color": "cyan", "html": "Good randomisation produces near-identical "
              "groups at baseline. A balance table is the first thing to check in any RCT &mdash; "
              "it is the evidence that the design worked."},
         ]},

        {"type": "content", "label": "J-PAL", "title": "RCTs in development: J-PAL &amp; the field",
         "blocks": [
             {"t": "body", "html": "The <strong>Abdul Latif Jameel Poverty Action Lab "
              "(J-PAL)</strong>, founded in 2003, popularised RCTs in development. Hundreds of "
              "trials &mdash; many in India &mdash; have tested deworming, remedial teaching, "
              "immunisation incentives, and more."},
             {"t": "hbox", "color": "green", "html": "A landmark example: <strong>Pratham's "
              "'Teaching at the Right Level'</strong> remedial-education model was refined and "
              "scaled through a sequence of RCTs across Indian states."},
         ]},

        {"type": "content", "label": "Growth", "title": "The rise of development RCTs",
         "blocks": [
             {"t": "chart", "canvas": "rctGrowthChart",
              "title": "Cumulative development RCTs registered (stylised, illustrative trend)",
              "source": "Illustrative &mdash; stylised to show the trend, not exact counts",
              "type": "line",
              "data": {"labels": ["2003", "2006", "2009", "2012", "2015", "2018", "2021", "2024"],
                       "datasets": [{"label": "Cumulative RCTs",
                                     "data": [10, 60, 180, 420, 760, 1150, 1500, 1850],
                                     "borderColor": "#10B981",
                                     "backgroundColor": "rgba(16,185,129,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Cumulative count (illustrative)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "The exact numbers here are illustrative, but "
              "the shape is real: development RCTs grew explosively after the mid-2000s."},
         ]},

        {"type": "content", "label": "Two Kinds of Validity", "title": "Internal vs external validity",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Internal validity", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Is the estimated effect causally correct "
                   "<em>for this sample</em>? RCTs are strong here &mdash; their headline virtue."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "External validity", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Will it hold <em>elsewhere</em> &mdash; other "
                   "states, scales, populations? RCTs are often weak here."}]}]},
             {"t": "hbox", "color": "red", "html": "A perfectly clean trial in one district may "
              "not generalise. 'It worked in Rajasthan' is not 'it will work in Bihar'."},
         ]},

        {"type": "content", "label": "Real-World Wrinkles", "title": "What can still go wrong",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Threat", "What happens", "Fix / response"],
              "rows": [
                  ["Attrition", "Treated &amp; control drop out differently", "Track everyone; bound effects"],
                  ["Spillovers", "Control units affected by treatment", "Randomise at cluster level"],
                  ["Non-compliance", "Assigned but don't take treatment", "Analyse by assignment (ITT)"],
                  ["Hawthorne effects", "Being watched changes behaviour", "Blinding where possible"]]},
             {"t": "hbox", "color": "cyan", "html": "<strong>Intention-to-treat (ITT)</strong> "
              "&mdash; analysing people by the group they were <em>assigned</em> to &mdash; "
              "preserves the randomisation even when compliance is imperfect."},
         ]},

        {"type": "content", "label": "Ethics", "title": "Is it ethical to randomise a benefit?",
         "blocks": [
             {"t": "bullets", "items": [
                 "Randomise when there is genuine uncertainty about whether the programme works "
                 "(<strong>equipoise</strong>)",
                 "Use waitlists or phased roll-outs so the control group eventually benefits",
                 "Never withhold a known, proven, life-saving treatment to run a trial",
                 "Secure informed consent and ethics-board (IRB) approval"]},
             {"t": "hbox", "color": "amber", "html": "Scarce budgets mean not everyone can be "
              "served at once anyway. A lottery for limited places can be both fair <em>and</em> "
              "a clean experiment."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Instrumental Variables"},

        {"type": "content", "label": "When You Can't Randomise", "title": "Borrowing randomness from nature",
         "blocks": [
             {"t": "body", "html": "Often you cannot run an experiment &mdash; the treatment "
              "already happened, or randomising is impossible. An <strong>instrumental variable "
              "(IV)</strong> finds a source of variation in X that is 'as good as random'."},
             {"t": "term", "word": "Instrumental variable (instrument)",
              "def": "A variable Z that shifts the treatment X but affects the outcome Y "
              "<em>only</em> through X. It isolates the part of X that is unrelated to the "
              "confounders."},
         ]},

        {"type": "content", "label": "The Logic", "title": "Use only the exogenous part of X",
         "blocks": [
             {"t": "flow", "steps": [
                 "Instrument Z (as-good-as-random)",
                 "shifts treatment X",
                 "X changes the outcome Y",
                 "Z affects Y ONLY through X"]},
             {"t": "hbox", "color": "cyan", "html": "IV throws away the endogenous, confounded "
              "variation in X and keeps only the clean variation driven by Z. That clean slice "
              "yields a causal estimate."},
         ]},

        {"type": "content", "label": "Two Conditions", "title": "An instrument must satisfy BOTH",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "1. Relevance", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Z must actually shift X &mdash; a real, "
                   "strong first-stage relationship between instrument and treatment. "
                   "<em>Testable</em> in the data."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "2. Exclusion restriction", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Z must affect Y <em>only</em> through X "
                   "&mdash; no other pathway, no direct effect, uncorrelated with the error. "
                   "<em>Untestable</em>; argued, not proven."}]}]},
             {"t": "hbox", "color": "red", "html": "BOTH are required. Relevance you can check; the "
              "exclusion restriction you must defend with theory and institutional knowledge "
              "&mdash; it is where most IV claims succeed or fail."},
         ]},

        {"type": "content", "label": "A Classic Example", "title": "Rainfall as an instrument",
         "blocks": [
             {"t": "body", "html": "To study whether economic downturns fuel conflict, researchers "
              "have used <strong>rainfall shocks</strong> as an instrument for agricultural "
              "income in rain-fed economies. Rain is plausibly random year to year."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Relevance:</strong> rainfall strongly affects farm income (first stage)",
                 "<strong>Exclusion:</strong> rainfall is argued to affect outcomes <em>only</em> "
                 "via income &mdash; the part you must defend",
                 "Caveat: if rain also affects, say, mobility or disease directly, exclusion fails"]},
         ]},

        {"type": "content", "label": "Another Example", "title": "Distance, sib-sex &amp; quarter of birth",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Instrument (Z)", "Treatment (X)", "Exclusion argument"],
              "rows": [
                  ["Distance to a school/college", "Years of schooling", "Distance affects wages only via schooling"],
                  ["Quarter of birth", "Years of schooling", "Birth-month is arbitrary, tied to school-start laws"],
                  ["Sex composition of first 2 kids", "Having a 3rd child", "Sex mix is random, shifts fertility"]]},
             {"t": "hbox", "color": "amber", "html": "Each is clever &mdash; and each has been "
              "<em>challenged</em> on exclusion grounds. A good IV invites scrutiny of the one "
              "assumption you cannot test."},
         ]},

        {"type": "content", "label": "What IV Estimates", "title": "A local effect, for compliers",
         "blocks": [
             {"t": "body", "html": "IV does not recover the average effect for everyone. It "
              "recovers the <strong>Local Average Treatment Effect (LATE)</strong> &mdash; the "
              "effect for the <em>compliers</em>, those whose treatment status is moved by the "
              "instrument."},
             {"t": "hbox", "color": "indigo", "html": "So 'the IV estimate' answers a specific "
              "question: the effect on people the instrument actually nudged. Different "
              "instruments can give different &mdash; both correct &mdash; LATEs."},
         ]},

        {"type": "content", "label": "Weak Instruments", "title": "The danger of a weak first stage",
         "blocks": [
             {"t": "body", "html": "If Z only weakly predicts X (a <strong>weak instrument</strong>), "
              "IV estimates become wildly imprecise and can be <em>more</em> biased than plain "
              "OLS &mdash; even tiny exclusion violations get amplified."},
             {"t": "hbox", "color": "red", "html": "Rule of thumb: report the first-stage "
              "<strong>F-statistic</strong>; a common (rough) threshold is F &gt; 10. A weak "
              "instrument is worse than no instrument at all."},
         ]},

        {"type": "content", "label": "Reading IV Critically", "title": "Three questions for any IV study",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Is it relevant?</strong> Is the first stage strong (high F)?",
                 "<strong>Is exclusion plausible?</strong> What is the story for 'only through X', "
                 "and what would break it?",
                 "<strong>Whose effect is it?</strong> Who are the compliers &mdash; and do you "
                 "care about them?"]},
             {"t": "hbox", "color": "cyan", "html": "A persuasive IV paper spends most of its "
              "words defending the exclusion restriction, not running the regression."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Difference-in-Differences"},

        {"type": "content", "label": "The Idea", "title": "Before-and-after, with a comparison group",
         "blocks": [
             {"t": "body", "html": "<strong>Difference-in-Differences (DiD)</strong> studies a "
              "policy that hits one group but not another. It compares the <em>change</em> in the "
              "treated group with the <em>change</em> in an untreated comparison group."},
             {"t": "term", "word": "Difference-in-Differences",
              "def": "An estimator that subtracts the before&ndash;after change in a comparison "
              "group from the before&ndash;after change in the treated group, netting out both "
              "fixed group differences and common time trends."},
         ]},

        {"type": "content", "label": "The Two Differences", "title": "Why subtract twice?",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Difference 1", "label": "Treated group: after &minus; before (removes "
                  "fixed traits of the group)", "color": "cyan"},
                 {"num": "Difference 2", "label": "Comparison group: after &minus; before (captures "
                  "what would have happened anyway)", "color": "indigo"}]},
             {"t": "hbox", "color": "green", "html": "The DiD estimate is Difference 1 &minus; "
              "Difference 2. The comparison group's change is the <strong>counterfactual</strong> "
              "trend for the treated group."},
         ]},

        {"type": "content", "label": "See It", "title": "A difference-in-differences plot",
         "blocks": [
             {"t": "chart", "canvas": "didChart",
              "title": "Outcome over time &mdash; treated vs comparison, policy at 'After'",
              "source": "Illustrative",
              "type": "line",
              "data": {"labels": ["Before", "After"],
                       "datasets": [
                           {"label": "Treated (actual)", "data": [40, 58],
                            "borderColor": "#10B981", "borderWidth": 3, "pointRadius": 5, "fill": False},
                           {"label": "Comparison", "data": [44, 50],
                            "borderColor": "#6366F1", "borderWidth": 3, "pointRadius": 5, "fill": False},
                           {"label": "Treated (counterfactual)", "data": [40, 46],
                            "borderColor": "#EF4444", "borderWidth": 2, "borderDash": [6, 6],
                            "pointRadius": 4, "fill": False}]},
              "options": {"__js__": "{ plugins:{legend:{display:true,position:'bottom'}}, scales:{ y:{ title:{display:true,text:'Outcome (%)'}, min:30, max:65 } } }"}},
             {"t": "hbox", "color": "amber", "html": "The DiD effect is the gap between the treated "
              "group's actual outcome (58) and its counterfactual (46) &mdash; about "
              "<strong>12 points</strong>. The dashed red line is the assumed parallel trend."},
         ]},

        {"type": "content", "label": "The Key Assumption", "title": "Parallel trends &mdash; not equal levels",
         "blocks": [
             {"t": "body", "html": "DiD is valid only if, <em>absent the policy</em>, the two "
              "groups would have moved in <strong>parallel</strong> &mdash; the same trend over "
              "time. The groups need NOT start at the same level."},
             {"t": "hbox", "color": "red", "html": "<strong>Common error:</strong> thinking DiD "
              "requires the groups to be identical before treatment. It does not. It requires "
              "their <em>trends</em> to be parallel &mdash; a statement about slopes, not levels."},
         ]},

        {"type": "content", "label": "Defending It", "title": "How to support parallel trends",
         "blocks": [
             {"t": "bullets", "items": [
                 "Plot <strong>pre-treatment trends</strong>: did the groups move together "
                 "<em>before</em> the policy?",
                 "Run a <strong>placebo / event-study</strong> check on pre-periods",
                 "Choose a comparison group as similar as possible to the treated one",
                 "Be honest: parallel trends is an <em>assumption</em>, never fully provable"]},
             {"t": "hbox", "color": "cyan", "html": "Parallel pre-trends do not <em>prove</em> "
              "parallel counterfactual trends &mdash; but their absence is a serious warning sign."},
         ]},

        {"type": "content", "label": "Natural Experiments", "title": "When policy creates the design",
         "blocks": [
             {"t": "body", "html": "DiD shines with <strong>natural experiments</strong> &mdash; "
              "policies rolled out to some states/districts and not others, or at different "
              "times. The staggered roll-out supplies the treatment and comparison groups."},
             {"t": "hbox", "color": "green", "html": "Indian examples: the phased district roll-out "
              "of <strong>NREGA (2006&ndash;08)</strong>, or state-level reforms introduced in "
              "some states before others, are natural settings for DiD."},
         ]},

        {"type": "content", "label": "When It Breaks", "title": "Threats to a DiD design",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Threat", "What it does", "Watch for"],
              "rows": [
                  ["Diverging trends", "Groups were drifting apart anyway", "Non-parallel pre-trends"],
                  ["Other shocks", "A second event hits only one group", "Concurrent policies"],
                  ["Composition change", "Who is in each group shifts over time", "Migration, attrition"],
                  ["Anticipation", "Behaviour changes before the policy", "Pre-period jumps"]]},
             {"t": "hbox", "color": "amber", "html": "Recent methods literature also warns that "
              "<strong>staggered</strong> roll-outs with two-way fixed effects can mislead if "
              "effects vary over time &mdash; use modern DiD estimators."},
         ]},

        {"type": "content", "label": "Reading DiD Critically", "title": "Questions for any DiD study",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Did the authors show parallel <strong>pre-trends</strong>?",
                 "Is the comparison group genuinely comparable?",
                 "Could another shock have hit only one group at the same time?",
                 "With staggered timing, did they use an appropriate modern estimator?"]},
             {"t": "hbox", "color": "cyan", "html": "DiD is powerful and intuitive &mdash; which is "
              "exactly why its one assumption deserves the hardest scrutiny."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Regression Discontinuity"},

        {"type": "content", "label": "The Idea", "title": "Assignment by an arbitrary cutoff",
         "blocks": [
             {"t": "body", "html": "Many programmes use a <strong>threshold</strong> rule: a "
              "scholarship for scores above 60, a poverty scheme for those below a deprivation "
              "score. <strong>Regression Discontinuity (RD)</strong> exploits that sharp cutoff."},
             {"t": "term", "word": "Regression Discontinuity (RD)",
              "def": "A design that compares units just above and just below a cutoff on a "
              "'running variable'. Near the threshold, who lands on which side is essentially "
              "random, so the two sides are comparable."},
         ]},

        {"type": "content", "label": "Why It Works", "title": "Just-above ≈ just-below",
         "blocks": [
             {"t": "body", "html": "A student scoring 59 and one scoring 61 are, in every "
              "meaningful way, alike &mdash; ability, background, motivation. Yet one gets the "
              "programme and the other does not. The cutoff manufactures a local experiment."},
             {"t": "hbox", "color": "cyan", "html": "The jump in the outcome <em>at</em> the "
              "threshold &mdash; a discontinuity that nothing else can explain &mdash; is the "
              "causal effect of the programme."},
         ]},

        {"type": "content", "label": "See It", "title": "A jump at the cutoff",
         "blocks": [
             {"t": "chart", "canvas": "rdChart",
              "title": "Outcome vs running variable &mdash; treatment assigned above the cutoff (50)",
              "source": "Illustrative",
              "type": "scatter",
              "data": {"datasets": [
                  {"label": "Below cutoff (untreated)",
                   "data": [{"x": 20, "y": 30}, {"x": 28, "y": 33}, {"x": 35, "y": 36},
                            {"x": 40, "y": 38}, {"x": 45, "y": 40}, {"x": 49, "y": 41}],
                   "backgroundColor": "#6366F1", "pointRadius": 7},
                  {"label": "Above cutoff (treated)",
                   "data": [{"x": 51, "y": 53}, {"x": 55, "y": 55}, {"x": 60, "y": 57},
                            {"x": 66, "y": 59}, {"x": 73, "y": 62}, {"x": 80, "y": 64}],
                   "backgroundColor": "#10B981", "pointRadius": 7}]},
              "options": {"__js__": "{ plugins:{legend:{display:true,position:'bottom'}}, scales:{ x:{ title:{display:true,text:'Running variable (e.g. test score)'} }, y:{ title:{display:true,text:'Outcome'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "The vertical <strong>jump</strong> at the "
              "cutoff (50) &mdash; roughly 41 to 53 &mdash; is the estimated effect. The smooth "
              "slope on each side is the relationship that would hold without any jump."},
         ]},

        {"type": "content", "label": "Sharp vs Fuzzy", "title": "Two flavours of RD",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Sharp RD", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Crossing the cutoff <em>perfectly</em> "
                   "determines treatment &mdash; everyone above is treated, everyone below is not."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Fuzzy RD", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Crossing the cutoff only <em>raises the "
                   "probability</em> of treatment. The jump in take-up is used like an instrument."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Fuzzy RD is essentially IV at the threshold: "
              "the cutoff instruments for actual treatment."},
         ]},

        {"type": "content", "label": "Local Validity", "title": "RD gives a LOCAL effect",
         "blocks": [
             {"t": "body", "html": "RD estimates the effect <strong>only at the cutoff</strong> "
              "&mdash; for units near the threshold. It says little about people far from it."},
             {"t": "hbox", "color": "red", "html": "<strong>Key caveat:</strong> the RD effect is "
              "<em>local</em>. A scholarship's effect for students scoring 59&ndash;61 may differ "
              "entirely from its effect for those scoring 90. Do not over-generalise the jump."},
         ]},

        {"type": "content", "label": "The Main Threat", "title": "Manipulation of the running variable",
         "blocks": [
             {"t": "body", "html": "RD fails if people can <strong>precisely manipulate</strong> "
              "which side of the cutoff they land on &mdash; an examiner nudging a 59 to a 61, a "
              "household mis-reporting assets to qualify."},
             {"t": "hbox", "color": "amber", "html": "Diagnostic: check for <strong>bunching</strong> "
              "&mdash; a suspicious pile-up of cases just on the favourable side of the cutoff "
              "(a McCrary density test). Smoothness across the threshold is the credibility test."},
         ]},

        {"type": "content", "label": "Practical Choices", "title": "Bandwidth and functional form",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Bandwidth:</strong> how wide a window around the cutoff to use &mdash; "
                 "narrow is cleaner but noisier",
                 "<strong>Functional form:</strong> fit flexible curves each side; beware "
                 "high-order polynomials that invent jumps",
                 "<strong>Covariate smoothness:</strong> other variables should NOT jump at the "
                 "cutoff &mdash; a useful placebo check"]},
             {"t": "hbox", "color": "cyan", "html": "Good RD work shows the estimate is robust to "
              "the bandwidth choice, not an artefact of one window."},
         ]},

        {"type": "content", "label": "Where RD Fits", "title": "RD in development practice",
         "blocks": [
             {"t": "body", "html": "RD is ideal wherever eligibility hinges on a score or "
              "threshold: poverty-line targeting (BPL cutoffs, SECC deprivation scores), "
              "exam-based scholarships, population thresholds that trigger a facility or grant."},
             {"t": "hbox", "color": "green", "html": "Because eligibility rules are everywhere in "
              "Indian welfare programmes, RD is often the most natural &mdash; and most credible "
              "&mdash; design available to an evaluator."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Panel Data &amp; Fixed Effects"},

        {"type": "content", "label": "Following Units Over Time", "title": "What panel data buys you",
         "blocks": [
             {"t": "body", "html": "<strong>Panel data</strong> tracks the <em>same</em> units "
              "&mdash; households, districts, firms &mdash; across multiple periods. This repeated "
              "observation lets us net out stable, unchanging differences between units."},
             {"t": "term", "word": "Panel (longitudinal) data",
              "def": "Data on the same set of units observed at two or more points in time, "
              "combining a cross-section with a time dimension."},
         ]},

        {"type": "content", "label": "The Core Trick", "title": "Each unit becomes its own control",
         "blocks": [
             {"t": "body", "html": "With <strong>fixed effects</strong>, we compare each unit "
              "<em>to itself</em> over time. Anything about the unit that stays constant &mdash; "
              "and so cannot explain <em>changes</em> &mdash; is swept out of the comparison."},
             {"t": "raw", "html": "<div style='font-family:monospace;font-size:1.0em;text-align:center;"
              "background:rgba(14,165,233,0.08);border:1px solid rgba(14,165,233,0.35);"
              "border-radius:10px;padding:18px;'>"
              "Y&#7522;&#8348; = &beta;X&#7522;&#8348; + &alpha;&#7522; + &delta;&#8348; + &epsilon;&#7522;&#8348;<br>"
              "<span style='font-size:0.8em;opacity:0.8'>&alpha;&#7522; = unit fixed effect&nbsp;&nbsp;"
              "&delta;&#8348; = time fixed effect</span></div>"},
         ]},

        {"type": "content", "label": "The Within Estimator", "title": "Fixed effects use within-unit variation",
         "blocks": [
             {"t": "body", "html": "The fixed-effects (or <strong>within</strong>) estimator "
              "subtracts each unit's own average from every observation, so &beta; is identified "
              "<em>only</em> from how a unit changes relative to itself over time."},
             {"t": "hbox", "color": "green", "html": "Differences <em>between</em> units &mdash; "
              "rich vs poor district, fertile vs arid land &mdash; are discarded. Only the "
              "within-unit story remains, and that is what removes time-invariant confounders."},
         ]},

        {"type": "content", "label": "The Crucial Limit", "title": "Fixed effects remove only TIME-INVARIANT confounders",
         "blocks": [
             {"t": "body", "html": "Unit fixed effects control for everything about a unit that is "
              "<strong>constant over time</strong> &mdash; geography, culture, fixed institutions "
              "&mdash; even if you never measured it."},
             {"t": "hbox", "color": "red", "html": "<strong>Critical caveat:</strong> they do "
              "<em>nothing</em> about confounders that <strong>change over time</strong>. A "
              "district-specific shock that moves with the treatment will still bias &beta;. "
              "Fixed effects are not a magic exogeneity machine."},
         ]},

        {"type": "content", "label": "Fixed vs Random Effects", "title": "Two ways to model the unit term",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Fixed effects", "Random effects"],
              "rows": [
                  ["Assumes", "Unit term may correlate with X", "Unit term uncorrelated with X"],
                  ["Uses", "Within-unit variation only", "Within + between variation"],
                  ["Robust to", "Time-invariant confounding", "More efficient if assumption holds"],
                  ["Safer when", "You fear omitted unit traits", "Strong, often unrealistic"]]},
             {"t": "hbox", "color": "amber", "html": "For causal work where you worry about "
              "unobserved unit traits, <strong>fixed effects</strong> is usually the safer "
              "default &mdash; it makes the weaker assumption."},
         ]},

        {"type": "content", "label": "First Differences", "title": "A close cousin: differencing",
         "blocks": [
             {"t": "body", "html": "With two periods, <strong>first-differencing</strong> &mdash; "
              "regressing the <em>change</em> in Y on the <em>change</em> in X &mdash; removes the "
              "fixed unit term just as fixed effects do. (DiD is exactly this idea with a "
              "comparison group.)"},
             {"t": "hbox", "color": "cyan", "html": "Fixed effects, first differences and DiD are "
              "a family: all exploit repeated observation to subtract away stable, unobserved "
              "differences between units."},
         ]},

        {"type": "content", "label": "Standard Errors", "title": "Why you must cluster",
         "blocks": [
             {"t": "body", "html": "In panel data, a unit's observations are <strong>correlated "
              "across time</strong> &mdash; this year looks like last year. Ignoring that makes "
              "standard errors far too small and 'significance' spurious."},
             {"t": "hbox", "color": "red", "html": "Fix: <strong>cluster the standard errors</strong> "
              "at the unit level (e.g. by district or village). Clustering acknowledges that "
              "observations within a group are not independent &mdash; honest uncertainty, not "
              "inflated confidence."},
         ]},

        {"type": "content", "label": "Reading Panel Work", "title": "Questions for a fixed-effects study",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Are <strong>both</strong> unit and time fixed effects included where needed?",
                 "Could a <strong>time-varying</strong> confounder still drive the result?",
                 "Are standard errors <strong>clustered</strong> at the right level?",
                 "Is &beta; identified from credible within-unit variation, or a few odd cases?"]},
             {"t": "hbox", "color": "cyan", "html": "Fixed effects buy a lot &mdash; but remember "
              "what they cannot buy: protection from confounders that move over time."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Reading &amp; Critiquing Results"},

        {"type": "content", "label": "Uncertainty", "title": "Standard errors quantify sampling noise",
         "blocks": [
             {"t": "term", "word": "Standard error",
              "def": "A measure of how much an estimate would vary across repeated random samples. "
              "It quantifies <em>sampling uncertainty</em> &mdash; how precisely the effect is "
              "pinned down &mdash; not whether the design is valid."},
             {"t": "hbox", "color": "amber", "html": "A small standard error says the number is "
              "<em>precise</em>. It says nothing about whether the number is <em>right</em> &mdash; "
              "a biased design gives precisely wrong answers."},
         ]},

        {"type": "content", "label": "Confidence Intervals", "title": "Report a range, not just a point",
         "blocks": [
             {"t": "body", "html": "A coefficient of 0.12 is shorthand. The honest version is a "
              "<strong>confidence interval</strong> &mdash; say [0.04, 0.20] &mdash; the range of "
              "effects consistent with the data at, usually, 95% confidence."},
             {"t": "hbox", "color": "cyan", "html": "If a 95% interval comfortably includes zero, "
              "the data cannot rule out 'no effect'. Always read the interval, not just the "
              "point estimate or the stars."},
         ]},

        {"type": "content", "label": "See It", "title": "Same point estimate, very different certainty",
         "blocks": [
             {"t": "chart", "canvas": "ciChart",
              "title": "Three studies, all estimating a +4-point effect (95% intervals)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["Study A (large n)", "Study B (medium n)", "Study C (small n)"],
                       "datasets": [
                           {"label": "Lower bound", "data": [3.0, 1.0, -3.0],
                            "backgroundColor": "rgba(0,0,0,0)"},
                           {"label": "Interval width", "data": [2.0, 6.0, 14.0],
                            "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ stacked:true, title:{display:true,text:'Effect (percentage points)'} }, y:{ stacked:true } } }"}},
             {"t": "hbox", "color": "amber", "html": "All three centre on +4, but only Study A "
              "rules out zero. Study C's interval spans negative values &mdash; its 'effect' is "
              "indistinguishable from no effect. The point estimate alone hides this."},
         ]},

        {"type": "content", "label": "Significance", "title": "What a p-value does &mdash; and doesn't &mdash; say",
         "blocks": [
             {"t": "term", "word": "p-value",
              "def": "The probability of seeing an estimate at least this extreme if the true "
              "effect were zero. A small p-value means the result is unlikely under 'no effect' "
              "&mdash; nothing more."},
             {"t": "hbox", "color": "red", "html": "Statistically significant &ne; large, "
              "important, or causally valid. With a big sample a trivial effect can be "
              "'significant'. Always ask: how <em>big</em> is the effect, and from a <em>credible "
              "design</em>?"},
         ]},

        {"type": "content", "label": "Effect Size", "title": "Is the effect big enough to matter?",
         "blocks": [
             {"t": "body", "html": "An effect can be real, precise and significant &mdash; yet too "
              "small to justify the cost. Always translate a coefficient into something a "
              "decision-maker feels: rupees, percentage points, children, school days."},
             {"t": "hbox", "color": "amber", "html": "Pair statistical significance with "
              "<strong>practical significance</strong> and a cost comparison. 'Significant' is the "
              "start of the conversation, not the end."},
         ]},

        {"type": "content", "label": "Robustness", "title": "Does the result survive poking?",
         "blocks": [
             {"t": "bullets", "items": [
                 "Does the estimate hold across <strong>alternative specifications</strong> and "
                 "control sets?",
                 "Does it survive different samples, sub-groups and outlier handling?",
                 "Are there <strong>placebo tests</strong> that should find nothing &mdash; and do?",
                 "Do the authors show the result is not knife-edge on one choice?"]},
             {"t": "hbox", "color": "cyan", "html": "A finding that appears only under one precise "
              "specification is fragile. Credible results are robust ones."},
         ]},

        {"type": "content", "label": "p-hacking", "title": "The garden of forking paths",
         "blocks": [
             {"t": "body", "html": "Try enough specifications, subgroups and outcomes and some "
              "will cross p &lt; 0.05 <em>by chance</em>. Reporting only those &mdash; "
              "<strong>p-hacking</strong> &mdash; manufactures false findings that will not "
              "replicate."},
             {"t": "hbox", "color": "red", "html": "Be wary of a lone 'significant' subgroup, an "
              "oddly specific specification, or many outcomes with one star. Ask what was tested "
              "but <em>not</em> reported."},
         ]},

        {"type": "content", "label": "Pre-registration", "title": "Tie your hands in advance",
         "blocks": [
             {"t": "body", "html": "A <strong>pre-analysis plan</strong> &mdash; specifying "
              "hypotheses, outcomes and methods <em>before</em> seeing the data &mdash; removes "
              "the freedom to fish. Registries (e.g. the AEA RCT Registry) make the commitment "
              "public."},
             {"t": "hbox", "color": "green", "html": "Pre-registration cannot make a bad design "
              "good, but it makes an honest design <em>credible</em> &mdash; readers know the "
              "result was not cherry-picked after the fact."},
         ]},

        {"type": "content", "label": "External Validity", "title": "Will it travel?",
         "blocks": [
             {"t": "body", "html": "A clean estimate is internally valid <em>for its setting</em>. "
              "Whether it generalises &mdash; to another state, scale, time or population &mdash; "
              "is <strong>external validity</strong>, a separate and often harder question."},
             {"t": "hbox", "color": "amber", "html": "Ask: what was the context and the sample? "
              "Would the mechanism plausibly work elsewhere? Scaling up can itself change the "
              "effect (general-equilibrium and implementation effects)."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Tools &amp; Further Reading"},

        {"type": "content", "label": "Software", "title": "What practitioners actually use",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Good for", "Note"],
              "rows": [
                  ["Stata", "Applied micro-econometrics, panel, IV, RD", "Industry standard; paid"],
                  ["R", "Free, flexible, reproducible analysis &amp; graphics", "Rich causal-inference packages"],
                  ["Python (statsmodels, linearmodels)", "Automation, large data, ML", "Free, general-purpose"],
                  ["Excel / Sheets", "Quick description, not inference", "Fine to start; outgrow it"]]},
             {"t": "hbox", "color": "cyan", "html": "The software matters far less than the "
              "<strong>research design</strong>. A clean design in Excel beats a flawed one in "
              "Stata."},
         ]},

        {"type": "content", "label": "Method Cheat-Sheet", "title": "Which design for which situation?",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["If you can&hellip;", "Use", "Key assumption"],
              "rows": [
                  ["Randomise treatment", "RCT", "Successful randomisation"],
                  ["Find an as-good-as-random nudge", "IV", "Relevance + exclusion"],
                  ["Compare a treated &amp; untreated group over time", "DiD", "Parallel trends"],
                  ["Exploit a cutoff rule", "RD", "No manipulation at cutoff"],
                  ["Follow units over time", "Panel fixed effects", "Confounders time-invariant"]]},
             {"t": "hbox", "color": "green", "html": "Start from the <em>variation you have</em>, "
              "then pick the design &mdash; not the other way round."},
         ]},

        {"type": "content", "label": "The Essential Books", "title": "Angrist &amp; Pischke",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Mostly Harmless Econometrics</em> &mdash; Angrist &amp; Pischke (the "
                 "design-based bible; RCT, IV, DiD, RD)",
                 "<em>Mastering 'Metrics</em> &mdash; Angrist &amp; Pischke (gentler, intuitive "
                 "introduction &mdash; start here)",
                 "<em>Causal Inference: The Mixtape</em> &mdash; Scott Cunningham (free online, "
                 "code-rich)"]},
             {"t": "hbox", "color": "cyan", "html": "If you read one book, read <strong>Mastering "
              "'Metrics</strong>. It teaches the five core designs in this course with humour and "
              "real studies."},
         ]},

        {"type": "content", "label": "Development Reading", "title": "Evidence in development",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Poor Economics</em> &mdash; Banerjee &amp; Duflo (RCTs and the lives of the "
                 "poor)",
                 "<em>Running Randomized Evaluations</em> &mdash; Glennerster &amp; Takavarasha "
                 "(a practical RCT field guide)",
                 "J-PAL &amp; Innovations for Poverty Action (IPA) &mdash; policy briefs and "
                 "evidence syntheses"]},
             {"t": "hbox", "color": "green", "html": "Read the <em>methods</em> section of real "
              "studies critically &mdash; it is the fastest way to internalise the ideas in this "
              "deck."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Always ask 'compared to what?'</strong> &mdash; causation needs a "
                 "counterfactual",
                 "<strong>Correlation is not causation</strong> &mdash; suspect selection and "
                 "confounding first",
                 "<strong>Design beats adjustment</strong> &mdash; RCT, IV, DiD, RD, fixed "
                 "effects each build a comparison",
                 "<strong>Every method has ONE load-bearing assumption</strong> &mdash; know it, "
                 "and interrogate it",
                 "<strong>Read the standard errors and the robustness</strong> &mdash; precise is "
                 "not the same as right"]},
         ]},

        {"type": "content", "label": "Where Next", "title": "Keep building",
         "blocks": [
             {"t": "body", "html": "Econometrics is learned by doing. Take a real Indian dataset, "
              "pose a causal question, and ask which design its variation can support &mdash; then "
              "stress-test the assumption that design relies on."},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Impact Evaluation</strong> and "
              "<strong>Exploratory Data Analysis</strong> 101 courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Econometrics 101 &middot; Complete",
         "headline": "Now go ask<br>'compared to what?'",
         "byline": "Every credible causal claim rests on a counterfactual and one load-bearing "
                   "assumption. You now know the five core designs and how to interrogate each "
                   "one. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
