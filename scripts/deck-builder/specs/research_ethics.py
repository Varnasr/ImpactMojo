# -*- coding: utf-8 -*-
"""
Research Ethics 101 — ImpactMojo 101 Series (native deck spec)
Foundational research ethics for South Asian development practitioners.
Build: python3 scripts/deck-builder/build.py research_ethics
"""

DECK = {
    "slug": "research-ethics",
    "title": "Research Ethics 101",
    "description": ("Research Ethics 101 — a free foundational course for development "
                    "practitioners and researchers in South Asia. From the Nuremberg Code and "
                    "the Belmont principles to informed consent, vulnerable populations, "
                    "privacy, ethics review under ICMR 2017 and India's DPDP Act 2023. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Research<br>Ethics<br>101",
         "sub": "Consent, Dignity &amp; Doing No Harm &mdash; a Foundational Course on "
                "Research Ethics for Development Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "~90 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "Why Research Ethics Matters", "slides": "Slides 3&ndash;10"},
             {"name": "History &amp; Codes", "slides": "Slides 11&ndash;19"},
             {"name": "Core Principles", "slides": "Slides 20&ndash;28"},
             {"name": "Informed Consent", "slides": "Slides 29&ndash;37"},
             {"name": "Vulnerable Populations &amp; Power", "slides": "Slides 38&ndash;46"},
             {"name": "Privacy, Confidentiality &amp; Anonymity", "slides": "Slides 47&ndash;56"},
             {"name": "Do No Harm &amp; Risk&ndash;Benefit", "slides": "Slides 57&ndash;65"},
             {"name": "Ethics Review in India", "slides": "Slides 66&ndash;74"},
             {"name": "Field Realities &amp; Dilemmas", "slides": "Slides 75&ndash;83"},
             {"name": "Data Ethics, Ownership &amp; Dissemination", "slides": "Slides 84&ndash;92"},
             {"name": "Putting It to Work", "slides": "Slides 93&ndash;99"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why Research Ethics Matters"},

        {"type": "content", "label": "The Premise", "title": "Every row in your data is a person",
         "blocks": [
             {"t": "body", "html": "Development research runs on people &mdash; their bodies, "
              "their households, their grief, their poverty. When you survey, interview, photograph "
              "or trial something with them, you take something from them. <strong>Research "
              "ethics</strong> is the discipline of taking responsibly."},
             {"t": "quote", "text": "Data are not just numbers; they are people reduced to "
              "numbers. The reduction is never neutral.",
              "attr": "&mdash; a principle of feminist data practice"},
         ]},

        {"type": "content", "label": "Definition", "title": "Research ethics, defined",
         "blocks": [
             {"t": "term", "word": "Research ethics",
              "def": "The set of principles and procedures that govern how we treat people, "
              "communities and data in research &mdash; ensuring respect, minimising harm, and "
              "distributing benefits and burdens fairly."},
             {"t": "hbox", "color": "cyan", "html": "Ethics is not a form you sign at the end. It "
              "is a way of thinking that runs from the research question to the final report and "
              "beyond &mdash; into how findings are used."},
         ]},

        {"type": "content", "label": "Power", "title": "Research is rarely between equals",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "The researcher holds", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Education, language, institutional backing",
                      "Control over what is asked and recorded",
                      "The power to publish &mdash; or not",
                      "Often, the keys to a programme or benefit"]}]}],
              "right": [{"t": "panel", "color": "amber", "title": "The participant often", "blocks": [
                  {"t": "bullets", "sm": True, "color": "amber", "items": [
                      "Is poorer, with less formal schooling",
                      "May fear losing a service by refusing",
                      "Gives time and trust for little return",
                      "Cannot check how their words are used"]}]}]},
             {"t": "hbox", "color": "red", "html": "This asymmetry is the reason ethics exists. "
              "Where power is unequal, &lsquo;they agreed&rsquo; is not enough."},
         ]},

        {"type": "content", "label": "Consent of the Governed", "title": "No research about us, without us",
         "blocks": [
             {"t": "body", "html": "Ethical research treats participants as the authors of their "
              "own lives, not as raw material. They consent to take part, shape what is asked, and "
              "retain a stake in what is found. <strong>Consent of the governed</strong> applies "
              "to knowledge as much as to politics."},
             {"t": "hbox", "color": "green", "html": "The test: could you explain your study, "
              "honestly and in full, to the people in it &mdash; and would they still agree?"},
         ]},

        {"type": "content", "label": "Why It Goes Wrong", "title": "Good intentions are not a safeguard",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Convenience:</strong> the poor are easy to study and rarely complain",
                 "<strong>Pressure:</strong> deadlines and donors push for data, fast",
                 "<strong>Distance:</strong> the analyst never meets the row in the spreadsheet",
                 "<strong>Habit:</strong> &lsquo;we always did it this way&rsquo;"]},
             {"t": "hbox", "color": "amber", "html": "Most ethical harm in development research is "
              "not malice. It is thoughtlessness, hurry and unexamined power."},
         ]},

        {"type": "content", "label": "The Stakes", "title": "What is at risk when ethics fails",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "People", "label": "Real harm &mdash; distress, stigma, breach of trust, "
                  "even physical or legal danger", "color": "red"},
                 {"num": "Truth", "label": "Coerced or careless data is bad data &mdash; ethics "
                  "and rigour rise together", "color": "amber"},
                 {"num": "Trust", "label": "One extractive study can close a community to "
                  "researchers for years", "color": "indigo"}]},
             {"t": "hbox", "color": "cyan", "html": "Ethics is not the enemy of good research. "
              "Unethical research is almost always weak research too."},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Foundations", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Why ethics matters; history &amp; codes",
                      "The three core principles",
                      "Informed consent in real conditions"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Practice", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Vulnerable groups, privacy, do-no-harm",
                      "Ethics review in India; field dilemmas",
                      "Data ethics and a working checklist"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Throughout, examples and rules come from India "
              "and the wider region &mdash; the conditions you will actually work in."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "History &amp; Codes"},

        {"type": "content", "label": "Why History", "title": "The rules were written in blood",
         "blocks": [
             {"t": "body", "html": "Modern research ethics did not arrive as abstract philosophy. "
              "Each major code was a response to a documented abuse &mdash; people harmed, deceived "
              "or experimented on without consent. To understand the rules, know what they answer."},
             {"t": "hbox", "color": "amber", "html": "The codes are not bureaucracy invented to "
              "slow you down. They are hard-won lessons from research that wounded people."},
         ]},

        {"type": "content", "label": "1947", "title": "The Nuremberg Code",
         "blocks": [
             {"t": "body", "html": "After the Second World War, the Nuremberg trials exposed brutal "
              "experiments performed on prisoners without consent. The <strong>Nuremberg Code "
              "(1947)</strong> was the response &mdash; the first international statement that "
              "research on humans requires consent."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Voluntary consent is &lsquo;absolutely essential&rsquo;",
                 "Participants may withdraw at any time",
                 "Risks must be justified by the expected benefit",
                 "Avoidable suffering and injury must be prevented"]},
             {"t": "hbox", "color": "indigo", "html": "Its first principle &mdash; voluntary, "
              "informed consent &mdash; remains the foundation of all research ethics today."},
         ]},

        {"type": "content", "label": "1964", "title": "The Declaration of Helsinki",
         "blocks": [
             {"t": "body", "html": "Adopted by the World Medical Association in <strong>1964</strong> "
              "and revised many times since, the <strong>Declaration of Helsinki</strong> turned "
              "broad principles into working guidance for medical research, and introduced the idea "
              "of independent ethics review."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "The participant&rsquo;s wellbeing takes priority over science and society",
                 "Independent committees should review research protocols",
                 "Special protections for those who cannot consent for themselves",
                 "Findings should be reported honestly and completely"]},
         ]},

        {"type": "content", "label": "1932&ndash;1972", "title": "Tuskegee: a study that betrayed",
         "blocks": [
             {"t": "body", "html": "In the U.S. Public Health Service&rsquo;s <strong>Tuskegee "
              "Syphilis Study (1932&ndash;1972)</strong>, hundreds of poor Black men with syphilis "
              "were observed for decades and deliberately left untreated &mdash; even after "
              "penicillin became a standard cure &mdash; and were never told the truth about their "
              "condition."},
             {"t": "hbox", "color": "red", "html": "Tuskegee shows every failure at once: no "
              "consent, deception, exploitation of the poor and marginalised, and treatment "
              "withheld. Its exposure forced the modern system of ethics oversight into being."},
         ]},

        {"type": "content", "label": "Lessons", "title": "What Tuskegee teaches development research",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Poverty and marginalisation make people easy to exploit &mdash; and easy to ignore",
                 "&lsquo;Just observing&rsquo; can still cause profound harm",
                 "Withholding benefit or information is itself an ethical breach",
                 "Trust, once broken, damages a whole community&rsquo;s relationship with research"]},
             {"t": "hbox", "color": "amber", "html": "The men were chosen <em>because</em> they were "
              "poor and powerless. That is precisely the population development research works "
              "with &mdash; so this history is not foreign; it is a warning aimed at us."},
         ]},

        {"type": "content", "label": "1979", "title": "The Belmont Report",
         "blocks": [
             {"t": "body", "html": "Issued in the United States in <strong>1979</strong> in the wake "
              "of Tuskegee, the <strong>Belmont Report</strong> distilled research ethics into three "
              "principles that still anchor ethics review worldwide."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Respect", "label": "for persons &mdash; autonomy &amp; consent", "color": "cyan"},
                 {"num": "Beneficence", "label": "maximise benefit, minimise harm", "color": "green"},
                 {"num": "Justice", "label": "fair distribution of risk &amp; benefit", "color": "indigo"}]},
             {"t": "hbox", "color": "cyan", "html": "We unpack all three in the next section &mdash; "
              "they translate directly into how you design and conduct fieldwork."},
         ]},

        {"type": "content", "label": "Timeline", "title": "A century of codifying conscience",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Year", "Milestone", "What it added"],
              "rows": [
                  ["1947", "Nuremberg Code", "Voluntary consent is essential"],
                  ["1964", "Declaration of Helsinki", "Ethics review; wellbeing over science"],
                  ["1972", "Tuskegee exposed", "Catalyst for modern oversight"],
                  ["1979", "Belmont Report", "Three guiding principles"],
                  ["1982/93", "CIOMS guidelines", "Ethics for low-resource &amp; global settings"],
                  ["2017", "ICMR National Guidelines", "India&rsquo;s comprehensive framework"],
                  ["2023", "DPDP Act (India)", "Personal data protection in law"]]},
         ]},

        {"type": "content", "label": "Global to Local", "title": "From Western codes to Indian guidance",
         "blocks": [
             {"t": "body", "html": "The early codes came from Europe and North America. But ethics "
              "in a context of deep poverty, low literacy and stark power gaps needs more than "
              "imported rules. The <strong>CIOMS</strong> guidelines and India&rsquo;s own "
              "<strong>ICMR</strong> framework adapt these principles to low-resource realities."},
             {"t": "hbox", "color": "green", "html": "We return to India&rsquo;s system &mdash; "
              "ICMR 2017, Institutional Ethics Committees and the DPDP Act &mdash; in Section Eight."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Core Principles"},

        {"type": "content", "label": "The Three Pillars", "title": "Belmont's principles, in practice",
         "blocks": [
             {"t": "flow", "steps": [
                 "RESPECT FOR PERSONS: treat people as autonomous; protect those who aren't",
                 "BENEFICENCE: do good, do no harm, weigh risk against benefit",
                 "JUSTICE: share the burdens and benefits of research fairly"]},
             {"t": "hbox", "color": "cyan", "html": "Every ethics committee, consent form and "
              "field protocol is an attempt to operationalise these three ideas. Learn them and you "
              "can reason through situations no checklist anticipated."},
         ]},

        {"type": "content", "label": "Principle One", "title": "Respect for persons &amp; autonomy",
         "blocks": [
             {"t": "term", "word": "Autonomy",
              "def": "The right of a competent person to make an informed, voluntary decision about "
              "whether to take part in research &mdash; free from coercion or manipulation."},
             {"t": "body", "html": "Respect for persons has two parts: honour the choices of those "
              "who <em>can</em> decide for themselves, and <strong>protect</strong> those whose "
              "autonomy is diminished &mdash; children, people with cognitive impairment, those "
              "under duress."},
         ]},

        {"type": "content", "label": "Principle Two", "title": "Beneficence &amp; non-maleficence",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Beneficence", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Actively do good &mdash; design research so "
                   "its benefits (knowledge, better programmes) are real and reach those who bear "
                   "the risk."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Non-maleficence", "blocks": [
                  {"t": "body", "cls": "sm", "html": "&lsquo;First, do no harm.&rsquo; Anticipate and "
                   "prevent injury &mdash; physical, psychological, social, legal, economic."}]}]},
             {"t": "hbox", "color": "amber", "html": "These pull in tension: more ambitious research "
              "can do more good but risks more harm. Ethics is the deliberate weighing of the two."},
         ]},

        {"type": "content", "label": "Principle Three", "title": "Justice &amp; fair distribution",
         "blocks": [
             {"t": "term", "word": "Distributive justice",
              "def": "The burdens of research (risk, time, intrusion) and its benefits (knowledge, "
              "interventions) should be shared fairly &mdash; not loaded onto the poor while the "
              "gains flow to others."},
             {"t": "hbox", "color": "red", "html": "Injustice in research: study the slum, publish "
              "in a foreign journal, change nothing in the slum. Justice asks &mdash; who carries "
              "the cost, and who collects the benefit?"},
         ]},

        {"type": "content", "label": "Justice in South Asia", "title": "Who is studied, and who gains?",
         "blocks": [
             {"t": "body", "html": "Justice is not abstract here. The same marginalised "
              "communities &mdash; Dalit, Adivasi, slum, migrant &mdash; are surveyed again and "
              "again, often with no feedback and no change. Meanwhile the convenient and powerful "
              "are rarely subjects at all."},
             {"t": "bullets", "color": "green", "items": [
                 "Select participants for sound reasons, not just because they are reachable",
                 "Ensure the group studied can plausibly benefit from the findings",
                 "Avoid concentrating research burden on the already over-studied"]},
         ]},

        {"type": "content", "label": "Principles in Conflict", "title": "When principles collide",
         "blocks": [
             {"t": "body", "html": "Real fieldwork pits the principles against each other. "
              "Respecting one person&rsquo;s autonomy may expose another; beneficence may require "
              "limiting choice; protecting confidentiality may clash with a duty to report harm."},
             {"t": "hbox", "color": "cyan", "html": "There is rarely a perfect answer. Ethics is "
              "reasoned, transparent judgement &mdash; documenting <em>why</em> you weighed the "
              "principles the way you did, ideally with an ethics committee&rsquo;s input."},
         ]},

        {"type": "content", "label": "Beyond Belmont", "title": "Newer principles for community research",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Respect for communities:</strong> groups, not just individuals, can be "
                 "harmed or stigmatised",
                 "<strong>Reciprocity:</strong> give something back &mdash; findings, services, "
                 "capacity",
                 "<strong>Transparency:</strong> be honest about funders, purpose and limits",
                 "<strong>Cultural humility:</strong> local norms shape what consent and respect "
                 "mean"]},
             {"t": "hbox", "color": "green", "html": "Development research increasingly adds these "
              "to the classic three &mdash; because its subjects are communities, not just patients "
              "in a clinic."},
         ]},

        {"type": "content", "label": "Anchor", "title": "Five questions the principles ask",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Does each person genuinely choose to take part? (autonomy)",
                 "Have I minimised every avoidable harm? (non-maleficence)",
                 "Is there real benefit, and to whom? (beneficence)",
                 "Are burden and benefit fairly shared? (justice)",
                 "Could I defend my choices openly to the participants? (transparency)"]},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Informed Consent"},

        {"type": "content", "label": "The Cornerstone", "title": "What informed consent really means",
         "blocks": [
             {"t": "term", "word": "Informed consent",
              "def": "A person&rsquo;s voluntary agreement to take part in research, given after "
              "they genuinely understand what it involves, what it is for, and what it may cost "
              "them &mdash; and knowing they can refuse or stop."},
             {"t": "hbox", "color": "amber", "html": "A thumbprint on a form nobody explained is "
              "not consent. A signature obtained under pressure is not consent. Consent is a "
              "process, not a piece of paper."},
         ]},

        {"type": "content", "label": "Three Elements", "title": "Voluntary, informed, comprehended",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Voluntary", "label": "Free choice &mdash; no coercion, no undue "
                  "inducement, no fear of losing a service", "color": "cyan"},
                 {"num": "Informed", "label": "Full, honest disclosure of purpose, risks, "
                  "benefits and rights", "color": "green"},
                 {"num": "Comprehended", "label": "Genuinely understood &mdash; not just heard or "
                  "signed", "color": "indigo"}]},
             {"t": "hbox", "color": "red", "html": "All three must hold. Disclosure without "
              "comprehension, or agreement without freedom, is consent in name only."},
         ]},

        {"type": "content", "label": "What to Disclose", "title": "What participants must be told",
         "blocks": [
             {"t": "bullets", "sm": True, "items": [
                 "Who you are, who funds the research, and why it is being done",
                 "What participation involves &mdash; time, questions, procedures",
                 "Foreseeable risks, discomforts and any benefits",
                 "How data will be stored, used, shared and for how long",
                 "That they may refuse or withdraw at any point, with no penalty",
                 "Whom to contact with questions or complaints"]},
             {"t": "hbox", "color": "cyan", "html": "Disclose in plain, local language &mdash; not "
              "legal English. If your participant could not paraphrase it back, you have not "
              "informed them."},
         ]},

        {"type": "content", "label": "Literacy", "title": "Consent where reading is not assumed",
         "blocks": [
             {"t": "body", "html": "Large numbers of participants in South Asian development "
              "research cannot read a printed consent form. A written form they cannot read is a "
              "ritual, not consent &mdash; and a thumbprint on it can mask total incomprehension."},
             {"t": "bullets", "color": "green", "items": [
                 "Explain verbally in the local language; let them ask questions",
                 "Use audio or witnessed oral consent where appropriate and approved",
                 "Check understanding by asking them to explain it back",
                 "Have an impartial literate witness when forms are thumb-printed"]},
         ]},

        {"type": "content", "label": "Power & Pressure", "title": "When 'yes' isn't really free",
         "blocks": [
             {"t": "body", "html": "Voluntariness is fragile where power is unequal. A villager may "
              "agree because the researcher arrived with officials, because they fear losing a "
              "ration or a programme, or simply because refusing a visitor feels rude or risky."},
             {"t": "hbox", "color": "red", "html": "Separate research from service delivery in the "
              "participant&rsquo;s mind. State clearly &mdash; and mean it &mdash; that refusing "
              "will not affect any benefit, scheme or relationship they have."},
         ]},

        {"type": "content", "label": "Minors", "title": "Children: assent and parental permission",
         "blocks": [
             {"t": "term", "word": "Assent",
              "def": "A child&rsquo;s own affirmative agreement to take part, alongside a parent or "
              "guardian&rsquo;s consent. A child who cannot legally consent can still meaningfully "
              "decline."},
             {"t": "body", "html": "For minors, you generally need <strong>both</strong> a "
              "parent&rsquo;s or guardian&rsquo;s informed consent <em>and</em> the child&rsquo;s "
              "own assent, in language suited to their age. A child&rsquo;s refusal should be "
              "respected even if a parent agrees."},
         ]},

        {"type": "content", "label": "Special Cases", "title": "Consent when capacity is limited",
         "blocks": [
             {"t": "table",
              "head": ["Situation", "Who consents", "Extra safeguard"],
              "rows": [
                  ["Minor (child)", "Guardian + child&rsquo;s assent", "Age-appropriate explanation"],
                  ["Cognitive impairment", "Legally authorised representative", "Assent where possible"],
                  ["Acute distress / crisis", "Defer or seek surrogate", "Re-consent when stable"],
                  ["Group / community study", "Individuals + community gatekeepers", "Avoid coercive leaders"],
                  ["Illiterate participant", "The person (orally)", "Impartial literate witness"]]},
             {"t": "hbox", "color": "cyan", "html": "Diminished capacity never means no consent "
              "&mdash; it means <em>more</em> protection, not less."},
         ]},

        {"type": "content", "label": "Ongoing", "title": "Consent is a process, not a moment",
         "blocks": [
             {"t": "bullets", "items": [
                 "Consent can be <strong>withdrawn</strong> at any time, for any reason",
                 "For long studies, <strong>re-consent</strong> as the research evolves",
                 "New uses of old data may need <strong>fresh</strong> consent",
                 "Silence or non-response is <em>not</em> agreement"]},
             {"t": "hbox", "color": "green", "html": "Treat consent as a living relationship: keep "
              "checking that the person still understands and still agrees as the work goes on."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Vulnerable Populations &amp; Power Asymmetry"},

        {"type": "content", "label": "The Core Idea", "title": "Vulnerability is about power, not weakness",
         "blocks": [
             {"t": "term", "word": "Vulnerable population",
              "def": "A group whose capacity to give free, informed consent or to protect its own "
              "interests is constrained &mdash; by poverty, age, dependence, stigma or lack of "
              "power &mdash; and which therefore needs additional protection."},
             {"t": "hbox", "color": "amber", "html": "Vulnerability is not a flaw in people. It is "
              "a feature of their <em>situation</em> &mdash; and often of the very inequality "
              "development research seeks to study."},
         ]},

        {"type": "content", "label": "Who Is Vulnerable", "title": "Many overlapping forms of vulnerability",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Group", "Source of vulnerability", "Heightened risk"],
              "rows": [
                  ["People in poverty", "Economic dependence", "Undue inducement; can't refuse"],
                  ["Children", "Limited autonomy", "Cannot fully consent; easily led"],
                  ["Women (in some settings)", "Gendered power", "Coerced consent; safety after"],
                  ["Dalit / Adivasi", "Caste &amp; social exclusion", "Stigma; extractive study"],
                  ["Persons with disability", "Access &amp; capacity barriers", "Exclusion or paternalism"],
                  ["Refugees / migrants", "Precarious legal status", "Fear; deportation; reprisal"]]},
             {"t": "hbox", "color": "red", "html": "Vulnerabilities <strong>stack</strong>: a poor, "
              "Dalit, disabled woman faces several at once. Read the whole person, not one label."},
         ]},

        {"type": "content", "label": "Poverty", "title": "Poverty turns inducement into pressure",
         "blocks": [
             {"t": "body", "html": "For someone living on the edge, a payment, a meal, or even the "
              "hope of future help can override free choice. The poorer the participant, the smaller "
              "the sum needed to compromise consent &mdash; and the harder it is to walk away."},
             {"t": "hbox", "color": "amber", "html": "Never let the promise &mdash; explicit or "
              "implied &mdash; of a benefit, scheme or job hang on participation. Decouple research "
              "from relief."},
         ]},

        {"type": "content", "label": "Gender", "title": "Gender, consent and safety",
         "blocks": [
             {"t": "bullets", "items": [
                 "A woman&rsquo;s &lsquo;yes&rsquo; may be a household&rsquo;s decision, not hers",
                 "Interviews on sensitive topics can put her at risk <em>after</em> you leave",
                 "Privacy is often impossible at home &mdash; others listen in",
                 "Women interviewers and safe spaces materially change what can be said"]},
             {"t": "hbox", "color": "red", "html": "On violence, reproduction or autonomy, ask: "
              "could this conversation, if overheard or discovered, endanger her? Design so the "
              "answer is no."},
         ]},

        {"type": "content", "label": "Caste & Exclusion", "title": "Caste, stigma and group harm",
         "blocks": [
             {"t": "body", "html": "Research on caste, manual scavenging, untouchability or "
              "atrocity touches deep stigma. A finding that brands a <em>community</em> &mdash; not "
              "just an individual &mdash; can entrench prejudice and cause collective harm."},
             {"t": "hbox", "color": "cyan", "html": "Protect groups, not only individuals. Ask how "
              "your framing and findings might be used against the community &mdash; and write to "
              "avoid feeding stigma."},
         ]},

        {"type": "content", "label": "Refugees & Migrants", "title": "When status itself is the risk",
         "blocks": [
             {"t": "body", "html": "For refugees, undocumented migrants and the displaced, the very "
              "act of being recorded can be dangerous. Data on identity, location or movement could "
              "expose them to detention, eviction or violence."},
             {"t": "bullets", "color": "red", "items": [
                 "Collect the minimum identifying data &mdash; or none",
                 "Never record status in a way that could be subpoenaed or leaked",
                 "Understand that fear may make refusal feel impossible"]},
         ]},

        {"type": "content", "label": "Over-Researched", "title": "The burden of being studied too much",
         "blocks": [
             {"t": "chart", "canvas": "reBurdenChart",
              "title": "Research burden is concentrated on the most marginalised (illustrative)",
              "source": "Illustrative, not real data",
              "type": "bar",
              "data": {"labels": ["Affluent urban", "General population", "Slum residents",
                                  "Tribal villages", "Refugee camps"],
                       "datasets": [{"label": "Relative frequency of being surveyed",
                                     "data": [8, 22, 60, 78, 95],
                                     "backgroundColor": ["#10B981", "#10B981", "#F59E0B",
                                                         "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100, title:{display:true,text:'Illustrative index'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "&lsquo;Survey fatigue&rsquo; is real and "
              "unequal. The same camps and bastis are visited endlessly, often with nothing in "
              "return. Justice means spreading &mdash; and lightening &mdash; the load."},
         ]},

        {"type": "content", "label": "Safeguards", "title": "Extra protection, not exclusion",
         "blocks": [
             {"t": "body", "html": "The answer to vulnerability is not to exclude these groups "
              "&mdash; that would erase exactly the people development research exists to serve. "
              "The answer is <strong>stronger safeguards</strong>."},
             {"t": "bullets", "color": "green", "items": [
                 "Stronger consent processes and impartial witnesses",
                 "Ethics-committee review attentive to the specific vulnerability",
                 "Match interviewer to participant (gender, language, community) where it helps",
                 "Clear referral pathways if research surfaces distress or danger"]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Privacy, Confidentiality &amp; Anonymity"},

        {"type": "content", "label": "Three Distinct Ideas", "title": "Privacy, confidentiality, anonymity",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Privacy", "label": "The person&rsquo;s right to control access to "
                  "themselves and their information", "color": "cyan"},
                 {"num": "Confidentiality", "label": "Your duty to protect the data they entrusted "
                  "to you", "color": "green"},
                 {"num": "Anonymity", "label": "Data that cannot be traced back to the individual "
                  "at all", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "These are often confused. You may promise "
              "confidentiality (you will guard it) without anonymity (you still know who said it). "
              "Promise only what you can deliver."},
         ]},

        {"type": "content", "label": "Privacy", "title": "Respecting the right to be left out",
         "blocks": [
             {"t": "body", "html": "Privacy is about <strong>boundaries</strong>: people decide "
              "what of themselves to reveal, to whom, and in what setting. Barging into a home, "
              "questioning in front of neighbours, or probing beyond what was agreed all violate it."},
             {"t": "hbox", "color": "cyan", "html": "Interview where the participant can speak "
              "freely and unheard. In crowded homes that may mean a courtyard, a separate room, or "
              "returning at a quieter time."},
         ]},

        {"type": "content", "label": "Confidentiality", "title": "Keeping the promise you made",
         "blocks": [
             {"t": "bullets", "items": [
                 "Share identifiable data only with those who genuinely need it",
                 "Never gossip about a participant&rsquo;s answers, even informally",
                 "Store names separately from responses, linked only by a code",
                 "State the <em>limits</em> of confidentiality up front (see Section Nine)"]},
             {"t": "hbox", "color": "red", "html": "A breach is not only a data leak. Repeating a "
              "woman&rsquo;s words to her husband, or a worker&rsquo;s to a boss, can ruin a life. "
              "Confidentiality is protection, not paperwork."},
         ]},

        {"type": "content", "label": "Anonymisation", "title": "Removing names is not enough",
         "blocks": [
             {"t": "body", "html": "Anonymity is harder than deleting a name. A combination of "
              "<strong>quasi-identifiers</strong> &mdash; village, age, caste, occupation, number "
              "of children &mdash; can pick out one person, especially in a small area where few "
              "share those traits."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Direct IDs", "label": "Name, Aadhaar, phone, photo &mdash; remove", "color": "red"},
                 {"num": "Quasi-IDs", "label": "Age + place + caste can re-identify &mdash; "
                  "aggregate or coarsen", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Re-identification", "title": "How a 'de-identified' file gives someone away",
         "blocks": [
             {"t": "flow", "steps": [
                 "REMOVE names &amp; IDs &mdash; feels anonymous",
                 "KEEP village + age + caste + job",
                 "SMALL AREA: only one person matches that combination",
                 "RE-IDENTIFIED &mdash; anonymity broken without a single name"]},
             {"t": "hbox", "color": "amber", "html": "The risk rises as the area shrinks and the "
              "detail grows. Coarsen (age bands not exact ages, district not village), suppress rare "
              "combinations, and check before you share."},
         ]},

        {"type": "content", "label": "Risk by Area", "title": "Smaller the area, higher the re-identification risk",
         "blocks": [
             {"t": "chart", "canvas": "reIdentRisk",
              "title": "Re-identification risk rises sharply as the geographic unit shrinks (illustrative)",
              "source": "Illustrative, not real data",
              "type": "bar",
              "data": {"labels": ["National", "State", "District", "Block", "Village", "Hamlet"],
                       "datasets": [{"label": "Illustrative re-identification risk",
                                     "data": [4, 9, 20, 42, 70, 92],
                                     "backgroundColor": ["#10B981", "#10B981", "#F59E0B",
                                                         "#F59E0B", "#EF4444", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100, title:{display:true,text:'Illustrative risk index'}} } }"}},
             {"t": "hbox", "color": "red", "html": "The same quasi-identifiers that are harmless "
              "nationally can pin down one family in a village. Match the detail you publish to the "
              "size of the area &mdash; coarsen aggressively for small places."},
         ]},

        {"type": "content", "label": "Data Security", "title": "Guard the data you hold",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Encrypt devices and files holding personal data",
                 "Use strong, unique passwords and access controls",
                 "Keep the name&ndash;code key separate and locked",
                 "Delete or fully anonymise raw identifiers once they&rsquo;re no longer needed",
                 "Beware paper forms, unencrypted phones and shared laptops in the field"]},
             {"t": "hbox", "color": "red", "html": "Most breaches are mundane: a lost phone, an "
              "open spreadsheet, a forwarded email. Security is a daily habit, not a one-off setting."},
         ]},

        {"type": "content", "label": "Sensitive Data", "title": "Some data demands extra care",
         "blocks": [
             {"t": "body", "html": "Information on health (HIV, mental illness), caste, religion, "
              "sexuality, immigration status, criminal involvement or experiences of violence "
              "carries higher stakes &mdash; disclosure can bring stigma, eviction, violence or "
              "prosecution."},
             {"t": "hbox", "color": "amber", "html": "For sensitive categories, raise every "
              "safeguard: minimise collection, tighten storage, restrict access, and ask whether "
              "you truly need the detail at all."},
         ]},

        {"type": "content", "label": "Honesty", "title": "Don't over-promise protection",
         "blocks": [
             {"t": "body", "html": "It is tempting to reassure participants with blanket promises of "
              "secrecy. But you may not control every risk &mdash; a court order, a funder, a small "
              "sample that gives people away. Promising the impossible is its own breach of trust."},
             {"t": "hbox", "color": "cyan", "html": "Tell the truth about what you can and cannot "
              "guarantee. Honest, limited promises protect people better than reassuring, false ones."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Do No Harm &amp; Risk&ndash;Benefit Assessment"},

        {"type": "content", "label": "First, Do No Harm", "title": "Harm in research is not only physical",
         "blocks": [
             {"t": "body", "html": "Development research rarely involves needles or drugs &mdash; "
              "so it is easy to assume it is harmless. It is not. Asking questions, recording "
              "answers and publishing findings can injure people in ways that never show on a body."},
             {"t": "hbox", "color": "amber", "html": "&lsquo;It&rsquo;s only a survey&rsquo; is a "
              "dangerous thought. Map every kind of harm <em>before</em> you enter the field, not "
              "after a participant is hurt."},
         ]},

        {"type": "content", "label": "Types of Harm", "title": "Five kinds of harm to anticipate",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Type", "Example in development research"],
              "rows": [
                  ["Physical", "Fieldwork that exposes a participant to danger or reprisal"],
                  ["Psychological", "Re-traumatising a survivor by probing painful memories"],
                  ["Social", "Stigma, gossip or exclusion if answers become known"],
                  ["Legal", "Recording undocumented status or illegal work that can be used against them"],
                  ["Economic", "Lost wages for time given; a job lost if an employer learns what was said"]]},
             {"t": "hbox", "color": "cyan", "html": "Walk through all five for every study. The "
              "harms that hurt most in development settings are usually social, psychological and "
              "economic &mdash; the invisible ones."},
         ]},

        {"type": "content", "label": "Where Harm Concentrates", "title": "In development research, the unseen harms dominate",
         "blocks": [
             {"t": "chart", "canvas": "reHarmTypes",
              "title": "Relative share of harm types in social-science fieldwork (illustrative)",
              "source": "Illustrative, not real data",
              "type": "doughnut",
              "data": {"labels": ["Social (stigma, gossip)", "Psychological (distress)",
                                  "Economic (lost wages, jobs)", "Legal (status, reprisal)",
                                  "Physical"],
                       "datasets": [{"data": [34, 28, 20, 12, 6],
                                     "backgroundColor": ["#6366F1", "#0EA5E9", "#F59E0B",
                                                         "#EF4444", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
             {"t": "hbox", "color": "amber", "html": "The harms that hurt most in development "
              "settings are usually the invisible ones &mdash; social, psychological, economic "
              "&mdash; not the physical risks a clinical model worries about."},
         ]},

        {"type": "content", "label": "The Matrix", "title": "Weighing likelihood against severity",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:8px 0;">'
                 '<svg viewBox="0 0 520 300" width="560" style="max-width:100%;font-family:inherit;">'
                 '<text x="260" y="22" text-anchor="middle" fill="#cbd5e1" font-size="15" font-weight="600">'
                 'Risk = Likelihood &#215; Severity</text>'
                 # axis labels
                 '<text x="20" y="160" fill="#94a3b8" font-size="12" transform="rotate(-90 20,160)" text-anchor="middle">Severity &#8594;</text>'
                 '<text x="260" y="292" fill="#94a3b8" font-size="12" text-anchor="middle">Likelihood &#8594;</text>'
                 # grid cells 3x3
                 '<rect x="70" y="50"  width="130" height="70" fill="#f59e0b" opacity="0.55"/>'
                 '<rect x="200" y="50" width="130" height="70" fill="#ef4444" opacity="0.6"/>'
                 '<rect x="330" y="50" width="130" height="70" fill="#ef4444" opacity="0.85"/>'
                 '<rect x="70" y="120"  width="130" height="70" fill="#10b981" opacity="0.5"/>'
                 '<rect x="200" y="120" width="130" height="70" fill="#f59e0b" opacity="0.55"/>'
                 '<rect x="330" y="120" width="130" height="70" fill="#ef4444" opacity="0.6"/>'
                 '<rect x="70" y="190"  width="130" height="70" fill="#10b981" opacity="0.75"/>'
                 '<rect x="200" y="190" width="130" height="70" fill="#10b981" opacity="0.5"/>'
                 '<rect x="330" y="190" width="130" height="70" fill="#f59e0b" opacity="0.55"/>'
                 # cell text
                 '<text x="135" y="90"  text-anchor="middle" fill="#0f172a" font-size="12" font-weight="600">Review</text>'
                 '<text x="265" y="90"  text-anchor="middle" fill="#0f172a" font-size="12" font-weight="600">Mitigate</text>'
                 '<text x="395" y="90"  text-anchor="middle" fill="#fff" font-size="12" font-weight="700">Avoid</text>'
                 '<text x="135" y="160" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="600">Proceed</text>'
                 '<text x="265" y="160" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="600">Review</text>'
                 '<text x="395" y="160" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="600">Mitigate</text>'
                 '<text x="135" y="230" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="600">Proceed</text>'
                 '<text x="265" y="230" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="600">Proceed</text>'
                 '<text x="395" y="230" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="600">Review</text>'
                 '</svg></div>')},
             {"t": "hbox", "color": "red", "html": "High-severity, high-likelihood research should "
              "not proceed as designed &mdash; redesign it. Low-low can proceed. The middle demands "
              "mitigation and ethics review."},
         ]},

        {"type": "content", "label": "Minimal Risk", "title": "The minimal-risk benchmark",
         "blocks": [
             {"t": "term", "word": "Minimal risk",
              "def": "Risk no greater than that ordinarily encountered in daily life or in routine "
              "interviews and examinations. Most social-science fieldwork aims to sit at or below "
              "this threshold."},
             {"t": "hbox", "color": "amber", "html": "But &lsquo;daily life&rsquo; differs by "
              "person. For an undocumented migrant or an abuse survivor, an ordinary-seeming "
              "question can carry far-from-minimal risk. Judge risk through the participant&rsquo;s "
              "eyes."},
         ]},

        {"type": "content", "label": "Risk vs Benefit", "title": "The risk&ndash;benefit balance",
         "blocks": [
             {"t": "flow", "steps": [
                 "IDENTIFY every plausible harm and benefit",
                 "ESTIMATE likelihood and severity of each",
                 "MINIMISE harms through design changes",
                 "JUDGE: do the benefits justify the residual risk?",
                 "If not &mdash; redesign or do not proceed"]},
             {"t": "hbox", "color": "cyan", "html": "Crucially, ask <em>who</em> bears the risk and "
              "<em>who</em> gains the benefit. Risk to the poor for benefit to others fails the "
              "justice test even if the totals look favourable."},
         ]},

        {"type": "content", "label": "Secondary Trauma", "title": "Harm to those who ask, too",
         "blocks": [
             {"t": "body", "html": "Researchers and field staff who hear accounts of violence, "
              "abuse and death can suffer <strong>vicarious or secondary trauma</strong>. Ignoring "
              "their wellbeing is both an ethical failure and a threat to data quality."},
             {"t": "bullets", "color": "green", "items": [
                 "Brief and debrief field teams on emotionally heavy topics",
                 "Build in breaks, rotation and access to support",
                 "Treat enumerators&rsquo; distress as real, not weakness"]},
         ]},

        {"type": "content", "label": "Mitigation", "title": "Designing harm out of the study",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Drop questions whose risk outweighs their value",
                 "Offer referral to services when sensitive issues surface",
                 "Let participants skip questions or pause at any time",
                 "Interview in private, safe settings; protect data tightly",
                 "Plan for the unexpected &mdash; disclosure of harm, acute distress"]},
             {"t": "hbox", "color": "green", "html": "Good design is the cheapest, most powerful "
              "ethical safeguard. Most harms are prevented at the protocol stage, not patched in "
              "the field."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Ethics Review in India"},

        {"type": "content", "label": "Independent Eyes", "title": "Why someone else must review your study",
         "blocks": [
             {"t": "body", "html": "Researchers are poorly placed to judge their own ethics &mdash; "
              "they are invested in their study going ahead. Independent <strong>ethics review</strong> "
              "exists so that a body with no stake in the result checks that participants are "
              "protected before any data is collected."},
             {"t": "hbox", "color": "cyan", "html": "Review is not a hurdle to clear and forget. It "
              "is a second pair of eyes that often catches risks the proposer cannot see."},
         ]},

        {"type": "content", "label": "A Maturing System", "title": "Ethics review has expanded across India",
         "blocks": [
             {"t": "chart", "canvas": "reReviewTrend",
              "title": "Growth in formal ethics review of research over time (illustrative trend)",
              "source": "Illustrative, indicative of direction not exact figures",
              "type": "line",
              "data": {"labels": ["2000", "2005", "2010", "2015", "2017", "2020", "2023"],
                       "datasets": [{"label": "Relative volume of protocols under ethics review",
                                     "data": [10, 22, 40, 62, 72, 84, 95],
                                     "borderColor": "#0EA5E9",
                                     "backgroundColor": "rgba(14,165,233,0.08)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100, title:{display:true,text:'Illustrative index'}} } }"}},
             {"t": "hbox", "color": "green", "html": "The direction is real even if these figures "
              "are illustrative: ICMR&rsquo;s 2017 guidelines and clinical-trial reforms have made "
              "independent ethics review the expected norm, not the exception."},
         ]},

        {"type": "content", "label": "The Committee", "title": "Institutional Ethics Committees (IEC / IRB)",
         "blocks": [
             {"t": "term", "word": "Institutional Ethics Committee (IEC)",
              "def": "A formally constituted, independent committee &mdash; the Indian counterpart "
              "of the IRB &mdash; that reviews research involving human participants to ensure their "
              "rights, safety and wellbeing are protected."},
             {"t": "body", "html": "A well-constituted committee includes scientists, a clinician, a "
              "legal expert, an ethicist and crucially a <strong>lay member</strong> who represents "
              "the community&rsquo;s perspective."},
         ]},

        {"type": "content", "label": "ICMR 2017", "title": "ICMR's National Ethical Guidelines, 2017",
         "blocks": [
             {"t": "body", "html": "The Indian Council of Medical Research&rsquo;s <strong>National "
              "Ethical Guidelines for Biomedical and Health Research Involving Human Participants "
              "(2017)</strong> are India&rsquo;s principal ethics framework &mdash; an update of "
              "ICMR&rsquo;s earlier guidance and the reference point for ethics committees."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Sets out core principles: autonomy, beneficence, justice and more",
                 "Defines how ethics committees are constituted and function",
                 "Details consent requirements and protection of vulnerable groups",
                 "Covers community-based, social and behavioural research, not only clinical"]},
         ]},

        {"type": "content", "label": "Principles in ICMR", "title": "What the ICMR guidelines emphasise",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Essentiality &amp; voluntariness:</strong> the research must be needed and "
                 "freely joined",
                 "<strong>Non-exploitation:</strong> fair compensation; no undue inducement",
                 "<strong>Privacy &amp; confidentiality:</strong> protect identity and data",
                 "<strong>Accountability &amp; transparency:</strong> answerable conduct throughout"]},
             {"t": "hbox", "color": "green", "html": "Even if your study is not biomedical, the "
              "ICMR principles are the practical benchmark Indian reviewers and funders will expect "
              "you to meet."},
         ]},

        {"type": "content", "label": "Clinical Oversight", "title": "DCGI and clinical trials",
         "blocks": [
             {"t": "body", "html": "Clinical trials of drugs and devices carry an extra layer of "
              "regulation. In India the <strong>Drugs Controller General of India (DCGI)</strong>, "
              "under the CDSCO, regulates clinical trials, and committees overseeing them must be "
              "registered with the national authority."},
             {"t": "hbox", "color": "amber", "html": "Most development research is <em>not</em> a "
              "clinical trial &mdash; but if your work touches drugs, devices or medical "
              "interventions, this regulatory regime applies and is non-negotiable."},
         ]},

        {"type": "content", "label": "What Reviewers Want", "title": "What an ethics committee checks",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Area", "The committee asks"],
              "rows": [
                  ["Value &amp; design", "Is the research worth doing and methodologically sound?"],
                  ["Consent", "Is the process genuinely free, informed and understood?"],
                  ["Risk&ndash;benefit", "Are harms minimised and justified by benefit?"],
                  ["Vulnerable groups", "Are extra safeguards in place and appropriate?"],
                  ["Privacy &amp; data", "How will identity and data be protected?"],
                  ["Justice", "Is participant selection and benefit-sharing fair?"]]},
         ]},

        {"type": "content", "label": "Getting Approval", "title": "Working with the committee well",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Submit <em>before</em> any data collection &mdash; never retrospectively",
                 "Include consent forms in the local language for review",
                 "Report changes, adverse events and completion as required",
                 "Treat reviewers&rsquo; questions as help, not obstruction"]},
             {"t": "hbox", "color": "red", "html": "Skipping review to &lsquo;save time&rsquo; can "
              "void publication, breach funder rules and &mdash; far worse &mdash; leave "
              "participants unprotected. Build review time into the plan from the start."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Field Realities &amp; Dilemmas"},

        {"type": "content", "label": "Where Ethics Lives", "title": "The form is signed. Now the hard part.",
         "blocks": [
             {"t": "body", "html": "Textbook ethics meets messy reality the moment you reach the "
              "village. Gatekeepers, crowds, raw emotion and impossible trade-offs do not appear in "
              "the protocol. This section rehearses the dilemmas you will actually face."},
             {"t": "quote", "text": "Ethics is not what you do when someone is watching. It is what "
              "you do in the doorway of a stranger&rsquo;s home, alone, deciding.",
              "attr": "&mdash; a field researcher&rsquo;s maxim"},
         ]},

        {"type": "content", "label": "Gatekeepers", "title": "The people who grant &mdash; or block &mdash; access",
         "blocks": [
             {"t": "term", "word": "Gatekeeper",
              "def": "A person who controls access to a community or group &mdash; a sarpanch, "
              "landlord, employer, NGO worker, husband or elder &mdash; whose permission you may "
              "need to reach participants."},
             {"t": "hbox", "color": "red", "html": "A gatekeeper&rsquo;s permission is not the "
              "participant&rsquo;s consent. And a powerful gatekeeper present in the room can make "
              "free, honest answers impossible. Their access can become their control."},
         ]},

        {"type": "content", "label": "Incentives", "title": "The fine line between thanks and coercion",
         "blocks": [
             {"t": "body", "html": "We met this under consent; in the field it sharpens. A crowd "
              "gathers when a payment is known; people answer to qualify; gatekeepers expect a cut. "
              "What was meant as respect becomes a market &mdash; and a source of pressure."},
             {"t": "hbox", "color": "amber", "html": "Be consistent, modest and transparent about "
              "any compensation. Never let it become the reason people take part, or a prize "
              "gatekeepers ration."},
         ]},

        {"type": "content", "label": "Duty to Disclose", "title": "When you learn of serious harm",
         "blocks": [
             {"t": "body", "html": "A participant discloses ongoing child abuse, a serious threat, "
              "or imminent danger. Confidentiality, normally sacred, now collides with a duty to "
              "prevent harm &mdash; and sometimes a legal mandatory-reporting obligation."},
             {"t": "bullets", "color": "red", "items": [
                 "State the <strong>limits</strong> of confidentiality <em>before</em> the interview",
                 "Know your legal reporting duties (e.g. child protection) in advance",
                 "Have referral pathways and a clear plan ready, not improvised"]},
         ]},

        {"type": "content", "label": "Photography", "title": "Photographs, video and recognisable faces",
         "blocks": [
             {"t": "body", "html": "A photograph is identifiable data and can travel far beyond your "
              "intent &mdash; into reports, websites, donor decks and social media. A recognisable "
              "face attached to a story of poverty, illness or violence can stigmatise for years."},
             {"t": "bullets", "color": "amber", "items": [
                 "Get <strong>specific</strong> consent for images, separate from interview consent",
                 "Explain exactly where the image may appear &mdash; and that it may be permanent",
                 "Avoid &lsquo;poverty-porn&rsquo; framing that strips dignity",
                 "For children and sensitive topics, default to no identifiable images"]},
         ]},

        {"type": "content", "label": "Dignity in Images", "title": "Representation is an ethical act",
         "blocks": [
             {"t": "hbox", "color": "red", "html": "Ask of every image you publish: would I be "
              "comfortable if this were a photo of my own family, captioned this way, seen by my "
              "neighbours and my employer? If not, do not use it."},
             {"t": "body", "html": "How you portray people in outputs &mdash; the framing, the "
              "caption, the crop &mdash; carries the same ethical weight as how you collected the "
              "data. Respect does not end at the camera."},
         ]},

        {"type": "content", "label": "Emotional Toll", "title": "When the field hurts the researcher",
         "blocks": [
             {"t": "body", "html": "Sitting with grief, violence and destitution day after day "
              "leaves a mark. Enumerators and researchers carry <strong>secondary trauma</strong>, "
              "and exhausted, distressed field teams also collect worse data and make worse ethical "
              "calls."},
             {"t": "hbox", "color": "green", "html": "Caring for the field team is an ethics issue, "
              "not a perk: debriefs, peer support, realistic workloads and permission to step back "
              "protect both people and data."},
         ]},

        {"type": "content", "label": "Reasoning It Out", "title": "A method for the dilemma in front of you",
         "blocks": [
             {"t": "flow", "steps": [
                 "NAME the conflict &mdash; which principles clash?",
                 "WHO is affected, and how badly?",
                 "OPTIONS &mdash; what are the realistic choices?",
                 "DECIDE for the most vulnerable person&rsquo;s protection",
                 "DOCUMENT the reasoning; consult your committee or peers"]},
             {"t": "hbox", "color": "cyan", "html": "You will not always get it right. But reasoned, "
              "documented, participant-centred judgement is the ethical standard &mdash; not "
              "pretending dilemmas do not exist."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Data Ethics, Ownership &amp; Dissemination"},

        {"type": "content", "label": "After the Field", "title": "Ethics doesn't stop at data collection",
         "blocks": [
             {"t": "body", "html": "The interview ends; the ethical duty does not. How you store, "
              "analyse, own, share and report the data &mdash; and whether anything flows back to "
              "the community &mdash; are ethical questions every bit as serious as consent."},
             {"t": "hbox", "color": "amber", "html": "Much extractive research is impeccable in the "
              "field and then takes everything and gives nothing back. The ethics of dissemination "
              "is where good intentions most often fail."},
         ]},

        {"type": "content", "label": "Who Owns It", "title": "Whose data is it, anyway?",
         "blocks": [
             {"t": "body", "html": "Communities are routinely <em>extracted</em> from &mdash; "
              "surveyed repeatedly while the knowledge, the publications and the value flow to "
              "outside institutions. The people who generated the data rarely own, control or "
              "benefit from it."},
             {"t": "bullets", "color": "green", "items": [
                 "Ask who owns the data &mdash; and who profits from it",
                 "Involve participants in deciding what gets measured and asked",
                 "Treat data as a shared resource, not a one-way harvest"]},
         ]},

        {"type": "content", "label": "Giving Back", "title": "Return the findings to the community",
         "blocks": [
             {"t": "body", "html": "<strong>Reciprocity</strong> means the people studied learn what "
              "was found, in a form they can use &mdash; not a 60-page English PDF, but a meeting, a "
              "poster, a radio spot, a conversation in their language."},
             {"t": "hbox", "color": "cyan", "html": "Plan and budget for dissemination back to "
              "participants from the start. &lsquo;We&rsquo;ll share results later&rsquo; almost "
              "always means never."},
         ]},

        {"type": "content", "label": "Accountability", "title": "Answerable to the community, not only the donor",
         "blocks": [
             {"t": "bullets", "items": [
                 "Be honest about who funds the work and why",
                 "Let participants challenge or correct your interpretation",
                 "Report uncomfortable findings, not only the flattering ones",
                 "Acknowledge the limits of what your study can claim"]},
             {"t": "hbox", "color": "green", "html": "True accountability runs <em>downward</em> to "
              "the researched, as well as upward to funders. Ask: to whom am I really answerable?"},
         ]},

        {"type": "content", "label": "The Law", "title": "India's Digital Personal Data Protection Act, 2023",
         "blocks": [
             {"t": "body", "html": "The <strong>DPDP Act, 2023</strong> is India&rsquo;s first "
              "comprehensive data-protection law. It sets duties for anyone handling personal "
              "digital data &mdash; researchers and NGOs included."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Collect only what you need, for a clearly stated purpose",
                 "Obtain free, informed, specific consent for personal data",
                 "Protect data with reasonable security safeguards",
                 "Stronger protections for children&rsquo;s data"]},
             {"t": "hbox", "color": "amber", "html": "Know your obligations before you collect. "
              "&lsquo;We&rsquo;re a small NGO&rsquo; is not an exemption."},
         ]},

        {"type": "content", "label": "FAIR & CARE", "title": "Two principles for ethical data sharing",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "FAIR", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>F</strong>indable, "
                   "<strong>A</strong>ccessible, <strong>I</strong>nteroperable, "
                   "<strong>R</strong>eusable &mdash; making data useful and shareable for science."}]}],
              "right": [{"t": "panel", "color": "green", "title": "CARE", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>C</strong>ollective benefit, "
                   "<strong>A</strong>uthority to control, <strong>R</strong>esponsibility, "
                   "<strong>E</strong>thics &mdash; centring the people in the data, especially "
                   "Indigenous communities."}]}]},
             {"t": "hbox", "color": "amber", "html": "FAIR optimises data for <em>use</em>; CARE "
              "asks who benefits and who decides. Open data is not automatically ethical data "
              "&mdash; hold both together."},
         ]},

        {"type": "content", "label": "Open Data Tension", "title": "When sharing data can harm",
         "blocks": [
             {"t": "body", "html": "Open data advances science &mdash; but releasing micro-data on "
              "marginalised people can enable re-identification, surveillance or stigma. The push "
              "to share must be balanced against the duty to protect."},
             {"t": "hbox", "color": "red", "html": "Before releasing a dataset, ask: could this be "
              "used to identify, target or harm the people in it? Aggregate, restrict access, or "
              "withhold where the risk is real."},
         ]},

        {"type": "content", "label": "Honest Reporting", "title": "Ethics in how you write it up",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Do not over-claim &mdash; report uncertainty and limitations honestly",
                 "Do not cherry-pick the findings that flatter the programme or funder",
                 "Do not write people in ways that strip dignity or entrench stigma",
                 "Do credit communities and field staff for the knowledge they made possible"]},
             {"t": "hbox", "color": "green", "html": "How you write is an ethical act. The last "
              "harm a study can do is to misrepresent the very people who trusted it with their "
              "lives."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Putting It to Work"},

        {"type": "content", "label": "Before You Start", "title": "Ethics checklist: planning",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "Is the research necessary, and could existing data answer the question?",
                 "Who bears the risk, and who gains the benefit?",
                 "Has an ethics committee reviewed the protocol and consent materials?",
                 "Are consent forms in the local language and tested for comprehension?",
                 "Are extra safeguards in place for vulnerable participants?"]},
         ]},

        {"type": "content", "label": "In the Field", "title": "Ethics checklist: fieldwork",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Is consent genuinely voluntary, informed and understood &mdash; every time?",
                 "Can people refuse or stop without losing any benefit?",
                 "Are interviews private, safe and free of coercive gatekeepers?",
                 "Are the limits of confidentiality stated up front?",
                 "Do you have referral pathways for distress or disclosed harm?",
                 "Is the field team supported and protected too?"]},
         ]},

        {"type": "content", "label": "After the Field", "title": "Ethics checklist: data &amp; dissemination",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Is personal data stored securely, with identifiers protected?",
                 "Have you guarded against re-identification before sharing?",
                 "Are you meeting DPDP Act obligations for personal data?",
                 "Will findings be returned to the community in a usable form?",
                 "Is the write-up honest, dignified and free of stigma?"]},
         ]},

        {"type": "content", "label": "Red Flags", "title": "Warning signs to stop and rethink",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "&lsquo;They&rsquo;re poor, they won&rsquo;t mind a few questions&rsquo;",
                 "&lsquo;We don&rsquo;t have time for ethics review&rsquo;",
                 "&lsquo;The incentive is large &mdash; everyone will agree&rsquo;",
                 "&lsquo;Just remove the names, it&rsquo;s anonymous&rsquo;",
                 "&lsquo;We&rsquo;ll share results back with them eventually&rsquo;"]},
             {"t": "hbox", "color": "amber", "html": "Each of these sentences has preceded real "
              "harm. When you hear yourself or a colleague say one, stop and apply the principles."},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "Where to turn for guidance",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>ICMR National Ethical Guidelines (2017)</strong> &mdash; India&rsquo;s "
                 "primary reference",
                 "<strong>Declaration of Helsinki</strong> &amp; the <strong>Belmont Report</strong> "
                 "&mdash; the foundations",
                 "<strong>CIOMS</strong> guidelines &mdash; ethics in low-resource &amp; "
                 "international research",
                 "<strong>DPDP Act, 2023</strong> &mdash; India&rsquo;s data-protection obligations",
                 "Your own <strong>Institutional Ethics Committee</strong> &mdash; consult it early "
                 "and often"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo&rsquo;s "
              "<strong>Data Literacy</strong>, <strong>Qualitative Methods</strong> and "
              "<strong>Research Methods</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Every row is a person</strong> &mdash; treat them as you would your own family",
                 "<strong>Consent is a process</strong> &mdash; voluntary, informed, understood, revocable",
                 "<strong>Vulnerability means more protection</strong>, never exclusion",
                 "<strong>Anonymising is harder than deleting names</strong> &mdash; guard against re-identification",
                 "<strong>Give the findings back</strong> &mdash; research should serve the researched"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Research Ethics 101 &middot; Complete",
         "headline": "Now go research<br>with conscience.",
         "byline": "Ethics is not a form you sign &mdash; it is how you treat every person whose "
                   "life becomes your data. Carry consent, dignity and do-no-harm into every study. "
                   "Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Data Literacy 101", "href": "https://www.impactmojo.in/101-courses/data-lit.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
