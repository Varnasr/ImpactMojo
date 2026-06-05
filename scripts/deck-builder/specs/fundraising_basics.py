# -*- coding: utf-8 -*-
"""
Fundraising Basics 101 — ImpactMojo 101 Series (native deck spec)
Foundational resource mobilisation for NGO & nonprofit staff in India & South Asia.
Build: python3 scripts/deck-builder/build.py fundraising_basics
"""

DECK = {
    "slug": "fundraising-basics",
    "title": "Fundraising Basics 101",
    "description": ("Fundraising Basics 101 — a free foundational course for NGO and nonprofit "
                    "staff in India and South Asia. From mission-first resource mobilisation and "
                    "the funding landscape to proposals, budgets, CSR under the Companies Act, "
                    "FCRA and 80G compliance, donor relationships and the ethics of fundraising. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Fundraising<br>Basics<br>101",
         "sub": "Resource Mobilisation, Donors, Proposals, CSR &amp; Compliance &mdash; a "
                "Foundational Course for NGO &amp; Nonprofit Staff in India &amp; South Asia",
         "tags": ["Practitioner Guide", "India &amp; South Asia", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Fundraising Really Is"},
             {"name": "The Funding Landscape"},
             {"name": "Knowing Your Donors"},
             {"name": "Strategy &amp; the Fundraising Cycle"},
             {"name": "Writing a Winning Proposal"},
             {"name": "Budgeting &amp; Financial Basics"},
             {"name": "Individual Giving &amp; Relationships"},
             {"name": "CSR in India"},
             {"name": "Compliance &amp; Accountability"},
             {"name": "Diversification &amp; Sustainability"},
             {"name": "Ethics, Practice &amp; Further Reading"},
         ]},

        # ===================== SECTION 01 — What Fundraising Really Is (8) =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Fundraising Really Is"},

        {"type": "content", "label": "Definition", "title": "Fundraising is resource mobilisation",
         "blocks": [
             {"t": "body", "html": "Fundraising is not begging for money. It is "
              "<strong>resource mobilisation</strong> &mdash; the disciplined work of securing "
              "the money, goods, skills and goodwill an organisation needs to deliver its "
              "mission. Money is one resource among several, and never the point in itself."},
             {"t": "term", "word": "Resource mobilisation",
              "def": "The full set of activities an organisation undertakes to acquire and "
              "sustain the financial and non-financial resources it needs to pursue its mission "
              "&mdash; from grants and individual gifts to volunteers, in-kind support and assets."},
             {"t": "hbox", "color": "cyan", "html": "You are not raising money for its own sake. "
              "You are raising the means to a mission. Keep that order straight and everything "
              "else follows."},
         ]},

        {"type": "content", "label": "Mission First", "title": "Mission first, money second",
         "blocks": [
             {"t": "flow", "steps": [
                 "MISSION: the change you exist to create",
                 "STRATEGY: how you will create it",
                 "RESOURCES: what that strategy needs",
                 "FUNDRAISING: how you secure those resources"]},
             {"t": "hbox", "color": "amber", "html": "Fundraising sits at the <em>end</em> of "
              "this chain, not the start. When money leads, organisations chase grants that pull "
              "them away from their mission &mdash; the classic 'mission drift'."},
         ]},

        {"type": "content", "label": "Relationships", "title": "Relationships, not transactions",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Transactional thinking", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Ask only when you need cash",
                      "Treat the donor as an ATM",
                      "Disappear after the cheque clears",
                      "One-off, anxious, extractive"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Relational thinking", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Build trust before the ask",
                      "Treat the donor as a partner",
                      "Report, thank, involve, repeat",
                      "Long-term, mutual, dignified"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "People give to people, and to causes they "
              "trust. The strongest fundraising is a relationship that happens to involve money."},
         ]},

        {"type": "content", "label": "What You Mobilise", "title": "Money is only one resource",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Money", "label": "Grants, donations, CSR, earned income", "color": "cyan"},
                 {"num": "In-kind", "label": "Goods, equipment, space, pro-bono services", "color": "green"},
                 {"num": "People", "label": "Volunteers, skills, board networks, advocates", "color": "indigo"}]},
             {"t": "body", "html": "A volunteer doctor, a donated server, a lawyer's pro-bono "
              "hours and a board member's introduction are all 'funds raised' in every sense "
              "that matters. Count them, value them, thank for them."},
         ]},

        {"type": "content", "label": "Who Does It", "title": "Fundraising is everyone's job",
         "blocks": [
             {"t": "body", "html": "Fundraising is not a back-office function owned by one "
              "person. The programme officer who documents impact, the field worker who tells a "
              "story well, the finance lead who reports cleanly &mdash; all are part of the "
              "fundraising machine."},
             {"t": "hbox", "color": "amber", "html": "The best 'fundraising department' is an "
              "organisation that delivers real impact and can prove it. Everything you raise "
              "rests on what you actually do."},
         ]},

        {"type": "content", "label": "The Exchange", "title": "What the donor gets in return",
         "blocks": [
             {"t": "body", "html": "A gift is not charity flowing one way. The donor receives "
              "something real: a share in the change, a sense of meaning, public recognition, "
              "tax benefit, or alignment with their values. Good fundraising names that value "
              "honestly."},
             {"t": "quote",
              "text": "Fundraising is the gentle art of teaching people the joy of giving.",
              "attr": "&mdash; Hank Rosso, founder of The Fund Raising School"},
         ]},

        {"type": "content", "label": "Myths", "title": "Three myths to unlearn early",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>'Good work funds itself.'</strong> It does not. Impact without "
                 "communication stays invisible &mdash; and invisible work goes unfunded.",
                 "<strong>'Overheads are waste.'</strong> Salaries, systems and audits are what "
                 "make impact possible, not a deduction from it.",
                 "<strong>'One big donor will save us.'</strong> Dependence on a single funder "
                 "is the fastest route to an organisational crisis."]},
         ]},

        {"type": "content", "label": "The Goal", "title": "Sustainable funding, not just this year's gap",
         "blocks": [
             {"t": "body", "html": "Beginners fundraise to plug the current shortfall. Mature "
              "organisations fundraise to build a <strong>resilient, diversified resource base</strong> "
              "&mdash; so the mission survives the loss of any single donor."},
             {"t": "hbox", "color": "green", "html": "The question is never just 'how do we "
              "cover this year?' It is 'how do we build a funding base that lasts?' This course "
              "works toward that answer."},
         ]},

        # ===================== SECTION 02 — The Funding Landscape (8) =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Funding Landscape"},

        {"type": "content", "label": "The Map", "title": "Where development money comes from",
         "blocks": [
             {"t": "body", "html": "Before you ask anyone for anything, map the terrain. NGO "
              "income in South Asia flows from a handful of distinct <strong>sources</strong>, "
              "each with its own logic, paperwork and relationship style."},
             {"t": "bullets", "items": [
                 "Grants from foundations &amp; trusts (domestic and international)",
                 "Government schemes, contracts and grants-in-aid",
                 "Corporate Social Responsibility (CSR) funds",
                 "Individual giving &mdash; small donors and major donors",
                 "Crowdfunding and digital campaigns",
                 "Earned income &mdash; fees, products, social enterprise"]},
         ]},

        {"type": "content", "label": "Funding Mix", "title": "A healthy, diversified funding mix",
         "blocks": [
             {"t": "chart", "canvas": "fundingMixChart",
              "title": "Illustrative diversified funding mix for a mid-size NGO",
              "source": "Illustrative &mdash; not a real organisation",
              "type": "doughnut",
              "data": {"labels": ["Institutional grants", "CSR", "Individual giving",
                                  "Government", "Earned income", "Crowdfunding"],
                       "datasets": [{"data": [30, 22, 20, 12, 11, 5],
                                     "backgroundColor": ["#0EA5E9", "#10B981", "#6366F1",
                                                         "#F59E0B", "#EF4444", "#94A3B8"]}]},
              "options": {"__js__": "{ plugins:{ legend:{ position:'right' } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Illustrative only &mdash; there is no "
              "'correct' split. The point is that no single slice dominates. Diversification is "
              "resilience."},
         ]},

        {"type": "content", "label": "Grants", "title": "Grants &amp; foundations",
         "blocks": [
             {"t": "twocol", "ratio": "a32",
              "left": [
                  {"t": "body", "html": "<strong>Grants</strong> are funds given by foundations, "
                   "trusts, bilateral and multilateral agencies for a defined purpose, usually "
                   "against a proposal and a reporting schedule. They are the backbone of many "
                   "NGOs &mdash; large, but competitive and often restricted."}],
              "right": [
                  {"t": "panel", "color": "amber", "title": "Watch for", "blocks": [
                      {"t": "bullets", "sm": True, "color": "amber", "items": [
                          "Restricted to specific activities",
                          "Heavy reporting burden",
                          "Time-limited &mdash; cliffs at project end"]}]}]},
         ]},

        {"type": "content", "label": "Government", "title": "Government funding",
         "blocks": [
             {"t": "body", "html": "Governments fund NGOs through <strong>grants-in-aid</strong>, "
              "scheme implementation and service contracts. The scale can be large and the "
              "alignment with public goals strong &mdash; but cycles are slow, paperwork is "
              "heavy, and payments can be delayed."},
             {"t": "hbox", "color": "amber", "html": "Government money rewards compliance and "
              "reach. Strong systems, clean accounts and patience matter more here than a "
              "polished pitch."},
         ]},

        {"type": "content", "label": "CSR", "title": "Corporate Social Responsibility (CSR)",
         "blocks": [
             {"t": "body", "html": "Since the Companies Act, 2013, large Indian companies must "
              "spend on social causes &mdash; making <strong>CSR</strong> one of the most "
              "significant domestic funding streams for Indian NGOs. We devote a full section to "
              "it later."},
             {"t": "hbox", "color": "cyan", "html": "CSR is partnership funding: companies seek "
              "credible delivery partners with the legal registrations and the track record to "
              "spend their money well and report it cleanly."},
         ]},

        {"type": "content", "label": "Individuals", "title": "Individual giving",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Why it matters", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Usually unrestricted &mdash; spend where needed",
                      "Loyal, renewable, recession-resilient",
                      "Builds a base that belongs to you"]}]}],
              "right": [{"t": "panel", "color": "amber", "title": "The catch", "blocks": [
                  {"t": "bullets", "sm": True, "color": "amber", "items": [
                      "Slow to build &mdash; years, not weeks",
                      "Needs investment up front",
                      "Many small gifts to manage well"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Individual giving is the hardest to start "
              "and the most valuable to own. It is the foundation of true independence."},
         ]},

        {"type": "content", "label": "Crowdfunding", "title": "Crowdfunding &amp; digital giving",
         "blocks": [
             {"t": "body", "html": "Platforms such as Ketto, Milaap, GiveIndia and DonateKart "
              "let organisations raise many small gifts online around a specific, urgent, "
              "shareable story. Powerful for acquisition and visibility &mdash; less so for "
              "steady core funding."},
             {"t": "hbox", "color": "amber", "html": "Crowdfunding rewards a sharp story and a "
              "clear, time-bound goal. It works best for a concrete need, not for 'general "
              "running costs'."},
         ]},

        {"type": "content", "label": "Earned Income", "title": "Earned income &amp; social enterprise",
         "blocks": [
             {"t": "body", "html": "Some organisations earn income directly &mdash; training "
              "fees, consultancy, sale of products made by beneficiaries, or a social-enterprise "
              "arm. Earned income is typically unrestricted and can grow with the organisation."},
             {"t": "hbox", "color": "red", "html": "But it carries commercial risk and can pull "
              "focus from the mission. Treat it as one stream in the mix, not a rescue plan, and "
              "check the tax and regulatory implications first."},
         ]},

        # ===================== SECTION 03 — Knowing Your Donors (8) =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Knowing Your Donors"},

        {"type": "content", "label": "Two Worlds", "title": "Institutional vs individual donors",
         "blocks": [
             {"t": "table",
              "head": ["", "Institutional", "Individual"],
              "rows": [
                  ["Who", "Foundations, CSR, government", "People who give from their own pocket"],
                  ["Decision", "Committees, proposals, criteria", "Emotion, trust, personal connection"],
                  ["Funds", "Usually restricted", "Often unrestricted"],
                  ["Cycle", "Formal, slow, scheduled", "Flexible, relationship-paced"],
                  ["Win them with", "Evidence &amp; alignment", "Story &amp; relationship"]]},
             {"t": "hbox", "color": "cyan", "html": "The two require different skills. Confusing "
              "them &mdash; pitching a foundation like a friend, or a friend like a logframe "
              "&mdash; is a common, costly error."},
         ]},

        {"type": "content", "label": "Motivations", "title": "Why donors actually give",
         "blocks": [
             {"t": "body", "html": "People and institutions give for reasons that are rarely "
              "only altruistic. Understanding the real motive lets you make an honest, "
              "resonant case."},
             {"t": "bullets", "items": [
                 "<strong>Belief</strong> in the cause and its urgency",
                 "<strong>Trust</strong> in this organisation to deliver",
                 "<strong>Identity</strong> &mdash; 'this is the kind of person/company I am'",
                 "<strong>Connection</strong> &mdash; a personal link to the issue",
                 "<strong>Recognition</strong>, legacy, faith, or tax benefit"]},
         ]},

        {"type": "content", "label": "Donor's View", "title": "See the gift through the donor's eyes",
         "blocks": [
             {"t": "body", "html": "Every donor is asking, often silently: <em>Why this cause? "
              "Why this organisation? Why now? Why me? What difference will my gift make, and "
              "how will I know?</em>"},
             {"t": "hbox", "color": "green", "html": "If your case for support answers those "
              "five questions clearly, you have done most of the work. If it cannot, no amount "
              "of asking will fix it."},
         ]},

        {"type": "content", "label": "Fund Types", "title": "Restricted vs unrestricted funds",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Restricted", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Tied to a specific project, activity or "
                   "line item. You must spend it as agreed and report against it. Most grants and "
                   "CSR are restricted."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Unrestricted", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Yours to allocate where the mission needs "
                   "it &mdash; including salaries, systems and the gaps grants won't cover. Gold "
                   "dust for an NGO."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Chase unrestricted funding deliberately. It "
              "is what keeps the lights on and lets you respond to what the work actually "
              "requires."},
         ]},

        {"type": "content", "label": "Power", "title": "The funder&ndash;grantee power imbalance",
         "blocks": [
             {"t": "body", "html": "Money carries power. The funder sets the agenda, the format, "
              "the timeline and the definition of success &mdash; while the grantee, closest to "
              "the community, often has the least say. This imbalance shapes the whole sector."},
             {"t": "quote",
              "text": "Whoever holds the purse strings tends to hold the pen that writes the "
              "theory of change.",
              "attr": "&mdash; a recurring critique in development practice"},
         ]},

        {"type": "content", "label": "Naming It", "title": "How the imbalance distorts the work",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Grantees chase fashionable themes rather than real local need",
                 "Energy drains into donor reports instead of community work",
                 "Short grant cycles block the long-term work that actually matters",
                 "NGOs stay silent on problems for fear of losing funding"]},
             {"t": "hbox", "color": "amber", "html": "Naming the imbalance is the first step to "
              "negotiating within it &mdash; for trust-based, flexible, multi-year funding that "
              "shifts power back toward the community."},
         ]},

        {"type": "content", "label": "Due Diligence", "title": "Vet the donor, too",
         "blocks": [
             {"t": "body", "html": "Fundraising due diligence runs both ways. Before accepting "
              "money, ask whether the donor's values, sources of wealth and conditions are "
              "compatible with your mission and your community's dignity."},
             {"t": "hbox", "color": "red", "html": "Some money costs too much &mdash; gifts that "
              "demand silence, distort the mission, or come from sources that harm the very "
              "people you serve. It is legitimate to say no."},
         ]},

        {"type": "content", "label": "Segment", "title": "Not all donors are the same",
         "blocks": [
             {"t": "body", "html": "Treat donors as distinct groups, not one undifferentiated "
              "crowd. A first-time ₹500 online giver, a loyal monthly donor and a CSR head each "
              "need a different message, channel and ask."},
             {"t": "hbox", "color": "cyan", "html": "<strong>Segmentation</strong> &mdash; "
              "grouping donors by giving level, channel, loyalty and interest &mdash; is the "
              "foundation of every relationship that follows."},
         ]},

        # ===================== SECTION 04 — Strategy & the Fundraising Cycle (8) ==========
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Strategy &amp; the Fundraising Cycle"},

        {"type": "content", "label": "Start Here", "title": "A strategy, not a scramble",
         "blocks": [
             {"t": "body", "html": "Most NGOs fundraise reactively &mdash; chasing whatever "
              "deadline appears. A <strong>fundraising strategy</strong> turns that scramble "
              "into a plan: how much you need, from whom, by when, and who is responsible."},
             {"t": "flow", "steps": [
                 "NEED: what the plan costs",
                 "SOURCES: who could fund it",
                 "TARGETS: how much from each",
                 "ACTIONS: who does what, by when"]},
         ]},

        {"type": "content", "label": "Case for Support", "title": "The case for support",
         "blocks": [
             {"t": "term", "word": "Case for support",
              "def": "The core document that answers why your cause deserves funding &mdash; the "
              "problem, your solution, the evidence it works, and the difference a gift will "
              "make. Every proposal and pitch draws from it."},
             {"t": "hbox", "color": "cyan", "html": "Write it once, well, and adapt it everywhere "
              "&mdash; for a grant, a CSR deck, a website page or a one-minute conversation. It "
              "is your single most reusable fundraising asset."},
         ]},

        {"type": "content", "label": "Prospect Research", "title": "Prospect research: find the right fit",
         "blocks": [
             {"t": "body", "html": "<strong>Prospect research</strong> is finding donors whose "
              "interests, geography, giving size and values match your work &mdash; before you "
              "spend effort asking. A perfect proposal to the wrong funder is wasted."},
             {"t": "bullets", "sm": True, "items": [
                 "What does the funder already fund? (Read their past grants.)",
                 "Do your theme, region and budget size fit theirs?",
                 "How do they prefer to be approached &mdash; and when?",
                 "Is there a warm introduction available?"]},
         ]},

        {"type": "content", "label": "The Cycle", "title": "Cultivation &rarr; ask &rarr; stewardship",
         "blocks": [
             {"t": "flow", "steps": [
                 "IDENTIFY: who could give",
                 "CULTIVATE: build the relationship &amp; trust",
                 "ASK: make a clear, specific request",
                 "STEWARD: thank, report, involve",
                 "RENEW: ask again, for more"]},
             {"t": "hbox", "color": "amber", "html": "The 'ask' is one moment in a long cycle. "
              "Organisations that rush to it &mdash; or stop after it &mdash; leave most of the "
              "money on the table."},
         ]},

        {"type": "content", "label": "Cultivation", "title": "Cultivation: trust before the ask",
         "blocks": [
             {"t": "body", "html": "<strong>Cultivation</strong> is the patient work of building "
              "a relationship before any request: sharing updates, inviting site visits, "
              "listening to the donor's interests, demonstrating credibility over time."},
             {"t": "hbox", "color": "cyan", "html": "You do not propose marriage on a first "
              "meeting. The bigger the gift you hope for, the more cultivation it deserves."},
         ]},

        {"type": "content", "label": "The Ask", "title": "Making the ask",
         "blocks": [
             {"t": "bullets", "items": [
                 "Be <strong>specific</strong>: a clear amount, for a clear purpose",
                 "Ask for what the work needs &mdash; do not undersell from fear",
                 "Make it easy to say yes: define the next step",
                 "Then <strong>stop talking</strong> and let the donor respond"]},
             {"t": "hbox", "color": "green", "html": "The commonest fundraising failure is "
              "simply never making a clear ask. People rarely give what they are not directly "
              "invited to give."},
         ]},

        {"type": "content", "label": "Stewardship", "title": "Stewardship: the relationship after the gift",
         "blocks": [
             {"t": "body", "html": "<strong>Stewardship</strong> is everything you do after the "
              "gift arrives: a prompt, genuine thank-you; honest reporting on what the money "
              "achieved; and keeping the donor connected to the impact they made possible."},
             {"t": "hbox", "color": "cyan", "html": "Stewardship is where the <em>next</em> gift "
              "is earned. A donor thanked well and shown real impact is your warmest prospect."},
         ]},

        {"type": "content", "label": "The Pyramid", "title": "The fundraising / donor pyramid",
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 760 360" width="100%" style="max-height:46vh" '
                 'xmlns="http://www.w3.org/2000/svg" font-family="inherit">'
                 '<polygon points="380,20 470,110 290,110" fill="#EF4444"/>'
                 '<polygon points="290,112 470,112 520,200 240,200" fill="#F59E0B"/>'
                 '<polygon points="240,202 520,202 580,290 180,290" fill="#6366F1"/>'
                 '<polygon points="180,292 580,292 640,350 120,350" fill="#0EA5E9"/>'
                 '<text x="380" y="80" fill="#fff" font-size="15" font-weight="700" '
                 'text-anchor="middle">Legacy / major gifts</text>'
                 '<text x="380" y="165" fill="#fff" font-size="15" font-weight="700" '
                 'text-anchor="middle">Major &amp; mid donors</text>'
                 '<text x="380" y="255" fill="#fff" font-size="15" font-weight="700" '
                 'text-anchor="middle">Regular / monthly donors</text>'
                 '<text x="380" y="330" fill="#fff" font-size="15" font-weight="700" '
                 'text-anchor="middle">First-time &amp; small donors (the base)</text>'
                 '<text x="655" y="345" fill="#94A3B8" font-size="12" '
                 'text-anchor="start">many</text>'
                 '<text x="395" y="40" fill="#94A3B8" font-size="12" '
                 'text-anchor="start">few</text>'
                 '</svg>')},
             {"t": "hbox", "color": "amber", "html": "Move donors <em>up</em> the pyramid over "
              "time: acquire many at the base, retain them, and deepen a few into major givers. "
              "Illustrative structure &mdash; the exact levels vary by organisation."},
         ]},

        # ===================== SECTION 05 — Writing a Winning Proposal (8) ===============
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Writing a Winning Proposal"},

        {"type": "content", "label": "Anatomy", "title": "What a proposal must contain",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Section", "Answers", "Common pitfall"],
              "rows": [
                  ["Problem statement", "Why does this matter?", "Vague, unevidenced"],
                  ["Objectives", "What will change?", "Activities mistaken for outcomes"],
                  ["Theory of change", "How does change happen?", "Missing logic"],
                  ["Activities &amp; plan", "What will you do?", "Unrealistic timeline"],
                  ["M&amp;E", "How will you know?", "No indicators"],
                  ["Budget", "What will it cost?", "Under-budgeted overheads"],
                  ["Sustainability", "What after the grant?", "Ignored entirely"]]},
         ]},

        {"type": "content", "label": "Problem Statement", "title": "The problem statement",
         "blocks": [
             {"t": "body", "html": "Open with the <strong>problem</strong>, not your "
              "organisation. State who is affected, how badly, and why it persists &mdash; backed "
              "by credible evidence (Census, NFHS, NSS, your own baseline). Make the funder feel "
              "the problem before you offer the solution."},
             {"t": "hbox", "color": "red", "html": "Weak: 'We are an NGO that does good work.' "
              "Strong: 'In these 40 villages, X% of children are out of school because Y &mdash; "
              "and here is what changes that.'"},
         ]},

        {"type": "content", "label": "Objectives", "title": "Objectives: specific and measurable",
         "blocks": [
             {"t": "body", "html": "Good objectives describe <strong>change</strong>, not "
              "busyness. 'Train 200 teachers' is an activity; 'improve Grade 3 reading levels in "
              "40 schools by one grade-level within two years' is an objective."},
             {"t": "hbox", "color": "cyan", "html": "A useful test: SMART &mdash; Specific, "
              "Measurable, Achievable, Relevant, Time-bound. If you cannot say how you would "
              "measure it, it is not yet an objective."},
         ]},

        {"type": "content", "label": "The Logic", "title": "Logframe &amp; theory of change",
         "blocks": [
             {"t": "flow", "steps": [
                 "INPUTS: money, staff, materials",
                 "ACTIVITIES: what you do",
                 "OUTPUTS: what you produce",
                 "OUTCOMES: what changes",
                 "IMPACT: the lasting difference"]},
             {"t": "hbox", "color": "amber", "html": "A <strong>logframe</strong> lays this out "
              "in a grid with indicators and assumptions; a <strong>theory of change</strong> "
              "explains <em>why</em> each arrow should hold. Funders want to see the logic, not "
              "just the list."},
         ]},

        {"type": "content", "label": "Outputs vs Outcomes", "title": "Outputs are not outcomes",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Output", "blocks": [
                  {"t": "body", "cls": "sm", "html": "What you produce: 500 women trained, 30 "
                   "wells built, 2,000 kits distributed. Countable, but not yet the point."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Outcome", "blocks": [
                  {"t": "body", "cls": "sm", "html": "What changes as a result: incomes rise, "
                   "disease falls, girls stay in school. This is what the funder is really "
                   "buying."}]}]},
             {"t": "hbox", "color": "red", "html": "Weak proposals count outputs and call it "
              "impact. Strong ones connect every output to the outcome it is meant to produce."},
         ]},

        {"type": "content", "label": "M&amp;E", "title": "Monitoring &amp; evaluation",
         "blocks": [
             {"t": "body", "html": "<strong>M&amp;E</strong> is how you and the funder will know "
              "whether the change happened. Each objective needs an indicator, a baseline, a "
              "target and a way to measure it &mdash; planned <em>before</em> the project starts, "
              "not bolted on at the end."},
             {"t": "hbox", "color": "cyan", "html": "Budget for M&amp;E and a baseline survey "
              "explicitly. A project with no way to measure success is a project the funder "
              "cannot trust."},
         ]},

        {"type": "content", "label": "Sustainability", "title": "What happens when the grant ends?",
         "blocks": [
             {"t": "body", "html": "Funders increasingly ask how the benefit will <strong>last</strong> "
              "beyond their money: community ownership, government adoption, earned income, or "
              "follow-on funding. A credible exit plan signals a serious organisation."},
             {"t": "hbox", "color": "amber", "html": "Be honest. A vague promise that 'the "
              "community will continue it' convinces no one. Name the specific mechanism that "
              "carries the work forward."},
         ]},

        {"type": "content", "label": "Craft", "title": "Writing that lands",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Follow the funder's format and word limits <strong>exactly</strong>",
                 "Lead with the problem and the change, not your history",
                 "Use evidence and one or two human stories &mdash; not a flood of jargon",
                 "Make the budget match the narrative, line for line",
                 "Have someone outside the project read it before you submit"]},
         ]},

        # ===================== SECTION 06 — Budgeting & Financial Basics (8) =============
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Budgeting &amp; Financial Basics"},

        {"type": "content", "label": "The Budget", "title": "The budget is a plan in numbers",
         "blocks": [
             {"t": "body", "html": "A project budget is your theory of change expressed in money "
              "&mdash; what each activity will cost and when. Funders read it closely: an "
              "unrealistic budget undermines an otherwise strong proposal."},
             {"t": "hbox", "color": "cyan", "html": "Two failures are equally damaging: padding "
              "the budget (loses trust) and under-budgeting (you cannot deliver, and you absorb "
              "the loss). Aim for honest and complete."},
         ]},

        {"type": "content", "label": "Cost Types", "title": "Direct vs indirect costs",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Direct costs", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Tied to the project: field staff salaries, "
                   "training materials, travel, beneficiary supplies. Easy to attribute and to "
                   "fund."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Indirect / overhead", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Shared running costs: rent, finance and "
                   "admin staff, audit, IT, electricity. Real and essential &mdash; but often "
                   "resisted by funders."}]}]},
             {"t": "hbox", "color": "amber", "html": "Indirect costs are not waste. They are the "
              "infrastructure that makes every direct activity possible."},
         ]},

        {"type": "content", "label": "Overheads", "title": "Why overheads are real costs",
         "blocks": [
             {"t": "body", "html": "Without finance staff, no clean accounts. Without an audit, "
              "no compliance. Without rent and IT, no office. <strong>Overheads</strong> are the "
              "skeleton that holds programmes up &mdash; yet many funders cap or refuse them."},
             {"t": "quote",
              "text": "You cannot run a serious organisation on a budget that pretends it has no "
              "running costs.",
              "attr": "&mdash; a widely shared frustration in the sector"},
         ]},

        {"type": "content", "label": "Starvation Cycle", "title": "The nonprofit starvation cycle",
         "blocks": [
             {"t": "flow", "steps": [
                 "Funders pressure NGOs to show low overheads",
                 "NGOs under-report and under-invest in core systems",
                 "Weak systems &mdash; staff, finance, IT &mdash; underperform",
                 "Funders see weakness, demand even leaner overheads",
                 "The cycle repeats, hollowing out the organisation"]},
             {"t": "hbox", "color": "red", "html": "The <strong>'starvation cycle'</strong> "
              "starves NGOs of the very capacity they need to deliver. Breaking it starts with "
              "honestly costing &mdash; and defending &mdash; your overheads."},
         ]},

        {"type": "content", "label": "Cost of Fundraising", "title": "Fundraising itself costs money",
         "blocks": [
             {"t": "chart", "canvas": "costFRChart",
              "title": "Illustrative cost to raise ₹100 by channel (₹ spent)",
              "source": "Illustrative ranges &mdash; vary widely by organisation",
              "type": "bar",
              "data": {"labels": ["Major donors", "Institutional grants", "Legacy / bequest",
                                  "Monthly / regular giving", "Events", "New-donor acquisition"],
                       "datasets": [{"label": "₹ spent to raise ₹100",
                                     "data": [8, 12, 10, 20, 35, 55],
                                     "backgroundColor": ["#10B981", "#10B981", "#10B981",
                                                         "#F59E0B", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'₹ spent per ₹100 raised'}, min:0 } } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative only. Acquiring new donors is "
              "expensive; <em>keeping</em> them is cheap. The first gift rarely pays for itself "
              "&mdash; the second and tenth do."},
         ]},

        {"type": "content", "label": "Cost Recovery", "title": "Full cost recovery",
         "blocks": [
             {"t": "term", "word": "Full cost recovery",
              "def": "Pricing each project to recover both its direct costs and a fair share of "
              "the organisation's overheads &mdash; so delivering the project does not quietly "
              "drain the organisation's reserves."},
             {"t": "hbox", "color": "cyan", "html": "Calculate your true overhead rate and apply "
              "it to every budget. Winning a grant that loses you money is not a win."},
         ]},

        {"type": "content", "label": "Co-funding", "title": "Co-funding &amp; matching",
         "blocks": [
             {"t": "body", "html": "Many funders require <strong>co-funding</strong> &mdash; a "
              "share of the budget from other sources &mdash; to share risk and confirm wider "
              "support. Others offer <strong>matching</strong>, doubling each rupee you raise "
              "elsewhere."},
             {"t": "hbox", "color": "green", "html": "Co-funding is leverage: one committed "
              "funder makes it easier to win the next. Sequence your asks so early wins unlock "
              "later ones."},
         ]},

        {"type": "content", "label": "Financial Health", "title": "Numbers funders check",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Reserves:</strong> can you survive a few months with no new money?",
                 "<strong>Audited accounts:</strong> clean, timely, externally verified",
                 "<strong>Programme-to-cost ratio:</strong> how much reaches the mission",
                 "<strong>Cash flow:</strong> can you bridge delayed grant payments?"]},
             {"t": "hbox", "color": "cyan", "html": "Strong, transparent finances are themselves "
              "a fundraising asset. Funders give to organisations that can clearly account for "
              "every rupee."},
         ]},

        # ===================== SECTION 07 — Individual Giving & Relationships (7) ========
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Individual Giving &amp; Relationships"},

        {"type": "content", "label": "Why Individuals", "title": "The case for individual giving",
         "blocks": [
             {"t": "body", "html": "Individual donors give the funding NGOs prize most: "
              "<strong>unrestricted, loyal and renewable</strong>. A base of committed individual "
              "givers is the closest an NGO comes to true financial independence."},
             {"t": "hbox", "color": "green", "html": "Grants and CSR come and go with priorities "
              "and budgets. A loyal individual donor base is yours &mdash; built slowly, but "
              "uniquely resilient."},
         ]},

        {"type": "content", "label": "Acquire vs Retain", "title": "Acquisition vs retention",
         "blocks": [
             {"t": "chart", "canvas": "acqRetChart",
              "title": "Illustrative: cost to acquire a new donor vs retain an existing one",
              "source": "Illustrative &mdash; relative costs, not real figures",
              "type": "bar",
              "data": {"labels": ["Acquire a new donor", "Retain an existing donor"],
                       "datasets": [{"label": "Relative cost",
                                     "data": [100, 20],
                                     "backgroundColor": ["#EF4444", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Relative cost (indexed)'}, min:0 } } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative. Acquiring a donor costs far "
              "more than keeping one. Organisations that pour everything into acquisition and "
              "neglect retention run to stand still."},
         ]},

        {"type": "content", "label": "Lifetime Value", "title": "Donor lifetime value",
         "blocks": [
             {"t": "term", "word": "Donor lifetime value (LTV)",
              "def": "The total amount a donor is likely to give across the whole span of their "
              "relationship with you &mdash; not just their first gift. It reframes a small first "
              "donation as the start of a long, valuable partnership."},
             {"t": "hbox", "color": "cyan", "html": "A ₹500 first-time donor who gives monthly "
              "for ten years is worth far more than a one-off ₹5,000 gift. Invest in the "
              "relationship, not just the transaction."},
         ]},

        {"type": "content", "label": "Stewardship", "title": "The thank-you is the next ask",
         "blocks": [
             {"t": "bullets", "items": [
                 "Thank <strong>promptly</strong> &mdash; within days, warmly and personally",
                 "Show the donor the <strong>impact</strong> of their specific gift",
                 "Communicate between asks, not only when you need money",
                 "Make them feel like an insider, not a wallet"]},
             {"t": "hbox", "color": "green", "html": "Retention is built on gratitude and "
              "transparency. A donor who feels seen and informed gives again &mdash; and brings "
              "others."},
         ]},

        {"type": "content", "label": "Monthly Giving", "title": "Monthly giving: the steady engine",
         "blocks": [
             {"t": "body", "html": "<strong>Monthly (recurring) donors</strong> are the most "
              "valuable individual givers: predictable income, low servicing cost, and high "
              "lifetime value. A growing monthly base smooths the cash-flow shocks that plague "
              "grant-dependent NGOs."},
             {"t": "hbox", "color": "cyan", "html": "Convert one-off donors into monthly ones, "
              "and keep churn low. A stable recurring base is the single most stabilising thing "
              "individual fundraising can build."},
         ]},

        {"type": "content", "label": "Major Donors", "title": "Major donors: depth over breadth",
         "blocks": [
             {"t": "body", "html": "A small number of <strong>major donors</strong> can provide "
              "a large share of individual income. They need personal cultivation, tailored "
              "proposals, direct access to leadership, and bespoke stewardship &mdash; closer to "
              "institutional fundraising than to a mass appeal."},
             {"t": "hbox", "color": "amber", "html": "Major-donor work is high-touch and "
              "patient. One strong relationship, carefully built over years, can transform an "
              "organisation's finances."},
         ]},

        {"type": "content", "label": "Storytelling", "title": "Story moves the individual gift",
         "blocks": [
             {"t": "body", "html": "Institutions respond to evidence; individuals respond to "
              "<strong>story</strong>. One real, specific human story &mdash; told with dignity "
              "and consent &mdash; moves more individual gifts than a page of statistics."},
             {"t": "hbox", "color": "red", "html": "But story has limits and ethics. We return "
              "to the duty of dignity &mdash; never 'poverty porn' &mdash; in the final section."},
         ]},

        # ===================== SECTION 08 — CSR in India (8) =============================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "CSR in India"},

        {"type": "content", "label": "The Law", "title": "Mandatory CSR: the Companies Act, 2013",
         "blocks": [
             {"t": "body", "html": "India was among the first countries to make corporate giving "
              "a legal duty. <strong>Section 135 of the Companies Act, 2013</strong> requires "
              "qualifying companies to spend on social causes &mdash; creating a major, distinctly "
              "Indian funding stream for NGOs."},
             {"t": "hbox", "color": "cyan", "html": "For Indian NGOs, CSR is often the largest "
              "domestic institutional source. Understanding the rules is essential to accessing "
              "it well."},
         ]},

        {"type": "content", "label": "Section 135", "title": "The ~2% rule",
         "blocks": [
             {"t": "body", "html": "Companies meeting prescribed thresholds of net worth, "
              "turnover or net profit must spend at least <strong>2% of their average net "
              "profits of the preceding three financial years</strong> on CSR activities."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "~2%", "label": "of average net profit (preceding 3 years) to be spent",
                  "color": "cyan", "source": "Companies Act 2013, Sec. 135"},
                 {"num": "3 years", "label": "the averaging window for net profit", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Confirm current thresholds and rules in the "
              "Act and CSR Rules before advising a company &mdash; the figures define who must "
              "spend and how much."},
         ]},

        {"type": "content", "label": "Who Must Spend", "title": "Which companies the rule covers",
         "blocks": [
             {"t": "body", "html": "Section 135 applies to companies that cross any of the "
              "prescribed thresholds of <strong>net worth, turnover or net profit</strong> in a "
              "financial year. Companies below all thresholds are not bound by the mandate."},
             {"t": "hbox", "color": "cyan", "html": "In practice this captures large companies. "
              "When prospecting CSR, target firms clearly above the thresholds &mdash; they have "
              "a legal obligation to spend and a board committee to direct it."},
         ]},

        {"type": "content", "label": "Schedule VII", "title": "Schedule VII: permitted activities",
         "blocks": [
             {"t": "body", "html": "CSR funds may only be spent on activities listed in "
              "<strong>Schedule VII</strong> of the Act &mdash; a defined menu of permitted "
              "social purposes."},
             {"t": "bullets", "sm": True, "items": [
                 "Eradicating hunger, poverty &amp; malnutrition; healthcare; sanitation",
                 "Promoting education and vocational skills",
                 "Gender equality and empowering women",
                 "Environmental sustainability and conservation",
                 "Rural development and other listed purposes"]},
             {"t": "hbox", "color": "red", "html": "If your project does not map to a Schedule "
              "VII head, a company cannot fund it from CSR. Frame proposals to fit the schedule "
              "explicitly."},
         ]},

        {"type": "content", "label": "CSR-1", "title": "CSR-1 registration",
         "blocks": [
             {"t": "body", "html": "To receive CSR funds, an implementing NGO must register with "
              "the Ministry of Corporate Affairs and obtain a <strong>CSR-1 registration number "
              "(Form CSR-1)</strong>. Without it, a company generally cannot route CSR money to "
              "your organisation."},
             {"t": "hbox", "color": "amber", "html": "Treat CSR-1 as a basic eligibility "
              "credential &mdash; alongside 12A and 80G. Get it in place before you approach "
              "companies, not after they say yes."},
         ]},

        {"type": "content", "label": "Illustrative Mix", "title": "Where CSR money tends to go",
         "blocks": [
             {"t": "chart", "canvas": "csrSectorChart",
              "title": "Illustrative split of CSR spend by sector",
              "source": "Illustrative pattern &mdash; not official figures",
              "type": "bar",
              "data": {"labels": ["Education", "Health &amp; sanitation", "Rural development",
                                  "Environment", "Livelihoods", "Other"],
                       "datasets": [{"label": "Share of CSR spend (%)",
                                     "data": [32, 26, 14, 10, 10, 8],
                                     "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}}, scales:{ x:{ title:{display:true,text:'Illustrative % of CSR spend'}, min:0 } } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative only. Education and health "
              "consistently attract large shares of CSR &mdash; useful to know, but confirm "
              "current patterns from published CSR data before relying on them."},
         ]},

        {"type": "content", "label": "Winning CSR", "title": "What companies look for in a partner",
         "blocks": [
             {"t": "bullets", "items": [
                 "Valid registrations &mdash; <strong>CSR-1, 12A, 80G</strong>",
                 "A track record they can verify and visit",
                 "Clean finances, audits and the ability to report rigorously",
                 "Alignment with the company's chosen Schedule VII theme and geography",
                 "Measurable outcomes the company can showcase to its board"]},
             {"t": "hbox", "color": "cyan", "html": "Companies are accountable to their boards "
              "for CSR spend. Make it easy for them to choose you &mdash; and to defend that "
              "choice."},
         ]},

        {"type": "content", "label": "Cautions", "title": "CSR is not a blank cheque",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "CSR is restricted to Schedule VII &mdash; not general core funding",
                 "Activities benefiting only employees do not count as CSR",
                 "Companies often want visible, brandable, short-cycle projects",
                 "Reporting and utilisation rules are strict &mdash; comply precisely"]},
             {"t": "hbox", "color": "amber", "html": "Manage the relationship as a true "
              "partnership &mdash; not a transaction &mdash; while protecting your mission from "
              "being reshaped purely for corporate visibility."},
         ]},

        # ===================== SECTION 09 — Compliance & Accountability (8) ==============
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Compliance &amp; Accountability"},

        {"type": "content", "label": "Why It Matters", "title": "Compliance is fundraising infrastructure",
         "blocks": [
             {"t": "body", "html": "The right legal registrations are not bureaucratic "
              "box-ticking &mdash; they are <strong>eligibility</strong>. Without them you cannot "
              "offer donors tax benefits, receive CSR, or accept foreign funds. Compliance "
              "unlocks fundraising."},
             {"t": "hbox", "color": "red", "html": "Disclaimer: this is an orientation, not legal "
              "advice. Rules change and details matter &mdash; always confirm with a qualified "
              "professional and the current statute."},
         ]},

        {"type": "content", "label": "12A", "title": "12A: income-tax exemption for the NGO",
         "blocks": [
             {"t": "term", "word": "12A registration",
              "def": "Registration under Section 12A (now 12AB) of the Income-tax Act that gives "
              "a charitable organisation exemption from income tax on its income, provided that "
              "income is applied to its charitable objects."},
             {"t": "hbox", "color": "cyan", "html": "12A protects <em>your</em> money: without "
              "it, your grants and donations could be taxed as income. It is a foundational "
              "registration for any NGO."},
         ]},

        {"type": "content", "label": "80G", "title": "80G: tax deduction for the donor",
         "blocks": [
             {"t": "term", "word": "80G registration",
              "def": "Registration under Section 80G of the Income-tax Act that lets <em>donors</em> "
              "claim a deduction on their taxable income for gifts made to your organisation."},
             {"t": "hbox", "color": "green", "html": "80G benefits the donor, not you &mdash; "
              "but that benefit is a powerful incentive to give. Display your 80G status clearly "
              "in every individual appeal."},
         ]},

        {"type": "content", "label": "12A vs 80G", "title": "Two registrations, two beneficiaries",
         "blocks": [
             {"t": "table",
              "head": ["", "12A / 12AB", "80G"],
              "rows": [
                  ["Benefits", "The NGO", "The donor"],
                  ["Effect", "NGO income exempt from tax", "Donor gets a deduction"],
                  ["Why fundraise without it?", "Income may be taxed", "Donors lose an incentive"],
                  ["Needed for CSR / FCRA", "Yes, typically", "Strengthens individual appeals"]]},
             {"t": "hbox", "color": "cyan", "html": "Most NGOs pursue both together. 12A keeps "
              "your income untaxed; 80G makes giving more attractive to donors."},
         ]},

        {"type": "content", "label": "FCRA", "title": "FCRA: foreign contributions",
         "blocks": [
             {"t": "term", "word": "FCRA",
              "def": "The Foreign Contribution (Regulation) Act &mdash; the law governing the "
              "receipt and use of foreign donations by organisations in India. An organisation "
              "must hold valid FCRA registration (or prior permission) to accept foreign funds."},
             {"t": "hbox", "color": "red", "html": "Accepting foreign money without valid FCRA "
              "status is a serious offence. If any of your funding originates abroad, FCRA "
              "compliance is non-negotiable."},
         ]},

        {"type": "content", "label": "FCRA 2020", "title": "The FCRA amendment of 2020",
         "blocks": [
             {"t": "body", "html": "The <strong>2020 amendment</strong> tightened the regime "
              "significantly. Two changes matter most for fundraisers:"},
             {"t": "bullets", "color": "amber", "items": [
                 "<strong>No sub-granting:</strong> an FCRA holder can no longer transfer "
                 "foreign funds to another organisation",
                 "<strong>Designated account:</strong> foreign contributions must first be "
                 "received in a designated <strong>SBI New Delhi (Main Branch)</strong> FCRA "
                 "account"]},
             {"t": "hbox", "color": "red", "html": "The no-sub-granting rule reshaped many "
              "partnership and intermediary models. If your model relied on passing on foreign "
              "funds, rethink it &mdash; with legal advice."},
         ]},

        {"type": "content", "label": "Transparency", "title": "Accountability is a two-way street",
         "blocks": [
             {"t": "body", "html": "Compliance satisfies the regulator; <strong>transparency</strong> "
              "earns trust. Beyond statutory filings, accountable NGOs publish what they raise, "
              "how they spend it, and what it achieved &mdash; to donors and to communities."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Audited annual accounts and an annual report",
                 "Honest reporting of both successes and failures",
                 "Accountability to communities, not only to funders"]},
         ]},

        {"type": "content", "label": "Compliance Calendar", "title": "Keep a compliance calendar",
         "blocks": [
             {"t": "bullets", "items": [
                 "Annual audit and filing of returns on time",
                 "FCRA annual return and quarterly disclosures, where applicable",
                 "Renewals of FCRA, 80G and 12A before they lapse",
                 "CSR utilisation reports to corporate partners"]},
             {"t": "hbox", "color": "red", "html": "A lapsed registration can freeze your "
              "funding overnight. Track every deadline &mdash; in fundraising, compliance and "
              "income are inseparable."},
         ]},

        # ===================== SECTION 10 — Diversification & Sustainability (8) =========
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Diversification &amp; Sustainability"},

        {"type": "content", "label": "The Risk", "title": "Single-donor dependence is fragile",
         "blocks": [
             {"t": "body", "html": "An organisation that draws most of its income from one funder "
              "is one decision away from crisis. When that funder changes priorities, the "
              "programme &mdash; and the people it serves &mdash; collapse with it."},
             {"t": "hbox", "color": "red", "html": "A useful warning sign: if any single donor "
              "provides a large share of your income, you have a concentration risk that needs a "
              "deliberate plan to reduce."},
         ]},

        {"type": "content", "label": "The Fix", "title": "Diversification is resilience",
         "blocks": [
             {"t": "body", "html": "<strong>Diversification</strong> spreads income across "
              "several sources &mdash; grants, CSR, individuals, government, earned income &mdash; "
              "so that losing any one does not threaten the mission. It is the single most "
              "important sustainability strategy."},
             {"t": "hbox", "color": "green", "html": "Diversification trades a little efficiency "
              "for a lot of resilience. A messier funding mix is a safer one."},
         ]},

        {"type": "content", "label": "Balance", "title": "Two failure modes of the funding mix",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Too concentrated", "blocks": [
                  {"t": "body", "cls": "sm", "html": "One or two funders dominate. Efficient "
                   "today, catastrophic the day they leave. The classic NGO failure."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Too scattered", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Dozens of tiny grants, each with its own "
                   "rules and reports. Resilient, but the reporting burden can swallow the "
                   "organisation."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Aim for the middle: several meaningful "
              "sources, none dominant, each worth the cost of servicing it."},
         ]},

        {"type": "content", "label": "Reserves", "title": "Reserves: the cushion that buys time",
         "blocks": [
             {"t": "body", "html": "<strong>Reserves</strong> &mdash; unrestricted funds set "
              "aside &mdash; let an organisation survive a delayed grant, a lost funder or an "
              "emergency without laying off staff or abandoning communities mid-project."},
             {"t": "hbox", "color": "green", "html": "Many advise building reserves covering "
              "several months of core costs. Reserves are not hoarding &mdash; they are the "
              "difference between a setback and a shutdown."},
         ]},

        {"type": "content", "label": "Unrestricted", "title": "Chase unrestricted income deliberately",
         "blocks": [
             {"t": "body", "html": "Sustainability depends on <strong>unrestricted</strong> "
              "income &mdash; the money that builds reserves, covers overheads and funds the "
              "gaps grants ignore. Individual giving and earned income are its main sources."},
             {"t": "hbox", "color": "cyan", "html": "Set an explicit target for the share of "
              "income that is unrestricted, and grow it year on year. It is the truest measure "
              "of financial freedom."},
         ]},

        {"type": "content", "label": "Earned Income", "title": "Earned income for stability",
         "blocks": [
             {"t": "body", "html": "Fees for training, consultancy, certified services or the "
              "sale of products can give an NGO income it controls &mdash; reducing dependence on "
              "any external funder and growing with the organisation."},
             {"t": "hbox", "color": "red", "html": "But earned income carries commercial risk "
              "and tax and regulatory implications. Build it carefully, as one diversified "
              "stream &mdash; never as a substitute for mission discipline."},
         ]},

        {"type": "content", "label": "Plan", "title": "Building a diversification plan",
         "blocks": [
             {"t": "flow", "steps": [
                 "MAP: your current income by source &amp; concentration",
                 "TARGET: a healthier future mix",
                 "INVEST: in the streams you lack (e.g. individuals)",
                 "SEQUENCE: realistic year-by-year shifts",
                 "REVIEW: track the mix every year"]},
             {"t": "hbox", "color": "amber", "html": "Diversification is a multi-year project, "
              "not a campaign. Building an individual-donor base or an earned-income line takes "
              "patience and upfront investment."},
         ]},

        {"type": "content", "label": "Sustainability", "title": "Sustainability is bigger than money",
         "blocks": [
             {"t": "body", "html": "True sustainability is not only a stable budget. It is "
              "capable staff, strong systems, community ownership and a clear mission &mdash; the "
              "things that let impact outlast any single grant or leader."},
             {"t": "hbox", "color": "green", "html": "Fundraising serves sustainability; it is "
              "not the same as it. Build the organisation, not just the next year's income."},
         ]},

        # ===================== SECTION 11 — Ethics, Practice & Further Reading (7) =======
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Ethics, Practice &amp; Further Reading"},

        {"type": "content", "label": "Dignity", "title": "Dignity in storytelling",
         "blocks": [
             {"t": "body", "html": "Fundraising runs on stories &mdash; and stories carry power "
              "over the people in them. The first ethical duty is to tell those stories with "
              "<strong>dignity</strong>: as agents of their own lives, not as objects of pity."},
             {"t": "quote",
              "text": "Show people as protagonists of their own story, not as proof of your "
              "compassion.",
              "attr": "&mdash; a principle of ethical communications"},
         ]},

        {"type": "content", "label": "Poverty Porn", "title": "No 'poverty porn'",
         "blocks": [
             {"t": "term", "word": "Poverty porn",
              "def": "Imagery or storytelling that exploits people's suffering &mdash; "
              "exaggerated misery, helplessness and humiliation &mdash; to trigger guilt and "
              "donations, while stripping the subject of agency and dignity."},
             {"t": "bullets", "sm": True, "color": "red", "items": [
                 "It dehumanises the people you claim to serve",
                 "It may raise money short-term but corrodes trust and self-respect",
                 "It reinforces stereotypes of helpless 'beneficiaries'"]},
         ]},

        {"type": "content", "label": "Consent", "title": "Informed consent for every story",
         "blocks": [
             {"t": "bullets", "items": [
                 "Get genuine, <strong>informed consent</strong> to use a person's image or story",
                 "Explain where and how it will be used &mdash; and let them decline",
                 "Protect identity where there is any risk of harm",
                 "Be honest: no staged scenes, no fabricated suffering"]},
             {"t": "hbox", "color": "amber", "html": "A signature on a release form is not "
              "consent if the person did not understand what they were agreeing to. The duty is "
              "to comprehension, not paperwork."},
         ]},

        {"type": "content", "label": "Two Accountabilities", "title": "Donor vs community accountability",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Upward (to donors)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Reports, audits, results, value for money. "
                   "Necessary &mdash; and loud, because donors hold the purse."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Downward (to community)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Listening, responsiveness, honesty, "
                   "sharing power. Just as important &mdash; and easily neglected, because "
                   "communities hold no cheque."}]}]},
             {"t": "hbox", "color": "red", "html": "The ethical challenge: do not let "
              "accountability to funders crowd out accountability to the people you exist to "
              "serve. Balance both, deliberately."},
         ]},

        {"type": "content", "label": "Ethical Lines", "title": "Lines a fundraiser should not cross",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "No misleading claims, inflated numbers or invented results",
                 "No exploiting suffering, fear or guilt to manipulate gifts",
                 "No accepting money whose conditions betray the mission",
                 "No pressure tactics that override a donor's free choice",
                 "No quiet sale or misuse of donor or community data"]},
             {"t": "hbox", "color": "cyan", "html": "Many countries have a fundraisers' code of "
              "ethics. Adopt one, write your own principles, and hold the whole team to them."},
         ]},

        {"type": "content", "label": "Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Mission first</strong> &mdash; money is the means, never the point",
                 "<strong>Relationships, not transactions</strong> &mdash; people give to trust",
                 "<strong>Diversify</strong> &mdash; never depend on a single donor",
                 "<strong>Get compliance right</strong> &mdash; CSR-1, 12A, 80G, FCRA",
                 "<strong>Tell stories with dignity</strong> &mdash; never 'poverty porn'"]},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "Further reading &amp; resources",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<strong>Companies Act, 2013 &amp; CSR Rules</strong> &mdash; the primary source on CSR",
                 "<strong>FCRA, 2010 (as amended 2020)</strong> &mdash; for any foreign funding",
                 "<strong>Income-tax Act, Sections 12A/12AB &amp; 80G</strong> &mdash; registrations",
                 "<em>The Fundraising Reader</em> and AFP / Hank Rosso on fundraising principles",
                 "Indian platforms: GiveIndia, Ketto, Milaap &mdash; for digital giving"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Nonprofit Management</strong>, <strong>Monitoring &amp; Evaluation</strong> "
              "and <strong>Financial Management</strong> 101 courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Fundraising Basics 101 &middot; Complete",
         "headline": "Now go build<br>a funding base that lasts.",
         "byline": "Fundraising is mission made possible &mdash; relationships, not transactions; "
                   "diversified, compliant and ethical. Explore the rest of the ImpactMojo 101 "
                   "Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
