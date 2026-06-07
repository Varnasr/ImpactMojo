#!/usr/bin/env python3
"""Deep Dive: The Care Economy — curated reading list."""
import dive_builder as db

sections = [
    {
        "title": "Why Care Counts — and Why It Wasn't Counted",
        "intro": "The feminist economics that exposed a hole at the centre of how we measure the economy: the unpaid work, mostly women's, that the System of National Accounts leaves out.",
        "items": [
            {"type": "book", "cite": "Marilyn Waring, <em>If Women Counted: A New Feminist Economics</em> (1988)", "url": "https://www.marilynwaring.com/", "annot": "The book that started the field. Waring, a former New Zealand MP, showed that the United Nations System of National Accounts simply does not count unpaid household and care work — so a tree felled has value but a child raised has none. A founding text of feminist economics and the intellectual root of every time-use survey that followed."},
            {"type": "book", "cite": "Nancy Folbre, <em>The Invisible Heart: Economics and Family Values</em> (2001)", "url": "https://thenewpress.com/", "annot": "Folbre's accessible classic argues that care — the work of raising children, tending the sick and old — is the invisible heart that markets depend on but cannot produce, and that leaving it to unpaid family labour quietly subsidises the whole economy. The clearest single statement of why care is an economic question, not a private one."},
            {"type": "paper", "cite": "Shahra Razavi, \"The Political and Social Economy of Care in a Development Context\" (UNRISD, 2007)", "url": "https://www.unrisd.org/", "annot": "Introduces the influential \"care diamond\" — the idea that care is provided across four institutions: the family, the state, the market, and the non-profit sector — and that development policy decides, often invisibly, how the burden is split between them. Essential conceptual scaffolding for everything that follows."},
        ],
    },
    {
        "title": "Measuring the Invisible",
        "intro": "You cannot redistribute what you do not measure. The data revolution that finally put a number on unpaid care.",
        "items": [
            {"type": "dataset", "cite": "Time Use in India 2019 — National Statistical Office, MoSPI", "url": "https://www.mospi.gov.in/", "annot": "India's first nationwide Time Use Survey in nearly two decades, and the single most important data source on the country's care economy. It found Indian women spend several hours a day on unpaid domestic and caregiving work while men spend a fraction of that — quantifying a gap that policy had long ignored. Read the report's tables on participation rates and time spent by sex."},
            {"type": "report", "cite": "ILO, <em>Care Work and Care Jobs for the Future of Decent Work</em> (2018)", "url": "https://www.ilo.org/publications", "annot": "The most comprehensive global accounting of care work, paid and unpaid. It estimates that unpaid care work, if valued, would be equivalent to a large share of global GDP, and that women perform the overwhelming majority of it. The reference report for the scale of the care economy and the case for investing in it."},
            {"type": "report", "cite": "Oxfam, <em>Time to Care: Unpaid and Underpaid Care Work and the Global Inequality Crisis</em> (2020)", "url": "https://policy-practice.oxfam.org/", "annot": "The report that took the feminist-economics argument to Davos. Its headline — that the unpaid care work done by women and girls adds enormous value to the economy while being treated as free — reframed care as central to the inequality debate. Polemical and data-rich; pair it with the ILO numbers it draws on."},
        ],
    },
    {
        "title": "The Framework: Recognize, Reduce, Redistribute",
        "intro": "How feminist economists turned a critique into a policy agenda — the \"3 Rs\" that now anchor the global care debate.",
        "items": [
            {"type": "paper", "cite": "Diane Elson, \"Recognize, Reduce, Redistribute Unpaid Care Work\" (the 3 Rs framework)", "url": "https://www.unwomen.org/en/what-we-do/economic-empowerment", "annot": "Elson's elegantly simple agenda: <em>recognise</em> unpaid care work as work (through measurement and acknowledgement), <em>reduce</em> the drudgery (through water, fuel, childcare infrastructure), and <em>redistribute</em> it — from women to men, and from households to the state and market. The framing now embedded in SDG target 5.4 and in care policy worldwide."},
            {"type": "web", "cite": "UN Women, SDG Target 5.4 and the global care agenda", "url": "https://www.unwomen.org/en/news/in-focus/csw", "annot": "How the 3 Rs became official global policy: SDG 5.4 commits governments to recognise and value unpaid care and domestic work through public services, infrastructure, and the promotion of shared responsibility within the household. The bridge from feminist theory to government targets."},
            {"type": "report", "cite": "ILO, <em>Care at Work</em> / investing in the care economy and the employment dividend", "url": "https://www.ilo.org/publications", "annot": "The economic-policy case: public investment in care services (childcare, eldercare, paid leave) is not just a cost but an employment engine that frees women's time, creates decent jobs, and pays back through higher participation and tax revenue. The argument that turns care from a welfare line item into infrastructure."},
        ],
    },
    {
        "title": "Care in South Asia",
        "intro": "Why the care economy is especially heavy, and especially invisible, in the Indian context — and how it connects to the region's puzzling female labour-force numbers.",
        "items": [
            {"type": "article", "cite": "Jayati Ghosh, on the care economy, women's work, and macroeconomic policy in India", "url": "https://www.networkideas.org/", "annot": "One of India's foremost development economists on why the unpaid care burden keeps women out of the paid workforce, how austerity shifts costs onto households (and so onto women), and what a feminist macroeconomics would look like. The macro context behind India's time-use numbers."},
            {"type": "paper", "cite": "Feminist economics of care in India — women's status, time poverty, and infrastructure", "url": "https://www.networkideas.org/", "annot": "A strand of Indian scholarship linking the care burden to \"time poverty\": where water, fuel, sanitation, and childcare are scarce, women's unpaid hours balloon and their paid options shrink. It connects the care economy directly to the basic-infrastructure agenda — and to the \"reduce\" in the 3 Rs."},
            {"type": "web", "cite": "India's female labour-force puzzle and the care constraint", "url": "/DeepDives/india-female-labour-force-participation.html", "annot": "Our companion Deep Dive on why so few Indian women work for pay — and why participation fell even as the economy grew. The unpaid care burden is one of the leading explanations; read the two lists together for the full picture of how care shapes women's economic lives."},
        ],
    },
    {
        "title": "Crisis, Pandemic, and the Road Ahead",
        "intro": "How the pandemic exposed the care economy — and what a serious policy response would build.",
        "items": [
            {"type": "report", "cite": "UN Women, <em>Whose Time to Care? Unpaid Care and Domestic Work During COVID-19</em> (2020)", "url": "https://data.unwomen.org/", "annot": "The pandemic's natural experiment. As schools and services closed, the unpaid care load surged — and fell disproportionately on women, even in dual-earner households. The clearest evidence that care is the economy's shock absorber, and that women absorb the shock. A turning point in mainstream attention to the issue."},
            {"type": "book", "cite": "Nancy Folbre (ed.), <em>For Love and Money: Care Provision in the United States</em> (Russell Sage, 2012)", "url": "https://www.russellsage.org/", "annot": "A rigorous edited volume on the paid care sector — childcare and eldercare workers, nurses, aides — and the \"care penalty\": why care jobs are systematically underpaid precisely because the work is associated with love and women. Bridges the unpaid and paid halves of the care economy, and points to where decent-work policy must go."},
        ],
    },
]

related = [
    {"url": "/101-courses/care-economy-101.html", "label": "Care Economy and Unpaid Work 101 — foundational course"},
    {"url": "/101-courses/wee-studies.html", "label": "Women's Economic Empowerment 101 — foundational course"},
    {"url": "/DeepDives/india-female-labour-force-participation.html", "label": "India's Female Labour-Force Puzzle — Deep Dive", "icon": "si_Globe_detailed"},
    {"url": "/catalog.html", "label": "Browse the full ImpactMojo catalog", "icon": "si_Crosshair_detailed"},
]

out, size, total = db.build(
    slug="the-care-economy",
    title="The Care Economy",
    topic="Gender &amp; Economics",
    tagline="The unpaid work that holds every economy up — mostly women's, mostly uncounted. A reading list on recognising, reducing, and redistributing care.",
    chips=["Unpaid Care Work", "Recognize · Reduce · Redistribute"],
    curator="ImpactMojo Editorial",
    curator_role="Curated by the ImpactMojo team",
    curator_bio="This is the list we reach for when explaining why \"the economy\" has always depended on work it refuses to count. It runs from the feminist economics that exposed the gap — Waring, Folbre, Razavi — through the data that finally measured it, to the Recognize-Reduce-Redistribute agenda now written into the SDGs, with a close look at why the care burden falls so heavily in South Asia. We're looking for an invited curator from feminist economics or care policy; pitches welcome.",
    curator_badge="House Pick",
    curator_initials="IM",
    note_paras=[
        "Every economy rests on a vast amount of work that no one pays for and the national accounts do not count: cooking, cleaning, fetching water and fuel, raising children, nursing the sick, caring for the old. This is the care economy, and it is performed overwhelmingly by women. When Marilyn Waring pointed out in 1988 that the global statistical system valued a polluting oil spill but not a mother's labour, she exposed a blind spot at the very centre of economics — one the field is still correcting.",
        "The numbers, once collected, are stark. India's 2019 Time Use Survey found that women spend several hours a day on unpaid domestic and caregiving work while men spend a small fraction of that; the ILO estimates that unpaid care work worldwide, if valued, would rival the largest sectors of the global economy. This is not a side issue. The care burden is one of the main reasons so few women in South Asia work for pay, and it is the hidden shock absorber that economies lean on in every crisis — as the pandemic made impossible to ignore.",
        "The hopeful turn is that critique has become agenda. Diane Elson's \"3 Rs\" — recognise, reduce, redistribute unpaid care work — now anchors SDG target 5.4 and a growing body of policy that treats childcare, eldercare, and basic infrastructure as economic investment rather than private charity. This list moves from the founding feminist economics through measurement and framework to the South Asian context and the road ahead. Start with Waring and Folbre for the why, the Time Use Survey and ILO report for the how-much, and Elson's 3 Rs for what to do about it.",
    ],
    sections=sections,
    related=related,
    citation="ImpactMojo Editorial (2026). \"The Care Economy.\" <em>ImpactMojo Deep Dives</em>. Retrieved from https://impactmojo.in/DeepDives/the-care-economy.html",
    meta_desc="The unpaid care work that holds every economy up — mostly women's, mostly uncounted. A curated reading list on feminist economics, time-use data, the Recognize-Reduce-Redistribute agenda, and care in South Asia.",
    reading_count=14,
)
print("Wrote", out, "-", size, "bytes,", total, "readings")
