# -*- coding: utf-8 -*-
"""
Exploratory Data Analysis 101 — ImpactMojo 101 Series (native deck spec)
EDA for development practitioners working with household survey data in South Asia.
Build: python3 scripts/deck-builder/build.py eda_hhs
"""

DECK = {
    "slug": "eda-hhs",
    "title": "Exploratory Data Analysis 101",
    "description": ("Exploratory Data Analysis 101 — a free foundational course for "
                    "development practitioners in South Asia. Inspect, clean, describe, "
                    "visualise and question household survey data &mdash; from NSS, PLFS "
                    "and NFHS structure to missingness, outliers, survey weights and "
                    "honest visuals. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Exploratory<br>Data<br>Analysis 101",
         "sub": "Inspecting, Cleaning &amp; Questioning Household Survey Data &mdash; a "
                "Foundational Course for Development Practitioners in South Asia",
         "tags": ["Household Surveys", "South Asia Focus", "~90 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What EDA Is &amp; Why", "slides": "Slides 3&ndash;10"},
             {"name": "Household Survey Data in India", "slides": "Slides 11&ndash;21"},
             {"name": "The EDA Workflow", "slides": "Slides 22&ndash;29"},
             {"name": "Knowing Your Variables", "slides": "Slides 30&ndash;38"},
             {"name": "Univariate Exploration", "slides": "Slides 39&ndash;48"},
             {"name": "Spotting Trouble", "slides": "Slides 49&ndash;58"},
             {"name": "Bivariate &amp; Multivariate", "slides": "Slides 59&ndash;68"},
             {"name": "Survey Weights &amp; Design", "slides": "Slides 69&ndash;77"},
             {"name": "Visual EDA Done Well", "slides": "Slides 78&ndash;85"},
             {"name": "From EDA to Questions", "slides": "Slides 86&ndash;93"},
             {"name": "Tools &amp; Reproducibility", "slides": "Slides 94&ndash;99"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What EDA Is &amp; Why"},

        {"type": "content", "label": "Definition", "title": "Look before you leap",
         "blocks": [
             {"t": "body", "html": "Before you fit a model, build an index or write a "
              "finding, you must <strong>look at the data</strong>. Exploratory Data "
              "Analysis (EDA) is the open-minded first pass &mdash; describing, plotting and "
              "questioning a dataset to understand its shape, gaps and surprises."},
             {"t": "term", "word": "Exploratory Data Analysis (EDA)",
              "def": "An attitude and a toolkit for examining data with few prior "
              "assumptions &mdash; using summaries and pictures to reveal structure, spot "
              "problems and generate questions, before any formal testing or modelling."},
             {"t": "hbox", "color": "cyan", "html": "EDA is detective work, not "
              "decoration. You are interrogating the data to find out what it can &mdash; "
              "and cannot &mdash; honestly say."},
         ]},

        {"type": "content", "label": "The Origin", "title": "Tukey and the case for exploring",
         "blocks": [
             {"t": "quote",
              "text": "Exploratory data analysis is an attitude, a flexibility, and a "
              "reliance on display, not a bundle of techniques.",
              "attr": "&mdash; John W. Tukey, who named EDA in 1977"},
             {"t": "body", "html": "Tukey argued that statistics had become obsessed with "
              "<em>confirming</em> hypotheses and neglected the prior, humbler task of "
              "<em>finding</em> them. EDA restored looking, sketching and questioning to "
              "the centre of data work."},
         ]},

        {"type": "content", "label": "Confirm vs Explore", "title": "Two modes of data work",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Exploratory", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Open-ended. <em>What is going on "
                   "here?</em> Generates questions and hypotheses. Forgiving of surprises. "
                   "Where every project should start."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Confirmatory", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Pre-specified. <em>Is this specific "
                   "claim true?</em> Tests a hypothesis fixed in advance. Where EDA "
                   "<em>leads</em>, but is not the same step."}]}]},
             {"t": "hbox", "color": "red", "html": "Danger: do not let exploration "
              "masquerade as confirmation. A pattern you found by digging is a "
              "<em>hypothesis</em> to test on fresh data, not a proven result."},
         ]},

        {"type": "content", "label": "Let It Speak", "title": "Let the data speak first",
         "blocks": [
             {"t": "body", "html": "Practitioners often arrive with a story they want the "
              "data to confirm. EDA asks you to hold that story loosely and let the numbers "
              "talk back &mdash; to notice the variable that is half missing, the district "
              "that behaves oddly, the impossible age."},
             {"t": "quote",
              "text": "The greatest value of a picture is when it forces us to notice what "
              "we never expected to see.",
              "attr": "&mdash; John W. Tukey"},
         ]},

        {"type": "content", "label": "Understand First", "title": "Understand before you model",
         "blocks": [
             {"t": "flow", "steps": [
                 "EXPLORE: what is in this dataset? what is wrong with it?",
                 "DESCRIBE: distributions, gaps, relationships",
                 "QUESTION: what hypotheses does this suggest?",
                 "ONLY THEN: model, test, conclude"]},
             {"t": "hbox", "color": "amber", "html": "Skipping EDA is how analysts end up "
              "modelling a coding error, averaging a top-coded variable, or reporting on a "
              "subgroup that is mostly missing data."},
         ]},

        {"type": "content", "label": "Why It Pays", "title": "What good EDA catches early",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Errors</strong> &mdash; impossible ages, negative incomes, "
                 "duplicated households",
                 "<strong>Gaps</strong> &mdash; a variable missing for 30% of women, not at random",
                 "<strong>Shape</strong> &mdash; consumption is skewed, so the mean misleads",
                 "<strong>Structure</strong> &mdash; the survey is clustered and weighted, "
                 "not a simple random sample",
                 "<strong>Surprises</strong> &mdash; the outlier district that is the real story"]},
             {"t": "hbox", "color": "green", "html": "Every hour of EDA saves a day of "
              "rework &mdash; and prevents a wrong number reaching a decision."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Foundations", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Indian household survey data",
                      "The EDA workflow",
                      "Variables, codebooks &amp; measurement"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Practice", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Univariate, bivariate &amp; multivariate views",
                      "Missingness, outliers, weights",
                      "Honest visuals &amp; reproducible tools"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Throughout, the data you meet is "
              "patterned on India's NSS, PLFS and NFHS &mdash; the surveys you will actually "
              "open at work."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Household Survey Data in India"},

        {"type": "content", "label": "The Unit", "title": "What is a household survey?",
         "blocks": [
             {"t": "term", "word": "Household survey",
              "def": "A survey that samples dwellings (households), then collects "
              "information about the household as a whole and about each member &mdash; "
              "the workhorse design behind NSS, PLFS, NFHS and most development data."},
             {"t": "body", "html": "Because so much of welfare &mdash; consumption, "
              "sanitation, who eats, who decides &mdash; happens at the household level, "
              "the household is the natural sampling unit. But many questions are about "
              "<em>people</em> within it."},
         ]},

        {"type": "content", "label": "Structure", "title": "Two rosters: households and members",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Household roster", "blocks": [
                  {"t": "body", "cls": "sm", "html": "One row per <strong>household</strong>: "
                   "assets, dwelling type, water source, ration card, total members. Keyed "
                   "by a household ID."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Member roster", "blocks": [
                  {"t": "body", "cls": "sm", "html": "One row per <strong>person</strong>: "
                   "age, sex, relation to head, education, work, health. Keyed by household "
                   "ID + person line number."}]}]},
             {"t": "hbox", "color": "amber", "html": "EDA must respect this hierarchy. "
              "Household-level and person-level variables live in different files and must "
              "be merged on the household ID before you can analyse them together."},
         ]},

        {"type": "content", "label": "Long &amp; Wide", "title": "Hierarchical data is nested",
         "blocks": [
             {"t": "table",
              "head": ["HH ID", "Person line", "Age", "Sex", "Education"],
              "rows": [
                  ["10231", "1", "44", "Male", "Secondary"],
                  ["10231", "2", "40", "Female", "Primary"],
                  ["10231", "3", "16", "Female", "Secondary"],
                  ["10231", "4", "11", "Male", "Primary"],
                  ["10232", "1", "67", "Female", "None"]]},
             {"t": "hbox", "color": "cyan", "html": "Four rows, one household (10231). To "
              "count households you need unique HH IDs; to count people you count rows. "
              "Confusing the two is a classic early error."},
         ]},

        {"type": "content", "label": "The Big Three", "title": "India's major household surveys",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Survey", "What it covers", "Who runs it", "Frequency"],
              "rows": [
                  ["NSS (consumption, etc.)", "Consumption expenditure, employment, social "
                   "consumption", "NSSO / MoSPI", "Rounds (subject rotates)"],
                  ["PLFS", "Labour force: work, unemployment, wages", "NSSO / MoSPI",
                   "Annual since 2017&ndash;18"],
                  ["NFHS", "Health, nutrition, fertility, anaemia, women's status", "IIPS / MoHFW",
                   "~5 yrs (NFHS-5: 2019&ndash;21)"],
                  ["CMIE-CPHS", "Household income, consumption, sentiment", "CMIE (private)",
                   "Continuous, 3 waves/yr"]]},
             {"t": "hbox", "color": "amber", "html": "Know these by name and by job. The "
              "right survey for a question depends on what it measures and how recently."},
         ]},

        {"type": "content", "label": "NSS &amp; PLFS", "title": "NSS and PLFS: the official workhorses",
         "blocks": [
             {"t": "body", "html": "The <strong>National Sample Survey (NSS)</strong> has "
              "measured consumption and employment for decades. The <strong>Periodic Labour "
              "Force Survey (PLFS)</strong> took over labour statistics in "
              "<strong>2017&ndash;18</strong>, giving annual rural and quarterly urban "
              "estimates."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "NSS", "label": "Consumption &amp; expenditure rounds underpin "
                  "official poverty estimates", "color": "cyan",
                  "source": "NSSO / MoSPI"},
                 {"num": "Annual", "label": "PLFS gives the labour force participation and "
                  "unemployment rates since 2017&ndash;18", "color": "indigo",
                  "source": "PLFS, MoSPI"}]},
         ]},

        {"type": "content", "label": "NFHS", "title": "NFHS: health, nutrition and gender",
         "blocks": [
             {"t": "body", "html": "The <strong>National Family Health Survey</strong> is "
              "India's Demographic and Health Survey. <strong>NFHS-5 (2019&ndash;21)</strong> "
              "covered the health, nutrition and demographic situation of women, children and "
              "households across every district."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "~636,000", "label": "households interviewed in NFHS-5", "color": "cyan",
                  "source": "NFHS-5, 2019&ndash;21"},
                 {"num": "707", "label": "districts covered", "color": "green",
                  "source": "IIPS / MoHFW"},
                 {"num": "5", "label": "rounds since 1992&ndash;93", "color": "indigo",
                  "source": "IIPS"}]},
         ]},

        {"type": "content", "label": "CMIE-CPHS", "title": "CMIE-CPHS: high-frequency private data",
         "blocks": [
             {"t": "body", "html": "The <strong>Consumer Pyramids Household Survey "
              "(CPHS)</strong>, run by the private firm CMIE, tracks a large panel of "
              "households continuously, giving fast readings on income, spending and "
              "unemployment between official rounds."},
             {"t": "hbox", "color": "amber", "html": "Useful for timeliness, but debated on "
              "sampling and representativeness. Treat it as complementary to &mdash; not a "
              "replacement for &mdash; the official surveys, and read the methodology critics."},
         ]},

        {"type": "content", "label": "Unit of Analysis", "title": "Decide your unit before you compute",
         "blocks": [
             {"t": "body", "html": "The <strong>unit of analysis</strong> is the entity each "
              "row of your working table represents &mdash; a household, a person, a child "
              "under five, a woman aged 15&ndash;49. Every statistic is implicitly 'per' some unit."},
             {"t": "hbox", "color": "red", "html": "A rate like the anaemia prevalence is "
              "<em>per eligible person</em>, not per household. Computing it on the household "
              "file, or without restricting to the eligible group, gives the wrong answer."},
         ]},

        {"type": "content", "label": "Design", "title": "These are not simple random samples",
         "blocks": [
             {"t": "flow", "steps": [
                 "STRATIFY: split by state &times; rural/urban",
                 "STAGE 1: sample villages / urban blocks (clusters)",
                 "STAGE 2: sample households within each cluster",
                 "RESULT: a stratified, multistage, clustered sample"]},
             {"t": "hbox", "color": "cyan", "html": "Because selection happens in stages and "
              "some groups are over-sampled, every household carries a <strong>survey "
              "weight</strong>. We return to weights in Section Eight &mdash; they change "
              "your EDA."},
         ]},

        {"type": "content", "label": "First Look", "title": "What to check the moment a file opens",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "How many rows, and what is one row &mdash; a household or a person?",
                 "Is there a household ID, a person line number, a weight variable?",
                 "Which file is the household roster, which the member roster?",
                 "What does the documentation say the unit and reference period are?"]},
             {"t": "hbox", "color": "amber", "html": "Read the survey's report and "
              "documentation <em>before</em> the data. Five minutes there saves hours of "
              "confusion later."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The EDA Workflow"},

        {"type": "content", "label": "The Loop", "title": "Six steps, repeated",
         "blocks": [
             {"t": "flow", "steps": [
                 "LOAD: read the data correctly",
                 "INSPECT: structure, types, size",
                 "CLEAN: codes, gaps, impossible values",
                 "DESCRIBE: summaries per variable",
                 "VISUALISE: plot distributions &amp; relations",
                 "QUESTION: form hypotheses, then loop back"]},
             {"t": "hbox", "color": "cyan", "html": "EDA is iterative, not linear. Each plot "
              "raises a question that sends you back to inspect or clean. Expect to go round "
              "this loop many times."},
         ]},

        {"type": "content", "label": "Load", "title": "Step 1 &mdash; load it right",
         "blocks": [
             {"t": "bullets", "items": [
                 "Read the right file format &mdash; fixed-width, CSV, .dta, .sav, .csv.gz",
                 "Make sure ID and code columns load as <strong>text</strong>, not numbers "
                 "(leading zeros vanish otherwise)",
                 "Preserve special missing codes; do not let them become real values",
                 "Check the row count against the documentation"]},
             {"t": "hbox", "color": "red", "html": "A household ID like 0457 silently "
              "becoming 457 will break every merge. Type matters from the very first line."},
         ]},

        {"type": "content", "label": "Inspect", "title": "Step 2 &mdash; inspect the skeleton",
         "blocks": [
             {"t": "table",
              "head": ["Question", "What you are checking"],
              "rows": [
                  ["How many rows &amp; columns?", "Size and whether the file is complete"],
                  ["What type is each column?", "Numeric, text, date, categorical codes"],
                  ["What is the range of each?", "Min, max, plausibility"],
                  ["How many distinct values?", "Categorical levels, accidental duplicates"],
                  ["How many missing per column?", "Where the gaps are"]]},
             {"t": "hbox", "color": "cyan", "html": "This is the data-equivalent of a "
              "doctor's first examination &mdash; vital signs before any diagnosis."},
         ]},

        {"type": "content", "label": "Clean", "title": "Step 3 &mdash; clean transparently",
         "blocks": [
             {"t": "body", "html": "Cleaning means standardising codes, recoding missing "
              "values, fixing types and flagging impossible entries &mdash; <strong>in a "
              "script, never by hand-editing the raw file.</strong>"},
             {"t": "hbox", "color": "green", "html": "Golden rule: keep the raw extract "
              "read-only. Every change lives in code, so it is documented, reversible and "
              "reproducible. We expand on this in Section Eleven."},
         ]},

        {"type": "content", "label": "Describe", "title": "Step 4 &mdash; describe every variable",
         "blocks": [
             {"t": "bullets", "items": [
                 "For <strong>continuous</strong> variables: min, max, mean, median, "
                 "quartiles, SD, % missing",
                 "For <strong>categorical</strong> variables: a frequency table of every level",
                 "Flag anything that looks impossible or surprising for a second look",
                 "Always describe <em>before</em> you visualise &mdash; numbers anchor the eye"]},
         ]},

        {"type": "content", "label": "Visualise", "title": "Step 5 &mdash; plot to see the shape",
         "blocks": [
             {"t": "body", "html": "Summaries can hide as much as they reveal. A histogram "
              "shows skew and bimodality a mean cannot; a scatter shows a curved relationship "
              "a correlation cannot. <strong>Always plot.</strong>"},
             {"t": "quote",
              "text": "Numerical calculations are exact, but graphs are rough.",
              "attr": "&mdash; John W. Tukey &mdash; and we need both"},
         ]},

        {"type": "content", "label": "Question", "title": "Step 6 &mdash; turn findings into questions",
         "blocks": [
             {"t": "body", "html": "Good EDA ends not with answers but with sharper "
              "<strong>questions</strong>: why is consumption bimodal here? why is this "
              "variable missing more for women? is the district outlier real or an error?"},
             {"t": "hbox", "color": "amber", "html": "Write the questions down. They become "
              "your analysis plan &mdash; and the line between what EDA suggested and what a "
              "later test confirmed."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Knowing Your Variables"},

        {"type": "content", "label": "The Key", "title": "The data dictionary is your map",
         "blocks": [
             {"t": "term", "word": "Data dictionary / codebook",
              "def": "The document that defines every variable: its name, meaning, units, "
              "allowed values, the codes for each category, the special missing codes, and "
              "who it applies to."},
             {"t": "hbox", "color": "red", "html": "A survey dataset without its codebook is "
              "a locked box. The number '2' could mean female, urban, 'no', or a missing "
              "code &mdash; only the dictionary tells you which."},
         ]},

        {"type": "content", "label": "Read It First", "title": "What the codebook tells you",
         "blocks": [
             {"t": "table",
              "head": ["Codebook field", "Why EDA needs it"],
              "rows": [
                  ["Variable label", "What it actually measures"],
                  ["Value codes", "1 = yes, 2 = no, 9 = missing"],
                  ["Units", "Rupees? months? per week?"],
                  ["Universe / who answers", "Only women 15&ndash;49? only workers?"],
                  ["Reference period", "Last 7 days? last 30? last year?"],
                  ["Skip patterns", "Why a block is blank for some rows"]]},
             {"t": "hbox", "color": "amber", "html": "The 'universe' field explains most "
              "'missing' data: a question about pregnancy is blank for men by design, not by error."},
         ]},

        {"type": "content", "label": "Levels", "title": "Four levels of measurement",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Level", "Meaning", "Survey example", "Valid maths"],
              "rows": [
                  ["Nominal", "Labels, no order", "Religion, state, ration-card type", "Counts, mode"],
                  ["Ordinal", "Ordered, unequal gaps", "Education level, wealth quintile", "Median, rank"],
                  ["Interval", "Equal gaps, no true zero", "Year of birth", "Mean, difference"],
                  ["Ratio", "Equal gaps, true zero", "Age, income, consumption", "All, ratios"]]},
             {"t": "hbox", "color": "red", "html": "The level decides which statistics are "
              "legal. You cannot average religion codes, and a wealth quintile is a rank "
              "(1&ndash;5), not a rupee amount."},
         ]},

        {"type": "content", "label": "Categorical vs Continuous", "title": "The first sort: categories or measures",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Categorical", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A fixed set of labels &mdash; sex, "
                   "caste category, district, employment status. You <strong>count</strong> "
                   "and <strong>tabulate</strong> these."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Continuous", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A measured quantity &mdash; age, "
                   "income, MPCE, height. You take <strong>means, medians</strong> and "
                   "<strong>histograms</strong> of these."}]}]},
             {"t": "hbox", "color": "amber", "html": "Watch the trap of <strong>coded "
              "categoricals</strong>: education stored as 1&ndash;8 looks numeric, but its "
              "mean is meaningless. Check the codebook, not the column type."},
         ]},

        {"type": "content", "label": "Coded Numbers", "title": "Numbers that are really labels",
         "blocks": [
             {"t": "body", "html": "Survey files store almost everything as numbers to save "
              "space. <strong>State = 9</strong> means Uttar Pradesh, not the quantity nine. "
              "Treating such codes as measurements is one of the commonest EDA errors."},
             {"t": "hbox", "color": "red", "html": "Before computing any mean, ask: is this a "
              "<em>quantity</em> or a <em>code</em>? The dictionary, not the data type, "
              "decides."},
         ]},

        {"type": "content", "label": "Special Codes", "title": "Missing codes hide in plain sight",
         "blocks": [
             {"t": "table",
              "head": ["Code", "Often means", "Risk if treated as a value"],
              "rows": [
                  ["99 / 999", "Not known / not stated", "Inflates the mean enormously"],
                  ["97 / 98", "Refused / not applicable", "Phantom category in tables"],
                  ["0", "Sometimes a real zero, sometimes 'none'", "Ambiguous &mdash; check codebook"],
                  ["Blank", "Skip pattern or true missing", "Silent loss of cases"]]},
             {"t": "hbox", "color": "amber", "html": "Recode special codes to explicit "
              "missing <em>before</em> any summary. A mean income of ₹1,400 lakh usually "
              "means a 9999999 'not stated' code slipped through."},
         ]},

        {"type": "content", "label": "Derived Variables", "title": "Variables you build yourself",
         "blocks": [
             {"t": "body", "html": "Much of EDA involves <strong>deriving</strong> variables: "
              "monthly per-capita consumption from total expenditure and household size; age "
              "groups from age; a binary 'has toilet' from a coded sanitation variable."},
             {"t": "hbox", "color": "cyan", "html": "Derive in a script, label the new "
              "variable clearly, and sanity-check its distribution. A derived variable "
              "inherits every error in its inputs."},
         ]},

        {"type": "content", "label": "Profiling", "title": "Build a variable profile",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Name and meaning (from the codebook)",
                 "Type: categorical or continuous; level of measurement",
                 "Range or set of levels; special missing codes",
                 "Universe: who is supposed to have a value",
                 "% missing, and whether the missingness looks patterned"]},
             {"t": "hbox", "color": "amber", "html": "A one-line profile per variable, "
              "written as you go, is the backbone of trustworthy analysis."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Univariate Exploration"},

        {"type": "content", "label": "One at a Time", "title": "Start with one variable",
         "blocks": [
             {"t": "body", "html": "<strong>Univariate</strong> exploration looks at each "
              "variable on its own &mdash; its frequencies, its distribution, its centre and "
              "spread. It is where most data problems first surface."},
             {"t": "flow", "steps": [
                 "CATEGORICAL: frequency table, bar chart",
                 "CONTINUOUS: histogram, density, summary stats",
                 "BOTH: count and inspect the missing"]},
         ]},

        {"type": "content", "label": "Frequency Tables", "title": "Count every level",
         "blocks": [
             {"t": "table",
              "head": ["Sanitation facility", "Households", "%"],
              "rows": [
                  ["Improved, not shared", "6,420", "64.2"],
                  ["Improved, shared", "1,180", "11.8"],
                  ["Unimproved", "910", "9.1"],
                  ["Open defecation", "1,390", "13.9"],
                  ["Not stated", "100", "1.0"]]},
             {"t": "hbox", "color": "cyan", "html": "Illustrative, patterned on NFHS-style "
              "categories. A frequency table is the first thing to run on any categorical "
              "variable &mdash; it reveals tiny categories, typos and stray codes at a glance."},
         ]},

        {"type": "content", "label": "Histograms", "title": "The histogram of a skewed variable",
         "blocks": [
             {"t": "chart", "canvas": "mpceHist",
              "title": "Monthly per-capita consumption expenditure (MPCE), illustrative",
              "source": "Illustrative, patterned on NSS consumption distributions",
              "type": "bar",
              "data": {"labels": ["0&ndash;1k", "1&ndash;2k", "2&ndash;3k", "3&ndash;4k",
                                  "4&ndash;5k", "5&ndash;6k", "6&ndash;8k", "8&ndash;10k",
                                  "10&ndash;15k", "15k+"],
                       "datasets": [{"label": "Households (%)",
                                     "data": [6, 19, 24, 18, 12, 8, 6, 3, 2.5, 1.5],
                                     "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'MPCE band (₹/month)'} }, y:{ title:{display:true,text:'% of households'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Note the long right tail. Consumption, "
              "like income and landholding, is <strong>right-skewed</strong> &mdash; a few "
              "households spend many times the typical amount."},
         ]},

        {"type": "content", "label": "Reading Shape", "title": "What a histogram reveals",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Centre:</strong> where the bulk of households sit",
                 "<strong>Spread:</strong> how wide the distribution is",
                 "<strong>Skew:</strong> a long tail on one side",
                 "<strong>Modes:</strong> one peak, or two (a hidden subgroup?)",
                 "<strong>Gaps &amp; spikes:</strong> heaping at round numbers, or a wall at a top-code"]},
             {"t": "hbox", "color": "cyan", "html": "The bin width matters: too wide hides "
              "structure, too narrow shows noise. Try a few widths before you conclude."},
         ]},

        {"type": "content", "label": "Density", "title": "Density: the smoothed histogram",
         "blocks": [
             {"t": "body", "html": "A <strong>density plot</strong> smooths the histogram "
              "into a curve, making it easier to compare shapes &mdash; for example, the "
              "consumption distribution for rural versus urban households on one set of axes."},
             {"t": "hbox", "color": "amber", "html": "Smoothing is a choice: too much "
              "smoothing erases real peaks; too little invents them. Treat the curve as one "
              "view, not the truth &mdash; and keep the histogram alongside."},
         ]},

        {"type": "content", "label": "Summary Stats", "title": "The five-number summary",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Min &amp; Max", "label": "the extremes &mdash; sanity-check both", "color": "cyan"},
                 {"num": "Q1, Median, Q3", "label": "the middle and the quartiles", "color": "green"},
                 {"num": "IQR", "label": "Q3 &minus; Q1: the robust spread of the middle 50%", "color": "indigo"}]},
             {"t": "hbox", "color": "cyan", "html": "Tukey's five-number summary (min, Q1, "
              "median, Q3, max) describes a distribution without assuming any shape &mdash; "
              "the heart of EDA."},
         ]},

        {"type": "content", "label": "Mean vs Median", "title": "For skewed money, trust the median",
         "blocks": [
             {"t": "chart", "canvas": "meanMedianMpce",
              "title": "Mean is pulled above the median by the right tail (illustrative)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["Median MPCE", "Mean MPCE"],
                       "datasets": [{"label": "₹/month",
                                     "data": [2850, 3680],
                                     "backgroundColor": ["#10B981", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'₹ per capita / month'}, beginAtZero:true } } }"}},
             {"t": "hbox", "color": "amber", "html": "The mean sits well above the median "
              "because the long tail of high spenders drags it up. For consumption, income "
              "and land, <strong>report the median</strong>."},
         ]},

        {"type": "content", "label": "Skew", "title": "Naming the skew",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Right-skewed", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Long tail to the <em>right</em>. Mean "
                   "&gt; median. Income, MPCE, landholding, firm size. The common case in "
                   "development data."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Left-skewed", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Long tail to the <em>left</em>. Mean "
                   "&lt; median. Rarer &mdash; e.g. age at death in a high-survival "
                   "population."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Skew is a signal, not a defect. It tells "
              "you which centre to report and warns you off methods that assume symmetry."},
         ]},

        {"type": "content", "label": "Transforms", "title": "The log scale tames the tail",
         "blocks": [
             {"t": "body", "html": "For strongly right-skewed money variables, plotting on a "
              "<strong>logarithmic</strong> scale spreads the squashed low values and pulls "
              "in the tail, often revealing a near-symmetric shape that is easier to read."},
             {"t": "hbox", "color": "amber", "html": "A transform is an exploratory lens, not "
              "a fact about the world. Always label the axis as logged, and remember to back-"
              "transform before reporting rupee figures."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Spotting Trouble"},

        {"type": "content", "label": "The Watchlist", "title": "What can be wrong with a column",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Problem", "Survey example", "How EDA spots it"],
              "rows": [
                  ["Missing values", "Income blank for some", "Count of NA per variable"],
                  ["Impossible values", "Age = 230, &minus;3 children", "Min/max range check"],
                  ["Special codes as data", "99 = 'not stated'", "Spike at 99 in histogram"],
                  ["Top-coding", "Income capped at a max", "Wall of cases at the ceiling"],
                  ["Heaping", "Ages bunched at 0, 5, 10", "Comb pattern in histogram"],
                  ["Duplicates", "Same HH twice", "Duplicate household IDs"]]},
         ]},

        {"type": "content", "label": "Missingness", "title": "Map where the gaps are",
         "blocks": [
             {"t": "chart", "canvas": "missChart",
              "title": "Share of records missing, by variable (illustrative)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["Age", "Sex", "Education", "Income", "Land area",
                                  "Anaemia (women)", "Phone no."],
                       "datasets": [{"label": "% missing",
                                     "data": [0.2, 0.1, 2.4, 18.6, 11.0, 6.5, 31.0],
                                     "backgroundColor": ["#10B981", "#10B981", "#10B981",
                                                         "#F59E0B", "#F59E0B", "#F59E0B",
                                                         "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'% of records missing'}, beginAtZero:true } } }"}},
             {"t": "hbox", "color": "amber", "html": "A missingness bar chart across "
              "variables is one of the most useful EDA plots. Income and 'not applicable' "
              "fields are usually the worst &mdash; and that is rarely random."},
         ]},

        {"type": "content", "label": "Why Missing", "title": "Why a value is missing matters most",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>By design (skip):</strong> the question did not apply &mdash; not a problem",
                 "<strong>Missing at random:</strong> gaps unrelated to the value &mdash; least harmful",
                 "<strong>Missing not at random:</strong> the richest refuse to state income "
                 "&mdash; this <em>biases</em> results"]},
             {"t": "hbox", "color": "red", "html": "Dropping rows with gaps can quietly "
              "delete the very households you care about. Before deleting or filling, ask "
              "<em>why</em> the value is absent &mdash; the pattern of absence is itself data."},
         ]},

        {"type": "content", "label": "Missingness Patterns", "title": "Look for structure in the gaps",
         "blocks": [
             {"t": "body", "html": "Cross-tabulate missingness against other variables: is "
              "income missing more for richer households? is a health variable missing more "
              "in one state? Patterned missingness is a finding, not just a nuisance."},
             {"t": "hbox", "color": "cyan", "html": "Create a 'missing flag' variable and "
              "explore <em>it</em> like any other &mdash; who is missing, and how do they "
              "differ from who is present?"},
         ]},

        {"type": "content", "label": "Outliers", "title": "Outliers: error, or the story?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Could be an error", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Age 230, a household of 60, income of "
                   "₹0 with five earners &mdash; check for a data-entry slip or a stray code "
                   "before analysing."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Could be the story", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The one district with triple the "
                   "stunting rate may be exactly where the programme is needed. Do not delete "
                   "it &mdash; investigate it."}]}]},
             {"t": "hbox", "color": "amber", "html": "Never silently drop outliers. Flag "
              "them, explain them, and decide transparently &mdash; and record it in the EDA log."},
         ]},

        {"type": "content", "label": "Finding Outliers", "title": "Rules of thumb for flagging extremes",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<strong>Range checks:</strong> can this value exist at all? (% in 0&ndash;100)",
                 "<strong>IQR rule:</strong> flag points beyond Q1 &minus; 1.5&times;IQR or "
                 "Q3 + 1.5&times;IQR",
                 "<strong>Logic checks:</strong> a 6-year-old cannot be married with children",
                 "<strong>Visual:</strong> the point detached from the cloud in a scatter"]},
             {"t": "hbox", "color": "cyan", "html": "These rules <em>flag</em> candidates for "
              "human review. They do not <em>decide</em> &mdash; judgement, not a threshold, "
              "removes a value."},
         ]},

        {"type": "content", "label": "Impossible Values", "title": "Logic the data must obey",
         "blocks": [
             {"t": "table",
              "head": ["Rule", "Violation to flag"],
              "rows": [
                  ["Age between 0 and ~110", "Age = 230, age = &minus;1"],
                  ["Percentages in 0&ndash;100", "Vaccination = 140%"],
                  ["Members &ge; earners", "8 earners in a 4-person household"],
                  ["Mother older than child", "Mother 14, child 10"],
                  ["Consumption &gt; 0", "MPCE = 0 with members present"]]},
             {"t": "hbox", "color": "red", "html": "Codify these checks once and re-run them "
              "on every extract. Built-in validation beats hoping you will notice."},
         ]},

        {"type": "content", "label": "Top-Coding", "title": "Top-coding: the artificial ceiling",
         "blocks": [
             {"t": "term", "word": "Top-coding",
              "def": "Capping a variable at a maximum value to protect privacy or limit "
              "outliers &mdash; e.g. all incomes above ₹10 lakh recorded as exactly ₹10 lakh. "
              "It creates a spike of identical values at the ceiling."},
             {"t": "hbox", "color": "amber", "html": "Top-coding makes the mean and the upper "
              "tail unreliable. Spot it as a wall of cases at one value, and note that you "
              "<em>cannot</em> study the top accurately from such data."},
         ]},

        {"type": "content", "label": "Before / After", "title": "Cleaning changes the picture",
         "blocks": [
             {"t": "chart", "canvas": "cleanChart",
              "title": "Age distribution before and after removing impossible values (illustrative)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["0&ndash;14", "15&ndash;29", "30&ndash;44", "45&ndash;59",
                                  "60&ndash;74", "75&ndash;110", "Impossible (&gt;110)"],
                       "datasets": [
                           {"label": "Before cleaning",
                            "data": [26, 28, 21, 14, 8, 2.5, 0.5],
                            "backgroundColor": "#EF4444"},
                           {"label": "After cleaning",
                            "data": [26, 28, 21, 14, 8, 3, 0],
                            "backgroundColor": "#10B981"}]},
              "options": {"__js__": "{ plugins:{legend:{display:true}}, scales:{ y:{ title:{display:true,text:'% of people'}, beginAtZero:true } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The impossible '&gt;110' sliver vanishes "
              "after recoding it to missing. Small in count, but it would have distorted any "
              "mean age &mdash; and revealed a data-entry problem worth reporting."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Bivariate &amp; Multivariate Exploration"},

        {"type": "content", "label": "Two at a Time", "title": "Now look at variables together",
         "blocks": [
             {"t": "body", "html": "<strong>Bivariate</strong> exploration asks how two "
              "variables move together; <strong>multivariate</strong> brings in a third. This "
              "is where relationships, gaps and confounders start to appear."},
             {"t": "flow", "steps": [
                 "CAT &times; CAT: cross-tabulation",
                 "CAT &times; CONTINUOUS: grouped summaries",
                 "CONTINUOUS &times; CONTINUOUS: scatter plot",
                 "MANY: correlation matrix, faceting"]},
         ]},

        {"type": "content", "label": "Cross-Tabs", "title": "Cross-tabulation: two categoricals",
         "blocks": [
             {"t": "table",
              "head": ["Sector", "Has toilet", "No toilet", "% with toilet"],
              "rows": [
                  ["Rural", "5,180", "2,020", "71.9"],
                  ["Urban", "2,610", "190", "93.2"],
                  ["All", "7,790", "2,210", "77.9"]]},
             {"t": "hbox", "color": "cyan", "html": "Illustrative. A cross-tab is the "
              "bivariate workhorse. The key choice is the direction of percentages: row "
              "percents answer 'of rural households, what share have a toilet?' &mdash; "
              "usually what you want."},
         ]},

        {"type": "content", "label": "Row vs Column", "title": "Percentage in the right direction",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Row %", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Within each row group: 'of rural "
                   "households, X% have a toilet.' Compares the outcome <em>across</em> "
                   "groups."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Column %", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Within each column: 'of households with "
                   "a toilet, X% are rural.' A different question entirely."}]}]},
             {"t": "hbox", "color": "red", "html": "Choosing the wrong direction silently "
              "answers a different question. State the comparison in words before you "
              "tabulate."},
         ]},

        {"type": "content", "label": "Grouped Summaries", "title": "A continuous variable, split by groups",
         "blocks": [
             {"t": "chart", "canvas": "groupedMpce",
              "title": "Median MPCE by social group (illustrative, patterned on NSS)",
              "source": "Illustrative, patterned on NSS consumption by social group",
              "type": "bar",
              "data": {"labels": ["ST", "SC", "OBC", "Others"],
                       "datasets": [{"label": "Median MPCE (₹/month)",
                                     "data": [2150, 2480, 2900, 3650],
                                     "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Median MPCE (₹/month)'}, beginAtZero:true } } }"}},
             {"t": "hbox", "color": "amber", "html": "Grouping a continuous variable by a "
              "category &mdash; here median consumption by social group &mdash; is the single "
              "most common development EDA move. Use the median for skewed money."},
         ]},

        {"type": "content", "label": "Quartiles by Group", "title": "Compare spread, not just centre",
         "blocks": [
             {"t": "chart", "canvas": "quartChart",
              "title": "MPCE quartiles by sector &mdash; the spread differs (illustrative)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["Q1 (25th)", "Median (50th)", "Q3 (75th)"],
                       "datasets": [
                           {"label": "Rural", "data": [1650, 2550, 3900],
                            "backgroundColor": "#0EA5E9"},
                           {"label": "Urban", "data": [2400, 3700, 6100],
                            "backgroundColor": "#F59E0B"}]},
              "options": {"__js__": "{ plugins:{legend:{display:true}}, scales:{ y:{ title:{display:true,text:'MPCE (₹/month)'}, beginAtZero:true } } }"}},
             {"t": "hbox", "color": "cyan", "html": "A true box plot is awkward in this "
              "toolkit, so we plot the quartiles directly. Urban consumption is both higher "
              "and more spread out &mdash; a fact the medians alone would hide."},
         ]},

        {"type": "content", "label": "Scatter", "title": "Two continuous variables: the scatter",
         "blocks": [
             {"t": "chart", "canvas": "scatterLitFert",
              "title": "Female literacy (%) vs total fertility rate, major states",
              "source": "Illustrative, patterned on Census 2011 &amp; NFHS-5",
              "type": "scatter",
              "data": {"datasets": [{"label": "States",
                       "data": [{"x": 92, "y": 1.8}, {"x": 84, "y": 1.7}, {"x": 76, "y": 1.8},
                                {"x": 73, "y": 2.1}, {"x": 70, "y": 2.0}, {"x": 66, "y": 2.1},
                                {"x": 64, "y": 2.4}, {"x": 60, "y": 2.5}, {"x": 59, "y": 2.7},
                                {"x": 53, "y": 3.0}, {"x": 50, "y": 3.0}, {"x": 57, "y": 2.6}],
                       "backgroundColor": "#6366F1", "pointRadius": 6}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Female literacy %'} }, y:{ title:{display:true,text:'Total fertility rate'}, min:1.5, max:3.2 } } }"}},
             {"t": "hbox", "color": "amber", "html": "A clear negative pattern &mdash; but "
              "remember it is a <em>state-level</em> picture. The ecological fallacy (next) "
              "warns against reading it as an individual truth."},
         ]},

        {"type": "content", "label": "Correlation", "title": "Correlation, and its limits",
         "blocks": [
             {"t": "term", "word": "Correlation (r)",
              "def": "A number from &minus;1 to +1 summarising how strongly two continuous "
              "variables move together <em>linearly</em>. It captures direction and strength "
              "&mdash; but only of a straight-line relationship."},
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Correlation is not causation</strong> &mdash; a confounder may drive both",
                 "<strong>r misses curves</strong> &mdash; a strong U-shape can give r near 0",
                 "<strong>Outliers move r a lot</strong> &mdash; one point can fake a relationship"]},
         ]},

        {"type": "content", "label": "Correlation Heatmap", "title": "The correlation matrix idea",
         "blocks": [
             {"t": "body", "html": "With many continuous variables, compute every pairwise "
              "correlation and lay them out as a colour-shaded <strong>heatmap</strong> "
              "&mdash; dark for strong, pale for weak. It is a fast scan for which variables "
              "travel together."},
             {"t": "hbox", "color": "amber", "html": "Treat the heatmap as a <em>map of "
              "questions</em>, not answers. A strong cell says 'look here', then you plot the "
              "pair to see whether the relationship is real, curved or driven by an outlier."},
         ]},

        {"type": "content", "label": "Disaggregate", "title": "Always split before you conclude",
         "blocks": [
             {"t": "body", "html": "A relationship in the whole sample can hide, or even "
              "reverse, within subgroups &mdash; <strong>Simpson's paradox</strong>. A scheme "
              "can look worse overall yet be better in every state if the states differ in "
              "size and baseline."},
             {"t": "hbox", "color": "red", "html": "Disaggregate by sex, sector, caste, state "
              "as part of routine EDA. The aggregate can point the opposite way to the truth."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Survey Weights &amp; Design Effects in EDA"},

        {"type": "content", "label": "The Catch", "title": "Unweighted exploration misleads",
         "blocks": [
             {"t": "body", "html": "Household surveys are <strong>not</strong> simple random "
              "samples. Some groups are deliberately over-sampled and response rates vary, so "
              "the raw sample does not mirror the population. Exploring it unweighted gives "
              "the wrong picture."},
             {"t": "hbox", "color": "red", "html": "A raw mean from NFHS or PLFS unit data is "
              "an estimate for the <em>sample</em>, not the population. To speak about India, "
              "you must apply the survey weights."},
         ]},

        {"type": "content", "label": "What Weights Are", "title": "Weights: how many people a row represents",
         "blocks": [
             {"t": "term", "word": "Survey weight",
              "def": "A number attached to each record saying how many people or households "
              "in the population that one respondent stands for. It corrects for unequal "
              "selection probabilities and non-response."},
             {"t": "body", "html": "If poor districts were over-sampled, their households "
              "carry <em>smaller</em> weights so they do not dominate the national figure; "
              "under-sampled groups carry larger weights."},
         ]},

        {"type": "content", "label": "Why Over-Sample", "title": "Why surveys over-sample on purpose",
         "blocks": [
             {"t": "body", "html": "To report reliably on a small group &mdash; a small "
              "state, a minority, an urban slum &mdash; the survey must interview "
              "<em>enough</em> of them. So it deliberately over-samples, then uses weights to "
              "restore the correct national balance."},
             {"t": "hbox", "color": "cyan", "html": "This is a feature, not a flaw. But it "
              "means the unweighted sample over-represents those groups &mdash; which is "
              "exactly why weights exist."},
         ]},

        {"type": "content", "label": "See the Gap", "title": "Weighted vs unweighted: a worked gap",
         "blocks": [
             {"t": "chart", "canvas": "weightChart",
              "title": "Estimated open-defecation rate, weighted vs unweighted (illustrative)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["State A", "State B", "National"],
                       "datasets": [
                           {"label": "Unweighted", "data": [22, 9, 17],
                            "backgroundColor": "#EF4444"},
                           {"label": "Weighted", "data": [22, 9, 13],
                            "backgroundColor": "#10B981"}]},
              "options": {"__js__": "{ plugins:{legend:{display:true}}, scales:{ y:{ title:{display:true,text:'% practising open defecation'}, beginAtZero:true } } }"}},
             {"t": "hbox", "color": "amber", "html": "State estimates match, but the national "
              "figure differs: an over-sampled high-rate state inflates the unweighted "
              "national average. Weighting fixes it &mdash; a four-point swing in the headline."},
         ]},

        {"type": "content", "label": "Design Effect", "title": "The design effect (DEFF)",
         "blocks": [
             {"t": "term", "word": "Design effect (DEFF)",
              "def": "How much the clustered, weighted design inflates the variance of an "
              "estimate compared with a simple random sample of the same size. DEFF = 2 means "
              "your effective sample is half the nominal one."},
             {"t": "body", "html": "Because households in the same village are similar, "
              "clustering means each extra interview adds <em>less</em> new information than a "
              "fresh random draw would. The DEFF quantifies that loss."},
         ]},

        {"type": "content", "label": "Effective Sample", "title": "Your sample is smaller than it looks",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "n = 10,000", "label": "nominal sample size", "color": "cyan"},
                 {"num": "DEFF = 2", "label": "typical for a clustered survey", "color": "amber"},
                 {"num": "&asymp; 5,000", "label": "effective sample size (n &divide; DEFF)", "color": "red"}]},
             {"t": "hbox", "color": "red", "html": "Ignore the design effect and your "
              "confidence intervals will be too narrow &mdash; you will claim more precision "
              "than the data supports."},
         ]},

        {"type": "content", "label": "In Practice", "title": "Handling weights and design in EDA",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Find the weight, cluster (PSU) and stratum variables in the codebook",
                 "Apply weights to every estimate meant to describe the population",
                 "Use survey-aware tools so standard errors account for the design",
                 "Report whether each figure is weighted &mdash; and at what level it is valid"]},
             {"t": "hbox", "color": "amber", "html": "Rule of thumb for EDA: explore "
              "<em>shapes</em> unweighted to find problems, but report any "
              "<em>population number</em> weighted."},
         ]},

        {"type": "content", "label": "Level of Validity", "title": "Respect the design's resolution",
         "blocks": [
             {"t": "body", "html": "A survey is only reliable down to the level it was "
              "<strong>designed</strong> for &mdash; usually state or district. Using a "
              "state-level estimate to claim something about one block asks the data a "
              "question it cannot answer."},
             {"t": "hbox", "color": "red", "html": "Common error: drilling NFHS or PLFS to a "
              "tiny subgroup until the cell has 11 households, then reporting a precise "
              "percentage. Check the unweighted count behind every estimate."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Visual EDA Done Well"},

        {"type": "content", "label": "Why Plot", "title": "Plotting is the heart of EDA",
         "blocks": [
             {"t": "body", "html": "EDA leans on display because the eye catches what tables "
              "hide &mdash; skew, clusters, gaps, outliers, curved relationships. The goal in "
              "exploration is speed and honesty, not polish."},
             {"t": "quote",
              "text": "There is no excuse for failing to plot and look.",
              "attr": "&mdash; J. W. Tukey &amp; F. Mosteller"},
         ]},

        {"type": "content", "label": "Small Multiples", "title": "Small multiples: compare many at once",
         "blocks": [
             {"t": "body", "html": "Rather than cramming ten states into one tangled chart, "
              "draw ten tiny identical charts in a grid &mdash; <strong>small multiples</strong>. "
              "Shared scales let the eye compare shapes effortlessly."},
             {"t": "hbox", "color": "green", "html": "Ideal for EDA across states, sectors or "
              "social groups: one consumption histogram per state, same axes, side by side. "
              "Patterns and exceptions jump out."},
         ]},

        {"type": "content", "label": "Faceting", "title": "Faceting: one plot, split by a variable",
         "blocks": [
             {"t": "term", "word": "Faceting",
              "def": "Splitting a single plot into a grid of panels, one per category of a "
              "variable &mdash; the same scatter or histogram drawn separately for rural and "
              "urban, or for each social group."},
             {"t": "hbox", "color": "cyan", "html": "Faceting is small multiples generated "
              "automatically from your data. It is the fastest way to disaggregate visually "
              "and catch a Simpson's-paradox reversal."},
         ]},

        {"type": "content", "label": "Box Plots", "title": "Box plots: distributions side by side",
         "blocks": [
             {"t": "body", "html": "A <strong>box plot</strong> draws Tukey's five-number "
              "summary as a box (Q1 to Q3) with a median line and whiskers, marking outliers "
              "as points. Lined up by group, it compares whole distributions at a glance."},
             {"t": "hbox", "color": "amber", "html": "Box plots show centre, spread and "
              "outliers together &mdash; perfect for comparing MPCE across states. Where a "
              "tool lacks them, plotting the quartiles (as we did earlier) is a fair substitute."},
         ]},

        {"type": "content", "label": "Honest Axes", "title": "Honest axes &mdash; usually start at zero",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "chart", "canvas": "truncEda", "title": "Y starts at 90 (misleading)",
                        "source": "Illustrative",
                        "type": "bar",
                        "data": {"labels": ["2015", "2019", "2021"],
                                 "datasets": [{"label": "Coverage %", "data": [92, 94, 96],
                                               "backgroundColor": "#EF4444"}]},
                        "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:90, max:97 } } }"}}],
              "right": [{"t": "chart", "canvas": "honestEda", "title": "Y starts at 0 (honest)",
                         "source": "Illustrative",
                         "type": "bar",
                         "data": {"labels": ["2015", "2019", "2021"],
                                  "datasets": [{"label": "Coverage %", "data": [92, 94, 96],
                                                "backgroundColor": "#10B981"}]},
                         "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100 } } }"}}]},
             {"t": "hbox", "color": "red", "html": "Same data. Truncating the y-axis makes a "
              "4-point rise look like a leap. Bar charts should start at zero."},
         ]},

        {"type": "content", "label": "Overplotting", "title": "When the scatter becomes a blob",
         "blocks": [
             {"t": "body", "html": "With tens of thousands of households, a scatter turns "
              "into a solid blob and hides its own density. EDA fixes this with "
              "<strong>transparency</strong>, smaller points, sampling, or binning into a "
              "2-D histogram."},
             {"t": "hbox", "color": "cyan", "html": "Large household surveys almost always "
              "overplot. If your scatter is a black cloud, you are seeing the count, not the "
              "pattern &mdash; thin it out."},
         ]},

        {"type": "content", "label": "Checklist", "title": "An exploratory-plot checklist",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Is the variable type matched to the chart (histogram for continuous, bar for categorical)?",
                 "Is the baseline honest, and are axes and units labelled?",
                 "Have you tried a log scale for skewed money?",
                 "Is the plot weighted if it is meant to describe the population?",
                 "Did you disaggregate to check for hidden subgroups?"]},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "From EDA to Questions &amp; Hypotheses"},

        {"type": "content", "label": "The Hand-off", "title": "EDA ends where testing begins",
         "blocks": [
             {"t": "body", "html": "Exploration is generative: it surfaces patterns and "
              "hunches. But a pattern <em>found</em> by exploring is a hypothesis, not a "
              "result. The next, separate step is to test it &mdash; ideally on fresh data."},
             {"t": "flow", "steps": [
                 "EDA: notice a pattern (median consumption lower in one social group)",
                 "QUESTION: is the gap real, or sampling noise?",
                 "HYPOTHESIS: state it precisely, in advance",
                 "TEST: confirm with appropriate, weighted methods"]},
         ]},

        {"type": "content", "label": "Can Do", "title": "What EDA can legitimately conclude",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Describe</strong> the sample: distributions, gaps, structure",
                 "<strong>Reveal</strong> data-quality problems and their extent",
                 "<strong>Compare</strong> groups descriptively (with weights, with caution)",
                 "<strong>Suggest</strong> relationships worth testing",
                 "<strong>Generate</strong> hypotheses and sharpen questions"]},
         ]},

        {"type": "content", "label": "Cannot Do", "title": "What EDA cannot conclude",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Prove causation</strong> &mdash; a pattern is not a cause",
                 "<strong>Confirm</strong> a hypothesis it was used to <em>find</em>",
                 "<strong>Establish significance</strong> by eyeballing &mdash; that needs a test",
                 "<strong>Generalise</strong> below the survey's design level"]},
             {"t": "hbox", "color": "amber", "html": "The cardinal sin: exploring until "
              "something 'looks significant', then reporting it as a confirmed finding. That "
              "is p-hacking by another name."},
         ]},

        {"type": "content", "label": "Forking Paths", "title": "Explore enough, and noise looks real",
         "blocks": [
             {"t": "body", "html": "Slice a dataset twenty ways and roughly one slice will "
              "show a striking pattern by chance alone. Exploration is meant to roam &mdash; "
              "which is exactly why its findings must be confirmed elsewhere."},
             {"t": "hbox", "color": "cyan", "html": "Be honest about how many things you "
              "looked at. A surprising subgroup result found on the twentieth cut deserves "
              "scepticism, not a headline."},
         ]},

        {"type": "content", "label": "Documenting", "title": "Document findings so they travel",
         "blocks": [
             {"t": "bullets", "items": [
                 "State each finding with its <strong>denominator</strong> and unit",
                 "Say whether it is weighted, and at what level it holds",
                 "Note the data-quality caveats behind it",
                 "Separate what EDA <em>suggested</em> from what was <em>tested</em>"]},
             {"t": "hbox", "color": "green", "html": "A finding without its caveats is a "
              "liability. The caveats are what make it usable by someone else &mdash; and "
              "by future-you."},
         ]},

        {"type": "content", "label": "Telling the Story", "title": "From exploration to a clear claim",
         "blocks": [
             {"t": "body", "html": "When EDA is done, translate it into plain language a "
              "decision-maker can act on: what is typical, where the gaps are, who is missing, "
              "and which questions still need a formal test."},
             {"t": "quote",
              "text": "Far better an approximate answer to the right question than an exact "
              "answer to the wrong one.",
              "attr": "&mdash; John W. Tukey"},
         ]},

        {"type": "content", "label": "Takeaways", "title": "The judgement EDA builds",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Look before you model</strong> &mdash; always plot and summarise first",
                 "<strong>Know your unit, codes and universe</strong> before any statistic",
                 "<strong>Why a value is missing</strong> matters more than how many",
                 "<strong>Weight</strong> any number meant to describe the population",
                 "<strong>A found pattern is a question</strong>, not yet an answer"]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Tools &amp; Reproducibility"},

        {"type": "content", "label": "The Toolkit", "title": "Tools for household-survey EDA",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Good for", "Note"],
              "rows": [
                  ["R + tidyverse", "Cleaning, plotting, reproducible analysis", "Free; "
                   "<em>survey</em> &amp; <em>srvyr</em> packages handle weights"],
                  ["Python + pandas", "Cleaning, large data, automation", "Free; "
                   "<em>samplics</em> / statsmodels for survey design"],
                  ["Stata", "Standard for official microdata", "<em>svyset</em> built-in for "
                   "weights &amp; design; widely used"],
                  ["Spreadsheets", "Quick first look, small tables", "Fine to start; not for "
                   "weighted survey estimates"]]},
             {"t": "hbox", "color": "cyan", "html": "Whichever you pick, choose a tool that "
              "understands <strong>survey weights and clustering</strong> &mdash; "
              "spreadsheets do not."},
         ]},

        {"type": "content", "label": "Reproducibility", "title": "Scripts, not manual edits",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Fragile", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Hand-edits in a spreadsheet, no record "
                   "of what changed. Next month nobody can reproduce the number &mdash; "
                   "including you."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Robust", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A documented script from raw extract to "
                   "result. Re-run it any time, audit every step, hand it to a colleague."}]}]},
             {"t": "hbox", "color": "amber", "html": "Golden rule, restated: <strong>never "
              "edit the raw file.</strong> Every clean, recode and exclusion lives in code."},
         ]},

        {"type": "content", "label": "Project Hygiene", "title": "A tidy, reproducible project",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Keep the <strong>raw</strong> extract read-only and dated",
                 "One script does the cleaning, another the analysis",
                 "Name files with versions and dates, not 'final_FINAL_v3'",
                 "Record the source, download date and any filters applied",
                 "Keep the codebook beside the data"]},
         ]},

        {"type": "content", "label": "Where to Get Data", "title": "Open microdata you can explore today",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>microdata.gov.in</strong> &mdash; MoSPI's NSS &amp; PLFS unit-level data",
                 "<strong>dhsprogram.com</strong> &mdash; NFHS / DHS datasets (on request)",
                 "<strong>data.gov.in</strong> &mdash; India's open government data portal",
                 "<strong>censusindia.gov.in</strong> &mdash; Census tables and maps",
                 "<strong>World Bank Microdata Library</strong> &mdash; regional comparisons"]},
             {"t": "hbox", "color": "amber", "html": "Always download the codebook and survey "
              "report alongside the data &mdash; the file is unreadable without them."},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "A short reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Exploratory Data Analysis</em> &mdash; John W. Tukey (the founding text)",
                 "<em>R for Data Science</em> &mdash; Wickham &amp; Grolemund (free online)",
                 "<em>The Visual Display of Quantitative Information</em> &mdash; Edward Tufte",
                 "<em>Analysis of Health Surveys</em> &mdash; Korn &amp; Graubard (survey design)",
                 "Your survey's own <strong>report and methodology note</strong> &mdash; read it first"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Quantitative Methods</strong> and "
              "<strong>Research Ethics</strong> 101 courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Exploratory Data Analysis 101 &middot; Complete",
         "headline": "Now go open<br>the data &mdash; and look.",
         "byline": "Before the model, before the finding, before the headline: inspect, "
                   "clean, describe, plot and question. That habit, applied to every "
                   "household survey you touch, is what makes your numbers trustworthy. "
                   "Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
