# -*- coding: utf-8 -*-
"""
Indian Constitution 101 — ImpactMojo 101 Series (native deck spec)
A citizen's and practitioner's guide to the Constitution of India.
Build: python3 scripts/deck-builder/build.py ind_constitution
"""

DECK = {
    "slug": "ind-constitution",
    "title": "Indian Constitution 101",
    "description": ("Indian Constitution 101 — a free foundational course on the making, "
                    "structure and living practice of the Constitution of India, for "
                    "development practitioners, students and citizens. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Indian<br>Constitution<br>101",
         "sub": "The Making, the Structure &amp; the Living Practice of the Constitution of "
                "India &mdash; a Foundational Course for Practitioners, Students &amp; Citizens",
         "tags": ["Constitution of India", "Rights-Based", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What a Constitution Is &amp; How India's Was Made"},
             {"name": "The Preamble &amp; Its Values"},
             {"name": "Fundamental Rights I: Equality &amp; Freedoms"},
             {"name": "Fundamental Rights II: Protection, Remedies"},
             {"name": "Directive Principles &amp; Fundamental Duties"},
             {"name": "The Union Government &amp; Its Structure"},
             {"name": "Federalism: Union, States &amp; the Schedules"},
             {"name": "The Judiciary &amp; Judicial Review"},
             {"name": "Local Self-Government"},
             {"name": "Amending the Constitution"},
             {"name": "Constitutionalism in Practice"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What a Constitution Is &amp; How India's Was Made"},

        {"type": "content", "label": "Definition", "title": "What is a constitution?",
         "blocks": [
             {"t": "body", "html": "A <strong>constitution</strong> is the supreme law of a "
              "country &mdash; the rulebook that creates the government, distributes power among "
              "its organs, and limits what the state may do to the people. Every other law must "
              "conform to it."},
             {"t": "term", "word": "Constitution",
              "def": "The fundamental, highest-ranking body of law that establishes the framework "
              "of government, defines the relationship between the state and the citizen, and "
              "guarantees rights. Ordinary laws that conflict with it are void."},
             {"t": "hbox", "color": "cyan", "html": "A constitution is not just a legal document. "
              "It is a political and moral charter &mdash; a promise a nation makes to itself "
              "about how power will be held and limited."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "Two jobs every constitution does",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Empowers", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Creates Parliament, executive, judiciary",
                      "Gives the state authority to govern",
                      "Sets out how laws are made",
                      "Defines who exercises which power"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Limits", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Guarantees rights against the state",
                      "Subjects all organs to the rule of law",
                      "Allows courts to strike down bad laws",
                      "Caps even the majority's power"]}]}]},
             {"t": "hbox", "color": "amber", "html": "A constitution both <em>gives</em> power and "
              "<em>fences</em> it. The fence is what protects the citizen from the very state the "
              "constitution creates."},
         ]},

        {"type": "content", "label": "The Backdrop", "title": "From colonial rule to a sovereign republic",
         "blocks": [
             {"t": "body", "html": "British India was governed by a succession of colonial "
              "statutes, the last being the <strong>Government of India Act, 1935</strong>. With "
              "independence on 15 August 1947, India had to author its own constitution &mdash; a "
              "law made by Indians, for Indians."},
             {"t": "hbox", "color": "cyan", "html": "The 1935 Act left a deep imprint: much of the "
              "administrative and federal machinery of the Constitution borrows from it &mdash; but "
              "now answerable to the people, not the Crown."},
         ]},

        {"type": "content", "label": "The Body", "title": "The Constituent Assembly, 1946&ndash;49",
         "blocks": [
             {"t": "body", "html": "The <strong>Constituent Assembly</strong> was the body that "
              "drafted the Constitution. It first met in <strong>December 1946</strong> and worked "
              "for nearly three years, debating clause by clause in the open."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "1946", "label": "First sitting of the Constituent Assembly", "color": "cyan"},
                 {"num": "~3 yrs", "label": "Time taken to draft and debate the text", "color": "green"},
                 {"num": "Many", "label": "Members across regions, communities &amp; views",
                  "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Dr. Rajendra Prasad was the Assembly's "
              "President; Jawaharlal Nehru moved the foundational Objectives Resolution that became "
              "the seed of the Preamble."},
         ]},

        {"type": "content", "label": "The Architect", "title": "B.R. Ambedkar and the Drafting Committee",
         "blocks": [
             {"t": "body", "html": "<strong>Dr. B.R. Ambedkar</strong> chaired the seven-member "
              "Drafting Committee that prepared the text for the Assembly. A jurist, economist and "
              "leader of the anti-caste movement, he is widely regarded as the chief architect of "
              "the Constitution."},
             {"t": "quote",
              "text": "However good a constitution may be, it is sure to turn out bad because "
              "those who are called to work it happen to be a bad lot.",
              "attr": "&mdash; B.R. Ambedkar, Constituent Assembly, 25 November 1949"},
         ]},

        {"type": "content", "label": "Adoption", "title": "Adopted 1949, in force 1950",
         "blocks": [
             {"t": "flow", "steps": [
                 "DRAFTED: Constituent Assembly debates, 1946&ndash;49",
                 "ADOPTED: 26 November 1949 (now Constitution Day)",
                 "COMMENCED: in force 26 January 1950 (Republic Day)",
                 "RESULT: India becomes a sovereign democratic republic"]},
             {"t": "hbox", "color": "red", "html": "Mind the two dates: the Constitution was "
              "<strong>adopted on 26 November 1949</strong> but came into <strong>force on 26 "
              "January 1950</strong>. 26 January was chosen to honour the 1930 'Purna Swaraj' "
              "pledge of complete independence."},
         ]},

        {"type": "content", "label": "Scale", "title": "The world's longest written constitution",
         "blocks": [
             {"t": "body", "html": "As originally enacted the Constitution of India had a Preamble, "
              "around <strong>395 Articles</strong> grouped into Parts, and several Schedules &mdash; "
              "making it the <strong>longest written constitution</strong> of any sovereign country. "
              "It has grown since through amendments."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "~395", "label": "Articles at adoption (more added since)", "color": "cyan"},
                 {"num": "8", "label": "Schedules at adoption (now 12)", "color": "green"},
                 {"num": "Longest", "label": "Written constitution of any nation", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Its length reflects ambition: it governs a "
              "vast, diverse federation and spells out detail other constitutions leave to "
              "ordinary law."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Preamble &amp; Its Values"},

        {"type": "content", "label": "The Opening", "title": "“We, the People of India…”",
         "blocks": [
             {"t": "body", "html": "The Constitution opens with a <strong>Preamble</strong> &mdash; "
              "a short statement of its source, purpose and guiding values. Its first words, "
              "<strong>'We, the People of India'</strong>, locate sovereignty in the people, not "
              "in a monarch or a colonial power."},
             {"t": "quote",
              "text": "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into "
              "a SOVEREIGN SOCIALIST SECULAR DEMOCRATIC REPUBLIC&hellip;",
              "attr": "&mdash; Preamble to the Constitution of India"},
         ]},

        {"type": "content", "label": "Source", "title": "Sovereignty rests with the people",
         "blocks": [
             {"t": "body", "html": "By beginning with the people, the Preamble makes a radical "
              "claim for its time: the Constitution does not flow down from a ruler &mdash; it "
              "flows up from the governed, who give it to themselves."},
             {"t": "term", "word": "Popular sovereignty",
              "def": "The principle that ultimate political authority belongs to the people, who "
              "are the source of the state's legitimacy and who constitute the government through "
              "the Constitution."},
         ]},

        {"type": "content", "label": "The Republic", "title": "Sovereign, Socialist, Secular, Democratic, Republic",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Word", "What it means"],
              "rows": [
                  ["Sovereign", "Free from external control; supreme in its own affairs"],
                  ["Socialist", "Committed to social &amp; economic justice and reduced inequality"],
                  ["Secular", "No state religion; equal treatment of all faiths"],
                  ["Democratic", "Government by the people through universal adult franchise"],
                  ["Republic", "An elected head of state &mdash; no hereditary monarch"]]},
             {"t": "hbox", "color": "amber", "html": "'Socialist' and 'Secular' were not in the "
              "original text &mdash; they were added by the <strong>42nd Amendment in 1976</strong>. "
              "The values, though, were present from the start."},
         ]},

        {"type": "content", "label": "The Goals", "title": "Justice, Liberty, Equality, Fraternity",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Justice", "label": "Social, economic and political", "color": "cyan"},
                 {"num": "Liberty", "label": "Of thought, expression, belief, faith and worship",
                  "color": "green"},
                 {"num": "Equality", "label": "Of status and of opportunity", "color": "indigo"},
                 {"num": "Fraternity", "label": "Assuring dignity of the individual &amp; unity of "
                  "the nation", "color": "amber"}]},
             {"t": "hbox", "color": "cyan", "html": "These four were drawn, in spirit, from the "
              "ideals of the French Revolution &mdash; but reworked for India's own struggle "
              "against caste, colonialism and inequality."},
         ]},

        {"type": "content", "label": "Fraternity", "title": "Dignity of the individual is the keystone",
         "blocks": [
             {"t": "body", "html": "Ambedkar singled out <strong>fraternity</strong> &mdash; a "
              "sense of common brotherhood and sisterhood &mdash; as essential. Without it, he "
              "warned, liberty and equality could not be sustained in a society scarred by caste."},
             {"t": "quote",
              "text": "Without fraternity, liberty and equality could not become a natural course "
              "of things. It would require a constable to enforce them.",
              "attr": "&mdash; B.R. Ambedkar"},
         ]},

        {"type": "content", "label": "Legal Status", "title": "Is the Preamble enforceable?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Not a source of power", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The Preamble itself grants no powers and "
                   "creates no enforceable rights &mdash; you cannot sue on the Preamble alone."}]}],
              "right": [{"t": "panel", "color": "green", "title": "But a guide", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Courts use it as a key to interpret "
                   "ambiguous provisions and to understand the Constitution's purpose and spirit."}]}]},
             {"t": "hbox", "color": "amber", "html": "The Supreme Court has held that the Preamble "
              "is a <strong>part of the Constitution</strong> and reflects its basic features &mdash; "
              "so even it cannot be amended to destroy those features."},
         ]},

        {"type": "content", "label": "Secularism", "title": "Indian secularism: principled distance",
         "blocks": [
             {"t": "body", "html": "Indian secularism does not mean a strict wall between religion "
              "and state. It means the state has <strong>no religion of its own</strong>, treats "
              "all faiths equally, and may intervene to reform religious practice in the name of "
              "rights and equality."},
             {"t": "hbox", "color": "cyan", "html": "This is why the state can both protect "
              "religious freedom (Articles 25&ndash;28) and outlaw practices like untouchability "
              "&mdash; a model scholars call 'principled distance'."},
         ]},

        {"type": "content", "label": "Why It Endures", "title": "The Preamble as a compass",
         "blocks": [
             {"t": "body", "html": "For a practitioner, the Preamble is a moral compass. When a "
              "policy or programme is debated, it can be tested against four words: does it advance "
              "<strong>justice, liberty, equality and fraternity</strong>?"},
             {"t": "hbox", "color": "green", "html": "Rights-based development draws directly on "
              "this vocabulary. The Preamble turns abstract goals into a shared, citable standard."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Fundamental Rights I: Equality &amp; Freedoms"},

        {"type": "content", "label": "Part III", "title": "Fundamental Rights, the heart of Part III",
         "blocks": [
             {"t": "body", "html": "<strong>Part III</strong> of the Constitution guarantees "
              "<strong>Fundamental Rights</strong> &mdash; rights so basic they are protected "
              "against the state itself and enforceable in court. They are the citizen's shield."},
             {"t": "term", "word": "Fundamental Rights",
              "def": "Justiciable rights guaranteed in Part III (Articles 12&ndash;35) that the "
              "state cannot ordinarily violate; a person may approach the courts directly if they "
              "are infringed."},
         ]},

        {"type": "content", "label": "Six Families", "title": "Six broad categories of rights",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Right", "Articles", "Covers"],
              "rows": [
                  ["Right to Equality", "14&ndash;18", "Equality before law, non-discrimination"],
                  ["Right to Freedom", "19&ndash;22", "Speech, movement, life &amp; liberty"],
                  ["Against Exploitation", "23&ndash;24", "No trafficking, forced or child labour"],
                  ["Freedom of Religion", "25&ndash;28", "Conscience, practice, propagation"],
                  ["Cultural &amp; Educational", "29&ndash;30", "Minority language &amp; institutions"],
                  ["Constitutional Remedies", "32", "The right to enforce all the rest"]]},
             {"t": "hbox", "color": "cyan", "html": "We take equality and freedoms first "
              "(Articles 14&ndash;22); the rest follow in the next section."},
         ]},

        {"type": "content", "label": "Article 14", "title": "Equality before the law",
         "blocks": [
             {"t": "body", "html": "<strong>Article 14</strong> guarantees to every person "
              "'equality before the law and the equal protection of the laws'. No one &mdash; not "
              "even the government &mdash; is above the law, and like cases must be treated alike."},
             {"t": "hbox", "color": "amber", "html": "Equality is not blind sameness. The state "
              "may make <em>reasonable classifications</em> &mdash; for example, special measures "
              "for the disadvantaged &mdash; so long as the distinction is rational and serves a "
              "legitimate aim."},
         ]},

        {"type": "content", "label": "Articles 15&ndash;16", "title": "No discrimination; equal opportunity",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Article 15", "blocks": [
                  {"t": "body", "cls": "sm", "html": "No discrimination on grounds of religion, "
                   "race, caste, sex or place of birth &mdash; and permits special provision for "
                   "women, children and backward classes."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Article 16", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Equality of opportunity in public employment, "
                   "while allowing reservation for under-represented backward classes."}]}]},
             {"t": "hbox", "color": "green", "html": "These articles are the constitutional basis "
              "for <strong>affirmative action</strong> &mdash; reservations are not an exception to "
              "equality but a tool to achieve real, substantive equality."},
         ]},

        {"type": "content", "label": "Articles 17&ndash;18", "title": "Abolishing untouchability and titles",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Article 17", "label": "Abolishes 'untouchability' and forbids its "
                  "practice in any form &mdash; an offence punishable by law", "color": "red"},
                 {"num": "Article 18", "label": "Abolishes titles (except military and academic "
                  "distinctions)", "color": "indigo"}]},
             {"t": "hbox", "color": "cyan", "html": "Article 17 is one of the Constitution's most "
              "radical clauses: it directly outlaws a centuries-old social practice &mdash; binding "
              "not just the state but every person."},
         ]},

        {"type": "content", "label": "Article 19", "title": "Six freedoms &mdash; and reasonable limits",
         "blocks": [
             {"t": "bullets", "items": [
                 "Freedom of <strong>speech and expression</strong>",
                 "Freedom to <strong>assemble</strong> peaceably and without arms",
                 "Freedom to form <strong>associations or unions</strong>",
                 "Freedom to <strong>move</strong> freely throughout India",
                 "Freedom to <strong>reside and settle</strong> anywhere in India",
                 "Freedom to practise any <strong>profession, occupation, trade</strong>"]},
             {"t": "hbox", "color": "amber", "html": "None of these is absolute. The state may "
              "impose <strong>reasonable restrictions</strong> &mdash; for sovereignty, public "
              "order, decency, and similar grounds &mdash; but the restriction must be reasonable, "
              "and courts decide if it is."},
         ]},

        {"type": "content", "label": "Articles 20&ndash;22", "title": "Liberty, life, and protection from arrest",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Article", "Protects"],
              "rows": [
                  ["20", "Against arbitrary conviction &mdash; no retrospective crimes, no double jeopardy, no self-incrimination"],
                  ["21", "Right to life and personal liberty &mdash; expanded by courts into dignity, privacy, health, environment"],
                  ["21A", "Right to free and compulsory education, ages 6&ndash;14"],
                  ["22", "Safeguards on arrest and detention &mdash; with debated exceptions for preventive detention"]]},
             {"t": "hbox", "color": "green", "html": "<strong>Article 21</strong> is the engine of "
              "modern rights jurisprudence: courts have read into 'life and personal liberty' a "
              "vast family of unstated rights, from a clean environment to privacy."},
         ]},

        {"type": "content", "label": "Article 21 Expanded", "title": "How 'life' grew into dignity",
         "blocks": [
             {"t": "body", "html": "Originally read narrowly, <strong>Article 21</strong> was "
              "transformed by the courts after the 1970s. 'Life' came to mean a life with "
              "<strong>dignity</strong> &mdash; not mere animal existence &mdash; and 'procedure "
              "established by law' had to be just, fair and reasonable."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Right to live with human dignity",
                 "Right to livelihood, shelter and health",
                 "Right to a clean environment",
                 "Right to privacy (recognised in 2017)"]},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Fundamental Rights II: Protection, Remedies"},

        {"type": "content", "label": "Articles 23&ndash;24", "title": "Right against exploitation",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Article 23", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Prohibits human trafficking, 'begar' and "
                   "other forms of forced labour. The basis for laws against bonded labour."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Article 24", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Prohibits employment of children below 14 in "
                   "factories, mines and other hazardous work."}]}]},
             {"t": "hbox", "color": "amber", "html": "For development practitioners, these articles "
              "underpin anti-trafficking work, bonded-labour rehabilitation and child-protection "
              "programmes &mdash; constitutional, not merely statutory, commitments."},
         ]},

        {"type": "content", "label": "Articles 25&ndash;28", "title": "Freedom of religion",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Article 25:</strong> freedom of conscience and to profess, practise and "
                 "propagate religion, subject to public order, morality and health",
                 "<strong>Article 26:</strong> freedom to manage religious affairs",
                 "<strong>Article 27:</strong> no one may be taxed to promote a particular religion",
                 "<strong>Article 28:</strong> limits on religious instruction in state-funded "
                 "educational institutions"]},
             {"t": "hbox", "color": "cyan", "html": "These rights belong to individuals and "
              "communities alike &mdash; and, crucially, are subject to the state's power to "
              "advance social welfare and reform."},
         ]},

        {"type": "content", "label": "Articles 29&ndash;30", "title": "Cultural and educational rights",
         "blocks": [
             {"t": "body", "html": "<strong>Articles 29 and 30</strong> protect minorities. Any "
              "section of citizens may conserve its distinct language, script or culture; and "
              "religious and linguistic minorities may establish and administer educational "
              "institutions of their choice."},
             {"t": "hbox", "color": "green", "html": "These are sometimes called the "
              "Constitution's promise to diversity &mdash; that majority rule will not mean the "
              "erasure of minority identity, language or learning."},
         ]},

        {"type": "content", "label": "Article 32", "title": "The right to constitutional remedies",
         "blocks": [
             {"t": "body", "html": "<strong>Article 32</strong> gives every person the right to "
              "move the Supreme Court directly to enforce the Fundamental Rights. A right without "
              "a remedy is hollow &mdash; Article 32 is the remedy that makes all the others real."},
             {"t": "quote",
              "text": "If I was asked to name any particular article in this Constitution as the "
              "most important &mdash; an article without which this Constitution would be a "
              "nullity &mdash; I could not refer to any other article except this one. It is the "
              "very soul of the Constitution and the very heart of it.",
              "attr": "&mdash; B.R. Ambedkar, on Article 32"},
         ]},

        {"type": "content", "label": "The Writs", "title": "Five writs the courts can issue",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Writ", "What it does"],
              "rows": [
                  ["Habeas Corpus", "'Produce the body' &mdash; challenge unlawful detention"],
                  ["Mandamus", "'We command' &mdash; order an authority to do its legal duty"],
                  ["Prohibition", "Stop a lower court exceeding its jurisdiction"],
                  ["Certiorari", "Quash an order passed without jurisdiction or in error"],
                  ["Quo Warranto", "'By what authority?' &mdash; challenge a public office-holder"]]},
             {"t": "hbox", "color": "cyan", "html": "The Supreme Court (Article 32) and the High "
              "Courts (Article 226) can issue these writs &mdash; High Court writ power is even "
              "wider, covering legal rights beyond Fundamental Rights."},
         ]},

        {"type": "content", "label": "Reasonable Limits", "title": "Rights are strong, but not unlimited",
         "blocks": [
             {"t": "body", "html": "Fundamental Rights can be subject to <strong>reasonable "
              "restrictions</strong> and, in defined circumstances, suspended during a national "
              "emergency &mdash; though after the experience of the 1975&ndash;77 Emergency, the "
              "safeguards around this were tightened."},
             {"t": "hbox", "color": "amber", "html": "The lesson the courts drew: a restriction on "
              "a fundamental right must be tested for whether it is <strong>fair, reasonable and "
              "proportionate</strong> &mdash; not merely whether a law authorises it."},
         ]},

        {"type": "content", "label": "Practitioner Lens", "title": "Why rights literacy matters in the field",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "A denial of rations or wages can be a violation of the right to life and livelihood",
                 "Caste-based exclusion engages Articles 15 and 17, not just social custom",
                 "Detention and policing of the poor engage Articles 21 and 22",
                 "A writ petition can be a faster remedy than a long civil suit"]},
             {"t": "hbox", "color": "amber", "html": "You do not need to be a lawyer to spot a "
              "rights violation &mdash; but knowing the article gives a complaint constitutional "
              "weight."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Directive Principles &amp; Fundamental Duties"},

        {"type": "content", "label": "Part IV", "title": "Directive Principles of State Policy",
         "blocks": [
             {"t": "body", "html": "<strong>Part IV</strong> sets out the <strong>Directive "
              "Principles of State Policy (DPSP)</strong> &mdash; goals the state should strive "
              "toward in making laws and policy: a welfare state, social justice and a decent life "
              "for all."},
             {"t": "term", "word": "Directive Principles",
              "def": "Guidelines in Part IV (Articles 36&ndash;51) directing the state to secure "
              "social and economic justice. They shape policy but, unlike Fundamental Rights, "
              "cannot by themselves be enforced in court."},
         ]},

        {"type": "content", "label": "Non-Justiciable", "title": "Rights you can sue on; principles you cannot",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Fundamental Rights", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>Justiciable.</strong> Enforceable "
                   "in court; the state must not violate them."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Directive Principles", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>Non-justiciable.</strong> Not "
                   "directly enforceable, but 'fundamental in the governance of the country'."}]}]},
             {"t": "hbox", "color": "amber", "html": "Ambedkar's design: rights set limits the "
              "state cannot cross; principles set a direction the state should travel. One is a "
              "wall, the other a road."},
         ]},

        {"type": "content", "label": "Examples", "title": "What the Directive Principles ask for",
         "blocks": [
             {"t": "bullets", "items": [
                 "Adequate means of livelihood and fair distribution of resources",
                 "Equal pay for equal work; protection of workers and children",
                 "Free and compulsory education for children (since reinforced as a right)",
                 "Public health, nutrition and a rising standard of living",
                 "Promotion of village panchayats and cottage industries",
                 "Protection of the environment, forests and wildlife"]},
         ]},

        {"type": "content", "label": "From Principle to Right", "title": "How directives become enforceable",
         "blocks": [
             {"t": "body", "html": "Though not directly enforceable, Directive Principles have "
              "repeatedly inspired enforceable law and judicial interpretation. The directive on "
              "education, for instance, helped the courts read education into the right to life "
              "&mdash; later made explicit as <strong>Article 21A</strong>."},
             {"t": "flow", "steps": [
                 "DIRECTIVE: state should provide for education (Part IV)",
                 "COURTS: read it into Article 21's right to life",
                 "AMENDMENT: Article 21A added (86th Amendment, 2002)",
                 "STATUTE: Right to Education Act, 2009"]},
         ]},

        {"type": "content", "label": "The Tension", "title": "When rights and principles collide",
         "blocks": [
             {"t": "body", "html": "Land reform and social-justice laws (driven by Directive "
              "Principles) sometimes clashed with property and equality rights. This tension drove "
              "some of the Constitution's biggest battles &mdash; and several amendments &mdash; "
              "over which should prevail."},
             {"t": "hbox", "color": "cyan", "html": "The settled position today: the state should "
              "harmonise the two, and may pursue Directive Principles &mdash; but not by destroying "
              "the basic structure of the Constitution."},
         ]},

        {"type": "content", "label": "Part IV-A", "title": "Fundamental Duties of citizens",
         "blocks": [
             {"t": "body", "html": "The <strong>42nd Amendment (1976)</strong> added "
              "<strong>Part IV-A</strong> and <strong>Article 51A</strong>, listing the "
              "<strong>Fundamental Duties</strong> of every citizen &mdash; the responsibilities "
              "that accompany rights."},
             {"t": "term", "word": "Fundamental Duties",
              "def": "Moral obligations of citizens listed in Article 51A &mdash; such as "
              "respecting the Constitution, safeguarding public property and protecting the "
              "environment. Like Directive Principles, they are not directly enforceable."},
         ]},

        {"type": "content", "label": "Examples", "title": "Some duties Article 51A asks of us",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Abide by the Constitution and respect its ideals and institutions",
                 "Cherish the ideals of the freedom struggle",
                 "Uphold the sovereignty, unity and integrity of India",
                 "Promote harmony and the spirit of common brotherhood",
                 "Protect and improve the natural environment",
                 "Develop the scientific temper, humanism and the spirit of inquiry"]},
         ]},

        {"type": "content", "label": "Balance", "title": "Rights, principles and duties as one whole",
         "blocks": [
             {"t": "body", "html": "Read together, the three parts form a balanced design: "
              "<strong>Fundamental Rights</strong> protect the individual, "
              "<strong>Directive Principles</strong> direct the state toward justice, and "
              "<strong>Fundamental Duties</strong> remind citizens of their share in the project."},
             {"t": "hbox", "color": "amber", "html": "A constitution is not only a list of "
              "entitlements. It is a compact &mdash; the state, the courts and the citizen each "
              "carry part of the load."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "The Union Government &amp; Its Structure"},

        {"type": "content", "label": "The Model", "title": "A parliamentary, federal democracy",
         "blocks": [
             {"t": "body", "html": "India is a <strong>parliamentary democracy</strong>: the real "
              "executive (the Prime Minister and Council of Ministers) is drawn from and "
              "accountable to the legislature, while the President is the constitutional head of "
              "state."},
             {"t": "hbox", "color": "cyan", "html": "This 'Westminster' model was adapted from "
              "Britain &mdash; but set within a written, supreme constitution and a federal "
              "structure, which Britain has neither of."},
         ]},

        {"type": "content", "label": "Three Organs", "title": "Legislature, executive, judiciary",
         "blocks": [
             {"t": "raw", "html":
              '<div style="display:flex;justify-content:center;margin:8px 0 14px">'
              '<svg viewBox="0 0 720 300" xmlns="http://www.w3.org/2000/svg" '
              'style="width:100%;max-width:720px;height:auto;font-family:inherit">'
              '<rect x="270" y="14" width="180" height="46" rx="8" fill="#1C1917" stroke="#0EA5E9" stroke-width="2"/>'
              '<text x="360" y="42" fill="#0EA5E9" font-size="17" font-weight="700" text-anchor="middle">THE CONSTITUTION</text>'
              '<line x1="360" y1="60" x2="360" y2="92" stroke="#6366F1" stroke-width="2"/>'
              '<line x1="130" y1="92" x2="590" y2="92" stroke="#6366F1" stroke-width="2"/>'
              '<line x1="130" y1="92" x2="130" y2="120" stroke="#6366F1" stroke-width="2"/>'
              '<line x1="360" y1="92" x2="360" y2="120" stroke="#6366F1" stroke-width="2"/>'
              '<line x1="590" y1="92" x2="590" y2="120" stroke="#6366F1" stroke-width="2"/>'
              '<rect x="40" y="120" width="180" height="64" rx="8" fill="#1C1917" stroke="#0EA5E9" stroke-width="2"/>'
              '<text x="130" y="148" fill="#0EA5E9" font-size="15" font-weight="700" text-anchor="middle">LEGISLATURE</text>'
              '<text x="130" y="170" fill="#94A3B8" font-size="12" text-anchor="middle">Makes the law</text>'
              '<rect x="270" y="120" width="180" height="64" rx="8" fill="#1C1917" stroke="#10B981" stroke-width="2"/>'
              '<text x="360" y="148" fill="#10B981" font-size="15" font-weight="700" text-anchor="middle">EXECUTIVE</text>'
              '<text x="360" y="170" fill="#94A3B8" font-size="12" text-anchor="middle">Implements the law</text>'
              '<rect x="500" y="120" width="180" height="64" rx="8" fill="#1C1917" stroke="#F59E0B" stroke-width="2"/>'
              '<text x="590" y="148" fill="#F59E0B" font-size="15" font-weight="700" text-anchor="middle">JUDICIARY</text>'
              '<text x="590" y="170" fill="#94A3B8" font-size="12" text-anchor="middle">Interprets the law</text>'
              '<text x="360" y="232" fill="#94A3B8" font-size="13" text-anchor="middle">'
              'Separation of powers with checks &amp; balances &mdash; each organ limits the others</text>'
              '<text x="360" y="260" fill="#64748B" font-size="11" text-anchor="middle">'
              'Illustrative diagram</text>'
              '</svg></div>'},
         ]},

        {"type": "content", "label": "Parliament", "title": "Two Houses make the Union legislature",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Lok Sabha", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The 'House of the People'. Directly elected; "
                   "represents the population; the government must keep its confidence."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Rajya Sabha", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The 'Council of States'. Indirectly elected; "
                   "represents the states; a permanent House that is never fully dissolved."}]}]},
             {"t": "hbox", "color": "amber", "html": "Two Houses serve two purposes: the Lok Sabha "
              "voices the people; the Rajya Sabha voices the states and adds a chamber of second "
              "thought."},
         ]},

        {"type": "content", "label": "Composition", "title": "Strength of the two Houses",
         "blocks": [
             {"t": "chart", "canvas": "housesChart",
              "title": "Approximate maximum strength of each House (illustrative)",
              "source": "Illustrative &mdash; approximate constitutional maxima",
              "type": "bar",
              "data": {"labels": ["Lok Sabha", "Rajya Sabha"],
                       "datasets": [{"label": "Members (max)", "data": [550, 250],
                                     "backgroundColor": ["#0EA5E9", "#6366F1"]}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ beginAtZero:true } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The Lok Sabha is far larger and directly "
              "elected &mdash; which is why the government is made and unmade there, not in the "
              "Rajya Sabha. Figures shown are approximate maxima, not current strength."},
         ]},

        {"type": "content", "label": "The Executive", "title": "President, Prime Minister, Council of Ministers",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Office", "Role"],
              "rows": [
                  ["President", "Constitutional head of state; acts on the advice of the Council of Ministers"],
                  ["Prime Minister", "Head of government; leads the Council; commands the Lok Sabha majority"],
                  ["Council of Ministers", "Runs the departments; collectively responsible to the Lok Sabha"],
                  ["Vice-President", "Ex-officio Chairperson of the Rajya Sabha"]]},
             {"t": "hbox", "color": "amber", "html": "Key point: the President is a "
              "<strong>nominal</strong> executive who, by convention and constitutional rule, acts "
              "on ministerial advice. Real executive power sits with the PM and Cabinet."},
         ]},

        {"type": "content", "label": "How a Bill Becomes Law", "title": "The path of legislation",
         "blocks": [
             {"t": "raw", "html":
              '<div style="display:flex;justify-content:center;margin:6px 0 12px">'
              '<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" '
              'style="width:100%;max-width:720px;height:auto;font-family:inherit">'
              '<g font-size="12" text-anchor="middle">'
              '<rect x="14" y="40" width="120" height="56" rx="8" fill="#1C1917" stroke="#0EA5E9" stroke-width="2"/>'
              '<text x="74" y="64" fill="#0EA5E9" font-weight="700">Bill introduced</text>'
              '<text x="74" y="82" fill="#94A3B8">in a House</text>'
              '<rect x="160" y="40" width="120" height="56" rx="8" fill="#1C1917" stroke="#6366F1" stroke-width="2"/>'
              '<text x="220" y="64" fill="#6366F1" font-weight="700">Debate &amp;</text>'
              '<text x="220" y="82" fill="#94A3B8">committee, vote</text>'
              '<rect x="306" y="40" width="120" height="56" rx="8" fill="#1C1917" stroke="#10B981" stroke-width="2"/>'
              '<text x="366" y="64" fill="#10B981" font-weight="700">Passed by</text>'
              '<text x="366" y="82" fill="#94A3B8">the other House</text>'
              '<rect x="452" y="40" width="120" height="56" rx="8" fill="#1C1917" stroke="#F59E0B" stroke-width="2"/>'
              '<text x="512" y="64" fill="#F59E0B" font-weight="700">President\'s</text>'
              '<text x="512" y="82" fill="#94A3B8">assent</text>'
              '<rect x="598" y="40" width="108" height="56" rx="8" fill="#1C1917" stroke="#EF4444" stroke-width="2"/>'
              '<text x="652" y="64" fill="#EF4444" font-weight="700">Becomes</text>'
              '<text x="652" y="82" fill="#94A3B8">an Act</text>'
              '<text x="146" y="72" fill="#64748B">&rarr;</text>'
              '<text x="292" y="72" fill="#64748B">&rarr;</text>'
              '<text x="438" y="72" fill="#64748B">&rarr;</text>'
              '<text x="584" y="72" fill="#64748B">&rarr;</text>'
              '<text x="360" y="150" fill="#94A3B8">Both Houses must agree; Money Bills follow a special route favouring the Lok Sabha</text>'
              '<text x="360" y="190" fill="#64748B" font-size="11">Illustrative &mdash; simplified path of an ordinary Bill</text>'
              '</g></svg></div>'},
         ]},

        {"type": "content", "label": "Separation of Powers", "title": "Checks and balances, Indian style",
         "blocks": [
             {"t": "body", "html": "India does not have a rigid separation of powers like the "
              "United States. The executive sits inside the legislature. But the "
              "<strong>judiciary is independent</strong>, and judicial review keeps both the "
              "legislature and executive within constitutional limits."},
             {"t": "hbox", "color": "cyan", "html": "The balance is dynamic: each organ checks the "
              "others. An independent judiciary is the keystone &mdash; it can strike down both "
              "unconstitutional laws and unlawful executive action."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Federalism: Union, States &amp; the Schedules"},

        {"type": "content", "label": "Federalism", "title": "Power shared between two levels",
         "blocks": [
             {"t": "body", "html": "India is a <strong>federation</strong>: governing power is "
              "divided between a national <strong>Union</strong> government and the "
              "<strong>State</strong> governments, each with its own sphere set by the "
              "Constitution &mdash; not by the goodwill of the other."},
             {"t": "term", "word": "Federalism",
              "def": "A system in which sovereignty is constitutionally shared between a central "
              "government and regional (state) governments, each supreme in its own assigned "
              "domain."},
         ]},

        {"type": "content", "label": "Seventh Schedule", "title": "Three lists divide the subjects",
         "blocks": [
             {"t": "chart", "canvas": "listsChart",
              "title": "Approximate number of entries in each legislative list (illustrative)",
              "source": "Illustrative &mdash; Seventh Schedule, approximate counts",
              "type": "bar",
              "data": {"labels": ["Union List", "State List", "Concurrent List"],
                       "datasets": [{"label": "Entries (approx.)", "data": [98, 59, 52],
                                     "backgroundColor": ["#0EA5E9", "#10B981", "#F59E0B"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The <strong>Seventh Schedule</strong> splits "
              "subjects into three lists. Entry counts have shifted over time; figures here are "
              "approximate and illustrative."},
         ]},

        {"type": "content", "label": "The Three Lists", "title": "Who legislates on what",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["List", "Who legislates", "Examples"],
              "rows": [
                  ["Union List", "Parliament only", "Defence, foreign affairs, currency, railways"],
                  ["State List", "State legislatures", "Police, public health, agriculture, land"],
                  ["Concurrent List", "Both (Union prevails if clash)", "Education, forests, marriage, criminal law"]]},
             {"t": "hbox", "color": "amber", "html": "If a Union and State law on a Concurrent "
              "subject conflict, the Union law generally prevails. <strong>Residuary powers</strong> "
              "&mdash; subjects on no list &mdash; rest with the Union."},
         ]},

        {"type": "content", "label": "Quasi-Federal", "title": "A federation with a strong Centre",
         "blocks": [
             {"t": "body", "html": "Scholars call India <strong>quasi-federal</strong> or a "
              "'holding-together' federation: federal in normal times, but tilted toward the "
              "Centre, which can become dominant in an emergency or where the Constitution gives "
              "it overriding power."},
             {"t": "hbox", "color": "cyan", "html": "The Constitution even avoids the word "
              "'federation'. Article 1 calls India a <strong>'Union of States'</strong> &mdash; "
              "deliberately signalling an indissoluble whole, not a pact states may leave."},
         ]},

        {"type": "content", "label": "Holding Together", "title": "Why India chose a strong Centre",
         "blocks": [
             {"t": "body", "html": "Drafted in the shadow of Partition, the Constitution prized "
              "<strong>unity</strong>. A strong Centre was a deliberate choice to hold a diverse, "
              "newly independent nation together against fragmentation."},
             {"t": "hbox", "color": "amber", "html": "The trade-off is real and live: a Centre "
              "strong enough to hold the nation together can also crowd the states. Indian "
              "federalism is a continuing negotiation, not a fixed line."},
         ]},

        {"type": "content", "label": "Cooperative Federalism", "title": "Working across levels",
         "blocks": [
             {"t": "body", "html": "In practice, much governance is <strong>cooperative</strong>: "
              "the Union and states share revenue, plan together and run joint schemes. Bodies for "
              "fiscal sharing and inter-state coordination smooth the overlaps."},
             {"t": "hbox", "color": "green", "html": "For practitioners, this matters: a single "
              "programme often involves Union funds, state implementation and local delivery &mdash; "
              "three levels that must align."},
         ]},

        {"type": "content", "label": "Emergencies", "title": "Three kinds of emergency provision",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Type", "Trigger (broadly)"],
              "rows": [
                  ["National emergency", "War, external aggression or armed rebellion"],
                  ["State emergency (President's Rule)", "Breakdown of constitutional machinery in a state"],
                  ["Financial emergency", "A threat to the financial stability of India"]]},
             {"t": "hbox", "color": "red", "html": "Emergencies let the Centre concentrate power &mdash; "
              "which is why they are hedged with safeguards. The 1975&ndash;77 national emergency "
              "led to amendments strengthening the limits on this power."},
         ]},

        {"type": "content", "label": "Asymmetry", "title": "Federalism is not one-size-fits-all",
         "blocks": [
             {"t": "body", "html": "Indian federalism is <strong>asymmetric</strong>: some states "
              "and areas have special constitutional arrangements recognising distinct histories "
              "and tribal self-governance, alongside Union Territories administered differently "
              "from states."},
             {"t": "hbox", "color": "cyan", "html": "Special schedules protect tribal areas and "
              "their customary governance &mdash; a reminder that equal citizenship can coexist "
              "with tailored institutions for distinct communities."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "The Judiciary &amp; Judicial Review"},

        {"type": "content", "label": "One System", "title": "A single, integrated judiciary",
         "blocks": [
             {"t": "body", "html": "Unlike some federations, India has a single "
              "<strong>integrated</strong> judiciary: the <strong>Supreme Court</strong> at the "
              "apex, <strong>High Courts</strong> in the states, and subordinate courts below &mdash; "
              "one ladder applying both Union and state law."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Supreme Court", "label": "Apex court; guardian of the Constitution",
                  "color": "amber"},
                 {"num": "High Courts", "label": "Top court in each state / group of states",
                  "color": "cyan"},
                 {"num": "Subordinate", "label": "District and lower courts", "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Independence", "title": "An independent judiciary",
         "blocks": [
             {"t": "body", "html": "Judicial independence is protected by the Constitution: "
              "security of tenure, salaries charged on the Consolidated Fund, and a difficult "
              "removal process insulate judges from pressure by the government of the day."},
             {"t": "hbox", "color": "cyan", "html": "Independence is not a privilege for judges &mdash; "
              "it is a guarantee for citizens. Only a fearless court can hold a powerful executive "
              "to the Constitution."},
         ]},

        {"type": "content", "label": "Judicial Review", "title": "Courts can strike down bad laws",
         "blocks": [
             {"t": "term", "word": "Judicial review",
              "def": "The power of the courts to examine laws and executive actions and to declare "
              "them void if they violate the Constitution. It makes the Constitution genuinely "
              "supreme."},
             {"t": "hbox", "color": "amber", "html": "Because the Constitution is the highest law, "
              "any statute that conflicts with it is, to that extent, void. Judicial review is the "
              "mechanism that enforces that supremacy."},
         ]},

        {"type": "content", "label": "Access", "title": "Original, appellate and advisory roles",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Original jurisdiction:</strong> disputes between the Union and states, "
                 "and Article 32 rights petitions",
                 "<strong>Appellate jurisdiction:</strong> appeals from the High Courts in "
                 "constitutional, civil and criminal matters",
                 "<strong>Advisory jurisdiction:</strong> the President may seek the Court's "
                 "opinion on questions of law",
                 "<strong>Writ jurisdiction:</strong> enforcing Fundamental Rights"]},
         ]},

        {"type": "content", "label": "PILs", "title": "Public Interest Litigation opens the courthouse door",
         "blocks": [
             {"t": "body", "html": "<strong>Public Interest Litigation (PIL)</strong> relaxed the "
              "old rule that only the directly affected person could sue. Now a public-spirited "
              "individual or group can approach the court on behalf of those too poor or "
              "marginalised to do so themselves."},
             {"t": "hbox", "color": "green", "html": "PIL transformed access to justice on issues "
              "like bonded labour, prison conditions, environment and the right to food &mdash; a "
              "powerful tool, used responsibly, for rights-based work."},
         ]},

        {"type": "content", "label": "The Big Question", "title": "Can Parliament amend any part it likes?",
         "blocks": [
             {"t": "body", "html": "A defining struggle in Indian constitutional history asked: "
              "is Parliament's power to amend the Constitution <strong>unlimited</strong>? Could "
              "it amend away even the Fundamental Rights, or the Constitution's core itself?"},
             {"t": "hbox", "color": "amber", "html": "The answer, reached in 1973, reshaped the "
              "balance between Parliament and the courts &mdash; and protects the Constitution "
              "from being rewritten beyond recognition."},
         ]},

        {"type": "content", "label": "Kesavananda Bharati", "title": "The Basic Structure doctrine, 1973",
         "blocks": [
             {"t": "body", "html": "In <strong>Kesavananda Bharati (1973)</strong>, the Supreme "
              "Court held that Parliament can amend the Constitution &mdash; but cannot alter or "
              "destroy its <strong>'basic structure'</strong>. Some core features lie beyond the "
              "reach of any amendment."},
             {"t": "quote",
              "text": "The amending power cannot be used to destroy or abrogate the basic "
              "structure or framework of the Constitution.",
              "attr": "&mdash; the principle of Kesavananda Bharati v. State of Kerala (1973)"},
         ]},

        {"type": "content", "label": "Basic Structure", "title": "What counts as the 'basic structure'?",
         "blocks": [
             {"t": "body", "html": "The Court has never fixed a closed list, but features "
              "repeatedly recognised as part of the basic structure include:"},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Supremacy of the Constitution and the rule of law",
                 "Separation of powers and judicial review",
                 "Federalism and secularism",
                 "Free and fair elections; democratic government",
                 "The essence of Fundamental Rights"]},
             {"t": "hbox", "color": "amber", "html": "The doctrine is a safety catch: it lets the "
              "Constitution evolve through amendment while guarding the identity that makes it "
              "<em>this</em> Constitution."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Local Self-Government"},

        {"type": "content", "label": "The Third Tier", "title": "Government closest to the people",
         "blocks": [
             {"t": "body", "html": "Beyond the Union and the states lies a <strong>third tier</strong>: "
              "elected local government. Until 1992 it was weak and discretionary; two amendments "
              "made it a constitutional mandate &mdash; bringing democracy down to the village and "
              "the ward."},
             {"t": "hbox", "color": "cyan", "html": "Local self-government is where most citizens "
              "actually meet the state &mdash; for water, roads, sanitation, schools and welfare. "
              "Its strength shapes everyday rights."},
         ]},

        {"type": "content", "label": "73rd &amp; 74th", "title": "The 1992 amendments that created the third tier",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "73rd Amendment", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Constitutionalises <strong>Panchayati Raj</strong> "
                   "&mdash; rural local government &mdash; with the new Part IX."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "74th Amendment", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Constitutionalises <strong>Municipalities</strong> "
                   "&mdash; urban local government &mdash; with the new Part IX-A."}]}]},
             {"t": "hbox", "color": "amber", "html": "Together, the <strong>73rd and 74th "
              "Amendments (1992)</strong> made local elections mandatory and gave local bodies "
              "constitutional standing &mdash; one of the largest experiments in grassroots "
              "democracy anywhere."},
         ]},

        {"type": "content", "label": "Three Tiers", "title": "Panchayats at village, block and district",
         "blocks": [
             {"t": "flow", "steps": [
                 "GRAM PANCHAYAT: the village level",
                 "PANCHAYAT SAMITI: the intermediate / block level",
                 "ZILA PARISHAD: the district level"]},
             {"t": "hbox", "color": "cyan", "html": "Smaller states may have fewer tiers. The "
              "structure mirrors the federal idea &mdash; nested levels, each elected, each with "
              "its own sphere."},
         ]},

        {"type": "content", "label": "Gram Sabha", "title": "The Gram Sabha: direct democracy",
         "blocks": [
             {"t": "term", "word": "Gram Sabha",
              "def": "The assembly of all adult voters of a village &mdash; the deliberative body "
              "to which the elected Gram Panchayat is answerable. A rare instance of direct, not "
              "merely representative, democracy."},
             {"t": "hbox", "color": "green", "html": "The Gram Sabha approves plans, selects "
              "beneficiaries and audits spending. Active Gram Sabhas are a frontline tool for "
              "transparency and accountability in development."},
         ]},

        {"type": "content", "label": "Reservations", "title": "Reservations in local government",
         "blocks": [
             {"t": "body", "html": "The amendments require <strong>reservation of seats</strong> "
              "for Scheduled Castes and Scheduled Tribes in proportion to their population, and for "
              "<strong>women</strong> &mdash; including reservation of the office of chairperson."},
             {"t": "hbox", "color": "amber", "html": "Many states reserve a third or more of seats "
              "for women, bringing large numbers of women into elected office &mdash; a major, if "
              "uneven, shift in who holds local power."},
         ]},

        {"type": "content", "label": "Functions &amp; Finance", "title": "Powers on paper vs power in practice",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Mandate", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The Eleventh and Twelfth Schedules list "
                   "subjects states <em>may</em> devolve &mdash; from water and sanitation to "
                   "primary education and welfare."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Reality", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Devolution of <strong>funds, functions and "
                   "functionaries</strong> varies widely; many local bodies remain "
                   "under-resourced."}]}]},
             {"t": "hbox", "color": "amber", "html": "The famous '3 Fs': real local power needs "
              "<strong>funds, functions and functionaries</strong> together. Seats without "
              "resources are influence without power."},
         ]},

        {"type": "content", "label": "Tribal Areas", "title": "PESA and self-rule in Scheduled Areas",
         "blocks": [
             {"t": "body", "html": "In tribal <strong>Scheduled Areas</strong>, a special law "
              "extends Panchayati Raj with stronger powers for the Gram Sabha &mdash; recognising "
              "customary self-governance and giving communities a say over local resources."},
             {"t": "hbox", "color": "green", "html": "This is local self-government adapted to "
              "context: it strengthens tribal communities' control over their land, forests and "
              "decisions, consistent with the Constitution's protective provisions."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Amending the Constitution"},

        {"type": "content", "label": "A Living Document", "title": "Built to change &mdash; carefully",
         "blocks": [
             {"t": "body", "html": "A constitution must endure for generations, yet adapt to "
              "changing times. India's is a <strong>living document</strong>: amendable, but "
              "through a process more demanding than ordinary law-making."},
             {"t": "hbox", "color": "cyan", "html": "The drafters sought a middle path &mdash; not "
              "so rigid it cannot adapt, not so flexible that it bends to every passing majority."},
         ]},

        {"type": "content", "label": "Article 368", "title": "The amendment power",
         "blocks": [
             {"t": "term", "word": "Article 368",
              "def": "The provision setting out Parliament's power and procedure to amend the "
              "Constitution &mdash; including the special majorities required, and, for some "
              "provisions, the consent of the states."},
             {"t": "hbox", "color": "amber", "html": "Article 368 is the Constitution's own clause "
              "for self-revision &mdash; but, since 1973, it cannot be used to destroy the basic "
              "structure."},
         ]},

        {"type": "content", "label": "Three Routes", "title": "How an amendment is passed",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Route", "Requirement"],
              "rows": [
                  ["Simple majority", "Some provisions amendable by ordinary majority (outside Article 368)"],
                  ["Special majority", "Majority of total membership and two-thirds of those present and voting in each House"],
                  ["Special majority + states", "The above, plus ratification by half the state legislatures for federal provisions"]]},
             {"t": "hbox", "color": "cyan", "html": "Changes touching federalism &mdash; the "
              "distribution of powers, the courts, the election of the President &mdash; need the "
              "states' consent too. The deeper the change, the higher the bar."},
         ]},

        {"type": "content", "label": "The Pace", "title": "Amendments by decade",
         "blocks": [
             {"t": "chart", "canvas": "amendChart",
              "title": "Constitutional amendments per decade (illustrative)",
              "source": "Illustrative &mdash; approximate, for pattern only",
              "type": "bar",
              "data": {"labels": ["1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s"],
                       "datasets": [{"label": "Amendments (approx.)",
                                     "data": [10, 15, 22, 20, 17, 12, 10],
                                     "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true } } }"}},
             {"t": "hbox", "color": "amber", "html": "The Constitution has been amended over a "
              "hundred times. The 1970s stand out &mdash; a turbulent decade of land reform, the "
              "Emergency and the basic-structure battle. Figures shown are illustrative."},
         ]},

        {"type": "content", "label": "Landmark Amendments", "title": "Amendments that reshaped the text",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Amendment", "What it did"],
              "rows": [
                  ["42nd (1976)", "Added 'Socialist', 'Secular', Fundamental Duties; expanded central power"],
                  ["44th (1978)", "Rolled back several 42nd-Amendment changes; strengthened rights"],
                  ["73rd &amp; 74th (1992)", "Constitutionalised panchayats and municipalities"],
                  ["86th (2002)", "Added Article 21A &mdash; the right to education"],
                  ["101st (2016)", "Introduced the Goods and Services Tax (GST)"]]},
             {"t": "hbox", "color": "cyan", "html": "The <strong>42nd Amendment</strong> is often "
              "called a 'mini-constitution' for the scale of its changes; much of it was later "
              "reversed by the 44th."},
         ]},

        {"type": "content", "label": "Courts and Amendments", "title": "Cases that defined the amending power",
         "blocks": [
             {"t": "flow", "steps": [
                 "GOLAKNATH (1967): courts limit amending of Fundamental Rights",
                 "24th &amp; 25th AMENDMENTS: Parliament asserts its power",
                 "KESAVANANDA (1973): basic structure cannot be destroyed",
                 "LATER CASES: the doctrine applied to strike down overreach"]},
             {"t": "hbox", "color": "amber", "html": "This back-and-forth between Parliament and "
              "the courts is not dysfunction &mdash; it is the checks-and-balances system finding "
              "the limits of each branch's power."},
         ]},

        {"type": "content", "label": "Why Limits Help", "title": "Why an unamendable core protects democracy",
         "blocks": [
             {"t": "body", "html": "The basic-structure doctrine means a temporary majority "
              "&mdash; however large &mdash; cannot abolish elections, judicial review or "
              "federalism. The rules of the democratic game are placed beyond the reach of any "
              "single winner."},
             {"t": "hbox", "color": "green", "html": "This is constitutionalism's deepest idea: "
              "some commitments are made <em>permanent</em> precisely so that democracy cannot "
              "vote itself out of existence."},
         ]},

        {"type": "content", "label": "Living Constitution", "title": "Two ways the Constitution evolves",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "By amendment", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Parliament formally changes the text through "
                   "Article 368 &mdash; the deliberate, visible route."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "By interpretation", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Courts read the same words in new ways &mdash; "
                   "as with Article 21's growth into dignity, privacy and a clean environment."}]}]},
             {"t": "hbox", "color": "amber", "html": "Both keep the Constitution alive. The text "
              "is fixed on the page but its meaning breathes &mdash; this is what 'living "
              "document' really means."},
         ]},

        {"type": "content", "label": "Stability and Change", "title": "An enduring balance",
         "blocks": [
             {"t": "body", "html": "Seven decades on, the Constitution has been amended often, "
              "interpreted continuously, and stretched by crises &mdash; yet it has held. Its "
              "blend of flexibility and a protected core is a large part of why."},
             {"t": "quote",
              "text": "The Constitution is not a mere lawyers' document; it is a vehicle of life, "
              "and its spirit is always the spirit of the age.",
              "attr": "&mdash; B.R. Ambedkar"},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Constitutionalism in Practice"},

        {"type": "content", "label": "Constitutionalism", "title": "Having a constitution is not enough",
         "blocks": [
             {"t": "term", "word": "Constitutionalism",
              "def": "The practice of actually limiting government by constitutional rules &mdash; "
              "not just having a written document, but living by its restraints, rights and "
              "institutions."},
             {"t": "hbox", "color": "cyan", "html": "Many regimes have constitutions on paper. "
              "Constitutionalism is the harder thing: independent courts, free elections and a "
              "rights culture that hold power to account in practice."},
         ]},

        {"type": "content", "label": "Rights-Based Programming", "title": "From beneficiaries to rights-holders",
         "blocks": [
             {"t": "body", "html": "A <strong>rights-based approach</strong> reframes development: "
              "people are not passive recipients of charity but <strong>rights-holders</strong> "
              "with constitutional and legal entitlements, and the state is a duty-bearer."},
             {"t": "hbox", "color": "green", "html": "This shift &mdash; from needs to rights "
              "&mdash; draws its authority straight from the Constitution. It changes how you "
              "design, demand and audit a programme."},
         ]},

        {"type": "content", "label": "Rights into Law", "title": "Constitutional values made statutory",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Law", "Constitutional root"],
              "rows": [
                  ["Right to Education Act, 2009", "Article 21A (86th Amendment, 2002)"],
                  ["Right to Information Act, 2005", "Article 19 &mdash; freedom of speech &amp; expression"],
                  ["MGNREGA, 2005", "Right to livelihood read into Article 21"],
                  ["Forest Rights Act, 2006", "Equality, livelihood and tribal rights"]]},
             {"t": "hbox", "color": "amber", "html": "Each landmark welfare law traces back to a "
              "constitutional value &mdash; the Constitution sets the direction; statutes turn it "
              "into enforceable entitlement."},
         ]},

        {"type": "content", "label": "RTI", "title": "The Right to Information",
         "blocks": [
             {"t": "body", "html": "The <strong>Right to Information Act, 2005</strong> flows from "
              "the right to free expression: an informed citizen is essential to democracy. It "
              "lets any citizen demand records from public authorities."},
             {"t": "hbox", "color": "green", "html": "RTI is among the most powerful tools a "
              "practitioner has: it makes the workings of the state visible, and underpins social "
              "audits and accountability work."},
         ]},

        {"type": "content", "label": "Privacy", "title": "Puttaswamy, 2017: privacy is a fundamental right",
         "blocks": [
             {"t": "body", "html": "In <strong>K.S. Puttaswamy v. Union of India (2017)</strong>, "
              "a nine-judge bench held that the <strong>right to privacy</strong> is a fundamental "
              "right, protected as part of the right to life and personal liberty under Article 21."},
             {"t": "hbox", "color": "cyan", "html": "A vivid example of the living Constitution: "
              "the word 'privacy' appears nowhere in the text, yet the Court found it within "
              "Article 21's guarantee of life and dignity."},
         ]},

        {"type": "content", "label": "Dignity &amp; Equality", "title": "NALSA and Navtej Johar",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "NALSA (2014)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The Supreme Court recognised transgender "
                   "persons as a 'third gender' and affirmed their rights to equality and "
                   "dignity."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Navtej Johar (2018)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The Court read down Section 377 to "
                   "decriminalise consensual same-sex relations between adults, affirming "
                   "dignity and equality."}]}]},
             {"t": "hbox", "color": "amber", "html": "Both rulings built on Articles 14, 15, 19 "
              "and 21 &mdash; equality, freedom and dignity &mdash; showing how old text protects "
              "new claims to inclusion."},
         ]},

        {"type": "content", "label": "Everyday Constitution", "title": "Where citizens meet the Constitution",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Voting in free and fair elections &mdash; universal adult franchise",
                 "Filing an RTI to see how public money is spent",
                 "Approaching a court when an entitlement is denied",
                 "A Gram Sabha holding its panchayat to account",
                 "A reservation that opens a seat, a job, a classroom"]},
             {"t": "hbox", "color": "green", "html": "The Constitution is not only in courtrooms. "
              "It lives in queues, classrooms, ration shops and panchayat meetings &mdash; "
              "wherever a citizen claims a right."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "A short reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>The Constitution of India</em> &mdash; the bare text (read the Preamble &amp; Part III)",
                 "<em>Introduction to the Constitution of India</em> &mdash; D.D. Basu",
                 "<em>The Indian Constitution: Cornerstone of a Nation</em> &mdash; Granville Austin",
                 "<em>Constituent Assembly Debates</em> &mdash; the drafters in their own words",
                 "Judgments: Kesavananda Bharati (1973), Puttaswamy (2017)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Human Rights</strong>, <strong>Governance &amp; Accountability</strong> and "
              "<strong>Public Policy</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>The Constitution is supreme</strong> &mdash; every law and act must conform to it",
                 "<strong>Rights come with remedies</strong> &mdash; Article 32 is their 'heart and soul'",
                 "<strong>Power is divided</strong> &mdash; across organs and across Union, states and local government",
                 "<strong>The basic structure is protected</strong> &mdash; no majority can amend it away",
                 "<strong>It is a living document</strong> &mdash; behind every clause is a citizen's dignity"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Indian Constitution 101 &middot; Complete",
         "headline": "We, the People<br>&mdash; that means you.",
         "byline": "The Constitution is not a relic for lawyers; it is a living promise every "
                   "citizen can claim and every practitioner can wield. Explore the rest of the "
                   "ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Human Rights 101", "href": "https://www.impactmojo.in/101-courses/"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
