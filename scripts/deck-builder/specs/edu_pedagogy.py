# -*- coding: utf-8 -*-
"""
Education and Pedagogy 101 — ImpactMojo 101 Series (native deck spec)
Foundational pedagogy for educators and education-programme staff in South Asia.
Build: python3 scripts/deck-builder/build.py edu_pedagogy
"""

DECK = {
    "slug": "edu-pedagogy",
    "title": "Education and Pedagogy 101",
    "description": ("Education and Pedagogy 101 — a free foundational course for educators and "
                    "education-programme staff in South Asia. From how learning works and Bloom's "
                    "taxonomy to constructivist and inclusive practice, assessment, foundational "
                    "literacy and numeracy, Teaching at the Right Level, Freire's critical pedagogy "
                    "and India's learning crisis. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Education<br>&amp; Pedagogy<br>101",
         "sub": "How Learning Works &amp; How to Teach Well &mdash; a Foundational Course for "
                "Educators &amp; Education-Programme Staff in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Pedagogy Is"},
             {"name": "How Learning Works"},
             {"name": "Bloom's Taxonomy"},
             {"name": "Constructivist &amp; Child-Centred Pedagogy"},
             {"name": "Assessment"},
             {"name": "Foundational Literacy &amp; Numeracy"},
             {"name": "Inclusive &amp; Equitable Pedagogy"},
             {"name": "Effective Classroom Practice"},
             {"name": "Pedagogy of the Oppressed"},
             {"name": "The Learning Crisis &amp; India"},
             {"name": "Teacher Development &amp; Practice"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Pedagogy Is"},

        {"type": "content", "label": "Definition", "title": "Pedagogy is the art &amp; science of teaching",
         "blocks": [
             {"t": "body", "html": "Teaching is not just knowing your subject and saying it aloud. "
              "<strong>Pedagogy</strong> is the deliberate craft of helping others learn &mdash; the "
              "choices a teacher makes about how to present ideas, organise a class, ask questions and "
              "respond to learners. It is part evidence, part judgement, part art."},
             {"t": "term", "word": "Pedagogy",
              "def": "The method and practice of teaching &mdash; how learning is designed, "
              "facilitated and sustained. From the Greek <em>paidagogos</em>, the slave who led a "
              "child to school. Today it means the whole craft of helping people learn."},
             {"t": "hbox", "color": "cyan", "html": "Two teachers can cover the same chapter from the "
              "same textbook and produce completely different learning. The difference is pedagogy."},
         ]},

        {"type": "content", "label": "Three Words", "title": "Pedagogy vs curriculum vs andragogy",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Curriculum", "label": "WHAT is taught &mdash; the content, syllabus, "
                  "sequence and goals", "color": "indigo"},
                 {"num": "Pedagogy", "label": "HOW it is taught &mdash; the methods and the "
                  "teacher-learner relationship", "color": "cyan"},
                 {"num": "Andragogy", "label": "How ADULTS learn &mdash; self-directed, experience-"
                  "based, problem-centred", "color": "amber"}]},
             {"t": "hbox", "color": "green", "html": "A strong curriculum taught with weak pedagogy "
              "still fails learners. The two are partners &mdash; the <em>what</em> and the "
              "<em>how</em> &mdash; not substitutes."},
         ]},

        {"type": "content", "label": "Pedagogy &amp; Andragogy", "title": "Children and adults do not learn the same way",
         "blocks": [
             {"t": "table",
              "head": ["", "Pedagogy (children)", "Andragogy (adults)"],
              "rows": [
                  ["Motivation", "Often external &mdash; marks, approval", "Internal &mdash; relevance to life"],
                  ["Role of teacher", "Directs and structures", "Facilitates and guides"],
                  ["Experience", "Limited &mdash; teacher supplies it", "Rich &mdash; a resource to draw on"],
                  ["Orientation", "Subject-centred", "Problem- &amp; task-centred"]]},
             {"t": "hbox", "color": "amber", "html": "Malcolm Knowles popularised <em>andragogy</em>. "
              "The line between the two is softer than it looks &mdash; even children learn best when "
              "the work feels relevant and they have some agency."},
         ]},

        {"type": "content", "label": "More Than Delivery", "title": "Teaching is a relationship, not a transmission",
         "blocks": [
             {"t": "body", "html": "The oldest picture of teaching is a jug pouring knowledge into an "
              "empty vessel. Modern pedagogy rejects it: learners are not empty, and minds are not "
              "filled by pouring. Learning happens <em>inside</em> the learner, who actively builds "
              "understanding."},
             {"t": "quote", "text": "Education is not the filling of a pail, but the lighting of a fire.",
              "attr": "&mdash; commonly attributed to W. B. Yeats"},
         ]},

        {"type": "content", "label": "The Teacher's Choices", "title": "Pedagogy is a thousand small decisions",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>How do I open?</strong> Hook curiosity, or recap prior learning?",
                 "<strong>How do I explain?</strong> Tell, show, ask, or let them try?",
                 "<strong>How do I check?</strong> One bright child's hand, or every learner?",
                 "<strong>How do I respond?</strong> Correct, or probe the thinking behind the error?",
                 "<strong>How do I group?</strong> Whole class, pairs, levels, or mixed ability?"]},
             {"t": "hbox", "color": "cyan", "html": "Each choice has evidence behind it. This course "
              "is about making those choices well, on purpose."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "The teacher is the largest in-school factor",
         "blocks": [
             {"t": "body", "html": "Decades of research agree on one thing: after a child's own "
              "background, the <strong>quality of teaching</strong> is the most powerful in-school "
              "influence on learning. Not buildings, not class size, not technology &mdash; the "
              "teacher and what they do."},
             {"t": "hbox", "color": "green", "html": "This is good news for an under-resourced system. "
              "Better pedagogy needs better practice more than it needs more money &mdash; and "
              "practice can be learned."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Foundations", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "How learning works in the mind",
                      "Bloom's taxonomy &amp; objectives",
                      "Constructivist, child-centred teaching",
                      "Assessment that helps learning"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Practice &amp; context", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Foundational literacy &amp; numeracy",
                      "Inclusive, equitable classrooms",
                      "Freire &amp; critical pedagogy",
                      "India's learning crisis &amp; NEP 2020"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Throughout, examples come from Indian classrooms "
              "and the wider region &mdash; the realities you actually work in."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "How Learning Works"},

        {"type": "content", "label": "Three Big Theories", "title": "How do we think learning happens?",
         "blocks": [
             {"t": "body", "html": "A century of research has produced three great families of "
              "learning theory. Each captures something true; good teachers draw on all three "
              "depending on the task."},
             {"t": "flow", "steps": [
                 "BEHAVIOURISM: learning as changed behaviour",
                 "COGNITIVISM: learning as mental processing",
                 "CONSTRUCTIVISM: learning as building understanding"]},
         ]},

        {"type": "content", "label": "Behaviourism", "title": "Learning as a change in behaviour",
         "blocks": [
             {"t": "body", "html": "<strong>Behaviourism</strong> (Pavlov, Skinner) sees learning as "
              "the formation of stimulus&ndash;response links, shaped by reinforcement. Reward a "
              "behaviour and it recurs; ignore it and it fades. The mind is a 'black box'."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Where it helps", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Drilling number facts, spelling, routines, "
                   "praise for effort, clear consequences. Useful for automaticity."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Where it falls short", "blocks": [
                  {"t": "body", "cls": "sm", "html": "It ignores understanding and meaning. Rote "
                   "reward can produce parroting without comprehension."}]}]},
         ]},

        {"type": "content", "label": "Cognitivism", "title": "Learning as processing in the mind",
         "blocks": [
             {"t": "body", "html": "<strong>Cognitivism</strong> opens the black box. It studies "
              "attention, memory and how information is encoded, stored and retrieved. Learning is "
              "what happens when new information connects to what is already in the mind."},
             {"t": "term", "word": "Working memory",
              "def": "The small, temporary store where we hold and manipulate information in the "
              "moment. It is easily overloaded &mdash; which is why we break ideas into steps and "
              "do not present ten new things at once."},
         ]},

        {"type": "content", "label": "Cognitive Load", "title": "Don't overload the working memory",
         "blocks": [
             {"t": "body", "html": "Working memory can hold only a few items at once. Cram a lesson "
              "with new vocabulary, a new procedure and a noisy room, and learning stalls &mdash; not "
              "because children are slow, but because the channel is full."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Break new content into small, sequenced steps",
                 "Connect the new to the already-known (prior knowledge)",
                 "Use worked examples before independent practice",
                 "Strip away clutter that competes for attention"]},
         ]},

        {"type": "content", "label": "Constructivism", "title": "Learners build their own understanding",
         "blocks": [
             {"t": "body", "html": "<strong>Constructivism</strong> holds that learners actively "
              "<em>construct</em> knowledge by making sense of new experience in the light of what "
              "they already believe. Understanding is built, not received."},
             {"t": "term", "word": "Constructivism",
              "def": "The view that knowledge is actively built by the learner, not passively "
              "absorbed. New ideas are integrated with, or made to revise, existing mental models "
              "(schemas)."},
             {"t": "hbox", "color": "amber", "html": "This is why misconceptions are so stubborn: a "
              "child fits new information into an old, wrong model. Good teaching surfaces and "
              "rebuilds that model, not just adds facts on top."},
         ]},

        {"type": "content", "label": "Piaget", "title": "Piaget: children think differently at different ages",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "<strong>Jean Piaget</strong> showed that children are not "
              "miniature adults &mdash; they pass through <em>stages</em> of cognitive development, "
              "each with its own way of reasoning."},
             {"t": "table",
              "head": ["Stage", "Roughly", "Hallmark"],
              "rows": [
                  ["Sensorimotor", "0&ndash;2 yrs", "Learning through senses &amp; movement"],
                  ["Pre-operational", "2&ndash;7 yrs", "Symbols &amp; language; not yet logical"],
                  ["Concrete operational", "7&ndash;11 yrs", "Logic about concrete, real things"],
                  ["Formal operational", "11+ yrs", "Abstract &amp; hypothetical reasoning"]]},
             {"t": "hbox", "color": "cyan", "html": "Practical lesson: young children need concrete, "
              "hands-on materials before abstract symbols. Stages are guides, not rigid timetables."},
         ]},

        {"type": "content", "label": "Vygotsky", "title": "Vygotsky: learning is social before it is individual",
         "blocks": [
             {"t": "body", "html": "<strong>Lev Vygotsky</strong> argued that children learn first "
              "<em>with others</em> &mdash; through talk, guidance and culture &mdash; and only later "
              "internalise that thinking on their own. Learning is social before it is solo."},
             {"t": "term", "word": "Zone of Proximal Development (ZPD)",
              "def": "The gap between what a learner can do alone and what they can do with help from "
              "a more capable other. Teaching is most powerful when it works inside this zone &mdash; "
              "just beyond independent reach."},
         ]},

        {"type": "content", "label": "Scaffolding", "title": "Scaffolding: support that is gradually removed",
         "blocks": [
             {"t": "body", "html": "<strong>Scaffolding</strong> is the temporary support a teacher "
              "gives a learner working in the ZPD &mdash; a hint, a worked example, a sentence "
              "starter, a peer partner. As the learner gains confidence, the support is withdrawn."},
             {"t": "flow", "steps": [
                 "I DO: teacher models the task",
                 "WE DO: teacher &amp; learners do it together",
                 "YOU DO TOGETHER: peers practise in pairs",
                 "YOU DO: learner works independently"]},
             {"t": "hbox", "color": "green", "html": "Like scaffolding on a building, it is meant to "
              "come down. Support that never fades creates dependence, not learning."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Bloom's Taxonomy"},

        {"type": "content", "label": "The Idea", "title": "Not all thinking is the same depth",
         "blocks": [
             {"t": "body", "html": "Reciting a date and evaluating a historical argument are both "
              "'knowing history' &mdash; but they demand very different thinking. <strong>Bloom's "
              "taxonomy</strong> orders cognitive tasks from simple to complex, giving teachers a "
              "ladder to plan and stretch learning."},
             {"t": "term", "word": "Taxonomy",
              "def": "A classification scheme. Benjamin Bloom's 1956 framework classified educational "
              "objectives; a 2001 revision by Anderson &amp; Krathwohl updated it into the six "
              "levels used today."},
         ]},

        {"type": "content", "label": "The Six Levels", "title": "Bloom's revised cognitive levels",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0">'
                 '<svg viewBox="0 0 460 300" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:560px;height:auto">'
                 '<polygon points="230,18 300,66 160,66" fill="#EF4444"/>'
                 '<polygon points="160,66 300,66 330,114 130,114" fill="#F59E0B"/>'
                 '<polygon points="130,114 330,114 360,162 100,162" fill="#6366F1"/>'
                 '<polygon points="100,162 360,162 390,210 70,210" fill="#0EA5E9"/>'
                 '<polygon points="70,210 390,210 415,258 45,258" fill="#10B981"/>'
                 '<polygon points="45,258 415,258 440,296 20,296" fill="#334155"/>'
                 '<text x="230" y="52" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="sans-serif">Create</text>'
                 '<text x="230" y="98" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="sans-serif">Evaluate</text>'
                 '<text x="230" y="146" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="sans-serif">Analyse</text>'
                 '<text x="230" y="194" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="sans-serif">Apply</text>'
                 '<text x="230" y="242" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="sans-serif">Understand</text>'
                 '<text x="230" y="284" fill="#fff" font-size="13" font-weight="700" text-anchor="middle" font-family="sans-serif">Remember</text>'
                 '</svg></div>')},
             {"t": "hbox", "color": "amber", "html": "The order, lowest to highest: <strong>Remember "
              "&rarr; Understand &rarr; Apply &rarr; Analyse &rarr; Evaluate &rarr; Create.</strong> "
              "Higher levels build on lower ones, but a good lesson visits many levels."},
         ]},

        {"type": "content", "label": "Lower Order", "title": "Remember, Understand, Apply",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Level", "The learner can&hellip;", "Verbs"],
              "rows": [
                  ["Remember", "Recall facts &amp; basic concepts", "list, name, define, recall"],
                  ["Understand", "Explain ideas in their own words", "explain, summarise, classify"],
                  ["Apply", "Use knowledge in a new situation", "use, solve, demonstrate, compute"]]},
             {"t": "hbox", "color": "cyan", "html": "These are essential foundations &mdash; you "
              "cannot analyse what you cannot recall. The problem is stopping here, which much rote "
              "schooling does."},
         ]},

        {"type": "content", "label": "Higher Order", "title": "Analyse, Evaluate, Create",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Level", "The learner can&hellip;", "Verbs"],
              "rows": [
                  ["Analyse", "Break apart, see relationships", "compare, contrast, examine"],
                  ["Evaluate", "Judge using criteria &amp; evidence", "judge, critique, justify"],
                  ["Create", "Combine parts into something new", "design, compose, plan, invent"]]},
             {"t": "hbox", "color": "green", "html": "Higher-order thinking is where deep, transferable "
              "learning lives. Most exam questions in our system sit stubbornly at the bottom two "
              "levels &mdash; testing recall, not reasoning."},
         ]},

        {"type": "content", "label": "Why Teachers Use It", "title": "Bloom as a planning tool",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Plan</strong> lessons that climb beyond recall to reasoning",
                 "<strong>Question</strong> at varied levels &mdash; not just 'what' but 'why' and 'what if'",
                 "<strong>Write objectives</strong> with precise, observable verbs",
                 "<strong>Design assessments</strong> that test understanding, not memory alone"]},
             {"t": "hbox", "color": "amber", "html": "A simple discipline: for every topic, ask one "
              "question from each level. It instantly raises the cognitive demand of a lesson."},
         ]},

        {"type": "content", "label": "Objectives", "title": "Writing a good learning objective",
         "blocks": [
             {"t": "body", "html": "A <strong>learning objective</strong> states what learners will be "
              "able to <em>do</em> by the end of a lesson &mdash; observable and checkable. Avoid "
              "vague verbs like 'know' or 'understand'; use Bloom's action verbs."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Weak", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'Students will understand fractions.' &mdash; "
                   "How would you ever see it? Not measurable."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Strong", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'Students will <em>compare</em> two fractions "
                   "and <em>explain</em> which is larger.' &mdash; Observable, checkable."}]}]},
         ]},

        {"type": "content", "label": "SMART &amp; ABCD", "title": "Anatomy of an objective",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Audience", "label": "WHO &mdash; 'Grade 4 learners will&hellip;'", "color": "cyan"},
                 {"num": "Behaviour", "label": "WHAT (action verb) &mdash; 'will solve&hellip;'", "color": "green"},
                 {"num": "Condition", "label": "GIVEN WHAT &mdash; 'using a number line&hellip;'", "color": "indigo"},
                 {"num": "Degree", "label": "HOW WELL &mdash; '4 out of 5 correctly'", "color": "amber"}]},
             {"t": "hbox", "color": "cyan", "html": "The ABCD frame keeps objectives concrete. If you "
              "cannot picture a learner doing it, the objective needs sharpening."},
         ]},

        {"type": "content", "label": "Beyond the Cognitive", "title": "Three domains of learning",
         "blocks": [
             {"t": "body", "html": "Bloom and colleagues described three domains. Schooling obsesses "
              "over the first and neglects the others &mdash; yet attitudes and skills shape lives "
              "just as much as knowledge."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Cognitive", "label": "Thinking &amp; knowledge (the famous six levels)", "color": "cyan"},
                 {"num": "Affective", "label": "Attitudes, values, feelings, motivation", "color": "amber"},
                 {"num": "Psychomotor", "label": "Physical skills &mdash; writing, tools, craft", "color": "green"}]},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Constructivist &amp; Child-Centred Pedagogy"},

        {"type": "content", "label": "The Shift", "title": "From teacher-centred to learner-centred",
         "blocks": [
             {"t": "table",
              "head": ["", "Teacher-centred", "Learner-centred"],
              "rows": [
                  ["Teacher is", "Sage on the stage", "Guide on the side"],
                  ["Learners are", "Passive listeners", "Active doers"],
                  ["Talk", "Mostly teacher", "Mostly learners"],
                  ["Errors are", "Failures to punish", "Information to use"]]},
             {"t": "hbox", "color": "cyan", "html": "This is not chaos or 'no teaching'. The "
              "learner-centred teacher works harder &mdash; designing tasks, posing questions and "
              "guiding thinking, instead of simply talking."},
         ]},

        {"type": "content", "label": "Active Learning", "title": "We learn by doing, not by watching",
         "blocks": [
             {"t": "body", "html": "<strong>Active learning</strong> puts learners to work: "
              "discussing, solving, building, explaining, predicting. Passive listening produces "
              "fragile knowledge; active engagement builds durable understanding."},
             {"t": "quote", "text": "Tell me and I forget, teach me and I may remember, involve me "
              "and I learn.",
              "attr": "&mdash; commonly attributed to Benjamin Franklin"},
         ]},

        {"type": "content", "label": "Inquiry", "title": "Inquiry-based learning: start with a question",
         "blocks": [
             {"t": "body", "html": "In <strong>inquiry-based learning</strong>, the lesson begins "
              "with a genuine question or problem, and learners investigate to find answers &mdash; "
              "observing, testing, reasoning &mdash; rather than being handed conclusions."},
             {"t": "flow", "steps": [
                 "ASK: a real, puzzling question",
                 "INVESTIGATE: gather &amp; test evidence",
                 "EXPLAIN: build an answer from findings",
                 "REFLECT: what changed in our thinking?"]},
         ]},

        {"type": "content", "label": "Activity-Based", "title": "Activity-Based Learning (ABL)",
         "blocks": [
             {"t": "body", "html": "<strong>Activity-Based Learning</strong> organises the curriculum "
              "into hands-on activities and self-paced cards, letting children learn by doing and "
              "progress at their own speed. Tamil Nadu's ABL reform brought it to scale in government "
              "primary schools."},
             {"t": "hbox", "color": "amber", "html": "ABL's strength is engagement and child agency. "
              "Its risk, seen at scale, is becoming mechanical &mdash; activity for its own sake. The "
              "<em>thinking</em> the activity provokes is what matters, not the activity."},
         ]},

        {"type": "content", "label": "Play", "title": "Play is the work of childhood",
         "blocks": [
             {"t": "body", "html": "For young children, <strong>play</strong> is not a break from "
              "learning &mdash; it <em>is</em> learning. Through play children experiment, take turns, "
              "use language, solve problems and build social and emotional skills."},
             {"t": "hbox", "color": "green", "html": "India's NEP 2020 and the new foundational stage "
              "make <strong>play-based, activity-based learning</strong> the foundation of early "
              "education &mdash; a major shift from early rote and worksheets."},
         ]},

        {"type": "content", "label": "The Teacher's Role", "title": "The teacher as facilitator",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Designs</strong> tasks worth doing, pitched in the ZPD",
                 "<strong>Asks</strong> more than tells &mdash; questions that provoke thinking",
                 "<strong>Listens</strong> to learner reasoning, including the errors",
                 "<strong>Scaffolds</strong> &mdash; just enough help, then steps back",
                 "<strong>Orchestrates</strong> talk among learners, not only with them"]},
             {"t": "hbox", "color": "cyan", "html": "'Guide on the side' does not mean absent. It "
              "means the teacher's expertise goes into <em>designing learning</em>, not just "
              "<em>delivering content</em>."},
         ]},

        {"type": "content", "label": "Constructive Alignment", "title": "Line up goals, teaching and assessment",
         "blocks": [
             {"t": "body", "html": "A coherent lesson aligns three things: the <strong>objective</strong> "
              "(what learners should be able to do), the <strong>activities</strong> (which let them "
              "practise exactly that), and the <strong>assessment</strong> (which checks that very "
              "thing). When they drift apart, teaching wobbles."},
             {"t": "flow", "steps": [
                 "OBJECTIVE: what learners will do",
                 "ACTIVITY: practise that very thing",
                 "ASSESSMENT: check that very thing"]},
         ]},

        {"type": "content", "label": "A Caution", "title": "Discovery alone is not enough",
         "blocks": [
             {"t": "body", "html": "Child-centred does not mean leaving children to discover "
              "everything unaided. For novices, pure unguided discovery is slow and frustrating &mdash; "
              "they lack the prior knowledge to find their way."},
             {"t": "hbox", "color": "red", "html": "The evidence favours <strong>guided</strong> "
              "construction: rich tasks plus clear modelling, worked examples and feedback. Freedom "
              "and structure are partners, not opposites."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Assessment"},

        {"type": "content", "label": "Two Purposes", "title": "Formative vs summative assessment",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Formative", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Assessment <em>for</em> learning &mdash; while "
                   "teaching, to find out what learners know and adjust. Low-stakes, frequent, "
                   "feedback-rich."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Summative", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Assessment <em>of</em> learning &mdash; after "
                   "teaching, to judge and certify. The exam, the report card, the board result."}]}]},
             {"t": "hbox", "color": "amber", "html": "An analogy: when the cook tastes the soup, that "
              "is formative; when the guest tastes it, that is summative. Our system over-uses the "
              "second and under-uses the first."},
         ]},

        {"type": "content", "label": "AfL", "title": "Assessment FOR learning changes outcomes",
         "blocks": [
             {"t": "body", "html": "<strong>Assessment for learning</strong> is not extra testing &mdash; "
              "it is the steady stream of checks a teacher uses <em>during</em> a lesson to see who "
              "has understood and what to do next. Done well, it is among the most powerful things a "
              "teacher can do."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Share what success looks like, up front",
                 "Use questions and tasks to reveal thinking",
                 "Give feedback that moves learning forward",
                 "Let learners assess themselves and peers"]},
         ]},

        {"type": "content", "label": "Frequency", "title": "Frequent low-stakes checks beat rare high-stakes ones",
         "blocks": [
             {"t": "chart", "canvas": "assessFreqChart",
              "title": "Illustrative: learning gain by assessment pattern",
              "source": "Illustrative &mdash; patterned on formative-assessment research",
              "type": "bar",
              "data": {"labels": ["One big term-end exam", "A few monthly tests",
                                   "Frequent low-stakes checks"],
                       "datasets": [{"label": "Relative learning gain (illustrative)",
                                     "data": [3, 6, 9],
                                     "backgroundColor": ["#EF4444", "#F59E0B", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:10, title:{display:true,text:'Relative gain (illustrative)'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Illustrative pattern only. The research direction "
              "is robust: many small checks that feed back into teaching outperform a single "
              "end-of-term verdict that arrives too late to help anyone."},
         ]},

        {"type": "content", "label": "Checking Everyone", "title": "Check all learners, not the fastest hand",
         "blocks": [
             {"t": "body", "html": "The commonest classroom routine &mdash; teacher asks, one eager "
              "child answers, lesson moves on &mdash; tells you only that <em>one</em> child knows. "
              "The quiet majority remain invisible."},
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Cold call</strong> &amp; no-hands-up &mdash; ask anyone, not volunteers",
                 "<strong>Mini-whiteboards</strong> &mdash; every learner shows an answer at once",
                 "<strong>Think&ndash;pair&ndash;share</strong> &mdash; all rehearse before answering",
                 "<strong>Exit tickets</strong> &mdash; one question, every child, end of class"]},
         ]},

        {"type": "content", "label": "Feedback", "title": "Feedback that moves learning forward",
         "blocks": [
             {"t": "body", "html": "Not all feedback helps. A mark or a grade alone tells a learner "
              "<em>where</em> they are, not <em>how to improve</em>. The most useful feedback is "
              "specific, timely, and about the work &mdash; not the person."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Weak feedback", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'7/10. Be more careful.' &mdash; A grade and a "
                   "scold. The learner has no idea what to change."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Strong feedback", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'Your method is right; you slipped on carrying "
                   "the ten. Redo these two and check.' &mdash; Actionable."}]}]},
         ]},

        {"type": "content", "label": "Effect Sizes", "title": "Feedback among the highest-impact practices",
         "blocks": [
             {"t": "chart", "canvas": "hattieFeedbackChart",
              "title": "Illustrative effect sizes for selected practices (patterned on Hattie's syntheses)",
              "source": "Illustrative &mdash; patterned on John Hattie, Visible Learning",
              "type": "bar",
              "data": {"labels": ["Feedback", "Formative assessment", "Direct instruction",
                                   "Small-group learning", "Reducing class size"],
                       "datasets": [{"label": "Effect size (illustrative)",
                                     "data": [0.7, 0.6, 0.6, 0.5, 0.2],
                                     "backgroundColor": ["#10B981", "#10B981", "#0EA5E9",
                                                         "#0EA5E9", "#F59E0B"]}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:1, title:{display:true,text:'Effect size (d) — illustrative'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative magnitudes only. Hattie's point "
              "stands: well-targeted feedback and formative assessment tend to outperform popular but "
              "costly fixes like cutting class size."},
         ]},

        {"type": "content", "label": "The Trouble With Rote", "title": "Rote learning and the exam machine",
         "blocks": [
             {"t": "body", "html": "Much South Asian schooling rewards memorising and reproducing text "
              "for high-stakes exams. Children can recite without understanding &mdash; and forget "
              "soon after the paper is over. The test drives the teaching, and the teaching narrows "
              "to the test."},
             {"t": "quote", "text": "What gets tested gets taught. If the exam asks only for recall, "
              "the classroom will teach only recall.",
              "attr": "&mdash; a maxim of assessment reform"},
         ]},

        {"type": "content", "label": "Better Exams", "title": "Make summative assessment honest &amp; humane",
         "blocks": [
             {"t": "bullets", "items": [
                 "Test <strong>application and reasoning</strong>, not just recall",
                 "Use <strong>competency-based</strong> items tied to real understanding",
                 "Reduce the stakes of any single high-pressure exam",
                 "Report <strong>what a learner can do</strong>, not just a rank"]},
             {"t": "hbox", "color": "green", "html": "NEP 2020 calls for exactly this shift &mdash; "
              "from rote, high-stakes board exams toward regular, competency-based, formative "
              "assessment that supports learning."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Foundational Literacy &amp; Numeracy"},

        {"type": "content", "label": "The Crisis", "title": "Schooling is not the same as learning",
         "blocks": [
             {"t": "body", "html": "India achieved near-universal primary enrolment &mdash; a real "
              "triumph. But getting children into school did not guarantee they learned. Many "
              "complete several years of schooling without mastering the basics of reading and "
              "arithmetic."},
             {"t": "term", "word": "Foundational Literacy &amp; Numeracy (FLN)",
              "def": "The ability to read with meaning and do basic maths by around Grade 3 &mdash; "
              "the floor on which all later learning is built. Without it, every later subject "
              "becomes a wall."},
         ]},

        {"type": "content", "label": "The Evidence", "title": "ASER: a quiet measure of a loud problem",
         "blocks": [
             {"t": "body", "html": "The <strong>Annual Status of Education Report (ASER)</strong>, run "
              "by the NGO <strong>Pratham</strong>, is a citizen-led household survey that simply asks "
              "children to read a short text and do basic arithmetic. Its consistent finding over "
              "years: a large share of children in upper primary grades cannot yet read a Grade-2 "
              "level text or do simple division."},
             {"t": "hbox", "color": "amber", "html": "Because ASER tests children at home, it reaches "
              "those who are absent or out of school &mdash; not just the ones present on exam day. "
              "That is what makes it so revealing."},
         ]},

        {"type": "content", "label": "The Learning Gap", "title": "Learning lags far behind the grade",
         "blocks": [
             {"t": "chart", "canvas": "aserGapChart",
              "title": "Illustrative: % of children who can read a Grade-2 level text, by grade",
              "source": "Illustrative pattern, in the spirit of ASER (Pratham) findings",
              "type": "bar",
              "data": {"labels": ["Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8"],
                       "datasets": [{"label": "% who can read Grade-2 text (illustrative)",
                                     "data": [27, 38, 50, 58, 66, 72],
                                     "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% of children (illustrative)'} } } }"}},
             {"t": "hbox", "color": "red", "html": "Illustrative shape only &mdash; not exact figures. "
              "The pattern is real and stark: even by Grade 8, a sizeable share of children cannot "
              "fluently read text meant for Grade 2. Learning trails the grade by years."},
         ]},

        {"type": "content", "label": "Why It Compounds", "title": "Why early gaps become permanent",
         "blocks": [
             {"t": "body", "html": "Curriculum and teaching march on at grade level, but many children "
              "fall behind in Grade 1 or 2 and never catch up. Each year the lesson assumes mastery "
              "the child never gained, so the gap widens silently &mdash; until the child stops "
              "understanding almost everything."},
             {"t": "flow", "steps": [
                 "Early gap in reading / number",
                 "Lessons assume mastery the child lacks",
                 "Child understands less each year",
                 "Disengagement, repetition, dropout"]},
         ]},

        {"type": "content", "label": "TaRL", "title": "Teaching at the Right Level (TaRL)",
         "blocks": [
             {"t": "body", "html": "Pratham's response: <strong>Teaching at the Right Level</strong>. "
              "Instead of teaching to the grade, briefly group children by their <em>current</em> "
              "learning level, teach foundational skills with simple activities, and move them up as "
              "they master each step."},
             {"t": "flow", "steps": [
                 "ASSESS each child's actual level (simple tools)",
                 "GROUP by level, not by grade, for a daily block",
                 "TEACH basics with activity-based methods",
                 "TRACK progress &amp; regroup as children advance"]},
         ]},

        {"type": "content", "label": "The Evidence", "title": "TaRL: tested by randomised trials",
         "blocks": [
             {"t": "body", "html": "TaRL is one of the most rigorously evaluated education approaches "
              "in the world. Researchers at <strong>J-PAL</strong> &mdash; co-founded by "
              "<strong>Abhijit Banerjee</strong> and <strong>Esther Duflo</strong> &mdash; ran a "
              "series of randomised controlled trials with Pratham across Indian states."},
             {"t": "hbox", "color": "green", "html": "The finding, repeated across trials: grouping "
              "children by learning level and teaching the basics produces large, cost-effective "
              "gains in reading and arithmetic &mdash; especially for the children furthest behind."},
         ]},

        {"type": "content", "label": "The Mechanism", "title": "Why grouping by level works",
         "blocks": [
             {"t": "chart", "canvas": "tarlChart",
              "title": "Illustrative: share of children who can read words/text, before vs after a TaRL-style block",
              "source": "Illustrative pattern, in the spirit of Pratham / J-PAL TaRL evaluations",
              "type": "bar",
              "data": {"labels": ["Cannot read", "Letters only", "Words", "Paragraph", "Story"],
                       "datasets": [
                           {"label": "Before (illustrative)",
                            "data": [35, 28, 18, 12, 7], "backgroundColor": "#F59E0B"},
                           {"label": "After (illustrative)",
                            "data": [12, 18, 22, 24, 24], "backgroundColor": "#10B981"}]},
              "options": {"__js__": "{ plugins:{legend:{display:true}}, scales:{ y:{ min:0, max:40, title:{display:true,text:'% of children (illustrative)'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Illustrative only. The logic: a child learns when "
              "teaching meets them where they are &mdash; inside the ZPD &mdash; rather than far above "
              "their current level."},
         ]},

        {"type": "content", "label": "Policy", "title": "NIPUN Bharat: FLN as a national mission",
         "blocks": [
             {"t": "body", "html": "In 2021 India launched <strong>NIPUN Bharat</strong> (National "
              "Initiative for Proficiency in Reading with Understanding and Numeracy), a mission under "
              "NEP 2020 to ensure every child attains foundational literacy and numeracy by the end "
              "of Grade 3."},
             {"t": "hbox", "color": "green", "html": "It marks a shift in national priority: from "
              "<em>enrolment and inputs</em> to <em>actual learning of the basics</em> &mdash; the "
              "single highest-leverage goal in Indian school education today."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Inclusive &amp; Equitable Pedagogy"},

        {"type": "content", "label": "The Principle", "title": "Every child can learn &mdash; design for all",
         "blocks": [
             {"t": "body", "html": "Inclusive pedagogy starts from a commitment: the classroom must "
              "work for <em>every</em> learner &mdash; girls and boys, the disabled, first-generation "
              "learners, children of every language, caste and background. Inclusion is not charity; "
              "it is the job."},
             {"t": "quote", "text": "Equity is not treating everyone the same. It is giving each "
              "learner what they need to reach the same goal.",
              "attr": "&mdash; a principle of inclusive education"},
         ]},

        {"type": "content", "label": "UDL", "title": "Universal Design for Learning (UDL)",
         "blocks": [
             {"t": "body", "html": "<strong>Universal Design for Learning</strong> designs lessons "
              "for variability from the start &mdash; like a ramp that helps the wheelchair user and "
              "everyone with a trolley. Offer multiple ways in, rather than retrofitting fixes for "
              "'special' cases."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Engagement", "label": "Multiple ways to spark interest &amp; motivation", "color": "cyan"},
                 {"num": "Representation", "label": "Multiple ways to present information", "color": "indigo"},
                 {"num": "Expression", "label": "Multiple ways for learners to show learning", "color": "green"}]},
         ]},

        {"type": "content", "label": "Language", "title": "Teach first in the mother tongue",
         "blocks": [
             {"t": "body", "html": "A child who does not understand the language of instruction cannot "
              "learn through it. Evidence is strong that early teaching in the <strong>mother tongue "
              "/ home language</strong> builds stronger foundations &mdash; and makes later "
              "second-language learning easier, not harder."},
             {"t": "hbox", "color": "green", "html": "NEP 2020 recommends the home language or mother "
              "tongue as the medium of instruction at least until Grade 5. In multilingual classrooms, "
              "<strong>multilingual pedagogy</strong> uses children's languages as a bridge, not a "
              "barrier."},
         ]},

        {"type": "content", "label": "Gender", "title": "Gender-responsive pedagogy",
         "blocks": [
             {"t": "bullets", "items": [
                 "Call on girls and boys equally &mdash; track your own questioning",
                 "Challenge stereotypes in examples ('the doctor she&hellip;')",
                 "Watch for who dominates group work and materials",
                 "Make the classroom and toilets safe, so girls stay enrolled"]},
             {"t": "hbox", "color": "amber", "html": "Bias is usually unconscious. Studies repeatedly "
              "find teachers calling on boys more and steering girls away from maths and science "
              "&mdash; without ever intending to."},
         ]},

        {"type": "content", "label": "Disability", "title": "Children with disabilities belong in the classroom",
         "blocks": [
             {"t": "body", "html": "India's <strong>RPwD Act, 2016</strong> and NEP 2020 affirm the "
              "right of children with disabilities to inclusive education &mdash; learning alongside "
              "peers, with support, rather than being segregated or excluded."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Reasonable accommodations &mdash; seating, time, format",
                 "Accessible materials &mdash; large print, audio, sign, braille",
                 "Identify and support specific learning difficulties early",
                 "Train teachers; involve special educators and families"]},
         ]},

        {"type": "content", "label": "First-Generation", "title": "First-generation learners need extra bridges",
         "blocks": [
             {"t": "body", "html": "A <strong>first-generation learner</strong> &mdash; the first in "
              "their family to attend school &mdash; cannot get help with homework at home, may lack "
              "books and quiet space, and faces a school culture that assumes knowledge they have not "
              "yet met."},
             {"t": "hbox", "color": "green", "html": "The remedy is not lower expectations but more "
              "scaffolding: explicit teaching of 'how school works', in-class practice instead of "
              "homework-dependence, and warm, high-expectation relationships."},
         ]},

        {"type": "content", "label": "Expectations", "title": "What teachers expect, learners tend to become",
         "blocks": [
             {"t": "body", "html": "The <strong>Pygmalion effect</strong>: when teachers expect more "
              "of a child, they teach, question and encourage differently &mdash; and the child often "
              "rises to it. When they expect less, the opposite happens, frequently along lines of "
              "caste, gender, class and disability."},
             {"t": "hbox", "color": "red", "html": "Low expectations are a silent form of exclusion. "
              "Equity begins with believing &mdash; and demonstrating &mdash; that every child in the "
              "room can learn."},
         ]},

        {"type": "content", "label": "Practical Inclusion", "title": "Small moves, big inclusion",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Seat learners who need support where you can reach them",
                 "Give wait-time &mdash; some learners need seconds longer to answer",
                 "Use peers as tutors &mdash; mixed pairs help both children",
                 "Offer the same goal by more than one route (UDL)",
                 "Notice who is silent, and find a way in for them"]},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Effective Classroom Practice"},

        {"type": "content", "label": "Lesson Shape", "title": "Every lesson has a beginning, middle and end",
         "blocks": [
             {"t": "flow", "steps": [
                 "OPEN: hook &amp; recall prior learning",
                 "MODEL: show the new idea clearly (I do)",
                 "PRACTISE: guided then independent (we / you do)",
                 "CHECK &amp; CLOSE: assess &amp; consolidate"]},
             {"t": "hbox", "color": "cyan", "html": "A predictable structure frees attention for "
              "learning. Children should always know where they are in a lesson and what is expected "
              "of them."},
         ]},

        {"type": "content", "label": "Questioning", "title": "Questioning is the teacher's sharpest tool",
         "blocks": [
             {"t": "bullets", "items": [
                 "Ask <strong>open</strong> questions ('why', 'how', 'what if') not just 'yes/no'",
                 "Give <strong>wait-time</strong> &mdash; 3&ndash;5 silent seconds after asking",
                 "<strong>Probe</strong>: 'How do you know?' 'Can you say more?'",
                 "Distribute questions across <em>all</em> learners, not the keen few",
                 "Welcome wrong answers &mdash; they reveal the thinking to teach"]},
             {"t": "hbox", "color": "amber", "html": "Most teacher questions are low-level recall "
              "answered in under a second. Slowing down and going deeper transforms a lesson."},
         ]},

        {"type": "content", "label": "Time on Task", "title": "Protect time for actual learning",
         "blocks": [
             {"t": "term", "word": "Time on task",
              "def": "The share of class time learners actually spend engaged in learning &mdash; not "
              "waiting, copying titles, settling, or watching the teacher do administration."},
             {"t": "body", "html": "In many classrooms a large slice of the period leaks away to "
              "transitions, discipline and routine. Tightening routines and reducing dead time is one "
              "of the cheapest ways to raise learning."},
         ]},

        {"type": "content", "label": "Management", "title": "Classroom management serves learning",
         "blocks": [
             {"t": "body", "html": "Good <strong>classroom management</strong> is not about control "
              "for its own sake &mdash; it creates the calm, orderly, predictable space in which "
              "learning can happen. The best management is mostly invisible, built on routines and "
              "relationships, not shouting."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Teach routines explicitly, then practise them",
                 "Set clear, consistent, fairly-applied expectations",
                 "Catch and praise good behaviour, not only bad",
                 "Keep the pace brisk &mdash; boredom breeds disruption"]},
         ]},

        {"type": "content", "label": "No Corporal Punishment", "title": "Fear does not teach",
         "blocks": [
             {"t": "body", "html": "Corporal punishment is <strong>banned</strong> in Indian schools "
              "under the RTE Act, 2009. Beyond the law, the evidence is clear: fear and humiliation "
              "damage learning, harm mental health, and drive children out of school."},
             {"t": "hbox", "color": "red", "html": "Discipline through relationship, routine and "
              "engagement &mdash; not through pain or shame. A frightened child is not a learning "
              "child."},
         ]},

        {"type": "content", "label": "Relationships", "title": "Relationships are the foundation of learning",
         "blocks": [
             {"t": "body", "html": "Children learn best from teachers they trust and who they believe "
              "care about them. A warm, respectful <strong>teacher&ndash;student relationship</strong> "
              "is not soft sentiment &mdash; it is a precondition for the risk-taking that learning "
              "requires."},
             {"t": "quote", "text": "Students don't care how much you know until they know how much "
              "you care.",
              "attr": "&mdash; a teaching maxim"},
         ]},

        {"type": "content", "label": "Praise &amp; Mindset", "title": "Praise the effort, build a growth mindset",
         "blocks": [
             {"t": "body", "html": "Carol Dweck's research distinguishes a <strong>fixed mindset</strong> "
              "('I'm just bad at maths') from a <strong>growth mindset</strong> ('I can't do this "
              "<em>yet</em>'). Praising effort and strategy &mdash; not innate 'cleverness' &mdash; "
              "helps learners persist through difficulty."},
             {"t": "hbox", "color": "green", "html": "Subtle but powerful: 'You worked hard on that "
              "method' builds resilience; 'You're so clever' makes children afraid to risk failure."},
         ]},

        {"type": "content", "label": "Putting It Together", "title": "What an effective lesson looks like",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "A clear, shared objective the learners understand",
                 "Brisk pace, little dead time, high time-on-task",
                 "New ideas modelled, then practised with support",
                 "Questions and checks that reach every learner",
                 "Warm, orderly climate built on routine and respect",
                 "A close that consolidates and checks the learning"]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Curriculum &amp; the Pedagogy of the Oppressed"},

        {"type": "content", "label": "Freire", "title": "Paulo Freire and education as freedom",
         "blocks": [
             {"t": "body", "html": "The Brazilian educator <strong>Paulo Freire</strong>, in his 1968 "
              "classic <em>Pedagogy of the Oppressed</em>, argued that education is never neutral: it "
              "either domesticates people to accept the world as it is, or liberates them to question "
              "and change it."},
             {"t": "term", "word": "Critical pedagogy",
              "def": "A tradition, rooted in Freire, that sees teaching as a political act and aims to "
              "help learners read both 'the word and the world' &mdash; to understand and act on the "
              "social conditions of their lives."},
         ]},

        {"type": "content", "label": "The Banking Model", "title": "Freire's critique: the 'banking' model",
         "blocks": [
             {"t": "body", "html": "Freire named the dominant style the <strong>banking model</strong>: "
              "the teacher 'deposits' information into passive students, who 'store' and 'withdraw' it "
              "for exams. Knowledge flows one way; learners are objects, not agents."},
             {"t": "quote", "text": "Education thus becomes an act of depositing, in which the "
              "students are the depositories and the teacher is the depositor.",
              "attr": "&mdash; Paulo Freire, Pedagogy of the Oppressed (1968)"},
         ]},

        {"type": "content", "label": "Problem-Posing", "title": "The alternative: problem-posing education",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Banking", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Teacher deposits, students receive",
                      "Knowledge is fixed &amp; handed down",
                      "Learners memorise &amp; obey",
                      "Reinforces the status quo"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Problem-posing", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Teacher &amp; learners inquire together",
                      "Knowledge is built through dialogue",
                      "Learners question &amp; create",
                      "Opens the world to change"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Note how closely Freire's problem-posing echoes "
              "constructivism &mdash; but with an explicit commitment to justice and agency."},
         ]},

        {"type": "content", "label": "Dialogue", "title": "Dialogue, not monologue",
         "blocks": [
             {"t": "body", "html": "For Freire, genuine education is <strong>dialogue</strong> between "
              "people who both teach and learn. The teacher is no longer the sole authority; learners' "
              "experiences and questions become the curriculum's raw material."},
             {"t": "term", "word": "Conscientisation",
              "def": "Freire's term (conscientiza&ccedil;&atilde;o) for developing a critical "
              "awareness of one's social reality through reflection and action &mdash; learning to "
              "perceive, and challenge, the forces that shape one's life."},
         ]},

        {"type": "content", "label": "Praxis", "title": "Reflection plus action equals praxis",
         "blocks": [
             {"t": "body", "html": "Freire insisted that critical reflection must lead to "
              "<strong>action</strong>, and action be guided by reflection &mdash; together, "
              "<em>praxis</em>. Education that only describes injustice without enabling people to act "
              "is hollow; action without thought is mere activism."},
             {"t": "flow", "steps": [
                 "REFLECT: read the word &amp; the world",
                 "ACT: work to change conditions",
                 "REFLECT again on what changed",
                 "= PRAXIS: an unending cycle"]},
         ]},

        {"type": "content", "label": "Hidden Curriculum", "title": "Schools teach more than the syllabus",
         "blocks": [
             {"t": "term", "word": "Hidden curriculum",
              "def": "The unwritten lessons schools teach through their routines, hierarchies and "
              "norms &mdash; about authority, obedience, competition, gender and whose knowledge "
              "counts &mdash; alongside the official syllabus."},
             {"t": "body", "html": "A child may learn 'equality' from a textbook while learning from "
              "seating, sweeping duties and who gets called on that their caste or gender places them "
              "below others. The hidden curriculum can quietly contradict the stated one."},
         ]},

        {"type": "content", "label": "Whose Knowledge", "title": "Curriculum is a choice about what counts",
         "blocks": [
             {"t": "body", "html": "Every curriculum selects: some knowledge, languages, histories and "
              "heroes are included; others are left out. Those choices carry power. A "
              "<strong>culturally responsive</strong> curriculum sees children's own languages, "
              "communities and knowledge as resources, not deficits."},
             {"t": "hbox", "color": "amber", "html": "Ask of any curriculum: whose stories does it "
              "tell? Whose are missing? Whom does it position as knower, and whom as ignorant?"},
         ]},

        {"type": "content", "label": "Freire Today", "title": "Why Freire still matters in our classrooms",
         "blocks": [
             {"t": "body", "html": "Freire's critique lands hard in a system shaped by rote, "
              "high-stakes exams and steep hierarchies. His call &mdash; treat learners as thinkers "
              "and agents, build knowledge through dialogue, connect learning to their lives &mdash; "
              "is the ethical core beneath every method in this course."},
             {"t": "hbox", "color": "green", "html": "Constructivism tells us <em>how</em> minds build "
              "knowledge. Freire reminds us <em>why</em> it matters: so that learners can read, "
              "question and reshape their world."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "The Learning Crisis &amp; India Context"},

        {"type": "content", "label": "Learning Poverty", "title": "Learning poverty: the global yardstick",
         "blocks": [
             {"t": "term", "word": "Learning poverty",
              "def": "A World Bank measure: the share of 10-year-olds unable to read and understand a "
              "simple text. It captures the gap between being <em>in school</em> and actually "
              "<em>learning</em>."},
             {"t": "body", "html": "Across low- and middle-income countries the share is high &mdash; "
              "and it rose further after pandemic school closures. For India and much of South Asia, "
              "learning poverty is the defining education challenge of our time."},
         ]},

        {"type": "content", "label": "ASER Findings", "title": "What ASER tells us, year after year",
         "blocks": [
             {"t": "bullets", "items": [
                 "Enrolment is near-universal &mdash; the access battle is largely won",
                 "Yet many upper-primary children read far below grade level",
                 "Basic arithmetic &mdash; division, fractions &mdash; lags badly",
                 "Gaps widen by socio-economic status, gender and region"]},
             {"t": "hbox", "color": "amber", "html": "ASER's value is in the <em>trend and the gap</em>, "
              "not a single tidy number. For exact current figures, always cite the latest ASER report "
              "from Pratham directly."},
         ]},

        {"type": "content", "label": "RTE Act", "title": "RTE Act, 2009: the right to education",
         "blocks": [
             {"t": "body", "html": "The <strong>Right to Education (RTE) Act, 2009</strong> made free "
              "and compulsory education a fundamental right for every child aged 6&ndash;14. It set "
              "norms for infrastructure, pupil&ndash;teacher ratios, no detention, no corporal "
              "punishment, and 25% reserved seats for disadvantaged children in private schools."},
             {"t": "hbox", "color": "cyan", "html": "RTE largely solved access and inputs. Its blind "
              "spot &mdash; widely debated &mdash; was <em>learning outcomes</em>: a right to schooling "
              "is not yet a right to learning."},
         ]},

        {"type": "content", "label": "Schooling vs Learning", "title": "Years in school &ne; years of learning",
         "blocks": [
             {"t": "chart", "canvas": "schoolLearnChart",
              "title": "Illustrative: years of schooling vs learning-adjusted years",
              "source": "Illustrative &mdash; concept of the World Bank's Human Capital Index",
              "type": "bar",
              "data": {"labels": ["Years of schooling", "Learning-adjusted years"],
                       "datasets": [{"label": "Years (illustrative)",
                                     "data": [10.2, 7.0],
                                     "backgroundColor": ["#6366F1", "#EF4444"]}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ min:0, max:12, title:{display:true,text:'Years (illustrative)'} } } }"}},
             {"t": "hbox", "color": "red", "html": "Illustrative magnitudes. The World Bank's "
              "learning-adjusted years of schooling discount time spent in school by how little is "
              "actually learned &mdash; the gap between the bars is the learning crisis."},
         ]},

        {"type": "content", "label": "NEP 2020", "title": "National Education Policy 2020",
         "blocks": [
             {"t": "body", "html": "<strong>NEP 2020</strong> is India's first major education policy "
              "in over three decades. It reframes the system around <strong>foundational literacy and "
              "numeracy</strong>, learning outcomes, flexibility and a more holistic, competency-based "
              "approach."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "FLN as the top priority &mdash; via the NIPUN Bharat mission",
                 "New 5+3+3+4 structure, starting with a play-based foundational stage",
                 "Mother-tongue / home-language instruction in early grades",
                 "A shift from rote, high-stakes exams to competency-based assessment"]},
         ]},

        {"type": "content", "label": "NCF", "title": "The National Curriculum Framework (NCF)",
         "blocks": [
             {"t": "body", "html": "The <strong>National Curriculum Framework</strong> translates "
              "policy into curriculum &mdash; what is taught and how, across stages. The NCF for "
              "Foundational Stage (2022) and the new NCF for School Education operationalise NEP "
              "2020's vision of play-based, activity-based, child-centred learning."},
             {"t": "hbox", "color": "green", "html": "Policy (NEP) sets direction; the NCF turns it "
              "into curriculum; textbooks and teachers turn the NCF into classroom practice. Each "
              "step can strengthen or dilute the vision."},
         ]},

        {"type": "content", "label": "From Policy to Practice", "title": "The hardest mile is the last one",
         "blocks": [
             {"t": "body", "html": "Good policy is necessary but not sufficient. NEP 2020, NIPUN "
              "Bharat and the NCF will only change children's lives if they reach the "
              "<strong>classroom</strong> &mdash; through trained, supported, motivated teachers using "
              "the methods in this course."},
             {"t": "hbox", "color": "amber", "html": "The gap between a policy document and a Grade-2 "
              "classroom in a remote block is where most reforms succeed or fail. That gap is closed "
              "by teachers &mdash; which is why teacher development is the last word."},
         ]},

        {"type": "content", "label": "Equity Lens", "title": "The crisis is not evenly shared",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Poorer children, on average, learn less &mdash; the gap compounds with age",
                 "Girls' learning is shaped by safety, chores and early marriage",
                 "Dalit, Adivasi and minority children face exclusion and low expectations",
                 "Rural and remote schools face the steepest teacher and resource gaps"]},
             {"t": "hbox", "color": "cyan", "html": "A learning crisis is also an equity crisis. The "
              "children furthest behind have the most to gain from better pedagogy &mdash; which is "
              "exactly why it matters."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Teacher Development &amp; Practice"},

        {"type": "content", "label": "Reflective Practice", "title": "The teacher who keeps learning",
         "blocks": [
             {"t": "body", "html": "Good teachers are not born; they are <em>made</em> &mdash; "
              "lesson by lesson, through deliberate reflection. <strong>Reflective practice</strong> "
              "means routinely asking what worked, what didn't and why, then changing the next lesson "
              "accordingly."},
             {"t": "flow", "steps": [
                 "PLAN the lesson",
                 "TEACH it",
                 "REFLECT: what did learners actually learn?",
                 "REFINE: change one thing next time"]},
         ]},

        {"type": "content", "label": "Communities of Practice", "title": "Teachers learn best from each other",
         "blocks": [
             {"t": "body", "html": "A <strong>community of practice</strong> is a group of teachers who "
              "learn together &mdash; observing each other, sharing what works, solving problems "
              "jointly. Isolated teachers stagnate; connected teachers improve."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Peer observation &mdash; watch a colleague, swap feedback",
                 "Lesson study &mdash; plan, observe and refine a lesson together",
                 "Block- or cluster-level teacher meetings",
                 "Mentoring of new teachers by experienced ones"]},
         ]},

        {"type": "content", "label": "Useful PD", "title": "What makes teacher training actually work",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Weak PD", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A one-off lecture, far from the classroom, never "
                   "followed up. Teachers nod, return, and change nothing."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Strong PD", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Ongoing, practical, subject-specific, with "
                   "in-class coaching and follow-up. Tied to real lessons teachers will teach."}]}]},
             {"t": "hbox", "color": "amber", "html": "The evidence is consistent: sustained, "
              "classroom-embedded support changes practice; one-shot workshops rarely do."},
         ]},

        {"type": "content", "label": "Teacher Wellbeing", "title": "You cannot pour from an empty cup",
         "blocks": [
             {"t": "body", "html": "Teachers in our system carry large classes, heavy paperwork and "
              "non-teaching duties. Burnout, low morale and absence all hurt learning. Teacher "
              "<strong>wellbeing and motivation</strong> are not soft extras &mdash; they are "
              "conditions for good pedagogy."},
             {"t": "hbox", "color": "green", "html": "Respect, autonomy, manageable workload, support "
              "and recognition do as much for classroom quality as any new method. Sustain the "
              "teacher, and you sustain the learning."},
         ]},

        {"type": "content", "label": "Your First Steps", "title": "Where to start this term",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Write one clear, Bloom-anchored objective per lesson",
                 "Check <em>every</em> learner's understanding, not the keenest hand",
                 "Find each child's level &mdash; teach the basics at the right level",
                 "Replace one lecture with one active task this week",
                 "Reflect after each lesson: what did they <em>actually</em> learn?"]},
             {"t": "hbox", "color": "amber", "html": "Don't try everything at once. Change one habit, "
              "embed it, then add the next. Pedagogy improves the way learning does &mdash; "
              "incrementally and deliberately."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Pedagogy of the Oppressed</em> &mdash; Paulo Freire (education &amp; liberation)",
                 "<em>Mind in Society</em> &mdash; Lev Vygotsky (the social mind &amp; the ZPD)",
                 "<em>Visible Learning</em> &mdash; John Hattie (what works, by effect size)",
                 "<em>Poor Economics</em> &mdash; Banerjee &amp; Duflo (evidence on TaRL &amp; schooling)",
                 "<em>ASER reports</em> &mdash; Pratham (the state of learning, every year)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Foundational Literacy &amp; Numeracy</strong>, <strong>Inclusive Education</strong> "
              "and <strong>Education Policy</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Learning is built, not poured</strong> &mdash; teach for understanding",
                 "<strong>Meet learners where they are</strong> &mdash; the ZPD, the right level",
                 "<strong>Check everyone, give feedback</strong> &mdash; assessment FOR learning",
                 "<strong>Foundations first</strong> &mdash; literacy &amp; numeracy unlock the rest",
                 "<strong>Every child can learn</strong> &mdash; expect it, design for it"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Education &amp; Pedagogy 101 &middot; Complete",
         "headline": "Now go light<br>the fire.",
         "byline": "You don't need a new syllabus to transform a classroom &mdash; you need better "
                   "pedagogy, practised deliberately, one lesson at a time. Explore the rest of the "
                   "ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
