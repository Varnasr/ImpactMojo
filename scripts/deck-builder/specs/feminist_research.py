# -*- coding: utf-8 -*-
"""
Feminist Research 101 — ImpactMojo 101 Series (native deck spec)
Feminist research theory and practice for South Asian development researchers.
Build: python3 scripts/deck-builder/build.py feminist_research
"""

DECK = {
    "slug": "feminist-research",
    "title": "Feminist Research 101",
    "description": ("Feminist Research 101 — a free foundational course for development "
                    "researchers and practitioners in South Asia. From the feminist critique "
                    "of objective science through standpoint theory, situated knowledges and "
                    "intersectionality to ethics, reflexivity, decolonial feminisms and a "
                    "practical checklist for doing research that challenges power. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Feminist<br>Research<br>101",
         "sub": "How Power Shapes Knowledge &mdash; and How to Do Research That Answers Back. "
                "A Foundational Course for Development Researchers in South Asia",
         "tags": ["Theory-Rich", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Feminist Research Is"},
             {"name": "A Short History"},
             {"name": "Core Commitments"},
             {"name": "Standpoint Theory"},
             {"name": "Situated Knowledges"},
             {"name": "Intersectionality in Research"},
             {"name": "Feminist Methods"},
             {"name": "Ethics &amp; Non-Extraction"},
             {"name": "Reflexivity &amp; Relationships"},
             {"name": "Decolonial &amp; Southern Feminisms"},
             {"name": "Doing It &amp; Further Reading"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Feminist Research Is"},

        {"type": "content", "label": "First Things First", "title": "Not just 'research about women'",
         "blocks": [
             {"t": "body", "html": "The commonest misconception: feminist research means studying "
              "women, or adding a 'gender' variable. It does not. <strong>Feminist research is a "
              "way of doing research</strong> &mdash; a stance on knowledge, power and method &mdash; "
              "that can be applied to any topic, including ones with no women in sight."},
             {"t": "hbox", "color": "cyan", "html": "You can study irrigation policy, fiscal "
              "transfers or migration feministically. The subject is not the point; the way you "
              "produce and use knowledge is."},
         ]},

        {"type": "content", "label": "Definition", "title": "Research as a political act",
         "blocks": [
             {"t": "term", "word": "Feminist research",
              "def": "Inquiry that treats knowledge production as shaped by power &mdash; especially "
              "gendered power &mdash; and that works deliberately to surface, question and shift "
              "that power rather than reproduce it. It asks not only 'what is true?' but 'true for "
              "whom, told by whom, in whose interest?'"},
             {"t": "body", "html": "Every research choice &mdash; what to ask, whom to count, which "
              "categories to use &mdash; carries values. Feminist research makes those values "
              "explicit instead of hiding them behind a claim of neutrality."},
         ]},

        {"type": "content", "label": "The Core Claim", "title": "Knowledge is produced, not found",
         "blocks": [
             {"t": "flow", "steps": [
                 "Someone decides a question is worth asking",
                 "Someone chooses what counts as evidence",
                 "Someone selects who is asked, and how",
                 "A 'fact' is produced &mdash; bearing all those choices"]},
             {"t": "hbox", "color": "amber", "html": "Knowledge does not fall from the sky as neutral "
              "fact. It is <em>made</em> &mdash; in institutions, by people, under constraints. "
              "Feminist research insists we examine the making, not just the made."},
         ]},

        {"type": "content", "label": "Challenging Power", "title": "Three kinds of power in any study",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Whose question?", "label": "Power to decide what is worth studying at all",
                  "color": "cyan"},
                 {"num": "Whose voice?", "label": "Power over who speaks and who is spoken about",
                  "color": "indigo"},
                 {"num": "Whose benefit?", "label": "Power over who gains from the knowledge produced",
                  "color": "amber"}]},
             {"t": "body", "html": "Conventional research often leaves all three with the researcher "
              "and the funder. Feminist research treats each as a question to be answered openly, "
              "not a default to be assumed."},
         ]},

        {"type": "content", "label": "Why It Matters Here", "title": "Development research is never neutral",
         "blocks": [
             {"t": "body", "html": "In South Asian development, research decides who is 'poor enough' "
              "for a scheme, whose labour counts as work, which households are 'female-headed'. "
              "These are not technical definitions &mdash; they are decisions about whose reality "
              "the state will see and act on."},
             {"t": "hbox", "color": "red", "html": "When unpaid care work is excluded from "
              "'economic activity', millions of women become statistically invisible. The "
              "measurement choice <em>is</em> the politics."},
         ]},

        {"type": "content", "label": "A Worked Contrast", "title": "Same topic, two ways of asking",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Conventional framing", "Feminist framing"],
              "rows": [
                  ["Question", "What is the female labour-force participation rate?",
                   "Why does so much of women's work go uncounted?"],
                  ["Categories", "Employed / unemployed", "Paid, unpaid, care, subsistence, hidden"],
                  ["Voice", "Survey codes the respondent", "Respondent helps define the categories"],
                  ["Aim", "Measure a gap", "Question who built the measure"]]},
             {"t": "hbox", "color": "cyan", "html": "Both can be rigorous. The feminist version "
              "refuses to take the existing categories as neutral givens."},
         ]},

        {"type": "content", "label": "Common Misreadings", "title": "What feminist research is not",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Not</strong> automatically qualitative &mdash; feminists do statistics too",
                 "<strong>Not</strong> unrigorous or 'just opinion' &mdash; it is held to high standards",
                 "<strong>Not</strong> only for or about women &mdash; gender structures everyone",
                 "<strong>Not</strong> value-free pretending &mdash; it is value-explicit by design"]},
             {"t": "hbox", "color": "amber", "html": "Making values explicit is the opposite of bias. "
              "Hidden values do the damage; named values can be debated and checked."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "A Short History"},

        {"type": "content", "label": "The Starting Point", "title": "A critique of 'objective' science",
         "blocks": [
             {"t": "body", "html": "Feminist research began as a critique. Western science claimed "
              "to produce <strong>universal, neutral, view-from-nowhere</strong> knowledge &mdash; "
              "yet its questions, its researchers and its assumptions were overwhelmingly elite, "
              "male and metropolitan."},
             {"t": "hbox", "color": "cyan", "html": "If the knowers were so partial, feminists "
              "asked, how could the knowledge be so universal? The claim to neutrality was itself "
              "a position &mdash; an unmarked one."},
         ]},

        {"type": "content", "label": "The Waves", "title": "A rough map of feminist movements",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Wave", "Roughly", "Central concern"],
              "rows": [
                  ["First", "Late 19th &ndash; early 20th c.", "Suffrage, legal personhood, property"],
                  ["Second", "1960s &ndash; 1980s", "Sexuality, labour, 'the personal is political'"],
                  ["Third", "1990s onward", "Difference, intersectionality, identity, voice"],
                  ["Fourth", "2010s onward", "Digital, networked, #MeToo, global solidarities"]]},
             {"t": "hbox", "color": "amber", "html": "The 'waves' are a Western shorthand, contested "
              "and imperfect &mdash; South Asian feminisms followed their own timelines. Use the map "
              "loosely, not as gospel."},
         ]},

        {"type": "content", "label": "The Personal Is Political", "title": "A slogan that reshaped research",
         "blocks": [
             {"t": "body", "html": "The second-wave insight that private life &mdash; housework, "
              "care, violence, the body &mdash; is structured by public power had a profound "
              "research consequence: domains once dismissed as <em>too private to study</em> became "
              "central objects of serious inquiry."},
             {"t": "hbox", "color": "green", "html": "Unpaid care, intimate-partner violence and "
              "household bargaining are now mainstream research topics. They were not, until "
              "feminists insisted the kitchen and the bedroom were political spaces."},
         ]},

        {"type": "content", "label": "Three Epistemologies", "title": "Harding's map of feminist approaches",
         "blocks": [
             {"t": "body", "html": "Sandra Harding influentially distinguished three feminist "
              "responses to the problem of biased science &mdash; not stages to pass through, but "
              "distinct positions still in use today."},
             {"t": "flow", "steps": [
                 "FEMINIST EMPIRICISM: better science fixes the bias",
                 "STANDPOINT THEORY: the margins see more clearly",
                 "POSTMODERN: distrust all universal claims to truth"]},
         ]},

        {"type": "content", "label": "Position One", "title": "Feminist empiricism: do science better",
         "blocks": [
             {"t": "term", "word": "Feminist empiricism",
              "def": "The view that sexist and androcentric bias is bad science &mdash; a failure to "
              "follow scientific norms rigorously &mdash; and can be corrected by more careful, more "
              "inclusive empirical work, without abandoning objectivity itself."},
             {"t": "body", "html": "Its strength: it works within the existing rules and shows, "
              "empirically, where mainstream science got things wrong. Its limit: it leaves the "
              "ideal of a neutral, value-free method largely unquestioned."},
         ]},

        {"type": "content", "label": "Position Two", "title": "Standpoint theory: knowledge from the margins",
         "blocks": [
             {"t": "body", "html": "The second position goes further: it argues that those at the "
              "<strong>margins of power</strong> can produce <em>better, less distorted</em> "
              "knowledge of how a system works, precisely because they must understand both their "
              "own world and that of the powerful to survive."},
             {"t": "hbox", "color": "cyan", "html": "We give standpoint theory a full section next "
              "&mdash; it is one of feminist research's most distinctive and debated contributions."},
         ]},

        {"type": "content", "label": "Position Three", "title": "Postmodern feminism: suspicion of grand truths",
         "blocks": [
             {"t": "body", "html": "The third position is wary of <em>any</em> single account of "
              "the truth, including a single 'woman's standpoint'. It stresses that 'woman' is not "
              "one thing, that all knowledge is partial and constructed, and that universalising "
              "claims tend to silence difference."},
             {"t": "hbox", "color": "amber", "html": "Its gift is humility and attention to "
              "difference; its danger is a relativism that can dissolve the political ground "
              "feminism needs to stand on. Most researchers hold the tension, not resolve it."},
         ]},

        {"type": "content", "label": "South Asian Roots", "title": "These debates were never only Western",
         "blocks": [
             {"t": "body", "html": "Parallel and independent feminist scholarship grew in South "
              "Asia &mdash; on women and work, on caste and patriarchy, on the household as a site "
              "of inequality &mdash; engaging Indian realities that Western frameworks often "
              "missed entirely."},
             {"t": "hbox", "color": "green", "html": "We return to Indian feminist scholarship and "
              "the question of caste in Section Ten. Keep it in view: the 'history' is plural, not "
              "a single Western line."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Core Commitments"},

        {"type": "content", "label": "The Five", "title": "What holds feminist research together",
         "blocks": [
             {"t": "body", "html": "Feminist research spans many methods and traditions, but a "
              "family of <strong>commitments</strong> recurs across them. Five appear again and "
              "again &mdash; the working ethics of the whole approach."},
             {"t": "flow", "steps": [
                 "REFLEXIVITY", "POSITIONALITY", "POWER", "VOICE", "RECIPROCITY"]},
         ]},

        {"type": "content", "label": "Commitment 1", "title": "Reflexivity: the researcher in the frame",
         "blocks": [
             {"t": "term", "word": "Reflexivity",
              "def": "The continuous, critical examination of how the researcher's own identity, "
              "assumptions, methods and presence shape every stage of the research &mdash; and "
              "the honest reporting of that influence."},
             {"t": "hbox", "color": "cyan", "html": "Conventional method tries to remove the "
              "researcher from view. Feminist method puts the researcher <em>in</em> the picture, "
              "as a visible part of how the knowledge was made."},
         ]},

        {"type": "content", "label": "Commitment 2", "title": "Positionality: where you stand shapes what you see",
         "blocks": [
             {"t": "term", "word": "Positionality",
              "def": "The recognition that your social location &mdash; gender, caste, class, "
              "race, language, nationality, institutional power &mdash; conditions your access, "
              "your blind spots and the responses you receive."},
             {"t": "body", "html": "A high-caste urban researcher and a local Dalit fieldworker "
              "asking the same question will not get the same answers. Positionality is not a "
              "confession to make once; it is an analytic tool to use throughout."},
         ]},

        {"type": "content", "label": "Commitment 3", "title": "Power: it runs through the whole encounter",
         "blocks": [
             {"t": "body", "html": "Power is not only in the topic studied; it saturates the "
              "research <em>relationship</em> &mdash; who sets the agenda, who can interrupt, who "
              "interprets, who publishes, who is paid."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Researcher holds", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "The agenda and the questions",
                      "The means of interpretation",
                      "The platform to publish"]}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Researched may hold", "blocks": [
                  {"t": "bullets", "sm": True, "color": "amber", "items": [
                      "What they choose to reveal",
                      "Knowledge the researcher lacks",
                      "The power to refuse or mislead"]}]}]},
         ]},

        {"type": "content", "label": "Commitment 4", "title": "Voice: who gets to speak, and be heard",
         "blocks": [
             {"t": "body", "html": "Feminist research takes seriously the task of letting people "
              "speak in their own terms &mdash; and notices when its own categories drown them out. "
              "But 'giving voice' is itself a power the researcher holds, and must be handled with care."},
             {"t": "hbox", "color": "red", "html": "Beware the trap: claiming to 'give voice' can "
              "quietly re-centre the researcher as the one who grants it. The aim is to amplify and "
              "not to ventriloquise."},
         ]},

        {"type": "content", "label": "Commitment 5", "title": "Reciprocity: research that gives back",
         "blocks": [
             {"t": "term", "word": "Reciprocity",
              "def": "The principle that a research relationship should not be purely extractive &mdash; "
              "that those who give their time, stories and trust should receive something in return, "
              "whether knowledge, recognition, or material support."},
             {"t": "body", "html": "It can be small (sharing findings in accessible form) or large "
              "(co-designing the study). What matters is rejecting the model of arriving, "
              "extracting and vanishing."},
         ]},

        {"type": "content", "label": "How They Connect", "title": "The commitments reinforce one another",
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 900 300" width="100%" style="max-height:300px">'
                 '<defs><marker id="ar1" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">'
                 '<path d="M0,0 L8,4 L0,8 Z" fill="#94a3b8"/></marker></defs>'
                 '<circle cx="150" cy="150" r="62" fill="rgba(14,165,233,0.14)" stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="150" y="146" text-anchor="middle" fill="#0EA5E9" font-size="17" font-weight="700">Positionality</text>'
                 '<text x="150" y="168" text-anchor="middle" fill="#cbd5e1" font-size="12">where I stand</text>'
                 '<circle cx="450" cy="150" r="62" fill="rgba(99,102,241,0.14)" stroke="#6366F1" stroke-width="2"/>'
                 '<text x="450" y="146" text-anchor="middle" fill="#818cf8" font-size="17" font-weight="700">Reflexivity</text>'
                 '<text x="450" y="168" text-anchor="middle" fill="#cbd5e1" font-size="12">examining it</text>'
                 '<circle cx="750" cy="150" r="62" fill="rgba(16,185,129,0.14)" stroke="#10B981" stroke-width="2"/>'
                 '<text x="750" y="142" text-anchor="middle" fill="#34d399" font-size="16" font-weight="700">Power, Voice</text>'
                 '<text x="750" y="162" text-anchor="middle" fill="#34d399" font-size="16" font-weight="700">&amp; Reciprocity</text>'
                 '<text x="750" y="182" text-anchor="middle" fill="#cbd5e1" font-size="12">acting on it</text>'
                 '<line x1="218" y1="150" x2="382" y2="150" stroke="#94a3b8" stroke-width="2" marker-end="url(#ar1)"/>'
                 '<line x1="518" y1="150" x2="682" y2="150" stroke="#94a3b8" stroke-width="2" marker-end="url(#ar1)"/>'
                 '</svg>')},
             {"t": "hbox", "color": "cyan", "html": "Naming your position makes reflexivity "
              "possible; reflexivity reveals the power at play; that recognition is what you act on "
              "through voice and reciprocity."},
         ]},

        {"type": "content", "label": "A Caution", "title": "Commitments are practice, not a checklist",
         "blocks": [
             {"t": "body", "html": "These commitments are easy to recite and hard to live. A "
              "positionality paragraph bolted onto an extractive study is decoration. The "
              "commitments only mean something when they actually change what you do."},
             {"t": "quote",
              "text": "Reflexivity that does not change the research is just a more sophisticated "
              "way of doing the same thing.",
              "attr": "&mdash; a working caution for the field"},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Standpoint Theory"},

        {"type": "content", "label": "The Big Idea", "title": "Knowledge looks different from below",
         "blocks": [
             {"t": "term", "word": "Standpoint theory",
              "def": "The argument that social position systematically shapes what one can know, "
              "and that the perspectives of dominated or marginalised groups can yield more complete "
              "and less distorted accounts of how a social system actually works."},
             {"t": "body", "html": "A standpoint is not the same as a mere opinion or viewpoint. It "
              "is an <em>achieved</em> critical understanding, won through reflection on shared "
              "experience of a structure of power."},
         ]},

        {"type": "content", "label": "Why The Margins See More", "title": "The double vision of the dominated",
         "blocks": [
             {"t": "body", "html": "To survive, those without power must understand both their own "
              "world <em>and</em> the world of the powerful. The powerful can afford to understand "
              "only their own. This asymmetry gives the margins a wider, more critical field of view."},
             {"t": "hbox", "color": "cyan", "html": "A domestic worker knows the household from the "
              "kitchen and from the drawing room. The employer rarely knows the kitchen at all. "
              "Whose account of that household is more complete?"},
         ]},

        {"type": "content", "label": "Harding", "title": "Sandra Harding and 'strong objectivity'",
         "blocks": [
             {"t": "body", "html": "Sandra Harding turned the usual charge on its head. Mainstream "
              "'objectivity', she argued, is <strong>too weak</strong>: it scrutinises the data but "
              "never the social values and assumptions built into the questions themselves."},
             {"t": "term", "word": "Strong objectivity",
              "def": "Harding's idea that genuine objectivity requires examining the researcher's "
              "own social location and starting assumptions as rigorously as the evidence &mdash; "
              "and that starting from marginalised lives produces stronger, not weaker, knowledge."},
         ]},

        {"type": "content", "label": "Strong vs Weak", "title": "Two senses of being objective",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Weak objectivity", "Strong objectivity (Harding)"],
              "rows": [
                  ["Scrutinises", "The data and analysis", "The data AND the assumptions behind the question"],
                  ["The knower", "Treated as neutral, invisible", "Examined as part of the inquiry"],
                  ["Starting point", "Dominant frameworks", "The lives of the marginalised"],
                  ["Claim", "View from nowhere", "Honest about the view from somewhere"]]},
             {"t": "hbox", "color": "green", "html": "The provocation: examining your own position "
              "is not a retreat from objectivity. It is what real objectivity demands."},
         ]},

        {"type": "content", "label": "Dorothy Smith", "title": "Starting from the everyday",
         "blocks": [
             {"t": "body", "html": "Sociologist Dorothy Smith argued that mainstream sociology spoke "
              "from the standpoint of the institutions that govern people &mdash; what she called "
              "the 'relations of ruling' &mdash; and rendered women's everyday lives invisible. She "
              "proposed beginning instead from people's actual, lived, daily experience."},
             {"t": "term", "word": "Institutional ethnography",
              "def": "Dorothy Smith's method: start from the everyday experience of real people and "
              "trace outward to show how distant institutional and textual relations organise and "
              "shape that experience &mdash; making 'the ruling relations' visible from below."},
         ]},

        {"type": "content", "label": "Hill Collins", "title": "Patricia Hill Collins and the matrix of domination",
         "blocks": [
             {"t": "term", "word": "Matrix of domination",
              "def": "Patricia Hill Collins's concept that race, class, gender and other systems of "
              "oppression are interlocking and mutually constituting &mdash; experienced together, "
              "through one another, rather than as separable, additive disadvantages."},
             {"t": "body", "html": "Collins also centred the idea of <strong>Black women as agents "
              "of knowledge</strong>, insisting that those at the intersection of oppressions "
              "produce theory, not merely data for others to theorise about."},
         ]},

        {"type": "content", "label": "Outsider Within", "title": "The vantage point of the 'outsider within'",
         "blocks": [
             {"t": "body", "html": "Hill Collins named the position of people who are inside an "
              "institution yet never fully of it &mdash; the domestic worker in the family, the "
              "first-generation scholar in the academy. This <strong>'outsider within'</strong> "
              "location offers a distinctive, critically clear angle of vision."},
             {"t": "hbox", "color": "cyan", "html": "Many development researchers from marginalised "
              "backgrounds occupy exactly this position &mdash; close enough to see the institution's "
              "inner workings, distant enough not to take them for granted."},
         ]},

        {"type": "content", "label": "Honest Critique", "title": "Standpoint theory's own hard questions",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Which standpoint? There is no single 'woman's' or 'poor person's' view",
                 "Does it romanticise the margins, as if suffering guaranteed insight?",
                 "Can outsiders ever access it &mdash; or must you live it to know it?",
                 "Risk of essentialism: treating a group as having one fixed perspective"]},
             {"t": "hbox", "color": "amber", "html": "Standpoint theorists take these seriously. "
              "Most now speak of <em>multiple</em>, intersecting standpoints &mdash; which leads "
              "straight to situated knowledges and intersectionality."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Situated Knowledges"},

        {"type": "content", "label": "Haraway", "title": "Donna Haraway, 'Situated Knowledges', 1988",
         "blocks": [
             {"t": "body", "html": "In a landmark 1988 essay, Donna Haraway offered feminism a way "
              "between two traps: the false certainty of 'objective' science and the paralysis of "
              "'it's all just perspective'. Her answer was <strong>situated knowledge</strong>."},
             {"t": "term", "word": "Situated knowledges",
              "def": "Haraway's idea that all knowledge is produced from a specific, embodied "
              "location &mdash; and that acknowledging this partiality is the precondition for "
              "objectivity, not its enemy."},
         ]},

        {"type": "content", "label": "The God Trick", "title": "The 'view from nowhere' is a trick",
         "blocks": [
             {"t": "term", "word": "The god trick",
              "def": "Haraway's name for the illusion of seeing everything from no particular place "
              "&mdash; the disembodied, all-seeing gaze that science claims when it presents its "
              "knowledge as a view from nowhere and everywhere at once."},
             {"t": "hbox", "color": "red", "html": "The god trick is seductive because it hides the "
              "knower. But there is no view from nowhere &mdash; only views that <em>pretend</em> to "
              "be from nowhere, and so escape accountability."},
         ]},

        {"type": "content", "label": "Partial Perspective", "title": "Objectivity through partiality, not above it",
         "blocks": [
             {"t": "body", "html": "Haraway's twist: <strong>only partial perspective promises "
              "objective vision.</strong> Because a situated view is locatable, it can be held "
              "accountable &mdash; we can ask where it was made and what it could and could not see. "
              "The god trick's view, being nowhere, can be questioned nowhere."},
             {"t": "quote",
              "text": "The only way to find a larger vision is to be somewhere in particular.",
              "attr": "&mdash; Donna Haraway, Situated Knowledges (1988)"},
         ]},

        {"type": "content", "label": "Two Failures", "title": "Between false neutrality and pure relativism",
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 900 250" width="100%" style="max-height:250px">'
                 '<rect x="20" y="90" width="250" height="80" rx="10" fill="rgba(239,68,68,0.12)" stroke="#EF4444" stroke-width="2"/>'
                 '<text x="145" y="122" text-anchor="middle" fill="#f87171" font-size="16" font-weight="700">The god trick</text>'
                 '<text x="145" y="146" text-anchor="middle" fill="#cbd5e1" font-size="12">one view claims to be ALL views</text>'
                 '<rect x="630" y="90" width="250" height="80" rx="10" fill="rgba(245,158,11,0.12)" stroke="#F59E0B" stroke-width="2"/>'
                 '<text x="755" y="122" text-anchor="middle" fill="#fbbf24" font-size="16" font-weight="700">Pure relativism</text>'
                 '<text x="755" y="146" text-anchor="middle" fill="#cbd5e1" font-size="12">all views equally (un)true</text>'
                 '<rect x="320" y="80" width="260" height="100" rx="12" fill="rgba(14,165,233,0.16)" stroke="#0EA5E9" stroke-width="2.5"/>'
                 '<text x="450" y="118" text-anchor="middle" fill="#38bdf8" font-size="17" font-weight="700">Situated knowledge</text>'
                 '<text x="450" y="142" text-anchor="middle" fill="#cbd5e1" font-size="12">partial, located,</text>'
                 '<text x="450" y="160" text-anchor="middle" fill="#cbd5e1" font-size="12">and accountable</text>'
                 '</svg>')},
             {"t": "body", "html": "Both failures escape accountability the same way: relativism "
              "and totalisation are mirror images, each refusing to say <em>from where</em> a claim "
              "is made. Situated knowledge refuses both."},
         ]},

        {"type": "content", "label": "Embodiment", "title": "Vision comes from a body, in a place",
         "blocks": [
             {"t": "body", "html": "Haraway insists knowledge is <strong>embodied</strong>: it comes "
              "from particular eyes, instruments, languages and histories. Even a satellite image is "
              "a situated way of seeing &mdash; built by someone, for some purpose, rendering some "
              "things visible and others not."},
             {"t": "hbox", "color": "cyan", "html": "There is no neutral instrument. A survey form, a "
              "poverty line, a remote-sensing model &mdash; each embodies a particular way of "
              "carving up the world."},
         ]},

        {"type": "content", "label": "For Practice", "title": "What situatedness asks of you",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "State <strong>from where</strong> your knowledge was produced &mdash; setting, tools, position",
                 "Name what your vantage point lets you see &mdash; and what it cannot",
                 "Treat 'the view from nowhere' in others' work as a claim to interrogate",
                 "Make your account locatable, so others can hold it accountable"]},
         ]},

        {"type": "content", "label": "Connecting Threads", "title": "Standpoint and situatedness, side by side",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Standpoint theory", "Situated knowledges"],
              "rows": [
                  ["Emphasis", "The margins see the system more fully", "ALL knowledge is located and partial"],
                  ["Objectivity", "Stronger from the margins", "Stronger when partiality is owned"],
                  ["Risk it guards against", "Dominant frameworks erase the marginalised", "The god trick AND relativism"],
                  ["Key figure", "Harding, Smith, Hill Collins", "Donna Haraway"]]},
             {"t": "hbox", "color": "cyan", "html": "They are allies, not rivals: both reject the "
              "view from nowhere and both make the knower part of the knowledge."},
         ]},

        {"type": "content", "label": "Why It Travels", "title": "A tool for reading any evidence",
         "blocks": [
             {"t": "body", "html": "Situated knowledge is not only for feminists studying gender. It "
              "is a lens for reading <em>any</em> claim: a World Bank model, a national poverty "
              "estimate, a programme evaluation. Ask of each &mdash; from where was this made, and "
              "what could it not see?"},
             {"t": "hbox", "color": "amber", "html": "This habit alone will sharpen how you read "
              "every report that crosses your desk for the rest of your career."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Intersectionality in Research"},

        {"type": "content", "label": "Crenshaw", "title": "Kimberle Crenshaw coins the term, 1989",
         "blocks": [
             {"t": "body", "html": "Legal scholar Kimberle Crenshaw introduced "
              "<strong>intersectionality</strong> in 1989 to describe how anti-discrimination law "
              "failed Black women: courts recognised race discrimination <em>or</em> sex "
              "discrimination, but not the distinct harm of facing both at once."},
             {"t": "term", "word": "Intersectionality",
              "def": "The analysis of how multiple systems of power &mdash; gender, race, caste, "
              "class, disability, sexuality &mdash; intersect to produce distinct, compounded "
              "experiences that cannot be understood by examining each system separately."},
         ]},

        {"type": "content", "label": "The Crossroads", "title": "Why the metaphor is a crossroads",
         "blocks": [
             {"t": "body", "html": "Crenshaw's image: a person standing where several roads of power "
              "cross can be struck by traffic from any direction &mdash; or several at once. The harm "
              "at the intersection is not the simple sum of the separate roads."},
             {"t": "hbox", "color": "red", "html": "Intersectionality is <strong>not additive.</strong> "
              "A Dalit woman's experience is not 'caste disadvantage plus gender disadvantage'. It is "
              "a specific reality produced by both at once, irreducible to either."},
         ]},

        {"type": "content", "label": "Additive vs Intersectional", "title": "The difference in how you analyse",
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 900 240" width="100%" style="max-height:240px">'
                 '<text x="225" y="34" text-anchor="middle" fill="#f87171" font-size="15" font-weight="700">Additive (limited)</text>'
                 '<rect x="120" y="58" width="210" height="40" rx="8" fill="rgba(245,158,11,0.16)" stroke="#F59E0B"/>'
                 '<text x="225" y="83" text-anchor="middle" fill="#fbbf24" font-size="13">gender disadvantage</text>'
                 '<text x="225" y="118" text-anchor="middle" fill="#94a3b8" font-size="18">+</text>'
                 '<rect x="120" y="128" width="210" height="40" rx="8" fill="rgba(99,102,241,0.16)" stroke="#6366F1"/>'
                 '<text x="225" y="153" text-anchor="middle" fill="#818cf8" font-size="13">caste disadvantage</text>'
                 '<line x1="450" y1="40" x2="450" y2="200" stroke="#334155" stroke-width="1.5" stroke-dasharray="5 5"/>'
                 '<text x="675" y="34" text-anchor="middle" fill="#34d399" font-size="15" font-weight="700">Intersectional</text>'
                 '<circle cx="630" cy="125" r="58" fill="rgba(245,158,11,0.18)" stroke="#F59E0B"/>'
                 '<circle cx="720" cy="125" r="58" fill="rgba(99,102,241,0.18)" stroke="#6366F1"/>'
                 '<text x="675" y="120" text-anchor="middle" fill="#5eead4" font-size="13" font-weight="700">a distinct</text>'
                 '<text x="675" y="138" text-anchor="middle" fill="#5eead4" font-size="13" font-weight="700">reality</text>'
                 '</svg>')},
             {"t": "hbox", "color": "cyan", "html": "Stacking two variables in a regression treats "
              "oppression as additive. Intersectionality asks you to study the overlap itself."},
         ]},

        {"type": "content", "label": "Caste, Class, Gender", "title": "The South Asian intersection",
         "blocks": [
             {"t": "body", "html": "In South Asia, the most consequential intersections braid "
              "<strong>caste, class and gender</strong> &mdash; with religion, region, language and "
              "disability layered through. A poverty figure that ignores caste will miss the "
              "structure that produces much of that poverty."},
             {"t": "hbox", "color": "amber", "html": "Indian feminists insisted on this early: a "
              "'sisterhood of all women' that ignored caste reproduced upper-caste dominance inside "
              "feminism itself. We return to this in Section Ten."},
         ]},

        {"type": "content", "label": "Disaggregation", "title": "Why the overall number lies",
         "blocks": [
             {"t": "chart", "canvas": "frIntersectChart",
              "title": "An overall rate can hide who is left furthest behind",
              "source": "Illustrative &mdash; pattern, not real figures",
              "type": "bar",
              "data": {"labels": ["Overall", "Upper-caste women", "OBC women", "Dalit women", "Adivasi women"],
                       "datasets": [{"label": "Outcome (%)",
                                     "data": [58, 74, 60, 44, 36],
                                     "backgroundColor": ["#6366F1", "#10B981", "#10B981", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100, title:{display:true,text:'%'}} } }"}},
             {"t": "hbox", "color": "red", "html": "The 'overall' bar is an average of unequal "
              "lives. Intersectional disaggregation is how the gap between the first and last bars "
              "becomes visible &mdash; and actionable."},
         ]},

        {"type": "content", "label": "From Identity to Structure", "title": "It's about systems, not just labels",
         "blocks": [
             {"t": "body", "html": "Intersectionality is often misread as a list of identity labels "
              "to collect. Crenshaw's point is structural: it is about interlocking <em>systems of "
              "power</em> &mdash; caste, patriarchy, capitalism &mdash; not just the attributes of "
              "individuals."},
             {"t": "hbox", "color": "cyan", "html": "Do not stop at 'we sampled Dalit women'. Ask "
              "how the systems of caste and patriarchy jointly produce the outcomes you observe. "
              "Structure, not just category."},
         ]},

        {"type": "content", "label": "Doing It Well", "title": "Intersectional research in practice",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Disaggregate &mdash; but go beyond single axes to their intersections",
                 "Sample so that small, multiply-marginalised groups are actually visible",
                 "Let categories be defined with communities, not imposed from outside",
                 "Analyse the systems, not only the individuals who bear their effects"]},
         ]},

        {"type": "content", "label": "A Caution", "title": "Intersectionality is not infinite slicing",
         "blocks": [
             {"t": "body", "html": "Taken naively, 'intersect everything' fragments a sample into "
              "groups too small to study and dissolves any shared political claim. The aim is not "
              "endless subdivision but attention to the <strong>structurally significant</strong> "
              "intersections in your context."},
             {"t": "hbox", "color": "amber", "html": "Ask which intersections <em>matter</em> for "
              "the power structure you are studying &mdash; not how many you can technically create."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Feminist Methods"},

        {"type": "content", "label": "The Big Misconception", "title": "There is no single 'feminist method'",
         "blocks": [
             {"t": "body", "html": "Feminist research is defined by its <strong>questions and "
              "commitments</strong>, not by a signature technique. There is no method that is "
              "feminist in itself, and none that cannot be used feministically."},
             {"t": "quote",
              "text": "What makes research feminist is less the methods it uses than the questions "
              "it asks and how it answers them.",
              "attr": "&mdash; a widely shared view in feminist methodology"},
         ]},

        {"type": "content", "label": "The Qualitative Lean", "title": "Why feminists often favour qualitative work",
         "blocks": [
             {"t": "body", "html": "Feminist research <em>tends</em> toward qualitative methods &mdash; "
              "in-depth interviews, oral history, ethnography, participatory work &mdash; because they "
              "make space for voice, context and meaning that pre-coded surveys can flatten."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Methods often used", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Semi-structured &amp; life-history interviews",
                      "Oral history and testimony",
                      "Participatory and visual methods"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "What they enable", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Categories defined by participants",
                      "Meaning and process, not just counts",
                      "Space for the unexpected to surface"]}]}]},
         ]},

        {"type": "content", "label": "Oral History", "title": "Recovering what records erased",
         "blocks": [
             {"t": "body", "html": "Oral history has been vital to feminist scholarship precisely "
              "because the marginalised rarely leave written archives. Listening to "
              "<strong>testimony</strong> recovers histories &mdash; of Partition, of labour, of "
              "violence &mdash; that official documents never recorded."},
             {"t": "hbox", "color": "cyan", "html": "In South Asia, feminist oral history of "
              "Partition recovered women's experiences of abduction, recovery and survival that "
              "the nationalist record had silenced for decades."},
         ]},

        {"type": "content", "label": "Participatory", "title": "Research with, not on, communities",
         "blocks": [
             {"t": "body", "html": "Participatory approaches shift the researcher from sole author "
              "toward facilitator &mdash; communities help frame questions, gather and interpret "
              "data, and decide what the findings are for. It directly enacts the commitments to "
              "voice and reciprocity."},
             {"t": "flow", "steps": [
                 "Community helps frame the question",
                 "Co-design what counts as data",
                 "Gather and interpret together",
                 "Decide jointly what the findings serve"]},
         ]},

        {"type": "content", "label": "Feminist Quantitative", "title": "Yes &mdash; feminists do statistics",
         "blocks": [
             {"t": "body", "html": "Rejecting numbers would surrender a powerful tool to those who "
              "misuse it. Feminist quantitative work counts what mainstream statistics ignore "
              "&mdash; unpaid care, time use, violence &mdash; and disaggregates relentlessly to "
              "make inequality visible."},
             {"t": "hbox", "color": "green", "html": "Time-use surveys that finally measure women's "
              "unpaid work, or gender-disaggregated budgets, are deeply feminist projects &mdash; "
              "and entirely quantitative."},
         ]},

        {"type": "content", "label": "Counting The Uncounted", "title": "The politics of the questionnaire",
         "blocks": [
             {"t": "body", "html": "What a survey counts shapes what the state can see. India's "
              "Time Use Survey, by measuring unpaid domestic and care work, made visible an enormous "
              "economy that labour-force statistics had erased."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Counted", "label": "Paid work, formal employment, market output",
                  "color": "green"},
                 {"num": "Long uncounted", "label": "Unpaid care, subsistence, domestic labour &mdash; "
                  "mostly women's", "color": "red"}]},
             {"t": "hbox", "color": "cyan", "html": "Designing the instrument <em>is</em> the "
              "feminist act. The method is conventional; the choice of what to measure is not."},
         ]},

        {"type": "content", "label": "Against Hierarchy", "title": "No method ranks above the others",
         "blocks": [
             {"t": "body", "html": "Feminist methodology resists the hierarchy that crowns "
              "randomised trials as the 'gold standard' and demotes qualitative or participatory "
              "work to mere 'colour'. The right method is the one that fits the question and "
              "respects the people in it."},
             {"t": "hbox", "color": "amber", "html": "Method-as-hierarchy often smuggles in a "
              "politics: the 'rigorous' methods are frequently the ones most distant from "
              "participants' own voices. Fit, not rank."},
         ]},

        {"type": "content", "label": "Mixed Methods", "title": "Numbers and stories, deliberately together",
         "blocks": [
             {"t": "body", "html": "Much strong feminist research is <strong>mixed</strong>: "
              "statistics establish the scale of a pattern; in-depth accounts explain the mechanism "
              "and restore the human meaning the numbers strip away."},
             {"t": "hbox", "color": "cyan", "html": "A figure tells you <em>how many</em> women left "
              "wage work after marriage; a life history tells you <em>why</em>, and what it cost. "
              "Together they make an argument neither could make alone."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Ethics &amp; Non-Extraction"},

        {"type": "content", "label": "Beyond Compliance", "title": "Ethics is more than a form to sign",
         "blocks": [
             {"t": "body", "html": "Institutional ethics review &mdash; consent forms, approvals "
              "&mdash; is a floor, not a ceiling. Feminist ethics asks a harder, ongoing question: "
              "is this whole relationship <strong>fair</strong> to the people who give us their time "
              "and trust?"},
             {"t": "hbox", "color": "cyan", "html": "A study can be fully 'IRB-approved' and still be "
              "extractive, careless or harmful. Compliance and ethics are not the same thing."},
         ]},

        {"type": "content", "label": "Consent", "title": "Consent as relationship, not signature",
         "blocks": [
             {"t": "bullets", "items": [
                 "Genuine consent is <strong>ongoing</strong> &mdash; it can be withdrawn at any time",
                 "It is informed only if people grasp how data will be used and shared",
                 "It must be free of coercion &mdash; hard when the researcher controls access to a scheme",
                 "A thumbprint on an unexplained form is not consent"]},
             {"t": "hbox", "color": "red", "html": "Where the researcher is linked to a programme "
              "people need, 'no' may not feel safe to say. Real consent requires that refusal carry "
              "no cost."},
         ]},

        {"type": "content", "label": "Care", "title": "An ethic of care in the field",
         "blocks": [
             {"t": "term", "word": "Ethic of care",
              "def": "An approach to research ethics grounded in attentiveness, responsibility and "
              "responsiveness to people in relationship &mdash; rather than only abstract rules and "
              "rights. It asks what those involved actually need, here and now."},
             {"t": "body", "html": "Asking a woman to recount violence or loss can re-open it. An "
              "ethic of care means knowing your limits, having referral support ready, and never "
              "treating a person's pain as merely a 'rich' data point."},
         ]},

        {"type": "content", "label": "Non-Extraction", "title": "Against the extractive model",
         "blocks": [
             {"t": "body", "html": "The extractive model is familiar: arrive, collect, leave, "
              "publish elsewhere &mdash; the value flows out, the community sees nothing back. "
              "Feminist ethics names this as a harm, not a neutral default."},
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 900 200" width="100%" style="max-height:200px">'
                 '<defs><marker id="ar2" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">'
                 '<path d="M0,0 L8,4 L0,8 Z" fill="#EF4444"/></marker>'
                 '<marker id="ar3" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto">'
                 '<path d="M0,0 L8,4 L0,8 Z" fill="#10B981"/></marker></defs>'
                 '<text x="225" y="30" text-anchor="middle" fill="#f87171" font-size="15" font-weight="700">Extractive</text>'
                 '<circle cx="120" cy="110" r="42" fill="rgba(148,163,184,0.12)" stroke="#94a3b8"/>'
                 '<text x="120" y="115" text-anchor="middle" fill="#cbd5e1" font-size="12">community</text>'
                 '<circle cx="330" cy="110" r="42" fill="rgba(148,163,184,0.12)" stroke="#94a3b8"/>'
                 '<text x="330" y="115" text-anchor="middle" fill="#cbd5e1" font-size="12">researcher</text>'
                 '<line x1="162" y1="100" x2="288" y2="100" stroke="#EF4444" stroke-width="2.5" marker-end="url(#ar2)"/>'
                 '<text x="225" y="92" text-anchor="middle" fill="#f87171" font-size="11">data, time, stories</text>'
                 '<text x="675" y="30" text-anchor="middle" fill="#34d399" font-size="15" font-weight="700">Reciprocal</text>'
                 '<circle cx="570" cy="110" r="42" fill="rgba(16,185,129,0.12)" stroke="#10B981"/>'
                 '<text x="570" y="115" text-anchor="middle" fill="#5eead4" font-size="12">community</text>'
                 '<circle cx="780" cy="110" r="42" fill="rgba(16,185,129,0.12)" stroke="#10B981"/>'
                 '<text x="780" y="115" text-anchor="middle" fill="#5eead4" font-size="12">researcher</text>'
                 '<line x1="612" y1="96" x2="738" y2="96" stroke="#10B981" stroke-width="2.5" marker-end="url(#ar3)"/>'
                 '<line x1="738" y1="124" x2="612" y2="124" stroke="#10B981" stroke-width="2.5" marker-end="url(#ar3)"/>'
                 '</svg>')},
         ]},

        {"type": "content", "label": "Giving Back", "title": "What reciprocity can look like",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Form", "Example", "Cost to you"],
              "rows": [
                  ["Share findings", "Return results in local language, accessibly", "Low"],
                  ["Recognition", "Credit local researchers and contributors", "Low"],
                  ["Capacity", "Train community members in the methods", "Medium"],
                  ["Material", "Fair compensation for time given", "Medium"],
                  ["Co-ownership", "Community shapes questions and outputs", "High"]]},
             {"t": "hbox", "color": "green", "html": "Reciprocity need not be grand. The minimum is "
              "this: the people you studied should be able to see, use and benefit from what you found."},
         ]},

        {"type": "content", "label": "Representation", "title": "The politics of how you portray people",
         "blocks": [
             {"t": "body", "html": "How you write people up is an ethical act. Will you portray them "
              "as passive victims, exotic others, or numbers &mdash; or as agents with knowledge, "
              "strategy and dignity? Representation can restore or strip away."},
             {"t": "hbox", "color": "red", "html": "The 'poor rural woman' as a helpless figure to "
              "be rescued is a representation that serves the rescuer. Watch for it in your own "
              "drafts."},
         ]},

        {"type": "content", "label": "Do No Harm", "title": "Anticipate harm beyond the interview",
         "blocks": [
             {"t": "bullets", "color": "amber", "items": [
                 "Could publication expose or endanger a participant in their community?",
                 "Could disaggregated data re-identify someone in a small village?",
                 "Could your questions strain relationships you will leave behind?",
                 "Who is accountable to participants once you have gone?"]},
             {"t": "hbox", "color": "cyan", "html": "You leave the field; they do not. Harm that "
              "lands after you depart is still harm you helped cause."},
         ]},

        {"type": "content", "label": "Ownership", "title": "Whose data is it, and who decides?",
         "blocks": [
             {"t": "body", "html": "Feminist ethics presses on ownership: who holds the data, who "
              "controls its later use, who profits from it? Communities are increasingly asserting "
              "<strong>data sovereignty</strong> &mdash; the right to govern data about themselves."},
             {"t": "hbox", "color": "amber", "html": "India's data-protection regime sets a legal "
              "floor for personal data. Feminist ethics asks for more: not just lawful handling, but "
              "just relationships."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Reflexivity &amp; Relationships"},

        {"type": "content", "label": "The Relationship", "title": "Research is a human relationship",
         "blocks": [
             {"t": "body", "html": "An interview is not data extraction from a unit; it is an "
              "encounter between people, shaped by who they each are. Feminist research treats the "
              "<strong>relationship itself</strong> as part of the data, not noise to be controlled away."},
             {"t": "hbox", "color": "cyan", "html": "Who you are changes what people tell you. That "
              "is not a flaw to eliminate &mdash; it is information to understand and report."},
         ]},

        {"type": "content", "label": "Insider / Outsider", "title": "Being inside or outside the group",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Insider", "Outsider"],
              "rows": [
                  ["Access", "Trust, shared language, context", "May need brokers and time"],
                  ["Blind spots", "Takes the familiar for granted", "Misreads the unfamiliar"],
                  ["What's shared", "People assume you already know", "People explain from scratch"],
                  ["Risk", "Over-identification", "Distance, projection"]]},
             {"t": "hbox", "color": "amber", "html": "Neither is simply 'better'. Each sees and "
              "misses different things &mdash; and most researchers are partly both, on different "
              "axes, at the same time."},
         ]},

        {"type": "content", "label": "Beyond The Binary", "title": "Most positions are 'in-between'",
         "blocks": [
             {"t": "body", "html": "The insider/outsider line is rarely clean. A woman researcher "
              "interviewing women shares gender but may differ in caste, class, language and power. "
              "You are usually insider on some axes and outsider on others, all at once."},
             {"t": "hbox", "color": "cyan", "html": "The honest question is not 'am I an insider?' "
              "but 'on which dimensions, and how does each shape what I am told?'"},
         ]},

        {"type": "content", "label": "Power In The Field", "title": "Power flows in more than one direction",
         "blocks": [
             {"t": "body", "html": "The researcher usually holds more institutional power &mdash; "
              "but not always all of it. A village elite, a male gatekeeper or a guarded respondent "
              "can control access, steer the conversation, or decide what stays unsaid."},
             {"t": "hbox", "color": "indigo", "html": "Map the power in each encounter honestly. "
              "Sometimes you hold it; sometimes you are managed by those you came to study. Both "
              "shape the knowledge produced."},
         ]},

        {"type": "content", "label": "Emotion", "title": "Emotions in the field are data, not weakness",
         "blocks": [
             {"t": "body", "html": "Mainstream method treats the researcher's feelings as "
              "contamination to be suppressed. Feminist research takes <strong>emotion</strong> "
              "seriously: discomfort, anger, grief and rapport are signals about the relationship "
              "and the power within it."},
             {"t": "hbox", "color": "amber", "html": "Your unease in an interview may be telling you "
              "something true about the power at play. Note it; do not just edit it out."},
         ]},

        {"type": "content", "label": "Doing Reflexivity", "title": "Reflexivity as a daily practice",
         "blocks": [
             {"t": "flow", "steps": [
                 "BEFORE: name your position and assumptions",
                 "DURING: keep a reflexive field journal",
                 "ANALYSIS: ask how your lens shaped the reading",
                 "WRITING: report your influence, do not hide it"]},
             {"t": "hbox", "color": "green", "html": "A reflexive journal &mdash; recording your "
              "reactions, surprises and unease alongside the field notes &mdash; is the single most "
              "practical reflexivity habit you can build."},
         ]},

        {"type": "content", "label": "The Reflexive Account", "title": "What belongs in the write-up",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Who you are, on the axes that mattered to this study",
                 "How you gained access, and through whom",
                 "How your presence likely shaped what was said",
                 "What your position let you see &mdash; and what it likely obscured"]},
             {"t": "hbox", "color": "red", "html": "Done badly, this becomes self-indulgent "
              "navel-gazing. Done well, it is analysis: it shows the reader how to weigh your "
              "findings."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Decolonial &amp; Southern Feminisms"},

        {"type": "content", "label": "The Critique", "title": "Whose feminism? Whose 'Third World woman'?",
         "blocks": [
             {"t": "body", "html": "By the 1980s, feminists from the global South challenged a "
              "Western feminism that claimed to speak for all women &mdash; while universalising a "
              "white, middle-class, Western experience and casting other women as backward objects "
              "of rescue."},
             {"t": "hbox", "color": "cyan", "html": "The challenge came from within feminism, not "
              "against it: a demand that feminist research examine its <em>own</em> power and "
              "partiality, exactly as it asked of science."},
         ]},

        {"type": "content", "label": "Mohanty", "title": "Chandra Mohanty, 'Under Western Eyes', 1984",
         "blocks": [
             {"t": "body", "html": "In her influential 1984 essay, Chandra Talpade Mohanty argued "
              "that much Western feminist scholarship constructed a single, monolithic "
              "<strong>'Third World woman'</strong> &mdash; poor, powerless, tradition-bound, "
              "victimised &mdash; defined only by lack, against an implicit Western norm of the "
              "free, modern woman."},
             {"t": "term", "word": "The 'Third World woman' (as critique)",
              "def": "Mohanty's term for a flattened, homogenising image produced by some Western "
              "feminist writing &mdash; erasing the diversity, agency and specific histories of "
              "actual women across the global South."},
         ]},

        {"type": "content", "label": "The Method Lesson", "title": "What Mohanty asks of research",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Do not treat 'women' as one undifferentiated, ready-made group",
                 "Study women as agents embedded in specific histories and structures",
                 "Watch how your categories may impose a Western norm as universal",
                 "Refuse the rescue narrative; attend to context, struggle and capacity"]},
             {"t": "hbox", "color": "amber", "html": "Mohanty's essay is a methodological warning as "
              "much as a political one: homogenising your subjects is also a <em>research error</em>."},
         ]},

        {"type": "content", "label": "Indian Feminist Scholarship", "title": "A rich, distinct tradition",
         "blocks": [
             {"t": "body", "html": "South Asian feminist scholarship developed its own questions: "
              "the household as a site of inequality, women's invisible labour, the politics of "
              "personal law, the gendered violence of Partition, and the inseparability of "
              "patriarchy from <strong>caste</strong>."},
             {"t": "hbox", "color": "cyan", "html": "Landmark collaborative work documented women's "
              "own accounts of Partition and the women's movement &mdash; insisting that Indian "
              "women's histories be written from Indian women's voices."},
         ]},

        {"type": "content", "label": "Caste", "title": "Caste and the limits of 'global sisterhood'",
         "blocks": [
             {"t": "body", "html": "Dalit feminists pressed a hard internal critique: mainstream "
              "Indian feminism, led largely by upper-caste women, often universalised <em>its</em> "
              "experience &mdash; reproducing inside feminism the very dominance feminism opposed."},
             {"t": "hbox", "color": "red", "html": "A 'sisterhood of all women' that ignores caste "
              "is not neutral &mdash; it quietly centres the upper-caste woman. The same move "
              "Mohanty named globally operates within the nation too."},
         ]},

        {"type": "content", "label": "Echoes", "title": "The same structure, at every scale",
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 900 220" width="100%" style="max-height:220px">'
                 '<rect x="60" y="40" width="780" height="150" rx="12" fill="rgba(99,102,241,0.07)" stroke="#6366F1" stroke-dasharray="5 4"/>'
                 '<text x="450" y="66" text-anchor="middle" fill="#818cf8" font-size="13">Western feminism speaks for &rarr; the global South</text>'
                 '<rect x="160" y="80" width="580" height="100" rx="10" fill="rgba(14,165,233,0.08)" stroke="#0EA5E9" stroke-dasharray="5 4"/>'
                 '<text x="450" y="106" text-anchor="middle" fill="#38bdf8" font-size="13">Elite Indian feminism speaks for &rarr; all Indian women</text>'
                 '<rect x="280" y="118" width="340" height="56" rx="8" fill="rgba(239,68,68,0.10)" stroke="#EF4444" stroke-dasharray="5 4"/>'
                 '<text x="450" y="150" text-anchor="middle" fill="#f87171" font-size="13">Upper-caste women speak for &rarr; Dalit women</text>'
                 '</svg>')},
             {"t": "hbox", "color": "amber", "html": "The lesson nests at every scale: whoever holds "
              "power within a movement can universalise their own partial view. Always ask who is "
              "speaking <em>for</em> whom."},
         ]},

        {"type": "content", "label": "Decolonising Method", "title": "Decolonising research practice",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Take Southern theorists as theorists, not just sources of raw data",
                 "Cite and build on regional scholarship, not only Western canon",
                 "Question imported categories &mdash; do they fit this context?",
                 "Shift authority over the research toward the communities studied"]},
             {"t": "hbox", "color": "cyan", "html": "Decolonising is not rejecting all Western theory; "
              "it is refusing to treat it as the only theory, and the South as mere fieldwork."},
         ]},

        {"type": "content", "label": "Standpoint, Returned", "title": "Why this is the heart of the course",
         "blocks": [
             {"t": "body", "html": "Notice the full circle. Decolonial and Dalit feminisms apply "
              "standpoint theory and situated knowledge <em>to feminism itself</em> &mdash; "
              "insisting that the most marginalised see what the relatively powerful, even within "
              "feminism, cannot."},
             {"t": "quote",
              "text": "There is no view from nowhere &mdash; not even a feminist one.",
              "attr": "&mdash; the recurring lesson of this course"},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Doing It &amp; Further Reading"},

        {"type": "content", "label": "From Theory To Practice", "title": "Turning commitments into choices",
         "blocks": [
             {"t": "body", "html": "Feminist research is not a doctrine to admire but a practice to "
              "do. Every stage &mdash; question, design, fieldwork, analysis, writing &mdash; offers "
              "a choice between reproducing power and answering back to it."},
             {"t": "flow", "steps": [
                 "QUESTION: whose problem, framed how?",
                 "DESIGN: who is counted, who defines the categories?",
                 "FIELD: what relationship, what care?",
                 "WRITE: whose voice, what representation?"]},
         ]},

        {"type": "content", "label": "The Checklist (1)", "title": "Before you start: ask yourself",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Whose question is this &mdash; and who decided it was worth asking?",
                 "Where do I stand in relation to the people I will study?",
                 "Which intersections of power matter most in this context?",
                 "Who is likely to be missing from my frame, and why?",
                 "What will the people I study get back from this?"]},
         ]},

        {"type": "content", "label": "The Checklist (2)", "title": "During and after: keep asking",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Are my categories letting people speak, or flattening them?",
                 "How is my presence shaping what I am being told?",
                 "Am I disaggregating enough to see who is left behind?",
                 "Could this analysis or write-up harm or expose anyone?",
                 "Does my account say from where it was made?"]},
             {"t": "hbox", "color": "amber", "html": "Print these ten questions. Revisit them at "
              "design, midline and write-up. They are the course, made portable."},
         ]},

        {"type": "content", "label": "D'Ignazio &amp; Klein", "title": "Data Feminism: seven principles",
         "compact": True,
         "blocks": [
             {"t": "body", "html": "Catherine D'Ignazio and Lauren Klein's <em>Data Feminism</em> "
              "(2020) brings these ideas to data science. A condensed sense of their principles:"},
             {"t": "table",
              "head": ["Principle", "In short"],
              "rows": [
                  ["Examine &amp; challenge power", "Ask how data entrenches inequality"],
                  ["Elevate emotion &amp; embodiment", "Value lived, felt experience as knowledge"],
                  ["Rethink binaries &amp; hierarchies", "Question the categories data imposes"],
                  ["Embrace pluralism", "Centre multiple, situated perspectives"],
                  ["Consider context", "No data speaks neutrally, stripped of its origins"],
                  ["Make labour visible", "Name whose work produced the data"]]},
         ]},

        {"type": "content", "label": "Reading List (1)", "title": "Foundational texts",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Sandra Harding &mdash; <em>Whose Science? Whose Knowledge?</em> (standpoint, strong objectivity)",
                 "Donna Haraway &mdash; <em>Situated Knowledges</em> (1988 essay; the god trick)",
                 "Patricia Hill Collins &mdash; <em>Black Feminist Thought</em> (matrix of domination)",
                 "Kimberle Crenshaw &mdash; the 1989 essay coining intersectionality",
                 "Dorothy Smith &mdash; <em>The Everyday World as Problematic</em> (institutional ethnography)"]},
         ]},

        {"type": "content", "label": "Reading List (2)", "title": "Southern, decolonial &amp; practical",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Chandra Talpade Mohanty &mdash; <em>Under Western Eyes</em> (1984) and after",
                 "Indian feminist scholarship on women's work, caste and the household",
                 "Dalit feminist writing on the limits of 'global sisterhood'",
                 "D'Ignazio &amp; Klein &mdash; <em>Data Feminism</em> (2020)",
                 "Feminist oral histories of Partition and the women's movement"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Research Ethics</strong>, <strong>Qualitative Methods</strong> and "
              "<strong>Data Literacy</strong> 101 courses."},
         ]},

        {"type": "content", "label": "Misreadings To Avoid", "title": "What to carry, and what to drop",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Drop the idea that&hellip;", "Carry the idea that&hellip;"],
              "rows": [
                  ["It's just 'research about women'", "It's a stance on power in all knowledge"],
                  ["It means avoiding numbers", "It counts what others ignore"],
                  ["Reflexivity is a confession", "Reflexivity is analysis"],
                  ["Intersectionality is adding labels", "It is studying interlocking systems"],
                  ["Objectivity is the enemy", "Owning your position makes you more objective"]]},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Knowledge is produced, not found</strong> &mdash; examine the making",
                 "<strong>There is no view from nowhere</strong> &mdash; name where yours is from",
                 "<strong>Power runs through method</strong> &mdash; not just through the topic",
                 "<strong>Study intersecting systems</strong> &mdash; caste, class and gender together",
                 "<strong>Research is a relationship</strong> &mdash; make it reciprocal, not extractive"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Feminist Research 101 &middot; Complete",
         "headline": "Now ask: true for<br>whom, told by whom?",
         "byline": "Feminist research is not a niche &mdash; it is a discipline of honesty about "
                   "power in every study you read or run. Carry the questions into your next "
                   "proposal, survey and report. Explore the rest of the ImpactMojo 101 Series, "
                   "free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Research Tracks", "href": "https://www.impactmojo.in/catalog.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
