# -*- coding: utf-8 -*-
"""
Sexual Health 101 — ImpactMojo 101 Series (native deck spec)
Rights-based, medically accurate SRHR foundations for South Asian practitioners.
Build: python3 scripts/deck-builder/build.py srhr_basics
"""

DECK = {
    "slug": "SRHR-basics",
    "title": "Sexual Health 101",
    "description": ("Sexual Health 101 — a free, rights-based foundational course on sexual and "
                    "reproductive health and rights (SRHR) for development and health practitioners "
                    "in South Asia: from the WHO definition and the ICPD framework to contraception, "
                    "maternal health, safe abortion, STIs and HIV, comprehensive sexuality education, "
                    "consent and youth-friendly services. ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Sexual<br>Health<br>101",
         "sub": "Sexual &amp; Reproductive Health and Rights &mdash; a Rights-Based, "
                "Non-Judgemental Foundation for Development &amp; Health Practitioners in South Asia",
         "tags": ["Rights-Based", "Medically Accurate", "South Asia Focus", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What SRHR Means"},
             {"name": "The Rights Framework"},
             {"name": "Bodies &amp; Puberty"},
             {"name": "Contraception &amp; Family Planning"},
             {"name": "Pregnancy &amp; Maternal Health"},
             {"name": "Safe Abortion &amp; the Law"},
             {"name": "STIs &amp; HIV"},
             {"name": "Comprehensive Sexuality Education"},
             {"name": "Gender, Consent &amp; GBV"},
             {"name": "Adolescents &amp; Access"},
             {"name": "SRHR in South Asia &amp; Practice"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What SRHR Means"},

        {"type": "content", "label": "Starting Point", "title": "Sexual health is health, not just the absence of disease",
         "blocks": [
             {"t": "body", "html": "Sexual and reproductive health is part of being well &mdash; "
              "not merely the absence of infection or unwanted pregnancy. The World Health "
              "Organization frames it as a state of <strong>physical, emotional, mental and social "
              "well-being</strong> in relation to sexuality."},
             {"t": "term", "word": "Sexual health (WHO)",
              "def": "A state of physical, emotional, mental and social well-being in relation to "
              "sexuality; not merely the absence of disease, dysfunction or infirmity. It requires "
              "a positive and respectful approach to sexuality and sexual relationships."},
             {"t": "hbox", "color": "cyan", "html": "This is a practitioner's starting point: SRHR "
              "is about dignity and well-being, approached without shame or judgement."},
         ]},

        {"type": "content", "label": "Four Letters", "title": "Unpacking S, R, H and R",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Sexual", "label": "Sexuality, pleasure, relationships, identity &mdash; "
                  "across the whole life course", "color": "cyan"},
                 {"num": "Reproductive", "label": "Fertility, pregnancy, childbirth and the ability "
                  "to decide whether and when to have children", "color": "green"},
                 {"num": "Health", "label": "Well-being and access to information, services and care",
                  "color": "indigo"},
                 {"num": "Rights", "label": "Entitlements rooted in human rights &mdash; autonomy, "
                  "equality, non-discrimination", "color": "amber"}]},
         ]},

        {"type": "content", "label": "Whole Life", "title": "SRHR spans the entire life course",
         "blocks": [
             {"t": "flow", "steps": [
                 "CHILDHOOD: age-appropriate body knowledge &amp; safety",
                 "ADOLESCENCE: puberty, consent, contraception, CSE",
                 "ADULTHOOD: family planning, pregnancy, STIs, fertility",
                 "LATER LIFE: menopause, ageing, continued sexual well-being"]},
             {"t": "hbox", "color": "green", "html": "SRHR is not only about young women of "
              "reproductive age. It concerns men, adolescents, older people, and people of every "
              "gender and sexuality."},
         ]},

        {"type": "content", "label": "Inclusion", "title": "SRHR is for everyone",
         "blocks": [
             {"t": "body", "html": "A rights-based approach is explicitly inclusive. SRHR belongs "
              "to people of all genders and sexual orientations, to unmarried as well as married "
              "people, and to persons with disabilities."},
             {"t": "bullets", "color": "indigo", "items": [
                 "<strong>LGBTQ+ people</strong> have the same rights to information and care",
                 "<strong>Persons with disabilities</strong> are sexual beings with equal rights, "
                 "too often denied autonomy",
                 "<strong>Unmarried people</strong>, including adolescents, need services and respect",
                 "<strong>Men and boys</strong> are partners in SRHR, not bystanders"]},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "Why SRHR sits at the centre of development",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Health &amp; survival", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Maternal &amp; newborn survival",
                      "Preventing and treating STIs and HIV",
                      "Preventing unsafe abortion"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Equality &amp; opportunity", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Girls staying in school",
                      "Women's economic participation",
                      "Gender equality and autonomy"]}]}]},
             {"t": "hbox", "color": "amber", "html": "SRHR is woven through the Sustainable "
              "Development Goals &mdash; on health (SDG&nbsp;3) and gender equality (SDG&nbsp;5)."},
         ]},

        {"type": "content", "label": "Language", "title": "How we talk about it shapes whether people seek help",
         "blocks": [
             {"t": "body", "html": "Stigma and shame keep people from clinics, classrooms and "
              "conversations. Practitioners set the tone: respectful, accurate, non-judgemental "
              "language is itself a form of care."},
             {"t": "table",
              "head": ["Avoid", "Prefer"],
              "rows": [
                  ["Shaming or moralising tone", "Neutral, factual, respectful"],
                  ["Assuming everyone is heterosexual / married", "Inclusive, open questions"],
                  ["Euphemism that confuses", "Clear, correct anatomical terms"],
                  ["Blaming the person", "Focusing on rights and support"]]},
         ]},

        {"type": "content", "label": "Section Map", "title": "Where this course goes next",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>The rights framework</strong> that underpins SRHR (ICPD, Guttmacher&ndash;Lancet)",
                 "<strong>Bodies, contraception, pregnancy, abortion, STIs</strong> &mdash; the clinical core",
                 "<strong>Comprehensive sexuality education</strong> and the evidence behind it",
                 "<strong>Gender, consent and GBV</strong>, and access for adolescents",
                 "<strong>SRHR in the South Asian context</strong> &mdash; barriers, programmes, practice"]},
             {"t": "hbox", "color": "cyan", "html": "Throughout, examples are India-centric, with "
              "sources named so you can verify and go deeper."},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "The Rights Framework"},

        {"type": "content", "label": "Foundations", "title": "SRHR is grounded in human rights",
         "blocks": [
             {"t": "body", "html": "The 'R' in SRHR is not rhetorical. These are existing human "
              "rights &mdash; to life, health, privacy, equality, non-discrimination and to be free "
              "from violence &mdash; applied to sexuality and reproduction."},
             {"t": "term", "word": "Reproductive rights",
              "def": "The right of all individuals and couples to decide freely and responsibly "
              "the number, spacing and timing of their children, and to have the information and "
              "means to do so &mdash; free of coercion, discrimination and violence."},
         ]},

        {"type": "content", "label": "1994", "title": "ICPD Cairo, 1994: a turning point",
         "blocks": [
             {"t": "body", "html": "The <strong>International Conference on Population and "
              "Development (ICPD)</strong>, held in Cairo in <strong>1994</strong>, shifted the "
              "global agenda from demographic targets to individual rights and well-being. 179 "
              "governments endorsed its Programme of Action."},
             {"t": "bullets", "color": "cyan", "items": [
                 "Moved from population <em>control</em> to reproductive <em>rights</em> and choice",
                 "Centred women's empowerment, health and dignity",
                 "Rejected coercive targets and incentives in family planning",
                 "Linked reproductive health to broader development"]},
         ]},

        {"type": "content", "label": "The Shift", "title": "From population targets to people's rights",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Before ICPD", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Numeric targets, demographic goals, and "
                   "&mdash; in some places &mdash; coercive sterilisation drives. People treated as "
                   "numbers to be managed."}]}],
              "right": [{"t": "panel", "color": "green", "title": "After ICPD", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Voluntary, informed choice; quality of care; "
                   "rights and well-being at the centre. The individual, not the target, comes "
                   "first."}]}]},
             {"t": "hbox", "color": "amber", "html": "India formally moved to a 'target-free' "
              "approach in family planning after Cairo &mdash; a direct legacy of ICPD."},
         ]},

        {"type": "content", "label": "Bodily Autonomy", "title": "Bodily autonomy is the core principle",
         "blocks": [
             {"t": "term", "word": "Bodily autonomy",
              "def": "The right to make decisions about one's own body and future, free from "
              "coercion, violence or discrimination &mdash; including decisions about sex, "
              "contraception, pregnancy and health care."},
             {"t": "hbox", "color": "indigo", "html": "Autonomy means a person can say yes, say no, "
              "and decide for themselves &mdash; the foundation on which all of SRHR rests."},
         ]},

        {"type": "content", "label": "The Definition", "title": "The Guttmacher&ndash;Lancet definition of SRHR",
         "blocks": [
             {"t": "body", "html": "In 2018 the <strong>Guttmacher&ndash;Lancet Commission</strong> "
              "set out an integrated, comprehensive definition of SRHR &mdash; widely used as a "
              "benchmark for what a full package of rights and services includes."},
             {"t": "quote",
              "text": "Sexual and reproductive health is a state of physical, emotional, mental and "
              "social well-being in relation to all aspects of sexuality and reproduction, not "
              "merely the absence of disease, dysfunction or infirmity.",
              "attr": "&mdash; Guttmacher&ndash;Lancet Commission, 2018"},
         ]},

        {"type": "content", "label": "Essential Package", "title": "What a comprehensive SRHR package includes",
         "compact": True,
         "blocks": [
             {"t": "bullets", "sm": True, "items": [
                 "Comprehensive sexuality education",
                 "Contraceptive counselling and a full method choice",
                 "Antenatal, childbirth and postnatal care",
                 "Safe abortion care and post-abortion care",
                 "Prevention and treatment of STIs, including HIV",
                 "Prevention and care for gender-based violence",
                 "Counselling and care for sexual health and infertility"]},
             {"t": "hbox", "color": "cyan", "html": "Source: Guttmacher&ndash;Lancet Commission "
              "(2018). These elements are interdependent &mdash; gaps in one weaken the rest."},
         ]},

        {"type": "content", "label": "Three Pillars", "title": "Availability, accessibility, acceptability, quality",
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Available", "label": "Services and supplies actually exist and are stocked",
                  "color": "cyan"},
                 {"num": "Accessible", "label": "Reachable, affordable and non-discriminatory for all",
                  "color": "green"},
                 {"num": "Acceptable", "label": "Respectful of dignity, confidentiality and culture",
                  "color": "indigo"},
                 {"num": "Quality", "label": "Medically appropriate, safe and good quality",
                  "color": "amber"}]},
             {"t": "hbox", "color": "amber", "html": "The 'AAAQ' framework (from the right to "
              "health) is a practical checklist for assessing any SRHR service."},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "Bodies &amp; Puberty"},

        {"type": "content", "label": "First Principles", "title": "Accurate, non-shaming body knowledge",
         "blocks": [
             {"t": "body", "html": "People &mdash; especially adolescents &mdash; have a right to "
              "correct information about their own bodies. Using accurate anatomical terms, without "
              "shame, helps people understand health, recognise problems and seek care."},
             {"t": "hbox", "color": "cyan", "html": "Myths and silence cause harm. Naming body "
              "parts and processes plainly is part of safeguarding and good health practice."},
         ]},

        {"type": "content", "label": "Puberty", "title": "Puberty: a normal stage of development",
         "blocks": [
             {"t": "body", "html": "Puberty is the transition to reproductive maturity, driven by "
              "hormones, usually beginning between roughly ages 8 and 14. Timing varies widely and "
              "normally &mdash; there is no single 'right' age."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Common changes", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Growth spurts and body changes",
                      "Development of secondary sex characteristics",
                      "Onset of menstruation; capacity for reproduction"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Also normal", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Mood changes and new emotions",
                      "Wide variation in timing between individuals",
                      "Curiosity and questions about sexuality"]}]}]},
         ]},

        {"type": "content", "label": "The Cycle", "title": "The menstrual cycle, simply",
         "blocks": [
             {"t": "body", "html": "The menstrual cycle is the monthly preparation of the body for "
              "a possible pregnancy. A common average is about <strong>28 days</strong>, but "
              "cycles between roughly 21 and 35 days are normal and vary between people."},
             {"t": "flow", "steps": [
                 "MENSTRUATION: the lining sheds (the 'period')",
                 "FOLLICULAR: an egg matures; lining rebuilds",
                 "OVULATION: an egg is released (around mid-cycle)",
                 "LUTEAL: body prepares; if no pregnancy, cycle repeats"]},
         ]},

        {"type": "content", "label": "Fertility Awareness", "title": "When pregnancy is possible",
         "blocks": [
             {"t": "body", "html": "Pregnancy is most likely around <strong>ovulation</strong>, in "
              "the days before and the day of egg release &mdash; the 'fertile window'. Because "
              "cycles vary, this window is not perfectly predictable, which is why fertility-"
              "awareness methods require care and training."},
             {"t": "hbox", "color": "amber", "html": "Accurate cycle knowledge supports informed "
              "choices &mdash; but on its own it is one of the <em>less</em> reliable ways to avoid "
              "pregnancy. We return to method effectiveness in the next section."},
         ]},

        {"type": "content", "label": "MHH", "title": "Menstrual health and hygiene",
         "blocks": [
             {"t": "body", "html": "<strong>Menstrual health and hygiene (MHH)</strong> means "
              "being able to manage menstruation safely, with dignity and without shame &mdash; "
              "access to clean materials, private spaces, water, soap and safe disposal, plus "
              "accurate information."},
             {"t": "bullets", "color": "green", "items": [
                 "Clean menstrual materials, changed as needed",
                 "Private, safe space with water and soap",
                 "Safe disposal or hygienic reuse of materials",
                 "Freedom from stigma, restriction and exclusion"]},
         ]},

        {"type": "content", "label": "Stigma", "title": "Menstrual stigma has real costs",
         "blocks": [
             {"t": "body", "html": "Across South Asia, menstruation is surrounded by taboos and "
              "restrictions &mdash; on movement, food, worship and school. These are cultural "
              "constructs, not health requirements, and they can harm well-being and education."},
             {"t": "hbox", "color": "red", "html": "Menstruation is normal and healthy. Practical "
              "support &mdash; toilets, materials, accurate information &mdash; matters more than "
              "any taboo. Challenge shame gently and factually."},
         ]},

        {"type": "content", "label": "When to Seek Care", "title": "Common concerns that deserve a check-up",
         "blocks": [
             {"t": "bullets", "items": [
                 "Periods that are extremely heavy, very painful or absent",
                 "Bleeding between periods or after sex",
                 "Unusual discharge, sores, pain or itching",
                 "Any concern about development, fertility or sexual health"]},
             {"t": "hbox", "color": "cyan", "html": "Normalising help-seeking is part of the job: "
              "many treatable conditions go unaddressed because of embarrassment or lack of "
              "information."},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Contraception &amp; Family Planning"},

        {"type": "content", "label": "The Right", "title": "Deciding whether and when to have children",
         "blocks": [
             {"t": "body", "html": "Family planning lets people decide the number, spacing and "
              "timing of children. It is a recognised human right and one of the most cost-"
              "effective health interventions &mdash; preventing unintended pregnancies, unsafe "
              "abortions and maternal deaths."},
             {"t": "hbox", "color": "green", "html": "The goal is <strong>informed, voluntary "
              "choice</strong> &mdash; never coercion, never a target. The person chooses the method "
              "that fits their life."},
         ]},

        {"type": "content", "label": "Method Families", "title": "A map of contraceptive methods",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Family", "Examples", "Notes"],
              "rows": [
                  ["Barrier", "Male &amp; female condoms, diaphragm", "Condoms also prevent STIs/HIV"],
                  ["Short-acting hormonal", "Pills, injectables, patch", "User must remember / re-dose"],
                  ["Long-acting reversible (LARC)", "IUD/IUCD, implant", "Years of protection; reversible"],
                  ["Permanent", "Female &amp; male sterilisation", "Intended to be permanent"],
                  ["Emergency", "Emergency contraceptive pill", "After unprotected sex; not routine"],
                  ["Fertility-awareness", "Cycle tracking, withdrawal", "Less reliable in typical use"]]},
             {"t": "hbox", "color": "cyan", "html": "No method is 'best' for everyone &mdash; the "
              "right method depends on health, preferences, stage of life and partner."},
         ]},

        {"type": "content", "label": "Effectiveness", "title": "Typical use vs perfect use",
         "blocks": [
             {"t": "body", "html": "Effectiveness has two numbers. <strong>Perfect use</strong> "
              "assumes the method is always used correctly; <strong>typical use</strong> reflects "
              "real life, with the occasional missed pill or unused condom. Typical use is what "
              "matters for counselling."},
             {"t": "term", "word": "Typical-use effectiveness",
              "def": "The percentage of users who avoid pregnancy over a year as the method is "
              "actually used in everyday life &mdash; usually lower than perfect-use effectiveness."},
         ]},

        {"type": "content", "label": "The Numbers", "title": "Effectiveness by method (typical use)",
         "blocks": [
             {"t": "chart", "canvas": "contraEffChart",
              "title": "Approx. % of users avoiding pregnancy in 1 year (typical use)",
              "source": "Well-established typical-use figures (e.g. WHO / CDC family planning guidance)",
              "type": "bar",
              "data": {"labels": ["Implant", "IUD/IUCD", "Injectable", "Pill", "Male condom",
                                  "Withdrawal", "Fertility-awareness"],
                       "datasets": [{"label": "% avoiding pregnancy (typical use)",
                                     "data": [99, 99, 96, 91, 82, 80, 77],
                                     "backgroundColor": "#0EA5E9"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% effective (typical use)'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Long-acting methods (implant, IUD) are the "
              "most effective because they remove the chance of user error. Figures are rounded "
              "and well-established; exact values vary slightly by source."},
         ]},

        {"type": "content", "label": "Dual Protection", "title": "Condoms protect twice over",
         "blocks": [
             {"t": "body", "html": "Condoms are unique: they prevent both <strong>pregnancy</strong> "
              "and the transmission of <strong>STIs, including HIV</strong>. This is called "
              "<strong>dual protection</strong>."},
             {"t": "hbox", "color": "green", "html": "Even when another method (a pill or IUD) is "
              "used for pregnancy prevention, a condom may still be needed for STI/HIV protection. "
              "The two jobs are different."},
         ]},

        {"type": "content", "label": "Emergency", "title": "Emergency contraception, accurately",
         "blocks": [
             {"t": "body", "html": "The <strong>emergency contraceptive pill</strong> can reduce "
              "the chance of pregnancy after unprotected sex or method failure, and works best the "
              "sooner it is taken. It is a backup, not a routine method."},
             {"t": "hbox", "color": "red", "html": "Important: emergency contraception is "
              "<strong>not</strong> an abortion &mdash; it works mainly by preventing or delaying "
              "ovulation. It also does not protect against STIs."},
         ]},

        {"type": "content", "label": "Informed Choice", "title": "Good counselling is the heart of family planning",
         "blocks": [
             {"t": "bullets", "items": [
                 "Present the <strong>full range</strong> of methods, not just one",
                 "Explain effectiveness, use, side-effects and reversibility honestly",
                 "Respect the person's preferences, life stage and circumstances",
                 "Make clear they can <strong>switch or stop</strong> at any time"]},
             {"t": "hbox", "color": "amber", "html": "Quality of care &mdash; not just supply "
              "&mdash; is what makes family planning rights-based. Coercion of any kind violates "
              "it."},
         ]},

        {"type": "content", "label": "Unmet Need", "title": "Unmet need for family planning",
         "blocks": [
             {"t": "term", "word": "Unmet need",
              "def": "The share of people who want to avoid or delay pregnancy but are not using "
              "any contraceptive method &mdash; a key indicator of gaps in access, information and "
              "autonomy."},
             {"t": "body", "html": "Reducing unmet need is a core SRHR goal. In India, modern "
              "contraceptive use has risen and unmet need has fallen over successive NFHS rounds, "
              "though gaps persist &mdash; especially for spacing methods and among young and "
              "newly married women."},
             {"t": "hbox", "color": "cyan", "html": "Source: National Family Health Survey (NFHS), "
              "successive rounds. Always check the latest round for current figures."},
         ]},

        {"type": "content", "label": "The Trend", "title": "Modern contraceptive use is rising in India",
         "blocks": [
             {"t": "chart", "canvas": "mcprChart",
              "title": "Modern contraceptive prevalence rate (mCPR), India (% of married women 15&ndash;49)",
              "source": "Illustrative trend patterned on NFHS rounds; check latest NFHS for exact figures",
              "type": "line",
              "data": {"labels": ["NFHS-3 (2005&ndash;06)", "NFHS-4 (2015&ndash;16)", "NFHS-5 (2019&ndash;21)"],
                       "datasets": [{"label": "mCPR (%)",
                                     "data": [49, 48, 57],
                                     "borderColor": "#6366F1",
                                     "backgroundColor": "rgba(99,102,241,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 5}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% using a modern method'} } } }"}},
             {"t": "hbox", "color": "cyan", "html": "Modern method use has risen and unmet need "
              "has fallen across NFHS rounds. Values shown are illustrative of the trend &mdash; "
              "consult the latest NFHS factsheet for exact numbers."},
         ]},

        {"type": "content", "label": "The Method Mix", "title": "India's method mix is shifting",
         "blocks": [
             {"t": "body", "html": "Historically, India's contraceptive use leaned heavily on "
              "<strong>female sterilisation</strong>. A rights-based system widens the mix &mdash; "
              "adding spacing methods (pills, IUDs, injectables, condoms) so people have real "
              "choice across their lives, not just one permanent option."},
             {"t": "hbox", "color": "amber", "html": "A balanced method mix &mdash; and more male "
              "responsibility &mdash; is a marker of a maturing, choice-based programme."},
         ]},

        {"type": "content", "label": "Men's Role", "title": "Family planning is not only women's work",
         "blocks": [
             {"t": "body", "html": "In much of South Asia, the burden of contraception falls "
              "overwhelmingly on women. Yet condoms and vasectomy are safe, simple options, and "
              "men's support shapes whether women can use any method at all."},
             {"t": "hbox", "color": "green", "html": "Engaging men and boys &mdash; as users and "
              "as supportive partners &mdash; is a recognised way to improve both uptake and gender "
              "equality."},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Pregnancy &amp; Maternal Health"},

        {"type": "content", "label": "Continuum", "title": "A continuum of care around pregnancy",
         "blocks": [
             {"t": "flow", "steps": [
                 "PRE-PREGNANCY: nutrition, planning, anaemia care",
                 "ANTENATAL: check-ups, screening, counselling",
                 "CHILDBIRTH: skilled, safe delivery",
                 "POSTNATAL: care for mother &amp; newborn after birth"]},
             {"t": "hbox", "color": "cyan", "html": "Most maternal and newborn deaths are "
              "preventable with timely, quality care across this whole continuum."},
         ]},

        {"type": "content", "label": "Antenatal Care", "title": "Antenatal care (ANC)",
         "blocks": [
             {"t": "body", "html": "<strong>Antenatal care</strong> is care during pregnancy: "
              "monitoring the mother and baby, screening for and managing complications, and "
              "counselling on nutrition, danger signs and birth planning. WHO recommends "
              "<strong>at least eight ANC contacts</strong> for a positive pregnancy experience."},
             {"t": "bullets", "color": "green", "items": [
                 "Detect and manage anaemia, hypertension and infection early",
                 "Iron-folic acid and other supplementation as advised",
                 "Tetanus protection and screening for STIs/HIV",
                 "Plan for a skilled, safe birth"]},
         ]},

        {"type": "content", "label": "Safe Delivery", "title": "Skilled birth attendance saves lives",
         "blocks": [
             {"t": "body", "html": "Having a <strong>skilled birth attendant</strong> &mdash; and "
              "a facility able to manage emergencies &mdash; is the single biggest protector "
              "against maternal and newborn death. Institutional delivery in India has risen "
              "substantially over the NFHS rounds."},
             {"t": "hbox", "color": "cyan", "html": "Source: NFHS. Programmes such as Janani "
              "Suraksha Yojana and Janani Shishu Suraksha Karyakram promote and support "
              "institutional delivery."},
         ]},

        {"type": "content", "label": "A Real Shift", "title": "Institutional delivery has risen sharply",
         "blocks": [
             {"t": "chart", "canvas": "instDelChart",
              "title": "Births delivered in a health facility, India (%)",
              "source": "Illustrative trend patterned on NFHS rounds; check latest NFHS for exact figures",
              "type": "bar",
              "data": {"labels": ["NFHS-3 (2005&ndash;06)", "NFHS-4 (2015&ndash;16)", "NFHS-5 (2019&ndash;21)"],
                       "datasets": [{"label": "Institutional births (%)",
                                     "data": [39, 79, 89],
                                     "backgroundColor": "#10B981"}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:100, title:{display:true,text:'% of births in a facility'} } } }"}},
             {"t": "hbox", "color": "green", "html": "One of India's clearest public-health gains. "
              "Values are illustrative of the well-documented upward trend &mdash; consult the "
              "latest NFHS factsheet for exact figures."},
         ]},

        {"type": "content", "label": "Maternal Mortality", "title": "What is maternal mortality?",
         "blocks": [
             {"t": "term", "word": "Maternal Mortality Ratio (MMR)",
              "def": "The number of maternal deaths per 100,000 live births. It captures deaths "
              "from pregnancy- and childbirth-related causes &mdash; a sensitive marker of a "
              "health system's reach and quality."},
             {"t": "body", "html": "Leading direct causes include severe bleeding, infection, "
              "high blood pressure disorders (pre-eclampsia/eclampsia) and complications of unsafe "
              "abortion &mdash; most of them preventable or treatable."},
         ]},

        {"type": "content", "label": "Progress", "title": "India's maternal mortality has fallen substantially",
         "blocks": [
             {"t": "chart", "canvas": "mmrTrendChart",
              "title": "India's Maternal Mortality Ratio over time (deaths per 100,000 live births)",
              "source": "SRS, Office of the Registrar General of India (trend; figures rounded)",
              "type": "line",
              "data": {"labels": ["2007&ndash;09", "2010&ndash;12", "2014&ndash;16", "2016&ndash;18", "2018&ndash;20"],
                       "datasets": [{"label": "MMR (per 100,000 live births)",
                                     "data": [212, 178, 130, 113, 97],
                                     "borderColor": "#10B981",
                                     "backgroundColor": "rgba(16,185,129,0.10)",
                                     "fill": True, "tension": 0.3, "pointRadius": 4}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, title:{display:true,text:'MMR per 100,000'} } } }"}},
             {"t": "hbox", "color": "green", "html": "India's MMR has fallen markedly per the "
              "Sample Registration System (SRS). The downward trend is well established; exact "
              "values are SRS estimates and are revised periodically &mdash; check the latest SRS "
              "bulletin."},
         ]},

        {"type": "content", "label": "Postnatal", "title": "The postnatal period is high-risk and often neglected",
         "blocks": [
             {"t": "body", "html": "Many maternal and newborn deaths happen in the days "
              "<em>after</em> birth, yet postnatal care is often the weakest link. Care in this "
              "window protects both mother and baby."},
             {"t": "bullets", "items": [
                 "Postnatal check-ups for mother and newborn",
                 "Support for breastfeeding and newborn warmth",
                 "Watch for danger signs (bleeding, fever, infection)",
                 "Family-planning counselling and emotional/mental-health support"]},
         ]},

        {"type": "content", "label": "Equity", "title": "Maternal health gaps are equity gaps",
         "blocks": [
             {"t": "body", "html": "National averages hide large gaps. Maternal outcomes are worse "
              "for poorer households, less-educated women, some states and districts, and "
              "marginalised communities &mdash; the people furthest from quality care."},
             {"t": "hbox", "color": "amber", "html": "Improving the average is not enough. "
              "Rights-based maternal health means closing the gap for those left behind. "
              "Disaggregate before you conclude."},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Safe Abortion &amp; the Law"},

        {"type": "content", "label": "Framing", "title": "Safe abortion is essential health care",
         "blocks": [
             {"t": "body", "html": "Access to safe abortion is part of comprehensive SRHR. Where "
              "it is unavailable or stigmatised, people resort to <strong>unsafe abortion</strong> "
              "&mdash; a major, preventable cause of maternal death and injury worldwide."},
             {"t": "hbox", "color": "cyan", "html": "This is a clinical and rights matter, "
              "approached without judgement. In India, abortion is <strong>legal</strong> under "
              "specified conditions &mdash; many people do not know this."},
         ]},

        {"type": "content", "label": "The Law", "title": "The Medical Termination of Pregnancy (MTP) Act",
         "blocks": [
             {"t": "body", "html": "India's <strong>Medical Termination of Pregnancy (MTP) Act, "
              "1971</strong> permits abortion by a registered medical practitioner under specified "
              "conditions &mdash; for example, risk to the woman's physical or mental health, fetal "
              "abnormality, or pregnancy from rape or contraceptive failure."},
             {"t": "hbox", "color": "amber", "html": "Note: abortion in India is governed by "
              "medical conditions and gestational limits in law &mdash; it is permitted on broad "
              "grounds, but it is not 'abortion on request' at any stage."},
         ]},

        {"type": "content", "label": "2021 Amendment", "title": "The MTP (Amendment) Act, 2021",
         "blocks": [
             {"t": "body", "html": "The <strong>2021 amendment</strong> expanded access. Among its "
              "key changes:"},
             {"t": "bullets", "color": "cyan", "items": [
                 "Raised the upper gestational limit to <strong>24 weeks</strong> for specific "
                 "categories of women (as defined in the rules)",
                 "Allowed certain abortions up to 20 weeks on the opinion of one provider",
                 "Recognised failure of contraception for unmarried women, not only married women",
                 "Required confidentiality &mdash; the provider must not reveal the woman's "
                 "identity except as permitted by law"]},
             {"t": "hbox", "color": "amber", "html": "Beyond 24 weeks, certain cases (e.g. "
              "substantial fetal abnormality) may be considered by a Medical Board. The exact "
              "categories are set out in the MTP Rules."},
         ]},

        {"type": "content", "label": "Comprehensive Care", "title": "Comprehensive abortion care",
         "blocks": [
             {"t": "term", "word": "Comprehensive abortion care",
              "def": "Information, safe abortion services (medical or surgical, as appropriate), "
              "and post-abortion care &mdash; including contraceptive counselling &mdash; delivered "
              "with dignity and confidentiality."},
             {"t": "bullets", "items": [
                 "Accurate information and supportive counselling",
                 "Safe method appropriate to the gestation",
                 "Management of any complications",
                 "Post-abortion contraception, if the person wants it"]},
         ]},

        {"type": "content", "label": "Distinction", "title": "Two laws that are easy to confuse",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "MTP Act", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Governs <em>when and how</em> a pregnancy may "
                   "be legally terminated. It is about access to safe abortion care."}]}],
              "right": [{"t": "panel", "color": "red", "title": "PCPNDT Act", "blocks": [
                  {"t": "body", "cls": "sm", "html": "The Pre-Conception and Pre-Natal Diagnostic "
                   "Techniques Act bans sex-selective <em>determination</em> to prevent sex-"
                   "selective abortion. It does not restrict legal abortion itself."}]}]},
             {"t": "hbox", "color": "amber", "html": "Conflating the two can wrongly deny women "
              "lawful abortion care. They serve different purposes."},
         ]},

        {"type": "content", "label": "Unsafe Abortion", "title": "The cost of restricting safe care",
         "blocks": [
             {"t": "body", "html": "Where safe, legal abortion is hard to reach, people turn to "
              "<strong>unsafe methods</strong> &mdash; untrained providers, unsafe procedures, "
              "dangerous self-medication. Unsafe abortion is a leading, and almost entirely "
              "preventable, cause of maternal death and injury."},
             {"t": "hbox", "color": "red", "html": "The evidence is clear: restricting access does "
              "not reduce abortions &mdash; it makes them less safe. Safe, legal services save "
              "lives."},
         ]},

        {"type": "content", "label": "Barriers", "title": "Why legal does not always mean accessible",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Stigma and fear of judgement keep people away",
                 "Providers and clients unaware of what the law allows",
                 "Shortage of trained providers and approved facilities",
                 "Confusion with the PCPNDT Act leading to denial of care"]},
             {"t": "hbox", "color": "cyan", "html": "Practitioners can help by knowing the law "
              "accurately, providing confidential information, and referring to safe, approved "
              "services."},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "STIs &amp; HIV"},

        {"type": "content", "label": "Basics", "title": "What are STIs?",
         "blocks": [
             {"t": "term", "word": "Sexually transmitted infection (STI)",
              "def": "An infection passed mainly through sexual contact. STIs can be bacterial "
              "(e.g. syphilis, gonorrhoea, chlamydia), viral (e.g. HIV, herpes, HPV) or "
              "parasitic. Many are curable; viral ones are usually manageable."},
             {"t": "body", "html": "Many STIs cause <strong>no symptoms</strong>, especially "
              "early on &mdash; so people can transmit them without knowing. This is why testing "
              "matters, not just symptoms."},
         ]},

        {"type": "content", "label": "Prevention", "title": "Preventing STIs and HIV",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Condoms</strong> &mdash; correct, consistent use is highly protective",
                 "<strong>Testing</strong> &mdash; know your status; many STIs are silent",
                 "<strong>Vaccination</strong> &mdash; e.g. HPV vaccine prevents cervical cancer",
                 "<strong>Prompt treatment</strong> &mdash; treat partners to stop re-infection"]},
             {"t": "hbox", "color": "cyan", "html": "Condoms remain the cornerstone &mdash; the "
              "only method offering dual protection against both STIs/HIV and pregnancy."},
         ]},

        {"type": "content", "label": "HIV Basics", "title": "HIV and AIDS, accurately",
         "blocks": [
             {"t": "body", "html": "<strong>HIV</strong> is a virus that weakens the immune system; "
              "untreated, it can progress to <strong>AIDS</strong>. It spreads through specific "
              "routes &mdash; unprotected sex, infected blood, shared injecting equipment, and "
              "from mother to child &mdash; <em>not</em> through everyday contact."},
             {"t": "hbox", "color": "red", "html": "HIV is <strong>not</strong> spread by sharing "
              "food, hugging, shaking hands, toilets or mosquito bites. Myths fuel stigma; facts "
              "dismantle it."},
         ]},

        {"type": "content", "label": "Treatment", "title": "HIV is now a manageable condition",
         "blocks": [
             {"t": "body", "html": "<strong>Antiretroviral therapy (ART)</strong> suppresses the "
              "virus, lets people live long, healthy lives, and &mdash; when the virus is "
              "undetectable &mdash; means it is not sexually transmitted (the "
              "'<strong>Undetectable = Untransmittable</strong>', or U=U, principle)."},
             {"t": "stats", "cols": 3, "cards": [
                 {"num": "Test", "label": "Free, confidential testing", "color": "cyan"},
                 {"num": "Treat", "label": "Lifelong ART, available free in India", "color": "green"},
                 {"num": "U=U", "label": "Undetectable = Untransmittable", "color": "indigo"}]},
         ]},

        {"type": "content", "label": "Prevention Tools", "title": "Prevention of mother-to-child &amp; PrEP",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>PMTCT:</strong> treatment in pregnancy can prevent transmission to the "
                 "baby in the great majority of cases",
                 "<strong>PrEP:</strong> medicine taken by HIV-negative people at higher risk to "
                 "prevent infection",
                 "<strong>PEP:</strong> emergency medicine soon after a possible exposure",
                 "<strong>Condoms:</strong> still central, and protect against other STIs too"]},
             {"t": "hbox", "color": "cyan", "html": "India's HIV response is delivered largely "
              "through NACO (the National AIDS Control Organisation) and its programmes."},
         ]},

        {"type": "content", "label": "Stigma", "title": "Stigma is a barrier to testing and treatment",
         "blocks": [
             {"t": "body", "html": "Fear of judgement stops people testing, disclosing and seeking "
              "care &mdash; which harms both individuals and public health. People living with HIV "
              "or an STI deserve confidentiality, dignity and non-discrimination."},
             {"t": "hbox", "color": "amber", "html": "Use accurate, non-blaming language. STIs are "
              "infections, not moral failings. Reducing stigma is itself a prevention strategy."},
         ]},

        {"type": "content", "label": "Common STIs", "title": "Some STIs at a glance",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["STI", "Type", "Note"],
              "rows": [
                  ["Chlamydia / gonorrhoea", "Bacterial", "Often silent; curable with antibiotics"],
                  ["Syphilis", "Bacterial", "Curable; dangerous in pregnancy if untreated"],
                  ["HIV", "Viral", "Manageable lifelong with ART"],
                  ["Herpes (HSV)", "Viral", "Manageable, not curable"],
                  ["HPV", "Viral", "Vaccine-preventable; can cause cervical cancer"]]},
             {"t": "hbox", "color": "cyan", "html": "Untreated STIs can cause infertility, "
              "pregnancy complications and increased HIV risk &mdash; another reason testing and "
              "early treatment matter."},
         ]},

        {"type": "content", "label": "Cervical Cancer", "title": "HPV, cervical cancer and prevention",
         "blocks": [
             {"t": "body", "html": "Most cervical cancer is caused by <strong>HPV</strong>, a "
              "common sexually transmitted virus. It is one of the most preventable cancers "
              "&mdash; through HPV vaccination and screening &mdash; yet remains a major cause of "
              "cancer death among women in the region."},
             {"t": "hbox", "color": "green", "html": "HPV vaccination (ideally before sexual "
              "debut) plus screening can prevent the great majority of cervical cancers. WHO has a "
              "global elimination strategy."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Comprehensive Sexuality Education"},

        {"type": "content", "label": "Definition", "title": "What comprehensive sexuality education is",
         "blocks": [
             {"t": "term", "word": "Comprehensive sexuality education (CSE)",
              "def": "Age-appropriate, scientifically accurate, rights-based teaching about the "
              "cognitive, emotional, physical and social aspects of sexuality &mdash; bodies, "
              "relationships, consent, gender, health and rights."},
             {"t": "body", "html": "CSE is far broader than 'sex' &mdash; it builds knowledge, "
              "skills, attitudes and values that help young people protect their health and form "
              "respectful relationships."},
         ]},

        {"type": "content", "label": "What It Covers", "title": "More than biology",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Knowledge", "blocks": [
                  {"t": "bullets", "sm": True, "items": [
                      "Bodies, puberty and reproduction",
                      "Contraception and STI/HIV prevention",
                      "Where to get help and services"]}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Skills &amp; values", "blocks": [
                  {"t": "bullets", "sm": True, "color": "indigo", "items": [
                      "Consent and communication",
                      "Recognising and resisting coercion and abuse",
                      "Respect, gender equality and rights"]}]}]},
         ]},

        {"type": "content", "label": "Key Principle", "title": "Age-appropriate and incremental",
         "blocks": [
             {"t": "body", "html": "CSE is <strong>age-appropriate</strong>: young children learn "
              "about bodies, feelings, safety and respect; older adolescents learn about "
              "relationships, contraception and rights. Content is matched to developmental stage."},
             {"t": "flow", "steps": [
                 "EARLY: body autonomy, naming parts, 'safe vs unsafe' touch",
                 "PRE-TEEN: puberty, emotions, respect, online safety",
                 "ADOLESCENT: relationships, consent, contraception, STIs",
                 "OLDER: rights, services, planning, gender equality"]},
         ]},

        {"type": "content", "label": "The Evidence", "title": "CSE does NOT increase sexual activity",
         "blocks": [
             {"t": "body", "html": "This is one of the best-established findings in the field. "
              "Rigorous reviews show that good CSE does <strong>not</strong> lead young people to "
              "start having sex earlier or to have more partners."},
             {"t": "hbox", "color": "green", "html": "If anything, the evidence points the other "
              "way: CSE is associated with <strong>delayed</strong> sexual debut and "
              "<strong>safer</strong> behaviour when young people do become sexually active."},
         ]},

        {"type": "content", "label": "What It Achieves", "title": "What the evidence shows CSE does",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Increases knowledge and corrects myths",
                 "Is linked to later sexual debut and fewer partners",
                 "Increases use of contraception and condoms among the sexually active",
                 "Builds skills to recognise abuse and seek help"]},
             {"t": "hbox", "color": "cyan", "html": "Source: UNESCO and WHO reviews of sexuality "
              "education evidence. Quality and rights-based content matter &mdash; "
              "'abstinence-only' programmes do not show these benefits."},
         ]},

        {"type": "content", "label": "Seeing the Evidence", "title": "What good CSE shifts",
         "blocks": [
             {"t": "chart", "canvas": "cseImpactChart",
              "title": "Direction of effect of quality CSE on key outcomes (schematic)",
              "source": "Illustrative schematic of findings in UNESCO/WHO evidence reviews",
              "type": "bar",
              "data": {"labels": ["Knowledge", "Later sexual debut", "Condom/contraceptive use",
                                  "Earlier sexual debut"],
                       "datasets": [{"label": "Direction of effect",
                                     "data": [3, 2, 2, 0],
                                     "backgroundColor": ["#10B981", "#10B981", "#10B981", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{ min:0, max:3, ticks:{display:false}, title:{display:true,text:'increase   \\u2192'} } } }"}},
             {"t": "hbox", "color": "amber", "html": "Schematic, not measured magnitudes: CSE "
              "raises knowledge and safer behaviour while the feared effect &mdash; earlier debut "
              "&mdash; does not appear. Source: UNESCO/WHO evidence reviews."},
         ]},

        {"type": "content", "label": "Myths", "title": "Common myths about CSE &mdash; and the facts",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Myth", "Fact"],
              "rows": [
                  ["It encourages young people to have sex", "Evidence shows the opposite or no effect"],
                  ["It is 'too much, too young'", "Content is age-appropriate and incremental"],
                  ["It is against our culture", "It builds respect, safety and consent &mdash; shared values"],
                  ["Silence keeps children safe", "Knowledge helps children recognise and report abuse"]]},
             {"t": "hbox", "color": "amber", "html": "Addressing myths respectfully &mdash; with "
              "evidence &mdash; is often the key to gaining community and parental support."},
         ]},

        {"type": "content", "label": "In India", "title": "CSE in the Indian context",
         "blocks": [
             {"t": "body", "html": "India delivers adolescence and life-skills education through "
              "school and health programmes (for example, the Adolescence Education Programme and "
              "the Health and Wellness Ambassador / 'School Health Programme' initiatives), though "
              "coverage and content vary by state."},
             {"t": "hbox", "color": "cyan", "html": "Framing matters: 'life skills', 'adolescent "
              "health' and 'wellness' framings often gain acceptance where the label 'sex "
              "education' meets resistance &mdash; while keeping the rights-based content."},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Gender, Consent &amp; GBV"},

        {"type": "content", "label": "Consent", "title": "Consent is the foundation of healthy sexuality",
         "blocks": [
             {"t": "term", "word": "Consent",
              "def": "A clear, freely given, informed and reversible agreement to a specific "
              "activity. It must be ongoing, and it cannot be given under pressure, deception, "
              "intoxication, or by someone below the legal age."},
             {"t": "hbox", "color": "indigo", "html": "Consent is enthusiastic and reversible: "
              "silence is not consent, and a yes can be withdrawn at any time."},
         ]},

        {"type": "content", "label": "What Consent Is", "title": "The features of real consent",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Freely given</strong> &mdash; no pressure, threat or manipulation",
                 "<strong>Informed</strong> &mdash; the person knows what they are agreeing to",
                 "<strong>Specific</strong> &mdash; to one thing, not a blanket permission",
                 "<strong>Reversible</strong> &mdash; can be withdrawn at any moment",
                 "<strong>Ongoing</strong> &mdash; checked each time, not assumed"]},
         ]},

        {"type": "content", "label": "Not Consent", "title": "What is NOT consent",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "<strong>Silence or no resistance</strong> &mdash; absence of 'no' is not 'yes'",
                 "<strong>A previous yes</strong> &mdash; consent to one act or occasion is not "
                 "consent to all",
                 "<strong>Agreement under pressure</strong>, fear, deception or coercion",
                 "<strong>From someone who cannot consent</strong> &mdash; below the legal age, "
                 "asleep, or heavily intoxicated"]},
             {"t": "hbox", "color": "amber", "html": "Within marriage too, consent matters: sex "
              "without consent is violence, whatever the relationship."},
         ]},

        {"type": "content", "label": "GBV", "title": "Gender-based violence and SRHR",
         "blocks": [
             {"t": "term", "word": "Gender-based violence (GBV)",
              "def": "Harmful acts directed at a person because of their gender &mdash; including "
              "physical, sexual, emotional and economic violence, and harmful practices. It is "
              "rooted in gender inequality and abuse of power."},
             {"t": "body", "html": "GBV is both a violation of rights and a major SRHR issue: it "
              "drives unintended pregnancy, STIs, injury, and mental-health harm, and it blocks "
              "people from seeking care."},
         ]},

        {"type": "content", "label": "Survivor-Centred", "title": "A survivor-centred response",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Safety</strong> first &mdash; for the survivor and any children",
                 "<strong>Confidentiality</strong> and respect &mdash; never blame the survivor",
                 "<strong>Choice</strong> &mdash; the survivor decides next steps",
                 "<strong>Referral</strong> &mdash; to health, legal, psychosocial and shelter support"]},
             {"t": "hbox", "color": "amber", "html": "Know your local referral pathway and helpline "
              "numbers before you need them. Care includes emergency contraception, STI/HIV "
              "prophylaxis and mental-health support."},
         ]},

        {"type": "content", "label": "Child Protection", "title": "POCSO and protecting children",
         "blocks": [
             {"t": "body", "html": "India's <strong>Protection of Children from Sexual Offences "
              "(POCSO) Act, 2012</strong> criminalises sexual offences against anyone under 18 and "
              "sets up child-friendly procedures for reporting, investigation and trial."},
             {"t": "hbox", "color": "red", "html": "POCSO places a legal duty to report child "
              "sexual abuse. Practitioners working with children must know their reporting "
              "obligations and child-protection protocols."},
         ]},

        {"type": "content", "label": "Age of Marriage", "title": "Legal age of marriage in India",
         "blocks": [
             {"t": "body", "html": "Under the <strong>Prohibition of Child Marriage Act, 2006</strong>, "
              "the legal minimum age of marriage in India is <strong>18 for women and 21 for "
              "men</strong>. Child marriage is associated with early pregnancy, school dropout and "
              "greater health risk."},
             {"t": "hbox", "color": "amber", "html": "Note: proposals to raise the age for women "
              "to 21 have been debated. State the current law accurately and check for updates "
              "before advising."},
         ]},

        {"type": "content", "label": "Inclusion", "title": "LGBTQ+ inclusion in SRHR",
         "blocks": [
             {"t": "body", "html": "A rights-based approach serves people of all sexual "
              "orientations and gender identities. In India, the Supreme Court read down Section "
              "377 in 2018 to decriminalise consensual same-sex relations, and the NALSA judgment "
              "(2014) affirmed the rights of transgender persons."},
             {"t": "hbox", "color": "indigo", "html": "Inclusive practice means non-judgemental "
              "services, correct names and pronouns, confidentiality, and care that does not "
              "assume everyone is heterosexual or cisgender."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Adolescents &amp; Access"},

        {"type": "content", "label": "Why Adolescents", "title": "Adolescents have distinct SRHR needs",
         "blocks": [
             {"t": "body", "html": "Adolescence (roughly ages 10&ndash;19) is when many SRHR needs "
              "emerge &mdash; puberty, first relationships, risk of early pregnancy and STIs &mdash; "
              "yet young people often face the greatest barriers to information and services."},
             {"t": "hbox", "color": "cyan", "html": "South Asia has a very large young population. "
              "Meeting adolescents' SRHR needs is both a rights obligation and a major "
              "opportunity."},
         ]},

        {"type": "content", "label": "RKSK", "title": "India's adolescent health programme (RKSK)",
         "blocks": [
             {"t": "body", "html": "<strong>Rashtriya Kishor Swasthya Karyakram (RKSK)</strong> is "
              "India's national adolescent health programme. It takes a holistic view of "
              "adolescent well-being and includes SRHR among its priority areas."},
             {"t": "bullets", "sm": True, "color": "cyan", "items": [
                 "Sexual and reproductive health",
                 "Nutrition (including anaemia)",
                 "Mental health and substance misuse",
                 "Injuries, violence and non-communicable disease"]},
             {"t": "hbox", "color": "green", "html": "RKSK promotes peer educators and "
              "Adolescent Friendly Health Clinics (AFHCs) to reach young people."},
         ]},

        {"type": "content", "label": "Barriers", "title": "What stops adolescents getting care",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Fear of being judged, or of parents finding out",
                 "Providers reluctant to serve unmarried young people",
                 "Lack of confidentiality and privacy at facilities",
                 "Cost, distance, clinic timings and lack of information"]},
             {"t": "hbox", "color": "amber", "html": "Many of these are about how services treat "
              "young people &mdash; not about the law. Attitudes are often the biggest barrier."},
         ]},

        {"type": "content", "label": "Confidentiality", "title": "Confidentiality builds trust",
         "blocks": [
             {"t": "body", "html": "Adolescents are far more likely to seek help when they trust "
              "that their visit will be <strong>private and confidential</strong>. Breaching "
              "confidentiality &mdash; or threatening to &mdash; drives them away and can put them "
              "at risk."},
             {"t": "hbox", "color": "red", "html": "Balance confidentiality with safeguarding: "
              "where there is abuse or serious risk (e.g. under POCSO), legal duties to protect "
              "the child apply. Know where that line sits."},
         ]},

        {"type": "content", "label": "Youth-Friendly", "title": "What makes a service youth-friendly?",
         "compact": True,
         "blocks": [
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Accessible", "label": "Convenient hours, location and low or no cost",
                  "color": "cyan"},
                 {"num": "Acceptable", "label": "Private, confidential, non-judgemental staff",
                  "color": "green"},
                 {"num": "Equitable", "label": "Serves all young people, married or not",
                  "color": "indigo"},
                 {"num": "Effective", "label": "Trained providers, the right supplies in stock",
                  "color": "amber"}]},
             {"t": "hbox", "color": "cyan", "html": "Youth-friendly is a way of working, not just "
              "a separate room. Provider attitude is the single biggest factor."},
         ]},

        {"type": "content", "label": "Engaging Young People", "title": "Reach adolescents where they are",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Peer educators</strong> &mdash; young people trust other young people",
                 "<strong>Schools and life-skills sessions</strong> &mdash; reach those still enrolled",
                 "<strong>Digital and helplines</strong> &mdash; private, accessible information",
                 "<strong>Community outreach</strong> &mdash; for those out of school"]},
             {"t": "hbox", "color": "green", "html": "Involve adolescents in designing services for "
              "adolescents. Participation improves both relevance and uptake."},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "SRHR in South Asia &amp; Practice"},

        {"type": "content", "label": "Context", "title": "The South Asian SRHR landscape",
         "blocks": [
             {"t": "body", "html": "South Asia has made major SRHR gains &mdash; falling maternal "
              "mortality, rising contraceptive use and institutional delivery &mdash; alongside "
              "persistent challenges: taboos, gender inequality, son preference and uneven access."},
             {"t": "hbox", "color": "cyan", "html": "Progress is real but uneven. The task is to "
              "extend quality SRHR to those still left behind &mdash; the poorest, the youngest "
              "and the most marginalised."},
         ]},

        {"type": "content", "label": "Taboos", "title": "Silence and stigma are health barriers",
         "blocks": [
             {"t": "body", "html": "Cultural silence around sex, menstruation and abortion keeps "
              "people from information and care. Breaking that silence &mdash; respectfully, "
              "without offending values &mdash; is core SRHR work."},
             {"t": "hbox", "color": "amber", "html": "Work <em>with</em> communities, families and "
              "trusted local voices. Confrontation hardens resistance; respectful engagement opens "
              "doors."},
         ]},

        {"type": "content", "label": "Access Gaps", "title": "Where the gaps are widest",
         "blocks": [
             {"t": "bullets", "color": "red", "items": [
                 "Rural and remote areas with few trained providers",
                 "Unmarried adolescents and young people",
                 "Poor, Dalit, Adivasi and other marginalised communities",
                 "LGBTQ+ people and persons with disabilities"]},
             {"t": "hbox", "color": "cyan", "html": "Equity lens: ask not just 'how is the average "
              "doing?' but 'who is still being missed, and why?'"},
         ]},

        {"type": "content", "label": "Programmes", "title": "Key Indian programmes and platforms",
         "compact": True,
         "blocks": [
             {"t": "table",
              "head": ["Programme / cadre", "Focus"],
              "rows": [
                  ["ASHA &amp; ANM workers", "Community-level SRHR outreach and referral"],
                  ["RKSK / AFHCs", "Adolescent health, including SRHR"],
                  ["JSY / JSSK", "Safe, institutional delivery and maternal care"],
                  ["NACO", "HIV prevention, testing and treatment"],
                  ["Family planning programme", "Counselling and a basket of methods"]]},
             {"t": "hbox", "color": "green", "html": "Frontline workers &mdash; especially ASHAs "
              "and ANMs &mdash; are the backbone of SRHR delivery in India."},
         ]},

        {"type": "content", "label": "Counselling", "title": "Principles of respectful SRHR counselling",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "Be <strong>non-judgemental</strong> &mdash; whatever the person's choices",
                 "Protect <strong>privacy and confidentiality</strong>",
                 "Give <strong>accurate, complete</strong> information, not opinions",
                 "Support the person's <strong>own decision</strong> &mdash; do not decide for them",
                 "Be inclusive of all genders, orientations and abilities"]},
         ]},

        {"type": "content", "label": "Practice Pitfalls", "title": "Common practice pitfalls to avoid",
         "blocks": [
             {"t": "table",
              "head": ["Pitfall", "Better practice"],
              "rows": [
                  ["Pushing one method or a target", "Offer the full range; respect choice"],
                  ["Refusing care to unmarried youth", "Serve all who need care, lawfully"],
                  ["Moralising or shaming", "Stay neutral, factual, supportive"],
                  ["Breaching confidentiality", "Protect privacy; know safeguarding limits"]]},
             {"t": "hbox", "color": "amber", "html": "The test of rights-based practice: did the "
              "person leave better informed, respected and free to decide?"},
         ]},

        {"type": "content", "label": "Self-Check", "title": "A practitioner's SRHR checklist",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "Am I being accurate, and non-judgemental?",
                 "Am I protecting privacy and confidentiality?",
                 "Am I including everyone &mdash; all genders, married or not, disabled or not?",
                 "Am I supporting the person's own informed choice?",
                 "Do I know the law and the local referral pathway?"]},
         ]},

        {"type": "content", "label": "Further Reading", "title": "Where to learn more",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>WHO</strong> &mdash; sexual and reproductive health guidance and definitions",
                 "<strong>Guttmacher Institute</strong> &mdash; SRHR research and the Guttmacher&ndash;Lancet definition",
                 "<strong>UNFPA</strong> &mdash; the United Nations sexual and reproductive health agency",
                 "<strong>UNESCO</strong> &mdash; International Technical Guidance on Sexuality Education",
                 "<strong>NFHS &amp; SRS (India)</strong> &mdash; national data on health and fertility"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Gender</strong>, <strong>Public Health</strong> and <strong>Adolescent "
              "Health</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>SRHR is a right</strong> &mdash; rooted in bodily autonomy and dignity",
                 "<strong>Condoms protect twice</strong> &mdash; against pregnancy and STIs/HIV",
                 "<strong>Abortion is legal in India</strong> under the MTP Act (amended 2021)",
                 "<strong>CSE works</strong> &mdash; and does not increase sexual activity",
                 "<strong>Be non-judgemental and inclusive</strong> &mdash; care for everyone"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Sexual Health 101 &middot; Complete",
         "headline": "Care without<br>judgement.",
         "byline": "SRHR is health, dignity and rights for everyone &mdash; whoever they are, "
                   "whatever their choices. Lead with accuracy, respect and inclusion. Explore the "
                   "rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
