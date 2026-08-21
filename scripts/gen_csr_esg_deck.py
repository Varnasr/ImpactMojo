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

def chart(context, canvas_id, takeaway):
    return ('<div class="chart-slide-frame">'
            '<div class="chart-context">%s</div>'
            '<div class="chart-canvas"><canvas id="%s"></canvas></div>'
            '<div class="chart-takeaway"><strong>What to see:</strong> %s</div>'
            '</div>' % (context, canvas_id, takeaway))

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
divider(1, "The Mandate", "Why corporate giving here is a legal duty")

sec("Section 01 &middot; The Distinction", "India made CSR a legal duty",
    "<p>In most countries corporate social responsibility is voluntary &mdash; a company "
    "chooses whether to spend, how much, and on what. India took a different route. The "
    "Companies Act 2013 made a minimum spend a statutory obligation for companies above "
    "certain thresholds, with a reporting duty attached.</p>"
    + "<p>The 2013 Act was not the first attempt. Voluntary guidelines were issued in 2009 "
    "and the National Voluntary Guidelines in 2011, and take-up was poor enough that the "
    "statutory route was chosen &mdash; which is itself part of the argument about whether "
    "mandating this works.</p>"
    + hbox("For a company in scope, CSR here is compliance rather than philanthropy. That one "
            "distinction changes who is accountable, what has to be documented, which "
            "deadlines apply, and what happens when money goes unspent &mdash; and it is why "
            "most international CSR writing does not transfer to the Indian setting.", "amber")
    + SRC % "Corporate Social Responsibility Voluntary Guidelines 2009; National Voluntary Guidelines 2011; Companies Act 2013.")

sec("Section 01 &middot; The Scale", "What two per cent means in practice",
    stats([("2%", "of average net profit, minimum"),
           ("3", "financial years averaged"),
           ("&#8377;34,909 cr", "the national total, FY2023-24")])
    + "<p>For a single company the arithmetic is small: a firm averaging &#8377;100 crore of "
    "net profit owes &#8377;2 crore a year. Aggregated across every covered company it becomes "
    "one of the larger non-government funding pools in Indian development &mdash; and, because "
    "it is a statutory duty rather than a discretionary budget, one that does not disappear in "
    "a bad year for the philanthropy sector.</p>"
    + "<p>The three-year window is the part most often forgotten. A company&rsquo;s "
    "obligation this year was fixed by profits it reported in years it can no longer change, "
    "which makes CSR budgeting a scheduling problem rather than a forecasting one.</p>"
    + hbox("Every number here is defined precisely in law, and each is taken apart later: "
           "Section 04 on how the two per cent is computed, Section 03 on what Schedule VII "
           "admits. Used loosely, all three mislead.", "cyan")
    + SRC % "Companies Act 2013, Section 135; national total from public disclosures, FY2023-24.")

sec("Section 01 &middot; The Vocabulary", "Three words used interchangeably, wrongly",
    terms([("CSR", "In India, a statutory spending and reporting obligation under Section 135 of the Companies Act 2013. Not a synonym for &lsquo;doing good&rsquo;."),
           ("ESG", "Environmental, Social and Governance &mdash; a disclosure and investment-analysis frame. About what a company reports on itself, largely for investors."),
           ("Sustainability", "The broadest and least precise. Sometimes a synonym for ESG reporting, sometimes an environmental claim, sometimes marketing.")])
    + hbox("When a job advert, a consultant or a policy document uses these as synonyms, it is "
            "collapsing three different obligations with three different audiences and three "
            "different legal statuses. CSR is a duty owed under company law; ESG is a "
            "disclosure regime aimed at investors; sustainability is a description. Keeping "
            "them apart is the first practical skill in this subject.", "cyan"))

sec("Section 01 &middot; Why It Happened", "The road to Section 135",
    "<p>Voluntary CSR guidelines came first &mdash; the Ministry of Corporate Affairs issued "
    "them in 2009 and revised them in 2011 as the National Voluntary Guidelines. Uptake was "
    "thin and uneven. The Companies Act 2013 replaced encouragement with obligation.</p>"
    + bullets(["<b>2009</b> &mdash; MCA Corporate Social Responsibility Voluntary Guidelines",
               "<b>2011</b> &mdash; National Voluntary Guidelines on social, environmental and economic responsibilities of business",
               "<b>2013</b> &mdash; Companies Act 2013 passed; Section 135 creates the obligation",
               "<b>2014</b> &mdash; Section 135 and the CSR Rules come into force on 1 April; India becomes the first country to mandate corporate social spending by statute",
               "<b>2021</b> &mdash; Amendment Rules add unspent-money machinery, CSR-1 registration and impact assessment"])
    + SRC % "Ministry of Corporate Affairs; Companies Act 2013.")

sec("Section 01 &middot; The Critique", "What the law is accused of, from both sides",
    twocol("The case for",
           bullets(["Predictable money for the social sector, at scale",
                    "Forces board-level attention rather than a marketing budget line",
                    "Creates a public record that can be audited and challenged"]),
           "The case against",
           bullets(["A tax by another name, without a tax&rsquo;s democratic allocation",
                    "Compliance-driven spending chases what is easy to document",
                    "Crowds out the awkward work &mdash; rights, advocacy, organising &mdash; that Schedule VII does not obviously cover"]))
    + "<p>The last point on the right is the one practitioners raise most and policy debate "
    "covers least. Schedule VII is a list of services and outcomes; work that is adversarial "
    "to power &mdash; legal aid against the state, union organising, campaigning &mdash; fits "
    "badly, and a funding stream that grows while that work does not is changing the shape of "
    "the sector, not only its budget.</p>"
    + "<p>Notice that the two columns are not symmetrical claims about the same thing. The "
    "left is mostly about <b>money reaching the sector</b>, which is measurable and largely "
    "true. The right is mostly about <b>who decides</b>, which is a question about legitimacy "
    "that no amount of spending data settles.</p>"
    + hbox("Both cases are argued seriously. A course that only teaches the mechanics and never "
           "the critique produces compliance officers, not practitioners.", "amber"))

sec("Section 01 &middot; What You Will Be Able To Do", "Five things, by the end",
    bullets(["Decide, from a company&rsquo;s financials, whether Section 135 applies to it",
             "Compute the minimum obligation and say which years feed the average",
             "Judge whether a proposed activity falls inside Schedule VII &mdash; and defend the judgement",
             "Trace unspent money to the right account within the right deadline",
             "Read a BRSR filing and say what it does and does not tell you"])
    + "<p>Each of these is a decision someone actually has to make: a company secretary "
    "determining scope, a finance team computing the figure, a programme manager arguing a "
    "boundary case, an NGO deciding whether it can accept the money, an analyst reading a "
    "filing.</p>"
    + hbox("Everything else here exists to support those five. If a slide does not eventually "
           "help with one of them, it is context rather than content &mdash; useful, but not "
           "the thing being taught.", "cyan"))

# ───────────────────────── 2. Section 135: who is bound ─────────────────────
divider(2, "Who Is Bound", "Section 135, and the threshold that catches you")

sec("Section 02 &middot; The Test", "Three thresholds, any one of which binds",
    "<p>Section 135(1) applies to every company &mdash; including a foreign company&rsquo;s "
    "Indian branch or project office &mdash; that meets <b>any one</b> of these in the "
    "immediately preceding financial year.</p>"
    + table(["Test", "Threshold"],
            [["Net worth", "&ge; &#8377;500 crore"],
             ["Turnover", "&ge; &#8377;1,000 crore"],
             ["Net profit", "&ge; &#8377;5 crore"]])
    + "<p>Test the year that just ended, not the current one and not an average. Scope is a "
    "single-year question with a yes or no answer, and it is asked afresh every year &mdash; "
    "a company can move in and out of scope as its balance sheet moves, subject to the "
    "three-year exit rule that follows.</p>"
    + hbox("<b>Any one</b>, not all three. A loss-making company with net worth above "
            "&#8377;500 crore is in scope, and so is a modestly capitalised distributor turning "
            "over &#8377;1,000 crore on thin margins. Reading the three as cumulative is the "
            "single most common error made about this section, and it produces confident, "
            "wrong advice that a company is exempt.", "amber")
    + SRC % "Companies Act 2013, Section 135(1).")

sec("Section 02 &middot; The Trap", "&lsquo;Immediately preceding financial year&rsquo;",
    "<p>Scope is tested on the <b>immediately preceding</b> financial year. The spending "
    "obligation is then calculated on the average of the <b>three</b> immediately preceding "
    "financial years. These are two different windows and they are routinely confused.</p>"
    + twocol("Am I in scope?", "<p>Look at <b>one</b> year &mdash; the one just ended.</p>",
             "How much do I owe?", "<p>Average <b>three</b> years of net profit, then take 2%.</p>")
    + "<p>The confusion is easy to make and expensive to carry, because it produces a "
    "plausible answer of the wrong kind: a company correctly identified as in scope, with an "
    "obligation computed from the wrong year, or a company correctly told its obligation is "
    "nil and wrongly told it has no duties at all.</p>"
    + hbox("Given four years of figures, the two answers use different rows. Scope reads one "
            "row &mdash; the year just ended. The amount reads three &mdash; and not the same "
            "three the scope test looked at.", "amber")
    + SRC % "Companies Act 2013, Section 135(1) and 135(5).")

sec("Section 02 &middot; Exit", "How a company falls out of scope",
    "<p>A company that ceases to meet the thresholds is not bound forever. Where a company "
    "no longer meets the criteria for three consecutive financial years, it is not required "
    "to constitute a CSR Committee, and the obligation lapses until it re-enters scope.</p>"
    + "<p>The three-year clock runs on the thresholds, not on the spending. A company that "
    "falls below the criteria in one year is still bound in that year and the two after it, "
    "and the obligation is computed on the three-year profit average from when it was "
    "profitable.</p>"
    + hbox("Entry is immediate; exit takes three years. The asymmetry is deliberate: it stops a "
            "company dipping below a threshold for a single year to avoid a spend, and it means "
            "a business in genuine decline keeps a CSR obligation calculated on better years. "
            "Both consequences follow from the same clause.", "cyan")
    + SRC % "Companies Act 2013, Section 135(9); Companies (CSR Policy) Rules 2014.")

sec("Section 02 &middot; Foreign Companies", "Branches and project offices are in scope",
    "<p>A foreign company with a <b>branch or project office in India</b> is covered if it "
    "meets the thresholds. Net worth, turnover and net profit are computed from the balance "
    "sheet and profit-and-loss account prepared under Section 381(1)(a) of the Act &mdash; that "
    "is, from the Indian operation, not the global group.</p>"
    + "<p>The consequence is that a multinational whose worldwide revenue is very large may owe "
    "nothing if its Indian branch is small, while a mid-sized foreign firm with a substantial "
    "Indian project office may be squarely in scope. Size in India is what the section reads.</p>"
    + hbox("CSR is widely assumed to be a domestic-company rule. It is not, and the assumption "
           "produces real compliance failures at foreign branches that never constituted a CSR "
           "Committee because nobody thought the section applied to them.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 3; Companies Act 2013, Section 381(1)(a).")

sec("Section 02 &middot; Net Profit", "Which profit figure the Act means",
    "<p>&lsquo;Net profit&rsquo; for CSR is <b>not</b> the headline profit-after-tax in a press "
    "release. It is net profit computed under Section 198, with specific adjustments &mdash; "
    "and the CSR Rules further exclude:</p>"
    + bullets(["Any profit arising from overseas branches of the company, whether operated as a separate company or otherwise",
               "Any dividend received from other companies in India which are themselves covered by and complying with Section 135"])
    + hbox("The second exclusion prevents the same rupee generating a CSR obligation twice as "
            "it moves up a group structure &mdash; but only where the paying company is itself "
            "covered by and complying with Section 135. A dividend from an uncovered company "
            "is not excluded, so a group with a mix of covered and uncovered subsidiaries has "
            "to look at each one.", "amber")
    + SRC % "Companies Act 2013, Sections 135 and 198; Companies (CSR Policy) Rules 2014, Rule 2(1)(h).")

sec("Section 02 &middot; Worked Example", "Does Section 135 apply?",
    table(["Company", "Net worth", "Turnover", "Net profit", "In scope?"],
          [["Alpha Ltd", "&#8377;620 cr", "&#8377;300 cr", "&#8377;2 cr", "<b>Yes</b> &mdash; net worth"],
           ["Beta Ltd", "&#8377;90 cr", "&#8377;1,240 cr", "Loss", "<b>Yes</b> &mdash; turnover"],
           ["Gamma Ltd", "&#8377;110 cr", "&#8377;400 cr", "&#8377;6 cr", "<b>Yes</b> &mdash; net profit"],
           ["Delta Ltd", "&#8377;80 cr", "&#8377;300 cr", "&#8377;3 cr", "No &mdash; none met"]])
    + hbox("Beta is the instructive case. It made a loss and is still in scope, because "
            "turnover crossed the line. Its obligation is computed on average net profit, which "
            "may well be nil &mdash; so Beta owes nothing and must still constitute a Committee "
            "or have its board act, adopt a policy, and report. <b>In scope</b> and "
            "<b>owing money</b> are separate questions with separate answers.", "amber")
    + SRC % "Companies Act 2013, Section 135(1) and 135(5).")

sec("Section 02 &middot; What The Threshold Catches", "How many companies the mandate reaches",
    "<p>Any <b>one</b> of the three thresholds brings a company into scope, so the binding test "
    "is usually turnover or net worth rather than profit. A loss-making company with turnover "
    "above &#8377;1,000 crore is still covered &mdash; and still owes two per cent of the average "
    "of its <i>preceding</i> three years.</p>"
    + table(["Threshold (any one)", "Trigger", "Who it typically catches"],
            [["Net worth", "&#8377;500 crore or more", "Asset-heavy manufacturers, banks"],
             ["Turnover", "&#8377;1,000 crore or more", "Large retail, FMCG, distribution"],
             ["Net profit", "&#8377;5 crore or more", "Profitable mid-caps otherwise below both"]])
    + hbox("The profit threshold is the lowest bar and the one most often assumed to be the only "
           "one. A company can be well under &#8377;5 crore of profit and firmly in scope on "
           "turnover alone.", "amber")
    + SRC % "Companies Act 2013, Section 135(1). Confirm current figures at mca.gov.in.")

# ───────────────────────── 3. Schedule VII ──────────────────────────────────
divider(3, "The Boundary Question", "Schedule VII, and what does not count")

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

sec("Section 03 &middot; Read It Liberally", "The MCA&rsquo;s own instruction",
    "<p>The Ministry of Corporate Affairs has repeatedly clarified that the entries in "
    "Schedule VII are to be interpreted <b>liberally</b>, so as to capture the essence of the "
    "subjects listed, rather than read as a narrow closed list.</p>"
    + "<p>&ldquo;Liberally&rdquo; is not the same as &ldquo;anything&rdquo;. The instruction "
    "is about reading the <b>essence</b> of each listed subject rather than its narrowest "
    "wording &mdash; a water project can be rural development, sanitation or environmental "
    "sustainability depending on its design, and none of those readings is wrong.</p>"
    + hbox("Treating Schedule VII as ten rigid boxes wrongly rejects sound projects; treating "
            "it as infinitely elastic wrongly approves anything. The working skill is arguing a "
            "boundary case in writing, with the entry named and the essence identified &mdash; "
            "which is also what an auditor will look for.", "cyan")
    + SRC % "MCA General Circulars and the CSR FAQ series; Schedule VII, Companies Act 2013.")

sec("Section 03 &middot; What Is Excluded", "The exclusions that catch people out",
    table(["Excluded", "Why"],
          [["Activities outside India", "With a narrow exception for training Indian sports personnel representing a State or India"],
           ["Activities benefiting only employees and their families", "CSR is directed outward; staff welfare is not CSR"],
           ["Contribution to any political party", "Expressly excluded &mdash; directly or indirectly"],
           ["Activities in the normal course of business", "With a time-limited exception created for certain COVID-19 vaccine R&amp;D"],
           ["Sponsorship for marketing benefit", "If the company derives marketing benefit, it is advertising, not CSR"],
           ["Fulfilling another statutory obligation", "Money you were already legally required to spend cannot be counted twice"]])
    + hbox("The last two do most of the work in practice. &ldquo;Normal course of "
            "business&rdquo; excludes anything a company would have done commercially, and "
            "&ldquo;another statutory obligation&rdquo; excludes anything it was already "
            "required to do &mdash; between them they rule out a great deal of spending that "
            "is genuinely beneficial and genuinely not CSR.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 2(1)(d).")

sec("Section 03 &middot; The Hard Cases", "Where reasonable people disagree",
    twocol("Probably CSR",
           bullets(["A skilling programme open to the wider community, run near a plant",
                    "Restoring a water body the company does not own",
                    "Funding a school the company&rsquo;s employees&rsquo; children may also attend, alongside others"]),
           "Probably not CSR",
           bullets(["A skilling programme that only feeds the company&rsquo;s own hiring pipeline",
                    "Effluent treatment the company is required to do anyway",
                    "A crèche for employees only &mdash; and in some cases already a statutory duty"]))
    + hbox("The pattern is consistent. The question is rarely &lsquo;is this "
            "good?&rsquo; &mdash; almost everything on both lists is good. It is <b>who is the "
            "beneficiary</b>, and <b>would this have been spent regardless</b>. An activity "
            "the company was already required to do, or would have done for its own "
            "operations, is business expenditure whatever else it also achieves.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 2(1)(d); MCA General Circulars.")

sec("Section 03 &middot; The Boundary Question", "Where Schedule VII is actually argued",
    "<p>The MCA has repeatedly instructed that Schedule VII be read <b>liberally</b>, so most "
    "disputes are not about whether an activity is worthy but about whether the company is the "
    "beneficiary.</p>"
    + twocol("Generally accepted",
             bullets(["A skilling programme open to the wider community",
                      "Rural drinking water near, but not only for, a plant",
                      "Disaster relief contributions to listed funds"]),
             "Generally rejected",
             bullets(["Training that serves only the company&rsquo;s own workforce",
                      "Sponsorship that primarily buys brand visibility",
                      "Work done in the normal course of business"]))
    + "<p>A useful working question: if the company vanished tomorrow, would this activity "
    "still be worth doing for the people it serves? If the answer is no &mdash; because the "
    "beneficiaries are its workforce, or the activity feeds its supply chain &mdash; it is "
    "probably business expenditure with a social character rather than CSR.</p>"
    + "<p>A useful working question: if the company vanished tomorrow, would this activity "
    "still be worth doing for the people it serves? If the answer is no &mdash; because the "
    "beneficiaries are its own workforce, or the activity feeds its supply chain &mdash; it is "
    "probably business expenditure with a social character rather than CSR.</p>"
    + hbox("The recurring test is the <b>employee-benefit exclusion</b>: an activity that "
            "benefits only employees and their families is not CSR. Most boundary cases turn "
            "on how wide the beneficiary group genuinely is, not on the merit of the activity "
            "itself.", "cyan")
    + SRC % "Schedule VII, Companies Act 2013; Companies (CSR Policy) Rules 2014, Rule 2(1)(d); MCA General Circulars.")

# ───────────────────────── 4. The two per cent ──────────────────────────────
divider(4, "The Two Per Cent", "How the obligation is computed")

sec("Section 04 &middot; The Formula", "Prescribed CSR expenditure",
    "<p>The board must ensure the company spends, in every financial year, at least "
    "<b>two per cent of the average net profit</b> made during the three immediately "
    "preceding financial years.</p>"
    + flow(["Take net profit under s.198 for each of 3 years", "Average them",
            "Multiply by 2%", "That is the minimum spend"])
    + "<p>Two words in that sentence do the work. <b>Average</b> means a single bad or "
    "spectacular year does not move the obligation much. <b>Preceding</b> means the amount is "
    "already fixed before the financial year begins &mdash; a company knows in April what it "
    "owes by March.</p>"
    + hbox("Where a company has not completed three financial years, the average is taken over "
            "such preceding years as it has completed. A company in its second year averages "
            "one year; the formula does not wait for three.", "cyan")
    + SRC % "Companies Act 2013, Section 135(5).")

sec("Section 04 &middot; Worked Example", "Computing a real obligation",
    table(["Financial year", "Net profit (s.198)"],
          [["FY 2023&ndash;24", "&#8377;40 crore"],
           ["FY 2024&ndash;25", "&#8377;70 crore"],
           ["FY 2025&ndash;26", "&#8377;10 crore"],
           ["<b>Average</b>", "<b>&#8377;40 crore</b>"],
           ["<b>2% obligation for FY 2026&ndash;27</b>", "<b>&#8377;80 lakh</b>"]])
    + "<p>Note which years feed the calculation. The obligation for FY 2026&ndash;27 is set by "
    "the three years <i>preceding</i> it, so the money a company must spend this year was "
    "determined by profits it has already made and already reported. There is no forecasting "
    "involved, and no discretion.</p>"
    + hbox("The averaging is what makes the obligation survive a bad year. A company that "
            "collapses to &#8377;10 crore of profit still owes on a &#8377;40 crore average "
            "&mdash; and a company having a spectacular year does not owe on it until the "
            "average catches up. The mechanism smooths in both directions.", "cyan")
    + SRC % "Companies Act 2013, Section 135(5).")

sec("A loss-making year", "Zero profit is not zero obligation",
    "<p>Because the base is a three-year average, a single loss-making year does not "
    "extinguish the obligation. Equally, a company can be <b>in scope</b> on turnover or net "
    "worth while its three-year average net profit is nil &mdash; in which case the "
    "prescribed expenditure is nil, but the reporting duty remains.</p>"
    + "<p>A company can therefore be in scope with a nil obligation, and it still owes the "
    "governance: a Committee or a board process, a policy, an action plan, and a report "
    "recording that the prescribed amount was nil. None of the duty structure switches off "
    "because the arithmetic came to zero.</p>"
    + hbox("The two tests do different work and move independently. <b>In scope</b> triggers "
            "governance and reporting duties; <b>average net profit</b> sets the amount. A "
            "company can be firmly in scope and owe nothing, and it still needs a Committee, a "
            "policy and a report.", "cyan")
    + SRC % "Companies Act 2013, Section 135(1) and 135(5).")

sec("Section 04 &middot; The One-Way Rule", "CSR money cannot flow back",
    "<p>Any surplus arising out of CSR activities <b>does not form part of the business profit</b> "
    "of the company. Three routes are open to it, and none of them ends at the company.</p>"
    + flow(["Ploughed back into the same project",
            "or to the Unspent CSR Account, and spent",
            "or transferred to a Schedule VII fund"])
    + "<p>Surplus here is wider than it first sounds: interest earned on CSR funds held in an "
    "account, income generated by a CSR asset, proceeds from the sale of anything produced by a "
    "CSR programme. A skilling centre that sells what its trainees make has generated CSR "
    "surplus, not revenue.</p>"
    + hbox("This closes the route by which a CSR project could quietly become a revenue line, "
           "and it is why a company cannot hold a capital asset created with CSR money. The "
           "money is spent when it leaves; it does not come back.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 7(2); read with Rule 7(4) on capital assets.")

sec("Section 04 &middot; Set-Off", "Spending more than you owe",
    "<p>Where a company spends more than its obligation in a financial year, the excess may be "
    "set off against the requirement of succeeding financial years, subject to conditions in "
    "the Rules &mdash; board approval, a limit on how far forward it carries, and the exclusion "
    "of any surplus arising out of CSR activities.</p>"
    + "<p>The mechanism exists because CSR spending is lumpy while the obligation is annual. A "
    "company that builds a facility in one year may spend three years&rsquo; worth at once; "
    "without set-off it would be over-compliant once and under-compliant twice.</p>"
    + hbox("Check the current text of Rule 7 before advising on set-off. The mechanism has been "
            "amended since it was introduced and the conditions are specific &mdash; in "
            "particular, the excess must be genuine expenditure and not a surplus generated by "
            "the CSR activity itself.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 7(3).")

sec("Section 04 &middot; Capital Assets", "Who may own what CSR money builds",
    "<p>CSR spend may create or acquire a capital asset, but the asset may not simply sit on "
    "the company&rsquo;s balance sheet. It must be held by a Section 8 company or a registered "
    "trust or society with an established track record, or by the beneficiaries themselves as "
    "a self-help group or collective, or by a public authority.</p>"
    + "<p>Assets created before the 2021 amendment had to be transferred within 180 days, "
    "extendable by a further 90 on board approval &mdash; a transitional rule that caught a "
    "great many company-owned school buildings and health centres.</p>"
    + hbox("A school building that remains the company&rsquo;s property is a corporate asset, "
            "not a contribution. The ownership rule is what makes CSR spending irreversible: "
            "money leaves, and what it builds leaves with it.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 7(4).")

sec("Section 04 &middot; Administrative Overheads", "The five per cent cap",
    "<p>Administrative overheads &mdash; the company&rsquo;s own expenses of managing and "
    "administering its CSR functions &mdash; may not exceed <b>five per cent</b> of total CSR "
    "expenditure for the financial year.</p>"
    + "<p>The cap covers the company&rsquo;s cost of running its own CSR function &mdash; "
    "salaries of CSR staff, office costs, programme audit. It does <b>not</b> cover the "
    "implementing partner&rsquo;s cost of delivering the project, which is project "
    "expenditure. An NGO&rsquo;s staff salaries for running the programme are programme cost, "
    "not the company&rsquo;s overhead.</p>"
    + hbox("Conflating the two is a common and expensive mistake, and it is why some NGOs are "
            "told their overheads are &lsquo;capped at 5%&rsquo; when the rule says nothing of "
            "the sort. Impact-assessment cost sits outside this cap and carries its own limit "
            "under Rule 8(3)(c).", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 7(1); read with Rule 8(3)(c).")

# ───────────────────────── 5. Governance ────────────────────────────────────
# ───────────────── 4b. Where the money actually goes ────────────────────────
sec("Section 04 &middot; The Base", "What Section 198 actually adjusts",
    "<p>&ldquo;Net profit&rdquo; here is not profit before tax from the income statement. It is "
    "profit computed under <b>Section 198</b>, which starts from the profit and loss account and "
    "then adds back and deducts specified items.</p>"
    + twocol("Credit is <b>not</b> given for",
             bullets(["Premium on shares or debentures issued",
                      "Profits on sale of forfeited shares",
                      "Profits of a capital nature, including on sale of undertakings",
                      "Surplus on revaluation of assets"]),
             "Deductions <b>not</b> allowed",
             bullets(["Income tax and super-tax",
                      "Voluntary compensation or damages",
                      "Loss of a capital nature",
                      "Set-off of past losses already adjusted"]))
    + hbox("Two exclusions matter most in practice: <b>profits from overseas branches</b> are "
           "excluded from the base, and <b>dividends received from other companies</b> that are "
           "themselves covered by Section 135 are excluded &mdash; so the same rupee is not taxed "
           "for CSR twice.", "amber")
    + SRC % "Companies Act 2013, Section 198; Companies (CSR Policy) Rules 2014, Rule 2(1)(h).")

sec("Section 04 &middot; Spending More Than You Owe", "Set-off, and its limits",
    "<p>A company that spends <b>above</b> its obligation may set the excess off against the "
    "requirement of up to the <b>three immediately succeeding financial years</b>.</p>"
    + bullets(["The excess must not include the surplus arising out of CSR activities",
               "The board must pass a resolution to that effect",
               "The set-off is capped at the excess actually spent, carried for three years"])
    + "<p>The board resolution is the operative condition. Excess spending does not create a "
    "set-off automatically &mdash; a company that overspends without resolving to carry the "
    "excess forward has simply overspent, and discovers this a year later when it tries to "
    "claim the credit.</p>"
    + hbox("Surplus generated by a CSR project &mdash; interest, sale proceeds, income from an "
           "asset &mdash; does not count as company income and does not create a set-off. It "
           "must be ploughed back into the same project, or into the Unspent CSR Account, or "
           "transferred to a Schedule VII fund.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rules 7(3) and 7(2).")

sec("Section 04 &middot; Assets Bought With CSR", "Who is allowed to hold them",
    "<p>Where CSR money creates or acquires a <b>capital asset</b>, the company may not hold it. "
    "The asset must sit with one of three kinds of holder.</p>"
    + flow(["A Section 8 company or registered trust/society with CSR-1",
            "or the beneficiaries themselves, as a self-help group or collective",
            "or a public authority"])
    + "<p>The rule attaches to the asset, not to the money that bought it. A company funding a "
    "building, a piece of equipment or a vehicle has to place the title outside itself &mdash; "
    "which means the implementing partner, a community body or the state must be able to hold "
    "it, maintain it and bear its running costs.</p>"
    + hbox("Assets created before the 2021 amendment had to be transferred within 180 days, "
           "extendable by 90. The rule exists because a company that keeps the school building "
           "it built with CSR money has bought an asset, not made a contribution.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 7(4).")

sec("Section 04 &middot; The National Picture", "What two per cent adds up to",
    "<p>Across all covered companies, mandated CSR came to <b>&#8377;34,909 crore in "
    "FY2023-24</b>. That is the whole of India&rsquo;s statutory corporate giving in one "
    "number &mdash; large enough to matter to the sectors it enters, small beside public "
    "expenditure on the same subjects.</p>"
    + stats([["&#8377;34,909 cr", "total CSR spend, FY2023-24"],
             ["2%", "of average net profit, three-year window"]])
    + "<p>It is also a number that only exists because of the statute. Voluntary corporate "
    "giving in India before 2014 was a fraction of this and concentrated in a handful of "
    "houses; whatever else the mandate did, it created a floor.</p>"
    + hbox("For scale: the Union Budget 2026-27 provides &#8377;95,692 crore for the rural "
           "employment guarantee alone. All of corporate CSR is roughly a third of that single "
           "scheme. CSR is a real funding stream and not a substitute for public spending.", "amber")
    + SRC % "CSR spend from public disclosures, compiled in the ImpactMojo CSR map. Budget figure: Budget at a Glance 2026-27.")

sec("Section 04 &middot; The Sector Split", "Where CSR money actually goes",
    chart("Mandated CSR expenditure by Schedule VII head, FY2023-24, &#8377; crore. "
          "Compiled from public company disclosures.",
          "csrSectorChart",
          "Health and education together take roughly seven rupees in every ten. Environment, "
          "rural development and every other Schedule VII head &mdash; gender, sport, heritage, "
          "disaster relief, technology incubation &mdash; divide the remaining 29 per cent "
          "between them. Schedule VII is far broader than the money that reaches it.")
    + "<p>The concentration is worth pausing on. Schedule VII lists education, health, "
    "gender equality, environment, rural development, sport, heritage, armed-forces veterans, "
    "technology incubation and more &mdash; and two heads absorb about seven rupees in ten. "
    "The distribution is not set by need; it is the aggregate of thousands of separate "
    "corporate decisions, and those cluster on what is legible, photographable and "
    "uncontroversial.</p>"
    + SRC % "Public disclosures, FY2023-24; interactive version at impactmojo.in/maps/csr-india.html.")

sec("Section 04 &middot; The Concentration Curve", "Ten firms, and everyone else",
    chart("The ten largest corporate CSR spenders, FY2023-24, &#8377; crore.",
          "csrTopTenChart",
          "These ten account for about &#8377;5,880 crore &mdash; roughly 17 per cent of all "
          "CSR &mdash; while thousands of other covered companies contribute the rest. That "
          "shapes fundraising: a handful of firms can fund a programme outright, while most "
          "covered companies have obligations of a few lakh to a few crore and behave quite "
          "differently as funders.")
    + "<p>The distribution is roughly what you would expect from a rule pegged to profit: "
    "banks, IT services, oil and steel &mdash; the most profitable large firms in the "
    "economy &mdash; with no relationship to where social need is concentrated.</p>"
    + "<p>The tail matters as much as the head. A company with a &#8377;40 lakh obligation "
    "cannot fund a district programme, cannot commission an impact assessment at Rule 8 "
    "thresholds, and will usually look for a partner who can absorb a small grant with light "
    "reporting. That is a different fundraising conversation from the one with a top-ten "
    "spender, and confusing the two wastes everyone&rsquo;s time.</p>"
    + SRC % "Public disclosures, FY2023-24, compiled in the ImpactMojo CSR map.")

sec("Section 04 &middot; Where It Lands", "The sector split, and what it implies",
    table(["Sector", "&#8377; crore", "Share"],
          [["Health &amp; sanitation", "13,400", "38.4%"],
           ["Education &amp; skilling", "11,300", "32.4%"],
           ["Environment", "3,800", "10.9%"],
           ["Rural development", "2,410", "6.9%"],
           ["All other heads", "3,980", "11.4%"]])
    + "<p>Set that against where Indian development need is usually said to sit. Nutrition, "
    "sanitation and primary care fall inside the health head; schooling and skilling inside "
    "education. Almost everything else &mdash; social protection, disability, legal aid, urban "
    "poverty, care work, gender-based violence &mdash; competes inside the 11.4 per cent "
    "labelled &lsquo;other&rsquo;.</p>"
    + "<p>Health and education together take <b>seven rupees in every ten</b>. The remaining "
    "Schedule VII heads &mdash; gender, sports, arts and heritage, disaster relief, technology "
    "incubation &mdash; share what is left.</p>"
    + hbox("Schedule VII lists far more activities than the money reaches. If you are raising "
           "CSR funds for a head outside the top two, you are competing for a much smaller "
           "pool than the breadth of the Schedule suggests.", "cyan")
    + SRC % "Public disclosures, FY2023-24; see the ImpactMojo CSR map for the interactive view.")

sec("Section 04 &middot; The Concentration", "Ten companies, and the long tail",
    table(["Rank", "Company", "&#8377; crore"],
          [["1", "HDFC Bank", "945"], ["2", "Reliance Industries", "900"],
           ["3", "Tata Consultancy Services", "813"], ["4", "ONGC", "612"],
           ["5", "Tata Steel", "573"], ["6", "Infosys", "451"],
           ["7", "Indian Oil", "436"], ["8", "Reliance Jio", "403"],
           ["9", "ITC", "380"], ["10", "ICICI Bank", "368"]])
    + "<p>The ten largest spenders account for roughly &#8377;5,880 crore &mdash; about "
    "<b>17 per cent</b> of all CSR &mdash; while thousands of covered companies contribute the "
    "rest in much smaller amounts.</p>"
    + hbox("This shapes fundraising. A handful of donors write cheques large enough to fund a "
           "programme outright; most covered companies have obligations of a few lakh to a few "
           "crore and behave quite differently as funders.", "amber")
    + SRC % "Public disclosures, FY2023-24, compiled in the ImpactMojo CSR map.")

divider(5, "The Board&rsquo;s Duty", "Committee, action plan, certification")

sec("Section 05 &middot; The Committee", "Who has to constitute one",
    "<p>A company in scope must constitute a CSR Committee of the Board, consisting of "
    "<b>three or more directors</b>, of which at least one must be an independent director.</p>"
    + bullets(["A company not required to appoint an independent director constitutes its Committee with two or more directors",
               "Where the amount to be spent does not exceed &#8377;50 lakh, the requirement to constitute a Committee does not apply, and the Board discharges its functions"])
    + hbox("The &#8377;50 lakh exemption is the practical one. It removes the committee "
            "requirement for the large number of companies whose obligation is small &mdash; "
            "but it removes only the committee, not the policy, the plan, the spend or the "
            "report. The board simply does all of it directly.", "cyan")
    + SRC % "Companies Act 2013, Section 135(1) and 135(9), as amended by the Companies (Amendment) Act 2020.")

sec("Section 05 &middot; The Committee", "Three statutory functions, and three it lacks",
    flow(["Formulate and recommend the CSR Policy",
          "Recommend the amount of expenditure",
          "Monitor the Policy from time to time"])
    + "<p>Since 2021 it also formulates the <b>annual action plan</b> for board approval. The "
    "Committee must have three or more directors including at least one independent director; "
    "a company not required to have an independent director may constitute it with two.</p>"
    + twocol("What it does",
             bullets(["Sets the policy and the plan",
                      "Recommends how much is spent",
                      "Monitors implementation"]),
             "What it does not do",
             bullets(["Select projects day to day",
                      "Implement anything itself",
                      "Certify that funds were properly used"]))
    + hbox("The last exclusion matters. Certification that CSR funds were disbursed and "
           "utilised for the stated purpose is the <b>Chief Financial Officer&rsquo;s</b> duty, "
           "not the Committee&rsquo;s &mdash; so the person who signs is not the person who "
           "set the policy.", "cyan")
    + SRC % "Companies Act 2013, Section 135(1) and 135(3); CSR Rules, Rules 5(2) and 4(5).")

sec("Section 05 &middot; The Board&rsquo;s Duties", "Where accountability actually sits",
    bullets(["Approve the CSR Policy and disclose its contents in the Board&rsquo;s report and on the website",
             "Ensure the activities in the Policy are actually undertaken",
             "Ensure the company spends the prescribed amount",
             "Satisfy itself that the funds disbursed have been utilised for the purposes and in the manner approved &mdash; with the CFO certifying this",
             "Where the amount is not spent, give the reason in the Board&rsquo;s report"])
    + "<p>Read the fourth duty carefully. The board must satisfy itself that funds were "
    "utilised <b>for the purposes and in the manner approved</b> &mdash; not merely that they "
    "were disbursed. Money that left the company and did something other than what the action "
    "plan said is not compliant spending.</p>"
    + hbox("The CFO certification is the teeth. It converts a governance aspiration into one "
            "named officer&rsquo;s signature, and it is the reason implementing partners are "
            "asked for utilisation certificates and beneficiary records rather than a "
            "narrative report.", "cyan")
    + SRC % "Companies Act 2013, Section 135; Companies (CSR Policy) Rules 2014, Rule 4(5).")

sec("Section 05 &middot; The Action Plan", "What the Committee must formulate",
    bullets(["The list of CSR projects or programmes approved, within Schedule VII",
             "The manner of execution",
             "The modalities of utilisation of funds and implementation schedules",
             "Monitoring and reporting mechanism",
             "Details of need and impact assessment, if any, for the projects"])
    + "<p>This list is why the annual action plan is the document an auditor reads first. It "
    "converts a policy &mdash; which can be aspirational &mdash; into named projects with "
    "money, dates and a named way of checking them.</p>"
    + hbox("The board may alter the plan at any time during the financial year, on the "
            "Committee&rsquo;s recommendation and with reasonable justification recorded. The "
            "recording is the operative part: an undocumented mid-year change is the finding "
            "that gets written up, not the change itself.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 5(2).")

sec("Section 05 &middot; Disclosure", "What has to be public, and where",
    "<p>The board&rsquo;s report must include an annual report on CSR containing the "
    "particulars specified in the Rules, and the company must publish three things <b>on its "
    "website</b>: the composition of the CSR Committee, the CSR Policy, and the projects "
    "approved by the board.</p>"
    + bullets(["Board&rsquo;s report &mdash; the annual CSR report, in the prescribed format",
               "Website &mdash; Committee composition, policy, approved projects",
               "Where impact assessment applies &mdash; the assessment report, annexed"])
    + hbox("The website duty is what makes independent scrutiny possible at all. Every listed "
           "Indian company of size has this material published and indexed, which means anyone "
           "can read the primary document rather than a summary of it &mdash; and can compare "
           "what a company said it would fund against what it reported spending.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 9; Section 134(3)(o).")

sec("Section 05 &middot; The Annual Action Plan", "What the board actually approves",
    "<p>Since the 2021 amendment the CSR Committee must formulate, and the board approve, an "
    "<b>annual action plan</b>. It is the document an auditor reads, and it must contain more "
    "than a list of intentions.</p>"
    + bullets(["The list of approved CSR projects, mapped to Schedule VII heads",
               "The manner of execution &mdash; directly, or through an implementing agency",
               "Modalities of utilisation of funds and implementation schedules",
               "Monitoring and reporting mechanism for each project",
               "Details of need and impact assessment, where undertaken"])
    + "<p>&ldquo;Need assessment&rdquo; sits quietly in that last line and is the most "
    "skipped item on it. A plan that names projects and budgets without any statement of how "
    "the need was established is complete on its face and hollow underneath &mdash; and it is "
    "how a company ends up funding what it already knows rather than what the district "
    "lacks.</p>"
    + hbox("The board may alter the plan during the year on the Committee&rsquo;s recommendation, "
           "with reasons recorded. An unrecorded change is the finding an auditor writes up.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 5(2).")

# ───────────────────────── 6. Unspent money ─────────────────────────────────
sec("Section 05 &middot; What Happens If You Do Not", "Enforcement, and how it changed",
    "<p>CSR non-compliance was a <b>criminal</b> offence as originally amended. The Companies "
    "(Amendment) Act 2020 decriminalised it, replacing imprisonment with monetary penalty.</p>"
    + table(["Who", "Penalty"],
            [["The company", "Twice the unspent amount required to be transferred, or &#8377;1 crore, whichever is less"],
             ["Every officer in default", "One-tenth of the amount required to be transferred, or &#8377;2 lakh, whichever is less"]])
    + "<p>The penalty attaches to the <b>failure to transfer</b> unspent money to the right "
    "account or fund, not to under-spending as such. A company that spends nothing but transfers "
    "correctly is in a different position from one that neither spends nor transfers.</p>"
    + hbox("Check the current figures before advising anyone. Penalty amounts and the criminal "
           "or civil character of company-law defaults have both been amended more than once "
           "since 2014.", "amber")
    + SRC % "Companies Act 2013, Section 135(7), as amended by the Companies (Amendment) Act 2020.")

sec("Section 05 &middot; The Argument Against", "Is a CSR mandate good policy?",
    "<p>India was the first country to make corporate social spending a statutory duty. That is "
    "a genuine policy experiment, and it is contested on both sides.</p>"
    + twocol("The case for",
             bullets(["Creates a large, predictable domestic funding stream",
                      "Forces a board conversation that would otherwise not happen",
                      "Produces a public record that can be audited and challenged",
                      "Directs private profit toward Schedule VII public purposes"]),
             "The case against",
             bullets(["A tax by another name, but without parliamentary control over how it is spent",
                      "Companies allocate public-purpose money with no democratic mandate",
                      "Compliance-driven spending rewards what is easy to report",
                      "Two per cent is arbitrary, and unrelated to any assessment of need"]))
    + hbox("Both readings are held by serious people. A course that teaches only the mechanics "
           "leaves you able to compute the obligation and unable to say whether the obligation "
           "should exist.", "cyan"))

divider(6, "The Money That Did Not Move", "Unspent CSR, and the 2021 machinery")

sec("Section 06 &middot; The 2021 Change", "When unspent money stopped being a footnote",
    "<p>Before 2021, a company that failed to spend explained itself in the board&rsquo;s "
    "report, and that was largely the end of it. Unspent CSR was a disclosure item, not a "
    "liability.</p>"
    + twocol("Before: comply or explain",
             bullets(["Underspend disclosed in the board&rsquo;s report",
                      "Reasons stated, no transfer required",
                      "Money stayed with the company",
                      "No penalty attached to the shortfall"]),
             "After: transfer or pay",
             bullets(["Unspent money must move to a defined account or fund",
                      "Deadlines of 30 days and 6 months apply",
                      "Three-year backstop on ongoing projects",
                      "Penalty attaches to failure to transfer"]))
    + hbox("This is the most consequential amendment to the regime since it began, and the "
           "reason so much CSR writing is out of date. If a reference predates 2021, its "
           "treatment of unspent money is simply wrong &mdash; check the date before trusting "
           "any guidance note on this point.", "amber")
    + SRC % "Companies (Amendment) Act 2019; Companies (CSR Policy) Amendment Rules 2021.")

sec("Section 06 &middot; The Fork", "Ongoing project, or not",
    twocol("Ongoing project",
           "<p>Transfer the unspent amount to a special account &mdash; the <b>Unspent CSR "
           "Account</b> &mdash; within <b>30 days</b> of the end of the financial year. Spend it "
           "within <b>three</b> financial years.</p>",
           "Not an ongoing project",
           "<p>Transfer the unspent amount to a fund specified in <b>Schedule VII</b> within "
           "<b>six months</b> of the end of the financial year.</p>")
    + "<p>The difference is not cosmetic. An ongoing project keeps the money within the "
    "company&rsquo;s control for up to three more years and lets it finish what it started. "
    "Anything else loses the money to a Central Government fund within six months, whatever "
    "the reason it went unspent.</p>"
    + hbox("Everything turns on whether the project is &lsquo;ongoing&rsquo;, and that word is "
            "defined rather than descriptive &mdash; the definition is on the next slide. "
            "Deciding after year-end that something was ongoing does not make it so.", "amber")
    + SRC % "Companies Act 2013, Section 135(5) and 135(6).")

sec("Section 06 &middot; Ongoing Project", "A defined term, not a description",
    "<p>An <b>ongoing project</b> means a multi-year project undertaken by a company in "
    "fulfilment of its CSR obligation, having a timeline <b>not exceeding three years</b> "
    "excluding the financial year in which it was commenced. It includes a project that was "
    "initially not approved as multi-year but whose duration is extended beyond one year by "
    "the Board on reasonable justification.</p>"
    + "<p>The extension clause matters as much as the definition. A project not originally "
    "approved as multi-year can become ongoing if the board extends it beyond a year with "
    "reasonable justification recorded &mdash; which is the legitimate route, and also the "
    "route a company takes when it wants to keep money it has not managed to spend.</p>"
    + hbox("Three years, <b>excluding</b> the commencement year &mdash; so an ongoing project "
            "can run into a fourth calendar year of activity and still be within the "
            "definition. Dropping the exclusion is the most common arithmetic error here, and "
            "it changes which unspent rule applies.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 2(1)(i).")

sec("Section 06 &middot; The Backstop", "What happens after three years",
    "<p>Money sitting in the Unspent CSR Account that is not spent within three financial "
    "years must be transferred to a fund specified in Schedule VII within <b>30 days</b> from "
    "the end of the third financial year.</p>"
    + flow(["FY ends unspent", "&rarr; Unspent CSR A/c in 30 days",
            "3 years to spend", "Still unspent &rarr; Schedule VII fund in 30 days"])
    + "<p>The three years run from the end of the financial year in which the money was "
    "transferred, not from when the project started. A project that slips can therefore "
    "exhaust the window while still running &mdash; and the unspent balance leaves anyway.</p>"
    + hbox("This is the clause that makes multi-year CSR planning real rather than notional. "
            "Money parked in the Unspent Account is not the company&rsquo;s to hold "
            "indefinitely; it is on a clock, and at the end of the clock it goes to a Central "
            "Government fund whatever the project&rsquo;s state.", "amber")
    + SRC % "Companies Act 2013, Section 135(6).")

sec("Section 06 &middot; The Funds", "Where unspent money is sent",
    bullets(["Prime Minister&rsquo;s National Relief Fund",
             "PM CARES Fund",
             "Clean Ganga Fund",
             "Swachh Bharat Kosh",
             "Any other fund set up by the Central Government as specified in Schedule VII"])
    + "<p>Every one of these is a fund of the Central Government. There is no option to "
    "transfer unspent money to a state fund, a local body, a district administration, or the "
    "NGO the company had been working with &mdash; even where that partner has a live project "
    "and the capacity to absorb the money.</p>"
    + hbox("The political consequence is worth stating plainly: money a company failed to "
            "direct locally is redirected centrally. One reading is that this prevents "
            "underspending from simply evaporating; another is that it converts a failure of "
            "corporate programme management into central revenue, with no say for the district "
            "the money was meant for. Both are live arguments.", "cyan")
    + SRC % "Schedule VII, Companies Act 2013; Section 135(5) and 135(6).")

sec("Section 06 &middot; Penalties", "An enforceable default, not a criminal one",
    "<p>Failure to comply with the transfer obligations attracts penalty on the company and on "
    "every officer in default under Section 135(7). The Companies (Amendment) Act 2020 "
    "converted the regime from <b>criminal to civil</b>.</p>"
    + "<p>That change is easy to read as a softening and is better read as a redesign. "
    "Criminalising a spending shortfall made directors personally liable to imprisonment for a "
    "budgeting failure, which chilled participation on boards without improving spending. A "
    "monetary penalty attached to the transfer duty targets the behaviour the state actually "
    "wants: money that is not spent must still leave the company.</p>"
    + hbox("Penalty amounts are capped by formula and have been amended. Read the current "
           "Section 135(7) before quoting a figure &mdash; a stale number in a compliance note "
           "is worse than no number at all.", "amber")
    + SRC % "Companies Act 2013, Section 135(7), as amended 2020.")

sec("Section 06 &middot; The Order Of Operations", "Which unspent rule applies, and when",
    "<p>The two unspent regimes are decided by one question: was the money committed to an "
    "<b>ongoing project</b>?</p>"
    + table(["Situation", "Where the money goes", "Deadline"],
            [["Unspent, ongoing project", "Unspent CSR Account (separate bank account)", "Within 30 days of year end"],
             ["Then unspent from that account", "A Schedule VII fund", "Within 3 financial years"],
             ["Unspent, not an ongoing project", "A Schedule VII fund directly", "Within 6 months of year end"]])
    + "<p>The first row requires a <b>separate bank account</b>, opened for the purpose and "
    "named for the financial year. It is not a ledger entry or a ring-fenced balance &mdash; "
    "the money physically moves, which is what makes the obligation checkable.</p>"
    + hbox("&ldquo;Ongoing project&rdquo; is defined, not descriptive: a multi-year project with a "
           "timeline not exceeding three years, excluding the year of commencement. Labelling "
           "something ongoing after the year has closed does not make it so.", "amber")
    + SRC % "Companies Act 2013, Section 135(5) and 135(6); CSR Rules, Rule 2(1)(i).")

# ───────────────────────── 7. Implementation ────────────────────────────────
divider(7, "Who May Spend It", "Implementation routes and CSR-1")

sec("Section 07 &middot; The Routes", "Four ways a company may deliver CSR",
    bullets(["<b>Itself</b> &mdash; directly, through its own teams",
             "<b>Its own foundation</b> &mdash; a Section 8 company, registered trust or society established by the company, alone or with others",
             "<b>A government entity</b> &mdash; established under an Act of Parliament or a State legislature",
             "<b>An external organisation</b> &mdash; a Section 8 company, registered public trust or registered society with an established track record of at least three years"])
    + "<p>The choice is not neutral. Delivering directly keeps control and builds no external "
    "capacity; a company foundation keeps control while looking independent; an established "
    "NGO brings field presence the company does not have, and takes a share of the decisions "
    "with it.</p>"
    + hbox("Note the asymmetry in the fourth route. An entity the company sets up itself faces "
            "no three-year track-record test; an independent organisation does. The rule is "
            "strictest on exactly the partners the company does not control.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(1).")

sec("Section 07 &middot; CSR-1", "When registration became mandatory",
    "<p>From <b>1 April 2021</b>, an entity intending to undertake CSR activities on behalf "
    "of a company must register itself with the Central Government by filing <b>Form CSR-1</b> "
    "electronically with the Registrar, and obtain a CSR Registration Number.</p>"
    + "<p>The registration is with the Registrar of Companies, not with the funding company, "
    "and it is a one-time filing rather than a per-grant approval. Once issued, the CSR "
    "Registration Number is quoted by every company that funds the entity.</p>"
    + hbox("For an NGO this is the practical gate. No CSR-1, no corporate money &mdash; "
            "regardless of how good the organisation is or how long it has worked. An "
            "organisation that has run programmes for a decade but never filed is, for CSR "
            "purposes, invisible.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(2).")

sec("Section 07 &middot; Filing CSR-1", "What the form actually asks for",
    bullets(["Registration under Section 12A and 80G of the Income-tax Act 1961, where applicable",
             "The entity type &mdash; Section 8 company, registered public trust or registered society",
             "Governing body details, PAN, and the registration certificate",
             "Digital signature of an authorised person",
             "Certification by a practising chartered accountant, company secretary or cost accountant"])
    + "<p>Filing is free and there is no fee, but it is not a formality: the professional "
    "certifying the form is attesting that the entity meets the eligibility conditions, "
    "including the three-year track record. On acceptance the MCA issues a <b>CSR registration "
    "number</b>, which the funding company records in its own reporting.</p>"
    + hbox("Check the current form and its attachments on the MCA portal before advising an "
           "organisation. The requirements have been revised more than once since 2021, and an "
           "outdated checklist wastes a filing cycle.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(2); Form CSR-1, mca.gov.in.")

sec("Section 07 &middot; The Track Record", "Three years, and who it shuts out",
    "<p>An external implementing organisation must have an <b>established track record of at "
    "least three years</b> in undertaking similar activities. An entity established by the "
    "company itself &mdash; its own foundation or Section 8 company &mdash; does not face this "
    "requirement.</p>"
    + twocol("What it prevents",
             bullets(["Shell intermediaries created to route funds",
                      "Untested entities handling large first grants",
                      "Agencies with no record to check"]),
             "What it costs",
             bullets(["New organisations cannot receive CSR at all for three years",
                      "Community-rooted groups without formal history are excluded",
                      "Corporate foundations face a lower bar than independent NGOs"]))
    + hbox("The asymmetry is the part worth noticing: the rule is strictest on exactly the "
           "organisations least able to absorb it, and lightest on entities the funder controls. "
           "It is a safeguard and a barrier at the same time, and both are real.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(1).")

sec("Monitoring the money", "The company cannot outsource responsibility",
    "<p>The Board must satisfy itself that funds disbursed have been utilised for the purposes "
    "and in the manner approved, and the Chief Financial Officer or the person responsible for "
    "financial management must certify to that effect.</p>"
    + "<p>The certification runs to the Chief Financial Officer or the person responsible for "
    "financial management &mdash; not to the CSR Committee that set the policy, and not to the "
    "implementing agency that did the work. The person who signs is downstream of both.</p>"
    + hbox("For an implementing NGO this translates into utilisation certificates, documented "
            "beneficiary records and audit trails. These are worth designing <b>at proposal "
            "stage</b> rather than assembling at year end, because the CFO cannot certify what "
            "was never recorded, and a grant that cannot be certified is a problem for the "
            "funder as well as the grantee.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(5).")

sec("Section 07 &middot; Collaboration", "Pooling, and the condition attached",
    "<p>A company may collaborate with other companies on a project, provided the CSR "
    "Committees of <b>each</b> are in a position to report separately on that project in "
    "accordance with the Rules.</p>"
    + "<p>The economics make this attractive. Most covered companies owe a few lakh to a few "
    "crore &mdash; enough to fund a fragment of a programme, not a programme. Ten such "
    "obligations pooled reach a scale at which a district-level intervention can be designed, "
    "staffed and evaluated rather than scattered across ten small grants.</p>"
    + hbox("The separate-reporting condition is what stops a pool becoming a black box. Each "
           "company must still be able to say what its own money did, which in practice means "
           "the implementing agency has to keep the accounting attributable rather than merged.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(4).")

sec("Section 07 &middot; What CSR-1 Requires", "The registration an NGO cannot skip",
    "<p>From 1 April 2021 no company may route CSR funds to an implementing agency that has not "
    "filed <b>Form CSR-1</b> with the Ministry of Corporate Affairs and obtained a registration "
    "number.</p>"
    + bullets(["The entity must be a Section 8 company, a registered public trust or a registered society",
               "It must hold registration under Section 12A and 80G of the Income-tax Act",
               "It must have an established track record of at least three years in similar activities",
               "The form is certified by a practising CA, CS or cost accountant"])
    + "<p>Read those four together and the shape of the eligible partner appears: formally "
    "registered, tax-compliant, professionally audited, and three years old. That is a "
    "reasonable description of an established NGO and a poor description of a new "
    "community organisation &mdash; which is the trade-off the rule makes deliberately.</p>"
    + hbox("The three-year track record is the clause that most often disqualifies a new "
           "organisation. A company cannot waive it; it is a condition on the agency, not a "
           "preference of the funder.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 4(1) and 4(2).")

# ───────────────────────── 8. Impact assessment ─────────────────────────────
divider(8, "Does It Work?", "Impact assessment, and what it rarely asks")

sec("When it is mandatory", "The two thresholds",
    "<p>A company must undertake impact assessment through an independent agency where it "
    "meets <b>both</b> limbs:</p>"
    + table(["Limb", "Threshold"],
            [["Company&rsquo;s average CSR obligation", "&ge; &#8377;10 crore in the three immediately preceding financial years"],
             ["The project", "Outlay &ge; &#8377;1 crore, and completed not less than one year before undertaking the study"]])
    + "<p>The one-year gap in the second limb is deliberate. Assessing a project immediately "
    "on completion measures delivery, not effect; most outcomes worth measuring &mdash; income, "
    "attendance, health status &mdash; take time to appear or to fade.</p>"
    + hbox("Both limbs must be met. A large company&rsquo;s small project is out of scope, and "
            "a small company&rsquo;s large project is out of scope. The result is that mandatory "
            "assessment reaches only a narrow band of CSR: big spenders&rsquo; big projects. "
            "Everything else is assessed voluntarily or not at all.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 8(3).")

sec("Section 08 &middot; Who Pays For It", "Assessment is chargeable to CSR",
    "<p>Impact assessment expenditure <b>may be booked to CSR</b> for that financial year, "
    "subject to a cap in the Rules expressed as a percentage of total CSR expenditure or an "
    "absolute figure, whichever is higher.</p>"
    + "<p>That matters more than it sounds. Evaluation is usually the first line cut, because "
    "it competes with delivery for the same budget and produces no beneficiaries. Making it "
    "chargeable to CSR means a company commissioning a serious assessment is not spending "
    "money it could otherwise have spent on the programme &mdash; it is spending CSR money on "
    "finding out whether the programme worked.</p>"
    + hbox("The cap sits outside the five per cent administrative-overhead limit, so a company "
           "does not have to choose between running its CSR function and evaluating it. Check "
           "the current figure in Rule 8(3)(c); it has been amended.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 8(3)(c).")

sec("Section 08 &middot; Independent Agency", "What independence means here",
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
                      "Evaluation training is directly employable here"]))
    + "<p>Nothing in the Rules prevents a good assessment. There is no ceiling on rigour, the "
    "cost is chargeable to CSR, and the report is published. What is missing is a floor "
    "&mdash; and in the absence of one, the quality of any given assessment depends entirely "
    "on whether the commissioning company wanted to find something out.</p>"
    + hbox("This is the seam where CSR meets monitoring and evaluation. The methods that answer "
           "&ldquo;did it work?&rdquo; are the same ones an impact assessment needs and usually "
           "does not use.", "cyan"))

sec("Section 08 &middot; A Better Assessment", "What it would have to do",
    bullets(["States the theory of change the project was built on, and tests it",
             "Distinguishes outputs from outcomes, and says which it can evidence",
             "Is explicit about attribution &mdash; what would have happened anyway",
             "Reports what did not work, not only what did",
             "Names its limitations, sample and period"])
    + "<p>None of this requires a randomised trial. It requires the author to be explicit "
    "about what the study can and cannot support &mdash; which is a writing discipline before "
    "it is a methodological one.</p>"
    + hbox("A report with no negative findings and no stated limitations is not an "
            "evaluation. Every real programme has something that did not work and some group "
            "it reached less well; a document that mentions neither has been written to "
            "persuade rather than to find out.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 8(3); see also the ImpactMojo MEL and Impact Evaluation courses.")

sec("Section 08 &middot; Attribution", "The question CSR reports usually dodge",
    "<p>A CSR report will say a programme reached 40,000 people. The evaluation question is "
    "different: <b>what changed that would not have changed anyway?</b></p>"
    + quote("Reach is an output. Change is an outcome. Attribution is a claim about causation "
            "&mdash; and it needs a comparison, not a headcount.",
            "The distinction every impact assessment stands or falls on")
    + "<p>The gap is not usually dishonesty. Reach is cheap to measure and change is "
    "expensive, so a report constrained by budget and deadline reports what it has. The "
    "problem is that both are presented in the same register, and a reader who does not know "
    "the difference will take a headcount for a result.</p>"
    + "<p>The honest version is available and rarely used: say what was delivered, say what "
    "was measured, and say plainly that the study cannot separate the programme&rsquo;s effect "
    "from everything else happening in those districts over those years. That sentence costs "
    "nothing and is almost never written.</p>"
    + hbox("The ImpactMojo Theory of Change and Impact Evaluation studios are where the "
            "comparison design gets built and defended &mdash; both free, both in the browser, "
            "and both producing an artefact rather than an essay.", "cyan"))

sec("Section 08 &middot; Where It Is Published", "The annexure, and why it matters",
    "<p>The impact assessment report must be placed before the board and <b>annexed to the "
    "annual report on CSR</b>. That annexure is filed and published, which makes it one of the "
    "few evaluation documents in Indian development that anyone can read without asking "
    "permission.</p>"
    + "<p>The quality varies enormously. Some are competent evaluations with a stated design, "
    "sample and limitations. Others are the programme brochure with a cover page. Both satisfy "
    "the same rule, because the Rules require an assessment by an independent agency without "
    "specifying what an assessment must contain.</p>"
    + hbox("This is a genuine research resource. Hundreds of impact assessments are published "
           "every year across sectors and states, and almost nobody reads them systematically. "
           "The variation between them is itself a finding about how evaluation is practised.", "cyan")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 8(3)(b).")

sec("Section 08 &middot; The Missing Counterfactual", "What impact assessment usually is not",
    "<p>The rules require an impact assessment through an <b>independent agency</b> for companies "
    "above the thresholds, but they do not specify a method. In practice most published "
    "assessments report what happened to participants and stop there.</p>"
    + twocol("What is usually reported",
             bullets(["Outputs delivered &mdash; people trained, units built",
                      "Before-and-after values for participants",
                      "Participant satisfaction"]),
             "What would answer the question",
             bullets(["A comparison group that did not receive the programme",
                      "An explicit statement of what would have happened anyway",
                      "Attrition and who is missing from the endline"]))
    + hbox("A before-and-after difference is not an impact estimate unless something rules out "
           "the alternative explanations. This is the same problem the evaluation literature "
           "treats at length &mdash; see our Impact Evaluation 101 and Causal Inference courses.", "amber")
    + SRC % "Companies (CSR Policy) Rules 2014, Rule 8(3).")

# ───────────────────────── 9. BRSR ──────────────────────────────────────────
divider(9, "From Spend To Disclosure", "BRSR and the nine NGRBC principles")

sec("Section 09 &middot; The Shift", "Different obligation, different audience",
    "<p>CSR under Section 135 asks: <i>did you spend, and on what?</i> ESG reporting asks a "
    "different question: <i>how does your business behave, and what does it cost the world?</i> "
    "The audience shifts from the regulator to the investor.</p>"
    + table(["", "Section 135 CSR", "BRSR / ESG"],
            [["Governs", "A spending obligation", "A disclosure obligation"],
             ["Scope", "The CSR budget", "The whole business"],
             ["Audience", "MCA, the board, the public", "Investors, analysts, regulators"],
             ["Regulator", "Ministry of Corporate Affairs", "SEBI"],
             ["Applies to", "Companies over Section 135 thresholds", "Top listed companies by market capitalisation"]])
    + "<p>The two overlap but do not nest. A large unlisted company can be squarely inside "
    "Section 135 and file no BRSR at all; a listed company can file a full BRSR while its CSR "
    "obligation is modest. They are different regimes with different regulators that happen to "
    "share a subject.</p>"
    + hbox("A company can spend its 2% impeccably and still have a poor ESG profile, because the "
           "2% is not where the harm is. This is the most important idea in the section."))

sec("Section 09 &middot; BRSR", "What the format is, and who files it",
    "<p>The <b>Business Responsibility and Sustainability Report</b> is SEBI&rsquo;s mandatory "
    "ESG disclosure format, replacing the earlier Business Responsibility Report. It applies "
    "to the top <b>1,000</b> listed entities by market capitalisation, mandatory from "
    "<b>FY 2022&ndash;23</b>.</p>"
    + "<p>It replaced the Business Responsibility Report, and the change of name marks a "
    "change of scope: the BRR asked mainly about conduct, while the BRSR adds quantitative "
    "environmental and social disclosure and a structure that can be compared across "
    "companies and years.</p>"
    + hbox("Applicability has expanded since introduction, including the BRSR Core subset with "
            "assurance phased in by market-capitalisation rank. Confirm the current position on "
            "sebi.gov.in rather than treating any threshold here as settled &mdash; this is the "
            "fastest-moving part of the whole subject.", "amber")
    + SRC % "SEBI (LODR) Regulations, Regulation 34(2)(f); SEBI circulars on BRSR and BRSR Core.")

sec("Section 09 &middot; NGRBC", "The nine principles underneath",
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

sec("Section 09 &middot; The Structure", "How a BRSR is laid out",
    flow(["Section A: General disclosures", "Section B: Management &amp; process",
          "Section C: Principle-wise performance"])
    + bullets(["<b>Section A</b> &mdash; entity details, products, employees, CSR, transparency",
               "<b>Section B</b> &mdash; policies against each of the nine principles, and governance of them",
               "<b>Section C</b> &mdash; essential and leadership indicators for each principle"])
    + hbox("The essential/leadership split is the useful one. Essential indicators are "
            "mandatory; leadership indicators are voluntary. A company reporting only the "
            "essential set is complying rather than leading, and the format makes that visible "
            "without any judgement on your part &mdash; you can simply count which leadership "
            "indicators were answered and which were left blank.", "cyan")
    + SRC % "SEBI BRSR format, Sections A, B and C.")

sec("Section 09 &middot; Assurance Arrives", "When a number gets checked",
    "<p>SEBI introduced <b>BRSR Core</b>: a defined subset of key performance indicators "
    "requiring <b>reasonable assurance</b>, phased in by market-capitalisation rank, with "
    "disclosure extending into the value chain.</p>"
    + table(["Level", "What the provider says", "Weight it bears"],
            [["None", "Nothing &mdash; the company asserts it", "The company&rsquo;s own claim"],
             ["Limited", "Nothing came to our attention suggesting it is wrong", "Negative comfort"],
             ["Reasonable", "In our opinion the figure is fairly stated", "A positive opinion"]])
    + hbox("Assurance is the difference between a company saying a number and a third party "
           "standing behind it. Reading any ESG claim, the first question is whether it is "
           "assured and at what level &mdash; and most published sustainability numbers, "
           "worldwide, carry none at all.", "cyan")
    + SRC % "SEBI circulars on BRSR Core; verify the current phase-in schedule at sebi.gov.in.")

sec("Section 09 &middot; Greenwashing", "What the format is designed to resist",
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
    + "<p>The boundary question does the most work. A group can report emissions for its "
    "listed parent and exclude the subsidiaries where the manufacturing happens, disclose the "
    "exclusion accurately in a footnote, and produce a headline figure that is true and "
    "useless. Nothing has been misstated; the reader has simply been given a different company "
    "from the one they thought they were reading about.</p>"
    + hbox("These tells work as a checklist, and they transfer directly to any sustainability "
            "report &mdash; Indian or not, corporate or governmental. None of them requires "
            "technical knowledge of the sector; they are questions about how a claim is "
            "constructed.", "amber"))

sec("Section 09 &middot; The Nine Principles", "What NGRBC actually asks",
    "<p>The BRSR is organised around the nine principles of the National Guidelines on "
    "Responsible Business Conduct. Each principle carries essential indicators (mandatory) and "
    "leadership indicators (voluntary).</p>"
    + bullets(["<b>P1</b> Integrity and ethical conduct",
               "<b>P2</b> Goods and services that are safe and sustainable",
               "<b>P3</b> Wellbeing of employees, including value-chain workers",
               "<b>P4</b> Responsiveness to all stakeholders",
               "<b>P5</b> Respect and promotion of human rights",
               "<b>P6</b> Protection and restoration of the environment",
               "<b>P7</b> Responsible and transparent public policy influence",
               "<b>P8</b> Inclusive growth and equitable development",
               "<b>P9</b> Value to consumers in a responsible manner"])
    + "<p>Principle 7 is the one that surprises people: responsible and transparent public "
    "policy influence. It asks a company to disclose the trade and industry bodies it belongs "
    "to and the positions it advocates &mdash; a question CSR reporting never asks, and one "
    "that reaches an activity with far more effect on outcomes than most CSR spending.</p>"
    + hbox("Principle 8 is where CSR itself is reported. The other eight are about how the "
           "business operates &mdash; which is why BRSR is a wider instrument than the CSR "
           "report it contains.", "cyan")
    + SRC % "National Guidelines on Responsible Business Conduct, MCA 2019; SEBI BRSR format.")

sec("Section 09 &middot; What Gets Assured", "BRSR Core, and why it exists",
    "<p>Disclosure without verification is a claim. SEBI introduced <b>BRSR Core</b> &mdash; a "
    "subset of attributes subject to <b>reasonable assurance</b> by an independent assurance "
    "provider, phased in by market capitalisation.</p>"
    + bullets(["Greenhouse gas footprint", "Water footprint", "Energy footprint",
               "Embracing circularity &mdash; waste management",
               "Enhancing employee wellbeing and safety",
               "Enabling gender diversity in business",
               "Enabling inclusive development",
               "Fairness in engaging with customers and suppliers",
               "Openness of business &mdash; concentration of purchases and sales"])
    + "<p>The nine are chosen to be quantitative and comparable rather than comprehensive. "
    "They leave out most of what NGRBC covers, and that is the design: assurance is expensive, "
    "so it is spent on the attributes where a wrong number would most mislead an investor.</p>"
    + hbox("&ldquo;Reasonable&rdquo; assurance is a higher bar than &ldquo;limited&rdquo;. "
           "Limited assurance says nothing came to the assurer&rsquo;s attention; reasonable "
           "assurance is a positive opinion. Which one a number carries changes how much weight "
           "it will bear.", "amber")
    + SRC % "SEBI circular on BRSR Core and assurance, July 2023; applicability phased from FY2023-24.")

sec("Section 09 &middot; How Greenwashing Shows", "Reading disclosure against itself",
    "<p>Greenwashing rarely takes the form of a false number. It usually takes the form of a "
    "true number chosen carefully.</p>"
    + table(["The move", "What to check"],
            [["Intensity instead of absolute", "Emissions per rupee can fall while total emissions rise"],
             ["Scope 1 and 2 only", "Most of a company&rsquo;s footprint is usually Scope 3 &mdash; the value chain"],
             ["A moved baseline year", "A favourable start year makes any trend look better"],
             ["Targets without interim milestones", "A 2070 pledge with nothing before 2040 commits no one currently serving"],
             ["Offsets counted as reductions", "Bought offsets are not the same as emissions not emitted"]])
    + "<p>Each of these has a defensible rationale, which is exactly why they are worth "
    "checking rather than accusing. Intensity metrics genuinely are the right measure for some "
    "questions; baselines genuinely do get restated when a company acquires or divests. The "
    "signal is not any single choice but whether every choice happens to run the same way.</p>"
    + hbox("None of these is a lie, and each is a normal reporting choice with a defensible "
           "rationale. That is what makes them worth checking rather than accusing.", "cyan"))

sec("Section 09 &middot; Reading A BRSR", "Where the disclosure is load-bearing",
    "<p>The BRSR runs to three sections and over a hundred data points. A reader with limited "
    "time gets most of the signal from a few of them.</p>"
    + bullets(["<b>Section A</b> &mdash; turnover, employees, and the products in scope. Establishes what the rest is about.",
               "<b>Section B</b> &mdash; policies against each of the nine NGRBC principles, and whether the board has approved them.",
               "<b>Section C</b> &mdash; the essential and leadership indicators, principle by principle. The numbers live here.",
               "<b>BRSR Core</b> &mdash; the nine attributes subject to reasonable assurance. These are the audited ones."])
    + "<p>Read Section A first and keep it open. Everything in Sections B and C is proportional "
    "to something declared there &mdash; turnover, employee numbers, plant locations &mdash; "
    "and a figure that looks impressive in isolation often looks ordinary once divided by the "
    "size of the business reporting it.</p>"
    + hbox("A policy answered &ldquo;Yes&rdquo; in Section B with no corresponding number in "
           "Section C is a policy that exists on paper. Compare the two sections against each "
           "other before believing either.", "cyan")
    + SRC % "SEBI LODR Regulations, Regulation 34(2)(f); SEBI BRSR Core circular, July 2023.")

# ───────────────────────── 10. Global frameworks ────────────────────────────
divider(10, "Where India Sits", "GRI, TCFD, ISSB, CSRD &mdash; and the gap")

sec("Section 10 &middot; The Landscape", "Why there are so many frameworks",
    "<p>ESG reporting grew from voluntary initiatives rather than a single regulator, so the "
    "field arrived crowded. Consolidation is underway but incomplete.</p>"
    + table(["Framework", "Focus", "Audience"],
            [["GRI", "Impact of the company on the world", "All stakeholders"],
             ["SASB", "Financially material sustainability issues, by industry", "Investors"],
             ["TCFD", "Climate-related financial risk and governance", "Investors, regulators"],
             ["ISSB (IFRS S1, S2)", "Global baseline for sustainability and climate disclosure", "Capital markets"],
             ["CSRD / ESRS", "Mandatory EU sustainability reporting", "EU regulators, investors"]])
    + hbox("Reading the audience column explains most of the differences. GRI was built for "
            "people affected by a company; SASB and ISSB for people investing in it. Those two "
            "purposes select different topics, different materiality tests and different "
            "levels of detail &mdash; which is why a company can look responsible in one "
            "framework and unremarkable in another without either being wrong.", "cyan")
    + SRC % "Framework bodies&rsquo; own documentation. Consolidation is active &mdash; confirm the current position.")

sec("Section 10 &middot; Double Materiality", "The idea that divides the field",
    twocol("Financial materiality",
           "<p>What sustainability issues affect the <b>company&rsquo;s</b> value? Used by SASB "
           "and ISSB. The question an investor asks.</p>",
           "Impact materiality",
           "<p>What effects does the company have on <b>people and the environment</b>? Used by "
           "GRI. The question a community asks.</p>")
    + "<p>The two questions can point in opposite directions. A factory&rsquo;s water use may "
    "be financially immaterial &mdash; water is cheap, supply is secure, no investor cares "
    "&mdash; while being the single most material fact about that factory to the village "
    "sharing the aquifer. Under financial materiality alone, it is not reported.</p>"
    + hbox("<b>Double materiality</b> &mdash; the EU&rsquo;s CSRD position &mdash; requires "
            "both. Which materiality a framework adopts tells you who it was written for, and "
            "it is the fastest way to read the politics of any reporting standard: follow the "
            "question it declines to ask.", "cyan")
    + SRC % "EU CSRD (2022/2464) and ESRS; GRI Standards; ISSB IFRS S1/S2.")

sec("Where BRSR sits", "India&rsquo;s position",
    "<p>BRSR is built on the NGRBC principles and covers both business conduct and "
    "environmental performance, so it sits closer to a broad-stakeholder view than to a purely "
    "investor-financial one &mdash; while BRSR Core&rsquo;s assured KPIs and value-chain reach "
    "move it toward investor-grade comparability.</p>"
    + "<p>It also arrived from a different direction. GRI and SASB grew out of voluntary "
    "investor and civil-society initiatives; BRSR descends from a government guideline "
    "(NGRBC) enforced by a securities regulator. That lineage is why it asks about business "
    "conduct and policy advocacy alongside emissions &mdash; questions an investor-first "
    "framework would not have started with.</p>"
    + hbox("BRSR is India&rsquo;s own instrument rather than a local copy of something else, "
            "and it is worth learning in that order: the NGRBC principles carry across to GRI "
            "readily, while arriving at NGRBC from GRI tends to miss what is distinctive about "
            "it &mdash; the explicit attention to business conduct alongside environmental "
            "performance.", "cyan")
    + SRC % "National Guidelines on Responsible Business Conduct, MCA 2019; SEBI BRSR format.")

sec("Section 10 &middot; The SDGs", "A useful frame with weak accountability",
    "<p>Companies routinely map CSR and ESG activity to the Sustainable Development Goals. "
    "The mapping is genuinely useful for communication and genuinely weak as accountability: "
    "the SDGs were written for states, have no corporate reporting requirement, and almost "
    "any activity can be mapped to at least one goal.</p>"
    + "<p>There are 17 goals, 169 targets and 231 unique indicators. The indicators are the "
    "part with measurement definitions attached, and they are also the part corporate SDG "
    "mapping almost never reaches &mdash; a report will claim alignment with a goal, "
    "occasionally a target, and essentially never an indicator.</p>"
    + hbox("When a report claims to advance eight SDGs, the question is which indicator, at "
            "which target, moved by how much. The answer is usually silence, and the silence is "
            "informative: goal-level alignment costs nothing to assert.", "amber")
    + SRC % "UN Sustainable Development Goals; Global Indicator Framework, UN Statistical Commission.")

sec("Section 10 &middot; Human Rights", "The framework CSR discussions skip",
    "<p>The <b>UN Guiding Principles on Business and Human Rights</b> set out a duty to "
    "protect, a corporate responsibility to respect, and access to remedy &mdash; with human "
    "rights due diligence at the centre. NGRBC Principle 5 carries this into the Indian frame.</p>"
    + hbox("Human rights due diligence is the part of ESG closest to social work practice, and "
           "the part most often thinned out in corporate reporting &mdash; it asks about harms "
           "the business causes, not benefits it funds.", "cyan")
    + "<p>The three pillars are not symmetrical. The state has a duty to <b>protect</b>; the "
    "company has a responsibility to <b>respect</b> &mdash; a lower bar, meaning do no harm "
    "rather than do good; and both owe access to <b>remedy</b> when harm occurs. CSR spending "
    "satisfies none of these, because it is about benefit conferred rather than harm avoided.</p>"
    + SRC % "UN Guiding Principles on Business and Human Rights, 2011; NGRBC Principle 5.")

sec("Section 10 &middot; Value Chains", "Where the harm usually is",
    "<p>A company&rsquo;s own operations are rarely where its worst impacts sit. They sit in "
    "the value chain &mdash; suppliers, contractors, informal labour. Scope 3 emissions, "
    "supplier labour conditions and contract-worker safety are where reporting is thinnest and "
    "the stakes are highest.</p>"
    + hbox("In India this connects directly to informal employment, contract labour and "
            "migrant work &mdash; and the numbers are not marginal. An account of corporate "
            "responsibility that stops at the company gate leaves out most of the workforce "
            "that produced the goods, which is precisely why CSRD makes value-chain reporting "
            "explicit and why BRSR&rsquo;s treatment of it is the part most often called "
            "thin.", "amber")
    + SRC % "UN Guiding Principles on Business and Human Rights; BRSR Core value-chain disclosures.")

sec("Section 10 &middot; Two Frameworks, One Company", "Why the same firm reports twice",
    "<p>An Indian listed company above the BRSR threshold with European customers may be "
    "reporting under BRSR and preparing for CSRD at the same time, and the two ask different "
    "questions of the same operations.</p>"
    + table(["", "BRSR", "CSRD / ESRS"],
            [["Driver", "SEBI listing regulation", "EU law, applied to large EU-active firms"],
             ["Materiality", "Single &mdash; effect on the business", "Double &mdash; and on people and planet"],
             ["Assurance", "Reasonable, on BRSR Core attributes", "Limited, moving to reasonable"],
             ["Value chain", "Limited", "Explicit, including suppliers"]])
    + "<p>For an Indian company this is not a hypothetical. CSRD reaches non-EU companies "
    "with substantial EU turnover, and reaches many more indirectly as suppliers to firms that "
    "are in scope &mdash; who then ask for the value-chain data their own reporting requires. "
    "The obligation arrives through the customer rather than the regulator.</p>"
    + hbox("Double materiality is the substantive difference. A risk that is immaterial to the "
           "company&rsquo;s finances but material to a community is out of scope in the first "
           "column and in scope in the second.", "amber")
    + SRC % "SEBI BRSR framework; EU Corporate Sustainability Reporting Directive (2022/2464) and ESRS.")

# ───────────────────────── 11. Reading critically ───────────────────────────
divider(11, "Reading It Critically", "Ten questions, and how to stay current")

sec("Section 11 &middot; The Core Skill", "What all of it reduces to",
    "<p>Few people who study this will spend a career drafting Section 135 policies. Almost "
    "everyone will have to read reports written by people with an interest in how they are "
    "read, and decide what to believe.</p>"
    + quote("A report is a claim, made by an interested party, in a format that party helped "
            "design. Read it as evidence, not as testimony.",
            "The habit this course is trying to build")
    + "<p>That does not mean assuming bad faith. Most CSR and sustainability reporting is "
    "produced by people trying to describe real work accurately, under formats and deadlines "
    "they did not choose. The discipline is to separate what the document establishes from "
    "what it asserts &mdash; and to notice that the two are laid out to look alike.</p>"
    + hbox("Everything else here &mdash; thresholds, Schedule VII, the unspent machinery, the "
            "BRSR structure &mdash; exists to let you do that separation on a real document. "
            "The law is the equipment; reading is the job.", "cyan"))

sec("Section 11 &middot; Ten Questions", "A checklist for any CSR or ESG report",
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
    + "<p>Nine of the ten can be answered from documents the company is already required to "
    "publish. Only the last needs judgement, and it is the one that most often produces the "
    "finding &mdash; a report whose numbers and narrative disagree has usually had the "
    "narrative written first.</p>"
    + hbox("This checklist is the most transferable thing here. It works on an Indian CSR "
            "annexure, a BRSR, a European sustainability statement or an NGO annual report, "
            "because every question is about how a claim is constructed rather than about the "
            "sector it is made in.", "cyan"))

sec("Section 11 &middot; Common Failures", "What weak reports look like",
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
    + "<p>The two columns fail differently. CSR reporting usually fails by being vague about "
    "what was done; ESG reporting usually fails by being precise about the wrong thing. A "
    "beneficiary count with no definition and an emissions-intensity figure with no absolute "
    "are the same move made in opposite registers.</p>"
    + hbox("None of these is necessarily deceptive. Each is what a reporting team produces "
            "under a deadline when nobody downstream is going to ask. They become tells only "
            "because they cluster: one is an oversight, four together is a pattern.", "cyan")
    + hbox("Both columns describe reports that comply fully with the law. Compliance and candour "
           "are different properties.", "amber"))

sec("Keeping current", "This area changes, and stale advice is dangerous",
    "<p>Thresholds, deadlines, forms, penalty amounts and BRSR applicability have all been "
    "amended since 2014, several times. Do not teach any figure in this deck as permanent.</p>"
    + bullets(["<b>mca.gov.in</b> &mdash; the Companies Act, the CSR Rules, circulars and the CSR FAQ",
               "<b>csr.gov.in</b> &mdash; the national CSR data portal, with company-level spending data",
               "<b>sebi.gov.in</b> &mdash; LODR regulations and BRSR circulars",
               "The company&rsquo;s own website &mdash; policy, committee composition and annual CSR report are all required to be public"])
    + hbox("Checking the primary source directly is a five-minute habit that outlasts "
            "everything else here. Thresholds, deadlines, forms, penalty amounts and BRSR "
            "applicability have all been amended since 2014 &mdash; and every secondary "
            "summary, including this one, is a snapshot of the law on the day it was "
            "written.", "amber"))

sec("Section 11 &middot; csr.gov.in", "A dataset, not just a portal",
    "<p>The national CSR portal publishes company-level CSR spending, by year, sector and "
    "state. It is a genuine dataset and it is open.</p>"
    + bullets(["Which sectors attract the most CSR money &mdash; and which almost none?",
               "How is spending distributed across states? Does it follow need, or follow head offices?",
               "Which companies report large obligations and small spends?"])
    + "<p>The distribution questions are the interesting ones. CSR is generated where "
    "companies are profitable and headquartered, which is not where need is greatest &mdash; so "
    "the geography of CSR spending is a live question about whether a decentralised, "
    "corporate-directed funding stream reaches the districts a public programme would have "
    "prioritised.</p>"
    + hbox("These are real research questions with public data behind them, and very few people "
            "are asking them systematically. The portal reports what companies filed, which is "
            "also its limitation: it is a record of disclosure, not an audit of delivery.", "cyan")
    + SRC % "National CSR Portal, csr.gov.in, Ministry of Corporate Affairs.")

sec("Section 11 &middot; The Honest Summary", "What this course can and cannot settle",
    twocol("Settled",
           bullets(["Who is in scope, and how the 2% is computed",
                    "What Schedule VII covers",
                    "Where unspent money must go, and by when",
                    "What a BRSR contains"]),
           "Contested",
           bullets(["Whether mandated CSR is good policy at all",
                    "Whether Schedule VII&rsquo;s boundaries are the right ones",
                    "Whether impact assessment as practised is evaluation",
                    "Whether ESG disclosure changes corporate behaviour",
                    "Whether two per cent is the right number, or any number is"]))
    + "<p>The left column can be checked against a statute. The right column cannot be settled "
    "by reading harder &mdash; it needs evidence that mostly does not exist yet, and value "
    "judgements that evidence would not settle anyway.</p>"
    + hbox("The left column is settled law; the right column is contested judgement. Anyone who "
            "cannot tell which is which will be badly served by this field &mdash; and the "
            "confusion runs both ways, with firm legal requirements treated as debatable and "
            "open policy questions asserted as settled.", "cyan"))

sec("Section 11 &middot; Going Further", "Where to take this next",
    bullets(["<b>Development Architecture 101</b> &mdash; how development funding is structured, including CSR flows",
             "<b>Climate Essentials 101</b> &mdash; the climate science and policy behind the E in ESG",
             "<b>MEL for Development</b> &mdash; the flagship, for the evaluation half of impact assessment",
             "<b>Theory of Change Studio</b> and <b>Impact Evaluation Studio</b> &mdash; build and defend the designs an assessment needs"])
    + "<p>Two of these matter more than the others depending on where you are going. If you "
    "will be <b>commissioning or reading impact assessments</b>, the MEL flagship and the two "
    "studios are the direct continuation of Section 08. If you will be <b>raising CSR funds</b>, "
    "Development Architecture 101 explains where corporate money sits among the other flows an "
    "organisation might approach.</p>"
    + hbox("Everything listed is free to open on impactmojo.in, with no login. The interactive "
            "CSR map used for the figures in Section 04 is at impactmojo.in/maps/csr-india.html, "
            "and is worth an hour on its own.", "cyan"))



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

CHARTS = """// Charts
const CHART_DEFAULTS = {
  responsive: true, maintainAspectRatio: false,
  plugins: { legend: { labels: { font: { family: 'JetBrains Mono', size: 10 }, color: '#78716C' } } },
  scales: {
    x: { ticks: { font: { family: 'JetBrains Mono', size: 9 }, color: '#78716C' }, grid: { color: 'rgba(0,0,0,0.05)' } },
    y: { ticks: { font: { family: 'JetBrains Mono', size: 9 }, color: '#78716C' }, grid: { color: 'rgba(0,0,0,0.05)' } }
  }
};

function initChart(slideIdx) {
  // Chart.js is a CDN script. A blocked CDN, an offline classroom or a corporate
  // firewall must degrade to a chartless slide with its caption and takeaway still
  // readable -- never a ReferenceError that stops the rest of the deck's JS.
  if (typeof Chart === 'undefined') return;
  const id = SLIDE_IDS[slideIdx];
  const mk = (cid, type, data, opts) => {
    const el = document.getElementById(cid);
    if (!el || el._imChart) return;
    el._imChart = new Chart(el, { type, data, options: { ...CHART_DEFAULTS, ...opts } });
  };

  if (document.getElementById('csrSectorChart')) {
    mk('csrSectorChart', 'bar', {
      labels: ['Health & sanitation','Education & skilling','Other heads','Environment','Rural development'],
      datasets: [{ label: 'Rs crore, FY2023-24', data: [13400, 11300, 3980, 3800, 2410],
        backgroundColor: ['#DC2626','#2563EB','#64748B','#0F766E','#D97706'] }]
    }, { indexAxis: 'y', plugins: { legend: { display: false } },
         scales: { x: { beginAtZero: true, title: { display: true, text: 'Rs crore' } } } });
  }

  if (document.getElementById('csrTopTenChart')) {
    mk('csrTopTenChart', 'bar', {
      labels: ['HDFC Bank','Reliance','TCS','ONGC','Tata Steel','Infosys','Indian Oil','Reliance Jio','ITC','ICICI Bank'],
      datasets: [{ label: 'Rs crore, FY2023-24', data: [945,900,813,612,573,451,436,403,380,368],
        backgroundColor: '#7C3AED' }]
    }, { indexAxis: 'y', plugins: { legend: { display: false } },
         scales: { x: { beginAtZero: true, title: { display: true, text: 'Rs crore' } } } });
  }
}


"""

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
    charts_js=CHARTS,
)
print("BUILT: 101-courses/csr-esg.html  (%d slides)" % len(slides))
