#!/usr/bin/env python3
"""Logframe 101 - the logical framework, built from the results chain up."""
import deck_builder as db

slides = []


def content(inner):
    slides.append(('content', inner))


def divider(num, label, title):
    slides.append(('divider', (num, label, title)))


slides.append(('title', None))
TOC = [
    ("What a Logframe Is", "3&ndash;9"),
    ("The Results Chain", "10&ndash;18"),
    ("Inputs, Activities, Outputs", "19&ndash;29"),
    ("Outcomes &amp; Impact", "30&ndash;40"),
    ("Indicators", "41&ndash;49"),
    ("Means of Verification", "50&ndash;57"),
    ("Assumptions", "58&ndash;64"),
    ("Risk", "65&ndash;73"),
    ("Building the Matrix", "74&ndash;81"),
    ("Critiques &amp; Limits", "82&ndash;89"),
    ("Tools &amp; Practice", "90&ndash;98"),
]
slides.append(('toc', TOC))

# ============ SECTION 1: What a Logframe Is (6) ============
divider(1, "Section One", "What a Logframe Is")

content('<div class="section-label">Definition</div>'
        '<div class="term-box"><div class="term-word">Logical framework (logframe)</div>'
        '<div class="term-def">A one-page matrix that lays out what a project is trying to achieve, how it will get '
        'there, how you will know if it worked, and what has to hold true for the logic to run. Rows are levels of '
        'result; columns are the indicator, its source, and the assumptions.</div></div>'
        '<div class="slide-body">It is two things at once: a <strong>planning</strong> tool that forces you to think '
        'through your logic, and a <strong>management</strong> tool you return to as the project runs.</div>')

content('<div class="section-label">The shape</div>'
        '<div class="slide-title md">A 4&times;4 grid, read two ways</div>'
        '<table class="ctable"><thead><tr><th>Results level</th><th>Indicator</th><th>Means of verification</th><th>Assumptions</th></tr></thead>'
        '<tbody>'
        '<tr><td><strong>Impact / Goal</strong></td><td>How measured</td><td>Where the data comes from</td><td>What must hold</td></tr>'
        '<tr><td><strong>Outcome / Purpose</strong></td><td>How measured</td><td>Source</td><td>Assumption</td></tr>'
        '<tr><td><strong>Outputs</strong></td><td>How measured</td><td>Source</td><td>Assumption</td></tr>'
        '<tr><td><strong>Activities</strong> (&amp; inputs)</td><td>How measured</td><td>Source</td><td>Assumption</td></tr>'
        '</tbody></table>'
        '<div class="hbox"><div class="hbox-text">Read <strong>down</strong> the first column for the story of change; '
        'read <strong>across</strong> a row to see how each result is measured and what it depends on.</div></div>')

content('<div class="section-label">Where it came from</div>'
        '<div class="slide-title md">A short history</div>'
        '<div class="slide-body">The logframe was developed for <strong>USAID in 1969</strong> by Leon Rosenberg and '
        'colleagues, to bring discipline to vague project plans. It spread through bilateral and UN agencies, was '
        'adapted by GTZ into the participatory <strong>ZOPP / objectives-oriented planning</strong> method, and '
        'remains a near-universal donor requirement today &mdash; the EU, DFID/FCDO, GIZ, the UN and most large '
        'NGOs all use a version.</div>'
        '<div class="hbox amber"><div class="hbox-text">Because so many donors mandate it, the logframe is often the '
        'first formal document a funded project produces. Knowing it well is a practical survival skill.</div></div>')

content('<div class="section-label">Why bother</div>'
        '<div class="slide-title md">What a good logframe gives you</div>'
        '<ul class="bullet-list green">'
        '<li><strong>A testable theory.</strong> It states, on one page, the if&ndash;then logic your project is betting on.</li>'
        '<li><strong>Shared language.</strong> Funder, manager and field team mean the same thing by &ldquo;outcome&rdquo;.</li>'
        '<li><strong>A monitoring spine.</strong> The indicators column tells you exactly what to collect.</li>'
        '<li><strong>Honesty about risk.</strong> The assumptions column makes you name what could break.</li>'
        '</ul>')

content('<div class="section-label">What it is not</div>'
        '<div class="slide-title md">A logframe is not the whole plan</div>'
        '<div class="slide-body">The matrix is a summary, not a substitute for a theory of change, a work plan, a '
        'budget or a risk register. It compresses a rich design into a grid &mdash; useful for discipline and '
        'reporting, dangerous if mistaken for the full picture.</div>'
        '<div class="hbox red"><div class="hbox-text">Filling in the boxes is not the same as having a sound design. '
        'A neat logframe over a weak theory is just tidy wishful thinking.</div></div>')

content('<div class="section-label">The family</div>'
        '<div class="slide-title md">Logframe, theory of change, results framework</div>'
        '<table class="ctable"><thead><tr><th>Tool</th><th>What it is</th><th>Strength</th></tr></thead><tbody>'
        '<tr><td>Theory of change</td><td>A narrative + diagram of how and why change happens</td><td>Rich, shows pathways &amp; mechanisms</td></tr>'
        '<tr><td>Results framework</td><td>A hierarchy of objectives and sub-objectives</td><td>Good for portfolios / strategy</td></tr>'
        '<tr><td>Logframe</td><td>A matrix of results, indicators, sources, assumptions</td><td>Compact, measurable, donor-ready</td></tr>'
        '</tbody></table>'
        '<div class="hbox indigo"><div class="hbox-text">Best practice: build the <strong>theory of change first</strong>, '
        'then summarise its causal spine into the logframe. The logframe is the ToC, disciplined into a grid.</div></div>')

# ============ SECTION 2: The Results Chain (8) ============
divider(2, "Section Two", "The Results Chain")

content('<div class="section-label">The spine</div>'
        '<div class="slide-title md">The results chain</div>'
        '<div class="flow">'
        '<div class="flow-step"><div class="flow-num">IN</div><div class="flow-label">Inputs</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">ACT</div><div class="flow-label">Activities</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">OUT</div><div class="flow-label">Outputs</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">OC</div><div class="flow-label">Outcomes</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">IMP</div><div class="flow-label">Impact</div></div>'
        '</div>'
        '<div class="hbox"><div class="hbox-text">Everything in a logframe hangs on this chain. The first job is to '
        'know exactly which link a given result belongs to &mdash; that is where most logframes go wrong.</div></div>')

content('<div class="section-label">The dividing line</div>'
        '<div class="slide-title md">What you control vs. what you influence</div>'
        '<div class="two-col half">'
        '<div class="col-panel green"><div class="col-panel-title">Your sphere of control</div>'
        '<div class="slide-body sm">Inputs, activities and outputs. If you do the work, these happen. You are '
        '<strong>accountable</strong> for them.</div></div>'
        '<div class="col-panel amber"><div class="col-panel-title">Your sphere of influence</div>'
        '<div class="slide-body sm">Outcomes and impact. These depend on how others respond &mdash; participants, '
        'systems, the wider world. You <strong>contribute</strong>; you do not solely cause them.</div></div></div>'
        '<div class="hbox red"><div class="hbox-text">The single most common logframe error is promising an '
        '<em>outcome</em> as if it were an <em>output</em> &mdash; claiming control over something you can only influence.</div></div>')

content('<div class="section-label">If&ndash;then</div>'
        '<div class="slide-title md">The chain is a stack of hypotheses</div>'
        '<div class="slide-body">Read upward, each level is an <em>if&ndash;then</em> claim: <em>if</em> we combine these '
        'inputs, <em>then</em> we can run these activities; <em>if</em> the activities happen, <em>then</em> we get '
        'these outputs; and so on. Each step is a bet that can fail.</div>'
        '<div class="hbox"><div class="hbox-text">The assumptions column (later) holds the &ldquo;and these other things '
        'also have to be true&rdquo; that each <em>if&ndash;then</em> quietly depends on.</div></div>')

content('<div class="section-label">Direction</div>'
        '<div class="slide-title md">Plan top-down, deliver bottom-up</div>'
        '<div class="slide-body">When you <strong>design</strong>, start from the impact you want and work down: what '
        'outcome would contribute to it, what outputs would produce that outcome, what activities make those outputs. '
        'When you <strong>implement</strong>, you move the other way: inputs fund activities that yield outputs.</div>'
        '<div class="hbox green"><div class="hbox-text">Designing downward keeps you honest &mdash; every activity has '
        'to earn its place by pointing at the result above it. Activities with no result above them are busywork.</div></div>')

content('<div class="section-label">A worked chain</div>'
        '<div class="slide-title md">One example, all the way up</div>'
        '<table class="ctable"><thead><tr><th>Level</th><th>Example (girls&rsquo; education programme)</th></tr></thead><tbody>'
        '<tr><td>Impact</td><td>Women&rsquo;s economic and social participation rises in the district</td></tr>'
        '<tr><td>Outcome</td><td>More girls complete secondary school</td></tr>'
        '<tr><td>Output</td><td>2,000 girls receive scholarships and after-school tutoring</td></tr>'
        '<tr><td>Activity</td><td>Recruit tutors; disburse scholarships; run classes</td></tr>'
        '<tr><td>Input</td><td>Funds, teachers, classrooms, materials</td></tr>'
        '</tbody></table>'
        '<div class="hbox"><div class="hbox-text">Notice the jump from output (girls enrolled and tutored) to outcome '
        '(girls completing school): that gap is where families, schools and the economy must cooperate.</div></div>')

content('<div class="section-label">Common confusion</div>'
        '<div class="slide-title md">Output or outcome? A quick test</div>'
        '<ul class="bullet-list sm">'
        '<li><strong>Output</strong> = the goods and services you deliver. &ldquo;500 health workers trained.&rdquo; '
        'It is done when you have done it.</li>'
        '<li><strong>Outcome</strong> = the change in others&rsquo; behaviour, knowledge or condition. &ldquo;Health '
        'workers correctly manage childhood illness.&rdquo; It depends on whether the training took.</li>'
        '</ul>'
        '<div class="hbox amber"><div class="hbox-text">Test: <em>could you report this complete the day you finish '
        'delivery?</em> If yes, it is an output. If it needs someone else to change, it is an outcome.</div></div>')

content('<div class="section-label">Attribution</div>'
        '<div class="slide-title md">The higher you climb, the less it is just you</div>'
        '<div class="slide-body">At output level, your project is the cause. At outcome level, you are one of several '
        'forces. At impact level, you are a small contributor among many &mdash; economic conditions, government policy, '
        'other programmes. This is the <strong>attribution gap</strong>.</div>'
        '<div class="hbox red"><div class="hbox-text">Claim <em>contribution</em>, not sole credit, for outcomes and '
        'impact. Over-claiming at the top of the chain is both dishonest and, when measured, easily disproved.</div></div>')

content('<div class="section-label">See it drawn</div>'
        '<div class="slide-title md">The chain, visualised</div>'
        '<div class="slide-body">ImpactMojo&rsquo;s <strong>The Long View</strong> includes an original diagram of the '
        'results chain and the attribution gap &mdash; the widening distance between what a project delivers and the '
        'change it hopes to see. It is the picture behind this whole section.</div>'
        '<div class="hbox indigo"><div class="hbox-text">A logframe is the results chain, written as a table. Keep the '
        'picture in your head as you fill in the rows.</div></div>')

# ============ SECTION 3: Inputs, Activities, Outputs (10) ============
divider(3, "Section Three", "Inputs, Activities, Outputs")

content('<div class="section-label">Inputs</div>'
        '<div class="slide-title md">Inputs: what you put in</div>'
        '<div class="slide-body">Inputs are the resources a project consumes: money, staff time, equipment, vehicles, '
        'training materials, partner contributions. In many logframe formats inputs sit alongside activities on the '
        'bottom row, often linked to the budget.</div>'
        '<ul class="bullet-list sm">'
        '<li>Be specific enough to cost: &ldquo;12 community mobilisers for 18 months&rdquo;, not &ldquo;staff&rdquo;.</li>'
        '<li>Include partner and community contributions (land, volunteer time) &mdash; they are real inputs.</li>'
        '</ul>')

content('<div class="section-label">Activities</div>'
        '<div class="slide-title md">Activities: what you do</div>'
        '<div class="slide-body">Activities are the actions that convert inputs into outputs: train, build, distribute, '
        'mobilise, advise. Write them as verbs. Each activity should connect clearly to an output above it.</div>'
        '<div class="hbox amber"><div class="hbox-text">Keep the logframe to a manageable set of activity <em>clusters</em> '
        '(say 3&ndash;6 per output). The detailed task list belongs in the work plan, not the matrix.</div></div>')

content('<div class="section-label">Outputs</div>'
        '<div class="slide-title md">Outputs: what you produce</div>'
        '<div class="slide-body">Outputs are the direct, countable products of your activities &mdash; the goods and '
        'services in the hands of participants. They are fully within your control, so they are written as '
        '<strong>completed deliverables</strong>.</div>'
        '<ul class="bullet-list green">'
        '<li>&ldquo;1,500 farmers trained in drip irrigation&rdquo;</li>'
        '<li>&ldquo;20 village water committees formed and functional&rdquo;</li>'
        '<li>&ldquo;A district nutrition dashboard built and handed over&rdquo;</li>'
        '</ul>')

content('<div class="section-label">Verbs &amp; tense</div>'
        '<div class="slide-title md">Phrase each level in its own grammar</div>'
        '<table class="ctable"><thead><tr><th>Level</th><th>Phrasing</th><th>Example</th></tr></thead><tbody>'
        '<tr><td>Activity</td><td>Verb (the doing)</td><td>Train health workers</td></tr>'
        '<tr><td>Output</td><td>Delivered / completed</td><td>500 health workers trained</td></tr>'
        '<tr><td>Outcome</td><td>Change of state in others</td><td>Health workers apply IMNCI protocols</td></tr>'
        '<tr><td>Impact</td><td>Higher-order condition</td><td>Under-5 mortality falls</td></tr>'
        '</tbody></table>'
        '<div class="hbox"><div class="hbox-text">Consistent phrasing is not pedantry &mdash; mixing an activity verb '
        'into an outcome row is the surface sign of muddled logic underneath.</div></div>')

content('<div class="section-label">One result per box</div>'
        '<div class="slide-title md">No smuggling with &ldquo;and&rdquo;</div>'
        '<div class="slide-body">A statement with an &ldquo;and&rdquo; in it is usually two results hiding in one box: '
        '&ldquo;farmers trained <em>and</em> adopting new methods&rdquo; bundles an output with an outcome. Split them.</div>'
        '<div class="hbox red"><div class="hbox-text">Each box should carry exactly one result, measurable on its own. '
        'If you cannot put a single indicator on it, it is doing too many jobs.</div></div>')

content('<div class="section-label">How many?</div>'
        '<div class="slide-title md">Keep the matrix small</div>'
        '<div class="slide-body">A workable logframe has <strong>one impact, one (sometimes two) outcomes, and a '
        'handful of outputs</strong> &mdash; rarely more than five or six. More than that and the matrix stops being a '
        'one-page summary and becomes an unreadable spreadsheet nobody returns to.</div>'
        '<div class="hbox amber"><div class="hbox-text">If you have ten outputs, you probably have two projects, or you '
        'have listed activities in the output row. Consolidate.</div></div>')

content('<div class="section-label">The vertical test</div>'
        '<div class="slide-title md">Read the logic upward and challenge it</div>'
        '<div class="slide-body">Once the left column is drafted, test it: at each step, ask <em>&ldquo;is this enough '
        'to plausibly produce the level above?&rdquo;</em> If outputs alone clearly will not deliver the outcome, the '
        'design has a gap &mdash; or there is an assumption you have not yet named.</div>'
        '<div class="hbox green"><div class="hbox-text">This upward read is the heart of the &ldquo;logical&rdquo; in '
        'logical framework. A logframe that fails it is just a list.</div></div>')

content('<div class="section-label">Worked rows</div>'
        '<div class="slide-title md">Inputs to outputs, filled in</div>'
        '<table class="ctable"><thead><tr><th>Level</th><th>Statement</th></tr></thead><tbody>'
        '<tr><td>Output 1</td><td>800 adolescent girls enrolled in after-school STEM clubs</td></tr>'
        '<tr><td>Activities</td><td>Set up 40 clubs; recruit &amp; train 40 facilitators; supply kits</td></tr>'
        '<tr><td>Inputs</td><td>40 facilitators, club kits, venue agreements, &#8377;X budget</td></tr>'
        '</tbody></table>'
        '<div class="hbox"><div class="hbox-text">Notice the output is countable (800 girls, 40 clubs) and complete on '
        'delivery &mdash; exactly what makes it an output and not an outcome.</div></div>')

content('<div class="section-label">Costing the chain</div>'
        '<div class="slide-title md">Tie inputs to the budget</div>'
        '<div class="slide-body">Inputs are the bridge between the logframe and the budget. A well-built logframe lets '
        'a reader trace money to activity to output: this is what makes it a management tool, not just a planning '
        'artefact. Donors increasingly ask for cost per output (unit economics).</div>'
        '<div class="hbox indigo"><div class="hbox-text">For more on cost per result, see ImpactMojo&rsquo;s '
        '<strong>Cost-Effectiveness 101</strong> and <strong>Public Finance &amp; Budgeting</strong> courses.</div></div>')

content('<div class="section-label">Section recap</div>'
        '<div class="slide-title md">The bottom half, in one line</div>'
        '<div class="hbox green"><div class="hbox-text"><strong>Inputs</strong> fund <strong>activities</strong> that '
        'produce <strong>outputs</strong> &mdash; all within your control, all written as you-did-it deliverables. The '
        'interesting, riskier half of the chain comes next.</div></div>'
        '<div class="slide-body">Get this half tight and countable, and the monitoring almost writes itself. Get it '
        'muddled, and no amount of indicator-crafting upstream will save the matrix.</div>')

# ============ SECTION 4: Outcomes & Impact (10) ============
divider(4, "Section Four", "Outcomes &amp; Impact")

content('<div class="section-label">Outcomes</div>'
        '<div class="slide-title md">Outcomes: the change you are really after</div>'
        '<div class="slide-body">An outcome is the change in behaviour, knowledge, relationships or condition that your '
        'outputs are meant to bring about. It is usually the <strong>purpose</strong> of the project &mdash; the single '
        'most important row in the matrix, and the hardest to write well.</div>'
        '<div class="hbox"><div class="hbox-text">If the impact is the destination and outputs are what you hand over, '
        'the outcome is the <em>uptake</em> &mdash; what people actually do differently because of what you delivered.</div></div>')

content('<div class="section-label">Impact</div>'
        '<div class="slide-title md">Impact: the higher purpose</div>'
        '<div class="slide-body">Impact (or goal) is the long-term, higher-level change your project contributes to: '
        'lower mortality, higher incomes, greater equality. It is usually shared with other actors and other '
        'programmes, realised over years, and beyond any single project to deliver alone.</div>'
        '<div class="hbox amber"><div class="hbox-text">State the impact you contribute to, but do not pretend to own '
        'it. &ldquo;Contributes to reduced child stunting in the district&rdquo; is honest; &ldquo;reduces stunting&rdquo; '
        'alone over-claims.</div></div>')

content('<div class="section-label">One purpose</div>'
        '<div class="slide-title md">Why most logframes allow only one outcome</div>'
        '<div class="slide-body">Classic logframe discipline insists on a <strong>single purpose / outcome</strong>. The '
        'reason is focus: a project chasing three outcomes usually does none well, and the matrix can no longer show a '
        'clean line of logic. If you genuinely have two, ask whether they are really two projects.</div>'
        '<div class="hbox red"><div class="hbox-text">Multiple outcomes are a warning sign, not an achievement. They '
        'often hide a lack of decision about what the project is actually for.</div></div>')

content('<div class="section-label">Writing an outcome</div>'
        '<div class="slide-title md">A good outcome statement</div>'
        '<ul class="bullet-list green">'
        '<li>Describes a change in <strong>someone other than the project</strong> (participants, institutions).</li>'
        '<li>Is realistic given the outputs &mdash; reachable within the project, not a wish.</li>'
        '<li>Is measurable: you can name an indicator that would move if it were true.</li>'
        '<li>Names the target group: <em>whose</em> behaviour or condition changes.</li>'
        '</ul>'
        '<div class="hbox"><div class="hbox-text">&ldquo;Smallholder farmers in 40 villages adopt and sustain drip '
        'irrigation&rdquo; &mdash; change, in named others, plausibly caused by the outputs, and measurable.</div></div>')

content('<div class="section-label">The big jump</div>'
        '<div class="slide-title md">Mind the output&ndash;outcome gap</div>'
        '<div class="slide-body">The leap from output to outcome is where projects most often fail &mdash; and where the '
        'assumptions matter most. Training delivered (output) does not guarantee practice changed (outcome); a clinic '
        'built does not guarantee it is used. Name what has to happen in between.</div>'
        '<div class="hbox amber"><div class="hbox-text">If you cannot explain <em>why</em> the outputs would lead to the '
        'outcome, you do not yet have a theory of change &mdash; you have a list of hopes.</div></div>')

content('<div class="section-label">Behaviour</div>'
        '<div class="slide-title md">Most outcomes are behaviour change</div>'
        '<div class="slide-body">In development work, the outcome is usually that some group <em>does something '
        'differently</em>: farmers adopt, mothers attend, officials enforce, girls stay in school. Behaviour is '
        'influenced by far more than your project, which is exactly why outcomes sit in the sphere of influence.</div>'
        '<div class="hbox indigo"><div class="hbox-text">Designing for behaviour change is its own craft &mdash; see '
        'ImpactMojo&rsquo;s <strong>Behaviour-Change Communication</strong> course and BCT repository.</div></div>')

content('<div class="section-label">Time</div>'
        '<div class="slide-title md">Results take time to appear</div>'
        '<div class="slide-body">Outputs land during the project; outcomes often emerge near or after its end; impact '
        'may take years. A logframe measured only at project close can miss the outcomes it was built to create &mdash; '
        'and credit impacts that have not yet had time to form.</div>'
        '<div class="hbox"><div class="hbox-text">Match your measurement timing to where each result sits in time. '
        'Some outcomes need a follow-up survey months after the last activity.</div></div>')

content('<div class="section-label">Worked top rows</div>'
        '<div class="slide-title md">Outcome and impact, filled in</div>'
        '<table class="ctable"><thead><tr><th>Level</th><th>Statement</th></tr></thead><tbody>'
        '<tr><td>Impact</td><td>Contributes to higher and more resilient incomes for smallholder households</td></tr>'
        '<tr><td>Outcome</td><td>Farmers in 40 villages adopt and sustain water-efficient irrigation</td></tr>'
        '<tr><td>Output</td><td>1,500 farmers trained and equipped with drip-irrigation kits</td></tr>'
        '</tbody></table>'
        '<div class="hbox green"><div class="hbox-text">&ldquo;Contributes to&rdquo; at impact, a behaviour change at '
        'outcome, a countable deliverable at output &mdash; each row in its proper grammar.</div></div>')

content('<div class="section-label">Sustainability</div>'
        '<div class="slide-title md">Will it last past the project?</div>'
        '<div class="slide-body">A strong outcome statement often carries a hint of durability &mdash; &ldquo;adopt '
        '<em>and sustain</em>&rdquo;. Donors increasingly ask not just whether change happened, but whether it will '
        'hold once funding ends. That depends on systems, ownership and incentives, not just your outputs.</div>'
        '<div class="hbox amber"><div class="hbox-text">Sustainability usually lives in the assumptions and in the exit '
        'strategy. Name who keeps the change alive after you leave.</div></div>')

content('<div class="section-label">Section recap</div>'
        '<div class="slide-title md">The top half, in one line</div>'
        '<div class="hbox green"><div class="hbox-text"><strong>Outputs</strong> are taken up as <strong>outcomes</strong> '
        '(behaviour change in others) which <strong>contribute to</strong> <strong>impact</strong> (higher-order '
        'change). You control the first, influence the second, and merely contribute to the third.</div></div>'
        '<div class="slide-body">With the left column complete, the next job is to make each row measurable. That is '
        'the indicators column.</div>')

# ============ SECTION 5: Indicators (8) ============
divider(5, "Section Five", "Indicators")

content('<div class="section-label">Definition</div>'
        '<div class="term-box"><div class="term-word">Indicator (OVI)</div>'
        '<div class="term-def">An <strong>objectively verifiable indicator</strong> is a specific, measurable sign that '
        'a result has been achieved. It answers: &ldquo;how would we know?&rdquo; For each row of the chain you name at '
        'least one indicator that would move if that result were real.</div></div>'
        '<div class="slide-body">&ldquo;Objectively verifiable&rdquo; means two people measuring it independently would '
        'get the same answer &mdash; no judgement call required.</div>')

content('<div class="section-label">SMART</div>'
        '<div class="slide-title md">Make every indicator SMART</div>'
        '<div class="stat-grid c3">'
        '<div class="stat-card"><div class="stat-number">S&middot;M</div><div class="stat-label"><strong>Specific</strong> &amp; '
        '<strong>Measurable</strong> &mdash; clear what, countable how</div></div>'
        '<div class="stat-card indigo"><div class="stat-number">A&middot;R</div><div class="stat-label"><strong>Achievable</strong> &amp; '
        '<strong>Relevant</strong> &mdash; realistic, and tied to the result</div></div>'
        '<div class="stat-card green"><div class="stat-number">T</div><div class="stat-label"><strong>Time-bound</strong> '
        '&mdash; by when</div></div>'
        '</div>'
        '<div class="hbox"><div class="hbox-text">&ldquo;% of trained midwives correctly performing newborn '
        'resuscitation, measured by observation, rising from 40% to 80% by end of year 2.&rdquo;</div></div>')

content('<div class="section-label">Anatomy</div>'
        '<div class="slide-title md">A full indicator has four parts</div>'
        '<ul class="bullet-list">'
        '<li><strong>Unit / what</strong> &mdash; % of women, number of villages, rate per 1,000.</li>'
        '<li><strong>Baseline</strong> &mdash; the value at the start. Without it you cannot show change.</li>'
        '<li><strong>Target</strong> &mdash; the value you commit to reach, by a date.</li>'
        '<li><strong>Disaggregation</strong> &mdash; by sex, age, caste, location, disability.</li>'
        '</ul>'
        '<div class="hbox red"><div class="hbox-text">An indicator with no baseline is the most common logframe fault. '
        'A target without a starting point measures nothing.</div></div>')

content('<div class="section-label">Quant &amp; qual</div>'
        '<div class="slide-title md">Numbers and judgements both count</div>'
        '<div class="two-col half">'
        '<div class="col-panel"><div class="col-panel-title">Quantitative</div>'
        '<div class="slide-body sm">Counts, rates, percentages, scores. Easy to verify, easy to aggregate &mdash; but '
        'can miss the &ldquo;why&rdquo;.</div></div>'
        '<div class="col-panel green"><div class="col-panel-title">Qualitative</div>'
        '<div class="slide-body sm">Quality of participation, perceived fairness, case stories. Harder to verify; use '
        'a defined scale or rubric so it stays objective.</div></div></div>'
        '<div class="hbox"><div class="hbox-text">The best logframes mix both: a number for &ldquo;how much&rdquo; and a '
        'qualitative measure for &ldquo;how well&rdquo;.</div></div>')

content('<div class="section-label">Proxies</div>'
        '<div class="slide-title md">When you can&rsquo;t measure it directly</div>'
        '<div class="slide-body">Some results &mdash; empowerment, resilience, trust &mdash; have no direct meter. A '
        '<strong>proxy indicator</strong> stands in: e.g. women&rsquo;s control over household spending as a proxy for '
        'empowerment. Choose proxies carefully and state that they are proxies.</div>'
        '<div class="hbox amber"><div class="hbox-text">Beware Goodhart&rsquo;s law: <em>when a measure becomes a target, '
        'it stops being a good measure.</em> People optimise the proxy, not the thing you cared about.</div></div>')

content('<div class="section-label">Too many</div>'
        '<div class="slide-title md">A few good indicators beat many weak ones</div>'
        '<div class="slide-body">Every indicator is a data-collection commitment. One or two strong indicators per '
        'result is usually enough; a logframe with forty indicators becomes a monitoring burden that crowds out '
        'actually running the project.</div>'
        '<div class="hbox red"><div class="hbox-text">Before adding an indicator, ask: <em>who will collect this, how '
        'often, and what decision will it inform?</em> If there is no answer, drop it.</div></div>')

content('<div class="section-label">Standard sets</div>'
        '<div class="slide-title md">Borrow indicators where you can</div>'
        '<div class="slide-body">Many sectors have agreed indicator sets &mdash; the SDG indicators, WHO and DHS health '
        'indicators, education access measures, IRIS+ for impact investing. Using standard definitions makes your '
        'results comparable and saves you re-inventing measurement.</div>'
        '<div class="hbox indigo"><div class="hbox-text">Match to national data where you can (NFHS, Census, PLFS) so '
        'your baseline and target sit in a context readers already know.</div></div>')

content('<div class="section-label">Worked indicators</div>'
        '<div class="slide-title md">Indicators across the chain</div>'
        '<table class="ctable"><thead><tr><th>Result</th><th>Indicator (with baseline &rarr; target)</th></tr></thead><tbody>'
        '<tr><td>Output</td><td>No. of farmers trained: 0 &rarr; 1,500 by Q6 (disagg. by sex)</td></tr>'
        '<tr><td>Outcome</td><td>% of trained farmers still using drip at 12 months: &ndash; &rarr; 60%</td></tr>'
        '<tr><td>Impact</td><td>Mean kharif income of participant households: baseline survey &rarr; +20%</td></tr>'
        '</tbody></table>'
        '<div class="hbox green"><div class="hbox-text">Each indicator carries a unit, a baseline, a target and a date '
        '&mdash; and gets harder to attribute the higher you go. That is honest measurement.</div></div>')

# ============ SECTION 6: Means of Verification (7) ============
divider(6, "Section Six", "Means of Verification")

content('<div class="section-label">Definition</div>'
        '<div class="term-box"><div class="term-word">Means of verification (MoV)</div>'
        '<div class="term-def">The third column: <strong>where the data for each indicator comes from</strong>, who '
        'collects it, how often, and how. If the indicator says &ldquo;what we measure&rdquo;, the MoV says &ldquo;how '
        'we will actually get that number&rdquo;.</div></div>'
        '<div class="slide-body">An indicator with no realistic means of verification is a promise you cannot keep. '
        'The two columns must be designed together.</div>')

content('<div class="section-label">Sources</div>'
        '<div class="slide-title md">Where verification data comes from</div>'
        '<ul class="bullet-list sm">'
        '<li><strong>Project records</strong> &mdash; attendance sheets, distribution logs, training registers (cheap, for outputs).</li>'
        '<li><strong>Surveys</strong> &mdash; baseline / midline / endline of participants (for outcomes).</li>'
        '<li><strong>Observation</strong> &mdash; direct checks of practice or quality.</li>'
        '<li><strong>Official statistics</strong> &mdash; NFHS, Census, administrative data (for impact / context).</li>'
        '<li><strong>Independent reports</strong> &mdash; third-party evaluations, audits.</li>'
        '</ul>')

content('<div class="section-label">The reality check</div>'
        '<div class="slide-title md">MoV is where ambition meets the budget</div>'
        '<div class="slide-body">Filling in the MoV column is a cost test. A fancy outcome indicator that needs a '
        '5,000-household panel survey may be unaffordable. If you cannot pay to verify it, you cannot claim it &mdash; '
        'so revise the indicator to something you can actually measure.</div>'
        '<div class="hbox red"><div class="hbox-text">Every indicator&rsquo;s MoV has a price. The monitoring budget is '
        'set, in effect, in this column &mdash; plan for it (often 5&ndash;10% of project cost).</div></div>')

content('<div class="section-label">Frequency</div>'
        '<div class="slide-title md">How often, and who</div>'
        '<div class="slide-body">A good MoV entry names the <strong>method</strong>, the <strong>frequency</strong> and '
        'the <strong>responsible person</strong>: &ldquo;observation checklist, quarterly, by the M&amp;E officer&rdquo;. '
        'Output data is usually continuous; outcome surveys are periodic; impact data may come once, at endline or '
        'after.</div>'
        '<div class="hbox"><div class="hbox-text">Tie the frequency to decisions: collect output data often enough to '
        'course-correct, but do not survey outcomes so often that measurement disrupts the work.</div></div>')

content('<div class="section-label">Quality</div>'
        '<div class="slide-title md">Verifiable means trustworthy</div>'
        '<div class="slide-body">The point of the MoV column is credibility: a sceptical reader (or auditor, or '
        'evaluator) should be able to follow it to the same conclusion. That means the source must be reliable, the '
        'method consistent, and the data retained.</div>'
        '<ul class="bullet-list sm">'
        '<li>Prefer sources someone else could independently check.</li>'
        '<li>Keep the raw data, not just the summary, so claims can be re-verified.</li>'
        '<li>For self-reported data, note the bias and triangulate where it matters.</li>'
        '</ul>')

content('<div class="section-label">Worked MoV</div>'
        '<div class="slide-title md">Indicator and its verification, paired</div>'
        '<table class="ctable"><thead><tr><th>Indicator</th><th>Means of verification</th></tr></thead><tbody>'
        '<tr><td>1,500 farmers trained</td><td>Training registers, ongoing, M&amp;E officer</td></tr>'
        '<tr><td>60% still using drip at 12 months</td><td>Follow-up sample survey of 300 farmers, year 2, external enumerators</td></tr>'
        '<tr><td>+20% kharif income</td><td>Baseline &amp; endline household survey; cross-checked with mandi records</td></tr>'
        '</tbody></table>'
        '<div class="hbox green"><div class="hbox-text">Cheap records for outputs, a sample survey for the outcome, a '
        'before/after survey for impact &mdash; cost rising with the level, as it should.</div></div>')

content('<div class="section-label">Connecting M&amp;E</div>'
        '<div class="slide-title md">The logframe is your M&amp;E plan&rsquo;s backbone</div>'
        '<div class="slide-body">Columns two and three &mdash; indicators and means of verification &mdash; are, in '
        'effect, your monitoring plan. A fuller M&amp;E plan just adds detail: tools, sampling, responsibilities, '
        'timing, analysis and use.</div>'
        '<div class="hbox indigo"><div class="hbox-text">For the wider system around the matrix, see ImpactMojo&rsquo;s '
        '<strong>MEL Basics 101</strong> and <strong>The Evidence Question</strong> flagship.</div></div>')

# ============ SECTION 7: Assumptions (6) ============
divider(7, "Section Seven", "Assumptions")

content('<div class="section-label">Definition</div>'
        '<div class="term-box"><div class="term-word">Assumptions</div>'
        '<div class="term-def">The fourth column: the <strong>external conditions that must hold</strong> for each '
        'step of the logic to work, but which are outside your control. They are the &ldquo;and also&rdquo; that every '
        'if&ndash;then quietly relies on.</div></div>'
        '<div class="slide-body">Assumptions are where a logframe gets honest. They name the things that could break '
        'your chain even if you do everything right.</div>')

content('<div class="section-label">The if&ndash;and&ndash;then logic</div>'
        '<div class="slide-title md">How assumptions complete the chain</div>'
        '<div class="slide-body">Read vertically <em>with</em> the assumptions: <em>IF</em> we deliver the outputs '
        '<em>AND</em> the assumptions at that level hold, <em>THEN</em> we reach the outcome. The assumption column '
        'sits to the side of each step, carrying the conditions that step depends on.</div>'
        '<div class="flow">'
        '<div class="flow-step"><div class="flow-num">IF</div><div class="flow-label">Outputs delivered</div></div>'
        '<div class="flow-arrow">+</div>'
        '<div class="flow-step"><div class="flow-num">AND</div><div class="flow-label">Assumptions hold</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">THEN</div><div class="flow-label">Outcome reached</div></div>'
        '</div>')

content('<div class="section-label">Examples</div>'
        '<div class="slide-title md">What assumptions look like</div>'
        '<ul class="bullet-list amber">'
        '<li>&ldquo;Monsoon rainfall is within normal range&rdquo; (for an agriculture outcome).</li>'
        '<li>&ldquo;The government does not cut the teacher-recruitment budget&rdquo; (for an education outcome).</li>'
        '<li>&ldquo;Trained staff are not transferred out within the year&rdquo; (for a health-quality outcome).</li>'
        '<li>&ldquo;Market prices for the crop stay stable&rdquo; (for an income impact).</li>'
        '</ul>'
        '<div class="hbox"><div class="hbox-text">Each is plausible, outside your control, and capable of breaking the '
        'logic. That is exactly what belongs in this column.</div></div>')

content('<div class="section-label">The assumptions algorithm</div>'
        '<div class="slide-title md">Decide what to do with each one</div>'
        '<div class="slide-body">For every assumption, ask two questions: <em>how likely is it to hold?</em> and '
        '<em>how important is it?</em></div>'
        '<table class="ctable"><thead><tr><th>Likely to hold?</th><th>Action</th></tr></thead><tbody>'
        '<tr><td>Almost certain</td><td>Note it, move on &mdash; not a real risk</td></tr>'
        '<tr><td>Likely but not sure</td><td>Keep in the logframe; monitor it</td></tr>'
        '<tr><td>Unlikely &amp; important</td><td>Redesign the project to remove the dependency, or add an activity to secure it</td></tr>'
        '<tr><td>Will not hold &amp; fatal</td><td>A &ldquo;killer assumption&rdquo; &mdash; the project may not be viable</td></tr>'
        '</tbody></table>')

content('<div class="section-label">Killer assumptions</div>'
        '<div class="slide-title md">When an assumption sinks the project</div>'
        '<div class="slide-body">A <strong>killer assumption</strong> is one that is both essential and unlikely to '
        'hold. If your whole outcome depends on a policy passing that almost certainly will not, no amount of good '
        'delivery will save you. Better to find this on paper than two years in.</div>'
        '<div class="hbox red"><div class="hbox-text">The discipline of writing assumptions exists largely to surface '
        'killer assumptions early &mdash; while you can still redesign or walk away.</div></div>')

content('<div class="section-label">Not an excuse</div>'
        '<div class="slide-title md">Assumptions are to manage, not to hide behind</div>'
        '<div class="slide-body">Assumptions are not a place to park everything that might go wrong so you can blame '
        'them later. Anything you can influence belongs in your activities, not your assumptions. Reserve the column '
        'for genuinely external conditions &mdash; and then actively monitor them.</div>'
        '<div class="hbox amber"><div class="hbox-text">Revisit assumptions at every review. An assumption that has '
        'started to fail is an early warning the outcome is at risk.</div></div>')

# ============ SECTION 8: Risk (8) ============
divider(8, "Section Eight", "Risk")

content('<div class="section-label">From assumptions to risk</div>'
        '<div class="slide-title md">A risk is an assumption that might fail</div>'
        '<div class="slide-body">Flip an assumption to its negative and you have a risk: &ldquo;rainfall is normal&rdquo; '
        '&rarr; &ldquo;drought reduces yields&rdquo;. Modern donor formats often pair the logframe with a '
        '<strong>risk register</strong> that goes further: naming, scoring and assigning each risk.</div>'
        '<div class="hbox"><div class="hbox-text">Same underlying reality, two lenses: the assumption is what you hope '
        'holds; the risk is what happens if it does not.</div></div>')

content('<div class="section-label">Scoring</div>'
        '<div class="slide-title md">Likelihood &times; impact</div>'
        '<div class="slide-body">Risks are usually scored on two axes &mdash; how <strong>likely</strong> they are and '
        'how big the <strong>impact</strong> would be &mdash; often on a 1&ndash;5 scale each. The product (or a colour '
        'grid) gives a rough priority so attention goes to the high&ndash;high corner.</div>'
        '<div class="hbox indigo"><div class="hbox-text">A 5&times;5 likelihood&ndash;impact grid is the standard '
        'picture. It is a small heatmap &mdash; and, like any heatmap, it is a rough sort, not a precise number.</div></div>')

content('<div class="section-label">The 4 Ts</div>'
        '<div class="slide-title md">Four ways to handle a risk</div>'
        '<div class="stat-grid c4">'
        '<div class="stat-card"><div class="stat-number">Treat</div><div class="stat-label">Act to reduce likelihood or impact</div></div>'
        '<div class="stat-card indigo"><div class="stat-number">Transfer</div><div class="stat-label">Shift it &mdash; insurance, partner, contract</div></div>'
        '<div class="stat-card amber"><div class="stat-number">Tolerate</div><div class="stat-label">Accept it; monitor; have a plan B</div></div>'
        '<div class="stat-card red"><div class="stat-number">Terminate</div><div class="stat-label">Avoid it &mdash; change or drop the activity</div></div>'
        '</div>'
        '<div class="hbox"><div class="hbox-text">Most risks are <em>treated</em> or <em>tolerated</em>. The value is '
        'in deciding deliberately, not in the label.</div></div>')

content('<div class="section-label">Types</div>'
        '<div class="slide-title md">Common risk categories</div>'
        '<ul class="bullet-list sm">'
        '<li><strong>Contextual</strong> &mdash; politics, economy, climate, conflict, policy shifts.</li>'
        '<li><strong>Programmatic</strong> &mdash; the intervention fails to work as designed; low uptake.</li>'
        '<li><strong>Institutional / fiduciary</strong> &mdash; partner capacity, fraud, financial mismanagement.</li>'
        '<li><strong>Reputational &amp; safeguarding</strong> &mdash; harm to participants, loss of trust.</li>'
        '</ul>'
        '<div class="hbox red"><div class="hbox-text">Safeguarding risk &mdash; the risk that a project harms the people '
        'it serves &mdash; is now a non-negotiable category for most funders. Never leave it out.</div></div>')

content('<div class="section-label">Owners</div>'
        '<div class="slide-title md">Every risk needs a name against it</div>'
        '<div class="slide-body">A risk register with no owners is a list nobody acts on. Each significant risk should '
        'have a named <strong>owner</strong> responsible for monitoring it and triggering the response, plus a '
        '<strong>trigger</strong> &mdash; the sign that the risk is materialising.</div>'
        '<div class="hbox amber"><div class="hbox-text">&ldquo;If enrolment is below 60% of target by month 3, the '
        'programme manager escalates and we activate the community-mobilisation contingency.&rdquo;</div></div>')

content('<div class="section-label">Living document</div>'
        '<div class="slide-title md">Review risk on a schedule</div>'
        '<div class="slide-body">Risk is not a one-time annex. New risks appear, old ones fade, scores change. A '
        'useful register is reviewed at every project board or quarterly review, with changes logged. A risk register '
        'written once and filed is theatre.</div>'
        '<div class="hbox"><div class="hbox-text">Tie the risk review to the same cadence as your logframe review, so '
        'assumptions and risks &mdash; two views of the same uncertainty &mdash; move together.</div></div>')

content('<div class="section-label">Worked register</div>'
        '<div class="slide-title md">A risk register row</div>'
        '<table class="ctable"><thead><tr><th>Risk</th><th>L&times;I</th><th>Response</th><th>Owner</th></tr></thead><tbody>'
        '<tr><td>Drought cuts yields, weakening the income case</td><td>3&times;4</td><td>Treat: promote water-efficient varieties; tolerate residual</td><td>Field lead</td></tr>'
        '<tr><td>Trained staff transferred out</td><td>4&times;3</td><td>Treat: train a wider pool; brief supervisors</td><td>M&amp;E officer</td></tr>'
        '<tr><td>Partner financial controls weak</td><td>2&times;5</td><td>Transfer/treat: audits, milestone disbursement</td><td>Finance</td></tr>'
        '</tbody></table>')

content('<div class="section-label">Section recap</div>'
        '<div class="slide-title md">Assumptions and risk, together</div>'
        '<div class="hbox green"><div class="hbox-text">The <strong>assumptions</strong> column names what must hold; the '
        '<strong>risk register</strong> names what happens if it does not, scores it, and assigns a response and an '
        'owner. Both make the logframe honest about uncertainty.</div></div>'
        '<div class="slide-body">With all four columns understood, you are ready to assemble the full matrix &mdash; and '
        'to test it as a whole.</div>')

# ============ SECTION 9: Building the Matrix (7) ============
divider(9, "Section Nine", "Building the Matrix")

content('<div class="section-label">Order of work</div>'
        '<div class="slide-title md">Build it in the right sequence</div>'
        '<div class="flow">'
        '<div class="flow-step"><div class="flow-num">1</div><div class="flow-label">Theory of change first</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">2</div><div class="flow-label">Left column (results)</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">3</div><div class="flow-label">Assumptions</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">4</div><div class="flow-label">Indicators</div></div>'
        '<div class="flow-arrow">&rarr;</div>'
        '<div class="flow-step"><div class="flow-num">5</div><div class="flow-label">Means of verification</div></div>'
        '</div>'
        '<div class="hbox"><div class="hbox-text">Resist the urge to start with indicators. If the logic is wrong, '
        'beautiful indicators measure the wrong thing.</div></div>')

content('<div class="section-label">Do it with people</div>'
        '<div class="slide-title md">A logframe is better built in a room</div>'
        '<div class="slide-body">The participatory tradition (ZOPP) builds the logframe in a workshop with the people '
        'who will deliver it and, ideally, those it serves. The matrix that results is usually weaker on paper but far '
        'stronger in practice, because the team owns the logic and has stress-tested it.</div>'
        '<div class="hbox green"><div class="hbox-text">The conversation is the point. A logframe handed down from a '
        'consultant who never met the team is a compliance document, not a plan.</div></div>')

content('<div class="section-label">Vertical logic</div>'
        '<div class="slide-title md">Test 1: does the column make sense going up?</div>'
        '<div class="slide-body">Read the results column from the bottom: activities &rarr; outputs &rarr; outcome '
        '&rarr; impact. At each arrow ask whether the lower level, plus its assumptions, is genuinely enough to reach '
        'the next. Gaps mean a missing output, a missing assumption, or an over-reach.</div>'
        '<div class="hbox amber"><div class="hbox-text">If you find yourself saying &ldquo;and then a miracle '
        'happens&rdquo; between two rows, you have found the gap.</div></div>')

content('<div class="section-label">Horizontal logic</div>'
        '<div class="slide-title md">Test 2: does each row hang together?</div>'
        '<div class="slide-body">Read each row across: result &rarr; indicator &rarr; means of verification &rarr; '
        'assumption. Does the indicator actually measure the result? Can the MoV realistically supply it? Is the '
        'assumption truly external? A row that fails this is internally inconsistent.</div>'
        '<div class="hbox"><div class="hbox-text">Vertical logic tests the <em>theory</em>; horizontal logic tests the '
        '<em>measurement</em>. A strong logframe passes both.</div></div>')

content('<div class="section-label">Common faults</div>'
        '<div class="slide-title md">What reviewers look for</div>'
        '<ul class="bullet-list red">'
        '<li>Activities dressed up as outputs; outputs dressed up as outcomes.</li>'
        '<li>Indicators with no baseline, or no realistic data source.</li>'
        '<li>Too many outcomes; a fuzzy, unmeasurable purpose.</li>'
        '<li>Assumptions that are really things the project controls.</li>'
        '<li>A matrix that contradicts the budget or the work plan.</li>'
        '</ul>')

content('<div class="section-label">Keep it alive</div>'
        '<div class="slide-title md">Revise the logframe as you learn</div>'
        '<div class="slide-body">A logframe is a hypothesis, and hypotheses get updated. Most donors allow &mdash; and '
        'expect &mdash; revisions at review points: refined targets, corrected assumptions, dropped indicators. A frozen '
        'logframe is a sign nobody is using it.</div>'
        '<div class="hbox green"><div class="hbox-text">Log every change and why. The trail of revisions is itself '
        'evidence of adaptive, learning-oriented management.</div></div>')

content('<div class="section-label">Full example</div>'
        '<div class="slide-title md">One complete row of the matrix</div>'
        '<table class="ctable"><thead><tr><th>Result</th><th>Indicator</th><th>MoV</th><th>Assumption</th></tr></thead><tbody>'
        '<tr><td>Outcome: farmers adopt &amp; sustain drip irrigation</td>'
        '<td>60% of trained farmers still using drip at 12 months</td>'
        '<td>Follow-up survey of 300, year 2</td>'
        '<td>Water availability and crop prices stay viable</td></tr>'
        '</tbody></table>'
        '<div class="hbox indigo"><div class="hbox-text">A single row, read across, contains a whole small theory: '
        'what changes, how we will know, where the number comes from, and what it depends on.</div></div>')

# ============ SECTION 10: Critiques & Limits (7) ============
divider(10, "Section Ten", "Critiques &amp; Limits")

content('<div class="section-label">Honest about the tool</div>'
        '<div class="slide-title md">The logframe has real critics</div>'
        '<div class="slide-body">For all its usefulness, the logframe has been criticised for decades &mdash; by '
        'practitioners, evaluators and scholars. Knowing the critiques makes you a better user: you keep the '
        'discipline while avoiding the traps.</div>'
        '<div class="hbox"><div class="hbox-text">The goal is not to abandon the logframe but to hold it lightly &mdash; '
        'as a useful summary, not a description of how change really works.</div></div>')

content('<div class="section-label">Critique 1</div>'
        '<div class="slide-title md">Change is rarely linear</div>'
        '<div class="slide-body">The results chain implies a tidy, one-directional flow. Real change is messy, '
        'looping, full of feedback and unintended effects. Complex problems &mdash; governance, social norms, systems '
        '&mdash; do not move in a straight line from activity to impact.</div>'
        '<div class="hbox amber"><div class="hbox-text">For complex settings, pair the logframe with systems thinking '
        'and outcome-mapping approaches that allow for non-linear, emergent change.</div></div>')

content('<div class="section-label">Critique 2</div>'
        '<div class="slide-title md">It can crowd out what it can&rsquo;t count</div>'
        '<div class="slide-body">Because the logframe rewards the measurable, teams can drift toward what is easy to '
        'count &mdash; outputs, numbers trained &mdash; and away from harder, more important changes in power, '
        'relationships or dignity. The map starts to shape the territory.</div>'
        '<div class="hbox red"><div class="hbox-text">&ldquo;Not everything that counts can be counted.&rdquo; Guard '
        'against measuring the trivial precisely while ignoring the vital.</div></div>')

content('<div class="section-label">Critique 3</div>'
        '<div class="slide-title md">It can lock in a plan that should flex</div>'
        '<div class="slide-body">A logframe agreed at the start, then treated as a contract, can punish teams for '
        'adapting &mdash; even when learning shows the original plan was wrong. Rigidly enforced, it discourages exactly '
        'the responsiveness good development needs.</div>'
        '<div class="hbox amber"><div class="hbox-text">This is what &ldquo;adaptive management&rdquo; and Doing '
        'Development Differently push back on: keep the logframe, but let it be revised as you learn.</div></div>')

content('<div class="section-label">Critique 4</div>'
        '<div class="slide-title md">It serves the donor more than the community</div>'
        '<div class="slide-body">Logframes are written upward, in the donor&rsquo;s language and categories. Critics '
        'note this can centre the funder&rsquo;s accountability over the priorities and knowledge of the people the '
        'project serves &mdash; a power dynamic worth naming.</div>'
        '<div class="hbox indigo"><div class="hbox-text">Building the logframe <em>with</em> communities, and including '
        'indicators they care about, pushes back against this. See <strong>Decolonial Development 101</strong>.</div></div>')

content('<div class="section-label">Alternatives</div>'
        '<div class="slide-title md">Complements and alternatives</div>'
        '<table class="ctable"><thead><tr><th>Approach</th><th>Good when&hellip;</th></tr></thead><tbody>'
        '<tr><td>Outcome Mapping</td><td>Change runs through many actors&rsquo; behaviour; boundaries are fuzzy</td></tr>'
        '<tr><td>Outcome Harvesting</td><td>Outcomes can&rsquo;t be predicted in advance; you work backwards</td></tr>'
        '<tr><td>Most Significant Change</td><td>You want participant-defined, story-based evidence</td></tr>'
        '<tr><td>Adaptive / DDD</td><td>The problem is complex and the path must be discovered</td></tr>'
        '</tbody></table>'
        '<div class="hbox"><div class="hbox-text">These are not rivals so much as companions. Many strong M&amp;E '
        'systems use a logframe for accountability and one of these for learning.</div></div>')

content('<div class="section-label">Balanced view</div>'
        '<div class="slide-title md">Use it well, hold it lightly</div>'
        '<div class="slide-body">The logframe endures because, used well, it does something valuable: it forces a team '
        'to state its logic, commit to measurement, and name its risks, on one honest page. Its failures are mostly '
        'failures of <em>how</em> it is used &mdash; rigidly, upward, as compliance.</div>'
        '<div class="hbox green"><div class="hbox-text">A good practitioner knows both the discipline and the limits. '
        'The matrix is a servant, not a master.</div></div>')

# ============ SECTION 11: Tools & Practice (8) ============
divider(11, "Section Eleven", "Tools &amp; Practice")

content('<div class="section-label">Donor formats</div>'
        '<div class="slide-title md">Every funder wants it slightly differently</div>'
        '<ul class="bullet-list sm">'
        '<li><strong>EU</strong> &mdash; intervention logic + indicators, baselines, targets, sources, assumptions.</li>'
        '<li><strong>FCDO (ex-DFID)</strong> &mdash; logframe with milestones per year, plus a separate theory of change.</li>'
        '<li><strong>USAID</strong> &mdash; results framework + activity MEL plans.</li>'
        '<li><strong>UN agencies</strong> &mdash; results-based management; results &amp; resources frameworks.</li>'
        '<li><strong>GIZ</strong> &mdash; results model / results matrix in the ZOPP tradition.</li>'
        '</ul>'
        '<div class="hbox"><div class="hbox-text">The logic underneath is the same. Learn the structure once and you '
        'can fill any donor&rsquo;s template.</div></div>')

content('<div class="section-label">Software</div>'
        '<div class="slide-title md">What people actually build them in</div>'
        '<ul class="bullet-list sm">'
        '<li><strong>A spreadsheet</strong> &mdash; honestly, most logframes live in Excel or Sheets. Fine.</li>'
        '<li><strong>Word tables</strong> &mdash; for the narrative proposal annex.</li>'
        '<li><strong>M&amp;E platforms</strong> &mdash; DevResults, TolaData, Logalto, Kobo + a dashboard, for live tracking.</li>'
        '</ul>'
        '<div class="hbox amber"><div class="hbox-text">The tool matters far less than the thinking. A sound logframe '
        'in a plain spreadsheet beats a muddled one in expensive software.</div></div>')

content('<div class="section-label">Templates</div>'
        '<div class="slide-title md">A reusable column checklist</div>'
        '<table class="ctable"><thead><tr><th>Column</th><th>Must contain</th></tr></thead><tbody>'
        '<tr><td>Results</td><td>One result per row, in the right grammar for its level</td></tr>'
        '<tr><td>Indicators</td><td>Unit, baseline, target, date, disaggregation</td></tr>'
        '<tr><td>MoV</td><td>Source, method, frequency, responsible person</td></tr>'
        '<tr><td>Assumptions</td><td>External conditions, monitored, not things you control</td></tr>'
        '</tbody></table>'
        '<div class="hbox green"><div class="hbox-text">Print this checklist next to your draft. If any cell is empty '
        'or vague, the logframe is not finished.</div></div>')

content('<div class="section-label">Quality check</div>'
        '<div class="slide-title md">A reviewer&rsquo;s ten-minute test</div>'
        '<ul class="bullet-list">'
        '<li>Can I read the left column as a believable story of change?</li>'
        '<li>Is there exactly one clear outcome?</li>'
        '<li>Does every indicator have a baseline and a source I trust?</li>'
        '<li>Are the assumptions genuinely external &mdash; and any killers flagged?</li>'
        '<li>Does the matrix agree with the budget and work plan?</li>'
        '</ul>'
        '<div class="hbox"><div class="hbox-text">Five yeses and you have a logframe worth funding. Any no is where '
        'the next revision starts.</div></div>')

content('<div class="section-label">Practice</div>'
        '<div class="slide-title md">Build one from a project you know</div>'
        '<div class="slide-body">The fastest way to learn the logframe is to draft one for a real or imagined project '
        'in your own field. Start from the impact, work down to activities, then fill the other three columns. Show it '
        'to a colleague and have them attack the logic.</div>'
        '<div class="hbox indigo"><div class="hbox-text">Try ImpactMojo&rsquo;s <strong>Theory of Change Workbench</strong> '
        'to build the causal story first, then summarise it into your logframe.</div></div>')

content('<div class="section-label">Connected courses</div>'
        '<div class="slide-title md">Where to go next at ImpactMojo</div>'
        '<ul class="bullet-list sm">'
        '<li><strong>Theory of Change 101</strong> &mdash; the narrative your logframe summarises.</li>'
        '<li><strong>MEL Basics 101</strong> &mdash; the wider monitoring, evaluation &amp; learning system.</li>'
        '<li><strong>Impact Evaluation 101</strong> &amp; <strong>Causal Inference</strong> &mdash; proving the outcome.</li>'
        '<li><strong>Cost-Effectiveness 101</strong> &mdash; cost per result, tied to your inputs row.</li>'
        '<li><strong>Data Visualization 101</strong> &mdash; turning your indicators into honest charts.</li>'
        '</ul>')

content('<div class="section-label">Further reading</div>'
        '<div class="slide-title md">Reading &amp; references</div>'
        '<ul class="bullet-list sm">'
        '<li>EuropeAid / EU &mdash; <em>Project Cycle Management Guidelines</em></li>'
        '<li>Bond &amp; FCDO &mdash; logframe and theory-of-change guidance notes</li>'
        '<li>Rosalind Eyben et al. &mdash; <em>The Politics of Evidence</em> (the critique)</li>'
        '<li>Patricia Rogers &mdash; work on complexity and theory-based evaluation</li>'
        '<li>BetterEvaluation.org &mdash; methods, including alternatives to the logframe</li>'
        '</ul>')

content('<div class="section-label">The whole tool</div>'
        '<div class="slide-title md">Logframe 101 in one sentence</div>'
        '<div class="hbox green"><div class="hbox-text">A logframe states, on one page, the change you are betting on '
        '(results), how you will know it happened (indicators), where the proof comes from (means of verification), '
        'and what has to hold true for the bet to pay (assumptions).</div></div>'
        '<div class="slide-body">Built with the team, tested up and across, and revised as you learn, it is one of the '
        'most useful disciplines in development practice &mdash; as long as you remember it is a summary of reality, '
        'not reality itself.</div>')

# ---- s99 recap ----
content('<div class="section-label">In one slide</div>'
        '<div class="slide-title md">The logframe, recapped</div>'
        '<div class="two-col half">'
        '<div class="col-panel green"><div class="col-panel-title">The rows (results)</div>'
        '<div class="slide-body sm">&bull; Inputs &rarr; Activities &rarr; Outputs (you control)<br>'
        '&bull; Outcome (you influence)<br>&bull; Impact (you contribute to)<br>'
        '&bull; One outcome; a handful of outputs</div></div>'
        '<div class="col-panel"><div class="col-panel-title">The columns</div>'
        '<div class="slide-body sm">&bull; Indicator: unit, baseline, target, date<br>'
        '&bull; MoV: source, method, frequency, who<br>&bull; Assumptions: external, monitored<br>'
        '&bull; Test vertically <em>and</em> horizontally</div></div>'
        '</div>'
        '<div class="hbox"><div class="hbox-text">Build the theory of change first; hold the matrix lightly; revise as '
        'you learn.</div></div>')

slides.append(('end', None))

assert len(slides) == 100, "got %d" % len(slides)

path, size, total = db.build(
    course="Logframe 101",
    out_name="logframe-101.html",
    meta_desc=("Logframe 101 - a free foundational course for development practitioners in South Asia. The logical "
               "framework, built from the results chain up: inputs, activities, outputs, outcomes and impact; "
               "indicators and SMART targets; means of verification; assumptions and risk; building and testing the "
               "matrix, its critiques, and donor formats. ImpactMojo, CC BY-NC-ND."),
    title_main_html="Logframe<br>101",
    title_sub_html=("The logical framework, built from the results chain up &mdash; results, indicators, means of "
                    "verification and assumptions, for development practitioners in South Asia."),
    title_tags=["Practical", "Donor-Ready", "100 Slides", "Free Access"],
    toc=TOC,
    slides=slides,
    end_headline_html="One honest<br>page.",
    end_byline=("You can now read, build, test and critique a logframe &mdash; the results chain, the four columns, "
                "and the assumptions that keep it honest. Next: build one for a project you know."),
)
print("Wrote", path, "-", size, "bytes,", total, "slides")
