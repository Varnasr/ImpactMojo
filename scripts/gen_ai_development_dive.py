#!/usr/bin/env python3
"""Deep Dive: AI and Development — curated reading list."""
import dive_builder as db

sections = [
    {
        "title": "The Promise: AI as a Development Tool",
        "intro": "Where machine learning genuinely moved the needle — measuring poverty, reaching services, and filling data gaps that defeated traditional methods.",
        "items": [
            {"type": "paper", "cite": "Jean, Burke, Xie, Davis, Lobell &amp; Ermon, \"Combining satellite imagery and machine learning to predict poverty,\" <em>Science</em> (2016)", "url": "https://www.science.org/doi/10.1126/science.aaf7894", "annot": "The landmark proof of concept. By training models on night-lights and daytime satellite imagery, the team estimated local poverty across African regions where survey data barely exists. The paper that showed AI could fill the development world's chronic data gaps — and launched a whole field of \"poverty from space\"."},
            {"type": "paper", "cite": "Blumenstock, Cadamuro &amp; On, \"Predicting poverty and wealth from mobile phone metadata,\" <em>Science</em> (2015)", "url": "https://www.science.org/doi/10.1126/science.aac4420", "annot": "A parallel breakthrough using call-detail records to map individual wealth across Rwanda. It demonstrated that the digital traces people already generate can stand in for expensive surveys — powerful, and immediately raising the privacy and consent questions that run through the rest of this list."},
            {"type": "paper", "cite": "Vinuesa et al., \"The role of artificial intelligence in achieving the Sustainable Development Goals,\" <em>Nature Communications</em> (2020)", "url": "https://www.nature.com/articles/s41467-019-14108-y", "annot": "A systematic attempt to map AI against all 17 SDGs. Its sober conclusion: AI could act as an enabler on the large majority of targets, but also as an <em>inhibitor</em> on many — and the gains accrue unevenly. The balanced overview to anchor any claim that \"AI will help development\"."},
        ],
    },
    {
        "title": "The Peril: Bias, Power, and Extraction",
        "intro": "The critical scholarship on who builds these systems, whose data trains them, and who bears the cost when they fail.",
        "items": [
            {"type": "paper", "cite": "Mohamed, Png &amp; Isaac, \"Decolonial AI: Decolonial Theory as Sociotechnical Foresight,\" <em>Philosophy &amp; Technology</em> (2020)", "url": "https://link.springer.com/article/10.1007/s13347-020-00405-8", "annot": "The foundational text for thinking about AI and the Global South. The authors apply decolonial theory to show how AI can reproduce colonial patterns — extracting data and labour from the periphery, concentrating value at the centre — and argue for foresight that centres the communities most affected. Essential framing."},
            {"type": "article", "cite": "Abeba Birhane, \"The Algorithmic Colonization of Africa\" (2020)", "url": "https://reallifemag.com/the-algorithmic-colonization-of-africa/", "annot": "A sharp, accessible essay arguing that the export of Western AI systems and Silicon Valley's \"solutionism\" to Africa repeats colonial dynamics under a technological banner — solving problems defined elsewhere, with little local ownership. Read it alongside the Decolonial AI paper for the critique in plain language."},
            {"type": "book", "cite": "Kate Crawford, <em>Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence</em> (Yale, 2021)", "url": "https://katecrawford.net/atlas", "annot": "Reframes AI as a material, extractive industry — of minerals, energy, data, and underpaid human labour — rather than a disembodied intelligence. The chapters on labour and classification are especially relevant to development, where the data-labelling that trains global models is often done cheaply in the Global South. The big-picture political economy."},
        ],
    },
    {
        "title": "Data Colonialism and the Politics of Data",
        "intro": "The argument that data itself is the new frontier of extraction — and what that means for the countries being mined.",
        "items": [
            {"type": "book", "cite": "Couldry &amp; Mejias, <em>The Costs of Connection: How Data Is Colonizing Human Life and Appropriating It for Capitalism</em> (2019)", "url": "https://www.sup.org/books/title/?id=28816", "annot": "Coins and develops \"data colonialism\": the idea that the wholesale capture of human life as data is a new form of the historic colonial land-grab, now global and ongoing. A theoretical backbone for understanding why questions of data sovereignty and ownership are central to AI-and-development debates."},
            {"type": "web", "cite": "Our companion Deep Dive: \"Data, Power, and the Global South\"", "url": "/DeepDives/data-power-global-south.html", "annot": "Who counts, who is counted, and who decides. This sibling reading list goes deeper on data politics, statistical capacity, and the governance of information in the developing world — the substrate on which every AI system in this list is built. Read the two together."},
            {"type": "report", "cite": "WHO, <em>Ethics and Governance of Artificial Intelligence for Health</em> (2021)", "url": "https://www.who.int/publications/i/item/9789240029200", "annot": "A rare, concrete governance document for a high-stakes sector. The WHO sets out six principles for AI in health — from protecting autonomy to ensuring equity and accountability — and is candid that much health AI is trained on data from rich countries and may not transfer safely to low-resource settings. A model for sectoral AI governance."},
        ],
    },
    {
        "title": "Infrastructure, Language, and the Road Ahead",
        "intro": "Digital public infrastructure, the large-language-model moment, and what an equitable AI agenda for development might look like.",
        "items": [
            {"type": "report", "cite": "World Bank, <em>World Development Report 2016: Digital Dividends</em>", "url": "https://www.worldbank.org/en/publication/wdr2016", "annot": "The Bank's foundational statement on digital technology and development, and still the best primer on why technology alone does not deliver gains — the \"analog complements\" of skills, institutions, and competition decide whether digital dividends reach the poor. The frame to apply to every AI promise: what has to be true around the technology for it to help?"},
            {"type": "web", "cite": "India Stack &amp; Digital Public Infrastructure — Aadhaar, UPI, and the DPI model", "url": "https://www.indiastack.org/", "annot": "India's open digital infrastructure — identity, payments, data-sharing — is now the world's most-studied template for population-scale digital systems, and the rails on which AI services for billions are being built. A live, contested case: lauded for inclusion and reach, criticised for surveillance and exclusion risks. Essential for the South Asian context."},
            {"type": "paper", "cite": "Bender, Gebru, McMillan-Major &amp; Mitchell, \"On the Dangers of Stochastic Parrots,\" <em>FAccT</em> (2021)", "url": "https://dl.acm.org/doi/10.1145/3442188.3445922", "annot": "The paper that named the risks of large language models before they went mainstream: environmental cost, baked-in bias, and the under-representation of the world's languages and the Global South in training data. Directly relevant to whether the LLM era serves South Asian users — and to ImpactMojo's own work on Indian-language access."},
            {"type": "web", "cite": "Toward an equitable AI-for-development agenda — local ownership, language, and capacity", "url": "https://www.unesco.org/en/artificial-intelligence/recommendation-ethics", "annot": "UNESCO's Recommendation on the Ethics of AI — adopted by nearly 200 countries — is the most broadly endorsed statement of what responsible AI should look like, with explicit attention to development, inclusion, and the Global South. A constructive closing reference: not whether to use AI, but how to govern it so the benefits and the say are shared."},
        ],
    },
]

related = [
    {"url": "/courses/devai/", "label": "AI for Impact: Data, Monitoring & Evaluation — flagship course"},
    {"url": "/101-courses/digital-ethics.html", "label": "Digital Ethics 101 — foundational course"},
    {"url": "/101-courses/data-feminism.html", "label": "Data Feminism 101 — foundational course"},
    {"url": "/DeepDives/data-power-global-south.html", "label": "Data, Power, and the Global South — Deep Dive", "icon": "si_Globe_detailed"},
    {"url": "/catalog.html", "label": "Browse the full ImpactMojo catalog", "icon": "si_Crosshair_detailed"},
]

out, size, total = db.build(
    slug="ai-and-development",
    title="AI and Development",
    topic="Technology &amp; Power",
    tagline="The most over-hyped and under-examined tool in the development toolkit. A reading list on what AI can genuinely do for the poor — and what it does to them.",
    chips=["Promise &amp; Peril", "Data Colonialism"],
    curator="ImpactMojo Editorial",
    curator_role="Curated by the ImpactMojo team",
    curator_bio="This is the list we reach for when the AI hype cycle reaches development — to separate what the technology has genuinely achieved from what is being sold. It pairs the breakthrough work (poverty from satellites and phone data) with the critical scholarship that has grown up alongside it (decolonial AI, data colonialism, the politics of training data), and ends on infrastructure, language, and what an equitable agenda would require. We're looking for an invited curator from AI ethics, data science, or digital development; pitches welcome.",
    curator_badge="House Pick",
    curator_initials="IM",
    note_paras=[
        "Artificial intelligence arrives in development wrapped in two stories at once. In the first, machine learning fills the data voids that have always hobbled anti-poverty work — mapping deprivation from satellites where no census reaches, predicting crop failure, routing health workers, translating across the languages the internet forgot. There is real substance here: the 2015–16 work predicting poverty from phone records and satellite imagery genuinely did something traditional surveys could not, and it launched a serious field.",
        "In the second story, AI is the newest form of an old extraction. The data that trains these systems is harvested, often without meaningful consent, from the very populations being studied; the value flows to a handful of firms and countries; the models encode the biases of their makers and the gaps in their training data; and the cheap human labour of labelling and moderation is outsourced to the Global South. A growing body of scholarship — decolonial AI, data colonialism, the political economy of the \"Atlas of AI\" — insists that we read AI-for-development as a question of power, not just of tools.",
        "Both stories are true, which is exactly why this list holds them together. It moves from the genuine breakthroughs, through the critical reframing, into the politics of data and governance, and out to infrastructure, the large-language-model moment, and what an equitable agenda would require — a question with real stakes for South Asia, where population-scale digital systems and Indian-language AI are being built right now. Start with the Jean and Blumenstock papers for the promise, then the Decolonial AI paper and Crawford's <em>Atlas</em> for the harder questions.",
    ],
    sections=sections,
    related=related,
    citation="ImpactMojo Editorial (2026). \"AI and Development.\" <em>ImpactMojo Deep Dives</em>. Retrieved from https://impactmojo.in/DeepDives/ai-and-development.html",
    meta_desc="What can AI genuinely do for the poor — and what does it do to them? A curated reading list on AI and development: poverty prediction from satellites and phones, decolonial AI and data colonialism, the politics of training data, digital public infrastructure, and the large-language-model moment in the Global South.",
    reading_count=13,
)
print("Wrote", out, "-", size, "bytes,", total, "readings")
