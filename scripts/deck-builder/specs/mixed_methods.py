# -*- coding: utf-8 -*-
"""
Mixed Methods 101 — ImpactMojo 101 Series (native deck spec)
Combining quantitative & qualitative evidence in one study, for South Asian
development researchers and MEL practitioners.
Build: python3 scripts/deck-builder/build.py mixed_methods
"""

DECK = {
    "slug": "mixed-methods",
    "title": "Mixed Methods 101",
    "description": ("Mixed Methods 101 — a free foundational course for development "
                    "researchers and MEL practitioners in South Asia on intentionally "
                    "combining quantitative and qualitative evidence within a single "
                    "study: the core designs, integration, quality and worked examples. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Mixed<br>Methods<br>101",
         "sub": "Intentionally Combining Quantitative &amp; Qualitative Evidence in One "
                "Study &mdash; a Foundational Course for Development Researchers &amp; MEL "
                "Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Mixed Methods Is"},
             {"name": "Why Mix? Five Purposes"},
             {"name": "Paradigms &amp; Pragmatism"},
             {"name": "The Core Designs"},
             {"name": "Choosing a Design"},
             {"name": "Sampling in Mixed Methods"},
             {"name": "Integration: the Heart"},
             {"name": "Quality &amp; Validity"},
             {"name": "Worked Examples"},
             {"name": "Common Pitfalls"},
             {"name": "Practice &amp; Tools"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Mixed Methods Is"},

        {"type": "content", "label": "Definition", "title": "Mixing is a choice, not an accident",
         "blocks": [
             {"t": "term", "word": "Mixed methods research",
              "def": "Research that intentionally collects, analyses and integrates both "
              "quantitative and qualitative data within a single study or programme of "
              "inquiry &mdash; so the combination answers questions neither approach could "
              "answer alone."},
             {"t": "hbox", "color": "cyan", "html": "The operative word is "
              "<strong>integration</strong>. Running a survey and some interviews in the "
              "same project is not yet mixed methods &mdash; it is two studies in a trench coat."},
         ]},

        {"type": "content", "label": "More Than Both", "title": "Doing both is not the same as mixing both",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Multi-method (parallel)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A quant strand and a qual strand sit "
                   "side by side. Each is written up separately. They never meet. The reader "
                   "does the integrating &mdash; if at all."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Mixed methods", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The strands are deliberately connected: "
                   "one informs the other, or they are merged and compared. Integration is "
                   "designed in, and reported as a finding in its own right."}]}]},
             {"t": "hbox", "color": "amber", "html": "Ask of any 'mixed' study: <em>where</em> "
              "do the numbers and the words actually talk to each other?"},
         ]},

        {"type": "content", "label": "The Promise", "title": "1 + 1 = 3",
         "blocks": [
             {"t": "body", "html": "The case for mixing rests on a simple idea: integrated "
              "quantitative and qualitative findings yield insight <em>greater than the sum "
              "of the parts</em>. Numbers show the pattern; words explain the mechanism; "
              "together they make a claim each alone could only gesture at."},
             {"t": "quote",
              "text": "The combination of qualitative and quantitative methods can produce a "
              "more complete picture &mdash; the whole is greater than the sum of the parts.",
              "attr": "&mdash; paraphrasing the '1 + 1 = 3' principle, mixed-methods literature"},
         ]},

        {"type": "content", "label": "Complementary Strengths", "title": "What each strand brings",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Quantitative", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Scale, prevalence, magnitude",
                      "Comparison across groups",
                      "Generalisable to a population",
                      "Tests hypotheses; measures effect"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Qualitative", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Meaning, process, context",
                      "Why and how, in whose words",
                      "Depth on the unexpected",
                      "Generates hypotheses; explains effect"]}]}]},
             {"t": "hbox", "color": "green", "html": "Each method's weakness is the other's "
              "strength. Mixing is offsetting one set of blind spots with another."},
         ]},

        {"type": "content", "label": "A Short History", "title": "From 'wars' to a third paradigm",
         "blocks": [
             {"t": "flow", "steps": [
                 "1960s&ndash;80s: quant dominates; qual fights for legitimacy",
                 "1980s&ndash;90s: 'paradigm wars' &mdash; are the two even compatible?",
                 "1989: Greene et al. map five purposes for mixing",
                 "2000s: Creswell &amp; Plano Clark codify designs; a 'third paradigm'"]},
             {"t": "hbox", "color": "cyan", "html": "Mixed methods is now widely treated as a "
              "distinct methodology &mdash; not a truce, but a framework with its own logic."},
         ]},

        {"type": "content", "label": "In Development", "title": "Why MEL practitioners reach for it",
         "blocks": [
             {"t": "body", "html": "Development questions are stubbornly mixed. <em>Did the "
              "programme work?</em> is quantitative. <em>For whom, why, and how?</em> is "
              "qualitative. An impact figure without a mechanism is hard to act on; a rich "
              "story without scale is hard to defend."},
             {"t": "bullets", "color": "green", "items": [
                 "Explain <em>why</em> an effect is large in one district, absent in another",
                 "Surface unintended consequences a survey never asked about",
                 "Give voice and context to a hard outcome number",
                 "Build instruments grounded in how people actually talk"]},
         ]},

        {"type": "content", "label": "What It Is Not", "title": "Three honest cautions up front",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Not a quality guarantee.</strong> Two weak strands make one weak study, not a strong one.",
                 "<strong>Not 'qual to decorate quant'.</strong> A few quotes around a regression is not integration.",
                 "<strong>Not free.</strong> Mixing roughly doubles the skills, time and coordination required."]},
             {"t": "hbox", "color": "amber", "html": "Mix because the <em>question</em> demands "
              "it &mdash; never because 'mixed methods' sounds rigorous in a proposal."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Foundations", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Why mix; paradigms &amp; pragmatism",
                      "The four core designs &amp; notation",
                      "Choosing, sampling, integrating"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Practice", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Quality, validity &amp; meta-inference",
                      "Worked development examples",
                      "Pitfalls, teams, tools, writing"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Pairs with ImpactMojo's "
              "<strong>Qualitative Methods</strong> and <strong>Data Literacy</strong> 101 "
              "decks &mdash; this one is about combining them."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Why Mix? Five Purposes"},

        {"type": "content", "label": "The Framework", "title": "Greene, Caracelli &amp; Graham's five purposes",
         "blocks": [
             {"t": "body", "html": "The most-cited answer to 'why mix?' comes from a 1989 "
              "review by <strong>Jennifer Greene, Valerie Caracelli and Wendy Graham</strong>. "
              "They distilled mixed-methods studies into <strong>five distinct purposes</strong> "
              "&mdash; still the field's working vocabulary."},
             {"t": "stats", "cols": 5, "cards": [
                 {"num": "1", "label": "Triangulation", "color": "cyan"},
                 {"num": "2", "label": "Complementarity", "color": "green"},
                 {"num": "3", "label": "Development", "color": "indigo"},
                 {"num": "4", "label": "Initiation", "color": "amber"},
                 {"num": "5", "label": "Expansion", "color": "red"}]},
             {"t": "hbox", "color": "amber", "html": "Name your purpose before your design. "
              "The 'why' should drive the 'how'."},
         ]},

        {"type": "content", "label": "Purpose 1", "title": "Triangulation: do they agree?",
         "blocks": [
             {"t": "term", "word": "Triangulation",
              "def": "Using two methods to study the same phenomenon, seeking convergence or "
              "corroboration &mdash; if both point the same way, confidence rises."},
             {"t": "body", "html": "Survey data say child immunisation rose; FGDs with mothers "
              "independently describe easier access and more outreach visits. Two routes, one "
              "conclusion &mdash; the finding is more credible for it."},
             {"t": "hbox", "color": "red", "html": "Watch the trap: when the two <em>disagree</em>, "
              "that is not a failure to fix &mdash; it is a finding to explain (see 'initiation')."},
         ]},

        {"type": "content", "label": "Purpose 2", "title": "Complementarity: a fuller picture",
         "blocks": [
             {"t": "body", "html": "Here the methods examine <em>different facets</em> of the "
              "same issue, each elaborating the other. The aim is not agreement but "
              "<strong>richness</strong> &mdash; depth layered onto breadth."},
             {"t": "hbox", "color": "cyan", "html": "A survey measures <em>how many</em> "
              "adolescent girls dropped out; interviews reveal the <em>texture</em> &mdash; "
              "menstruation, distance, safety, marriage. Neither replaces the other; together "
              "they explain the dropout."},
         ]},

        {"type": "content", "label": "Purpose 3", "title": "Development: one method builds the other",
         "blocks": [
             {"t": "flow", "steps": [
                 "Qual first: interviews surface local categories &amp; language",
                 "Use them to design a valid, grounded survey instrument",
                 "Quant then: measure prevalence at scale",
                 "Each strand sequentially informs the next"]},
             {"t": "hbox", "color": "green", "html": "Development is sequential by definition: "
              "findings from method A <em>shape</em> method B &mdash; sampling, instruments or "
              "implementation."},
         ]},

        {"type": "content", "label": "Purpose 4", "title": "Initiation: provoke new questions",
         "blocks": [
             {"t": "body", "html": "<strong>Initiation</strong> deliberately looks for "
              "<em>contradiction</em> and paradox between strands &mdash; the friction that "
              "reframes the question and sparks fresh insight."},
             {"t": "hbox", "color": "amber", "html": "Survey: satisfaction with the clinic is "
              "high. Interviews: people are quietly furious about waiting times. The "
              "<em>dissonance</em> is the discovery &mdash; perhaps 'satisfaction' measured "
              "low expectations, not good service."},
         ]},

        {"type": "content", "label": "Purpose 5", "title": "Expansion: extend the breadth",
         "blocks": [
             {"t": "body", "html": "<strong>Expansion</strong> uses different methods for "
              "different components of an inquiry &mdash; commonly quant for <em>outcomes</em> "
              "and qual for <em>process</em> &mdash; to extend the study's range, not to "
              "study one thing two ways."},
             {"t": "hbox", "color": "cyan", "html": "Classic in evaluation: measure the impact "
              "(quant) <em>and</em> evaluate how implementation actually unfolded (qual) within "
              "the same study."},
         ]},

        {"type": "content", "label": "Side by Side", "title": "The five purposes at a glance",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Purpose", "Core question", "Strands"],
              "rows": [
                  ["Triangulation", "Do independent methods converge?", "Same phenomenon"],
                  ["Complementarity", "Can one enrich the other?", "Overlapping facets"],
                  ["Development", "Can one build the other?", "Sequential, A &rarr; B"],
                  ["Initiation", "Where do they contradict?", "Tension sought"],
                  ["Expansion", "Can we widen the scope?", "Different components"]]},
             {"t": "hbox", "color": "amber", "html": "Source: Greene, Caracelli &amp; Graham "
              "(1989), <em>Toward a Conceptual Framework for Mixed-Method Evaluation Designs</em>."},
         ]},

        {"type": "content", "label": "Using It", "title": "From purpose to a design decision",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Triangulation</strong> &rarr; collect concurrently, then compare",
                 "<strong>Development</strong> &rarr; collect sequentially, A informs B",
                 "<strong>Complementarity / Expansion</strong> &rarr; embed one within the other",
                 "<strong>Initiation</strong> &rarr; stay open; let contradiction redirect you"]},
             {"t": "hbox", "color": "green", "html": "The purpose points at the design; the "
              "next sections turn that into concrete blueprints."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Paradigms &amp; Pragmatism"},

        {"type": "content", "label": "Why It Comes Up", "title": "Methods carry worldviews",
         "blocks": [
             {"t": "term", "word": "Paradigm",
              "def": "A shared set of beliefs about what reality is (ontology) and how we can "
              "know it (epistemology) &mdash; the worldview a research approach is built on."},
             {"t": "body", "html": "Quantitative work grew from <strong>post-positivism</strong> "
              "(one measurable reality); much qualitative work from "
              "<strong>constructivism</strong> (realities are socially constructed). Mixing "
              "seems to ask one study to hold two worldviews at once."},
         ]},

        {"type": "content", "label": "Two Worldviews", "title": "Post-positivism vs constructivism",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Post-positivism", "Constructivism"],
              "rows": [
                  ["Reality", "One, measurable", "Multiple, constructed"],
                  ["Knower &amp; known", "Separate, objective", "Intertwined, situated"],
                  ["Goal", "Explain, predict, generalise", "Understand, interpret meaning"],
                  ["Typical method", "Survey, experiment", "Interview, ethnography"],
                  ["Logic", "Deductive, test theory", "Inductive, build theory"]]},
             {"t": "hbox", "color": "amber", "html": "Stated this starkly, the two look "
              "irreconcilable &mdash; which is exactly the objection mixed methods had to answer."},
         ]},

        {"type": "content", "label": "The Objection", "title": "The incompatibility thesis",
         "blocks": [
             {"t": "term", "word": "Incompatibility thesis",
              "def": "The claim that quantitative and qualitative methods rest on opposed, "
              "irreconcilable paradigms &mdash; so combining them in one study is "
              "philosophically incoherent."},
             {"t": "body", "html": "If methods are welded to worldviews, the argument runs, you "
              "cannot honestly mix them. This was a central charge in the "
              "<strong>'paradigm wars'</strong> of the 1980s."},
         ]},

        {"type": "content", "label": "The Answer", "title": "Pragmatism: the home of mixed methods",
         "blocks": [
             {"t": "body", "html": "Mixed-methods scholars &mdash; notably "
              "<strong>Tashakkori &amp; Teddlie</strong> &mdash; answered with "
              "<strong>pragmatism</strong>: choose methods by what works for the research "
              "<em>question</em>, not by allegiance to a paradigm."},
             {"t": "quote",
              "text": "The research question is more important than either the method or the "
              "philosophical worldview that underlies it.",
              "attr": "&mdash; the pragmatist stance, after Tashakkori &amp; Teddlie"},
         ]},

        {"type": "content", "label": "Pragmatism", "title": "What pragmatism actually claims",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Knowledge is judged by its <strong>consequences</strong> and usefulness",
                 "The forced choice between objective and subjective is <strong>false</strong>",
                 "Methods are <strong>tools</strong> &mdash; pick the fit-for-purpose one",
                 "What 'works' to answer the question is the test of a good design"]},
             {"t": "hbox", "color": "green", "html": "Pragmatism does not deny paradigms exist "
              "&mdash; it denies they must dictate your toolkit. The question is sovereign."},
         ]},

        {"type": "content", "label": "Stances", "title": "More than one way to hold the paradigms",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "A-paradigmatic / pragmatist", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Set the philosophy aside; let the question "
                   "and the practical payoff decide. The mainstream mixed-methods position."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Dialectical", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Deliberately hold opposing paradigms in "
                   "tension, mining the friction for insight &mdash; close kin to 'initiation'."}]}]},
             {"t": "hbox", "color": "amber", "html": "Other researchers adopt a "
              "<strong>transformative</strong> stance, foregrounding equity and the standpoint "
              "of marginalised groups throughout the design."},
         ]},

        {"type": "content", "label": "Common Ground", "title": "The two strands share more than they fight over",
         "blocks": [
             {"t": "bullets", "items": [
                 "Both seek to <strong>reduce error</strong> and rule out alternative explanations",
                 "Both rely on <strong>systematic, transparent</strong> procedures",
                 "Both can be done well or badly &mdash; rigour is method-agnostic",
                 "Both ultimately serve <strong>better understanding</strong> for decisions"]},
             {"t": "hbox", "color": "green", "html": "Once you see the shared commitments, "
              "combining the methods looks less like a contradiction and more like good sense."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "You can mix &mdash; with eyes open",
         "blocks": [
             {"t": "body", "html": "The incompatibility thesis is answered, not ignored. You may "
              "mix methods coherently &mdash; <em>provided</em> you can say why your question "
              "needs both and how you will reconcile what they tell you."},
             {"t": "hbox", "color": "cyan", "html": "Philosophy earns its keep here: it forces "
              "you to be explicit about your stance, so reviewers can judge the study on its "
              "own terms."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "The Core Designs"},

        {"type": "content", "label": "A Shared Language", "title": "The notation of mixed methods",
         "blocks": [
             {"t": "body", "html": "<strong>Creswell &amp; Plano Clark</strong> gave the field "
              "a compact notation for describing designs. Learn these four marks and you can "
              "write any design in a line."},
             {"t": "table",
              "head": ["Symbol", "Meaning"],
              "rows": [
                  ["QUAN / QUAL (caps)", "The dominant, prioritised strand"],
                  ["quan / qual (lower)", "The secondary, supporting strand"],
                  ["+ (plus)", "Strands run concurrently, at the same time"],
                  ["&rarr; (arrow)", "Strands run sequentially, one then the next"]]},
             {"t": "hbox", "color": "amber", "html": "Two questions define every design: "
              "<strong>timing</strong> (+ or &rarr;) and <strong>priority</strong> (which is "
              "in caps)."},
         ]},

        {"type": "content", "label": "Design 1", "title": "Convergent parallel: QUAN + QUAL",
         "blocks": [
             {"t": "raw", "html":
              '<svg viewBox="0 0 760 220" width="100%" style="max-height:230px">'
              '<rect x="40" y="30" width="280" height="64" rx="10" fill="rgba(14,165,233,0.16)" stroke="#0EA5E9" stroke-width="2"/>'
              '<text x="180" y="60" fill="#0EA5E9" font-size="22" font-weight="700" text-anchor="middle">QUAN</text>'
              '<text x="180" y="82" fill="#cbd5e1" font-size="13" text-anchor="middle">collect &amp; analyse</text>'
              '<rect x="40" y="126" width="280" height="64" rx="10" fill="rgba(99,102,241,0.16)" stroke="#6366F1" stroke-width="2"/>'
              '<text x="180" y="156" fill="#818cf8" font-size="22" font-weight="700" text-anchor="middle">QUAL</text>'
              '<text x="180" y="178" fill="#cbd5e1" font-size="13" text-anchor="middle">collect &amp; analyse</text>'
              '<text x="372" y="115" fill="#F59E0B" font-size="34" font-weight="700" text-anchor="middle">+</text>'
              '<path d="M420 110 L470 110" stroke="#94a3b8" stroke-width="2" marker-end="url(#a4)"/>'
              '<defs><marker id="a4" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#94a3b8"/></marker></defs>'
              '<rect x="476" y="78" width="244" height="64" rx="10" fill="rgba(16,185,129,0.16)" stroke="#10B981" stroke-width="2"/>'
              '<text x="598" y="106" fill="#10B981" font-size="18" font-weight="700" text-anchor="middle">MERGE &amp;</text>'
              '<text x="598" y="128" fill="#10B981" font-size="18" font-weight="700" text-anchor="middle">COMPARE</text>'
              '</svg>'},
             {"t": "hbox", "color": "cyan", "html": "Both strands run <strong>at the same "
              "time, with equal weight</strong>; results are merged and compared at "
              "interpretation. Best for <strong>triangulation</strong>."},
         ]},

        {"type": "content", "label": "Design 2", "title": "Explanatory sequential: QUAN &rarr; qual",
         "blocks": [
             {"t": "raw", "html":
              '<svg viewBox="0 0 760 150" width="100%" style="max-height:170px">'
              '<rect x="20" y="44" width="200" height="62" rx="10" fill="rgba(14,165,233,0.16)" stroke="#0EA5E9" stroke-width="2"/>'
              '<text x="120" y="72" fill="#0EA5E9" font-size="22" font-weight="700" text-anchor="middle">QUAN</text>'
              '<text x="120" y="94" fill="#cbd5e1" font-size="12" text-anchor="middle">survey &amp; results</text>'
              '<path d="M226 75 L300 75" stroke="#F59E0B" stroke-width="3" marker-end="url(#a4b)"/>'
              '<text x="263" y="60" fill="#F59E0B" font-size="13" text-anchor="middle">explain</text>'
              '<defs><marker id="a4b" markerWidth="11" markerHeight="11" refX="6" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="#F59E0B"/></marker></defs>'
              '<rect x="306" y="44" width="220" height="62" rx="10" fill="rgba(99,102,241,0.16)" stroke="#6366F1" stroke-width="2"/>'
              '<text x="416" y="72" fill="#818cf8" font-size="20" font-weight="700" text-anchor="middle">qual</text>'
              '<text x="416" y="94" fill="#cbd5e1" font-size="12" text-anchor="middle">follow-up interviews</text>'
              '<path d="M532 75 L600 75" stroke="#94a3b8" stroke-width="2" marker-end="url(#a4c)"/>'
              '<defs><marker id="a4c" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#94a3b8"/></marker></defs>'
              '<rect x="606" y="44" width="134" height="62" rx="10" fill="rgba(16,185,129,0.16)" stroke="#10B981" stroke-width="2"/>'
              '<text x="673" y="80" fill="#10B981" font-size="15" font-weight="700" text-anchor="middle">interpret</text>'
              '</svg>'},
             {"t": "hbox", "color": "cyan", "html": "Quant comes first and leads; qualitative "
              "follow-up <strong>explains the numbers</strong> &mdash; surprising results, "
              "outliers, group differences. The most common design in evaluation."},
         ]},

        {"type": "content", "label": "Design 3", "title": "Exploratory sequential: QUAL &rarr; quan",
         "blocks": [
             {"t": "raw", "html":
              '<svg viewBox="0 0 760 150" width="100%" style="max-height:170px">'
              '<rect x="20" y="44" width="210" height="62" rx="10" fill="rgba(99,102,241,0.16)" stroke="#6366F1" stroke-width="2"/>'
              '<text x="125" y="72" fill="#818cf8" font-size="22" font-weight="700" text-anchor="middle">QUAL</text>'
              '<text x="125" y="94" fill="#cbd5e1" font-size="12" text-anchor="middle">explore &amp; themes</text>'
              '<path d="M236 75 L310 75" stroke="#F59E0B" stroke-width="3" marker-end="url(#a4d)"/>'
              '<text x="273" y="60" fill="#F59E0B" font-size="13" text-anchor="middle">build</text>'
              '<defs><marker id="a4d" markerWidth="11" markerHeight="11" refX="6" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="#F59E0B"/></marker></defs>'
              '<rect x="316" y="44" width="220" height="62" rx="10" fill="rgba(14,165,233,0.16)" stroke="#0EA5E9" stroke-width="2"/>'
              '<text x="426" y="72" fill="#0EA5E9" font-size="20" font-weight="700" text-anchor="middle">quan</text>'
              '<text x="426" y="94" fill="#cbd5e1" font-size="12" text-anchor="middle">instrument &amp; test</text>'
              '<path d="M542 75 L610 75" stroke="#94a3b8" stroke-width="2" marker-end="url(#a4e)"/>'
              '<defs><marker id="a4e" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#94a3b8"/></marker></defs>'
              '<rect x="616" y="44" width="124" height="62" rx="10" fill="rgba(16,185,129,0.16)" stroke="#10B981" stroke-width="2"/>'
              '<text x="678" y="80" fill="#10B981" font-size="15" font-weight="700" text-anchor="middle">interpret</text>'
              '</svg>'},
             {"t": "hbox", "color": "cyan", "html": "Qualitative comes first and leads; it "
              "<strong>builds a grounded instrument or typology</strong> the quantitative "
              "strand then tests at scale. Matches the 'development' purpose."},
         ]},

        {"type": "content", "label": "Design 4", "title": "Embedded: one strand inside another",
         "blocks": [
             {"t": "raw", "html":
              '<svg viewBox="0 0 760 200" width="100%" style="max-height:210px">'
              '<rect x="60" y="24" width="640" height="150" rx="14" fill="rgba(14,165,233,0.10)" stroke="#0EA5E9" stroke-width="2.5"/>'
              '<text x="380" y="52" fill="#0EA5E9" font-size="20" font-weight="700" text-anchor="middle">QUAN &mdash; e.g. a trial / RCT (the larger design)</text>'
              '<rect x="250" y="78" width="260" height="74" rx="10" fill="rgba(99,102,241,0.20)" stroke="#6366F1" stroke-width="2"/>'
              '<text x="380" y="110" fill="#818cf8" font-size="18" font-weight="700" text-anchor="middle">qual</text>'
              '<text x="380" y="132" fill="#cbd5e1" font-size="13" text-anchor="middle">embedded process strand</text>'
              '</svg>'},
             {"t": "hbox", "color": "cyan", "html": "A supportive strand is <strong>nested "
              "inside</strong> a dominant design &mdash; classically a qualitative process "
              "evaluation embedded within an experiment, asking a different but related question."},
         ]},

        {"type": "content", "label": "Four Designs", "title": "The core designs, compared",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Design", "Notation", "Timing", "Best for"],
              "rows": [
                  ["Convergent parallel", "QUAN + QUAL", "Concurrent", "Triangulation, fuller picture"],
                  ["Explanatory sequential", "QUAN &rarr; qual", "Sequential", "Explaining numbers"],
                  ["Exploratory sequential", "QUAL &rarr; quan", "Sequential", "Building instruments"],
                  ["Embedded", "QUAN(qual)", "Either", "Adding a different sub-question"]]},
             {"t": "hbox", "color": "amber", "html": "Source: Creswell &amp; Plano Clark, "
              "<em>Designing and Conducting Mixed Methods Research</em>. Real studies often "
              "combine or extend these."},
         ]},

        {"type": "content", "label": "Beyond the Four", "title": "Complex &amp; multiphase designs",
         "blocks": [
             {"t": "body", "html": "The four are building blocks. Large programmes chain them "
              "into <strong>multiphase</strong> designs &mdash; an exploratory phase to build "
              "tools, a convergent phase to evaluate, an explanatory phase to interpret &mdash; "
              "across years."},
             {"t": "hbox", "color": "green", "html": "You are not picking one design forever. "
              "You are choosing the right pattern for <em>this</em> question, then connecting "
              "patterns as a programme matures."},
         ]},

        {"type": "content", "label": "Read a Notation", "title": "Practice: what does this study do?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "QUAL &rarr; QUAN", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Sequential, <em>equal</em> weight, qual "
                   "first. Explore to build a survey, then weight both strands equally at "
                   "interpretation."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "quan + QUAL", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Concurrent, qualitative-led, with a "
                   "smaller supporting quantitative strand running alongside."}]}]},
             {"t": "hbox", "color": "amber", "html": "Caps = priority, position = order, "
              "the connector = timing. Three marks, the whole design."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Choosing a Design"},

        {"type": "content", "label": "Start Here", "title": "The question chooses the design",
         "blocks": [
             {"t": "body", "html": "Do not start from 'I want to do mixed methods'. Start from "
              "the question, and let three sub-questions point you to a design: <strong>which "
              "order, which priority, which point of contact</strong>."},
             {"t": "flow", "steps": [
                 "What do I actually need to know?",
                 "Which method leads &mdash; and does the other follow or run alongside?",
                 "Which strand carries more weight for this claim?",
                 "Where will the strands meet?"]},
         ]},

        {"type": "content", "label": "Decision 1", "title": "Which order? Timing of the strands",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Concurrent ( + )", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Collect both at once. Faster; suits "
                   "triangulation. But the strands cannot inform each other's design."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Sequential ( &rarr; )", "blocks": [
                  {"t": "body", "cls": "sm", "html": "One finishes before the next begins, so A "
                   "shapes B. Slower; suits building and explaining."}]}]},
             {"t": "hbox", "color": "amber", "html": "If you need one strand to design the "
              "other, you <em>must</em> go sequential &mdash; time it into the workplan early."},
         ]},

        {"type": "content", "label": "Decision 2", "title": "Which priority? Weighting the strands",
         "blocks": [
             {"t": "body", "html": "Priority is which strand carries the main analytic load "
              "&mdash; signalled by the CAPS in the notation. It follows from the question, not "
              "from which method you find easier or fund more."},
             {"t": "bullets", "items": [
                 "<strong>QUAN-led:</strong> the headline claim is about magnitude or impact",
                 "<strong>QUAL-led:</strong> the headline claim is about meaning or process",
                 "<strong>Equal:</strong> both claims matter and stand together"]},
             {"t": "hbox", "color": "red", "html": "A frequent failure is unstated priority: a "
              "qual strand quietly demoted to decoration. Decide weighting openly, in advance."},
         ]},

        {"type": "content", "label": "Decision 3", "title": "Where will the strands meet?",
         "blocks": [
             {"t": "body", "html": "Every mixed design must name its <strong>point(s) of "
              "integration</strong> &mdash; where numbers and words actually connect. A design "
              "with no such point is multi-method, not mixed."},
             {"t": "bullets", "color": "cyan", "items": [
                 "At <strong>design</strong>: one strand builds the other's sampling/instrument",
                 "At <strong>data</strong>: one dataset is transformed to join the other",
                 "At <strong>analysis / interpretation</strong>: merge, compare, joint display"]},
         ]},

        {"type": "content", "label": "A Chooser", "title": "If your aim is&hellip; pick&hellip;",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Your aim", "Likely design"],
              "rows": [
                  ["Corroborate a finding two ways", "Convergent parallel (QUAN + QUAL)"],
                  ["Explain surprising survey results", "Explanatory sequential (QUAN &rarr; qual)"],
                  ["Build a context-valid instrument", "Exploratory sequential (QUAL &rarr; quan)"],
                  ["Understand how a trial played out", "Embedded (QUAN with qual process strand)"],
                  ["Provoke new questions from tension", "Concurrent, dialectical stance"]]},
         ]},

        {"type": "content", "label": "Constraints", "title": "Be honest about feasibility",
         "blocks": [
             {"t": "bullets", "color": "amber", "items": [
                 "<strong>Time:</strong> sequential designs need two field rounds &mdash; budget the gap",
                 "<strong>Team:</strong> do you have both quant and qual skills, or must you hire?",
                 "<strong>Money:</strong> mixing roughly doubles instruments, training, analysis",
                 "<strong>Access:</strong> can you return to the same site for the second strand?"]},
             {"t": "hbox", "color": "red", "html": "An elegant design you cannot resource "
              "becomes a poor one in practice. Match ambition to capacity."},
         ]},

        {"type": "content", "label": "Write It Down", "title": "Specify the design before fieldwork",
         "blocks": [
             {"t": "body", "html": "Pin the design in your protocol: the notation, the purpose, "
              "the priority, the timing and &mdash; above all &mdash; the planned point of "
              "integration. This is your defence against drift."},
             {"t": "hbox", "color": "green", "html": "A one-line design statement &mdash; "
              "'QUAN &rarr; qual explanatory, integrated via joint display' &mdash; tells a "
              "reviewer in seconds what you are doing and why. And document deviations as they "
              "happen: an honest account of how the design evolved beats a too-tidy one."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Sampling in Mixed Methods"},

        {"type": "content", "label": "Two Logics", "title": "Sampling pulls in opposite directions",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Quant sampling", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Probability, larger n, aims for "
                   "<strong>representativeness</strong> so findings generalise to a population."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Qual sampling", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Purposive, smaller n, aims for "
                   "<strong>information-richness</strong> &mdash; cases chosen because they "
                   "illuminate the question."}]}]},
             {"t": "hbox", "color": "amber", "html": "Mixed methods must hold both logics at "
              "once &mdash; and decide how the two samples relate."},
         ]},

        {"type": "content", "label": "Key Choice", "title": "Concurrent vs sequential sampling",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Concurrent:</strong> draw both samples independently, around the same "
                 "time &mdash; they need not overlap",
                 "<strong>Sequential:</strong> draw the second sample <em>from the results</em> "
                 "of the first &mdash; the order creates the link"]},
             {"t": "hbox", "color": "cyan", "html": "Sequential sampling is where mixing earns "
              "its keep: the first strand tells you <em>whom</em> the second should talk to."},
         ]},

        {"type": "content", "label": "Nested Samples", "title": "Drawing the qual sample from the quant",
         "blocks": [
             {"t": "term", "word": "Nested sample",
              "def": "A sample for one strand drawn as a subset of the other strand's sample "
              "&mdash; e.g. interviewing a purposive selection of survey respondents."},
             {"t": "body", "html": "In an explanatory design, you might survey 1,200 households, "
              "then interview 30 chosen <em>from</em> them &mdash; deliberately spanning high "
              "and low outcomes to explain the spread."},
             {"t": "hbox", "color": "green", "html": "Nesting lets you link a person's numbers "
              "to their words &mdash; the tightest form of integration at the case level."},
         ]},

        {"type": "content", "label": "Selecting Cases", "title": "Whom to follow up &mdash; on purpose",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<strong>Extreme cases:</strong> the biggest gainers and the non-responders",
                 "<strong>Typical cases:</strong> households near the median, to ground the norm",
                 "<strong>Confirming / disconfirming:</strong> cases that test the emerging story",
                 "<strong>Maximum variation:</strong> span the range deliberately"]},
             {"t": "hbox", "color": "amber", "html": "The survey gives you a sampling frame for "
              "the interviews that no convenience approach could match &mdash; use it."},
         ]},

        {"type": "content", "label": "Sizing", "title": "How big should each strand be?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Quant: powered", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Size for the precision or power the claim "
                   "needs &mdash; margin of error, effect size, subgroups."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Qual: saturation", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Size for <strong>saturation</strong> "
                   "&mdash; keep sampling until new interviews stop yielding new themes."}]}]},
             {"t": "hbox", "color": "red", "html": "Do not judge the qual strand by quant logic. "
              "'Only 25 interviews?' is the wrong question if those 25 reached saturation."},
         ]},

        {"type": "content", "label": "Frame Matters", "title": "Mind the gap between the two frames",
         "blocks": [
             {"t": "body", "html": "If the survey frame and the interview frame differ &mdash; "
              "different villages, different eligibility &mdash; your integration compares "
              "apples and oranges. Make the relationship between frames explicit."},
             {"t": "hbox", "color": "cyan", "html": "Best practice in development MEL: sample "
              "the qualitative cases from <em>within</em> the quantitative sites, so context "
              "and outcomes line up."},
         ]},

        {"type": "content", "label": "Equity Lens", "title": "Sample to see the excluded",
         "blocks": [
             {"t": "body", "html": "A representative survey can still drown out small, "
              "marginalised groups. Purposive qualitative sampling is how you deliberately "
              "<strong>over-listen</strong> to those the averages bury &mdash; Dalit, Adivasi, "
              "disabled, migrant respondents."},
             {"t": "hbox", "color": "green", "html": "Mixed methods can correct for whom the "
              "numbers miss &mdash; but only if you design the qual sample to do exactly that."},
         ]},

        {"type": "content", "label": "Plan It", "title": "A sampling plan for both strands",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "State each strand's frame, method and target size, and the <em>rationale</em>",
                 "State whether the samples are independent, nested or identical",
                 "If sequential, state the rule for selecting the second from the first",
                 "Name how the two samples will be linked at analysis"]},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Integration: the Heart"},

        {"type": "content", "label": "The Core Idea", "title": "Integration is what makes it mixed",
         "blocks": [
             {"t": "term", "word": "Integration",
              "def": "The deliberate point(s) at which the quantitative and qualitative strands "
              "are brought together &mdash; connected, merged or embedded &mdash; so that the "
              "combination yields more than the strands apart."},
             {"t": "hbox", "color": "red", "html": "If you can remove either strand and the "
              "conclusions barely change, you never really integrated. Integration is the test "
              "of a genuine mixed-methods study."},
         ]},

        {"type": "content", "label": "Three Ways", "title": "Connecting, merging, embedding",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Approach", "How it works", "Typical design"],
              "rows": [
                  ["Connecting", "One strand's results lead into the next", "Sequential designs"],
                  ["Merging", "Bring both datasets together to compare", "Convergent parallel"],
                  ["Embedding", "One strand nested to support the other", "Embedded design"]]},
             {"t": "hbox", "color": "amber", "html": "These map onto the designs: the design "
              "you chose already implies <em>how</em> you will integrate."},
         ]},

        {"type": "content", "label": "Tool 1", "title": "The joint display",
         "blocks": [
             {"t": "body", "html": "A <strong>joint display</strong> is a single table or "
              "figure that arrays quantitative and qualitative results side by side around a "
              "common organising principle &mdash; the workhorse of integration."},
             {"t": "raw", "html":
              '<table style="width:100%;border-collapse:collapse;font-size:14px;margin-top:6px">'
              '<thead><tr style="background:rgba(14,165,233,0.14)">'
              '<th style="border:1px solid #334155;padding:8px;text-align:left;color:#67e8f9">Sub-group</th>'
              '<th style="border:1px solid #334155;padding:8px;text-align:left;color:#67e8f9">QUAN: outcome</th>'
              '<th style="border:1px solid #334155;padding:8px;text-align:left;color:#a5b4fc">QUAL: why (illustrative)</th>'
              '<th style="border:1px solid #334155;padding:8px;text-align:left;color:#6ee7b7">Meta-inference</th></tr></thead>'
              '<tbody>'
              '<tr><td style="border:1px solid #334155;padding:8px">High-uptake block</td>'
              '<td style="border:1px solid #334155;padding:8px">Uptake ~80%</td>'
              '<td style="border:1px solid #334155;padding:8px">"The ASHA visits every week"</td>'
              '<td style="border:1px solid #334155;padding:8px">Frontline contact drives uptake</td></tr>'
              '<tr><td style="border:1px solid #334155;padding:8px">Low-uptake block</td>'
              '<td style="border:1px solid #334155;padding:8px">Uptake ~35%</td>'
              '<td style="border:1px solid #334155;padding:8px">"The centre is two hours away"</td>'
              '<td style="border:1px solid #334155;padding:8px">Distance, not awareness, is the barrier</td></tr>'
              '</tbody></table>'},
             {"t": "hbox", "color": "cyan", "html": "The right-most column &mdash; the "
              "<em>meta-inference</em> &mdash; is the integration. The numbers and quotes only "
              "set it up."},
         ]},

        {"type": "content", "label": "Tool 2", "title": "Following a thread",
         "blocks": [
             {"t": "body", "html": "<strong>Following a thread</strong> starts from a striking "
              "finding in one strand and traces it deliberately through the other &mdash; "
              "weaving a single line of argument across both datasets."},
             {"t": "flow", "steps": [
                 "Spot a surprising survey result (a sharp gender gap)",
                 "Pull the thread into the interviews on that theme",
                 "Return to the data to test what the interviews suggest",
                 "Report one integrated narrative, not two"]},
         ]},

        {"type": "content", "label": "Tool 3", "title": "Data transformation",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Quantitising:</strong> turn qualitative codes into counts &mdash; "
                 "'how many interviewees raised distance?' &mdash; to merge with survey data",
                 "<strong>Qualitising:</strong> turn quantitative profiles into narrative "
                 "typologies &mdash; 'the reluctant adopter' &mdash; to compare with cases"]},
             {"t": "hbox", "color": "amber", "html": "Powerful but lossy: counting themes can "
              "strip their meaning. Transform with care, and keep the original alongside."},
         ]},

        {"type": "content", "label": "When They Agree", "title": "Convergence builds confidence",
         "blocks": [
             {"t": "body", "html": "When both strands point the same way, you have "
              "<strong>convergence</strong> &mdash; the strongest, most reassuring outcome of "
              "integration. The claim now rests on two independent legs."},
             {"t": "hbox", "color": "green", "html": "Report convergence explicitly: 'survey "
              "and interviews independently identified distance as the binding constraint' is a "
              "stronger sentence than either finding alone."},
         ]},

        {"type": "content", "label": "When They Clash", "title": "Divergence is a finding, not a failure",
         "blocks": [
             {"t": "body", "html": "When strands <strong>disagree</strong>, resist the urge to "
              "pick a winner or bury the conflict. Dissonance often exposes a flaw in one "
              "measure &mdash; or a deeper truth the averages hid."},
             {"t": "bullets", "color": "red", "items": [
                 "Re-examine both measures: which question were they really answering?",
                 "Look for the subgroup or context that reconciles them",
                 "Report the tension honestly &mdash; it is frequently the best insight"]},
         ]},

        {"type": "content", "label": "The Payoff", "title": "Meta-inferences: the 1 + 1 = 3",
         "blocks": [
             {"t": "term", "word": "Meta-inference",
              "def": "An overall conclusion drawn by integrating the inferences from both "
              "strands &mdash; a claim that neither the quantitative nor the qualitative "
              "analysis could have reached alone."},
             {"t": "hbox", "color": "cyan", "html": "The meta-inference is the deliverable of "
              "mixed methods. If your write-up has none &mdash; only a results section per "
              "strand &mdash; the integration has not happened yet."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Quality &amp; Validity"},

        {"type": "content", "label": "A Harder Bar", "title": "Three quality questions, not one",
         "blocks": [
             {"t": "body", "html": "A mixed study must satisfy quality on three fronts: the "
              "quant strand on its own terms, the qual strand on its own terms, and &mdash; "
              "uniquely &mdash; the <strong>quality of the integration</strong> itself."},
             {"t": "flow", "steps": [
                 "Is the QUAN strand rigorous? (validity, reliability, power)",
                 "Is the QUAL strand rigorous? (credibility, transferability)",
                 "Is the MIXING rigorous? (does integration add genuine value?)"]},
         ]},

        {"type": "content", "label": "Each Strand", "title": "Hold each to its own standard",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Concern", "Quantitative term", "Qualitative term"],
              "rows": [
                  ["Truth value", "Internal validity", "Credibility"],
                  ["Applicability", "External validity", "Transferability"],
                  ["Consistency", "Reliability", "Dependability"],
                  ["Neutrality", "Objectivity", "Confirmability"]]},
             {"t": "hbox", "color": "red", "html": "Do not impose quant criteria on the qual "
              "strand or vice versa. Each tradition has its own well-developed standards "
              "&mdash; use them."},
         ]},

        {"type": "content", "label": "The Mixing Standard", "title": "Legitimation",
         "blocks": [
             {"t": "term", "word": "Legitimation",
              "def": "The validity framework specific to mixed methods (Onwuegbuzie &amp; "
              "Johnson): the extent to which combining the strands yields credible, defensible "
              "meta-inferences."},
             {"t": "body", "html": "Where single-method work asks 'is this valid?', mixed "
              "methods adds: 'is the <em>integration</em> legitimate?' &mdash; a distinct "
              "question Tashakkori &amp; Teddlie also pushed the field to formalise."},
         ]},

        {"type": "content", "label": "Legitimation Types", "title": "Ways integration can go wrong",
         "blocks": [
             {"t": "bullets", "color": "amber", "items": [
                 "<strong>Sample integration:</strong> do the two samples support a joint claim?",
                 "<strong>Weakness minimisation:</strong> does each strand cover the other's gaps?",
                 "<strong>Conversion:</strong> is quantitising / qualitising done faithfully?",
                 "<strong>Political:</strong> are conflicting findings reconciled honestly, "
                 "not by fiat?"]},
             {"t": "hbox", "color": "cyan", "html": "Each is a place to interrogate your own "
              "study before a reviewer does."},
         ]},

        {"type": "content", "label": "Two Dimensions", "title": "Design quality vs interpretive rigour",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Design quality", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Is the design suitable, adequate and "
                   "faithfully implemented? Did the strands actually run as planned, with the "
                   "integration point intact?"}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Interpretive rigour", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Do the meta-inferences truly follow from "
                   "the integrated evidence? Are they consistent, plausible and not "
                   "over-reaching?"}]}]},
             {"t": "hbox", "color": "amber", "html": "After Tashakkori &amp; Teddlie's "
              "<em>inference quality</em>: a good design badly interpreted &mdash; or vice "
              "versa &mdash; still fails."},
         ]},

        {"type": "content", "label": "Strengthen It", "title": "Practices that raise quality",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Pre-specify the design, priority and integration point in a protocol",
                 "Use joint displays so integration is visible and checkable",
                 "Triangulate &mdash; and report divergence, do not hide it",
                 "Member-check qualitative findings; report quant uncertainty",
                 "Keep an audit trail of decisions across both strands"]},
         ]},

        {"type": "content", "label": "Reporting", "title": "Report the mixing, not just the methods",
         "blocks": [
             {"t": "body", "html": "Reporting guidance (e.g. <strong>GRAMMS</strong> &mdash; "
              "Good Reporting of A Mixed Methods Study) asks you to justify the design, describe "
              "each strand, and crucially <strong>show where and how you integrated</strong>."},
             {"t": "hbox", "color": "red", "html": "Common reviewer complaint: a paper reports "
              "two strands but never the integration. State the meta-inference explicitly, or "
              "the mixing is invisible."},
         ]},

        {"type": "content", "label": "Bottom Line", "title": "Quality is mostly about integration",
         "blocks": [
             {"t": "body", "html": "A mixed study can have a flawless survey and superb "
              "interviews and still be weak &mdash; if the two never genuinely meet. The "
              "distinctive quality question is always: <em>did mixing add value, defensibly?</em>"},
             {"t": "hbox", "color": "cyan", "html": "Judge the join, not just the parts. That "
              "is what separates mixed methods from two studies stapled together."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Worked Examples"},

        {"type": "content", "label": "Example 1", "title": "An RCT with an embedded process evaluation",
         "blocks": [
             {"t": "body", "html": "A cash-transfer programme is tested with a "
              "<strong>randomised trial</strong> (QUAN). Nested inside is a qualitative "
              "<strong>process evaluation</strong> (qual): how was the cash spent, who in the "
              "household decided, what got in the way?"},
             {"t": "hbox", "color": "cyan", "html": "Notation: <strong>QUAN(qual)</strong>, "
              "embedded. The trial measures <em>whether</em> it worked; the embedded strand "
              "explains <em>why</em>, and flags whether the mechanism matched the theory of change."},
         ]},

        {"type": "content", "label": "Example 1, cont.", "title": "Why the qual strand earns its place",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Trial alone says", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'Consumption rose by X; the effect was "
                   "larger for female-headed households.' True &mdash; but mute on mechanism."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Embedded qual adds", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Women described controlling the transfer "
                   "for the first time &mdash; explaining the heterogeneity the trial only "
                   "detected."}]}]},
             {"t": "hbox", "color": "amber", "html": "The meta-inference &mdash; 'the effect "
              "ran through women's control of the cash' &mdash; needed both strands."},
         ]},

        {"type": "content", "label": "Example 2", "title": "A survey explained by follow-up interviews",
         "blocks": [
             {"t": "body", "html": "A district health survey (QUAN) finds institutional "
              "delivery is high overall but stubbornly low in three blocks. Purposive "
              "<strong>follow-up interviews</strong> (qual) in those blocks explain the gap "
              "&mdash; an <strong>explanatory sequential</strong> design."},
             {"t": "raw", "html":
              '<svg viewBox="0 0 760 120" width="100%" style="max-height:130px">'
              '<rect x="20" y="34" width="230" height="52" rx="9" fill="rgba(14,165,233,0.16)" stroke="#0EA5E9" stroke-width="2"/>'
              '<text x="135" y="58" fill="#0EA5E9" font-size="16" font-weight="700" text-anchor="middle">QUAN: survey finds</text>'
              '<text x="135" y="76" fill="#cbd5e1" font-size="12" text-anchor="middle">3 blocks lagging</text>'
              '<path d="M256 60 L322 60" stroke="#F59E0B" stroke-width="3" marker-end="url(#a9)"/>'
              '<defs><marker id="a9" markerWidth="11" markerHeight="11" refX="6" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 z" fill="#F59E0B"/></marker></defs>'
              '<rect x="328" y="34" width="240" height="52" rx="9" fill="rgba(99,102,241,0.16)" stroke="#6366F1" stroke-width="2"/>'
              '<text x="448" y="58" fill="#818cf8" font-size="16" font-weight="700" text-anchor="middle">qual: interviews there</text>'
              '<text x="448" y="76" fill="#cbd5e1" font-size="12" text-anchor="middle">reveal the barrier</text>'
              '<path d="M574 60 L636 60" stroke="#94a3b8" stroke-width="2" marker-end="url(#a9b)"/>'
              '<defs><marker id="a9b" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#94a3b8"/></marker></defs>'
              '<rect x="642" y="34" width="98" height="52" rx="9" fill="rgba(16,185,129,0.16)" stroke="#10B981" stroke-width="2"/>'
              '<text x="691" y="64" fill="#10B981" font-size="14" font-weight="700" text-anchor="middle">act</text>'
              '</svg>'},
         ]},

        {"type": "content", "label": "Example 2, joint display", "title": "Reading the two together",
         "blocks": [
             {"t": "chart", "canvas": "mmDeliveryChart",
              "title": "Institutional delivery by block (%) &mdash; illustrative",
              "source": "Illustrative, patterned on district HMIS-style data",
              "type": "bar",
              "data": {"labels": ["District avg", "Block A", "Block B", "Block C"],
                       "datasets": [{"label": "Institutional delivery (%)",
                                     "data": [84, 41, 38, 44],
                                     "backgroundColor": ["#6366F1", "#EF4444", "#EF4444", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100, title:{display:true,text:'%'}} } }"}},
             {"t": "hbox", "color": "cyan", "html": "Interviews (illustrative) attributed the "
              "three low blocks to a closed sub-centre and night-time transport fears &mdash; "
              "the meta-inference the bars alone could not give."},
         ]},

        {"type": "content", "label": "Example 3", "title": "Building an empowerment scale, locally",
         "blocks": [
             {"t": "body", "html": "An <strong>exploratory sequential</strong> study (QUAL "
              "&rarr; quan): in-depth interviews first surface how women in a region actually "
              "describe agency &mdash; in mobility, money and voice. Those categories build a "
              "survey scale that is then validated at scale."},
             {"t": "hbox", "color": "green", "html": "The payoff: an instrument grounded in "
              "<em>local</em> meaning, not imported from another context &mdash; the "
              "'development' purpose in action, answering a validity problem head-on."},
         ]},

        {"type": "content", "label": "Example 4", "title": "Triangulating a corruption estimate",
         "blocks": [
             {"t": "body", "html": "A <strong>convergent parallel</strong> study estimates "
              "leakage in a welfare scheme three ways at once: a household survey of benefits "
              "received, administrative records of benefits disbursed, and qualitative "
              "interviews on how diversion happens."},
             {"t": "hbox", "color": "amber", "html": "Where the three converge, confidence is "
              "high. Where the survey and records <em>diverge</em>, the interviews explain the "
              "gap &mdash; turning a discrepancy into the finding."},
         ]},

        {"type": "content", "label": "RealWorld Evaluation", "title": "Mixing under real constraints",
         "blocks": [
             {"t": "body", "html": "<strong>Michael Bamberger</strong> and colleagues "
              "(<em>RealWorld Evaluation</em>) argue mixed methods is often the most practical "
              "response to development reality: tight budgets, short timelines, no baseline, "
              "and political pressure."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Use existing secondary data to substitute for a missing baseline",
                 "Add a small qual strand to interpret a thin quant one (or vice versa)",
                 "Triangulate to compensate when no single method can be done fully"]},
         ]},

        {"type": "content", "label": "Common Thread", "title": "What the examples share",
         "blocks": [
             {"t": "body", "html": "In every case the value lives in the join: the trial needed "
              "the mechanism, the survey needed the explanation, the scale needed the local "
              "voice, the estimate needed corroboration. None is two studies side by side."},
             {"t": "hbox", "color": "green", "html": "When you sketch your own study, write the "
              "meta-inference you hope to reach <em>first</em> &mdash; then check both strands "
              "are actually needed to get there."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Common Pitfalls"},

        {"type": "content", "label": "Pitfall 1", "title": "Parallel play: no integration",
         "blocks": [
             {"t": "body", "html": "The commonest failure: a quant chapter and a qual chapter "
              "that never speak. Two methods were used; nothing was <em>mixed</em>. The reader "
              "is left to do the integration the authors avoided."},
             {"t": "hbox", "color": "red", "html": "Diagnostic: delete one strand. If the "
              "conclusions survive intact, you had parallel play, not mixed methods."},
         ]},

        {"type": "content", "label": "Pitfall 2", "title": "Qual as decoration",
         "blocks": [
             {"t": "body", "html": "A regression table dressed up with three illustrative "
              "quotes is not integration &mdash; it is garnish. The qualitative strand here "
              "adds colour but no independent evidence and no meta-inference."},
             {"t": "hbox", "color": "amber", "html": "Quotes should <em>change</em> what you "
              "conclude, not merely illustrate a number you already had. Otherwise the qual "
              "strand is doing no analytic work."},
         ]},

        {"type": "content", "label": "Pitfall 3", "title": "Unequal weighting by accident",
         "blocks": [
             {"t": "body", "html": "Priority should be a <em>decision</em>, not a side-effect "
              "of which strand had more money or a more confident analyst. Too often the survey "
              "silently dominates and the interviews are demoted at write-up."},
             {"t": "hbox", "color": "red", "html": "If the qual strand cost a third of the "
              "budget but gets one paragraph, ask whether priority was chosen &mdash; or just "
              "happened."},
         ]},

        {"type": "content", "label": "Pitfall 4", "title": "Under-estimating skills &amp; time",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Skills gap", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Few researchers are equally strong in "
                   "both traditions. A team weak on one side produces a lopsided study with a "
                   "token strand."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Time gap", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Sequential designs need two field rounds "
                   "and the gap between. Budgets and timelines built for one method "
                   "under-resource the second."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Plan for both costs up front &mdash; or "
              "the weaker strand becomes the decoration you did not intend."},
         ]},

        {"type": "content", "label": "Pitfall 5", "title": "Forcing methods the question doesn't need",
         "blocks": [
             {"t": "body", "html": "Sometimes a single method answers the question best. "
              "Bolting on a second strand 'because mixed methods is rigorous' wastes resources "
              "and dilutes focus &mdash; <strong>methodolatry</strong>, not method."},
             {"t": "hbox", "color": "green", "html": "The honest test: can you state a question "
              "that genuinely needs both? If not, do one method well rather than two methods "
              "thinly."},
         ]},

        {"type": "content", "label": "Pitfall 6", "title": "Ignoring divergence",
         "blocks": [
             {"t": "body", "html": "When the strands disagree, the temptation is to quietly "
              "trust the numbers and shelve the interviews (or the reverse). Suppressing "
              "divergence throws away the study's most informative result."},
             {"t": "hbox", "color": "red", "html": "Reviewers notice a too-tidy convergence. "
              "Report disagreement, and what you think it means &mdash; that is rigour, not "
              "weakness."},
         ]},

        {"type": "content", "label": "Pitfall 7", "title": "Vague design, mid-study drift",
         "blocks": [
             {"t": "body", "html": "Without a pre-specified design, priority and integration "
              "point, a study drifts: the planned sequential link is skipped, the joint display "
              "never gets built, and 'mixed methods' becomes a label, not a method."},
             {"t": "hbox", "color": "amber", "html": "A one-line design statement in the "
              "protocol is the cheapest insurance against drift &mdash; write it before you "
              "collect a single data point."},
         ]},

        {"type": "content", "label": "Avoiding Them", "title": "A pre-flight checklist",
         "compact": True,
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Can I name the question that needs <em>both</em> strands?",
                 "Have I stated the design, priority and timing in notation?",
                 "Have I named the integration point &mdash; before fieldwork?",
                 "Does the team have real skills in both traditions?",
                 "Is there time and budget for the second strand, properly?",
                 "Will I report divergence as openly as convergence?"]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Practice &amp; Tools"},

        {"type": "content", "label": "Build the Team", "title": "Mixing needs mixed skills",
         "blocks": [
             {"t": "body", "html": "Few people do both traditions equally well, so most strong "
              "mixed-methods work is <strong>team</strong> work &mdash; pairing quant and qual "
              "specialists who genuinely respect each other's craft."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Bring both specialists into <em>design</em>, not just analysis",
                 "Agree the integration point together, early",
                 "Make space for the strands to challenge each other's findings"]},
         ]},

        {"type": "content", "label": "Software", "title": "Tools for each strand &mdash; and the join",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Good for", "Note"],
              "rows": [
                  ["R / Python", "Quant analysis, reproducible workflows", "Free, scriptable"],
                  ["Stata / SPSS", "Survey analysis with weights", "Common in MEL shops"],
                  ["NVivo / ATLAS.ti", "Coding qualitative data", "Support joint-display matrices"],
                  ["Dedoose", "Built for mixed-methods integration", "Links codes to variables"],
                  ["KoboToolbox / ODK", "Collecting both data types in the field", "Free, offline-capable"]]},
             {"t": "hbox", "color": "amber", "html": "No tool integrates <em>for</em> you. "
              "Software stores and links the data; the meta-inference is still yours to make."},
         ]},

        {"type": "content", "label": "Writing It Up", "title": "Structuring a mixed-methods report",
         "blocks": [
             {"t": "bullets", "items": [
                 "State the <strong>design and rationale</strong> in notation, up front",
                 "Report each strand clearly &mdash; but do not stop there",
                 "Devote a dedicated <strong>integration</strong> section to joint displays",
                 "Lead the discussion with the <strong>meta-inferences</strong>",
                 "Be explicit about convergence <em>and</em> divergence"]},
             {"t": "hbox", "color": "green", "html": "If a reader can find your meta-inference "
              "in thirty seconds, the write-up has done its job."},
         ]},

        {"type": "content", "label": "Publishing", "title": "Getting mixed work past reviewers",
         "blocks": [
             {"t": "body", "html": "Mixed-methods papers are often rejected for "
              "<em>insufficient integration</em> or for a strand judged thin by single-method "
              "reviewers. Pre-empt both: justify the mixing and show the join."},
             {"t": "hbox", "color": "cyan", "html": "Use a reporting standard such as GRAMMS, "
              "and consider a journal or section that understands mixed designs &mdash; reviewers "
              "matched to the method judge it fairly."},
         ]},

        {"type": "content", "label": "Reading List", "title": "The foundational texts",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Creswell &amp; Plano Clark &mdash; <em>Designing and Conducting Mixed Methods "
                 "Research</em> (the designs &amp; notation)",
                 "Greene &mdash; <em>Mixed Methods in Social Inquiry</em> (purposes &amp; "
                 "the dialectical stance)",
                 "Tashakkori &amp; Teddlie &mdash; <em>Handbook of Mixed Methods</em> "
                 "(pragmatism, legitimation, inference quality)",
                 "Bamberger et al. &mdash; <em>RealWorld Evaluation</em> (mixing under "
                 "development constraints)"]},
         ]},

        {"type": "content", "label": "Go Deeper", "title": "Where to keep learning",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Journal of Mixed Methods Research</strong> &mdash; the field's home journal",
                 "<strong>BetterEvaluation</strong> &mdash; practical mixed-methods guidance for MEL",
                 "<strong>3ie</strong> &amp; <strong>JPAL</strong> &mdash; evaluations that embed qual in trials",
                 "<strong>GRAMMS</strong> reporting criteria &mdash; a checklist for your write-up"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Qualitative Methods</strong>, <strong>Data Literacy</strong> and "
              "<strong>Theory of Change</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Mix on purpose</strong> &mdash; intentional combination, not 'both at once'",
                 "<strong>Let the question choose the design</strong> &mdash; timing &amp; priority",
                 "<strong>Integration is the heart</strong> &mdash; joint displays, meta-inferences",
                 "<strong>Divergence is a finding</strong> &mdash; never suppress it",
                 "<strong>1 + 1 = 3</strong> only when the strands genuinely meet"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Mixed Methods 101 &middot; Complete",
         "headline": "Now make the<br>numbers and words<br>talk to each other.",
         "byline": "Mixed methods is not doing both &mdash; it is designing the point where "
                   "quantitative and qualitative evidence meet, so the whole exceeds the sum of "
                   "its parts. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
