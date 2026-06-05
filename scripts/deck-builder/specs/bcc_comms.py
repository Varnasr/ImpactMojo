# -*- coding: utf-8 -*-
"""
Behaviour Change Communication 101 — ImpactMojo 101 Series (native deck spec)
Foundational SBCC for development & public-health communicators in South Asia.
Build: python3 scripts/deck-builder/build.py bcc_comms
"""

DECK = {
    "slug": "bcc-comms",
    "title": "Behaviour Change Communication 101",
    "description": ("Behaviour Change Communication 101 — a free foundational course for "
                    "development and public-health communicators in South Asia. From the "
                    "awareness-action gap to behaviour theories, audience research, message "
                    "design, channels, campaigns and ethics — with India-centric examples. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Behaviour<br>Change<br>Communication",
         "sub": "From Awareness to Action &mdash; a Foundational Course in SBCC for "
                "Development &amp; Public-Health Communicators in South Asia",
         "tags": ["Theory-Grounded", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What BCC &amp; SBCC Are"},
             {"name": "Why Behaviour Is Hard to Change"},
             {"name": "Individual Behaviour Theories"},
             {"name": "Social &amp; Environmental Theories"},
             {"name": "Behavioural Economics &amp; Nudges"},
             {"name": "Knowing Your Audience"},
             {"name": "Formative Research"},
             {"name": "Designing Messages"},
             {"name": "Channels &amp; the Communication Mix"},
             {"name": "Campaigns &amp; Community Engagement"},
             {"name": "Monitoring, Ethics &amp; Examples"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What BCC &amp; SBCC Are"},

        {"type": "content", "label": "Definition", "title": "Communication that changes what people do",
         "blocks": [
             {"t": "body", "html": "Public-health and development work runs on behaviour &mdash; "
              "washing hands, using a toilet, attending antenatal care, immunising a child. "
              "<strong>Behaviour Change Communication (BCC)</strong> is the strategic use of "
              "communication to help people adopt and sustain healthier, safer behaviours."},
             {"t": "term", "word": "Behaviour Change Communication (BCC)",
              "def": "An evidence-based, planned process that uses communication to promote and "
              "sustain individual, community and societal behaviour change &mdash; not to inform "
              "for its own sake, but to move people from intention to action."},
             {"t": "hbox", "color": "cyan", "html": "BCC is not advertising and not health "
              "education alone. It is communication designed around a specific behaviour, a "
              "specific audience and the barriers between them."},
         ]},

        {"type": "content", "label": "BCC &rarr; SBCC", "title": "Why the field added an 'S'",
         "blocks": [
             {"t": "body", "html": "Early programmes focused on the individual: give a person the "
              "right message and they will change. Practitioners learned that behaviour is also "
              "shaped by families, norms, services and policy &mdash; so the field broadened to "
              "<strong>Social and Behaviour Change Communication (SBCC)</strong>."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "BCC (older lens)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Focus on the individual decision. Persuade "
                   "the person; assume the environment will follow."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "SBCC (current lens)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Work across individual, community and "
                   "social-norm levels at once &mdash; and address the services and policies that "
                   "enable or block the behaviour."}]}]},
         ]},

        {"type": "content", "label": "The Core Claim", "title": "Beyond awareness, towards action",
         "blocks": [
             {"t": "flow", "steps": [
                 "AWARENESS: 'I have heard of ORS'",
                 "KNOWLEDGE: 'I know it treats dehydration'",
                 "INTENTION: 'I plan to use it'",
                 "ACTION: 'I gave it during the last episode'",
                 "MAINTENANCE: 'I use it every time'"]},
             {"t": "hbox", "color": "amber", "html": "Most campaigns stop at awareness. SBCC's job "
              "is the whole chain &mdash; and especially the drop-offs between each step."},
         ]},

        {"type": "content", "label": "The Central Problem", "title": "The awareness-action gap",
         "blocks": [
             {"t": "chart", "canvas": "awarenessFunnel",
              "title": "The behaviour funnel: people fall away at every step (illustrative)",
              "source": "Illustrative &mdash; shape typical of SBCC programme data",
              "type": "bar",
              "data": {"labels": ["Aware", "Knows correctly", "Intends", "Tries once", "Practises regularly"],
                       "datasets": [{"label": "Share of audience (%)",
                                     "data": [90, 70, 50, 32, 18],
                                     "backgroundColor": ["#0EA5E9", "#0EA5E9", "#6366F1", "#F59E0B", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100, title:{display:true,text:'% of audience'}} } }"}},
             {"t": "hbox", "color": "red", "html": "High awareness, low practice is the signature "
              "pattern of weak campaigns. The gap &mdash; not the awareness number &mdash; is where "
              "the real work lies."},
         ]},

        {"type": "content", "label": "What SBCC Is Not", "title": "Common misconceptions",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Not 'more posters'.</strong> Volume of messaging is not the same as change.",
                 "<strong>Not one-off.</strong> Behaviour change needs sustained, repeated contact.",
                 "<strong>Not blame.</strong> 'People are ignorant' ignores real barriers.",
                 "<strong>Not only mass media.</strong> Interpersonal contact often does the heavy lifting."]},
             {"t": "hbox", "color": "amber", "html": "If a campaign assumes that telling people the "
              "facts is enough, it has already mistaken the problem."},
         ]},

        {"type": "content", "label": "Where SBCC Fits", "title": "Communication is one lever, not the only one",
         "blocks": [
             {"t": "body", "html": "SBCC works best alongside the other levers of change. A "
              "handwashing message fails without soap and water nearby; an immunisation message "
              "fails without a functioning session and a friendly nurse."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "SBCC can do", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Shift attitudes, norms and intentions",
                      "Build skills and self-efficacy",
                      "Cue and remind at the right moment"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "SBCC cannot do alone", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Supply soap, toilets, vaccines or clinics",
                      "Fix a hostile or distant service",
                      "Remove the cost of changing"]}]}]},
         ]},

        {"type": "content", "label": "Roadmap", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Understand", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Why behaviour resists change",
                      "Individual and social theories",
                      "Behavioural economics and nudges"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Design &amp; Deliver", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Audience, research and messages",
                      "Channels and campaigns",
                      "Monitoring, ethics and Indian examples"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Throughout, examples come from India and the "
              "wider region &mdash; the behaviours and campaigns you will actually meet at work."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Why Behaviour Is Hard to Change"},

        {"type": "content", "label": "The Hard Truth", "title": "Knowledge alone rarely changes behaviour",
         "blocks": [
             {"t": "body", "html": "The oldest assumption in health communication is that if people "
              "<em>knew</em> better, they would <em>do</em> better. Decades of evidence say "
              "otherwise: knowledge is necessary but almost never sufficient."},
             {"t": "quote",
              "text": "We are not short of people who know smoking is harmful, that handwashing "
              "saves lives, that helmets prevent injury. Knowing is the easy part.",
              "attr": "&mdash; a recurring lesson of SBCC practice"},
             {"t": "hbox", "color": "red", "html": "If knowledge changed behaviour, no doctor "
              "would smoke. This single insight reshapes how you design every campaign."},
         ]},

        {"type": "content", "label": "Two Gaps", "title": "The knowledge gap and the intention-action gap",
         "blocks": [
             {"t": "flow", "steps": [
                 "KNOWLEDGE GAP: don't know what or how",
                 "ATTITUDE: know, but don't value it",
                 "INTENTION: value it, plan to act",
                 "INTENTION-ACTION GAP: plan, but don't do",
                 "BEHAVIOUR: actually do it"]},
             {"t": "hbox", "color": "amber", "html": "Two different gaps need two different "
              "responses. Information closes the first; cues, skills and removing friction close "
              "the second &mdash; the harder, more neglected one."},
         ]},

        {"type": "content", "label": "Intention-Action Gap", "title": "Most people who intend, still don't act",
         "blocks": [
             {"t": "chart", "canvas": "intentionGap",
              "title": "From intention to action, people leak away (illustrative)",
              "source": "Illustrative &mdash; pattern documented across behaviours",
              "type": "bar",
              "data": {"labels": ["Intend to change", "Make a plan", "Act once", "Sustain it"],
                       "datasets": [{"label": "% of those who intended",
                                     "data": [100, 65, 45, 25],
                                     "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100, title:{display:true,text:'% of intenders'}} } }"}},
             {"t": "hbox", "color": "cyan", "html": "Good intentions are real but fragile. The "
              "design question is not 'how do I create intention?' but 'how do I help intention "
              "survive contact with daily life?'"},
         ]},

        {"type": "content", "label": "Why Intentions Fail", "title": "What stands between wanting and doing",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Forgetting:</strong> the moment to act passes unnoticed",
                 "<strong>Friction:</strong> the behaviour is even slightly inconvenient",
                 "<strong>Habit:</strong> the old behaviour fires automatically",
                 "<strong>Present bias:</strong> the cost is now, the benefit is later",
                 "<strong>Competing demands:</strong> survival crowds out 'good for you'"]},
             {"t": "hbox", "color": "green", "html": "Each failure has a design fix &mdash; "
              "reminders, defaults, making the act easy, linking to existing routines. SBCC is "
              "as much about friction as about persuasion."},
         ]},

        {"type": "content", "label": "Social Barriers", "title": "Behaviour is watched, judged and shared",
         "blocks": [
             {"t": "body", "html": "Few behaviours are private. A young wife's antenatal visit, a "
              "man's vasectomy, a girl's menstrual hygiene &mdash; all are governed by what "
              "families, neighbours and elders permit, expect or shame."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "indigo", "title": "Social barriers", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Norms about what 'people like us' do",
                      "Family gatekeepers &mdash; mothers-in-law, husbands",
                      "Stigma, gossip and reputation"]}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why it matters", "blocks": [
                  {"t": "body", "cls": "sm", "html": "An individual may be fully convinced and "
                   "still not act, because acting would defy the people they live among."}]}]},
         ]},

        {"type": "content", "label": "Structural Barriers", "title": "Sometimes the barrier is not in the head",
         "blocks": [
             {"t": "body", "html": "No amount of messaging overcomes a missing toilet, an absent "
              "nurse, a four-hour walk to a clinic, or a wage lost to attend a session. These are "
              "<strong>structural barriers</strong> &mdash; outside the individual's control."},
             {"t": "hbox", "color": "red", "html": "Diagnosing a structural barrier as an "
              "attitude problem is the most expensive mistake in SBCC. You will run a campaign "
              "against a wall that no message can move."},
         ]},

        {"type": "content", "label": "Ability vs Motivation", "title": "Make it easy before you make it desired",
         "blocks": [
             {"t": "body", "html": "When a behaviour is hard, even strong motivation fails. When a "
              "behaviour is easy, even modest motivation succeeds. Practitioners often over-invest "
              "in motivation and under-invest in <strong>making the behaviour easy</strong>."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Reduce friction", "label": "Bring the behaviour closer, simpler, cheaper, "
                  "faster", "color": "green"},
                 {"num": "Then motivate", "label": "Add reasons once the act is genuinely doable",
                  "color": "cyan"}]},
         ]},

        {"type": "content", "label": "Implication", "title": "Design around barriers, not assumptions",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Find the real barrier</strong> before choosing a message",
                 "<strong>Separate the gaps</strong> &mdash; knowledge vs intention vs ability",
                 "<strong>Address norms</strong>, not just individuals",
                 "<strong>Flag structural blocks</strong> to those who can fix them",
                 "<strong>Make the behaviour easy</strong> wherever you can"]},
             {"t": "hbox", "color": "cyan", "html": "The rest of this course is, in effect, a "
              "toolkit for doing exactly this &mdash; barrier by barrier."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Individual Behaviour Theories"},

        {"type": "content", "label": "Why Theory", "title": "Theories are maps of why people act",
         "blocks": [
             {"t": "body", "html": "A behaviour theory is a tested explanation of what drives a "
              "behaviour. It tells you <em>which levers to pull</em> &mdash; so you design from "
              "evidence, not instinct. This section covers three classic individual-level theories."},
             {"t": "term", "word": "Behaviour-change theory",
              "def": "A structured account of the factors that cause a behaviour and how they "
              "interact &mdash; used to diagnose barriers and select communication strategies."},
         ]},

        {"type": "content", "label": "Health Belief Model", "title": "The Health Belief Model (HBM)",
         "blocks": [
             {"t": "body", "html": "One of the earliest health-behaviour theories. It says people "
              "act when they believe a threat is real <em>and</em> that acting is worth it. "
              "Developed by U.S. public-health researchers in the 1950s."},
             {"t": "table",
              "head": ["Construct", "The question in the person's head"],
              "rows": [
                  ["Perceived susceptibility", "Could this happen to me?"],
                  ["Perceived severity", "Would it be serious if it did?"],
                  ["Perceived benefits", "Will this action actually help?"],
                  ["Perceived barriers", "What will it cost me to act?"],
                  ["Cues to action", "What prompts me to do it now?"],
                  ["Self-efficacy", "Can I actually do it?"]]},
         ]},

        {"type": "content", "label": "HBM in Practice", "title": "Reading a behaviour through the HBM",
         "blocks": [
             {"t": "body", "html": "Take an expectant mother skipping antenatal check-ups. The HBM "
              "asks: does she think complications could affect <em>her</em>? Does she see them as "
              "serious? Does she believe check-ups help more than they cost?"},
             {"t": "hbox", "color": "cyan", "html": "The model's gift to communicators: "
              "<strong>perceived barriers usually outweigh perceived benefits.</strong> Lowering "
              "the felt cost of acting often beats raising fear of the disease."},
         ]},

        {"type": "content", "label": "Theory of Planned Behaviour", "title": "Theory of Planned Behaviour (Ajzen)",
         "blocks": [
             {"t": "body", "html": "Icek Ajzen's Theory of Planned Behaviour &mdash; an extension "
              "of the earlier Theory of Reasoned Action &mdash; holds that behaviour follows from "
              "<strong>intention</strong>, which is built from three things."},
             {"t": "flow", "steps": [
                 "ATTITUDE: do I view the behaviour positively?",
                 "SUBJECTIVE NORM: do important others approve?",
                 "PERCEIVED CONTROL: do I feel able to do it?",
                 "&rarr; INTENTION &rarr; BEHAVIOUR"]},
             {"t": "hbox", "color": "amber", "html": "The crucial addition over Reasoned Action is "
              "<strong>perceived behavioural control</strong> &mdash; the felt sense of 'I can do "
              "this', which also directly affects whether the act happens."},
         ]},

        {"type": "content", "label": "TPB in Practice", "title": "Three levers, three messages",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Attitude", "label": "Show the behaviour as good and rewarding", "color": "cyan"},
                 {"num": "Norms", "label": "Show that respected others do &amp; approve of it", "color": "indigo"},
                 {"num": "Control", "label": "Show it is feasible &mdash; demonstrate, simplify", "color": "green"}]},
             {"t": "hbox", "color": "cyan", "html": "TPB tells you which lever is weak for "
              "<em>your</em> audience &mdash; and therefore which message to lead with. Don't "
              "preach attitude when the real block is felt control."},
         ]},

        {"type": "content", "label": "Stages of Change", "title": "The Transtheoretical Model (Prochaska &amp; DiClemente)",
         "blocks": [
             {"t": "body", "html": "Prochaska and DiClemente observed that people change in "
              "<strong>stages</strong>, not in one leap. Their Transtheoretical Model maps the "
              "journey &mdash; and warns against treating everyone as if they are ready to act."},
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:8px 0">'
                 '<svg viewBox="0 0 520 520" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:340px;max-width:80%;height:auto;font-family:inherit">'
                 '<circle cx="260" cy="260" r="180" fill="none" stroke="#1C1917" stroke-width="2" stroke-dasharray="6,7"/>'
                 # five nodes around the wheel
                 '<circle cx="260" cy="80" r="40" fill="#0EA5E9"/>'
                 '<circle cx="431" cy="204" r="40" fill="#6366F1"/>'
                 '<circle cx="366" cy="406" r="40" fill="#F59E0B"/>'
                 '<circle cx="154" cy="406" r="40" fill="#10B981"/>'
                 '<circle cx="89" cy="204" r="40" fill="#EF4444"/>'
                 '<text x="260" y="78" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">Pre-</text>'
                 '<text x="260" y="92" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">contempl.</text>'
                 '<text x="431" y="202" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">Contempl-</text>'
                 '<text x="431" y="216" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">ation</text>'
                 '<text x="366" y="404" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">Prepar-</text>'
                 '<text x="366" y="418" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">ation</text>'
                 '<text x="154" y="411" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">Action</text>'
                 '<text x="89" y="202" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">Mainten-</text>'
                 '<text x="89" y="216" text-anchor="middle" fill="#fff" font-size="13" font-weight="700">ance</text>'
                 '<text x="260" y="265" text-anchor="middle" fill="#1C1917" font-size="15" font-weight="700">STAGES OF</text>'
                 '<text x="260" y="286" text-anchor="middle" fill="#1C1917" font-size="15" font-weight="700">CHANGE</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "Match the Stage", "title": "Meet people where they are",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Stage", "Where the person is", "Communication job"],
              "rows": [
                  ["Precontemplation", "Not even considering change", "Raise awareness, plant doubt"],
                  ["Contemplation", "Weighing pros and cons", "Tip the balance; show benefits"],
                  ["Preparation", "Intending to act soon", "Give a concrete plan and skills"],
                  ["Action", "Doing it, recently started", "Reinforce, reward, problem-solve"],
                  ["Maintenance", "Sustaining the new behaviour", "Prevent relapse, build habit"]]},
             {"t": "hbox", "color": "red", "html": "Aiming an 'act now' message at someone in "
              "precontemplation wastes both your effort and their patience. Segment by stage."},
         ]},

        {"type": "content", "label": "Using the Theories", "title": "No single theory explains everything",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>HBM</strong> is strong on perceived threat and the cost-benefit of acting",
                 "<strong>TPB</strong> adds social approval and felt control over the act",
                 "<strong>Stages of Change</strong> reminds you that readiness varies",
                 "Good programmes <strong>borrow constructs</strong> from several, fit to the behaviour"]},
             {"t": "hbox", "color": "green", "html": "Treat theories as a diagnostic toolbox, not "
              "doctrine. Pick the constructs that explain <em>your</em> behaviour and audience."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Social &amp; Environmental Theories"},

        {"type": "content", "label": "Beyond the Individual", "title": "Behaviour lives in a social ecosystem",
         "blocks": [
             {"t": "body", "html": "Individual theories explain the person; social theories explain "
              "the world around them. The <strong>socio-ecological model</strong> reminds us that "
              "behaviour sits inside nested layers of influence."},
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:6px 0">'
                 '<svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:520px;max-width:100%;height:auto;font-family:inherit">'
                 '<rect x="10" y="20" width="500" height="260" rx="12" fill="#EF4444" opacity="0.12" stroke="#EF4444"/>'
                 '<rect x="60" y="50" width="400" height="200" rx="12" fill="#F59E0B" opacity="0.14" stroke="#F59E0B"/>'
                 '<rect x="120" y="80" width="280" height="140" rx="12" fill="#6366F1" opacity="0.16" stroke="#6366F1"/>'
                 '<rect x="180" y="110" width="160" height="80" rx="12" fill="#10B981" opacity="0.18" stroke="#10B981"/>'
                 '<circle cx="260" cy="150" r="32" fill="#0EA5E9"/>'
                 '<text x="260" y="155" text-anchor="middle" fill="#fff" font-size="14" font-weight="700">Person</text>'
                 '<text x="260" y="103" text-anchor="middle" fill="#10B981" font-size="12" font-weight="700">FAMILY / PEERS</text>'
                 '<text x="260" y="73" text-anchor="middle" fill="#6366F1" font-size="12" font-weight="700">COMMUNITY</text>'
                 '<text x="260" y="43" text-anchor="middle" fill="#F59E0B" font-size="12" font-weight="700">INSTITUTIONS / SERVICES</text>'
                 '<text x="260" y="270" text-anchor="middle" fill="#EF4444" font-size="12" font-weight="700">POLICY / SOCIETY</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "Social Cognitive Theory", "title": "Social Cognitive Theory (Bandura)",
         "blocks": [
             {"t": "body", "html": "Albert Bandura showed that people learn behaviours by "
              "<strong>observing others</strong> &mdash; modelling &mdash; and by seeing those "
              "others rewarded. Change is a constant interplay between the person, their behaviour "
              "and their environment (reciprocal determinism)."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Observational learning:</strong> we copy credible models",
                 "<strong>Vicarious reinforcement:</strong> we act when models are rewarded",
                 "<strong>Self-efficacy:</strong> belief in one's own ability to do it"]},
             {"t": "hbox", "color": "cyan", "html": "This is the theoretical engine behind "
              "role-model storytelling and entertainment-education &mdash; show a relatable "
              "character succeeding, and viewers believe they can too."},
         ]},

        {"type": "content", "label": "Self-Efficacy", "title": "Self-efficacy: 'I can do this'",
         "blocks": [
             {"t": "term", "word": "Self-efficacy (Bandura)",
              "def": "A person's belief in their own capacity to perform a specific behaviour. "
              "It is behaviour-specific &mdash; high for one act, low for another &mdash; and is a "
              "powerful predictor of whether intention becomes action."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Mastery", "label": "Small successes build belief &mdash; demonstrate, "
                  "let them practise", "color": "green"},
                 {"num": "Modelling", "label": "Seeing 'someone like me' succeed raises efficacy",
                  "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Diffusion of Innovations", "title": "Diffusion of Innovations (Rogers)",
         "blocks": [
             {"t": "body", "html": "Everett Rogers described how new ideas and practices spread "
              "through a community over time &mdash; not all at once, but in waves, starting with a "
              "small group of risk-tolerant adopters."},
             {"t": "chart", "canvas": "diffusionCurve",
              "title": "Adopter categories spread over time (Rogers)",
              "source": "Rogers, Diffusion of Innovations &mdash; standard proportions",
              "type": "bar",
              "data": {"labels": ["Innovators", "Early adopters", "Early majority", "Late majority", "Laggards"],
                       "datasets": [{"label": "Share of population (%)",
                                     "data": [2.5, 13.5, 34, 34, 16],
                                     "backgroundColor": ["#10B981", "#0EA5E9", "#6366F1", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:40, title:{display:true,text:'% of population'}} } }"}},
         ]},

        {"type": "content", "label": "Using Diffusion", "title": "Find and back the early adopters",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Innovators &amp; early adopters</strong> are your entry point &mdash; reach them first",
                 "<strong>Opinion leaders</strong> bridge to the majority; their endorsement matters most",
                 "<strong>The early majority</strong> waits for proof from people like them",
                 "<strong>Laggards</strong> need the behaviour to become the new normal before they move"]},
             {"t": "hbox", "color": "green", "html": "Don't try to convert everyone at once. Seed "
              "the behaviour with credible early adopters and let it diffuse along social ties."},
         ]},

        {"type": "content", "label": "Social Norms", "title": "We do what we think others do",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Descriptive norm", "blocks": [
                  {"t": "body", "cls": "sm", "html": "What I believe most people actually do "
                   "&mdash; 'everyone here defecates in the open'."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Injunctive norm", "blocks": [
                  {"t": "body", "cls": "sm", "html": "What I believe most people approve of "
                   "&mdash; 'using a toilet is what respectable families do'."}]}]},
             {"t": "hbox", "color": "amber", "html": "Powerful and double-edged: telling people "
              "'too many still defecate in the open' can <em>normalise</em> the very behaviour you "
              "oppose. Highlight the growing healthy norm instead."},
         ]},

        {"type": "content", "label": "Norms in Practice", "title": "Shifting the norm, not just the person",
         "blocks": [
             {"t": "body", "html": "When a behaviour is governed by norms, persuading individuals "
              "one by one is slow and fragile. Changing the <strong>shared expectation</strong> "
              "lets many people change together, with social cover."},
             {"t": "hbox", "color": "cyan", "html": "Public commitments, community pledges and "
              "visible role models work because they change what people believe their neighbours "
              "expect &mdash; the heart of community-led approaches in the next sections."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Behavioural Economics &amp; Nudges"},

        {"type": "content", "label": "A Different Lens", "title": "People are predictably irrational",
         "blocks": [
             {"t": "body", "html": "Classical models assume people weigh costs and benefits "
              "rationally. Behavioural economics shows we rely on mental shortcuts and are swayed "
              "by how choices are framed &mdash; in ways that are systematic and predictable."},
             {"t": "hbox", "color": "cyan", "html": "This is liberating for communicators: if "
              "behaviour responds to context and framing, then small design changes &mdash; not "
              "just big persuasion &mdash; can move it."},
         ]},

        {"type": "content", "label": "COM-B", "title": "The COM-B model (Michie)",
         "blocks": [
             {"t": "body", "html": "Susan Michie's COM-B model sits at the centre of the "
              "<strong>Behaviour Change Wheel</strong>. It says any behaviour requires three "
              "things at once &mdash; remove any one and the behaviour fails."},
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:8px 0">'
                 '<svg viewBox="0 0 460 300" xmlns="http://www.w3.org/2000/svg" '
                 'style="width:460px;max-width:100%;height:auto;font-family:inherit">'
                 '<circle cx="160" cy="120" r="80" fill="#0EA5E9" opacity="0.85"/>'
                 '<circle cx="300" cy="120" r="80" fill="#6366F1" opacity="0.85"/>'
                 '<circle cx="230" cy="210" r="80" fill="#10B981" opacity="0.85"/>'
                 '<text x="120" y="115" text-anchor="middle" fill="#fff" font-size="17" font-weight="700">CAPABILITY</text>'
                 '<text x="120" y="138" text-anchor="middle" fill="#fff" font-size="12">can I?</text>'
                 '<text x="340" y="115" text-anchor="middle" fill="#fff" font-size="17" font-weight="700">OPPORTUNITY</text>'
                 '<text x="340" y="138" text-anchor="middle" fill="#fff" font-size="12">does context allow?</text>'
                 '<text x="230" y="235" text-anchor="middle" fill="#fff" font-size="17" font-weight="700">MOTIVATION</text>'
                 '<text x="230" y="258" text-anchor="middle" fill="#fff" font-size="12">do I want to?</text>'
                 '<text x="230" y="158" text-anchor="middle" fill="#1C1917" font-size="15" font-weight="700">BEHAVIOUR</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "COM-B in Use", "title": "Diagnose which component is missing",
         "blocks": [
             {"t": "table",
              "head": ["Component", "Ask", "If missing, then&hellip;"],
              "rows": [
                  ["Capability", "Do they know how &amp; feel able?", "Teach, demonstrate, build skills"],
                  ["Opportunity", "Does the environment allow it?", "Fix access, cues, norms, time"],
                  ["Motivation", "Do they want to, in the moment?", "Reasons, emotion, habit, incentives"]]},
             {"t": "hbox", "color": "green", "html": "COM-B's discipline: <strong>diagnose before "
              "you prescribe.</strong> A motivation campaign cannot fix an opportunity problem."},
         ]},

        {"type": "content", "label": "Cognitive Biases", "title": "Shortcuts that shape decisions",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Present bias:</strong> we over-value now over later",
                 "<strong>Loss aversion:</strong> losing ₹100 hurts more than gaining ₹100 pleases",
                 "<strong>Status quo bias:</strong> we stick with the default",
                 "<strong>Social proof:</strong> we follow what others seem to do",
                 "<strong>Availability:</strong> vivid recent events feel more likely"]},
             {"t": "hbox", "color": "amber", "html": "Biases are not flaws to lecture away &mdash; "
              "they are levers. Design with the grain of how minds actually work."},
         ]},

        {"type": "content", "label": "Nudges", "title": "Defaults, framing and commitment",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Defaults", "label": "Make the healthy option the automatic one &mdash; "
                  "opt-out, not opt-in", "color": "cyan"},
                 {"num": "Framing", "label": "Same fact, better wording &mdash; '90% protected' vs "
                  "'10% at risk'", "color": "indigo"},
                 {"num": "Commitment", "label": "Small public pledges make people follow through",
                  "color": "green"}]},
             {"t": "term", "word": "Nudge",
              "def": "A change in how choices are presented that steers behaviour predictably "
              "without forbidding options or changing economic incentives &mdash; popularised by "
              "Thaler &amp; Sunstein."},
         ]},

        {"type": "content", "label": "Choice Architecture", "title": "The design of the decision shapes the choice",
         "blocks": [
             {"t": "body", "html": "Every decision happens inside an environment &mdash; the order "
              "of options, the default, the friction, the salient cue. The "
              "<strong>choice architecture</strong> is never neutral; the only question is whether "
              "you designed it deliberately."},
             {"t": "hbox", "color": "cyan", "html": "Putting the immunisation register at the "
              "anganwadi door, or making ORS the first item on a shelf, is choice architecture "
              "&mdash; quiet design that beats loud persuasion."},
         ]},

        {"type": "content", "label": "EAST", "title": "A practical checklist: make it EAST",
         "blocks": [
             {"t": "table",
              "head": ["Principle", "Meaning"],
              "rows": [
                  ["Easy", "Reduce friction; use simple defaults and clear steps"],
                  ["Attractive", "Draw attention; make it personal and appealing"],
                  ["Social", "Show that others are doing it; harness norms"],
                  ["Timely", "Prompt at the moment people are most receptive"]]},
             {"t": "hbox", "color": "green", "html": "EAST, from the UK Behavioural Insights Team, "
              "is a quick field test for any behavioural intervention you design."},
         ]},

        {"type": "content", "label": "Limits", "title": "Nudges are not a substitute for systems",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Nudges work at the margin &mdash; they don't supply missing services",
                 "Overused, they can feel manipulative or paternalistic",
                 "They must be transparent and in the person's genuine interest",
                 "Structural barriers still need structural fixes"]},
             {"t": "hbox", "color": "amber", "html": "A nudge towards handwashing is no answer to a "
              "village with no water. Use behavioural design <em>and</em> fix the system."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Knowing Your Audience"},

        {"type": "content", "label": "First Principle", "title": "There is no such thing as 'the public'",
         "blocks": [
             {"t": "body", "html": "'The community' is not one audience. A new mother, her "
              "mother-in-law, the ASHA, the village head and the absent migrant husband each see a "
              "behaviour differently. Speaking to everyone usually means reaching no one."},
             {"t": "quote", "text": "If you are talking to everybody, you are talking to nobody.",
              "attr": "&mdash; a maxim of audience-centred communication"},
         ]},

        {"type": "content", "label": "Segmentation", "title": "Audience segmentation",
         "blocks": [
             {"t": "term", "word": "Audience segmentation",
              "def": "Dividing a broad population into smaller groups that share characteristics, "
              "barriers or motivations &mdash; so messages, channels and messengers can be tailored "
              "to each group rather than averaged across all."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Demographic:</strong> age, sex, education, location",
                 "<strong>Behavioural:</strong> current practice and stage of change",
                 "<strong>Psychographic:</strong> values, fears, aspirations",
                 "<strong>By barrier:</strong> grouped by what stops them"]},
         ]},

        {"type": "content", "label": "Three Audiences", "title": "Primary, secondary and influencing audiences",
         "blocks": [
             {"t": "flow", "steps": [
                 "PRIMARY: the person whose behaviour must change",
                 "SECONDARY: those close who shape that behaviour",
                 "INFLUENCING / TERTIARY: leaders &amp; policy who set the climate"]},
             {"t": "hbox", "color": "cyan", "html": "Example &mdash; primary: the pregnant woman; "
              "secondary: husband and mother-in-law; influencing: the panchayat, the ASHA, local "
              "health policy. A good campaign speaks to all three layers."},
         ]},

        {"type": "content", "label": "Gatekeepers", "title": "The people who hold the gate",
         "blocks": [
             {"t": "body", "html": "In much of South Asia, a woman's health behaviour is often "
              "decided <em>for</em> her. The mother-in-law, husband or elder is frequently the real "
              "<strong>gatekeeper</strong> &mdash; and may be a more important audience than the "
              "person who performs the behaviour."},
             {"t": "hbox", "color": "amber", "html": "Mapping gatekeepers is not optional. Miss "
              "them and your message reaches a person who lacks the power to act on it."},
         ]},

        {"type": "content", "label": "Barriers &amp; Motivators", "title": "What stops them? What would move them?",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Barriers", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Cost, distance, time, lost wages",
                      "Fear, stigma, past bad experience",
                      "Disapproval of family or neighbours",
                      "Low self-efficacy &mdash; 'I can't'"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Motivators", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Protecting one's child",
                      "Respect, status, belonging",
                      "Convenience and saving money",
                      "Approval of trusted others"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "Motivators are rarely 'health' in the "
              "abstract. People act for love, pride, money and belonging &mdash; design for those."},
         ]},

        {"type": "content", "label": "Personas", "title": "Make the audience a real person",
         "blocks": [
             {"t": "body", "html": "A <strong>persona</strong> turns a segment into a named, "
              "concrete character &mdash; with a life, a routine, a barrier and a motivator &mdash; "
              "so the whole team designs for a real human, not an abstraction."},
             {"t": "darkcard", "label": "Persona example",
              "title": "Sunita, 23, first-time mother, rural Bihar",
              "body": "Lives in a joint family; her mother-in-law decides clinic visits. Owns a "
              "shared phone, watches TV serials at night. Barrier: can't leave the house alone. "
              "Motivator: desperate for a healthy baby. Reachable via: the ASHA and her husband."},
         ]},

        {"type": "content", "label": "Insight", "title": "From data to a single human insight",
         "blocks": [
             {"t": "body", "html": "The goal of all this audience work is one sharp "
              "<strong>insight</strong>: the true, often surprising reason a person does or "
              "doesn't act &mdash; expressed in their own emotional logic, not the programme's."},
             {"t": "hbox", "color": "amber", "html": "Weak insight: 'mothers lack awareness of "
              "immunisation'. Strong insight: 'mothers fear the fever after the shot more than the "
              "disease it prevents'. The second tells you exactly what to address."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Formative Research"},

        {"type": "content", "label": "Research First", "title": "Understand the behaviour before you design",
         "blocks": [
             {"t": "body", "html": "<strong>Formative research</strong> is the listening you do "
              "<em>before</em> creating any message &mdash; to learn what people actually do, why, "
              "and what would move them. Skipping it is the commonest cause of campaign failure."},
             {"t": "term", "word": "Formative research",
              "def": "Early, exploratory research that shapes an intervention &mdash; understanding "
              "the audience, the behaviour, its barriers and motivators &mdash; before messages, "
              "materials or channels are decided."},
         ]},

        {"type": "content", "label": "What to Find Out", "title": "The questions formative research answers",
         "blocks": [
             {"t": "bullets", "items": [
                 "Who currently does the behaviour &mdash; and who doesn't?",
                 "What are the real barriers and motivators for each group?",
                 "Who and what do people trust as sources?",
                 "What language, images and channels resonate locally?",
                 "Which small, feasible action can we realistically ask for?"]},
             {"t": "hbox", "color": "cyan", "html": "Notice: not one of these can be answered from "
              "a desk. Formative research is fieldwork, mostly qualitative."},
         ]},

        {"type": "content", "label": "Methods", "title": "How formative research is done",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Method", "Good for", "Note"],
              "rows": [
                  ["In-depth interviews", "Personal, sensitive behaviours", "Rich, but small numbers"],
                  ["Focus group discussions", "Norms, shared language, reactions", "Beware dominant voices"],
                  ["Observation", "What people actually do vs say", "Reveals the say-do gap"],
                  ["Trials of improved practices", "Testing a behaviour in real homes", "Households try, then report"],
                  ["Quick surveys", "Rough prevalence &amp; segments", "Sizing, not deep 'why'"]]},
             {"t": "hbox", "color": "amber", "html": "Watch the say-do gap: what people report in a "
              "group and what they do at home often differ. Observe where you can."},
         ]},

        {"type": "content", "label": "Barrier Analysis", "title": "Barrier analysis",
         "blocks": [
             {"t": "body", "html": "<strong>Barrier analysis</strong> is a structured method to "
              "find which factors most separate people who practise a behaviour from those who "
              "don't &mdash; so you target the barriers that actually matter."},
             {"t": "flow", "steps": [
                 "Pick a specific behaviour",
                 "Interview practisers and non-practisers",
                 "Compare their beliefs, norms, efficacy",
                 "Find the determinants that differ most",
                 "Design messages against those determinants"]},
         ]},

        {"type": "content", "label": "Doer / Non-Doer", "title": "The 'doer / non-doer' approach",
         "blocks": [
             {"t": "body", "html": "At the heart of barrier analysis is a simple comparison: "
              "interview people who already do the behaviour (<strong>doers</strong>) and people "
              "who don't (<strong>non-doers</strong>), and look for the differences."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Doers", "blocks": [
                  {"t": "body", "cls": "sm", "html": "What do they believe, who supports them, what "
                   "made it easy? These are your assets to amplify."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Non-doers", "blocks": [
                  {"t": "body", "cls": "sm", "html": "What stops them &mdash; belief, norm, access, "
                   "efficacy? The biggest gap is your priority barrier."}]}]},
             {"t": "hbox", "color": "cyan", "html": "The genius is comparison. The factor on which "
              "doers and non-doers differ most is where your communication should aim first."},
         ]},

        {"type": "content", "label": "Self-Efficacy &amp; Norms", "title": "Probe the levers, not just the facts",
         "blocks": [
             {"t": "body", "html": "Good formative research doesn't just ask 'do you know X?'. It "
              "probes the theory constructs: perceived risk, perceived benefit, felt control, "
              "social approval &mdash; because those, not facts, predict behaviour."},
             {"t": "hbox", "color": "green", "html": "Tie your questions back to a theory (HBM, TPB, "
              "COM-B). Then your findings translate directly into which lever to pull."},
         ]},

        {"type": "content", "label": "Sizing the Behaviour", "title": "Then count: how common is it, and where?",
         "blocks": [
             {"t": "body", "html": "Qualitative work tells you <em>why</em>; a quick quantitative "
              "scan tells you <em>how big</em> and <em>where</em>. Pairing the two lets you "
              "prioritise the segments and places where the gap &mdash; and the opportunity "
              "&mdash; is largest."},
             {"t": "hbox", "color": "cyan", "html": "Use existing data first &mdash; NFHS, HMIS, "
              "district reports &mdash; before commissioning your own survey. Much of the sizing "
              "is already done and free."},
         ]},

        {"type": "content", "label": "Pretesting", "title": "Formative research never really stops",
         "blocks": [
             {"t": "body", "html": "The same listening discipline continues into "
              "<strong>pretesting</strong> (covered in the next section) and into monitoring. "
              "Research is not a phase you finish &mdash; it is a habit of checking your assumptions "
              "against reality throughout."},
             {"t": "hbox", "color": "amber", "html": "Budget for it. Programmes that 'have no time "
              "for research' spend far more, later, fixing campaigns that didn't land."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Designing Messages"},

        {"type": "content", "label": "One Job", "title": "The single overriding communication objective",
         "blocks": [
             {"t": "body", "html": "A strong piece of communication tries to achieve "
              "<strong>one</strong> clear thing with <strong>one</strong> audience. The "
              "<strong>Single Overriding Communication Objective (SOCO)</strong> forces that "
              "discipline before you write a word."},
             {"t": "term", "word": "SOCO",
              "def": "Single Overriding Communication Objective &mdash; the one specific change in "
              "knowledge, attitude or action you want one audience to take away from one message. "
              "If you have three SOCOs, you have three messages."},
         ]},

        {"type": "content", "label": "Cram &amp; Confuse", "title": "Too many messages means no message",
         "blocks": [
             {"t": "body", "html": "The strongest temptation in development communication is to "
              "say everything at once &mdash; nutrition, hygiene, immunisation, family planning "
              "&mdash; on a single poster. The audience remembers none of it."},
             {"t": "hbox", "color": "red", "html": "Discipline: one behaviour, one audience, one "
              "ask, per piece. A campaign can have many materials, but each carries a single, "
              "clear job."},
         ]},

        {"type": "content", "label": "Emotion &amp; Reason", "title": "Emotional and rational appeals",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Rational appeal", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Facts, benefits, evidence &mdash; 'ORS "
                   "replaces fluids lost in diarrhoea'. Necessary, but rarely moving on its own."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Emotional appeal", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Feeling, identity, story &mdash; a mother's "
                   "relief as her child recovers. Emotion is what makes a message stick and act."}]}]},
             {"t": "hbox", "color": "green", "html": "The best messages braid both: a reason to "
              "believe and a feeling to act on. Emotion opens the door; facts justify the choice."},
         ]},

        {"type": "content", "label": "Fear vs Positive", "title": "Fear appeals: handle with great care",
         "blocks": [
             {"t": "body", "html": "Fear can grab attention, but used carelessly it backfires: "
              "people deny the threat, feel helpless, or tune out. Fear works only when paired with "
              "a clear, doable action that resolves it."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Fear alone fails", "blocks": [
                  {"t": "body", "cls": "sm", "html": "'Smoking kills' with no path forward "
                   "&mdash; high threat, low efficacy &rarr; denial and avoidance."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Positive framing wins", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Show the rewarding, aspirational behaviour "
                   "&mdash; the proud, healthy family &mdash; and an easy first step."}]}]},
         ]},

        {"type": "content", "label": "Make It Stick", "title": "Qualities of a memorable message",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Simple:</strong> one core idea, plainly said",
                 "<strong>Concrete:</strong> a specific action, not a vague value",
                 "<strong>Credible:</strong> from a trusted source or relatable model",
                 "<strong>Emotional:</strong> makes the audience feel something",
                 "<strong>Story-shaped:</strong> a person, a problem, a change"]},
             {"t": "hbox", "color": "cyan", "html": "Ask for a small, specific, feasible action "
              "&mdash; 'wash hands with soap before feeding your baby' &mdash; not 'maintain "
              "hygiene'."},
         ]},

        {"type": "content", "label": "Messenger", "title": "Who says it matters as much as what is said",
         "blocks": [
             {"t": "body", "html": "The same message lands differently from a distant official, a "
              "film star, a respected elder, or a neighbour who has done it. "
              "<strong>Source credibility</strong> is part of the message."},
             {"t": "hbox", "color": "amber", "html": "For everyday behaviours, a relatable peer "
              "&mdash; 'someone like me' &mdash; often out-persuades a celebrity. Match the "
              "messenger to the audience and the behaviour."},
         ]},

        {"type": "content", "label": "Pretesting", "title": "Pretest before you print",
         "blocks": [
             {"t": "body", "html": "<strong>Pretesting</strong> is showing draft materials to a "
              "small sample of the real audience and checking comprehension, attractiveness, "
              "acceptability and whether they would act &mdash; <em>before</em> mass production."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Do they understand the core message correctly?",
                 "Is anything confusing, dull or offensive?",
                 "Do they see it as for 'people like me'?",
                 "Does it prompt the intended action?"]},
             {"t": "hbox", "color": "red", "html": "Skipping pretesting is gambling a whole "
              "budget on an untested guess. One afternoon of pretesting saves crores in wasted "
              "print runs."},
         ]},

        {"type": "content", "label": "Calls to Action", "title": "End with a clear, doable ask",
         "blocks": [
             {"t": "body", "html": "Every message should make the next step obvious. A vague hope "
              "(&lsquo;be healthier&rsquo;) leaves people unsure what to do; a precise, easy ask "
              "(&lsquo;take your baby for the 9-month measles shot&rsquo;) gets done."},
             {"t": "hbox", "color": "cyan", "html": "Pair the ask with where, when and how &mdash; "
              "the place, the day, the simple step. Closing the intention-action gap starts with "
              "an unmissable call to action."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Channels &amp; the Communication Mix"},

        {"type": "content", "label": "No Magic Channel", "title": "Different channels do different jobs",
         "blocks": [
             {"t": "body", "html": "Mass media reaches millions but persuades shallowly; "
              "interpersonal contact reaches few but changes deeply. The art is the "
              "<strong>communication mix</strong> &mdash; combining channels so each does what it "
              "is best at."},
             {"t": "chart", "canvas": "channelReach",
              "title": "Reach vs depth of influence by channel (illustrative)",
              "source": "Illustrative &mdash; general SBCC pattern",
              "type": "scatter",
              "data": {"datasets": [{"label": "Channels",
                       "data": [{"x": 95, "y": 25}, {"x": 70, "y": 40}, {"x": 55, "y": 55},
                                {"x": 40, "y": 70}, {"x": 20, "y": 90}],
                       "backgroundColor": "#6366F1", "pointRadius": 9}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ x:{title:{display:true,text:'Reach (breadth) %'},min:0,max:100}, y:{title:{display:true,text:'Depth of influence %'},min:0,max:100} } }"}},
         ]},

        {"type": "content", "label": "Channel Map", "title": "The four broad channel families",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Family", "Examples", "Strength"],
              "rows": [
                  ["Mass media", "TV, radio, print, outdoor", "Wide reach, awareness, norms"],
                  ["Mid-media / folk", "Street theatre, melas, wall art", "Local, engaging, trusted"],
                  ["Interpersonal", "FLWs, counselling, peer groups", "Deep, tailored, persuasive"],
                  ["Digital / mobile", "SMS, IVR, WhatsApp, social", "Targeted, two-way, cheap"]]},
             {"t": "hbox", "color": "cyan", "html": "Reach builds awareness; interpersonal contact "
              "converts it to action. A campaign that uses only one family usually under-performs."},
         ]},

        {"type": "content", "label": "Mass Media", "title": "Mass media: reach and the power to set norms",
         "blocks": [
             {"t": "body", "html": "Radio and television still reach vast South Asian audiences, "
              "including the less literate. Mass media is unbeatable for awareness and for "
              "signalling that a behaviour is becoming the new normal."},
             {"t": "hbox", "color": "amber", "html": "But broadcast is one-way and shallow. It can "
              "tell millions that toilets matter; it cannot answer the one fear keeping a "
              "particular family from building one."},
         ]},

        {"type": "content", "label": "Mid-Media &amp; Folk", "title": "Mid-media and folk forms",
         "blocks": [
             {"t": "body", "html": "Between mass and interpersonal sits <strong>mid-media</strong>: "
              "street plays (nukkad natak), puppet shows, folk songs, video vans, wall paintings "
              "and melas &mdash; rooted in local culture and able to gather a crowd."},
             {"t": "hbox", "color": "green", "html": "Folk forms carry credibility and emotion that "
              "a glossy ad cannot. In low-literacy, high-trust settings they often out-perform "
              "broadcast for changing minds."},
         ]},

        {"type": "content", "label": "Interpersonal", "title": "Interpersonal communication: the persuasion engine",
         "blocks": [
             {"t": "body", "html": "<strong>Interpersonal communication (IPC)</strong> &mdash; a "
              "frontline worker counselling a mother, a peer group, a home visit &mdash; allows "
              "questions, tailoring, demonstration and trust. It is where intention most often "
              "turns into action."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Two-way", "label": "People can ask, object, be reassured", "color": "cyan"},
                 {"num": "Tailored", "label": "Address this person's specific barrier", "color": "indigo"},
                 {"num": "Trusted", "label": "A known, credible human face", "color": "green"}]},
         ]},

        {"type": "content", "label": "Community Mobilisation", "title": "Community mobilisation",
         "blocks": [
             {"t": "body", "html": "Beyond one-to-one, <strong>community mobilisation</strong> "
              "organises groups &mdash; women's collectives, self-help groups, village health and "
              "sanitation committees &mdash; to act together and hold the new behaviour as a shared "
              "commitment."},
             {"t": "hbox", "color": "cyan", "html": "Collective action changes the norm and gives "
              "individuals social cover to change. It is the bridge from personal message to "
              "community movement &mdash; the theme of the next section."},
         ]},

        {"type": "content", "label": "Digital &amp; Mobile", "title": "Digital and mobile channels",
         "blocks": [
             {"t": "body", "html": "Mobile penetration has opened SMS reminders, interactive voice "
              "response (IVR), WhatsApp groups and social media &mdash; cheap, targeted, two-way, "
              "and able to prompt at the right moment to close the intention-action gap."},
             {"t": "hbox", "color": "red", "html": "But mind the divide: phone access skews male, "
              "richer, younger and urban. A digital-only campaign can quietly exclude the very "
              "people most in need."},
         ]},

        {"type": "content", "label": "Designing the Mix", "title": "Choose channels to fit audience and objective",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Match the channel to the audience</strong> &mdash; what do they actually use and trust?",
                 "<strong>Match the channel to the job</strong> &mdash; awareness vs deep persuasion",
                 "<strong>Layer channels</strong> so they reinforce one consistent message",
                 "<strong>Sequence them</strong> &mdash; broadcast to seed, IPC to convert",
                 "<strong>Budget realistically</strong> &mdash; IPC is powerful but costly to scale"]},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Campaigns &amp; Community Engagement"},

        {"type": "content", "label": "The Cycle", "title": "The SBCC campaign cycle",
         "blocks": [
             {"t": "flow", "steps": [
                 "ANALYSE: audience &amp; behaviour",
                 "DESIGN: strategy, SOCO, channels",
                 "DEVELOP &amp; PRETEST: materials",
                 "IMPLEMENT: roll out the mix",
                 "MONITOR &amp; EVALUATE: learn &amp; adapt"]},
             {"t": "hbox", "color": "cyan", "html": "It is a loop, not a line. Findings from "
              "monitoring feed back into analysis and design &mdash; campaigns improve by "
              "iterating, not by launching once."},
         ]},

        {"type": "content", "label": "Strategy First", "title": "A campaign is a strategy, not a slogan",
         "blocks": [
             {"t": "body", "html": "Behind every good campaign is a written "
              "<strong>communication strategy</strong>: the behaviour, the audiences, the barriers, "
              "the SOCO, the messages, the channels, the messengers and the indicators &mdash; "
              "agreed before any creative work."},
             {"t": "hbox", "color": "amber", "html": "The logo and tagline come last. Programmes "
              "that start with a slogan and reverse-engineer a strategy almost always miss the "
              "real barrier."},
         ]},

        {"type": "content", "label": "Community-Led", "title": "Community-led change beats top-down telling",
         "blocks": [
             {"t": "body", "html": "When a community diagnoses its own problem and decides to act, "
              "the change holds. Outside messengers can catalyse, but ownership &mdash; not "
              "instruction &mdash; sustains behaviour."},
             {"t": "quote", "text": "People support what they help create.",
              "attr": "&mdash; a principle of participatory development"},
         ]},

        {"type": "content", "label": "CLTS", "title": "Community-Led Total Sanitation (Kamal Kar)",
         "blocks": [
             {"t": "body", "html": "<strong>Community-Led Total Sanitation (CLTS)</strong>, "
              "pioneered by Kamal Kar in Bangladesh, abandons subsidies and lecturing. Instead, "
              "facilitators help a whole community confront the reality of open defecation and "
              "decide, collectively, to end it."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Triggering:</strong> a facilitated 'walk of shame' and self-realisation",
                 "<strong>Collective decision:</strong> the whole village commits, not individuals",
                 "<strong>Local solutions:</strong> people build toilets their own way",
                 "<strong>Goal:</strong> an open-defecation-free (ODF) community"]},
             {"t": "hbox", "color": "green", "html": "CLTS works because it changes the "
              "<em>norm</em> and harnesses collective pride and shame &mdash; behaviour theory in "
              "action at community scale."},
         ]},

        {"type": "content", "label": "Entertainment-Education", "title": "Entertainment-education",
         "blocks": [
             {"t": "body", "html": "<strong>Entertainment-education</strong> weaves behaviour-change "
              "messages into genuinely entertaining stories &mdash; TV serials, radio dramas, "
              "films &mdash; so audiences learn from characters they love, not lectures they "
              "tolerate."},
             {"t": "hbox", "color": "cyan", "html": "It draws directly on Bandura: viewers model "
              "the choices of relatable, rewarded characters. South Asia's serial dramas have long "
              "carried messages on dowry, girls' education and family planning this way."},
         ]},

        {"type": "content", "label": "FLW-Led IPC", "title": "Frontline workers and ASHA-led communication",
         "blocks": [
             {"t": "body", "html": "India's vast frontline &mdash; <strong>ASHAs, ANMs and "
              "anganwadi workers</strong> &mdash; are the backbone of interpersonal SBCC. They "
              "carry messages the last mile, into homes, in the local idiom, from a familiar face."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "~1 million+", "label": "ASHAs across India, embedded in their own "
                  "villages", "color": "indigo", "source": "National Health Mission"},
                 {"num": "Home-based", "label": "Counselling at the doorstep, repeatedly, over time",
                  "color": "green"}]},
             {"t": "hbox", "color": "amber", "html": "Their power depends on support: training, job "
              "aids, manageable workload and respect. Overloaded, untrained FLWs cannot persuade."},
         ]},

        {"type": "content", "label": "Group Engagement", "title": "Groups multiply individual change",
         "blocks": [
             {"t": "body", "html": "Participatory learning and action groups &mdash; such as "
              "women's <strong>self-help groups</strong> and participatory women's groups &mdash; "
              "let members discuss problems, plan together and support each other through change."},
             {"t": "hbox", "color": "cyan", "html": "Participatory women's group approaches have "
              "shown real promise for maternal and newborn health in South Asia &mdash; peer "
              "support turning knowledge into sustained practice."},
         ]},

        {"type": "content", "label": "Sustaining It", "title": "From campaign to lasting change",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Repeat and reinforce</strong> &mdash; one burst rarely sticks",
                 "<strong>Build local ownership</strong> so change outlives the project",
                 "<strong>Make the new behaviour the visible norm</strong>",
                 "<strong>Remove the friction</strong> so the easy choice is the healthy one",
                 "<strong>Celebrate progress</strong> publicly to lock in the gain"]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Monitoring, Ethics &amp; Examples"},

        {"type": "content", "label": "Measure What Matters", "title": "From exposure to behaviour",
         "blocks": [
             {"t": "body", "html": "It is easy to count outputs &mdash; posters printed, spots "
              "aired &mdash; and mistake them for results. SBCC monitoring must follow the chain "
              "all the way to behaviour."},
             {"t": "flow", "steps": [
                 "OUTPUTS: materials produced, sessions held",
                 "REACH / EXPOSURE: who saw or heard it",
                 "OUTCOMES: changed knowledge, attitude, norm",
                 "BEHAVIOUR: what people now actually do",
                 "IMPACT: health &amp; wellbeing change"]},
         ]},

        {"type": "content", "label": "Indicators", "title": "Indicators along the chain",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Level", "Example indicator"],
              "rows": [
                  ["Exposure", "% who recall the campaign message"],
                  ["Knowledge", "% who correctly state when to use ORS"],
                  ["Attitude / norm", "% who believe neighbours approve of toilets"],
                  ["Intention", "% who intend to immunise their child"],
                  ["Behaviour", "% of children fully immunised"]]},
             {"t": "hbox", "color": "amber", "html": "Recall is not behaviour. A campaign everyone "
              "remembers but no one acts on has failed at the only step that counts."},
         ]},

        {"type": "content", "label": "Indian Example", "title": "Handwashing with soap",
         "blocks": [
             {"t": "body", "html": "Handwashing campaigns shifted from telling people that germs "
              "exist to building a <strong>habit</strong> tied to specific moments &mdash; after "
              "the toilet, before feeding a child &mdash; using cues, emotion (disgust, nurture) "
              "and repetition rather than facts alone."},
             {"t": "chart", "canvas": "handwashCampaign",
              "title": "Reported handwashing at key times, before vs after a campaign (illustrative)",
              "source": "Illustrative &mdash; not actual programme figures",
              "type": "bar",
              "data": {"labels": ["After toilet", "Before feeding child", "Before eating"],
                       "datasets": [
                           {"label": "Before", "data": [38, 25, 30], "backgroundColor": "#94A3B8"},
                           {"label": "After", "data": [62, 54, 58], "backgroundColor": "#10B981"}]},
              "options": {"__js__": "{ scales:{ y:{min:0,max:100, title:{display:true,text:'% reporting'}} } }"}},
         ]},

        {"type": "content", "label": "Indian Example", "title": "Immunisation &mdash; Mission Indradhanush",
         "blocks": [
             {"t": "body", "html": "India's <strong>Mission Indradhanush</strong> paired service "
              "delivery with intensive communication &mdash; ASHA mobilisation, local influencers, "
              "addressing rumours and fears &mdash; to reach children who had been missed or "
              "partially immunised."},
             {"t": "hbox", "color": "cyan", "html": "The lesson: communication and service must "
              "move together. Demand-generation without a reliable session, or sessions without "
              "demand, both fall short."},
         ]},

        {"type": "content", "label": "Indian Example", "title": "Swachh Bharat &mdash; sanitation at scale",
         "blocks": [
             {"t": "body", "html": "The <strong>Swachh Bharat Mission</strong> combined "
              "infrastructure with one of the largest behaviour-change efforts ever attempted "
              "&mdash; mass media, celebrity endorsement, CLTS-style community triggering and "
              "frontline mobilisation to make toilet use the norm."},
             {"t": "hbox", "color": "amber", "html": "It also showed the limits of any campaign: "
              "building a toilet is not the same as <em>using</em> it. Sustained behaviour, not "
              "construction counts, is the real measure."},
         ]},

        {"type": "content", "label": "Indian Example", "title": "ORS &mdash; a quiet behaviour-change success",
         "blocks": [
             {"t": "body", "html": "Promoting <strong>oral rehydration solution (ORS)</strong> for "
              "childhood diarrhoea is among the great public-health communication stories &mdash; "
              "shifting a simple, low-cost home practice across decades through repeated, "
              "consistent messaging and frontline counselling."},
             {"t": "hbox", "color": "green", "html": "ORS shows SBCC at its best: a single, "
              "feasible behaviour, a clear benefit (a child who recovers), and patient, sustained "
              "promotion &mdash; not a one-off campaign."},
         ]},

        {"type": "content", "label": "Ethics", "title": "Persuasion that respects people",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Avoid stigma:</strong> never shame the poor, the sick or the marginalised",
                 "<strong>Be truthful:</strong> no exaggerated fear or false promises",
                 "<strong>Respect autonomy:</strong> inform and enable, don't coerce",
                 "<strong>Do no harm:</strong> check that messages don't endanger anyone",
                 "<strong>Be inclusive:</strong> reach those usually left out"]},
             {"t": "hbox", "color": "red", "html": "The line between a nudge and manipulation is "
              "honesty and the person's own interest. Stay on the right side of it &mdash; "
              "deliberately."},
         ]},

        {"type": "content", "label": "Avoiding Harm", "title": "When campaigns backfire",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Stigma trap", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Shaming open defecation can humiliate the "
                   "poorest, who often lack means &mdash; not will &mdash; to build a toilet."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Norm trap", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Saying 'most people still don't do X' "
                   "tells the audience the bad behaviour is normal &mdash; reinforcing it."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Ethical SBCC is also <em>effective</em> SBCC. "
              "Respect, dignity and truth are not constraints on impact &mdash; they enable it."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "Take it further",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Diffusion of Innovations</em> &mdash; Everett Rogers",
                 "<em>Influence: The Psychology of Persuasion</em> &mdash; Robert Cialdini",
                 "<em>Nudge</em> &mdash; Thaler &amp; Sunstein; the <em>EAST</em> framework (BIT)",
                 "Behaviour Change Wheel &amp; COM-B &mdash; Susan Michie and colleagues",
                 "Johns Hopkins CCP and UNICEF SBCC guidance &amp; toolkits"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Public Health</strong>, <strong>Qualitative Methods</strong> and "
              "<strong>Monitoring &amp; Evaluation</strong> 101 courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Behaviour Change Communication 101 &middot; Complete",
         "headline": "Don't just inform.<br>Change what people do.",
         "byline": "Knowledge rarely changes behaviour on its own. Find the real barrier, design "
                   "for how minds and communities actually work, and meet people where they are. "
                   "Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
