# -*- coding: utf-8 -*-
"""
SEL Basics 101 — ImpactMojo 101 Series (native deck spec)
Foundational social and emotional learning for educators in South Asia.
Build: python3 scripts/deck-builder/build.py sel_basics
"""

DECK = {
    "slug": "sel-basics",
    "title": "SEL Basics 101",
    "description": ("SEL Basics 101 — a free foundational course for educators and "
                    "education-programme staff in South Asia. Understand social and emotional "
                    "learning: the CASEL five competencies, the evidence base, classroom "
                    "practice, measurement cautions and how to contextualise SEL for India "
                    "and the region. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "SEL<br>Basics<br>101",
         "sub": "Social &amp; Emotional Learning &mdash; a Foundational Course for Educators "
                "&amp; Education-Programme Staff in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What SEL Is (and Isn't)"},
             {"name": "The Evidence Base for SEL"},
             {"name": "The CASEL Framework"},
             {"name": "Self-Awareness"},
             {"name": "Self-Management"},
             {"name": "Social Awareness"},
             {"name": "Relationship Skills"},
             {"name": "Responsible Decision-Making"},
             {"name": "Implementing SEL"},
             {"name": "Measuring SEL &mdash; with Care"},
             {"name": "SEL in South Asia &amp; India"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What SEL Is (and Isn't)"},

        {"type": "content", "label": "Definition", "title": "Social and emotional learning, defined",
         "blocks": [
             {"t": "body", "html": "Children do not leave their feelings at the classroom door. "
              "<strong>Social and emotional learning (SEL)</strong> is the process through which "
              "young people and adults acquire and apply the knowledge, skills and attitudes to "
              "understand and manage emotions, set goals, show empathy, build relationships and "
              "make responsible decisions."},
             {"t": "term", "word": "Social and emotional learning (SEL)",
              "def": "The process of developing the self-awareness, self-control and "
              "interpersonal skills that are vital for school, work and life success &mdash; "
              "definition adapted from CASEL."},
             {"t": "hbox", "color": "cyan", "html": "SEL is not a separate subject bolted on to a "
              "busy day. It is the human foundation that all other learning is built upon."},
         ]},

        {"type": "content", "label": "The Name", "title": "What does CASEL stand for?",
         "blocks": [
             {"t": "body", "html": "The most widely used SEL framework comes from "
              "<strong>CASEL &mdash; the Collaborative for Academic, Social, and Emotional "
              "Learning</strong>, a US-based organisation founded in 1994 that has shaped how "
              "schools worldwide define and teach these skills."},
             {"t": "hbox", "color": "indigo", "html": "Throughout this course, when we say 'the "
              "five competencies' we mean CASEL's framework. We will meet each one in turn."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "Emotions drive attention, memory and learning",
         "blocks": [
             {"t": "body", "html": "Neuroscience is clear: emotion and cognition are deeply "
              "linked. A child who is anxious, dysregulated or unsafe cannot attend, encode or "
              "recall well. Regulating emotion is a <em>precondition</em> for academic learning, "
              "not a distraction from it."},
             {"t": "flow", "steps": [
                 "FEEL SAFE: a regulated nervous system",
                 "ATTEND: focus is freed for the task",
                 "ENGAGE: relationships make effort worthwhile",
                 "LEARN: cognition can do its work"]},
         ]},

        {"type": "content", "label": "What SEL Is Not", "title": "Clearing up four misconceptions",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Not</strong> therapy or counselling &mdash; it is everyday teaching, for all",
                 "<strong>Not</strong> 'soft' or optional &mdash; it predicts hard outcomes",
                 "<strong>Not</strong> just being nice &mdash; it is a set of teachable skills",
                 "<strong>Not</strong> a Western luxury &mdash; every culture nurtures these capacities"]},
             {"t": "hbox", "color": "amber", "html": "SEL names and structures something good "
              "teachers have always done. It makes the implicit explicit and teachable."},
         ]},

        {"type": "content", "label": "Skills, Not Traits", "title": "These are skills, and skills can be taught",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "The trait myth", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'Some children are just well-behaved; "
                   "others aren't.' This treats emotional skill as fixed and lets schools off "
                   "the hook."}]}],
              "right": [{"t": "panel", "color": "green", "title": "The skills view", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Self-control, empathy and cooperation are "
                   "<em>practised</em> capacities &mdash; like reading or arithmetic, they grow "
                   "with instruction and feedback."}]}]},
             {"t": "hbox", "color": "cyan", "html": "If it can be taught, it can be learned by "
              "<em>every</em> child &mdash; the equity case for SEL begins here."},
         ]},

        {"type": "content", "label": "A Long Lineage", "title": "An old idea with a new name",
         "blocks": [
             {"t": "body", "html": "Educating 'the whole child' &mdash; head, heart and hand "
              "&mdash; runs through Gandhi's Nai Talim, Tagore's Shantiniketan, Aristotle's "
              "ethics and countless Indigenous traditions. SEL is a modern, evidence-based "
              "expression of a very old wisdom."},
             {"t": "quote", "text": "Educating the mind without educating the heart is no "
              "education at all.", "attr": "&mdash; commonly attributed to Aristotle"},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Foundations", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "What SEL is, and the evidence for it",
                      "The CASEL framework and its five competencies",
                      "A slow walk through each competency"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Practice", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Implementing SEL well (the SAFE approach)",
                      "Measuring SEL without doing harm",
                      "Contextualising SEL for South Asia"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Examples are drawn from Indian and South "
              "Asian classrooms &mdash; the settings you actually work in."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Evidence Base for SEL"},

        {"type": "content", "label": "The Landmark Study", "title": "Durlak et al. (2011): the foundational meta-analysis",
         "blocks": [
             {"t": "body", "html": "The most cited evidence for SEL is a meta-analysis by "
              "<strong>Durlak and colleagues (2011)</strong>, which pooled "
              "<strong>213 school-based SEL programmes</strong> involving more than "
              "<strong>270,000 students</strong> from kindergarten to high school."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "213", "label": "school-based SEL programmes pooled", "color": "cyan",
                  "source": "Durlak et al. (2011)"},
                 {"num": "270,000+", "label": "students across the studies", "color": "indigo",
                  "source": "Durlak et al. (2011)"}]},
         ]},

        {"type": "content", "label": "The Headline Finding", "title": "An 11-percentile-point academic gain",
         "blocks": [
             {"t": "body", "html": "In Durlak et al. (2011), students in SEL programmes showed an "
              "<strong>11-percentile-point gain in academic achievement</strong> compared with "
              "control groups &mdash; alongside improved social skills, attitudes and behaviour, "
              "and reduced emotional distress."},
             {"t": "hbox", "color": "green", "html": "Read this carefully: it is an "
              "<em>average</em> effect across many programmes, and it shows that attending to "
              "emotion does not crowd out academics &mdash; it supports them."},
             {"t": "hbox", "color": "amber", "html": "Caution: a percentile-point gain is not the "
              "same as a percentage rise in marks. Attribute the figure to Durlak et al. (2011); "
              "do not inflate it."},
         ]},

        {"type": "content", "label": "Many Outcomes", "title": "SEL touches several outcomes at once",
         "blocks": [
             {"t": "chart", "canvas": "selOutcomesChart",
              "title": "Domains improved by SEL programmes (illustrative, framed on Durlak et al. 2011)",
              "source": "Schematic illustration of meta-analytic findings; magnitudes illustrative",
              "type": "bar",
              "data": {"labels": ["Social &amp; emotional skills", "Attitudes", "Positive behaviour",
                                   "Conduct problems (reduced)", "Emotional distress (reduced)",
                                   "Academic performance"],
                       "datasets": [{"label": "Direction &amp; relative strength (illustrative)",
                                     "data": [9, 7, 6, 6, 5, 4],
                                     "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ display:false } } }"}},
             {"t": "hbox", "color": "red", "html": "The bars show <em>direction and rough "
              "relative strength only</em> &mdash; not precise effect sizes. The real point: SEL "
              "improves multiple domains together."},
         ]},

        {"type": "content", "label": "Beyond Marks", "title": "Behavioural and life outcomes",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Behaviour:</strong> fewer conduct problems, less bullying and aggression",
                 "<strong>Wellbeing:</strong> lower anxiety, depression and emotional distress",
                 "<strong>Belonging:</strong> better relationships and a more positive school climate",
                 "<strong>Long term:</strong> follow-up studies link SEL to better later wellbeing"]},
             {"t": "hbox", "color": "cyan", "html": "SEL is one of the few interventions that "
              "improves how children <em>feel</em>, how they <em>behave</em> and how they "
              "<em>learn</em> &mdash; at the same time."},
         ]},

        {"type": "content", "label": "The Long View", "title": "Effects that show up years later",
         "blocks": [
             {"t": "body", "html": "Longitudinal research (including later work by Taylor, "
              "Durlak and colleagues) finds that the benefits of good SEL programmes "
              "<strong>persist</strong> &mdash; predicting better mental health, relationships "
              "and conduct months and years after the programme ends."},
             {"t": "hbox", "color": "green", "html": "Skills, once built, keep paying off. This is "
              "why early, sustained SEL is more than a feel-good add-on."},
         ]},

        {"type": "content", "label": "A Sound Investment", "title": "The economic case",
         "blocks": [
             {"t": "body", "html": "Cost-benefit studies of SEL programmes have reported "
              "favourable returns &mdash; savings from reduced behavioural problems, grade "
              "repetition and later social costs. The exact ratio varies by programme and "
              "setting."},
             {"t": "hbox", "color": "amber", "html": "Treat specific return-on-investment figures "
              "cautiously and check their source and context before quoting them. The "
              "<em>direction</em> &mdash; SEL tends to pay for itself &mdash; is well supported."},
         ]},

        {"type": "content", "label": "Read Evidence Well", "title": "What the evidence does and doesn't say",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "It does say", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Well-implemented SEL improves outcomes on average",
                      "Quality of implementation matters greatly",
                      "Benefits span skills, behaviour and academics"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "It doesn't say", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "That any SEL label guarantees results",
                      "That one number applies to every context",
                      "That poorly run programmes will work"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Most evidence is from high-income settings. "
              "Promising South Asian studies are growing &mdash; we return to this in Section 11."},
         ]},

        {"type": "content", "label": "A Global Endorsement", "title": "Why SEL has spread worldwide",
         "blocks": [
             {"t": "body", "html": "Because of evidence like this, SEL has moved from the "
              "margins to the mainstream &mdash; adopted by school systems across the US, Europe, "
              "Latin America, Africa and increasingly South Asia, and backed by bodies such as "
              "UNESCO and UNICEF as part of quality education."},
             {"t": "hbox", "color": "cyan", "html": "Global momentum is real, but context still "
              "matters. A programme that worked in one setting must be tested and adapted, not "
              "assumed, in another."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The CASEL Framework"},

        {"type": "content", "label": "The Five", "title": "CASEL's five core competencies",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "1", "label": "Self-awareness", "color": "cyan"},
                 {"num": "2", "label": "Self-management", "color": "green"},
                 {"num": "3", "label": "Social awareness", "color": "indigo"},
                 {"num": "4", "label": "Relationship skills", "color": "amber"},
                 {"num": "5", "label": "Responsible decision-making", "color": "red"}]},
             {"t": "hbox", "color": "cyan", "html": "These five &mdash; defined by CASEL &mdash; "
              "are the backbone of this course. Sections 4 to 8 take one competency each."},
         ]},

        {"type": "content", "label": "See the Five", "title": "The five competencies, at a glance",
         "blocks": [
             {"t": "chart", "canvas": "casel5Radar",
              "title": "CASEL's five core competencies (illustrative balance, not measured data)",
              "source": "CASEL framework; values illustrative for shape only",
              "type": "radar",
              "data": {"labels": ["Self-awareness", "Self-management", "Social awareness",
                                  "Relationship skills", "Responsible decision-making"],
                       "datasets": [{"label": "A balanced SEL profile (illustrative)",
                                     "data": [8, 8, 8, 8, 8],
                                     "borderColor": "#0EA5E9",
                                     "backgroundColor": "rgba(14,165,233,0.15)",
                                     "pointBackgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ r:{ min:0, max:10, ticks:{display:false} } } }"}},
             {"t": "hbox", "color": "amber", "html": "The competencies reinforce one another. "
              "The radar is a memory aid &mdash; the equal values are illustrative, not a "
              "measurement of any real child."},
         ]},

        {"type": "content", "label": "Self vs Others", "title": "Two halves: managing self, navigating others",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Intrapersonal", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Self-awareness &mdash; knowing your inner world",
                      "Self-management &mdash; steering it"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Interpersonal", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Social awareness &mdash; reading others",
                      "Relationship skills &mdash; connecting with them"]}]}]},
             {"t": "hbox", "color": "green", "html": "Responsible decision-making sits at the "
              "centre, drawing on all four to choose well in real situations."},
         ]},

        {"type": "content", "label": "More Than Five", "title": "The CASEL 'wheel': SEL is systemic",
         "blocks": [
             {"t": "body", "html": "CASEL pictures the five competencies at the centre of a "
              "<strong>wheel</strong>, surrounded by four widening settings. SEL is not just "
              "what happens in a child's head &mdash; it is nurtured (or undermined) by the "
              "systems around them."},
             {"t": "flow", "steps": [
                 "CLASSROOMS: SEL instruction &amp; climate",
                 "SCHOOLS: schoolwide culture &amp; policy",
                 "FAMILIES &amp; CAREGIVERS: partnership",
                 "COMMUNITIES: aligned support beyond the gate"]},
         ]},

        {"type": "content", "label": "Classrooms", "title": "The innermost ring: classrooms",
         "blocks": [
             {"t": "body", "html": "Closest to the child is the classroom &mdash; through "
              "<strong>explicit SEL instruction</strong>, supportive teacher-student "
              "relationships and <strong>integration</strong> of SEL into how subjects are "
              "taught."},
             {"t": "hbox", "color": "cyan", "html": "A warm, predictable, participatory classroom "
              "is itself an SEL intervention &mdash; before a single dedicated lesson is taught."},
         ]},

        {"type": "content", "label": "Schools", "title": "The next ring: the whole school",
         "blocks": [
             {"t": "body", "html": "SEL thrives when the <strong>whole school</strong> is aligned "
              "&mdash; in discipline policies, in how staff treat each other, in the morning "
              "assembly, the corridors and the playground, not only in timetabled lessons."},
             {"t": "hbox", "color": "amber", "html": "Mixed signals undo SEL: teaching empathy in "
              "a lesson while running a harsh, punitive discipline system teaches the opposite."},
         ]},

        {"type": "content", "label": "Families", "title": "Families and caregivers as partners",
         "blocks": [
             {"t": "body", "html": "Children's strongest emotional learning happens at home. "
              "When schools <strong>partner</strong> with families &mdash; sharing language, "
              "respecting home cultures, inviting caregivers in &mdash; SEL is reinforced rather "
              "than contradicted."},
             {"t": "hbox", "color": "green", "html": "In many South Asian homes, joint families "
              "and elders are powerful emotional teachers. Build on that, do not bypass it."},
         ]},

        {"type": "content", "label": "Communities", "title": "The outer ring: communities",
         "blocks": [
             {"t": "body", "html": "Community partners &mdash; faith groups, NGOs, sports clubs, "
              "youth programmes, local leaders &mdash; extend SEL beyond the school gate and "
              "anchor it in children's wider lives."},
             {"t": "hbox", "color": "cyan", "html": "The four rings are why SEL is best understood "
              "as a <em>systemic</em> commitment, not a single lesson plan."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Self-Awareness"},

        {"type": "content", "label": "Competency One", "title": "Self-awareness: knowing your inner world",
         "blocks": [
             {"t": "term", "word": "Self-awareness",
              "def": "The ability to understand one's own emotions, thoughts and values, and how "
              "they influence behaviour across contexts &mdash; including accurate "
              "self-perception and a sense of purpose. (CASEL)"},
             {"t": "body", "html": "It is the first competency because you cannot manage, "
              "express or regulate a feeling you cannot first <em>notice and name</em>."},
         ]},

        {"type": "content", "label": "Name to Tame", "title": "Naming emotions calms them",
         "blocks": [
             {"t": "body", "html": "A core SEL practice is building an <strong>emotional "
              "vocabulary</strong>. Children who can say 'I feel frustrated' rather than only "
              "act it out gain a moment of choice between feeling and reaction."},
             {"t": "hbox", "color": "cyan", "html": "'Name it to tame it.' Putting words to "
              "feelings is one of the simplest, most powerful regulation skills &mdash; for "
              "children and teachers alike."},
         ]},

        {"type": "content", "label": "Classroom Practice", "title": "Building an emotional vocabulary",
         "blocks": [
             {"t": "bullets", "items": [
                 "A daily <strong>mood check-in</strong> &mdash; a feelings chart or quick round",
                 "<strong>Feelings words</strong> in the home languages children actually speak",
                 "Teachers <strong>modelling</strong>: 'I felt nervous before this, so I&hellip;'",
                 "Stories and characters as a safe way to discuss emotions"]},
             {"t": "hbox", "color": "amber", "html": "Use the rich emotion words your languages "
              "already hold. English is not the language of feelings for most Indian children."},
         ]},

        {"type": "content", "label": "Strengths", "title": "Knowing strengths, not only deficits",
         "blocks": [
             {"t": "body", "html": "Self-awareness includes recognising one's own "
              "<strong>strengths</strong>, interests and values &mdash; not just problems. A "
              "child who knows what she is good at carries a more resilient sense of self."},
             {"t": "hbox", "color": "green", "html": "Strength-spotting is especially powerful for "
              "children whose schooling tells them mostly what they get <em>wrong</em>."},
         ]},

        {"type": "content", "label": "Growth Mindset", "title": "'I can't do it' &mdash; 'I can't do it yet'",
         "blocks": [
             {"t": "term", "word": "Growth mindset",
              "def": "The belief, developed in Carol Dweck's research, that ability can grow with "
              "effort and good strategies &mdash; as opposed to a fixed mindset that treats it "
              "as innate and unchangeable."},
             {"t": "body", "html": "A growth mindset is part of healthy self-awareness: it shapes "
              "how a child interprets struggle, failure and feedback."},
         ]},

        {"type": "content", "label": "Praise the Process", "title": "How feedback shapes mindset",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Fixed-mindset praise", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'You're so clever!' ties worth to talent "
                   "&mdash; so failure feels like proof of being not-clever."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Growth-mindset praise", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'You worked hard and tried a new strategy!' "
                   "ties worth to effort and method &mdash; which a child can always change."}]}]},
             {"t": "hbox", "color": "amber", "html": "Mindset is not magic. It works alongside "
              "real teaching and fair conditions &mdash; never as a way to blame children for "
              "structural barriers."},
         ]},

        {"type": "content", "label": "Self-Awareness in Adults", "title": "Teachers need it too",
         "blocks": [
             {"t": "body", "html": "A teacher who can notice her own rising frustration has a "
              "choice the unaware teacher does not. Adult self-awareness is the quiet engine of "
              "a calm classroom."},
             {"t": "hbox", "color": "cyan", "html": "We return to teacher SEL in Section 9. For "
              "now: you cannot teach a skill you are not practising yourself."},
         ]},

        {"type": "content", "label": "A Caution", "title": "Self-awareness without judgement",
         "blocks": [
             {"t": "body", "html": "Building self-awareness should never tip into making children "
              "feel there is something wrong with their feelings. The goal is to "
              "<strong>notice and accept</strong> emotions &mdash; all of them &mdash; not to "
              "label some as bad."},
             {"t": "hbox", "color": "amber", "html": "'There are no bad feelings, only feelings "
              "that need understanding.' Anger and sadness are information, not misbehaviour."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Self-Management"},

        {"type": "content", "label": "Competency Two", "title": "Self-management: steering your inner world",
         "blocks": [
             {"t": "term", "word": "Self-management",
              "def": "The ability to manage emotions, thoughts and behaviours effectively across "
              "situations &mdash; including regulating emotions, managing stress, controlling "
              "impulses, and setting and working toward goals. (CASEL)"},
             {"t": "body", "html": "If self-awareness is noticing the feeling, self-management is "
              "<em>choosing what to do</em> with it."},
         ]},

        {"type": "content", "label": "Regulation", "title": "Emotion regulation: from spike to calm",
         "blocks": [
             {"t": "chart", "canvas": "regCurveChart",
              "title": "Emotional arousal over time: with and without regulation skills (illustrative)",
              "source": "Illustrative; arousal on a relative scale",
              "type": "line",
              "data": {"labels": ["Trigger", "+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8"],
                       "datasets": [
                           {"label": "Without regulation skills",
                            "data": [2, 8, 9, 9, 8, 8, 7, 7, 6],
                            "borderColor": "#EF4444", "tension": 0.4, "pointRadius": 0, "fill": False},
                           {"label": "With regulation skills (e.g. breathing, naming)",
                            "data": [2, 8, 6, 4, 3, 2, 2, 1, 1],
                            "borderColor": "#10B981", "tension": 0.4, "pointRadius": 0, "fill": False}]},
              "options": {"__js__": "{ scales:{ y:{ title:{display:true,text:'Arousal (relative)'}, min:0, max:10 } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Regulation does not stop the spike &mdash; it "
              "shortens the recovery. Skills help a child come back to calm faster."},
         ]},

        {"type": "content", "label": "Calming Tools", "title": "Concrete regulation strategies",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Slow breathing</strong> &mdash; longer out-breaths settle the body",
                 "<strong>A pause</strong> &mdash; counting, a sip of water, a step outside",
                 "A <strong>calm-down corner</strong> &mdash; a safe space, not a punishment",
                 "<strong>Naming the feeling</strong> &mdash; the link back to self-awareness"]},
             {"t": "hbox", "color": "amber", "html": "Strategies must be taught and practised when "
              "children are calm &mdash; not introduced for the first time mid-meltdown."},
         ]},

        {"type": "content", "label": "Stress", "title": "Understanding stress &mdash; and toxic stress",
         "blocks": [
             {"t": "body", "html": "Some stress is normal and even helpful. But "
              "<strong>chronic, severe stress</strong> &mdash; from poverty, violence or neglect "
              "&mdash; can overwhelm a child's developing regulation system and harm learning and "
              "health."},
             {"t": "hbox", "color": "red", "html": "Self-management skills help, but they are "
              "<em>not</em> a substitute for safety. A child facing real danger needs protection "
              "first, breathing exercises second."},
         ]},

        {"type": "content", "label": "Impulse Control", "title": "The space between stimulus and response",
         "blocks": [
             {"t": "body", "html": "Self-management grows the <strong>pause</strong> between an "
              "urge and an action &mdash; the space in which choice lives. This is impulse "
              "control, and it strengthens with practice and brain maturation."},
             {"t": "quote", "text": "Between stimulus and response there is a space. In that space "
              "is our power to choose our response.",
              "attr": "&mdash; commonly attributed to Viktor Frankl"},
         ]},

        {"type": "content", "label": "Goals", "title": "Goal-setting: turning hopes into steps",
         "blocks": [
             {"t": "flow", "steps": [
                 "WANT: 'I want to do better in maths'",
                 "SPECIFIC GOAL: 'Practise tables 15 minutes daily'",
                 "PLAN: when, where, with whom",
                 "REVIEW: what worked, what to adjust"]},
             {"t": "hbox", "color": "green", "html": "Goal-setting links emotion to action. It "
              "teaches that effort, planning and persistence &mdash; not just luck &mdash; shape "
              "outcomes."},
         ]},

        {"type": "content", "label": "Delayed Gratification", "title": "Persistence and patience",
         "blocks": [
             {"t": "body", "html": "Working toward a goal means tolerating frustration and "
              "delaying reward &mdash; finishing the hard problem, practising the difficult "
              "passage. SEL builds the stamina that turns intention into achievement."},
             {"t": "hbox", "color": "cyan", "html": "Frame setbacks as information, not verdicts: "
              "'That strategy didn't work &mdash; what will you try next?'"},
         ]},

        {"type": "content", "label": "Self-Management in Class", "title": "Routines that build self-management",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Predictable routines and clear signals reduce the need to self-regulate from scratch",
                 "A visible daily schedule lowers anxiety about what comes next",
                 "Brief movement or breathing breaks reset a restless class",
                 "Co-created class agreements give children ownership of behaviour"]},
             {"t": "hbox", "color": "cyan", "html": "Structure is kindness. A well-ordered "
              "classroom does much of the regulating <em>for</em> children, freeing them to learn."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Social Awareness"},

        {"type": "content", "label": "Competency Three", "title": "Social awareness: reading others",
         "blocks": [
             {"t": "term", "word": "Social awareness",
              "def": "The ability to understand the perspectives of and empathise with others, "
              "including those from diverse backgrounds and cultures, and to recognise social "
              "norms and available supports. (CASEL)"},
             {"t": "body", "html": "If the first two competencies look inward, social awareness "
              "turns outward &mdash; to the feelings, viewpoints and contexts of other people."},
         ]},

        {"type": "content", "label": "Empathy", "title": "What empathy is &mdash; and isn't",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Empathy", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Sensing and understanding what another "
                   "person feels &mdash; 'I can imagine how that felt for you.'"}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Not the same as", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Pity (looking down on), or agreement. You "
                   "can empathise with someone you disagree with."}]}]},
             {"t": "hbox", "color": "green", "html": "Empathy is the emotional root of kindness, "
              "cooperation and the will to reduce others' suffering."},
         ]},

        {"type": "content", "label": "Perspective-Taking", "title": "Seeing through another's eyes",
         "blocks": [
             {"t": "body", "html": "<strong>Perspective-taking</strong> is the cognitive partner "
              "of empathy: actively imagining how a situation looks and feels to someone else, "
              "whose experience differs from your own."},
             {"t": "bullets", "sm": True, "items": [
                 "'How might the new student feel today?'",
                 "Reading a story from a different character's side",
                 "Pausing a conflict to ask each child what they wanted"]},
         ]},

        {"type": "content", "label": "Diversity", "title": "Empathy across difference",
         "blocks": [
             {"t": "body", "html": "Indian classrooms hold immense diversity &mdash; of caste, "
              "religion, language, region, class, ability and gender. Social awareness includes "
              "valuing this difference rather than fearing or ranking it."},
             {"t": "hbox", "color": "amber", "html": "SEL done well actively counters prejudice. "
              "Done carelessly &mdash; ignoring caste or communal realities &mdash; it can paper "
              "over them. Name difference with respect."},
         ]},

        {"type": "content", "label": "Belonging", "title": "Reading the room: norms and belonging",
         "blocks": [
             {"t": "body", "html": "Social awareness also means reading <strong>social norms</strong> "
              "and noticing who is included and who is left out &mdash; the child eating alone, "
              "the one never chosen for a team."},
             {"t": "hbox", "color": "cyan", "html": "A socially aware class notices exclusion and "
              "acts on it. Belonging is not a frill; it is a precondition for learning."},
         ]},

        {"type": "content", "label": "Practising It", "title": "Building social awareness in class",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Cooperative tasks that mix children across groups",
                 "Literature and history from many communities' viewpoints",
                 "Class discussions of fairness, exclusion and kindness",
                 "Service and contact with people unlike oneself"]},
             {"t": "hbox", "color": "cyan", "html": "Contact under fair, cooperative conditions is "
              "one of the most reliable ways to reduce prejudice between groups."},
         ]},

        {"type": "content", "label": "The Empathy-Action Gap", "title": "From feeling to doing",
         "blocks": [
             {"t": "body", "html": "Social awareness matters most when it leads to action. A "
              "child who notices a classmate's distress <em>and acts</em> on it &mdash; a kind "
              "word, an invitation, standing up to unfairness &mdash; turns empathy into "
              "<strong>compassion</strong>."},
             {"t": "hbox", "color": "green", "html": "This is the bridge to the next competency: "
              "awareness of others becomes useful only through the relationship skills that let "
              "a child act."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Relationship Skills"},

        {"type": "content", "label": "Competency Four", "title": "Relationship skills: connecting with others",
         "blocks": [
             {"t": "term", "word": "Relationship skills",
              "def": "The ability to establish and maintain healthy, supportive relationships and "
              "to navigate settings with diverse people &mdash; including communicating clearly, "
              "listening, cooperating and resolving conflict constructively. (CASEL)"},
             {"t": "body", "html": "Awareness of others becomes useful only when a child can "
              "<em>act</em> on it &mdash; that is what relationship skills provide."},
         ]},

        {"type": "content", "label": "Communication", "title": "Clear, respectful communication",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Active listening</strong> &mdash; attending fully, then reflecting back",
                 "<strong>'I' statements</strong> &mdash; 'I felt left out' rather than 'You ignored me'",
                 "Reading tone and body language, not only words",
                 "Asking questions instead of assuming"]},
             {"t": "hbox", "color": "cyan", "html": "Listening is half of communication and the "
              "harder half. Teach it as an active skill, not a default behaviour."},
         ]},

        {"type": "content", "label": "Cooperation", "title": "Working together",
         "blocks": [
             {"t": "body", "html": "Cooperation &mdash; sharing tasks, taking turns, contributing "
              "to a shared goal &mdash; is learned through structured group work, classroom jobs "
              "and play, not exhortation alone."},
             {"t": "hbox", "color": "green", "html": "Design groups so every child has a real "
              "role. 'Group work' where one child does everything teaches the opposite of "
              "cooperation."},
         ]},

        {"type": "content", "label": "Conflict Is Normal", "title": "Conflict resolution, not conflict avoidance",
         "blocks": [
             {"t": "body", "html": "Conflict is inevitable and not, in itself, bad. The SEL goal "
              "is not a conflict-free classroom but children equipped to handle conflict "
              "<strong>constructively</strong>."},
             {"t": "hbox", "color": "amber", "html": "Suppressed conflict festers. Skilled "
              "conflict, openly worked through, builds stronger relationships and deeper "
              "understanding."},
         ]},

        {"type": "content", "label": "A Resolution Process", "title": "A simple conflict-resolution sequence",
         "blocks": [
             {"t": "flow", "steps": [
                 "COOL DOWN: regulate before talking",
                 "EACH SPEAKS: 'I felt&hellip; because&hellip;'",
                 "EACH LISTENS: reflect the other's view back",
                 "SOLVE TOGETHER: find a fair next step"]},
             {"t": "hbox", "color": "cyan", "html": "Notice how this draws on every prior "
              "competency &mdash; regulation, awareness, empathy, communication. SEL is "
              "cumulative."},
         ]},

        {"type": "content", "label": "Peers Helping Peers", "title": "Peer mediation and helping cultures",
         "blocks": [
             {"t": "body", "html": "Many schools train older or trained students as "
              "<strong>peer mediators</strong> who help classmates resolve disputes. This "
              "distributes SEL skills and builds a culture of mutual help."},
             {"t": "hbox", "color": "green", "html": "Children often listen to peers more readily "
              "than to adults. A culture where students support each other multiplies a "
              "teacher's reach."},
         ]},

        {"type": "content", "label": "Bullying", "title": "Healthy relationships counter bullying",
         "blocks": [
             {"t": "body", "html": "Strong relationship skills, empathy and a culture of "
              "belonging are among the most effective protections against "
              "<strong>bullying</strong> &mdash; addressing it at its roots, not just punishing "
              "incidents."},
             {"t": "hbox", "color": "amber", "html": "Bystanders matter most. SEL that empowers "
              "the watching majority to speak up changes a school's climate."},
         ]},

        {"type": "content", "label": "Teacher Relationships", "title": "The relationship that matters most",
         "blocks": [
             {"t": "body", "html": "Of all the relationships in a school, the "
              "<strong>teacher-student bond</strong> is the most powerful lever for learning and "
              "wellbeing. A child who feels known and valued by one caring adult is more "
              "resilient to almost everything else."},
             {"t": "hbox", "color": "cyan", "html": "Before any curriculum: greet children by "
              "name, notice who is struggling, and repair ruptures. Relationship is the "
              "intervention."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Responsible Decision-Making"},

        {"type": "content", "label": "Competency Five", "title": "Responsible decision-making: choosing well",
         "blocks": [
             {"t": "term", "word": "Responsible decision-making",
              "def": "The ability to make caring, constructive choices about personal behaviour "
              "and social interactions across diverse situations &mdash; weighing ethics, "
              "safety, consequences and the wellbeing of self and others. (CASEL)"},
             {"t": "body", "html": "This fifth competency integrates the other four into the act "
              "of <em>choosing</em> in real, often messy, situations."},
         ]},

        {"type": "content", "label": "Ethics", "title": "From rules to reasons",
         "blocks": [
             {"t": "body", "html": "Responsible decision-making moves children beyond 'because I "
              "was told' toward reasoning about <strong>fairness, harm and care</strong> &mdash; "
              "an internal compass, not just external control."},
             {"t": "hbox", "color": "cyan", "html": "The aim is children who do the right thing "
              "when no one is watching &mdash; because they understand <em>why</em> it is right."},
         ]},

        {"type": "content", "label": "Consequences", "title": "Thinking through consequences",
         "blocks": [
             {"t": "body", "html": "A key skill is pausing to ask: <em>what might happen next, "
              "for me and for others?</em> Anticipating consequences turns impulsive reaction "
              "into considered choice."},
             {"t": "flow", "steps": [
                 "STOP: notice the decision point",
                 "OPTIONS: what could I do?",
                 "CONSEQUENCES: who is affected, how?",
                 "CHOOSE &amp; REFLECT: decide, then learn from it"]},
         ]},

        {"type": "content", "label": "Problem-Solving", "title": "A problem-solving frame",
         "blocks": [
             {"t": "bullets", "items": [
                 "Define the problem clearly &mdash; what exactly is wrong?",
                 "Brainstorm several possible solutions, without judging yet",
                 "Weigh each option's likely consequences",
                 "Choose, act, then review how it went"]},
             {"t": "hbox", "color": "green", "html": "Taught explicitly, this frame transfers far "
              "beyond the classroom &mdash; to friendships, family and, later, work and "
              "citizenship."},
         ]},

        {"type": "content", "label": "Real Dilemmas", "title": "Practising on real-ish dilemmas",
         "blocks": [
             {"t": "body", "html": "Children build judgement by discussing age-appropriate "
              "dilemmas: a friend cheating, an unfair rule, an excluded classmate, online "
              "pressure. Discussion &mdash; not lecturing &mdash; is what develops reasoning."},
             {"t": "hbox", "color": "amber", "html": "There is rarely one 'correct' answer. The "
              "learning is in the reasoning, the listening and the weighing of others' "
              "wellbeing."},
         ]},

        {"type": "content", "label": "Agency", "title": "Decision-making as citizenship",
         "blocks": [
             {"t": "body", "html": "Responsible decision-making scales up: from playground choices "
              "to how young people treat the environment, engage with their community and act as "
              "ethical citizens."},
             {"t": "hbox", "color": "cyan", "html": "SEL, at its best, is not about compliance. "
              "It grows thoughtful, caring people who can shape a fairer society."},
         ]},

        {"type": "content", "label": "All Five Together", "title": "Decision-making integrates the whole framework",
         "blocks": [
             {"t": "body", "html": "A single real choice can call on every competency at once: "
              "noticing your anger (self-awareness), calming it (self-management), sensing the "
              "other's hurt (social awareness), talking it through (relationship skills) and "
              "choosing fairly (responsible decision-making)."},
             {"t": "hbox", "color": "green", "html": "This is why the five are a framework, not a "
              "checklist. In life they fire together &mdash; and SEL practice rehearses the whole "
              "ensemble."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Implementing SEL"},

        {"type": "content", "label": "Two Routes", "title": "Explicit instruction and integration",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Explicit SEL", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Dedicated lessons that directly teach a "
                   "skill &mdash; e.g. a 20-minute lesson on naming feelings or resolving "
                   "conflict."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Integrated SEL", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Weaving SEL into ordinary teaching &mdash; "
                   "cooperative maths, empathy through literature, reflection after group "
                   "work."}]}]},
             {"t": "hbox", "color": "amber", "html": "The strongest programmes do "
              "<strong>both</strong>: explicit lessons to build skills, plus integration so "
              "skills are used all day."},
         ]},

        {"type": "content", "label": "The Quality Test", "title": "SAFE: four features of programmes that work",
         "blocks": [
             {"t": "body", "html": "Durlak et al. (2011) found that effective SEL programmes "
              "shared four features, summarised by the acronym <strong>SAFE</strong>."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "S &mdash; Sequenced", "label": "Connected, step-by-step activities that "
                  "build skills", "color": "cyan"},
                 {"num": "A &mdash; Active", "label": "Active forms of learning &mdash; practice, "
                  "not just talk", "color": "green"},
                 {"num": "F &mdash; Focused", "label": "Time set aside specifically for skill "
                  "development", "color": "indigo"},
                 {"num": "E &mdash; Explicit", "label": "Targets specific skills, named clearly", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Why SAFE", "title": "What SAFE really tells us",
         "blocks": [
             {"t": "body", "html": "SAFE is a quality test. Programmes lacking these features "
              "&mdash; a one-off assembly, a poster on a wall, a lecture about kindness &mdash; "
              "tend not to work, however well-intentioned."},
             {"t": "hbox", "color": "red", "html": "When you appraise any SEL resource, ask: is it "
              "Sequenced, Active, Focused and Explicit? If not, expect little."},
         ]},

        {"type": "content", "label": "Whole-School", "title": "The whole-school approach",
         "blocks": [
             {"t": "body", "html": "SEL works best as a <strong>whole-school</strong> commitment "
              "&mdash; shared language across classrooms, supportive discipline policies, leader "
              "buy-in and a climate where adults model the skills too."},
             {"t": "hbox", "color": "amber", "html": "A lone enthusiastic teacher can do good, but "
              "isolated efforts fade. Embedding SEL in school culture is what makes it last."},
         ]},

        {"type": "content", "label": "Fidelity &amp; Dosage", "title": "Implementation quality decides outcomes",
         "blocks": [
             {"t": "chart", "canvas": "fidelityChart",
              "title": "Outcomes by implementation quality (illustrative)",
              "source": "Illustrative; mirrors the well-evidenced pattern that fidelity matters",
              "type": "bar",
              "data": {"labels": ["Poor / partial<br>implementation", "Well-implemented<br>(SAFE, full dosage)"],
                       "datasets": [{"label": "Relative benefit (illustrative)",
                                     "data": [2, 8],
                                     "backgroundColor": ["#EF4444", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ display:false } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Same programme, very different results. "
              "<strong>Fidelity</strong> (following the design) and <strong>dosage</strong> "
              "(enough time) often matter more than which programme you pick. Bars illustrative."},
         ]},

        {"type": "content", "label": "Teacher SEL", "title": "You can't pour from an empty cup",
         "blocks": [
             {"t": "body", "html": "Teachers are the delivery mechanism for SEL &mdash; and their "
              "own stress, regulation and relationships shape the classroom climate. "
              "<strong>Teacher wellbeing and SEL competence</strong> are part of the programme, "
              "not a side issue."},
             {"t": "hbox", "color": "green", "html": "Supporting teachers' own social-emotional "
              "skills improves both their wellbeing and their students' outcomes. Invest in the "
              "adults."},
         ]},

        {"type": "content", "label": "Common Pitfalls", "title": "How SEL implementation goes wrong",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Treating SEL as a one-off event, not an ongoing practice",
                 "Buying a packaged curriculum but skipping teacher training",
                 "Contradicting SEL with harsh, punitive discipline",
                 "Ignoring local language, culture and context"]},
             {"t": "hbox", "color": "amber", "html": "Most SEL failures are implementation "
              "failures, not failures of the idea. Plan for quality from the start."},
         ]},

        {"type": "content", "label": "Start Small", "title": "Starting where you are",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Begin with a daily check-in and a calm classroom routine",
                 "Model the skills yourself, out loud",
                 "Add explicit lessons gradually, then integrate across subjects",
                 "Build toward whole-school and family partnership over time"]},
             {"t": "hbox", "color": "cyan", "html": "You do not need a budget or a branded "
              "programme to begin. Relationships and routines cost nothing and matter most."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Measuring SEL &mdash; with Care"},

        {"type": "content", "label": "Why Measure", "title": "Why measure SEL at all?",
         "blocks": [
             {"t": "body", "html": "Measurement can help teachers understand students, improve "
              "programmes and make the case for investment. But measuring inner skills is far "
              "harder &mdash; and riskier &mdash; than measuring a spelling test."},
             {"t": "hbox", "color": "amber", "html": "This section is as much about <em>cautions</em> "
              "as methods. Bad SEL measurement can do real harm."},
         ]},

        {"type": "content", "label": "The Toolkit", "title": "How SEL is commonly assessed",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Method", "What it captures", "Watch-out"],
              "rows": [
                  ["Student self-report", "How children rate their own skills", "Bias, mood, social desirability"],
                  ["Teacher report", "Observed behaviour over time", "Halo effect, teacher bias"],
                  ["Observation", "Skills in real interactions", "Time-consuming, observer effects"],
                  ["Climate surveys", "Whether the school feels safe &amp; fair", "Indirect; aggregate"]]},
             {"t": "hbox", "color": "cyan", "html": "No single method is sufficient. Triangulate "
              "&mdash; and treat every score as a clue, not a verdict."},
         ]},

        {"type": "content", "label": "Self-Report Limits", "title": "The limits of asking children to rate themselves",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Children may answer how they think they <em>should</em> &mdash; social desirability",
                 "A child who has grown <em>more</em> self-aware may rate herself <em>lower</em>",
                 "Reading level and question wording skew young children's answers",
                 "A snapshot mood is read as a stable trait"]},
             {"t": "hbox", "color": "amber", "html": "Self-report is useful for reflection and "
              "programme feedback &mdash; but a shaky basis for judging individual children."},
         ]},

        {"type": "content", "label": "The Big Caution", "title": "Do not put SEL on a high-stakes test",
         "blocks": [
             {"t": "body", "html": "CASEL and many researchers warn strongly against using SEL "
              "measures for <strong>high-stakes</strong> purposes &mdash; ranking children, "
              "grading teachers, or deciding funding."},
             {"t": "hbox", "color": "red", "html": "High stakes corrupt the measure: people game "
              "it, children learn to give 'right' answers, and a tool meant to help becomes a "
              "tool to judge and exclude."},
         ]},

        {"type": "content", "label": "Goodhart", "title": "When a measure becomes a target",
         "blocks": [
             {"t": "quote", "text": "When a measure becomes a target, it ceases to be a good "
              "measure.", "attr": "&mdash; Goodhart's law, as popularised by Marilyn Strathern"},
             {"t": "body", "html": "Attach rewards or punishments to an SEL score and you change "
              "the very behaviour you are trying to read &mdash; this is especially dangerous for "
              "something as intimate as a child's emotional life."},
         ]},

        {"type": "content", "label": "Equity in Measurement", "title": "Whose 'good behaviour' are we measuring?",
         "blocks": [
             {"t": "body", "html": "SEL measures can carry cultural bias. Norms for "
              "'assertiveness', 'eye contact' or 'self-control' differ across cultures, castes, "
              "genders and neurotypes. A tool can mistake <em>difference</em> for "
              "<em>deficit</em>."},
             {"t": "hbox", "color": "red", "html": "Ask: whose standard of 'competence' is built "
              "into this tool? Measurement must not become a new way to label marginalised "
              "children as lacking."},
         ]},

        {"type": "content", "label": "Measure Responsibly", "title": "Principles for responsible SEL measurement",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Measure to <strong>improve</strong>, never to rank or punish",
                 "Use multiple methods; treat scores as clues, not verdicts",
                 "Check tools for cultural and linguistic fairness",
                 "Protect privacy &mdash; emotional data is sensitive data",
                 "Focus on programmes and climate, not on labelling individuals"]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "SEL in South Asia &amp; India"},

        {"type": "content", "label": "Policy", "title": "NEP 2020 puts emotion on the agenda",
         "blocks": [
             {"t": "body", "html": "India's <strong>National Education Policy 2020</strong> "
              "explicitly emphasises <strong>socio-emotional learning</strong> and the holistic "
              "development of learners &mdash; not just cognitive skills &mdash; placing "
              "wellbeing, values and life skills at the centre of education."},
             {"t": "hbox", "color": "green", "html": "This is a major opening. SEL in India is no "
              "longer a fringe idea &mdash; it is aligned with national policy direction."},
         ]},

        {"type": "content", "label": "On the Ground", "title": "SEL initiatives across the region",
         "blocks": [
             {"t": "bullets", "items": [
                 "State 'Happiness' and life-skills curricula in several Indian states",
                 "NGO and foundation SEL programmes in government schools",
                 "Life-skills and wellbeing modules in many South Asian systems",
                 "Growing teacher-training attention to classroom climate"]},
             {"t": "hbox", "color": "cyan", "html": "Verify specifics locally before citing a "
              "particular scheme &mdash; programmes evolve, and names and reach change over "
              "time."},
         ]},

        {"type": "content", "label": "Don't Just Import", "title": "Contextualisation, not copy-paste",
         "blocks": [
             {"t": "body", "html": "Most SEL curricula were designed in the Global North. "
              "Transplanting them unchanged can misfire &mdash; in language, examples, values and "
              "classroom realities. SEL must be <strong>adapted</strong>, not merely "
              "translated."},
             {"t": "hbox", "color": "amber", "html": "Ask: do the stories, names, dilemmas and "
              "emotion words fit the children in front of you? If not, rebuild them with local "
              "teachers and communities."},
         ]},

        {"type": "content", "label": "Culture", "title": "Individual and collective selves",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Imported framing", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Often centres the individual &mdash; "
                   "'my' feelings, 'my' goals, personal self-expression."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Many South Asian settings", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Centre family, community and "
                   "interdependence &mdash; duty, respect and the collective self."}]}]},
             {"t": "hbox", "color": "green", "html": "Neither is 'more advanced'. Good SEL honours "
              "collective values while still giving each child voice and dignity."},
         ]},

        {"type": "content", "label": "Equity", "title": "SEL and India's inequalities",
         "blocks": [
             {"t": "body", "html": "SEL can either challenge or reinforce inequality. Done well, "
              "it builds belonging across caste, class, religion and gender. Done carelessly, it "
              "can blame marginalised children for 'poor self-control' shaped by injustice."},
             {"t": "hbox", "color": "red", "html": "Never use SEL to pathologise poverty or "
              "difference. A hungry, frightened or excluded child needs justice and safety, not "
              "a lesson in 'grit'."},
         ]},

        {"type": "content", "label": "Trauma-Informed", "title": "Being trauma-informed",
         "blocks": [
             {"t": "body", "html": "Many children in the region face adversity &mdash; poverty, "
              "violence, displacement, loss. A <strong>trauma-informed</strong> approach asks not "
              "'what's wrong with this child?' but <strong>'what has this child been "
              "through?'</strong>"},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Prioritise safety, predictability and trusted relationships",
                 "Recognise that 'misbehaviour' is often a stress response",
                 "Know your limits &mdash; refer serious distress to trained help"]},
         ]},

        {"type": "content", "label": "Language", "title": "Teaching feelings in the mother tongue",
         "blocks": [
             {"t": "body", "html": "Emotions live most vividly in a child's home language. SEL in "
              "an unfamiliar language stays abstract; SEL in the <strong>mother tongue</strong> "
              "&mdash; with local idioms, stories and emotion words &mdash; reaches the heart."},
             {"t": "hbox", "color": "green", "html": "This aligns with NEP 2020's emphasis on "
              "early learning in the mother tongue. Feelings and first language belong together."},
         ]},

        {"type": "content", "label": "Cautions", "title": "Honest cautions for SEL in our context",
         "blocks": [
             {"t": "bullets", "color": "amber", "items": [
                 "Crowded classrooms and exam pressure leave little space &mdash; plan realistically",
                 "Most evidence is from elsewhere; build and share local evidence",
                 "Beware SEL as a buzzword that ticks a box without changing practice",
                 "Protect it from becoming one more thing children are tested and ranked on"]},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Emotions and learning are inseparable</strong> &mdash; SEL supports academics",
                 "<strong>These are teachable skills</strong>, organised by CASEL's five competencies",
                 "<strong>Implementation quality decides outcomes</strong> &mdash; make it SAFE",
                 "<strong>Measure to help, never to rank</strong> or punish",
                 "<strong>Adapt for our context</strong> &mdash; language, culture, equity, care"]},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "Further reading and resources",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<strong>CASEL</strong> (casel.org) &mdash; the framework, the wheel and tools",
                 "Durlak, Weissberg, Dymnicki, Taylor &amp; Schellinger (2011) &mdash; the meta-analysis",
                 "<strong>NEP 2020</strong> &mdash; India's policy on socio-emotional learning",
                 "<em>Permission to Feel</em> &mdash; Marc Brackett (emotional intelligence in schools)",
                 "<em>Mindset</em> &mdash; Carol Dweck (growth mindset)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Child Rights</strong>, <strong>Inclusive Education</strong> and "
              "<strong>Mental Health</strong> 101 courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "SEL Basics 101 &middot; Complete",
         "headline": "Teach the heart,<br>and the mind follows.",
         "byline": "Social and emotional learning is not a luxury or a Western import &mdash; it "
                   "is the human foundation of all good education, and it can be taught in every "
                   "classroom. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Handouts", "href": "https://www.impactmojo.in"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
