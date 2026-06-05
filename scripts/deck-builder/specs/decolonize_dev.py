# -*- coding: utf-8 -*-
"""
Decolonial Development 101 — ImpactMojo 101 Series (native deck spec)
A critical-theory primer on decolonising development for practitioners,
researchers and students in the Global South / South Asia.
Build: python3 scripts/deck-builder/build.py decolonize_dev
"""

DECK = {
    "slug": "decolonize-dev",
    "title": "Decolonial Development 101",
    "description": ("Decolonial Development 101 — a free foundational course for "
                    "practitioners, researchers and students in the Global South and South "
                    "Asia. From the colonial roots of 'development' and the coloniality of "
                    "power to epistemic injustice, decolonising aid and research, and "
                    "post-development alternatives like buen vivir, ubuntu and swaraj. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Decolonial<br>Development<br>101",
         "sub": "Unlearning the &lsquo;Civilising Mission&rsquo; &mdash; a Foundational Course "
                "on Decolonising Development for the Global South &amp; South Asia",
         "tags": ["Critical Theory", "Global South Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What &lsquo;Decolonising Development&rsquo; Means"},
             {"name": "The Colonial Roots of &lsquo;Development&rsquo;"},
             {"name": "Eurocentrism, Knowledge &amp; Power"},
             {"name": "Critiques of the Mainstream"},
             {"name": "Coloniality"},
             {"name": "Whose Knowledge Counts"},
             {"name": "Decolonising Aid &amp; the NGO Sector"},
             {"name": "Decolonising Research &amp; Data"},
             {"name": "Post-Development &amp; Alternatives"},
             {"name": "Decolonising Practice"},
             {"name": "Tensions, Critiques &amp; Further Reading"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What &lsquo;Decolonising Development&rsquo; Means"},

        {"type": "content", "label": "Starting Point", "title": "Beyond a buzzword",
         "blocks": [
             {"t": "body", "html": "&lsquo;Decolonising&rsquo; is everywhere &mdash; in funding "
              "calls, conference titles and job descriptions. Used loosely it becomes a slogan "
              "that changes nothing. This course treats it as a serious analytical project: "
              "naming how colonial power still shapes who develops whom, with whose knowledge, "
              "in whose interest."},
             {"t": "hbox", "color": "cyan", "html": "Decolonising development is not a rebrand. "
              "It asks who holds power over the very idea of &lsquo;development&rsquo; &mdash; and "
              "whether that idea can be remade or must be left behind."},
         ]},

        {"type": "content", "label": "Definition", "title": "Decolonising development, defined",
         "blocks": [
             {"t": "term", "word": "Decolonising development",
              "def": "A critical and practical project that exposes and undoes the colonial "
              "relations of power, knowledge and economy embedded in development &mdash; "
              "challenging who sets agendas, whose knowledge counts, where resources flow, and "
              "whose vision of a good life prevails."},
             {"t": "body", "cls": "sm", "html": "It works at three levels at once: <strong>"
              "knowledge</strong> (whose ideas are authoritative), <strong>power</strong> (who "
              "decides), and <strong>economy</strong> (who owns and profits)."},
         ]},

        {"type": "content", "label": "What It Is Not", "title": "What decolonising is &mdash; and is not",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Decolonising is&hellip;", "Decolonising is not&hellip;"],
              "rows": [
                  ["Shifting power and resources", "A diversity photo on a report"],
                  ["Questioning whose knowledge counts", "A new mission statement alone"],
                  ["Structural &mdash; agendas, funding, ownership", "A workshop you attend once"],
                  ["Often uncomfortable for institutions", "Comfortable and costless"],
                  ["About relations, not just representation", "Hiring one local and stopping"]]},
             {"t": "hbox", "color": "red", "html": "Beware &lsquo;decolonisation as metaphor&rsquo;: "
              "language that signals virtue while leaving money, control and authority exactly "
              "where they were."},
         ]},

        {"type": "content", "label": "Three Registers", "title": "Decolonial, postcolonial, anti-colonial",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [
                  {"t": "bullets", "items": [
                      "<strong>Anti-colonial:</strong> the political struggle to end direct "
                      "colonial rule (Fanon, the independence movements)",
                      "<strong>Postcolonial:</strong> analysing culture, identity and discourse "
                      "after empire (Said, Spivak, Bhabha)",
                      "<strong>Decolonial:</strong> a Latin American school centring "
                      "&lsquo;coloniality&rsquo; &mdash; the lasting structures of power "
                      "(Quijano, Mignolo)"]}],
              "right": [
                  {"t": "hbox", "color": "indigo", "html": "Overlapping, not identical. This "
                   "course draws on all three but leans on the <em>decolonial</em> idea that "
                   "colonialism ended while coloniality lives on."}]},
         ]},

        {"type": "content", "label": "Why It Matters Here", "title": "Why this matters in South Asia",
         "blocks": [
             {"t": "body", "html": "South Asia was both a laboratory of empire and a cradle of "
              "anti-colonial thought &mdash; from the drain of wealth debates to Gandhi&rsquo;s "
              "swaraj. Yet much of its development sector still imports frameworks, metrics and "
              "&lsquo;best practice&rsquo; designed elsewhere."},
             {"t": "hbox", "color": "amber", "html": "The question is sharp for practitioners: "
              "are we delivering an externally authored model of progress, or building one rooted "
              "in the histories and aspirations of the people we serve?"},
         ]},

        {"type": "content", "label": "A Spectrum", "title": "Three ways the sector responds",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Cosmetic", "label": "New words, same structures &mdash; &lsquo;decolonising&rsquo; "
                  "as a logo refresh", "color": "red"},
                 {"num": "Reformist", "label": "Shift real power and funding within the existing "
                  "system &mdash; localisation, #ShiftThePower", "color": "amber"},
                 {"num": "Radical", "label": "Question development itself &mdash; post-development, "
                  "the pluriverse", "color": "green"}]},
             {"t": "hbox", "color": "indigo", "html": "This course visits all three. You need not "
              "pick one to take every one seriously &mdash; but you must tell them apart."},
         ]},

        {"type": "content", "label": "Stakes", "title": "Whose questions are we even asking?",
         "blocks": [
             {"t": "flow", "steps": [
                 "WHO defines the problem (&lsquo;underdevelopment&rsquo;)?",
                 "WHO sets the goal (the &lsquo;developed&rsquo; benchmark)?",
                 "WHOSE knowledge counts as expertise?",
                 "WHO owns the resources and the results?"]},
             {"t": "hbox", "color": "cyan", "html": "Decolonising development means refusing to "
              "treat these as settled. Every answer was historically produced &mdash; and can be "
              "produced differently."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course unfolds",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Diagnosis", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Colonial roots of &lsquo;development&rsquo;",
                      "Eurocentrism, knowledge &amp; power",
                      "Mainstream critiques &amp; coloniality",
                      "Whose knowledge counts"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Response", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Decolonising aid, research &amp; data",
                      "Post-development &amp; alternatives",
                      "Concrete shifts in practice",
                      "Tensions, critiques &amp; reading"]}]}]},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Colonial Roots of &lsquo;Development&rsquo;"},

        {"type": "content", "label": "Origins", "title": "&lsquo;Development&rsquo; has a history, not just a meaning",
         "blocks": [
             {"t": "body", "html": "We talk of development as if it were a timeless, neutral goal. "
              "But the modern idea &mdash; some countries are &lsquo;developed&rsquo;, others must "
              "catch up &mdash; is a twentieth-century invention with deep colonial roots."},
             {"t": "quote", "text": "Development was the conceptual heir of the civilising "
              "mission: the same hierarchy of peoples, with the vocabulary changed.",
              "attr": "&mdash; a recurring claim in critical development studies"},
         ]},

        {"type": "content", "label": "The Civilising Mission", "title": "From &lsquo;civilising&rsquo; to &lsquo;developing&rsquo;",
         "blocks": [
             {"t": "term", "word": "The civilising mission",
              "def": "The colonial justification that European rule uplifted &lsquo;backward&rsquo; "
              "peoples &mdash; the mission civilisatrice, the &lsquo;white man&rsquo;s burden&rsquo; "
              "&mdash; casting domination as benevolence and tutelage."},
             {"t": "hbox", "color": "amber", "html": "Strip away the racial language and the "
              "structure survives: an advanced party guiding a deficient one toward a single, "
              "predefined destination. That structure migrated into &lsquo;development&rsquo;."},
         ]},

        {"type": "content", "label": "Macaulay", "title": "Educating the colonised in the coloniser&rsquo;s image",
         "blocks": [
             {"t": "body", "html": "Thomas Macaulay&rsquo;s 1835 <em>Minute on Indian Education</em> "
              "openly aimed to form &lsquo;a class&hellip; Indian in blood and colour, but English "
              "in taste, in opinions, in morals and in intellect&rsquo; &mdash; dismissing Indian "
              "and Arabic learning wholesale."},
             {"t": "hbox", "color": "red", "html": "Here is coloniality of knowledge in plain "
              "view: native learning declared worthless, the coloniser&rsquo;s curriculum installed "
              "as universal. Its institutional legacy long outlived the Raj."},
         ]},

        {"type": "content", "label": "Truman 1949", "title": "Point Four and the birth of &lsquo;underdevelopment&rsquo;",
         "blocks": [
             {"t": "body", "html": "On 20 January 1949, in his inaugural address, US President "
              "Harry Truman announced <strong>Point Four</strong>: a programme of technical aid "
              "for &lsquo;underdeveloped areas&rsquo;. With that word, half the world was "
              "re-described overnight."},
             {"t": "quote", "text": "We must embark on a bold new program for&hellip; the "
              "improvement and growth of underdeveloped areas.",
              "attr": "&mdash; Harry S. Truman, Inaugural Address, 20 Jan 1949 (Point Four)"},
         ]},

        {"type": "content", "label": "The Invention", "title": "Naming a problem into existence",
         "blocks": [
             {"t": "body", "html": "Arturo Escobar argues that &lsquo;underdevelopment&rsquo; was "
              "not discovered but <strong>invented</strong> &mdash; the moment diverse societies "
              "were lumped together as a deficient mass, defined by what they lacked relative to "
              "the United States."},
             {"t": "flow", "steps": [
                 "Define a norm: the US/Western standard of living",
                 "Measure others against it (GDP per capita)",
                 "Label the gap: &lsquo;underdevelopment&rsquo;",
                 "Prescribe the cure: &lsquo;development&rsquo;"]},
         ]},

        {"type": "content", "label": "The Development Era", "title": "An age of plans, experts and aid",
         "blocks": [
             {"t": "body", "html": "The decades after 1949 institutionalised development: the "
              "World Bank and IMF (Bretton Woods, 1944), bilateral aid agencies, five-year plans, "
              "the &lsquo;Decade of Development&rsquo; (the 1960s) and an emerging class of "
              "international experts."},
             {"t": "hbox", "color": "indigo", "html": "Decolonisation of territory and the rise "
              "of development overlapped almost exactly. As flags changed, a new, subtler form of "
              "external guidance moved in."},
         ]},

        {"type": "content", "label": "Continuity", "title": "Colonial economy did not simply end",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Inherited structures", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Commodity exports, manufactured imports",
                      "Infrastructure built to extract, not connect",
                      "Borders drawn by imperial convenience"]}]}],
              "right": [{"t": "panel", "color": "amber", "title": "New dependencies", "blocks": [
                  {"t": "bullets", "sm": True, "color": "amber", "items": [
                      "Sovereign debt &amp; conditionalities",
                      "Aid tied to donor goods &amp; consultants",
                      "Terms of trade tilted to the core"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Independence transferred political authority "
              "without dismantling the economic architecture of empire."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Development carries its origins",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "The idea is recent, not eternal &mdash; born around 1949",
                 "It inherited the hierarchy of the civilising mission",
                 "&lsquo;Underdevelopment&rsquo; was constructed, then treated as fact",
                 "Decolonising means seeing this history inside today&rsquo;s practice"]},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Eurocentrism, Knowledge &amp; Power"},

        {"type": "content", "label": "The Core Claim", "title": "Knowledge is never innocent of power",
         "blocks": [
             {"t": "body", "html": "A central decolonial insight, drawn from Michel Foucault and "
              "radicalised by postcolonial thinkers: <strong>knowledge and power produce each "
              "other</strong>. To define and describe a people is already to exercise power over "
              "them."},
             {"t": "term", "word": "Eurocentrism",
              "def": "Treating European history, categories and experience as the universal "
              "standard against which all societies are measured &mdash; so that other knowledges "
              "appear partial, local or primitive."},
         ]},

        {"type": "content", "label": "Said 1978", "title": "Edward Said&rsquo;s <em>Orientalism</em>",
         "blocks": [
             {"t": "body", "html": "In <em>Orientalism</em> (1978), Edward Said showed how Western "
              "scholarship constructed &lsquo;the Orient&rsquo; as exotic, irrational and "
              "unchanging &mdash; a mirror that flattered the West as rational and modern, and "
              "justified ruling over it."},
             {"t": "quote", "text": "The Orient was almost a European invention.",
              "attr": "&mdash; Edward Said, Orientalism (1978)"},
         ]},

        {"type": "content", "label": "How It Works", "title": "Representation as domination",
         "blocks": [
             {"t": "flow", "steps": [
                 "The West produces knowledge ABOUT the East",
                 "That knowledge defines the East as inferior &amp; static",
                 "The definition justifies intervention &amp; rule",
                 "Rule produces more &lsquo;knowledge&rsquo; &mdash; the loop closes"]},
             {"t": "hbox", "color": "amber", "html": "Said&rsquo;s point: who gets to represent "
              "whom is a question of power. The expert report on &lsquo;them&rsquo;, written "
              "&lsquo;there&rsquo;, is part of the apparatus."},
         ]},

        {"type": "content", "label": "Escobar 1995", "title": "Arturo Escobar&rsquo;s <em>Encountering Development</em>",
         "blocks": [
             {"t": "body", "html": "In <em>Encountering Development</em> (1995), Arturo Escobar "
              "applied a Foucauldian lens to development itself, treating it as a <strong>"
              "discourse</strong>: a whole system of knowledge, institutions and practices that "
              "produces its own objects &mdash; &lsquo;the poor&rsquo;, &lsquo;the Third "
              "World&rsquo;."},
             {"t": "quote", "text": "Development&hellip; created a space in which only certain "
              "things could be said and even imagined.",
              "attr": "&mdash; Arturo Escobar, Encountering Development (1995)"},
         ]},

        {"type": "content", "label": "Development as Discourse", "title": "What a &lsquo;discourse&rsquo; does",
         "blocks": [
             {"t": "term", "word": "Discourse",
              "def": "More than talk: an organised system of statements, categories and "
              "institutions that defines what counts as true, normal and possible &mdash; and "
              "thereby what can even be thought."},
             {"t": "hbox", "color": "indigo", "html": "If development is a discourse, then "
              "tweaking projects inside it is not enough. The categories themselves &mdash; "
              "&lsquo;poverty&rsquo;, &lsquo;the target population&rsquo; &mdash; carry the power."},
         ]},

        {"type": "content", "label": "Manufacturing the Object", "title": "How &lsquo;the poor&rsquo; get made",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "A village before", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Diverse livelihoods, commons, kin networks, "
                   "ways of knowing land and season &mdash; messy, plural, locally meaningful."}]}],
              "right": [{"t": "panel", "color": "red", "title": "A &lsquo;target group&rsquo; after", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Recoded as a poverty line, a deficiency, a "
                   "set of indicators to be raised &mdash; legible to the project, illegible as a "
                   "world."}]}]},
             {"t": "hbox", "color": "amber", "html": "The discourse does not just describe; it "
              "<em>reshapes</em> reality into something the apparatus can act on."},
         ]},

        {"type": "content", "label": "Universals", "title": "The trouble with the &lsquo;universal&rsquo;",
         "blocks": [
             {"t": "body", "html": "Markets, the rational individual, linear progress, the nuclear "
              "household, the modern state &mdash; presented as universal, these are in fact a "
              "<strong>particular</strong> European history dressed up as everyone&rsquo;s future."},
             {"t": "hbox", "color": "cyan", "html": "Decolonising knowledge means re-particularising "
              "the &lsquo;universal&rsquo;: asking where each supposedly neutral category actually "
              "came from, and whom it fits."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Reading the frame, not just the project",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Knowledge about the South is entangled with power over it",
                 "Said: representation can be a form of rule",
                 "Escobar: development is a discourse that makes its own objects",
                 "Ask not only &lsquo;does this project work?&rsquo; but &lsquo;whose categories "
                 "is it working within?&rsquo;"]},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Critiques of the Mainstream"},

        {"type": "content", "label": "The Orthodoxy", "title": "Modernisation theory",
         "blocks": [
             {"t": "body", "html": "The post-war orthodoxy, crystallised in W. W. Rostow&rsquo;s "
              "<em>Stages of Economic Growth</em> (1960), held that all societies climb the same "
              "ladder &mdash; from &lsquo;traditional&rsquo; to &lsquo;high mass consumption&rsquo; "
              "&mdash; if they adopt Western institutions and values."},
             {"t": "term", "word": "Modernisation theory",
              "def": "The view that development is a single, linear path; poor countries are "
              "simply at an earlier stage and must become more like the West to advance."},
         ]},

        {"type": "content", "label": "Hidden Assumptions", "title": "What modernisation theory smuggles in",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "One destination for all &mdash; the Western present",
                 "&lsquo;Tradition&rsquo; as obstacle, not resource",
                 "The obstacle is <em>internal</em> &mdash; culture, attitudes, institutions",
                 "Therefore: history, colonialism and global structure can be ignored"]},
             {"t": "hbox", "color": "amber", "html": "Its deepest move is to locate the cause of "
              "poverty <em>inside</em> poor societies &mdash; conveniently absolving the colonial "
              "and global system that helped produce it."},
         ]},

        {"type": "content", "label": "The Counter-School", "title": "Dependency theory turns the lens around",
         "blocks": [
             {"t": "body", "html": "From Latin America in the 1960s&ndash;70s, <strong>dependency "
              "theory</strong> argued the opposite: poor countries are not &lsquo;behind&rsquo; "
              "but actively <em>under</em>developed &mdash; their poverty produced by the same "
              "global system that enriched the &lsquo;core&rsquo;."},
             {"t": "term", "word": "Dependency",
              "def": "A relationship in which the economies of peripheral countries are shaped by "
              "and subordinated to the needs of dominant &lsquo;core&rsquo; economies &mdash; "
              "growth at the centre conditioned on extraction from the periphery."},
         ]},

        {"type": "content", "label": "Prebisch &amp; Frank", "title": "Prebisch, Frank and &lsquo;the development of underdevelopment&rsquo;",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Ra&uacute;l Prebisch", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Argued that the terms of trade move against "
                   "commodity exporters over time &mdash; the periphery runs to stand still. Led "
                   "ECLA and shaped UNCTAD."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Andre Gunder Frank", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Coined &lsquo;the development of "
                   "underdevelopment&rsquo;: the same process that develops the metropole "
                   "underdevelops the satellite. Same coin, two sides."}]}]},
             {"t": "hbox", "color": "amber", "html": "The radical implication: integration into "
              "the world economy on existing terms may deepen, not cure, underdevelopment."},
         ]},

        {"type": "content", "label": "World-Systems", "title": "Wallerstein: one system, three zones",
         "blocks": [
             {"t": "body", "html": "Immanuel Wallerstein&rsquo;s <strong>world-systems "
              "analysis</strong> scaled the argument up: since the &lsquo;long sixteenth "
              "century&rsquo;, there has been a single capitalist world-economy divided into "
              "<strong>core, periphery and semi-periphery</strong>."},
             {"t": "flow", "steps": [
                 "CORE: high-wage, high-tech, captures surplus",
                 "SEMI-PERIPHERY: mixed, mediating, mobile",
                 "PERIPHERY: low-wage, raw materials, surplus extracted",
                 "ONE system &mdash; the zones are relational, not separate"]},
         ]},

        {"type": "content", "label": "The Big Picture", "title": "From a ladder to a web",
         "blocks": [
             {"t": "table", "compact": True,
              "head": ["", "Modernisation", "Dependency / World-Systems"],
              "rows": [
                  ["Unit of analysis", "The nation, on its own", "The whole global system"],
                  ["Cause of poverty", "Internal: tradition, culture", "External: extraction, structure"],
                  ["Path", "One ladder, all climb it", "Position in a web; mobility is hard"],
                  ["Prescription", "Become more like the West", "Change the terms; sometimes delink"]]},
             {"t": "hbox", "color": "cyan", "html": "These critiques reframed poverty as a "
              "<em>relation</em>, not a stage &mdash; a crucial step toward the decolonial idea "
              "of coloniality."},
         ]},

        {"type": "content", "label": "Where They Fall Short", "title": "Even the critics stayed inside the frame",
         "blocks": [
             {"t": "body", "html": "Dependency and world-systems brilliantly diagnosed economic "
              "structure &mdash; but mostly within a Western, economistic, Marxist frame. They "
              "said little about <strong>knowledge, race, gender and the coloniality of being</strong>."},
             {"t": "hbox", "color": "indigo", "html": "That gap is exactly what the decolonial "
              "school &mdash; Quijano, Mignolo &mdash; set out to fill. To them we now turn."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Three lenses on the same gap",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Modernisation: catch up by becoming Western (poverty is internal)",
                 "Dependency: poverty is produced by extraction (Prebisch, Frank)",
                 "World-systems: one capitalist system, core and periphery (Wallerstein)",
                 "All economic; the decolonial turn adds knowledge, race and being"]},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Coloniality"},

        {"type": "content", "label": "The Key Distinction", "title": "Colonialism ended; coloniality did not",
         "blocks": [
             {"t": "body", "html": "The decolonial school&rsquo;s founding move is to separate two "
              "things usually merged. <strong>Colonialism</strong> was a political event &mdash; "
              "rule by a foreign power &mdash; that mostly ended. <strong>Coloniality</strong> is "
              "the deeper pattern of power it left behind, and which lives on."},
             {"t": "quote", "text": "Coloniality survives colonialism.",
              "attr": "&mdash; Walter Mignolo, paraphrasing the decolonial thesis"},
         ]},

        {"type": "content", "label": "Quijano 2000", "title": "An&iacute;bal Quijano&rsquo;s &lsquo;coloniality of power&rsquo;",
         "blocks": [
             {"t": "term", "word": "Coloniality of power",
              "def": "An&iacute;bal Quijano&rsquo;s concept (notably in &lsquo;Coloniality of "
              "Power, Eurocentrism, and Latin America&rsquo;, 2000): the enduring global "
              "structure, born with colonial conquest, that organises labour, knowledge, "
              "authority and being around a racial hierarchy."},
             {"t": "hbox", "color": "cyan", "html": "Quijano&rsquo;s claim: the modern idea of "
              "<strong>race</strong> was invented to naturalise colonial domination &mdash; and "
              "that racialised order still sorts the world today."},
         ]},

        {"type": "content", "label": "Three Faces", "title": "Power, knowledge and being",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Power", "label": "Who controls labour, land, authority &mdash; sorted by "
                  "a racial hierarchy", "color": "cyan"},
                 {"num": "Knowledge", "label": "Whose ways of knowing count as &lsquo;science&rsquo;; "
                  "others demoted to belief", "color": "indigo"},
                 {"num": "Being", "label": "Whose humanity is full; who is rendered lesser, "
                  "doubted, dispensable", "color": "amber"}]},
             {"t": "hbox", "color": "red", "html": "Coloniality operates on all three at once. "
              "You cannot decolonise the economy while leaving knowledge and being untouched."},
         ]},

        {"type": "content", "label": "Mignolo", "title": "Walter Mignolo and the decolonial option",
         "blocks": [
             {"t": "body", "html": "Walter Mignolo names the underside of modernity: there is no "
              "<strong>modernity without coloniality</strong>. Europe&rsquo;s self-image as "
              "rational and progressive was built on, and required, the domination of others."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Delinking", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Detaching from the assumption that "
                   "European categories are the only valid ones &mdash; epistemic disobedience."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Border thinking", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Thinking from the colonial difference &mdash; "
                   "from the experience and knowledge of those on modernity&rsquo;s margins."}]}]},
         ]},

        {"type": "content", "label": "Modernity/Coloniality", "title": "Two sides of one coin",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;align-items:center;margin:14px 0;">'
                 '<svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;max-width:560px;height:auto;font-family:inherit;">'
                 '<defs><linearGradient id="coinG" x1="0" y1="0" x2="1" y2="0">'
                 '<stop offset="0" stop-color="#0EA5E9"/><stop offset="1" stop-color="#1C1917"/>'
                 '</linearGradient></defs>'
                 '<ellipse cx="280" cy="100" rx="240" ry="78" fill="none" stroke="url(#coinG)" '
                 'stroke-width="3"/>'
                 '<line x1="280" y1="24" x2="280" y2="176" stroke="#F59E0B" stroke-width="2" '
                 'stroke-dasharray="5,5"/>'
                 '<text x="155" y="92" text-anchor="middle" fill="#0EA5E9" font-size="22" '
                 'font-weight="700">MODERNITY</text>'
                 '<text x="155" y="118" text-anchor="middle" fill="#0EA5E9" font-size="12">'
                 'progress &middot; reason &middot; markets</text>'
                 '<text x="405" y="92" text-anchor="middle" fill="#EF4444" font-size="22" '
                 'font-weight="700">COLONIALITY</text>'
                 '<text x="405" y="118" text-anchor="middle" fill="#EF4444" font-size="12">'
                 'conquest &middot; race &middot; extraction</text>'
                 '<text x="280" y="195" text-anchor="middle" fill="#78716C" font-size="11">'
                 'one coin &mdash; the bright face requires the dark</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "Coloniality of Knowledge", "title": "The geopolitics of knowing",
         "blocks": [
             {"t": "body", "html": "Knowledge is presented as placeless and universal, yet it is "
              "produced from <strong>somewhere</strong> &mdash; overwhelmingly a handful of "
              "institutions in the global North. Theory comes from there; the South supplies data "
              "and case studies."},
             {"t": "hbox", "color": "amber", "html": "Decolonial thinkers call this the "
              "&lsquo;hubris of the zero point&rsquo;: the pretence of a view from nowhere that is "
              "actually a view from the centre of power."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Why coloniality changes the task",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Coloniality outlives colonialism &mdash; the structure, not the flag",
                 "Quijano: a racial hierarchy organising power, knowledge and being",
                 "Mignolo: no modernity without coloniality; delink and think from the border",
                 "So decolonising is not &lsquo;more development&rsquo; but a different relation to "
                 "power and knowledge"]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Whose Knowledge Counts"},

        {"type": "content", "label": "The Question", "title": "Knowledge has a hierarchy",
         "blocks": [
             {"t": "body", "html": "Not all knowledge is treated equally. A randomised trial counts "
              "as &lsquo;evidence&rsquo;; a farmer&rsquo;s reading of the monsoon or an elder&rsquo;s "
              "account of a forest is filed under &lsquo;belief&rsquo;, &lsquo;anecdote&rsquo; or "
              "&lsquo;folklore&rsquo;."},
             {"t": "term", "word": "Epistemic injustice",
              "def": "Harm done to someone specifically as a knower &mdash; when their testimony "
              "is unfairly doubted, or when the shared concepts needed to make sense of their "
              "experience are missing or suppressed."},
         ]},

        {"type": "content", "label": "Two Forms", "title": "Testimonial and hermeneutical injustice",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Testimonial", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A speaker is given less credibility because "
                   "of who they are &mdash; the illiterate, the rural, the woman, the Adivasi &mdash; "
                   "regardless of what they know."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Hermeneutical", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A whole group&rsquo;s experience cannot be "
                   "voiced because the dominant vocabulary has no words for it &mdash; the gap "
                   "itself is an injustice."}]}]},
             {"t": "hbox", "color": "amber", "html": "After Miranda Fricker. Both forms quietly "
              "shape whose evidence reaches a development decision &mdash; and whose never does."},
         ]},

        {"type": "content", "label": "Spivak 1988", "title": "Spivak: &lsquo;Can the Subaltern Speak?&rsquo;",
         "blocks": [
             {"t": "body", "html": "In her 1988 essay <em>Can the Subaltern Speak?</em>, Gayatri "
              "Chakravorty Spivak asks whether the most marginalised &mdash; the &lsquo;"
              "subaltern&rsquo; &mdash; can be heard at all within structures built by colonial "
              "and patriarchal power."},
             {"t": "quote", "text": "Can the subaltern speak? &mdash; or only ever be spoken for?",
              "attr": "&mdash; after Gayatri C. Spivak, &lsquo;Can the Subaltern Speak?&rsquo; (1988)"},
         ]},

        {"type": "content", "label": "The Sharp Edge", "title": "Speaking <em>for</em> versus making space to speak",
         "blocks": [
             {"t": "body", "html": "Spivak&rsquo;s warning cuts at well-meaning development too. "
              "Even those who claim to give voice to the oppressed may, in the act of representing "
              "them, talk <em>over</em> them &mdash; translating their reality into the "
              "expert&rsquo;s terms."},
             {"t": "hbox", "color": "red", "html": "The honest question is not &lsquo;how do we "
              "speak for them?&rsquo; but &lsquo;what structures stop them from being heard &mdash; "
              "and how do we dismantle those?&rsquo;"},
         ]},

        {"type": "content", "label": "Indigenous &amp; Local Knowledge", "title": "Knowledge that the frame ignores",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Agro-ecology:</strong> seed diversity, intercropping, soil and water "
                 "wisdom honed over generations",
                 "<strong>Medicine:</strong> rich pharmacopoeias, later mined and patented from "
                 "outside",
                 "<strong>Ecology:</strong> sacred groves and commons that conserve biodiversity",
                 "<strong>Governance:</strong> customary institutions for sharing land, water and "
                 "risk"]},
             {"t": "hbox", "color": "amber", "html": "&lsquo;Traditional&rsquo; is not the opposite "
              "of &lsquo;valid&rsquo;. Much of it is sophisticated, tested knowledge &mdash; simply "
              "produced outside the academy."},
         ]},

        {"type": "content", "label": "Ngugi 1986", "title": "Ng&#361;g&#297;: <em>Decolonising the Mind</em>",
         "blocks": [
             {"t": "body", "html": "In <em>Decolonising the Mind</em> (1986), Ng&#361;g&#297; wa "
              "Thiong&rsquo;o argues that the deepest colonial weapon was control of culture and "
              "<strong>language</strong> &mdash; making the colonised see themselves through the "
              "coloniser&rsquo;s eyes. He renounced English for Gikuyu in his own creative work."},
             {"t": "quote", "text": "The bullet was the means of the physical subjugation. "
              "Language was the means of the spiritual subjugation.",
              "attr": "&mdash; Ng&#361;g&#297; wa Thiong&rsquo;o, Decolonising the Mind (1986)"},
         ]},

        {"type": "content", "label": "Language &amp; Development", "title": "What gets lost in the donor&rsquo;s language",
         "blocks": [
             {"t": "body", "html": "When proposals, logframes, training and evaluation all happen "
              "in English (or in technical jargon), communities are made into clients of their own "
              "development &mdash; able to receive, rarely to author."},
             {"t": "hbox", "color": "cyan", "html": "A concrete decolonial test: in whose language "
              "is the agenda set? Who needs a translator to question the plan &mdash; the community, "
              "or the funder?"},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Pluralising the knowers",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Epistemic injustice: some are doubted simply as knowers",
                 "Spivak: beware speaking <em>for</em>; dismantle what silences",
                 "Indigenous and local knowledge are knowledge, not folklore",
                 "Ng&#361;g&#297;: decolonise the mind &mdash; and the language of the work"]},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Decolonising Aid &amp; the NGO Sector"},

        {"type": "content", "label": "The Architecture", "title": "Who holds the purse holds the power",
         "blocks": [
             {"t": "body", "html": "Modern aid runs along a chain: donor governments and "
              "foundations &rarr; international NGOs &rarr; national NGOs &rarr; community groups. "
              "Money, accountability and prestige concentrate at the top; risk and delivery sink "
              "to the bottom."},
             {"t": "flow", "steps": [
                 "DONOR sets priorities &amp; rules",
                 "INGO designs &amp; takes the contract",
                 "Local NGO implements on thin margins",
                 "COMMUNITY receives &mdash; rarely decides"]},
         ]},

        {"type": "content", "label": "White Saviourism", "title": "The white-saviour industrial complex",
         "blocks": [
             {"t": "term", "word": "White-saviour industrial complex",
              "def": "A phrase popularised by Teju Cole for the way intervention in the South can "
              "centre the rescuer&rsquo;s feelings, image and validation &mdash; treating distant "
              "others as a backdrop for heroism rather than as agents."},
             {"t": "hbox", "color": "red", "html": "The tell: the campaign is about the donor&rsquo;s "
              "goodness, not the community&rsquo;s agency. The poster child has no name; the "
              "volunteer is the protagonist."},
         ]},

        {"type": "content", "label": "Paternalism", "title": "&lsquo;We know what they need&rsquo;",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Paternalist reflex", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Outsiders define the problem",
                      "Solutions arrive pre-designed",
                      "&lsquo;Beneficiaries&rsquo; are passive recipients"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Decolonial reflex", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Communities name their own priorities",
                      "Solutions co-created and owned",
                      "People are agents and decision-makers"]}]}]},
             {"t": "hbox", "color": "amber", "html": "The shift is from <em>doing for</em> to "
              "<em>doing with</em> &mdash; and ultimately to <em>getting out of the way of</em>."},
         ]},

        {"type": "content", "label": "Who Leads INGOs", "title": "Power tracks the org chart",
         "blocks": [
             {"t": "chart", "canvas": "ingoLeadChart",
              "title": "Where decision-making power sits in a typical INGO chain (illustrative)",
              "source": "Illustrative &mdash; pattern, not a measured statistic",
              "type": "bar",
              "data": {"labels": ["Northern HQ / board", "Regional office", "Country office",
                                  "Local partner NGO", "Community"],
                       "datasets": [{"label": "Share of real decision-making power (%)",
                                     "data": [48, 22, 18, 9, 3],
                                     "backgroundColor": ["#1C1917", "#6366F1", "#0EA5E9",
                                                         "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, "
                          "scales:{ x:{ min:0, max:50, title:{display:true,text:'% of decision power (illustrative)'} } } }"}},
             {"t": "hbox", "color": "red", "html": "Illustrative, but the shape is real: those "
              "closest to the problem hold the least say over how it is addressed."},
         ]},

        {"type": "content", "label": "Localisation", "title": "Localisation and the Grand Bargain",
         "blocks": [
             {"t": "body", "html": "<strong>Localisation</strong> is the pledge to shift more "
              "funding, decision-making and leadership to local and national actors. The 2016 "
              "humanitarian <em>Grand Bargain</em> set a much-cited target of 25% of funding "
              "&lsquo;as directly as possible&rsquo; to local responders."},
             {"t": "hbox", "color": "amber", "html": "Years on, the directly-funded share has "
              "stayed in low single digits by most counts. The gap between rhetoric and money is "
              "where decolonising aid lives or dies."},
         ]},

        {"type": "content", "label": "ShiftThePower", "title": "#ShiftThePower",
         "blocks": [
             {"t": "body", "html": "The <strong>#ShiftThePower</strong> movement pushes beyond "
              "localisation-as-subcontracting toward genuinely shifting power, resources and "
              "trust to communities &mdash; community philanthropy, untied core funding, "
              "Southern-led agendas."},
             {"t": "bullets", "color": "green", "items": [
                 "From projects to long-term, flexible, core support",
                 "From upward accountability to downward accountability",
                 "From INGO as broker to community as principal"]},
         ]},

        {"type": "content", "label": "Honest Tension", "title": "Can a sector decolonise its own funding?",
         "blocks": [
             {"t": "body", "html": "There is a structural awkwardness: organisations are being "
              "asked to give away the very money, contracts and visibility that sustain them. "
              "Turkeys rarely vote for an early Christmas."},
             {"t": "hbox", "color": "cyan", "html": "This is why decolonising aid cannot be left "
              "to good intentions alone. It needs changed incentives, donor rules and metrics that "
              "reward ceding power &mdash; the subject of Section 10."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Follow the money and the mandate",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "The aid chain concentrates power at the top",
                 "White saviourism centres the rescuer, not the agent",
                 "Localisation pledges outrun the money that follows",
                 "#ShiftThePower: untie funding, flip accountability, cede the agenda"]},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Decolonising Research &amp; Data"},

        {"type": "content", "label": "Research as Power", "title": "Research is rarely neutral",
         "blocks": [
             {"t": "body", "html": "Who funds the study, frames the questions, holds the data and "
              "signs the paper are all expressions of power. As Linda Tuhiwai Smith writes in "
              "<em>Decolonizing Methodologies</em> (1999), &lsquo;research&rsquo; is one of the "
              "dirtiest words in the indigenous vocabulary &mdash; for good historical reason."},
             {"t": "quote", "text": "The word &lsquo;research&rsquo; is probably one of the dirtiest "
              "words in the indigenous world&rsquo;s vocabulary.",
              "attr": "&mdash; Linda Tuhiwai Smith, Decolonizing Methodologies (1999)"},
         ]},

        {"type": "content", "label": "Extraction", "title": "Extractive research and &lsquo;helicopter&rsquo; studies",
         "blocks": [
             {"t": "term", "word": "Helicopter (parachute) research",
              "def": "When researchers from richer institutions drop into a community, gather data "
              "or samples, and leave &mdash; publishing elsewhere with little local involvement, "
              "credit or benefit returned."},
             {"t": "hbox", "color": "red", "html": "The community is mined for raw material; the "
              "value &mdash; papers, careers, IP &mdash; is processed and kept abroad. It mirrors "
              "the colonial commodity economy, in data form."},
         ]},

        {"type": "content", "label": "Authorship Gap", "title": "Who writes about the Global South?",
         "blocks": [
             {"t": "chart", "canvas": "authorshipChart",
              "title": "Authorship of research about the Global South, by author location (illustrative)",
              "source": "Illustrative &mdash; directional pattern noted across global-health studies",
              "type": "doughnut",
              "data": {"labels": ["Global North-based authors", "Global South-based authors"],
                       "datasets": [{"data": [70, 30],
                                     "backgroundColor": ["#1C1917", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{position:'bottom'}} }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative, but studies of global-health "
              "and development literature repeatedly find Northern institutions over-represented as "
              "lead and senior authors of research <em>about</em> the South."},
         ]},

        {"type": "content", "label": "Data Sovereignty", "title": "Who owns the data?",
         "blocks": [
             {"t": "term", "word": "Data sovereignty",
              "def": "The principle that peoples and communities have the right to govern the "
              "collection, ownership and use of data about them &mdash; especially Indigenous data "
              "sovereignty, asserting collective control over community data."},
             {"t": "hbox", "color": "cyan", "html": "In development, this reframes survey data not "
              "as the researcher&rsquo;s asset but as belonging, at least in part, to the people it "
              "describes."},
         ]},

        {"type": "content", "label": "CARE Principles", "title": "CARE: people and purpose, not just data",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Letter", "Principle", "Meaning"],
              "rows": [
                  ["C", "Collective benefit", "Data ecosystems should benefit the communities involved"],
                  ["A", "Authority to control", "Communities govern how their data is used"],
                  ["R", "Responsibility", "Those working with data are accountable to communities"],
                  ["E", "Ethics", "People&rsquo;s rights and wellbeing come first, throughout"]]},
             {"t": "hbox", "color": "green", "html": "The CARE Principles (Global Indigenous Data "
              "Alliance) complement the technical FAIR principles by re-centring <em>people</em> "
              "and <em>power</em>, not just machine-readability."},
         ]},

        {"type": "content", "label": "Findings", "title": "Who owns &mdash; and gets &mdash; the findings?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Extractive default", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Results leave with the researcher; the paper "
                   "sits behind a paywall the community cannot reach; nothing returns."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Decolonial practice", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Findings shared back in usable form and local "
                   "language; co-authorship; open access; community signs off before publication."}]}]},
             {"t": "hbox", "color": "amber", "html": "A simple test: six months on, does the "
              "community have anything from the study &mdash; or only a memory of being surveyed?"},
         ]},

        {"type": "content", "label": "Better Methods", "title": "Toward accountable, shared research",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Co-design questions with the community from the start",
                 "Build in <strong>participatory</strong> methods (PRA, community-led mapping)",
                 "Pay, credit and co-author local researchers properly",
                 "Negotiate data governance and benefit-sharing up front",
                 "Return results in accessible formats and languages"]},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Research with, not on",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Research carries power &mdash; framing, ownership, authorship",
                 "Reject helicopter studies that extract and leave",
                 "Honour data sovereignty and the CARE principles",
                 "Share findings back; the community is a partner, not a sample"]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Post-Development &amp; Alternatives"},

        {"type": "content", "label": "The Radical Turn", "title": "What if development is the problem?",
         "blocks": [
             {"t": "body", "html": "<strong>Post-development</strong> thinkers &mdash; Escobar, "
              "Wolfgang Sachs, Gustavo Esteva, Majid Rahnema &mdash; go further than reform. They "
              "argue the whole project should be abandoned, not improved: it homogenises diverse "
              "ways of living into a single, Western blueprint."},
             {"t": "quote", "text": "The idea of development stands&hellip; like a ruin in the "
              "intellectual landscape.",
              "attr": "&mdash; Wolfgang Sachs (ed.), The Development Dictionary (1992)"},
         ]},

        {"type": "content", "label": "The Pluriverse", "title": "Escobar&rsquo;s pluriverse",
         "blocks": [
             {"t": "term", "word": "Pluriverse",
              "def": "Arturo Escobar&rsquo;s vision of &lsquo;a world where many worlds fit&rsquo; "
              "&mdash; against the one-world, one-future model of development; many coexisting ways "
              "of being, knowing and organising life."},
             {"t": "hbox", "color": "indigo", "html": "The phrase comes from the Zapatistas. Its "
              "promise: not a better single path, but the dignity of many paths."},
         ]},

        {"type": "content", "label": "Buen Vivir", "title": "Buen vivir / sumak kawsay",
         "blocks": [
             {"t": "body", "html": "From Andean Indigenous thought, <strong>buen vivir</strong> "
              "(<em>sumak kawsay</em> in Kichwa) means &lsquo;good living&rsquo; or &lsquo;living "
              "well together&rsquo; &mdash; a life in balance with community and nature, not the "
              "endless accumulation of more."},
             {"t": "hbox", "color": "green", "html": "It is constitutional in Ecuador (2008) and "
              "Bolivia (2009), and grounds the idea of rights of nature &mdash; an alternative "
              "<em>end</em> of development, not just a different means."},
         ]},

        {"type": "content", "label": "Ubuntu", "title": "Ubuntu: I am because we are",
         "blocks": [
             {"t": "body", "html": "From Southern Africa, <strong>ubuntu</strong> &mdash; "
              "&lsquo;a person is a person through other persons&rsquo; &mdash; centres relationship, "
              "dignity and the collective over the isolated, maximising individual of mainstream "
              "economics."},
             {"t": "hbox", "color": "cyan", "html": "Ubuntu reframes wellbeing as fundamentally "
              "<em>relational</em>: my flourishing is bound up with yours &mdash; a direct "
              "challenge to development&rsquo;s individualist core."},
         ]},

        {"type": "content", "label": "Swaraj &amp; Swadeshi", "title": "Gandhi: swaraj and swadeshi",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Swaraj", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Self-rule &mdash; not merely independence "
                   "from Britain but self-governance and self-reliance down to the village; rule "
                   "over oneself."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Swadeshi", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Of one&rsquo;s own country &mdash; local "
                   "production and economy, the spinning wheel against imported cloth and "
                   "dependence."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Gandhi&rsquo;s <em>Hind Swaraj</em> (1909) "
              "rejected the Western industrial model itself &mdash; an early, South Asian "
              "post-development argument in its own right."},
         ]},

        {"type": "content", "label": "Degrowth", "title": "Degrowth: questioning growth itself",
         "blocks": [
             {"t": "body", "html": "<strong>Degrowth</strong>, largely a Northern critique, argues "
              "that infinite economic growth on a finite planet is neither possible nor desirable "
              "&mdash; and that rich economies must shrink their material throughput so all can "
              "live well."},
             {"t": "hbox", "color": "amber", "html": "It converges with post-development on "
              "rejecting growth-as-goal &mdash; though decolonial voices insist degrowth must "
              "start in the over-consuming North, not be imposed on those still meeting basic "
              "needs."},
         ]},

        {"type": "content", "label": "Compared", "title": "Many worlds, one refusal",
         "blocks": [
             {"t": "table",
              "head": ["Alternative", "Roots", "Core value"],
              "rows": [
                  ["Buen vivir", "Andean Indigenous", "Living well, in balance with nature"],
                  ["Ubuntu", "Southern Africa", "Relational, communal humanity"],
                  ["Swaraj / swadeshi", "South Asia (Gandhi)", "Self-rule and local self-reliance"],
                  ["Degrowth", "Global North critique", "Less throughput, more wellbeing"],
                  ["Pluriverse", "Decolonial / Zapatista", "Many worlds coexisting"]]},
             {"t": "hbox", "color": "green", "html": "What unites them is a refusal of the "
              "single, growth-defined, Western destination &mdash; and a plurality of locally "
              "rooted ends."},
         ]},

        {"type": "content", "label": "Takeaway", "title": "Ends, not just means",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Post-development questions the goal, not only the method",
                 "Buen vivir, ubuntu, swaraj: locally rooted visions of a good life",
                 "Degrowth challenges growth-as-goal &mdash; starting in the North",
                 "The pluriverse: a world where many worlds fit"]},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Decolonising Practice"},

        {"type": "content", "label": "From Theory to Action", "title": "What changes on Monday morning?",
         "blocks": [
             {"t": "body", "html": "Critique without practice is just sophistication. Decolonising "
              "is finally a set of concrete shifts in how programmes are funded, designed, staffed, "
              "spoken and judged &mdash; small choices that move power, repeated at scale."},
             {"t": "flow", "steps": [
                 "LANGUAGE: how we name people &amp; problems",
                 "PARTNERSHIP: who decides",
                 "FUNDING: where money &amp; risk sit",
                 "EVALUATION: who defines success"]},
         ]},

        {"type": "content", "label": "Language", "title": "Change the words, expose the relations",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Common term", "Reframe", "Why"],
              "rows": [
                  ["Beneficiary", "Participant, partner, rights-holder", "Restores agency, not charity"],
                  ["Capacity-building (one-way)", "Mutual learning", "Assumes the South lacks; the North learns too"],
                  ["Field / the field", "The community, the place, by name", "&lsquo;Field&rsquo; objectifies and distances"],
                  ["Giving voice to", "Making space to be heard", "They already have a voice"],
                  ["Third World / developing", "Global South, Majority World", "Less hierarchical framing"]]},
             {"t": "hbox", "color": "amber", "html": "Words are not the whole task &mdash; but "
              "changing them forces the underlying relation into view."},
         ]},

        {"type": "content", "label": "Partnership", "title": "Real partnership shares decisions, not just risk",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Communities set priorities <em>before</em> the proposal is written",
                 "Southern partners are principals, not subcontractors",
                 "Decision rights, not just delivery, sit with local actors",
                 "Exit planned from day one &mdash; build to hand over, then leave"]},
             {"t": "hbox", "color": "green", "html": "Test it: in the next big decision, who can "
              "actually say no &mdash; the funder, the INGO, or the community?"},
         ]},

        {"type": "content", "label": "Funding", "title": "Move the money, move the power",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Power-hoarding funding", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Short, restricted, project grants",
                      "Heavy upward reporting",
                      "Risk pushed down the chain"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Power-shifting funding", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Multi-year, flexible, core funding",
                      "Trust-based, light-touch reporting",
                      "Risk shared; overheads fairly covered"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Decolonising aid is, very concretely, a "
              "fight over the design of grant agreements."},
         ]},

        {"type": "content", "label": "Evaluation", "title": "Who defines success?",
         "blocks": [
             {"t": "body", "html": "If donors alone set the indicators, &lsquo;success&rsquo; means "
              "&lsquo;what the donor values&rsquo;. Decolonising evaluation asks communities to "
              "define what a good outcome is &mdash; and weighs their judgement seriously."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Co-define indicators with participants",
                 "Value qualitative, relational and locally meaningful change",
                 "Build downward accountability &mdash; to communities, not only funders",
                 "Treat &lsquo;most significant change&rsquo; stories as real evidence"]},
         ]},

        {"type": "content", "label": "Representation", "title": "Tell the story without taking it",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "No &lsquo;poverty porn&rsquo; &mdash; no dignity-stripping imagery for donations",
                 "Name people; secure genuine, informed consent for images and stories",
                 "Show agency and context, not only need",
                 "Let people tell their own stories, in their own words"]},
             {"t": "hbox", "color": "red", "html": "The image on the fundraising leaflet is a "
              "decolonial question: does it restore dignity, or trade it for a donation?"},
         ]},

        {"type": "content", "label": "Self-Audit", "title": "A decolonial check for any programme",
         "compact": True,
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Who set the agenda &mdash; and in whose language?",
                 "Where does the money go, and who bears the risk?",
                 "Whose knowledge counted as expertise?",
                 "Who can say no to the plan?",
                 "Who defines and measures success?",
                 "What returns to the community &mdash; and what is extracted?"]},
             {"t": "hbox", "color": "cyan", "html": "Run this on a project you know. The honest "
              "answers map exactly where power still sits."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Tensions, Critiques &amp; Further Reading"},

        {"type": "content", "label": "Stay Critical", "title": "Decolonising deserves its own critique",
         "blocks": [
             {"t": "body", "html": "An intellectually honest course turns the lens on itself. "
              "Decolonial thought has real tensions and blind spots &mdash; naming them protects "
              "the project from becoming the dogma it set out to challenge."},
             {"t": "hbox", "color": "indigo", "html": "Holding both is the mature position: the "
              "critique of development is powerful <em>and</em> incomplete."},
         ]},

        {"type": "content", "label": "Romanticisation", "title": "The risk of romanticising the &lsquo;local&rsquo;",
         "blocks": [
             {"t": "body", "html": "Celebrating indigenous and traditional ways can slide into "
              "<strong>romanticisation</strong> &mdash; ignoring that local structures, too, can "
              "be unequal: caste, patriarchy, gerontocracy, exclusion."},
             {"t": "hbox", "color": "red", "html": "&lsquo;The community&rsquo; is not a "
              "harmonious whole. Decolonising must not become a cover for defending local "
              "injustice in the name of authenticity."},
         ]},

        {"type": "content", "label": "Essentialism", "title": "The essentialism trap",
         "blocks": [
             {"t": "term", "word": "Essentialism",
              "def": "Treating &lsquo;Western&rsquo; and &lsquo;indigenous&rsquo; (or East and "
              "West) as fixed, pure, opposed essences &mdash; ironically reproducing the very "
              "binary that Orientalism built."},
             {"t": "hbox", "color": "amber", "html": "Knowledge has always travelled and mixed. "
              "Hybridity (Homi Bhabha) reminds us there is no untouched &lsquo;authentic&rsquo; to "
              "return to &mdash; only living, entangled traditions."},
         ]},

        {"type": "content", "label": "The Hardest Question", "title": "Can a colonial sector decolonise itself?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "The pessimist", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The aid system <em>is</em> the colonial "
                   "relation. Asking it to decolonise is asking the master&rsquo;s house to "
                   "dismantle itself with the master&rsquo;s tools."}]}],
              "right": [{"t": "panel", "color": "green", "title": "The pragmatist", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Until the system is gone, those inside can "
                   "still shift real power and resources. Imperfect change beats principled "
                   "paralysis."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Audre Lorde&rsquo;s warning &mdash; &lsquo;the "
              "master&rsquo;s tools will never dismantle the master&rsquo;s house&rsquo; &mdash; "
              "haunts every reform. Sit with the tension; do not resolve it cheaply."},
         ]},

        {"type": "content", "label": "Co-optation", "title": "When &lsquo;decolonising&rsquo; gets captured",
         "blocks": [
             {"t": "body", "html": "The sharpest present danger is <strong>co-optation</strong>: "
              "the language is adopted, the structures untouched. &lsquo;Decolonising&rsquo; "
              "becomes a workshop, a job title, a grant theme &mdash; a new layer of expertise atop "
              "the old hierarchy."},
             {"t": "hbox", "color": "red", "html": "The discipline: judge by power and money moved, "
              "never by the vocabulary used. If nothing shifted, nothing was decolonised."},
         ]},

        {"type": "content", "label": "The Canon", "title": "Key thinkers, correctly placed",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Thinker", "Work", "Contribution"],
              "rows": [
                  ["Frantz Fanon", "The Wretched of the Earth (1961)", "Colonialism&rsquo;s violence &amp; psychology of liberation"],
                  ["Edward Said", "Orientalism (1978)", "How the West constructed &lsquo;the Orient&rsquo;"],
                  ["Ng&#361;g&#297; wa Thiong&rsquo;o", "Decolonising the Mind (1986)", "Language, culture &amp; the colonised mind"],
                  ["Gayatri Spivak", "Can the Subaltern Speak? (1988)", "Can the marginalised be heard?"],
                  ["Arturo Escobar", "Encountering Development (1995)", "Development as discourse; the pluriverse"],
                  ["An&iacute;bal Quijano", "Coloniality of Power (2000)", "Race &amp; the lasting colonial matrix"]]},
         ]},

        {"type": "content", "label": "Read &amp; Connect", "title": "Where to go next",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>The Wretched of the Earth</em> &mdash; Frantz Fanon (1961)",
                 "<em>Orientalism</em> &mdash; Edward Said (1978)",
                 "<em>Decolonising the Mind</em> &mdash; Ng&#361;g&#297; wa Thiong&rsquo;o (1986)",
                 "<em>Encountering Development</em> &mdash; Arturo Escobar (1995)",
                 "<em>The Development Dictionary</em> &mdash; Wolfgang Sachs, ed. (1992)",
                 "<em>Decolonizing Methodologies</em> &mdash; Linda Tuhiwai Smith (1999)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo&rsquo;s "
              "<strong>Development Economics</strong>, <strong>Research Ethics</strong> and "
              "<strong>Participatory Methods</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "&lsquo;Development&rsquo; has colonial roots &mdash; it is not neutral",
                 "Coloniality outlives colonialism: power, knowledge and being",
                 "Whose knowledge counts is a question of power, not merit",
                 "Decolonising means moving money and decisions, not just words",
                 "Stay critical &mdash; of development, and of decolonising itself"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Decolonial Development 101 &middot; Complete",
         "headline": "Whose development,<br>on whose terms?",
         "byline": "Decolonising is not a slogan but a discipline &mdash; following the power, the "
                   "money and the knowledge in every programme you touch. Explore the rest of the "
                   "ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
