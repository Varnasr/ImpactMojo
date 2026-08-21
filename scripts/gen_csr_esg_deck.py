#!/usr/bin/env python3
"""CSR & ESG 101 - Indian statutory CSR first, then sustainability reporting.

India-first by design: Section 135 of the Companies Act 2013 and Schedule VII
are the part that legally binds an Indian company, so they come before GRI or
TCFD. The global frameworks arrive late, as context for BRSR.

Legal thresholds and dates change. Every claim that could go stale carries its
source on the slide, and section 11 tells the learner to check the current
position at mca.gov.in and sebi.gov.in rather than trusting a deck.
"""
import deck_builder as db

slides = []
content = lambda inner: slides.append(('content', inner))
divider = lambda n, l, t: slides.append(('divider', (n, l, t)))

def sec(label, title, body):
    content('<div class="section-label">%s</div><div class="slide-title md">%s</div>%s' % (label, title, body))

def hbox(text, tone='amber'):
    return '<div class="hbox %s"><div class="hbox-text">%s</div></div>' % (tone, text)

def table(headers, rows):
    h = ''.join('<th>%s</th>' % x for x in headers)
    b = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows)
    return '<table class="ctable"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (h, b)

def bullets(items):
    return '<ul class="bullet-list">%s</ul>' % ''.join('<li>%s</li>' % i for i in items)

def stats(cards):
    c = ''.join('<div class="stat-card"><div class="stat-number">%s</div>'
                '<div class="stat-label">%s</div></div>' % (n, l) for n, l in cards)
    return '<div class="stat-grid">%s</div>' % c

def terms(pairs):
    return ''.join('<div class="term-box"><span class="term-word">%s</span>'
                   '<span class="term-def">%s</span></div>' % (w, d) for w, d in pairs)

def quote(text, attr):
    return ('<div class="quote-block"><div class="quote-text">%s</div>'
            '<div class="quote-attr">%s</div></div>' % (text, attr))

def flow(steps):
    out = []
    for i, s in enumerate(steps):
        if i: out.append('<div class="flow-arrow">&rarr;</div>')
        out.append('<div class="flow-step"><div class="flow-num">%02d</div>'
                   '<div class="flow-label">%s</div></div>' % (i + 1, s))
    return '<div class="flow">%s</div>' % ''.join(out)

def twocol(a_title, a_body, b_title, b_body):
    return ('<div class="two-col"><div class="col-panel"><div class="col-panel-title">%s</div>%s</div>'
            '<div class="col-panel"><div class="col-panel-title">%s</div>%s</div></div>'
            % (a_title, a_body, b_title, b_body))

SRC = '<div class="chart-source">%s</div>'

slides.append(('title', None))
TOC = [
    ("Why CSR Is a Statute Here", "3&ndash;9"),
    ("Section 135: Who Is Bound", "10&ndash;18"),
    ("Schedule VII: What Counts", "19&ndash;27"),
    ("The Two Per Cent", "28&ndash;36"),
    ("Governance &amp; the Committee", "37&ndash;44"),
    ("Unspent Money", "45&ndash;53"),
    ("Who May Implement", "54&ndash;61"),
    ("Impact Assessment", "62&ndash;69"),
    ("From CSR to ESG: BRSR", "70&ndash;79"),
    ("Global Frameworks in Context", "80&ndash;88"),
    ("Reading a Report Critically", "89&ndash;98"),
]
slides.append(('toc', None))   # payload filled in below, from real divider positions

# ───────────────────────── 1. Why CSR is a statute here ─────────────────────
divider(1, "Starting Point", "Why CSR is a statute here, not a slogan")

sec("The distinction", "India made CSR a legal duty",
    "<p>In most countries corporate social responsibility is voluntary &mdash; a company "
    "chooses whether to spend, how much, and on what. India took a different route. The "
    "Companies Act 2013 made a minimum spend a statutory obligation for companies above "
    "certain thresholds, with a reporting duty attached.</p>"
    + hbox("This is the single most important thing to understand before anything else: for a "
           "company in scope, CSR here is compliance, not philanthropy. That changes who is "
           "accountable, what gets documented, and what happens when money goes unspent."))

sec("The scale", "What that means in practice",
    stats([("2%", "of average net profit, minimum"),
           ("3", "financial years averaged"),
           ("VII", "the Schedule that lists what counts")])
    + hbox("Every number on this slide is defined precisely in law. Section 4 takes the 2% apart; "
           "Section 3 takes Schedule VII apart. Do not use these figures loosely.", "cyan"))

sec("The vocabulary", "Three words people use interchangeably, wrongly",
    terms([("CSR", "In India, a statutory spending and reporting obligation under Section 135 of the Companies Act 2013. Not a synonym for &lsquo;doing good&rsquo;."),
           ("ESG", "Environmental, Social and Governance &mdash; a disclosure and investment-analysis frame. About what a company reports on itself, largely for investors."),
           ("Sustainability", "The broadest and least precise. Sometimes a synonym for ESG reporting, sometimes an environmental claim, sometimes marketing.")])
    + hbox("If a syllabus, a job advert or a consultant uses these as synonyms, they are describing "
           "three different obligations with three different audiences. Keep them apart."))

sec("Why it happened", "The road to Section 135",
    "<p>Voluntary CSR guidelines came first &mdash; the Ministry of Corporate Affairs issued "
    "them in 2009 and revised them in 2011 as the National Voluntary Guidelines. Uptake was "
    "thin and uneven. The Companies Act 2013 replaced encouragement with obligation.</p>"
    + bullets(["<b>2009</b> &mdash; MCA Corporate Social Responsibility Voluntary Guidelines",
               "<b>2011</b> &mdash; National Voluntary Guidelines on social, environmental and economic responsibilities of business",
               "<b>2013</b> &mdash; Companies Act 2013 passed; Section 135 creates the obligation",
               "<b>2014</b> &mdash; Section 135 and the CSR Rules come into force on 1 April",
               "<b>2021</b> &mdash; Amendment Rules add unspent-money machinery, CSR-1 registration and impact assessment"])
    + SRC % "Ministry of Corporate Affairs; Companies Act 2013.")

sec("The critique", "What the law is accused of",
    twocol("The case for",
           bullets(["Predictable money for the social sector, at scale",
                    "Forces board-level attention rather than a marketing budget line",
                    "Creates a public record that can be audited and challenged"]),
           "The case against",
           bullets(["A tax by another name, without a tax&rsquo;s democratic allocation",
                    "Compliance-driven spending chases what is easy to document",
                    "Crowds out the awkward work &mdash; rights, advocacy, organising &mdash; that Schedule VII does not obviously cover"]))
    + hbox("Both cases are argued seriously. A course that only teaches the mechanics and never "
           "the critique produces compliance officers, not practitioners.", "amber"))

sec("For your syllabus", "What a student should be able to do",
    bullets(["Decide, from a company&rsquo;s financials, whether Section 135 applies to it",
             "Compute the minimum obligation and say which years feed the average",
             "Judge whether a proposed activity falls inside Schedule VII &mdash; and defend the judgement",
             "Trace unspent money to the right account within the right deadline",
             "Read a BRSR filing and say what it does and does not tell you"])
    + hbox("These are the assessable skills. Everything else in this deck exists to support them."))

# ───────────────────────── 2. Section 135: who is bound ─────────────────────
divider(2, "Scope", "Section 135: who is bound, and from when")

sec("The test", "Three thresholds, any one of which binds you",
    "<p>Section 135(1) applies to every company &mdash; including a foreign company&rsquo;s "
    "Indian branch or project office &mdash; that meets <b>any one</b> of these in the "
    "immediately preceding financial year.</p>"
    + table(["Test", "Threshold"],
            [["Net worth", "&ge; &#8377;500 crore"],
             ["Turnover", "&ge; &#8377;1,000 crore"],
             ["Net profit", "&ge; &#8377;5 crore"]])
    + hbox("<b>Any one</b>, not all three. A loss-making company with net worth above &#8377;500 crore "
           "is in scope. This is the single most common error students make.")
    + SRC % "Companies Act 2013, Section 135(1).")

sec("The trap", "&lsquo;Immediately preceding financial year&rsquo;",
    "<p>Scope is tested on the <b>immediately preceding</b> financial year. The spending "
    "obligation is then calculated on the average of the <b>three</b> immediately preceding "
    "financial years. These are two different windows and they are routinely confused.</p>"
    + twocol("Am I in scope?", "<p>Look at <b>one</b> year &mdash; the one just ended.</p>",
             "How much do I owe?", "<p>Average <b>three</b> years of net profit, then take 2%.</p>")
    + hbox("Set this as a exam question. Give a company four years of figures and ask for both "
           "answers. The students who have understood it will use different rows for each.", "cyan"))

sec("Exit", "Falling out of scope",
    "<p>A company that ceases to meet the thresholds is not bound forever. Where a company "
    "no longer meets the criteria for three consecutive financial years, it is not required "
    "to constitute a CSR Committee, and the obligation lapses until it re-enters scope.</p>"
    + hbox("Entry is immediate; exit takes three years. The asymmetry is deliberate &mdash; it "
           "stops a company from dipping below a threshold for one year to avoid a spend.")
    + SRC % "Companies Act 2013, Section 135(9) and the CSR Rules.")

sec("Foreign companies", "Branches and project offices are covered",
    "<p>A foreign company with a branch or project office in India is in scope if it meets "
    "the thresholds. Net worth, turnover and net profit are computed from the balance sheet "
    "and profit-and-loss account prepared under Section 381(1)(a) of the Act.</p>"
    + hbox("Students at business schools often assume CSR is a domestic-company rule. It is not.")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 3.")

sec("Net profit", "Which profit figure the Act means",
    "<p>&lsquo;Net profit&rsquo; for CSR is <b>not</b> the headline profit-after-tax in a press "
    "release. It is net profit computed under Section 198, with specific adjustments &mdash; "
    "and the CSR Rules further exclude:</p>"
    + bullets(["Any profit arising from overseas branches of the company, whether operated as a separate company or otherwise",
               "Any dividend received from other companies in India which are themselves covered by and complying with Section 135"])
    + hbox("The second exclusion prevents the same rupee of profit generating a CSR obligation "
           "twice as it moves up a group structure.")
    + SRC % "Companies Act 2013, Sections 135 and 198; Companies (CSR Policy) Rules 2014.")

sec("Worked example", "Does Section 135 apply?",
    table(["Company", "Net worth", "Turnover", "Net profit", "In scope?"],
          [["Alpha Ltd", "&#8377;620 cr", "&#8377;300 cr", "&#8377;2 cr", "<b>Yes</b> &mdash; net worth"],
           ["Beta Ltd", "&#8377;90 cr", "&#8377;1,240 cr", "Loss", "<b>Yes</b> &mdash; turnover"],
           ["Gamma Ltd", "&#8377;110 cr", "&#8377;400 cr", "&#8377;6 cr", "<b>Yes</b> &mdash; net profit"],
           ["Delta Ltd", "&#8377;80 cr", "&#8377;300 cr", "&#8377;3 cr", "No &mdash; none met"]])
    + hbox("Beta is the instructive one. It made a loss and is still in scope, because turnover "
           "crossed the line. Its obligation, however, is computed on average net profit &mdash; "
           "which may be nil. In scope is not the same as owing money."))

sec("Set this as work", "A classroom exercise",
    "<p>Hand students the published annual report of any listed Indian company and ask three "
    "questions:</p>"
    + bullets(["Which threshold, if any, brings it into scope &mdash; and in which year?",
               "What is its prescribed CSR expenditure for the year just ended?",
               "Does the CSR note in the report agree with your figure? If not, why not?"])
    + hbox("The third question is where the learning is. Published figures and student "
           "calculations diverge for real reasons &mdash; Section 198 adjustments, overseas "
           "branch profits &mdash; and chasing the difference teaches the section properly.", "cyan"))

# ───────────────────────── 3. Schedule VII ──────────────────────────────────
divider(3, "Eligibility", "Schedule VII: what actually counts")

sec("The list", "Schedule VII in outline",
    "<p>Schedule VII lists the activities a company may include in its CSR policy. It is the "
    "gate: spending outside it is not CSR expenditure, however worthy.</p>"
    + bullets(["Eradicating hunger, poverty and malnutrition; promoting health care including preventive health care; sanitation; safe drinking water",
               "Promoting education, including special education and employment-enhancing vocational skills; livelihood enhancement projects",
               "Promoting gender equality; empowering women; homes and hostels for women and orphans; old age homes; reducing inequalities faced by socially and economically backward groups",
               "Environmental sustainability; ecological balance; conservation of natural resources; animal welfare; agroforestry",
               "Protection of national heritage, art and culture; public libraries; traditional arts and handicrafts",
               "Measures for the benefit of armed forces veterans, war widows and their dependants",
               "Training to promote rural, nationally recognised, Paralympic or Olympic sports",
               "Contribution to specified government funds",
               "Contributions to incubators and to specified research and development bodies",
               "Rural development projects; slum area development; disaster management including relief, rehabilitation and reconstruction"])
    + SRC % "Companies Act 2013, Schedule VII. Paraphrased in outline &mdash; read the Schedule itself before advising anyone.")

sec("Read it liberally", "The MCA&rsquo;s own instruction",
    "<p>The Ministry of Corporate Affairs has repeatedly clarified that the entries in "
    "Schedule VII are to be interpreted <b>liberally</b>, so as to capture the essence of the "
    "subjects listed, rather than read as a narrow closed list.</p>"
    + hbox("This matters for teaching. A student who treats Schedule VII as ten rigid boxes will "
           "wrongly reject sound projects. One who treats it as infinitely elastic will wrongly "
           "approve anything. The skill is arguing the boundary.")
    + SRC % "MCA General Circulars and the CSR FAQ series.")

sec("What is excluded", "The exclusions that catch people out",
    table(["Excluded", "Why"],
          [["Activities outside India", "With a narrow exception for training Indian sports personnel representing a State or India"],
           ["Activities benefiting only employees and their families", "CSR is directed outward; staff welfare is not CSR"],
           ["Contribution to any political party", "Expressly excluded &mdash; directly or indirectly"],
           ["Activities in the normal course of business", "With a time-limited exception created for certain COVID-19 vaccine R&amp;D"],
           ["Sponsorship for marketing benefit", "If the company derives marketing benefit, it is advertising, not CSR"],
           ["Fulfilling another statutory obligation", "Money you were already legally required to spend cannot be counted twice"]])
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 2(1)(d).")

sec("The hard cases", "Where reasonable people disagree",
    twocol("Probably CSR",
           bullets(["A skilling programme open to the wider community, run near a plant",
                    "Restoring a water body the company does not own",
                    "Funding a school the company&rsquo;s employees&rsquo; children may also attend, alongside others"]),
           "Probably not CSR",
           bullets(["A skilling programme that only feeds the company&rsquo;s own hiring pipeline",
                    "Effluent treatment the company is required to do anyway",
                    "A crèche for employees only &mdash; and in some cases already a statutory duty"]))
    + hbox("Notice the pattern. The question is rarely &lsquo;is this good?&rsquo; It is &lsquo;who "
           "is the beneficiary, and would this have been spent regardless?&rsquo;", "amber"))

sec("Set this as work", "The Schedule VII boundary exercise",
    "<p>Give students six proposed projects, three clearly inside the Schedule, three on the "
    "boundary. Ask each student to rule on all six <b>and write the reasoning</b>, then to "
    "argue a partner&rsquo;s boundary case the other way.</p>"
    + hbox("Mark the reasoning, not the verdict. On a genuine boundary case, either answer can be "
           "defensible; only one of them can be well argued.", "cyan"))

# ───────────────────────── 4. The two per cent ──────────────────────────────
divider(4, "The Money", "The two per cent, and how it is computed")

sec("The formula", "Prescribed CSR expenditure",
    "<p>The board must ensure the company spends, in every financial year, at least "
    "<b>two per cent of the average net profit</b> made during the three immediately "
    "preceding financial years.</p>"
    + flow(["Take net profit under s.198 for each of 3 years", "Average them",
            "Multiply by 2%", "That is the minimum spend"])
    + hbox("Where a company has not completed three financial years, the average is taken over "
           "such preceding financial years as it has completed.")
    + SRC % "Companies Act 2013, Section 135(5).")

sec("Worked example", "Computing the obligation",
    table(["Financial year", "Net profit (s.198)"],
          [["FY 2023&ndash;24", "&#8377;40 crore"],
           ["FY 2024&ndash;25", "&#8377;70 crore"],
           ["FY 2025&ndash;26", "&#8377;10 crore"],
           ["<b>Average</b>", "<b>&#8377;40 crore</b>"],
           ["<b>2% obligation for FY 2026&ndash;27</b>", "<b>&#8377;80 lakh</b>"]])
    + hbox("The averaging is what makes this survive a bad year. A company that collapses to "
           "&#8377;10 crore of profit still owes on a &#8377;40 crore average &mdash; and a company "
           "having a spectacular year does not owe on it until the average catches up."))

sec("A loss-making year", "Zero profit is not zero obligation",
    "<p>Because the base is a three-year average, a single loss-making year does not "
    "extinguish the obligation. Equally, a company can be <b>in scope</b> on turnover or net "
    "worth while its three-year average net profit is nil &mdash; in which case the "
    "prescribed expenditure is nil, but the reporting duty remains.</p>"
    + hbox("Teach the two branches separately: <b>in scope</b> triggers governance and reporting; "
           "<b>average net profit</b> sets the amount. They can move independently.", "cyan"))

sec("Surplus", "CSR cannot make money",
    "<p>Any surplus arising out of CSR activities does not form part of the business profit "
    "of the company. It must be ploughed back into the same project, or transferred to the "
    "Unspent CSR Account and spent, or transferred to a fund specified in Schedule VII.</p>"
    + hbox("This closes a route by which a &lsquo;CSR&rsquo; project could quietly become a revenue line.")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 7(2).")

sec("Set-off", "Spending more than you owe",
    "<p>Where a company spends more than its obligation in a financial year, that excess may "
    "be set off against the requirement for succeeding financial years, subject to conditions "
    "set out in the Rules &mdash; including board approval and limits on how far forward the "
    "set-off may be carried.</p>"
    + hbox("Check the current text of Rule 7 before advising on set-off. The mechanism has been "
           "amended since it was introduced and the conditions are specific.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 7(3).")

sec("Capital assets", "Who may own what CSR money builds",
    "<p>CSR spend may create or acquire a capital asset, but the asset may not simply sit on "
    "the company&rsquo;s balance sheet. It must be held by a Section 8 company or a registered "
    "trust or society with an established track record, or by the beneficiaries themselves as "
    "a self-help group or collective, or by a public authority.</p>"
    + hbox("A school building that remains the company&rsquo;s property is a corporate asset, not "
           "CSR. The ownership rule is what makes the spend irreversible.")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 7(4).")

sec("Administrative overheads", "The five per cent cap",
    "<p>Administrative overheads &mdash; the company&rsquo;s own expenses of managing and "
    "administering its CSR functions &mdash; may not exceed <b>five per cent</b> of total CSR "
    "expenditure for the financial year.</p>"
    + hbox("This is the company&rsquo;s own overhead, not the implementing partner&rsquo;s "
           "programme delivery cost. Conflating the two is a common and expensive mistake, and "
           "it is why some NGOs are told their overheads are &lsquo;capped at 5%&rsquo; when the "
           "rule says nothing of the sort.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 7(1).")

sec("Set this as work", "The overheads argument",
    "<p>Ask students to find a real CSR partnership where an NGO was told its "
    "administrative costs must fit within 5%, and write a one-page note to the company "
    "explaining what Rule 7(1) actually caps.</p>"
    + hbox("This is a real and recurring dispute in the Indian social sector. Students who can "
           "argue it precisely become useful to their future employers immediately.", "cyan"))

# ───────────────────────── 5. Governance ────────────────────────────────────
divider(5, "Governance", "The Committee, the policy and the board")

sec("The Committee", "Who must constitute one",
    "<p>A company in scope must constitute a CSR Committee of the Board, consisting of "
    "<b>three or more directors</b>, of which at least one must be an independent director.</p>"
    + bullets(["A company not required to appoint an independent director constitutes its Committee with two or more directors",
               "Where the amount to be spent does not exceed &#8377;50 lakh, the requirement to constitute a Committee does not apply, and the Board discharges its functions"])
    + SRC % "Companies Act 2013, Section 135(1) and 135(9), as amended by the Companies (Amendment) Act 2020.")

sec("What the Committee does", "Three statutory functions",
    flow(["Formulate and recommend the CSR Policy",
          "Recommend the amount of expenditure",
          "Monitor the Policy from time to time"])
    + hbox("Notice what is absent: the Committee does not choose projects in the sense of "
           "day-to-day selection, and it does not implement. It sets policy and watches."))

sec("The Board&rsquo;s duties", "Where accountability actually sits",
    bullets(["Approve the CSR Policy and disclose its contents in the Board&rsquo;s report and on the website",
             "Ensure the activities in the Policy are actually undertaken",
             "Ensure the company spends the prescribed amount",
             "Satisfy itself that the funds disbursed have been utilised for the purposes and in the manner approved &mdash; with the CFO certifying this",
             "Where the amount is not spent, give the reason in the Board&rsquo;s report"])
    + hbox("The CFO certification is the teeth. It converts a governance aspiration into a named "
           "officer&rsquo;s signature.")
    + SRC % "Companies Act 2013, Section 135; Companies (CSR Policy) Rules 2014, Rule 4(5).")

sec("The annual action plan", "What the Committee must formulate",
    bullets(["The list of CSR projects or programmes approved, within Schedule VII",
             "The manner of execution",
             "The modalities of utilisation of funds and implementation schedules",
             "Monitoring and reporting mechanism",
             "Details of need and impact assessment, if any, for the projects"])
    + hbox("The Board may alter the plan at any time during the financial year, on the "
           "Committee&rsquo;s recommendation, based on reasonable justification.")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 5(2).")

sec("Disclosure", "What must be public",
    "<p>The Board&rsquo;s report must include an annual report on CSR containing the "
    "particulars specified in the Rules, and the company must disclose the composition of the "
    "CSR Committee, the CSR Policy and the projects approved <b>on its website</b>.</p>"
    + hbox("The website duty is what makes classroom research possible. Any listed Indian company "
           "of size has this material published; students can read the real thing rather than a "
           "textbook summary.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 9.")

sec("Set this as work", "Reading a real CSR policy",
    "<p>Assign each student a different company. Ask them to find, on the company&rsquo;s own "
    "website: the CSR Policy, the Committee composition, and the annual CSR report. Then:</p>"
    + bullets(["Does the Committee meet the statutory composition?",
               "Does the annual action plan name projects, or only themes?",
               "Can you trace a rupee from the prescribed amount to a named project?"])
    + hbox("Most students find they cannot answer the third question from public documents. That "
           "finding <b>is</b> the result, and it is the beginning of the accountability critique."))

# ───────────────────────── 6. Unspent money ─────────────────────────────────
divider(6, "Unspent", "What happens to money you did not spend")

sec("The 2021 change", "Unspent CSR stopped being a footnote",
    "<p>Before 2021, a company that failed to spend explained itself in the Board&rsquo;s "
    "report and that was largely the end of it. The Companies (Amendment) Act 2019 and the "
    "CSR Amendment Rules 2021 replaced &lsquo;comply or explain&rsquo; with a transfer "
    "obligation and deadlines.</p>"
    + hbox("This is the most consequential amendment to the CSR regime since it began. If your "
           "reference material predates 2021, its treatment of unspent money is wrong."))

sec("The fork", "Ongoing project, or not",
    twocol("Ongoing project",
           "<p>Transfer the unspent amount to a special account &mdash; the <b>Unspent CSR "
           "Account</b> &mdash; within <b>30 days</b> of the end of the financial year. Spend it "
           "within <b>three</b> financial years.</p>",
           "Not an ongoing project",
           "<p>Transfer the unspent amount to a fund specified in <b>Schedule VII</b> within "
           "<b>six months</b> of the end of the financial year.</p>")
    + hbox("Everything turns on whether the project is &lsquo;ongoing&rsquo;. That word is defined, "
           "and the definition is on the next slide.", "amber")
    + SRC % "Companies Act 2013, Section 135(5) and 135(6).")

sec("Ongoing project", "The definition matters",
    "<p>An <b>ongoing project</b> means a multi-year project undertaken by a company in "
    "fulfilment of its CSR obligation, having a timeline <b>not exceeding three years</b> "
    "excluding the financial year in which it was commenced. It includes a project that was "
    "initially not approved as multi-year but whose duration is extended beyond one year by "
    "the Board on reasonable justification.</p>"
    + hbox("Three years, excluding the commencement year. Students routinely drop the exclusion "
           "and get the arithmetic wrong.")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 2(1)(i).")

sec("If you still do not spend it", "The three-year backstop",
    "<p>Money sitting in the Unspent CSR Account that is not spent within three financial "
    "years must be transferred to a fund specified in Schedule VII within <b>30 days</b> from "
    "the end of the third financial year.</p>"
    + flow(["FY ends unspent", "&rarr; Unspent CSR A/c in 30 days",
            "3 years to spend", "Still unspent &rarr; Schedule VII fund in 30 days"])
    + SRC % "Companies Act 2013, Section 135(6).")

sec("The funds", "Where unspent money goes",
    bullets(["Prime Minister&rsquo;s National Relief Fund",
             "PM CARES Fund",
             "Clean Ganga Fund",
             "Swachh Bharat Kosh",
             "Any other fund set up by the Central Government as specified in Schedule VII"])
    + hbox("Note what this means politically: money a company failed to direct locally is "
           "redirected centrally. Whether that is a feature or a defect is a live argument, and "
           "worth putting to students.", "cyan"))

sec("Penalties", "It is now an enforceable default",
    "<p>Failure to comply with the transfer obligations attracts penalties on the company and "
    "on officers in default, as set out in Section 135(7). The Companies (Amendment) Act 2020 "
    "converted the regime from criminal to civil penalty.</p>"
    + hbox("Penalty amounts have been amended and are capped by formula. Read the current "
           "Section 135(7) before quoting a figure &mdash; a stale number in a compliance note is "
           "worse than no number.", "amber")
    + SRC % "Companies Act 2013, Section 135(7).")

sec("Set this as work", "The unspent-money decision tree",
    "<p>Give students four scenarios and ask for the destination account and the deadline in "
    "each: a two-year skilling project half spent; a one-off disaster relief grant unspent; "
    "a project extended by the Board from one year to two; money still sitting in an Unspent "
    "CSR Account after three years.</p>"
    + hbox("Ask for the <b>date</b>, not the rule. Forcing a calendar date exposes whether the "
           "student has understood &lsquo;excluding the year of commencement&rsquo;.", "cyan"))

# ───────────────────────── 7. Implementation ────────────────────────────────
divider(7, "Delivery", "Who may actually implement")

sec("The routes", "Four ways a company may deliver CSR",
    bullets(["<b>Itself</b> &mdash; directly, through its own teams",
             "<b>Its own foundation</b> &mdash; a Section 8 company, registered trust or society established by the company, alone or with others",
             "<b>A government entity</b> &mdash; established under an Act of Parliament or a State legislature",
             "<b>An external organisation</b> &mdash; a Section 8 company, registered public trust or registered society with an established track record of at least three years"])
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(1).")

sec("CSR-1", "Registration became mandatory",
    "<p>From <b>1 April 2021</b>, an entity intending to undertake CSR activities on behalf "
    "of a company must register itself with the Central Government by filing <b>Form CSR-1</b> "
    "electronically with the Registrar, and obtain a CSR Registration Number.</p>"
    + hbox("For NGOs this is the practical gate. No CSR-1, no corporate money &mdash; regardless of "
           "how good the organisation is or how long it has worked.")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(2).")

sec("What CSR-1 requires", "In outline",
    bullets(["Registration under Section 12A and 80G of the Income-tax Act 1961, where applicable",
             "Details of the entity &mdash; Section 8 company, registered trust or registered society",
             "Governing body details and PAN",
             "Digital signature of an authorised person and certification by a practising professional"])
    + hbox("Check the current form and its attachments on the MCA portal before advising an "
           "organisation. Requirements have been revised.", "amber"))

sec("The three-year track record", "What it excludes",
    "<p>An external implementing organisation must have an <b>established track record of at "
    "least three years</b> in undertaking similar activities. An entity established by the "
    "company itself does not face this requirement.</p>"
    + hbox("This is a real barrier to new and community-rooted organisations, and a real "
           "safeguard against shell intermediaries. It does both things at once; say so in class "
           "rather than presenting only one side.", "cyan"))

sec("Monitoring the money", "The company cannot outsource responsibility",
    "<p>The Board must satisfy itself that funds disbursed have been utilised for the purposes "
    "and in the manner approved, and the Chief Financial Officer or the person responsible for "
    "financial management must certify to that effect.</p>"
    + hbox("For an implementing NGO this translates into utilisation certificates, documented "
           "beneficiary records and audit trails. Teach students to design these <b>at proposal "
           "stage</b>, not at year end.")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(5).")

sec("Collaboration", "Companies may pool",
    "<p>A company may collaborate with other companies for undertaking projects, provided the "
    "CSR Committees of each are in a position to report separately on those projects in "
    "accordance with the Rules.</p>"
    + hbox("Pooling is how small obligations reach a scale worth designing for. The reporting "
           "condition is what stops it becoming a black box.")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(4).")

sec("Set this as work", "The NGO readiness audit",
    "<p>Ask students to take a real local NGO &mdash; ideally one they know &mdash; and produce "
    "a one-page readiness assessment for receiving CSR funds:</p>"
    + bullets(["Is it a Section 8 company, registered trust or registered society?",
               "Does it have three years of track record in the relevant activity?",
               "Is it CSR-1 registered? If not, what does it need first?",
               "Could it produce a utilisation certificate that would satisfy a CFO?"])
    + hbox("This is the single most employable exercise in the deck. Students who can do it are "
           "immediately useful to any NGO seeking corporate funding.", "cyan"))

# ───────────────────────── 8. Impact assessment ─────────────────────────────
divider(8, "Evidence", "Impact assessment: where CSR meets M&amp;E")

sec("When it is mandatory", "The two thresholds",
    "<p>A company must undertake impact assessment through an independent agency where it "
    "meets <b>both</b> limbs:</p>"
    + table(["Limb", "Threshold"],
            [["Company&rsquo;s average CSR obligation", "&ge; &#8377;10 crore in the three immediately preceding financial years"],
             ["The project", "Outlay &ge; &#8377;1 crore, and completed not less than one year before undertaking the study"]])
    + hbox("Both limbs. A large company&rsquo;s small project is out; a small company&rsquo;s large "
           "project is out.")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 8(3).")

sec("What it costs", "The assessment is chargeable to CSR",
    "<p>Impact assessment expenditure may be booked to CSR for that financial year, subject "
    "to a cap set out in the Rules &mdash; expressed as a percentage of total CSR expenditure "
    "or an absolute figure, whichever is higher.</p>"
    + hbox("Check the current cap in Rule 8(3)(c); it has been amended. The principle &mdash; that "
           "evaluation is fundable from the CSR budget rather than an unfunded extra &mdash; has "
           "not changed.", "amber"))

sec("Independent agency", "What independence means here",
    "<p>The Rules require an <b>independent agency</b>. They do not prescribe a methodology, a "
    "qualification or an accreditation. In practice this is a real weakness and a real "
    "opportunity.</p>"
    + twocol("The weakness",
             bullets(["No methodological floor",
                      "The company selects and pays the evaluator",
                      "Reports vary from serious evaluation to extended brochure"]),
             "The opportunity",
             bullets(["A genuine market for evaluation skills in India",
                      "Nothing stops a company commissioning a rigorous design",
                      "Your students can be the people who do it properly"]))
    + hbox("This is exactly the seam where a CSR course and an M&amp;E course meet. If you teach "
           "both, teach them together here.", "cyan"))

sec("What a good assessment does", "Beyond counting outputs",
    bullets(["States the theory of change the project was built on, and tests it",
             "Distinguishes outputs from outcomes, and says which it can evidence",
             "Is explicit about attribution &mdash; what would have happened anyway",
             "Reports what did not work, not only what did",
             "Names its limitations, sample and period"])
    + hbox("A report with no negative findings and no stated limitations is not an evaluation. "
           "Teach students to say so politely and in writing."))

sec("Attribution", "The question CSR reports usually dodge",
    "<p>A CSR report will say a programme reached 40,000 people. The evaluation question is "
    "different: <b>what changed that would not have changed anyway?</b></p>"
    + quote("Reach is an output. Change is an outcome. Attribution is a claim about causation "
            "&mdash; and it needs a comparison, not a headcount.",
            "The distinction every impact assessment stands or falls on")
    + hbox("If you teach M&amp;E alongside this, the ImpactMojo studios on Theory of Change and "
           "Impact Evaluation let students build and defend the comparison design.", "cyan"))

sec("Where it is published", "The annexure",
    "<p>The impact assessment report must be placed before the Board and annexed to the "
    "annual report on CSR.</p>"
    + hbox("Which means it is public. Students can and should read real ones &mdash; and the "
           "variation in quality between them is itself a teaching object.")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 8(3)(b).")

sec("Set this as work", "Critique a real impact assessment",
    "<p>Find a published CSR impact assessment for any large Indian company. Ask students to "
    "mark it against five questions:</p>"
    + bullets(["Is there a stated theory of change?",
               "Are outputs and outcomes distinguished?",
               "Is there any comparison group, or any counterfactual reasoning at all?",
               "Are limitations stated?",
               "Would you, as the board, change anything after reading it?"])
    + hbox("Marks for the reasoning, not the verdict. Most published assessments score poorly on "
           "questions three and four; the point is for students to be able to say <i>why</i>, "
           "precisely, and to propose a better design."))

# ───────────────────────── 9. BRSR ──────────────────────────────────────────
divider(9, "Reporting", "From CSR to ESG: the BRSR")

sec("The shift", "Different obligation, different audience",
    "<p>CSR under Section 135 asks: <i>did you spend, and on what?</i> ESG reporting asks a "
    "different question: <i>how does your business behave, and what does it cost the world?</i> "
    "The audience shifts from the regulator to the investor.</p>"
    + table(["", "Section 135 CSR", "BRSR / ESG"],
            [["Governs", "A spending obligation", "A disclosure obligation"],
             ["Scope", "The CSR budget", "The whole business"],
             ["Audience", "MCA, the board, the public", "Investors, analysts, regulators"],
             ["Applies to", "Companies over Section 135 thresholds", "Top listed companies by market capitalisation"]])
    + hbox("A company can spend its 2% impeccably and still have a poor ESG profile, because the "
           "2% is not where the harm is. This is the most important idea in the section."))

sec("BRSR", "What it is",
    "<p>The <b>Business Responsibility and Sustainability Report</b> is SEBI&rsquo;s mandatory "
    "ESG disclosure format, replacing the earlier Business Responsibility Report. It applies "
    "to the top <b>1,000</b> listed entities by market capitalisation, mandatory from "
    "<b>FY 2022&ndash;23</b>.</p>"
    + hbox("Applicability has expanded since introduction, including a &lsquo;BRSR Core&rsquo; "
           "subset with assurance requirements phased in by market-cap rank. Confirm the current "
           "position on sebi.gov.in before teaching the thresholds as settled.", "amber")
    + SRC % "SEBI (LODR) Regulations; SEBI circulars on BRSR.")

sec("NGRBC", "The nine principles underneath",
    "<p>BRSR is structured on the <b>National Guidelines on Responsible Business Conduct</b>. "
    "Businesses should:</p>"
    + bullets(["Conduct themselves with integrity, ethics, transparency and accountability",
               "Provide goods and services in a safe and sustainable manner",
               "Respect and promote the wellbeing of all employees, including those in value chains",
               "Respect the interests of and be responsive to all stakeholders",
               "Respect and promote human rights",
               "Protect and restore the environment",
               "Engage in policy advocacy responsibly and transparently",
               "Promote inclusive growth and equitable development",
               "Engage with and provide value to consumers responsibly"])
    + SRC % "Ministry of Corporate Affairs, National Guidelines on Responsible Business Conduct, 2019.")

sec("The structure", "How a BRSR is laid out",
    flow(["Section A: General disclosures", "Section B: Management &amp; process",
          "Section C: Principle-wise performance"])
    + bullets(["<b>Section A</b> &mdash; entity details, products, employees, CSR, transparency",
               "<b>Section B</b> &mdash; policies against each of the nine principles, and governance of them",
               "<b>Section C</b> &mdash; essential and leadership indicators for each principle"])
    + hbox("The essential/leadership split matters: essential indicators are mandatory, leadership "
           "indicators are voluntary. A company reporting only essential indicators is complying, "
           "not leading &mdash; and the format lets you see which.", "cyan"))

sec("BRSR Core", "Assurance arrives",
    "<p>SEBI introduced a <b>BRSR Core</b> &mdash; a defined subset of key performance "
    "indicators requiring <b>reasonable assurance</b>, phased in by market-capitalisation "
    "rank, with disclosures extending to the value chain.</p>"
    + hbox("Assurance is the difference between a company saying a number and a third party "
           "standing behind it. When you read any ESG claim, the first question is whether it is "
           "assured, and to what level.")
    + SRC % "SEBI circulars on BRSR Core. Verify the current phase-in schedule.")

sec("Greenwashing", "What the format is designed to resist",
    twocol("The tells",
           bullets(["Targets with no baseline",
                    "Intensity metrics only, never absolutes",
                    "Scope 1 and 2 emissions reported, Scope 3 omitted",
                    "&lsquo;Committed to&rsquo; and &lsquo;aim to&rsquo; without a date"]),
           "The checks",
           bullets(["Is the figure assured, and at what level?",
                    "Is the boundary stated &mdash; which entities are included?",
                    "Is last year&rsquo;s figure restated, and why?",
                    "Does the narrative match the numbers?"]))
    + hbox("Teach the tells as a checklist. They transfer directly to any sustainability report a "
           "student will ever read, Indian or not.", "amber"))

sec("Set this as work", "Read one BRSR properly",
    "<p>Assign one BRSR filing per student, from companies in different sectors. Ask for a "
    "two-page note answering:</p>"
    + bullets(["Which leadership indicators did they answer, and which did they skip?",
               "Is any figure assured? At what level?",
               "Find one number that contradicts a claim in the narrative",
               "What does the CSR section tell you that Section 135 filings do not?"])
    + hbox("The third question is the real assignment. Contradictions are common, and finding one "
           "converts a student from a reader of reports into an analyst of them.", "cyan"))

# ───────────────────────── 10. Global frameworks ────────────────────────────
divider(10, "Context", "The global frameworks, and where India sits")

sec("The landscape", "Why there are so many",
    "<p>ESG reporting grew from voluntary initiatives rather than a single regulator, so the "
    "field arrived crowded. Consolidation is underway but incomplete.</p>"
    + table(["Framework", "Focus", "Audience"],
            [["GRI", "Impact of the company on the world", "All stakeholders"],
             ["SASB", "Financially material sustainability issues, by industry", "Investors"],
             ["TCFD", "Climate-related financial risk and governance", "Investors, regulators"],
             ["ISSB (IFRS S1, S2)", "Global baseline for sustainability and climate disclosure", "Capital markets"],
             ["CSRD / ESRS", "Mandatory EU sustainability reporting", "EU regulators, investors"]])
    + SRC % "Framework bodies&rsquo; own documentation. Consolidation is active &mdash; confirm the current position.")

sec("Double materiality", "The idea that divides the field",
    twocol("Financial materiality",
           "<p>What sustainability issues affect the <b>company&rsquo;s</b> value? Used by SASB "
           "and ISSB. The question an investor asks.</p>",
           "Impact materiality",
           "<p>What effects does the company have on <b>people and the environment</b>? Used by "
           "GRI. The question a community asks.</p>")
    + hbox("<b>Double materiality</b> &mdash; the EU&rsquo;s CSRD position &mdash; requires both. "
           "Which materiality a framework adopts tells you who it was written for, and it is the "
           "fastest way to read the politics of any reporting standard.", "cyan"))

sec("Where BRSR sits", "India&rsquo;s position",
    "<p>BRSR is built on the NGRBC principles and covers both business conduct and "
    "environmental performance, so it sits closer to a broad-stakeholder view than to a purely "
    "investor-financial one &mdash; while BRSR Core&rsquo;s assured KPIs and value-chain reach "
    "move it toward investor-grade comparability.</p>"
    + hbox("Teach BRSR as India&rsquo;s own instrument, not as a local copy of something else. "
           "Students who understand NGRBC can read GRI quickly; the reverse is less true."))

sec("The SDGs", "Useful frame, weak accountability",
    "<p>Companies routinely map CSR and ESG activity to the Sustainable Development Goals. "
    "The mapping is genuinely useful for communication and genuinely weak as accountability: "
    "the SDGs were written for states, have no corporate reporting requirement, and almost "
    "any activity can be mapped to at least one goal.</p>"
    + hbox("When a report claims to advance eight SDGs, ask which indicator, at which target, "
           "moved by how much. The answer is usually silence.", "amber"))

sec("Human rights", "The framework CSR discussions often skip",
    "<p>The <b>UN Guiding Principles on Business and Human Rights</b> set out a duty to "
    "protect, a corporate responsibility to respect, and access to remedy &mdash; with human "
    "rights due diligence at the centre. NGRBC Principle 5 carries this into the Indian frame.</p>"
    + hbox("This is the part of ESG closest to social work practice, and the part most often "
           "left out of business-school CSR teaching. If your students come from a social work "
           "background, it is where they will have the most to say.", "cyan")
    + SRC % "UN Guiding Principles on Business and Human Rights, 2011.")

sec("Value chains", "Where the harm usually is",
    "<p>A company&rsquo;s own operations are rarely where its worst impacts sit. They sit in "
    "the value chain &mdash; suppliers, contractors, informal labour. Scope 3 emissions, "
    "supplier labour conditions and contract-worker safety are where reporting is thinnest and "
    "the stakes are highest.</p>"
    + hbox("In India this connects directly to informal employment, contract labour and migrant "
           "work. A course that stops at the company gate misses the majority of the workforce "
           "involved in producing the goods."))

sec("Set this as work", "Map a company both ways",
    "<p>Take one company. Ask students to list its five most significant sustainability issues "
    "twice &mdash; once by <b>financial</b> materiality, once by <b>impact</b> materiality &mdash; "
    "and then to explain each difference between the lists.</p>"
    + hbox("The gap between the two lists is the argument of the entire field, made concrete on "
           "one company in one class.", "cyan"))

# ───────────────────────── 11. Reading critically ───────────────────────────
divider(11, "Practice", "Reading a report critically, and keeping current")

sec("The core skill", "Everything reduces to this",
    "<p>Your students will not spend careers drafting Section 135 policies. They will read "
    "reports written by people with an interest in how they read, and decide what to "
    "believe.</p>"
    + quote("A report is a claim, made by an interested party, in a format that party helped "
            "design. Read it as evidence, not as testimony.",
            "The disposition this whole course is trying to build"))

sec("Ten questions", "A checklist for any CSR or ESG report",
    bullets(["What is the reporting boundary &mdash; which entities are in?",
             "Is the prescribed CSR amount stated, and does the arithmetic work?",
             "Is any amount unspent, and where did it go?",
             "Are projects named, or only themes?",
             "Who implemented, and are they CSR-1 registered?",
             "Is there an impact assessment, and does it have a counterfactual?",
             "Are ESG figures assured &mdash; and reasonable or limited assurance?",
             "Are targets given a baseline and a date?",
             "Are Scope 3 emissions reported or omitted?",
             "Does anything in the numbers contradict the narrative?"])
    + hbox("Print this. It is the single most transferable artefact in the deck.", "cyan"))

sec("Common failures", "What weak reports look like",
    twocol("In CSR reporting",
           bullets(["Beneficiary counts with no definition of &lsquo;reached&rsquo;",
                    "Themes instead of projects",
                    "Administrative overheads confused with partner delivery costs",
                    "Unspent money explained but not traced"]),
           "In ESG reporting",
           bullets(["Intensity metrics hiding absolute growth",
                    "Restated baselines with no explanation",
                    "Leadership indicators skipped without comment",
                    "&lsquo;Net zero by 2070&rsquo; with no interim milestone"]))
    + hbox("Both columns describe reports that comply fully with the law. Compliance and candour "
           "are different properties.", "amber"))

sec("Keeping current", "This area changes, and stale advice is dangerous",
    "<p>Thresholds, deadlines, forms, penalty amounts and BRSR applicability have all been "
    "amended since 2014, several times. Do not teach any figure in this deck as permanent.</p>"
    + bullets(["<b>mca.gov.in</b> &mdash; the Companies Act, the CSR Rules, circulars and the CSR FAQ",
               "<b>csr.gov.in</b> &mdash; the national CSR data portal, with company-level spending data",
               "<b>sebi.gov.in</b> &mdash; LODR regulations and BRSR circulars",
               "The company&rsquo;s own website &mdash; policy, committee composition and annual CSR report are all required to be public"])
    + hbox("Teach students to check the primary source themselves. It is a five-minute habit that "
           "outlasts everything else in this course."))

sec("csr.gov.in", "A dataset, not just a portal",
    "<p>The national CSR portal publishes company-level CSR spending, by year, sector and "
    "state. It is a genuine dataset and it is open.</p>"
    + bullets(["Which sectors attract the most CSR money &mdash; and which almost none?",
               "How is spending distributed across states? Does it follow need, or follow head offices?",
               "Which companies report large obligations and small spends?"])
    + hbox("These are real research questions with public data behind them. They make good "
           "dissertations and better classroom arguments than any case study.", "cyan"))

sec("The honest summary", "What this course can and cannot settle",
    twocol("Settled",
           bullets(["Who is in scope, and how the 2% is computed",
                    "What Schedule VII covers",
                    "Where unspent money must go, and by when",
                    "What a BRSR contains"]),
           "Contested",
           bullets(["Whether mandated CSR is good policy at all",
                    "Whether Schedule VII&rsquo;s boundaries are the right ones",
                    "Whether impact assessment as practised is evaluation",
                    "Whether ESG disclosure changes corporate behaviour"]))
    + hbox("Teach the left column as fact and the right column as argument. Students who cannot "
           "tell which is which will be badly served by this field."))

sec("Going further", "Where to take this next",
    bullets(["<b>Development Architecture 101</b> &mdash; how development funding is structured, including CSR flows",
             "<b>Climate Essentials 101</b> &mdash; the climate science and policy behind the E in ESG",
             "<b>MEL for Development</b> &mdash; the flagship, for the evaluation half of impact assessment",
             "<b>Theory of Change Studio</b> and <b>Impact Evaluation Studio</b> &mdash; build and defend the designs an assessment needs"])
    + hbox("Everything listed is free to open on impactmojo.in, with no login.", "cyan"))



# ── Derive the agenda from where the dividers actually landed ───────────────
# Writing slide ranges by hand guarantees they drift the moment a slide is
# added or cut, and a table of contents that lies is worse than none. Compute
# them from the built list instead: each section runs from the slide after its
# divider to the slide before the next divider (or the end screen).
_div = [(i, p) for i, (k, p) in enumerate(slides) if k == 'divider']
_toc = []
for j, (idx, payload) in enumerate(_div):
    start = idx + 2                                    # 1-indexed, slide after the divider
    end = (_div[j + 1][0]) if j + 1 < len(_div) else len(slides)
    _toc.append((payload[2], "%d&ndash;%d" % (start, end)))
slides[1] = ('toc', _toc)
TOC = _toc

slides.append(('end', None))

db.build(
    course="CSR &amp; ESG 101",
    out_name="csr-esg.html",
    meta_desc=("Corporate social responsibility and ESG for India: Section 135 of the Companies "
               "Act 2013, Schedule VII, the two per cent, unspent-money rules, CSR-1, impact "
               "assessment, and SEBI's BRSR - with the global frameworks as context. Free, "
               "no login, CC BY-NC-ND 4.0."),
    title_main_html="CSR &amp;<br>ESG 101",
    title_sub_html=("India made corporate responsibility a statute. Start with what the law "
                    "actually requires &mdash; then read any sustainability report critically."),
    title_tags=["Companies Act 2013", "Schedule VII", "BRSR", "India-first"],
    toc=TOC,
    slides=slides,
    end_headline_html="Compliance is the floor.<br>Judgement is the work.",
    end_byline="ImpactMojo &middot; Free development education for South Asia",
)
print("BUILT: 101-courses/csr-esg.html  (%d slides)" % len(slides))
