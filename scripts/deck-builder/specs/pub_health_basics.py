# -*- coding: utf-8 -*-
"""
Public Health 101 — ImpactMojo 101 Series (native deck spec)
Foundational public health for development & health practitioners in South Asia.
Build: python3 scripts/deck-builder/build.py pub_health_basics
"""

DECK = {
    "slug": "pub-health-basics",
    "title": "Public Health 101",
    "description": ("Public Health 101 — a free foundational course for development and "
                    "health practitioners in South Asia: population health and prevention, "
                    "social determinants, epidemiology, disease burden, health systems and "
                    "India's path to universal health coverage. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Public<br>Health<br>101",
         "sub": "Population Health, Prevention &amp; Health Systems &mdash; a Foundational "
                "Course for Development &amp; Health Practitioners in South Asia",
         "tags": ["Research-Backed", "India Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Public Health Is"},
             {"name": "Social Determinants of Health"},
             {"name": "Epidemiology Basics"},
             {"name": "Measuring Population Health"},
             {"name": "Communicable Disease &amp; Immunisation"},
             {"name": "Non-Communicable Diseases"},
             {"name": "Maternal, Newborn, Child Health &amp; Nutrition"},
             {"name": "Health Systems"},
             {"name": "India's Health System"},
             {"name": "Health Equity &amp; Global Health"},
             {"name": "Prevention in Practice &amp; Further Reading"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Public Health Is"},

        {"type": "content", "label": "Definition", "title": "Health is more than the absence of disease",
         "blocks": [
             {"t": "quote",
              "text": "Health is a state of complete physical, mental and social well-being, "
              "and not merely the absence of disease or infirmity.",
              "attr": "&mdash; Constitution of the World Health Organization, 1946"},
             {"t": "body", "html": "<strong>Public health</strong> takes that definition and "
              "applies it not to one patient but to whole populations &mdash; villages, districts, "
              "nations. Its unit of concern is the group, not the individual."},
             {"t": "hbox", "color": "cyan", "html": "A clinician asks 'why is this patient ill?'. "
              "Public health asks 'why are these people ill, and how do we stop the next thousand "
              "from falling ill?'"},
         ]},

        {"type": "content", "label": "The Core Idea", "title": "Population health, not one patient at a time",
         "blocks": [
             {"t": "term", "word": "Public health",
              "def": "The science and art of preventing disease, prolonging life and promoting "
              "health through the organised efforts of society &mdash; acting on populations and "
              "the conditions that shape their health."},
             {"t": "term", "word": "Population health",
              "def": "The health outcomes of a group of people and the distribution of those "
              "outcomes within the group &mdash; including the gaps between rich and poor."},
         ]},

        {"type": "content", "label": "Two Models", "title": "Clinical care vs the public health approach",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["", "Clinical / curative care", "Public health"],
              "rows": [
                  ["Unit", "The individual patient", "The population"],
                  ["Timing", "After illness appears", "Before illness appears (mostly)"],
                  ["Focus", "Diagnosis &amp; treatment", "Prevention &amp; promotion"],
                  ["Setting", "Hospital, clinic", "Community, policy, environment"],
                  ["Measure of success", "Patient recovers", "Fewer people fall ill"]]},
             {"t": "hbox", "color": "amber", "html": "They are partners, not rivals. A strong "
              "health system needs both the doctor who treats the case and the system that "
              "prevents the next outbreak."},
         ]},

        {"type": "content", "label": "Prevention First", "title": "The cliff and the ambulance",
         "blocks": [
             {"t": "body", "html": "An old parable: people keep falling off a cliff, so the village "
              "stations an <em>ambulance at the bottom</em>. Public health asks why we do not build "
              "a <strong>fence at the top</strong>. Prevention is the fence."},
             {"t": "flow", "steps": [
                 "Treat the sick (ambulance at the bottom)",
                 "Detect early (catch them on the way down)",
                 "Prevent exposure (a fence at the top)",
                 "Change the conditions (move the path away from the edge)"]},
         ]},

        {"type": "content", "label": "What It Acts On", "title": "Public health works upstream",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Downstream (clinical)", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Treat the diarrhoea case",
                      "Prescribe ORS &amp; antibiotics",
                      "Rehydrate the dehydrated child"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Upstream (public health)", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Safe drinking water &amp; sanitation",
                      "Handwashing &amp; hygiene promotion",
                      "Rotavirus vaccine in the schedule"]}]}]},
             {"t": "hbox", "color": "cyan", "html": "The further upstream you act, the more people "
              "you protect &mdash; and usually the cheaper it is per life saved."},
         ]},

        {"type": "content", "label": "The Core Functions", "title": "What public health systems actually do",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Assessment:</strong> monitor health, detect outbreaks, diagnose problems",
                 "<strong>Policy:</strong> develop laws and plans that protect health",
                 "<strong>Assurance:</strong> ensure services, a competent workforce and access",
                 "<strong>Promotion:</strong> inform and empower people about health",
                 "<strong>Equity:</strong> work so that everyone has a fair chance at health"]},
         ]},

        {"type": "content", "label": "Why It Pays", "title": "Prevention is one of the best buys in development",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Immunisation", "label": "among the most cost-effective health "
                  "investments known", "color": "green", "source": "WHO"},
                 {"num": "Water &amp; sanitation", "label": "every rupee returns several in "
                  "averted illness &amp; lost work", "color": "cyan"},
                 {"num": "Tobacco control", "label": "taxes and bans save lives at almost no "
                  "cost to the state", "color": "indigo"}]},
             {"t": "hbox", "color": "amber", "html": "Returns are illustrative of a robust pattern: "
              "prevention typically costs far less per life-year saved than late-stage treatment."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Social Determinants of Health"},

        {"type": "content", "label": "The Big Insight", "title": "Most of what makes us healthy lies outside the clinic",
         "blocks": [
             {"t": "body", "html": "Where you are born, grow, live, work and age shapes your health "
              "far more than the medicines you take. These conditions are the "
              "<strong>social determinants of health</strong>."},
             {"t": "term", "word": "Social determinants of health (SDH)",
              "def": "The non-medical conditions &mdash; income, education, housing, water, "
              "sanitation, caste, gender, environment &mdash; that shape health and drive the "
              "unfair gaps between groups."},
         ]},

        {"type": "content", "label": "The Rainbow", "title": "The Dahlgren&ndash;Whitehead model",
         "blocks": [
             {"t": "body", "html": "The classic 'rainbow' model places the individual at the centre "
              "and wraps successive layers of influence around them &mdash; each layer something "
              "policy can act on."},
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 760 300" width="100%" style="max-height:320px">'
                 '<g font-family="inherit" text-anchor="middle">'
                 '<path d="M40 290 A 360 360 0 0 1 720 290 Z" fill="rgba(99,102,241,0.18)" stroke="#6366F1"/>'
                 '<path d="M110 290 A 290 290 0 0 1 650 290 Z" fill="rgba(14,165,233,0.18)" stroke="#0EA5E9"/>'
                 '<path d="M180 290 A 220 220 0 0 1 580 290 Z" fill="rgba(16,185,129,0.20)" stroke="#10B981"/>'
                 '<path d="M250 290 A 150 150 0 0 1 510 290 Z" fill="rgba(245,158,11,0.22)" stroke="#F59E0B"/>'
                 '<text x="380" y="282" font-size="14" font-weight="700" fill="#fff">Age, sex &amp; constitution</text>'
                 '<text x="380" y="232" font-size="13" fill="#fff">Individual lifestyle</text>'
                 '<text x="380" y="176" font-size="13" fill="#fff">Social &amp; community networks</text>'
                 '<text x="380" y="120" font-size="13" fill="#fff">Living &amp; working conditions</text>'
                 '<text x="380" y="60" font-size="13" fill="#fff">General socio-economic, cultural &amp; environmental conditions</text>'
                 '</g></svg>')},
         ]},

        {"type": "content", "label": "Postcode vs Genes", "title": "Your postcode can matter more than your genetic code",
         "blocks": [
             {"t": "body", "html": "Two children born the same day in the same city can differ by "
              "many years in life expectancy &mdash; not because of their genes, but because of the "
              "neighbourhood, water, schooling and income they are born into."},
             {"t": "hbox", "color": "red", "html": "A poor child in a low-income district faces "
              "higher infant mortality, more stunting and shorter life expectancy than a richer "
              "child a few kilometres away. The gap is made, not given."},
         ]},

        {"type": "content", "label": "The Gradient", "title": "Marmot: health follows a social gradient",
         "blocks": [
             {"t": "body", "html": "Sir Michael Marmot's work showed health is not simply "
              "'rich = healthy, poor = sick'. It runs as a <strong>gradient</strong>: at every "
              "step down the social ladder, health gets a little worse &mdash; all the way up."},
             {"t": "quote",
              "text": "Why treat people and send them back to the conditions that made them sick?",
              "attr": "&mdash; Sir Michael Marmot"},
         ]},

        {"type": "content", "label": "Inequalities", "title": "Health inequality vs health inequity",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Inequality", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Any difference in health between groups. "
                   "Some are natural &mdash; the old are frailer than the young."}]}],
              "right": [{"t": "panel", "color": "red", "title": "Inequity", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Differences that are <em>avoidable, unfair "
                   "and unjust</em> &mdash; a Dalit child stunted because of caste and poverty. "
                   "These are the public-health target."}]}]},
             {"t": "hbox", "color": "amber", "html": "Public health is not only about lowering "
              "averages &mdash; it is about closing unjust gaps."},
         ]},

        {"type": "content", "label": "South Asia", "title": "Determinants that bite hardest in the region",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Determinant", "Why it matters here"],
              "rows": [
                  ["Sanitation", "Open defecation drives diarrhoea, worms and stunting"],
                  ["Clean cooking fuel", "Biomass smoke fuels respiratory disease in women"],
                  ["Caste &amp; tribe", "Dalit &amp; Adivasi communities face worse outcomes"],
                  ["Gender", "Son preference, anaemia, unpaid care work, mobility"],
                  ["Air quality", "Among the world's most polluted air in many cities"],
                  ["Income &amp; informality", "Most workers lack sick pay or health cover"]]},
         ]},

        {"type": "content", "label": "Causes of Causes", "title": "Treat the causes of the causes",
         "blocks": [
             {"t": "flow", "steps": [
                 "OUTCOME: a child has diarrhoea",
                 "CAUSE: contaminated water",
                 "CAUSE OF THE CAUSE: no piped supply or toilet",
                 "ROOT: poverty, weak local governance, exclusion"]},
             {"t": "hbox", "color": "cyan", "html": "Marmot's phrase: behind the medical cause sits "
              "a <strong>cause of the cause</strong>. Real prevention works on those roots."},
         ]},

        {"type": "content", "label": "Action", "title": "Health in all policies",
         "blocks": [
             {"t": "body", "html": "Because health is made outside the clinic, improving it needs "
              "more than the health ministry. Roads, water, schools, food, housing and jobs are "
              "all health policy &mdash; the idea of <strong>health in all policies</strong>."},
             {"t": "hbox", "color": "green", "html": "A new toilet, a girls' school, a clean-fuel "
              "subsidy or a minimum wage can do more for health than a new hospital wing."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Epidemiology Basics"},

        {"type": "content", "label": "The Toolkit", "title": "Epidemiology is public health's detective science",
         "blocks": [
             {"t": "term", "word": "Epidemiology",
              "def": "The study of how often diseases and health states occur in populations, "
              "where, in whom, and why &mdash; and how to control them. It is the basic science "
              "of public health."},
             {"t": "body", "html": "Epidemiology answers the classic questions: "
              "<strong>who, where, when</strong> (descriptive) and <strong>why and how</strong> "
              "(analytic). From John Snow's 1854 cholera map onward, it has driven prevention."},
         ]},

        {"type": "content", "label": "Two Key Measures", "title": "Incidence vs prevalence",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Incidence", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>NEW</strong> cases arising over a "
                   "<em>period</em>. Measures the <em>risk</em> of getting the disease &mdash; the "
                   "speed of the tap filling the sink."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Prevalence", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>ALL</strong> existing cases at a "
                   "<em>point</em> in time. Measures the <em>burden</em> &mdash; how much water is "
                   "in the sink right now."}]}]},
             {"t": "hbox", "color": "amber", "html": "A long-lasting disease like diabetes has high "
              "prevalence even with modest incidence; a quick illness like flu can have high "
              "incidence but low prevalence at any instant."},
         ]},

        {"type": "content", "label": "Worked Example", "title": "Incidence and prevalence, side by side",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Incidence", "label": "= new cases in a period &divide; population at "
                  "risk &mdash; e.g. new TB cases per 100,000 per year", "color": "cyan"},
                 {"num": "Prevalence", "label": "= all current cases &divide; total population "
                  "&mdash; e.g. % of adults living with diabetes today", "color": "indigo"}]},
             {"t": "hbox", "color": "red", "html": "Mixing them up misleads. A fall in prevalence "
              "could mean fewer new cases &mdash; or simply that more patients died. Always ask "
              "which one a figure is."},
         ]},

        {"type": "content", "label": "Rates &amp; Ratios", "title": "Rate, ratio and proportion",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Term", "What it is", "Example"],
              "rows": [
                  ["Proportion", "Part out of a whole (the part is in the whole)", "% of children fully immunised"],
                  ["Ratio", "One quantity relative to another", "Sex ratio: females per 1,000 males"],
                  ["Rate", "Events per population per unit time", "Deaths per 1,000 per year"]]},
             {"t": "hbox", "color": "cyan", "html": "Always demand the <strong>denominator</strong>: "
              "per 1,000 people, per 100,000 live births, per year. A bare count cannot be compared."},
         ]},

        {"type": "content", "label": "The Triad", "title": "The epidemiological triad",
         "blocks": [
             {"t": "body", "html": "Classic model of infectious disease: an outbreak needs an "
              "<strong>agent</strong>, a susceptible <strong>host</strong> and a favourable "
              "<strong>environment</strong> &mdash; all three meeting through a vector or route."},
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 600 260" width="100%" style="max-height:280px">'
                 '<g font-family="inherit" text-anchor="middle" font-size="14" font-weight="700">'
                 '<polygon points="300,40 70,220 530,220" fill="none" stroke="#0EA5E9" stroke-width="2"/>'
                 '<circle cx="300" cy="40" r="34" fill="rgba(14,165,233,0.25)" stroke="#0EA5E9"/>'
                 '<text x="300" y="45" fill="#fff">AGENT</text>'
                 '<circle cx="70" cy="220" r="34" fill="rgba(16,185,129,0.25)" stroke="#10B981"/>'
                 '<text x="70" y="225" fill="#fff">HOST</text>'
                 '<circle cx="530" cy="220" r="40" fill="rgba(245,158,11,0.25)" stroke="#F59E0B"/>'
                 '<text x="530" y="218" fill="#fff">ENVIRON-</text>'
                 '<text x="530" y="234" fill="#fff">MENT</text>'
                 '</g></svg>')},
             {"t": "hbox", "color": "green", "html": "Break any side of the triangle &mdash; kill "
              "the agent, protect the host, fix the environment &mdash; and transmission stops."},
         ]},

        {"type": "content", "label": "Outbreaks", "title": "Investigating an outbreak, step by step",
         "compact": True,
         "blocks": [
             {"t": "flow", "steps": [
                 "Confirm the outbreak &amp; the diagnosis",
                 "Define a case &mdash; person, place, time",
                 "Find cases &amp; describe (epidemic curve, map)",
                 "Form &amp; test a hypothesis on the source",
                 "Control measures &amp; communicate"]},
             {"t": "hbox", "color": "cyan", "html": "John Snow did this in 1854: he mapped cholera "
              "deaths to the Broad Street pump and had the handle removed &mdash; epidemiology "
              "before anyone knew the germ."},
         ]},

        {"type": "content", "label": "Spread", "title": "R0: how contagious is it?",
         "blocks": [
             {"t": "term", "word": "Basic reproduction number (R0)",
              "def": "The average number of new infections one case causes in a fully susceptible "
              "population. R0 &gt; 1: the epidemic grows. R0 &lt; 1: it dies out."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Measles", "label": "very high R0 &mdash; among the most contagious "
                  "diseases known", "color": "red"},
                 {"num": "COVID-19", "label": "moderate R0, varying by variant", "color": "amber"},
                 {"num": "R0 &lt; 1", "label": "the target &mdash; each case infects fewer than "
                  "one other", "color": "green"}]},
             {"t": "hbox", "color": "cyan", "html": "R0 values are illustrative ranges &mdash; the "
              "key idea is the threshold at 1, not a precise figure."},
         ]},

        {"type": "content", "label": "Study Designs", "title": "How epidemiologists gather evidence",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Design", "What it does", "Strength"],
              "rows": [
                  ["Cross-sectional", "Snapshot of a population", "Fast, gives prevalence"],
                  ["Case-control", "Compare sick vs well, look back", "Good for rare disease"],
                  ["Cohort", "Follow exposed vs unexposed forward", "Gives incidence &amp; risk"],
                  ["Randomised trial", "Randomly assign the intervention", "Strongest for causation"]]},
             {"t": "hbox", "color": "amber", "html": "The design decides what you can claim. Only "
              "well-run trials and strong cohorts let you talk confidently about cause."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Measuring Population Health"},

        {"type": "content", "label": "Why Measure", "title": "You cannot manage what you do not measure",
         "blocks": [
             {"t": "body", "html": "To act on a population's health you must first count it: how "
              "many are born, how many die, of what, at what age. These vital statistics are the "
              "dashboard of public health."},
             {"t": "bullets", "sm": True, "items": [
                 "<strong>Mortality:</strong> who dies, when and from what",
                 "<strong>Morbidity:</strong> who is ill, and with what",
                 "<strong>Survival:</strong> how long people live and in what health"]},
         ]},

        {"type": "content", "label": "Mortality", "title": "The key mortality indicators",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Indicator", "Meaning", "Per"],
              "rows": [
                  ["IMR", "Infant deaths under 1 year", "per 1,000 live births"],
                  ["U5MR", "Deaths under 5 years", "per 1,000 live births"],
                  ["NMR", "Neonatal deaths (first 28 days)", "per 1,000 live births"],
                  ["MMR", "Maternal deaths", "per 100,000 live births"],
                  ["CDR", "Crude death rate (all ages)", "per 1,000 population"]]},
             {"t": "hbox", "color": "cyan", "html": "Note the denominators differ &mdash; IMR and "
              "U5MR per 1,000 births, MMR per 100,000 births because maternal death is rarer. "
              "Mixing the bases is a common error."},
         ]},

        {"type": "content", "label": "Trend", "title": "India's infant and under-five mortality have fallen sharply",
         "blocks": [
             {"t": "chart", "canvas": "phImrU5mrChart",
              "title": "India IMR &amp; U5MR decline (per 1,000 live births)",
              "source": "Trend per SRS; values illustrative/rounded",
              "type": "line",
              "data": {"labels": ["1990", "2000", "2010", "2015", "2020"],
                       "datasets": [
                           {"label": "IMR", "data": [80, 66, 44, 37, 28],
                            "borderColor": "#0EA5E9", "backgroundColor": "rgba(14,165,233,0.08)",
                            "fill": True, "tension": 0.3, "pointRadius": 4},
                           {"label": "U5MR", "data": [114, 90, 58, 43, 32],
                            "borderColor": "#EF4444", "backgroundColor": "rgba(239,68,68,0.06)",
                            "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ scales:{ y:{ title:{display:true,text:'Per 1,000 live births'}, min:0 } } }"}},
             {"t": "hbox", "color": "green", "html": "The downward trend is well established (SRS); "
              "plotted values are rounded/illustrative. India's child mortality has fallen "
              "substantially over three decades &mdash; a major public-health success still in progress."},
         ]},

        {"type": "content", "label": "Maternal Mortality", "title": "Maternal deaths: falling, but uneven",
         "blocks": [
             {"t": "chart", "canvas": "phMmrChart",
              "title": "India maternal mortality ratio (per 100,000 live births)",
              "source": "Trend per SRS Special Bulletins; values illustrative/rounded",
              "type": "bar",
              "data": {"labels": ["2000", "2007", "2012", "2017", "2020"],
                       "datasets": [{"label": "MMR", "data": [370, 254, 178, 122, 97],
                                     "backgroundColor": "#6366F1"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Deaths per 100,000 live births'}, min:0 } } }"}},
             {"t": "hbox", "color": "amber", "html": "Direction is solid (SRS); figures are rounded "
              "for teaching. India has cut MMR by more than half this century &mdash; yet state "
              "gaps remain wide, with southern states far ahead of several northern ones."},
         ]},

        {"type": "content", "label": "Morbidity", "title": "Illness, not just death",
         "blocks": [
             {"t": "body", "html": "Mortality misses the living burden &mdash; the disabled, the "
              "chronically ill, the depressed. <strong>Morbidity</strong> measures sickness and "
              "disability, increasingly the larger share of suffering as people live longer."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Incidence", "label": "new illness arising &mdash; risk of falling ill",
                  "color": "cyan"},
                 {"num": "Prevalence", "label": "all illness present &mdash; the burden to care for",
                  "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Survival", "title": "Life expectancy: a summary of a population's health",
         "blocks": [
             {"t": "body", "html": "<strong>Life expectancy at birth</strong> is the average years "
              "a newborn would live if current death rates held. It is a single, powerful summary "
              "of how healthy a population is."},
             {"t": "chart", "canvas": "phLifeExpChart",
              "title": "India life expectancy at birth (years)",
              "source": "Trend per SRS / UN; values illustrative/rounded",
              "type": "line",
              "data": {"labels": ["1950", "1970", "1990", "2010", "2020"],
                       "datasets": [{"label": "Life expectancy (years)",
                                     "data": [37, 49, 58, 67, 70],
                                     "borderColor": "#10B981",
                                     "backgroundColor": "rgba(16,185,129,0.08)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ title:{display:true,text:'Years'}, min:30, max:80 } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Trend per SRS / UN; figures rounded. India's "
              "life expectancy has roughly doubled since Independence to about 70 &mdash; a great "
              "gain of the public-health era, though still below the global frontier."},
         ]},

        {"type": "content", "label": "Leading Causes", "title": "What kills, and what disables, differ",
         "blocks": [
             {"t": "body", "html": "The biggest <em>killers</em> are not always the biggest "
              "<em>burdens</em>. A disease that disables for decades without killing can cost more "
              "healthy life than one that kills quickly &mdash; which is why we need a measure that "
              "captures both."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Counts deaths", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Mortality data ranks the fatal &mdash; heart "
                   "disease, stroke, respiratory illness &mdash; but is blind to suffering that "
                   "does not kill."}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Counts burden", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Burden data adds the disabling &mdash; mental "
                   "illness, anaemia, musculoskeletal pain &mdash; that mortality alone misses "
                   "entirely."}]}]},
         ]},

        {"type": "content", "label": "Quality of Life", "title": "The DALY: combining death and disability",
         "blocks": [
             {"t": "term", "word": "Disability-Adjusted Life Year (DALY)",
              "def": "One DALY is one lost year of healthy life. DALYs add Years of Life Lost to "
              "early death (YLL) and Years Lived with Disability (YLD) into one measure of total "
              "disease burden."},
             {"t": "body", "html": "DALYs let us compare very different problems &mdash; a fatal "
              "disease and a disabling-but-survivable one &mdash; on the same scale, to set "
              "priorities fairly."},
         ]},

        {"type": "content", "label": "Surveillance", "title": "The early-warning system",
         "blocks": [
             {"t": "term", "word": "Surveillance",
              "def": "The ongoing, systematic collection, analysis and use of health data to "
              "detect problems early and act &mdash; 'information for action'."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "India's systems", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "IDSP &mdash; integrated disease surveillance",
                      "HMIS &mdash; facility service data",
                      "Civil registration of births &amp; deaths"]}]}],
              "right": [{"t": "panel", "color": "amber", "title": "Why it matters", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Catch an outbreak in week one, not month "
                   "three. Surveillance is the difference between a contained cluster and an "
                   "epidemic."}]}]},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Communicable Disease &amp; Immunisation"},

        {"type": "content", "label": "The Chain", "title": "The chain of infection",
         "blocks": [
             {"t": "flow", "steps": [
                 "AGENT: the pathogen",
                 "RESERVOIR: where it lives",
                 "PORTAL OF EXIT: how it leaves",
                 "TRANSMISSION: how it travels",
                 "PORTAL OF ENTRY &rarr; SUSCEPTIBLE HOST"]},
             {"t": "hbox", "color": "green", "html": "Prevention = breaking one link. Sanitation "
              "breaks transmission; vaccines protect the host; isolation removes the reservoir."},
         ]},

        {"type": "content", "label": "Routes", "title": "How infections spread",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Route", "Example diseases", "Key barrier"],
              "rows": [
                  ["Airborne / droplet", "TB, measles, COVID-19", "Ventilation, masks, vaccines"],
                  ["Faecal&ndash;oral", "Cholera, typhoid, polio", "Safe water, sanitation"],
                  ["Vector-borne", "Malaria, dengue, kala-azar", "Nets, spraying, source control"],
                  ["Blood / sexual", "HIV, hepatitis B", "Safe blood, condoms, PrEP"],
                  ["Contact", "Scabies, trachoma", "Hygiene, treatment"]]},
         ]},

        {"type": "content", "label": "How Vaccines Work", "title": "Vaccines train immunity in advance",
         "blocks": [
             {"t": "body", "html": "A <strong>vaccine</strong> shows the immune system a harmless "
              "piece or weakened form of a pathogen, so the body learns to fight the real thing "
              "before ever meeting it &mdash; protection without the disease."},
             {"t": "hbox", "color": "cyan", "html": "Vaccination is among the most cost-effective "
              "of all health interventions and has saved more lives than almost any other measure "
              "in history (WHO)."},
         ]},

        {"type": "content", "label": "Herd Immunity", "title": "Herd immunity protects those who cannot be vaccinated",
         "blocks": [
             {"t": "term", "word": "Herd (population) immunity",
              "def": "When enough of a population is immune that the pathogen cannot find new "
              "hosts, transmission collapses &mdash; protecting even the unvaccinated."},
             {"t": "body", "html": "The <strong>threshold rises with R0</strong>: the more "
              "contagious the disease, the higher the share that must be immune. A highly "
              "contagious disease like measles needs a <em>very</em> high coverage to hold the line."},
             {"t": "hbox", "color": "red", "html": "This is why measles returns the moment coverage "
              "dips &mdash; its high R0 demands one of the highest immunity thresholds of any disease."},
         ]},

        {"type": "content", "label": "India's Programme", "title": "The Universal Immunisation Programme (UIP)",
         "blocks": [
             {"t": "body", "html": "India's <strong>UIP</strong> is one of the largest public-health "
              "programmes in the world, providing free vaccines against a dozen-plus diseases. "
              "<strong>Mission Indradhanush</strong> targets the children it misses."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "12+", "label": "diseases covered free under the UIP", "color": "green",
                  "source": "MoHFW"},
                 {"num": "~26 million", "label": "infants targeted each year", "color": "cyan",
                  "source": "MoHFW (illustrative)"},
                 {"num": "Polio-free", "label": "India certified polio-free in 2014 (WHO)",
                  "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Coverage", "title": "Full immunisation coverage has improved",
         "blocks": [
             {"t": "chart", "canvas": "phImmCoverageChart",
              "title": "Children 12&ndash;23 months fully immunised, India (%)",
              "source": "NFHS rounds; values illustrative/rounded",
              "type": "bar",
              "data": {"labels": ["NFHS-3 (2005-06)", "NFHS-4 (2015-16)", "NFHS-5 (2019-21)"],
                       "datasets": [{"label": "Fully immunised (%)", "data": [44, 62, 76],
                                     "backgroundColor": ["#F59E0B", "#0EA5E9", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% of children'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Trend per NFHS; figures rounded for teaching. "
              "Coverage has risen markedly &mdash; but the last mile, the unreached child, is the "
              "hardest and where herd immunity is won or lost."},
         ]},

        {"type": "content", "label": "The Big Three", "title": "TB, HIV and malaria in South Asia",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Disease", "Burden note", "India's response"],
              "rows": [
                  ["Tuberculosis", "India carries a large share of global TB", "NTEP; free diagnosis &amp; treatment; elimination goal"],
                  ["HIV/AIDS", "Concentrated epidemic in key populations", "NACO; free ART; targeted prevention"],
                  ["Malaria", "Falling, but endemic pockets remain", "NVBDCP; nets, spraying, prompt treatment"]]},
             {"t": "hbox", "color": "cyan", "html": "All three are <em>treatable and preventable</em> "
              "&mdash; the challenge is reach, adherence and stigma, not the absence of tools."},
         ]},

        {"type": "content", "label": "Stewardship", "title": "Antimicrobial resistance: a slow-motion crisis",
         "blocks": [
             {"t": "body", "html": "Overuse of antibiotics in people, animals and farming is "
              "breeding resistant bacteria. <strong>Antimicrobial resistance (AMR)</strong> "
              "threatens to make routine infections deadly again."},
             {"t": "hbox", "color": "red", "html": "Public-health responses: prescribe only when "
              "needed, complete courses, control infection in hospitals, and curb antibiotics in "
              "livestock. AMR is everyone's problem."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Non-Communicable Diseases"},

        {"type": "content", "label": "The Shift", "title": "The epidemiological transition",
         "blocks": [
             {"t": "term", "word": "Epidemiological transition",
              "def": "The long-run shift in a population's main health burden from infectious "
              "diseases and child deaths toward chronic, non-communicable diseases of later life."},
             {"t": "body", "html": "As countries develop, the leading killers change from "
              "infections and malnutrition to <strong>non-communicable diseases (NCDs)</strong> "
              "&mdash; heart disease, diabetes, cancer."},
         ]},

        {"type": "content", "label": "The Double Burden", "title": "South Asia faces both at once",
         "blocks": [
             {"t": "chart", "canvas": "phCdNcdChart",
              "title": "Illustrative shift in share of deaths: communicable vs NCD",
              "source": "Illustrative of a well-established transition (WHO/GBD)",
              "type": "line",
              "data": {"labels": ["1990", "2000", "2010", "2020"],
                       "datasets": [
                           {"label": "Communicable, maternal, nutritional (%)",
                            "data": [50, 42, 32, 26], "borderColor": "#0EA5E9",
                            "tension": 0.3, "pointRadius": 4, "fill": False},
                           {"label": "Non-communicable diseases (%)",
                            "data": [40, 48, 58, 64], "borderColor": "#EF4444",
                            "tension": 0.3, "pointRadius": 4, "fill": False}]},
              "options": {"__js__": "{ scales:{ y:{ min:0, max:80, title:{display:true,text:'% of all deaths'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Shares are illustrative of the documented "
              "trend. South Asia carries a <strong>double burden</strong>: NCDs rise before "
              "infectious disease is conquered &mdash; straining systems built for the old battle."},
         ]},

        {"type": "content", "label": "Nutrition Transition", "title": "Diets and bodies are changing too",
         "blocks": [
             {"t": "body", "html": "The <strong>nutrition transition</strong> &mdash; from "
              "traditional diets to processed food, sugar, salt and fat, with less physical "
              "activity &mdash; drives obesity and diabetes even as undernutrition persists."},
             {"t": "hbox", "color": "red", "html": "Many South Asian households now hold both: a "
              "stunted child and an overweight adult under one roof. This is the "
              "<em>double burden of malnutrition</em>."},
         ]},

        {"type": "content", "label": "The Main NCDs", "title": "Four diseases, shared roots",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["NCD", "Note for South Asia"],
              "rows": [
                  ["Cardiovascular disease", "The leading cause of death; strikes at younger ages here"],
                  ["Diabetes", "India has one of the world's largest diabetic populations"],
                  ["Cancer", "Tobacco-linked oral cancer is especially common"],
                  ["Chronic respiratory disease", "Driven by air pollution &amp; biomass smoke"]]},
             {"t": "hbox", "color": "cyan", "html": "Different diseases, but they share a small set "
              "of modifiable risk factors &mdash; which is what makes prevention possible."},
         ]},

        {"type": "content", "label": "Risk Factors", "title": "A few behaviours drive most NCDs",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Tobacco</strong> &mdash; smoked and smokeless (gutka, khaini)",
                 "<strong>Unhealthy diet</strong> &mdash; salt, sugar, trans-fat",
                 "<strong>Physical inactivity</strong>",
                 "<strong>Harmful alcohol use</strong>",
                 "<strong>Air pollution</strong> &mdash; ambient and household"]},
             {"t": "hbox", "color": "green", "html": "These are <em>modifiable</em>. Tax, regulate, "
              "label, build walkable cities and clean the air &mdash; population-level prevention "
              "beats treating millions one by one."},
         ]},

        {"type": "content", "label": "Mental Health", "title": "Mental health is public health",
         "blocks": [
             {"t": "body", "html": "Depression, anxiety, substance use and suicide are a vast, "
              "under-counted share of the disease burden &mdash; yet mental health receives a tiny "
              "fraction of health spending across South Asia."},
             {"t": "hbox", "color": "amber", "html": "Stigma keeps people silent and services thin. "
              "India's <strong>National Mental Health Programme</strong> and the 2017 Mental "
              "Healthcare Act aim to widen access and protect rights."},
         ]},

        {"type": "content", "label": "Injuries", "title": "Don't forget injuries",
         "blocks": [
             {"t": "body", "html": "Road-traffic crashes, drowning, burns, falls and self-harm kill "
              "and disable enormous numbers &mdash; disproportionately the young and "
              "working-age &mdash; yet rarely feature in 'disease' debates."},
             {"t": "hbox", "color": "cyan", "html": "Helmets, seat-belts, speed limits, safer roads "
              "and licensing are classic public-health wins &mdash; engineering and law, not "
              "medicine, save these lives."},
         ]},

        {"type": "content", "label": "Best Buys", "title": "WHO 'best buys' for NCDs",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Raise tobacco and alcohol taxes",
                 "Ban tobacco advertising; plain packaging; smoke-free spaces",
                 "Cut salt in the food supply; eliminate industrial trans-fat",
                 "Screen and treat high blood pressure in primary care",
                 "Vaccinate against HPV and hepatitis B to prevent cancers"]},
             {"t": "hbox", "color": "cyan", "html": "These are cost-effective, population-wide and "
              "mostly regulatory &mdash; the state acting upstream, not the clinic acting downstream."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Maternal, Newborn, Child Health &amp; Nutrition"},

        {"type": "content", "label": "The Continuum", "title": "The continuum of care",
         "blocks": [
             {"t": "body", "html": "Maternal and child health is not a series of one-off events but "
              "a <strong>continuum</strong> &mdash; care must connect across time and across the "
              "places it is given, or children fall through the gaps."},
             {"t": "flow", "steps": [
                 "Adolescence &amp; pre-pregnancy",
                 "Pregnancy (antenatal care)",
                 "Childbirth (skilled birth attendance)",
                 "Postnatal &amp; newborn care",
                 "Infancy &amp; early childhood"]},
         ]},

        {"type": "content", "label": "Why Mothers Die", "title": "Most maternal deaths are preventable",
         "blocks": [
             {"t": "body", "html": "The major direct causes &mdash; haemorrhage, infection (sepsis), "
              "high blood pressure (eclampsia), obstructed labour and unsafe abortion &mdash; are "
              "almost all <strong>preventable or treatable</strong> with timely, skilled care."},
             {"t": "hbox", "color": "red", "html": "The 'three delays' kill: delay in deciding to "
              "seek care, delay in reaching a facility, and delay in receiving care once there. "
              "Public health attacks all three."},
         ]},

        {"type": "content", "label": "What Works", "title": "The proven package for safe motherhood",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Antenatal care &mdash; check-ups, iron-folic acid, tetanus, danger-sign education",
                 "Skilled attendance at birth, with referral for complications",
                 "Emergency obstetric and newborn care within reach",
                 "Postnatal visits for mother and baby in the critical first days",
                 "Family planning to space and limit pregnancies"]},
             {"t": "hbox", "color": "cyan", "html": "India's institutional-delivery rate rose "
              "sharply after schemes like JSY paid for facility births &mdash; a major driver of "
              "falling maternal mortality (NFHS / SRS)."},
         ]},

        {"type": "content", "label": "Newborns", "title": "The newborn period is the most dangerous",
         "blocks": [
             {"t": "body", "html": "A large share of all under-five deaths happen in the first "
              "<strong>28 days</strong> of life &mdash; the neonatal period. Saving newborns is "
              "now the frontier of child survival."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Warmth", "label": "kangaroo mother care for low-birth-weight babies",
                  "color": "amber"},
                 {"num": "Early breastfeeding", "label": "within the first hour", "color": "green"},
                 {"num": "Cord &amp; infection care", "label": "clean cord, prompt treatment of sepsis",
                  "color": "cyan"}]},
         ]},

        {"type": "content", "label": "Child Nutrition", "title": "Stunting, wasting and underweight",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Indicator", "What it measures", "Signals"],
              "rows": [
                  ["Stunting", "Low height-for-age", "Chronic, long-term undernutrition"],
                  ["Wasting", "Low weight-for-height", "Acute, recent malnutrition (dangerous)"],
                  ["Underweight", "Low weight-for-age", "A mix of both"],
                  ["Anaemia", "Low haemoglobin", "Iron deficiency; very common here"]]},
             {"t": "hbox", "color": "red", "html": "South Asia carries one of the world's heaviest "
              "burdens of child stunting and anaemia (NFHS-5). Stunting is largely irreversible "
              "after age two &mdash; which is why timing is everything."},
         ]},

        {"type": "content", "label": "The Window", "title": "The first 1,000 days",
         "blocks": [
             {"t": "body", "html": "From conception to a child's second birthday &mdash; the "
              "<strong>first 1,000 days</strong> &mdash; nutrition and care set the trajectory for "
              "lifelong health, brain development and earnings. Damage here is hard to undo."},
             {"t": "flow", "steps": [
                 "Pregnancy: maternal nutrition &amp; weight gain",
                 "0&ndash;6 months: exclusive breastfeeding",
                 "6&ndash;24 months: safe complementary feeding",
                 "Throughout: hygiene, healthcare, micronutrients"]},
         ]},

        {"type": "content", "label": "India's Platforms", "title": "ICDS, anganwadis and POSHAN",
         "blocks": [
             {"t": "body", "html": "India delivers child nutrition through the world's largest such "
              "programme: <strong>Integrated Child Development Services (ICDS)</strong> and its "
              "network of <strong>anganwadi centres</strong>, now under "
              "<strong>POSHAN Abhiyaan</strong>."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Supplementary nutrition for children and pregnant/lactating women",
                 "Growth monitoring and counselling",
                 "Immunisation, health check-ups and referral",
                 "Pre-school education for 3&ndash;6 year-olds"]},
         ]},

        {"type": "content", "label": "Beyond Food", "title": "Nutrition is more than food",
         "blocks": [
             {"t": "body", "html": "A child can eat enough yet stay stunted if repeated infection "
              "drains nutrients. <strong>WASH</strong> &mdash; water, sanitation and hygiene "
              "&mdash; is as much a nutrition intervention as feeding."},
             {"t": "hbox", "color": "green", "html": "Sanitation, clean water, breastfeeding, "
              "women's education and birth spacing all shape nutrition. Food alone never fixes "
              "stunting."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Health Systems"},

        {"type": "content", "label": "Definition", "title": "What is a health system?",
         "blocks": [
             {"t": "term", "word": "Health system",
              "def": "All the organisations, people and actions whose primary purpose is to "
              "promote, restore or maintain health &mdash; not just hospitals, but financing, "
              "workforce, supplies, information and governance."},
             {"t": "body", "html": "A health system aims to improve health, respond fairly to "
              "people, and protect them from financial hardship when they fall ill."},
         ]},

        {"type": "content", "label": "The Framework", "title": "The WHO six building blocks",
         "compact": True,
         "blocks": [
             {"t": "raw", "html": (
                 '<svg viewBox="0 0 760 200" width="100%" style="max-height:220px">'
                 '<g font-family="inherit" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">'
                 '<rect x="20" y="40" width="115" height="110" rx="8" fill="rgba(14,165,233,0.22)" stroke="#0EA5E9"/>'
                 '<text x="77" y="90">Service</text><text x="77" y="108">delivery</text>'
                 '<rect x="145" y="40" width="115" height="110" rx="8" fill="rgba(16,185,129,0.22)" stroke="#10B981"/>'
                 '<text x="202" y="90">Health</text><text x="202" y="108">workforce</text>'
                 '<rect x="270" y="40" width="115" height="110" rx="8" fill="rgba(245,158,11,0.22)" stroke="#F59E0B"/>'
                 '<text x="327" y="99">Information</text>'
                 '<rect x="395" y="40" width="115" height="110" rx="8" fill="rgba(99,102,241,0.22)" stroke="#6366F1"/>'
                 '<text x="452" y="84">Medical</text><text x="452" y="102">products &amp;</text><text x="452" y="120">vaccines</text>'
                 '<rect x="520" y="40" width="115" height="110" rx="8" fill="rgba(14,165,233,0.22)" stroke="#0EA5E9"/>'
                 '<text x="577" y="99">Financing</text>'
                 '<rect x="645" y="40" width="100" height="110" rx="8" fill="rgba(239,68,68,0.22)" stroke="#EF4444"/>'
                 '<text x="695" y="84">Leadership</text><text x="695" y="102">&amp;</text><text x="695" y="120">governance</text>'
                 '<text x="380" y="22" font-size="14">The Six Building Blocks of a Health System (WHO)</text>'
                 '</g></svg>')},
             {"t": "hbox", "color": "cyan", "html": "Weaken any block &mdash; no staff, no medicines, "
              "no data, no money, no leadership &mdash; and the whole system falters. They are "
              "interdependent."},
         ]},

        {"type": "content", "label": "Workforce", "title": "There is no health without a health workforce",
         "blocks": [
             {"t": "body", "html": "Doctors, nurses, midwives, pharmacists and community health "
              "workers are the system's beating heart. Many countries, including parts of South "
              "Asia, fall short of WHO's benchmark for health workers per population."},
             {"t": "hbox", "color": "amber", "html": "Shortages cluster exactly where need is "
              "greatest &mdash; rural, remote and poor areas. Distribution, not just numbers, is "
              "the equity problem."},
         ]},

        {"type": "content", "label": "Financing", "title": "Three ways to pay for health",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Mechanism", "How it works", "Equity"],
              "rows": [
                  ["Out-of-pocket", "Patient pays at the point of care", "Worst &mdash; sickness = debt"],
                  ["Tax-funded", "Government funds from general taxes", "Strong if well funded"],
                  ["Insurance", "Pooled premiums (social or private)", "Good if it covers the poor"]]},
             {"t": "hbox", "color": "red", "html": "The more health is paid <strong>out-of-pocket</strong> "
              "at the point of use, the more illness pushes families into poverty. Pooling and "
              "prepayment are the route out."},
         ]},

        {"type": "content", "label": "The Goal", "title": "Universal Health Coverage (UHC)",
         "blocks": [
             {"t": "term", "word": "Universal Health Coverage (UHC)",
              "def": "All people get the quality health services they need &mdash; promotion, "
              "prevention, treatment, rehabilitation &mdash; without suffering financial hardship "
              "to pay for them."},
             {"t": "body", "html": "UHC is a target of the Sustainable Development Goals (SDG 3.8). "
              "It has three dimensions: <strong>who</strong> is covered, <strong>which services</strong>, "
              "and <strong>what share of cost</strong> is protected."},
         ]},

        {"type": "content", "label": "The Cube", "title": "Three dimensions of moving toward UHC",
         "blocks": [
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Population", "label": "Who is covered? Extend to everyone", "color": "cyan"},
                 {"num": "Services", "label": "What is covered? Add needed services", "color": "green"},
                 {"num": "Costs", "label": "What share is covered? Cut out-of-pocket", "color": "amber"}]},
             {"t": "hbox", "color": "indigo", "html": "No country covers everything for everyone "
              "free; UHC is a direction of travel, expanding along all three axes as resources grow."},
         ]},

        {"type": "content", "label": "Foundations", "title": "Primary Health Care: Alma-Ata, 1978",
         "blocks": [
             {"t": "quote",
              "text": "Health for All.",
              "attr": "&mdash; the rallying cry of the Alma-Ata Declaration, 1978"},
             {"t": "body", "html": "The <strong>Declaration of Alma-Ata (1978)</strong> made "
              "<strong>Primary Health Care (PHC)</strong> the foundation of health systems: "
              "essential care, close to where people live, with community participation and "
              "across sectors."},
         ]},

        {"type": "content", "label": "Renewal", "title": "Astana 2018 renews the PHC promise",
         "blocks": [
             {"t": "body", "html": "Forty years on, the <strong>Astana Declaration (2018)</strong> "
              "re-committed the world to Primary Health Care as the most efficient route to UHC "
              "&mdash; updated for NCDs, ageing, technology and empowered communities."},
             {"t": "hbox", "color": "green", "html": "The thread from Alma-Ata to Astana to "
              "India's Health &amp; Wellness Centres is the same: strong, comprehensive primary "
              "care is the backbone of any health system that works."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "India's Health System"},

        {"type": "content", "label": "The Structure", "title": "A federal, mixed health system",
         "blocks": [
             {"t": "body", "html": "Health is mainly a <strong>state subject</strong> in India: "
              "states run most services, the centre sets policy and co-funds national programmes. "
              "A vast <strong>private sector</strong> delivers much of the actual care."},
             {"t": "hbox", "color": "amber", "html": "The result is enormous variation between "
              "states &mdash; Kerala and Tamil Nadu perform near middle-income levels while several "
              "northern states lag far behind."},
         ]},

        {"type": "content", "label": "Three Tiers", "title": "The rural public health structure",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Tier", "Facility", "Roughly serves"],
              "rows": [
                  ["First contact", "Sub-Centre (SC) / HWC", "~3,000&ndash;5,000 people"],
                  ["Primary", "Primary Health Centre (PHC)", "~20,000&ndash;30,000 people"],
                  ["First referral", "Community Health Centre (CHC)", "~80,000&ndash;120,000 people"],
                  ["Higher", "District hospital &amp; above", "The district"]]},
             {"t": "hbox", "color": "cyan", "html": "Population norms are indicative and differ for "
              "tribal and hilly areas. The pyramid routes routine care low and complex care up."},
         ]},

        {"type": "content", "label": "The Mission", "title": "The National Health Mission (NHM)",
         "blocks": [
             {"t": "body", "html": "Launched as the National Rural Health Mission in 2005 and later "
              "broadened, the <strong>NHM</strong> is the main vehicle for strengthening public "
              "health &mdash; infrastructure, staff, programmes and community workers."},
             {"t": "bullets", "sm": True, "color": "green", "items": [
                 "Built and upgraded thousands of rural facilities",
                 "Created the ASHA community health worker cadre",
                 "Funded the schemes behind falling IMR and MMR"]},
         ]},

        {"type": "content", "label": "ASHAs", "title": "ASHAs: the bridge to the community",
         "blocks": [
             {"t": "term", "word": "ASHA (Accredited Social Health Activist)",
              "def": "A trained local woman who links her community to the health system &mdash; "
              "promoting institutional births, immunisation, ante/postnatal care and more, paid "
              "largely through performance incentives."},
             {"t": "hbox", "color": "cyan", "html": "Around a million ASHAs form one of the "
              "world's largest community health workforces &mdash; central to India's gains in "
              "maternal and child health. The WHO recognised them with a Global Health Leaders "
              "award in 2022."},
         ]},

        {"type": "content", "label": "The New Push", "title": "Ayushman Bharat: two pillars",
         "blocks": [
             {"t": "body", "html": "Launched in <strong>2018</strong>, <strong>Ayushman Bharat</strong> "
              "is India's flagship move toward UHC, built on two complementary pillars."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Pillar 1: HWCs", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>Health &amp; Wellness Centres</strong> "
                   "upgrade sub-centres and PHCs to deliver <em>comprehensive</em> primary care "
                   "&mdash; including NCDs and mental health &mdash; free, near home."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Pillar 2: PM-JAY", "blocks": [
                  {"t": "body", "cls": "sm", "html": "<strong>PM-JAY</strong> gives poor and "
                   "vulnerable families a large annual cover for hospital (secondary &amp; "
                   "tertiary) care &mdash; one of the world's biggest health-insurance schemes."}]}]},
         ]},

        {"type": "content", "label": "Two Halves", "title": "Primary care plus financial protection",
         "blocks": [
             {"t": "flow", "steps": [
                 "HWCs: keep people healthy &amp; catch disease early (prevention)",
                 "Strong primary care reduces need for costly hospital care",
                 "PM-JAY: shield families from catastrophic hospital bills",
                 "Together: move toward Universal Health Coverage"]},
             {"t": "hbox", "color": "cyan", "html": "The design mirrors the global lesson: invest "
              "in primary care <em>and</em> protect against the big bills. One without the other "
              "leaves people exposed."},
         ]},

        {"type": "content", "label": "The Core Problem", "title": "Out-of-pocket spending impoverishes families",
         "blocks": [
             {"t": "chart", "canvas": "phOopChart",
              "title": "Out-of-pocket as a share of total health spending (illustrative)",
              "source": "Illustrative, patterned on National Health Accounts trend",
              "type": "bar",
              "data": {"labels": ["India (high OOP)", "Lower-OOP comparator", "Strong-UHC system"],
                       "datasets": [{"label": "OOP share of health spending (%)",
                                     "data": [55, 35, 15],
                                     "backgroundColor": ["#EF4444", "#F59E0B", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:70, title:{display:true,text:'% out-of-pocket'} } } }"}},
             {"t": "hbox", "color": "red", "html": "Figures are illustrative. India's out-of-pocket "
              "share, though falling, has long been high &mdash; medical bills push millions into "
              "poverty each year (National Health Accounts). Cutting it is the central UHC challenge."},
         ]},

        {"type": "content", "label": "Public Spending", "title": "India spends comparatively little public money on health",
         "blocks": [
             {"t": "body", "html": "Government health spending in India has long hovered around "
              "1&ndash;2% of GDP &mdash; low by international standards. The National Health Policy "
              "2017 set a goal of raising it toward 2.5% of GDP."},
             {"t": "hbox", "color": "amber", "html": "Low public spending is the root of high "
              "out-of-pocket costs. More pooled public money is the surest way to financial "
              "protection &mdash; the unfinished agenda of Indian health reform."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Health Equity &amp; Global Health"},

        {"type": "content", "label": "The Inverse Law", "title": "The inverse care law",
         "blocks": [
             {"t": "quote",
              "text": "The availability of good medical care tends to vary inversely with the "
              "need of the population served.",
              "attr": "&mdash; Julian Tudor Hart, 1971"},
             {"t": "body", "html": "Those who need care most &mdash; the poor, rural and "
              "marginalised &mdash; tend to get the least and worst of it, while the well-off get "
              "the most. Markets, left alone, deepen this."},
         ]},

        {"type": "content", "label": "Who Is Left Behind", "title": "Equity means seeing the gaps",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Caste &amp; tribe:</strong> Dalit &amp; Adivasi communities face worse outcomes",
                 "<strong>Gender:</strong> anaemia, son preference, neglected women's health",
                 "<strong>Geography:</strong> remote, hilly, conflict-affected and urban-slum areas",
                 "<strong>Disability &amp; age:</strong> services rarely designed for them",
                 "<strong>Income:</strong> the poorest carry the heaviest disease burden"]},
             {"t": "hbox", "color": "amber", "html": "Always <strong>disaggregate</strong>: a good "
              "national average can hide a failing programme for those who matter most."},
         ]},

        {"type": "content", "label": "Pandemics", "title": "Pandemics and the International Health Regulations",
         "blocks": [
             {"t": "body", "html": "Disease respects no border. The <strong>International Health "
              "Regulations (IHR, 2005)</strong> legally bind countries to detect, report and "
              "respond to public-health emergencies of international concern."},
             {"t": "hbox", "color": "red", "html": "COVID-19 exposed the cost of weak preparedness: "
              "the strength of every country's basic public-health system &mdash; surveillance, "
              "labs, workforce &mdash; is global security, not just local welfare."},
         ]},

        {"type": "content", "label": "One Health", "title": "One Health: people, animals, environment",
         "blocks": [
             {"t": "term", "word": "One Health",
              "def": "An approach recognising that human, animal and environmental health are "
              "linked &mdash; many new diseases jump from animals to people (zoonoses), so we must "
              "act across all three."},
             {"t": "body", "html": "Most recent emerging epidemics &mdash; avian flu, Nipah, "
              "COVID-19 &mdash; are zoonotic. Antimicrobial resistance, too, spans humans, "
              "livestock and the environment."},
         ]},

        {"type": "content", "label": "Climate", "title": "Climate change is a health crisis",
         "blocks": [
             {"t": "body", "html": "The WHO calls climate change the greatest health threat of the "
              "century. It is a public-health issue, not only an environmental one."},
             {"t": "bullets", "sm": True, "color": "red", "items": [
                 "Heatwaves &mdash; deadly, especially for outdoor workers and the elderly",
                 "Shifting ranges of malaria, dengue and other vector-borne disease",
                 "Floods and droughts &mdash; injury, displacement, food insecurity",
                 "Air pollution &mdash; respiratory and heart disease"]},
         ]},

        {"type": "content", "label": "Co-Benefits", "title": "Good climate policy is good health policy",
         "blocks": [
             {"t": "body", "html": "The link cuts both ways. Cleaner air, active transport, less "
              "red meat and greener cities cut emissions <em>and</em> prevent disease &mdash; the "
              "<strong>health co-benefits</strong> of climate action."},
             {"t": "hbox", "color": "green", "html": "Framing climate action around immediate "
              "health gains &mdash; cleaner air today, not only a cooler planet tomorrow &mdash; "
              "makes the case more compelling and more local."},
         ]},

        {"type": "content", "label": "Global Solidarity", "title": "Global health is shared responsibility",
         "blocks": [
             {"t": "body", "html": "From vaccine access to disease eradication, health beyond "
              "borders needs cooperation: the WHO, Gavi, the Global Fund and the SDGs all rest on "
              "the idea that no one is safe until everyone is."},
             {"t": "hbox", "color": "cyan", "html": "Smallpox &mdash; the only human disease ever "
              "eradicated (1980) &mdash; proves what coordinated global public health can achieve."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "Prevention in Practice &amp; Further Reading"},

        {"type": "content", "label": "Levels of Prevention", "title": "Four levels of prevention",
         "blocks": [
             {"t": "chart", "canvas": "phPreventionChart",
              "title": "Where each level acts along the course of disease",
              "source": "Standard public-health framework (Leavell &amp; Clark)",
              "type": "bar",
              "data": {"labels": ["Primordial", "Primary", "Secondary", "Tertiary"],
                       "datasets": [{"label": "Acts at this stage",
                                     "data": [1, 2, 3, 4],
                                     "backgroundColor": ["#10B981", "#0EA5E9", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ indexAxis:'y', plugins:{legend:{display:false}, tooltip:{enabled:false}}, scales:{ x:{ display:false }, y:{ title:{display:true,text:'Earlier  \\u2192  later in disease course'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "The earlier you act, the more people you "
              "protect &mdash; and usually the cheaper it is. Primordial and primary prevention "
              "are the heart of public health."},
         ]},

        {"type": "content", "label": "The Four Levels", "title": "What each level means",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Level", "Acts on", "Example"],
              "rows": [
                  ["Primordial", "Risk factors before they arise", "Clean air policy; healthy food environment"],
                  ["Primary", "Stop disease before it starts", "Immunisation, sanitation, tobacco tax"],
                  ["Secondary", "Catch disease early", "Screening for BP, diabetes, cervical cancer"],
                  ["Tertiary", "Limit harm once disease exists", "Rehabilitation, managing complications"]]},
         ]},

        {"type": "content", "label": "Two Strategies", "title": "High-risk vs population approach",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "High-risk", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Find and treat the few at greatest risk "
                   "&mdash; e.g. those with very high blood pressure. Efficient per person, but "
                   "misses the many at modest risk."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Population", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Shift the whole distribution &mdash; e.g. "
                   "less salt for everyone. Each person gains little, but the population gains a "
                   "lot. Geoffrey Rose's insight."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Rose's 'prevention paradox': a measure that "
              "brings large benefit to a population often offers little to each individual &mdash; "
              "which is why population strategies can be a hard sell."},
         ]},

        {"type": "content", "label": "Health Promotion", "title": "Health promotion: more than telling people what to do",
         "blocks": [
             {"t": "term", "word": "Health promotion",
              "def": "The process of enabling people to increase control over, and improve, their "
              "health &mdash; combining education, healthy public policy, supportive environments "
              "and community action (Ottawa Charter, 1986)."},
             {"t": "hbox", "color": "red", "html": "Lecturing people to 'eat better' fails if the "
              "shop sells only junk and the wage buys only the cheapest calories. Change the "
              "environment, not just the message."},
         ]},

        {"type": "content", "label": "Communication", "title": "Behaviour change and risk communication",
         "blocks": [
             {"t": "bullets", "items": [
                 "Make the healthy choice the <strong>easy</strong> choice (defaults, access)",
                 "Use <strong>trusted local messengers</strong> &mdash; ASHAs, teachers, faith leaders",
                 "Be honest about uncertainty; rumours fill information vacuums",
                 "Tackle <strong>stigma</strong> &mdash; for HIV, TB, leprosy, mental illness"]},
             {"t": "hbox", "color": "amber", "html": "COVID-19 showed that clear, trusted, two-way "
              "communication is as vital as any vaccine. Misinformation is a public-health hazard."},
         ]},

        {"type": "content", "label": "Keep Learning", "title": "A short reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>The Health of Nations</em> &mdash; on the social roots of health",
                 "<em>The Status Syndrome</em> &mdash; Michael Marmot (the social gradient)",
                 "<em>An Uncertain Glory: India &amp; its Contradictions</em> &mdash; Dr&egrave;ze &amp; Sen",
                 "WHO &amp; Lancet reports on UHC, NCDs and climate &amp; health",
                 "India's NFHS, SRS and National Health Accounts &mdash; the core data"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Data Literacy</strong>, <strong>Maternal &amp; Child Health</strong> and "
              "<strong>Social Determinants</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Public health acts on populations</strong>, mostly upstream and before illness",
                 "<strong>Most health is made outside the clinic</strong> &mdash; in the social determinants",
                 "<strong>Incidence is new cases; prevalence is all cases</strong> &mdash; never mix them",
                 "<strong>Prevention and primary care</strong> are the backbone of UHC",
                 "<strong>Cut out-of-pocket spending</strong> &mdash; no one should be ruined by illness"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Public Health 101 &middot; Complete",
         "headline": "Build the fence<br>at the top of the cliff.",
         "byline": "Treating the sick will always matter &mdash; but the greatest gains come from "
                   "preventing illness and acting on the conditions that make people ill. Explore "
                   "the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
