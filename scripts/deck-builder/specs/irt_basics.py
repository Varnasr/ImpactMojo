# -*- coding: utf-8 -*-
"""
Item Response Theory 101 — ImpactMojo 101 Series (native deck spec)
A practitioner's introduction to IRT for development M&E and assessment
in South Asia. Build: python3 scripts/deck-builder/build.py irt_basics
"""

# --------------------------------------------------------------------------
# Logistic ICC helper points (computed once, embedded as literals below).
# P(theta) = c + (1-c) / (1 + exp(-1.7*a*(theta-b)))   [logistic metric, D=1.7]
# theta grid: -3 .. +3 in steps of 0.5 (13 points).
# These were generated in Python so the curve shapes are correct; values are
# illustrative, not empirical.
# --------------------------------------------------------------------------
THETA = ["-3", "-2.5", "-2", "-1.5", "-1", "-0.5", "0", "0.5", "1", "1.5", "2", "2.5", "3"]

# Easy item (b=-1), medium (b=0), hard (b=+1); all a=1.0
ICC_EASY = [0.032, 0.072, 0.154, 0.299, 0.5, 0.701, 0.846, 0.928, 0.968, 0.986, 0.994, 0.997, 0.999]
ICC_MED  = [0.006, 0.014, 0.032, 0.072, 0.154, 0.299, 0.5, 0.701, 0.846, 0.928, 0.968, 0.986, 0.994]
ICC_HARD = [0.001, 0.003, 0.006, 0.014, 0.032, 0.072, 0.154, 0.299, 0.5, 0.701, 0.846, 0.928, 0.968]
# Discrimination: steep (a=1.8), flat (a=0.5); both b=0
ICC_STEEP = [0.0, 0.0, 0.002, 0.01, 0.045, 0.178, 0.5, 0.822, 0.955, 0.99, 0.998, 1.0, 1.0]
ICC_FLAT  = [0.072, 0.107, 0.154, 0.218, 0.299, 0.395, 0.5, 0.605, 0.701, 0.782, 0.846, 0.893, 0.928]
# 3PL with guessing (c=0.25, a=1, b=0) vs a 2PL with no guessing (c=0)
ICC_3PL = [0.255, 0.261, 0.274, 0.304, 0.366, 0.475, 0.625, 0.775, 0.884, 0.946, 0.976, 0.989, 0.995]
ICC_2PL = ICC_MED
# DIF: same item, reference vs focal group (focal effective b shifted +0.8)
DIF_REF   = [0.002, 0.006, 0.017, 0.045, 0.115, 0.265, 0.5, 0.735, 0.885, 0.955, 0.983, 0.994, 0.998]
DIF_FOCAL = [0.0, 0.001, 0.003, 0.009, 0.025, 0.066, 0.164, 0.352, 0.601, 0.807, 0.92, 0.97, 0.989]
# Test information (3 items at b=-1,0,1) and SEM = 1/sqrt(I)
TEST_INFO = [0.11, 0.241, 0.484, 0.84, 1.189, 1.406, 1.476, 1.406, 1.189, 0.84, 0.484, 0.241, 0.11]
SEM_CURVE = [3.015, 2.037, 1.437, 1.091, 0.917, 0.843, 0.823, 0.843, 0.917, 1.091, 1.437, 2.037, 3.015]
INFO_TARGETED = [0.005, 0.011, 0.027, 0.064, 0.147, 0.324, 0.661, 1.177, 1.705, 1.934, 1.705, 1.177, 0.661]


def _line_ds(label, data, color, fill=False):
    return {"label": label, "data": data, "borderColor": color,
            "backgroundColor": color, "tension": 0.4, "pointRadius": 0,
            "borderWidth": 3, "fill": fill}


# Chart.js options for an ICC plot (probability 0-1 on y, theta on x)
ICC_OPTS = ("{ plugins:{ legend:{ labels:{ color:'#cbd5e1' } } }, "
            "scales:{ x:{ title:{display:true,text:'Latent trait \\u03b8',color:'#94a3b8'}, "
            "ticks:{color:'#94a3b8'}, grid:{color:'rgba(148,163,184,0.12)'} }, "
            "y:{ min:0, max:1, title:{display:true,text:'P(correct / endorse)',color:'#94a3b8'}, "
            "ticks:{color:'#94a3b8'}, grid:{color:'rgba(148,163,184,0.12)'} } } }")

INFO_OPTS = ("{ plugins:{ legend:{ labels:{ color:'#cbd5e1' } } }, "
             "scales:{ x:{ title:{display:true,text:'Latent trait \\u03b8',color:'#94a3b8'}, "
             "ticks:{color:'#94a3b8'}, grid:{color:'rgba(148,163,184,0.12)'} }, "
             "y:{ min:0, title:{display:true,text:'Information',color:'#94a3b8'}, "
             "ticks:{color:'#94a3b8'}, grid:{color:'rgba(148,163,184,0.12)'} } } }")

SEM_OPTS = ("{ plugins:{ legend:{ display:false } }, "
            "scales:{ x:{ title:{display:true,text:'Latent trait \\u03b8',color:'#94a3b8'}, "
            "ticks:{color:'#94a3b8'}, grid:{color:'rgba(148,163,184,0.12)'} }, "
            "y:{ min:0, title:{display:true,text:'Standard error (SEM)',color:'#94a3b8'}, "
            "ticks:{color:'#94a3b8'}, grid:{color:'rgba(148,163,184,0.12)'} } } }")


DECK = {
    "slug": "irt-basics",
    "title": "Item Response Theory 101",
    "description": ("Item Response Theory 101 — a free foundational course for development "
                    "M&E and assessment practitioners in South Asia. Understand latent traits, "
                    "item characteristic curves, difficulty and discrimination, information, DIF "
                    "and how IRT powers learning assessments and empowerment, wealth and food-"
                    "security scales. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Item<br>Response<br>Theory 101",
         "sub": "Measuring Latent Traits Well &mdash; a Foundational Course on IRT for "
                "Assessment &amp; M&amp;E Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "The Measurement Problem"},
             {"name": "Classical Test Theory &amp; Its Limits"},
             {"name": "The Big Idea of IRT"},
             {"name": "The Item Characteristic Curve"},
             {"name": "Item Difficulty &mdash; the b Parameter"},
             {"name": "Item Discrimination &mdash; the a Parameter"},
             {"name": "Guessing &amp; the Model Family"},
             {"name": "Information &amp; Precision"},
             {"name": "Validating Scales &amp; DIF"},
             {"name": "Applications in Development"},
             {"name": "Assumptions, Limits &amp; Tools"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "The Measurement Problem"},

        {"type": "content", "label": "The Core Problem", "title": "You cannot see what you most want to measure",
         "blocks": [
             {"t": "body", "html": "Development work is full of things we care about but cannot "
              "observe directly: a child's <strong>reading ability</strong>, a woman's "
              "<strong>empowerment</strong>, a household's <strong>food insecurity</strong>. "
              "We only ever see <em>responses</em> &mdash; answers to items, ticks on a scale."},
             {"t": "term", "word": "Latent trait",
              "def": "An unobservable characteristic of a person &mdash; ability, attitude, "
              "deprivation &mdash; that we infer from their answers to a set of items. By "
              "convention it is written as theta (&theta;)."},
         ]},

        {"type": "content", "label": "From Trait to Answer", "title": "We observe answers, not the trait",
         "blocks": [
             {"t": "flow", "steps": [
                 "LATENT TRAIT: reading ability (θ) &mdash; unseen",
                 "ITEMS: a child reads words, sentences, a paragraph",
                 "RESPONSES: correct / incorrect on each item",
                 "INFERENCE: a measurement model estimates θ from the pattern"]},
             {"t": "hbox", "color": "cyan", "html": "A <strong>measurement model</strong> is the "
              "bridge: it links the unseen trait to the seen responses, with explicit assumptions "
              "you can check."},
         ]},

        {"type": "content", "label": "Three Examples", "title": "The same problem, three development settings",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Ability", "label": "ASER-style early-grade reading &amp; arithmetic &mdash; "
                  "a child either can or cannot do each task", "color": "cyan"},
                 {"num": "Empowerment", "label": "A woman's decision-making, mobility &amp; "
                  "asset control &mdash; agree / disagree items", "color": "indigo"},
                 {"num": "Food insecurity", "label": "FIES &mdash; eight yes/no experiences from "
                  "worry to going a whole day without eating", "color": "amber"}]},
             {"t": "body", "cls": "sm", "html": "In each case the trait is on a hidden continuum "
              "and the items are graded markers along it."},
         ]},

        {"type": "content", "label": "Why A Model", "title": "Why not just count right answers?",
         "blocks": [
             {"t": "body", "html": "The obvious approach &mdash; add up correct answers, or count "
              "'yes' responses &mdash; treats every item as equal and every score gap as the same "
              "size. But a hard item is not worth the same as an easy one, and the jump from 4 to "
              "5 correct is not the same as 8 to 9."},
             {"t": "hbox", "color": "amber", "html": "A measurement model lets items differ &mdash; "
              "in difficulty, in how well they sort people &mdash; and places people and items on "
              "<em>one</em> common scale."},
         ]},

        {"type": "content", "label": "Two Traditions", "title": "Two families of measurement theory",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Classical Test Theory (CTT)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Works on the <em>total score</em>. Simple, "
                   "familiar, everywhere &mdash; but its statistics depend on the particular sample "
                   "and the particular test."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Item Response Theory (IRT)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Models each <em>item</em> and each "
                   "<em>person</em> separately, on a shared scale. More demanding, but the "
                   "properties travel across samples and forms."}]}]},
             {"t": "body", "cls": "sm", "html": "This course starts from CTT &mdash; what it is, "
              "and exactly where it strains &mdash; then builds IRT as the answer."},
         ]},

        {"type": "content", "label": "What Good Measurement Buys You", "title": "Why measurement quality is not a luxury",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Comparability:</strong> compare a child this year with last year, or "
                 "one state's empowerment score with another's, on the same ruler",
                 "<strong>Fairness:</strong> detect items that behave differently for girls, or "
                 "for one language group",
                 "<strong>Precision where it matters:</strong> know exactly where the test "
                 "measures well and where it is guessing",
                 "<strong>Honest scores:</strong> a number that means the same thing for everyone"]},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Foundations", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "The measurement problem &amp; CTT's limits",
                      "The big idea of IRT and the ICC",
                      "Difficulty (b), discrimination (a), guessing (c)"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Using IRT well", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Information, precision and test targeting",
                      "Validating scales: fit, dimensionality, DIF",
                      "Applications, assumptions and tools"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Examples are drawn from learning assessments, "
              "empowerment, wealth and food-security scales used across the region."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Classical Test Theory &amp; Its Limits"},

        {"type": "content", "label": "The CTT Score", "title": "The familiar sum or percentage score",
         "blocks": [
             {"t": "body", "html": "Classical Test Theory is the world of the <strong>total "
              "score</strong>: number correct, percentage right, the count of 'yes' responses on "
              "a scale. It is what nearly every report and dashboard already uses."},
             {"t": "flow", "steps": [
                 "Observed score = True score + Error",
                 "X = T + E",
                 "Goal: estimate T, shrink E"]},
         ]},

        {"type": "content", "label": "Reliability", "title": "Reliability: how much is signal, not noise?",
         "blocks": [
             {"t": "term", "word": "Reliability",
              "def": "The share of the variation in scores that reflects true differences between "
              "people rather than measurement error. It runs from 0 (all noise) to 1 (no error)."},
             {"t": "body", "cls": "sm", "html": "A reliable test gives nearly the same score if a "
              "person sits it twice. Low reliability means scores wobble for reasons that have "
              "nothing to do with the trait."},
         ]},

        {"type": "content", "label": "Cronbach's Alpha", "title": "Cronbach's alpha &mdash; the workhorse statistic",
         "blocks": [
             {"t": "body", "html": "<strong>Cronbach's alpha</strong> estimates reliability from a "
              "single sitting by asking how consistently the items hang together. Rules of thumb "
              "put 'acceptable' around 0.70 and up &mdash; but the number is widely misread."},
             {"t": "hbox", "color": "amber", "html": "Alpha rises simply by adding more items, and "
              "high alpha does <em>not</em> prove the scale measures one thing. It is a useful "
              "summary, not a certificate of quality."},
         ]},

        {"type": "content", "label": "Limit 1", "title": "CTT statistics are sample-dependent",
         "blocks": [
             {"t": "body", "html": "An item's CTT 'difficulty' is just the proportion who got it "
              "right (the <em>p-value</em>). Give the same item to a high-ability school and a "
              "struggling one and that proportion changes &mdash; so the item looks 'easier' or "
              "'harder' depending on <em>who</em> sat it."},
             {"t": "hbox", "color": "red", "html": "The item did not change. The sample did. Yet "
              "the headline statistic moved &mdash; that is the problem."},
         ]},

        {"type": "content", "label": "Sample-Dependence Illustrated", "title": "Same item, two samples, two p-values",
         "blocks": [
             {"t": "table",
              "head": ["Group", "% correct on Item Q", "CTT verdict"],
              "rows": [
                  ["High-ability school", "88%", "An easy item"],
                  ["Mixed government school", "61%", "A moderate item"],
                  ["Struggling school", "34%", "A hard item"]]},
             {"t": "hbox", "color": "amber", "html": "Illustrative figures. One physical item, "
              "three contradictory CTT difficulties &mdash; because the p-value confounds the item "
              "with the people who answered it."},
         ]},

        {"type": "content", "label": "Limit 2", "title": "CTT statistics are test-dependent",
         "blocks": [
             {"t": "body", "html": "A person's CTT ability is their score <em>on this particular "
              "test</em>. Put them on an easier form and the score climbs; a harder form and it "
              "falls. The person's standing is tangled up with the difficulty of the form they "
              "happened to take."},
             {"t": "hbox", "color": "red", "html": "Two children with the same true ability can "
              "get different scores purely because they sat different forms. Comparing across "
              "forms or years becomes guesswork."},
         ]},

        {"type": "content", "label": "Limit 3", "title": "One error figure for the whole scale",
         "blocks": [
             {"t": "body", "html": "CTT reports a single <strong>standard error of measurement</strong> "
              "for everyone. But in reality a test measures a middling student far more precisely "
              "than it measures a top scorer (who finds every item easy) or a very weak one (who "
              "finds every item hard)."},
             {"t": "hbox", "color": "amber", "html": "Precision genuinely varies across the ability "
              "range. CTT pretends it is constant &mdash; IRT will let it vary, which is closer to "
              "the truth."},
         ]},

        {"type": "content", "label": "Where CTT Strains", "title": "Three jobs CTT cannot do cleanly",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["You want to&hellip;", "CTT problem", "IRT answer (coming)"],
              "rows": [
                  ["Compare items fairly across samples", "p-values shift with the sample", "Item params are sample-free"],
                  ["Compare people across forms/years", "Scores depend on the form", "θ is on a common scale"],
                  ["Know precision at each level", "One SEM for all", "Information varies along θ"],
                  ["Build an adaptive or short form", "Hard &mdash; scores not comparable", "Items &amp; people share a metric"]]},
             {"t": "hbox", "color": "cyan", "html": "None of this means CTT is wrong &mdash; just "
              "that it asks too much of one total score. IRT splits the job apart."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The Big Idea of IRT"},

        {"type": "content", "label": "One Scale", "title": "Put people and items on the same ruler",
         "blocks": [
             {"t": "body", "html": "The central move of IRT is deceptively simple: place "
              "<strong>each person's trait (&theta;)</strong> and <strong>each item's difficulty</strong> "
              "on one shared continuum. A person is somewhere on the line; so is every item."},
             {"t": "hbox", "color": "cyan", "html": "If a person sits <em>above</em> an item on "
              "the scale, they are likely to get it right or endorse it. <em>Below</em> it, "
              "unlikely. The distance between them sets the probability."},
         ]},

        {"type": "content", "label": "The Logit Scale", "title": "A trait scale centred on zero",
         "blocks": [
             {"t": "body", "html": "By convention &theta; is scaled to have mean 0 and standard "
              "deviation 1 in the reference group, usually running from about &minus;3 to +3. "
              "Negative means lower ability / less of the trait; positive means more."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "θ ≈ −2", "label": "low trait &mdash; struggles with most items", "color": "red"},
                 {"num": "θ ≈ 0", "label": "average for the reference group", "color": "indigo"},
                 {"num": "θ ≈ +2", "label": "high trait &mdash; succeeds on most items", "color": "green"}]},
         ]},

        {"type": "content", "label": "The Probability Statement", "title": "IRT predicts a probability, not a yes/no",
         "blocks": [
             {"t": "body", "html": "IRT never says a person <em>will</em> get an item right. It "
              "gives the <strong>probability</strong> of a correct (or endorsing) response, as a "
              "function of where the person and the item sit on the scale."},
             {"t": "term", "word": "P(correct | θ)",
              "def": "The probability that a person with trait level theta answers an item "
              "correctly (for a test) or endorses it (for an attitude / experience scale). It "
              "rises smoothly as theta rises."},
         ]},

        {"type": "content", "label": "The Logistic Form", "title": "The S-shaped probability curve",
         "blocks": [
             {"t": "body", "html": "That probability follows a smooth <strong>logistic</strong> "
              "function of &theta;. Far below the item, P is near 0; far above, near 1; in between "
              "it climbs through an S-shape. This curve is the heart of IRT."},
             {"t": "hbox", "color": "cyan", "html": "Crucially the curve is <strong>monotonic</strong>: "
              "more trait always means a higher chance of success. It never dips."},
         ]},

        {"type": "content", "label": "First Look", "title": "One item's curve across the trait range",
         "blocks": [
             {"t": "chart", "canvas": "iccFirstLook",
              "title": "Probability of a correct response rises with θ (item at b=0)",
              "source": "Illustrative logistic ICC (a=1, b=0)",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("Item at b = 0", ICC_MED, "#0EA5E9")]},
              "options": {"__js__": ICC_OPTS}},
             {"t": "hbox", "color": "green", "html": "At &theta; = 0 the chance is 50%. Move up "
              "the scale and success becomes near-certain; move down and it fades to near zero."},
         ]},

        {"type": "content", "label": "What Travels", "title": "Why this fixes CTT's headaches",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Item properties are sample-independent:</strong> the curve describes the "
                 "item itself, not the group that sat it (when the model fits)",
                 "<strong>Person estimates are test-independent:</strong> &theta; means the same "
                 "thing whatever items you used",
                 "<strong>Items &amp; people share a metric:</strong> you can match a test to a "
                 "person, link forms, and build short or adaptive tests"]},
             {"t": "hbox", "color": "amber", "html": "These gains hold <em>only</em> when the "
              "model's assumptions hold &mdash; a promise we will scrutinise later."},
         ]},

        {"type": "content", "label": "Reading An Endorsement Scale", "title": "The same idea for attitudes &amp; experiences",
         "blocks": [
             {"t": "body", "html": "For a food-insecurity or empowerment scale there is no 'right' "
              "answer &mdash; the curve gives the probability of <strong>endorsing</strong> the "
              "item ('yes, we worried about food'). Severe items are endorsed only by households "
              "high on the insecurity continuum."},
             {"t": "hbox", "color": "cyan", "html": "'Could you visit a health centre alone?' and "
              "'did you go a whole day without eating?' are items placed at very different points "
              "on their respective scales."},
         ]},

        {"type": "content", "label": "The Promise", "title": "What the rest of the course unpacks",
         "blocks": [
             {"t": "body", "html": "Everything that follows is detail on that one S-curve: "
              "<strong>where</strong> it sits (difficulty, b), <strong>how steep</strong> it is "
              "(discrimination, a), whether it has a <strong>floor</strong> (guessing, c), how "
              "much <strong>information</strong> it carries, and whether it behaves the "
              "<strong>same for everyone</strong> (DIF)."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "The Item Characteristic Curve"},

        {"type": "content", "label": "Definition", "title": "The Item Characteristic Curve (ICC)",
         "blocks": [
             {"t": "term", "word": "Item Characteristic Curve (ICC)",
              "def": "The graph of the probability of a correct / endorsing response (y, 0 to 1) "
              "against the latent trait theta (x). One curve per item; its shape encodes "
              "everything the model says about that item."},
             {"t": "body", "cls": "sm", "html": "Also called the item response function. Read it "
              "left to right: as the person's trait increases, the chance of success increases."},
         ]},

        {"type": "content", "label": "How To Read It", "title": "Reading an ICC in three moves",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Pick a &theta; on the x-axis</strong> &mdash; a person's trait level",
                 "<strong>Go up to the curve, then across</strong> &mdash; read the probability",
                 "<strong>The whole curve</strong> tells you how the item behaves for everyone"]},
             {"t": "hbox", "color": "cyan", "html": "Two numbers define the basic curve: where it "
              "crosses 50% (difficulty) and how steeply it rises there (discrimination)."},
         ]},

        {"type": "content", "label": "Anatomy", "title": "The three landmarks of an ICC",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Lower tail", "label": "P near 0 (or near c) for very low θ &mdash; "
                  "the item is too hard for them", "color": "red"},
                 {"num": "Inflection", "label": "the steepest point &mdash; where the item best "
                  "separates people", "color": "indigo"},
                 {"num": "Upper tail", "label": "P near 1 for very high θ &mdash; the item is "
                  "trivially easy for them", "color": "green"}]},
         ]},

        {"type": "content", "label": "The Curve", "title": "A single, well-behaved ICC",
         "blocks": [
             {"t": "chart", "canvas": "iccSingle",
              "title": "One item's ICC (a=1, b=0): monotonic, S-shaped, 0 to 1",
              "source": "Illustrative logistic ICC",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("Item ICC", ICC_MED, "#6366F1", fill=True)]},
              "options": {"__js__": ICC_OPTS}},
             {"t": "body", "cls": "sm", "html": "The 50% point sits at &theta; = 0 here &mdash; "
              "that is this item's difficulty. The slope through that point is its discrimination."},
         ]},

        {"type": "content", "label": "Monotonic", "title": "An ICC only ever goes up",
         "blocks": [
             {"t": "body", "html": "A valid ICC is <strong>monotonically increasing</strong>: more "
              "of the trait never lowers the chance of a correct response. If a fitted curve dips "
              "or wiggles, something is wrong &mdash; a mis-keyed item, a trick question, or a "
              "broken assumption."},
             {"t": "hbox", "color": "red", "html": "A non-monotonic empirical curve is a red flag, "
              "not a finding. Investigate the item before trusting it."},
         ]},

        {"type": "content", "label": "Comparing Items", "title": "Several items on one set of axes",
         "blocks": [
             {"t": "chart", "canvas": "iccCompareFour",
              "title": "Four items overlaid: easy/hard differ in position, steep/flat in slope",
              "source": "Illustrative ICCs",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("Easy (b=−1)", ICC_EASY, "#10B981"),
                  _line_ds("Hard (b=+1)", ICC_HARD, "#EF4444"),
                  _line_ds("Steep (a=1.8)", ICC_STEEP, "#0EA5E9"),
                  _line_ds("Flat (a=0.5)", ICC_FLAT, "#F59E0B")]},
              "options": {"__js__": ICC_OPTS}},
             {"t": "hbox", "color": "cyan", "html": "Overlaying ICCs is how psychometricians read "
              "an item bank at a glance &mdash; left/right tells you difficulty, steepness tells "
              "you discrimination."},
         ]},

        {"type": "content", "label": "Probability To Score", "title": "From curves to a person's estimate",
         "blocks": [
             {"t": "body", "html": "Given a person's pattern of right and wrong answers and the "
              "fitted ICCs, the software finds the &theta; that makes that pattern most likely. "
              "That &theta; &mdash; not the raw count &mdash; is the person's IRT score."},
             {"t": "flow", "steps": [
                 "Item ICCs (a, b, c) estimated",
                 "Person's response pattern observed",
                 "Find θ that best fits the pattern",
                 "θ with a standard error = the score"]},
         ]},

        {"type": "content", "label": "Why Curves Beat Counts", "title": "The same raw score, different meaning",
         "blocks": [
             {"t": "body", "html": "Two children each get 6 of 12 right. One passed the six "
              "<em>easy</em> items; the other passed six <em>hard</em> ones and missed easy "
              "items. CTT calls them equal. IRT, reading <em>which</em> items, places them at "
              "different &theta;."},
             {"t": "hbox", "color": "cyan", "html": "The response <em>pattern</em> carries "
              "information that the raw total throws away."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Item Difficulty &mdash; the b Parameter"},

        {"type": "content", "label": "Definition", "title": "b locates the item on the trait scale",
         "blocks": [
             {"t": "term", "word": "Difficulty (b)",
              "def": "The point on the theta scale where the item's success probability is 50% "
              "(for a 2PL/1PL model). It is measured in the same units as theta, so an item and a "
              "person can be compared directly."},
             {"t": "hbox", "color": "amber", "html": "Mantra: <strong>higher b = harder item</strong>. "
              "A hard item's curve sits to the <em>right</em>; you need more trait to have a "
              "50&ndash;50 chance."},
         ]},

        {"type": "content", "label": "The Key Picture", "title": "Easy, medium and hard items",
         "blocks": [
             {"t": "chart", "canvas": "iccDifficulty",
              "title": "Three items, same a, different b: the curve slides right as b rises",
              "source": "Illustrative ICCs (a=1; b = −1, 0, +1)",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("Easy (b = −1)", ICC_EASY, "#10B981"),
                  _line_ds("Medium (b = 0)", ICC_MED, "#0EA5E9"),
                  _line_ds("Hard (b = +1)", ICC_HARD, "#EF4444")]},
              "options": {"__js__": ICC_OPTS}},
             {"t": "hbox", "color": "cyan", "html": "Read off the 50% line: the easy item crosses "
              "it at &theta; = &minus;1, the hard item at &theta; = +1. That crossing point "
              "<em>is</em> b."},
         ]},

        {"type": "content", "label": "Same Units", "title": "b and θ share one scale",
         "blocks": [
             {"t": "body", "html": "Because b is expressed in &theta; units, you can ask: is this "
              "person above or below this item? A child at &theta; = 0.5 is comfortably above an "
              "easy item (b = &minus;1) but below a hard one (b = +1)."},
             {"t": "hbox", "color": "green", "html": "This shared metric is what lets you "
              "<strong>target</strong> a test &mdash; choose items whose b's surround the people "
              "you most need to measure."},
         ]},

        {"type": "content", "label": "Worked Example", "title": "Ordering items by difficulty",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Item (early-grade reading)", "b (illustrative)", "Interpretation"],
              "rows": [
                  ["Recognise a letter", "−2.0", "Very easy &mdash; most children pass"],
                  ["Read a familiar word", "−0.8", "Easy"],
                  ["Read a simple sentence", "0.2", "Moderate"],
                  ["Read a short paragraph", "1.0", "Hard"],
                  ["Answer a comprehension question", "1.8", "Very hard"]]},
             {"t": "hbox", "color": "amber", "html": "Illustrative values. The ordering &mdash; "
              "letter to comprehension &mdash; is what an ASER-style ladder captures, and b puts "
              "numbers on it."},
         ]},

        {"type": "content", "label": "Difficulty For Scales", "title": "For attitude scales, b means 'severity'",
         "blocks": [
             {"t": "body", "html": "On a food-insecurity scale, b is better read as "
              "<strong>severity</strong>: how much insecurity it takes before a household endorses "
              "the item. 'We worried about food' has a low b; 'a household member went a whole day "
              "without eating' has a high b."},
             {"t": "hbox", "color": "cyan", "html": "A well-built scale spreads its items' b's "
              "from mild to severe, so it can place households all along the continuum."},
         ]},

        {"type": "content", "label": "Item Map", "title": "Mapping items along the trait scale",
         "blocks": [
             {"t": "chart", "canvas": "itemMap",
              "title": "Item-difficulty map: where five items 'bite' on the θ scale",
              "source": "Illustrative b values on the θ axis",
              "type": "scatter",
              "data": {"datasets": [{"label": "Items (by difficulty b)",
                       "data": [{"x": -2.0, "y": 1}, {"x": -0.8, "y": 1}, {"x": 0.2, "y": 1},
                                {"x": 1.0, "y": 1}, {"x": 1.8, "y": 1}],
                       "backgroundColor": "#6366F1", "pointRadius": 9}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ "
                          "x:{ min:-3, max:3, title:{display:true,text:'Difficulty b on the \\u03b8 scale',color:'#94a3b8'}, "
                          "ticks:{color:'#94a3b8'}, grid:{color:'rgba(148,163,184,0.12)'} }, "
                          "y:{ display:false, min:0, max:2 } } }"}},
             {"t": "hbox", "color": "amber", "html": "Gaps in the map are blind spots: between "
              "b = &minus;0.8 and 0.2 the test thins out, so it measures children there less well."},
         ]},

        {"type": "content", "label": "Common Confusion", "title": "Difficulty is about the item, not the topic",
         "blocks": [
             {"t": "body", "html": "b is empirical: it is set by how people actually respond, not "
              "by how hard the item <em>looks</em>. A question that seems advanced may be easy if "
              "everyone was taught it; a 'simple' item may be hard if the wording confuses people."},
             {"t": "hbox", "color": "red", "html": "Never assign difficulty by intuition. Estimate "
              "it from data, then sanity-check the surprises &mdash; they often reveal a flawed "
              "item."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Item Discrimination &mdash; the a Parameter"},

        {"type": "content", "label": "Definition", "title": "a measures how sharply an item sorts people",
         "blocks": [
             {"t": "term", "word": "Discrimination (a)",
              "def": "How steeply the ICC rises at its midpoint &mdash; how well the item "
              "distinguishes people just below its difficulty from those just above it. Higher a "
              "means a steeper curve and a sharper distinction."},
             {"t": "hbox", "color": "amber", "html": "Mantra: <strong>higher a = steeper ICC = "
              "better at separating</strong> low-trait from high-trait people near its b."},
         ]},

        {"type": "content", "label": "The Key Picture", "title": "A steep item and a flat item",
         "blocks": [
             {"t": "chart", "canvas": "iccDiscrim",
              "title": "Same difficulty (b=0), different discrimination: steep vs flat",
              "source": "Illustrative ICCs (b=0; a = 1.8 vs 0.5)",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("Steep (a = 1.8)", ICC_STEEP, "#0EA5E9"),
                  _line_ds("Flat (a = 0.5)", ICC_FLAT, "#F59E0B")]},
              "options": {"__js__": ICC_OPTS}},
             {"t": "hbox", "color": "cyan", "html": "Both cross 50% at &theta; = 0 (same b). The "
              "steep item leaps from low to high probability over a narrow band &mdash; it sorts "
              "people sharply right there. The flat item barely distinguishes anyone."},
         ]},

        {"type": "content", "label": "Why Steep Helps", "title": "A steep item is a sharp ruler",
         "blocks": [
             {"t": "body", "html": "Near its difficulty, a high-a item changes a person's success "
              "probability a lot for a small change in &theta;. That sensitivity is exactly what "
              "lets it tell two nearby people apart &mdash; it carries more information (next "
              "section)."},
             {"t": "hbox", "color": "green", "html": "High discrimination is generally desirable "
              "&mdash; but only near that item's b. Away from b, even a steep item is flat and "
              "tells you little."},
         ]},

        {"type": "content", "label": "Low Discrimination", "title": "When an item barely sorts anyone",
         "blocks": [
             {"t": "body", "html": "A low-a (flat) item gives almost the same success probability "
              "to people across a wide range of &theta;. Low-trait and high-trait people answer it "
              "similarly &mdash; so it adds little to distinguishing them."},
             {"t": "hbox", "color": "red", "html": "Very low or negative a is a warning: the item "
              "may be ambiguous, off-topic, or mis-keyed. Items that do not discriminate are "
              "candidates for revision or removal."},
         ]},

        {"type": "content", "label": "Negative Discrimination", "title": "A curve that goes the wrong way",
         "blocks": [
             {"t": "body", "html": "If an item shows <strong>negative</strong> discrimination, "
              "higher-trait people do <em>worse</em> on it than lower-trait people &mdash; the ICC "
              "slopes downward. That should never happen for a sound item."},
             {"t": "hbox", "color": "amber", "html": "Usual culprits: the answer key is wrong, the "
              "item measures something else, or it is a trick question. Fix or drop it &mdash; do "
              "not leave it scoring people backwards."},
         ]},

        {"type": "content", "label": "a and b Together", "title": "Difficulty and discrimination are independent",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Low a (flat)", "High a (steep)"],
              "rows": [
                  ["Low b (easy)", "Easy, sorts weakly", "Easy, sorts low-trait people sharply"],
                  ["High b (hard)", "Hard, sorts weakly", "Hard, sorts high-trait people sharply"]]},
             {"t": "hbox", "color": "cyan", "html": "b says <em>where</em> the item works; a says "
              "<em>how well</em> it works there. A good item bank mixes b's to cover the range and "
              "favours high a's at each level."},
         ]},

        {"type": "content", "label": "Scale Items", "title": "Discrimination on an empowerment scale",
         "blocks": [
             {"t": "body", "html": "On an empowerment scale, a high-a item is one whose endorsement "
              "cleanly separates more- from less-empowered women near its severity. A low-a item "
              "&mdash; one answered similarly regardless of empowerment &mdash; is dead weight."},
             {"t": "hbox", "color": "green", "html": "Selecting high-a items is how scale "
              "developers shorten a questionnaire without losing measurement quality."},
         ]},

        {"type": "content", "label": "Caution", "title": "Steeper is not always better",
         "blocks": [
             {"t": "body", "html": "An extremely steep item measures superbly &mdash; but only in a "
              "razor-thin band of &theta;. A test built only of very steep items can measure one "
              "narrow region brilliantly and everywhere else poorly."},
             {"t": "hbox", "color": "amber", "html": "Balance matters: you want high discrimination "
              "<em>spread across</em> the range you care about, not piled at one point."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Guessing &amp; the Model Family"},

        {"type": "content", "label": "The Floor", "title": "On multiple-choice items, no one scores zero",
         "blocks": [
             {"t": "body", "html": "On a 4-option multiple-choice item, even a child who knows "
              "nothing has roughly a 1-in-4 chance of being right. So the ICC should not fall to "
              "zero at low &theta; &mdash; it should flatten out at a <strong>lower asymptote</strong>."},
             {"t": "term", "word": "Guessing (c)",
              "def": "The lower asymptote of the ICC &mdash; the success probability for someone "
              "with very low theta. It is the floor created by guessing or by partial cues."},
         ]},

        {"type": "content", "label": "The Key Picture", "title": "A guessing floor lifts the lower tail",
         "blocks": [
             {"t": "chart", "canvas": "iccGuessing",
              "title": "With guessing (c=0.25) the curve floors near 0.25, not 0",
              "source": "Illustrative ICCs (a=1, b=0; c=0 vs c=0.25)",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("No guessing (c = 0)", ICC_2PL, "#0EA5E9"),
                  _line_ds("With guessing (c = 0.25)", ICC_3PL, "#F59E0B")]},
              "options": {"__js__": ICC_OPTS}},
             {"t": "hbox", "color": "cyan", "html": "Note the amber curve never drops below ~0.25. "
              "A very low-ability student still has a one-in-four chance &mdash; that is the "
              "guessing floor."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "Ignoring guessing biases difficulty",
         "blocks": [
             {"t": "body", "html": "If you fit a model with no guessing parameter to multiple-choice "
              "data, the floor created by guessing gets misread as the item being 'easier' than it "
              "is &mdash; biasing b and distorting low-ability scores."},
             {"t": "hbox", "color": "amber", "html": "c matters most at the <em>bottom</em> of the "
              "scale &mdash; precisely where many development assessments most need to measure "
              "well."},
         ]},

        {"type": "content", "label": "The Model Family", "title": "1PL, 2PL, 3PL: what each one adds",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Model", "Free parameters", "Adds&hellip;"],
              "rows": [
                  ["1PL / Rasch", "b only (a fixed equal)", "Difficulty differs; all items equally discriminating"],
                  ["2PL", "a and b", "Items also differ in discrimination"],
                  ["3PL", "a, b and c", "Plus a guessing floor"]]},
             {"t": "hbox", "color": "cyan", "html": "Each step adds realism &mdash; and demands "
              "more data to estimate the extra parameters reliably."},
         ]},

        {"type": "content", "label": "Rasch / 1PL", "title": "The Rasch model: every item equally discriminating",
         "blocks": [
             {"t": "body", "html": "The <strong>1PL / Rasch</strong> model <em>fixes a to be the "
              "same for every item</em>, so items differ only in difficulty (b). The ICCs are "
              "parallel S-curves &mdash; same shape, shifted left or right."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Why people love it", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Simple, stable, needs less data",
                      "Raw score is a sufficient statistic",
                      "Elegant measurement properties"]}]}],
              "right": [{"t": "panel", "color": "amber", "title": "The trade-off", "blocks": [
                  {"t": "body", "cls": "sm", "html": "It <em>assumes</em> equal discrimination. "
                   "Where items genuinely differ in a, Rasch will misfit some of them."}]}]},
         ]},

        {"type": "content", "label": "2PL", "title": "The 2PL model: let discrimination vary",
         "blocks": [
             {"t": "body", "html": "The <strong>2PL</strong> frees a, so each item has its own "
              "slope as well as its own difficulty. ICCs can now be steep or flat, crossing one "
              "another. It fits more datasets but needs more respondents."},
             {"t": "hbox", "color": "cyan", "html": "Use 2PL when items plainly differ in how well "
              "they sort people &mdash; common for attitude and empowerment scales."},
         ]},

        {"type": "content", "label": "3PL", "title": "The 3PL model: add a guessing floor",
         "blocks": [
             {"t": "body", "html": "The <strong>3PL</strong> adds c, the guessing asymptote &mdash; "
              "built for multiple-choice ability tests where lucky guesses are real. It is the "
              "most flexible of the three but the hungriest for data and the trickiest to estimate."},
             {"t": "hbox", "color": "red", "html": "c is notoriously hard to pin down &mdash; it "
              "lives in the sparsely-populated low-&theta; tail. Large samples are essential, or c "
              "is often fixed to 1/(number of options)."},
         ]},

        {"type": "content", "label": "Choosing", "title": "Which model should you use?",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Start simple.</strong> Rasch/1PL if items are similar and data is "
                 "limited &mdash; many large-scale assessments use it deliberately",
                 "<strong>Move to 2PL</strong> when discrimination clearly varies and you have "
                 "the sample size",
                 "<strong>Reserve 3PL</strong> for multiple-choice ability tests with guessing "
                 "and very large samples",
                 "<strong>Let fit and theory decide</strong> &mdash; not the wish for the fanciest "
                 "model"]},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Information &amp; Precision"},

        {"type": "content", "label": "The Idea", "title": "Information = measurement precision",
         "blocks": [
             {"t": "term", "word": "Item information",
              "def": "How much an item reduces uncertainty about theta at each point on the scale. "
              "An item is most informative around its own difficulty b, and more so the higher its "
              "discrimination a."},
             {"t": "hbox", "color": "cyan", "html": "Information is the IRT replacement for one "
              "blanket reliability figure: it tells you <em>where on the scale</em> the item "
              "measures well."},
         ]},

        {"type": "content", "label": "Item Information", "title": "An item informs most around its difficulty",
         "blocks": [
             {"t": "chart", "canvas": "itemInfo",
              "title": "Item information function (item at b=0): peaks at its difficulty",
              "source": "Illustrative item information (a=1, b=0)",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("Information", [0.017, 0.04, 0.09, 0.194, 0.377, 0.606, 0.722,
                                           0.606, 0.377, 0.194, 0.09, 0.04, 0.017], "#10B981", fill=True)]},
              "options": {"__js__": INFO_OPTS}},
             {"t": "hbox", "color": "green", "html": "The peak sits at &theta; = 0 &mdash; the "
              "item's b. An item tells you most about people whose trait is near its difficulty, "
              "and little about those far from it."},
         ]},

        {"type": "content", "label": "Test Information", "title": "Add items, add information",
         "blocks": [
             {"t": "body", "html": "The <strong>test information function</strong> is just the sum "
              "of the item information functions. Where many items pile up, the test measures "
              "precisely; where items are sparse, it measures poorly."},
             {"t": "chart", "canvas": "testInfo",
              "title": "Test information (3 items at b = −1, 0, +1): broad, peaks near 0",
              "source": "Illustrative test information function",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("Test information", TEST_INFO, "#0EA5E9", fill=True)]},
              "options": {"__js__": INFO_OPTS}},
         ]},

        {"type": "content", "label": "Information And SEM", "title": "More information means less error",
         "blocks": [
             {"t": "body", "html": "Precision and information are two sides of one coin: the "
              "standard error of measurement at any &theta; is <strong>1 / &radic;information</strong>. "
              "High information &rarr; small standard error; low information &rarr; large error."},
             {"t": "chart", "canvas": "semCurve",
              "title": "Standard error varies along θ &mdash; lowest where information is highest",
              "source": "Illustrative SEM = 1 / √(test information)",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("SEM", SEM_CURVE, "#EF4444")]},
              "options": {"__js__": SEM_OPTS}},
         ]},

        {"type": "content", "label": "The Contrast", "title": "Precision is not constant &mdash; and IRT shows it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "CTT", "blocks": [
                  {"t": "body", "cls": "sm", "html": "One standard error for everyone &mdash; "
                   "pretends the test is equally precise across the whole range."}]}],
              "right": [{"t": "panel", "color": "green", "title": "IRT", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Error is <em>lowest</em> where information "
                   "peaks (usually mid-range) and rises sharply in the tails. Honest, and "
                   "actionable."}]}]},
             {"t": "hbox", "color": "amber", "html": "If you must measure the very weak or very "
              "strong precisely, you need items targeted there &mdash; the middle-heavy test will "
              "fail them."},
         ]},

        {"type": "content", "label": "Targeting", "title": "Targeting a test where it matters",
         "blocks": [
             {"t": "chart", "canvas": "infoTargeted",
              "title": "Two tests, same length: a 'high-θ' form moves the information peak right",
              "source": "Illustrative test information (items centred at θ≈0 vs θ≈+1.5)",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("Centred test (b ≈ −1,0,1)", TEST_INFO, "#0EA5E9"),
                  _line_ds("High-θ test (b ≈ 1,1.5,2)", INFO_TARGETED, "#6366F1")]},
              "options": {"__js__": INFO_OPTS}},
             {"t": "hbox", "color": "cyan", "html": "Choosing items by their b is how you "
              "<strong>target</strong> a form &mdash; e.g. to grade top performers, or to "
              "pinpoint a pass/fail cut-score."},
         ]},

        {"type": "content", "label": "Cut-Scores", "title": "Put your information where the decision is",
         "blocks": [
             {"t": "body", "html": "If a programme classifies children as 'at grade level' or not, "
              "the decision happens at one &theta; &mdash; the cut-score. That is exactly where you "
              "want maximum information and minimum error."},
             {"t": "hbox", "color": "green", "html": "Pack items with b's near the cut-score. A "
              "test can be short yet decisive if its information is concentrated where the call is "
              "actually made."},
         ]},

        {"type": "content", "label": "Adaptive Testing", "title": "How computer-adaptive tests use information",
         "blocks": [
             {"t": "body", "html": "Because items and people share a scale, a "
              "<strong>computer-adaptive test</strong> can pick each next item to be maximally "
              "informative at the test-taker's current &theta; estimate &mdash; honing in fast."},
             {"t": "flow", "steps": [
                 "Estimate θ so far",
                 "Pick the most informative unused item near that θ",
                 "Update θ from the answer",
                 "Stop when the standard error is small enough"]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Validating Scales &amp; DIF"},

        {"type": "content", "label": "Earn The Benefits", "title": "IRT's promises hold only if assumptions do",
         "blocks": [
             {"t": "body", "html": "Sample-free items, test-free scores, a clean common metric "
              "&mdash; these gifts depend on the model actually fitting the data. Validation is the "
              "work of checking that it does."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Does the model <strong>fit</strong> the responses?",
                 "Is the scale <strong>unidimensional</strong>?",
                 "Are responses <strong>locally independent</strong>?",
                 "Does each item behave the <strong>same across groups</strong> (no DIF)?"]},
         ]},

        {"type": "content", "label": "Model Fit", "title": "Checking model fit",
         "blocks": [
             {"t": "body", "html": "Fit asks whether the observed responses match what the fitted "
              "ICCs predict &mdash; overall and item by item. A badly fitting item's empirical "
              "curve departs from its modelled S-curve."},
             {"t": "hbox", "color": "amber", "html": "Use item-fit statistics and, crucially, plot "
              "the empirical vs modelled ICC. A picture catches misfit that a single index can "
              "hide &mdash; and points to the offending item."},
         ]},

        {"type": "content", "label": "Unidimensionality", "title": "Assumption 1: one trait at a time",
         "blocks": [
             {"t": "term", "word": "Unidimensionality",
              "def": "The assumption that a single latent trait accounts for the responses. The "
              "items should all tap the same underlying continuum &mdash; one theta, not several."},
             {"t": "hbox", "color": "red", "html": "A 'reading' test that secretly also measures "
              "vocabulary <em>and</em> reasoning violates this. Check with factor analysis before "
              "trusting a one-dimensional &theta;."},
         ]},

        {"type": "content", "label": "Local Independence", "title": "Assumption 2: items don't lean on each other",
         "blocks": [
             {"t": "term", "word": "Local independence",
              "def": "Once you account for theta, responses to different items are independent. "
              "Knowing the answer to one item should give no extra clue to another, beyond what "
              "theta already explains."},
             {"t": "hbox", "color": "amber", "html": "Violated by item chains &mdash; e.g. several "
              "questions about one reading passage, where missing the passage sinks them all "
              "together. Bundle or rewrite such items."},
         ]},

        {"type": "content", "label": "DIF Defined", "title": "Differential Item Functioning (DIF)",
         "blocks": [
             {"t": "term", "word": "Differential Item Functioning (DIF)",
              "def": "When two people with the SAME theta but from different groups (e.g. girls "
              "vs boys, one region vs another) have different probabilities of answering an item "
              "correctly. The item behaves differently across groups."},
             {"t": "hbox", "color": "red", "html": "DIF is potential <strong>item bias</strong>. "
              "Same trait, different odds &mdash; the item is reading something other than the "
              "trait for one group."},
         ]},

        {"type": "content", "label": "Seeing DIF", "title": "DIF makes one item's ICC split by group",
         "blocks": [
             {"t": "chart", "canvas": "difChart",
              "title": "Same item, two groups: the ICCs diverge → DIF",
              "source": "Illustrative ICCs for one item across two groups",
              "type": "line",
              "data": {"labels": THETA, "datasets": [
                  _line_ds("Group A (reference)", DIF_REF, "#0EA5E9"),
                  _line_ds("Group B (focal)", DIF_FOCAL, "#F59E0B")]},
              "options": {"__js__": ICC_OPTS}},
             {"t": "hbox", "color": "amber", "html": "At any given &theta;, Group B's success "
              "probability is lower &mdash; the item is effectively harder for them at the same "
              "trait level. That is uniform DIF."},
         ]},

        {"type": "content", "label": "DIF vs Real Gaps", "title": "DIF is not the same as a group difference",
         "blocks": [
             {"t": "body", "html": "If girls genuinely have higher reading ability than boys, "
              "they will score higher &mdash; that is a real trait difference, not DIF. DIF is when "
              "girls and boys <em>at the same ability</em> still differ on a <em>specific</em> item."},
             {"t": "hbox", "color": "cyan", "html": "DIF conditions on &theta;. It isolates item "
              "bias from true group differences &mdash; a distinction CTT cannot make cleanly."},
         ]},

        {"type": "content", "label": "Acting On DIF", "title": "What to do when an item shows DIF",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Investigate the content:</strong> a word, context or example unfamiliar "
                 "to one group (an urban example, a gendered scenario)",
                 "<strong>Check the translation:</strong> DIF across language versions often "
                 "signals a poor or unequal translation",
                 "<strong>Revise or remove</strong> biased items before reporting scores",
                 "<strong>Document</strong> the DIF review &mdash; fairness is part of validity"]},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Applications in Development"},

        {"type": "content", "label": "Learning Assessments", "title": "ASER- and NAS-style learning assessments",
         "blocks": [
             {"t": "body", "html": "Large learning assessments &mdash; India's NAS, citizen-led "
              "ASER, and cross-national studies &mdash; lean on IRT to place children on a single "
              "proficiency scale and to compare across grades, states and years."},
             {"t": "hbox", "color": "cyan", "html": "IRT is what lets 'reading at grade-2 level' "
              "mean the same thing whether a child sat form A or form B, this year or last."},
         ]},

        {"type": "content", "label": "Equating", "title": "Equating: comparing across forms and years",
         "blocks": [
             {"t": "term", "word": "Equating / linking",
              "def": "Placing different test forms onto a common theta scale &mdash; usually via "
              "shared 'anchor' items &mdash; so scores from different forms or years are directly "
              "comparable."},
             {"t": "body", "cls": "sm", "html": "Because IRT item parameters are (when the model "
              "fits) sample-independent, anchor items let you stitch separate forms into one "
              "continuous scale."},
         ]},

        {"type": "content", "label": "Why Equating Matters", "title": "Measuring change without changing the ruler",
         "blocks": [
             {"t": "body", "html": "To track learning over years you must change the questions "
              "(security, age-appropriateness) <em>without</em> changing what the score means. "
              "Equating via anchor items keeps the ruler fixed while the items rotate."},
             {"t": "hbox", "color": "red", "html": "Without equating, a 'rise in scores' could "
              "just be an easier form. Equating separates real learning gains from changes in the "
              "test."},
         ]},

        {"type": "content", "label": "Food Insecurity", "title": "FIES: a global IRT-based scale",
         "blocks": [
             {"t": "body", "html": "The <strong>Food Insecurity Experience Scale (FIES)</strong> "
              "&mdash; eight yes/no experience items &mdash; is modelled with a Rasch/1PL approach "
              "so that severity is comparable across countries and languages, underpinning SDG "
              "indicator 2.1.2."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "8 items", "label": "from 'worried' to 'a whole day without eating'", "color": "amber"},
                 {"num": "Severity = b", "label": "items ordered from mild to severe insecurity", "color": "indigo"},
                 {"num": "Equated", "label": "calibrated to a global reference scale", "color": "cyan"}]},
         ]},

        {"type": "content", "label": "Empowerment", "title": "Empowerment and agency scales",
         "blocks": [
             {"t": "body", "html": "Women's empowerment indices and agency scales combine items on "
              "mobility, decision-making and asset control. IRT checks whether they measure one "
              "coherent trait, ranks items by severity, and flags items that work differently "
              "across regions or castes."},
             {"t": "hbox", "color": "cyan", "html": "It turns a bag of agree/disagree items into a "
              "calibrated scale &mdash; and reveals which items actually discriminate between more- "
              "and less-empowered women."},
         ]},

        {"type": "content", "label": "Wealth Scales", "title": "Asset and wealth indices",
         "blocks": [
             {"t": "body", "html": "Asset-based wealth indices (the kind behind NFHS/DHS wealth "
              "quintiles) ask whether a household owns particular assets. IRT and related latent-"
              "trait methods place households on a wealth continuum from the pattern of ownership."},
             {"t": "hbox", "color": "amber", "html": "A motorcycle and a mud floor sit at very "
              "different points on the wealth scale &mdash; just as easy and hard items sit at "
              "different b's. The logic is identical."},
         ]},

        {"type": "content", "label": "Attitude Scales", "title": "Attitude, stigma and knowledge scales",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Health knowledge:</strong> grade items from basic to advanced and "
                 "measure understanding precisely where a campaign targets it",
                 "<strong>Stigma / attitude scales:</strong> order statements by how much "
                 "prejudice it takes to endorse them",
                 "<strong>Quality-of-life &amp; depression screeners:</strong> many are now built "
                 "and validated with IRT"]},
         ]},

        {"type": "content", "label": "The Payoff", "title": "What IRT gives a development programme",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Shorter instruments:</strong> keep the most informative items, cut "
                 "respondent burden",
                 "<strong>Comparable numbers:</strong> across forms, years, regions and languages",
                 "<strong>Fairer measures:</strong> DIF screening removes biased items",
                 "<strong>Targeted precision:</strong> measure best exactly where decisions are made"]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Assumptions, Limits &amp; Tools"},

        {"type": "content", "label": "Recap The Assumptions", "title": "IRT is powerful, not magic",
         "blocks": [
             {"t": "bullets", "color": "amber", "items": [
                 "<strong>Unidimensionality</strong> &mdash; one trait drives the responses",
                 "<strong>Local independence</strong> &mdash; items don't lean on each other",
                 "<strong>Correct model</strong> &mdash; the chosen 1PL/2PL/3PL actually fits",
                 "<strong>Monotonicity</strong> &mdash; more trait, higher success probability"]},
             {"t": "hbox", "color": "red", "html": "Break an assumption and the elegant guarantees "
              "&mdash; sample-free items, comparable scores &mdash; quietly stop holding."},
         ]},

        {"type": "content", "label": "Sample Size", "title": "IRT is data-hungry",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Model", "Rough sample-size guidance", "Note"],
              "rows": [
                  ["1PL / Rasch", "~200+ respondents", "Most forgiving"],
                  ["2PL", "~500+ respondents", "Estimating a needs more data"],
                  ["3PL", "~1,000+ respondents", "c is hard to estimate; often fixed"]]},
             {"t": "hbox", "color": "amber", "html": "Illustrative rules of thumb only &mdash; "
              "needs depend on test length, item quality and how spread the sample is. Small, "
              "homogeneous samples can defeat even a simple model."},
         ]},

        {"type": "content", "label": "Other Limits", "title": "Where IRT can mislead",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Garbage items in, garbage scale out</strong> &mdash; IRT cannot rescue "
                 "badly written items",
                 "<strong>A neat &theta; can hide a contested concept</strong> &mdash; 'empowerment' "
                 "is political, not just psychometric",
                 "<strong>Multidimensional traits</strong> forced onto one scale lose meaning",
                 "<strong>Black-box scores</strong> are harder for non-specialists to interpret "
                 "than a percentage"]},
         ]},

        {"type": "content", "label": "Software", "title": "Tools for fitting IRT models",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Good for", "Note"],
              "rows": [
                  ["R: mirt", "Uni- &amp; multidimensional IRT, all common models", "Free, powerful, well documented"],
                  ["R: ltm", "1PL/2PL/3PL for dichotomous &amp; graded items", "Free, gentle entry point"],
                  ["R: TAM / eRm", "Large-scale &amp; Rasch modelling", "Free; TAM mirrors big assessments"],
                  ["Stata: irt suite", "IRT within a familiar stats package", "Built-in irt commands"],
                  ["jMetrik / IRTPRO", "Point-and-click psychometrics", "Lower coding barrier"]]},
         ]},

        {"type": "content", "label": "A Workflow", "title": "A sensible IRT workflow",
         "blocks": [
             {"t": "flow", "steps": [
                 "CHECK dimensionality &amp; local independence",
                 "FIT the simplest defensible model (start Rasch)",
                 "EXAMINE item fit, a, b, (c) and information",
                 "SCREEN for DIF across key groups",
                 "REVISE items, then score &amp; report θ with its error"]},
         ]},

        {"type": "content", "label": "Communicating", "title": "Translating θ for non-specialists",
         "blocks": [
             {"t": "body", "html": "A &theta; of 1.2 means nothing to a programme officer or a "
              "parent. Part of doing IRT well is translating the scale back into language people "
              "act on &mdash; proficiency bands, 'can read a paragraph', percentile, or a clear "
              "cut-score."},
             {"t": "hbox", "color": "amber", "html": "Always report the <strong>standard error</strong> "
              "alongside the score, and describe what the cut-points mean in real-world terms. A "
              "precise number nobody understands helps no one."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "Where to go deeper",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Item Response Theory for Psychologists</em> &mdash; Embretson &amp; Reise "
                 "(the standard, readable introduction)",
                 "<em>The Theory and Practice of Item Response Theory</em> &mdash; de Ayala",
                 "<em>Fundamentals of Item Response Theory</em> &mdash; Hambleton, Swaminathan &amp; Rogers",
                 "<em>Applying the Rasch Model</em> &mdash; Bond &amp; Fox (Rasch-focused)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Survey Design</strong> and "
              "<strong>Monitoring &amp; Evaluation</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>The trait is hidden</strong> &mdash; IRT models the probability of each "
                 "response from &theta;",
                 "<strong>Higher b = harder; higher a = steeper</strong>; c is the guessing floor",
                 "<strong>Information, not one reliability number</strong> &mdash; precision varies "
                 "along &theta;, so target your test",
                 "<strong>DIF</strong> = same &theta;, different odds across groups &mdash; check "
                 "for it",
                 "<strong>The guarantees hold only if the assumptions do</strong> &mdash; validate, "
                 "don't assume"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Item Response Theory 101 &middot; Complete",
         "headline": "Now measure the<br>unmeasurable, well.",
         "byline": "From a child's reading ability to a household's food security, IRT turns "
                   "answers into honest, comparable, fair scores &mdash; if you respect its "
                   "assumptions. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
