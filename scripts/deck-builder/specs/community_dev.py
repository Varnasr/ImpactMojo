# -*- coding: utf-8 -*-
"""
Community Development 101 — ImpactMojo 101 Series (native deck spec)
Foundations of community development practice for South Asian practitioners.
Build: python3 scripts/deck-builder/build.py community_dev
"""

DECK = {
    "slug": "community-dev",
    "title": "Community Development 101",
    "description": ("Community Development 101 — a free foundational course for development "
                    "practitioners in South Asia. Participation, empowerment, asset-based "
                    "approaches, community organising, participatory tools, self-help groups, "
                    "power and elite capture, sustainability and panchayati raj — from Arnstein "
                    "and Chambers to Ostrom and India's DAY-NRLM. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Community<br>Development<br>101",
         "sub": "Participation, Power &amp; Self-Reliance &mdash; a Foundational Course on "
                "Working <em>with</em> Communities for Practitioners in South Asia",
         "tags": ["Practice-Grounded", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Community Development Is"},
             {"name": "Principles &amp; Values"},
             {"name": "Participation &amp; Its Ladder"},
             {"name": "Asset-Based Community Development"},
             {"name": "Community Organising &amp; Mobilisation"},
             {"name": "Participatory Tools (PRA / PLA)"},
             {"name": "Self-Help Groups &amp; Collective Action"},
             {"name": "Power, Conflict &amp; Elite Capture"},
             {"name": "Sustainability, Ownership &amp; Exit"},
             {"name": "Community Development in South Asia"},
             {"name": "Practice &amp; Pitfalls"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Community Development Is"},

        {"type": "content", "label": "Definition", "title": "Development done with, not to, people",
         "blocks": [
             {"t": "body", "html": "<strong>Community development</strong> is a process by which "
              "people who share a place or condition act together to shape the decisions that "
              "affect their lives &mdash; building their collective capacity, organisation and "
              "voice along the way. The point is not only the road or the well; it is the "
              "<em>capability to act</em> that the community keeps afterwards."},
             {"t": "term", "word": "Community development",
              "def": "A process and an outcome: people working collectively to identify their "
              "own needs and act on them, strengthening relationships, leadership and "
              "self-reliance &mdash; not simply delivering goods to passive recipients."},
             {"t": "hbox", "color": "cyan", "html": "Test of good practice: when the project "
              "ends, is the community <em>more</em> able to act on its own future than before? "
              "If not, something was delivered, but little was developed."},
         ]},

        {"type": "content", "label": "Service vs Development", "title": "Delivering a service is not developing a community",
         "blocks": [
             {"t": "table",
              "head": ["", "Service delivery", "Community development"],
              "rows": [
                  ["Sees people as", "Beneficiaries / recipients", "Actors / decision-makers"],
                  ["Defines the problem", "The agency", "The community"],
                  ["Measure of success", "Outputs delivered", "Capacity &amp; voice built"],
                  ["When it ends", "Flow of goods stops", "People keep acting"],
                  ["Main risk", "Dependency", "Slow, hard to count"]],},
             {"t": "hbox", "color": "amber", "html": "Both have a place. The error is calling a "
              "service-delivery project 'community development' &mdash; and being surprised when "
              "nothing self-sustains."},
         ]},

        {"type": "content", "label": "The Contested Word", "title": "'Community' is not as simple as it sounds",
         "blocks": [
             {"t": "body", "html": "We speak of 'the community' as if it were one thing with one "
              "voice. In reality a village is layered by <strong>caste, class, gender, religion, "
              "age and faction</strong> &mdash; with unequal power and conflicting interests."},
             {"t": "bullets", "color": "red", "sm": True, "items": [
                 "There is rarely a single 'community interest' &mdash; there are interests",
                 "Who claims to speak <em>for</em> the community is itself a question of power",
                 "Romanticising 'the community' can hide who is being excluded within it"]},
             {"t": "hbox", "color": "indigo", "html": "Practitioner habit: never say 'the "
              "community wants&hellip;' without asking <em>which</em> part, and who was in the "
              "room when it was decided."},
         ]},

        {"type": "content", "label": "Many Meanings", "title": "Three senses of 'community'",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Place", "label": "People sharing a location &mdash; a village, ward, "
                  "basti or hamlet", "color": "cyan"},
                 {"num": "Identity", "label": "People sharing a trait &mdash; caste, faith, "
                  "occupation, disability, gender", "color": "indigo"},
                 {"num": "Interest", "label": "People sharing a concern &mdash; water users, "
                  "forest dwellers, weavers", "color": "green"}]},
             {"t": "body", "cls": "sm", "html": "These overlap and cut across each other. A single "
              "village holds several identity and interest communities at once &mdash; which is "
              "exactly why 'the community' can never be assumed to be unified."},
         ]},

        {"type": "content", "label": "Two Directions", "title": "Endogenous vs exogenous change",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Endogenous (from within)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Change driven by the community's own "
                   "priorities, knowledge and resources. The outsider supports; the community "
                   "leads. Slower, but owned &mdash; and durable."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Exogenous (from outside)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Change introduced by an external agency, "
                   "scheme or expert. Faster and well-resourced &mdash; but easily resented, "
                   "poorly fitted, and prone to collapse when funding leaves."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Most real work blends the two. The craft is "
              "to bring outside resources <em>in service of</em> an inside agenda &mdash; not to "
              "substitute the agency's plan for the community's."},
         ]},

        {"type": "content", "label": "A Short History", "title": "Where the idea comes from",
         "blocks": [
             {"t": "flow", "steps": [
                 "Colonial 'rural reconstruction' &amp; welfare",
                 "1950s state-led Community Development Programme (India, 1952)",
                 "1970s critique: top-down, elite-captured",
                 "Participation, empowerment &amp; rights-based approaches"]},
             {"t": "body", "cls": "sm", "html": "India launched a national Community Development "
              "Programme in 1952. Its mixed record &mdash; impressive in reach, weak in genuine "
              "participation &mdash; shaped the participatory turn that followed."},
         ]},

        {"type": "content", "label": "The Shift", "title": "From 'beneficiary' to 'citizen'",
         "blocks": [
             {"t": "quote",
              "text": "The best way to help people is to help them help themselves.",
              "attr": "&mdash; a long-standing principle of community development practice"},
             {"t": "body", "html": "The language matters. A <em>beneficiary</em> receives; a "
              "<em>citizen</em> claims rights and holds the state to account. Community "
              "development at its best turns recipients of schemes into claimants of "
              "entitlements &mdash; and authors of their own plans."},
         ]},

        {"type": "content", "label": "The Outsider's Place", "title": "You are a guest in someone else's life",
         "blocks": [
             {"t": "body", "html": "Whoever you are &mdash; NGO worker, official, researcher "
              "&mdash; you enter the community as an <strong>outsider</strong>. The community will "
              "live with the consequences of every decision long after you have moved on to the "
              "next project."},
             {"t": "hbox", "color": "indigo", "html": "That asymmetry should breed humility, not "
              "authority. The people you work with are the experts on their own lives; your "
              "expertise is in process, connection and leverage &mdash; not in their reality."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Principles &amp; Values"},

        {"type": "content", "label": "The Compass", "title": "Values, not just techniques",
         "blocks": [
             {"t": "body", "html": "Community development is value-driven before it is "
              "technical. The tools (mapping, SHGs, meetings) mean little without the "
              "<strong>principles</strong> that decide who is in the room, who decides, and who "
              "benefits."},
             {"t": "stats", "cols": 5, "cards": [
                 {"num": "Participation", "label": "people shape decisions", "color": "cyan"},
                 {"num": "Empowerment", "label": "power grows from within", "color": "indigo"},
                 {"num": "Self-determination", "label": "communities choose", "color": "green"},
                 {"num": "Equity", "label": "the excluded come first", "color": "amber"},
                 {"num": "Sustainability", "label": "it outlasts the project", "color": "red"}]},
         ]},

        {"type": "content", "label": "Principle 1", "title": "Participation",
         "blocks": [
             {"t": "term", "word": "Participation",
              "def": "People affected by a decision taking an active part in making it &mdash; "
              "not merely being informed or consulted, but genuinely influencing the outcome."},
             {"t": "body", "html": "Participation is the bedrock principle, but it is also the "
              "most abused word in the sector. Calling a meeting is not participation if the "
              "decisions were already made. We return to <em>how</em> real it is in Section 3."},
         ]},

        {"type": "content", "label": "Principle 2", "title": "Empowerment",
         "blocks": [
             {"t": "term", "word": "Empowerment",
              "def": "The process by which people who lack power gain greater control over the "
              "decisions, resources and institutions that affect their lives &mdash; "
              "individually and collectively."},
             {"t": "hbox", "color": "amber", "html": "Empowerment is not something an agency "
              "<em>gives</em>. Power is taken, organised and exercised. The outsider can open "
              "space and remove barriers &mdash; but cannot hand over agency like a sack of rice."},
         ]},

        {"type": "content", "label": "Principle 3", "title": "Self-determination",
         "blocks": [
             {"t": "body", "html": "Communities have the right to set their own priorities &mdash; "
              "even when those priorities differ from the agency's logframe, the donor's theme, "
              "or the expert's view of what they 'should' want."},
             {"t": "hbox", "color": "red", "html": "The hard test: are you willing to support a "
              "community decision you disagree with? If the answer is always no, you are "
              "delivering your agenda, not enabling theirs."},
         ]},

        {"type": "content", "label": "Principle 4", "title": "Equity &amp; inclusion",
         "blocks": [
             {"t": "body", "html": "A village 'consensus' often reflects the voice of dominant "
              "caste, class and gender. Equity means deliberately reaching the people a normal "
              "process leaves out &mdash; Dalits, Adivasis, women, persons with disabilities, "
              "the landless."},
             {"t": "bullets", "color": "green", "sm": True, "items": [
                 "Equality treats everyone the same; equity gives more support where need is greater",
                 "Hold separate spaces so marginalised voices form before the big meeting",
                 "Ask of any outcome: who gained, who was absent, who paid?"]},
         ]},

        {"type": "content", "label": "Principle 5", "title": "Sustainability",
         "blocks": [
             {"t": "body", "html": "Sustainability is not only environmental. It asks whether the "
              "<strong>institution, the skills and the will</strong> survive after the project "
              "and its money depart."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Social", "label": "leadership &amp; organisation persist", "color": "cyan"},
                 {"num": "Financial", "label": "activity funds itself locally", "color": "green"},
                 {"num": "Ecological", "label": "the resource base is not depleted", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Working Values", "title": "How these values show up in conduct",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Respect:</strong> treat local knowledge as expertise, not ignorance",
                 "<strong>Humility:</strong> the outsider is a guest, not the hero of the story",
                 "<strong>Transparency:</strong> share budgets, plans and decisions openly",
                 "<strong>Accountability:</strong> answer to the community, not only the donor",
                 "<strong>Do no harm:</strong> never leave a community worse or more divided"]},
         ]},

        {"type": "content", "label": "A Caution", "title": "Values can become slogans",
         "blocks": [
             {"t": "quote",
              "text": "Participation has been used both to enable people and to manipulate them. "
              "The word alone guarantees nothing.",
              "attr": "&mdash; a recurring critique in participatory practice"},
             {"t": "hbox", "color": "indigo", "html": "Every principle in this section can be "
              "performed without being practised. The chapters that follow are about telling the "
              "difference &mdash; in the room, not on the poster."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Participation &amp; Its Ladder"},

        {"type": "content", "label": "The Question", "title": "Participation is a matter of degree",
         "blocks": [
             {"t": "body", "html": "Not all 'participation' is equal. Being told about a decision "
              "is participation of a kind &mdash; but so is making the decision. The gap between "
              "them is the gap between tokenism and power."},
             {"t": "hbox", "color": "cyan", "html": "The classic map of this gap is Sherry "
              "Arnstein's <strong>Ladder of Citizen Participation</strong> (1969) &mdash; eight "
              "rungs grouped into three levels."},
         ]},

        {"type": "content", "label": "Arnstein 1969", "title": "Arnstein's Ladder of Citizen Participation",
         "compact": True,
         "blocks": [
             {"t": "raw", "html": '''<div style="display:flex;justify-content:center;margin:6px 0">
<svg viewBox="0 0 760 360" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:760px;height:auto;font-family:inherit">
  <!-- level brackets -->
  <rect x="8" y="12" width="150" height="124" rx="6" fill="#10B981" opacity="0.14"/>
  <rect x="8" y="144" width="150" height="124" rx="6" fill="#F59E0B" opacity="0.14"/>
  <rect x="8" y="276" width="150" height="76" rx="6" fill="#EF4444" opacity="0.14"/>
  <text x="83" y="64" fill="#10B981" font-size="15" font-weight="700" text-anchor="middle">CITIZEN</text>
  <text x="83" y="84" fill="#10B981" font-size="15" font-weight="700" text-anchor="middle">POWER</text>
  <text x="83" y="200" fill="#F59E0B" font-size="15" font-weight="700" text-anchor="middle">TOKENISM</text>
  <text x="83" y="306" fill="#EF4444" font-size="14" font-weight="700" text-anchor="middle">NON-</text>
  <text x="83" y="324" fill="#EF4444" font-size="14" font-weight="700" text-anchor="middle">PARTICIPATION</text>
  <!-- rungs (top = most power) -->
  <g font-size="14" fill="#1C1917">
    <rect x="180" y="16" width="560" height="36" rx="5" fill="#10B981" opacity="0.9"/><text x="196" y="39" fill="#fff" font-weight="700">8 &#183; Citizen control</text>
    <rect x="180" y="60" width="560" height="36" rx="5" fill="#10B981" opacity="0.7"/><text x="196" y="83" fill="#fff" font-weight="700">7 &#183; Delegated power</text>
    <rect x="180" y="104" width="560" height="36" rx="5" fill="#10B981" opacity="0.5"/><text x="196" y="127" fill="#1C1917" font-weight="700">6 &#183; Partnership</text>
    <rect x="180" y="148" width="560" height="36" rx="5" fill="#F59E0B" opacity="0.85"/><text x="196" y="171" fill="#fff" font-weight="700">5 &#183; Placation</text>
    <rect x="180" y="192" width="560" height="36" rx="5" fill="#F59E0B" opacity="0.6"/><text x="196" y="215" fill="#1C1917" font-weight="700">4 &#183; Consultation</text>
    <rect x="180" y="236" width="560" height="36" rx="5" fill="#F59E0B" opacity="0.4"/><text x="196" y="259" fill="#1C1917" font-weight="700">3 &#183; Informing</text>
    <rect x="180" y="280" width="560" height="36" rx="5" fill="#EF4444" opacity="0.6"/><text x="196" y="303" fill="#fff" font-weight="700">2 &#183; Therapy</text>
    <rect x="180" y="324" width="560" height="34" rx="5" fill="#EF4444" opacity="0.85"/><text x="196" y="346" fill="#fff" font-weight="700">1 &#183; Manipulation</text>
  </g>
  <text x="752" y="20" fill="#0EA5E9" font-size="11" text-anchor="end">more power &#8593;</text>
</svg></div>''' },
             {"t": "body", "cls": "sm", "html": "Source: Sherry R. Arnstein, &lsquo;A Ladder of "
              "Citizen Participation&rsquo;, <em>Journal of the American Institute of Planners</em>, "
              "1969. Diagram illustrative."},
         ]},

        {"type": "content", "label": "The Three Levels", "title": "Non-participation, tokenism, citizen power",
         "blocks": [
             {"t": "twocol", "ratio": "a23",
              "left": [{"t": "panel", "color": "red", "title": "Non-participation", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>Manipulation &amp; Therapy.</strong> "
                   "Not participation at all &mdash; the aim is to 'educate' or pacify people, not "
                   "to share power."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Degrees of tokenism", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>Informing, Consultation, Placation.</strong> "
                   "People hear and are heard &mdash; but lack the power to ensure their views "
                   "change anything."}]}]},
             {"t": "panel", "color": "green", "title": "Degrees of citizen power", "blocks": [
                 {"t": "body", "cls": "sm", "html": "<strong>Partnership, Delegated power, Citizen "
                  "control.</strong> Real negotiating power and, at the top, genuine control over "
                  "decisions and resources."}]},
         ]},

        {"type": "content", "label": "The Trap", "title": "Tokenism wears participation's clothes",
         "blocks": [
             {"t": "body", "html": "The dangerous rungs are the middle ones. <strong>Consultation "
              "and placation</strong> look and feel participatory &mdash; meetings, feedback "
              "forms, a token seat on a committee &mdash; while power stays exactly where it was."},
             {"t": "hbox", "color": "red", "html": "Arnstein's sharp point: there is a critical "
              "difference between going through the empty <em>ritual</em> of participation and "
              "having the real <em>power</em> to affect the outcome."},
         ]},

        {"type": "content", "label": "Diagnose Your Own Work", "title": "Which rung are you really on?",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["What you did", "Looks like", "Actually is"],
              "rows": [
                  ["Held an awareness camp", "Participation", "Informing (rung 3)"],
                  ["Collected feedback, then decided anyway", "Consultation", "Tokenism (rung 4)"],
                  ["Gave the SHG a seat, but no vote", "Partnership", "Placation (rung 5)"],
                  ["Community jointly plans &amp; controls budget", "Real partnership", "Citizen power (6&ndash;8)"]],},
             {"t": "hbox", "color": "cyan", "html": "Be honest about the rung. Most projects sit "
              "lower than they claim &mdash; and that is the first thing to fix."},
         ]},

        {"type": "content", "label": "Hart's Ladder", "title": "Participation for children &amp; youth",
         "blocks": [
             {"t": "body", "html": "Roger Hart adapted Arnstein's ladder for <strong>children and "
              "young people</strong> (UNICEF, 1992). Its lower three rungs name forms of "
              "<em>false</em> participation that are especially common with youth."},
             {"t": "bullets", "color": "red", "sm": True, "items": [
                 "<strong>Manipulation:</strong> children used to carry adults' messages",
                 "<strong>Decoration:</strong> children present for show, not voice",
                 "<strong>Tokenism:</strong> a child on the panel who has no real say"]},
             {"t": "hbox", "color": "green", "html": "Hart's higher rungs run from adult-initiated "
              "but shared with children, up to child-initiated, shared decisions with adults "
              "&mdash; genuine youth agency."},
         ]},

        {"type": "content", "label": "Beyond the Ladder", "title": "Spaces, not just rungs",
         "blocks": [
             {"t": "body", "html": "Later thinkers noted a ladder implies more is always better. "
              "Sometimes a community rationally chooses to be merely <em>informed</em>. What "
              "matters is whether the level was <strong>chosen</strong> by the community or "
              "<strong>imposed</strong> on it."},
             {"t": "hbox", "color": "indigo", "html": "Ask not only 'how high on the ladder?' but "
              "'who decided how high to go, and who opened or closed the space?'"},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Asset-Based Community Development"},

        {"type": "content", "label": "A Flip", "title": "Start from strengths, not deficits",
         "blocks": [
             {"t": "body", "html": "Most planning starts with a <strong>needs assessment</strong>: "
              "a list of what is wrong, missing and broken. <strong>Asset-Based Community "
              "Development (ABCD)</strong> flips this &mdash; it begins by mapping what a "
              "community already <em>has</em>."},
             {"t": "hbox", "color": "cyan", "html": "Pioneered by John Kretzmann and John "
              "McKnight (Northwestern University, 1993) in <em>Building Communities from the "
              "Inside Out</em>."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "The deficit lens does quiet harm",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Needs-based lens", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Sees a map of problems and gaps",
                      "Makes the community a client",
                      "Hands the agency the power",
                      "Deepens dependency"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Asset-based lens", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Sees a map of capacities",
                      "Makes the community the agent",
                      "Starts with local power",
                      "Builds self-reliance"]}]}],},
             {"t": "hbox", "color": "amber", "html": "A community told only what it lacks learns "
              "to wait for outsiders. A community shown what it holds learns to act."},
         ]},

        {"type": "content", "label": "Kretzmann &amp; McKnight", "title": "What counts as an asset?",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Individuals", "label": "Skills, knowledge &amp; gifts of every resident "
                  "&mdash; including those usually 'written off'", "color": "cyan"},
                 {"num": "Associations", "label": "Informal groups &mdash; mahila mandals, youth "
                  "clubs, savings circles, temple committees", "color": "indigo"},
                 {"num": "Institutions", "label": "Schools, anganwadis, PHCs, banks, the "
                  "panchayat &mdash; local formal bodies", "color": "green"},
                 {"num": "Physical &amp; natural", "label": "Land, water, commons, buildings, "
                  "markets, infrastructure", "color": "amber"}]},
         ]},

        {"type": "content", "label": "The Tool", "title": "Asset mapping",
         "blocks": [
             {"t": "raw", "html": '''<div style="display:flex;justify-content:center;margin:4px 0">
<svg viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:720px;height:auto;font-family:inherit">
  <circle cx="360" cy="160" r="52" fill="#1C1917"/>
  <text x="360" y="156" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">COMMUNITY</text>
  <text x="360" y="174" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">ASSETS</text>
  <!-- four asset nodes -->
  <line x1="360" y1="160" x2="170" y2="70" stroke="#0EA5E9" stroke-width="2"/>
  <line x1="360" y1="160" x2="550" y2="70" stroke="#6366F1" stroke-width="2"/>
  <line x1="360" y1="160" x2="170" y2="250" stroke="#10B981" stroke-width="2"/>
  <line x1="360" y1="160" x2="550" y2="250" stroke="#F59E0B" stroke-width="2"/>
  <g text-anchor="middle">
    <circle cx="170" cy="70" r="44" fill="#0EA5E9"/><text x="170" y="66" fill="#fff" font-size="12" font-weight="700">Individuals</text><text x="170" y="82" fill="#fff" font-size="10">skills &amp; gifts</text>
    <circle cx="550" cy="70" r="44" fill="#6366F1"/><text x="550" y="66" fill="#fff" font-size="12" font-weight="700">Associations</text><text x="550" y="82" fill="#fff" font-size="10">local groups</text>
    <circle cx="170" cy="250" r="44" fill="#10B981"/><text x="170" y="246" fill="#fff" font-size="12" font-weight="700">Institutions</text><text x="170" y="262" fill="#fff" font-size="10">school, PHC</text>
    <circle cx="550" cy="250" r="44" fill="#F59E0B"/><text x="550" y="246" fill="#fff" font-size="12" font-weight="700">Natural</text><text x="550" y="262" fill="#fff" font-size="10">land, water</text>
  </g>
</svg></div>''' },
             {"t": "body", "cls": "sm", "html": "Walk the village together and place every "
              "capacity on a shared map. The act of mapping is itself empowering &mdash; people "
              "<em>see</em> their own wealth. (ABCD asset map, illustrative.)"},
         ]},

        {"type": "content", "label": "From Map to Action", "title": "Connect assets to one another",
         "blocks": [
             {"t": "flow", "steps": [
                 "MAP the gifts, groups, institutions &amp; resources",
                 "CONNECT assets that don't yet talk to each other",
                 "MOBILISE around a goal the community sets",
                 "LEVERAGE outside help only to fill genuine gaps"]},
             {"t": "hbox", "color": "green", "html": "The breakthrough is often not a new "
              "resource but a new <em>connection</em> &mdash; the retired teacher who starts "
              "coaching, the SHG that links to the bank."},
         ]},

        {"type": "content", "label": "Not Either / Or", "title": "Assets first &mdash; but needs are real",
         "blocks": [
             {"t": "body", "html": "ABCD is sometimes caricatured as ignoring genuine poverty and "
              "letting the state off the hook. Done well, it does neither: it starts from "
              "strengths <em>and</em> then claims the rights and services a community is owed."},
             {"t": "hbox", "color": "red", "html": "Watch-out: 'use your own assets' must never "
              "become an excuse for the state to withdraw. Asset-based does not mean "
              "self-financed."},
         ]},

        {"type": "content", "label": "In Practice", "title": "ABCD with an Indian SHG, illustrative",
         "blocks": [
             {"t": "chart", "canvas": "abcdAssetChart",
              "title": "Mapping one hamlet's assets before planning (illustrative count)",
              "source": "Illustrative example, not from a survey",
              "type": "bar",
              "data": {"labels": ["Skills &amp; gifts", "Local groups", "Institutions",
                                  "Natural / physical"],
                       "datasets": [{"label": "Assets identified",
                                     "data": [34, 9, 6, 12],
                                     "backgroundColor": ["#0EA5E9", "#6366F1", "#10B981", "#F59E0B"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true, title:{display:true,text:'count (illustrative)'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Communities are routinely surprised by how "
              "long the 'skills &amp; gifts' column is &mdash; the deficit lens had made it "
              "invisible."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Community Organising &amp; Mobilisation"},

        {"type": "content", "label": "Power", "title": "Organising is about building power",
         "blocks": [
             {"t": "body", "html": "Where development often asks 'how do we deliver services?', "
              "<strong>community organising</strong> asks 'how do people without power build "
              "enough of it to win change from those who have it?'"},
             {"t": "term", "word": "Community organising",
              "def": "Bringing people together around shared grievances to build collective power "
              "and act on their own behalf &mdash; negotiating, pressuring or demanding change "
              "from those who hold power."},
         ]},

        {"type": "content", "label": "Alinsky", "title": "Saul Alinsky and the organising tradition",
         "blocks": [
             {"t": "body", "html": "Saul Alinsky, the Chicago organiser whose <em>Rules for "
              "Radicals</em> (1971) shaped modern organising, insisted that lasting change comes "
              "from <strong>organised people</strong>, not goodwill or charity."},
             {"t": "quote",
              "text": "Change comes from power, and power comes from organisation.",
              "attr": "&mdash; Saul Alinsky, community organiser"},
         ]},

        {"type": "content", "label": "Mobilising vs Organising", "title": "A crowd is not an organisation",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Mobilising", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Turning people out for an event &mdash; a "
                   "rally, a gram sabha, a signature drive. Fast, visible &mdash; but it fades "
                   "when the event ends."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Organising", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Building durable structures, leaders and "
                   "relationships that act again and again. Slower &mdash; but it lasts beyond "
                   "any single campaign."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Mobilising spends power; organising builds "
              "it. Good practice mobilises <em>through</em> an organisation it is also building."},
         ]},

        {"type": "content", "label": "The Method", "title": "How organising actually works",
         "blocks": [
             {"t": "flow", "steps": [
                 "LISTEN: one-to-one conversations surface real grievances",
                 "IDENTIFY: a winnable, specific, felt issue",
                 "BUILD: leaders &amp; an organisation from within",
                 "ACT: collective action; negotiate or pressure",
                 "REFLECT: evaluate, then take on the next issue"]},
             {"t": "hbox", "color": "indigo", "html": "Alinsky's rule of thumb: pick issues that "
              "are <strong>immediate, specific and winnable</strong> &mdash; early wins build the "
              "confidence to tackle bigger fights."},
         ]},

        {"type": "content", "label": "Leadership", "title": "Leaders from within, not imported",
         "blocks": [
             {"t": "body", "html": "The organiser's job is to <strong>develop local leaders</strong> "
              "and then step back &mdash; not to become the indispensable leader themselves. The "
              "test of an organiser is what continues after they leave."},
             {"t": "quote",
              "text": "A good organiser works to make themselves unnecessary.",
              "attr": "&mdash; a maxim of the organising tradition"},
         ]},

        {"type": "content", "label": "Issue, Not Problem", "title": "Turning a problem into an issue",
         "blocks": [
             {"t": "body", "html": "A <strong>problem</strong> is a broad condition &mdash; "
              "'poverty', 'no water'. An <strong>issue</strong> is a specific, winnable handle on "
              "it &mdash; 'the panchayat must repair the handpump in Ward 4 before summer.'"},
             {"t": "hbox", "color": "green", "html": "Issues have a clear target, a clear ask and "
              "a clear deadline. They are how diffuse grievance becomes organised action."},
         ]},

        {"type": "content", "label": "South Asian Roots", "title": "The region's own organising traditions",
         "blocks": [
             {"t": "body", "html": "South Asia has deep home-grown traditions of collective "
              "action that long predate imported models &mdash; from Gandhian constructive work "
              "and the Bhoodan land-gift movement to SEWA's organising of informal women "
              "workers and the Right to Information campaign."},
             {"t": "hbox", "color": "amber", "html": "Borrow methods critically. The principles "
              "of organising travel; the tactics must fit local caste, gender and political "
              "realities &mdash; not be copied wholesale from elsewhere."},
         ]},

        {"type": "content", "label": "A Caution", "title": "Organising is not always the right tool",
         "blocks": [
             {"t": "body", "html": "Confrontational organising builds power &mdash; but it can "
              "also provoke backlash against the very people it aims to protect, especially where "
              "the marginalised are few and the powerful are entrenched."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Fits when", "blocks": [
                  {"t": "body", "cls": "sm", "html": "There is a clear adversary, a winnable "
                   "demand, and enough collective strength to withstand pushback."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Risky when", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The marginalised are isolated and exposed, "
                   "or where patient relationship-building would protect them better."}]}]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Participatory Tools (PRA / PLA)"},

        {"type": "content", "label": "Chambers", "title": "Handing the stick to the people",
         "blocks": [
             {"t": "body", "html": "<strong>Participatory Rural Appraisal (PRA)</strong> &mdash; "
              "later widened to <strong>Participatory Learning and Action (PLA)</strong> &mdash; "
              "is a family of methods for communities to analyse <em>their own</em> reality and "
              "plan action. It is most associated with Robert Chambers of IDS, Sussex."},
             {"t": "quote",
              "text": "Whose reality counts? Put the first last.",
              "attr": "&mdash; Robert Chambers, Institute of Development Studies"},
         ]},

        {"type": "content", "label": "The Reversal", "title": "From extracting data to enabling analysis",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Conventional survey", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Outsider asks questions, takes the data "
                   "away, analyses it elsewhere. Knowledge flows <em>out</em> of the community."}]}],
              "right": [{"t": "panel", "color": "green", "title": "PRA / PLA", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Community draws, ranks and analyses on the "
                   "ground; the outsider facilitates. Knowledge stays <em>in</em> the community."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Chambers' core shift: the outsider's role is "
              "to <strong>facilitate</strong>, not interrogate &mdash; 'hand over the stick' "
              "(and the chalk, and the map)."},
         ]},

        {"type": "content", "label": "The Toolkit", "title": "Core participatory tools",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tool", "What people do", "Reveals"],
              "rows": [
                  ["Social / resource map", "Draw the village on the ground", "Who lives where, what exists"],
                  ["Transect walk", "Walk a line across the village together", "Land use, problems, on-site detail"],
                  ["Seasonal calendar", "Chart the year's rhythm", "Hunger months, work, illness, cash flow"],
                  ["Wellbeing ranking", "Sort households by local criteria", "Who is poor, by whose definition"],
                  ["Venn diagram", "Circles for local institutions", "Which bodies matter, and to whom"],
                  ["Timeline / trend", "Recall change over years", "History, shocks, what shifted"]],},
         ]},

        {"type": "content", "label": "Mapping", "title": "Community mapping",
         "blocks": [
             {"t": "body", "html": "People draw their own village &mdash; on the ground with "
              "sticks, seeds and chalk, or on paper &mdash; marking households, water, fields, "
              "roads and facilities. A non-literate elder can map a watershed with total fluency."},
             {"t": "hbox", "color": "green", "html": "Mapping levels the room. It values local "
              "spatial knowledge over the outsider's literacy &mdash; and the map becomes a "
              "shared object everyone can argue over and improve."},
         ]},

        {"type": "content", "label": "Seasonality", "title": "Seasonal calendars",
         "blocks": [
             {"t": "body", "html": "A <strong>seasonal calendar</strong> plots the year across "
              "rows &mdash; rainfall, crops, work, food stocks, debt, migration, illness &mdash; "
              "revealing the rhythm of vulnerability that an annual average hides entirely."},
             {"t": "hbox", "color": "amber", "html": "The lean months between harvests &mdash; "
              "when food, cash and work all run thin at once &mdash; jump out of a seasonal "
              "calendar in a way a yearly figure never could."},
         ]},

        {"type": "content", "label": "Wellbeing Ranking", "title": "Who is poor &mdash; by whose definition?",
         "blocks": [
             {"t": "body", "html": "In <strong>wellbeing (or wealth) ranking</strong>, community "
              "members sort their own households into groups using <em>their own</em> criteria of "
              "what makes a household better or worse off."},
             {"t": "hbox", "color": "indigo", "html": "It often surfaces dimensions an income line "
              "misses &mdash; a widow with land but no labour, a family shamed by debt &mdash; and "
              "challenges official Below-Poverty-Line lists."},
         ]},

        {"type": "content", "label": "Cautions", "title": "PRA can be faked, rushed or captured too",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Ritualised:</strong> tools run mechanically to tick a 'participatory' box",
                 "<strong>Rushed:</strong> a one-day exercise extracting data, then gone",
                 "<strong>Captured:</strong> dominant voices draw the map; the marginalised stay silent",
                 "<strong>Raised &amp; betrayed:</strong> expectations lifted, then no follow-through"]},
             {"t": "hbox", "color": "amber", "html": "Chambers himself warned of 'PRA tourism'. "
              "The method is only as good as the attitudes and behaviour behind it."},
         ]},

        {"type": "content", "label": "Behaviour First", "title": "Attitudes matter more than techniques",
         "blocks": [
             {"t": "quote",
              "text": "PRA is more about behaviour and attitudes than about methods and tools.",
              "attr": "&mdash; Robert Chambers"},
             {"t": "body", "html": "Sit down, shut up, and listen. Be patient. Don't dominate. "
              "Hand over the stick. Embrace error. The diagrams are easy to learn; the humility "
              "to let go of control is the hard part."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Self-Help Groups &amp; Collective Action"},

        {"type": "content", "label": "The SHG", "title": "What a Self-Help Group is",
         "blocks": [
             {"t": "term", "word": "Self-Help Group (SHG)",
              "def": "A small, usually women-only group (typically 10&ndash;20 members) who save "
              "regularly into a common fund, lend to one another, and over time link to banks and "
              "act collectively on shared concerns."},
             {"t": "body", "html": "The SHG is South Asia's most widespread vehicle of "
              "community-level collective action &mdash; financial at its root, but social and "
              "political in its reach."},
         ]},

        {"type": "content", "label": "Why It Works", "title": "Savings first, then so much more",
         "blocks": [
             {"t": "flow", "steps": [
                 "SAVE: members pool small, regular savings",
                 "LEND: internal loans at the group's own terms",
                 "LINK: the group connects to a bank (SHG-Bank Linkage)",
                 "ACT: the group takes on health, rights, governance"]},
             {"t": "hbox", "color": "green", "html": "The genius is sequence: financial discipline "
              "builds trust and a habit of meeting &mdash; which becomes the platform for "
              "everything else a community might organise around."},
         ]},

        {"type": "content", "label": "Federations", "title": "From groups to federations",
         "blocks": [
             {"t": "body", "html": "Individual SHGs federate upward &mdash; into "
              "<strong>village organisations</strong> and then <strong>cluster- or "
              "block-level federations</strong> &mdash; gaining scale, bargaining power and a "
              "collective voice with banks and the state."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "SHG", "label": "10&ndash;20 members, one habitation", "color": "cyan"},
                 {"num": "VO", "label": "village organisation of several SHGs", "color": "indigo"},
                 {"num": "Federation", "label": "cluster / block of many VOs", "color": "green"}]},
         ]},

        {"type": "content", "label": "The Commons", "title": "Managing shared resources together",
         "blocks": [
             {"t": "body", "html": "Much of what poor communities depend on is held in "
              "<strong>common</strong> &mdash; grazing land, forests, fisheries, irrigation "
              "water, groundwater. The old fear was that shared resources are inevitably "
              "overused: the 'tragedy of the commons'."},
             {"t": "hbox", "color": "indigo", "html": "Elinor Ostrom showed this 'tragedy' is not "
              "inevitable &mdash; communities can and do govern shared resources sustainably, "
              "without privatisation or state takeover."},
         ]},

        {"type": "content", "label": "Ostrom", "title": "Elinor Ostrom and governing the commons",
         "blocks": [
             {"t": "body", "html": "Elinor Ostrom won the 2009 Nobel Memorial Prize in Economics "
              "for showing how communities sustainably manage common resources. Her "
              "<strong>design principles</strong> describe what makes collective governance work."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Clear boundaries &mdash; who may use the resource, and what",
                 "Rules that fit local conditions, made by the users themselves",
                 "Collective choice: those affected help set the rules",
                 "Monitoring, graduated sanctions &amp; cheap conflict resolution",
                 "Recognised right to organise; nested layers for larger systems"]},
         ]},

        {"type": "content", "label": "India's Mission", "title": "DAY-NRLM: SHGs at national scale",
         "blocks": [
             {"t": "body", "html": "India's <strong>Deendayal Antyodaya Yojana &ndash; National "
              "Rural Livelihoods Mission (DAY-NRLM)</strong> mobilises rural poor women into SHGs "
              "and their federations at vast scale &mdash; arguably the world's largest "
              "community-institution programme."},
             {"t": "hbox", "color": "amber", "html": "It builds on earlier state efforts &mdash; "
              "Andhra Pradesh's SERP and Kerala's Kudumbashree are landmark models of "
              "women-led SHG federations."},
         ]},

        {"type": "content", "label": "The Scale", "title": "SHG growth in India, illustrative trend",
         "blocks": [
             {"t": "chart", "canvas": "shgGrowthChart",
              "title": "SHGs mobilised under the rural livelihoods mission (illustrative trend)",
              "source": "Illustrative &mdash; pattern, not exact figures",
              "type": "line",
              "data": {"labels": ["2013", "2015", "2017", "2019", "2021", "2023"],
                       "datasets": [{"label": "SHGs (millions, illustrative)",
                                     "data": [2.1, 3.3, 4.5, 6.0, 7.5, 9.0],
                                     "borderColor": "#10B981",
                                     "backgroundColor": "rgba(16,185,129,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true, title:{display:true,text:'SHGs (millions, illustrative)'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The exact numbers vary by source and year; "
              "the <em>shape</em> &mdash; sustained, rapid growth into the millions &mdash; is the "
              "real story. Figures here are illustrative."},
         ]},

        {"type": "content", "label": "Honest Caveats", "title": "SHGs are powerful, not magic",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Over-lending can push members into a debt trap, not out of one",
                 "The poorest and most marginalised are often left out of groups",
                 "Targets-driven formation creates 'paper' SHGs that never function",
                 "Financial inclusion does not automatically deliver empowerment"]},
             {"t": "hbox", "color": "amber", "html": "An SHG is a platform, not a cure. What is "
              "built on it &mdash; voice, rights, livelihoods &mdash; decides whether it "
              "transforms anything."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Power, Conflict &amp; Elite Capture"},

        {"type": "content", "label": "Read the Room", "title": "Power is always in the room",
         "blocks": [
             {"t": "body", "html": "Every community decision happens inside structures of power "
              "&mdash; caste, class, gender, age, party. Ignoring power does not make it neutral; "
              "it just lets the powerful win quietly."},
             {"t": "hbox", "color": "indigo", "html": "Power analysis asks three questions: who "
              "decides, who benefits, and who is kept out? Ask them of <em>every</em> meeting and "
              "plan."},
         ]},

        {"type": "content", "label": "Forms of Power", "title": "Power has visible and hidden faces",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Visible", "label": "Formal decisions &mdash; who sits on the committee, "
                  "who signs", "color": "cyan"},
                 {"num": "Hidden", "label": "Who sets the agenda &mdash; and keeps issues off it",
                  "color": "amber"},
                 {"num": "Invisible", "label": "Norms &amp; beliefs &mdash; people accepting "
                  "'this is not for us'", "color": "red"}]},
             {"t": "body", "cls": "sm", "html": "The most stubborn exclusion is invisible: when a "
              "Dalit woman does not speak because everyone, including her, treats her silence as "
              "natural. That is power working without anyone raising a voice."},
         ]},

        {"type": "content", "label": "The Core Risk", "title": "Elite capture",
         "blocks": [
             {"t": "term", "word": "Elite capture",
              "def": "When the benefits of a programme &mdash; resources, decisions, "
              "representation &mdash; are siphoned by locally powerful individuals or groups, at "
              "the expense of the people it was meant to reach."},
             {"t": "body", "html": "Participatory and decentralised programmes are <em>especially</em> "
              "vulnerable: handing power 'to the community' can simply hand it to whoever already "
              "dominates the community."},
         ]},

        {"type": "content", "label": "How It Happens", "title": "The quiet mechanics of capture",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "The dominant caste/class chairs the committee 'because they have time'",
                 "Meetings held at times or places the poor and women cannot attend",
                 "Information shared in language or jargon that excludes most members",
                 "Contracts and works routed to the same few connected families"]},
             {"t": "hbox", "color": "amber", "html": "Capture rarely looks like theft. It looks "
              "like the natural, unquestioned order of things &mdash; which is exactly why it is "
              "so hard to name."},
         ]},

        {"type": "content", "label": "Gender &amp; Caste", "title": "Who is excluded within the community",
         "blocks": [
             {"t": "body", "html": "The same village that is marginalised from outside is itself "
              "stratified within. Women, Dalits, Adivasis and persons with disabilities are "
              "routinely the <strong>last consulted and first overlooked</strong> &mdash; even in "
              "'participatory' processes."},
             {"t": "hbox", "color": "green", "html": "Inclusion takes deliberate design: separate "
              "spaces for women to speak, reserved roles, facilitation that draws out the quiet, "
              "and meeting times that fit the lives of the excluded."},
         ]},

        {"type": "content", "label": "Speaking For", "title": "Who really speaks for the community?",
         "blocks": [
             {"t": "body", "html": "When the sarpanch, the contractor or the loudest man says "
              "'the community wants this', a practitioner's job is to ask: <em>which</em> "
              "community, chosen <em>how</em>, accountable to <em>whom</em>?"},
             {"t": "hbox", "color": "red", "html": "A self-appointed spokesperson is not a "
              "mandate. Triangulate &mdash; cross-check claims with the people who were not in "
              "the room."},
         ]},

        {"type": "content", "label": "Conflict", "title": "Conflict is normal &mdash; and useful",
         "blocks": [
             {"t": "body", "html": "Bringing power to the surface <em>creates</em> conflict. That "
              "is not a failure of community development &mdash; it is often a sign that real "
              "interests, long suppressed, are finally being voiced."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Avoid", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Suppressing conflict to keep a false peace "
                   "&mdash; which simply preserves the existing imbalance of power."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Do", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Surface it, name interests, mediate fairly, "
                   "and seek outcomes the least powerful can also accept."}]}]},
         ]},

        {"type": "content", "label": "Managing It", "title": "Handling conflict constructively",
         "blocks": [
             {"t": "flow", "steps": [
                 "NAME the real interests behind stated positions",
                 "SEPARATE people from the problem",
                 "BROADEN options before narrowing to a deal",
                 "PROTECT the weakest party's stake in the outcome"]},
             {"t": "hbox", "color": "cyan", "html": "A facilitator is not neutral about "
              "<em>fairness</em>. Staying 'neutral' between the powerful and the powerless simply "
              "sides with the powerful."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Sustainability, Ownership &amp; Exit"},

        {"type": "content", "label": "The Endgame", "title": "Plan the exit from day one",
         "blocks": [
             {"t": "body", "html": "The measure of community development is what survives "
              "<em>after</em> the agency leaves. Yet exit is usually an afterthought &mdash; a "
              "rushed handover when the grant runs out. It should be designed from the very "
              "beginning."},
             {"t": "hbox", "color": "cyan", "html": "Ask on day one: 'What will the community own, "
              "run and fund without us in five years?' Build backwards from that answer."},
         ]},

        {"type": "content", "label": "The Trap", "title": "Dependency: the silent failure",
         "blocks": [
             {"t": "term", "word": "Dependency",
              "def": "When a community comes to rely on an external agency for activity, decisions "
              "or funds &mdash; losing, rather than gaining, the capacity to act on its own."},
             {"t": "hbox", "color": "red", "html": "Generous, well-meaning, sustained support can "
              "create dependency just as surely as neglect causes harm. Doing things "
              "<em>for</em> people too long teaches them to wait."},
         ]},

        {"type": "content", "label": "Ownership", "title": "Ownership cannot be transferred at the end",
         "blocks": [
             {"t": "body", "html": "Ownership is not a handover ceremony; it is who decided, who "
              "contributed and who controlled resources <em>throughout</em>. A community that did "
              "not build it will not defend it."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Low ownership", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Agency designed, built and ran it; community "
                   "'received' it. Falls into disrepair within a year of exit."}]}],
              "right": [{"t": "panel", "color": "green", "title": "High ownership", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Community chose, co-invested and managed it "
                   "from the start. Maintains and adapts it long after."}]}]},
         ]},

        {"type": "content", "label": "Signals", "title": "Spot dependency before it sets in",
         "blocks": [
             {"t": "bullets", "color": "amber", "items": [
                 "Nothing happens unless the field staff convene the meeting",
                 "Every problem is brought to the agency, not to the local institution",
                 "The committee cannot name what it will do once funds stop",
                 "Contributions (cash, labour, time) come only from the project, never the community"]},
             {"t": "hbox", "color": "green", "html": "The cure is deliberate stepping back &mdash; "
              "let the local institution lead, struggle and learn while you are still there to "
              "support, not after you have gone."},
         ]},

        {"type": "content", "label": "The Outsider", "title": "The role of the outsider / facilitator",
         "blocks": [
             {"t": "body", "html": "The outsider is a <strong>catalyst and facilitator</strong>, "
              "not a provider or a chief. The aim is to start a reaction the community can sustain "
              "&mdash; and then to become, gracefully, unnecessary."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Do", "label": "Facilitate, connect, coach, open doors, step back",
                  "color": "green"},
                 {"num": "Don't", "label": "Decide, dominate, deliver everything, become "
                  "indispensable", "color": "red"}]},
         ]},

        {"type": "content", "label": "Phasing Out", "title": "A graduated withdrawal",
         "blocks": [
             {"t": "flow", "steps": [
                 "LEAD: agency does much, community observes",
                 "SHARE: agency &amp; community do it together",
                 "SUPPORT: community leads, agency advises",
                 "WITHDRAW: community runs it; agency on call",
                 "EXIT: agency leaves; institution endures"]},
             {"t": "hbox", "color": "cyan", "html": "Withdrawal should be gradual, announced "
              "early and predictable &mdash; never a sudden disappearance when the grant cycle "
              "happens to end."},
         ]},

        {"type": "content", "label": "Before / After", "title": "What durable ownership looks like, illustrative",
         "blocks": [
             {"t": "chart", "canvas": "ownershipChart",
              "title": "Local institution still active two years after exit (illustrative)",
              "source": "Illustrative comparison, not a study",
              "type": "bar",
              "data": {"labels": ["Agency-led handover", "Community-owned from start"],
                       "datasets": [{"label": "Still functioning after 2 years (%)",
                                     "data": [28, 74],
                                     "backgroundColor": ["#EF4444", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ beginAtZero:true, max:100, title:{display:true,text:'% still active (illustrative)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative, but it names a real and "
              "well-observed pattern: what a community builds, it keeps; what is handed to it, it "
              "tends to lose."},
         ]},

        {"type": "content", "label": "Sustaining Finance", "title": "Where the money comes from after exit",
         "blocks": [
             {"t": "body", "html": "Financial sustainability is the hardest kind. An institution "
              "that depends entirely on the agency's grant has no future once the grant ends. "
              "Durable community institutions build their <em>own</em> resource base."},
             {"t": "bullets", "color": "cyan", "sm": True, "items": [
                 "Member contributions &mdash; savings, fees, a corpus the group owns",
                 "Linkage to mainstream finance &mdash; banks, government schemes",
                 "Earned income &mdash; a service or enterprise the institution runs",
                 "Claimed entitlements &mdash; convergence with public budgets (MGNREGA, NRLM)"]},
             {"t": "hbox", "color": "green", "html": "The strongest exits leave a community not "
              "just willing but <em>able</em> to fund what matters &mdash; from its own resources "
              "and the public resources it has learned to claim."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Community Development in South Asia"},

        {"type": "content", "label": "The Frame", "title": "Local self-government as the arena",
         "blocks": [
             {"t": "body", "html": "In South Asia, community development largely plays out through "
              "<strong>local self-government</strong> &mdash; the panchayat in India, the union "
              "council in Pakistan and Bangladesh, the local body in Nepal and Sri Lanka. Knowing "
              "this machinery is part of the craft."},
             {"t": "hbox", "color": "cyan", "html": "Community institutions (SHGs, user groups) "
              "and statutory bodies (panchayats) work best when they reinforce, rather than "
              "bypass, one another."},
         ]},

        {"type": "content", "label": "73rd Amendment", "title": "India's 73rd Constitutional Amendment, 1992",
         "blocks": [
             {"t": "body", "html": "The <strong>73rd Constitutional Amendment (1992)</strong> gave "
              "constitutional status to <strong>panchayati raj</strong> &mdash; a three-tier "
              "system of elected village, block and district councils &mdash; as institutions of "
              "local self-government."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Three tiers: gram (village), intermediate (block), zila (district)",
                 "Regular elections every five years",
                 "Reservation of seats for SC, ST and women",
                 "A Gram Sabha &mdash; the assembly of all village voters"]},
         ]},

        {"type": "content", "label": "Gram Sabha", "title": "The Gram Sabha: direct democracy in the village",
         "blocks": [
             {"t": "term", "word": "Gram Sabha",
              "def": "The assembly of all adult voters in a village &mdash; the only directly "
              "democratic, face-to-face body in the panchayati raj system, meant to approve plans, "
              "select beneficiaries and hold the panchayat to account."},
             {"t": "hbox", "color": "amber", "html": "On paper, the Gram Sabha is where community "
              "development and the state meet. In practice, attendance and real power vary widely "
              "&mdash; reviving it is itself a community-development task."},
         ]},

        {"type": "content", "label": "Reservation", "title": "Reservation: who gets to lead",
         "blocks": [
             {"t": "body", "html": "Reserving panchayat seats and chairs for women and for "
              "Scheduled Castes and Tribes has brought more than a million women and lakhs of "
              "Dalit and Adivasi citizens into elected office &mdash; a structural intervention in "
              "who holds local power."},
             {"t": "hbox", "color": "green", "html": "It is not automatic: 'proxy' leadership "
              "(the <em>sarpanch-pati</em> husband) persists. But evidence shows real shifts in "
              "voice and priorities where reserved leaders are genuinely supported."},
         ]},

        {"type": "content", "label": "NRLM", "title": "The rural livelihoods mission at work",
         "blocks": [
             {"t": "body", "html": "<strong>DAY-NRLM</strong> threads community development through "
              "the state: women's SHGs and federations link to banks, run social-audit processes, "
              "and increasingly interface with the panchayat &mdash; turning savings groups into "
              "agents of local governance."},
             {"t": "hbox", "color": "cyan", "html": "Convergence is the watchword: SHG federations "
              "+ MGNREGA + panchayat + line departments, woven together at the village so the "
              "pieces reinforce rather than duplicate."},
         ]},

        {"type": "content", "label": "Watershed", "title": "Watershed &amp; natural-resource movements",
         "blocks": [
             {"t": "body", "html": "Participatory <strong>watershed development</strong> &mdash; "
              "communities jointly conserving soil and water across a micro-catchment &mdash; is "
              "one of South Asia's signature community-development arenas, alongside Joint Forest "
              "Management and water-user associations."},
             {"t": "hbox", "color": "amber", "html": "These are textbook commons (Ostrom): they "
              "succeed where user groups make and enforce their own rules &mdash; and fail where "
              "the structure is imposed from above and captured."},
         ]},

        {"type": "content", "label": "Landmark Models", "title": "Movements the region learns from",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Model", "Where", "Known for"],
              "rows": [
                  ["Kudumbashree", "Kerala, India", "State-wide women's SHG network &amp; governance"],
                  ["SEWA", "Gujarat &amp; beyond", "Organising women in the informal economy"],
                  ["Watershed programmes", "Maharashtra, Rajasthan", "Community-managed water &amp; soil"],
                  ["AKRSP", "Pakistan / India", "Village organisations &amp; rural support"],
                  ["Grameen / BRAC", "Bangladesh", "Microfinance &amp; community institutions"]],},
             {"t": "hbox", "color": "indigo", "html": "Study these critically &mdash; for what "
              "travels and what is specific to their context. None is a template to copy "
              "wholesale."},
         ]},

        {"type": "content", "label": "The Gap", "title": "Devolution on paper vs in practice",
         "blocks": [
             {"t": "body", "html": "The law devolved <strong>functions, funds and functionaries</strong> "
              "(the '3 Fs') to panchayats. In practice, real powers and budgets often remain with "
              "higher tiers and line departments &mdash; the unfinished business of decentralisation."},
             {"t": "hbox", "color": "red", "html": "A common practitioner role: helping "
              "communities <em>claim</em> the powers the law already grants them &mdash; the gap "
              "between the statute and the street is where much of the work lives."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Practice &amp; Pitfalls"},

        {"type": "content", "label": "The Core Skill", "title": "Facilitation, not instruction",
         "blocks": [
             {"t": "body", "html": "The master skill of community development is "
              "<strong>facilitation</strong> &mdash; helping a group think, decide and act for "
              "itself, without taking over. The facilitator manages the <em>process</em> so the "
              "community owns the <em>content</em>."},
             {"t": "bullets", "color": "cyan", "sm": True, "items": [
                 "Ask more than you tell; question more than you answer",
                 "Draw out the quiet; gently check the dominant",
                 "Make the process visible &mdash; agree it openly with the group",
                 "Be comfortable with silence, and with not being in control"]},
         ]},

        {"type": "content", "label": "Listening", "title": "Deep listening is a technique",
         "blocks": [
             {"t": "quote",
              "text": "We have two ears and one mouth, so that we may listen twice as much as we speak.",
              "attr": "&mdash; a proverb every facilitator should keep"},
             {"t": "body", "html": "Most outsiders talk too much. Disciplined listening &mdash; "
              "to what is said, who says it, and what is left unsaid &mdash; is the single habit "
              "that most improves practice."},
         ]},

        {"type": "content", "label": "Do No Harm", "title": "First, do no harm",
         "blocks": [
             {"t": "body", "html": "Intervention is never neutral. Bringing resources, attention "
              "and new rules into a community shifts its balance of power &mdash; sometimes for "
              "the better, sometimes not. The <strong>do-no-harm</strong> lens makes you check "
              "the side-effects."},
             {"t": "bullets", "color": "red", "sm": True, "items": [
                 "Could this deepen existing divisions of caste, class or gender?",
                 "Could benefits be captured by the already-powerful?",
                 "Could we be raising expectations we cannot meet?",
                 "Could we be undermining a local institution that already works?"]},
         ]},

        {"type": "content", "label": "Common Pitfalls", "title": "The recurring mistakes",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Pitfall", "Looks like", "Antidote"],
              "rows": [
                  ["Target-chasing", "Forming groups to hit a number", "Quality &amp; function over count"],
                  ["Participation theatre", "Meetings that change nothing", "Share real decision power"],
                  ["Ignoring power", "Assuming one 'community voice'", "Power &amp; inclusion analysis"],
                  ["Creating dependency", "Doing everything for people", "Step back, build local capacity"],
                  ["No exit plan", "Collapse when funding ends", "Design ownership &amp; exit from day 1"]],},
         ]},

        {"type": "content", "label": "Measuring It", "title": "Measuring what is hard to count",
         "blocks": [
             {"t": "body", "html": "Capacity, voice and empowerment resist neat metrics &mdash; "
              "which tempts agencies to count only outputs (meetings held, groups formed). Resist "
              "that. Track the harder, truer signs of change."},
             {"t": "bullets", "color": "green", "sm": True, "items": [
                 "Do marginalised members now speak and lead in meetings?",
                 "Does the local institution act without the agency convening it?",
                 "Are people claiming entitlements and holding the state to account?",
                 "Combine numbers with stories &mdash; the change is in both"]},
         ]},

        {"type": "content", "label": "The Long View", "title": "Community development takes time",
         "blocks": [
             {"t": "body", "html": "Trust, organisation and leadership grow at the speed of "
              "relationships &mdash; not project cycles. The work is slow, non-linear and often "
              "invisible until, quite suddenly, a community acts on its own."},
             {"t": "hbox", "color": "amber", "html": "Beware the funding mismatch: three-year "
              "grants chasing changes that take a decade. Manage expectations &mdash; yours, the "
              "donor's and the community's &mdash; honestly."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Whose Reality Counts? Putting the First Last</em> &mdash; Robert Chambers",
                 "<em>Rural Development: Putting the Last First</em> &mdash; Robert Chambers",
                 "<em>Governing the Commons</em> &mdash; Elinor Ostrom",
                 "<em>Building Communities from the Inside Out</em> &mdash; Kretzmann &amp; McKnight (ABCD)",
                 "<em>Rules for Radicals</em> &mdash; Saul Alinsky (community organising)"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Participatory Methods</strong>, <strong>Gender &amp; Development</strong> "
              "and <strong>Local Governance</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Work with people, not for them</strong> &mdash; build capacity, not just outputs",
                 "<strong>'The community' is not one thing</strong> &mdash; ask who is missing within it",
                 "<strong>Participation is a matter of degree</strong> &mdash; aim above tokenism",
                 "<strong>Start from assets</strong> &mdash; then claim rights and resources",
                 "<strong>Plan your exit from day one</strong> &mdash; ownership cannot be handed over at the end"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Community Development 101 &middot; Complete",
         "headline": "Now go &mdash; and<br>work yourself out of a job.",
         "byline": "The best community development leaves a community more able to act on its own "
                   "future than you found it. Hand over the stick, build power from within, and "
                   "explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
