# -*- coding: utf-8 -*-
"""
Digital Ethics 101 — ImpactMojo 101 Series (native deck spec)
Ethics of digital technology for South Asian development practitioners.
Build: python3 scripts/deck-builder/build.py digital_ethics
"""

DECK = {
    "slug": "digital-ethics",
    "title": "Digital Ethics 101",
    "description": ("Digital Ethics 101 — a free foundational course for development "
                    "practitioners in South Asia on deploying digital technology responsibly: "
                    "data privacy and the DPDP Act, algorithmic bias, AI, digital identity, "
                    "surveillance, the digital divide, platform power, online harms and "
                    "responsible design. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Digital<br>Ethics<br>101",
         "sub": "Deploying Technology Responsibly &mdash; a Foundational Course on Data, AI "
                "&amp; Digital Rights for Development Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "Why Digital Ethics Matters"},
             {"name": "Data Privacy &amp; Protection"},
             {"name": "Algorithmic Bias &amp; Fairness"},
             {"name": "AI in Development"},
             {"name": "Digital Identity &amp; Inclusion"},
             {"name": "Surveillance, Power &amp; Consent"},
             {"name": "The Digital Divide"},
             {"name": "Platform Power &amp; Data Colonialism"},
             {"name": "Misinformation &amp; Online Harms"},
             {"name": "Responsible Design &amp; Principles"},
             {"name": "Governance, Regulation &amp; Practice"},
         ]},

        # ===================== SECTION 01 — 8 content =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why Digital Ethics Matters"},

        {"type": "content", "label": "The Promise", "title": "Technology entered development with a promise",
         "blocks": [
             {"t": "body", "html": "Mobile money, biometric IDs, telemedicine, e-governance and AI "
              "have reached deep into the lives of the poor in South Asia &mdash; faster than almost "
              "anywhere on earth. The promise was real: leapfrog broken systems, cut leakage, "
              "deliver at scale."},
             {"t": "hbox", "color": "cyan", "html": "But the same systems that include millions can "
              "exclude millions &mdash; and at this scale, a design flaw is not a bug, it is a "
              "policy that touches a billion people."},
         ]},

        {"type": "content", "label": "Definition", "title": "What we mean by digital ethics",
         "blocks": [
             {"t": "term", "word": "Digital ethics",
              "def": "The study of how digital technologies &mdash; data, algorithms, platforms, AI "
              "&mdash; should be designed, deployed and governed so they respect rights, dignity and "
              "fairness, especially for the people with least power to refuse them."},
             {"t": "body", "html": "It is not a compliance checkbox bolted on at the end. It is a "
              "set of questions asked from the first design meeting: who benefits, who is harmed, "
              "who can opt out, and who decides?"},
         ]},

        {"type": "content", "label": "The Clash", "title": "'Move fast and break things' meets vulnerable people",
         "blocks": [
             {"t": "quote",
              "text": "Move fast and break things.",
              "attr": "&mdash; an early Silicon Valley motto"},
             {"t": "hbox", "color": "red", "html": "When the 'things' you break are someone's "
              "ration entitlement, pension, or right to be seen by the state, the cost of a failed "
              "experiment is not lost revenue &mdash; it is a missed meal."},
         ]},

        {"type": "content", "label": "Tech4Dev", "title": "The double edge of every deployment",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Promise", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Reach the last mile cheaply",
                      "Cut leakage and ghost beneficiaries",
                      "Real-time monitoring of services",
                      "Give people a digital voice"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "Peril", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Exclude those who cannot authenticate",
                      "Surveil the poor as a condition of aid",
                      "Automate and hide existing bias",
                      "Extract data, return little value"]}]}]},
             {"t": "hbox", "color": "amber", "html": "Neither column is the whole truth. Ethics is "
              "the discipline of holding both at once."},
         ]},

        {"type": "content", "label": "Scale", "title": "Why scale changes the ethics",
         "blocks": [
             {"t": "body", "html": "A flawed clinic harms a village. A flawed national platform "
              "harms a nation. Digital systems concentrate decisions &mdash; one ruleset, one "
              "database, one model &mdash; so errors no longer cancel out; they replicate."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "1 ruleset", "label": "decides eligibility for hundreds of millions", "color": "indigo"},
                 {"num": "1 outage", "label": "can freeze entitlements across whole states", "color": "red"}]},
         ]},

        {"type": "content", "label": "Who Is Affected", "title": "Practitioners sit on both sides",
         "blocks": [
             {"t": "body", "html": "You may <strong>deploy</strong> digital tools &mdash; a survey "
              "app, a beneficiary database, a chatbot. You are also <strong>affected</strong> by "
              "them &mdash; the platforms you depend on, the IDs your participants must carry."},
             {"t": "hbox", "color": "cyan", "html": "This course is for both roles: to build more "
              "carefully, and to push back on systems that harm the communities you serve."},
         ]},

        {"type": "content", "label": "The Core Questions", "title": "Five questions to ask of any digital system",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Who benefits</strong> &mdash; and who bears the risk?",
                 "<strong>Who is excluded</strong> by the design, and how loudly do they fail?",
                 "<strong>What data</strong> is collected, and could it be used against people?",
                 "<strong>Who decides</strong> &mdash; and can an affected person contest a decision?",
                 "<strong>What if it breaks</strong> &mdash; is there a human fallback?"]},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The harms", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Privacy, bias and AI",
                      "Identity and surveillance",
                      "The divide and platform power",
                      "Misinformation and online harm"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "The response", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Responsible design principles",
                      "Privacy and ethics by design",
                      "Governance and regulation",
                      "A practical org checklist"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Throughout, the examples are South Asian "
              "&mdash; Aadhaar, the DPDP Act, WhatsApp, the systems you actually meet at work."},
         ]},

        # ===================== SECTION 02 — 8 content =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Data Privacy &amp; Protection"},

        {"type": "content", "label": "Foundations", "title": "What counts as personal data",
         "blocks": [
             {"t": "term", "word": "Personal data",
              "def": "Any information that relates to an identified or identifiable individual "
              "&mdash; name, Aadhaar number, phone, location, biometric, health record, even a "
              "combination of seemingly harmless fields."},
             {"t": "hbox", "color": "amber", "html": "'It's just a phone number' is how most leaks "
              "begin. Personal data is anything that can be traced back to a person, alone or in "
              "combination."},
         ]},

        {"type": "content", "label": "Why Privacy", "title": "Privacy is not secrecy &mdash; it is control",
         "blocks": [
             {"t": "body", "html": "Privacy is not having something to hide. It is the power to "
              "decide who knows what about you, and to live without being watched, profiled or "
              "sorted by default."},
             {"t": "quote",
              "text": "Arguing that you don't care about privacy because you have nothing to hide "
              "is like saying you don't care about free speech because you have nothing to say.",
              "attr": "&mdash; Edward Snowden"},
         ]},

        {"type": "content", "label": "Landmark", "title": "Puttaswamy (2017): privacy is a fundamental right",
         "blocks": [
             {"t": "body", "html": "In <em>K.S. Puttaswamy v. Union of India</em> (2017), a "
              "nine-judge bench of the Supreme Court of India held unanimously that the "
              "<strong>right to privacy is a fundamental right</strong> under Article 21 of the "
              "Constitution."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "9 judges", "label": "unanimous Constitution Bench", "color": "indigo",
                  "source": "Puttaswamy, 2017"},
                 {"num": "Art. 21", "label": "privacy read into the right to life &amp; liberty", "color": "cyan"},
                 {"num": "Proportionality", "label": "any intrusion must be lawful, necessary &amp; proportionate", "color": "green"}]},
         ]},

        {"type": "content", "label": "The Test", "title": "When can the state intrude on privacy?",
         "blocks": [
             {"t": "body", "html": "Puttaswamy set a <strong>proportionality test</strong>: a "
              "restriction on privacy is valid only if it clears every step. This is the lens for "
              "judging any data-collecting programme."},
             {"t": "flow", "steps": [
                 "LEGALITY: backed by a valid law",
                 "LEGITIMATE AIM: a genuine state goal",
                 "NECESSITY: no less-intrusive way works",
                 "PROPORTIONALITY: benefit outweighs the harm"]},
         ]},

        {"type": "content", "label": "Principle", "title": "Consent: the floor, not the ceiling",
         "blocks": [
             {"t": "bullets", "items": [
                 "Consent must be <strong>free</strong> &mdash; not the price of a basic service",
                 "<strong>Informed</strong> &mdash; people know what, why, for how long",
                 "<strong>Specific</strong> &mdash; for a stated purpose, not 'anything forever'",
                 "<strong>Revocable</strong> &mdash; people can withdraw without penalty"]},
             {"t": "hbox", "color": "red", "html": "A thumbprint on a form nobody explained, given "
              "to receive a pension, is not free or informed consent."},
         ]},

        {"type": "content", "label": "Principle", "title": "Purpose limitation &amp; data minimisation",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Purpose limitation", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Data collected for one purpose should not be "
                   "quietly reused for another. Immunisation records are not a recruitment list."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Data minimisation", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Collect the least you need. Every extra field "
                   "is a future liability &mdash; a breach risk and a tool that can be turned on people."}]}]},
             {"t": "hbox", "color": "amber", "html": "The safest data is the data you never "
              "collected. Ask of every field: do we truly need this?"},
         ]},

        {"type": "content", "label": "The Law", "title": "India's Digital Personal Data Protection Act, 2023",
         "blocks": [
             {"t": "body", "html": "The <strong>DPDP Act, 2023</strong> is India's first "
              "comprehensive data-protection law. It applies to anyone processing digital personal "
              "data &mdash; including NGOs, researchers and small organisations."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Process data only for a lawful purpose, with consent or a legitimate use",
                 "Honour rights to access, correction and erasure",
                 "Notify breaches and the Data Protection Board",
                 "Stronger safeguards for children's data and processing"]},
             {"t": "hbox", "color": "amber", "html": "'We're a small NGO' is not an exemption. Know "
              "your obligations before you collect a single record."},
         ]},

        {"type": "content", "label": "Re-identification", "title": "Anonymisation is harder than deleting names",
         "blocks": [
             {"t": "body", "html": "Removing names does not make data safe. A combination of "
              "<strong>village + age + caste + occupation</strong> can re-identify one person, "
              "especially in small areas where few share those traits."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Direct IDs", "label": "Name, Aadhaar, phone &mdash; remove entirely", "color": "red"},
                 {"num": "Quasi-IDs", "label": "Age + place + caste can re-identify &mdash; coarsen or aggregate", "color": "amber"}]},
         ]},

        # ===================== SECTION 03 — 8 content =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Algorithmic Bias &amp; Fairness"},

        {"type": "content", "label": "The Myth", "title": "Algorithms are not automatically neutral",
         "blocks": [
             {"t": "body", "html": "It is tempting to think a formula cannot discriminate &mdash; "
              "the maths just crunches numbers. But an algorithm learns from data produced by an "
              "unequal world, and it can faithfully reproduce that inequality at scale."},
             {"t": "hbox", "color": "red", "html": "Bias does not come from 'the maths being "
              "racist'. It comes from biased data, biased proxies and biased objectives &mdash; "
              "all human choices."},
         ]},

        {"type": "content", "label": "Definition", "title": "What algorithmic bias means",
         "blocks": [
             {"t": "term", "word": "Algorithmic bias",
              "def": "A systematic, unfair difference in how an automated system treats different "
              "groups &mdash; producing outcomes that disadvantage people by gender, caste, "
              "religion, region, language or disability."},
             {"t": "body", "html": "It is rarely intentional. It is usually inherited &mdash; from "
              "the data the model was trained on, and the world that data came from."},
         ]},

        {"type": "content", "label": "Source One", "title": "Bias enters through the training data",
         "blocks": [
             {"t": "body", "html": "A model learns patterns from past examples. If history "
              "under-served women, recorded fewer female-headed loans, or skipped remote villages, "
              "the model learns that those people are 'lower priority' &mdash; and repeats it."},
             {"t": "hbox", "color": "amber", "html": "The model is a mirror. If the data reflects a "
              "world that excluded people, the model will too &mdash; only faster and with an air "
              "of objectivity."},
         ]},

        {"type": "content", "label": "Source Two", "title": "Proxies smuggle in protected traits",
         "blocks": [
             {"t": "body", "html": "Even if you remove caste, religion or gender from the data, "
              "other fields can stand in for them. <strong>Pincode</strong> can proxy for caste or "
              "religion; <strong>name</strong> can reveal community; <strong>occupation</strong> "
              "can track historical disadvantage."},
             {"t": "hbox", "color": "red", "html": "Dropping the sensitive column does not remove "
              "the bias if a proxy remains. The model finds the back door."},
         ]},

        {"type": "content", "label": "Source Three", "title": "Feedback loops make bias self-fulfilling",
         "blocks": [
             {"t": "raw", "html":
              '<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" '
              'style="width:100%;max-height:320px;font-family:inherit">'
              '<defs><marker id="ahde" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">'
              '<path d="M0,0 L8,3 L0,6 Z" fill="#F59E0B"/></marker></defs>'
              '<rect x="40" y="30" width="200" height="70" rx="10" fill="none" stroke="#0EA5E9" stroke-width="2.5"/>'
              '<text x="140" y="60" fill="#0EA5E9" font-size="15" text-anchor="middle" font-weight="700">Biased data</text>'
              '<text x="140" y="82" fill="#cbd5e1" font-size="12" text-anchor="middle">past exclusion recorded</text>'
              '<rect x="520" y="30" width="200" height="70" rx="10" fill="none" stroke="#6366F1" stroke-width="2.5"/>'
              '<text x="620" y="60" fill="#6366F1" font-size="15" text-anchor="middle" font-weight="700">Model scores</text>'
              '<text x="620" y="82" fill="#cbd5e1" font-size="12" text-anchor="middle">group rated low priority</text>'
              '<rect x="520" y="200" width="200" height="70" rx="10" fill="none" stroke="#EF4444" stroke-width="2.5"/>'
              '<text x="620" y="230" fill="#EF4444" font-size="15" text-anchor="middle" font-weight="700">Less service</text>'
              '<text x="620" y="252" fill="#cbd5e1" font-size="12" text-anchor="middle">fewer loans / visits</text>'
              '<rect x="40" y="200" width="200" height="70" rx="10" fill="none" stroke="#10B981" stroke-width="2.5"/>'
              '<text x="140" y="230" fill="#10B981" font-size="15" text-anchor="middle" font-weight="700">New data</text>'
              '<text x="140" y="252" fill="#cbd5e1" font-size="12" text-anchor="middle">confirms the bias</text>'
              '<line x1="240" y1="65" x2="515" y2="65" stroke="#F59E0B" stroke-width="2.5" marker-end="url(#ahde)"/>'
              '<line x1="620" y1="100" x2="620" y2="195" stroke="#F59E0B" stroke-width="2.5" marker-end="url(#ahde)"/>'
              '<line x1="515" y1="235" x2="245" y2="235" stroke="#F59E0B" stroke-width="2.5" marker-end="url(#ahde)"/>'
              '<line x1="140" y1="195" x2="140" y2="105" stroke="#F59E0B" stroke-width="2.5" marker-end="url(#ahde)"/>'
              '</svg>'},
             {"t": "hbox", "color": "red", "html": "Each loop deepens the gap: the group gets less, "
              "generates less data, and looks even 'riskier' next time."},
         ]},

        {"type": "content", "label": "Illustration", "title": "When a model fails one group more than another",
         "blocks": [
             {"t": "chart", "canvas": "biasErrChart",
              "title": "Illustrative: a 'good' overall model with unequal error rates",
              "source": "Illustrative example, not real data",
              "type": "bar",
              "data": {"labels": ["Overall", "Group A", "Group B"],
                       "datasets": [
                           {"label": "False-negative rate (%)",
                            "data": [12, 6, 26],
                            "backgroundColor": ["#6366F1", "#10B981", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:30, title:{display:true,text:'% wrongly denied'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "A 12% overall error can hide a 26% error for "
              "one group. Aggregate accuracy is not fairness."},
         ]},

        {"type": "content", "label": "Many Fairnesses", "title": "Fairness is not one thing",
         "blocks": [
             {"t": "body", "html": "There are several mathematical definitions of fairness &mdash; "
              "equal error rates, equal selection rates, equal outcomes &mdash; and they often "
              "<strong>cannot all hold at once</strong>. Choosing one is a value judgement, not a "
              "technical default."},
             {"t": "hbox", "color": "cyan", "html": "So the right question is not 'is it fair?' but "
              "'fair in which sense, for whom, and who decided?'"},
         ]},

        {"type": "content", "label": "Response", "title": "Auditing for bias is a practice, not a one-off",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Disaggregate</strong> performance by gender, caste, region, language",
                 "<strong>Test for proxies</strong> &mdash; can removed traits be reconstructed?",
                 "<strong>Document</strong> training data, its gaps and known limitations",
                 "<strong>Re-audit</strong> as the system and population change over time"]},
             {"t": "hbox", "color": "amber", "html": "Fairness is not automatic and never finished. "
              "It has to be measured, on purpose, again and again."},
         ]},

        # ===================== SECTION 04 — 8 content =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "AI in Development"},

        {"type": "content", "label": "The Moment", "title": "AI arrives in the development sector",
         "blocks": [
             {"t": "body", "html": "From crop advisories and chatbots to diagnostic tools and "
              "beneficiary targeting, AI &mdash; including large language models &mdash; is now "
              "being piloted across South Asian programmes. The question is no longer whether, but "
              "<strong>how responsibly</strong>."},
             {"t": "hbox", "color": "cyan", "html": "AI is a powerful amplifier. It amplifies good "
              "design and good data &mdash; and it amplifies bias, error and exclusion just as "
              "efficiently."},
         ]},

        {"type": "content", "label": "Opportunities", "title": "Where AI can genuinely help",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [
                  {"t": "bullets", "items": [
                      "<strong>Translation:</strong> bridge dozens of languages and scripts cheaply",
                      "<strong>Diagnostics:</strong> screen X-rays, retina scans, skin conditions where doctors are scarce",
                      "<strong>Targeting:</strong> find likely-eligible households for outreach",
                      "<strong>Triage:</strong> route calls, summarise field reports, flag urgent cases"]}],
              "right": [
                  {"t": "hbox", "color": "green", "html": "Used as an <em>assistant</em> to "
                   "stretched human workers, AI can extend reach into places services never went."}]},
         ]},

        {"type": "content", "label": "Risk One", "title": "Opacity: the black-box problem",
         "blocks": [
             {"t": "term", "word": "Black box",
              "def": "A system whose internal reasoning cannot be inspected or explained &mdash; "
              "you see the input and the output, but not why it decided as it did."},
             {"t": "hbox", "color": "red", "html": "If a model denies someone a benefit and no one "
              "can explain why, the person cannot contest it. Opacity quietly removes the right to "
              "an explanation &mdash; and to appeal."},
         ]},

        {"type": "content", "label": "Risk Two", "title": "Automating exclusion at scale",
         "blocks": [
             {"t": "body", "html": "When an AI system decides who is 'eligible', 'at risk' or "
              "'likely fraudulent', it can lock millions out with no human in the room. The error "
              "is invisible to the operator and devastating to the excluded."},
             {"t": "hbox", "color": "amber", "html": "A false 'ineligible' is not an abstraction. "
              "It is a widow without a pension, a child without a scholarship &mdash; harm that "
              "compounds silently."},
         ]},

        {"type": "content", "label": "Risk Three", "title": "Hallucination &amp; overtrust",
         "blocks": [
             {"t": "body", "html": "Generative AI can produce confident, fluent answers that are "
              "simply <strong>wrong</strong>. In health, legal or entitlement advice, a plausible "
              "falsehood delivered with authority is dangerous."},
             {"t": "hbox", "color": "red", "html": "The risk grows when users assume the machine "
              "must know better. Fluency is not accuracy. Always keep a verified human source for "
              "high-stakes advice."},
         ]},

        {"type": "content", "label": "The Safeguard", "title": "Human-in-the-loop",
         "blocks": [
             {"t": "flow", "steps": [
                 "AI suggests (screen, score, draft)",
                 "Human reviews with context &amp; judgement",
                 "Human decides &mdash; and is accountable",
                 "Affected person can question the decision"]},
             {"t": "hbox", "color": "green", "html": "For any decision that affects rights or "
              "entitlements, AI should <strong>inform</strong> a human, never <strong>replace</strong> "
              "one. Keep a person accountable and reachable."},
         ]},

        {"type": "content", "label": "Match the Stakes", "title": "Not every task needs the same caution",
         "blocks": [
             {"t": "table",
              "head": ["Use", "Stakes", "Guardrail"],
              "rows": [
                  ["Draft a report summary", "Low", "Human edits before sending"],
                  ["Translate a notice", "Medium", "Native speaker verifies"],
                  ["Screen a medical scan", "High", "Clinician confirms every case"],
                  ["Decide benefit eligibility", "Very high", "Human decides; appeal route open"]]},
             {"t": "hbox", "color": "cyan", "html": "Calibrate oversight to the harm of being "
              "wrong. The higher the stakes, the more human judgement and the easier the appeal."},
         ]},

        {"type": "content", "label": "Before You Deploy", "title": "Questions before piloting any AI",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "What is the harm if it is confidently wrong &mdash; and who bears it?",
                 "Can we explain a decision to the person it affects?",
                 "Was it tested on people like ours &mdash; our languages, our context?",
                 "Is there a human fallback and a working appeal route?",
                 "Who is accountable when it fails &mdash; and can they be reached?"]},
         ]},

        # ===================== SECTION 05 — 8 content =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Digital Identity &amp; Inclusion"},

        {"type": "content", "label": "Aadhaar", "title": "The world's largest biometric ID system",
         "blocks": [
             {"t": "body", "html": "<strong>Aadhaar</strong>, run by the Unique Identification "
              "Authority of India (UIDAI), assigns a 12-digit number linked to fingerprints, iris "
              "scans and a photograph. It is the largest biometric identity system ever built."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "~1.3 bn", "label": "Aadhaar numbers issued (widely reported)", "color": "indigo",
                  "source": "UIDAI, widely reported"},
                 {"num": "UIDAI", "label": "the statutory authority that runs it", "color": "cyan"}]},
         ]},

        {"type": "content", "label": "The Scale", "title": "Enrolment at a scale without precedent",
         "blocks": [
             {"t": "chart", "canvas": "aadhaarChart",
              "title": "Aadhaar enrolment growth (illustrative trajectory toward ~1.3 bn)",
              "source": "Illustrative trajectory; ~1.3 bn total widely reported by UIDAI",
              "type": "line",
              "data": {"labels": ["2011", "2013", "2015", "2017", "2019", "2021", "2023"],
                       "datasets": [{"label": "Aadhaar numbers (crore, illustrative)",
                                     "data": [1, 50, 90, 115, 124, 130, 135],
                                     "borderColor": "#6366F1",
                                     "backgroundColor": "rgba(99,102,241,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{title:{display:true,text:'crore (illustrative)'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "The shape is illustrative; the headline "
              "&mdash; near-universal adult coverage &mdash; is widely reported. Scale this large "
              "makes both the gains and the harms enormous."},
         ]},

        {"type": "content", "label": "The Gains", "title": "What digital ID made possible",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "A portable identity for people who had no documents at all",
                 "Direct benefit transfers into bank accounts, cutting some intermediaries",
                 "Removal of some duplicate and 'ghost' beneficiaries",
                 "Easier access to opening bank accounts and SIM cards"]},
             {"t": "hbox", "color": "green", "html": "For someone previously invisible to the "
              "state, a verifiable identity can be genuinely empowering."},
         ]},

        {"type": "content", "label": "The Harms", "title": "Authentication failure becomes exclusion",
         "blocks": [
             {"t": "body", "html": "When entitlements are tied to biometric authentication, anyone "
              "the machine cannot read can be turned away. Worn fingerprints from manual labour, "
              "poor connectivity, server downtime, or a mismatch can mean <strong>no ration "
              "today</strong>."},
             {"t": "hbox", "color": "red", "html": "Researchers and journalists have documented "
              "cases where authentication failures left the elderly and labourers unable to draw "
              "the food they were entitled to. Exclusion by error is still exclusion."},
         ]},

        {"type": "content", "label": "Inclusion vs Exclusion", "title": "The same system, two outcomes",
         "blocks": [
             {"t": "table",
              "head": ["Dimension", "Benefit", "Harm"],
              "rows": [
                  ["Identity", "The undocumented become visible", "Errors make the visible disappear"],
                  ["Delivery", "Faster transfers, fewer ghosts", "Failed auth blocks real beneficiaries"],
                  ["Mandate", "One ID, many services", "Function creep, no real opt-out"],
                  ["Bodies", "Biometrics are hard to forge", "Worn fingerprints exclude labourers"]]},
             {"t": "hbox", "color": "amber", "html": "The lesson is not 'reject digital ID'. It is "
              "design for the person the machine fails &mdash; because at this scale, even a small "
              "failure rate is millions of people."},
         ]},

        {"type": "content", "label": "Design Fix", "title": "Always build a non-digital fallback",
         "blocks": [
             {"t": "body", "html": "Any system where authentication gates a basic entitlement must "
              "have a guaranteed manual override &mdash; a way to receive your due when the "
              "technology fails, without being sent home."},
             {"t": "flow", "steps": [
                 "Biometric fails",
                 "Try alternative (OTP, face, operator)",
                 "Still fails &rarr; manual exception register",
                 "Entitlement delivered &mdash; never denied for tech"]},
         ]},

        {"type": "content", "label": "Voluntary?", "title": "When 'optional' is not really a choice",
         "blocks": [
             {"t": "body", "html": "An ID described as voluntary stops being voluntary if you "
              "cannot get a pension, ration, scholarship or SIM without it. Coerced consent is the "
              "central tension in mandatory-by-practice digital identity."},
             {"t": "hbox", "color": "red", "html": "Ask of any 'voluntary' system: what happens to "
              "someone who says no? If the answer is 'they lose a basic service', it is not "
              "voluntary."},
         ]},

        {"type": "content", "label": "Principle", "title": "Inclusion is the test, not enrolment",
         "blocks": [
             {"t": "hbox", "color": "cyan", "html": "A digital ID is not successful because a "
              "billion people enrolled. It is successful only if the <strong>last</strong> person "
              "&mdash; the worn-fingerprint labourer in a low-connectivity village &mdash; can still "
              "claim what is theirs."},
             {"t": "body", "html": "Measure systems by their failure cases, not their headline "
              "coverage. The margin is where the ethics lives."},
         ]},

        # ===================== SECTION 06 — 8 content =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Surveillance, Power &amp; Consent"},

        {"type": "content", "label": "The Shift", "title": "From serving people to watching them",
         "blocks": [
             {"t": "body", "html": "Digital systems built to deliver services also generate "
              "detailed records of where people go, what they receive and whom they know. Delivery "
              "and surveillance can run on the very same rails."},
             {"t": "hbox", "color": "amber", "html": "The question is rarely 'is there a camera?' "
              "It is 'who can see this data, link it, and act on it &mdash; and can the watched "
              "person say no?'"},
         ]},

        {"type": "content", "label": "Function Creep", "title": "Data collected for X, used for Y",
         "blocks": [
             {"t": "term", "word": "Function creep",
              "def": "When data gathered for one stated purpose is gradually repurposed for others "
              "&mdash; without fresh consent, often without the subject's knowledge."},
             {"t": "body", "html": "A database built to deliver food can become a tool to track, "
              "profile or police the same people. The data outlives the promise made when it was "
              "collected."},
         ]},

        {"type": "content", "label": "Whose Privacy", "title": "The surveillance of the poor",
         "blocks": [
             {"t": "body", "html": "Those who depend on the state are watched most. To receive "
              "welfare, the poor must hand over biometrics, locations, family details and "
              "transaction histories &mdash; a level of scrutiny the wealthy never face to access "
              "their own money."},
             {"t": "quote",
              "text": "Surveillance is distributed unequally: those with the least power are "
              "watched the most.",
              "attr": "&mdash; a recurring finding in surveillance studies"},
         ]},

        {"type": "content", "label": "Conditionality", "title": "Welfare conditionality as control",
         "blocks": [
             {"t": "body", "html": "When aid is conditional on monitored behaviour &mdash; "
              "attendance tracked, accounts linked, movements logged &mdash; the price of help "
              "becomes constant observation. Dignity is quietly traded for entitlement."},
             {"t": "hbox", "color": "red", "html": "Conditions framed as 'accountability' often "
              "land hardest on those least able to comply &mdash; and punish poverty rather than "
              "relieve it."},
         ]},

        {"type": "content", "label": "Chilling Effects", "title": "Being watched changes behaviour",
         "blocks": [
             {"t": "term", "word": "Chilling effect",
              "def": "When the knowledge or suspicion of being monitored makes people self-censor "
              "&mdash; avoiding lawful speech, association or services out of fear."},
             {"t": "hbox", "color": "amber", "html": "People may skip a clinic, a meeting or a "
              "complaint because a record might be kept and used against them. The harm is real "
              "even when no one is actually watching."},
         ]},

        {"type": "content", "label": "Power", "title": "Surveillance is about asymmetry",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "They can see you", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Location, transactions, contacts, biometrics "
                   "&mdash; linked across databases into a single profile."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "You cannot see them", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Who holds the data, what rules apply, how to "
                   "correct an error or contest a decision &mdash; opaque."}]}]},
             {"t": "hbox", "color": "cyan", "html": "The ethical fault line is this asymmetry of "
              "visibility and power, not the technology itself."},
         ]},

        {"type": "content", "label": "Consent Again", "title": "Consent under power imbalance",
         "blocks": [
             {"t": "body", "html": "Consent means little when refusal means losing a livelihood or "
              "a service. A person desperate for aid cannot freely 'agree' to data terms they "
              "could never negotiate."},
             {"t": "hbox", "color": "amber", "html": "Where power is unequal, the burden shifts: "
              "the system must justify what it takes, rather than the person justify their refusal."},
         ]},

        {"type": "content", "label": "Safeguards", "title": "Guardrails against surveillance creep",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Purpose-bind</strong> data and delete it when the purpose ends",
                 "<strong>Separate</strong> service delivery from policing and profiling",
                 "<strong>Minimise</strong> linkage across databases by default",
                 "<strong>Independent oversight</strong> with teeth, and a real complaint route"]},
         ]},

        # ===================== SECTION 07 — 8 content =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "The Digital Divide"},

        {"type": "content", "label": "Definition", "title": "The divide is not one gap but many",
         "blocks": [
             {"t": "term", "word": "Digital divide",
              "def": "The unequal distribution of access to digital devices, connectivity, skills "
              "and meaningful use &mdash; cutting along gender, income, geography, language and "
              "disability."},
             {"t": "body", "html": "It is not simply 'has a phone or not'. It runs from owning a "
              "device, to affording data, to being able to read the screen, to using it for "
              "anything that improves your life."},
         ]},

        {"type": "content", "label": "Gender", "title": "The gender gap in access",
         "blocks": [
             {"t": "chart", "canvas": "genderDivideChart",
              "title": "Illustrative: mobile &amp; internet access by gender",
              "source": "Illustrative pattern; a real gender gap is widely documented in South Asia",
              "type": "bar",
              "data": {"labels": ["Owns a mobile", "Uses the internet", "Owns a smartphone"],
                       "datasets": [
                           {"label": "Men", "data": [78, 52, 44], "backgroundColor": "#0EA5E9"},
                           {"label": "Women", "data": [58, 33, 26], "backgroundColor": "#F59E0B"}]},
              "options": {"__js__": "{ scales:{ y:{min:0,max:100, title:{display:true,text:'% (illustrative)'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "Figures are illustrative, but the pattern is "
              "well documented: women in South Asia are markedly less likely to own a phone or use "
              "the internet than men."},
         ]},

        {"type": "content", "label": "Geography", "title": "Rural, urban and the connectivity gap",
         "blocks": [
             {"t": "chart", "canvas": "ruralDivideChart",
              "title": "Illustrative: internet use, urban vs rural",
              "source": "Illustrative pattern; an urban-rural gap is widely documented",
              "type": "bar",
              "data": {"labels": ["Urban", "Rural"],
                       "datasets": [{"label": "Internet use (%)", "data": [68, 40],
                                     "backgroundColor": ["#6366F1", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100, title:{display:true,text:'% (illustrative)'}} } }"}},
             {"t": "hbox", "color": "cyan", "html": "Coverage maps flatter reality: a tower nearby "
              "does not mean an affordable, reliable signal inside a home."},
         ]},

        {"type": "content", "label": "Other Axes", "title": "Income, language and disability",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Income:</strong> data, devices and electricity all cost money the poorest lack",
                 "<strong>Language:</strong> most services assume English or one dominant language",
                 "<strong>Literacy:</strong> text-heavy interfaces exclude non-readers",
                 "<strong>Disability:</strong> apps rarely work with screen-readers or for low vision"]},
             {"t": "hbox", "color": "amber", "html": "These axes stack. A poor, rural, non-literate "
              "woman with a disability faces every gap at once."},
         ]},

        {"type": "content", "label": "Layers", "title": "Access, skills, and meaningful use",
         "blocks": [
             {"t": "flow", "steps": [
                 "LEVEL 1: Is there a device &amp; signal?",
                 "LEVEL 2: Can they afford to use it?",
                 "LEVEL 3: Do they have the skills &amp; language?",
                 "LEVEL 4: Does it actually improve their life?"]},
             {"t": "hbox", "color": "green", "html": "Closing only the first gap and declaring "
              "victory leaves most people stranded at the higher levels."},
         ]},

        {"type": "content", "label": "The Trap", "title": "The risk of 'digital by default'",
         "blocks": [
             {"t": "body", "html": "When a service goes online-only &mdash; applications, "
              "grievances, payments &mdash; the people on the wrong side of the divide are pushed "
              "out of the systems they need most."},
             {"t": "hbox", "color": "red", "html": "Digital-by-default can become "
              "<strong>digital-or-nothing</strong>: efficient for the connected, a wall for "
              "everyone else."},
         ]},

        {"type": "content", "label": "Intermediaries", "title": "When access depends on a middleman",
         "blocks": [
             {"t": "body", "html": "Many people reach digital services only through an intermediary "
              "&mdash; a relative, a shopkeeper, a kiosk operator. That helps, but it means handing "
              "over passwords, OTPs and personal data, and trusting someone else with your "
              "transactions."},
             {"t": "hbox", "color": "amber", "html": "Dependence on intermediaries creates new "
              "risks: fees, errors, exclusion of those without a trusted helper, and fresh privacy "
              "exposure."},
         ]},

        {"type": "content", "label": "Design Response", "title": "Designing for the unconnected",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Keep an offline / in-person channel for every essential service",
                 "Support local languages, voice and icons &mdash; not just English text",
                 "Build for low-end phones, patchy networks and assisted use",
                 "Measure who is <em>left out</em>, not just who is served"]},
         ]},

        # ===================== SECTION 08 — 8 content =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Platform Power &amp; Data Colonialism"},

        {"type": "content", "label": "The Gatekeepers", "title": "A few platforms shape the digital world",
         "blocks": [
             {"t": "body", "html": "A handful of Big Tech firms run the search engines, app stores, "
              "social networks, cloud servers and operating systems that most digital life in South "
              "Asia depends on &mdash; and most of them are headquartered far away."},
             {"t": "hbox", "color": "amber", "html": "When the rails are owned by a few firms, they "
              "set the rules: what is visible, what is allowed, what data is taken, and what it "
              "costs to take part."},
         ]},

        {"type": "content", "label": "Concept", "title": "Data colonialism",
         "blocks": [
             {"t": "term", "word": "Data colonialism",
              "def": "The large-scale extraction of data from people and communities &mdash; often "
              "in the Global South &mdash; for the benefit of firms elsewhere, echoing older "
              "patterns of resource extraction."},
             {"t": "body", "html": "The raw material is human life itself: behaviour, location, "
              "relationships, attention &mdash; mined, processed and monetised far from where it "
              "was produced."},
         ]},

        {"type": "content", "label": "The Flow", "title": "Where the value goes",
         "blocks": [
             {"t": "flow", "steps": [
                 "Users in the Global South generate data",
                 "Platforms collect &amp; process it abroad",
                 "Profiles, ads &amp; AI models are built",
                 "Profit &amp; control accrue elsewhere"]},
             {"t": "hbox", "color": "red", "html": "The people who produce the data rarely own it, "
              "see the profit, or shape the terms. The value flows one way."},
         ]},

        {"type": "content", "label": "Extraction", "title": "The Global South as a data source",
         "blocks": [
             {"t": "body", "html": "Fast-growing user bases in South Asia are highly valuable: huge "
              "markets, rich data, and often weaker bargaining power and regulation. The region "
              "supplies users and data, but holds little of the infrastructure or the upside."},
             {"t": "hbox", "color": "amber", "html": "Cheap or 'free' services are paid for in "
              "data. The product offered for free is usually the user's attention and information."},
         ]},

        {"type": "content", "label": "Asymmetry", "title": "Who captures the value",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Platforms gain", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Ad revenue and market dominance",
                      "Training data for AI models",
                      "Lock-in and network effects"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Users get", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "A free service &mdash; for now",
                      "Little say over terms or data",
                      "No share of the value created"]}]}]},
         ]},

        {"type": "content", "label": "Dependence", "title": "When development runs on rented rails",
         "blocks": [
             {"t": "body", "html": "NGOs and governments increasingly build on platforms they do "
              "not control &mdash; cloud servers, messaging apps, ad systems. A change in pricing, "
              "policy or access can disrupt critical services overnight."},
             {"t": "hbox", "color": "amber", "html": "Ask before you build: what happens to our "
              "beneficiaries if this platform changes its rules, raises its price, or shuts our "
              "account?"},
         ]},

        {"type": "content", "label": "Sovereignty", "title": "Data sovereignty &amp; local alternatives",
         "blocks": [
             {"t": "body", "html": "<strong>Data sovereignty</strong> is the idea that a community "
              "or country should have meaningful control over data about its people. Public digital "
              "infrastructure and open-source tools are part of the response."},
             {"t": "hbox", "color": "green", "html": "The goal is not autarky but agency: the "
              "ability to set terms, keep critical data local, and not be wholly dependent on a "
              "single foreign firm."},
         ]},

        {"type": "content", "label": "Practitioner Stance", "title": "Using platforms with eyes open",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Prefer open, portable formats so you are not locked in",
                 "Keep your own copy of essential data, off the platform",
                 "Read the data terms &mdash; what does the platform take from your users?",
                 "Favour public or community infrastructure for critical services where viable"]},
         ]},

        # ===================== SECTION 09 — 8 content =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Misinformation &amp; Online Harms"},

        {"type": "content", "label": "The Landscape", "title": "Information disorder in everyday life",
         "blocks": [
             {"t": "body", "html": "False and misleading content spreads through the same channels "
              "people rely on for news, health advice and family contact. In South Asia, much of it "
              "flows through <strong>WhatsApp</strong> and other messaging apps."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Misinformation", "blocks": [
                  {"t": "body", "cls": "sm", "html": "False, but shared without intent to harm "
                   "&mdash; a worried relative forwarding a 'cure'."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Disinformation", "blocks": [
                  {"t": "body", "cls": "sm", "html": "False and spread <em>deliberately</em> "
                   "&mdash; to deceive, profit or incite."}]}]},
         ]},

        {"type": "content", "label": "Why It Spreads", "title": "The mechanics of a rumour",
         "blocks": [
             {"t": "body", "html": "Encrypted, closed groups make forwarded messages feel personal "
              "and trustworthy &mdash; they come from family, not a stranger. There is no visible "
              "source, no correction, and outrage travels faster than fact."},
             {"t": "hbox", "color": "amber", "html": "A message from your uncle's group carries the "
              "weight of your uncle, even when its content is false. Trust in the messenger "
              "launders the message."},
         ]},

        {"type": "content", "label": "Real Harm", "title": "When rumours turn to violence",
         "blocks": [
             {"t": "body", "html": "Viral rumours &mdash; for example false 'child-kidnapper' "
              "messages forwarded on WhatsApp &mdash; have been linked to mob violence and "
              "killings in India. Online falsehood becomes offline harm."},
             {"t": "hbox", "color": "red", "html": "This is not a debate about opinions. "
              "Misinformation at scale can get people hurt and killed, and inflame communal "
              "tension."},
         ]},

        {"type": "content", "label": "Targeting the Poor", "title": "Scams that prey on the vulnerable",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Fake 'KYC update' messages that steal banking OTPs",
                 "Bogus government-scheme and lottery messages demanding a fee",
                 "Loan-app traps with hidden charges and harassment",
                 "Phishing aimed at first-time, low-literacy internet users"]},
             {"t": "hbox", "color": "amber", "html": "New users with little digital experience and "
              "thin financial buffers are prime targets &mdash; and lose the most when caught."},
         ]},

        {"type": "content", "label": "Health &amp; Elections", "title": "Where false information does the most damage",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Health", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Vaccine rumours, fake cures and dangerous "
                   "remedies cost lives, as seen vividly during COVID-19."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Democracy", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Coordinated falsehoods can distort elections, "
                   "inflame division and erode trust in institutions."}]}]},
         ]},

        {"type": "content", "label": "Moderation", "title": "Content moderation in Indian languages",
         "blocks": [
             {"t": "body", "html": "Platforms moderate far better in English than in Hindi, Tamil, "
              "Bengali, Marathi and dozens of other languages. Harmful content in under-resourced "
              "languages and code-mixed scripts often slips through."},
             {"t": "hbox", "color": "red", "html": "The places with the most users and the highest "
              "real-world stakes frequently get the least moderation investment. Language is a "
              "safety gap."},
         ]},

        {"type": "content", "label": "Tension", "title": "Moderation vs free expression",
         "blocks": [
             {"t": "body", "html": "Removing harmful content and protecting free speech pull "
              "against each other. Over-removal silences dissent and minorities; under-removal lets "
              "harm spread. Neither side is automatically right."},
             {"t": "hbox", "color": "amber", "html": "Beware moderation powers framed as safety "
              "that become tools to suppress legitimate criticism. Who decides, and who can appeal, "
              "matters as much as the rule."},
         ]},

        {"type": "content", "label": "What Helps", "title": "Responses that actually work",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Digital literacy</strong>: teach people to pause, check and verify before forwarding",
                 "<strong>Friction</strong>: limits on mass-forwarding slow viral spread",
                 "<strong>Local fact-checking</strong> in the languages people actually use",
                 "<strong>Trusted messengers</strong> &mdash; community voices counter rumours best"]},
         ]},

        # ===================== SECTION 10 — 7 content =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Responsible Design &amp; Principles"},

        {"type": "content", "label": "The Shift", "title": "Ethics at the start, not the audit",
         "blocks": [
             {"t": "body", "html": "Most digital harm is designed in early and discovered late. "
              "Responsible design moves ethical questions to the <strong>first</strong> meeting, "
              "where they are cheap to fix &mdash; not the launch review, where they are not."},
             {"t": "hbox", "color": "cyan", "html": "You cannot bolt ethics on at the end. By then "
              "the data is collected, the model is trained and the exclusions are baked in."},
         ]},

        {"type": "content", "label": "By Design", "title": "Privacy &amp; ethics by design",
         "blocks": [
             {"t": "term", "word": "Privacy by design",
              "def": "Building privacy protections into a system's architecture and defaults from "
              "the outset &mdash; rather than adding them later as an afterthought or an opt-in."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Privacy-protective <strong>defaults</strong>, not opt-out traps",
                 "Collect the minimum; delete when done",
                 "Security and access controls built in from day one"]},
         ]},

        {"type": "content", "label": "A Real Framework", "title": "The Principles for Digital Development",
         "blocks": [
             {"t": "body", "html": "The <strong>Principles for Digital Development</strong> are a "
              "widely endorsed set of guidelines for using technology in development work &mdash; a "
              "real, sector-wide framework, not a slogan."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Design <strong>with</strong> the user; understand the existing ecosystem",
                 "Design for <strong>scale</strong> and <strong>sustainability</strong>",
                 "Be <strong>data-driven</strong>; use open standards and reusable tools",
                 "<strong>Address privacy &amp; security</strong>; be collaborative"]},
         ]},

        {"type": "content", "label": "The Rule", "title": "Do no (digital) harm",
         "blocks": [
             {"t": "body", "html": "The humanitarian principle of <strong>do no harm</strong> "
              "applies fully to data and technology. Before deploying, ask how the system could be "
              "misused &mdash; and who would be hurt if it were."},
             {"t": "flow", "steps": [
                 "Map who could be harmed",
                 "Map how data could be misused",
                 "Design the safeguard &amp; the fallback",
                 "Decide: is the benefit worth the residual risk?"]},
         ]},

        {"type": "content", "label": "Core Practice", "title": "Data minimisation as a habit",
         "blocks": [
             {"t": "body", "html": "The single most protective habit is to <strong>collect "
              "less</strong>. Every field you do not gather is a breach that cannot happen and a "
              "tool that cannot be turned against people later."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Collect less", "label": "fewer fields, less risk, less liability", "color": "green"},
                 {"num": "Keep less", "label": "delete on a schedule; don't hoard 'just in case'", "color": "cyan"}]},
         ]},

        {"type": "content", "label": "Participation", "title": "Design with, not for",
         "blocks": [
             {"t": "body", "html": "The people affected by a system know its failure modes best. "
              "Involving them in design surfaces exclusions, language gaps and risks that "
              "outsiders simply cannot see."},
             {"t": "hbox", "color": "green", "html": "Nothing about us without us. Co-design is not "
              "a courtesy &mdash; it is how you find the harms before they reach a million people."},
         ]},

        {"type": "content", "label": "Accountability", "title": "Build in redress from the start",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "A clear, reachable way to <strong>contest</strong> an automated decision",
                 "A <strong>human</strong> who can override the system when it is wrong",
                 "Plain-language notice of what data is held and why",
                 "An <strong>exit</strong>: people can correct, delete, or refuse"]},
             {"t": "hbox", "color": "cyan", "html": "A system with no appeal route is not "
              "efficient &mdash; it is unaccountable."},
         ]},

        # ===================== SECTION 11 — 7 content =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Governance, Regulation &amp; Practice"},

        {"type": "content", "label": "Who Governs", "title": "The layers that hold systems to account",
         "blocks": [
             {"t": "flow", "steps": [
                 "LAW: the DPDP Act &amp; constitutional rights",
                 "REGULATOR: a data-protection authority",
                 "ORGANISATION: your own policies &amp; reviews",
                 "PRACTITIONER: the daily choices you make"]},
             {"t": "hbox", "color": "cyan", "html": "Governance is not only the regulator's job. "
              "The last and most frequent line of defence is the person designing the form."},
         ]},

        {"type": "content", "label": "The Authority", "title": "Data protection authorities",
         "blocks": [
             {"t": "body", "html": "The DPDP Act establishes a <strong>Data Protection Board of "
              "India</strong> to handle breaches and grievances. Globally, independent data "
              "protection authorities enforce rules, investigate complaints and impose penalties."},
             {"t": "hbox", "color": "amber", "html": "A law is only as strong as the body that "
              "enforces it. Watch for independence, resources and real power to act &mdash; not "
              "just words on paper."},
         ]},

        {"type": "content", "label": "Rights", "title": "The rights people hold over their data",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Access:</strong> know what data is held about you",
                 "<strong>Correction:</strong> fix what is wrong",
                 "<strong>Erasure:</strong> have data deleted when no longer needed",
                 "<strong>Grievance:</strong> complain and seek redress"]},
             {"t": "hbox", "color": "cyan", "html": "Help the communities you work with understand "
              "these rights. A right nobody knows about protects nobody."},
         ]},

        {"type": "content", "label": "Checklist", "title": "An organisation's digital-ethics checklist",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Area", "Ask before you deploy"],
              "rows": [
                  ["Purpose", "Is each data field truly necessary?"],
                  ["Consent", "Is it free, informed, specific, revocable?"],
                  ["Inclusion", "Who does this design exclude &mdash; and is there a fallback?"],
                  ["Bias", "Have we tested outcomes across groups?"],
                  ["Security", "Who can access this, and is it protected?"],
                  ["Redress", "Can a person contest a decision and reach a human?"]]},
         ]},

        {"type": "content", "label": "Procurement", "title": "Ethics when you buy, not just when you build",
         "blocks": [
             {"t": "body", "html": "Most organisations buy or adopt tools rather than build them. "
              "The ethics questions still apply &mdash; ask the vendor, and make the answers part "
              "of the contract."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Where is data stored, and who can access it?",
                 "Has the tool been tested for bias and accessibility?",
                 "What happens to our data if we leave the vendor?"]},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Behind every record is a person</strong> &mdash; usually with little power to refuse",
                 "<strong>Collect less</strong> &mdash; minimisation is the strongest safeguard",
                 "<strong>Design for the person the system fails</strong>, not the headline coverage",
                 "<strong>Bias is inherited</strong> from data and proxies &mdash; audit, don't assume",
                 "<strong>Keep a human accountable</strong> and an appeal route open"]},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "Further reading &amp; companion courses",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Weapons of Math Destruction</em> &mdash; Cathy O'Neil (algorithmic harm)",
                 "<em>The Costs of Connection</em> &mdash; Couldry &amp; Mejias (data colonialism)",
                 "<em>Automating Inequality</em> &mdash; Virginia Eubanks (welfare &amp; tech)",
                 "<em>Data Feminism</em> &mdash; D'Ignazio &amp; Klein (power and data)",
                 "The <em>Principles for Digital Development</em> &mdash; the sector framework"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Research Ethics</strong> and "
              "<strong>AI &amp; Society</strong> 101 courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Digital Ethics 101 &middot; Complete",
         "headline": "Build it like a<br>person is on the other side.",
         "byline": "Every database, model and app in development touches someone with little power "
                   "to refuse it. Ask who benefits, who is excluded, and who can contest the "
                   "decision &mdash; before you deploy. Explore the rest of the ImpactMojo 101 "
                   "Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
