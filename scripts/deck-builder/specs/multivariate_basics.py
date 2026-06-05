# -*- coding: utf-8 -*-
"""
Multivariate Analysis 101 — ImpactMojo 101 Series (native deck spec)
Multiple regression and friends for South Asian development practitioners.
Build: python3 scripts/deck-builder/build.py multivariate_basics
"""

DECK = {
    "slug": "multivariate-basics",
    "title": "Multivariate Analysis 101",
    "description": ("Multivariate Analysis 101 — a free foundational course for development "
                    "practitioners and analysts in South Asia. From bivariate to multiple "
                    "regression: controlling for confounders, reading coefficients, model fit, "
                    "diagnostics, multicollinearity, interactions, logistic regression and the "
                    "NFHS wealth index via PCA. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Multivariate<br>Analysis<br>101",
         "sub": "Controlling for Several Things at Once &mdash; Multiple Regression and Its "
                "Cousins for Development Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "From Bivariate to Multivariate"},
             {"name": "Multiple Linear Regression"},
             {"name": "Interpreting Coefficients"},
             {"name": "Model Fit &amp; Inference"},
             {"name": "Assumptions &amp; Residual Diagnostics"},
             {"name": "Multicollinearity"},
             {"name": "Interactions &amp; Non-Linearity"},
             {"name": "Logistic Regression"},
             {"name": "Data Reduction &mdash; PCA &amp; Factor Analysis"},
             {"name": "Pitfalls"},
             {"name": "Reporting &amp; Tools"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "From Bivariate to Multivariate"},

        {"type": "content", "label": "Starting Point", "title": "One outcome, one predictor",
         "blocks": [
             {"t": "body", "html": "<strong>Bivariate analysis</strong> looks at two variables at "
              "a time: child stunting and household income; learning scores and class size. A "
              "simple regression or correlation summarises how they move together."},
             {"t": "term", "word": "Bivariate",
              "def": "An analysis of the relationship between exactly two variables &mdash; one "
              "outcome and one predictor &mdash; with nothing else held constant."},
             {"t": "hbox", "color": "cyan", "html": "The trouble: in the real world, almost "
              "nothing varies one at a time. Income, education, caste and location all move "
              "together."},
         ]},

        {"type": "content", "label": "The Real World", "title": "Outcomes have many causes at once",
         "blocks": [
             {"t": "body", "html": "Whether a child is stunted depends on income, the mother's "
              "education, sanitation, diet, birth order and more &mdash; <em>simultaneously</em>. "
              "Look at any one in isolation and you mix up its effect with all the others."},
             {"t": "flow", "steps": [
                 "Mother's education",
                 "Household income",
                 "Sanitation &amp; water",
                 "&rarr; Child stunting"]},
             {"t": "hbox", "color": "amber", "html": "Multivariate analysis is simply analysis "
              "that handles several predictors at the same time."},
         ]},

        {"type": "content", "label": "The Core Problem", "title": "Confounding: the lurking variable",
         "blocks": [
             {"t": "term", "word": "Confounder",
              "def": "A variable that influences both the predictor and the outcome, creating a "
              "misleading association between them when it is left out of the analysis."},
             {"t": "body", "html": "Districts with more private clinics may show <em>worse</em> "
              "average health &mdash; not because clinics harm anyone, but because clinics open "
              "where the population is older and sicker. Age confounds the clinic&ndash;health link."},
         ]},

        {"type": "content", "label": "See It", "title": "Why a raw comparison misleads",
         "blocks": [
             {"t": "body", "html": "Suppose richer households both eat more diverse diets "
              "<em>and</em> have less stunting. A bivariate look at 'diet diversity vs stunting' "
              "credits diet with the whole gap &mdash; part of which is really just income."},
             {"t": "flow", "steps": [
                 "Income (confounder)",
                 "raises diet diversity",
                 "AND lowers stunting",
                 "&rarr; diet looks more powerful than it is"]},
             {"t": "hbox", "color": "red", "html": "Without controlling for income, the diet "
              "coefficient is biased. This is the problem multivariate analysis exists to solve."},
         ]},

        {"type": "content", "label": "The Fix", "title": "'Holding other variables constant'",
         "blocks": [
             {"t": "body", "html": "Multiple regression estimates the effect of each predictor "
              "<strong>while statistically holding the others fixed</strong> &mdash; comparing "
              "households that differ in diet but have the <em>same</em> income, education and "
              "sanitation."},
             {"t": "hbox", "color": "cyan", "html": "This is the single most important idea in the "
              "course. A multivariate coefficient is a <em>partial</em> effect: the contribution "
              "of one variable, net of the others in the model."},
         ]},

        {"type": "content", "label": "Caveat", "title": "Control is not the same as causation",
         "blocks": [
             {"t": "body", "html": "Holding observed variables constant removes <em>those</em> "
              "confounders &mdash; but only those. Anything you did not measure (motivation, "
              "local prices, unobserved health) can still bias the estimate."},
             {"t": "hbox", "color": "amber", "html": "Controlling for what you can measure is "
              "necessary but not sufficient for causal claims. Keep your conclusions honest about "
              "what remains unobserved."},
         ]},

        {"type": "content", "label": "Vocabulary", "title": "The words analysts use",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Term", "Also called", "Meaning"],
              "rows": [
                  ["Outcome", "Dependent variable, Y", "What you are trying to explain"],
                  ["Predictor", "Independent variable, X, covariate", "What you use to explain it"],
                  ["Coefficient", "Slope, &beta;", "Effect of a predictor on the outcome"],
                  ["Control", "Adjust for, condition on", "Hold a variable constant"],
                  ["Residual", "Error, e", "What the model fails to predict"]]},
             {"t": "hbox", "color": "cyan", "html": "We will use 'predictor' and 'covariate' "
              "interchangeably; both just mean a right-hand-side variable."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "Where this course goes",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The workhorse", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Multiple linear regression",
                      "Reading coefficients correctly",
                      "Model fit, inference, diagnostics"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Beyond the basics", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Interactions and non-linearity",
                      "Logistic regression for yes/no outcomes",
                      "PCA &amp; factor analysis; pitfalls; tools"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Examples lean on NFHS, PLFS and the kind of "
              "data you actually meet at work."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Multiple Linear Regression"},

        {"type": "content", "label": "The Model", "title": "Predicting Y from several Xs",
         "blocks": [
             {"t": "body", "html": "Multiple linear regression models the outcome as a straight-"
              "line combination of predictors plus an error term:"},
             {"t": "title", "size": "sm",
              "html": "Y = &beta;<sub>0</sub> + &beta;<sub>1</sub>X<sub>1</sub> + "
              "&beta;<sub>2</sub>X<sub>2</sub> + &hellip; + &beta;<sub>k</sub>X<sub>k</sub> + e",
              "style": "text-align:center;font-family:monospace"},
             {"t": "hbox", "color": "cyan", "html": "It is the same machinery as simple "
              "regression &mdash; just with several Xs at once. Everything that follows builds on "
              "this one line."},
         ]},

        {"type": "content", "label": "The Pieces", "title": "What each symbol means",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Symbol", "Name", "What it is"],
              "rows": [
                  ["Y", "Outcome", "What you predict (e.g. test score)"],
                  ["&beta;<sub>0</sub>", "Intercept", "Predicted Y when every X = 0"],
                  ["&beta;<sub>1</sub>&hellip;&beta;<sub>k</sub>", "Slope coefficients",
                   "Partial effect of each predictor"],
                  ["X<sub>1</sub>&hellip;X<sub>k</sub>", "Predictors", "Your covariates"],
                  ["e", "Error / residual", "Everything the model misses"]]},
             {"t": "hbox", "color": "amber", "html": "The intercept is rarely interesting on its "
              "own &mdash; 'all Xs = 0' is often impossible (a household with zero adults). The "
              "slopes carry the story."},
         ]},

        {"type": "content", "label": "Worked Setup", "title": "An example we will reuse",
         "blocks": [
             {"t": "body", "html": "Suppose we model a child's <strong>height-for-age z-score</strong> "
              "(an anthropometric outcome) on three predictors:"},
             {"t": "title", "size": "sm",
              "html": "HAZ = &beta;<sub>0</sub> + &beta;<sub>1</sub>(income) + "
              "&beta;<sub>2</sub>(mother's years of schooling) + &beta;<sub>3</sub>(improved toilet) + e",
              "style": "text-align:center;font-family:monospace"},
             {"t": "hbox", "color": "amber", "html": "All coefficients in this deck are "
              "<strong>illustrative</strong> &mdash; chosen to teach interpretation, not reported "
              "as real NFHS findings."},
         ]},

        {"type": "content", "label": "The Geometry", "title": "Fitting a plane, not a line",
         "blocks": [
             {"t": "body", "html": "With one predictor, regression fits a <em>line</em> through a "
              "cloud of points. With two predictors, it fits a <em>plane</em>; with many, a "
              "hyper-plane you cannot draw. The idea is unchanged: find the surface closest to the "
              "data."},
             {"t": "hbox", "color": "cyan", "html": "'Closest' has a precise meaning &mdash; the "
              "surface that makes the prediction errors as small as possible, in a specific sense."},
         ]},

        {"type": "content", "label": "How It's Fit", "title": "Ordinary least squares (OLS)",
         "blocks": [
             {"t": "term", "word": "Ordinary least squares",
              "def": "The method that chooses the coefficients minimising the sum of the squared "
              "residuals &mdash; the squared vertical gaps between each observed Y and the value "
              "the model predicts."},
             {"t": "body", "html": "Squaring the residuals penalises big misses heavily and treats "
              "over- and under-prediction symmetrically. The software solves it instantly; your "
              "job is to set up and read the model well."},
         ]},

        {"type": "content", "label": "Key Idea", "title": "Each slope is a partial effect",
         "blocks": [
             {"t": "body", "html": "In our HAZ model, &beta;<sub>2</sub> is the change in "
              "height-for-age associated with <strong>one more year of the mother's schooling</strong>, "
              "<em>holding income and toilet access constant</em>."},
             {"t": "hbox", "color": "green", "html": "Compared with a bivariate estimate, the "
              "multivariate slope strips out the part of schooling's apparent effect that was "
              "really income or sanitation in disguise."},
         ]},

        {"type": "content", "label": "Fitted vs Residual", "title": "Prediction = signal + leftover",
         "blocks": [
             {"t": "body", "html": "For each child the model gives a <strong>fitted value</strong> "
              "(its best guess of HAZ) and a <strong>residual</strong> (observed &minus; fitted). "
              "The residual is what the predictors could not explain."},
             {"t": "flow", "steps": [
                 "Observed Y",
                 "&minus; Fitted Y (the model's guess)",
                 "= Residual (the leftover)",
                 "&rarr; diagnostics live in the residuals"]},
         ]},

        {"type": "content", "label": "Why Linear First", "title": "Start simple, then complicate",
         "blocks": [
             {"t": "body", "html": "Linear regression is the default workhorse because it is "
              "transparent, fast, and surprisingly flexible &mdash; you can add interactions, "
              "squared terms and log transforms without leaving the framework."},
             {"t": "hbox", "color": "cyan", "html": "Master the linear model and you have the "
              "scaffolding for almost every method that follows, including logistic regression."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Interpreting Coefficients"},

        {"type": "content", "label": "The Golden Sentence", "title": "How to read any coefficient",
         "blocks": [
             {"t": "body", "html": "Read every slope with one template: <em>'A one-unit increase "
              "in X is associated with a &beta;-unit change in Y, holding the other variables "
              "constant.'</em>"},
             {"t": "hbox", "color": "cyan", "html": "Get this sentence right and most "
              "interpretation errors vanish. The three load-bearing phrases are <strong>one-unit</strong>, "
              "<strong>associated with</strong>, and <strong>holding the others constant</strong>."},
         ]},

        {"type": "content", "label": "Units Matter", "title": "A coefficient is glued to its units",
         "blocks": [
             {"t": "body", "html": "If income is measured in <strong>rupees</strong>, "
              "&beta;<sub>income</sub> is the effect of one extra rupee &mdash; a tiny number. "
              "Measure income in <strong>thousands of rupees</strong> and the coefficient is 1,000 "
              "times larger. The relationship is identical; only the scale changed."},
             {"t": "hbox", "color": "amber", "html": "Always state units. A coefficient of '0.002' "
              "is meaningless until you know 0.002 of <em>what</em>, per <em>what</em>."},
         ]},

        {"type": "content", "label": "Continuous Predictors", "title": "Worked reading: a continuous X",
         "blocks": [
             {"t": "body", "html": "Illustrative result: &beta;<sub>schooling</sub> = "
              "<strong>0.06</strong> in our HAZ model."},
             {"t": "hbox", "color": "cyan", "html": "Read it as: 'Each additional year of the "
              "mother's schooling is associated with a <strong>0.06</strong> higher "
              "height-for-age z-score, holding income and toilet access constant.' Five extra "
              "years &asymp; 0.30 z-score."},
             {"t": "body", "cls": "sm", "html": "Illustrative figure &mdash; not a reported NFHS coefficient."},
         ]},

        {"type": "content", "label": "Dummy Variables", "title": "Encoding categories as 0/1",
         "blocks": [
             {"t": "term", "word": "Dummy variable",
              "def": "A 0/1 indicator standing for a category &mdash; e.g. improved toilet = 1, "
              "else 0. Its coefficient is the gap between that category and the baseline."},
             {"t": "body", "html": "For a dummy, 'a one-unit increase' simply means switching from "
              "0 to 1 &mdash; from the baseline group to the indicated group."},
         ]},

        {"type": "content", "label": "Baseline Categories", "title": "Every dummy needs something to compare to",
         "blocks": [
             {"t": "body", "html": "A categorical variable with <em>k</em> categories becomes "
              "<em>k&minus;1</em> dummies; the omitted one is the <strong>baseline</strong>. For "
              "religion with Hindu/Muslim/Christian/Other, if 'Hindu' is omitted, each coefficient "
              "is that group's gap <em>relative to Hindu</em>."},
             {"t": "hbox", "color": "red", "html": "Never interpret a dummy without naming the "
              "baseline. '&beta; = &minus;0.4 for urban' means nothing until you know it is "
              "relative to rural."},
         ]},

        {"type": "content", "label": "Dummy Example", "title": "Reading a 0/1 coefficient",
         "blocks": [
             {"t": "body", "html": "Illustrative result: &beta;<sub>improved&nbsp;toilet</sub> = "
              "<strong>0.18</strong> (baseline = no improved toilet)."},
             {"t": "hbox", "color": "cyan", "html": "Read it as: 'Children in households with an "
              "improved toilet have, on average, a <strong>0.18</strong> higher height-for-age "
              "z-score than otherwise-similar children without one.' The phrase "
              "'otherwise-similar' is the controls doing their work."},
             {"t": "body", "cls": "sm", "html": "Illustrative figure."},
         ]},

        {"type": "content", "label": "Standardised", "title": "Unstandardised vs standardised coefficients",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Unstandardised (b)", "Standardised (&beta;)"],
              "rows": [
                  ["Units", "Original (rupees, years)", "Standard deviations"],
                  ["Reads as", "Effect of 1 real unit", "Effect of a 1-SD change"],
                  ["Comparable across Xs?", "No &mdash; different scales", "Yes &mdash; common scale"],
                  ["Best for", "Real-world meaning", "Ranking relative importance"]]},
             {"t": "hbox", "color": "amber", "html": "Standardised coefficients let you ask 'which "
              "predictor matters most?' &mdash; but lose the plain-language 'per rupee' meaning. "
              "Report unstandardised for interpretation, standardised for comparison."},
         ]},

        {"type": "content", "label": "Sign &amp; Size", "title": "Direction first, then magnitude",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Sign:</strong> + means Y rises with X; &minus; means Y falls as X rises",
                 "<strong>Size:</strong> how much Y moves per unit of X &mdash; in context",
                 "<strong>Always ask 'is this big?'</strong> &mdash; a 0.02 z-score gain may be "
                 "real but trivial; a 0.4 gain may be programme-changing"]},
             {"t": "hbox", "color": "cyan", "html": "A coefficient is not 'important' just because "
              "it is non-zero. Judge magnitude against what would matter for your decision."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Model Fit &amp; Inference"},

        {"type": "content", "label": "How Good Is the Fit?", "title": "R&sup2;: variance explained",
         "blocks": [
             {"t": "term", "word": "R&sup2; (R-squared)",
              "def": "The share of the variation in the outcome that the model's predictors "
              "explain &mdash; ranging from 0 (explains nothing) to 1 (explains everything)."},
             {"t": "body", "html": "An R&sup2; of 0.34 means the predictors account for 34% of the "
              "variation in the outcome; the other 66% is residual &mdash; unmeasured causes and noise."},
         ]},

        {"type": "content", "label": "See It", "title": "R&sup2; as a slice of total variation",
         "blocks": [
             {"t": "chart", "canvas": "r2Doughnut",
              "title": "Variation in the outcome: explained vs unexplained (illustrative)",
              "source": "Illustrative",
              "type": "doughnut",
              "data": {"labels": ["Explained by model (R&sup2; = 34%)", "Unexplained (residual)"],
                       "datasets": [{"data": [34, 66],
                                     "backgroundColor": ["#10B981", "#1f2937"]}]},
              "options": {"__js__": "{ plugins:{ legend:{ position:'bottom' } } }"}},
             {"t": "hbox", "color": "amber", "html": "In social data, R&sup2; values of 0.1&ndash;0.4 "
              "are common and not shameful &mdash; human behaviour is genuinely noisy. A high "
              "R&sup2; is not the goal; an honest, well-specified model is."},
         ]},

        {"type": "content", "label": "The Catch", "title": "R&sup2; only ever goes up",
         "blocks": [
             {"t": "body", "html": "Add <em>any</em> predictor &mdash; even random noise &mdash; "
              "and R&sup2; will rise or stay flat; it can never fall. So a bigger R&sup2; does not "
              "prove the new variable belongs in the model."},
             {"t": "hbox", "color": "red", "html": "Chasing R&sup2; by piling in predictors is a "
              "recipe for overfitting. You need a measure that <em>penalises</em> needless "
              "complexity."},
         ]},

        {"type": "content", "label": "The Fix", "title": "Adjusted R&sup2;",
         "blocks": [
             {"t": "term", "word": "Adjusted R&sup2;",
              "def": "A version of R&sup2; that penalises each extra predictor. It rises only when "
              "a new variable improves the model by more than chance would predict &mdash; and can "
              "fall when you add a useless one."},
             {"t": "hbox", "color": "green", "html": "Compare models on <strong>adjusted</strong> "
              "R&sup2;, not raw R&sup2;. If adjusted R&sup2; drops when you add a variable, that "
              "variable is earning its place by less than it costs."},
         ]},

        {"type": "content", "label": "Is the Model Worth Anything?", "title": "The F-test",
         "blocks": [
             {"t": "body", "html": "The <strong>F-test</strong> asks a whole-model question: do "
              "the predictors <em>together</em> explain more than nothing? Its null hypothesis is "
              "that <em>all</em> slope coefficients are zero at once."},
             {"t": "hbox", "color": "cyan", "html": "A small F-test p-value says 'this model beats "
              "a model with no predictors'. It does not tell you <em>which</em> predictor matters "
              "&mdash; that is the t-tests' job."},
         ]},

        {"type": "content", "label": "Is This Predictor Real?", "title": "t-tests on each coefficient",
         "blocks": [
             {"t": "body", "html": "Each coefficient gets its own <strong>t-test</strong>: is this "
              "particular slope distinguishable from zero, given its uncertainty? The output is a "
              "<em>t-statistic</em> and a <em>p-value</em> per predictor."},
             {"t": "term", "word": "Standard error",
              "def": "The estimated uncertainty in a coefficient. t = coefficient &divide; standard "
              "error; a large t (small p) means the slope is unlikely to be zero by chance."},
         ]},

        {"type": "content", "label": "The Honest Range", "title": "Confidence intervals beat stars",
         "blocks": [
             {"t": "body", "html": "A coefficient of 0.06 with a 95% confidence interval of "
              "<strong>0.02 to 0.10</strong> says the plausible effect lies in that band. The "
              "interval shows both direction <em>and</em> precision &mdash; far more than a lone "
              "p-value or a row of asterisks."},
             {"t": "hbox", "color": "amber", "html": "If a 95% interval comfortably excludes zero, "
              "the effect is 'significant' at the 5% level &mdash; but always read the width. A "
              "wide interval means you really do not know much."},
         ]},

        {"type": "content", "label": "See It", "title": "Coefficients with confidence intervals",
         "blocks": [
             {"t": "chart", "canvas": "coefForest",
              "title": "Illustrative coefficients on height-for-age, with 95% CIs",
              "source": "Illustrative &mdash; not reported NFHS estimates",
              "type": "bar",
              "data": {"labels": ["Income (per ₹1,000)", "Mother's schooling (per year)",
                                   "Improved toilet (vs none)"],
                       "datasets": [{"label": "Coefficient",
                                     "data": [0.03, 0.06, 0.18],
                                     "backgroundColor": ["#0EA5E9", "#6366F1", "#10B981"],
                                     "errorLo": [0.01, 0.02, 0.07],
                                     "errorHi": [0.05, 0.10, 0.29]}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{ legend:{ display:false } }, "
                          "scales:{ x:{ title:{ display:true, text:'Effect on HAZ z-score' }, "
                          "suggestedMin:0 } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Bars are the point estimates; the listed "
              "intervals (e.g. toilet: 0.07&ndash;0.29) are the 95% CIs. None crosses zero here, so "
              "each is 'significant' &mdash; but the toilet effect is the least precise."},
         ]},

        {"type": "content", "label": "Significance &ne; Importance", "title": "Statistically real, practically tiny",
         "blocks": [
             {"t": "body", "html": "With a large sample &mdash; and NFHS has hundreds of thousands "
              "of records &mdash; even a microscopic effect can be 'statistically significant'. "
              "Significance is about <em>certainty</em>, not <em>size</em>."},
             {"t": "hbox", "color": "red", "html": "Always report the effect size and its units "
              "alongside the p-value. 'Significant' answers 'is it real?', never 'does it matter?'"},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Assumptions &amp; Residual Diagnostics"},

        {"type": "content", "label": "The Fine Print", "title": "OLS rests on assumptions",
         "blocks": [
             {"t": "body", "html": "Least-squares estimates are trustworthy only if a few "
              "assumptions roughly hold. Violations do not always bias the coefficients, but they "
              "can wreck the standard errors &mdash; and so the p-values and intervals."},
             {"t": "hbox", "color": "cyan", "html": "Most assumptions are checked by looking at "
              "the <strong>residuals</strong> &mdash; the model's leftovers. Plotting them is "
              "non-negotiable."},
         ]},

        {"type": "content", "label": "The Four", "title": "What linear regression assumes",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Assumption", "Plain meaning", "Check with"],
              "rows": [
                  ["Linearity", "The true relationship is a straight line", "Residual vs fitted plot"],
                  ["Independence", "Observations don't lean on each other", "Study design; clustering"],
                  ["Homoscedasticity", "Error spread is constant across X", "Residual vs fitted plot"],
                  ["Normal residuals", "Errors are roughly bell-shaped", "Q&ndash;Q plot, histogram"]]},
             {"t": "hbox", "color": "amber", "html": "Note what is <em>not</em> required: the "
              "predictors themselves need not be normal, and Y need not be normal &mdash; only the "
              "residuals."},
         ]},

        {"type": "content", "label": "Linearity", "title": "Is a straight line the right shape?",
         "blocks": [
             {"t": "body", "html": "If the real relationship curves &mdash; income's effect on "
              "nutrition flattening at high incomes &mdash; a straight-line model will "
              "systematically over- and under-predict in patterns."},
             {"t": "hbox", "color": "cyan", "html": "Diagnosis: plot residuals against fitted "
              "values. A curve or a smile in that plot says the linearity assumption is failing "
              "&mdash; consider a transform or a squared term (Section 7)."},
         ]},

        {"type": "content", "label": "Independence", "title": "When observations cluster",
         "blocks": [
             {"t": "body", "html": "Children in the same village share water, clinics and shocks, "
              "so their outcomes are correlated. Treating them as fully independent makes standard "
              "errors look <em>smaller</em> than they are &mdash; falsely confident results."},
             {"t": "hbox", "color": "red", "html": "Survey data like NFHS is clustered by design. "
              "Use clustered or survey-adjusted standard errors, or you will overstate significance."},
         ]},

        {"type": "content", "label": "Homoscedasticity", "title": "Constant error spread",
         "blocks": [
             {"t": "term", "word": "Homoscedasticity",
              "def": "The residuals have roughly the same spread across all fitted values. Its "
              "opposite, heteroscedasticity, is a fan or funnel shape in the residual plot."},
             {"t": "body", "html": "Income data is a classic offender: the rich vary far more in "
              "spending than the poor, so residuals widen as predicted spending rises. Coefficients "
              "stay unbiased, but the standard errors are wrong."},
         ]},

        {"type": "content", "label": "See It", "title": "Good residuals vs a heteroscedastic fan",
         "blocks": [
             {"t": "chart", "canvas": "residScatter",
              "title": "Residual vs fitted: even band (good) vs widening fan (bad)",
              "source": "Illustrative",
              "type": "scatter",
              "data": {"datasets": [
                  {"label": "Homoscedastic (good)",
                   "data": [{"x": 1, "y": 0.3}, {"x": 2, "y": -0.4}, {"x": 3, "y": 0.2},
                            {"x": 4, "y": -0.3}, {"x": 5, "y": 0.4}, {"x": 6, "y": -0.2},
                            {"x": 7, "y": 0.3}, {"x": 8, "y": -0.35}, {"x": 9, "y": 0.25}],
                   "backgroundColor": "#10B981", "pointRadius": 5},
                  {"label": "Heteroscedastic (bad)",
                   "data": [{"x": 1, "y": 0.1}, {"x": 2, "y": -0.2}, {"x": 3, "y": 0.5},
                            {"x": 4, "y": -0.6}, {"x": 5, "y": 1.1}, {"x": 6, "y": -1.3},
                            {"x": 7, "y": 1.8}, {"x": 8, "y": -2.0}, {"x": 9, "y": 2.4}],
                   "backgroundColor": "#EF4444", "pointRadius": 5}]},
              "options": {"__js__": "{ plugins:{ legend:{ position:'bottom' } }, "
                          "scales:{ x:{ title:{ display:true, text:'Fitted value' } }, "
                          "y:{ title:{ display:true, text:'Residual' } } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The green band stays flat; the red points fan "
              "out as the fitted value grows. The fan is the warning sign &mdash; reach for robust "
              "standard errors or a log transform."},
         ]},

        {"type": "content", "label": "Normal Residuals", "title": "The Q&ndash;Q plot",
         "blocks": [
             {"t": "body", "html": "Inference (t-tests, CIs) assumes the residuals are roughly "
              "normal. Check with a <strong>Q&ndash;Q plot</strong>: if the residuals are normal, "
              "the points hug the diagonal line; fat tails or skew show as departures at the ends."},
             {"t": "hbox", "color": "green", "html": "Good news: with a large sample, mild "
              "non-normality barely matters thanks to the central limit theorem. Worry most about "
              "it in small samples."},
         ]},

        {"type": "content", "label": "The Habit", "title": "Plot first, conclude later",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Residual vs fitted:</strong> checks linearity and equal spread at once",
                 "<strong>Q&ndash;Q plot:</strong> checks normality of residuals",
                 "<strong>Leverage / influence plot:</strong> finds the points bending the fit",
                 "<strong>Scale&ndash;location plot:</strong> a sharper look at spread"]},
             {"t": "hbox", "color": "amber", "html": "Anscombe's lesson applies here too: numbers "
              "alone hide trouble. Run the diagnostic plots on every model before you trust a "
              "single coefficient."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Multicollinearity"},

        {"type": "content", "label": "The Problem", "title": "When predictors overlap",
         "blocks": [
             {"t": "term", "word": "Multicollinearity",
              "def": "When two or more predictors are highly correlated with each other, so they "
              "carry overlapping information about the outcome."},
             {"t": "body", "html": "Household income, monthly expenditure and asset ownership all "
              "measure roughly the same thing &mdash; living standards. Put all three in a model "
              "and the regression struggles to separate their individual effects."},
         ]},

        {"type": "content", "label": "Why It Hurts", "title": "Unstable, imprecise coefficients",
         "blocks": [
             {"t": "body", "html": "When predictors overlap, the model cannot tell which one "
              "deserves the credit. The result: coefficients with <strong>huge standard errors</strong>, "
              "wild swings if you add or drop a variable, and sometimes nonsensical signs."},
             {"t": "hbox", "color": "red", "html": "Crucially, multicollinearity does <em>not</em> "
              "bias the coefficients &mdash; it makes them <em>imprecise</em>. The overall "
              "prediction can still be fine; the individual effects become untrustworthy."},
         ]},

        {"type": "content", "label": "The Symptoms", "title": "How to spot it",
         "blocks": [
             {"t": "bullets", "color": "amber", "items": [
                 "A high overall R&sup2; and significant F-test, but <em>no</em> individual "
                 "predictor is significant",
                 "Coefficients flip sign or size when you add/remove a variable",
                 "Implausibly large standard errors on variables you expected to matter",
                 "Predictors you know are related (income &amp; expenditure) are both in the model"]},
             {"t": "hbox", "color": "cyan", "html": "These symptoms point you toward a formal "
              "diagnostic &mdash; the variance inflation factor."},
         ]},

        {"type": "content", "label": "The Diagnostic", "title": "The Variance Inflation Factor (VIF)",
         "blocks": [
             {"t": "term", "word": "VIF",
              "def": "For each predictor, how much its coefficient's variance is inflated by "
              "correlation with the other predictors. VIF = 1 means no overlap; higher means more."},
             {"t": "body", "html": "It is computed by regressing each predictor on all the others. "
              "The more predictable a variable is from the rest, the higher its VIF &mdash; and the "
              "shakier its coefficient."},
         ]},

        {"type": "content", "label": "Rules of Thumb", "title": "How high is too high?",
         "blocks": [
             {"t": "chart", "canvas": "vifBar",
              "title": "Illustrative VIFs &mdash; expenditure &amp; income overlap badly",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["Mother's schooling", "Improved toilet", "Income", "Expenditure"],
                       "datasets": [{"label": "VIF",
                                     "data": [1.4, 1.8, 7.9, 8.3],
                                     "backgroundColor": ["#10B981", "#10B981", "#EF4444", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{ legend:{ display:false } }, "
                          "scales:{ y:{ title:{ display:true, text:'VIF' }, suggestedMax:10 } } }"}},
             {"t": "hbox", "color": "amber", "html": "Common rule of thumb: <strong>VIF above "
              "5&ndash;10 signals a problem.</strong> Here income and expenditure both blow past "
              "it &mdash; they are measuring the same underlying wealth."},
         ]},

        {"type": "content", "label": "The Remedies", "title": "What to do about it",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Remedy", "How", "When"],
              "rows": [
                  ["Drop one", "Remove a redundant predictor", "Two variables measure the same thing"],
                  ["Combine", "Build one index (e.g. PCA)", "Several proxies for one concept"],
                  ["Centre / rescale", "Subtract the mean before squaring/interacting", "Collinearity from interaction terms"],
                  ["Get more data", "Larger / more varied sample", "Overlap is mild, not structural"],
                  ["Accept it", "Keep the model, widen the CIs", "You only care about prediction"]]},
             {"t": "hbox", "color": "green", "html": "If two predictors are basically the same "
              "concept, do not agonise &mdash; keep one, or fold them into a single index. The "
              "wealth index in Section 9 is exactly this move."},
         ]},

        {"type": "content", "label": "A Subtlety", "title": "Don't 'fix' collinearity you need",
         "blocks": [
             {"t": "body", "html": "If two predictors are genuinely distinct concepts that happen "
              "to correlate &mdash; education and income &mdash; dropping one can <em>reintroduce</em> "
              "confounding. The cure may be worse than the disease."},
             {"t": "hbox", "color": "cyan", "html": "Decide based on your question. If you need "
              "the partial effect of education net of income, keep both and accept wider intervals "
              "rather than deleting a real confounder."},
         ]},

        {"type": "content", "label": "Recap", "title": "Multicollinearity in one breath",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "It is about predictors overlapping with <em>each other</em>, not with Y",
                 "It inflates standard errors; it does not bias coefficients",
                 "Diagnose with VIF (watch for &gt; 5&ndash;10) and unstable signs",
                 "Remedy by dropping, combining, or simply accepting wider uncertainty"]},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Interactions &amp; Non-Linearity"},

        {"type": "content", "label": "Beyond Straight Lines", "title": "When one slope isn't enough",
         "blocks": [
             {"t": "body", "html": "The plain model assumes each predictor's effect is the same "
              "for everyone and constant at every level. Reality is richer: effects can "
              "<em>depend on</em> other variables, or <em>change</em> as a variable grows."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Interaction", "blocks": [
                  {"t": "body", "cls": "sm", "html": "X's effect depends on another variable "
                   "(e.g. schooling helps more where toilets exist)."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Non-linearity", "blocks": [
                  {"t": "body", "cls": "sm", "html": "X's effect changes with its own level "
                   "(e.g. income matters more at the bottom)."}]}]},
         ]},

        {"type": "content", "label": "Interactions", "title": "An effect that depends on context",
         "blocks": [
             {"t": "term", "word": "Interaction term",
              "def": "A predictor formed by multiplying two variables (X1 &times; X2). Its "
              "coefficient captures how the effect of one variable changes across levels of the other."},
             {"t": "body", "html": "Model: HAZ = &hellip; + &beta;<sub>1</sub>(schooling) + "
              "&beta;<sub>2</sub>(toilet) + &beta;<sub>3</sub>(schooling &times; toilet). "
              "&beta;<sub>3</sub> tells you whether schooling's payoff differs for households with "
              "and without a toilet."},
         ]},

        {"type": "content", "label": "See It", "title": "Two slopes from one interaction",
         "blocks": [
             {"t": "chart", "canvas": "interactLine",
              "title": "Schooling's effect on HAZ, by toilet access (illustrative)",
              "source": "Illustrative",
              "type": "line",
              "data": {"labels": ["0", "3", "6", "9", "12"],
                       "datasets": [
                           {"label": "Improved toilet",
                            "data": [-1.0, -0.55, -0.10, 0.35, 0.80],
                            "borderColor": "#10B981", "backgroundColor": "#10B981",
                            "tension": 0, "pointRadius": 4, "fill": False},
                           {"label": "No improved toilet",
                            "data": [-1.4, -1.20, -1.00, -0.80, -0.60],
                            "borderColor": "#EF4444", "backgroundColor": "#EF4444",
                            "tension": 0, "pointRadius": 4, "fill": False}]},
              "options": {"__js__": "{ plugins:{ legend:{ position:'bottom' } }, "
                          "scales:{ x:{ title:{ display:true, text:\"Mother's years of schooling\" } }, "
                          "y:{ title:{ display:true, text:'Predicted HAZ' } } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The steeper green line means schooling helps "
              "more where sanitation is in place &mdash; an interaction. Two different slopes, one "
              "model. Without the interaction term you would force them to be parallel."},
         ]},

        {"type": "content", "label": "Reading Interactions", "title": "The main effect changes meaning",
         "blocks": [
             {"t": "body", "html": "Once you include X1&times;X2, the coefficient on X1 alone is "
              "no longer 'the effect of X1'. It is the effect of X1 <strong>when X2 = 0</strong>. "
              "The full effect of X1 is &beta;<sub>1</sub> + &beta;<sub>3</sub>&middot;X2."},
             {"t": "hbox", "color": "red", "html": "This trips people up constantly. In a model "
              "with interactions, never read a main-effect coefficient in isolation &mdash; always "
              "say 'at what level of the other variable?'"},
         ]},

        {"type": "content", "label": "Non-Linearity", "title": "Quadratic and polynomial terms",
         "blocks": [
             {"t": "body", "html": "Add a squared term &mdash; &beta;<sub>1</sub>X + "
              "&beta;<sub>2</sub>X&sup2; &mdash; to bend the line into a curve. This captures "
              "diminishing returns (income's effect flattening) or U-shapes (age and earnings)."},
             {"t": "hbox", "color": "amber", "html": "Centre X before squaring to tame the "
              "collinearity between X and X&sup2;, and resist going past a quadratic &mdash; high-"
              "order polynomials wiggle wildly and overfit."},
         ]},

        {"type": "content", "label": "Log Transforms", "title": "Taming skew, reading elasticities",
         "blocks": [
             {"t": "body", "html": "Logging a right-skewed variable like income compresses its long "
              "tail and often straightens a curved relationship. It also changes how you read the "
              "coefficient &mdash; in percentage terms."},
             {"t": "term", "word": "Elasticity",
              "def": "In a log&ndash;log model, the coefficient is an elasticity: the percentage "
              "change in Y for a 1% change in X. A coefficient of 0.4 means a 1% rise in X is "
              "linked to a 0.4% rise in Y."},
         ]},

        {"type": "content", "label": "Log Cheat-Sheet", "title": "Four ways logs change the reading",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Model", "Coefficient &beta; reads as&hellip;"],
              "rows": [
                  ["Y on X (level&ndash;level)", "&beta;-unit change in Y per 1-unit X"],
                  ["Y on log X (level&ndash;log)", "&beta;/100 change in Y per 1% rise in X"],
                  ["log Y on X (log&ndash;level)", "~100&middot;&beta; % change in Y per 1-unit X"],
                  ["log Y on log X (log&ndash;log)", "&beta; % change in Y per 1% change in X (elasticity)"]]},
             {"t": "hbox", "color": "cyan", "html": "Logs are the practitioner's friend for money "
              "variables: they fix skew, ease heteroscedasticity, and give intuitive percentage "
              "interpretations."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Logistic Regression"},

        {"type": "content", "label": "A Different Outcome", "title": "When Y is yes/no",
         "blocks": [
             {"t": "body", "html": "Many development outcomes are <strong>binary</strong>: a child "
              "is fully immunised or not; a woman delivered in a facility or not; a household is "
              "below the poverty line or not. Linear regression is the wrong tool for these."},
             {"t": "hbox", "color": "red", "html": "Fit a straight line to a 0/1 outcome and it "
              "will happily predict probabilities below 0 or above 1 &mdash; nonsense. We need a "
              "model that stays inside 0&ndash;1."},
         ]},

        {"type": "content", "label": "The Solution", "title": "Model the probability with an S-curve",
         "blocks": [
             {"t": "body", "html": "<strong>Logistic regression</strong> models the probability of "
              "'yes' using an S-shaped (logistic) curve that flattens near 0 and 1, so predictions "
              "always stay in the valid range."},
             {"t": "hbox", "color": "cyan", "html": "The trick: instead of modelling the "
              "probability directly, it models the <em>log-odds</em> of the outcome as a linear "
              "function of the predictors. That keeps the familiar 'linear in the Xs' structure."},
         ]},

        {"type": "content", "label": "Odds &amp; Log-Odds", "title": "From probability to log-odds",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Quantity", "Definition", "Range"],
              "rows": [
                  ["Probability p", "Chance of 'yes'", "0 to 1"],
                  ["Odds", "p &divide; (1 &minus; p)", "0 to &infin;"],
                  ["Log-odds (logit)", "ln(odds)", "&minus;&infin; to +&infin;"]]},
             {"t": "body", "html": "A probability of 0.8 is odds of 4 (4-to-1 on) and log-odds of "
              "about 1.39. Logistic regression's coefficients live on this <strong>log-odds</strong> "
              "scale &mdash; which is why they are not directly readable."},
         ]},

        {"type": "content", "label": "The Key Move", "title": "Coefficients are in log-odds &mdash; exponentiate them",
         "blocks": [
             {"t": "body", "html": "A logistic coefficient &beta; is the change in <em>log-odds</em> "
              "per one-unit increase in X. That is hard to feel. So we take "
              "<strong>exp(&beta;)</strong> to get an <strong>odds ratio</strong> &mdash; a "
              "multiplicative effect on the odds."},
             {"t": "hbox", "color": "red", "html": "This is the most-mangled idea in applied "
              "statistics: the raw coefficient is log-odds; <strong>exp(coefficient) is the odds "
              "ratio</strong>. Never read the raw logit coefficient as a probability."},
         ]},

        {"type": "content", "label": "Reading Odds Ratios", "title": "Above 1, below 1, equal to 1",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>OR &gt; 1:</strong> the predictor <em>raises</em> the odds of 'yes' "
                 "(OR 1.5 &rarr; odds 50% higher)",
                 "<strong>OR &lt; 1:</strong> the predictor <em>lowers</em> the odds "
                 "(OR 0.7 &rarr; odds 30% lower)",
                 "<strong>OR = 1:</strong> no association &mdash; this is the null value"]},
             {"t": "hbox", "color": "amber", "html": "Because odds ratios are multiplicative, the "
              "null is <strong>1</strong>, not 0. A 95% CI for an OR that includes 1 is "
              "'not significant'."},
         ]},

        {"type": "content", "label": "See It", "title": "Odds ratios for facility delivery",
         "blocks": [
             {"t": "chart", "canvas": "orBar",
              "title": "Illustrative odds ratios for facility delivery (vs home)",
              "source": "Illustrative &mdash; patterned on NFHS-style predictors",
              "type": "bar",
              "data": {"labels": ["Mother's schooling (per year)", "Urban (vs rural)",
                                   "Wealth quintile (per step)", "Birth order 4+ (vs 1)"],
                       "datasets": [{"label": "Odds ratio",
                                     "data": [1.12, 1.85, 1.45, 0.62],
                                     "backgroundColor": ["#6366F1", "#10B981", "#0EA5E9", "#EF4444"]}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{ legend:{ display:false } }, "
                          "scales:{ x:{ title:{ display:true, text:'Odds ratio (1 = no effect)' }, "
                          "suggestedMin:0 } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Read across the line at <strong>OR = 1</strong>: "
              "urban residence and wealth raise the odds of a facility delivery; high birth order "
              "(OR 0.62) lowers them by about 38%. All illustrative."},
         ]},

        {"type": "content", "label": "Careful Reading", "title": "Odds ratios are not risk ratios",
         "blocks": [
             {"t": "body", "html": "An odds ratio of 2 does <strong>not</strong> mean the "
              "probability doubles. Odds and probability diverge sharply when outcomes are common. "
              "For a rare outcome the two are close; for a common one they are not."},
             {"t": "hbox", "color": "red", "html": "Say 'the <em>odds</em> are 85% higher', not "
              "'85% more likely'. If your audience needs probabilities, report predicted "
              "probabilities at chosen covariate values instead."},
         ]},

        {"type": "content", "label": "Same Discipline", "title": "Everything else carries over",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Coefficients are still <em>partial</em> effects &mdash; net of the other predictors",
                 "Each odds ratio still comes with a confidence interval &mdash; report it",
                 "Multicollinearity, interactions and dummies all behave as before",
                 "Fit is judged differently (pseudo-R&sup2;, classification, AUC), not by OLS R&sup2;"]},
             {"t": "hbox", "color": "cyan", "html": "Logistic regression is the same way of "
              "thinking on a new scale &mdash; learn the log-odds/odds-ratio translation and you "
              "are most of the way there."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Data Reduction &mdash; PCA &amp; Factor Analysis"},

        {"type": "content", "label": "The Problem", "title": "Too many indicators, one concept",
         "blocks": [
             {"t": "body", "html": "You may have twenty asset and housing variables &mdash; "
              "fridge, TV, motorcycle, pucca walls, electricity, toilet type &mdash; all proxying "
              "one idea: <strong>household living standards</strong>. Putting all twenty in a "
              "regression is messy and collinear."},
             {"t": "hbox", "color": "cyan", "html": "<strong>Data reduction</strong> compresses "
              "many correlated indicators into a few summary scores that capture most of their "
              "shared information."},
         ]},

        {"type": "content", "label": "PCA", "title": "Principal Component Analysis",
         "blocks": [
             {"t": "term", "word": "Principal Component Analysis",
              "def": "A technique that re-expresses many correlated variables as a smaller set of "
              "uncorrelated 'components', ordered so the first captures the most variance, the "
              "second the next-most, and so on."},
             {"t": "body", "html": "The <strong>first principal component</strong> is the single "
              "weighted combination of the variables that explains the largest share of their "
              "joint variation &mdash; usually the 'size' or 'level' they share."},
         ]},

        {"type": "content", "label": "How Much to Keep", "title": "The scree plot",
         "blocks": [
             {"t": "chart", "canvas": "screeBar",
              "title": "Variance explained by each component (illustrative scree)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["PC1", "PC2", "PC3", "PC4", "PC5", "PC6"],
                       "datasets": [{"label": "% variance explained",
                                     "data": [48, 14, 9, 6, 4, 3],
                                     "backgroundColor": ["#10B981", "#0EA5E9", "#6366F1",
                                                         "#64748b", "#64748b", "#64748b"]}]},
              "options": {"__js__": "{ plugins:{ legend:{ display:false } }, "
                          "scales:{ y:{ title:{ display:true, text:'% of variance' } } } }"}},
             {"t": "hbox", "color": "amber", "html": "The first component dwarfs the rest &mdash; "
              "the classic signal that one dimension (wealth) underlies the asset variables. Keep "
              "components up to the 'elbow' where the bars level off."},
         ]},

        {"type": "content", "label": "The Canonical Use", "title": "The DHS / NFHS wealth index",
         "blocks": [
             {"t": "body", "html": "The standard <strong>DHS/NFHS wealth index</strong> is built "
              "with PCA. Asset, housing and utility variables go in; the <strong>first principal "
              "component</strong> becomes each household's wealth score &mdash; the textbook "
              "example of PCA in development."},
             {"t": "hbox", "color": "cyan", "html": "Households are then ranked and split into five "
              "<strong>wealth quintiles</strong>. This is the 'wealth quintile' you see throughout "
              "NFHS tables &mdash; a PCA score in disguise."},
         ]},

        {"type": "content", "label": "See It", "title": "The wealth-index distribution",
         "blocks": [
             {"t": "chart", "canvas": "wealthDist",
              "title": "Distribution of a PCA wealth score, split into quintiles (illustrative)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["Poorest", "Poorer", "Middle", "Richer", "Richest"],
                       "datasets": [{"label": "% of households",
                                     "data": [20, 20, 20, 20, 20],
                                     "backgroundColor": ["#EF4444", "#F59E0B", "#0EA5E9",
                                                         "#6366F1", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{ legend:{ display:false } }, "
                          "scales:{ y:{ title:{ display:true, text:'% of households' }, "
                          "suggestedMax:30 } } }"}},
             {"t": "hbox", "color": "cyan", "html": "By construction the quintiles each hold ~20% "
              "of households &mdash; the index is a continuous score <em>cut</em> into five equal "
              "bands. The underlying score itself is continuous and right-skewed in level."},
         ]},

        {"type": "content", "label": "PCA vs Factor Analysis", "title": "Cousins, not twins",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "PCA", "Factor analysis"],
              "rows": [
                  ["Goal", "Summarise / compress variance", "Find latent underlying factors"],
                  ["Direction", "Variables &rarr; components", "Factors &rarr; cause the variables"],
                  ["Model of error", "None &mdash; pure re-expression", "Separates shared vs unique variance"],
                  ["Typical use", "Indices (wealth index)", "Psychometrics, attitude scales"]]},
             {"t": "hbox", "color": "amber", "html": "In practice they often give similar results "
              "for index-building. PCA is the default for wealth indices; factor analysis suits "
              "questionnaire scales where a true latent trait is assumed."},
         ]},

        {"type": "content", "label": "Watch-Outs", "title": "Reduction has costs",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Components can be hard to <strong>name</strong> &mdash; what does PC2 mean?",
                 "PCA is scale-sensitive &mdash; standardise variables (or use a suitable method) first",
                 "An asset index reflects what is <em>in</em> the basket &mdash; urban-skewed assets bias it",
                 "Compressing always discards some information by design"]},
             {"t": "hbox", "color": "cyan", "html": "Used well, data reduction tames "
              "multicollinearity and yields one clean predictor. Used blindly, it buries the very "
              "structure you wanted to study."},
         ]},

        {"type": "content", "label": "Recap", "title": "Data reduction in one breath",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Many correlated indicators &rarr; a few uncorrelated summary scores",
                 "PCA's first component = the dominant shared dimension (often 'level' or 'wealth')",
                 "The NFHS/DHS wealth index <em>is</em> the first principal component of assets",
                 "Quintiles are that continuous score cut into five equal groups"]},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Pitfalls"},

        {"type": "content", "label": "Pitfall 1", "title": "Overfitting",
         "blocks": [
             {"t": "body", "html": "Throw enough predictors at a small sample and the model fits "
              "the <em>noise</em>, not the signal. It looks brilliant in your data and fails on the "
              "next dataset &mdash; it memorised rather than learned."},
             {"t": "hbox", "color": "red", "html": "Symptoms: many predictors relative to "
              "observations, dazzling in-sample R&sup2;, coefficients that change wildly across "
              "samples. Cure: simpler models, adjusted R&sup2;, out-of-sample testing."},
         ]},

        {"type": "content", "label": "Pitfall 2", "title": "Omitted-variable bias",
         "blocks": [
             {"t": "body", "html": "Leave out a real confounder and its effect contaminates the "
              "variables you did include. This is the mirror image of controlling: omit income and "
              "the diet coefficient absorbs income's effect."},
             {"t": "hbox", "color": "amber", "html": "The bias's direction depends on how the "
              "omitted variable relates to both X and Y. Unlike multicollinearity, this one "
              "genuinely <strong>biases</strong> coefficients &mdash; it is the more dangerous problem."},
         ]},

        {"type": "content", "label": "A False Trade-Off", "title": "Multicollinearity vs causality",
         "blocks": [
             {"t": "body", "html": "These two pitfalls pull in opposite directions. Dropping a "
              "collinear predictor cures the imprecision &mdash; but if that predictor was a real "
              "confounder, dropping it <em>creates</em> omitted-variable bias."},
             {"t": "hbox", "color": "cyan", "html": "The resolution is your <em>question</em>. For "
              "an unbiased causal estimate, keep the confounder and tolerate wide intervals. For "
              "pure prediction, collinearity may not matter at all."},
         ]},

        {"type": "content", "label": "Pitfall 3", "title": "Controlling for a mediator",
         "blocks": [
             {"t": "term", "word": "Mediator",
              "def": "A variable on the causal path between X and Y &mdash; X causes the mediator, "
              "which in turn causes Y. It transmits the effect rather than confounding it."},
             {"t": "body", "html": "Education raises income, and income improves child nutrition. "
              "Income is a <strong>mediator</strong> of education's effect &mdash; not a confounder "
              "to be controlled away."},
         ]},

        {"type": "content", "label": "Why It's a Trap", "title": "'Controlling for' can bias the answer",
         "blocks": [
             {"t": "body", "html": "If you 'control for' income while estimating education's effect "
              "on nutrition, you <strong>block</strong> the very pathway through which education "
              "works &mdash; and understate its total effect. More controls is not always better."},
             {"t": "hbox", "color": "red", "html": "Rule: control for <em>confounders</em> (common "
              "causes), never for <em>mediators</em> (intermediate effects) or things caused by the "
              "outcome. Draw the causal story before choosing controls."},
         ]},

        {"type": "content", "label": "Pitfall 4", "title": "Extrapolation",
         "blocks": [
             {"t": "body", "html": "A model fitted on households earning ₹5,000&ndash;₹40,000 a "
              "month says nothing reliable about a household earning ₹5 lakh. Predicting outside "
              "the range of your data assumes the line keeps going &mdash; it rarely does."},
             {"t": "hbox", "color": "amber", "html": "Stay within the support of your data. The "
              "neat straight line is an artefact of the range you observed, not a law of nature "
              "beyond it."},
         ]},

        {"type": "content", "label": "Pitfall 5", "title": "p-hacking &amp; the forking paths",
         "blocks": [
             {"t": "body", "html": "Try enough specifications &mdash; add this control, drop that "
              "one, split by region, redefine the outcome &mdash; and something will cross p &lt; "
              "0.05 by chance. Reporting only the winning run manufactures false findings."},
             {"t": "hbox", "color": "red", "html": "Defend against it: pre-specify your model, "
              "report what you tried, show robustness across specifications, and trust replication "
              "over a single surprising result."},
         ]},

        {"type": "content", "label": "Pitfalls Recap", "title": "Six traps, one habit",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Pitfall", "What goes wrong", "Guard"],
              "rows": [
                  ["Overfitting", "Fits noise, fails out of sample", "Simplicity, adjusted R&sup2;, hold-out"],
                  ["Omitted-variable bias", "Confounder contaminates coefficients", "Include real confounders"],
                  ["Collinearity confusion", "Drop a confounder to 'fix' VIF", "Let the question decide"],
                  ["Controlling a mediator", "Blocks the causal pathway", "Don't control intermediates"],
                  ["Extrapolation", "Predicts beyond the data", "Stay within range"],
                  ["p-hacking", "Chance result sold as finding", "Pre-specify, replicate"]]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Reporting &amp; Tools"},

        {"type": "content", "label": "A Workflow", "title": "How to build a model, in order",
         "blocks": [
             {"t": "flow", "steps": [
                 "ASK: a precise question &amp; outcome",
                 "DRAW: the causal story &mdash; confounders vs mediators",
                 "FIT: choose linear or logistic; add controls",
                 "CHECK: residuals, VIF, fit",
                 "REPORT: effects, CIs, caveats"]},
             {"t": "hbox", "color": "green", "html": "Notice the thinking happens <em>before</em> "
              "the software runs. Drawing the causal story first is what tells you which variables "
              "to control &mdash; and which to leave alone."},
         ]},

        {"type": "content", "label": "The Regression Table", "title": "What a results table must show",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Predictor", "Coefficient", "95% CI", "p"],
              "rows": [
                  ["Income (per ₹1,000)", "0.03", "0.01 &ndash; 0.05", "&lt;0.01"],
                  ["Mother's schooling (yr)", "0.06", "0.02 &ndash; 0.10", "&lt;0.01"],
                  ["Improved toilet (vs none)", "0.18", "0.07 &ndash; 0.29", "&lt;0.01"],
                  ["Intercept", "&minus;1.42", "&mdash;", "&mdash;"]]},
             {"t": "hbox", "color": "amber", "html": "Always report coefficients with "
              "<strong>confidence intervals</strong>, the sample size, R&sup2;/adjusted R&sup2;, "
              "and the units. Illustrative figures shown."},
         ]},

        {"type": "content", "label": "Good Reporting", "title": "Habits that earn trust",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "State your <strong>question and model</strong> before the numbers",
                 "Give effect <strong>sizes with units</strong>, not just stars",
                 "Show <strong>confidence intervals</strong>; note the sample size and any weights",
                 "Report the <strong>diagnostics</strong> you ran and what you found",
                 "Be explicit about what is <strong>association</strong> vs causal claim"]},
         ]},

        {"type": "content", "label": "The Toolbox", "title": "R, Python and Stata",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Strengths", "Note"],
              "rows": [
                  ["R", "Stats-first, superb diagnostics &amp; graphics", "Free; lm(), glm(), broom"],
                  ["Python (statsmodels)", "Cleaning + modelling in one place", "Free; pandas, scikit-learn"],
                  ["Stata", "Survey data, clustered SEs, ubiquitous in econ", "Paid; svy: prefix"],
                  ["SPSS", "Menu-driven, common in academia", "Paid; gentle on-ramp"]]},
             {"t": "hbox", "color": "cyan", "html": "For NFHS/PLFS work, whatever you choose must "
              "handle <strong>survey weights and clustered standard errors</strong> &mdash; R's "
              "survey package, Python's statsmodels, or Stata's svy commands."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Mostly Harmless Econometrics</em> &mdash; Angrist &amp; Pischke",
                 "<em>Introductory Econometrics</em> &mdash; Jeffrey Wooldridge",
                 "<em>An Introduction to Statistical Learning</em> &mdash; James et al. (free PDF)",
                 "<em>Regression and Other Stories</em> &mdash; Gelman, Hill &amp; Vehtari",
                 "DHS Wealth Index methodology &mdash; Rutstein &amp; Johnson (the PCA reference)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Exploratory Data Analysis</strong> and "
              "<strong>Causal Inference</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>A coefficient is a partial effect</strong> &mdash; the rest held constant",
                 "<strong>Adjusted R&sup2; over R&sup2;</strong>, and read confidence intervals, not just stars",
                 "<strong>Plot your residuals</strong> &mdash; diagnostics live there",
                 "<strong>Logistic coefficients are log-odds</strong>; exp() gives odds ratios (OR &gt; 1 raises odds)",
                 "<strong>Control confounders, never mediators</strong> &mdash; and never claim cause from control alone"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Multivariate Analysis 101 &middot; Complete",
         "headline": "Now hold the<br>other things constant.",
         "byline": "You don't need to derive the maths &mdash; you need to set up an honest model, "
                   "read each coefficient as a partial effect, check the residuals, and know when "
                   "a control helps or harms. Explore the rest of the ImpactMojo 101 Series, free "
                   "forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
