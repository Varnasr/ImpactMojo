# -*- coding: utf-8 -*-
"""
Observation to Insight 101 — ImpactMojo 101 Series (native deck spec)
Field observation as a rigorous method for development practitioners in South Asia.
Build: python3 scripts/deck-builder/build.py obs2insight
"""

DECK = {
    "slug": "obs2insight",
    "title": "Observation to Insight 101",
    "description": ("Observation to Insight 101 — a free foundational course for development "
                    "practitioners in South Asia. Learn to observe the field rigorously: from "
                    "the say-do gap and Spradley's framework to field notes, structured tools, "
                    "triangulation, bias, ethics and turning patterns into decisions. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Observation<br>to Insight<br>101",
         "sub": "Seeing What Surveys Miss &mdash; Field Observation as a Rigorous Method "
                "for Development Practitioners in South Asia",
         "tags": ["Method-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "Why Observation Matters"},
             {"name": "Types of Observation"},
             {"name": "What to Observe"},
             {"name": "Field Notes"},
             {"name": "Structured Observation Tools"},
             {"name": "Sensemaking: Notes to Patterns"},
             {"name": "Triangulation"},
             {"name": "From Insight to Action"},
             {"name": "Bias &amp; Rigour"},
             {"name": "Ethics of Observation"},
             {"name": "Practice &amp; Tools"},
         ]},

        # ===================== SECTION 01 — Why observation matters =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why Observation Matters"},

        {"type": "content", "label": "The Method", "title": "Observation is data, not decoration",
         "blocks": [
             {"t": "body", "html": "Most development evidence comes from what people <em>tell</em> "
              "us &mdash; surveys, interviews, self-reports. <strong>Observation</strong> is the "
              "disciplined practice of learning by watching what people actually do, in the real "
              "settings where they do it. It is a method with its own rigour, not a coffee break."},
             {"t": "term", "word": "Observation",
              "def": "Systematically watching, listening to and recording behaviour, interactions "
              "and settings in the field &mdash; to understand what happens, not only what people "
              "say happens."},
             {"t": "hbox", "color": "cyan", "html": "You do not need a clipboard to start. You need "
              "to be present, curious and honest about what you actually see."},
         ]},

        {"type": "content", "label": "The Core Gap", "title": "The say&ndash;do gap",
         "blocks": [
             {"t": "body", "html": "People do not always do what they say &mdash; not from "
              "dishonesty, but because memory is faulty, norms shape answers, and habits run below "
              "awareness. The <strong>say&ndash;do gap</strong> is the distance between reported "
              "and observed behaviour."},
             {"t": "flow", "steps": [
                 "SAY: 'We always wash hands before eating'",
                 "DO: observed handwashing at far fewer meals",
                 "GAP: the difference is the finding",
                 "OBSERVE: only watching reveals it"]},
         ]},

        {"type": "content", "label": "See It", "title": "Reported vs observed handwashing",
         "blocks": [
             {"t": "chart", "canvas": "sayDoChart",
              "title": "Self-reported vs observed handwashing before meals",
              "source": "ILLUSTRATIVE &mdash; figures invented to show the pattern, not real data",
              "type": "bar",
              "data": {"labels": ["Village A", "Village B", "Village C", "Village D"],
                       "datasets": [
                           {"label": "Self-reported (%)", "data": [88, 92, 80, 85],
                            "backgroundColor": "#6366F1"},
                           {"label": "Observed (%)", "data": [41, 55, 33, 47],
                            "backgroundColor": "#10B981"}]},
              "options": {"__js__": "{ scales:{ y:{ min:0, max:100, title:{display:true,text:'%'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "ILLUSTRATIVE numbers. The point is the shape: "
              "reported practice sits well above observed practice. Programmes built on self-report "
              "alone can chase a behaviour that is not there."},
         ]},

        {"type": "content", "label": "What Surveys Miss", "title": "The questionnaire never asked",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>The unspoken:</strong> a clinic queue where men are served before women",
                 "<strong>The unmeasured:</strong> the broken hand-pump nobody listed as a problem",
                 "<strong>The contextual:</strong> who sits where, who speaks, who stays silent",
                 "<strong>The routine:</strong> habits so normal that respondents forget to mention them"]},
             {"t": "hbox", "color": "cyan", "html": "A survey can only return answers to questions "
              "you already knew to ask. Observation surfaces the questions you did not."},
         ]},

        {"type": "content", "label": "Methods Compared", "title": "Where observation fits among methods",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Method", "Answers", "Blind spot"],
              "rows": [
                  ["Survey", "How many / how widespread", "Only what you knew to ask"],
                  ["Interview", "What people say &amp; why they say it", "Say&ndash;do gap; recall error"],
                  ["Document review", "What is officially recorded", "What records omit or inflate"],
                  ["Observation", "What people actually do, in context", "Hard to scale; observer effect"]]},
             {"t": "hbox", "color": "cyan", "html": "Observation is not better than the others "
              "&mdash; it sees what they cannot. That is why it earns a place in any serious study."},
         ]},

        {"type": "content", "label": "Being Present", "title": "The value of simply being there",
         "blocks": [
             {"t": "body", "html": "Time in the field builds <strong>tacit understanding</strong> "
              "&mdash; the feel of a place, its rhythms, its tensions. Much of what matters in "
              "development is relational and spatial, and only becomes visible to someone who lingers."},
             {"t": "quote",
              "text": "You can observe a lot just by watching.",
              "attr": "&mdash; attributed to Yogi Berra"},
         ]},

        {"type": "content", "label": "Where It Fits", "title": "Observation across the project cycle",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Stage", "What observation adds"],
              "rows": [
                  ["Needs assessment", "Surfaces problems people don't name in surveys"],
                  ["Design", "Grounds the intervention in real routines and constraints"],
                  ["Implementation", "Shows how a programme is actually used, not just delivered"],
                  ["Monitoring", "Catches gaps between protocol and practice early"],
                  ["Evaluation", "Explains <em>why</em> outcomes happened, not only whether"]]},
         ]},

        {"type": "content", "label": "A Caution", "title": "Observation is powerful, not infallible",
         "blocks": [
             {"t": "body", "html": "Watching is interpretation. Two observers can see the same scene "
              "and record different things. The rest of this course is about making observation "
              "<strong>systematic</strong>, <strong>transparent</strong> and <strong>ethical</strong> "
              "&mdash; so it earns the word 'evidence'."},
             {"t": "hbox", "color": "amber", "html": "Good observation is not 'just looking'. It is "
              "looking with a question, a method, and a record."},
         ]},

        # ===================== SECTION 02 — Types of observation =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Types of Observation"},

        {"type": "content", "label": "Three Dimensions", "title": "Three choices define your observation",
         "blocks": [
             {"t": "body", "html": "Every observation sits on three axes. Decide each one "
              "deliberately before you enter the field &mdash; they shape what you can see and "
              "what you owe the people you watch."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Role", "label": "Participant &harr; non-participant", "color": "cyan"},
                 {"num": "Structure", "label": "Structured &harr; unstructured", "color": "indigo"},
                 {"num": "Disclosure", "label": "Overt &harr; covert", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Role", "title": "The participant&harr;non-participant spectrum",
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 1000 200" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;height:auto;font-family:inherit">'
                 '<line x1="80" y1="110" x2="920" y2="110" stroke="#1C1917" stroke-width="3"/>'
                 '<polygon points="920,110 905,102 905,118" fill="#1C1917"/>'
                 '<polygon points="80,110 95,102 95,118" fill="#1C1917"/>'
                 '<circle cx="160" cy="110" r="9" fill="#10B981"/>'
                 '<circle cx="400" cy="110" r="9" fill="#0EA5E9"/>'
                 '<circle cx="640" cy="110" r="9" fill="#6366F1"/>'
                 '<circle cx="880" cy="110" r="9" fill="#F59E0B"/>'
                 '<text x="160" y="150" text-anchor="middle" fill="#1C1917" font-size="20" font-weight="700">Complete</text>'
                 '<text x="160" y="174" text-anchor="middle" fill="#1C1917" font-size="20" font-weight="700">participant</text>'
                 '<text x="400" y="150" text-anchor="middle" fill="#1C1917" font-size="20">Participant-</text>'
                 '<text x="400" y="174" text-anchor="middle" fill="#1C1917" font-size="20">as-observer</text>'
                 '<text x="640" y="150" text-anchor="middle" fill="#1C1917" font-size="20">Observer-</text>'
                 '<text x="640" y="174" text-anchor="middle" fill="#1C1917" font-size="20">as-participant</text>'
                 '<text x="880" y="150" text-anchor="middle" fill="#1C1917" font-size="20" font-weight="700">Complete</text>'
                 '<text x="880" y="174" text-anchor="middle" fill="#1C1917" font-size="20" font-weight="700">observer</text>'
                 '<text x="160" y="70" text-anchor="middle" fill="#10B981" font-size="18" font-weight="700">deep immersion</text>'
                 '<text x="880" y="70" text-anchor="middle" fill="#F59E0B" font-size="18" font-weight="700">pure watching</text>'
                 '</svg>')},
             {"t": "hbox", "color": "cyan", "html": "Gold &amp; others mapped this classic "
              "continuum. More participation buys you depth and trust; less buys you distance and "
              "a wider view. You will often move along it within one study."},
         ]},

        {"type": "content", "label": "Participant", "title": "Participant observation",
         "blocks": [
             {"t": "body", "html": "The observer <strong>takes part</strong> in the life of the "
              "setting &mdash; joining a self-help group meeting, working a shift, sharing a meal "
              "&mdash; while observing. The anthropologist's classic stance."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Gains", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Trust and access insiders never grant outsiders",
                      "Felt, embodied understanding of routines",
                      "The unguarded, backstage moments"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Costs", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Time-intensive &mdash; weeks or months",
                      "Risk of 'going native' and losing distance",
                      "Your presence changes the scene"]}]}]},
         ]},

        {"type": "content", "label": "Non-Participant", "title": "Non-participant observation",
         "blocks": [
             {"t": "body", "html": "The observer <strong>stays apart</strong> &mdash; watching a "
              "school classroom from the back, timing a clinic queue, mapping a market &mdash; "
              "without joining in. More detached, more easily structured."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Gains", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Cleaner, more comparable records",
                      "Less time per site; cover more sites",
                      "Easier to standardise across observers"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Costs", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Surface view &mdash; misses meaning",
                      "Less trust, less backstage access",
                      "A watcher in the corner still alters behaviour"]}]}]},
         ]},

        {"type": "content", "label": "Structure", "title": "Structured vs unstructured",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Structured", "Unstructured"],
              "rows": [
                  ["Tool", "Checklist, coding sheet, timer", "Open field notebook"],
                  ["Question", "Pre-defined &mdash; you know what to count", "Open &mdash; you discover what matters"],
                  ["Output", "Counts, ratings, frequencies", "Rich descriptive narrative"],
                  ["Best for", "Comparison, monitoring, scale", "Exploration, meaning, the unexpected"],
                  ["Risk", "Misses what's not on the sheet", "Hard to compare across sites"]]},
             {"t": "hbox", "color": "cyan", "html": "Many studies start unstructured (to learn "
              "what to look at) and then add structure (to count it reliably)."},
         ]},

        {"type": "content", "label": "Disclosure", "title": "Overt vs covert",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Overt", "blocks": [
                  {"t": "body", "cls": "sm", "html": "People know they are being observed and have "
                   "consented. The ethical default. Costs you some of the natural behaviour you "
                   "came to see (the observer effect)."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Covert", "blocks": [
                  {"t": "body", "cls": "sm", "html": "People do not know they are observed. Yields "
                   "unguarded behaviour &mdash; but denies consent and carries serious ethical and "
                   "legal risk. Rarely justifiable in development work."}]}]},
             {"t": "hbox", "color": "amber", "html": "Default to overt. Covert observation needs an "
              "exceptional justification and ethics-committee approval &mdash; we return to this "
              "in Section 10."},
         ]},

        {"type": "content", "label": "Choosing", "title": "Match the type to the question",
         "blocks": [
             {"t": "bullets", "items": [
                 "Want <strong>meaning and process</strong>? Lean participant and unstructured.",
                 "Want <strong>comparable counts</strong> across sites? Lean non-participant and structured.",
                 "Watching a <strong>private or sensitive</strong> setting? Overt, with consent, always.",
                 "Most real studies <strong>blend</strong> these, and shift as understanding grows."]},
             {"t": "hbox", "color": "cyan", "html": "There is no single 'best' type &mdash; only "
              "the type that fits your question, your ethics and your time."},
         ]},

        # ===================== SECTION 03 — What to observe =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "What to Observe"},

        {"type": "content", "label": "The Problem", "title": "A field site overwhelms the eye",
         "blocks": [
             {"t": "body", "html": "Stand in a busy market, an anganwadi, a gram sabha &mdash; a "
              "thousand things happen at once. Without a framework you record randomly, miss "
              "patterns, and tire fast. You need a lens that tells you <em>what to look at</em>."},
             {"t": "hbox", "color": "amber", "html": "The cure for overwhelm is not to watch harder. "
              "It is to watch with a structure."},
         ]},

        {"type": "content", "label": "Spradley", "title": "Spradley's nine dimensions of a social situation",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "James Spradley (<em>Participant Observation</em>, 1980) gave "
              "fieldworkers a checklist of <strong>nine dimensions</strong> present in any social "
              "situation. Run through them and you will rarely miss something important."},
             {"t": "table",
              "head": ["Dimension", "Ask&hellip;"],
              "rows": [
                  ["Space", "The physical place &mdash; layout, boundaries"],
                  ["Actors", "The people present &mdash; who, how many"],
                  ["Activities", "The set of related acts people do"],
                  ["Objects", "The physical things present"],
                  ["Acts", "Single actions people take"],
                  ["Events", "The activities bundled into occasions"],
                  ["Time", "Sequencing &mdash; what happens over time"],
                  ["Goals", "What people are trying to accomplish"],
                  ["Feelings", "Emotions felt and expressed"]]},
         ]},

        {"type": "content", "label": "Grand Tour", "title": "Spradley's 'grand-tour' observation",
         "blocks": [
             {"t": "body", "html": "Spradley advised starting with a <strong>grand-tour</strong>: "
              "a broad sweep that takes in the whole setting before zooming in. Walk the space, map "
              "it, get the lay of the land &mdash; then narrow to a <strong>mini-tour</strong> of "
              "one corner in detail."},
             {"t": "flow", "steps": [
                 "GRAND-TOUR: scan the whole setting",
                 "MAP: space, actors, objects",
                 "MINI-TOUR: zoom in on one activity",
                 "FOCUS: follow the question that emerges"]},
         ]},

        {"type": "content", "label": "Apply It", "title": "The nine dimensions at an anganwadi",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Dimension", "At an anganwadi centre"],
              "rows": [
                  ["Space", "One room; cooking corner; mat for children"],
                  ["Actors", "Worker, helper, 18 children, two mothers"],
                  ["Activities", "Meal service, weighing, pre-school play"],
                  ["Objects", "Growth chart, weighing scale, ration sacks"],
                  ["Acts", "A child refuses food; worker records weight"],
                  ["Events", "The hot-cooked-meal session"],
                  ["Time", "Children arrive late; meal slips past schedule"],
                  ["Goals", "Nutrition, school-readiness, attendance"],
                  ["Feelings", "Restlessness; a mother's worry over weight"]]},
         ]},

        {"type": "content", "label": "Mapping", "title": "Draw the space",
         "blocks": [
             {"t": "body", "html": "A simple sketch map &mdash; doorways, seating, the queue, where "
              "the worker stands &mdash; captures spatial patterns words cannot. Who sits near the "
              "front? Who is pushed to the margins? Space encodes power."},
             {"t": "hbox", "color": "cyan", "html": "Keep a sketch map in every field notebook. "
              "Mark movement with arrows; mark where people cluster and where they avoid."},
         ]},

        {"type": "content", "label": "Focus", "title": "From broad to focused observation",
         "blocks": [
             {"t": "body", "html": "Observation funnels over time: from <strong>descriptive</strong> "
              "(take in everything) to <strong>focused</strong> (track the dimensions that matter) "
              "to <strong>selective</strong> (count specific, well-defined behaviours)."},
             {"t": "flow", "steps": [
                 "DESCRIPTIVE: observe broadly, note all nine dimensions",
                 "FOCUSED: narrow to the emerging question",
                 "SELECTIVE: record specific, defined behaviours"]},
         ]},

        {"type": "content", "label": "Your Lens", "title": "What you look for shapes what you find",
         "blocks": [
             {"t": "body", "html": "A framework focuses attention &mdash; but a fixed framework can "
              "also blind you to what it leaves out. Hold your lens firmly enough to be systematic, "
              "loosely enough to be surprised."},
             {"t": "hbox", "color": "amber", "html": "Leave a column in your notes for "
              "'<em>things that don't fit my framework</em>'. That column is often where the "
              "insight hides."},
         ]},

        # ===================== SECTION 04 — Field notes =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Field Notes"},

        {"type": "content", "label": "The Record", "title": "If it isn't written down, it didn't happen",
         "blocks": [
             {"t": "body", "html": "Observation produces nothing without a <strong>record</strong>. "
              "Memory decays fast and reshapes itself to fit our expectations. Field notes are the "
              "raw data of observation &mdash; the single most important craft in this course."},
             {"t": "quote",
              "text": "Writing fieldnotes is not a record of what happened so much as a way of "
              "thinking about what happened.",
              "attr": "&mdash; Emerson, Fretz &amp; Shaw, Writing Ethnographic Fieldnotes"},
         ]},

        {"type": "content", "label": "Two Moments", "title": "Jotted notes, then expanded notes",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Jotted notes (in the field)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Quick scratch notes, key words, a sketch, an "
                   "exact quote. Brief and unobtrusive &mdash; just enough to trigger memory later."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Expanded notes (after)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Written up the same day, while memory is fresh: "
                   "the full scene, in order, with detail. The jottings are the seed; the expanded "
                   "notes are the crop."}]}]},
             {"t": "hbox", "color": "red", "html": "The golden rule of fieldnotes: <strong>write "
              "up the same day.</strong> One night's sleep erases more than you think."},
         ]},

        {"type": "content", "label": "Two Layers", "title": "Descriptive vs reflective notes",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Descriptive", "Reflective / analytic"],
              "rows": [
                  ["Content", "What you saw and heard", "What you think it means"],
                  ["Voice", "Concrete, low-inference", "Interpretive, questioning"],
                  ["Example", "'Worker weighed 6 children, recorded 4'", "'Why were 2 not recorded?'"],
                  ["Keep them", "Separate &mdash; in distinct columns or marks", "Separate &mdash; so you can tell fact from hunch"]]},
             {"t": "hbox", "color": "cyan", "html": "Use a clear marker (e.g. [OC] for 'observer "
              "comment') so analytic asides never get mistaken for observed fact."},
         ]},

        {"type": "content", "label": "Low Inference", "title": "Describe before you interpret",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "High inference", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'The mother was hostile and uncooperative.' "
                   "&mdash; a judgement, already an interpretation, hard to verify."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Low inference", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'The mother folded her arms, looked away, and "
                   "answered in one word.' &mdash; observable detail anyone could have recorded."}]}]},
             {"t": "hbox", "color": "amber", "html": "Record the behaviour, not your label for it. "
              "Labels can be revised later; lost observations cannot be recovered."},
         ]},

        {"type": "content", "label": "Thick Description", "title": "Thick description",
         "blocks": [
             {"t": "term", "word": "Thick description",
              "def": "Clifford Geertz's term: an account that records not just an action but its "
              "context and meaning &mdash; the difference between a 'twitch' and a 'wink' lies in "
              "what it means to the people involved."},
             {"t": "body", "html": "Thin: 'a man nodded.' Thick: 'when the upper-caste landlord "
              "entered, the labourer stopped speaking mid-sentence and nodded &mdash; a gesture of "
              "deference everyone present understood.' Thick description carries the meaning."},
         ]},

        {"type": "content", "label": "Quotes", "title": "Capture verbatim speech",
         "blocks": [
             {"t": "body", "html": "When someone says something striking, write it down "
              "<strong>word for word</strong>, in their language, in quotation marks. A real "
              "quote is worth a paragraph of paraphrase &mdash; and it is honest evidence."},
             {"t": "hbox", "color": "cyan", "html": "Mark verbatim quotes clearly. Mark your "
              "paraphrases too. Later you must know which words were theirs and which were yours."},
         ]},

        {"type": "content", "label": "Craft", "title": "Practical fieldnote discipline",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Head every note: <strong>date, time, place, who was present</strong>",
                 "Write in the past tense, in order, scene by scene",
                 "Note what did <em>not</em> happen, and who was absent",
                 "Distinguish quotes, observations and your own thoughts",
                 "Number your pages; never tear any out"]},
         ]},

        {"type": "content", "label": "The Notebook", "title": "Your field notebook is the instrument",
         "blocks": [
             {"t": "body", "html": "In observation, there is no machine between you and the data "
              "&mdash; <strong>you</strong> are the instrument, and your notebook is its output. "
              "Treat it with the seriousness a surveyor gives a calibrated gauge."},
             {"t": "hbox", "color": "amber", "html": "Protect it. Back it up. A lost notebook is a "
              "lost dataset &mdash; and often weeks of irreplaceable fieldwork."},
         ]},

        # ===================== SECTION 05 — Structured observation tools =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Structured Observation Tools"},

        {"type": "content", "label": "Why Structure", "title": "When you need to count, not narrate",
         "blocks": [
             {"t": "body", "html": "Once you know <em>what</em> matters, structured tools let you "
              "record it consistently &mdash; across observers, sites and time &mdash; so you can "
              "count, compare and track. Structure trades richness for reliability."},
             {"t": "hbox", "color": "cyan", "html": "Structured tools answer 'how often / how many / "
              "how long'. Use them once unstructured observation has told you what to count."},
         ]},

        {"type": "content", "label": "Checklists", "title": "Observation checklists",
         "blocks": [
             {"t": "body", "html": "A <strong>checklist</strong> records whether defined things are "
              "present or absent: Is the growth chart displayed? Is the toilet functional? Is the "
              "teacher present? Simple, fast, and brutally clear."},
             {"t": "hbox", "color": "green", "html": "Make each item observable and unambiguous. "
              "'Toilet functional' must be defined &mdash; water present, door closes, not used "
              "for storage &mdash; so any observer marks it the same way."},
         ]},

        {"type": "content", "label": "Rating Scales", "title": "Rating scales",
         "blocks": [
             {"t": "body", "html": "A <strong>rating scale</strong> records degree, not just "
              "presence: classroom engagement on a 1&ndash;5 scale, cleanliness from poor to "
              "excellent. Powerful, but only if every point is anchored with a description."},
             {"t": "hbox", "color": "amber", "html": "Unanchored scales invite disagreement. Define "
              "what a '3' looks like versus a '4', with concrete examples, or two observers will "
              "never agree."},
         ]},

        {"type": "content", "label": "Sampling Time", "title": "Time sampling vs event sampling",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Time sampling", "Event sampling"],
              "rows": [
                  ["Rule", "Observe at set intervals (every 5 min)", "Record every time an event occurs"],
                  ["Captures", "What is typical / how prevalent", "How often a specific event happens"],
                  ["Good for", "Ongoing states (on-task, idle)", "Discrete events (a conflict, a sale)"],
                  ["Misses", "Events between snapshots", "Nothing of that event &mdash; but ignores the rest"]]},
             {"t": "hbox", "color": "cyan", "html": "Time sampling = repeated snapshots. Event "
              "sampling = a trigger you watch for. Pick by whether you care about states or events."},
         ]},

        {"type": "content", "label": "Tally", "title": "A time-sampling tally in a classroom",
         "blocks": [
             {"t": "chart", "canvas": "tallyChart",
              "title": "Children on-task at 5-minute snapshots (one 40-min lesson)",
              "source": "ILLUSTRATIVE &mdash; invented tally to show the method",
              "type": "bar",
              "data": {"labels": ["0", "5", "10", "15", "20", "25", "30", "35"],
                       "datasets": [{"label": "Children on-task (of 30)",
                                     "data": [27, 25, 24, 20, 18, 14, 19, 12],
                                     "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:30,title:{display:true,text:'on-task (of 30)'}}, x:{title:{display:true,text:'minute of lesson'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "ILLUSTRATIVE. Snapshots every 5 minutes turn "
              "a vague impression ('attention drifted') into a countable, comparable pattern."},
         ]},

        {"type": "content", "label": "Guides", "title": "Observation guides",
         "blocks": [
             {"t": "body", "html": "Between a free notebook and a rigid checklist sits the "
              "<strong>observation guide</strong>: a structured prompt list of things to attend to, "
              "with room for open description. It steers without straitjacketing."},
             {"t": "hbox", "color": "green", "html": "A good guide is one page: the dimensions to "
              "cover, the key questions, and space to write what you did not expect."},
         ]},

        {"type": "content", "label": "Definitions", "title": "Operationalise every behaviour you count",
         "blocks": [
             {"t": "body", "html": "A structured tool is only as good as its definitions. Before "
              "you can tally 'on-task' or 'aggressive interaction', you must write down exactly "
              "what counts &mdash; an observable rule any observer can apply the same way."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Too vague", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'Child engaged' &mdash; engaged how? Two "
                   "observers will count completely different things."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Operationalised", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'Eyes on the teacher or task material, not "
                   "talking off-topic' &mdash; observable, repeatable, countable."}]}]},
         ]},

        {"type": "content", "label": "Agreement", "title": "Inter-observer agreement",
         "blocks": [
             {"t": "term", "word": "Inter-observer agreement",
              "def": "The extent to which two or more observers, watching the same thing with the "
              "same tool, record the same result. A core test of whether a structured observation "
              "is reliable or just one person's impression."},
             {"t": "body", "html": "Have two observers code the same session independently, then "
              "compare. Wide disagreement means your definitions are loose, not that one observer "
              "is 'wrong'. Tighten the tool and re-test."},
         ]},

        {"type": "content", "label": "Pilot", "title": "Pilot every instrument",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Test the checklist or scale in the real setting first",
                 "Watch where two observers diverge &mdash; fix those items",
                 "Check it can be completed in the time available",
                 "Refine definitions until the tool is boringly unambiguous"]},
             {"t": "hbox", "color": "amber", "html": "An untested observation tool is a guess. The "
              "pilot is where you turn it into an instrument."},
         ]},

        # ===================== SECTION 06 — Sensemaking =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Sensemaking: Notes to Patterns"},

        {"type": "content", "label": "The Pile", "title": "From a pile of notes to a pattern",
         "blocks": [
             {"t": "body", "html": "After fieldwork you hold pages of notes, tallies and quotes. "
              "<strong>Sensemaking</strong> is the disciplined work of turning that pile into "
              "patterns, and patterns into insight. It is analysis, and it deserves as much rigour "
              "as the observing did."},
             {"t": "flow", "steps": [
                 "NOTES: raw descriptions",
                 "CODES: label recurring things",
                 "THEMES: group codes into patterns",
                 "INSIGHT: what the patterns mean"]},
         ]},

        {"type": "content", "label": "Memoing", "title": "Memo as you go",
         "blocks": [
             {"t": "term", "word": "Memo",
              "def": "A short, dated note in which the observer thinks on paper &mdash; a hunch, a "
              "question, an emerging idea, a link between observations. Memos turn fleeting thoughts "
              "into a traceable trail of analysis."},
             {"t": "hbox", "color": "cyan", "html": "Do not wait until the end to think. Write memos "
              "throughout fieldwork &mdash; the best ideas arrive in the field, then vanish."},
         ]},

        {"type": "content", "label": "Coding", "title": "Coding your observations",
         "blocks": [
             {"t": "body", "html": "<strong>Coding</strong> means tagging stretches of notes with "
              "short labels &mdash; 'waiting', 'gatekeeping', 'workaround', 'deference' &mdash; so "
              "you can gather everything about each idea across all your notes."},
             {"t": "flow", "steps": [
                 "READ: go through the notes closely",
                 "OPEN-CODE: name what you see, freely",
                 "GROUP: cluster similar codes",
                 "RECODE: refine into a stable set"]},
         ]},

        {"type": "content", "label": "Themes", "title": "Looking for recurring themes",
         "blocks": [
             {"t": "body", "html": "A <strong>theme</strong> is a pattern that recurs across "
              "observations and carries meaning for your question. Themes are built, not found: you "
              "assemble them from repeated codes, then test whether they really hold."},
             {"t": "hbox", "color": "green", "html": "Ask of any candidate theme: How often does it "
              "appear? Across how many sites and observers? Is there a clear example I can point to?"},
         ]},

        {"type": "content", "label": "Anomalies", "title": "Hunt the case that doesn't fit",
         "blocks": [
             {"t": "body", "html": "The instinct is to smooth over the observation that breaks your "
              "pattern. Resist it. The <strong>anomaly</strong> &mdash; the negative case &mdash; "
              "is where understanding deepens: it shows the limits of your pattern, or reveals a "
              "better one."},
             {"t": "hbox", "color": "amber", "html": "Actively search for disconfirming cases. A "
              "pattern that survives an honest hunt for exceptions is one you can trust."},
         ]},

        {"type": "content", "label": "Frequency", "title": "Count where you can, carefully",
         "blocks": [
             {"t": "body", "html": "Qualitative does not mean anti-number. Noting that a behaviour "
              "appeared in 9 of 12 observed sessions is honest and useful &mdash; far better than "
              "the vague word 'often', which lets readers imagine any figure they like."},
             {"t": "hbox", "color": "cyan", "html": "Prefer '<strong>in most sessions (9 of 12)</strong>' "
              "to '<em>frequently</em>'. Modest counts make qualitative claims auditable."},
         ]},

        {"type": "content", "label": "Saturation", "title": "Know when you've seen enough",
         "blocks": [
             {"t": "term", "word": "Saturation",
              "def": "The point at which further observation stops yielding new themes &mdash; you "
              "keep seeing what you have already seen. A practical signal that you have observed "
              "enough on a given question."},
             {"t": "hbox", "color": "green", "html": "Saturation is a judgement, not a finish line. "
              "Reaching it on one theme does not mean you have it on another."},
         ]},

        {"type": "content", "label": "Audit Trail", "title": "Show your working",
         "blocks": [
             {"t": "body", "html": "Rigour in qualitative analysis is about <strong>transparency</strong>. "
              "Keep an audit trail: your codes, the rule for each, example quotes, and how a theme "
              "was built. Another analyst should be able to follow your path from notes to claim."},
             {"t": "hbox", "color": "amber", "html": "If you cannot show how you got from your "
              "notebook to your conclusion, neither can your reader trust it."},
         ]},

        # ===================== SECTION 07 — Triangulation =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Triangulation"},

        {"type": "content", "label": "The Idea", "title": "No single method sees everything",
         "blocks": [
             {"t": "term", "word": "Triangulation",
              "def": "Using more than one method, source or observer to study the same question, so "
              "that the strengths of each compensate for the blind spots of the others &mdash; "
              "borrowed from surveying, where two bearings fix a point."},
             {"t": "body", "html": "Observation tells you what people <em>do</em>; interviews tell "
              "you what it <em>means</em> to them; documents and data tell you the <em>scale</em>. "
              "Together they triangulate the truth."},
         ]},

        {"type": "content", "label": "The Triangle", "title": "Three lines of sight on one question",
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;height:auto;font-family:inherit">'
                 '<polygon points="450,60 130,360 770,360" fill="none" stroke="#1C1917" stroke-width="2.5"/>'
                 '<circle cx="450" cy="60" r="14" fill="#0EA5E9"/>'
                 '<circle cx="130" cy="360" r="14" fill="#10B981"/>'
                 '<circle cx="770" cy="360" r="14" fill="#F59E0B"/>'
                 '<circle cx="450" cy="262" r="9" fill="#6366F1"/>'
                 '<line x1="450" y1="60" x2="450" y2="262" stroke="#6366F1" stroke-width="1.5" stroke-dasharray="5,5"/>'
                 '<line x1="130" y1="360" x2="450" y2="262" stroke="#6366F1" stroke-width="1.5" stroke-dasharray="5,5"/>'
                 '<line x1="770" y1="360" x2="450" y2="262" stroke="#6366F1" stroke-width="1.5" stroke-dasharray="5,5"/>'
                 '<text x="450" y="38" text-anchor="middle" fill="#0EA5E9" font-size="22" font-weight="700">OBSERVATION</text>'
                 '<text x="450" y="20" text-anchor="middle" fill="#1C1917" font-size="16">what people do</text>'
                 '<text x="130" y="392" text-anchor="middle" fill="#10B981" font-size="22" font-weight="700">INTERVIEWS</text>'
                 '<text x="130" y="412" text-anchor="middle" fill="#1C1917" font-size="16">what it means</text>'
                 '<text x="770" y="392" text-anchor="middle" fill="#F59E0B" font-size="22" font-weight="700">DOCUMENTS &amp; DATA</text>'
                 '<text x="770" y="412" text-anchor="middle" fill="#1C1917" font-size="16">the scale</text>'
                 '<text x="450" y="300" text-anchor="middle" fill="#6366F1" font-size="18" font-weight="700">the question</text>'
                 '</svg>')},
             {"t": "hbox", "color": "cyan", "html": "Denzin distinguished several kinds: of method, "
              "of source, of observer, and of theory. The principle is the same &mdash; one bearing "
              "is a guess; three fix a position."},
         ]},

        {"type": "content", "label": "With Interviews", "title": "Observation + interviews",
         "blocks": [
             {"t": "body", "html": "Observe first, then ask. Seeing a practice lets you ask far "
              "sharper interview questions &mdash; about the very thing you watched &mdash; and "
              "lets you probe the gap between what you saw and what people say."},
             {"t": "hbox", "color": "green", "html": "'I noticed the queue formed differently "
              "today &mdash; can you help me understand why?' Observation earns you questions no "
              "outsider could otherwise ask."},
         ]},

        {"type": "content", "label": "With Documents", "title": "Observation + documents and records",
         "blocks": [
             {"t": "body", "html": "Registers, muster rolls, attendance sheets and meeting minutes "
              "are claims about reality. Observation tests them: does the attendance register match "
              "the children you counted in the room?"},
             {"t": "hbox", "color": "amber", "html": "Where the record and the room disagree, you "
              "have not found an error &mdash; you have found a finding worth understanding."},
         ]},

        {"type": "content", "label": "With Numbers", "title": "Observation + quantitative data",
         "blocks": [
             {"t": "body", "html": "Survey and administrative data tell you <em>how widespread</em>; "
              "observation tells you <em>how and why</em>. A dashboard shows immunisation coverage "
              "dipped; observation of the session shows the cold-chain box was empty."},
             {"t": "hbox", "color": "cyan", "html": "Numbers raise the question; observation often "
              "answers it. Pair a surprising statistic with a visit to where it is produced."},
         ]},

        {"type": "content", "label": "Convergence", "title": "When sources agree: convergence",
         "blocks": [
             {"t": "body", "html": "When observation, interviews and data all point the same way, "
              "your confidence rises sharply. Independent methods reaching the same conclusion are "
              "unlikely to be wrong in the same direction by chance."},
             {"t": "hbox", "color": "green", "html": "Convergence is the strongest evidence a "
              "field study can offer: many bearings, one position."},
         ]},

        {"type": "content", "label": "Divergence", "title": "When sources disagree: divergence",
         "blocks": [
             {"t": "body", "html": "Disagreement is not failure &mdash; it is information. If the "
              "register says 30 and you counted 18, if women report ease of access but you observe "
              "them turned away, the <strong>divergence itself is the finding</strong>."},
             {"t": "hbox", "color": "amber", "html": "Do not paper over a conflict between sources. "
              "Investigate it: one source may be wrong, or each may be true of a different reality."},
         ]},

        {"type": "content", "label": "Observers", "title": "Triangulating across observers",
         "blocks": [
             {"t": "body", "html": "Triangulation is not only across methods. Two observers watching "
              "the <em>same</em> setting &mdash; ideally differing in gender, language or background "
              "&mdash; will notice different things. Comparing their notes is itself a check on bias "
              "and a way to see more."},
             {"t": "hbox", "color": "green", "html": "Where two observers agree, confidence rises. "
              "Where they differ, you learn how positionality shaped each view &mdash; both useful."},
         ]},

        {"type": "content", "label": "Discipline", "title": "Triangulation is a habit, not a checkbox",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Plan from the start to look at each question more than one way",
                 "Record which method produced which claim",
                 "Treat agreement as confirmation, disagreement as a lead",
                 "Never let one striking observation stand entirely alone"]},
         ]},

        # ===================== SECTION 08 — From insight to action =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "From Insight to Action"},

        {"type": "content", "label": "So What", "title": "The 'so what?' test",
         "blocks": [
             {"t": "body", "html": "A pattern is not yet an insight, and an insight is not yet a "
              "decision. After every finding, ask the practitioner's question: "
              "<strong>so what?</strong> What should change because we now know this?"},
             {"t": "flow", "steps": [
                 "OBSERVATION: what we saw",
                 "PATTERN: what recurs",
                 "INSIGHT: what it means",
                 "ACTION: what we'll do differently"]},
         ]},

        {"type": "content", "label": "Insight", "title": "What makes a finding an insight?",
         "blocks": [
             {"t": "body", "html": "An <strong>insight</strong> is a finding that is "
              "<em>actionable</em> and <em>non-obvious</em> &mdash; it changes how you understand "
              "the problem, and it points somewhere. 'Attendance is low' is a fact; 'attendance "
              "collapses on ration-delivery days because mothers must queue elsewhere' is an insight."},
             {"t": "hbox", "color": "cyan", "html": "Test: could someone act differently because of "
              "this? If not, keep digging &mdash; you have a fact, not yet an insight."},
         ]},

        {"type": "content", "label": "The Funnel", "title": "The observation-to-insight funnel",
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 820 400" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;height:auto;font-family:inherit">'
                 '<polygon points="60,40 760,40 660,110 160,110" fill="#0EA5E9" opacity="0.9"/>'
                 '<polygon points="160,120 660,120 580,190 240,190" fill="#6366F1" opacity="0.9"/>'
                 '<polygon points="240,200 580,200 510,270 310,270" fill="#10B981" opacity="0.9"/>'
                 '<polygon points="310,280 510,280 450,350 370,350" fill="#F59E0B" opacity="0.95"/>'
                 '<text x="410" y="83" text-anchor="middle" fill="#fff" font-size="22" font-weight="700">RAW OBSERVATIONS &mdash; everything seen</text>'
                 '<text x="410" y="163" text-anchor="middle" fill="#fff" font-size="22" font-weight="700">CODED PATTERNS &mdash; what recurs</text>'
                 '<text x="410" y="243" text-anchor="middle" fill="#fff" font-size="22" font-weight="700">INSIGHTS &mdash; what it means</text>'
                 '<text x="410" y="322" text-anchor="middle" fill="#1C1917" font-size="22" font-weight="700">DECISIONS</text>'
                 '</svg>')},
             {"t": "hbox", "color": "amber", "html": "The funnel narrows for a reason: many "
              "observations yield few decisions. The discipline is choosing which patterns are "
              "worth acting on."},
         ]},

        {"type": "content", "label": "Recommendations", "title": "Turn patterns into recommendations",
         "blocks": [
             {"t": "body", "html": "A useful recommendation is <strong>specific, owned and "
              "feasible</strong>: who should do what, by when. 'Improve services' helps no one; "
              "'shift the weighing session to avoid the ration-queue clash, with the supervisor "
              "confirming the new time' can be acted on tomorrow."},
             {"t": "hbox", "color": "green", "html": "Tie every recommendation back to the "
              "observation that motivates it. Evidence-to-action should be traceable in one line."},
         ]},

        {"type": "content", "label": "Feedback", "title": "Close the loop with the field",
         "blocks": [
             {"t": "body", "html": "Insight that never returns to the people who generated it is "
              "extraction. Share findings back with frontline workers and the community &mdash; "
              "both to <strong>respect</strong> them and to <strong>check</strong> your "
              "interpretation against theirs."},
             {"t": "hbox", "color": "cyan", "html": "Member checking: showing your reading of events "
              "to the people you observed is both an ethical duty and a validity test."},
         ]},

        {"type": "content", "label": "Loops", "title": "Build observation into the system",
         "blocks": [
             {"t": "body", "html": "The most powerful use of observation is not the one-off study "
              "but the <strong>feedback loop</strong>: routine, light-touch field observation that "
              "continuously corrects the programme &mdash; supervision visits that actually watch, "
              "and act."},
             {"t": "flow", "steps": [
                 "OBSERVE in routine visits",
                 "FLAG gaps between protocol and practice",
                 "ADJUST the programme",
                 "OBSERVE again"]},
         ]},

        {"type": "content", "label": "Caution", "title": "Don't over-reach from what you saw",
         "blocks": [
             {"t": "body", "html": "Observation at a handful of sites cannot, on its own, prove a "
              "statement about a whole district. State what your observation can carry &mdash; rich "
              "explanation, mechanism, hypotheses &mdash; and be honest about what it cannot."},
             {"t": "hbox", "color": "red", "html": "The fastest way to lose credibility is to claim "
              "population-level certainty from a few vivid visits. Match the claim to the evidence."},
         ]},

        {"type": "content", "label": "Communicate", "title": "Make the insight land",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Lead with the insight and its 'so what?', not the methodology",
                 "Use one concrete observed example to make it vivid",
                 "Show the triangulation that backs it",
                 "Name the decision it implies, and who owns it"]},
         ]},

        # ===================== SECTION 09 — Bias & rigour =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Bias &amp; Rigour"},

        {"type": "content", "label": "The Risk", "title": "The observer is part of the experiment",
         "blocks": [
             {"t": "body", "html": "In observation there is no neutral camera. <strong>You</strong> "
              "select, perceive and interpret &mdash; and your presence changes the scene. Rigour "
              "is not the absence of bias; it is the disciplined management of it."},
             {"t": "hbox", "color": "amber", "html": "The honest question is not 'am I biased?' "
              "(you are) but 'which biases are at work here, and what am I doing about them?'"},
         ]},

        {"type": "content", "label": "Observer Effect", "title": "The observer effect &amp; the Hawthorne effect",
         "blocks": [
             {"t": "term", "word": "Observer (Hawthorne) effect",
              "def": "People behave differently when they know they are being watched &mdash; named "
              "after the 1920s&ndash;30s Hawthorne Works studies, where worker output changed simply "
              "because attention was being paid."},
             {"t": "hbox", "color": "cyan", "html": "Mitigate by spending enough time that your "
              "presence becomes ordinary, observing routine rather than special events, and being "
              "honest in reporting that you were there."},
         ]},

        {"type": "content", "label": "Selective Attention", "title": "Selective attention",
         "blocks": [
             {"t": "body", "html": "The eye cannot take in everything, so it filters &mdash; and "
              "the filter is shaped by what you expect and care about. The famous "
              "'invisible gorilla' experiment showed observers can miss the obvious while counting "
              "something else."},
             {"t": "hbox", "color": "amber", "html": "Counter it with a framework that forces "
              "attention to dimensions you might skip &mdash; and with a second observer who notices "
              "what you do not."},
         ]},

        {"type": "content", "label": "Confirmation Bias", "title": "Confirmation bias",
         "blocks": [
             {"t": "term", "word": "Confirmation bias",
              "def": "The tendency to notice, record and weight what fits what you already believe, "
              "while overlooking what contradicts it &mdash; the single most dangerous bias in "
              "field observation."},
             {"t": "hbox", "color": "red", "html": "The discipline of hunting for disconfirming "
              "cases (Section 6) exists precisely to fight this. If everything confirms your prior, "
              "suspect yourself, not the world."},
         ]},

        {"type": "content", "label": "Going Native", "title": "Going native &mdash; losing the distance",
         "blocks": [
             {"t": "body", "html": "<strong>Going native</strong> is the opposite risk to detachment: "
              "the observer so identifies with the group that they stop questioning, adopt its "
              "assumptions, and lose the outsider's vantage that made observation valuable."},
             {"t": "hbox", "color": "amber", "html": "The fieldworker's tightrope: close enough to "
              "understand, distant enough to see. Step off and write reflective notes regularly to "
              "keep your footing."},
         ]},

        {"type": "content", "label": "Reflexivity", "title": "Reflexivity",
         "blocks": [
             {"t": "term", "word": "Reflexivity",
              "def": "The practice of examining how you &mdash; your assumptions, reactions and "
              "presence &mdash; shape what you observe and conclude, and recording it openly as "
              "part of the data."},
             {"t": "body", "html": "Keep a reflexive thread in your notes: What surprised me? What "
              "irritated me? What did I expect to see? Your reactions are evidence about both the "
              "setting and yourself."},
         ]},

        {"type": "content", "label": "Positionality", "title": "Positionality",
         "blocks": [
             {"t": "body", "html": "Who you are &mdash; gender, caste, class, age, language, the "
              "agency you represent &mdash; shapes what people show you and what you are able to "
              "see. <strong>Positionality</strong> is naming that honestly."},
             {"t": "hbox", "color": "cyan", "html": "A young male outsider and a local older woman "
              "will observe different versions of the same household. Neither is the truth; both "
              "must be named."},
         ]},

        {"type": "content", "label": "Rigour Toolkit", "title": "How to make observation trustworthy",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Prolonged engagement:</strong> enough time to see past the performance",
                 "<strong>Triangulation:</strong> multiple methods, sources and observers",
                 "<strong>Disconfirming cases:</strong> actively seek what breaks your pattern",
                 "<strong>Audit trail:</strong> show how you got from notes to claim",
                 "<strong>Member checking:</strong> test your reading with those observed",
                 "<strong>Reflexivity:</strong> name your own influence on the data"]},
         ]},

        # ===================== SECTION 10 — Ethics of observation =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Ethics of Observation"},

        {"type": "content", "label": "First Principle", "title": "You are watching real people's lives",
         "blocks": [
             {"t": "body", "html": "Observation enters people's spaces, routines and vulnerabilities "
              "&mdash; often without them gaining anything. Ethics is not a clearance form at the "
              "end; it is a duty that runs through every minute in the field."},
             {"t": "quote",
              "text": "The privilege of observing someone's life carries the obligation to protect it.",
              "attr": "&mdash; a principle of field research ethics"},
         ]},

        {"type": "content", "label": "Consent", "title": "Informed consent in observation",
         "blocks": [
             {"t": "body", "html": "People should know who you are, that you are observing, why, "
              "what you will do with what you record, and that they may decline &mdash; in a "
              "language and form they truly understand. Consent is harder in observation, because "
              "settings are fluid and people come and go."},
             {"t": "hbox", "color": "amber", "html": "Gain consent from gatekeepers <em>and</em> "
              "the people themselves. A headmaster's permission is not a child's consent."},
         ]},

        {"type": "content", "label": "Public vs Private", "title": "Privacy in public and private space",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Setting", "Expectation", "Your duty"],
              "rows": [
                  ["Open public space (market, road)", "Low privacy", "Observe, but don't single out individuals"],
                  ["Semi-public (clinic, school)", "Mixed", "Seek institutional and individual consent"],
                  ["Private (home, ritual, body)", "High privacy", "Explicit consent; many things stay unrecorded"]]},
             {"t": "hbox", "color": "red", "html": "'It happened in public' does not make everything "
              "fair to record. Sensitive acts in public spaces still deserve discretion."},
         ]},

        {"type": "content", "label": "Cameras", "title": "Photography &amp; recording",
         "blocks": [
             {"t": "body", "html": "A camera or recorder raises the stakes sharply: images and audio "
              "are identifiable, permanent and easily shared. They need their own, explicit consent "
              "&mdash; separate from consent to be observed."},
             {"t": "bullets", "color": "red", "sm": True, "items": [
                 "Never photograph children or sensitive scenes without specific consent",
                 "Explain where images will appear and for how long",
                 "Allow people to say yes to observation but no to the camera",
                 "Store and transmit recordings securely"]},
         ]},

        {"type": "content", "label": "Power", "title": "Power and vulnerability",
         "blocks": [
             {"t": "body", "html": "The observer usually holds more power than the observed &mdash; "
              "literacy, institutional backing, the ability to leave. In settings of poverty, caste "
              "or gender hierarchy, a 'request' from an outsider can feel impossible to refuse."},
             {"t": "hbox", "color": "amber", "html": "Make refusal genuinely costless. Watch for "
              "consent given only because saying no felt unsafe &mdash; that is not real consent."},
         ]},

        {"type": "content", "label": "Harm", "title": "Do no harm &mdash; including by what you reveal",
         "blocks": [
             {"t": "bullets", "items": [
                 "What you write could expose someone to retaliation if read by the wrong person",
                 "Disguise identities; aggregate; remove tell-tale details in small communities",
                 "Some things you observe should never be published &mdash; judgement, not rules",
                 "If you witness serious harm, your duty of care may override your role as observer"]},
             {"t": "hbox", "color": "red", "html": "Anonymity in a small village is hard: 'the only "
              "widow with a disabled son' identifies a person. Protect with care, not just labels."},
         ]},

        {"type": "content", "label": "Covert Again", "title": "The high bar for covert observation",
         "blocks": [
             {"t": "body", "html": "Covert observation denies people the chance to consent. It can "
              "only be contemplated when the knowledge is important, no other method is possible, "
              "and harm is minimal &mdash; and even then it needs formal ethics approval. In most "
              "development work it is neither necessary nor defensible."},
             {"t": "hbox", "color": "amber", "html": "If you find yourself hiding why you are there, "
              "stop and ask whether the study should happen at all."},
         ]},

        {"type": "content", "label": "Reciprocity", "title": "Give something back",
         "blocks": [
             {"t": "body", "html": "People give you their time, their space and their trust. "
              "Ethical observation asks what flows back: findings shared in usable form, "
              "recommendations that improve the service they use, respect for their time and "
              "their account of their own lives."},
             {"t": "hbox", "color": "green", "html": "The test of ethical fieldwork: would the "
              "people you observed feel fairly treated if they read everything you wrote about them?"},
         ]},

        # ===================== SECTION 11 — Practice & tools =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Practice &amp; Tools"},

        {"type": "content", "label": "Plan First", "title": "Planning an observation",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Decide", "Before you go"],
              "rows": [
                  ["Question", "What exactly am I trying to learn?"],
                  ["Type", "Participant or not? Structured or not? Overt (yes)"],
                  ["Site &amp; timing", "Where, when, and for how long?"],
                  ["Tool", "Notebook, guide, checklist &mdash; prepared and piloted"],
                  ["Consent", "Whose permission, and how I'll ask"],
                  ["Recording", "How I'll capture and protect what I see"]]},
             {"t": "hbox", "color": "cyan", "html": "An hour of planning saves a wasted day in the "
              "field. Walk in knowing your question and your method."},
         ]},

        {"type": "content", "label": "Template", "title": "A simple field-note template",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Header:</strong> date, time, place, observer, who was present",
                 "<strong>Sketch map:</strong> the space and where people were",
                 "<strong>Descriptive column:</strong> what happened, in order, low-inference",
                 "<strong>Reflective column [OC]:</strong> your questions and hunches, kept separate",
                 "<strong>Verbatim quotes:</strong> striking words, in quotation marks",
                 "<strong>Follow-ups:</strong> what to check or ask next time"]},
         ]},

        {"type": "content", "label": "Note Apps", "title": "Tools for capturing and analysing",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Good for", "Note"],
              "rows": [
                  ["Paper notebook", "Always-works field jottings", "Unbeatable; no battery, low intrusion"],
                  ["Voice memos", "Dictating expanded notes en route home", "Transcribe the same day"],
                  ["KoboToolbox / ODK", "Structured checklists on a phone, offline", "Free; great for counts &amp; ratings"],
                  ["Notes app / Obsidian", "Typing up and linking expanded notes", "Searchable; back it up"],
                  ["Taguette / spreadsheet", "Coding notes &amp; tagging themes", "Free; enough for most studies"]]},
             {"t": "hbox", "color": "amber", "html": "Tools serve the method, never replace it. A "
              "disciplined notebook beats a fancy app used carelessly."},
         ]},

        {"type": "content", "label": "Pitfalls", "title": "Common mistakes to avoid",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Writing up notes 'later' &mdash; later never comes; memory rots",
                 "Recording judgements instead of observable detail",
                 "Forgetting the camera and notebook also alter behaviour",
                 "Over-claiming from a few vivid visits",
                 "Skipping consent because the setting felt 'public'"]},
         ]},

        {"type": "content", "label": "Further Reading", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Participant Observation</em> &mdash; James P. Spradley (the nine dimensions, grand-tour)",
                 "<em>Writing Ethnographic Fieldnotes</em> &mdash; Emerson, Fretz &amp; Shaw",
                 "<em>The Interpretation of Cultures</em> &mdash; Clifford Geertz ('thick description')",
                 "<em>Qualitative Data Analysis</em> &mdash; Miles, Huberman &amp; Salda&ntilde;a (coding, display)",
                 "<em>Reflections on Fieldwork</em> &amp; field-methods guides from IDS and PRA traditions"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Qualitative Methods</strong>, <strong>Research Ethics</strong> and "
              "<strong>Data Literacy</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Watch what people do</strong> &mdash; the say&ndash;do gap is the finding",
                 "<strong>Use a framework</strong> &mdash; Spradley's nine dimensions focus the eye",
                 "<strong>Write it up the same day</strong> &mdash; the notebook is your instrument",
                 "<strong>Triangulate</strong> &mdash; one bearing is a guess; three fix a position",
                 "<strong>Observe ethically</strong> &mdash; behind every observation is a person"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Observation to Insight 101 &middot; Complete",
         "headline": "Now go and<br>watch closely.",
         "byline": "Surveys tell you what people say; observation shows you what they do. Go to "
                   "the field with a question, a notebook and a conscience &mdash; and turn what "
                   "you see into insight. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
