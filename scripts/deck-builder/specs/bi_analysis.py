# -*- coding: utf-8 -*-
"""
Bivariate Analysis 101 — ImpactMojo 101 Series (native deck spec)
The relationship between two variables, for South Asian development practitioners.
Build: python3 scripts/deck-builder/build.py bi_analysis
"""

DECK = {
    "slug": "bi-analysis",
    "title": "Bivariate Analysis 101",
    "description": ("Bivariate Analysis 101 — a free foundational course for development "
                    "practitioners and researchers in South Asia. The step after describing "
                    "one variable: cross-tabulation, correlation, comparing groups, chi-square, "
                    "simple regression and the pitfalls of reading two variables together, with "
                    "India-centric examples. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Bivariate<br>Analysis<br>101",
         "sub": "How Two Variables Move Together &mdash; Cross-Tabs, Correlation, Group "
                "Comparisons &amp; Simple Regression for Development Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "~90 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Bivariate Analysis Is", "slides": "Slides 3&ndash;10"},
             {"name": "Choosing a Method by Variable Type", "slides": "Slides 11&ndash;17"},
             {"name": "Cross-Tabulation &amp; Contingency Tables", "slides": "Slides 18&ndash;25"},
             {"name": "Visualising Relationships", "slides": "Slides 26&ndash;34"},
             {"name": "Correlation", "slides": "Slides 35&ndash;44"},
             {"name": "Comparing Two Groups", "slides": "Slides 45&ndash;53"},
             {"name": "Comparing Several Groups (ANOVA)", "slides": "Slides 54&ndash;61"},
             {"name": "Association Between Categories (Chi-Square)", "slides": "Slides 62&ndash;71"},
             {"name": "Simple Linear Regression", "slides": "Slides 72&ndash;81"},
             {"name": "Pitfalls", "slides": "Slides 82&ndash;91"},
             {"name": "Reporting, Practice &amp; Tools", "slides": "Slides 92&ndash;99"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Bivariate Analysis Is"},

        {"type": "content", "label": "Definition", "title": "From one variable to two",
         "blocks": [
             {"t": "body", "html": "Univariate analysis describes <strong>one</strong> variable at "
              "a time &mdash; the average household size, the spread of incomes. <strong>Bivariate "
              "analysis</strong> is the very next step: it asks how <strong>two</strong> variables "
              "relate to each other."},
             {"t": "term", "word": "Bivariate analysis",
              "def": "The study of the relationship between two variables &mdash; whether they "
              "move together, how strongly, and in what direction. 'Bi' = two; 'variate' = "
              "variable."},
             {"t": "hbox", "color": "cyan", "html": "Most interesting development questions are "
              "bivariate at heart: does <em>this</em> go with <em>that</em>? Does schooling go "
              "with earnings? Does the programme go with better outcomes?"},
         ]},

        {"type": "content", "label": "The Step After Describing", "title": "Where it sits in the analysis ladder",
         "blocks": [
             {"t": "flow", "steps": [
                 "UNIVARIATE: describe one variable (centre, spread, shape)",
                 "BIVARIATE: relate two variables (direction, strength)",
                 "MULTIVARIATE: many variables at once (control, adjust)"]},
             {"t": "hbox", "color": "amber", "html": "This course lives squarely in the middle "
              "rung. Master it before reaching for regression with twenty controls &mdash; the "
              "two-variable picture is where most reasoning errors are caught."},
         ]},

        {"type": "content", "label": "Two Questions", "title": "Direction and strength",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Direction", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Do they move the <em>same</em> way "
                   "(positive) or <em>opposite</em> ways (negative)? More literacy, fewer "
                   "births &mdash; that is a negative direction."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Strength", "blocks": [
                  {"t": "body", "cls": "sm", "html": "How <em>tightly</em> do they track each "
                   "other? A loose cloud is weak; a near-straight line is strong."}]}]},
             {"t": "hbox", "color": "green", "html": "Almost every bivariate tool you will meet "
              "is just a precise way to answer these two questions &mdash; plus a third: could "
              "this be chance?"},
         ]},

        {"type": "content", "label": "Vocabulary", "title": "Explanatory and response variables",
         "blocks": [
             {"t": "term", "word": "Explanatory variable (X)",
              "def": "The variable you think does the explaining or predicting &mdash; also "
              "called the independent or predictor variable. Conventionally on the horizontal "
              "axis."},
             {"t": "term", "word": "Response variable (Y)",
              "def": "The outcome you want to understand or predict &mdash; also called the "
              "dependent variable. Conventionally on the vertical axis."},
             {"t": "hbox", "color": "amber", "html": "Naming X and Y does <em>not</em> prove X "
              "causes Y. It only states which one you are treating as the outcome. The causal "
              "claim must be earned separately."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "The questions practitioners actually ask",
         "blocks": [
             {"t": "bullets", "items": [
                 "Do villages with self-help groups have higher women's savings?",
                 "Is anaemia more common among Adivasi women than others?",
                 "Does distance to a health centre predict institutional delivery?",
                 "Did test scores differ between the treated and control schools?",
                 "Is caste associated with whether a household has a toilet?"]},
             {"t": "hbox", "color": "cyan", "html": "Each is a relationship between two variables "
              "&mdash; and each maps to a specific bivariate method, which Section Two helps "
              "you choose."},
         ]},

        {"type": "content", "label": "Warning Up Front", "title": "A relationship is a clue, not a verdict",
         "blocks": [
             {"t": "body", "html": "Bivariate analysis can <em>reveal</em> a relationship, "
              "<em>quantify</em> its strength, and tell you whether it is likely real or just "
              "noise. What it cannot do, on its own, is prove that one variable "
              "<strong>causes</strong> the other."},
             {"t": "quote", "text": "The plural of anecdote is not data; and the presence of "
              "correlation is not the presence of cause.",
              "attr": "&mdash; a working principle of careful analysis"},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Tools", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Cross-tabs for category &times; category",
                      "Correlation for number &times; number",
                      "t-tests and ANOVA for comparing groups",
                      "Chi-square and simple regression"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Judgement", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Choosing the right method",
                      "Reading effect size, not just p-values",
                      "Spotting confounders and fallacies",
                      "Reporting a relationship honestly"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Examples come from India and the wider "
              "region &mdash; the data you actually meet at work."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Choosing a Method by Variable Type"},

        {"type": "content", "label": "The Master Move", "title": "First, classify both variables",
         "blocks": [
             {"t": "body", "html": "The single most useful habit in bivariate analysis: before "
              "choosing any method, ask <strong>what kind of variable</strong> each of your two "
              "is &mdash; <strong>categorical</strong> or <strong>numeric</strong>. The pair of "
              "answers points straight to the right tool."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Categorical", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Labels or groups &mdash; sex, caste, "
                   "religion, district, yes/no. Includes ordered categories (wealth quintile, "
                   "Likert scale)."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Numeric", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Counts and measurements &mdash; age, "
                   "income, test score, fertility rate, distance in km. You can meaningfully "
                   "average them."}]}]},
         ]},

        {"type": "content", "label": "The Decision Table", "title": "Method by the two variable types",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["X type", "Y type", "Describe with", "Test with"],
              "rows": [
                  ["Categorical", "Categorical", "Cross-tab, % &amp; bars", "Chi-square test"],
                  ["Categorical (2 groups)", "Numeric", "Group means, box plots", "t-test"],
                  ["Categorical (3+ groups)", "Numeric", "Group means, box plots", "One-way ANOVA"],
                  ["Numeric", "Numeric", "Scatter plot", "Correlation / regression"]]},
             {"t": "hbox", "color": "cyan", "html": "Pin this table to your wall. Nine times out "
              "of ten, classifying your two variables tells you exactly which method to reach for."},
         ]},

        {"type": "content", "label": "Cat &times; Cat", "title": "Two categories: is membership linked?",
         "blocks": [
             {"t": "body", "html": "When both variables are categories &mdash; say "
              "<strong>caste group</strong> and <strong>has a household toilet (yes/no)</strong> "
              "&mdash; you ask whether knowing one tells you anything about the other."},
             {"t": "hbox", "color": "indigo", "html": "Describe it with a <strong>cross-tabulation</strong> "
              "and percentages; test it with a <strong>chi-square test of independence</strong>. "
              "Covered in Sections Three and Eight."},
         ]},

        {"type": "content", "label": "Cat &times; Num", "title": "A group label and a number: compare means",
         "blocks": [
             {"t": "body", "html": "When one variable is a group label and the other is numeric "
              "&mdash; <strong>treatment vs control</strong> and <strong>test score</strong> "
              "&mdash; you compare the numeric outcome <em>across</em> the groups."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Two groups", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Difference in means &mdash; the "
                   "<strong>t-test</strong> idea. Section Six."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Three or more groups", "blocks": [
                  {"t": "body", "cls": "sm", "html": "One-way <strong>ANOVA</strong> compares "
                   "all the group means at once. Section Seven."}]}]},
         ]},

        {"type": "content", "label": "Num &times; Num", "title": "Two numbers: do they track each other?",
         "blocks": [
             {"t": "body", "html": "When both variables are numeric &mdash; <strong>female "
              "literacy</strong> and <strong>fertility rate</strong> across districts &mdash; "
              "plot one against the other on a scatter and measure how tightly they move "
              "together."},
             {"t": "hbox", "color": "amber", "html": "Describe the strength with "
              "<strong>correlation</strong> (Section Five); model the line with simple "
              "<strong>linear regression</strong> (Section Nine)."},
         ]},

        {"type": "content", "label": "A Caution", "title": "The method serves the question, not the reverse",
         "blocks": [
             {"t": "body", "html": "Do not pick a fancy test and then hunt for variables to feed "
              "it. Start from the real question, classify the two variables it involves, and let "
              "the decision table hand you the method."},
             {"t": "quote", "text": "Far better an approximate answer to the right question than "
              "an exact answer to the wrong one.",
              "attr": "&mdash; John Tukey"},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Cross-Tabulation &amp; Contingency Tables"},

        {"type": "content", "label": "The Workhorse", "title": "Counting two categories together",
         "blocks": [
             {"t": "term", "word": "Cross-tabulation (contingency table)",
              "def": "A table that counts how many cases fall into each combination of two "
              "categorical variables &mdash; rows for one variable, columns for the other."},
             {"t": "body", "html": "It is the most-used tool in applied development analysis: a "
              "single table that shows, at a glance, how two group memberships line up."},
         ]},

        {"type": "content", "label": "A 2&times;2 Table", "title": "Toilet ownership by location (raw counts)",
         "blocks": [
             {"t": "table",
              "head": ["", "Has toilet", "No toilet", "Total"],
              "rows": [
                  ["Rural", "320", "280", "600"],
                  ["Urban", "340", "60", "400"],
                  ["Total", "660", "340", "1,000"]]},
             {"t": "hbox", "color": "amber", "html": "Illustrative figures. The four inner cells "
              "are the <em>joint</em> counts; the right and bottom margins are the "
              "<strong>marginal</strong> totals for each variable on its own."},
         ]},

        {"type": "content", "label": "Why Percentages", "title": "Raw counts mislead when groups differ in size",
         "blocks": [
             {"t": "body", "html": "Rural and urban have different totals (600 vs 400), so "
              "comparing raw counts is unfair. To compare fairly, convert to "
              "<strong>percentages</strong> &mdash; but in which direction?"},
             {"t": "hbox", "color": "red", "html": "This is the single most common cross-tab "
              "error: percentaging the wrong way and reading a relationship backwards. Get the "
              "direction right and the table tells the truth."},
         ]},

        {"type": "content", "label": "Row Percentages", "title": "Percent within each row",
         "blocks": [
             {"t": "table",
              "head": ["", "Has toilet", "No toilet", "Row total"],
              "rows": [
                  ["Rural", "53%", "47%", "100%"],
                  ["Urban", "85%", "15%", "100%"]]},
             {"t": "hbox", "color": "cyan", "html": "Each <em>row</em> sums to 100%. This "
              "answers: <strong>of rural households, what share have a toilet?</strong> 53% rural "
              "vs 85% urban &mdash; a clear location gap. (Illustrative.)"},
         ]},

        {"type": "content", "label": "Column Percentages", "title": "Percent within each column",
         "blocks": [
             {"t": "table",
              "head": ["", "Has toilet", "No toilet"],
              "rows": [
                  ["Rural", "48%", "82%"],
                  ["Urban", "52%", "18%"],
                  ["Column total", "100%", "100%"]]},
             {"t": "hbox", "color": "indigo", "html": "Each <em>column</em> sums to 100%. This "
              "answers a different question: <strong>of households without a toilet, what share "
              "are rural?</strong> 82%. Same table, different story."},
         ]},

        {"type": "content", "label": "The Rule", "title": "Percentage in the direction of the cause",
         "blocks": [
             {"t": "body", "html": "Convention: percentage <strong>within categories of the "
              "explanatory variable</strong>, then compare <em>across</em> them. If location "
              "(X) might shape toilet ownership (Y), percentage within rural and within urban "
              "&mdash; that is row percentaging here."},
             {"t": "flow", "steps": [
                 "Put X in the rows",
                 "Percentage so each row = 100%",
                 "Compare the same Y-column across rows"]},
         ]},

        {"type": "content", "label": "Reading a 2&times;2", "title": "What a difference in percentages means",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "85% &minus; 53%", "label": "= 32 percentage-point gap in toilet "
                  "ownership, urban vs rural", "color": "green"},
                 {"num": "Direction", "label": "Urban households far more likely to have a "
                  "toilet &mdash; a positive urban&ndash;toilet link", "color": "cyan"}]},
             {"t": "hbox", "color": "amber", "html": "A gap in the table <em>suggests</em> an "
              "association. Whether it is bigger than chance is what the chi-square test in "
              "Section Eight decides."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Visualising Relationships"},

        {"type": "content", "label": "Plot First", "title": "Always look before you compute",
         "blocks": [
             {"t": "body", "html": "Before any coefficient or test, <strong>draw the "
              "relationship</strong>. A picture reveals direction, strength, curvature, "
              "clusters and outliers that a single number can hide entirely."},
             {"t": "quote", "text": "The greatest value of a picture is when it forces us to "
              "notice what we never expected to see.",
              "attr": "&mdash; John Tukey"},
         ]},

        {"type": "content", "label": "Match Plot to Types", "title": "Which chart for which pair",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Variable pair", "Best plot", "Shows"],
              "rows": [
                  ["Numeric &times; numeric", "Scatter plot", "Direction, strength, shape"],
                  ["Categorical &times; numeric", "Box plot by group", "Spread &amp; median per group"],
                  ["Categorical &times; numeric", "Grouped / clustered bars", "Mean per group"],
                  ["Categorical &times; categorical", "Stacked / grouped bars", "Shares within groups"]]},
         ]},

        {"type": "content", "label": "Scatter Plots", "title": "The workhorse for two numbers",
         "blocks": [
             {"t": "body", "html": "A <strong>scatter plot</strong> puts the explanatory "
              "variable on the X-axis, the response on the Y-axis, and one dot per case. The "
              "<em>cloud's tilt</em> shows direction; its <em>tightness</em> shows strength."},
             {"t": "hbox", "color": "cyan", "html": "Read it like this: upward cloud = positive; "
              "downward = negative; round blob = no linear relationship; tight line = strong; "
              "fat cloud = weak."},
         ]},

        {"type": "content", "label": "See It", "title": "Three scatters: positive, negative, none",
         "blocks": [
             {"t": "chart", "canvas": "scatterThreeChart",
              "title": "Same axes, three relationships",
              "source": "Illustrative",
              "type": "scatter",
              "data": {"datasets": [
                  {"label": "Positive", "backgroundColor": "#10B981", "pointRadius": 5,
                   "data": [{"x": 1, "y": 2}, {"x": 2, "y": 3}, {"x": 3, "y": 3.5},
                            {"x": 4, "y": 5}, {"x": 5, "y": 5.5}, {"x": 6, "y": 7},
                            {"x": 7, "y": 7.5}, {"x": 8, "y": 9}]},
                  {"label": "Negative", "backgroundColor": "#EF4444", "pointRadius": 5,
                   "data": [{"x": 1, "y": 9}, {"x": 2, "y": 8}, {"x": 3, "y": 6.5},
                            {"x": 4, "y": 6}, {"x": 5, "y": 4.5}, {"x": 6, "y": 4},
                            {"x": 7, "y": 2.5}, {"x": 8, "y": 2}]},
                  {"label": "No relationship", "backgroundColor": "#6366F1", "pointRadius": 5,
                   "data": [{"x": 1, "y": 5}, {"x": 2, "y": 7}, {"x": 3, "y": 4},
                            {"x": 4, "y": 6}, {"x": 5, "y": 5}, {"x": 6, "y": 7},
                            {"x": 7, "y": 4.5}, {"x": 8, "y": 6}]}]},
              "options": {"__js__": "{ scales:{ x:{ title:{display:true,text:'X'} }, y:{ title:{display:true,text:'Y'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Green rises, red falls, indigo wanders. "
              "Your eye reads direction and strength instantly &mdash; before any number."},
         ]},

        {"type": "content", "label": "Real-Feeling Data", "title": "Female literacy vs child mortality, by state",
         "blocks": [
             {"t": "chart", "canvas": "litMortChart",
              "title": "Female literacy (%) vs under-5 mortality (per 1,000), major states",
              "source": "Illustrative, patterned on Census 2011 &amp; NFHS-5",
              "type": "scatter",
              "data": {"datasets": [{"label": "States", "backgroundColor": "#6366F1", "pointRadius": 6,
                       "data": [{"x": 92, "y": 7}, {"x": 84, "y": 12}, {"x": 76, "y": 20},
                                {"x": 73, "y": 26}, {"x": 70, "y": 30}, {"x": 66, "y": 33},
                                {"x": 64, "y": 38}, {"x": 60, "y": 42}, {"x": 59, "y": 47},
                                {"x": 57, "y": 50}, {"x": 53, "y": 55}, {"x": 50, "y": 60}]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Female literacy %'} }, y:{ title:{display:true,text:'Under-5 mortality / 1,000'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "A strong negative pattern: states with "
              "higher female literacy tend to have lower child mortality. Illustrative, but it "
              "mirrors the real Census&ndash;NFHS picture closely."},
         ]},

        {"type": "content", "label": "Box Plots", "title": "Comparing a number across groups",
         "blocks": [
             {"t": "body", "html": "For a categorical X and numeric Y, a <strong>box plot per "
              "group</strong> beats a single average. Each box shows the median (the line), the "
              "middle 50% (the box), the range (the whiskers) and outliers (the dots)."},
             {"t": "hbox", "color": "green", "html": "Box plots let you see not just whether the "
              "<em>centres</em> differ between groups, but whether the <em>spreads</em> do "
              "&mdash; two distributions with the same mean can look completely different."},
         ]},

        {"type": "content", "label": "Grouped Bars", "title": "A mean compared across groups",
         "blocks": [
             {"t": "chart", "canvas": "groupedBarChart",
              "title": "Mean monthly earnings by education level (illustrative, ₹000)",
              "source": "Illustrative, patterned on PLFS-style data",
              "type": "bar",
              "data": {"labels": ["No schooling", "Primary", "Secondary", "Higher sec.", "Graduate+"],
                       "datasets": [{"label": "Mean earnings (₹000/month)",
                                     "data": [7.5, 9.5, 13, 17, 28],
                                     "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true, title:{display:true,text:'₹000 / month'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "A clean grouped bar shows the mean of a "
              "numeric outcome rising across ordered categories &mdash; the visual form of a "
              "category &times; number relationship."},
         ]},

        {"type": "content", "label": "Honest Charts", "title": "The same rules still apply",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Start bar axes at <strong>zero</strong> &mdash; a truncated axis fakes a gap",
                 "Label both axes with <strong>units</strong>",
                 "Note the <strong>denominator</strong> and sample size",
                 "Put the <strong>source</strong> and date on the chart",
                 "Do not let one outlier dominate a scatter unremarked"]},
             {"t": "hbox", "color": "amber", "html": "A bivariate chart is an argument about a "
              "relationship. Truncated axes and missing denominators turn an honest pattern "
              "into a misleading one."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Correlation"},

        {"type": "content", "label": "The Number", "title": "Putting a value on 'move together'",
         "blocks": [
             {"t": "term", "word": "Correlation coefficient (r)",
              "def": "A single number summarising how strongly and in which direction two "
              "numeric variables move together in a straight-line sense. It ranges from "
              "&minus;1 to +1."},
             {"t": "body", "html": "Where a scatter shows the relationship, <em>r</em> "
              "<strong>measures</strong> it &mdash; one number for direction and strength "
              "combined."},
         ]},

        {"type": "content", "label": "The Scale", "title": "r runs from &minus;1 to +1",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "&minus;1", "label": "Perfect negative &mdash; points fall exactly on "
                  "a downward line", "color": "red"},
                 {"num": "0", "label": "No linear relationship &mdash; a shapeless cloud", "color": "indigo"},
                 {"num": "+1", "label": "Perfect positive &mdash; points fall exactly on an "
                  "upward line", "color": "green"}]},
             {"t": "hbox", "color": "cyan", "html": "The <em>sign</em> gives direction; the "
              "<em>distance from zero</em> gives strength. r = &minus;0.8 and r = +0.8 are "
              "equally strong, opposite in direction."},
         ]},

        {"type": "content", "label": "Pearson's r", "title": "The default: Pearson correlation",
         "blocks": [
             {"t": "body", "html": "The everyday correlation is <strong>Pearson's r</strong>. "
              "Crucially, it measures only the <strong>linear</strong> (straight-line) component "
              "of a relationship between two numeric variables."},
             {"t": "hbox", "color": "red", "html": "If the true relationship is curved &mdash; "
              "rising then falling &mdash; Pearson's r can be near zero even when the two "
              "variables are tightly related. Pearson sees lines, not curves."},
         ]},

        {"type": "content", "label": "Rough Guide", "title": "Interpreting the size of r",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["|r|", "Rough strength", "What the scatter looks like"],
              "rows": [
                  ["0.0 &ndash; 0.1", "Negligible", "Shapeless cloud"],
                  ["0.1 &ndash; 0.3", "Weak", "Faint tilt"],
                  ["0.3 &ndash; 0.5", "Moderate", "Clear tilt, wide scatter"],
                  ["0.5 &ndash; 0.7", "Strong", "Tight tilt"],
                  ["0.7 &ndash; 1.0", "Very strong", "Near a straight line"]]},
             {"t": "hbox", "color": "amber", "html": "These bands are conventions, not laws. In "
              "messy social data, an r of 0.3 can be a genuinely important signal."},
         ]},

        {"type": "content", "label": "Worked Example", "title": "Literacy and fertility, quantified",
         "blocks": [
             {"t": "chart", "canvas": "litFertCorrChart",
              "title": "Female literacy (%) vs total fertility rate, major states",
              "source": "Illustrative, patterned on Census 2011 &amp; NFHS-5",
              "type": "scatter",
              "data": {"datasets": [{"label": "States", "backgroundColor": "#6366F1", "pointRadius": 6,
                       "data": [{"x": 92, "y": 1.8}, {"x": 84, "y": 1.7}, {"x": 76, "y": 1.8},
                                {"x": 73, "y": 2.1}, {"x": 70, "y": 2.0}, {"x": 66, "y": 2.1},
                                {"x": 64, "y": 2.4}, {"x": 60, "y": 2.5}, {"x": 59, "y": 2.7},
                                {"x": 57, "y": 2.6}, {"x": 53, "y": 3.0}, {"x": 50, "y": 3.0}]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Female literacy %'} }, y:{ title:{display:true,text:'Total fertility rate'}, min:1.5, max:3.2 } } }"}},
             {"t": "hbox", "color": "cyan", "html": "This cloud has a clear downward tilt &mdash; "
              "an r near &minus;0.9 (illustrative). Strong and negative. But strength is not the "
              "same as cause: literacy may proxy for income, health and much else."},
         ]},

        {"type": "content", "label": "Spearman", "title": "When to use rank correlation instead",
         "blocks": [
             {"t": "term", "word": "Spearman's rank correlation (&rho;)",
              "def": "Pearson's correlation computed on the ranks of the data rather than the "
              "raw values. It measures whether two variables move together in the same order, "
              "not strictly in a straight line."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Use it for <strong>ordinal</strong> data &mdash; wealth quintiles, Likert scales",
                 "Use it for <strong>skewed</strong> data &mdash; income, landholding",
                 "Use it when the relationship is monotonic but <strong>curved</strong>",
                 "It is robust to <strong>outliers</strong> that would swing Pearson's r"]},
         ]},

        {"type": "content", "label": "Pearson vs Spearman", "title": "Two correlations, side by side",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Pearson r", "Spearman &rho;"],
              "rows": [
                  ["Measures", "Linear association", "Monotonic (rank) association"],
                  ["Best data", "Numeric, roughly symmetric", "Ordinal or skewed numeric"],
                  ["Outlier-sensitive?", "Yes &mdash; one point can swing it", "No &mdash; uses ranks"],
                  ["Range", "&minus;1 to +1", "&minus;1 to +1"]]},
             {"t": "hbox", "color": "amber", "html": "When Pearson and Spearman disagree "
              "sharply, suspect non-linearity or an outlier &mdash; and go back to the scatter."},
         ]},

        {"type": "content", "label": "Strength &ne; Significance", "title": "A big r and a small p are different things",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Strength (effect size)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>How big</strong> is the "
                   "relationship? That is what r itself tells you &mdash; the practical "
                   "magnitude."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Significance (p-value)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>How sure</strong> are we it is "
                   "not zero by chance? That depends heavily on sample size."}]}]},
             {"t": "hbox", "color": "red", "html": "With thousands of cases, a tiny, "
              "uninteresting r = 0.05 can be 'statistically significant'. Always report the "
              "size, not just the star."},
         ]},

        {"type": "content", "label": "r-squared Preview", "title": "Square it for 'variance explained'",
         "blocks": [
             {"t": "body", "html": "Square the correlation and you get <strong>R&sup2;</strong> "
              "&mdash; the share of the variation in one variable that is statistically "
              "accounted for by the other. r = 0.7 means R&sup2; = 0.49: about half the "
              "variation is shared."},
             {"t": "hbox", "color": "cyan", "html": "We return to R&sup2; properly in the "
              "regression section &mdash; it is the natural bridge from correlation to a fitted "
              "line."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Comparing Two Groups"},

        {"type": "content", "label": "The Setup", "title": "One group label, one number",
         "blocks": [
             {"t": "body", "html": "A categorical X with <strong>two</strong> values "
              "(treatment/control, girls/boys, SHG/non-SHG) and a numeric Y (score, income, "
              "weight). The question: do the <strong>two group means differ</strong> &mdash; "
              "and is the difference real?"},
             {"t": "flow", "steps": [
                 "Split the data into two groups by X",
                 "Compute each group's mean of Y",
                 "Ask: is the gap bigger than chance?"]},
         ]},

        {"type": "content", "label": "Difference in Means", "title": "The quantity of interest",
         "blocks": [
             {"t": "chart", "canvas": "twoGroupChart",
              "title": "Mean test score: control vs treatment schools (illustrative)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["Control", "Treatment"],
                       "datasets": [{"label": "Mean score (out of 100)",
                                     "data": [54, 61],
                                     "backgroundColor": ["#94A3B8", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true, max:100, title:{display:true,text:'Mean score'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The raw difference is 7 points "
              "(61 &minus; 54). But two questions remain: could a 7-point gap arise by chance, "
              "and is 7 points <em>big enough to matter</em>?"},
         ]},

        {"type": "content", "label": "The t-test Idea", "title": "Signal divided by noise",
         "blocks": [
             {"t": "term", "word": "t-test",
              "def": "A test of whether the difference between two group means is larger than "
              "we would expect from sampling variation alone &mdash; essentially, the size of "
              "the gap relative to how noisy the data are."},
             {"t": "body", "html": "Intuitively, t &asymp; <strong>difference in means &divide; "
              "uncertainty in that difference</strong>. A big, clean gap gives a big t; a small "
              "gap drowned in scatter gives a small t."},
         ]},

        {"type": "content", "label": "What Drives It", "title": "Three things make a gap convincing",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>A larger difference</strong> between the two means",
                 "<strong>Less spread</strong> (variation) within each group",
                 "<strong>A larger sample</strong> in each group"]},
             {"t": "hbox", "color": "amber", "html": "The same 7-point gap is unconvincing with "
              "20 noisy pupils per arm, but compelling with 2,000 tightly clustered ones. "
              "Sample size and spread decide the verdict."},
         ]},

        {"type": "content", "label": "The p-value", "title": "What a p-value does and doesn't say",
         "blocks": [
             {"t": "term", "word": "p-value",
              "def": "The probability of seeing a difference at least this large if there were "
              "truly no difference between the groups. Small p (say &lt; 0.05) means the gap is "
              "unlikely to be pure chance."},
             {"t": "hbox", "color": "red", "html": "A p-value is <strong>not</strong> the "
              "probability the effect is real, nor a measure of its size. It only addresses "
              "'could this be chance?' &mdash; nothing about importance."},
         ]},

        {"type": "content", "label": "Effect Size", "title": "How big, in plain terms",
         "blocks": [
             {"t": "body", "html": "Significance asks <em>whether</em> there is a difference; "
              "<strong>effect size</strong> asks <em>how big</em>. Report it in real units "
              "(7 marks, ₹400/month) or as a standardised measure (Cohen's d) so others can "
              "judge whether it matters."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "p-value", "label": "Is the gap likely real, not chance?", "color": "indigo"},
                 {"num": "Effect size", "label": "Is the gap big enough to act on?", "color": "green"}]},
         ]},

        {"type": "content", "label": "The Trap", "title": "Significant but trivial &mdash; and vice versa",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Significant but trivial", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Huge sample &rarr; a 0.3-mark difference "
                   "is 'significant' but means nothing for any child."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Real but 'not significant'", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Tiny pilot &rarr; a promising 9-point gap "
                   "fails the test purely for lack of sample. Absence of evidence is not evidence "
                   "of absence."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Always read the p-value and the effect size "
              "<em>together</em>. Neither alone tells the whole story."},
         ]},

        {"type": "content", "label": "Assumptions", "title": "When the simple t-test is appropriate",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "The two groups are <strong>independent</strong> (different people)",
                 "Y is roughly <strong>symmetric</strong> within each group (or n is large)",
                 "For paired data &mdash; same people before/after &mdash; use a "
                 "<strong>paired</strong> t-test instead",
                 "For severely skewed data, consider a rank-based alternative"]},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Comparing Several Groups (ANOVA)"},

        {"type": "content", "label": "The Setup", "title": "When there are three or more groups",
         "blocks": [
             {"t": "body", "html": "A categorical X with <strong>three or more</strong> values "
              "&mdash; four caste groups, five wealth quintiles, six districts &mdash; and a "
              "numeric Y. We want to know whether the group means differ overall."},
             {"t": "hbox", "color": "red", "html": "Tempting shortcut: run a t-test on every "
              "pair. Don't. With many pairs, the chance of a false 'significant' result piles "
              "up fast &mdash; the multiple-comparisons problem."},
         ]},

        {"type": "content", "label": "The Idea", "title": "One-way ANOVA, conceptually",
         "blocks": [
             {"t": "term", "word": "One-way ANOVA",
              "def": "Analysis of Variance &mdash; a single test of whether the means of three "
              "or more groups differ by more than chance, by comparing variation BETWEEN groups "
              "to variation WITHIN groups."},
             {"t": "body", "html": "Despite the name, ANOVA is about <em>means</em>. It uses "
              "variances as the yardstick for deciding whether those means are really apart."},
         ]},

        {"type": "content", "label": "Between vs Within", "title": "The heart of ANOVA",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Between-group variation", "blocks": [
                  {"t": "body", "cls": "sm", "html": "How far apart the <em>group means</em> are "
                   "from each other &mdash; the signal."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Within-group variation", "blocks": [
                  {"t": "body", "cls": "sm", "html": "How much individuals scatter <em>inside</em> "
                   "each group &mdash; the noise."}]}]},
             {"t": "hbox", "color": "green", "html": "The F-ratio = between &divide; within. If "
              "groups sit far apart relative to their internal scatter, F is large &mdash; "
              "evidence the means genuinely differ."},
         ]},

        {"type": "content", "label": "See It", "title": "Mean nutrition score by wealth quintile",
         "blocks": [
             {"t": "chart", "canvas": "anovaChart",
              "title": "Mean child height-for-age z-score by wealth quintile (illustrative)",
              "source": "Illustrative, patterned on NFHS-5",
              "type": "bar",
              "data": {"labels": ["Poorest", "Poorer", "Middle", "Richer", "Richest"],
                       "datasets": [{"label": "Mean HAZ z-score",
                                     "data": [-1.9, -1.6, -1.3, -0.9, -0.4],
                                     "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Mean HAZ z-score'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Five group means rising steadily across "
              "quintiles. ANOVA asks: taken together, is this spread of means bigger than the "
              "scatter within each quintile? (Illustrative; the real gradient is well documented.)"},
         ]},

        {"type": "content", "label": "After ANOVA", "title": "It says 'somewhere', not 'where'",
         "blocks": [
             {"t": "body", "html": "A significant ANOVA tells you the groups are <strong>not all "
              "equal</strong> &mdash; but not <em>which</em> ones differ. To locate the "
              "differences, follow up with <strong>post-hoc</strong> pairwise comparisons that "
              "correct for multiple testing."},
             {"t": "hbox", "color": "amber", "html": "Think of ANOVA as the smoke alarm: it "
              "tells you there is a fire somewhere, then post-hoc tests find the room."},
         ]},

        {"type": "content", "label": "Assumptions", "title": "When one-way ANOVA fits",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Groups are <strong>independent</strong>",
                 "Y is roughly <strong>symmetric</strong> within each group (or n is large)",
                 "Group <strong>spreads</strong> are not wildly different",
                 "For badly skewed data, a rank-based alternative (Kruskal&ndash;Wallis) may suit"]},
             {"t": "hbox", "color": "green", "html": "ANOVA is the natural extension of the "
              "two-group t-test to many groups &mdash; same logic, scaled up."},
         ]},

        {"type": "content", "label": "Recap", "title": "Comparing groups, at a glance",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Groups", "Y type", "Method"],
              "rows": [
                  ["2 (independent)", "Numeric", "Two-sample t-test"],
                  ["2 (same units, paired)", "Numeric", "Paired t-test"],
                  ["3 or more", "Numeric", "One-way ANOVA"],
                  ["3+, skewed data", "Numeric", "Kruskal&ndash;Wallis"]]},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Association Between Categories (Chi-Square)"},

        {"type": "content", "label": "The Setup", "title": "Two categories: are they independent?",
         "blocks": [
             {"t": "body", "html": "Back to two <strong>categorical</strong> variables and a "
              "cross-tab. The <strong>chi-square test of independence</strong> asks: is the "
              "pattern in this table bigger than we would expect if the two variables were "
              "completely unrelated?"},
             {"t": "term", "word": "Independence",
              "def": "Two variables are independent if knowing one tells you nothing about the "
              "other &mdash; the distribution of Y is the same within every category of X."},
         ]},

        {"type": "content", "label": "The Core Idea", "title": "Observed vs expected counts",
         "blocks": [
             {"t": "body", "html": "Chi-square compares what you <strong>observed</strong> in "
              "each cell with what you would <strong>expect</strong> if the two variables were "
              "independent. Big gaps between observed and expected = evidence of association."},
             {"t": "flow", "steps": [
                 "Compute expected counts (if independent)",
                 "Compare with observed counts, cell by cell",
                 "Sum the scaled squared gaps &rarr; &chi;&sup2;",
                 "Large &chi;&sup2; &rarr; reject independence"]},
         ]},

        {"type": "content", "label": "Expected Counts", "title": "What 'no relationship' would predict",
         "blocks": [
             {"t": "body", "html": "Each cell's expected count is "
              "<strong>(row total &times; column total) &divide; grand total</strong>. It is the "
              "count you'd see if Y were distributed identically across every category of X."},
             {"t": "hbox", "color": "cyan", "html": "Example: with 660 of 1,000 households owning "
              "a toilet (66%), independence predicts 66% of the 600 rural households &mdash; "
              "396 &mdash; would own one. We observed only 320. That gap is the signal."},
         ]},

        {"type": "content", "label": "Observed vs Expected", "title": "Side by side (illustrative)",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Cell", "Observed", "Expected", "Gap"],
              "rows": [
                  ["Rural, toilet", "320", "396", "&minus;76"],
                  ["Rural, no toilet", "280", "204", "+76"],
                  ["Urban, toilet", "340", "264", "+76"],
                  ["Urban, no toilet", "60", "136", "&minus;76"]]},
             {"t": "hbox", "color": "amber", "html": "Rural areas have far fewer toilets than "
              "independence predicts, urban far more. Consistent gaps like these push "
              "&chi;&sup2; up. (Illustrative figures.)"},
         ]},

        {"type": "content", "label": "Reading the Result", "title": "What chi-square tells you",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Small p", "label": "Reject independence &mdash; the two variables ARE "
                  "associated", "color": "green"},
                 {"num": "Large p", "label": "No evidence of association &mdash; consistent with "
                  "independence", "color": "indigo"}]},
             {"t": "hbox", "color": "red", "html": "Chi-square tells you <em>whether</em> there "
              "is an association, not how <strong>strong</strong> it is. For strength, report a "
              "measure like Cram&eacute;r's V alongside the test."},
         ]},

        {"type": "content", "label": "Validity", "title": "When chi-square is valid",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Each case counted <strong>once</strong> (independent observations)",
                 "Cells hold <strong>counts</strong>, not percentages or means",
                 "<strong>Expected</strong> count &ge; 5 in (almost) every cell",
                 "Categories are mutually exclusive and exhaustive"]},
             {"t": "hbox", "color": "red", "html": "The expected-count rule is the one most often "
              "broken: with thin cells the chi-square approximation fails. Use Fisher's exact "
              "test for small tables instead."},
         ]},

        {"type": "content", "label": "Common Mistakes", "title": "Three ways chi-square goes wrong",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Feeding it <strong>percentages</strong> instead of raw counts",
                 "Ignoring tiny <strong>expected</strong> counts in sparse cells",
                 "Reading a significant result as proof of <strong>causation</strong>",
                 "Forgetting it says nothing about the <strong>strength</strong> of association"]},
         ]},

        {"type": "content", "label": "In Practice", "title": "Chi-square in a development workflow",
         "blocks": [
             {"t": "body", "html": "It is the natural partner to the cross-tab: you describe the "
              "two categories with row percentages, then test whether the visible gap is bigger "
              "than chance with chi-square."},
             {"t": "darkcard", "label": "Worked flow", "title": "Caste &times; toilet ownership",
              "body": "Build the cross-tab &rarr; percentage within caste &rarr; eyeball the gap "
              "&rarr; check expected counts &ge; 5 &rarr; run chi-square &rarr; report the test "
              "<em>and</em> a strength measure &rarr; resist the leap to 'caste causes&hellip;'."},
         ]},

        {"type": "content", "label": "Recap", "title": "The category &times; category toolkit",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Step", "Tool", "Answers"],
              "rows": [
                  ["Describe", "Cross-tab + % ", "What does the pattern look like?"],
                  ["Test", "Chi-square", "Is it bigger than chance?"],
                  ["Quantify strength", "Cram&eacute;r's V", "How strong is it?"],
                  ["Small table?", "Fisher's exact", "Same question, thin cells"]]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Simple Linear Regression"},

        {"type": "content", "label": "From Cloud to Line", "title": "Drawing the best line through a scatter",
         "blocks": [
             {"t": "body", "html": "Correlation gives a number for a numeric&ndash;numeric "
              "relationship. <strong>Simple linear regression</strong> goes one step further: "
              "it fits the single straight <strong>line of best fit</strong> through the scatter, "
              "summarising the relationship as an equation."},
             {"t": "term", "word": "Simple linear regression",
              "def": "Modelling a numeric response Y as a straight-line function of one numeric "
              "predictor X: Y = intercept + slope &times; X, plus error."},
         ]},

        {"type": "content", "label": "See It", "title": "A regression line over a scatter",
         "blocks": [
             {"t": "chart", "canvas": "regLineChart",
              "title": "Years of schooling vs monthly earnings, with line of best fit",
              "source": "Illustrative",
              "type": "scatter",
              "data": {"datasets": [
                  {"label": "Individuals", "type": "scatter", "backgroundColor": "#6366F1",
                   "pointRadius": 5,
                   "data": [{"x": 0, "y": 6}, {"x": 2, "y": 8}, {"x": 4, "y": 9},
                            {"x": 5, "y": 12}, {"x": 6, "y": 11}, {"x": 8, "y": 15},
                            {"x": 10, "y": 16}, {"x": 12, "y": 20}, {"x": 14, "y": 22},
                            {"x": 16, "y": 27}]},
                  {"label": "Line of best fit", "type": "line", "borderColor": "#EF4444",
                   "borderWidth": 2, "pointRadius": 0, "fill": False,
                   "data": [{"x": 0, "y": 6}, {"x": 16, "y": 26}]}]},
              "options": {"__js__": "{ scales:{ x:{ title:{display:true,text:'Years of schooling'} }, y:{ title:{display:true,text:'Earnings (₹000/month)'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The red line is the one that sits closest to "
              "all the points at once &mdash; it minimises the total squared vertical distance "
              "from points to line (least squares). Illustrative data."},
         ]},

        {"type": "content", "label": "The Equation", "title": "Y = a + bX",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "a (intercept)", "label": "Predicted Y when X = 0 &mdash; where the "
                  "line crosses the vertical axis", "color": "cyan"},
                 {"num": "b (slope)", "label": "Change in Y for each 1-unit rise in X &mdash; "
                  "the rate of the relationship", "color": "green"}]},
             {"t": "hbox", "color": "amber", "html": "The slope carries the action. Its "
              "<em>sign</em> matches the correlation's sign; its <em>size</em> is in real units "
              "of Y per unit of X."},
         ]},

        {"type": "content", "label": "Intercept Care", "title": "When the intercept is meaningless",
         "blocks": [
             {"t": "body", "html": "The intercept is the predicted Y at X = 0 &mdash; but X = 0 "
              "may be nonsensical or far outside your data. The earnings at <em>zero</em> years "
              "of schooling may be a mathematical artefact, not a real group."},
             {"t": "hbox", "color": "cyan", "html": "Interpret the intercept only when X = 0 is "
              "both meaningful and within the range of your data. Otherwise treat it as a "
              "mathematical anchor for the line."},
         ]},

        {"type": "content", "label": "Reading the Slope", "title": "What b means in plain words",
         "blocks": [
             {"t": "body", "html": "In our example the line rises about ₹1,250 per extra year "
              "of schooling (illustrative). So <strong>b &asymp; 1.25</strong> in ₹000: "
              "&lsquo;each additional year of schooling is associated with about ₹1,250 more "
              "monthly earnings.&rsquo;"},
             {"t": "hbox", "color": "red", "html": "Note the phrase <em>&lsquo;associated "
              "with&rsquo;</em>, not <em>&lsquo;causes&rsquo;</em>. Regression fits a line; it "
              "does not, by itself, license a causal claim."},
         ]},

        {"type": "content", "label": "R-squared", "title": "How much variation the line explains",
         "blocks": [
             {"t": "term", "word": "R&sup2; (coefficient of determination)",
              "def": "The proportion of the variation in Y that is explained by X through the "
              "fitted line. It runs from 0 (line explains nothing) to 1 (line explains "
              "everything). In simple regression, R&sup2; = r&sup2;."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "R&sup2; = 0.8", "label": "Line explains 80% of the variation in Y; "
                  "20% is left unexplained", "color": "green"},
                 {"num": "R&sup2; = 0.1", "label": "Line explains just 10% &mdash; X is a weak "
                  "guide to Y", "color": "amber"}]},
         ]},

        {"type": "content", "label": "R-squared Caution", "title": "High R&sup2; is not always good",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "A high R&sup2; does <strong>not</strong> prove the model is correct or causal",
                 "In social data, an R&sup2; of 0.2 can still be a useful finding",
                 "A low R&sup2; with a clear slope can still matter for policy",
                 "R&sup2; says nothing about whether a <strong>straight</strong> line fits"]},
             {"t": "hbox", "color": "amber", "html": "Report R&sup2; for context, but never let "
              "it crowd out the slope, its uncertainty, and a look at the scatter."},
         ]},

        {"type": "content", "label": "Prediction vs Explanation", "title": "Two different goals for one line",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Explanation", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Understand the <em>relationship</em>: how "
                   "does Y change with X, and how strong is it? The slope is the prize."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Prediction", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Estimate Y for a new X you haven't "
                   "measured. Accuracy, not interpretation, is the prize."}]}]},
             {"t": "hbox", "color": "green", "html": "Be clear which you are doing &mdash; the "
              "same line, read for different purposes, demands different cautions."},
         ]},

        {"type": "content", "label": "Extrapolation", "title": "Don't predict beyond your data",
         "blocks": [
             {"t": "body", "html": "<strong>Extrapolation</strong> &mdash; using the line far "
              "outside the range of X you actually observed &mdash; is one of regression's "
              "classic traps. A line fitted on 0&ndash;16 years of schooling says nothing "
              "reliable about 30 years."},
             {"t": "hbox", "color": "red", "html": "The relationship may bend, plateau or break "
              "entirely outside your data. Predict within the range you measured, and flag any "
              "step beyond it."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Pitfalls"},

        {"type": "content", "label": "The Big One", "title": "Correlation is not causation",
         "blocks": [
             {"t": "body", "html": "A relationship between two variables can arise for several "
              "reasons, only one of which is &lsquo;X causes Y&rsquo;. This is the single most "
              "important caution in all of bivariate analysis."},
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Reverse causation:</strong> Y might cause X",
                 "<strong>Confounding:</strong> a third factor C drives both",
                 "<strong>Selection:</strong> how the sample was chosen creates the link",
                 "<strong>Chance:</strong> with enough variables, some correlate by luck"]},
         ]},

        {"type": "content", "label": "Confounding", "title": "The lurking third variable",
         "blocks": [
             {"t": "body", "html": "A <strong>confounder</strong> is a variable linked to both X "
              "and Y that creates &mdash; or distorts &mdash; the relationship between them. It "
              "is the commonest reason a bivariate link is misleading."},
             {"t": "flow", "steps": [
                 "Household wealth (confounder C)",
                 "drives girls' schooling (X)",
                 "AND drives child survival (Y)",
                 "so X and Y correlate &mdash; partly via C"]},
         ]},

        {"type": "content", "label": "Why It Matters Here", "title": "Bivariate links almost always hide confounders",
         "blocks": [
             {"t": "body", "html": "Recall our literacy&ndash;fertility scatter. Female literacy "
              "really does track lower fertility &mdash; but richer states also have better "
              "health systems, later marriage and more contraception. Wealth and development "
              "confound the simple two-variable picture."},
             {"t": "hbox", "color": "amber", "html": "This is exactly why bivariate analysis is "
              "a starting point. To isolate one variable's effect you need to <em>control</em> "
              "for confounders &mdash; the job of multivariate regression."},
         ]},

        {"type": "content", "label": "Ecological Fallacy", "title": "Group patterns &ne; individual truths",
         "blocks": [
             {"t": "term", "word": "Ecological fallacy",
              "def": "Wrongly inferring something about individuals from a relationship observed "
              "only at the group (district, state) level."},
             {"t": "body", "html": "States with higher average literacy have lower average "
              "fertility &mdash; that does <em>not</em> mean the literate <em>women</em> within "
              "a state are the ones with fewer children. A relationship across districts need "
              "not hold across people."},
         ]},

        {"type": "content", "label": "Outliers &amp; Leverage", "title": "One point can swing everything",
         "blocks": [
             {"t": "body", "html": "A single extreme point can dominate a correlation or drag a "
              "regression line toward itself &mdash; high <strong>leverage</strong>. The whole "
              "&lsquo;relationship&rsquo; may rest on one unusual case."},
             {"t": "hbox", "color": "red", "html": "Always check: does the pattern survive if I "
              "remove the most extreme point? If r or the slope collapses, the finding was that "
              "one point, not a real trend."},
         ]},

        {"type": "content", "label": "Non-linearity", "title": "Straight-line tools miss curves",
         "blocks": [
             {"t": "body", "html": "Pearson's r and linear regression assume a <strong>straight "
              "line</strong>. A U-shaped or saturating relationship &mdash; common in real data "
              "&mdash; can show a near-zero correlation while being strongly, but non-linearly, "
              "related."},
             {"t": "hbox", "color": "cyan", "html": "The fix is the cheapest in statistics: "
              "<strong>plot the scatter</strong>. A curve is obvious to the eye and invisible "
              "to r."},
         ]},

        {"type": "content", "label": "Anscombe", "title": "Four datasets, identical statistics",
         "blocks": [
             {"t": "chart", "canvas": "anscombeChart",
              "title": "Anscombe-style: same r, four very different shapes",
              "source": "After F. J. Anscombe (1973)",
              "type": "scatter",
              "data": {"datasets": [
                  {"label": "Linear", "backgroundColor": "#10B981", "pointRadius": 5,
                   "data": [{"x": 4, "y": 4.3}, {"x": 5, "y": 5.7}, {"x": 6, "y": 6.1},
                            {"x": 7, "y": 6.4}, {"x": 8, "y": 7.0}, {"x": 9, "y": 8.8},
                            {"x": 10, "y": 8.0}, {"x": 11, "y": 8.3}, {"x": 13, "y": 9.9}]},
                  {"label": "Curved", "backgroundColor": "#F59E0B", "pointRadius": 5,
                   "data": [{"x": 4, "y": 5.0}, {"x": 5, "y": 6.5}, {"x": 6, "y": 7.6},
                            {"x": 7, "y": 8.3}, {"x": 8, "y": 8.8}, {"x": 9, "y": 9.0},
                            {"x": 10, "y": 8.9}, {"x": 11, "y": 8.5}, {"x": 13, "y": 6.5}]},
                  {"label": "Outlier-driven", "backgroundColor": "#EF4444", "pointRadius": 5,
                   "data": [{"x": 4, "y": 5.4}, {"x": 5, "y": 5.6}, {"x": 6, "y": 5.8},
                            {"x": 7, "y": 6.0}, {"x": 8, "y": 6.2}, {"x": 9, "y": 6.4},
                            {"x": 10, "y": 6.6}, {"x": 13, "y": 12.7}, {"x": 11, "y": 6.8}]}]},
              "options": {"__js__": "{ scales:{ x:{ title:{display:true,text:'X'} }, y:{ title:{display:true,text:'Y'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Anscombe's quartet (1973): four datasets "
              "with near-identical means, variances and correlation, yet utterly different "
              "shapes. The lesson, still true: <strong>always plot your data.</strong>"},
         ]},

        {"type": "content", "label": "Simpson's Paradox", "title": "A trend can reverse when you split",
         "blocks": [
             {"t": "body", "html": "<strong>Simpson's paradox:</strong> a relationship in the "
              "pooled data can <em>flip direction</em> within every subgroup. A scheme can look "
              "worse overall yet be better in <em>every</em> district &mdash; if districts "
              "differ in size and baseline."},
             {"t": "hbox", "color": "red", "html": "Always disaggregate before concluding. The "
              "aggregate two-variable relationship can point the opposite way to the truth."},
         ]},

        {"type": "content", "label": "Pitfall Checklist", "title": "Before you believe a relationship",
         "compact": True,
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Did I <strong>plot</strong> it &mdash; is the shape really linear?",
                 "Could a <strong>confounder</strong> explain it?",
                 "Does it survive removing the <strong>outlier</strong>?",
                 "Is this a <strong>group</strong> pattern I'm reading onto individuals?",
                 "Does it <strong>reverse</strong> when I disaggregate?",
                 "Is there a plausible <strong>mechanism</strong>, or just a coincidence?"]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Reporting, Practice &amp; Tools"},

        {"type": "content", "label": "Report Honestly", "title": "How to report a relationship",
         "blocks": [
             {"t": "bullets", "items": [
                 "State the <strong>direction</strong> and <strong>strength</strong> in plain words",
                 "Give the <strong>effect size</strong> in real units, not just a p-value",
                 "Report the <strong>uncertainty</strong> &mdash; confidence interval or range",
                 "Name the <strong>sample size</strong> and how it was drawn",
                 "Flag the obvious <strong>confounders</strong> you could not rule out"]},
         ]},

        {"type": "content", "label": "Causal Language", "title": "Mind your verbs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Safe phrasing", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "&lsquo;is associated with&rsquo;",
                      "&lsquo;tends to go with&rsquo;",
                      "&lsquo;is correlated with&rsquo;"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Reserve for evidence", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "&lsquo;causes&rsquo;",
                      "&lsquo;leads to&rsquo;",
                      "&lsquo;increases / reduces&rsquo;"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Causal verbs need a causal design &mdash; "
              "an experiment or a careful quasi-experiment. A bivariate correlation does not "
              "earn them."},
         ]},

        {"type": "content", "label": "Common Sins", "title": "What to avoid in write-ups",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Reporting a p-value with <strong>no effect size</strong>",
                 "Claiming <strong>causation</strong> from a correlation",
                 "Hiding the <strong>scatter</strong> behind a single coefficient",
                 "Testing many pairs and reporting only the <strong>one that worked</strong>",
                 "Using a state-level relationship to make <strong>individual</strong> claims"]},
         ]},

        {"type": "content", "label": "A Worked Habit", "title": "A reliable bivariate workflow",
         "blocks": [
             {"t": "flow", "steps": [
                 "CLASSIFY: what type is each variable?",
                 "PLOT: scatter, box plot or bars",
                 "DESCRIBE: direction, strength, shape",
                 "TEST: the matching method",
                 "INTERPRET: effect size + uncertainty",
                 "CAUTION: confounders, fallacies"]},
             {"t": "hbox", "color": "green", "html": "Six steps, every time. The discipline is "
              "what turns a number into a defensible finding."},
         ]},

        {"type": "content", "label": "Tools", "title": "Software for bivariate analysis",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Good for", "Note"],
              "rows": [
                  ["Excel / Google Sheets", "Cross-tabs, scatter, CORREL, t-test", "Start here; pivot tables for cross-tabs"],
                  ["R", "Every test, publication graphics", "Free; cor.test, t.test, aov, chisq.test, lm"],
                  ["Python (pandas, scipy, statsmodels)", "Cleaning + tests + regression", "Free, general-purpose"],
                  ["Jamovi / JASP", "Point-and-click stats", "Free, friendly for learners"],
                  ["Stata / SPSS", "Survey data, weights", "Common in research shops"]]},
             {"t": "hbox", "color": "cyan", "html": "Tools matter less than habits: classify, "
              "plot, then test. A clear scatter in a spreadsheet beats a misread coefficient "
              "in any package."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Statistics</em> &mdash; Freedman, Pisani &amp; Purves (the gold standard primer)",
                 "<em>The Art of Statistics</em> &mdash; David Spiegelhalter",
                 "<em>How to Lie with Statistics</em> &mdash; Darrell Huff",
                 "<em>Naked Statistics</em> &mdash; Charles Wheelan",
                 "<em>Mostly Harmless Econometrics</em> &mdash; Angrist &amp; Pischke (going causal)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Exploratory Data Analysis</strong> and "
              "<strong>Research Methods</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Classify both variables first</strong> &mdash; it picks the method",
                 "<strong>Plot before you compute</strong> &mdash; shape, outliers, curves",
                 "<strong>Report effect size, not just the p-value</strong>",
                 "<strong>Correlation is not causation</strong> &mdash; hunt the confounder",
                 "<strong>Group patterns are not individual truths</strong> &mdash; mind the fallacies"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Bivariate Analysis 101 &middot; Complete",
         "headline": "Two variables.<br>One honest story.",
         "byline": "Classify, plot, test, and resist the leap to cause. Every relationship in your "
                   "data deserves that discipline. Explore the rest of the ImpactMojo 101 Series, "
                   "free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
