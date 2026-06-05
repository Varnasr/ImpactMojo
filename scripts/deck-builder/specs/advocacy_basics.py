# -*- coding: utf-8 -*-
"""
Advocacy Basics 101 — ImpactMojo 101 Series (native deck spec)
Foundational advocacy skills for South Asian development & civil-society practitioners.
Build: python3 scripts/deck-builder/build.py advocacy_basics
"""

DECK = {
    "slug": "advocacy-basics",
    "title": "Advocacy Basics 101",
    "description": ("Advocacy Basics 101 — a free foundational course for development and "
                    "civil-society practitioners in South Asia: how to analyse power, frame an "
                    "issue, map stakeholders, build a strategy and theory of change, read policy "
                    "windows, choose tactics, and advocate ethically. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Advocacy<br>Basics<br>101",
         "sub": "Influencing Policy, Practice, Power &amp; Norms &mdash; a Foundational Course "
                "for Development &amp; Civil-Society Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Advocacy Is"},
             {"name": "Types &amp; Approaches"},
             {"name": "Understanding Power"},
             {"name": "The Advocacy Cycle"},
             {"name": "Problem &amp; Issue Framing"},
             {"name": "Stakeholder &amp; Power Mapping"},
             {"name": "Strategy &amp; Theory of Change"},
             {"name": "The Policy Process &amp; Windows"},
             {"name": "Tactics &amp; Messaging"},
             {"name": "Monitoring, Evaluation &amp; Learning"},
             {"name": "Ethics, Risk &amp; Sustainability"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Advocacy Is"},

        {"type": "content", "label": "Definition", "title": "Advocacy is the work of shifting power",
         "blocks": [
             {"t": "body", "html": "<strong>Advocacy</strong> is the deliberate effort to "
              "influence the decisions, policies, practices and behaviours of those who hold power "
              "&mdash; so that public systems work better for people who are excluded. It is about "
              "changing the rules, not just delivering within them."},
             {"t": "term", "word": "Advocacy",
              "def": "A planned process to influence policy, practice, power relations and social "
              "norms in favour of a marginalised group or cause &mdash; by changing what "
              "decision-makers decide and what is considered normal."},
             {"t": "hbox", "color": "cyan", "html": "Advocacy asks a sharper question than service "
              "delivery: not 'how do we help these people?' but 'why are they excluded, and who "
              "can change that?'"},
         ]},

        {"type": "content", "label": "Four Targets", "title": "What advocacy tries to change",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Policy", "label": "Laws, schemes, budgets, official rules", "color": "cyan"},
                 {"num": "Practice", "label": "How institutions actually behave day to day", "color": "green"},
                 {"num": "Power", "label": "Who decides, and whose voice counts", "color": "indigo"},
                 {"num": "Norms", "label": "What a society treats as normal or acceptable", "color": "amber"}]},
             {"t": "hbox", "color": "amber", "html": "A good law that is never implemented is a "
              "practice problem; a stigma that survives the law is a norms problem. Advocacy may "
              "need all four."},
         ]},

        {"type": "content", "label": "The Big Distinction", "title": "Advocacy vs service delivery",
         "blocks": [
             {"t": "table",
              "head": ["", "Service delivery", "Advocacy"],
              "rows": [
                  ["Question", "How do we meet the need?", "Why does the need persist?"],
                  ["Acts on", "Individuals &amp; communities", "Systems &amp; decision-makers"],
                  ["Goal", "Fill the gap", "Close the gap at source"],
                  ["Measure", "People reached", "Policy / practice changed"],
                  ["Time-frame", "Immediate", "Often years"]]},
             {"t": "hbox", "color": "cyan", "html": "They are complements. Service delivery reveals "
              "the problem and earns legitimacy; advocacy attacks the cause. Many strong NGOs do both."},
         ]},

        {"type": "content", "label": "Why Advocate", "title": "Service delivery alone never scales",
         "blocks": [
             {"t": "flow", "steps": [
                 "You run 50 schools well",
                 "But 5,000 govt schools lack teachers",
                 "Charity cannot fill that gap",
                 "Only a policy &amp; budget shift can"]},
             {"t": "body", "html": "When a problem is structural &mdash; in law, budget allocation "
              "or institutional behaviour &mdash; only a structural response reaches everyone. That "
              "is the case for advocacy: <strong>leverage</strong>, not just reach."},
         ]},

        {"type": "content", "label": "Boundaries", "title": "Advocacy, activism, lobbying, campaigning",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Term", "Core meaning", "Note"],
              "rows": [
                  ["Advocacy", "Influence decisions &amp; norms for a cause", "The umbrella term"],
                  ["Lobbying", "Direct influence on legislators / officials", "A narrow, specific tactic"],
                  ["Campaigning", "Sustained, public, time-bound push", "A vehicle for advocacy"],
                  ["Activism", "Visible action to demand change", "Often confrontational, outsider"]]},
             {"t": "hbox", "color": "amber", "html": "These overlap. Lobbying and campaigning are "
              "<em>tactics</em> within advocacy; activism is a <em>style</em>. Knowing the "
              "difference helps you choose the right tool &mdash; and describe yourself accurately."},
         ]},

        {"type": "content", "label": "Lobbying, Precisely", "title": "Lobbying is the narrowest tool",
         "blocks": [
             {"t": "term", "word": "Lobbying",
              "def": "Direct, private communication with legislators or officials to influence a "
              "specific law, regulation, budget line or decision. It is one tactic inside advocacy "
              "&mdash; not a synonym for it."},
             {"t": "hbox", "color": "red", "html": "The distinction is legal as well as conceptual: "
              "in many jurisdictions lobbying is regulated and reportable, and a charity's freedom "
              "to lobby may be restricted. Broad public advocacy usually is not lobbying."},
         ]},

        {"type": "content", "label": "Who Does It", "title": "Advocacy is for everyone, not just experts",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Communities</strong> advocating for their own rights &mdash; the strongest legitimacy",
                 "<strong>NGOs &amp; networks</strong> with reach, evidence and convening power",
                 "<strong>Coalitions</strong> that pool numbers and credibility",
                 "<strong>Researchers &amp; media</strong> who put issues on the agenda",
                 "<strong>Insiders</strong> &mdash; sympathetic officials and reformers within the system"]},
             {"t": "hbox", "color": "green", "html": "The most durable advocacy is led <em>by</em> "
              "the people affected, not done <em>for</em> them. We return to that distinction in "
              "Section Two."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Types &amp; Approaches"},

        {"type": "content", "label": "Inside or Outside", "title": "Insider vs outsider advocacy",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Insider", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Quiet engagement with decision-makers: "
                   "consultations, expert committees, private meetings, technical inputs. Access "
                   "and trust; risk of co-option."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Outsider", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Public pressure from outside: protest, media, "
                   "petitions, mobilisation, litigation. Independence and visibility; risk of being "
                   "shut out."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Most effective advocacy is <strong>both at "
              "once</strong> &mdash; an inside-track negotiator backed by an outside-track that "
              "makes the negotiator's offer look reasonable."},
         ]},

        {"type": "content", "label": "The Repertoire", "title": "Four broad approaches",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Lobbying", "label": "Direct influence on officials &amp; legislators", "color": "cyan"},
                 {"num": "Campaigning", "label": "Sustained public push to build pressure", "color": "green"},
                 {"num": "Litigation", "label": "Using courts to enforce or create rights", "color": "indigo"},
                 {"num": "Mobilisation", "label": "Organising people to act collectively", "color": "amber"}]},
             {"t": "body", "html": "Few campaigns use only one. They are sequenced and combined &mdash; "
              "research to mobilisation to lobbying, with litigation held in reserve as leverage."},
         ]},

        {"type": "content", "label": "The Courts", "title": "Litigation &amp; PIL in South Asia",
         "blocks": [
             {"t": "body", "html": "<strong>Public Interest Litigation (PIL)</strong> lets citizens "
              "and groups ask courts to enforce rights on behalf of those who cannot reach the "
              "court themselves. In India it has shaped rights to food, education and a clean "
              "environment."},
             {"t": "hbox", "color": "amber", "html": "Litigation can win a binding order overnight "
              "&mdash; but courts cannot run programmes. A judgment is the start of an "
              "implementation fight, not the end of advocacy."},
         ]},

        {"type": "content", "label": "Mass Action", "title": "Social mobilisation",
         "blocks": [
             {"t": "body", "html": "<strong>Social mobilisation</strong> organises affected people "
              "into a visible, collective force &mdash; marches, jan sunwais (public hearings), "
              "dharnas, mass petitions. Numbers are the currency that decision-makers cannot ignore."},
             {"t": "term", "word": "Jan Sunwai (public hearing)",
              "def": "A South Asian social-audit tool where officials answer to citizens in the "
              "open, comparing records against people's testimony. It turns abstract accountability "
              "into a face-to-face demand."},
         ]},

        {"type": "content", "label": "A Landmark", "title": "MKSS, the RTI movement &amp; social audit",
         "blocks": [
             {"t": "body", "html": "In Rajasthan, the Mazdoor Kisan Shakti Sangathan (MKSS) used "
              "public hearings to expose corruption in local works &mdash; building grassroots "
              "demand that helped drive India's <strong>Right to Information Act, 2005</strong>."},
             {"t": "hbox", "color": "green", "html": "It shows the full repertoire in sequence: "
              "mobilisation generated evidence, evidence fuelled a campaign, the campaign won a law "
              "&mdash; and the law became a permanent tool for the next fight."},
         ]},

        {"type": "content", "label": "Whose Voice", "title": "Advocacy WITH vs advocacy FOR communities",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Advocacy WITH", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Affected people set the agenda, lead, and "
                   "speak. The organisation accompanies and amplifies. Builds power that outlasts "
                   "the project."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Advocacy FOR", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Outsiders speak on people's behalf. Faster, "
                   "but risks substituting expert voice for lived voice &mdash; and leaves no power "
                   "behind."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Default to <strong>with</strong>; use "
              "<strong>for</strong> only where speaking out is unsafe for those affected &mdash; "
              "and even then, on their terms."},
         ]},

        {"type": "content", "label": "Representation", "title": "'Nothing about us without us'",
         "blocks": [
             {"t": "quote",
              "text": "Nothing about us without us.",
              "attr": "&mdash; disability-rights movement, now a wider principle of legitimate advocacy"},
             {"t": "body", "html": "Legitimacy comes from <em>proximity</em> to the problem. Before "
              "you speak, ask: who gave me this mandate, and would the affected community recognise "
              "themselves in what I am saying?"},
         ]},

        {"type": "content", "label": "Choosing", "title": "There is no single 'right' approach",
         "blocks": [
             {"t": "bullets", "items": [
                 "Match the approach to the <strong>target</strong> &mdash; courts, ministers, the public differ",
                 "Match it to your <strong>power</strong> &mdash; access, numbers, evidence or moral authority",
                 "Match it to the <strong>risk</strong> &mdash; what is safe for your constituents",
                 "Sequence &amp; combine &mdash; insider and outsider, evidence and pressure"]},
             {"t": "hbox", "color": "amber", "html": "The choice is strategic, not ideological. The "
              "rest of this course is about making it deliberately."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Understanding Power"},

        {"type": "content", "label": "The Core", "title": "Advocacy is applied power analysis",
         "blocks": [
             {"t": "body", "html": "Every advocacy problem is, underneath, a question of power: who "
              "has it, how it works, and how it can shift. Before strategy, analyse power &mdash; "
              "otherwise you push on the wrong door."},
             {"t": "hbox", "color": "cyan", "html": "This section borrows two classic frameworks: "
              "Steven Lukes' <em>three faces of power</em> and the activist-friendly "
              "<em>power-over / with / to / within</em> typology, plus John Gaventa's "
              "<em>power cube</em>."},
         ]},

        {"type": "content", "label": "Lukes", "title": "Steven Lukes' three faces of power",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Face / dimension", "How power works", "Advocacy example"],
              "rows": [
                  ["1. Decision-making", "Winning open conflicts", "Vote, ruling or budget line goes your way"],
                  ["2. Agenda-setting", "Keeping issues off the table", "An issue is never even debated"],
                  ["3. Shaping desires", "Forming what people want &amp; accept", "People see injustice as normal, fated"]]},
             {"t": "body", "html": "Lukes (<em>Power: A Radical View</em>, 1974) argued power is "
              "deepest when it is invisible &mdash; when it shapes what people believe is possible, "
              "so no conflict appears at all."},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "The hardest power is the kind you can't see",
         "blocks": [
             {"t": "flow", "steps": [
                 "1st face: you lose a fair fight",
                 "2nd face: you never get the fight",
                 "3rd face: nobody thinks there is anything to fight about"]},
             {"t": "hbox", "color": "red", "html": "Naming the third face is itself advocacy. "
              "Consciousness-raising &mdash; helping people see an accepted condition as an "
              "injustice &mdash; is how change begins where no visible conflict exists yet."},
         ]},

        {"type": "content", "label": "VeneKlasen &amp; Miller", "title": "Four expressions of power",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Form", "Meaning", "For advocacy"],
              "rows": [
                  ["Power OVER", "Control, domination, repression", "The power we seek to change"],
                  ["Power WITH", "Collective strength, solidarity", "Coalitions, mobilisation"],
                  ["Power TO", "Individual capacity to act", "Skills, agency, leadership"],
                  ["Power WITHIN", "Self-worth, dignity, confidence", "The root of voice &amp; courage"]]},
             {"t": "body", "html": "From Lisa VeneKlasen &amp; Valerie Miller, <em>A New Weave of "
              "Power, People &amp; Politics</em> (2002). Advocacy converts <strong>power-within</strong> "
              "and <strong>power-to</strong> into <strong>power-with</strong> to confront "
              "<strong>power-over</strong>."},
         ]},

        {"type": "content", "label": "Positive Power", "title": "Not all power is domination",
         "blocks": [
             {"t": "body", "html": "It is tempting to treat power as a dirty word. But "
              "<strong>power-with</strong>, <strong>power-to</strong> and "
              "<strong>power-within</strong> are exactly what advocacy <em>builds</em>. The goal is "
              "not to abolish power but to redistribute and democratise it."},
             {"t": "hbox", "color": "green", "html": "A campaign that wins a policy but leaves the "
              "community no more confident or organised has spent power-over without building "
              "power-with. Ask what power your work <em>creates</em>."},
         ]},

        {"type": "content", "label": "Gaventa", "title": "The power cube: three dimensions",
         "blocks": [
             {"t": "body", "html": "John Gaventa (IDS) maps power along three axes at once &mdash; "
              "the <strong>power cube</strong>. It helps locate exactly <em>where</em> a change "
              "must happen."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Spaces", "label": "Closed &middot; Invited &middot; Claimed/created", "color": "cyan"},
                 {"num": "Places", "label": "Local &middot; National &middot; Global", "color": "indigo"},
                 {"num": "Forms", "label": "Visible &middot; Hidden &middot; Invisible", "color": "amber"}]},
             {"t": "body", "cls": "sm", "html": "Source: John Gaventa, 'Finding the Spaces for "
              "Change: A Power Analysis', IDS Bulletin (2006)."},
         ]},

        {"type": "content", "label": "Visualise", "title": "The power cube, drawn",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;align-items:center;padding:6px 0">'
                 '<svg viewBox="0 0 460 300" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;max-width:560px;height:auto">'
                 # cube — front face
                 '<rect x="70" y="90" width="200" height="160" fill="rgba(14,165,233,0.10)" '
                 'stroke="#0EA5E9" stroke-width="2"/>'
                 # top face
                 '<polygon points="70,90 150,40 350,40 270,90" fill="rgba(99,102,241,0.12)" '
                 'stroke="#6366F1" stroke-width="2"/>'
                 # right face
                 '<polygon points="270,90 350,40 350,200 270,250" fill="rgba(245,158,11,0.12)" '
                 'stroke="#F59E0B" stroke-width="2"/>'
                 # internal grid (front)
                 '<line x1="136" y1="90" x2="136" y2="250" stroke="#0EA5E9" stroke-width="1" stroke-dasharray="3,3"/>'
                 '<line x1="203" y1="90" x2="203" y2="250" stroke="#0EA5E9" stroke-width="1" stroke-dasharray="3,3"/>'
                 '<line x1="70" y1="143" x2="270" y2="143" stroke="#0EA5E9" stroke-width="1" stroke-dasharray="3,3"/>'
                 '<line x1="70" y1="196" x2="270" y2="196" stroke="#0EA5E9" stroke-width="1" stroke-dasharray="3,3"/>'
                 # axis labels
                 '<text x="170" y="278" fill="#0EA5E9" font-size="13" font-weight="700">SPACES</text>'
                 '<text x="305" y="155" fill="#F59E0B" font-size="13" font-weight="700" '
                 'transform="rotate(90 305 155)">PLACES</text>'
                 '<text x="200" y="28" fill="#6366F1" font-size="13" font-weight="700">FORMS</text>'
                 '<text x="78" y="110" fill="#94a3b8" font-size="10">closed</text>'
                 '<text x="148" y="110" fill="#94a3b8" font-size="10">invited</text>'
                 '<text x="212" y="110" fill="#94a3b8" font-size="10">claimed</text>'
                 '</svg></div>')},
             {"t": "hbox", "color": "cyan", "html": "Read it as: <em>which space</em> (closed, "
              "invited, or claimed), <em>at which level</em>, and <em>which form</em> of power are "
              "you trying to move? The answer dictates your tactic."},
         ]},

        {"type": "content", "label": "Spaces", "title": "Closed, invited and claimed spaces",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Closed:</strong> decisions made behind shut doors &mdash; you are not in the room",
                 "<strong>Invited:</strong> you are asked in &mdash; consultations, committees (watch for tokenism)",
                 "<strong>Claimed / created:</strong> spaces people open themselves &mdash; movements, public hearings"]},
             {"t": "hbox", "color": "amber", "html": "Strategy follows the space: prise open a "
              "closed space, use an invited one without being co-opted, and build claimed spaces "
              "where none exist."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "The Advocacy Cycle"},

        {"type": "content", "label": "The Loop", "title": "Advocacy is a cycle, not a straight line",
         "blocks": [
             {"t": "flow", "steps": [
                 "RESEARCH: understand the problem &amp; power",
                 "STRATEGY: set objectives, targets, tactics",
                 "ACTION: do the advocacy",
                 "MONITORING: track what shifts",
                 "LEARNING: adapt &amp; loop back"]},
             {"t": "hbox", "color": "cyan", "html": "It loops because the political world moves. "
              "Each round of action teaches you something that should reshape the next round's "
              "strategy."},
         ]},

        {"type": "content", "label": "Step 1", "title": "Research: know the problem and the power",
         "blocks": [
             {"t": "body", "html": "Good advocacy rests on two kinds of homework: "
              "<strong>evidence</strong> about the problem (its scale, causes, who it hurts) and "
              "<strong>power analysis</strong> about the decision (who decides, what moves them)."},
             {"t": "bullets", "sm": True, "items": [
                 "What exactly is wrong, and for whom?",
                 "What are the root causes (Section Five)?",
                 "Who has the power to change it (Section Six)?",
                 "What is the realistic, winnable ask?"]},
         ]},

        {"type": "content", "label": "Step 2", "title": "Strategy: turn analysis into a plan",
         "blocks": [
             {"t": "body", "html": "Strategy connects your goal to your context: a clear "
              "<strong>objective</strong>, the <strong>targets</strong> who can deliver it, the "
              "<strong>tactics</strong> that move them, and a <strong>theory of change</strong> "
              "that links them (Section Seven)."},
             {"t": "hbox", "color": "amber", "html": "Most advocacy fails not from weak passion "
              "but from skipping strategy &mdash; rushing to a march before deciding who it is "
              "meant to move, and how."},
         ]},

        {"type": "content", "label": "Step 3", "title": "Action: do the advocacy",
         "blocks": [
             {"t": "bullets", "items": [
                 "Build coalitions and constituencies",
                 "Generate and package the evidence",
                 "Engage targets &mdash; insider meetings, outsider pressure",
                 "Use media, digital and grassroots channels (Section Nine)",
                 "Stay flexible &mdash; seize windows as they open (Section Eight)"]},
             {"t": "hbox", "color": "cyan", "html": "Action is the visible part &mdash; but its "
              "effectiveness was mostly decided in the research and strategy steps before it."},
         ]},

        {"type": "content", "label": "Step 4", "title": "Monitoring: track the shifts",
         "blocks": [
             {"t": "body", "html": "Advocacy outcomes are slow and indirect, so monitor the "
              "<strong>signals</strong> along the way: a minister's changed language, a new "
              "consultation, an issue reaching committee, a coalition growing &mdash; not just the "
              "final law."},
             {"t": "hbox", "color": "green", "html": "These intermediate markers tell you whether "
              "your theory of change is working <em>before</em> the final outcome arrives. Section "
              "Ten goes deeper."},
         ]},

        {"type": "content", "label": "Step 5", "title": "Learning: adapt and loop back",
         "blocks": [
             {"t": "body", "html": "Politics is unpredictable, so treat each cycle as a learning "
              "round. What moved? What didn't? Did the target have the power you assumed? Feed the "
              "answers straight back into the next strategy."},
             {"t": "quote", "text": "No plan survives first contact with the political world. The "
              "advantage goes to those who learn fastest.",
              "attr": "&mdash; a working principle of adaptive advocacy"},
         ]},

        {"type": "content", "label": "Pace", "title": "Advocacy runs on a long clock",
         "blocks": [
             {"t": "body", "html": "Landmark changes &mdash; India's RTI, MGNREGA, the Right to "
              "Education &mdash; took years of cycles, setbacks and re-strategising. Expect a "
              "marathon, and design for endurance, not a single sprint."},
             {"t": "hbox", "color": "amber", "html": "Build the cycle into your funding, staffing "
              "and morale. Campaigns that assume one push will win tend to burn out at the first "
              "rejection."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Problem &amp; Issue Framing"},

        {"type": "content", "label": "Problem vs Issue", "title": "A problem is broad; an issue is actionable",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Problem", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Big, complex, structural &mdash; 'child "
                   "malnutrition'. Important, but too large to campaign on directly."}]}],
              "right": [{"t": "panel", "color": "cyan", "title": "Issue", "blocks": [
                  {"t": "body", "cls": "sm", "html": "A specific, solvable slice with a clear "
                   "decision-maker &mdash; 'the district must fill 200 vacant anganwadi-worker posts'."}]}]},
             {"t": "hbox", "color": "amber", "html": "You advocate on <strong>issues</strong>, not "
              "problems. The craft of framing is cutting a winnable issue out of an overwhelming "
              "problem."},
         ]},

        {"type": "content", "label": "Root Causes", "title": "Dig beneath the symptom",
         "blocks": [
             {"t": "body", "html": "Treating symptoms wastes effort. <strong>Root-cause "
              "analysis</strong> &mdash; asking 'but why?' repeatedly &mdash; finds the leverage "
              "point where a single change unlocks many effects."},
             {"t": "flow", "steps": [
                 "Children are malnourished",
                 "Why? Anganwadis are not functioning",
                 "Why? Posts are vacant &amp; funds delayed",
                 "ROOT: budget release &amp; recruitment rules"]},
         ]},

        {"type": "content", "label": "Tools", "title": "The 'problem tree'",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;padding:4px 0">'
                 '<svg viewBox="0 0 460 250" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;max-width:560px;height:auto">'
                 # effects (top)
                 '<rect x="60" y="14" width="150" height="30" rx="5" fill="rgba(239,68,68,0.12)" stroke="#EF4444"/>'
                 '<rect x="250" y="14" width="150" height="30" rx="5" fill="rgba(239,68,68,0.12)" stroke="#EF4444"/>'
                 '<text x="135" y="33" fill="#EF4444" font-size="11" text-anchor="middle">Effect: stunting</text>'
                 '<text x="325" y="33" fill="#EF4444" font-size="11" text-anchor="middle">Effect: school dropout</text>'
                 # core problem
                 '<rect x="140" y="100" width="180" height="36" rx="6" fill="rgba(14,165,233,0.15)" stroke="#0EA5E9" stroke-width="2"/>'
                 '<text x="230" y="123" fill="#0EA5E9" font-size="12" font-weight="700" text-anchor="middle">CORE: poor nutrition</text>'
                 # roots (bottom)
                 '<rect x="50" y="200" width="150" height="30" rx="5" fill="rgba(245,158,11,0.12)" stroke="#F59E0B"/>'
                 '<rect x="260" y="200" width="150" height="30" rx="5" fill="rgba(245,158,11,0.12)" stroke="#F59E0B"/>'
                 '<text x="125" y="219" fill="#F59E0B" font-size="11" text-anchor="middle">Root: vacant posts</text>'
                 '<text x="335" y="219" fill="#F59E0B" font-size="11" text-anchor="middle">Root: delayed funds</text>'
                 # connectors
                 '<line x1="230" y1="100" x2="135" y2="44" stroke="#94a3b8" stroke-width="1"/>'
                 '<line x1="230" y1="100" x2="325" y2="44" stroke="#94a3b8" stroke-width="1"/>'
                 '<line x1="230" y1="136" x2="125" y2="200" stroke="#94a3b8" stroke-width="1"/>'
                 '<line x1="230" y1="136" x2="335" y2="200" stroke="#94a3b8" stroke-width="1"/>'
                 '</svg></div>')},
             {"t": "hbox", "color": "cyan", "html": "Roots are causes; branches are effects. "
              "Advocacy aims at a <strong>root you can actually move</strong> &mdash; here, the "
              "rules on posts and funds, not the stunting itself."},
         ]},

        {"type": "content", "label": "The Ask", "title": "Choose a winnable, specific ask",
         "blocks": [
             {"t": "body", "html": "An <strong>ask</strong> is the concrete thing you want a named "
              "decision-maker to do. Vague asks ('end poverty') cannot be granted; specific asks "
              "('release the sanctioned anganwadi budget by March') can be."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Specific &mdash; a clear, single action",
                 "Winnable &mdash; within the target's actual power",
                 "Owned &mdash; one named decision-maker can grant it",
                 "Meaningful &mdash; it genuinely improves lives"]},
         ]},

        {"type": "content", "label": "Trade-offs", "title": "Winnable vs ambitious",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Too ambitious", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Inspiring but unwinnable. Repeated defeat "
                   "demoralises supporters and signals weakness to opponents."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Too modest", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Easily won but changes little. Burns "
                   "credibility on something that did not need a campaign."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Aim for a <strong>stretch but credible</strong> "
              "ask &mdash; hard enough to matter, plausible enough to win, building momentum toward "
              "the bigger goal."},
         ]},

        {"type": "content", "label": "Framing", "title": "How you frame the issue shapes who supports it",
         "blocks": [
             {"t": "term", "word": "Framing",
              "def": "The choice of which aspect of an issue to emphasise &mdash; the values, "
              "metaphors and storyline through which people understand it. The same facts, framed "
              "differently, mobilise different audiences."},
             {"t": "body", "html": "Sanitation framed as <em>dignity</em> reaches a different "
              "audience than the same issue framed as <em>public health</em> or as <em>women's "
              "safety</em>. Frame for the audience you need to move."},
         ]},

        {"type": "content", "label": "Framing in Practice", "title": "From need to right",
         "blocks": [
             {"t": "body", "html": "A powerful shift in South Asian advocacy reframes a "
              "<strong>need</strong> ('the poor need food') as a <strong>right</strong> ('citizens "
              "have a right to food'). Rights create entitlements and accountability; needs invite "
              "charity."},
             {"t": "hbox", "color": "green", "html": "The Right to Food, Right to Education and "
              "Right to Information campaigns all made this move &mdash; turning a request into a "
              "claim the state is bound to honour."},
         ]},

        {"type": "content", "label": "Caution", "title": "Frame honestly",
         "blocks": [
             {"t": "body", "html": "Framing chooses emphasis; it must never distort facts. "
              "Exaggeration that is later exposed destroys the credibility that is an advocate's "
              "core asset &mdash; and it is hard to rebuild."},
             {"t": "hbox", "color": "red", "html": "The test: would the framing still hold if your "
              "opponent fact-checked it in public? If not, reframe &mdash; don't gamble your "
              "legitimacy."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Stakeholder &amp; Power Mapping"},

        {"type": "content", "label": "Map First", "title": "Know who is in the game",
         "blocks": [
             {"t": "body", "html": "Before choosing tactics, map the players. "
              "<strong>Stakeholder mapping</strong> identifies everyone who affects or is affected "
              "by your issue, and clarifies where each stands and how much they matter."},
             {"t": "hbox", "color": "cyan", "html": "It answers the two questions tactics depend "
              "on: <em>whom must we move</em>, and <em>who can help us move them</em>?"},
         ]},

        {"type": "content", "label": "Four Roles", "title": "Allies, opponents, targets, influentials",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Role", "Who they are", "What you do"],
              "rows": [
                  ["Targets", "Those with power to grant your ask", "Persuade or pressure them"],
                  ["Allies", "Those who share your goal", "Mobilise &amp; coordinate them"],
                  ["Opponents", "Those who resist the change", "Counter, neutralise or split them"],
                  ["Influentials", "Those targets listen to", "Win them to reach the target"]]},
             {"t": "hbox", "color": "amber", "html": "Note: the <strong>target</strong> is whoever "
              "can say yes &mdash; not necessarily your opponent. Often it is a busy official who "
              "is simply undecided."},
         ]},

        {"type": "content", "label": "The Spectrum", "title": "Everyone sits on a spectrum of support",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;padding:6px 0">'
                 '<svg viewBox="0 0 460 110" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;max-width:600px;height:auto">'
                 '<defs><linearGradient id="spec" x1="0" y1="0" x2="1" y2="0">'
                 '<stop offset="0" stop-color="#10B981"/><stop offset="0.5" stop-color="#94a3b8"/>'
                 '<stop offset="1" stop-color="#EF4444"/></linearGradient></defs>'
                 '<rect x="20" y="40" width="420" height="22" rx="11" fill="url(#spec)" opacity="0.85"/>'
                 '<text x="22" y="30" fill="#10B981" font-size="10">Active allies</text>'
                 '<text x="130" y="30" fill="#10B981" font-size="10">Passive allies</text>'
                 '<text x="225" y="30" fill="#94a3b8" font-size="10">Neutral</text>'
                 '<text x="300" y="30" fill="#EF4444" font-size="10">Passive opp.</text>'
                 '<text x="392" y="30" fill="#EF4444" font-size="10">Active opp.</text>'
                 '<text x="20" y="86" fill="#cbd5e1" font-size="11" font-weight="700">Goal: move each group one step toward you &mdash; not flip opponents overnight</text>'
                 '</svg></div>')},
             {"t": "hbox", "color": "green", "html": "Marshall Ganz's insight: you rarely convert "
              "active opponents. You win by moving <em>passive allies to active</em> and "
              "<em>neutrals to passive allies</em> &mdash; growing your side faster than theirs."},
         ]},

        {"type": "content", "label": "The Matrix", "title": "The support&ndash;influence matrix",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;padding:2px 0">'
                 '<svg viewBox="0 0 420 270" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;max-width:520px;height:auto">'
                 # quadrant fills
                 '<rect x="60" y="30" width="150" height="100" fill="rgba(245,158,11,0.10)"/>'
                 '<rect x="210" y="30" width="150" height="100" fill="rgba(16,185,129,0.12)"/>'
                 '<rect x="60" y="130" width="150" height="100" fill="rgba(148,163,184,0.10)"/>'
                 '<rect x="210" y="130" width="150" height="100" fill="rgba(99,102,241,0.10)"/>'
                 # axes
                 '<line x1="60" y1="30" x2="60" y2="230" stroke="#cbd5e1" stroke-width="1.5"/>'
                 '<line x1="60" y1="230" x2="360" y2="230" stroke="#cbd5e1" stroke-width="1.5"/>'
                 '<line x1="210" y1="30" x2="210" y2="230" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>'
                 '<line x1="60" y1="130" x2="360" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,4"/>'
                 # quadrant labels
                 '<text x="135" y="80" fill="#F59E0B" font-size="11" text-anchor="middle" font-weight="700">High influence /</text>'
                 '<text x="135" y="94" fill="#F59E0B" font-size="11" text-anchor="middle" font-weight="700">low support</text>'
                 '<text x="135" y="108" fill="#94a3b8" font-size="9" text-anchor="middle">PERSUADE</text>'
                 '<text x="285" y="80" fill="#10B981" font-size="11" text-anchor="middle" font-weight="700">High influence /</text>'
                 '<text x="285" y="94" fill="#10B981" font-size="11" text-anchor="middle" font-weight="700">high support</text>'
                 '<text x="285" y="108" fill="#94a3b8" font-size="9" text-anchor="middle">PARTNER / EMPOWER</text>'
                 '<text x="135" y="180" fill="#94a3b8" font-size="11" text-anchor="middle" font-weight="700">Low / low</text>'
                 '<text x="135" y="194" fill="#94a3b8" font-size="9" text-anchor="middle">MONITOR</text>'
                 '<text x="285" y="180" fill="#6366F1" font-size="11" text-anchor="middle" font-weight="700">Low influence /</text>'
                 '<text x="285" y="194" fill="#6366F1" font-size="11" text-anchor="middle" font-weight="700">high support</text>'
                 '<text x="285" y="208" fill="#94a3b8" font-size="9" text-anchor="middle">INFORM / MOBILISE</text>'
                 # axis titles
                 '<text x="210" y="256" fill="#cbd5e1" font-size="11" text-anchor="middle">Support for your cause &rarr;</text>'
                 '<text x="44" y="130" fill="#cbd5e1" font-size="11" text-anchor="middle" transform="rotate(-90 44 130)">Influence &rarr;</text>'
                 '</svg></div>')},
             {"t": "hbox", "color": "cyan", "html": "Plot each stakeholder on these two axes &mdash; "
              "<strong>influence</strong> and <strong>support</strong> &mdash; and the quadrant "
              "tells you how to treat them."},
         ]},

        {"type": "content", "label": "Plot Them", "title": "A worked stakeholder map",
         "blocks": [
             {"t": "chart", "canvas": "stakeScatter",
              "title": "Stakeholders by influence and support (illustrative)",
              "source": "Illustrative example",
              "type": "scatter",
              "data": {"datasets": [
                  {"label": "Allies", "data": [{"x": 8.5, "y": 9}, {"x": 6, "y": 8.5}, {"x": 3, "y": 7.5}],
                   "backgroundColor": "#10B981", "pointRadius": 9},
                  {"label": "Persuadable", "data": [{"x": 8, "y": 5}, {"x": 9, "y": 4}, {"x": 6.5, "y": 5.5}],
                   "backgroundColor": "#F59E0B", "pointRadius": 9},
                  {"label": "Opponents", "data": [{"x": 9, "y": 1.5}, {"x": 7, "y": 2}],
                   "backgroundColor": "#EF4444", "pointRadius": 9}]},
              "options": {"__js__": "{ scales:{ x:{ title:{display:true,text:'Influence \\u2192'}, min:0, max:10 }, y:{ title:{display:true,text:'Support \\u2192'}, min:0, max:10 } } }"}},
             {"t": "hbox", "color": "amber", "html": "The most valuable people are the "
              "<strong>amber</strong> ones: high influence, undecided. Winning a few of them often "
              "decides the campaign."},
         ]},

        {"type": "content", "label": "Opponents", "title": "Understand opponents, don't demonise them",
         "blocks": [
             {"t": "bullets", "items": [
                 "Map their <strong>interests</strong> &mdash; what do they actually want to protect?",
                 "Map their <strong>arguments</strong> &mdash; prepare credible rebuttals in advance",
                 "Look for <strong>splits</strong> &mdash; opponents are rarely a single bloc",
                 "Find shared ground where a deal is possible"]},
             {"t": "hbox", "color": "cyan", "html": "Today's opponent can be tomorrow's ally on the "
              "next issue. Hard on the problem, respectful to the person &mdash; it keeps doors open."},
         ]},

        {"type": "content", "label": "Coalitions", "title": "Allies are an asset to be organised",
         "blocks": [
             {"t": "body", "html": "Allies multiply your power &mdash; but only if coordinated. A "
              "loose coalition with a shared message and clear roles outweighs a dozen "
              "organisations acting alone and contradicting each other."},
             {"t": "hbox", "color": "green", "html": "Coalition-building is itself advocacy work: "
              "it converts scattered <em>power-to</em> into collective <em>power-with</em>. More on "
              "coalitions in Section Nine."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Strategy &amp; Theory of Change"},

        {"type": "content", "label": "The Spine", "title": "Strategy links every choice to your goal",
         "blocks": [
             {"t": "body", "html": "An advocacy <strong>strategy</strong> is a coherent argument "
              "about how change will happen: <em>if</em> we do these things with these people "
              "aimed at these targets, <em>then</em> this change follows &mdash; for these reasons."},
             {"t": "flow", "steps": [
                 "GOAL: the change you want",
                 "OBJECTIVES: steps toward it",
                 "TARGETS: who can deliver each",
                 "TACTICS: how you move them"]},
         ]},

        {"type": "content", "label": "Objectives", "title": "Set SMART advocacy objectives",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Letter", "Means", "Advocacy example"],
              "rows": [
                  ["S &mdash; Specific", "A single clear change", "State adopts a crèche policy"],
                  ["M &mdash; Measurable", "You'll know if it happened", "Notification issued, budget tagged"],
                  ["A &mdash; Achievable", "Within reach of your power", "The dept can act without new law"],
                  ["R &mdash; Relevant", "Tied to the real goal", "Crèches enable women's work"],
                  ["T &mdash; Time-bound", "A deadline", "Before the next budget cycle"]]},
             {"t": "hbox", "color": "amber", "html": "'Raise awareness' fails every SMART test. "
              "Awareness is a means; name the <em>decision</em> it is meant to produce."},
         ]},

        {"type": "content", "label": "Theory of Change", "title": "Make your assumptions explicit",
         "blocks": [
             {"t": "term", "word": "Theory of change",
              "def": "An explicit, testable account of how and why your activities are expected to "
              "lead to the change you seek &mdash; including the assumptions each step depends on."},
             {"t": "body", "html": "Writing it down exposes the weak links. The step most likely to "
              "break is usually a hidden <strong>assumption</strong> &mdash; 'we assume the "
              "minister will care if the media covers this'."},
         ]},

        {"type": "content", "label": "ToC, Drawn", "title": "From activities to impact",
         "blocks": [
             {"t": "flow", "steps": [
                 "ACTIVITIES: research, meetings, mobilising",
                 "OUTPUTS: report, coalition, media hits",
                 "OUTCOMES: target shifts position",
                 "IMPACT: policy changes; lives improve"]},
             {"t": "hbox", "color": "cyan", "html": "Outputs are what <em>you</em> control; "
              "outcomes are what <em>others</em> do because of you. Advocacy success lives at the "
              "outcome level &mdash; and so must your measurement (Section Ten)."},
         ]},

        {"type": "content", "label": "Pathways", "title": "Map more than one route to the goal",
         "blocks": [
             {"t": "body", "html": "Power is uncertain, so never bet on a single pathway. Plan a "
              "primary route (say, insider negotiation) and a backup (public pressure, or "
              "litigation) that can be activated if the first stalls."},
             {"t": "hbox", "color": "green", "html": "The inside and outside tracks reinforce each "
              "other: visible pressure outside makes the quiet deal inside look like the "
              "reasonable option."},
         ]},

        {"type": "content", "label": "Tactics by Target", "title": "Match the tactic to the target",
         "blocks": [
             {"t": "chart", "canvas": "tacticGrid",
              "title": "Which tactics suit which target (illustrative fit, 0&ndash;10)",
              "source": "Illustrative",
              "type": "bar",
              "data": {"labels": ["Minister", "Bureaucrat", "Legislator", "Public", "Courts"],
                       "datasets": [
                           {"label": "Insider meetings", "data": [8, 9, 6, 1, 2], "backgroundColor": "#0EA5E9"},
                           {"label": "Media pressure", "data": [7, 3, 6, 9, 2], "backgroundColor": "#F59E0B"},
                           {"label": "Mobilisation", "data": [6, 2, 7, 9, 1], "backgroundColor": "#10B981"},
                           {"label": "Litigation", "data": [3, 4, 2, 1, 10], "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ scales:{ x:{ stacked:false }, y:{ min:0, max:10, title:{display:true,text:'Fit'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "No tactic is universally best. A bureaucrat "
              "responds to evidence and quiet meetings; the public responds to story and "
              "mobilisation; a court responds to litigation. Match deliberately."},
         ]},

        {"type": "content", "label": "Resources", "title": "Be honest about what you can sustain",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>People:</strong> staff, volunteers, the affected constituency",
                 "<strong>Money:</strong> can you fund a multi-year effort?",
                 "<strong>Relationships:</strong> access, trust, allies, media contacts",
                 "<strong>Evidence &amp; credibility:</strong> your most portable asset"]},
             {"t": "hbox", "color": "red", "html": "Ambition must fit capacity. A strategy your "
              "organisation cannot resource is not bold &mdash; it is a plan to disappoint your "
              "constituency."},
         ]},

        {"type": "content", "label": "Write It Down", "title": "A one-page strategy you can revisit",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "The goal and the specific, SMART objective(s)",
                 "Targets and influentials &mdash; who can say yes",
                 "Tactics matched to each target",
                 "The theory of change and its key assumptions",
                 "Indicators of progress and the review date"]},
             {"t": "hbox", "color": "cyan", "html": "If it does not fit on a page, it is not yet a "
              "strategy. The discipline of compression forces the real choices into the open."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "The Policy Process &amp; Windows"},

        {"type": "content", "label": "How Policy Moves", "title": "Policy rarely changes on the merits alone",
         "blocks": [
             {"t": "body", "html": "Good evidence is necessary but never sufficient. Policy changes "
              "when problem, solution and politics <em>align</em> &mdash; and when an advocate is "
              "ready to act in the brief moment they do."},
             {"t": "hbox", "color": "cyan", "html": "The classic map of this is John Kingdon's "
              "<strong>multiple-streams</strong> framework, from <em>Agendas, Alternatives, and "
              "Public Policies</em> (1984)."},
         ]},

        {"type": "content", "label": "The Cycle", "title": "The stages of the policy process",
         "blocks": [
             {"t": "flow", "steps": [
                 "AGENDA-SETTING: issue gets attention",
                 "FORMULATION: options designed",
                 "ADOPTION: a decision is taken",
                 "IMPLEMENTATION: it is delivered",
                 "EVALUATION: does it work?"]},
             {"t": "hbox", "color": "amber", "html": "The model is tidy; reality is messy and "
              "loops. But it shows advocacy has a job at <em>every</em> stage &mdash; getting "
              "adopted is not the finish line; implementation often is the real fight."},
         ]},

        {"type": "content", "label": "Kingdon", "title": "Kingdon's three streams",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Stream", "What flows in it", "Advocate's job"],
              "rows": [
                  ["Problem", "Conditions defined as public problems", "Frame the condition as urgent"],
                  ["Policy", "Solutions &amp; proposals floating around", "Have a ready, workable solution"],
                  ["Politics", "Mood, elections, who holds power", "Read &amp; ride the political moment"]]},
             {"t": "body", "html": "Kingdon argued these three streams flow largely "
              "<em>independently</em>. Big change happens only when they are joined &mdash; the "
              "moment he calls a <strong>policy window</strong>."},
         ]},

        {"type": "content", "label": "Visualise", "title": "When the streams converge",
         "blocks": [
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;padding:4px 0">'
                 '<svg viewBox="0 0 460 230" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:100%;max-width:560px;height:auto">'
                 # three streams flowing right
                 '<path d="M20,50 C140,40 240,60 330,55" fill="none" stroke="#0EA5E9" stroke-width="6" opacity="0.7"/>'
                 '<path d="M20,115 C140,125 240,105 330,115" fill="none" stroke="#10B981" stroke-width="6" opacity="0.7"/>'
                 '<path d="M20,180 C140,170 240,185 330,175" fill="none" stroke="#6366F1" stroke-width="6" opacity="0.7"/>'
                 '<text x="22" y="40" fill="#0EA5E9" font-size="11" font-weight="700">PROBLEM</text>'
                 '<text x="22" y="105" fill="#10B981" font-size="11" font-weight="700">POLICY</text>'
                 '<text x="22" y="170" fill="#6366F1" font-size="11" font-weight="700">POLITICS</text>'
                 # convergence node
                 '<circle cx="350" cy="115" r="30" fill="rgba(245,158,11,0.18)" stroke="#F59E0B" stroke-width="2.5"/>'
                 '<path d="M330,55 L342,95" stroke="#94a3b8" stroke-width="1"/>'
                 '<path d="M330,175 L342,135" stroke="#94a3b8" stroke-width="1"/>'
                 '<text x="350" y="112" fill="#F59E0B" font-size="10" text-anchor="middle" font-weight="700">POLICY</text>'
                 '<text x="350" y="125" fill="#F59E0B" font-size="10" text-anchor="middle" font-weight="700">WINDOW</text>'
                 '<text x="395" y="119" fill="#cbd5e1" font-size="22">&rarr;</text>'
                 '<text x="350" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">an advocate ready here wins</text>'
                 '</svg></div>')},
             {"t": "hbox", "color": "cyan", "html": "A <strong>policy window</strong> is the brief "
              "opening when all three align. They close fast &mdash; advocacy is partly the art of "
              "being prepared when one opens."},
         ]},

        {"type": "content", "label": "Windows", "title": "What opens a policy window?",
         "blocks": [
             {"t": "bullets", "items": [
                 "A <strong>focusing event</strong> &mdash; a disaster, scandal or crisis",
                 "A <strong>change of government</strong> or a new minister",
                 "A <strong>budget or election cycle</strong> creating an opening",
                 "A <strong>court ruling</strong> that forces the issue",
                 "Shifting public mood &mdash; the 'national mood' in Kingdon's terms"]},
             {"t": "hbox", "color": "amber", "html": "You cannot always create a window &mdash; but "
              "you can keep a solution polished and a coalition warm, so you are ready the day one "
              "opens."},
         ]},

        {"type": "content", "label": "Entrepreneurs", "title": "Policy entrepreneurs join the streams",
         "blocks": [
             {"t": "term", "word": "Policy entrepreneur",
              "def": "In Kingdon's model, an actor who invests time and credibility to couple a "
              "ready solution to a recognised problem at the moment a political window opens. "
              "Advocates are, at their best, policy entrepreneurs."},
             {"t": "body", "html": "Their edge is preparation: a credible solution already drafted, "
              "relationships already built, and the alertness to recognise the window before it "
              "closes."},
         ]},

        {"type": "content", "label": "Agenda-Setting", "title": "Getting onto the agenda is half the battle",
         "blocks": [
             {"t": "body", "html": "Most issues never get debated at all &mdash; recall Lukes' "
              "<em>second face</em> of power. <strong>Agenda-setting</strong> is the work of "
              "forcing an ignored issue into public and official attention."},
             {"t": "hbox", "color": "green", "html": "Media coverage, striking data, a human story, "
              "or a focusing event can lift an issue onto the agenda &mdash; the necessary first "
              "step before any solution can be considered."},
         ]},

        {"type": "content", "label": "After the Win", "title": "Adoption is not implementation",
         "blocks": [
             {"t": "body", "html": "A law on paper changes nothing until it is funded, staffed and "
              "enforced. In South Asia the gap between a progressive law and its delivery is often "
              "where the real advocacy battle lies."},
             {"t": "hbox", "color": "red", "html": "Plan for the implementation fight from the "
              "start. Budget tracking, social audits and grievance redress are advocacy too &mdash; "
              "often the harder, longer half."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Tactics &amp; Messaging"},

        {"type": "content", "label": "Two Halves", "title": "Evidence and narrative together",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Evidence", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The credible case: data, research, costed "
                   "proposals. Earns you a seat at the table and survives scrutiny."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Narrative", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The human story that makes people care. "
                   "Moves hearts and builds the will to act on the evidence."}]}]},
             {"t": "hbox", "color": "green", "html": "Evidence without story is ignored; story "
              "without evidence is dismissed. Persuasion needs <strong>both the head and the "
              "heart</strong>."},
         ]},

        {"type": "content", "label": "The Message", "title": "Craft a clear, repeatable message",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Problem:</strong> what is wrong, in one line",
                 "<strong>Solution:</strong> the specific change you want",
                 "<strong>Action:</strong> exactly what the audience should do",
                 "<strong>Why now:</strong> the urgency &mdash; the window"]},
             {"t": "hbox", "color": "cyan", "html": "Discipline beats cleverness. One message, "
              "repeated consistently by everyone in the coalition, lands harder than ten clever "
              "ones that confuse."},
         ]},

        {"type": "content", "label": "Audience", "title": "Tailor the message, keep the ask",
         "blocks": [
             {"t": "body", "html": "The core ask stays fixed; the <strong>framing</strong> flexes "
              "by audience. A finance ministry hears cost-benefit; a community hears dignity and "
              "rights; an editor hears a story with a human face."},
             {"t": "hbox", "color": "amber", "html": "Speak to the audience's values, not your own. "
              "The question is never 'what convinces me?' but 'what moves <em>them</em>?'"},
         ]},

        {"type": "content", "label": "Messengers", "title": "Who says it matters as much as what is said",
         "blocks": [
             {"t": "body", "html": "The most credible messenger is often not the NGO but the "
              "<strong>affected person</strong> speaking for themselves, or a respected "
              "independent voice &mdash; a doctor, a judge, a community elder."},
             {"t": "hbox", "color": "green", "html": "Match the messenger to the audience: a "
              "scientist for a sceptical ministry, an affected mother for the evening news. "
              "Authenticity is the currency."},
         ]},

        {"type": "content", "label": "Channels", "title": "Media, digital and grassroots",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Channel", "Strength", "Watch-out"],
              "rows": [
                  ["Mainstream media", "Reach, legitimacy, agenda-setting", "You don't control the framing"],
                  ["Digital / social", "Speed, low cost, mobilising", "Echo chambers; the digital divide"],
                  ["Grassroots organising", "Depth, durability, legitimacy", "Slow; resource-intensive"],
                  ["Direct engagement", "Access to decision-makers", "Risk of co-option"]]},
             {"t": "hbox", "color": "red", "html": "Mind the <strong>digital divide</strong>: in "
              "much of South Asia an online-only campaign silently excludes women, the poor and "
              "rural communities &mdash; often the very people you represent."},
         ]},

        {"type": "content", "label": "Coalitions", "title": "Build coalitions that hold",
         "blocks": [
             {"t": "bullets", "items": [
                 "Agree a <strong>shared goal</strong> and a common message early",
                 "Define <strong>roles</strong> &mdash; who leads, who fronts, who funds",
                 "Make decisions transparently to keep trust",
                 "Let members keep their identity while acting together"]},
             {"t": "hbox", "color": "cyan", "html": "Diverse coalitions &mdash; unusual allies "
              "across sectors &mdash; signal that an issue is broad, not narrow self-interest. "
              "That breadth is itself persuasive."},
         ]},

        {"type": "content", "label": "Grassroots Power", "title": "Mobilisation turns numbers into pressure",
         "blocks": [
             {"t": "body", "html": "Decision-makers respond to organised constituencies. "
              "Grassroots mobilisation &mdash; public hearings, mass petitions, peaceful "
              "demonstrations &mdash; converts scattered grievance into visible, countable power."},
             {"t": "hbox", "color": "green", "html": "It also builds <strong>power-within</strong> "
              "and <strong>power-with</strong>: people who organise for one win are ready and "
              "confident for the next."},
         ]},

        {"type": "content", "label": "Framing, Again", "title": "Frame to expand, not shrink, your coalition",
         "blocks": [
             {"t": "body", "html": "A good frame is a <strong>bridge</strong>: it lets people who "
              "do not share your politics still support your ask. A narrow, partisan frame shrinks "
              "your base; an inclusive one grows it."},
             {"t": "quote", "text": "Whoever sets the terms of the debate tends to win it.",
              "attr": "&mdash; a maxim of strategic communication"},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Monitoring, Evaluation &amp; Learning"},

        {"type": "content", "label": "Why It's Hard", "title": "Advocacy is hard to measure &mdash; honestly",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Long &amp; non-linear:</strong> change can take years and arrive in leaps",
                 "<strong>Many actors:</strong> you are one of many pushing the same way",
                 "<strong>Attribution:</strong> who can claim a policy that 'everyone' wanted?",
                 "<strong>Counterfactual:</strong> would it have changed anyway?"]},
             {"t": "hbox", "color": "amber", "html": "These are real difficulties, not excuses. "
              "They mean advocacy needs <em>different</em> measurement tools &mdash; not none."},
         ]},

        {"type": "content", "label": "Shift the Question", "title": "Contribution, not attribution",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Attribution", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'We caused this change.' Almost never "
                   "provable in advocacy &mdash; too many hands on the lever."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Contribution", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'We plausibly helped, and here is the "
                   "evidence of how.' Honest, defensible, and far more useful."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Credible advocacy evaluation claims a "
              "<strong>contribution</strong> to change, traced through a plausible story &mdash; "
              "not sole credit."},
         ]},

        {"type": "content", "label": "Markers", "title": "Measure progress, not just the final win",
         "blocks": [
             {"t": "body", "html": "Because the final outcome is slow, track the intermediate "
              "<strong>signals of change</strong> that show your theory of change is working &mdash; "
              "long before the law is passed."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "A decision-maker's language or position shifts",
                 "Your issue reaches a committee or consultation",
                 "Media coverage rises; the frame you want spreads",
                 "Your coalition and constituency grow"]},
         ]},

        {"type": "content", "label": "Outcome Harvesting", "title": "Work backwards from observed change",
         "blocks": [
             {"t": "term", "word": "Outcome harvesting",
              "def": "An evaluation method that first identifies observable changes in actors' "
              "behaviour, then works backwards to assess whether and how the advocacy contributed "
              "&mdash; rather than testing against pre-set targets."},
             {"t": "hbox", "color": "cyan", "html": "It fits advocacy's unpredictability: you "
              "cannot always predict <em>which</em> change will come, but you can recognise and "
              "trace it once it does."},
         ]},

        {"type": "content", "label": "Other Tools", "title": "A small toolkit for advocacy ME&amp;L",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Method", "What it does", "Good for"],
              "rows": [
                  ["Outcome harvesting", "Finds &amp; verifies actual changes", "Unpredictable, emergent results"],
                  ["Contribution analysis", "Tests a plausible causal story", "Claiming a credible share"],
                  ["Process tracing", "Traces the chain of events", "Did our action move the next link?"],
                  ["Most significant change", "Collects stories of change", "Capturing the unexpected"]]},
             {"t": "hbox", "color": "amber", "html": "Pick the method to fit a slow, contested, "
              "multi-actor reality &mdash; not a results framework borrowed from service delivery."},
         ]},

        {"type": "content", "label": "Learning", "title": "Evaluate to learn, not just to report",
         "blocks": [
             {"t": "body", "html": "The point of advocacy ME&amp;L is to <strong>get better</strong>: "
              "to test whether your theory of change holds and adjust it. A finding that your "
              "assumption was wrong is a success, not a failure &mdash; if you act on it."},
             {"t": "hbox", "color": "green", "html": "Build in honest reflection points. The "
              "campaigns that win over years are the ones that learn fastest between rounds."},
         ]},

        {"type": "content", "label": "Track It", "title": "An advocacy-outcome timeline",
         "blocks": [
             {"t": "chart", "canvas": "outcomeTimeline",
              "title": "Intermediate outcomes accumulate before the policy win (illustrative)",
              "source": "Illustrative",
              "type": "line",
              "data": {"labels": ["Yr 1", "Yr 2", "Yr 3", "Yr 4", "Yr 5"],
                       "datasets": [
                           {"label": "Coalition members", "data": [4, 9, 15, 22, 26],
                            "borderColor": "#10B981", "tension": 0.3, "pointRadius": 4, "fill": False},
                           {"label": "Media mentions (10s)", "data": [1, 3, 6, 11, 14],
                            "borderColor": "#F59E0B", "tension": 0.3, "pointRadius": 4, "fill": False},
                           {"label": "Official engagements", "data": [0, 2, 5, 9, 13],
                            "borderColor": "#0EA5E9", "tension": 0.3, "pointRadius": 4, "fill": False}]},
              "options": {"__js__": "{ scales:{ y:{ min:0, title:{display:true,text:'Count'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The 'win' in year 5 rests on years of "
              "invisible progress. Tracking these markers keeps a long campaign motivated &mdash; "
              "and accountable &mdash; while the headline outcome is still out of reach."},
         ]},

        {"type": "content", "label": "Reporting", "title": "Report advocacy honestly to funders",
         "blocks": [
             {"t": "bullets", "items": [
                 "Claim <strong>contribution</strong>, never sole credit",
                 "Report the intermediate outcomes, not only the final win",
                 "Be candid about setbacks &mdash; they build trust",
                 "Show the learning that reshaped your strategy"]},
             {"t": "hbox", "color": "amber", "html": "Funders who understand advocacy expect "
              "non-linear progress. Over-claiming to impress them sets a trap you will be held to "
              "next year."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Ethics, Risk &amp; Sustainability"},

        {"type": "content", "label": "Legitimacy", "title": "By what right do you speak?",
         "blocks": [
             {"t": "body", "html": "An advocate's power rests on <strong>legitimacy</strong> &mdash; "
              "a credible claim to represent or serve those affected. Lose it and your evidence, "
              "access and moral authority all weaken at once."},
             {"t": "bullets", "sm": True, "items": [
                 "Mandate &mdash; who authorised you to speak?",
                 "Proximity &mdash; how close are you to the affected?",
                 "Accountability &mdash; to whom do you answer?",
                 "Track record &mdash; is your evidence reliable?"]},
         ]},

        {"type": "content", "label": "Accountability", "title": "Accountable to constituents first",
         "blocks": [
             {"t": "body", "html": "Advocacy organisations face a pull between funders (who pay) "
              "and constituents (whom they serve). The ethical anchor is clear: your first "
              "accountability is <strong>downward</strong>, to the people you claim to represent."},
             {"t": "hbox", "color": "red", "html": "When a funder's priorities and the community's "
              "needs diverge, the community must win &mdash; or your legitimacy is hollow."},
         ]},

        {"type": "content", "label": "Do No Harm", "title": "Advocacy can put people at risk",
         "blocks": [
             {"t": "body", "html": "Speaking out can expose the very people you represent to "
              "backlash &mdash; from employers, local power-holders or the state. "
              "<strong>Do-no-harm</strong> means weighing those risks <em>with</em> the community "
              "before you act."},
             {"t": "hbox", "color": "amber", "html": "Sometimes the safest, most ethical choice is "
              "to advocate quietly, or to protect identities &mdash; even when a loud campaign "
              "would suit the organisation better."},
         ]},

        {"type": "content", "label": "Civic Space", "title": "Shrinking civic space in South Asia",
         "blocks": [
             {"t": "body", "html": "Across the region, the space for civil society has narrowed: "
              "tighter NGO regulation, surveillance, and pressure on dissent. Advocates increasingly "
              "operate under real legal and political constraint."},
             {"t": "hbox", "color": "red", "html": "This is the operating environment, not a "
              "footnote. Strategy must account for what is legally and physically safe &mdash; for "
              "the organisation and for constituents."},
         ]},

        {"type": "content", "label": "FCRA", "title": "India's FCRA and foreign-funded advocacy",
         "blocks": [
             {"t": "body", "html": "India's <strong>Foreign Contribution (Regulation) Act</strong> "
              "governs NGOs' access to foreign funds. Amendments (notably in 2020) tightened "
              "compliance, barred sub-granting of foreign funds, and have been used to restrict "
              "organisations engaged in advocacy."},
             {"t": "hbox", "color": "amber", "html": "Stated honestly: FCRA materially shapes who "
              "can fund advocacy in India. Many groups diversify toward domestic funding to protect "
              "their independence. Know the current rules &mdash; they change."},
         ]},

        {"type": "content", "label": "Honesty", "title": "Evidence integrity is non-negotiable",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Never fabricate, cherry-pick or exaggerate data",
                 "Acknowledge uncertainty and the limits of your evidence",
                 "Correct mistakes openly and quickly",
                 "Frame for emphasis &mdash; never to mislead"]},
             {"t": "hbox", "color": "red", "html": "Credibility is built over years and lost in a "
              "day. One exposed exaggeration can sink a campaign &mdash; and damage the wider "
              "sector's standing."},
         ]},

        {"type": "content", "label": "Sustainability", "title": "Build power that outlasts the campaign",
         "blocks": [
             {"t": "bullets", "items": [
                 "Leave behind organised, confident communities &mdash; not dependency",
                 "Build local leadership, so the work survives staff turnover",
                 "Diversify funding to protect independence",
                 "Defend implementation &mdash; a win unwatched can be reversed"]},
             {"t": "hbox", "color": "green", "html": "The deepest measure of advocacy is not a "
              "single law won but <strong>power redistributed</strong> &mdash; people more able to "
              "claim their rights tomorrow than they were today."},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>A New Weave of Power, People &amp; Politics</em> &mdash; VeneKlasen &amp; Miller (power &amp; advocacy planning)",
                 "<em>Power: A Radical View</em> &mdash; Steven Lukes (the three faces of power)",
                 "<em>Agendas, Alternatives, and Public Policies</em> &mdash; John Kingdon (windows &amp; streams)",
                 "<em>Finding the Spaces for Change</em> &mdash; John Gaventa (the power cube, IDS)",
                 "Oxfam &amp; ODI advocacy &amp; influencing guides &mdash; practical, free online"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's <strong>Policy "
              "Analysis</strong>, <strong>Campaign Strategy</strong> and <strong>Community "
              "Organising</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Analyse power first</strong> &mdash; who decides, and how power really works",
                 "<strong>Choose a winnable, specific ask</strong> &mdash; issues, not problems",
                 "<strong>Map your stakeholders</strong> &mdash; move people one step toward you",
                 "<strong>Be ready for the window</strong> &mdash; align problem, policy and politics",
                 "<strong>Advocate WITH people, ethically</strong> &mdash; build power that lasts"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Advocacy Basics 101 &middot; Complete",
         "headline": "Now go shift<br>the power.",
         "byline": "Advocacy is a craft you build over years &mdash; analyse power, frame the "
                   "issue, map the players, seize the window, and stay accountable to the people "
                   "you serve. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
