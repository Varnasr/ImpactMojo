# -*- coding: utf-8 -*-
"""
Maternal Health 101 — ImpactMojo 101 Series (native deck spec)
Foundational maternal health for development & public-health practitioners in South Asia.
Build: python3 scripts/deck-builder/build.py maternal_health
"""

DECK = {
    "slug": "maternal-health",
    "title": "Maternal Health 101",
    "description": ("Maternal Health 101 — a free foundational course for development and "
                    "public-health practitioners in South Asia: why mothers die, the three "
                    "delays, the continuum of care, antenatal and emergency obstetric care, "
                    "family planning and safe abortion, equity, and India's programmes from "
                    "JSY to SUMAN. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Maternal<br>Health<br>101",
         "sub": "Why Mothers Die &mdash; and How They Survive: a Foundational Course for "
                "Development &amp; Public-Health Practitioners in South Asia",
         "tags": ["Research-Backed", "South Asia Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "Why Maternal Health Matters"},
             {"name": "Why Mothers Die"},
             {"name": "The Three Delays"},
             {"name": "The Continuum of Care"},
             {"name": "Antenatal Care"},
             {"name": "Skilled Birth &amp; Institutional Delivery"},
             {"name": "Emergency Obstetric &amp; Newborn Care"},
             {"name": "Postnatal &amp; Newborn Care"},
             {"name": "Family Planning &amp; Safe Abortion"},
             {"name": "Social Determinants &amp; Equity"},
             {"name": "India's Programmes &amp; Progress"},
         ]},

        # ===================== SECTION 01 — Why it matters (8) =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "Why Maternal Health Matters"},

        {"type": "content", "label": "The Stakes", "title": "A death that should almost never happen",
         "blocks": [
             {"t": "body", "html": "A <strong>maternal death</strong> is the death of a woman "
              "while pregnant or within 42 days of the end of pregnancy, from any cause related "
              "to or aggravated by the pregnancy &mdash; but not from accidental causes."},
             {"t": "hbox", "color": "red", "html": "The tragedy is not that it happens, but that "
              "it almost always <strong>should not</strong>. The vast majority of maternal deaths "
              "are preventable with care that already exists."},
         ]},

        {"type": "content", "label": "Definitions", "title": "Speaking the same language",
         "blocks": [
             {"t": "term", "word": "Maternal Mortality Ratio (MMR)",
              "def": "The number of maternal deaths per 100,000 live births. The headline measure "
              "of how safe pregnancy and childbirth are in a population."},
             {"t": "term", "word": "Maternal Mortality Rate",
              "def": "Maternal deaths per 100,000 women of reproductive age &mdash; reflects both "
              "the risk per pregnancy and how often women become pregnant. Distinct from the ratio."},
         ]},

        {"type": "content", "label": "A Rights Issue", "title": "Maternal health is a human right",
         "blocks": [
             {"t": "body", "html": "Safe motherhood is not charity. It flows from the rights to "
              "<strong>life, health, equality and non-discrimination</strong> &mdash; affirmed in "
              "the constitution and in international human-rights law."},
             {"t": "quote",
              "text": "More women die in pregnancy and childbirth than from almost any other cause "
              "&mdash; and they die because their lives are not valued enough to prevent it.",
              "attr": "&mdash; a foundational claim of the safe-motherhood movement"},
         ]},

        {"type": "content", "label": "The Global Target", "title": "SDG 3.1: the world's promise",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "< 70", "label": "global MMR target per 100,000 live births by 2030",
                  "color": "cyan", "source": "SDG 3.1"},
                 {"num": "2030", "label": "the deadline every country signed up to", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "SDG 3.1 also sets a national floor: "
              "<strong>no country with an MMR above 140</strong> &mdash; twice the global average "
              "&mdash; by 2030. Equity, not just the average, is the goal."},
         ]},

        {"type": "content", "label": "Mostly Preventable", "title": "Most maternal deaths are preventable",
         "blocks": [
             {"t": "body", "html": "The clinical causes of maternal death are well understood and "
              "the remedies are known, cheap and decades old: a trained attendant, a drug to stop "
              "bleeding, antibiotics, a timely caesarean, safe blood."},
             {"t": "hbox", "color": "green", "html": "This is what makes maternal mortality a "
              "<strong>justice</strong> problem, not only a medical one. Women die not because we "
              "lack the knowledge, but because care does not reach them in time."},
         ]},

        {"type": "content", "label": "Where It Happens", "title": "A burden concentrated in the poorest places",
         "blocks": [
             {"t": "body", "html": "Almost all maternal deaths occur in low- and lower-middle-income "
              "countries; sub-Saharan Africa and Southern Asia together carry the overwhelming "
              "majority. Within countries, the burden falls hardest on the poor and remote."},
             {"t": "hbox", "color": "amber", "html": "A woman's risk of dying in childbirth can vary "
              "many-fold between her district and a richer one in the same state. Maternal health "
              "is a map of inequality."},
         ]},

        {"type": "content", "label": "This Course", "title": "How this course is built",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "The problem", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Why mothers die &mdash; direct &amp; indirect causes",
                      "The three delays that kill",
                      "The continuum of care that saves"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "The response", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Antenatal, skilled birth, emergency &amp; postnatal care",
                      "Family planning, safe abortion, equity",
                      "India's programmes and its progress"]}]}]},
             {"t": "hbox", "color": "indigo", "html": "Throughout, the lens is South Asian and "
              "India-centric &mdash; the systems and schemes you will actually work within."},
         ]},

        # ===================== SECTION 02 — Why mothers die (8) =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Why Mothers Die"},

        {"type": "content", "label": "Two Families of Cause", "title": "Direct and indirect causes",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Direct", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Deaths from obstetric complications of "
                   "pregnancy, labour and the postpartum &mdash; or from their treatment. "
                   "Haemorrhage, sepsis, eclampsia, obstructed labour, unsafe abortion."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Indirect", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Deaths from pre-existing or new conditions "
                   "<em>aggravated</em> by pregnancy &mdash; anaemia, heart disease, diabetes, "
                   "infections like TB or malaria."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Both matter. As direct deaths fall with better "
              "obstetric care, indirect causes &mdash; especially anaemia &mdash; make up a larger "
              "share of the remaining burden."},
         ]},

        {"type": "content", "label": "The Big Picture", "title": "What kills mothers: the leading causes",
         "blocks": [
             {"t": "chart", "canvas": "causesDoughnut",
              "title": "Distribution of direct maternal deaths by cause (illustrative pattern)",
              "source": "Illustrative; patterned on WHO global cause-of-death analyses",
              "type": "doughnut",
              "data": {"labels": ["Haemorrhage", "Hypertensive disorders", "Sepsis",
                                  "Obstructed labour", "Unsafe abortion", "Other direct"],
                       "datasets": [{"data": [27, 16, 11, 9, 8, 29],
                                     "backgroundColor": ["#EF4444", "#6366F1", "#F59E0B",
                                                         "#0EA5E9", "#10B981", "#94A3B8"]}]},
              "options": {"__js__": "{ plugins:{ legend:{ position:'right' } } }"}},
             {"t": "hbox", "color": "red", "html": "Bleeding is the single biggest killer "
              "worldwide. Shares vary by country &mdash; treat these as illustrative, not exact."},
         ]},

        {"type": "content", "label": "Direct Cause #1", "title": "Haemorrhage: death in minutes",
         "blocks": [
             {"t": "body", "html": "<strong>Obstetric haemorrhage</strong> &mdash; severe bleeding, "
              "most often <em>after</em> delivery (postpartum haemorrhage, PPH) &mdash; is the "
              "leading direct cause of maternal death. A woman can bleed to death in under two hours."},
             {"t": "hbox", "color": "green", "html": "It is also among the most treatable: a uterotonic "
              "drug (oxytocin) given right after birth, prompt referral, and access to safe blood "
              "prevent most PPH deaths."},
         ]},

        {"type": "content", "label": "Direct Cause #2", "title": "Hypertensive disorders &amp; eclampsia",
         "blocks": [
             {"t": "body", "html": "<strong>Pre-eclampsia</strong> &mdash; high blood pressure with "
              "protein in the urine &mdash; can progress to <strong>eclampsia</strong>, where the "
              "mother convulses. Both threaten mother and baby."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "BP + protein", "label": "the warning signs antenatal care screens for",
                  "color": "indigo"},
                 {"num": "MgSO&#8324;", "label": "magnesium sulphate prevents &amp; controls seizures "
                  "&mdash; cheap, effective", "color": "green"}]},
         ]},

        {"type": "content", "label": "Direct Cause #3", "title": "Sepsis: infection after birth",
         "blocks": [
             {"t": "body", "html": "<strong>Puerperal sepsis</strong> is a serious infection of the "
              "genital tract after childbirth or abortion, often from unhygienic delivery practices "
              "or prolonged labour. It can become fatal within days."},
             {"t": "hbox", "color": "cyan", "html": "Clean hands, clean delivery surface, clean cord "
              "care and timely antibiotics &mdash; the 'six cleans' of safe delivery &mdash; prevent "
              "most cases."},
         ]},

        {"type": "content", "label": "Direct Causes #4 &amp; #5", "title": "Obstructed labour &amp; unsafe abortion",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "Obstructed labour", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The baby cannot pass through the birth canal. "
                   "Without a timely caesarean it can cause rupture, death, or lifelong "
                   "<strong>obstetric fistula</strong>."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Unsafe abortion", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Termination by untrained people or in unsafe "
                   "conditions. A wholly preventable cause &mdash; legal, safe abortion services "
                   "eliminate it."}]}]},
             {"t": "hbox", "color": "indigo", "html": "Both point to the same fix: a skilled "
              "attendant and access to emergency and safe services when they are needed."},
         ]},

        {"type": "content", "label": "Indirect Causes", "title": "Anaemia: the silent multiplier",
         "blocks": [
             {"t": "body", "html": "<strong>Anaemia</strong> &mdash; too little haemoglobin to carry "
              "oxygen &mdash; rarely kills on its own, but it weakens a woman so that bleeding, "
              "infection or a difficult labour becomes lethal. It is the great <em>indirect</em> "
              "killer in South Asia."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "~57%", "label": "of pregnant women aged 15&ndash;49 in India anaemic",
                  "color": "red", "source": "NFHS-5, 2019&ndash;21"},
                 {"num": "Iron + folic acid", "label": "supplementation &amp; diet are the front-line "
                  "response", "color": "green"}]},
         ]},

        {"type": "content", "label": "When Death Strikes", "title": "The most dangerous hours",
         "blocks": [
             {"t": "body", "html": "Most maternal deaths cluster around <strong>labour, delivery and "
              "the first 24 hours postpartum</strong> &mdash; the window when haemorrhage, eclampsia "
              "and obstructed labour turn fatal."},
             {"t": "hbox", "color": "red", "html": "This is why a <strong>skilled attendant at birth</strong> "
              "and rapid access to emergency care matter more than almost anything else. The danger "
              "is concentrated, and so the response must be ready."},
         ]},

        # ===================== SECTION 03 — Three delays (8) =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The Three Delays"},

        {"type": "content", "label": "The Framework", "title": "Why women die: the three delays",
         "blocks": [
             {"t": "body", "html": "The clinical cause is only the final step. Behind most maternal "
              "deaths lies a fatal delay. The <strong>'three delays' model</strong> "
              "(Thaddeus &amp; Maine, 1994) maps where the system fails."},
             {"t": "term", "word": "The three delays",
              "def": "Delay 1: in deciding to seek care. Delay 2: in reaching a facility. "
              "Delay 3: in receiving adequate care once there. A death usually reflects more than one."},
         ]},

        {"type": "content", "label": "Visualised", "title": "The path from complication to outcome",
         "blocks": [
             {"t": "raw", "html":
              '<svg viewBox="0 0 1100 300" width="100%" role="img" '
              'aria-label="Three delays diagram from complication to outcome">'
              '<defs><marker id="mhArrow" markerWidth="10" markerHeight="10" refX="8" refY="3" '
              'orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#94A3B8"/></marker></defs>'
              '<rect x="20" y="120" width="150" height="60" rx="10" fill="#1e293b" stroke="#475569"/>'
              '<text x="95" y="155" fill="#e2e8f0" font-size="16" text-anchor="middle">Complication</text>'
              '<line x1="170" y1="150" x2="225" y2="150" stroke="#94A3B8" stroke-width="2" marker-end="url(#mhArrow)"/>'
              '<rect x="230" y="110" width="180" height="80" rx="10" fill="#7f1d1d" stroke="#ef4444"/>'
              '<text x="320" y="140" fill="#fecaca" font-size="15" text-anchor="middle">Delay 1</text>'
              '<text x="320" y="165" fill="#fecaca" font-size="13" text-anchor="middle">Deciding to seek</text>'
              '<line x1="410" y1="150" x2="465" y2="150" stroke="#94A3B8" stroke-width="2" marker-end="url(#mhArrow)"/>'
              '<rect x="470" y="110" width="180" height="80" rx="10" fill="#78350f" stroke="#f59e0b"/>'
              '<text x="560" y="140" fill="#fde68a" font-size="15" text-anchor="middle">Delay 2</text>'
              '<text x="560" y="165" fill="#fde68a" font-size="13" text-anchor="middle">Reaching care</text>'
              '<line x1="650" y1="150" x2="705" y2="150" stroke="#94A3B8" stroke-width="2" marker-end="url(#mhArrow)"/>'
              '<rect x="710" y="110" width="180" height="80" rx="10" fill="#3730a3" stroke="#6366f1"/>'
              '<text x="800" y="140" fill="#c7d2fe" font-size="15" text-anchor="middle">Delay 3</text>'
              '<text x="800" y="165" fill="#c7d2fe" font-size="13" text-anchor="middle">Receiving care</text>'
              '<line x1="890" y1="150" x2="945" y2="150" stroke="#94A3B8" stroke-width="2" marker-end="url(#mhArrow)"/>'
              '<rect x="950" y="120" width="130" height="60" rx="10" fill="#064e3b" stroke="#10b981"/>'
              '<text x="1015" y="155" fill="#a7f3d0" font-size="16" text-anchor="middle">Outcome</text>'
              '</svg>'},
             {"t": "hbox", "color": "cyan", "html": "Each delay is a place where the system &mdash; "
              "and we &mdash; can intervene to keep a mother alive."},
         ]},

        {"type": "content", "label": "Delay One", "title": "Delay 1: deciding to seek care",
         "blocks": [
             {"t": "body", "html": "The family does not recognise the danger, or hesitates &mdash; "
              "because of cost, distance, custom, or the low value placed on a woman's health."},
             {"t": "bullets", "color": "red", "sm": True, "items": [
                 "Danger signs not known or dismissed as 'normal'",
                 "Decision rests with a husband or elder, not the woman",
                 "Fear of cost, or of the facility itself",
                 "Belief that birth is a private, home affair"]},
         ]},

        {"type": "content", "label": "Delay Two", "title": "Delay 2: reaching care",
         "blocks": [
             {"t": "body", "html": "The family decides to go &mdash; but cannot get there in time. "
              "Roads, distance, transport and terrain become matters of life and death."},
             {"t": "bullets", "color": "amber", "sm": True, "items": [
                 "No vehicle, or no money for one, at 2&nbsp;a.m.",
                 "Long distance to the nearest functioning facility",
                 "Monsoon, hills or rivers cutting off villages",
                 "No referral transport linking village to hospital"]},
         ]},

        {"type": "content", "label": "Delay Three", "title": "Delay 3: receiving adequate care",
         "blocks": [
             {"t": "body", "html": "She reaches the facility &mdash; and still does not get what she "
              "needs. The third delay happens <em>inside</em> the system."},
             {"t": "bullets", "color": "indigo", "sm": True, "items": [
                 "No doctor, no blood, no working theatre on duty",
                 "Stockouts of oxytocin, magnesium sulphate, antibiotics",
                 "Staff unable to manage the complication; further referral",
                 "Delays in payment, paperwork or decision-making"]},
         ]},

        {"type": "content", "label": "What It Teaches", "title": "Why the model changed everything",
         "blocks": [
             {"t": "body", "html": "Before the three-delays model, maternal death was framed as a "
              "purely medical event. The model reframed it as a <strong>systems failure</strong> "
              "&mdash; spanning the household, the road and the hospital."},
             {"t": "hbox", "color": "green", "html": "The insight: to save mothers you must fix all "
              "three delays at once. A perfect hospital is useless if she never reaches it; perfect "
              "transport is useless if it has nowhere to take her."},
         ]},

        {"type": "content", "label": "Matching Solutions", "title": "Each delay has its own remedy",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Delay", "Root cause", "What helps"],
              "rows": [
                  ["1. Deciding", "Awareness, cost, gender norms", "ASHA outreach, danger-sign education, cash incentives"],
                  ["2. Reaching", "Distance, transport", "Referral ambulances (e.g. 102/108), birth-waiting homes"],
                  ["3. Receiving", "Facility readiness", "EmONC, staff, drugs, blood, free entitlements"]]},
             {"t": "hbox", "color": "cyan", "html": "India's flagship schemes map directly onto these "
              "three delays &mdash; a useful lens for any programme you design or assess."},
         ]},

        {"type": "content", "label": "Use It", "title": "A diagnostic you can apply tomorrow",
         "blocks": [
             {"t": "body", "html": "When you review a maternal death &mdash; in a verbal autopsy, a "
              "case review, or a community meeting &mdash; walk it through the three delays. Where "
              "did the time go?"},
             {"t": "hbox", "color": "amber", "html": "Most deaths reveal failures at more than one "
              "delay. Naming each one turns a tragedy into a list of fixable, system-level actions."},
         ]},

        # ===================== SECTION 04 — Continuum of care (8) =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "The Continuum of Care"},

        {"type": "content", "label": "The Big Idea", "title": "Care is a chain, not a single event",
         "blocks": [
             {"t": "body", "html": "Maternal and newborn health is not one moment &mdash; it is a "
              "<strong>continuum</strong> that runs from before pregnancy, through pregnancy, birth "
              "and the weeks after, into early childhood. A break anywhere puts mother and baby at risk."},
             {"t": "term", "word": "Continuum of care",
              "def": "Linked, uninterrupted care across time (pre-pregnancy &rarr; pregnancy &rarr; "
              "birth &rarr; postnatal &rarr; childhood) and across place (home &rarr; community &rarr; "
              "facility)."},
         ]},

        {"type": "content", "label": "The Stages", "title": "The four core stages",
         "blocks": [
             {"t": "flow", "steps": [
                 "ANTENATAL: care through pregnancy",
                 "SKILLED BIRTH: a trained attendant at delivery",
                 "POSTNATAL: mother &amp; newborn in the first 6 weeks",
                 "NEWBORN: care of the baby from the first minute"]},
             {"t": "hbox", "color": "cyan", "html": "Each stage protects against specific risks &mdash; "
              "and each handover between stages is where women fall out of the system."},
         ]},

        {"type": "content", "label": "Two Dimensions", "title": "Across time and across place",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Across time", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Pre-pregnancy &rarr; antenatal &rarr; birth "
                   "&rarr; postnatal &rarr; childhood. No stage skipped."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Across place", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Home and community (ASHA, ANM) linked to "
                   "facilities (PHC, CHC, district hospital) by referral."}]}]},
             {"t": "hbox", "color": "green", "html": "Strong systems connect both dimensions &mdash; "
              "the home visit and the operating theatre are part of one chain."},
         ]},

        {"type": "content", "label": "The Weakest Links", "title": "Where the chain usually breaks",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Women attend antenatal care but deliver at home unattended",
                 "They deliver in a facility but leave within hours, missing postnatal care",
                 "Referral between levels fails &mdash; no transport, no slot, no follow-up",
                 "The newborn is never separately checked"]},
             {"t": "hbox", "color": "amber", "html": "Coverage of any single stage is not enough. "
              "The question is whether each woman moves through <em>all</em> of them."},
         ]},

        {"type": "content", "label": "Who Delivers It", "title": "The frontline team",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Cadre", "Role", "Based at"],
              "rows": [
                  ["ASHA", "Mobiliser, accompanies women, follow-up", "Village"],
                  ["ANM", "Antenatal checks, immunisation, deliveries", "Sub-centre / HWC"],
                  ["Staff nurse / SBA", "Skilled birth attendance", "PHC / CHC"],
                  ["Medical officer", "Complications, caesarean (where trained)", "CHC / hospital"],
                  ["Specialist (Ob-Gyn)", "Comprehensive emergency care", "District hospital"]]},
             {"t": "hbox", "color": "cyan", "html": "The ASHA is the hinge of the whole continuum in "
              "India &mdash; the link between the household and the health system."},
         ]},

        {"type": "content", "label": "Levels of Care", "title": "A referral system, tier by tier",
         "blocks": [
             {"t": "flow", "steps": [
                 "SUB-CENTRE / HWC: antenatal, normal birth",
                 "PHC: basic emergency obstetric care",
                 "CHC / FRU: comprehensive care, caesarean, blood",
                 "DISTRICT HOSPITAL: full specialist &amp; newborn care"]},
             {"t": "hbox", "color": "indigo", "html": "Each tier handles what it can and refers up "
              "what it cannot. A functioning referral chain &mdash; with transport and communication "
              "&mdash; is what makes the continuum real."},
         ]},

        {"type": "content", "label": "The Payoff", "title": "Why the continuum saves lives",
         "blocks": [
             {"t": "body", "html": "Antenatal care detects risk early; skilled birth manages the most "
              "dangerous hours; postnatal care catches haemorrhage and infection; newborn care "
              "protects the baby. Together they close the gaps no single intervention can."},
             {"t": "hbox", "color": "cyan", "html": "The rest of this course follows the continuum "
              "&mdash; one stage at a time &mdash; before turning to family planning, equity and "
              "India's programmes."},
         ]},

        # ===================== SECTION 05 — Antenatal care (8) =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Antenatal Care"},

        {"type": "content", "label": "What &amp; Why", "title": "Antenatal care: the first line of defence",
         "blocks": [
             {"t": "term", "word": "Antenatal care (ANC)",
              "def": "The care a woman receives during pregnancy &mdash; check-ups, screening, "
              "advice, supplements and immunisation &mdash; to keep her and her baby healthy and "
              "to detect problems early."},
             {"t": "body", "html": "Good ANC turns a silent risk into a managed one: it finds the "
              "anaemia, the rising blood pressure, the malpresentation &mdash; before they become "
              "emergencies."},
         ]},

        {"type": "content", "label": "The Shift", "title": "From 4 contacts to 8: WHO's 2016 model",
         "blocks": [
             {"t": "body", "html": "In 2016 WHO moved from a minimum of <strong>4 antenatal visits</strong> "
              "to a recommended <strong>8 contacts</strong> &mdash; more touchpoints, better outcomes, "
              "and a more positive pregnancy experience."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "4 &rarr; 8", "label": "minimum visits raised to recommended contacts",
                  "color": "indigo", "source": "WHO ANC model, 2016"},
                 {"num": "1st trimester", "label": "the first contact should be early &mdash; "
                  "before 12 weeks", "color": "cyan"}]},
         ]},

        {"type": "content", "label": "Coverage in India", "title": "How many women get full ANC?",
         "blocks": [
             {"t": "chart", "canvas": "ancTrendChart",
              "title": "Mothers with at least 4 antenatal visits, India (%)",
              "source": "NFHS rounds (NFHS-3, -4, -5); values rounded",
              "type": "bar",
              "data": {"labels": ["NFHS-3 (2005-06)", "NFHS-4 (2015-16)", "NFHS-5 (2019-21)"],
                       "datasets": [{"label": "4+ ANC visits (%)", "data": [37, 51, 59],
                                     "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100} } }"}},
             {"t": "hbox", "color": "green", "html": "Real improvement &mdash; but a large share of "
              "women still fall short of four visits, let alone eight. Early, complete ANC remains "
              "an unfinished agenda."},
         ]},

        {"type": "content", "label": "The Danger Signs", "title": "What every pregnant woman should know",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Vaginal bleeding",
                 "Severe headache, blurred vision (signs of pre-eclampsia)",
                 "High fever",
                 "Swelling of face and hands; convulsions",
                 "Reduced or absent fetal movement; leaking fluid"]},
             {"t": "hbox", "color": "amber", "html": "Teaching danger signs directly attacks "
              "<strong>Delay 1</strong>: a family that recognises the warning acts sooner."},
         ]},

        {"type": "content", "label": "Anaemia &amp; Nutrition", "title": "Fighting anaemia in pregnancy",
         "blocks": [
             {"t": "body", "html": "Because anaemia underlies so many maternal deaths, ANC screens "
              "haemoglobin and counsels on a diet richer in iron, alongside supplementation."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Hb test", "label": "every pregnant woman should be screened for anaemia",
                  "color": "indigo"},
                 {"num": "Diet + IFA", "label": "iron-rich food plus supplements is the core response",
                  "color": "green"}]},
         ]},

        {"type": "content", "label": "IFA", "title": "Iron and folic acid: the cheapest protection",
         "blocks": [
             {"t": "body", "html": "<strong>Iron and folic acid (IFA)</strong> supplements raise "
              "haemoglobin and prevent neural-tube defects. The standard advice is daily IFA through "
              "pregnancy and into the postpartum period."},
             {"t": "hbox", "color": "cyan", "html": "Cheap and effective &mdash; but only if women "
              "actually take the tablets. Counselling, supply and follow-up matter as much as the "
              "prescription itself."},
         ]},

        {"type": "content", "label": "TT / Td", "title": "Tetanus protection: a quiet success",
         "blocks": [
             {"t": "body", "html": "Tetanus toxoid (now Td) vaccination of pregnant women protects "
              "against <strong>maternal and neonatal tetanus</strong> &mdash; once a major killer of "
              "newborns through infected cord-cutting."},
             {"t": "hbox", "color": "green", "html": "Sustained TT coverage, alongside clean delivery, "
              "helped India eliminate maternal and neonatal tetanus as a public-health problem &mdash; "
              "proof that simple measures, at scale, save lives."},
         ]},

        {"type": "content", "label": "A Full ANC Visit", "title": "What a good check-up actually does",
         "compact": True,
         "blocks": [
             {"t": "bullets", "items": [
                 "Weigh, measure blood pressure, test haemoglobin and urine",
                 "Check fetal growth, position and heartbeat",
                 "Give IFA, calcium and TT/Td; treat infections",
                 "Counsel on diet, danger signs and birth planning",
                 "Identify high-risk pregnancies and plan referral"]},
             {"t": "hbox", "color": "amber", "html": "A visit that only records weight is not ANC. "
              "Quality &mdash; not just the tick-box of attendance &mdash; is what protects the mother."},
         ]},

        # ===================== SECTION 06 — Skilled birth (8) =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Skilled Birth &amp; Institutional Delivery"},

        {"type": "content", "label": "The Decisive Factor", "title": "A skilled attendant changes everything",
         "blocks": [
             {"t": "term", "word": "Skilled birth attendant (SBA)",
              "def": "An accredited health professional &mdash; doctor, nurse or midwife &mdash; "
              "trained to manage normal birth and to recognise, manage or refer complications."},
             {"t": "body", "html": "Because the deadliest complications strike during labour and "
              "the hours after, <strong>who attends the birth</strong> is the single most decisive "
              "factor in whether a mother lives."},
         ]},

        {"type": "content", "label": "Why Institutions", "title": "Why institutional delivery matters",
         "blocks": [
             {"t": "body", "html": "A facility birth brings the woman to where the drugs, equipment, "
              "blood and skills are &mdash; so that when haemorrhage or eclampsia strikes, the "
              "response is minutes away, not hours."},
             {"t": "hbox", "color": "red", "html": "A home birth with no trained help and no transport "
              "stacks all three delays at once. Institutional delivery is, above all, a strategy "
              "against delay."},
         ]},

        {"type": "content", "label": "The Trend", "title": "India's institutional-delivery surge",
         "blocks": [
             {"t": "chart", "canvas": "instDelivChart",
              "title": "Institutional births in India (%)",
              "source": "NFHS rounds (NFHS-3, -4, -5); values rounded",
              "type": "line",
              "data": {"labels": ["NFHS-3 (2005-06)", "NFHS-4 (2015-16)", "NFHS-5 (2019-21)"],
                       "datasets": [{"label": "Institutional delivery (%)",
                                     "data": [39, 79, 89],
                                     "borderColor": "#10B981",
                                     "backgroundColor": "rgba(16,185,129,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 5}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100} } }"}},
             {"t": "hbox", "color": "green", "html": "One of India's great public-health shifts: "
              "from under half to roughly nine in ten births in a facility within fifteen years."},
         ]},

        {"type": "content", "label": "The Lever", "title": "JSY: paying women to deliver safely",
         "blocks": [
             {"t": "body", "html": "<strong>Janani Suraksha Yojana (JSY)</strong>, launched in 2005 "
              "under the National Rural Health Mission, is a <strong>conditional cash transfer</strong>: "
              "it pays eligible women a cash incentive to give birth in a health facility."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "2005", "label": "JSY launched under NRHM", "color": "indigo",
                  "source": "MoHFW"},
                 {"num": "Cash on delivery", "label": "incentive paid for institutional birth, "
                  "with the ASHA as link", "color": "cyan"}]},
         ]},

        {"type": "content", "label": "How JSY Works", "title": "Demand-side financing, in practice",
         "blocks": [
             {"t": "body", "html": "JSY tackles the cost barrier behind Delays 1 and 2 &mdash; the "
              "money for transport, the wage lost, the fear of facility charges &mdash; by putting "
              "cash in the mother's hands for choosing a facility birth."},
             {"t": "hbox", "color": "amber", "html": "It is widely credited with driving the rise in "
              "institutional delivery. But cash gets her through the door; it cannot guarantee "
              "quality once she is inside &mdash; that is the next challenge."},
         ]},

        {"type": "content", "label": "Removing Cost", "title": "JSSK: free entitlements at delivery",
         "blocks": [
             {"t": "body", "html": "<strong>Janani Shishu Suraksha Karyakram (JSSK)</strong>, 2011, "
              "goes further: it entitles every pregnant woman to <strong>free</strong> delivery "
              "&mdash; including caesarean &mdash; in public facilities, with no out-of-pocket charge."},
             {"t": "bullets", "color": "green", "sm": True, "items": [
                 "Free delivery, drugs, diagnostics and diet",
                 "Free blood and free referral transport",
                 "Same free entitlements for sick newborns"]},
         ]},

        {"type": "content", "label": "JSY vs JSSK", "title": "Two schemes, two barriers",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "JSY (2005)", "JSSK (2011)"],
              "rows": [
                  ["Mechanism", "Cash incentive to the woman", "Free services, no charges"],
                  ["Barrier addressed", "Decision &amp; cost of coming", "Cost incurred at facility"],
                  ["Type", "Demand-side (conditional cash)", "Supply-side entitlement"],
                  ["Together", "Get her to come", "Make sure it costs her nothing"]]},
             {"t": "hbox", "color": "cyan", "html": "JSY pulls women in; JSSK removes the bill once "
              "they arrive. The two are designed to work hand in hand."},
         ]},

        {"type": "content", "label": "The Caveat", "title": "Coming is not the same as being cared for",
         "blocks": [
             {"t": "body", "html": "A facility birth only saves a life if the facility is <em>ready</em> "
              "&mdash; staffed, stocked, and able to manage an emergency. A crowded labour room without "
              "drugs or a skilled provider is a false promise."},
             {"t": "hbox", "color": "red", "html": "This is why India's focus has shifted from "
              "<em>getting women in</em> to <em>quality of care</em> &mdash; the agenda behind LaQshya "
              "and SUMAN, which we reach later."},
         ]},

        # ===================== SECTION 07 — EmONC (8) =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Emergency Obstetric &amp; Newborn Care"},

        {"type": "content", "label": "The Last Line", "title": "When prevention is not enough",
         "blocks": [
             {"t": "body", "html": "Some complications cannot be predicted or prevented &mdash; they "
              "simply happen. <strong>Emergency Obstetric and Newborn Care (EmONC)</strong> is the "
              "set of life-saving services that treat them when they do."},
             {"t": "hbox", "color": "red", "html": "Most women who develop a complication have no "
              "known risk factor beforehand. That is why <em>every</em> birth needs access to "
              "emergency care &mdash; not just the 'high-risk' ones."},
         ]},

        {"type": "content", "label": "Two Levels", "title": "Basic vs comprehensive EmONC",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Basic EmONC (BEmONC)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Delivered at PHC level without surgery: "
                   "the seven 'signal functions' that stabilise most emergencies."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Comprehensive (CEmONC)", "blocks": [
                  {"t": "body", "cls": "sm", "html": "BEmONC <em>plus</em> caesarean section and "
                   "safe blood transfusion &mdash; needs a hospital / FRU with theatre and blood bank."}]}]},
             {"t": "hbox", "color": "amber", "html": "A district needs enough of <em>both</em>, "
              "geographically spread, so that no woman is more than a short ride from the care she "
              "might suddenly need."},
         ]},

        {"type": "content", "label": "Signal Functions", "title": "The seven basic signal functions",
         "compact": True,
         "blocks": [
             {"t": "bullets", "sm": True, "items": [
                 "Give parenteral antibiotics (sepsis)",
                 "Give parenteral uterotonics (haemorrhage)",
                 "Give parenteral anticonvulsants &mdash; magnesium sulphate (eclampsia)",
                 "Manually remove the placenta",
                 "Remove retained products (post-abortion / post-delivery)",
                 "Perform assisted vaginal delivery",
                 "Perform basic newborn resuscitation"]},
             {"t": "hbox", "color": "cyan", "html": "CEmONC adds two more: <strong>caesarean section</strong> "
              "and <strong>blood transfusion</strong>. These nine functions define a facility's "
              "real capability."},
         ]},

        {"type": "content", "label": "Referral", "title": "The chain that makes EmONC work",
         "blocks": [
             {"t": "body", "html": "EmONC is only as good as the <strong>referral system</strong> that "
              "moves a woman from where she is to where the care is &mdash; fast, with the right "
              "information arriving ahead of her."},
             {"t": "bullets", "color": "indigo", "sm": True, "items": [
                 "Recognise the complication and decide to refer early",
                 "Pre-referral stabilisation (e.g. first dose of MgSO&#8324;)",
                 "Functioning transport (ambulance 102 / 108)",
                 "Communication so the receiving facility is ready"]},
         ]},

        {"type": "content", "label": "The Tool", "title": "The partograph: watching labour in time",
         "blocks": [
             {"t": "term", "word": "Partograph",
              "def": "A simple chart used during labour to track the baby's descent, cervical "
              "dilation, the mother's vitals and the fetal heartbeat against time &mdash; with "
              "'alert' and 'action' lines that signal when to intervene."},
             {"t": "body", "html": "By making slow or obstructed labour visible early, the partograph "
              "turns a creeping emergency into a timely decision to act or refer."},
         ]},

        {"type": "content", "label": "Reading It", "title": "Why the partograph saves lives",
         "blocks": [
             {"t": "body", "html": "When labour crosses the <strong>alert line</strong>, the team is "
              "warned; if it crosses the <strong>action line</strong>, intervention &mdash; "
              "augmentation, referral or caesarean &mdash; is overdue. It is a clock and a conscience "
              "in one page."},
             {"t": "hbox", "color": "green", "html": "Low-cost, low-tech, high-impact: the partograph "
              "needs no electricity and catches obstructed labour before it ruptures the uterus or "
              "kills the baby."},
         ]},

        {"type": "content", "label": "Newborn Side", "title": "The first minute: newborn resuscitation",
         "blocks": [
             {"t": "body", "html": "Many newborns who do not breathe at birth can be revived with "
              "simple <strong>bag-and-mask resuscitation</strong> in the first minute &mdash; the "
              "'golden minute'. No baby should die for want of this basic skill."},
             {"t": "hbox", "color": "amber", "html": "Skilling every birth attendant in newborn "
              "resuscitation links maternal and newborn survival: the same hands, the same moment, "
              "two lives."},
         ]},

        {"type": "content", "label": "System Readiness", "title": "What 'ready' really means",
         "blocks": [
             {"t": "bullets", "color": "cyan", "items": [
                 "<strong>People:</strong> a skilled provider on duty, every shift",
                 "<strong>Drugs:</strong> oxytocin, magnesium sulphate, antibiotics in stock",
                 "<strong>Blood:</strong> a functioning supply for haemorrhage",
                 "<strong>Theatre:</strong> a working space for caesarean",
                 "<strong>Transport:</strong> referral that actually moves"]},
             {"t": "hbox", "color": "red", "html": "A single missing link &mdash; a stockout, an absent "
              "doctor, a broken ambulance &mdash; can convert a survivable emergency into a death. "
              "Readiness is a whole-system property."},
         ]},

        # ===================== SECTION 08 — Postnatal & newborn (8) =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Postnatal &amp; Newborn Care"},

        {"type": "content", "label": "The Forgotten Window", "title": "After birth: the neglected period",
         "blocks": [
             {"t": "body", "html": "Care often stops at delivery &mdash; yet a large share of maternal "
              "and most newborn deaths occur <em>after</em> birth. The <strong>postnatal period</strong> "
              "is the most dangerous and the most neglected part of the continuum."},
             {"t": "hbox", "color": "red", "html": "Women discharged within hours of delivery, with no "
              "follow-up, are sent home into the very window when haemorrhage and infection strike."},
         ]},

        {"type": "content", "label": "The Timeline", "title": "The critical first 48 hours and 6 weeks",
         "blocks": [
             {"t": "flow", "steps": [
                 "FIRST 24 HOURS: highest risk of PPH &mdash; do not discharge early",
                 "FIRST 48 HOURS: watch bleeding, BP, infection, breastfeeding",
                 "FIRST WEEK: home visits for mother &amp; newborn",
                 "FIRST 6 WEEKS: complete recovery &amp; family-planning counselling"]},
             {"t": "hbox", "color": "amber", "html": "WHO recommends at least the first postnatal "
              "contact within 24 hours, with further contacts over the following weeks &mdash; for "
              "facility and home births alike."},
         ]},

        {"type": "content", "label": "The Main Threat", "title": "Postpartum haemorrhage after birth",
         "blocks": [
             {"t": "body", "html": "<strong>Postpartum haemorrhage (PPH)</strong> &mdash; excessive "
              "bleeding after delivery &mdash; remains the top cause of postnatal maternal death. It "
              "can begin suddenly and kill within an hour or two."},
             {"t": "hbox", "color": "green", "html": "Active management of the third stage of labour "
              "&mdash; a uterotonic at delivery, controlled cord traction, uterine massage &mdash; "
              "prevents most PPH. Vigilance in the first hours catches the rest."},
         ]},

        {"type": "content", "label": "Home Outreach", "title": "Bringing care to the doorstep: HBNC",
         "blocks": [
             {"t": "body", "html": "India's <strong>Home-Based Newborn Care (HBNC)</strong> programme "
              "has ASHAs visit mother and newborn at home on a fixed schedule in the first six weeks "
              "&mdash; checking, counselling, and referring danger signs."},
             {"t": "hbox", "color": "cyan", "html": "These visits catch the deaths that the facility, "
              "by discharging early, would otherwise miss &mdash; and reach the women least likely to "
              "return on their own."},
         ]},

        {"type": "content", "label": "Newborn Danger Signs", "title": "Warning signs in the baby",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Not feeding well or unable to suckle",
                 "Fast, difficult, or very slow breathing",
                 "Fever or, dangerously, low body temperature",
                 "Lethargy, reduced movement, or convulsions",
                 "Yellowness, or redness/discharge at the cord"]},
             {"t": "hbox", "color": "amber", "html": "Most newborn deaths happen in the first week. "
              "Teaching families to recognise these signs &mdash; and to act &mdash; is core to "
              "postnatal care."},
         ]},

        {"type": "content", "label": "Warmth &amp; Skin-to-Skin", "title": "Kangaroo Mother Care",
         "blocks": [
             {"t": "body", "html": "<strong>Kangaroo Mother Care (KMC)</strong> &mdash; continuous "
              "skin-to-skin contact, exclusive breastfeeding, and early discharge with support &mdash; "
              "dramatically improves survival of small and preterm babies."},
             {"t": "hbox", "color": "green", "html": "Low-cost and powerful: the mother's body provides "
              "the warmth, the feeding and the bonding an incubator cannot. It works even where "
              "technology is scarce."},
         ]},

        {"type": "content", "label": "Breastfeeding", "title": "The first hour, then six months",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "First hour", "label": "early initiation of breastfeeding within an hour "
                  "of birth", "color": "cyan"},
                 {"num": "6 months", "label": "exclusive breastfeeding &mdash; nothing but breast "
                  "milk", "color": "green"}]},
             {"t": "body", "html": "Early and exclusive breastfeeding protects the newborn against "
              "infection and undernutrition &mdash; one of the most cost-effective child-survival "
              "interventions known."},
         ]},

        {"type": "content", "label": "Mother &amp; Baby Together", "title": "Postnatal care is a package",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Mother:</strong> check bleeding, BP, infection, mood, breastfeeding",
                 "<strong>Newborn:</strong> weight, warmth, feeding, danger signs, immunisation",
                 "<strong>Counsel:</strong> nutrition, hygiene, and birth spacing",
                 "<strong>Refer:</strong> any danger sign in either, without delay"]},
             {"t": "hbox", "color": "indigo", "html": "Mother and baby are one clinical unit in this "
              "window. Care that treats them together &mdash; at home and at the facility &mdash; "
              "closes the deadliest gap in the continuum."},
         ]},

        # ===================== SECTION 09 — FP & safe abortion (8) =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Family Planning &amp; Safe Abortion"},

        {"type": "content", "label": "The Link", "title": "Family planning is maternal survival",
         "blocks": [
             {"t": "body", "html": "Every pregnancy carries risk. Letting women choose <strong>whether, "
              "when and how often</strong> to become pregnant directly reduces the number of "
              "high-risk pregnancies &mdash; and so reduces maternal death."},
             {"t": "hbox", "color": "green", "html": "Family planning is one of the most cost-effective "
              "ways to save mothers' lives: fewer unintended pregnancies, fewer unsafe abortions, "
              "fewer dangerous births."},
         ]},

        {"type": "content", "label": "Birth Spacing", "title": "Why timing and spacing matter",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Too young:</strong> adolescent bodies face higher risk of obstructed labour, "
                 "eclampsia and death",
                 "<strong>Too close:</strong> pregnancies spaced under two years deplete the mother "
                 "and raise risk",
                 "<strong>Too many:</strong> high parity compounds the cumulative danger",
                 "<strong>Too old:</strong> risk rises again at the upper end of reproductive age"]},
             {"t": "hbox", "color": "cyan", "html": "Avoiding the 'too young, too close, too many, too "
              "old' pregnancies is a direct maternal-health intervention."},
         ]},

        {"type": "content", "label": "Unmet Need", "title": "Women who want to space but cannot",
         "blocks": [
             {"t": "term", "word": "Unmet need for family planning",
              "def": "The share of women who want to delay or avoid pregnancy but are not using any "
              "method of contraception &mdash; a gap between desire and access."},
             {"t": "body", "html": "Closing unmet need &mdash; through supply, choice and counselling "
              "&mdash; prevents unintended pregnancies and the unsafe abortions and risky births that "
              "follow them."},
         ]},

        {"type": "content", "label": "The Basket", "title": "A range of methods, freely chosen",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Type", "Examples", "Note"],
              "rows": [
                  ["Spacing", "Condoms, pills, injectables, IUCD", "Reversible; user's choice"],
                  ["Long-acting", "IUCD, implants", "Effective for years, reversible"],
                  ["Permanent", "Female &amp; male sterilisation", "For those who want no more children"],
                  ["Emergency", "Emergency contraceptive pill", "After unprotected sex"]]},
             {"t": "hbox", "color": "amber", "html": "The principle is <strong>informed choice</strong>, "
              "not targets. India's expanded basket (injectables, the Antara programme) widens options "
              "&mdash; quality counselling makes them real."},
         ]},

        {"type": "content", "label": "Rights, Not Targets", "title": "From population control to choice",
         "blocks": [
             {"t": "body", "html": "Historically, family-planning programmes chased demographic "
              "<strong>targets</strong>, sometimes coercively. The modern, rights-based approach "
              "centres the woman's voluntary, informed decision."},
             {"t": "hbox", "color": "red", "html": "Coercion &mdash; quotas, incentives that distort "
              "choice, camp sterilisations without consent &mdash; is both a rights violation and bad "
              "public health. Voluntary, quality services work better."},
         ]},

        {"type": "content", "label": "Safe Abortion", "title": "Unsafe abortion is a preventable death",
         "blocks": [
             {"t": "body", "html": "Where safe, legal abortion is unavailable, women resort to unsafe "
              "methods &mdash; a wholly preventable cause of maternal death and injury. Access to safe "
              "abortion is a pillar of maternal survival."},
             {"t": "hbox", "color": "green", "html": "The remedy is straightforward: legal services, "
              "trained providers, and the medicines and procedures that make abortion safe."},
         ]},

        {"type": "content", "label": "The Law", "title": "India's MTP Act framework",
         "blocks": [
             {"t": "body", "html": "The <strong>Medical Termination of Pregnancy (MTP) Act</strong> "
              "permits abortion under defined conditions by registered providers. The 2021 amendment "
              "expanded grounds and raised the gestational limit in specified circumstances."},
             {"t": "bullets", "color": "cyan", "sm": True, "items": [
                 "Permitted on health, fetal, contraceptive-failure and other grounds",
                 "Must be performed by a registered medical practitioner",
                 "2021 amendment widened access and confidentiality protections"]},
         ]},

        {"type": "content", "label": "Law vs Access", "title": "Legal does not yet mean reachable",
         "blocks": [
             {"t": "body", "html": "A permissive law is necessary but not sufficient. Women still face "
              "stigma, provider shortages, lack of awareness, and refusal &mdash; so unsafe abortion "
              "persists despite legality."},
             {"t": "hbox", "color": "amber", "html": "Bridging the gap between the law on paper and "
              "services on the ground &mdash; trained providers, supplies, non-judgemental care &mdash; "
              "is the unfinished task."},
         ]},

        # ===================== SECTION 10 — Equity (8) =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Social Determinants &amp; Equity"},

        {"type": "content", "label": "The Deeper Causes", "title": "Beyond the clinic: why some women die",
         "blocks": [
             {"t": "body", "html": "Clinical causes are the <em>how</em>; social determinants are the "
              "<em>why</em>. Poverty, gender, caste, education and geography decide who reaches care "
              "in time &mdash; and who does not."},
             {"t": "hbox", "color": "cyan", "html": "Two women with the same complication can face very "
              "different odds, set long before labour begins, by where and to whom they were born."},
         ]},

        {"type": "content", "label": "Early Marriage", "title": "Child marriage &amp; adolescent pregnancy",
         "blocks": [
             {"t": "body", "html": "Girls married and pregnant as adolescents face far higher risk: "
              "their bodies are not ready, they have less power to seek care, and they are more likely "
              "to suffer obstructed labour and eclampsia."},
             {"t": "hbox", "color": "red", "html": "Delaying marriage and first pregnancy &mdash; "
              "through education, agency and enforcement of the legal age &mdash; is one of the most "
              "powerful upstream maternal-health interventions."},
         ]},

        {"type": "content", "label": "Anaemia &amp; Nutrition", "title": "Lifelong undernutrition, compounded",
         "blocks": [
             {"t": "body", "html": "A girl undernourished and anaemic through childhood enters "
              "pregnancy already depleted. Maternal anaemia is not just a clinical fact &mdash; it is "
              "the biological signature of a lifetime of inequality."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "~57%", "label": "of pregnant women in India anaemic", "color": "red",
                  "source": "NFHS-5, 2019&ndash;21"},
                 {"num": "Life course", "label": "nutrition before pregnancy matters as much as "
                  "during it", "color": "amber"}]},
         ]},

        {"type": "content", "label": "The Gaps", "title": "Caste, poverty and region",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Caste:</strong> Dalit and Adivasi women face worse access and outcomes",
                 "<strong>Poverty:</strong> the poorest quintile lags on ANC, skilled birth and survival",
                 "<strong>Region:</strong> MMR varies several-fold across Indian states",
                 "<strong>Rural &amp; remote:</strong> distance and weak facilities raise every delay"]},
             {"t": "hbox", "color": "amber", "html": "National averages hide these gaps. Equity means "
              "asking not just 'how many?' but '<em>which</em> women are still dying, and where?'"},
         ]},

        {"type": "content", "label": "See the Gap", "title": "Why disaggregation matters",
         "blocks": [
             {"t": "chart", "canvas": "equityGapChart",
              "title": "Skilled birth attendance by wealth group (illustrative pattern)",
              "source": "Illustrative; patterned on NFHS-style wealth gradients",
              "type": "bar",
              "data": {"labels": ["Overall", "Richest", "Middle", "Poorest"],
                       "datasets": [{"label": "Skilled birth attendance (%)",
                                     "data": [89, 96, 90, 78],
                                     "backgroundColor": ["#6366F1", "#10B981", "#0EA5E9", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:100} } }"}},
             {"t": "hbox", "color": "cyan", "html": "A good national average can still hide a poorest "
              "group left far behind. Disaggregation is how equity becomes visible &mdash; and "
              "actionable."},
         ]},

        {"type": "content", "label": "Gender &amp; Power", "title": "Whose body, whose decision?",
         "blocks": [
             {"t": "body", "html": "Maternal health sits inside gender relations. When a woman cannot "
              "decide to seek care, control household money, or move without permission, her survival "
              "depends on others' choices."},
             {"t": "hbox", "color": "indigo", "html": "Empowering women &mdash; education, income, "
              "mobility, voice &mdash; is not adjacent to maternal health. It is maternal health, "
              "working through Delay 1."},
         ]},

        {"type": "content", "label": "Dignity in Birth", "title": "Respectful maternity care",
         "blocks": [
             {"t": "term", "word": "Respectful maternity care (RMC)",
              "def": "Care that preserves a woman's dignity, privacy, consent and choice during "
              "pregnancy and childbirth &mdash; free from abuse, neglect or discrimination."},
             {"t": "body", "html": "How a woman is treated is not a soft extra. Disrespect drives "
              "women away from facilities &mdash; reintroducing Delay 1 even where services exist."},
         ]},

        {"type": "content", "label": "The Shadow Side", "title": "Obstetric violence",
         "blocks": [
             {"t": "body", "html": "<strong>Obstetric violence</strong> &mdash; verbal abuse, "
              "non-consented procedures, neglect, discrimination by caste or poverty, demands for "
              "informal payment &mdash; is a real and documented barrier in many facilities."},
             {"t": "hbox", "color": "red", "html": "A woman mistreated once may never return &mdash; "
              "and may warn others away. Respectful care is therefore not only ethical; it is "
              "essential to keeping the gains in institutional delivery."},
         ]},

        # ===================== SECTION 11 — India's programmes & progress (8) =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "India's Programmes &amp; Progress"},

        {"type": "content", "label": "The Architecture", "title": "The National Health Mission",
         "blocks": [
             {"t": "body", "html": "India's maternal-health effort runs through the "
              "<strong>National Health Mission (NHM)</strong> &mdash; the umbrella under which JSY, "
              "JSSK, the ASHA cadre and quality programmes sit and connect."},
             {"t": "hbox", "color": "cyan", "html": "Think of NHM as the system; the schemes that "
              "follow are its instruments &mdash; each targeting a specific delay or stage of the "
              "continuum."},
         ]},

        {"type": "content", "label": "The Scheme Map", "title": "How the programmes fit together",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Programme", "What it does", "Targets"],
              "rows": [
                  ["JSY (2005)", "Cash incentive for facility birth", "Delays 1 &amp; 2"],
                  ["JSSK (2011)", "Free delivery, drugs, transport, blood", "Delay 2 &amp; cost"],
                  ["PMSMA", "Fixed-day free quality antenatal check-ups", "ANC stage"],
                  ["LaQshya", "Labour-room &amp; maternity-OT quality", "Delay 3 / quality"],
                  ["SUMAN", "Assured, free, dignified maternal &amp; newborn care", "Whole continuum"]]},
             {"t": "hbox", "color": "indigo", "html": "Read down the column: the schemes evolved from "
              "<em>getting women in</em> toward <em>guaranteeing quality and dignity</em> once they "
              "arrive."},
         ]},

        {"type": "content", "label": "The Frontline", "title": "ASHAs: the million-strong link",
         "blocks": [
             {"t": "body", "html": "The <strong>Accredited Social Health Activist (ASHA)</strong> "
              "&mdash; a local woman trained as a community health worker &mdash; is the hinge of "
              "India's maternal-health system: mobilising, accompanying, following up, and earning "
              "incentives for each link she completes."},
             {"t": "hbox", "color": "green", "html": "Nearly a million ASHAs connect households to the "
              "system. Much of India's progress on institutional delivery and ANC runs through them."},
         ]},

        {"type": "content", "label": "Quality Push", "title": "From access to assured quality",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "LaQshya", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Labour Room Quality Improvement &mdash; raising "
                   "the standard of care in labour rooms and maternity operating theatres."}]}],
              "right": [{"t": "panel", "color": "green", "title": "SUMAN", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Surakshit Matritva Aashwasan &mdash; an "
                   "<em>assurance</em> of free, zero-expense, dignified and respectful care for every "
                   "mother and newborn."}]}]},
             {"t": "hbox", "color": "amber", "html": "These mark India's strategic shift: the next "
              "lives to be saved depend less on coverage and more on <strong>quality and respect</strong>."},
         ]},

        {"type": "content", "label": "The Progress", "title": "India's MMR has fallen markedly",
         "blocks": [
             {"t": "chart", "canvas": "mmrDeclineChart",
              "title": "Maternal Mortality Ratio, India (per 100,000 live births)",
              "source": "SRS Special Bulletins on Maternal Mortality; values illustrative of the "
                        "well-established declining trend",
              "type": "line",
              "data": {"labels": ["2004-06", "2007-09", "2010-12", "2014-16", "2016-18", "2018-20"],
                       "datasets": [{"label": "MMR",
                                     "data": [254, 212, 178, 130, 113, 97],
                                     "borderColor": "#EF4444",
                                     "backgroundColor": "rgba(239,68,68,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 5}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0} } }"}},
             {"t": "hbox", "color": "green", "html": "A steep, sustained decline per the SRS &mdash; "
              "India has roughly crossed the SDG-aligned national threshold, though several states "
              "still lag well behind."},
         ]},

        {"type": "content", "label": "Unfinished Agenda", "title": "Progress is real, but uneven",
         "blocks": [
             {"t": "body", "html": "The national average improves while the gaps persist: high-burden "
              "states, poorer districts, and marginalised groups still face MMRs far above the target."},
             {"t": "hbox", "color": "red", "html": "The next phase is about <strong>equity and quality</strong>: "
              "reaching the last women, in the hardest places, with care that is not only available but "
              "good and respectful."},
         ]},

        {"type": "content", "label": "Measuring It", "title": "How we know if we are winning",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Indicator", "What it tells you", "Source"],
              "rows": [
                  ["MMR", "Deaths per 100,000 live births", "SRS"],
                  ["Institutional delivery (%)", "Where women give birth", "NFHS / HMIS"],
                  ["4+ / 8 ANC contacts (%)", "Antenatal coverage", "NFHS"],
                  ["Skilled birth attendance (%)", "Who attends the birth", "NFHS"],
                  ["Maternal death review", "Why each death happened", "Facility / community MDR"]]},
             {"t": "hbox", "color": "cyan", "html": "Counting deaths is not enough &mdash; "
              "<strong>maternal death reviews</strong> ask <em>why</em> each one happened, turning "
              "numbers back into the three delays you can fix."},
         ]},

        {"type": "content", "label": "Further Reading", "title": "Where to go next",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<strong>WHO</strong> &mdash; recommendations on antenatal, intrapartum &amp; postnatal care",
                 "<strong>SRS Special Bulletins</strong> on Maternal Mortality (Census office)",
                 "<strong>NFHS-5</strong> national &amp; state fact sheets (IIPS / MoHFW)",
                 "<strong>MoHFW</strong> guidelines: JSY, JSSK, PMSMA, LaQshya, SUMAN, HBNC",
                 "<em>Thaddeus &amp; Maine (1994)</em> &mdash; 'Too far to walk', the three-delays paper"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Public Health</strong>, <strong>Gender</strong> and <strong>Nutrition</strong> "
              "101 courses."},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Maternal Health 101 &middot; Complete",
         "headline": "No woman should die<br>giving life.",
         "byline": "Most maternal deaths are preventable &mdash; if we close the three delays, hold "
                   "the continuum of care, and reach the last woman in the hardest place. Explore the "
                   "rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
