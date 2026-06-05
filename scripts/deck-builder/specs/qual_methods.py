# -*- coding: utf-8 -*-
"""
Qualitative Methods 101 — ImpactMojo 101 Series (native deck spec)
Foundational qualitative research methods for South Asian development practitioners.
Build: python3 scripts/deck-builder/build.py qual_methods
"""

DECK = {
    "slug": "qual-methods",
    "title": "Qualitative Methods 101",
    "description": ("Qualitative Methods 101 — a free foundational course for development "
                    "practitioners and researchers in South Asia. Design and conduct rigorous "
                    "qualitative research: paradigms, purposive sampling, interviews, focus "
                    "groups, observation, participatory and visual methods, coding, thematic "
                    "analysis, trustworthiness and ethics. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Qualitative<br>Methods<br>101",
         "sub": "Asking <em>Why</em> and <em>How</em> &mdash; a Foundational Course on "
                "Qualitative Research for Development Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "~90 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Qualitative Research Is", "slides": "Slides 4&ndash;10"},
             {"name": "Paradigms &amp; Approaches", "slides": "Slides 12&ndash;19"},
             {"name": "Designing a Qualitative Study", "slides": "Slides 21&ndash;27"},
             {"name": "Sampling", "slides": "Slides 29&ndash;36"},
             {"name": "In-Depth &amp; Semi-Structured Interviews", "slides": "Slides 38&ndash;45"},
             {"name": "Focus Group Discussions", "slides": "Slides 47&ndash;54"},
             {"name": "Observation &amp; Ethnography", "slides": "Slides 56&ndash;62"},
             {"name": "Participatory &amp; Visual Methods", "slides": "Slides 64&ndash;71"},
             {"name": "Data Management &amp; Coding", "slides": "Slides 73&ndash;79"},
             {"name": "Thematic Analysis &amp; Interpretation", "slides": "Slides 81&ndash;88"},
             {"name": "Trustworthiness, Ethics &amp; Reading", "slides": "Slides 90&ndash;99"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Qualitative Research Is &amp; When To Use It"},

        {"type": "content", "label": "Definition", "title": "Qualitative research studies meaning",
         "blocks": [
             {"t": "body", "html": "Where quantitative research counts and measures, "
              "<strong>qualitative research</strong> seeks to understand how people make sense "
              "of their lives, in their own words and contexts. It works with text, talk, "
              "images and observed behaviour &mdash; not numbers."},
             {"t": "term", "word": "Qualitative research",
              "def": "The systematic study of meaning, process and lived experience in "
              "context &mdash; producing rich, detailed, non-numerical data and interpreting "
              "it to understand the <em>why</em> and <em>how</em> behind what people do."},
             {"t": "hbox", "color": "cyan", "html": "It is not 'soft' or 'unscientific'. Done "
              "well, it is systematic, rigorous and transparent &mdash; just with different "
              "standards of quality than statistics."},
         ]},

        {"type": "content", "label": "The Questions", "title": "Different questions, different tools",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Quantitative asks", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "How many? How much? How often?",
                      "Did the outcome change &mdash; by how much?",
                      "Is the difference statistically significant?",
                      "How is X distributed across the population?"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Qualitative asks", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Why did it work &mdash; or fail?",
                      "How do people experience this scheme?",
                      "What does 'empowerment' mean to them?",
                      "What process led to this outcome?"]}]}],
             },
             {"t": "hbox", "color": "amber", "html": "Match the method to the question. A "
              "<em>why</em> or <em>how</em> question rarely yields to a survey alone."},
         ]},

        {"type": "content", "label": "When To Use It", "title": "When qualitative is the right choice",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Exploring</strong> a new or poorly understood phenomenon",
                 "<strong>Understanding process</strong> &mdash; how change actually happens",
                 "<strong>Hearing</strong> marginalised voices in their own terms",
                 "<strong>Explaining</strong> a surprising quantitative finding",
                 "<strong>Generating</strong> hypotheses, theory and survey instruments",
                 "Studying <strong>sensitive</strong> or context-bound topics"]},
         ]},

        {"type": "content", "label": "Complementarity", "title": "Numbers and stories, together",
         "blocks": [
             {"t": "flow", "steps": [
                 "QUANTITATIVE: 18% of girls drop out after Class 8",
                 "QUALITATIVE: interviews reveal why &mdash; distance, safety, marriage",
                 "INSIGHT: the barrier is the journey, not the school",
                 "ACTION: cycles &amp; safe transport, not new classrooms"]},
             {"t": "hbox", "color": "green", "html": "Numbers tell you <em>that</em> something "
              "is happening; qualitative work tells you <em>why</em> &mdash; and what to do "
              "about it. Mixed methods are often strongest."},
         ]},

        {"type": "content", "label": "What It Produces", "title": "Rich, thick, contextual data",
         "blocks": [
             {"t": "term", "word": "Thick description",
              "def": "Clifford Geertz's term for detailed accounts that capture not just "
              "behaviour but its context and meaning &mdash; so a reader can grasp why an act "
              "matters to the people involved."},
             {"t": "body", "html": "A wink is not just an eye movement: it could be a twitch, "
              "a flirtation, a signal or a parody. <strong>Thick description</strong> records "
              "enough context to tell which &mdash; that interpretive layer is the point."},
         ]},

        {"type": "content", "label": "Strengths", "title": "What qualitative work does best",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Depth", "label": "Rich understanding of a few cases", "color": "cyan"},
                 {"num": "Context", "label": "Findings grounded in lived setting", "color": "green"},
                 {"num": "Flexibility", "label": "Design can adapt as you learn", "color": "indigo"},
                 {"num": "Voice", "label": "Participants speak in their own words", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Limits", "title": "What it cannot do &mdash; and that's fine",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "It does <strong>not</strong> measure prevalence &mdash; you cannot say '60% feel X'",
                 "It does <strong>not</strong> aim for statistical generalisation to a population",
                 "It is <strong>not</strong> faster or cheaper for large-scale tracking",
                 "It cannot be judged by sample size or representativeness alone"]},
             {"t": "hbox", "color": "amber", "html": "These are not weaknesses to apologise "
              "for &mdash; they are simply outside the method's purpose. Judge qualitative "
              "work by depth and rigour, not by how many people it counted."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Paradigms &amp; Approaches"},

        {"type": "content", "label": "Why Paradigms", "title": "Your assumptions shape your method",
         "blocks": [
             {"t": "body", "html": "Behind every study sits a <strong>paradigm</strong> &mdash; "
              "a set of beliefs about what reality is (ontology) and how we can know it "
              "(epistemology). These quietly decide what counts as good evidence."},
             {"t": "term", "word": "Paradigm",
              "def": "A worldview &mdash; the basic assumptions about the nature of reality and "
              "knowledge that guide how a researcher frames questions, collects data and "
              "judges truth."},
         ]},

        {"type": "content", "label": "Two Poles", "title": "Positivist vs interpretivist",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Positivist", "blocks": [
                  {"t": "body", "cls": "sm", "html": "There is one objective reality 'out there', "
                   "knowable through neutral measurement. The researcher stands apart. Drives "
                   "most quantitative work."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Interpretivist", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Reality is socially constructed; people "
                   "make meaning. Knowledge is built <em>with</em> participants, not extracted. "
                   "Underpins most qualitative work."}]}]},
             {"t": "hbox", "color": "amber", "html": "Most qualitative research leans "
              "interpretivist &mdash; but critical and pragmatic paradigms sit alongside, and "
              "many practitioners mix them deliberately."},
         ]},

        {"type": "content", "label": "More Paradigms", "title": "Critical and pragmatic stances",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Critical / transformative", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Research should expose and challenge power, "
                   "caste, class and gender injustice &mdash; and contribute to change. Aligned "
                   "with participatory and feminist methods."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Pragmatic", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Use whatever method answers the question "
                   "best. Comfortable mixing qualitative and quantitative. Common in applied "
                   "development research."}]}]},
         ]},

        {"type": "content", "label": "Five Traditions", "title": "Major qualitative approaches",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Approach", "Central question", "Signature method"],
              "rows": [
                  ["Grounded theory", "What theory explains this process?", "Iterative coding, constant comparison"],
                  ["Phenomenology", "What is the lived experience of X?", "In-depth experiential interviews"],
                  ["Ethnography", "How does this culture / group work?", "Prolonged immersion, observation"],
                  ["Case study", "How &amp; why, in this bounded case?", "Multiple sources on one case"],
                  ["Narrative", "What story do people tell of their lives?", "Life-history interviews"]]},
             {"t": "hbox", "color": "cyan", "html": "The approach you choose shapes your "
              "sampling, your data and your analysis &mdash; pick it on purpose, not by habit."},
         ]},

        {"type": "content", "label": "Grounded Theory", "title": "Building theory from the data up",
         "blocks": [
             {"t": "body", "html": "Developed by <strong>Glaser &amp; Strauss</strong> (1967), "
              "grounded theory builds theory <em>inductively</em> from data rather than testing "
              "a pre-set hypothesis. Coding and data collection proceed together until a theory "
              "emerges."},
             {"t": "flow", "steps": [
                 "Collect data",
                 "Code &amp; compare incidents (constant comparison)",
                 "Sample more cases to test emerging ideas (theoretical sampling)",
                 "Refine until categories saturate &rarr; theory"]},
         ]},

        {"type": "content", "label": "Phenomenology", "title": "Studying lived experience",
         "blocks": [
             {"t": "body", "html": "<strong>Phenomenology</strong> asks what an experience is "
              "like from the inside &mdash; the essence of, say, living with a disability, or "
              "of a mother's first contact with an anganwadi. It brackets the researcher's "
              "assumptions to centre the participant's world."},
             {"t": "hbox", "color": "indigo", "html": "Data is deep, first-person and "
              "experiential. Often just a handful of participants, each interviewed at length."},
         ]},

        {"type": "content", "label": "Ethnography", "title": "Understanding a way of life",
         "blocks": [
             {"t": "body", "html": "<strong>Ethnography</strong> immerses the researcher in a "
              "community over time &mdash; living among, observing and participating &mdash; to "
              "understand culture, norms and everyday practice from within. Its roots are in "
              "anthropology."},
             {"t": "hbox", "color": "amber", "html": "South Asia has a rich ethnographic "
              "tradition &mdash; from village studies of the 1950s&ndash;60s to today's "
              "ethnographies of bureaucracy, markets and migration. It rewards patience over "
              "speed."},
         ]},

        {"type": "content", "label": "Case Study", "title": "One bounded case, many lenses",
         "blocks": [
             {"t": "term", "word": "Case study",
              "def": "An in-depth, multi-source examination of a single bounded unit &mdash; a "
              "village, a programme, an organisation, an event &mdash; studied in its real-life "
              "context. (Associated with Robert Yin and Robert Stake.)"},
             {"t": "body", "html": "Strong for <em>how</em> and <em>why</em> questions about "
              "contemporary events you cannot control. A single SHG federation, studied through "
              "interviews, records and observation, can illuminate a whole model."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Designing a Qualitative Study"},

        {"type": "content", "label": "Start Here", "title": "Design before you collect anything",
         "blocks": [
             {"t": "body", "html": "Qualitative research is flexible, but flexibility is not the "
              "same as improvisation. A clear design &mdash; question, approach, participants, "
              "methods, analysis plan &mdash; is what makes the study rigorous and defensible."},
             {"t": "flow", "steps": [
                 "RESEARCH QUESTION: what do we genuinely not know?",
                 "APPROACH: grounded theory? ethnography? case study?",
                 "PARTICIPANTS &amp; METHODS: who, how, how many?",
                 "ANALYSIS PLAN: how will meaning be drawn out?"]},
         ]},

        {"type": "content", "label": "Good Questions", "title": "What a strong qualitative question looks like",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Strong", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "'How do widows in rural Bihar navigate access to pensions?'",
                      "Open, exploratory, focused on process &amp; meaning",
                      "Lets the answer surprise you"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Weak", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "'How many widows receive pensions?'",
                      "Closed, countable &mdash; a survey question",
                      "Presumes you already know the categories"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Qualitative questions usually begin with "
              "<strong>how</strong>, <strong>what</strong> or <strong>in what way</strong> "
              "&mdash; rarely with <em>how many</em>."},
         ]},

        {"type": "content", "label": "Conceptual Framework", "title": "Map the ideas guiding your study",
         "blocks": [
             {"t": "term", "word": "Conceptual framework",
              "def": "A visual or written map of the key concepts, assumptions and expected "
              "relationships that frame your study &mdash; drawn from theory, literature and "
              "your own experience. It guides what you look at without dictating what you find."},
             {"t": "body", "html": "It is a <em>working</em> map, not a hypothesis to confirm. "
              "Expect to revise it as fieldwork teaches you what you missed."},
         ]},

        {"type": "content", "label": "Rigor By Design", "title": "Build quality in from the start",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Choose methods that genuinely <strong>fit</strong> the question",
                 "Plan for <strong>multiple sources</strong> to triangulate (interviews + observation + documents)",
                 "Anticipate <strong>negative cases</strong> &mdash; who might contradict your emerging story?",
                 "Decide how you will keep an <strong>audit trail</strong> of decisions",
                 "Plan <strong>reflexivity</strong> &mdash; how will you track your own influence?"]},
             {"t": "hbox", "color": "green", "html": "Trustworthiness is engineered into the "
              "design, not bolted on at the end."},
         ]},

        {"type": "content", "label": "Emergent Design", "title": "A plan that can learn",
         "blocks": [
             {"t": "body", "html": "Unlike a survey fixed before launch, qualitative design is "
              "often <strong>emergent</strong>: early interviews reshape later ones, and the "
              "sample grows in the direction the data points. This is a feature, not sloppiness."},
             {"t": "hbox", "color": "amber", "html": "Document every change and why you made it. "
              "Emergent design demands <em>more</em> discipline in record-keeping, not less."},
         ]},

        {"type": "content", "label": "How Much Data", "title": "Depth over breadth",
         "blocks": [
             {"t": "chart", "canvas": "qualScopeChart",
              "title": "Qualitative vs quantitative: how scope trades off (illustrative)",
              "source": "Illustrative schematic",
              "type": "bar",
              "data": {"labels": ["Number of cases", "Depth per case", "Context captured", "Generalisability"],
                       "datasets": [
                           {"label": "Quantitative", "data": [9, 2, 3, 8],
                            "backgroundColor": "#0EA5E9"},
                           {"label": "Qualitative", "data": [2, 9, 9, 3],
                            "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ scales:{ y:{ min:0, max:10, title:{display:true,text:'Relative emphasis (illustrative)'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Qualitative work deliberately trades "
              "breadth for depth. Twelve rich interviews can teach more than a thousand thin "
              "ones &mdash; if chosen and analysed well."},
         ]},

        {"type": "content", "label": "Mixed Methods", "title": "Designing across the divide",
         "blocks": [
             {"t": "table",
              "head": ["Design", "Sequence", "Purpose"],
              "rows": [
                  ["Exploratory", "Qual &rarr; Quant", "Qual builds the survey instrument"],
                  ["Explanatory", "Quant &rarr; Qual", "Qual explains a survey finding"],
                  ["Convergent", "Qual &amp; Quant together", "Triangulate two views of one issue"],
                  ["Embedded", "One inside the other", "Qual adds depth to an RCT or vice versa"]]},
             {"t": "hbox", "color": "green", "html": "In development evaluation, qualitative work "
              "embedded in a larger study often explains <em>why</em> the headline number came "
              "out the way it did."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Sampling"},

        {"type": "content", "label": "Different Logic", "title": "Not random &mdash; purposeful",
         "blocks": [
             {"t": "body", "html": "Qualitative sampling does <strong>not</strong> aim for a "
              "statistically representative slice. It aims to select cases that are "
              "<em>information-rich</em> &mdash; the people, sites or events most likely to "
              "illuminate the question."},
             {"t": "term", "word": "Purposive sampling",
              "def": "Deliberately selecting participants because of what they can teach you "
              "about the phenomenon &mdash; not by chance, but by relevance, richness and fit "
              "to the research question."},
         ]},

        {"type": "content", "label": "Strategies", "title": "Flavours of purposive sampling",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Strategy", "Logic", "Good for"],
              "rows": [
                  ["Maximum variation", "Span the diversity deliberately", "Common patterns across difference"],
                  ["Typical case", "The 'ordinary' instance", "Describing the norm"],
                  ["Extreme / deviant", "The unusual case", "Outliers, failures, exemplars"],
                  ["Critical case", "'If it's true here&hellip;'", "A telling, decisive instance"],
                  ["Homogeneous", "A tight, similar group", "Focus groups, in-depth focus"],
                  ["Confirming / disconfirming", "Seek cases that test the theory", "Strengthening rigour"]]},
         ]},

        {"type": "content", "label": "Theoretical Sampling", "title": "Let the data choose who's next",
         "blocks": [
             {"t": "body", "html": "In grounded theory, <strong>theoretical sampling</strong> "
              "means deciding whom to approach next based on what your emerging analysis needs "
              "&mdash; chasing the gaps and testing the categories, not filling a quota."},
             {"t": "flow", "steps": [
                 "Analyse what you have",
                 "Spot a gap or untested idea",
                 "Select the next case to probe it",
                 "Repeat until categories are full"]},
         ]},

        {"type": "content", "label": "Snowball", "title": "Reaching hidden and hard-to-find groups",
         "blocks": [
             {"t": "term", "word": "Snowball sampling",
              "def": "Asking participants to refer others who fit the study &mdash; building the "
              "sample through social chains. Essential for hidden, stigmatised or hard-to-reach "
              "populations who appear on no list."},
             {"t": "hbox", "color": "amber", "html": "Useful for sex workers, undocumented "
              "migrants, manual scavengers or survivors of violence &mdash; but referrals "
              "travel within networks, so start from several unconnected seeds to avoid one "
              "narrow circle."},
         ]},

        {"type": "content", "label": "Saturation", "title": "Knowing when to stop",
         "blocks": [
             {"t": "term", "word": "Data saturation",
              "def": "The point at which new interviews stop yielding new codes, themes or "
              "insights &mdash; the data has begun to repeat. A core stopping rule in much "
              "qualitative research."},
             {"t": "body", "html": "Saturation is a judgement, not a magic number. You reach it "
              "when additional cases confirm rather than extend what you already understand."},
         ]},

        {"type": "content", "label": "See It", "title": "How new themes taper off",
         "blocks": [
             {"t": "chart", "canvas": "saturationChart",
              "title": "New themes discovered per additional interview (illustrative)",
              "source": "Illustrative saturation curve",
              "type": "line",
              "data": {"labels": ["2", "4", "6", "8", "10", "12", "14", "16", "18", "20"],
                       "datasets": [{"label": "New themes added",
                                     "data": [9, 7, 6, 4, 3, 2, 1, 1, 0, 0],
                                     "borderColor": "#10B981",
                                     "backgroundColor": "rgba(16,185,129,0.08)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'New themes per interview'} }, x:{ title:{display:true,text:'Interviews conducted'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "By around interview 12&ndash;16 here, "
              "little new emerges &mdash; saturation. The exact point depends on scope, "
              "diversity and the breadth of your question."},
         ]},

        {"type": "content", "label": "Small-n Logic", "title": "Why a few cases can be enough",
         "blocks": [
             {"t": "body", "html": "Qualitative studies are often built on a dozen interviews or "
              "a single case &mdash; and that is legitimate. The goal is "
              "<strong>analytic generalisation</strong> (to theory and concepts), not "
              "<strong>statistical generalisation</strong> (to a population)."},
             {"t": "hbox", "color": "amber", "html": "'But your sample is only 15!' misreads the "
              "method. You are not estimating a proportion &mdash; you are understanding a "
              "process deeply enough that it transfers to similar settings."},
         ]},

        {"type": "content", "label": "Practical Sizes", "title": "Rough guides, not rules",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "5&ndash;25", "label": "in-depth interviews for a focused study",
                  "color": "cyan", "source": "Indicative ranges"},
                 {"num": "3&ndash;6", "label": "focus groups per audience segment",
                  "color": "green", "source": "Indicative"},
                 {"num": "1&ndash;a few", "label": "cases in a case study", "color": "indigo"}]},
             {"t": "hbox", "color": "red", "html": "Treat these as starting points, never "
              "targets. Saturation and the question &mdash; not a fixed number &mdash; decide "
              "when you are done."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "In-Depth &amp; Semi-Structured Interviews"},

        {"type": "content", "label": "The Workhorse", "title": "The interview is qualitative research's core tool",
         "blocks": [
             {"t": "body", "html": "Most development qualitative work rests on the "
              "<strong>semi-structured interview</strong> &mdash; a guided conversation that "
              "follows a flexible list of topics while letting the participant lead where it "
              "matters."},
             {"t": "term", "word": "Semi-structured interview",
              "def": "An interview organised around an open guide of themes and key questions, "
              "but free to follow up, reorder and probe &mdash; balancing comparability across "
              "interviews with depth in each."},
         ]},

        {"type": "content", "label": "The Spectrum", "title": "From rigid to open",
         "blocks": [
             {"t": "table",
              "head": ["Type", "Structure", "Best for"],
              "rows": [
                  ["Structured", "Fixed wording &amp; order", "Comparability; near a survey"],
                  ["Semi-structured", "Guide + freedom to probe", "Most qualitative studies"],
                  ["Unstructured", "A topic, then follow the person", "Life histories, ethnography"]]},
             {"t": "hbox", "color": "cyan", "html": "Semi-structured is the sweet spot for most "
              "practitioners: enough structure to compare across interviews, enough freedom to "
              "discover the unexpected."},
         ]},

        {"type": "content", "label": "The Guide", "title": "Build an interview guide, not a questionnaire",
         "blocks": [
             {"t": "bullets", "items": [
                 "Open <strong>broadly</strong> &mdash; easy, non-threatening 'grand tour' questions first",
                 "Group questions by <strong>theme</strong>, moving from general to specific",
                 "Use <strong>open-ended</strong> wording &mdash; never yes/no",
                 "Save <strong>sensitive</strong> topics until rapport is built",
                 "Keep it short &mdash; a guide of themes, not a script of 40 questions"]},
         ]},

        {"type": "content", "label": "Question Craft", "title": "Ask open, neutral questions",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Do", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "'Tell me about a typical day&hellip;'",
                      "'What was that like for you?'",
                      "'Can you walk me through&hellip;?'"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Avoid", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Leading: 'Don't you find the scheme helpful?'",
                      "Double-barrelled: 'clean and safe?'",
                      "Jargon: 'How is your empowerment?'"]}]}]},
         ]},

        {"type": "content", "label": "Probing", "title": "The probe is where depth comes from",
         "blocks": [
             {"t": "body", "html": "A <strong>probe</strong> gently deepens an answer without "
              "leading it. The richest data usually comes <em>after</em> the first reply, when "
              "you ask the participant to go further."},
             {"t": "bullets", "color": "cyan", "items": [
                 "<strong>Silence</strong> &mdash; the most underused probe; let them fill it",
                 "<strong>Echo:</strong> repeat their last words as a question",
                 "<strong>Elaboration:</strong> 'Tell me more about that&hellip;'",
                 "<strong>Specifying:</strong> 'Can you give me an example?'"]},
         ]},

        {"type": "content", "label": "Rapport", "title": "People talk when they feel safe",
         "blocks": [
             {"t": "bullets", "items": [
                 "Meet in a place <strong>they</strong> find comfortable and private",
                 "Open with warmth and small talk; explain who you are and why",
                 "Listen more than you speak &mdash; aim for 80/20",
                 "Match pace and register; never rush a hesitation",
                 "Be honest about what the research can and cannot do for them"]},
             {"t": "hbox", "color": "amber", "html": "In South Asian fieldwork, gender, caste, "
              "language and the presence of family members all shape who will speak freely. "
              "Plan the setting deliberately."},
         ]},

        {"type": "content", "label": "Power", "title": "The interview is never an equal exchange",
         "blocks": [
             {"t": "body", "html": "The researcher usually holds more power &mdash; of class, "
              "language, education, institution. Participants may tell you what they think you "
              "want to hear, or what is safe to say. Naming this is the first step to "
              "managing it."},
             {"t": "hbox", "color": "red", "html": "A literate outsider with a clipboard "
              "interviewing a Dalit landless woman carries the weight of every prior "
              "encounter. Reflexivity about power is not optional &mdash; it is method."},
         ]},

        {"type": "content", "label": "Language", "title": "Multilingual realities of the field",
         "blocks": [
             {"t": "bullets", "items": [
                 "Interview in the participant's <strong>own language or dialect</strong> wherever possible",
                 "If using an interpreter, brief them as a research partner, not a translation machine",
                 "Beware concepts that <strong>don't translate</strong> &mdash; 'empowerment', 'stress', 'rights'",
                 "Record original phrases; meaning often lives in the exact local words"]},
             {"t": "hbox", "color": "cyan", "html": "Translation is interpretation. Every step "
              "from Bhojpuri speech to English transcript loses and reshapes meaning &mdash; "
              "document the chain."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Focus Group Discussions"},

        {"type": "content", "label": "What It Is", "title": "A facilitated group conversation",
         "blocks": [
             {"t": "term", "word": "Focus group discussion (FGD)",
              "def": "A facilitated discussion among a small group (typically 6&ndash;10 people) "
              "on a focused topic &mdash; designed to surface shared views, norms, disagreements "
              "and the social construction of meaning through interaction."},
             {"t": "body", "html": "The data is not just what individuals say &mdash; it is what "
              "the <em>group</em> produces together: the consensus, the debate, the silences."},
         ]},

        {"type": "content", "label": "When It Shines", "title": "What FGDs do that interviews can't",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Reveal <strong>shared norms</strong> and community-level views",
                 "Surface <strong>disagreement</strong> and debate in real time",
                 "Generate ideas through <strong>interaction</strong> &mdash; one comment sparks another",
                 "Efficiently explore a topic with several voices at once"]},
         ]},

        {"type": "content", "label": "Composition", "title": "Homogeneous enough to speak freely",
         "blocks": [
             {"t": "body", "html": "Group members should be <strong>similar enough</strong> on "
              "what matters (gender, age, status) that everyone feels safe speaking &mdash; but "
              "varied enough to spark discussion."},
             {"t": "hbox", "color": "red", "html": "In South Asia, mixing genders, castes or "
              "employers and workers in one FGD usually silences the less powerful. Run "
              "<em>separate</em> groups &mdash; women-only, youth-only &mdash; and compare across them."},
         ]},

        {"type": "content", "label": "Logistics", "title": "Getting the practicalities right",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "6&ndash;10", "label": "participants per group", "color": "cyan"},
                 {"num": "60&ndash;90 min", "label": "typical duration", "color": "green"},
                 {"num": "2 staff", "label": "a facilitator + a note-taker", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Choose a neutral, accessible venue; sit in "
              "a circle; arrange childcare and timing so women and workers can actually attend. "
              "Access shapes who is in the room."},
         ]},

        {"type": "content", "label": "Facilitation", "title": "The facilitator's craft",
         "blocks": [
             {"t": "bullets", "items": [
                 "Set <strong>ground rules</strong>: one voice at a time, all views welcome, confidentiality",
                 "Ask open questions, then <strong>step back</strong> and let the group talk",
                 "Draw out the <strong>quiet</strong>; gently rein in the dominant",
                 "Stay <strong>neutral</strong> &mdash; don't signal which answers you like",
                 "Watch the clock and the energy; close with a summary check"]},
         ]},

        {"type": "content", "label": "Group Dynamics", "title": "The group is a force in the data",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Watch for", "blocks": [
                  {"t": "bullets", "sm": True, "color": "amber", "items": [
                      "Dominant voices crowding out others",
                      "Groupthink &mdash; false consensus",
                      "Social-desirability: 'correct' public answers"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Use the note-taker for", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Who spoke, who stayed silent",
                      "Body language and reactions",
                      "Where the room agreed or split"]}]}]},
         ]},

        {"type": "content", "label": "When Not To", "title": "Times to skip the FGD",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Sensitive or stigmatised</strong> topics &mdash; violence, sexuality, debt, caste shame",
                 "When you need <strong>individual</strong> experiences, not group norms",
                 "Where <strong>power gaps</strong> in the group will silence people",
                 "When confidentiality between participants cannot be assured"]},
             {"t": "hbox", "color": "amber", "html": "For sensitive matters, the private "
              "in-depth interview protects the participant and yields more honest data. Choose "
              "the method that keeps people safe."},
         ]},

        {"type": "content", "label": "Analysing", "title": "Read interaction, not just transcript",
         "blocks": [
             {"t": "body", "html": "When you analyse an FGD, attend to the "
              "<strong>interaction</strong>: where did consensus form, where did it crack, "
              "what could <em>not</em> be said? The disagreements are often the richest data."},
             {"t": "hbox", "color": "cyan", "html": "Treat the group, not the individual, as "
              "the unit. And never report an FGD finding as if it were a head-count of opinions."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Observation &amp; Ethnography"},

        {"type": "content", "label": "Why Observe", "title": "What people do, not just what they say",
         "blocks": [
             {"t": "body", "html": "People cannot always articulate what they do &mdash; and "
              "sometimes what they say differs from what they do. "
              "<strong>Observation</strong> captures practice, routine, ritual and the taken-"
              "for-granted that no interview surfaces."},
             {"t": "quote", "text": "The most familiar things are hardest to see precisely "
              "because we stop noticing them.",
              "attr": "&mdash; a guiding intuition of ethnographic fieldwork"},
         ]},

        {"type": "content", "label": "A Spectrum", "title": "Degrees of participation",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Role", "Researcher's stance", "Trade-off"],
              "rows": [
                  ["Complete observer", "Detached, unseen", "No influence, but thin understanding"],
                  ["Observer-as-participant", "Mostly watching, some joining", "Balance of distance &amp; access"],
                  ["Participant-as-observer", "Mostly joining, known as researcher", "Rich access, more influence"],
                  ["Complete participant", "Fully immersed, covert", "Deep insight, but ethically fraught"]]},
             {"t": "hbox", "color": "cyan", "html": "Most development fieldwork sits in the "
              "middle &mdash; openly a researcher, but participating enough to understand from "
              "the inside."},
         ]},

        {"type": "content", "label": "Participant Observation", "title": "Learning by taking part",
         "blocks": [
             {"t": "term", "word": "Participant observation",
              "def": "The ethnographer's core method: taking part in the daily life of a group "
              "while systematically observing and recording it &mdash; understanding a setting "
              "by experiencing it, over time."},
             {"t": "body", "html": "Sitting through gram sabha meetings month after month, or "
              "working alongside ASHA workers, reveals how things <em>actually</em> run &mdash; "
              "the workarounds, hierarchies and informal rules no document records."},
         ]},

        {"type": "content", "label": "Field Notes", "title": "If it isn't written down, it didn't happen",
         "blocks": [
             {"t": "bullets", "items": [
                 "Jot brief <strong>scratch notes</strong> discreetly in the field",
                 "Write full <strong>field notes</strong> the same day &mdash; memory fades fast",
                 "Separate <strong>observation</strong> from <strong>interpretation</strong> on the page",
                 "Record the mundane: who sat where, what was said, what was avoided",
                 "Date, time and locate every entry"]},
             {"t": "hbox", "color": "amber", "html": "Field notes are your data. Discipline here "
              "&mdash; daily, detailed, dated &mdash; separates ethnography from anecdote."},
         ]},

        {"type": "content", "label": "Note Layers", "title": "Three things to capture",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Descriptive", "label": "What happened &mdash; concrete, factual", "color": "cyan"},
                 {"num": "Reflective", "label": "What it might mean &mdash; emerging ideas", "color": "indigo"},
                 {"num": "Personal", "label": "Your feelings, doubts, reactions", "color": "amber"}]},
             {"t": "hbox", "color": "green", "html": "Keeping the three layers distinct lets you "
              "later separate evidence from interpretation from your own bias."},
         ]},

        {"type": "content", "label": "Reflexivity", "title": "You are part of what you study",
         "blocks": [
             {"t": "term", "word": "Reflexivity",
              "def": "The continuous, critical examination of how the researcher's identity, "
              "assumptions and presence shape the data and its interpretation &mdash; and making "
              "that influence visible rather than pretending it away."},
             {"t": "body", "html": "Your gender, caste, class, language and institution change "
              "what people show and tell you. Reflexivity does not remove this &mdash; it makes "
              "it part of the analysis."},
         ]},

        {"type": "content", "label": "Positionality", "title": "Insider or outsider?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Insider access", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Sharing language, place or community can "
                   "open doors and build trust &mdash; but may blind you to what feels 'obvious'."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Outsider distance", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Being from outside can let you notice the "
                   "taken-for-granted &mdash; but you must work harder for trust and context."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Most researchers are partly both. Name your "
              "<strong>positionality</strong> openly &mdash; it is a strength to examine, not a "
              "flaw to hide."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Participatory &amp; Visual Methods"},

        {"type": "content", "label": "A Shift In Power", "title": "Research with, not on, people",
         "blocks": [
             {"t": "body", "html": "Participatory methods hand analytical power to communities "
              "themselves &mdash; people map, rank, diagram and interpret their own reality. The "
              "researcher facilitates rather than extracts."},
             {"t": "quote", "text": "Whose reality counts? The reality of the few, or the "
              "reality of the many poor?",
              "attr": "&mdash; Robert Chambers, pioneer of participatory approaches"},
         ]},

        {"type": "content", "label": "PRA / PLA", "title": "Participatory Rural Appraisal and its Indian roots",
         "blocks": [
             {"t": "term", "word": "PRA / PLA",
              "def": "Participatory Rural Appraisal (later Participatory Learning &amp; Action): "
              "a family of facilitated, visual, group methods that enable communities &mdash; "
              "including non-literate people &mdash; to analyse their own conditions and act."},
             {"t": "body", "html": "Associated with <strong>Robert Chambers</strong> and the "
              "IDS at Sussex, PRA grew through extensive practice across India and South Asia "
              "in the late 1980s and 1990s, deeply shaping NGO and government fieldwork."},
         ]},

        {"type": "content", "label": "The Toolkit", "title": "Common participatory tools",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "What it does", "Reveals"],
              "rows": [
                  ["Social mapping", "Community draws its own settlement", "Households, services, exclusion"],
                  ["Resource mapping", "Map land, water, forests", "Access &amp; control of resources"],
                  ["Transect walk", "Walk a line across the village", "Land use, conditions, the overlooked"],
                  ["Seasonal calendar", "Chart the year's rhythms", "Hunger months, work, migration"],
                  ["Wealth ranking", "Community sorts households", "Local definitions of poverty"],
                  ["Venn diagram", "Map institutions &amp; their closeness", "Power, links, who matters"]]},
         ]},

        {"type": "content", "label": "Transect Walk", "title": "Walking the village together",
         "blocks": [
             {"t": "body", "html": "A <strong>transect walk</strong> is a structured stroll "
              "across the community with residents, observing and discussing land, water, "
              "housing and problems as you go. The walk surfaces what a seated meeting misses "
              "&mdash; and reaches the hamlets on the edge."},
             {"t": "hbox", "color": "cyan", "html": "Who guides the walk matters: route it "
              "through Dalit and Adivasi tolas, not only the dominant-caste centre, or you will "
              "map only the powerful."},
         ]},

        {"type": "content", "label": "Mapping", "title": "Maps drawn by those who live there",
         "blocks": [
             {"t": "body", "html": "When community members draw their own map &mdash; on the "
              "ground with sticks, seeds and chalk &mdash; they include what matters to "
              "<em>them</em> and place themselves in it. The map becomes a conversation, not "
              "just a record."},
             {"t": "hbox", "color": "amber", "html": "The product is valuable; the "
              "<em>process</em> &mdash; the debate while drawing &mdash; is often where the real "
              "insight lives. Record both."},
         ]},

        {"type": "content", "label": "Photovoice", "title": "Participants document their own world",
         "blocks": [
             {"t": "term", "word": "Photovoice",
              "def": "A participatory visual method in which community members take photographs "
              "of their lives and concerns, then discuss and caption them &mdash; putting the "
              "camera, and the framing of the story, in participants' hands."},
             {"t": "body", "html": "Powerful for engaging youth, women and others whose "
              "perspectives are usually filtered through outsiders &mdash; and for advocacy, "
              "where the images speak directly to decision-makers."},
         ]},

        {"type": "content", "label": "Strengths &amp; Cautions", "title": "Participatory methods are not a free pass",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Strengths", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Include non-literate &amp; marginalised voices",
                      "Build local ownership and action",
                      "Surface local categories &amp; priorities"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Cautions", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Can be co-opted as a ritual that excludes",
                      "Dominant voices may still capture the process",
                      "'Participation' without power to act is hollow"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Chambers himself warned against PRA "
              "becoming a hurried, extractive box-ticking exercise. The attitude and behaviour "
              "of the facilitator matter more than the tool."},
         ]},

        {"type": "content", "label": "Ethics Of Visuals", "title": "Special care with images",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Get <strong>consent</strong> for taking <em>and</em> for using photographs",
                 "Recognise photos can <strong>identify</strong> people who cannot be anonymised",
                 "Agree who <strong>owns</strong> the images and where they may appear",
                 "Protect participants who photograph <strong>sensitive</strong> or risky subjects"]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Data Management &amp; Coding"},

        {"type": "content", "label": "First, Get Organised", "title": "Manage data before you analyse it",
         "blocks": [
             {"t": "body", "html": "Qualitative projects drown in material &mdash; recordings, "
              "transcripts, field notes, photos, consent forms. Disciplined "
              "<strong>data management</strong> from day one is what makes analysis possible "
              "and ethical."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Label every file by participant <strong>code</strong>, never name",
                 "Keep a master log linking codes to (securely stored) identities",
                 "Back up; encrypt sensitive files; control who can access them"]},
         ]},

        {"type": "content", "label": "Transcription", "title": "Turning talk into text",
         "blocks": [
             {"t": "body", "html": "<strong>Transcription</strong> converts recordings into "
              "text you can analyse. It is slow &mdash; roughly four to six hours per hour of "
              "audio &mdash; and full of interpretive choices."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Verbatim", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Every word, pause, 'um' and laugh. Needed "
                   "for fine discourse analysis."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Cleaned / intelligent", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Tidied for readability, keeping meaning. "
                   "Common for thematic analysis."}]}]},
         ]},

        {"type": "content", "label": "Translation", "title": "Transcribe and translate with care",
         "blocks": [
             {"t": "bullets", "items": [
                 "Decide: transcribe in the <strong>original language</strong>, then translate &mdash; or translate live?",
                 "Original-then-translate preserves nuance but doubles the work",
                 "Keep <strong>key terms</strong> in the original with a gloss &mdash; some words have no English equal",
                 "Have a second person check translations of sensitive passages"]},
             {"t": "hbox", "color": "amber", "html": "Every translation decision is an "
              "analytic decision. Be transparent about who translated, from what, and how."},
         ]},

        {"type": "content", "label": "What Is Coding", "title": "Coding: tagging meaning in the data",
         "blocks": [
             {"t": "term", "word": "Coding",
              "def": "Systematically labelling segments of data with short tags ('codes') that "
              "capture their meaning &mdash; the foundational step that turns pages of text into "
              "organised, analysable material."},
             {"t": "body", "html": "A code might be a phrase like <em>'fear of travel'</em> or "
              "<em>'pension delay'</em>. You apply it everywhere that idea appears, so you can "
              "later gather and compare all instances."},
         ]},

        {"type": "content", "label": "Two Directions", "title": "Inductive vs deductive coding",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Inductive (bottom-up)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Codes emerge <em>from</em> the data. You "
                   "read with an open mind and let the participants' own categories surface. "
                   "Close to grounded theory."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Deductive (top-down)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Codes come from theory or a framework you "
                   "bring to the data. Faster and more comparable, but risks missing the "
                   "unexpected."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Most real projects are <strong>hybrid</strong> "
              "&mdash; a starter framework, held loosely, plus new codes as they emerge."},
         ]},

        {"type": "content", "label": "The Codebook", "title": "Write the rules down",
         "blocks": [
             {"t": "body", "html": "A <strong>codebook</strong> is your living dictionary: each "
              "code, its definition, when to apply it (and when not), and an example. It keeps "
              "you consistent &mdash; and lets a second coder work the same way."},
             {"t": "table",
              "head": ["Code", "Definition", "Example quote"],
              "rows": [
                  ["fear_of_travel", "Worry about safety/distance of journeys", "'I won't send her so far alone'"],
                  ["pension_delay", "Entitlement received late or not at all", "'Six months, still no money'"]]},
         ]},

        {"type": "content", "label": "Software", "title": "CAQDAS: tools that organise, not analyse",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Note", "Cost"],
              "rows": [
                  ["NVivo", "Widely used, feature-rich", "Paid licence"],
                  ["ATLAS.ti", "Strong for visual networks", "Paid licence"],
                  ["Dedoose", "Web-based, good for mixed methods &amp; teams", "Subscription"],
                  ["Taguette", "Free &amp; open-source basic coding", "Free"],
                  ["Spreadsheet + colour", "Perfectly fine for small studies", "Free"]]},
             {"t": "hbox", "color": "red", "html": "<strong>CAQDAS</strong> software organises, "
              "retrieves and counts codes &mdash; it does <em>not</em> do the thinking. The "
              "interpretation is always yours."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Thematic Analysis &amp; Interpretation"},

        {"type": "content", "label": "The Workhorse Method", "title": "From codes to themes",
         "blocks": [
             {"t": "term", "word": "Thematic analysis",
              "def": "A flexible, widely used method for identifying, analysing and reporting "
              "patterns ('themes') across qualitative data &mdash; systematised most influentially "
              "by Virginia Braun &amp; Victoria Clarke (2006)."},
             {"t": "body", "html": "A <strong>theme</strong> is not just a frequent topic; it is "
              "a pattern of meaning that says something important about the research question."},
         ]},

        {"type": "content", "label": "Braun &amp; Clarke", "title": "Six phases of thematic analysis",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Phase", "What you do"],
              "rows": [
                  ["1. Familiarisation", "Read &amp; re-read; immerse in the data"],
                  ["2. Generating codes", "Tag interesting features systematically"],
                  ["3. Searching for themes", "Cluster codes into candidate themes"],
                  ["4. Reviewing themes", "Check themes against data; refine, split, merge"],
                  ["5. Defining themes", "Name each theme and pin down its essence"],
                  ["6. Writing up", "Build the narrative with vivid, evidenced extracts"]]},
             {"t": "hbox", "color": "cyan", "html": "The phases are <strong>recursive</strong>, "
              "not a one-way conveyor &mdash; you move back and forth as understanding deepens."},
         ]},

        {"type": "content", "label": "Codes &rarr; Themes", "title": "How small tags become big ideas",
         "blocks": [
             {"t": "raw", "html":
              '<div style="display:flex;flex-direction:column;align-items:center;gap:10px;'
              'font-family:inherit;color:#cbd5e1;">'
              '<div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center;">'
              '<span style="background:rgba(14,165,233,.15);border:1px solid #0EA5E9;'
              'border-radius:6px;padding:4px 10px;font-size:.7em;">fear_of_travel</span>'
              '<span style="background:rgba(14,165,233,.15);border:1px solid #0EA5E9;'
              'border-radius:6px;padding:4px 10px;font-size:.7em;">no_safe_transport</span>'
              '<span style="background:rgba(14,165,233,.15);border:1px solid #0EA5E9;'
              'border-radius:6px;padding:4px 10px;font-size:.7em;">harassment_on_road</span>'
              '<span style="background:rgba(14,165,233,.15);border:1px solid #0EA5E9;'
              'border-radius:6px;padding:4px 10px;font-size:.7em;">school_too_far</span></div>'
              '<div style="font-size:1.6em;color:#6366F1;">&darr;</div>'
              '<div style="display:flex;gap:8px;justify-content:center;">'
              '<span style="background:rgba(99,102,241,.15);border:1px solid #6366F1;'
              'border-radius:6px;padding:6px 14px;font-size:.85em;font-weight:600;">'
              'Sub-theme: the journey, not the school</span></div>'
              '<div style="font-size:1.6em;color:#10B981;">&darr;</div>'
              '<div style="display:flex;gap:8px;justify-content:center;">'
              '<span style="background:rgba(16,185,129,.15);border:1px solid #10B981;'
              'border-radius:6px;padding:8px 18px;font-size:1em;font-weight:700;">'
              'THEME: Mobility &amp; safety shape girls&rsquo; access</span></div>'
              '</div>'},
             {"t": "hbox", "color": "amber", "html": "Themes are <em>constructed</em> by the "
              "analyst, not lying in wait to be found. Different lenses yield different &mdash; "
              "equally valid &mdash; themes."},
         ]},

        {"type": "content", "label": "Frequency Caution", "title": "A theme is not a tally",
         "blocks": [
             {"t": "chart", "canvas": "codeFreqChart",
              "title": "Code frequency across 15 interviews (illustrative)",
              "source": "Illustrative coding counts",
              "type": "bar",
              "data": {"labels": ["fear_of_travel", "pension_delay", "marriage_pressure",
                                  "cost_of_fees", "no_female_teacher"],
                       "datasets": [{"label": "Interviews mentioning",
                                     "data": [12, 9, 8, 6, 3],
                                     "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Interviews mentioning (of 15)'} } }, indexAxis:'y' }"}},
             {"t": "hbox", "color": "red", "html": "Counts can orient you &mdash; but a rare "
              "code may carry the most important insight. Never reduce qualitative analysis to "
              "'most-mentioned wins'."},
         ]},

        {"type": "content", "label": "Beyond Coding", "title": "Interpretation is more than sorting",
         "blocks": [
             {"t": "body", "html": "Coding organises; <strong>interpretation</strong> explains. "
              "The analytic leap is asking: what is going on here? Why this pattern? What does "
              "it tell us about the question &mdash; and about what stays unsaid?"},
             {"t": "flow", "steps": [
                 "DESCRIBE: what participants said",
                 "INTERPRET: what it might mean",
                 "EXPLAIN: why, and how it connects",
                 "THEORISE: the bigger pattern it reveals"]},
         ]},

        {"type": "content", "label": "Triangulation", "title": "Strength from multiple angles",
         "blocks": [
             {"t": "term", "word": "Triangulation",
              "def": "Using multiple sources, methods, analysts or theories to examine the same "
              "question &mdash; where they converge, confidence grows; where they diverge, you "
              "learn something new."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Data", "label": "Several sources &mdash; interviews, observation, documents", "color": "cyan"},
                 {"num": "Method", "label": "FGD + interview + records on one issue", "color": "green"},
                 {"num": "Investigator", "label": "Multiple analysts compare reads", "color": "indigo"},
                 {"num": "Theory", "label": "More than one lens on the data", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Negative Cases", "title": "Hunt for what contradicts you",
         "blocks": [
             {"t": "body", "html": "A rigorous analyst actively seeks <strong>negative "
              "cases</strong> &mdash; data that does not fit the emerging story &mdash; and "
              "either revises the explanation or accounts for the exception. Confirmation alone "
              "is not analysis."},
             {"t": "hbox", "color": "amber", "html": "If everything fits your first impression, "
              "you probably stopped looking. The disconfirming case is where understanding "
              "matures."},
         ]},

        {"type": "content", "label": "Using Quotes", "title": "Evidence your themes with care",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Use quotes to <strong>illustrate</strong> a theme, not to <em>prove</em> prevalence",
                 "Choose <strong>vivid, representative</strong> extracts &mdash; and revealing exceptions",
                 "Give enough <strong>context</strong> that the reader can judge your reading",
                 "Attribute by code &amp; relevant attributes, never by identity"]},
             {"t": "hbox", "color": "red", "html": "Cherry-picking the one dramatic quote that "
              "suits your argument is a real risk. Show the range, including what cuts against you."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Trustworthiness, Ethics &amp; Reading"},

        {"type": "content", "label": "Rigour, Renamed", "title": "Quality has different names here",
         "blocks": [
             {"t": "body", "html": "Qualitative research cannot be judged by validity, "
              "reliability and generalisability in the statistical sense. "
              "<strong>Lincoln &amp; Guba</strong> (1985) offered four parallel criteria for "
              "<strong>trustworthiness</strong>."},
             {"t": "term", "word": "Trustworthiness",
              "def": "Lincoln &amp; Guba's framework for rigour in qualitative research: "
              "credibility, transferability, dependability and confirmability &mdash; the "
              "qualitative counterparts to validity, generalisability, reliability and "
              "objectivity."},
         ]},

        {"type": "content", "label": "Four Criteria", "title": "Lincoln &amp; Guba's trustworthiness",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Criterion", "Quant parallel", "How you build it"],
              "rows": [
                  ["Credibility", "Internal validity", "Triangulation, member checking, prolonged engagement"],
                  ["Transferability", "External validity", "Thick description so readers judge fit"],
                  ["Dependability", "Reliability", "Audit trail of all decisions"],
                  ["Confirmability", "Objectivity", "Reflexivity; findings traceable to data"]]},
             {"t": "hbox", "color": "cyan", "html": "Learn these four words. They are how "
              "qualitative rigour is named, defended and reviewed."},
         ]},

        {"type": "content", "label": "Building Credibility", "title": "Techniques that earn trust",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Member checking:</strong> take findings back to participants to verify",
                 "<strong>Triangulation:</strong> converge multiple sources and methods",
                 "<strong>Prolonged engagement:</strong> enough time in the field to understand",
                 "<strong>Peer debriefing:</strong> a colleague challenges your interpretation",
                 "<strong>Negative-case analysis:</strong> account for what doesn't fit"]},
         ]},

        {"type": "content", "label": "The Audit Trail", "title": "Show your working",
         "blocks": [
             {"t": "term", "word": "Audit trail",
              "def": "A transparent record of every methodological and analytic decision &mdash; "
              "from sampling to coding to theme-building &mdash; so an outsider could follow how "
              "you reached your conclusions."},
             {"t": "hbox", "color": "green", "html": "Dependability and confirmability both rest "
              "on this trail. Keep memos as you go; reconstructing decisions afterwards is far "
              "harder and far less honest."},
         ]},

        {"type": "content", "label": "Reflexivity Again", "title": "Reflexivity is a rigour tool, not a confession",
         "blocks": [
             {"t": "body", "html": "Stating your positionality and tracking your influence is "
              "central to <strong>confirmability</strong>. It is not navel-gazing &mdash; it is "
              "how qualitative research demonstrates that findings come from the data, not "
              "merely from the researcher."},
             {"t": "hbox", "color": "amber", "html": "Keep a reflexive journal alongside your "
              "field notes. The two together let readers see both the world and your lens on it."},
         ]},

        {"type": "content", "label": "Ethics: The Floor", "title": "Consent, confidentiality, do no harm",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Informed consent:</strong> people understand what, why and how &mdash; and can refuse",
                 "<strong>Confidentiality:</strong> protect identities; codes not names; secure storage",
                 "<strong>Do no harm:</strong> anticipate distress, stigma and risk; have a referral plan",
                 "<strong>Voluntary:</strong> no coercion, no penalty for declining or stopping"]},
             {"t": "hbox", "color": "cyan", "html": "Qualitative work goes deep into people's "
              "lives, so its ethical demands are heavier &mdash; rapport must never become a "
              "tool of extraction."},
         ]},

        {"type": "content", "label": "Context-Specific Ethics", "title": "Ethics in South Asian fieldwork",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Consent may need to be <strong>oral</strong> where literacy is low &mdash; document it carefully",
                 "<strong>Gatekeepers</strong> (sarpanch, husband, employer) can pressure participation &mdash; protect real choice",
                 "Small communities make <strong>anonymity</strong> fragile &mdash; coarsen identifying detail",
                 "India's <strong>DPDP Act, 2023</strong> applies to digital personal data you collect"]},
             {"t": "hbox", "color": "amber", "html": "Reciprocity matters: share findings back, "
              "respect people's time, and never promise benefits you cannot deliver."},
         ]},

        {"type": "content", "label": "Common Pitfalls", "title": "Mistakes to avoid",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Reporting qualitative findings as percentages ('80% said&hellip;')",
                 "Cherry-picking quotes that flatter your argument",
                 "Treating coding as the analysis &mdash; stopping before interpretation",
                 "Ignoring your own influence on the data",
                 "Claiming statistical generalisation from a purposive sample"]},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Match method to question</strong> &mdash; qualitative answers <em>why</em> and <em>how</em>",
                 "<strong>Sample for richness, not representativeness</strong> &mdash; stop at saturation",
                 "<strong>Depth is the point</strong> &mdash; a few cases, understood deeply",
                 "<strong>You are part of the data</strong> &mdash; be reflexive about power and position",
                 "<strong>Rigour is trustworthiness</strong> &mdash; credibility, transferability, dependability, confirmability"]},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Qualitative Research &amp; Evaluation Methods</em> &mdash; Michael Quinn Patton",
                 "<em>Using Thematic Analysis in Psychology</em> &mdash; Braun &amp; Clarke (2006)",
                 "<em>Naturalistic Inquiry</em> &mdash; Lincoln &amp; Guba (1985)",
                 "<em>The Discovery of Grounded Theory</em> &mdash; Glaser &amp; Strauss (1967)",
                 "<em>Whose Reality Counts?</em> &mdash; Robert Chambers (participatory methods)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Research Ethics</strong> and "
              "<strong>Monitoring &amp; Evaluation</strong> 101 courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Qualitative Methods 101 &middot; Complete",
         "headline": "Now go listen<br>&mdash; and listen well.",
         "byline": "Qualitative research is the discipline of taking people's words, worlds and "
                   "meanings seriously &mdash; rigorously, ethically, and with humility about "
                   "your own lens. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
