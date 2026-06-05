# -*- coding: utf-8 -*-
"""
Child Development 101 — ImpactMojo 101 Series (native deck spec)
Early childhood development for development & health practitioners in South Asia.
Build: python3 scripts/deck-builder/build.py child_development
"""

DECK = {
    "slug": "child-development",
    "title": "Child Development 101",
    "description": ("Child Development 101 — a free foundational course on early childhood "
                    "development for health and development practitioners in South Asia: the "
                    "first 1,000 days, domains and theories of development, nutrition, health, "
                    "responsive caregiving, the Nurturing Care Framework, adversity, India's ECD "
                    "ecosystem and how to measure it. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Child<br>Development<br>101",
         "sub": "Early Childhood Development &mdash; the First 1,000 Days, the Science of "
                "Growth &amp; What It Takes to Help Every Child Thrive in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "Why Early Childhood Matters"},
             {"name": "Domains of Development"},
             {"name": "Theories of Development"},
             {"name": "Nutrition &amp; the First 1,000 Days"},
             {"name": "Health &amp; Survival"},
             {"name": "Early Learning &amp; Responsive Care"},
             {"name": "The Nurturing Care Framework"},
             {"name": "Risk &amp; Adversity"},
             {"name": "India's ECD Ecosystem"},
             {"name": "Measuring ECD"},
             {"name": "Practice, Equity &amp; Reading"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why Early Childhood Matters"},

        {"type": "content", "label": "Definition", "title": "What we mean by 'child development'",
         "blocks": [
             {"t": "body", "html": "<strong>Early childhood development (ECD)</strong> is the "
              "process by which children, from conception to about age eight, grow in body, brain "
              "and behaviour &mdash; learning to move, think, speak, feel and relate. It is "
              "holistic: the domains develop together, not in isolation."},
             {"t": "term", "word": "Early childhood development (ECD)",
              "def": "The physical, cognitive, language and social-emotional growth of a child in "
              "the earliest years &mdash; shaped by the interaction of genes, nutrition, health, "
              "relationships and environment."},
             {"t": "hbox", "color": "cyan", "html": "ECD is not just 'health' or just 'education'. "
              "It is the whole child, and it begins before birth."},
         ]},

        {"type": "content", "label": "The Window", "title": "The first 1,000 days",
         "blocks": [
             {"t": "body", "html": "From conception to a child's second birthday is roughly "
              "<strong>1,000 days</strong> &mdash; the period of fastest brain growth and the "
              "window in which good nutrition, health and care pay the highest dividends, and in "
              "which damage is hardest to reverse."},
             {"t": "flow", "steps": [
                 "~270 days: pregnancy",
                 "+365 days: first year",
                 "+365 days: second year",
                 "= ~1,000 days that shape a lifetime"]},
             {"t": "hbox", "color": "amber", "html": "The framing is well established in nutrition "
              "and development science: the earliest window is when investment matters most."},
         ]},

        {"type": "content", "label": "Brain Science", "title": "Brain architecture is built, not given",
         "blocks": [
             {"t": "body", "html": "In the early years the brain forms new neural connections at "
              "an extraordinary pace &mdash; far faster than at any later age. Like a house, the "
              "brain is built from the foundation up: sturdy early architecture supports all later "
              "learning; weak foundations are costly to repair."},
             {"t": "hbox", "color": "indigo", "html": "Genes lay the blueprint, but experience "
              "&mdash; nutrition, stimulation, responsive relationships &mdash; does the building. "
              "This is why the early environment is decisive."},
         ]},

        {"type": "content", "label": "Visualising It", "title": "Why neural connections form early",
         "blocks": [
             {"t": "chart", "canvas": "synapseChart",
              "title": "Pace of synapse formation peaks in the earliest years (schematic)",
              "source": "Illustrative, patterned on developmental neuroscience",
              "type": "line",
              "data": {"labels": ["Birth", "1 yr", "2 yr", "3 yr", "5 yr", "8 yr", "12 yr", "Adult"],
                       "datasets": [{"label": "Relative rate of connection-building",
                                     "data": [40, 95, 90, 75, 55, 40, 30, 25],
                                     "borderColor": "#6366F1",
                                     "backgroundColor": "rgba(99,102,241,0.10)",
                                     "fill": True, "tension": 0.4, "pointRadius": 3}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Relative pace'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The shape, not the exact numbers, is the "
              "point: the brain is most malleable when the child is youngest."},
         ]},

        {"type": "content", "label": "The Economics", "title": "High returns to early investment",
         "blocks": [
             {"t": "body", "html": "Economist <strong>James Heckman</strong> showed that "
              "investing in disadvantaged young children yields higher economic and social returns "
              "than equivalent spending later &mdash; through better health, schooling, earnings "
              "and reduced crime. The earlier the investment, the higher the return."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Heckman", "label": "Returns to human-capital investment are highest in "
                  "early childhood", "color": "green", "source": "Heckman (2006, 2008)"},
                 {"num": "Earlier &gt; later", "label": "Remediation in adolescence costs more and "
                  "achieves less", "color": "amber"}]},
             {"t": "hbox", "color": "cyan", "html": "ECD is among the most cost-effective "
              "investments a country can make &mdash; an economic argument, not only a moral one."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "The Heckman logic, step by step",
         "blocks": [
             {"t": "flow", "steps": [
                 "Skills beget skills &mdash; early learning makes later learning easier",
                 "Early gaps widen over time if left unaddressed",
                 "So early investment compounds; late remediation fights an uphill battle",
                 "Conclusion: invest early, especially in disadvantaged children"]},
             {"t": "hbox", "color": "indigo", "html": "This 'dynamic complementarity' is why the "
              "first years are not just one stage among many &mdash; they set the trajectory."},
         ]},

        {"type": "content", "label": "The Stakes", "title": "Millions of children not reaching their potential",
         "blocks": [
             {"t": "body", "html": "Globally, a large share of children under five in low- and "
              "middle-income countries are estimated to be at risk of not reaching their "
              "developmental potential &mdash; chiefly because of poverty, stunting and "
              "inadequate stimulation. South Asia carries a heavy share of this burden."},
             {"t": "hbox", "color": "red", "html": "These are not isolated tragedies but a "
              "population-scale loss of human potential &mdash; and largely preventable. That is "
              "why ECD is a development priority, not a niche concern."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Domains of Development"},

        {"type": "content", "label": "Four Domains", "title": "Development happens on four fronts",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Physical / motor", "label": "Body growth, gross &amp; fine movement", "color": "cyan"},
                 {"num": "Cognitive", "label": "Thinking, memory, problem-solving, attention", "color": "green"},
                 {"num": "Language", "label": "Understanding &amp; using words and communication", "color": "indigo"},
                 {"num": "Social-emotional", "label": "Relationships, feelings, self-regulation", "color": "amber"}]},
             {"t": "hbox", "color": "cyan", "html": "These are useful labels for observation "
              "&mdash; but in a real child they are deeply intertwined."},
         ]},

        {"type": "content", "label": "Physical & Motor", "title": "From rolling over to running",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Gross motor", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Head control, sitting, crawling",
                      "Standing, walking, running",
                      "Climbing, jumping, balance"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Fine motor", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Grasping, transferring objects",
                      "Pincer grip (thumb &amp; finger)",
                      "Scribbling, stacking, self-feeding"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Motor development follows a broad sequence "
              "&mdash; head to toe, centre outward &mdash; but the <em>timing</em> varies "
              "normally from child to child."},
         ]},

        {"type": "content", "label": "Cognitive", "title": "Building a thinking mind",
         "blocks": [
             {"t": "body", "html": "Cognitive development is how children come to understand the "
              "world: paying attention, remembering, sorting and comparing, solving small "
              "problems, and grasping that an object still exists when hidden "
              "(<em>object permanence</em>)."},
             {"t": "hbox", "color": "indigo", "html": "Curiosity is the engine. A child who pours "
              "water from cup to cup again and again is running experiments &mdash; cognition in "
              "action, not mischief."},
         ]},

        {"type": "content", "label": "Language", "title": "From cooing to conversation",
         "blocks": [
             {"t": "flow", "steps": [
                 "Cooing &amp; babbling (first months)",
                 "First words (~around 1 year)",
                 "Word explosion &amp; two-word phrases (toddler)",
                 "Sentences &amp; questions (preschool)"]},
             {"t": "hbox", "color": "cyan", "html": "Language grows on a diet of <strong>talk</strong>. "
              "Children who hear more words, songs and stories &mdash; in any language &mdash; tend "
              "to develop richer vocabulary and stronger early literacy."},
         ]},

        {"type": "content", "label": "Social-Emotional", "title": "Learning to feel, relate and regulate",
         "blocks": [
             {"t": "body", "html": "Social-emotional development covers forming attachments, "
              "reading others' feelings, managing one's own emotions, taking turns and developing "
              "a sense of self. It is the foundation of mental health and later learning."},
             {"t": "term", "word": "Self-regulation",
              "def": "The growing ability to manage attention, emotion and impulse &mdash; to "
              "wait, calm down, focus and persist. It underpins school readiness and lifelong "
              "wellbeing."},
         ]},

        {"type": "content", "label": "Interaction", "title": "The domains do not develop in silos",
         "blocks": [
             {"t": "body", "html": "Real development is interactive. A toddler learning to walk "
              "(motor) explores more (cognitive), names what she finds (language) and shares it "
              "with a caregiver (social-emotional) &mdash; all in one moment."},
             {"t": "hbox", "color": "amber", "html": "This is why a single deficit &mdash; say, "
              "poor nutrition or little stimulation &mdash; ripples across every domain at once. "
              "Holistic problems need holistic responses."},
         ]},

        {"type": "content", "label": "Milestones", "title": "Milestones are a guide, not a deadline",
         "blocks": [
             {"t": "body", "html": "<strong>Developmental milestones</strong> &mdash; sitting, "
              "first words, sharing &mdash; describe what most children do by a certain age. They "
              "help spot children who may need extra support."},
             {"t": "hbox", "color": "red", "html": "But ranges are wide and normal. A milestone "
              "missed by a few weeks is rarely cause for alarm; a persistent, large delay across "
              "domains is a reason to seek assessment."},
         ]},

        {"type": "content", "label": "Nature & Nurture", "title": "Genes and environment, together",
         "blocks": [
             {"t": "body", "html": "Development is never nature <em>or</em> nurture; it is nature "
              "<em>through</em> nurture. Genes set possibilities; nutrition, health, relationships "
              "and stimulation decide which are realised."},
             {"t": "hbox", "color": "green", "html": "The hopeful implication: because so much "
              "depends on environment, so much can be improved by changing it. ECD programmes work "
              "on exactly this lever."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Theories of Development"},

        {"type": "content", "label": "Why Theory", "title": "Theories give us a map",
         "blocks": [
             {"t": "body", "html": "No single theory explains a whole child, but each offers a "
              "lens: how children think, how they learn with others, how they bond, and how their "
              "wider world shapes them. Together they guide good practice."},
             {"t": "flow", "steps": [
                 "Piaget: how children think",
                 "Vygotsky: how children learn with others",
                 "Bowlby &amp; Ainsworth: how children bond",
                 "Bronfenbrenner: how the environment shapes children"]},
         ]},

        {"type": "content", "label": "Piaget", "title": "Piaget: children build understanding in stages",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Stage", "Approx. age", "Hallmark"],
              "rows": [
                  ["Sensorimotor", "0&ndash;2 yrs", "Learning through senses &amp; action; object permanence"],
                  ["Preoperational", "2&ndash;7 yrs", "Symbols, language, pretend play; egocentric thinking"],
                  ["Concrete operational", "7&ndash;11 yrs", "Logical thinking about concrete things; conservation"],
                  ["Formal operational", "11+ yrs", "Abstract &amp; hypothetical reasoning"]]},
             {"t": "hbox", "color": "cyan", "html": "Ages are approximate and stages overlap. "
              "Piaget's key insight endures: children are active builders of knowledge, not empty "
              "vessels to be filled."},
         ]},

        {"type": "content", "label": "Piaget in Practice", "title": "What Piaget means for caregivers",
         "blocks": [
             {"t": "bullets", "items": [
                 "Young children learn by <strong>doing</strong> &mdash; touching, pouring, "
                 "stacking, exploring",
                 "Hands-on, concrete experiences beat abstract instruction",
                 "Mistakes are how children test and revise their understanding",
                 "Match activities to the child's stage, not just their age in years"]},
         ]},

        {"type": "content", "label": "Vygotsky", "title": "Vygotsky: learning is social",
         "blocks": [
             {"t": "body", "html": "Lev Vygotsky argued that children learn through interaction "
              "with more capable others &mdash; parents, siblings, teachers &mdash; and through "
              "culture and language. Thinking is social before it is individual."},
             {"t": "term", "word": "Zone of Proximal Development (ZPD)",
              "def": "The gap between what a child can do alone and what they can do with help. "
              "Learning happens best in this zone &mdash; challenging, but reachable with support."},
         ]},

        {"type": "content", "label": "Scaffolding", "title": "Scaffolding: support that fades",
         "blocks": [
             {"t": "body", "html": "<strong>Scaffolding</strong> is the help an adult gives within "
              "the ZPD &mdash; a hint, a demonstration, a guiding question &mdash; then gradually "
              "withdraws as the child masters the task, like removing scaffolding from a finished "
              "building."},
             {"t": "hbox", "color": "green", "html": "Practical for any caregiver: do it "
              "<em>with</em> the child, not <em>for</em> the child. Offer just enough help to keep "
              "them succeeding, then step back."},
         ]},

        {"type": "content", "label": "Attachment", "title": "Bowlby & Ainsworth: the power of bonds",
         "blocks": [
             {"t": "body", "html": "John Bowlby proposed that infants are biologically primed to "
              "form a close bond &mdash; <strong>attachment</strong> &mdash; with a primary "
              "caregiver, and that this bond is the secure base from which they explore the world."},
             {"t": "term", "word": "Secure base",
              "def": "A trusted caregiver a child can return to for comfort, which paradoxically "
              "gives the child the confidence to venture out and explore."},
         ]},

        {"type": "content", "label": "Attachment Styles", "title": "Ainsworth's 'Strange Situation'",
         "blocks": [
             {"t": "body", "html": "Mary Ainsworth's classic studies identified patterns of "
              "attachment based on how infants responded to brief separations from and reunions "
              "with a caregiver."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Secure:</strong> distressed at separation, comforted at reunion &mdash; "
                 "the most adaptive pattern",
                 "<strong>Insecure-avoidant:</strong> appears to ignore the caregiver",
                 "<strong>Insecure-ambivalent:</strong> distressed and hard to soothe",
                 "(Later work added a <strong>disorganised</strong> pattern)"]},
             {"t": "hbox", "color": "amber", "html": "Responsive, consistent caregiving fosters "
              "secure attachment &mdash; a foundation for emotional health."},
         ]},

        {"type": "content", "label": "Bronfenbrenner", "title": "Bronfenbrenner: the child in nested systems",
         "blocks": [
             {"t": "body", "html": "Urie Bronfenbrenner's <strong>ecological systems theory</strong> "
              "places the child at the centre of nested environments, each influencing development "
              "&mdash; from the immediate family out to society and its values."},
             {"t": "flow", "steps": [
                 "Microsystem: family, anganwadi, peers",
                 "Mesosystem: links between those settings",
                 "Exosystem: parent's workplace, local services",
                 "Macrosystem: culture, policy, economy"]},
             {"t": "hbox", "color": "indigo", "html": "The lesson for programmes: you cannot "
              "support a child without supporting the systems around them."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Nutrition &amp; the First 1,000 Days"},

        {"type": "content", "label": "Fuel for Growth", "title": "Nutrition builds the brain and body",
         "blocks": [
             {"t": "body", "html": "Adequate nutrition in pregnancy and the early years is the raw "
              "material for brain and body growth. Deficits in this window can cause lasting harm "
              "to physical growth, cognition and immunity &mdash; harm that later feeding cannot "
              "fully undo."},
             {"t": "hbox", "color": "cyan", "html": "This is why nutrition sits at the heart of "
              "the first-1,000-days agenda &mdash; it is, quite literally, developmental "
              "infrastructure."},
         ]},

        {"type": "content", "label": "Two Faces", "title": "Stunting and wasting are different problems",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Stunting", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Low <strong>height-for-age</strong>. A sign "
                   "of <em>chronic</em> undernutrition &mdash; long-term, often irreversible, "
                   "linked to impaired cognition."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Wasting", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Low <strong>weight-for-height</strong>. A "
                   "sign of <em>acute</em> undernutrition &mdash; recent, dangerous, raises the "
                   "risk of death, but treatable."}]}]},
             {"t": "hbox", "color": "amber", "html": "A child can be stunted, wasted, both, or "
              "neither. Underweight (low weight-for-age) is a third, composite measure."},
         ]},

        {"type": "content", "label": "The Indian Picture", "title": "Stunting has declined but remains high",
         "blocks": [
             {"t": "chart", "canvas": "stuntingTrendChart",
              "title": "Child stunting in India has fallen over successive NFHS rounds (schematic)",
              "source": "Illustrative, patterned on NFHS-3/4/5 directional trend",
              "type": "bar",
              "data": {"labels": ["NFHS-3 (~2005-06)", "NFHS-4 (~2015-16)", "NFHS-5 (~2019-21)"],
                       "datasets": [{"label": "Children under 5 stunted (%)",
                                     "data": [48, 38, 36],
                                     "backgroundColor": ["#EF4444", "#F59E0B", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:55, title:{display:true,text:'% stunted'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Direction is well established: stunting has "
              "declined across rounds yet remains high (around a third of under-fives in NFHS-5). "
              "Treat exact bar values as illustrative."},
         ]},

        {"type": "content", "label": "Breastfeeding", "title": "Exclusive breastfeeding for six months",
         "blocks": [
             {"t": "body", "html": "WHO recommends <strong>early initiation</strong> of "
              "breastfeeding within the first hour, <strong>exclusive breastfeeding</strong> for "
              "the first six months (no water, no other food), and continued breastfeeding "
              "alongside other foods up to two years and beyond."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "First hour", "label": "Initiate breastfeeding early", "color": "cyan"},
                 {"num": "6 months", "label": "Exclusive breastfeeding, no other food or water", "color": "green"},
                 {"num": "2 years +", "label": "Continue alongside complementary foods", "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Complementary Feeding", "title": "After six months: add foods, keep nursing",
         "blocks": [
             {"t": "body", "html": "From six months, breastmilk alone is no longer enough. "
              "<strong>Complementary feeding</strong> introduces safe, soft, nutritious family "
              "foods &mdash; at the right frequency, amount and variety &mdash; while breastfeeding "
              "continues."},
             {"t": "hbox", "color": "red", "html": "The 6&ndash;24 month window is where many "
              "children falter: feeding that is too late, too thin, too infrequent or too "
              "monotonous drives much of the region's stunting."},
         ]},

        {"type": "content", "label": "Micronutrients", "title": "The 'hidden hunger' of micronutrients",
         "blocks": [
             {"t": "body", "html": "A child can eat enough calories yet lack vital "
              "<strong>micronutrients</strong> &mdash; iron, vitamin A, iodine, zinc, folate. "
              "These deficiencies, often invisible, impair growth, immunity and brain development."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Iron:</strong> deficiency causes anaemia, harms cognition",
                 "<strong>Vitamin A:</strong> protects sight and immunity",
                 "<strong>Iodine:</strong> essential for brain development",
                 "<strong>Zinc:</strong> supports growth and recovery from illness"]},
         ]},

        {"type": "content", "label": "Anaemia", "title": "Anaemia: a stubborn South Asian challenge",
         "blocks": [
             {"t": "body", "html": "<strong>Anaemia</strong> &mdash; too few healthy red blood "
              "cells, usually from iron deficiency &mdash; remains very common among young "
              "children and women in India. NFHS-5 found anaemia had <em>not</em> improved, and "
              "in many groups worsened, despite years of programmes."},
             {"t": "hbox", "color": "red", "html": "Anaemia in mothers and children is both a "
              "cause and a consequence of poor development &mdash; sapping energy, learning and, "
              "in pregnancy, raising risks for the next generation."},
         ]},

        {"type": "content", "label": "Maternal Nutrition", "title": "It starts before birth",
         "blocks": [
             {"t": "body", "html": "A child's first 1,000 days begin in the womb. A "
              "well-nourished mother &mdash; with enough iron, folate, calories and rest &mdash; "
              "is the first nutrition programme. Low birth weight, often rooted in maternal "
              "undernutrition, starts many children at a disadvantage."},
             {"t": "hbox", "color": "amber", "html": "Adolescent girls, future mothers, are part "
              "of the 1,000-days story too. Breaking the intergenerational cycle means investing "
              "in their nutrition long before pregnancy."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Health &amp; Survival"},

        {"type": "content", "label": "Survival First", "title": "A child must survive to develop",
         "blocks": [
             {"t": "body", "html": "Development presupposes survival. The early years are also the "
              "most dangerous: most under-five deaths cluster in the first weeks and months of "
              "life, from preventable causes &mdash; prematurity, infection, birth complications, "
              "pneumonia and diarrhoea."},
             {"t": "hbox", "color": "red", "html": "Survival and development are not separate "
              "agendas. The same investments &mdash; nutrition, care, clean environments, health "
              "services &mdash; serve both."},
         ]},

        {"type": "content", "label": "Key Measures", "title": "IMR and U5MR: tracking child survival",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "IMR", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>Infant Mortality Rate</strong> &mdash; "
                   "deaths before age 1 per 1,000 live births. A core indicator of a society's "
                   "health."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "U5MR", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>Under-Five Mortality Rate</strong> "
                   "&mdash; deaths before age 5 per 1,000 live births. Captures the wider toll on "
                   "young children."}]}]},
             {"t": "hbox", "color": "green", "html": "Both have fallen markedly in India over "
              "decades &mdash; a real public-health success &mdash; yet gaps persist across "
              "states, wealth groups and between girls and boys."},
         ]},

        {"type": "content", "label": "Immunisation", "title": "Vaccines: one of the best buys in health",
         "blocks": [
             {"t": "body", "html": "Childhood immunisation protects against diseases that once "
              "killed or disabled millions &mdash; measles, polio, diphtheria, tetanus, pertussis "
              "and more. India's <strong>Universal Immunization Programme</strong> is among the "
              "largest in the world."},
             {"t": "hbox", "color": "cyan", "html": "<strong>Full immunisation</strong> means a "
              "child receives all recommended vaccines on schedule. Mission Indradhanush has "
              "pushed to reach children who were being left out."},
         ]},

        {"type": "content", "label": "Coverage", "title": "Full immunisation coverage has risen",
         "blocks": [
             {"t": "chart", "canvas": "immunChart",
              "title": "Full immunisation among children 12&ndash;23 months, India (schematic)",
              "source": "Illustrative, patterned on NFHS-4 to NFHS-5 direction",
              "type": "bar",
              "data": {"labels": ["NFHS-4 (~2015-16)", "NFHS-5 (~2019-21)"],
                       "datasets": [{"label": "Fully immunised (%)",
                                     "data": [62, 76],
                                     "backgroundColor": ["#F59E0B", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% fully immunised'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Coverage rose between rounds &mdash; the "
              "direction is robust &mdash; but bar values here are illustrative. Pockets of "
              "low coverage remain."},
         ]},

        {"type": "content", "label": "WASH", "title": "Clean water, sanitation and hygiene",
         "blocks": [
             {"t": "body", "html": "<strong>WASH</strong> &mdash; water, sanitation and hygiene "
              "&mdash; is foundational to child health. Dirty water and poor sanitation cause "
              "repeated diarrhoea and infection, which in turn drive undernutrition and stunting."},
             {"t": "hbox", "color": "indigo", "html": "The link runs both ways: a child fighting "
              "constant infection cannot absorb nutrients well. This is why nutrition programmes "
              "increasingly include WASH."},
         ]},

        {"type": "content", "label": "Infection-Nutrition", "title": "The vicious cycle of infection and undernutrition",
         "blocks": [
             {"t": "flow", "steps": [
                 "Poor WASH &rarr; repeated infection",
                 "Infection &rarr; appetite loss &amp; poor absorption",
                 "Undernutrition &rarr; weaker immunity",
                 "Weaker immunity &rarr; more infection (cycle repeats)"]},
             {"t": "hbox", "color": "red", "html": "Breaking this cycle at any point &mdash; "
              "clean water, breastfeeding, immunisation, prompt treatment &mdash; helps the whole "
              "child."},
         ]},

        {"type": "content", "label": "The Frontline", "title": "ASHAs, ANMs and the health system",
         "blocks": [
             {"t": "body", "html": "India's rural health frontline includes the "
              "<strong>ASHA</strong> (Accredited Social Health Activist), the "
              "<strong>ANM</strong> (Auxiliary Nurse Midwife) and the anganwadi worker &mdash; "
              "linking families to immunisation, antenatal care, institutional delivery and "
              "nutrition services."},
             {"t": "hbox", "color": "green", "html": "Much of India's progress on child survival "
              "rides on this last-mile workforce, largely women, often stretched thin."},
         ]},

        {"type": "content", "label": "Health = Development", "title": "Why health and development are inseparable",
         "blocks": [
             {"t": "body", "html": "A healthy child explores, plays and learns; a frequently sick "
              "child cannot. Illness drains the energy and attention that development requires, "
              "and chronic illness or undernutrition can leave lasting cognitive marks."},
             {"t": "hbox", "color": "cyan", "html": "So the case for child health is not only "
              "about preventing death &mdash; it is about protecting every survivor's chance to "
              "thrive."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Early Learning &amp; Responsive Care"},

        {"type": "content", "label": "Beyond Survival", "title": "Children need more than food and vaccines",
         "blocks": [
             {"t": "body", "html": "A child who is fed and healthy still needs "
              "<strong>stimulation</strong> and <strong>responsive relationships</strong> to "
              "develop fully. The brain is built through back-and-forth interaction, not in "
              "isolation."},
             {"t": "hbox", "color": "cyan", "html": "This is the part of ECD most often neglected "
              "&mdash; and the cheapest to fix. It costs little to talk, sing and play with a child."},
         ]},

        {"type": "content", "label": "Serve & Return", "title": "Serve-and-return: the basic unit of learning",
         "blocks": [
             {"t": "body", "html": "When a baby babbles, gestures or cries (a 'serve') and an "
              "adult responds warmly &mdash; with words, eye contact, a touch (a 'return') &mdash; "
              "neural connections strengthen. This <strong>serve-and-return</strong> interaction "
              "is how relationships build the brain."},
             {"t": "flow", "steps": [
                 "Child serves: looks, points, babbles",
                 "Adult returns: responds, names, smiles",
                 "Child serves again &mdash; a conversation",
                 "Repeated thousands of times &rarr; brain architecture"]},
         ]},

        {"type": "content", "label": "Play", "title": "Play is serious developmental work",
         "blocks": [
             {"t": "body", "html": "Play is not a break from learning &mdash; it <em>is</em> "
              "learning. Through play children practise motor skills, language, problem-solving, "
              "cooperation and self-regulation, all at once and with joy."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Free play:</strong> child-led exploration",
                 "<strong>Guided play:</strong> adult gently extends the learning",
                 "<strong>Pretend play:</strong> builds language &amp; perspective-taking",
                 "Everyday objects &mdash; pots, stones, cloth &mdash; make fine toys"]},
         ]},

        {"type": "content", "label": "Talk & Stimulation", "title": "Talk, sing, count, read",
         "blocks": [
             {"t": "body", "html": "Rich early environments are full of <strong>language and "
              "stimulation</strong>: naming objects, telling stories, singing, counting, pointing "
              "things out. None of it requires money &mdash; only time and attention."},
             {"t": "hbox", "color": "green", "html": "A powerful, equity-friendly message for "
              "families: the most important early-learning resource is a responsive adult who "
              "talks and plays &mdash; available in every home."},
         ]},

        {"type": "content", "label": "Responsive Care", "title": "Responsive caregiving, defined",
         "blocks": [
             {"t": "term", "word": "Responsive caregiving",
              "def": "Noticing, understanding and responding promptly and appropriately to a "
              "child's signals &mdash; hunger, distress, curiosity, invitation to play. It is the "
              "engine of secure attachment and early learning."},
             {"t": "hbox", "color": "cyan", "html": "Responsiveness, not perfection, is the goal. "
              "Caregivers who tune in 'often enough' give children the consistency they need."},
         ]},

        {"type": "content", "label": "Pre-Primary", "title": "Preschool and pre-primary education",
         "blocks": [
             {"t": "body", "html": "Quality early childhood education &mdash; in an anganwadi, "
              "balwadi, or pre-primary class &mdash; prepares children for school by building "
              "language, early numeracy, social skills and the habits of learning. Quality matters "
              "more than mere enrolment."},
             {"t": "hbox", "color": "amber", "html": "The danger is 'downward' schoolification "
              "&mdash; rote drilling of three-year-olds. Good pre-primary is play-based and "
              "developmentally appropriate, not a junior version of Class 1."},
         ]},

        {"type": "content", "label": "School Readiness", "title": "What 'ready for school' really means",
         "blocks": [
             {"t": "body", "html": "School readiness is not knowing the alphabet at three. It is "
              "a bundle: a healthy body, curiosity, language, the ability to sit, share, focus and "
              "manage feelings &mdash; the social-emotional and cognitive base for formal learning."},
             {"t": "hbox", "color": "indigo", "html": "And readiness runs both ways: schools must "
              "also be ready for children &mdash; welcoming, child-friendly and prepared for "
              "diverse starting points."},
         ]},

        {"type": "content", "label": "Caregiver Support", "title": "Support caregivers, not just children",
         "blocks": [
             {"t": "body", "html": "Responsive care is hard for a parent who is exhausted, "
              "depressed, anxious or overworked. Maternal mental health, family support and time "
              "are preconditions for warm, responsive caregiving."},
             {"t": "hbox", "color": "green", "html": "Effective ECD programmes coach and support "
              "caregivers &mdash; through home visits and group sessions &mdash; rather than "
              "treating the child as a separate unit."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "The Nurturing Care Framework"},

        {"type": "content", "label": "The Framework", "title": "Nurturing Care: a shared global roadmap",
         "blocks": [
             {"t": "body", "html": "In 2018, WHO, UNICEF and the World Bank launched the "
              "<strong>Nurturing Care Framework</strong> &mdash; an evidence-based blueprint for "
              "what every young child needs to survive and thrive, organised around five "
              "interrelated components."},
             {"t": "hbox", "color": "cyan", "html": "Its power is integration: it brings health, "
              "nutrition, learning, protection and caregiving into one coherent agenda rather than "
              "competing silos."},
         ]},

        {"type": "content", "label": "Five Components", "title": "The five components of nurturing care",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Good health", "label": "For mother &amp; child", "color": "cyan"},
                 {"num": "Adequate nutrition", "label": "From conception onward", "color": "green"},
                 {"num": "Responsive caregiving", "label": "Warm, attuned relationships", "color": "indigo"},
                 {"num": "Early learning", "label": "Play, talk &amp; stimulation", "color": "amber"},
                 {"num": "Security &amp; safety", "label": "Protection from harm", "color": "red"}]},
             {"t": "hbox", "color": "cyan", "html": "Source: WHO / UNICEF / World Bank, "
              "<em>Nurturing Care Framework</em> (2018)."},
         ]},

        {"type": "content", "label": "Balanced View", "title": "All five components, working together",
         "blocks": [
             {"t": "chart", "canvas": "nurtureRadar",
              "title": "Nurturing care is strongest when no component is neglected (schematic)",
              "source": "Illustrative &mdash; WHO/UNICEF Nurturing Care components",
              "type": "radar",
              "data": {"labels": ["Good health", "Adequate nutrition", "Responsive caregiving",
                                  "Early learning", "Security &amp; safety"],
                       "datasets": [
                           {"label": "A thriving setting",
                            "data": [9, 9, 8, 8, 9],
                            "borderColor": "#10B981",
                            "backgroundColor": "rgba(16,185,129,0.15)", "pointRadius": 3},
                           {"label": "A setting neglecting learning &amp; care",
                            "data": [8, 7, 3, 3, 6],
                            "borderColor": "#EF4444",
                            "backgroundColor": "rgba(239,68,68,0.12)", "pointRadius": 3}]},
              "options": {"__js__": "{ scales:{ r:{ min:0, max:10, ticks:{display:false} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Values are illustrative. The message: a "
              "child fed and vaccinated but starved of stimulation and care is still not "
              "receiving nurturing care."},
         ]},

        {"type": "content", "label": "Good Health", "title": "Component 1: Good health",
         "blocks": [
             {"t": "body", "html": "Good health covers the physical and mental health of both "
              "child <em>and</em> caregiver: antenatal care, safe birth, immunisation, treatment "
              "of illness, and attention to maternal mental health &mdash; because a caregiver's "
              "wellbeing shapes the child's."},
             {"t": "hbox", "color": "cyan", "html": "Note that the framework explicitly includes "
              "the caregiver's health, not only the child's. The dyad is the unit of care."},
         ]},

        {"type": "content", "label": "Responsive Caregiving", "title": "Component 3: the connective tissue",
         "blocks": [
             {"t": "body", "html": "Responsive caregiving &mdash; observing and responding to a "
              "child's cues &mdash; is described as the component that <em>enables</em> the others: "
              "responsive feeding, responsive stimulation, responsive protection."},
             {"t": "hbox", "color": "indigo", "html": "It is the thread running through health, "
              "nutrition, learning and safety. Without it, the other inputs land less well."},
         ]},

        {"type": "content", "label": "Security & Safety", "title": "Component 5: protection from harm",
         "blocks": [
             {"t": "body", "html": "Security and safety means protection from physical and "
              "emotional harm &mdash; violence, neglect, accidents, pollution &mdash; and the "
              "predictability of a safe, stable environment in which a child can settle and "
              "explore."},
             {"t": "hbox", "color": "red", "html": "Toxic stress and unsafe environments undermine "
              "every other component. Safety is not a luxury added at the end; it is a foundation."},
         ]},

        {"type": "content", "label": "Why It Works", "title": "Bundled services beat isolated ones",
         "blocks": [
             {"t": "body", "html": "Because the components reinforce one another, delivering them "
              "<strong>together</strong> &mdash; through the same frontline worker, the same home "
              "visit, the same anganwadi &mdash; is more effective and efficient than separate "
              "vertical programmes."},
             {"t": "hbox", "color": "green", "html": "The framework's practical contribution: it "
              "gives ministries, NGOs and donors a common language to coordinate around the whole "
              "child."},
         ]},

        {"type": "content", "label": "Whose Job", "title": "Families lead; systems must enable",
         "blocks": [
             {"t": "body", "html": "Nurturing care is delivered first and foremost by families "
              "&mdash; but families need an enabling environment: supportive policies, services, "
              "community attitudes, financial security and time. Both halves are essential."},
             {"t": "hbox", "color": "cyan", "html": "So 'support the family to care for the "
              "child' becomes the organising principle for ECD programming under this framework."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Risk &amp; Adversity"},

        {"type": "content", "label": "Headwinds", "title": "Development against the odds",
         "blocks": [
             {"t": "body", "html": "Many children grow up facing serious risks &mdash; poverty, "
              "undernutrition, violence, neglect, parental illness, instability. These adversities "
              "can derail development unless buffered by protective relationships and support."},
             {"t": "hbox", "color": "amber", "html": "Risk is not destiny. The same science that "
              "shows how adversity harms also shows how protective factors and timely support can "
              "shield children."},
         ]},

        {"type": "content", "label": "Poverty", "title": "How poverty reaches into early childhood",
         "blocks": [
             {"t": "body", "html": "Poverty rarely acts alone. It bundles together poor nutrition, "
              "crowded and unsafe housing, more illness, parental stress, less stimulation and "
              "fewer services &mdash; a web of disadvantages that compound across the early years."},
             {"t": "hbox", "color": "red", "html": "This is why income poverty and developmental "
              "risk track so closely &mdash; and why ECD is, in part, a strategy to break the "
              "intergenerational transmission of poverty."},
         ]},

        {"type": "content", "label": "Stress Types", "title": "Positive, tolerable and toxic stress",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Type", "What it is", "Effect"],
              "rows": [
                  ["Positive", "Brief, mild stress (a new face)", "Normal, healthy &mdash; builds coping"],
                  ["Tolerable", "Serious but buffered by support", "Manageable if relationships protect"],
                  ["Toxic", "Strong, frequent, unbuffered adversity", "Can disrupt brain development"]]},
             {"t": "hbox", "color": "indigo", "html": "The decisive variable is the buffering "
              "relationship. The same hardship can be tolerable with a supportive adult &mdash; or "
              "toxic without one."},
         ]},

        {"type": "content", "label": "Toxic Stress", "title": "When stress gets 'under the skin'",
         "blocks": [
             {"t": "body", "html": "<strong>Toxic stress</strong> &mdash; prolonged adversity "
              "without protective relationships &mdash; can keep the body's stress system switched "
              "on, disrupting the developing brain and shaping long-term health, learning and "
              "behaviour. This is how adversity gets 'under the skin'."},
             {"t": "hbox", "color": "red", "html": "It links early hardship to later outcomes in "
              "physical and mental health &mdash; a biological pathway from social conditions to "
              "the body."},
         ]},

        {"type": "content", "label": "ACEs", "title": "Adverse Childhood Experiences (ACEs)",
         "blocks": [
             {"t": "term", "word": "Adverse Childhood Experiences (ACEs)",
              "def": "Potentially traumatic events in childhood &mdash; abuse, neglect, violence "
              "in the home, parental mental illness or substance use, separation. Higher ACE "
              "counts are linked to worse health and social outcomes across life."},
             {"t": "hbox", "color": "amber", "html": "ACEs are common and cumulative &mdash; but "
              "their effects can be mitigated by safe, stable, nurturing relationships. "
              "Prevention and buffering both matter."},
         ]},

        {"type": "content", "label": "Neglect", "title": "Neglect: the absence that harms",
         "blocks": [
             {"t": "body", "html": "Neglect &mdash; the chronic absence of responsive interaction, "
              "stimulation or care &mdash; can be as damaging to early development as active abuse. "
              "The young brain needs input; sustained deprivation of it leaves marks."},
             {"t": "hbox", "color": "red", "html": "Because neglect is quiet and invisible, it is "
              "easily overlooked. Yet the lack of 'serve-and-return' interaction is itself a "
              "developmental risk."},
         ]},

        {"type": "content", "label": "Resilience", "title": "Resilience can be built",
         "blocks": [
             {"t": "body", "html": "<strong>Resilience</strong> &mdash; doing well despite "
              "adversity &mdash; is not a fixed trait some children are born with. It is built, "
              "above all, through at least one stable, committed relationship with a supportive "
              "adult."},
             {"t": "hbox", "color": "green", "html": "The single most reliable protective factor "
              "in the research is a caring, consistent relationship. That is also the most "
              "actionable lever for programmes."},
         ]},

        {"type": "content", "label": "Implication", "title": "What adversity means for practice",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Reduce the source of adversity where possible (income, safety, services)",
                 "Strengthen the buffering relationship &mdash; support caregivers",
                 "Act early; the same support does more, sooner",
                 "Screen for risk without stigmatising families"]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "India's ECD Ecosystem"},

        {"type": "content", "label": "ICDS", "title": "ICDS: the world's largest ECD programme",
         "blocks": [
             {"t": "body", "html": "Launched in <strong>1975</strong>, the "
              "<strong>Integrated Child Development Services (ICDS)</strong> scheme delivers a "
              "package &mdash; supplementary nutrition, immunisation, health check-ups, referral, "
              "pre-school education and nutrition counselling &mdash; through a vast network of "
              "anganwadi centres."},
             {"t": "hbox", "color": "cyan", "html": "ICDS embodied the integrated, holistic idea "
              "of ECD decades before the Nurturing Care Framework gave it a name."},
         ]},

        {"type": "content", "label": "Anganwadi", "title": "The anganwadi centre: ECD's front door",
         "blocks": [
             {"t": "body", "html": "The <strong>anganwadi</strong> ('courtyard shelter') is the "
              "neighbourhood ECD hub, staffed by an anganwadi worker and helper. It serves "
              "children under six, pregnant and lactating women, and adolescent girls &mdash; "
              "India's primary platform for reaching young children at scale."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Under 6", "label": "Children served, plus mothers &amp; adolescent girls", "color": "green"},
                 {"num": "Last mile", "label": "Often the only public service in the hamlet", "color": "indigo"}]},
         ]},

        {"type": "content", "label": "The Six Services", "title": "What an anganwadi is meant to deliver",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Service", "For whom"],
              "rows": [
                  ["Supplementary nutrition", "Children, pregnant &amp; lactating women"],
                  ["Pre-school (ECCE)", "Children 3&ndash;6"],
                  ["Nutrition &amp; health education", "Mothers &amp; caregivers"],
                  ["Immunisation (with health system)", "Children &amp; mothers"],
                  ["Health check-ups", "Children &amp; mothers"],
                  ["Referral services", "Those needing higher care"]]},
             {"t": "hbox", "color": "amber", "html": "On paper, a complete package. In practice, "
              "quality varies widely &mdash; pre-school education and stimulation are often the "
              "weakest links."},
         ]},

        {"type": "content", "label": "POSHAN Abhiyaan", "title": "POSHAN Abhiyaan: a national nutrition mission",
         "blocks": [
             {"t": "body", "html": "Launched in <strong>2018</strong>, "
              "<strong>POSHAN Abhiyaan</strong> (the National Nutrition Mission) aims to reduce "
              "stunting, undernutrition and anaemia through convergence across departments, "
              "technology-enabled monitoring, and community mobilisation around the first 1,000 "
              "days."},
             {"t": "hbox", "color": "green", "html": "Its emphasis on <em>convergence</em> "
              "&mdash; health, ICDS, WASH and more acting together &mdash; mirrors the integrated "
              "logic of nurturing care."},
         ]},

        {"type": "content", "label": "RTE & NEP", "title": "RTE and NEP 2020: a push on early education",
         "blocks": [
             {"t": "body", "html": "The <strong>National Education Policy (NEP) 2020</strong> "
              "makes <strong>Early Childhood Care and Education (ECCE)</strong> a national priority "
              "&mdash; aiming for universal quality pre-primary for ages 3&ndash;6 and bringing the "
              "early years formally into the education system's 'foundational stage'."},
             {"t": "hbox", "color": "indigo", "html": "This is a significant shift: early learning "
              "&mdash; long the orphan of the ECD package &mdash; is being elevated as the "
              "foundation of all schooling."},
         ]},

        {"type": "content", "label": "Foundational Learning", "title": "The foundational learning agenda",
         "blocks": [
             {"t": "body", "html": "NEP 2020 frames ages 3&ndash;8 as a continuous "
              "<strong>foundational stage</strong>, with a mission for "
              "<strong>foundational literacy and numeracy (FLN)</strong> &mdash; ensuring children "
              "gain basic reading and arithmetic in the early grades."},
             {"t": "hbox", "color": "amber", "html": "The premise: too many children pass through "
              "early grades without basic skills, and the fix begins in the pre-primary years, not "
              "later."},
         ]},

        {"type": "content", "label": "The Workforce", "title": "ASHAs, AWWs and convergence",
         "blocks": [
             {"t": "body", "html": "India's ECD effort rests on its frontline women workers: the "
              "<strong>ASHA</strong>, the <strong>anganwadi worker (AWW)</strong> and the "
              "<strong>ANM</strong> &mdash; the 'ASHA-Anganwadi-ANM' convergence at the village "
              "level."},
             {"t": "hbox", "color": "green", "html": "Strengthening this workforce &mdash; "
              "training, pay, tools, manageable workloads &mdash; is among the highest-leverage "
              "ECD investments India can make."},
         ]},

        {"type": "content", "label": "Gaps & Reforms", "title": "Strengths and stubborn gaps",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Strengths", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Unmatched scale and reach",
                      "Integrated package by design",
                      "Renewed policy momentum"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Gaps", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Uneven quality, weak pre-school component",
                      "Overstretched, underpaid workers",
                      "Anaemia &amp; equity gaps persist"]}]}]},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Measuring ECD"},

        {"type": "content", "label": "Why Measure", "title": "What gets measured gets attended to",
         "blocks": [
             {"t": "body", "html": "Measuring development helps spot children who need support, "
              "track whether programmes work, and hold systems accountable. But young children are "
              "hard to measure well &mdash; they change fast and behave differently across "
              "settings."},
             {"t": "hbox", "color": "amber", "html": "Measure with humility: tools are aids to "
              "judgement, not verdicts on a child. Labels stick, so use them carefully."},
         ]},

        {"type": "content", "label": "Milestones", "title": "Milestone monitoring: the everyday tool",
         "blocks": [
             {"t": "body", "html": "The simplest measurement is tracking <strong>milestones</strong> "
              "&mdash; does the child sit, walk, speak, respond &mdash; against typical age ranges, "
              "for example via a child health (MCP) card used by frontline workers and families."},
             {"t": "hbox", "color": "cyan", "html": "The aim is not to grade children but to "
              "catch large delays early, when support helps most &mdash; 'surveillance', not "
              "judgement."},
         ]},

        {"type": "content", "label": "Screening Tools", "title": "Structured tools like the ASQ",
         "blocks": [
             {"t": "body", "html": "Structured screening tools &mdash; such as the "
              "<strong>Ages &amp; Stages Questionnaires (ASQ)</strong> &mdash; use caregiver "
              "reports across domains to flag children who may need fuller assessment. They screen; "
              "they do not diagnose."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Screening:</strong> a quick first filter for possible delay",
                 "<strong>Assessment:</strong> a deeper, specialist evaluation that follows",
                 "Tools must be adapted and validated for local language &amp; culture"]},
         ]},

        {"type": "content", "label": "Population Measures", "title": "From one child to whole populations",
         "blocks": [
             {"t": "body", "html": "To compare progress across countries and over time, we need "
              "<strong>population-level</strong> measures of child development &mdash; not just "
              "clinical assessment of individuals. These feed into global monitoring, including "
              "the Sustainable Development Goals."},
             {"t": "hbox", "color": "indigo", "html": "SDG target 4.2 calls for tracking how many "
              "children are <em>developmentally on track</em> &mdash; which created demand for "
              "simple, comparable population tools."},
         ]},

        {"type": "content", "label": "ECDI", "title": "The Early Childhood Development Index",
         "blocks": [
             {"t": "body", "html": "The <strong>Early Childhood Development Index (ECDI)</strong>, "
              "used in UNICEF's <strong>MICS</strong> household surveys, asks caregivers a short "
              "set of questions to estimate the share of children 'developmentally on track' "
              "across literacy-numeracy, physical, social-emotional and learning domains."},
             {"t": "hbox", "color": "cyan", "html": "It is a blunt, population instrument &mdash; "
              "not a diagnosis &mdash; but it lets countries benchmark and track ECD at scale and "
              "spot inequities."},
         ]},

        {"type": "content", "label": "Equity Gaps", "title": "Averages hide who is left behind",
         "blocks": [
             {"t": "chart", "canvas": "ecdEquityChart",
              "title": "Development outcomes often differ sharply by wealth group (schematic)",
              "source": "Illustrative &mdash; typical wealth-gradient pattern",
              "type": "bar",
              "data": {"labels": ["Overall", "Richest", "Q4", "Q3", "Q2", "Poorest"],
                       "datasets": [{"label": "On track (%)",
                                     "data": [64, 82, 74, 64, 54, 44],
                                     "backgroundColor": ["#6366F1", "#10B981", "#10B981",
                                                         "#F59E0B", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% on track'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Values are illustrative, but the gradient is "
              "real: ECD outcomes track closely with wealth, mother's education, caste, and "
              "rural-urban divides. Always disaggregate."},
         ]},

        {"type": "content", "label": "Measurement Cautions", "title": "Reading ECD data critically",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Caregiver-reported tools can be biased by expectations &amp; recall",
                 "Tools built elsewhere may not fit local context without adaptation",
                 "A single number per child can mislabel &mdash; children develop unevenly",
                 "Screening flags risk; only assessment confirms it"]},
             {"t": "hbox", "color": "cyan", "html": "Good measurement informs support and equity; "
              "bad measurement labels and excludes. The difference is care and context."},
         ]},

        {"type": "content", "label": "Disability & Inclusion", "title": "Identifying developmental disability early",
         "blocks": [
             {"t": "body", "html": "Early identification of developmental disabilities and delays "
              "&mdash; in hearing, vision, movement, cognition or communication &mdash; opens the "
              "door to early intervention, when the brain is most responsive and gains are "
              "greatest."},
             {"t": "hbox", "color": "green", "html": "Inclusive ECD means designing programmes so "
              "that children with disabilities are found, welcomed and supported &mdash; not "
              "screened out. Equity includes them by default."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Practice, Equity &amp; Reading"},

        {"type": "content", "label": "Designing Programmes", "title": "Principles of good ECD programming",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Integrate:</strong> bundle health, nutrition, learning, care &amp; safety",
                 "<strong>Start early:</strong> begin in pregnancy, sustain through the early years",
                 "<strong>Support caregivers:</strong> they deliver most of the care",
                 "<strong>Build on what exists:</strong> strengthen anganwadis, ASHAs, schemes",
                 "<strong>Measure for learning:</strong> use data to improve, not just to report"]},
         ]},

        {"type": "content", "label": "Reaching the Margins", "title": "Equity: reach the hardest to reach first",
         "blocks": [
             {"t": "body", "html": "Because disadvantage compounds, the children who would gain "
              "<em>most</em> from ECD are often the ones programmes reach <em>least</em> &mdash; "
              "the poorest, most remote, Dalit and Adivasi communities, migrants, and children "
              "with disabilities."},
             {"t": "hbox", "color": "amber", "html": "Equity is not reaching everyone equally; it "
              "is reaching the most marginalised <em>more</em>. Universal services with extra "
              "effort for the excluded &mdash; 'progressive universalism'."},
         ]},

        {"type": "content", "label": "Gender", "title": "Gender runs through early childhood",
         "blocks": [
             {"t": "body", "html": "Gender shapes ECD on two fronts: the <strong>child</strong> "
              "&mdash; son preference can mean unequal feeding, care and health-seeking for girls "
              "&mdash; and the <strong>caregiver</strong>, since the burden of care falls "
              "overwhelmingly on women, whose own health, time and status matter for the child."},
             {"t": "hbox", "color": "indigo", "html": "Investing in women &mdash; their education, "
              "nutrition, autonomy and support &mdash; is among the most powerful ECD interventions "
              "there is."},
         ]},

        {"type": "content", "label": "Common Pitfalls", "title": "Mistakes ECD programmes make",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Treating nutrition <em>or</em> stimulation, never both together",
                 "Counting inputs (centres built) and ignoring quality of care",
                 "Designing for the average child and missing the marginalised",
                 "Burdening frontline workers without support, pay or training",
                 "Importing a model without adapting it to local context"]},
         ]},

        {"type": "content", "label": "The Case", "title": "Why ECD is worth the investment",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Equity", "label": "Levels the field before school begins", "color": "cyan"},
                 {"num": "Economy", "label": "High returns to early investment (Heckman)", "color": "green"},
                 {"num": "Rights", "label": "Every child's right to survive &amp; develop", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Moral, economic and equity arguments all "
              "point the same way: invest in the early years, and invest most in the children who "
              "have least."},
         ]},

        {"type": "content", "label": "Reading List", "title": "A short ECD reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Nurturing Care Framework</em> &mdash; WHO / UNICEF / World Bank (2018)",
                 "<em>Lancet</em> ECD Series &mdash; the evidence base for early childhood",
                 "Center on the Developing Child (Harvard) &mdash; brain architecture, toxic stress",
                 "Heckman, <em>The Economics of Human Potential</em> &mdash; returns to early investment",
                 "NFHS-5 &amp; POSHAN / NITI Aayog reports &mdash; the Indian data picture"]},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>The first 1,000 days</strong> shape a lifetime &mdash; act in that window",
                 "<strong>Development is holistic</strong> &mdash; nutrition, health, learning &amp; care together",
                 "<strong>Relationships build the brain</strong> &mdash; responsive caregiving is the engine",
                 "<strong>Adversity is not destiny</strong> &mdash; buffering relationships protect children",
                 "<strong>Reach the marginalised most</strong> &mdash; equity is the point of ECD"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Child Development 101 &middot; Complete",
         "headline": "Every child deserves<br>the chance to thrive.",
         "byline": "The science is clear and the tools exist &mdash; what young children need most "
                   "is good health, good nutrition, safety, and warm, responsive relationships in "
                   "their earliest years. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
