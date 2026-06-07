#!/usr/bin/env python3
"""Deep Dive: Climate Migration in South Asia — curated reading list."""
import dive_builder as db

sections = [
    {
        "title": "The Big Picture and the Numbers",
        "intro": "What the science says about climate and human movement, and the projections that put South Asia at the centre of the story.",
        "items": [
            {"type": "report", "cite": "IPCC, Sixth Assessment Report, Working Group II: <em>Impacts, Adaptation and Vulnerability</em> (2022)", "url": "https://www.ipcc.ch/report/ar6/wg2/", "annot": "The authoritative scientific baseline. Its chapters on Asia and on poverty and livelihoods set out how heat, floods, cyclones, sea-level rise, and erratic monsoons are reshaping where people can live and work — and conclude that displacement and migration are already among climate change's clearest human consequences. Read the Asia regional chapter and the Summary for Policymakers first."},
            {"type": "report", "cite": "Rigaud et al., <em>Groundswell: Preparing for Internal Climate Migration</em> (World Bank, 2018 &amp; 2021)", "url": "https://www.worldbank.org/en/news/feature/2021/09/13/climate-change-could-force-216-million-people-to-migrate-within-their-own-countries-by-2050", "annot": "The most-cited projection in the field: the World Bank estimates that, on current trends, climate change could push well over 100 million people to migrate <em>within</em> their own countries by 2050, with South Asia among the hardest-hit regions. Crucially, it shows the numbers fall sharply with early action on emissions and development — the projection is a warning, not a fate."},
            {"type": "dataset", "cite": "Internal Displacement Monitoring Centre (IDMC), Global Report on Internal Displacement (GRID)", "url": "https://www.internal-displacement.org/", "annot": "The annual count of people displaced by disasters, updated yearly. It consistently shows that weather-related hazards — floods and storms above all — displace far more people each year than conflict, and that South Asian countries (India, Bangladesh, Pakistan) routinely top the disaster-displacement tables. The source for who is actually moving, now, not in 2050."},
        ],
    },
    {
        "title": "How to Think About It",
        "intro": "Why \"climate refugee\" is the wrong phrase, and the framing that replaced it: migration as one adaptation among many, driven by many causes at once.",
        "items": [
            {"type": "paper", "cite": "Richard Black et al., \"Migration as adaptation,\" <em>Nature</em> (2011)", "url": "https://www.nature.com/articles/479477a", "annot": "The single most influential reframing. Black and colleagues argue that environmental change rarely causes migration on its own — it works through economic, political, and social drivers — and that migration can be a successful <em>adaptation</em> to climate stress rather than simply its tragic result. The paper that retired the simple \"climate refugee\" narrative."},
            {"type": "report", "cite": "Foresight, <em>Migration and Global Environmental Change</em> (UK Government Office for Science, 2011)", "url": "https://www.gov.uk/government/publications/migration-and-global-environmental-change-future-challenges-and-opportunities", "annot": "The landmark report behind the Black <em>Nature</em> piece, and the origin of the \"trapped populations\" insight: the poorest and most vulnerable often <em>cannot</em> afford to move, and so are left behind in the most dangerous places. A vital corrective to the assumption that climate impacts produce mass exodus — sometimes they produce immobility."},
            {"type": "web", "cite": "IOM, on environmental migration, terminology, and the limits of \"climate refugee\"", "url": "https://www.iom.int/", "annot": "The International Organization for Migration's resources explain why no legal category of \"climate refugee\" exists — the 1951 Refugee Convention does not cover those fleeing environmental change — and what protection gaps that leaves. Important grounding for any policy discussion, and for understanding why the language we use matters."},
        ],
    },
    {
        "title": "South Asia Up Close",
        "intro": "The specific geographies where climate and movement already collide — deltas, coasts, drylands, and the cities people move to.",
        "items": [
            {"type": "article", "cite": "Bangladesh: sea-level rise, salinity, riverbank erosion, and the road to Dhaka", "url": "https://www.iom.int/countries/bangladesh", "annot": "The world's most-studied case. Bangladesh's low-lying delta faces sea-level rise, saltwater intrusion ruining farmland, and relentless riverbank erosion — and much of the resulting movement flows into the megacity of Dhaka, already among the fastest-growing on earth. The clearest illustration of climate stress translating into rural-to-urban migration."},
            {"type": "article", "cite": "The Sundarbans and India's vulnerable coasts — displacement in the delta", "url": "https://www.internal-displacement.org/countries/india/", "annot": "On the Indian side of the Bengal delta, the Sundarbans are losing islands and inhabitants to erosion and storm surge, while cyclones along the eastern coast displace millions episodically. A reminder that within India, climate migration is already a lived reality for coastal and delta communities — not a future scenario."},
            {"type": "report", "cite": "Asian Development Bank, on climate change and migration in Asia and the Pacific", "url": "https://www.adb.org/", "annot": "ADB's regional analysis situates South Asia's displacement within a wider Asian picture and stresses the policy levers: building urban capacity to absorb migrants, investing in adaptation so people can stay where they wish, and planning relocation where they cannot. A useful bridge from diagnosis to the policy agenda."},
            {"type": "article", "cite": "Drylands, heat, and agrarian distress as drivers of seasonal migration in India", "url": "https://www.indiawaterportal.org/", "annot": "Beyond the coasts, recurring drought and extreme heat across India's drylands push millions into seasonal and circular labour migration — a long-standing pattern that climate change is intensifying. Connects the climate story to India's vast internal-migration system and to the agrarian-distress literature."},
        ],
    },
    {
        "title": "Protection, Justice, and Policy",
        "intro": "Who is responsible, who pays, and what a humane response would actually look like.",
        "items": [
            {"type": "web", "cite": "Loss and Damage, planned relocation, and the justice question", "url": "https://unfccc.int/topics/adaptation-and-resilience/workstreams/loss-and-damage-ld", "annot": "Climate migration is, at root, a justice issue: those displaced have contributed least to the emissions driving it. The UNFCCC's Loss and Damage track — and the fund agreed at COP27 — is where the question of who pays for climate harm, including displacement and planned relocation, is being fought out. Essential for the equity dimension."},
            {"type": "report", "cite": "UNHCR &amp; the protection gap for the climate-displaced", "url": "https://www.unhcr.org/what-we-do/build-better-futures/environment-disasters-and-climate-change", "annot": "UNHCR's work on disaster and climate displacement maps the legal grey zone: most people displaced by climate are not refugees in law, and cross-border protection remains patchy. It documents the emerging frameworks — regional agreements, the Global Compact for Migration — trying to fill the gap. The state of play on rights and protection."},
            {"type": "paper", "cite": "Migration as adaptation in practice — labour mobility, remittances, and resilience", "url": "https://www.iom.int/resources", "annot": "A practical strand of research and policy argues that, managed well, migration strengthens resilience: remittances fund adaptation back home, planned labour mobility relieves pressure on stressed regions, and circular migration spreads risk. The constructive counterpoint to the crisis framing — and the agenda most likely to actually help."},
        ],
    },
]

related = [
    {"url": "/101-courses/climate-essentials.html", "label": "Climate Essentials 101 — foundational course"},
    {"url": "/101-courses/env-justice.html", "label": "Environmental Justice 101 — foundational course"},
    {"url": "/DeepDives/climate-just-transitions-south-asia.html", "label": "Climate and Just Transitions in South Asia — Deep Dive", "icon": "si_Globe_detailed"},
    {"url": "/DeepDives/climate-adaptation-finance.html", "label": "Climate Adaptation Finance & Loss and Damage — Deep Dive", "icon": "si_Globe_detailed"},
    {"url": "/catalog.html", "label": "Browse the full ImpactMojo catalog", "icon": "si_Crosshair_detailed"},
]

out, size, total = db.build(
    slug="climate-migration-south-asia",
    title="Climate Migration in South Asia",
    topic="Climate &amp; Migration",
    tagline="Floods, salt, heat, and the people who move — and the people who can't. A reading list on climate, displacement, and adaptation across the region most exposed to both.",
    chips=["Displacement &amp; Adaptation", "Deltas, Coasts &amp; Drylands"],
    curator="ImpactMojo Editorial",
    curator_role="Curated by the ImpactMojo team",
    curator_bio="This is the list we hand anyone trying to get past the \"climate refugee\" headlines to what the evidence actually shows. It runs from the global science and the headline projections, through the framing that reshaped the field — migration as adaptation, and the \"trapped populations\" who cannot move — into South Asia's specific deltas, coasts, and drylands, and out to the hard questions of protection and justice. We're looking for an invited curator from migration studies or climate adaptation; pitches welcome.",
    curator_badge="House Pick",
    curator_initials="IM",
    note_paras=[
        "South Asia sits at the sharp end of two global forces at once: it is among the regions most exposed to climate change, and it is home to some of the largest and most mobile populations on earth. Sea-level rise eats at the Bengal delta; saltwater creeps into Bangladeshi farmland; cyclones batter the eastern Indian coast; heatwaves and failing monsoons stress the drylands. Where these pressures meet poverty and dense settlement, people move — and the question of how climate reshapes human movement here is one of the defining development questions of the century.",
        "The first thing the evidence does is complicate the headlines. There is no such thing, in law, as a \"climate refugee,\" and the image of millions fleeing rising seas in a single wave is misleading. Environmental change rarely drives migration on its own; it works through economic, social, and political channels, and migration is often a deliberate <em>adaptation</em> — a way to spread risk and send money home — rather than simply a tragedy. Just as important is the opposite finding: the poorest are frequently <em>trapped</em>, unable to afford to leave the most dangerous places. Most climate-related movement, too, is internal — within countries, often from countryside to city — not across borders.",
        "And it is, finally, a justice question. The people displaced by climate change have done the least to cause it, which is why displacement now sits inside the global fight over Loss and Damage and who should pay for climate harm. This list moves from the science and the numbers, through the conceptual framing, into South Asia's specific geographies, and out to protection and policy. Start with the IPCC and Groundswell for scale, then Black's <em>Nature</em> paper and the Foresight report for how to think about it clearly.",
    ],
    sections=sections,
    related=related,
    citation="ImpactMojo Editorial (2026). \"Climate Migration in South Asia.\" <em>ImpactMojo Deep Dives</em>. Retrieved from https://impactmojo.in/DeepDives/climate-migration-south-asia.html",
    meta_desc="Floods, salt, heat, and the people who move — and the people who can't. A curated reading list on climate change, displacement, and migration-as-adaptation across South Asia, from the IPCC and the World Bank's Groundswell projections to the deltas of Bangladesh and the question of who pays.",
    reading_count=13,
)
print("Wrote", out, "-", size, "bytes,", total, "readings")
