# -*- coding: utf-8 -*-
"""
Survey Design 101 — ImpactMojo 101 Series (native deck spec)
Designing trustworthy field surveys for South Asian development & MEL practitioners.
Build: python3 scripts/deck-builder/build.py survey_design
"""

DECK = {
    "slug": "survey-design",
    "title": "Survey Design 101",
    "description": ("Survey Design 101 — a free foundational course for development and MEL "
                    "practitioners running field surveys in South Asia. From objectives and "
                    "questionnaire design to sampling, modes, translation, pretesting, "
                    "fieldwork quality and survey ethics under the DPDP Act. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Survey<br>Design<br>101",
         "sub": "Designing, Writing &amp; Running Trustworthy Field Surveys &mdash; a "
                "Foundational Course for Development &amp; MEL Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Surveys Are &amp; When to Use One"},
             {"name": "The Survey Lifecycle"},
             {"name": "From Concept to Question"},
             {"name": "Writing Good Questions"},
             {"name": "Question &amp; Response Types"},
             {"name": "Questionnaire Structure &amp; Flow"},
             {"name": "Sampling for Surveys"},
             {"name": "Modes of Data Collection"},
             {"name": "Translation &amp; Cultural Adaptation"},
             {"name": "Pretesting, Piloting &amp; Fieldwork Quality"},
             {"name": "Ethics, Data &amp; Practice"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Surveys Are &amp; When to Use One"},

        {"type": "content", "label": "Definition", "title": "A survey is a measurement instrument",
         "blocks": [
             {"t": "body", "html": "A <strong>survey</strong> systematically collects "
              "standardised information from a sample of people, using the <em>same</em> "
              "questions in the <em>same</em> way, so answers can be counted and compared. "
              "Its power is standardisation; its discipline is design."},
             {"t": "term", "word": "Survey",
              "def": "A method of gathering quantitative information by asking a defined sample "
              "of respondents a fixed set of questions under controlled conditions, so the "
              "results can be aggregated and generalised to a population."},
             {"t": "hbox", "color": "cyan", "html": "A survey is not 'a list of questions'. It "
              "is an instrument that turns a concept into a number &mdash; and like any "
              "instrument, a badly built one produces confident nonsense."},
         ]},

        {"type": "content", "label": "When To Use One", "title": "Surveys answer 'how many' and 'how much'",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "A survey fits when&hellip;", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "You need numbers you can generalise",
                      "The concept is well understood already",
                      "You want to compare groups or track change",
                      "The population is too large to ask everyone"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "A survey misfits when&hellip;", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "You don't yet know the right questions",
                      "You need depth, meaning or 'why'",
                      "The topic is too sensitive for fixed answers",
                      "Good administrative data already exists"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Reach for a survey to <em>measure</em> "
              "something you already understand &mdash; not to <em>discover</em> what matters."},
         ]},

        {"type": "content", "label": "Three Data Sources", "title": "Survey, qualitative or administrative?",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Survey", "Qualitative", "Administrative"],
              "rows": [
                  ["Answers", "How many, how much", "Why, how, meaning", "What the system records"],
                  ["Strength", "Generalisable, comparable", "Depth, context, mechanism", "Cheap, continuous"],
                  ["Sample", "Representative sample", "Small, purposive", "Everyone served"],
                  ["Cost", "High &mdash; fieldwork", "Moderate", "Already collected"],
                  ["Blind spot", "Misses the 'why'", "Cannot generalise", "Misses who is not served"]]},
             {"t": "hbox", "color": "cyan", "html": "These are partners. A survey tells you "
              "<em>that</em> outcomes differ; qualitative work tells you <em>why</em>; admin "
              "data tells you what your programme already knows for free."},
         ]},

        {"type": "content", "label": "Exhaust Free Data First", "title": "Don't survey what already exists",
         "blocks": [
             {"t": "body", "html": "Before commissioning a survey, check whether the answer is "
              "already in <strong>secondary data</strong> &mdash; the Census, NFHS, PLFS/NSS, "
              "or your own HMIS, UDISE+ and MGNREGA records. Re-collecting wastes budget and, "
              "worse, wastes respondents' time."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "NFHS-5", "label": "Health, nutrition, fertility down to district",
                  "color": "cyan", "source": "IIPS / MoHFW, 2019&ndash;21"},
                 {"num": "PLFS", "label": "Employment &amp; unemployment, annual since 2017&ndash;18",
                  "color": "green", "source": "MoSPI"},
                 {"num": "HMIS", "label": "Your own facility data, updated monthly",
                  "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Rule of thumb: a new survey is justified "
              "only for what existing data genuinely cannot answer at the level you need."},
         ]},

        {"type": "content", "label": "Strengths", "title": "What a good survey buys you",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Generalisation:</strong> a few thousand can describe millions",
                 "<strong>Comparability:</strong> identical questions across people, places, time",
                 "<strong>Quantification:</strong> attach a number and a margin of error to a claim",
                 "<strong>Coverage:</strong> reach groups and topics no register captures",
                 "<strong>Transparency:</strong> a documented instrument others can scrutinise"]},
         ]},

        {"type": "content", "label": "Limits", "title": "What a survey can never give you",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Meaning:</strong> fixed options flatten messy human reality",
                 "<strong>The unasked:</strong> a closed question can only return its own choices",
                 "<strong>Truth on tap:</strong> people misremember, please, and self-present",
                 "<strong>The missing:</strong> whoever the frame and fieldwork miss stays invisible"]},
             {"t": "hbox", "color": "amber", "html": "A survey measures what you thought to ask, "
              "from whoever you managed to reach. Both boundaries are design choices &mdash; "
              "make them deliberately."},
         ]},

        {"type": "content", "label": "Mindset", "title": "The respondent is doing you a favour",
         "blocks": [
             {"t": "quote",
              "text": "Asking a question is asking for time, attention and trust from someone "
              "who owes you none. Design as if you will have to sit through your own survey.",
              "attr": "&mdash; a field researcher's rule of thumb"},
             {"t": "hbox", "color": "cyan", "html": "Every needless question, every confusing "
              "scale, every minute of length is a cost paid by a real person &mdash; often a "
              "busy, poor, over-surveyed one. Respect is good methodology."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Survey Lifecycle"},

        {"type": "content", "label": "The Whole Journey", "title": "Eight stages from question to use",
         "blocks": [
             {"t": "flow", "steps": [
                 "OBJECTIVES: the decision the survey must serve",
                 "INDICATORS: what to measure, defined precisely",
                 "INSTRUMENT: the questionnaire that captures it",
                 "SAMPLE: whom to ask, and how many",
                 "FIELDWORK: collecting data well in the field",
                 "DATA: clean, weighted, documented",
                 "ANALYSIS: turning answers into findings",
                 "USE: feeding a real decision"]},
             {"t": "hbox", "color": "cyan", "html": "Most survey failures are designed in at the "
              "start &mdash; not in the analysis. Time spent on the first four stages is repaid "
              "many times over in the last four."},
         ]},

        {"type": "content", "label": "Start From The Decision", "title": "Objectives before questions",
         "blocks": [
             {"t": "body", "html": "The first question is never 'what should we ask?' but "
              "<strong>'what decision will this survey inform?'</strong> Work backwards from the "
              "decision to the findings you need, then to the indicators, then to the questions."},
             {"t": "flow", "steps": [
                 "DECISION: where to scale the nutrition programme?",
                 "FINDING NEEDED: which blocks have highest stunting?",
                 "INDICATOR: % children under 5 stunted, by block",
                 "QUESTION: child's height &amp; age, measured directly"]},
             {"t": "hbox", "color": "red", "html": "If you cannot name the decision a question "
              "serves, cut the question. 'Nice to know' is the enemy of a usable survey."},
         ]},

        {"type": "content", "label": "Research Questions", "title": "Sharpen vague aims into answerable questions",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Too vague", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;Understand women's livelihoods in "
                   "the district.&rdquo; &mdash; unmeasurable; no population, no indicator, no "
                   "time frame."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Answerable", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;What share of women aged 18&ndash;45 "
                   "in Block X earned cash income in the last 30 days, and from what source?&rdquo;"}]}]},
             {"t": "hbox", "color": "amber", "html": "A good research question names <em>who</em>, "
              "<em>what</em>, <em>where</em> and <em>over what period</em>. If it doesn't, the "
              "questionnaire can't either."},
         ]},

        {"type": "content", "label": "Scope", "title": "Decide the unit and the reference period",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Unit of analysis:</strong> the household? the individual? the child? "
                 "the enterprise? Mixing units quietly breaks your numbers.",
                 "<strong>Respondent vs subject:</strong> a mother may report for a child &mdash; "
                 "name who answers about whom.",
                 "<strong>Reference period:</strong> last 7 days? last month? last year? "
                 "The window changes both recall and the indicator itself."]},
             {"t": "hbox", "color": "cyan", "html": "&lsquo;Household income&rsquo; and "
              "&lsquo;respondent's income&rsquo; are different surveys. Decide the unit before "
              "you write a single question."},
         ]},

        {"type": "content", "label": "Plan The Whole Chain", "title": "Design the analysis before fieldwork",
         "blocks": [
             {"t": "body", "html": "Sketch your <strong>dummy tables</strong> &mdash; the exact "
              "tables and charts you will produce &mdash; before collecting a single response. "
              "If a planned table needs a variable no question captures, you found the gap in "
              "time to fix it."},
             {"t": "hbox", "color": "green", "html": "&ldquo;Which table will this question feed?&rdquo; "
              "is the single best test of whether a question belongs in the instrument."},
         ]},

        {"type": "content", "label": "Resources", "title": "Budget, time and team shape the design",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Constraint", "Pushes toward", "Watch-out"],
              "rows": [
                  ["Tight budget", "Shorter instrument, phone mode", "Coverage &amp; quality loss"],
                  ["Short timeline", "Smaller sample, fewer items", "Underpowered estimates"],
                  ["Few trained staff", "Simpler skips, CAPI logic", "Enumerator error"],
                  ["Remote terrain", "Cluster sampling, offline tools", "Travel cost &amp; fatigue"]]},
             {"t": "hbox", "color": "amber", "html": "Constraints are not excuses for sloppiness "
              "&mdash; they are inputs to design. A realistic small survey beats an ambitious "
              "one that collapses in the field."},
         ]},

        {"type": "content", "label": "Documentation", "title": "Write it down as you go",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "A <strong>survey protocol</strong>: objectives, population, sample, methods",
                 "A <strong>questionnaire</strong> with variable names and routing",
                 "A <strong>field manual</strong> for enumerators and supervisors",
                 "A <strong>data dictionary</strong>: every variable, code and unit"]},
             {"t": "hbox", "color": "cyan", "html": "These four documents are the difference "
              "between a survey someone can trust and re-use, and a one-off whose meaning dies "
              "with the team that ran it."},
         ]},

        {"type": "content", "label": "Iterate", "title": "The lifecycle loops, it doesn't end",
         "blocks": [
             {"t": "body", "html": "Pretesting sends you back to rewrite questions. Piloting "
              "sends you back to fix routing and sample. Analysis reveals what the next round "
              "should ask. A survey programme is a <strong>cycle of learning</strong>, not a "
              "single shot."},
             {"t": "quote", "text": "No questionnaire survives first contact with respondents. "
              "The good ones are the most rewritten.",
              "attr": "&mdash; survey methodology folklore"},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "From Concept to Question"},

        {"type": "content", "label": "The Core Problem", "title": "You cannot ask 'empowerment' directly",
         "blocks": [
             {"t": "body", "html": "Most things surveys care about &mdash; empowerment, food "
              "security, trust, wellbeing &mdash; are <strong>concepts</strong>, not facts you "
              "can simply request. The questionnaire is the bridge from an abstract concept to "
              "a concrete, observable answer."},
             {"t": "flow", "steps": [
                 "CONCEPT: food security",
                 "DIMENSIONS: access, sufficiency, anxiety",
                 "INDICATOR: days household ate fewer meals last month",
                 "QUESTION: &ldquo;In the last 30 days, on how many days&hellip;?&rdquo;"]},
         ]},

        {"type": "content", "label": "Operationalising", "title": "Turn the concept into a measurement rule",
         "blocks": [
             {"t": "term", "word": "Operationalisation",
              "def": "The precise rule that converts a concept into something countable: exactly "
              "what to ask, of whom, over what period, in what units, and how the answer maps "
              "to the indicator."},
             {"t": "body", "html": "&lsquo;Is the household poor?&rsquo; only becomes measurable "
              "once you fix the definition &mdash; income below a line? deprived on a set of "
              "MPI indicators? &mdash; and write the exact questions that test it."},
         ]},

        {"type": "content", "label": "The Instrument Measures", "title": "The questionnaire IS the measurement",
         "blocks": [
             {"t": "body", "html": "There is no underlying 'true survey' that a questionnaire "
              "merely records. The wording, order, options and translation <em>are</em> the "
              "instrument &mdash; change them and you change what you measure. Two questionnaires "
              "on the 'same' topic can yield different numbers, both correct for their wording."},
             {"t": "hbox", "color": "red", "html": "This is why comparability demands "
              "<em>identical</em> instruments. Surveys compare answers to <em>questions</em>, "
              "not to reality directly &mdash; so the question must hold still."},
         ]},

        {"type": "content", "label": "Total Survey Error", "title": "A map of everything that can go wrong",
         "blocks": [
             {"t": "body", "html": "Groves' <strong>Total Survey Error (TSE)</strong> framework "
              "organises every source of error in a survey into two families: errors of "
              "<strong>representation</strong> (the wrong people) and errors of "
              "<strong>measurement</strong> (the wrong answers). Good design manages both at once."},
             {"t": "term", "word": "Total Survey Error",
              "def": "The accumulated difference between a survey estimate and the true "
              "population value, from all sources &mdash; sampling and non-sampling, "
              "representation and measurement &mdash; considered together (Groves et al.)."},
         ]},

        {"type": "content", "label": "The TSE Tree", "title": "Two branches, many leaves",
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 1180 470" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;height:auto;font-family:inherit">'
                 '<defs><style>'
                 '.n{stroke-width:2;rx:10;ry:10}'
                 '.t{font-size:19px;font-weight:700;fill:#0f172a}'
                 '.s{font-size:15px;fill:#334155}'
                 '.lk{stroke:#94a3b8;stroke-width:2;fill:none}'
                 '</style></defs>'
                 # links
                 '<path class="lk" d="M590,72 L300,140"/>'
                 '<path class="lk" d="M590,72 L880,140"/>'
                 '<path class="lk" d="M300,176 L160,250"/>'
                 '<path class="lk" d="M300,176 L300,250"/>'
                 '<path class="lk" d="M300,176 L440,250"/>'
                 '<path class="lk" d="M880,176 L740,250"/>'
                 '<path class="lk" d="M880,176 L1020,250"/>'
                 # root
                 '<rect class="n" x="470" y="36" width="240" height="40" fill="#E0F2FE" stroke="#0EA5E9"/>'
                 '<text class="t" x="590" y="62" text-anchor="middle">Total Survey Error</text>'
                 # branch heads
                 '<rect class="n" x="180" y="140" width="240" height="40" fill="#EDE9FE" stroke="#6366F1"/>'
                 '<text class="t" x="300" y="166" text-anchor="middle">Representation</text>'
                 '<rect class="n" x="760" y="140" width="240" height="40" fill="#D1FAE5" stroke="#10B981"/>'
                 '<text class="t" x="880" y="166" text-anchor="middle">Measurement</text>'
                 # representation leaves
                 '<rect class="n" x="60" y="252" width="200" height="64" fill="#fff" stroke="#6366F1"/>'
                 '<text class="s" x="160" y="278" text-anchor="middle">Coverage error</text>'
                 '<text class="s" x="160" y="300" text-anchor="middle">(frame gaps)</text>'
                 '<rect class="n" x="200" y="330" width="200" height="64" fill="#fff" stroke="#6366F1"/>'
                 '<text class="s" x="300" y="356" text-anchor="middle">Sampling error</text>'
                 '<text class="s" x="300" y="378" text-anchor="middle">(chance of the draw)</text>'
                 '<rect class="n" x="340" y="252" width="200" height="64" fill="#fff" stroke="#6366F1"/>'
                 '<text class="s" x="440" y="278" text-anchor="middle">Non-response</text>'
                 '<text class="s" x="440" y="300" text-anchor="middle">(refusals, not-at-home)</text>'
                 # measurement leaves
                 '<rect class="n" x="640" y="252" width="200" height="64" fill="#fff" stroke="#10B981"/>'
                 '<text class="s" x="740" y="278" text-anchor="middle">Validity</text>'
                 '<text class="s" x="740" y="300" text-anchor="middle">(asks wrong thing)</text>'
                 '<rect class="n" x="780" y="330" width="220" height="64" fill="#fff" stroke="#10B981"/>'
                 '<text class="s" x="890" y="356" text-anchor="middle">Response error</text>'
                 '<text class="s" x="890" y="378" text-anchor="middle">(recall, bias, wording)</text>'
                 '<rect class="n" x="920" y="252" width="200" height="64" fill="#fff" stroke="#10B981"/>'
                 '<text class="s" x="1020" y="278" text-anchor="middle">Processing error</text>'
                 '<text class="s" x="1020" y="300" text-anchor="middle">(entry, coding)</text>'
                 '</svg>')},
         ]},

        {"type": "content", "label": "Two Families", "title": "Representation vs measurement error",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Representation (wrong people)", "Measurement (wrong answers)"],
              "rows": [
                  ["Coverage", "Frame misses part of the population", "&mdash;"],
                  ["Sampling", "Chance variation in who is drawn", "&mdash;"],
                  ["Non-response", "Those who answer differ from those who don't", "&mdash;"],
                  ["Validity", "&mdash;", "Question doesn't capture the concept"],
                  ["Response", "&mdash;", "Recall, social desirability, bad wording"],
                  ["Processing", "&mdash;", "Data entry &amp; coding mistakes"]]},
             {"t": "hbox", "color": "amber", "html": "Sampling error shrinks with sample size. "
              "The other five do not &mdash; they need <em>design</em>, not a bigger n."},
         ]},

        {"type": "content", "label": "Trade-Offs", "title": "You manage error within a fixed budget",
         "blocks": [
             {"t": "body", "html": "TSE's practical lesson: a fixed budget forces trade-offs. "
              "Spending everything on a huge sample (less sampling error) may starve enumerator "
              "training (more response error). Total error is what matters &mdash; not any one "
              "component."},
             {"t": "hbox", "color": "cyan", "html": "Ask of every design choice: which errors "
              "does it reduce, which does it grow, and is the <em>total</em> smaller? A smaller "
              "but well-run survey often beats a larger, sloppier one."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Writing Good Questions"},

        {"type": "content", "label": "The Golden Rule", "title": "Clear, specific, one idea",
         "blocks": [
             {"t": "body", "html": "A good survey question is understood the <em>same way</em> "
              "by every respondent and the question-writer. Three tests cover most failures: is "
              "it <strong>clear</strong>, is it <strong>specific</strong>, does it ask "
              "<strong>one</strong> thing?"},
             {"t": "flow", "steps": [
                 "CLEAR: plain words the respondent uses",
                 "SPECIFIC: a definite thing, time and unit",
                 "ONE IDEA: a single answerable question",
                 "NEUTRAL: no nudge toward an answer"]},
         ]},

        {"type": "content", "label": "Double-Barrelled", "title": "One question, one idea &mdash; never two",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Bad", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;Is the health centre clean and "
                   "well-staffed?&rdquo; &mdash; clean but understaffed? The respondent can't "
                   "answer; you can't interpret."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Good", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;Is the health centre clean?&rdquo; "
                   "<br><em>then</em><br>&ldquo;Is the health centre adequately staffed?&rdquo; "
                   "&mdash; two questions, two clean answers."}]}]},
             {"t": "hbox", "color": "amber", "html": "Watch for the word <strong>and</strong> "
              "&mdash; it is the commonest sign a question is secretly two."},
         ]},

        {"type": "content", "label": "Leading", "title": "Don't tell the respondent what to say",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Leading", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;Don't you agree the new clinic has "
                   "improved care?&rdquo; &mdash; pushes a yes; politeness does the rest."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Neutral", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;Since the new clinic opened, has "
                   "the care you receive become better, stayed the same, or become worse?&rdquo;"}]}]},
             {"t": "hbox", "color": "cyan", "html": "Offer the full range of answers in the "
              "question itself. A balanced stem signals that any answer is acceptable."},
         ]},

        {"type": "content", "label": "Loaded &amp; Assuming", "title": "Don't smuggle in assumptions",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Loaded", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;How much did the corrupt official "
                   "demand?&rdquo; &mdash; assumes corruption and a demand. &ldquo;How many "
                   "children do you still want?&rdquo; assumes she wants more."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Open the assumption", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;Did you pay anything beyond the "
                   "official fee?&rdquo; &mdash; <em>then</em> ask how much. Let a filter "
                   "establish the fact before you ask about it."}]}]},
             {"t": "hbox", "color": "amber", "html": "A loaded question forces a false premise. "
              "Use a filter question to establish the fact <em>before</em> asking about it."},
         ]},

        {"type": "content", "label": "Jargon", "title": "Use the respondent's words, not yours",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Insider language", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;Do you utilise institutional "
                   "delivery services and avail ANC?&rdquo; &mdash; acronyms and jargon no "
                   "respondent uses."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Plain", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;When you were pregnant, did you go "
                   "for check-ups? Where did you give birth &mdash; at home or at a "
                   "facility?&rdquo;"}]}]},
             {"t": "hbox", "color": "cyan", "html": "If a question needs the enumerator to "
              "explain a word, the word is wrong. Write for the least-schooled respondent in "
              "your sample."},
         ]},

        {"type": "content", "label": "Reference Periods", "title": "Anchor every question in time",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Vague", "Anchored", "Why it's better"],
              "rows": [
                  ["&ldquo;Do you usually&hellip;?&rdquo;", "&ldquo;In the last 7 days&hellip;?&rdquo;", "Defines 'usually' for everyone"],
                  ["&ldquo;recently&rdquo;", "&ldquo;in the last 30 days&rdquo;", "Same window for all respondents"],
                  ["&ldquo;your income&rdquo;", "&ldquo;income last month&rdquo;", "Fixes the unit of time"],
                  ["&ldquo;often sick&rdquo;", "&ldquo;ill in the past 2 weeks&rdquo;", "Countable, comparable"]]},
             {"t": "hbox", "color": "green", "html": "The right window balances recall against "
              "rarity: short enough to remember, long enough to capture the event. Health uses "
              "2 weeks; consumption, 30 days; big purchases, a year."},
         ]},

        {"type": "content", "label": "Recall Error", "title": "Memory fades &mdash; and bends",
         "blocks": [
             {"t": "term", "word": "Recall error",
              "def": "The gap between what actually happened and what a respondent remembers and "
              "reports &mdash; events forgotten, dates blurred, or 'telescoped' in from outside "
              "the reference period."},
             {"t": "bullets", "items": [
                 "<strong>Forgetting:</strong> small, routine events vanish first",
                 "<strong>Telescoping:</strong> a memorable event is pulled into the window",
                 "<strong>Salience:</strong> big events (a death, a wedding) recalled far better",
                 "<strong>Fix:</strong> shorter windows, anchoring to landmark dates &amp; festivals"]},
         ]},

        {"type": "content", "label": "A Rewrite Drill", "title": "Spot every flaw, then fix it",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Before", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;Don't you think you should usually "
                   "spend more on your children's education and health?&rdquo;"},
                  {"t": "body", "cls": "sm", "html": "<em>Leading + double-barrelled + vague + "
                   "loaded</em> &mdash; all four faults in one line."}]}],
              "right": [{"t": "panel", "color": "green", "title": "After", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&ldquo;In the last 30 days, about how much "
                   "did your household spend on schooling?&rdquo; <em>then</em> &ldquo;&hellip;on "
                   "health?&rdquo;"}]}]},
             {"t": "hbox", "color": "cyan", "html": "Read every question aloud and ask: am I "
              "leading, doubling up, assuming, or using jargon? Most bad questions fail more "
              "than one test at once."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Question &amp; Response Types"},

        {"type": "content", "label": "Open vs Closed", "title": "Let them speak, or give them choices?",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Open-ended", "Closed-ended"],
              "rows": [
                  ["Answer", "In their own words", "Pick from fixed options"],
                  ["Best for", "Exploring, unknown answers", "Counting, comparing"],
                  ["Analysis", "Slow &mdash; needs coding", "Fast &mdash; ready to tabulate"],
                  ["Risk", "Vague, hard to compare", "Misses the unlisted answer"],
                  ["Use when", "Few cases, discovery", "Most quantitative items"]]},
             {"t": "hbox", "color": "amber", "html": "A closed question can only ever return the "
              "options you wrote. Pretest open-ended first to learn the real answer set, then "
              "close it for scale."},
         ]},

        {"type": "content", "label": "Closed Done Well", "title": "Exhaustive and mutually exclusive",
         "blocks": [
             {"t": "body", "html": "Response options must cover <strong>every</strong> possible "
              "answer (exhaustive) and never overlap (mutually exclusive). A respondent should "
              "always find exactly one box that fits."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Overlapping", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Age: 0&ndash;18, 18&ndash;30, 30&ndash;50 "
                   "&mdash; where does an 18- or 30-year-old go? And what about 60+?"}]}],
              "right": [{"t": "panel", "color": "green", "title": "Clean", "blocks": [
                  {"t": "body", "cls": "sm", "html": "0&ndash;17, 18&ndash;29, 30&ndash;49, "
                   "50&ndash;64, 65+ &mdash; no gaps, no overlaps, a home for everyone."}]}]},
         ]},

        {"type": "content", "label": "Likert Scales", "title": "Measuring agreement and attitude",
         "blocks": [
             {"t": "term", "word": "Likert scale",
              "def": "A symmetric, ordered set of response options &mdash; typically 5 or 7 "
              "points &mdash; running from strong disagreement to strong agreement, with a "
              "neutral midpoint and balanced wording on each side."},
             {"t": "body", "html": "Example: <em>Strongly disagree &middot; Disagree &middot; "
              "Neither &middot; Agree &middot; Strongly agree.</em> Keep the steps balanced, "
              "label every point (not just the ends), and use the same scale throughout a block."},
         ]},

        {"type": "content", "label": "Scale Choices", "title": "How many points, and a midpoint?",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Choice", "Pro", "Con"],
              "rows": [
                  ["5 points", "Simple, fast, fits small screens", "Less fine-grained"],
                  ["7 points", "More discrimination", "Harder to read aloud"],
                  ["With midpoint", "Allows a genuine neutral", "Some hide there to avoid choosing"],
                  ["Forced (no midpoint)", "Pushes a stance", "Fabricates an opinion that isn't there"]]},
             {"t": "hbox", "color": "cyan", "html": "For face-to-face fieldwork with mixed "
              "literacy, a labelled <strong>5-point</strong> scale read aloud usually travels "
              "best. Whatever you pick, keep it consistent across the instrument."},
         ]},

        {"type": "content", "label": "Rating &amp; Ranking", "title": "Rate each, or order them?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Rating", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Score each item on its own scale (rate each "
                   "service 1&ndash;5). Easy, but everything can end up 'good'."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Ranking", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Force an order (rank your top 3 priorities). "
                   "Reveals trade-offs, but is cognitively harder &mdash; keep the list short."}]}]},
             {"t": "hbox", "color": "amber", "html": "Ranking more than 4&ndash;5 items overloads "
              "respondents in the field. If you must, ask only for the top few, not a full order."},
         ]},

        {"type": "content", "label": "Don't Know", "title": "When 'don't know' is data, not laziness",
         "blocks": [
             {"t": "body", "html": "A genuine <strong>&lsquo;Don't know&rsquo;</strong> or "
              "<strong>&lsquo;Refused&rsquo;</strong> option prevents respondents from guessing "
              "or enumerators from inventing answers. But offered too readily, it becomes an "
              "easy escape that hollows out your data."},
             {"t": "bullets", "sm": True, "items": [
                 "Keep DK/Refused available but <em>not</em> read aloud as a default",
                 "Distinguish &lsquo;don't know&rsquo; from &lsquo;not applicable&rsquo; from &lsquo;refused&rsquo;",
                 "Code them separately &mdash; never silently as missing or zero"]},
         ]},

        {"type": "content", "label": "Filters &amp; Skips", "title": "Ask only what applies",
         "blocks": [
             {"t": "body", "html": "A <strong>filter</strong> (gateway) question routes each "
              "respondent to only the relevant items via <strong>skip logic</strong> &mdash; "
              "so a man is never asked about his last pregnancy, and a non-farmer skips the "
              "whole farming module."},
             {"t": "flow", "steps": [
                 "FILTER: Did anyone in the household farm last season?",
                 "IF NO &rarr; skip the entire agriculture module",
                 "IF YES &rarr; ask crops, area, inputs, yield",
                 "RESULT: shorter interview, cleaner data"]},
         ]},

        {"type": "content", "label": "Routing On CAPI", "title": "Why skip logic loves a screen",
         "blocks": [
             {"t": "body", "html": "On paper, complex skips invite enumerator error &mdash; "
              "missed branches, contradictory entries. On <strong>CAPI</strong> "
              "(computer-assisted personal interviewing), the device enforces routing "
              "automatically and can run real-time consistency checks."},
             {"t": "hbox", "color": "green", "html": "Build skips, ranges and logic checks into "
              "the digital instrument so impossible answers (a 6-year-old with children) are "
              "caught at the doorstep, not in cleaning weeks later."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Questionnaire Structure &amp; Flow"},

        {"type": "content", "label": "The Whole Arc", "title": "A questionnaire has a beginning, middle, end",
         "blocks": [
             {"t": "body", "html": "Order is not cosmetic &mdash; it shapes answers and "
              "completion. A well-built instrument moves the respondent through a deliberate "
              "<strong>arc</strong>: welcome, easy questions, the core, the sensitive, then "
              "the close."},
             {"t": "flow", "steps": [
                 "INTRO: consent, purpose, confidentiality",
                 "WARM-UP: easy, non-threatening items",
                 "CORE: the main substantive modules",
                 "SENSITIVE: income, health, beliefs &mdash; late",
                 "CLOSE: demographics, thanks"]},
         ]},

        {"type": "content", "label": "The Questionnaire Map", "title": "A flow diagram of one instrument",
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 1180 430" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;height:auto;font-family:inherit">'
                 '<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="3" '
                 'orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#64748b"/></marker>'
                 '<style>.bx{rx:10;ry:10;stroke-width:2}.lb{font-size:15px;fill:#0f172a;font-weight:600}'
                 '.sm2{font-size:13px;fill:#475569}.ln{stroke:#64748b;stroke-width:2;fill:none;marker-end:url(#ah)}'
                 '.yn{font-size:13px;fill:#475569;font-style:italic}</style></defs>'
                 # boxes top row
                 '<rect class="bx" x="40" y="40" width="180" height="56" fill="#E0F2FE" stroke="#0EA5E9"/>'
                 '<text class="lb" x="130" y="64" text-anchor="middle">Consent</text>'
                 '<text class="sm2" x="130" y="84" text-anchor="middle">screen / refuse &rarr; end</text>'
                 '<rect class="bx" x="300" y="40" width="180" height="56" fill="#fff" stroke="#0EA5E9"/>'
                 '<text class="lb" x="390" y="64" text-anchor="middle">Warm-up</text>'
                 '<text class="sm2" x="390" y="84" text-anchor="middle">easy items</text>'
                 '<rect class="bx" x="560" y="40" width="200" height="56" fill="#fff" stroke="#10B981"/>'
                 '<text class="lb" x="660" y="64" text-anchor="middle">Filter: farms?</text>'
                 '<text class="sm2" x="660" y="84" text-anchor="middle">gateway question</text>'
                 # branch
                 '<rect class="bx" x="840" y="20" width="200" height="50" fill="#D1FAE5" stroke="#10B981"/>'
                 '<text class="lb" x="940" y="50" text-anchor="middle">Agriculture module</text>'
                 '<rect class="bx" x="840" y="100" width="200" height="44" fill="#FEF3C7" stroke="#F59E0B"/>'
                 '<text class="lb" x="940" y="128" text-anchor="middle">Skip module</text>'
                 # second row
                 '<rect class="bx" x="560" y="210" width="200" height="56" fill="#EDE9FE" stroke="#6366F1"/>'
                 '<text class="lb" x="660" y="234" text-anchor="middle">Core modules</text>'
                 '<text class="sm2" x="660" y="254" text-anchor="middle">main outcomes</text>'
                 '<rect class="bx" x="300" y="210" width="200" height="56" fill="#FEE2E2" stroke="#EF4444"/>'
                 '<text class="lb" x="400" y="234" text-anchor="middle">Sensitive block</text>'
                 '<text class="sm2" x="400" y="254" text-anchor="middle">income, health</text>'
                 '<rect class="bx" x="40" y="210" width="180" height="56" fill="#E0F2FE" stroke="#0EA5E9"/>'
                 '<text class="lb" x="130" y="234" text-anchor="middle">Demographics</text>'
                 '<text class="sm2" x="130" y="254" text-anchor="middle">&amp; close / thanks</text>'
                 # arrows
                 '<path class="ln" d="M220,68 L298,68"/>'
                 '<path class="ln" d="M480,68 L558,68"/>'
                 '<path class="ln" d="M760,58 L838,45"/>'
                 '<text class="yn" x="800" y="38">yes</text>'
                 '<path class="ln" d="M760,80 L838,118"/>'
                 '<text class="yn" x="800" y="108">no</text>'
                 '<path class="ln" d="M940,144 L940,180 L760,238"/>'
                 '<path class="ln" d="M940,70 L940,90"/>'
                 '<path class="ln" d="M560,238 L502,238"/>'
                 '<path class="ln" d="M300,238 L222,238"/>'
                 '</svg>')},
         ]},

        {"type": "content", "label": "Logical Order", "title": "Group by topic, move from general to specific",
         "blocks": [
             {"t": "bullets", "items": [
                 "Cluster related items into clearly signposted <strong>modules</strong>",
                 "Within a module, go from <strong>general</strong> to <strong>specific</strong>",
                 "Keep the same response scale within a block to build rhythm",
                 "Don't jump topics erratically &mdash; context-switching tires and confuses"]},
             {"t": "hbox", "color": "cyan", "html": "A respondent who can follow the logic stays "
              "engaged and answers more accurately. Disordered questionnaires leak data through "
              "fatigue and confusion."},
         ]},

        {"type": "content", "label": "Question Order Effects", "title": "Earlier questions colour later answers",
         "blocks": [
             {"t": "body", "html": "Asking about local crime, <em>then</em> overall life "
              "satisfaction, drags satisfaction down &mdash; the first question primes the "
              "second. <strong>Order effects</strong> are real and measurable."},
             {"t": "hbox", "color": "amber", "html": "Put general attitude questions <em>before</em> "
              "specific ones on the same topic, and keep the order identical across rounds so "
              "any priming is at least constant and comparable."},
         ]},

        {"type": "content", "label": "Warm Up First", "title": "Open with easy, relevant questions",
         "blocks": [
             {"t": "body", "html": "The first questions should be <strong>easy, non-threatening "
              "and obviously relevant</strong> &mdash; they build rapport and signal that the "
              "survey is safe. Never open with income, caste or a long grid; you'll lose people "
              "at the door."},
             {"t": "hbox", "color": "green", "html": "Save demographics like income and caste "
              "for late in the interview, once trust is established &mdash; not as an "
              "intimidating opening gate."},
         ]},

        {"type": "content", "label": "Sensitive Questions", "title": "Handle the hard topics with care",
         "blocks": [
             {"t": "bullets", "items": [
                 "Place them <strong>late</strong>, after rapport is built",
                 "Normalise: &ldquo;Many people find&hellip;&rdquo; lowers the threat",
                 "Offer <strong>private modes</strong> (self-completion, sealed response) for "
                 "stigmatised topics",
                 "Always allow refusal without penalty or pressure"]},
             {"t": "hbox", "color": "red", "html": "Income, health status, violence, caste, "
              "sexual behaviour and political views all invite <em>social-desirability bias</em>. "
              "Design reduces it; clumsy placement amplifies it."},
         ]},

        {"type": "content", "label": "Length &amp; Fatigue", "title": "Every extra minute costs quality",
         "blocks": [
             {"t": "chart", "canvas": "fatigueChart",
              "title": "Illustrative: data quality declines as the interview lengthens",
              "source": "Illustrative pattern (respondent fatigue)",
              "type": "line",
              "data": {"labels": ["10", "20", "30", "40", "50", "60", "75", "90"],
                       "datasets": [{"label": "Relative answer quality (%)",
                                     "data": [99, 97, 94, 88, 80, 70, 56, 42],
                                     "borderColor": "#EF4444",
                                     "backgroundColor": "rgba(239,68,68,0.08)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Interview length (minutes)'} }, y:{ min:0, max:100, title:{display:true,text:'Answer quality (illustrative %)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "As fatigue sets in, respondents "
              "&lsquo;straight-line&rsquo; grids, pick the first option, and say 'don't know' "
              "to escape. Ruthlessly cut every question that doesn't feed a planned table."},
         ]},

        {"type": "content", "label": "Layout", "title": "Design the page, not just the words",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Number questions and variables consistently for clean data entry",
                 "Make instructions to the enumerator visually distinct from the question text",
                 "Show skip instructions <em>at</em> the branching question, in bold",
                 "On CAPI, one screen per question reduces missed items and accidental skips"]},
             {"t": "hbox", "color": "cyan", "html": "A cramped, ambiguous layout produces "
              "enumerator errors that no amount of cleaning fully repairs. Layout is part of "
              "measurement."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Sampling for Surveys"},

        {"type": "content", "label": "Why Sample", "title": "A good sample stands in for millions",
         "blocks": [
             {"t": "body", "html": "You rarely need to ask everyone. A well-drawn "
              "<strong>sample</strong> of a few thousand can describe a population of millions "
              "&mdash; the principle behind NFHS, PLFS and every credible poll. The magic is "
              "not size, it is <strong>representativeness</strong>."},
             {"t": "hbox", "color": "cyan", "html": "Data Literacy 101 covers the basics of "
              "sampling; here we go deeper into the choices a survey designer actually makes in "
              "the field."},
         ]},

        {"type": "content", "label": "Probability Methods", "title": "Let chance choose &mdash; it removes bias",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Method", "How", "Use when"],
              "rows": [
                  ["Simple random", "Every unit equal chance", "You have a full list"],
                  ["Systematic", "Every k-th unit from a list", "Ordered list, no hidden cycle"],
                  ["Stratified", "Split into groups, sample each", "Must represent subgroups"],
                  ["Cluster", "Sample whole groups (villages)", "People geographically spread"],
                  ["Multistage", "Clusters, then units within", "Large national surveys (NFHS)"]]},
             {"t": "hbox", "color": "green", "html": "Only probability sampling lets you compute "
              "a margin of error and generalise honestly. Everything else can describe, but not "
              "infer."},
         ]},

        {"type": "content", "label": "The Sampling Frame", "title": "Your survey is only as good as its list",
         "blocks": [
             {"t": "term", "word": "Sampling frame",
              "def": "The actual list of units from which you draw your sample &mdash; the "
              "operational stand-in for the target population. Whoever the frame omits, your "
              "survey can never reach."},
             {"t": "flow", "steps": [
                 "TARGET POPULATION: whom you want to learn about",
                 "SAMPLING FRAME: the list you can actually draw from",
                 "SAMPLE: who you end up selecting",
                 "RESPONDENTS: who actually answers"]},
             {"t": "hbox", "color": "red", "html": "The frame is often the weakest link. A list "
              "of phone numbers is not a list of citizens; a voter roll misses children and "
              "recent migrants. Coverage error starts here."},
         ]},

        {"type": "content", "label": "Stratify To Compare", "title": "Over-sample small groups on purpose",
         "blocks": [
             {"t": "body", "html": "If you need reliable estimates for a small subgroup &mdash; "
              "say, a tribal block or a minority community &mdash; a proportional sample may "
              "yield too few of them. <strong>Stratify</strong> and deliberately over-sample "
              "that group, then correct with weights."},
             {"t": "hbox", "color": "amber", "html": "Design choice: representing every district "
              "equally, or every person equally? You usually can't have both at once &mdash; "
              "decide which your analysis needs, and weight accordingly."},
         ]},

        {"type": "content", "label": "Sample Size", "title": "How many do I actually need?",
         "blocks": [
             {"t": "chart", "canvas": "moeSurveyChart",
              "title": "Margin of error vs sample size (95% confidence, p=0.5)",
              "source": "Standard sampling theory",
              "type": "line",
              "data": {"labels": ["100", "200", "384", "600", "1067", "1500", "2400", "4000"],
                       "datasets": [{"label": "Margin of error (±%)",
                                     "data": [9.8, 6.9, 5.0, 4.0, 3.0, 2.5, 2.0, 1.5],
                                     "borderColor": "#0EA5E9",
                                     "backgroundColor": "rgba(14,165,233,0.08)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'± percentage points'} } } }"}},
             {"t": "hbox", "color": "green", "html": "Landmark numbers (95% CI, p=0.5): "
              "<strong>n&asymp;384</strong> gives about <strong>±5%</strong>; "
              "<strong>n&asymp;1,067</strong> gives about <strong>±3%</strong>. Halving the "
              "error roughly quadruples the sample &mdash; precision gets expensive fast."},
         ]},

        {"type": "content", "label": "Drivers Of Size", "title": "What changes the number you need",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["If you want&hellip;", "You need&hellip;", "Note"],
              "rows": [
                  ["Tighter margin of error", "A larger sample", "±3% needs ~3&times; the n of ±5%"],
                  ["Estimates for subgroups", "More per subgroup", "Each cell needs its own n"],
                  ["To detect a small change", "More power", "Effect size drives this"],
                  ["Cluster (not random) design", "An inflation factor", "The 'design effect'"]]},
             {"t": "hbox", "color": "cyan", "html": "Cluster sampling saves travel cost but "
              "inflates required size via the <strong>design effect</strong> &mdash; people in "
              "one village resemble each other, so each adds less new information."},
         ]},

        {"type": "content", "label": "Bias Beats Size", "title": "The errors a bigger sample can't fix",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Coverage bias:</strong> the frame systematically misses people",
                 "<strong>Non-response bias:</strong> refusers differ from responders",
                 "<strong>Selection bias:</strong> the draw method favours some over others"]},
             {"t": "hbox", "color": "amber", "html": "A bigger biased sample is just a more "
              "confident wrong answer. Sample size shrinks <em>sampling</em> error only &mdash; "
              "never bias. Fix bias with design, not with n."},
         ]},

        {"type": "content", "label": "Weights", "title": "Why survey results come 'weighted'",
         "blocks": [
             {"t": "body", "html": "When groups are over-sampled by design or respond at "
              "different rates, surveys apply <strong>weights</strong> so each respondent "
              "represents the right number of real people. Unit data from NFHS or PLFS gives "
              "wrong totals if you ignore the weights."},
             {"t": "hbox", "color": "indigo", "html": "Weighting is the bridge back to the "
              "population. (Data Literacy 101 covers how to read weighted estimates; here the "
              "point is to <em>plan</em> for them at the design stage.)"},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Modes of Data Collection"},

        {"type": "content", "label": "Mode Matters", "title": "How you ask changes what you hear",
         "blocks": [
             {"t": "body", "html": "The <strong>mode</strong> &mdash; face-to-face, phone, web, "
              "self-completion &mdash; is not a neutral pipe. It shapes who you reach, how long "
              "they'll stay, how honest they are, and what you can ask. Choose it as carefully "
              "as the questions."},
             {"t": "term", "word": "Mode",
              "def": "The channel through which questions are delivered and answers captured. "
              "Each mode carries its own coverage, cost, length limit and pattern of response "
              "bias."},
         ]},

        {"type": "content", "label": "Face-to-Face &amp; CAPI", "title": "The South Asian workhorse",
         "blocks": [
             {"t": "body", "html": "Most rigorous development surveys in South Asia still rely "
              "on <strong>face-to-face</strong> interviews, increasingly via "
              "<strong>CAPI</strong> &mdash; computer-assisted personal interviewing &mdash; on "
              "a tablet or phone running KoboToolbox, ODK or SurveyCTO."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Strengths", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Reaches low-literacy &amp; offline areas",
                      "Long, complex instruments possible",
                      "Built-in skips &amp; range checks",
                      "Direct measurement (height, weight, GPS)"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Costs", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Expensive &mdash; travel &amp; staff",
                      "Slow to field at scale",
                      "Interviewer effects &amp; bias",
                      "Device &amp; charging logistics"]}]}]},
         ]},

        {"type": "content", "label": "Phone &amp; IVR", "title": "Fast and cheap &mdash; but who picks up?",
         "blocks": [
             {"t": "body", "html": "<strong>Phone</strong> surveys and <strong>IVR</strong> "
              "(interactive voice response, automated calls) are cheap, fast and safe in a "
              "crisis &mdash; widely used during COVID-19. But they must be short, and they "
              "systematically miss people without phones."},
             {"t": "hbox", "color": "red", "html": "In rural South Asia, phone ownership skews "
              "male, younger, richer and more urban. A phone frame quietly excludes the poorest "
              "women in the remotest places &mdash; precisely those many programmes target."},
         ]},

        {"type": "content", "label": "Web", "title": "Cheapest reach, narrowest coverage",
         "blocks": [
             {"t": "body", "html": "<strong>Web</strong> surveys cost almost nothing to send to "
              "thousands and allow rich self-completion of sensitive items. But for general "
              "populations in South Asia, internet access is far from universal &mdash; coverage "
              "error is severe."},
             {"t": "hbox", "color": "amber", "html": "Web works well for connected, literate "
              "audiences &mdash; staff, professionals, urban youth. It badly misrepresents the "
              "general public, especially the poor and elderly."},
         ]},

        {"type": "content", "label": "Trade-Offs", "title": "Four modes, four profiles",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Mode", "Cost", "Coverage", "Length", "Best for"],
              "rows": [
                  ["Face-to-face / CAPI", "High", "Broadest", "Long", "Rigorous, rural, complex"],
                  ["Phone / IVR", "Low", "Phone owners", "Short", "Speed, crises, monitoring"],
                  ["Web", "Lowest", "Connected only", "Medium", "Staff &amp; literate audiences"],
                  ["Self-completion", "Medium", "Literate", "Medium", "Sensitive topics"]]},
             {"t": "hbox", "color": "cyan", "html": "There is no best mode &mdash; only the "
              "right trade-off for your population, budget, topic and timeline. Match the mode "
              "to the people you must reach."},
         ]},

        {"type": "content", "label": "Coverage By Mode", "title": "Which mode reaches whom",
         "blocks": [
             {"t": "chart", "canvas": "modeCoverageChart",
              "title": "Illustrative: share of a rural population reachable, by mode",
              "source": "Illustrative pattern for rural South Asia",
              "type": "bar",
              "data": {"labels": ["Face-to-face", "Phone / IVR", "Web"],
                       "datasets": [{"label": "Reachable population (illustrative %)",
                                     "data": [95, 65, 30],
                                     "backgroundColor": ["#10B981", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'Reachable (illustrative %)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative, not measured &mdash; but the "
              "pattern is real: as cost falls, coverage narrows. Cheaper modes systematically "
              "shed the hardest-to-reach."},
         ]},

        {"type": "content", "label": "Mode Effects", "title": "The same question, a different answer",
         "blocks": [
             {"t": "term", "word": "Mode effect",
              "def": "A systematic difference in responses caused purely by the mode of "
              "administration &mdash; for example, people report stigmatised behaviour more "
              "honestly to a screen than to a human interviewer's face."},
             {"t": "hbox", "color": "red", "html": "This wrecks comparability. If round one was "
              "face-to-face and round two was by phone, an apparent change may be a mode effect, "
              "not real. Hold the mode constant across rounds wherever you can."},
         ]},

        {"type": "content", "label": "Mixed Mode", "title": "Combining modes &mdash; carefully",
         "blocks": [
             {"t": "body", "html": "<strong>Mixed-mode</strong> designs (web first, phone "
              "follow-up, face-to-face for refusers) can boost response and cut cost. But they "
              "blend the modes' different biases, so disentangling real change from mode effects "
              "gets harder."},
             {"t": "hbox", "color": "cyan", "html": "If you mix modes, record the mode for every "
              "response so you can test and adjust for mode effects in analysis &mdash; never "
              "leave it invisible."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Translation &amp; Cultural Adaptation"},

        {"type": "content", "label": "Multilingual Reality", "title": "South Asia is not monolingual",
         "blocks": [
             {"t": "body", "html": "A survey in Bihar may need Hindi, Maithili, Bhojpuri and "
              "Urdu; one across India, a dozen languages and scripts. The instrument respondents "
              "actually hear is the <strong>translated</strong> one &mdash; so translation "
              "<em>is</em> instrument design, not an afterthought."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "22", "label": "languages in the Eighth Schedule of India's Constitution",
                  "color": "cyan"},
                 {"num": "100+", "label": "languages with substantial speaker bases", "color": "indigo"},
                 {"num": "1", "label": "instrument must mean the same thing in all of them",
                  "color": "green"}]},
         ]},

        {"type": "content", "label": "Equivalence Is The Goal", "title": "Translate meaning, not just words",
         "blocks": [
             {"t": "body", "html": "A literally correct translation can still measure something "
              "different. The aim is <strong>conceptual equivalence</strong> &mdash; the "
              "translated question evokes the <em>same</em> concept, with the same difficulty "
              "and connotations, as the original."},
             {"t": "hbox", "color": "amber", "html": "&lsquo;Do you feel empowered?&rsquo; has no "
              "clean equivalent in many languages. Adapt to a locally meaningful idea (&lsquo;Can "
              "you decide this on your own?&rsquo;) rather than translating the abstract word."},
         ]},

        {"type": "content", "label": "Back-Translation", "title": "The standard quality check",
         "blocks": [
             {"t": "term", "word": "Back-translation",
              "def": "One translator renders the source into the target language; an independent "
              "second translator, blind to the original, translates it back. Comparing the "
              "back-translation to the original surfaces meaning lost or shifted."},
             {"t": "flow", "steps": [
                 "SOURCE: English question",
                 "FORWARD: translate to Hindi (translator A)",
                 "BACK: Hindi &rarr; English (translator B, blind)",
                 "RECONCILE: compare, fix discrepancies"]},
         ]},

        {"type": "content", "label": "Beyond Back-Translation", "title": "Committee &amp; team approaches",
         "blocks": [
             {"t": "body", "html": "Back-translation catches literal errors but can miss "
              "awkwardness and cultural misfit. A <strong>committee or team approach</strong> "
              "&mdash; bilingual experts, translators and field staff reviewing together &mdash; "
              "produces more natural, usable wording."},
             {"t": "hbox", "color": "green", "html": "Best practice combines both: forward "
              "translation, expert committee review, back-translation, then cognitive testing "
              "with real speakers of the target language."},
         ]},

        {"type": "content", "label": "Local Categories", "title": "Use categories people recognise",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Imported", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Western occupation lists, &lsquo;nuclear vs "
                   "extended family&rsquo;, or income bands that ignore how people are actually "
                   "paid (daily wage, in kind, seasonal)."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Local", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Categories drawn from how the community "
                   "describes work, household and kinship &mdash; refined during pretesting in "
                   "each setting."}]}]},
             {"t": "hbox", "color": "amber", "html": "Caste, kinship and livelihood categories "
              "vary enormously across regions. A code list that fits Tamil Nadu may be "
              "meaningless in Assam."},
         ]},

        {"type": "content", "label": "Units &amp; Measures", "title": "Ask in units people use",
         "blocks": [
             {"t": "bullets", "items": [
                 "Land in <strong>local units</strong> (bigha, katha, acre) &mdash; then convert",
                 "Time by the <strong>agricultural or festival calendar</strong>, not just dates",
                 "Quantities in market units (a <em>seer</em>, a <em>tin</em>, a bundle)",
                 "Money as it is actually earned &mdash; daily, weekly, per task, in kind"]},
             {"t": "hbox", "color": "cyan", "html": "Forcing respondents to convert into "
              "unfamiliar units in their heads adds error. Capture the local unit, record the "
              "conversion factor, and convert later in analysis."},
         ]},

        {"type": "content", "label": "Calendars &amp; Anchors", "title": "Anchor recall in the local year",
         "blocks": [
             {"t": "body", "html": "&lsquo;In the last 12 months&rsquo; is abstract; "
              "&lsquo;since last Diwali&rsquo; or &lsquo;since the kharif harvest&rsquo; is "
              "vivid. A <strong>local events calendar</strong> built into the instrument sharpens "
              "recall and aligns reference periods across respondents."},
             {"t": "hbox", "color": "green", "html": "Build the calendar of festivals, harvests "
              "and landmark local events with field staff <em>before</em> fieldwork &mdash; it "
              "is one of the cheapest accuracy gains available."},
         ]},

        {"type": "content", "label": "Adapt, Then Standardise", "title": "Same concept, locally clothed",
         "blocks": [
             {"t": "body", "html": "The discipline is to adapt the <em>wording, examples and "
              "units</em> to each setting while holding the <em>concept and the indicator</em> "
              "identical. That is what keeps a multilingual survey both locally meaningful and "
              "nationally comparable."},
             {"t": "quote", "text": "Translate the meaning, standardise the measurement. Lose "
              "either and the comparison collapses.",
              "attr": "&mdash; a cross-cultural survey principle"},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Pretesting, Piloting &amp; Fieldwork Quality"},

        {"type": "content", "label": "Test Before You Trust", "title": "No instrument is ready on the first draft",
         "blocks": [
             {"t": "body", "html": "Between &lsquo;finished&rsquo; questionnaire and real "
              "fieldwork sit two distinct checks: <strong>pretesting</strong> (do the questions "
              "work?) and <strong>piloting</strong> (does the whole operation work?). Skipping "
              "them is the most expensive false economy in survey work."},
             {"t": "flow", "steps": [
                 "PRETEST: cognitive interviews on the questions",
                 "REVISE: fix wording, options, routing",
                 "PILOT: a dry run of the whole operation",
                 "FINALISE: lock the instrument &amp; protocol"]},
         ]},

        {"type": "content", "label": "Cognitive Interviews", "title": "Find out how respondents actually think",
         "blocks": [
             {"t": "term", "word": "Cognitive interviewing",
              "def": "A pretesting method where a few respondents answer questions while "
              "thinking aloud, and the interviewer probes how they understood the words, "
              "recalled the facts, and chose their answer."},
             {"t": "hbox", "color": "cyan", "html": "It reveals what a draft cannot: that "
              "&lsquo;household&rsquo; means different things to different people, that a recall "
              "window is impossible, that an option everyone needs is missing. A dozen good "
              "cognitive interviews save a thousand bad responses."},
         ]},

        {"type": "content", "label": "The Pilot", "title": "Rehearse the entire operation",
         "blocks": [
             {"t": "bullets", "items": [
                 "Run the <strong>full instrument</strong> end-to-end in real conditions",
                 "Time it &mdash; is the interview length tolerable?",
                 "Test the <strong>CAPI routing</strong>, GPS, and data sync",
                 "Check logistics: travel, access, consent, refusal handling",
                 "Review the pilot data: are variables populating as expected?"]},
             {"t": "hbox", "color": "green", "html": "The pilot tests the <em>system</em>, not "
              "just the questions: sampling, fieldwork, devices, supervision and data flow, all "
              "at once, before they fail at scale."},
         ]},

        {"type": "content", "label": "Enumerator Training", "title": "Your data is collected by people",
         "blocks": [
             {"t": "body", "html": "However good the instrument, it is administered by "
              "enumerators. <strong>Standardised training</strong> &mdash; on the questions, the "
              "skips, neutral probing, consent and edge cases &mdash; is what makes 'the same "
              "question asked the same way' actually true in the field."},
             {"t": "bullets", "sm": True, "color": "indigo", "items": [
                 "Read every question verbatim &mdash; no improvised paraphrase",
                 "Probe neutrally; never suggest an answer",
                 "Handle &lsquo;don't know&rsquo; and refusals correctly",
                 "Practice with role-plays and mock interviews before going live"]},
         ]},

        {"type": "content", "label": "Interviewer Effects", "title": "Who asks can change the answer",
         "blocks": [
             {"t": "term", "word": "Interviewer effects",
              "def": "Systematic differences in responses arising from the interviewer &mdash; "
              "their gender, caste, manner, or subtle cues &mdash; rather than from the "
              "respondent's true situation."},
             {"t": "hbox", "color": "amber", "html": "On gender-based violence or reproductive "
              "health, a woman enumerator usually elicits franker answers from women. Match "
              "interviewer characteristics to the topic, and standardise manner through training."},
         ]},

        {"type": "content", "label": "Social Desirability", "title": "People answer how they think they should",
         "blocks": [
             {"t": "term", "word": "Social-desirability bias",
              "def": "The tendency to give answers that present the respondent favourably &mdash; "
              "over-reporting good behaviour (hand-washing, school attendance) and under-reporting "
              "the stigmatised (drinking, violence, open defecation)."},
             {"t": "bullets", "sm": True, "items": [
                 "Normalise: &ldquo;Many people&hellip;&rdquo; before a sensitive item",
                 "Use private self-completion for stigmatised topics",
                 "Assure confidentiality &mdash; and mean it",
                 "Ask about behaviour, not identity, where possible"]},
         ]},

        {"type": "content", "label": "Back-Checks", "title": "Verify the fieldwork while it happens",
         "blocks": [
             {"t": "body", "html": "Supervisors re-contact a sample of respondents "
              "(<strong>back-checks</strong>) and observe live interviews "
              "(<strong>spot-checks</strong>) to confirm the interview happened, key answers "
              "match, and protocol was followed &mdash; catching error and fabrication early."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Back-check", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Re-ask a few stable questions by phone or "
                   "revisit; compare to the original to detect errors or faked interviews."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Spot-check", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A supervisor sits in on live interviews to "
                   "observe technique, neutrality and consent in real time."}]}]},
         ]},

        {"type": "content", "label": "Non-Response", "title": "Chase response &mdash; and study the refusers",
         "blocks": [
             {"t": "body", "html": "<strong>Non-response</strong> &mdash; refusals, "
              "not-at-homes, ineligibles &mdash; bites hardest when those who don't answer "
              "<em>differ</em> from those who do. The poorest, the busiest and the most private "
              "are often the hardest to reach, biasing the result."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Make repeat visits at different times of day",
                 "Track and report the <strong>response rate</strong> honestly",
                 "Compare responders to the frame to test for bias",
                 "Adjust with weights &mdash; but weights can't fully cure deep non-response"]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Ethics, Data &amp; Practice"},

        {"type": "content", "label": "Behind Every Row", "title": "Every respondent is a person, not a data point",
         "blocks": [
             {"t": "body", "html": "In a survey, each row is someone who gave you their time and "
              "trust &mdash; often a poor, busy, over-surveyed person with little power over how "
              "their answers are used. Survey ethics is respect made operational, not a "
              "compliance form."},
             {"t": "quote", "text": "The respondent owes you nothing. Everything they give, they "
              "give as a gift &mdash; treat it like one.",
              "attr": "&mdash; a field ethics principle"},
         ]},

        {"type": "content", "label": "Informed Consent", "title": "Consent is the floor, not a formality",
         "blocks": [
             {"t": "bullets", "items": [
                 "State plainly <strong>what</strong> you collect and <strong>why</strong>",
                 "Explain how it will be stored, used, shared, and for how long",
                 "Make clear they may <strong>refuse or stop</strong>, with no penalty",
                 "Deliver it in a language and form they genuinely understand"]},
             {"t": "hbox", "color": "amber", "html": "A thumbprint on an unexplained form is not "
              "consent. For children and other vulnerable respondents, extra safeguards and "
              "guardian consent apply."},
         ]},

        {"type": "content", "label": "Data Protection &amp; DPDP", "title": "India's data law reaches your survey",
         "blocks": [
             {"t": "body", "html": "The <strong>Digital Personal Data Protection Act, 2023</strong> "
              "sets duties for anyone handling personal digital data in India &mdash; including "
              "NGOs and researchers running CAPI surveys on tablets and phones."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Collect only what you need, for a stated purpose (purpose limitation)",
                 "Obtain free, informed, specific consent",
                 "Protect data with reasonable security safeguards",
                 "Stronger protections for children's data"]},
             {"t": "hbox", "color": "amber", "html": "&lsquo;We're a small NGO&rsquo; is not an "
              "exemption. Know your obligations <em>before</em> the first interview, not after a "
              "breach."},
         ]},

        {"type": "content", "label": "Keep It Safe", "title": "Anonymisation is harder than deleting names",
         "blocks": [
             {"t": "body", "html": "Removing names is not enough. Village + age + caste + "
              "occupation can <strong>re-identify</strong> one person in a small area. Survey "
              "data needs deliberate de-identification, encryption and access control &mdash; "
              "especially with GPS coordinates attached."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Direct IDs", "label": "Name, Aadhaar, phone, GPS &mdash; separate &amp; protect",
                  "color": "red"},
                 {"num": "Quasi-IDs", "label": "Age + place + caste can re-identify &mdash; "
                  "aggregate or coarsen", "color": "amber"}]},
         ]},

        {"type": "content", "label": "From Survey To Data", "title": "Design for clean data, then document it",
         "blocks": [
             {"t": "body", "html": "A good instrument hands the analyst clean, well-named data. "
              "Build validation into the CAPI form, keep the raw export untouched, and ship a "
              "<strong>data dictionary</strong> so every variable, code and unit is "
              "self-explanatory months later."},
             {"t": "hbox", "color": "green", "html": "A survey is not done when fieldwork ends. "
              "It is done when someone else can open your documented dataset and understand "
              "exactly what every column means and how it was made."},
         ]},

        {"type": "content", "label": "The Tools", "title": "Software for modern field surveys",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "Good for", "Note"],
              "rows": [
                  ["KoboToolbox", "Humanitarian &amp; NGO CAPI", "Free, offline, widely used"],
                  ["ODK (Open Data Kit)", "Open-source mobile collection", "Free, flexible, technical"],
                  ["SurveyCTO", "Rigorous research surveys", "Paid; strong quality controls"],
                  ["Survey Solutions", "Large official surveys", "Free (World Bank)"]]},
             {"t": "hbox", "color": "cyan", "html": "All build skip logic, range checks and "
              "offline collection into the instrument &mdash; turning design discipline into "
              "fewer field errors. Tools matter less than the design habits behind them."},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "A short, serious reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Survey Methodology</em> &mdash; Groves, Fowler, Couper et al. (the TSE bible)",
                 "<em>Survey Research Methods</em> &mdash; Floyd J. Fowler (concise, practical)",
                 "<em>Improving Survey Questions</em> &mdash; Floyd J. Fowler (question design)",
                 "<em>Asking Questions</em> &mdash; Bradburn, Sudman &amp; Wansink",
                 "DIME / J-PAL / IPA field guides &mdash; practical survey toolkits"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy 101</strong>, <strong>Qualitative Methods</strong> and "
              "<strong>Research Ethics</strong> courses for the full toolkit."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember six things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Start from the decision</strong> &mdash; objectives before questions",
                 "<strong>One question, one idea</strong> &mdash; clear, specific, neutral",
                 "<strong>The questionnaire is the measurement</strong> &mdash; wording is data",
                 "<strong>Manage total survey error</strong> &mdash; not just sample size",
                 "<strong>Pretest, pilot, back-check</strong> &mdash; never trust a first draft",
                 "<strong>Behind every row is a person</strong> &mdash; consent and care"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Survey Design 101 &middot; Complete",
         "headline": "Now go design<br>a survey worth answering.",
         "byline": "A trustworthy survey is built, not improvised &mdash; from the decision it "
                   "serves to the last back-check in the field. Explore the rest of the "
                   "ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
