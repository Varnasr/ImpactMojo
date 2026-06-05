# -*- coding: utf-8 -*-
"""
Environmental Justice 101 — ImpactMojo 101 Series (native deck spec)
Foundational environmental justice for South Asian development & environment practitioners.
Build: python3 scripts/deck-builder/build.py env_justice
"""

DECK = {
    "slug": "env-justice",
    "title": "Environmental Justice 101",
    "description": ("Environmental Justice 101 — a free foundational course for development "
                    "and environment practitioners in South Asia. Who bears environmental "
                    "harm and who reaps its benefits: from caste, class and Adivasi rights to "
                    "climate justice, the Forest Rights Act, pollution and just transition. "
                    "ImpactMojo, CC BY-NC-ND."),
    "slides": [

        # ===================== S1 TITLE =====================
        {"type": "title",
         "main": "Environmental<br>Justice<br>101",
         "sub": "Who Bears the Harm, Who Reaps the Benefit &mdash; a Foundational Course on "
                "Environmental Justice for Practitioners in South Asia",
         "tags": ["Research-Backed", "India Focus", "100 Slides", "Free Access"]},

        # ===================== S2 TOC =====================
        {"type": "toc", "label": "Agenda", "title": "What We Cover",
         "items": [
             {"name": "What Environmental Justice Is"},
             {"name": "Origins of the Movement"},
             {"name": "The Three Dimensions"},
             {"name": "Who Bears the Burden"},
             {"name": "Climate Justice"},
             {"name": "Land, Forest &amp; the Commons"},
             {"name": "Pollution &amp; Health"},
             {"name": "Just Transition"},
             {"name": "Movements &amp; Resistance"},
             {"name": "Principles &amp; Legal Tools"},
             {"name": "EJ in Practice &amp; Reading"},
         ]},

        # ===================== SECTION 01 =====================
        {"type": "divider", "num": "01", "label": "Section One",
         "title": "What Environmental Justice Is"},

        {"type": "content", "label": "Definition", "title": "Justice is about who bears the harm",
         "blocks": [
             {"t": "body", "html": "Pollution, floods, displacement and toxic waste do not fall "
              "evenly. <strong>Environmental justice</strong> asks who carries the burden of "
              "environmental harm and who enjoys the benefits &mdash; and insists that the answer "
              "should not track caste, class, ethnicity or income."},
             {"t": "term", "word": "Environmental justice",
              "def": "The fair distribution of environmental benefits and burdens, and the "
              "meaningful inclusion of all communities &mdash; regardless of caste, class, race "
              "or income &mdash; in the decisions that shape their environment."},
             {"t": "hbox", "color": "cyan", "html": "It is not a question of trees versus people. "
              "It is a question of <em>which</em> people live with the pollution, and which live "
              "with the parks."},
         ]},

        {"type": "content", "label": "The Framing", "title": "&lsquo;The environment is where we live, work and pray&rsquo;",
         "blocks": [
             {"t": "quote",
              "text": "The environment is where we live, where we work, where we play and where "
              "we pray.",
              "attr": "&mdash; a defining slogan of the US environmental-justice movement"},
             {"t": "body", "html": "This reframing was radical. It moved &lsquo;the "
              "environment&rsquo; from distant wilderness and charismatic wildlife to the "
              "everyday surroundings of ordinary people &mdash; the slum beside the drain, the "
              "fields beside the smelter, the basti downwind of the chimney."},
         ]},

        {"type": "content", "label": "Two Lenses", "title": "Conservation is not the same as justice",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "Conservation lens", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Protect forests, rivers, species and "
                   "habitats. Vital &mdash; but can treat people as a threat to be removed from "
                   "nature."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Justice lens", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Asks who depends on those forests and "
                   "rivers, who is displaced to protect them, and who decides. Centres people and "
                   "power."}]}]},
             {"t": "hbox", "color": "amber", "html": "Both matter. But a fortress conservation "
              "that evicts Adivasi forest-dwellers to make a tiger reserve can be ecologically "
              "sound and deeply unjust at the same time."},
         ]},

        {"type": "content", "label": "Environmentalism of the Poor", "title": "The South has its own environmentalism",
         "blocks": [
             {"t": "body", "html": "Ramachandra Guha and Joan Martinez-Alier described an "
              "<strong>&lsquo;environmentalism of the poor&rsquo;</strong>: in the Global South, "
              "environmental struggles are rarely about leisure or scenery: they are about "
              "survival &mdash; access to water, forests, fish and clean air on which livelihoods "
              "directly depend."},
             {"t": "hbox", "color": "cyan", "html": "When the river is your drinking water, your "
              "irrigation and your fishery, defending it is not a lifestyle choice. It is "
              "defending the means of life itself."},
         ]},

        {"type": "content", "label": "Distribution", "title": "Harms and benefits flow in opposite directions",
         "blocks": [
             {"t": "flow", "steps": [
                 "BENEFIT: cheap power, metal, cement for cities &amp; industry",
                 "HARM: the mine, the ash pond, the smokestack",
                 "located in: a poor, rural, often Adivasi or Dalit area",
                 "so: one group profits, another pays in health &amp; land"]},
             {"t": "hbox", "color": "red", "html": "Environmental justice names this split. The "
              "people who consume the most resources are rarely the people who live next to the "
              "damage of producing them."},
         ]},

        {"type": "content", "label": "Procedure Too", "title": "It is about voice, not just outcomes",
         "blocks": [
             {"t": "body", "html": "Justice is not only about <em>where</em> the harm lands. It "
              "is about <em>who got to decide</em>. A community that was never consulted, whose "
              "objections were never heard, suffers an injustice even before the first tree is "
              "felled."},
             {"t": "bullets", "color": "indigo", "items": [
                 "Were affected people informed, in their language, in time?",
                 "Could they object, and was the objection weighed?",
                 "Were their knowledge and consent treated as binding?"]},
         ]},

        {"type": "content", "label": "Why It Matters", "title": "Why practitioners need this lens",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Programmes have environmental footprints</strong> &mdash; and they land "
                 "on someone",
                 "<strong>The poorest are most exposed</strong> to pollution, heat and disaster",
                 "<strong>&lsquo;Green&rsquo; can be unjust</strong> &mdash; a dam or a solar park "
                 "can still displace",
                 "<strong>Recognising whose burden it is</strong> is the first step to a fairer "
                 "design"]},
         ]},

        # ===================== SECTION 02 =====================
        {"type": "divider", "num": "02", "label": "Section Two",
         "title": "Origins of the Movement"},

        {"type": "content", "label": "The Spark", "title": "Warren County, North Carolina, 1982",
         "blocks": [
             {"t": "body", "html": "In <strong>1982</strong>, the state of North Carolina chose "
              "<strong>Warren County</strong> &mdash; a poor, majority-Black county &mdash; as the "
              "dump site for soil contaminated with toxic PCBs. Residents lay down in the road to "
              "block the trucks. Over 500 were arrested."},
             {"t": "hbox", "color": "cyan", "html": "The protests failed to stop the landfill, but "
              "they catalysed a national movement and gave it a name. Warren County is widely "
              "remembered as the birthplace of the US environmental-justice movement."},
         ]},

        {"type": "content", "label": "Naming the Wrong", "title": "The term &lsquo;environmental racism&rsquo;",
         "blocks": [
             {"t": "body", "html": "Civil-rights leader <strong>Benjamin Chavis</strong>, then "
              "head of the United Church of Christ Commission for Racial Justice, coined the term "
              "<strong>&lsquo;environmental racism&rsquo;</strong> in the wake of Warren County."},
             {"t": "term", "word": "Environmental racism",
              "def": "The disproportionate siting of polluting facilities, waste and "
              "environmental hazards in communities of colour &mdash; and their systematic "
              "exclusion from environmental decision-making."},
         ]},

        {"type": "content", "label": "The Evidence", "title": "A pattern, not a coincidence",
         "blocks": [
             {"t": "body", "html": "A landmark 1987 report, <em>Toxic Wastes and Race in the "
              "United States</em>, found that the single strongest predictor of where hazardous-"
              "waste facilities were sited was the <strong>race</strong> of the surrounding "
              "community &mdash; even after accounting for income."},
             {"t": "hbox", "color": "red", "html": "The finding reframed pollution as a civil-"
              "rights issue. Where you were born, and to whom, shaped the air you breathed and the "
              "water you drank."},
         ]},

        {"type": "content", "label": "India's Own Roots", "title": "South Asia did not import this struggle",
         "blocks": [
             {"t": "body", "html": "The vocabulary &lsquo;environmental justice&rsquo; travelled "
              "from the United States, but the <em>struggles</em> are indigenous and older. India "
              "has a deep tradition of communities defending forests, rivers and air &mdash; long "
              "before the term existed."},
             {"t": "flow", "steps": [
                 "1730s: Bishnoi sacrifice at Khejarli to save trees",
                 "1973: Chipko in the Himalaya",
                 "1980s: Silent Valley, Bhopal, Narmada",
                 "2000s+: Niyamgiri, anti-POSCO, coastal struggles"]},
         ]},

        {"type": "content", "label": "Chipko 1973", "title": "Chipko: hugging the trees, 1973",
         "blocks": [
             {"t": "body", "html": "In <strong>1973</strong>, in the Chamoli district of the "
              "Garhwal Himalaya, villagers &mdash; many of them women &mdash; embraced trees to "
              "stop contractors from felling them. <strong>Chipko</strong> (&lsquo;to cling&rsquo;) "
              "became a global symbol of grassroots forest defence."},
             {"t": "hbox", "color": "green", "html": "Chipko fused ecology and livelihood: the "
              "forests provided fuel, fodder and protection from landslides. Defending the trees "
              "was defending the village economy &mdash; environmentalism of the poor in action."},
         ]},

        {"type": "content", "label": "Bhopal 1984", "title": "Bhopal: the world's worst industrial disaster",
         "blocks": [
             {"t": "body", "html": "On the night of <strong>2&ndash;3 December 1984</strong>, "
              "methyl isocyanate gas leaked from the <strong>Union Carbide</strong> pesticide "
              "plant in Bhopal. Thousands died within days; many more died and were maimed in the "
              "years that followed."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Dec 1984", "label": "Union Carbide MIC gas leak, Bhopal", "color": "red"},
                 {"num": "Decades on", "label": "contaminated groundwater &amp; unfinished "
                  "justice for survivors", "color": "amber"}]},
             {"t": "hbox", "color": "red", "html": "Bhopal is the textbook case of who bears "
              "industrial risk: the densely populated, poor settlements pressed up against the "
              "plant gates."},
         ]},

        {"type": "content", "label": "Silent Valley", "title": "Silent Valley: a forest saved, 1970s&ndash;80s",
         "blocks": [
             {"t": "body", "html": "A proposed hydroelectric dam on the Kunthipuzha river "
              "threatened to drown the <strong>Silent Valley</strong> rainforest in Kerala. A "
              "sustained campaign by scientists, poets and citizens led the government to abandon "
              "the project and declare a national park in <strong>1984</strong>."},
             {"t": "hbox", "color": "cyan", "html": "Silent Valley showed that development and "
              "ecology could be weighed against each other in public &mdash; and that a movement "
              "could win."},
         ]},

        {"type": "content", "label": "Common Thread", "title": "What these origins share",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>The harm is concentrated</strong> on the poor and the marginalised",
                 "<strong>The decision was taken elsewhere</strong> &mdash; by the state or "
                 "industry, not the affected",
                 "<strong>Resistance is local and embodied</strong> &mdash; bodies on the road, "
                 "arms around trees",
                 "<strong>Livelihood and ecology are inseparable</strong> in the struggle"]},
         ]},

        # ===================== SECTION 03 =====================
        {"type": "divider", "num": "03", "label": "Section Three",
         "title": "The Three Dimensions"},

        {"type": "content", "label": "A Framework", "title": "Justice has three faces",
         "blocks": [
             {"t": "body", "html": "Scholars of environmental justice distinguish three "
              "dimensions. A struggle can win on one and still fail on the others &mdash; so it "
              "helps to name them separately."},
             {"t": "raw", "html": (
                 '<div style="display:flex;justify-content:center;margin:8px 0;">'
                 '<svg viewBox="0 0 540 270" width="560" style="max-width:100%;font-family:inherit;">'
                 '<circle cx="180" cy="110" r="78" fill="#0EA5E9" opacity="0.45"/>'
                 '<circle cx="360" cy="110" r="78" fill="#10B981" opacity="0.45"/>'
                 '<circle cx="270" cy="190" r="78" fill="#6366F1" opacity="0.45"/>'
                 '<text x="150" y="100" text-anchor="middle" fill="#e2e8f0" font-size="14" font-weight="700">Distributive</text>'
                 '<text x="150" y="120" text-anchor="middle" fill="#cbd5e1" font-size="11">who gets harm</text>'
                 '<text x="390" y="100" text-anchor="middle" fill="#e2e8f0" font-size="14" font-weight="700">Procedural</text>'
                 '<text x="390" y="120" text-anchor="middle" fill="#cbd5e1" font-size="11">who decides</text>'
                 '<text x="270" y="205" text-anchor="middle" fill="#e2e8f0" font-size="14" font-weight="700">Recognition</text>'
                 '<text x="270" y="224" text-anchor="middle" fill="#cbd5e1" font-size="11">who counts</text>'
                 '</svg></div>')},
         ]},

        {"type": "content", "label": "Dimension One", "title": "Distributive justice: who gets the harm",
         "blocks": [
             {"t": "term", "word": "Distributive justice",
              "def": "The fair allocation of environmental goods (clean air, green space, safe "
              "water) and bads (pollution, waste, risk) across people and places."},
             {"t": "body", "html": "This is the most visible dimension &mdash; the dump in the "
              "Dalit hamlet, the refinery beside the fishing village, the park in the gated colony. "
              "It asks: <strong>is the burden shared fairly?</strong>"},
         ]},

        {"type": "content", "label": "Dimension Two", "title": "Procedural justice: who gets to decide",
         "blocks": [
             {"t": "term", "word": "Procedural justice",
              "def": "Fair, inclusive and transparent processes for environmental decisions "
              "&mdash; access to information, genuine consultation, and the power to influence "
              "the outcome."},
             {"t": "hbox", "color": "indigo", "html": "A public hearing held in English, in a "
              "distant town, on short notice, in technical jargon, is a procedural injustice "
              "&mdash; the form of participation without its substance."},
         ]},

        {"type": "content", "label": "Dimension Three", "title": "Recognition justice: who even counts",
         "blocks": [
             {"t": "term", "word": "Recognition justice",
              "def": "Respect for the identity, knowledge, culture and rights of affected "
              "communities &mdash; refusing to treat them as invisible, ignorant or expendable."},
             {"t": "body", "html": "Before a community can be fairly heard (procedure) or fairly "
              "treated (distribution), it must first be <strong>recognised</strong> as a "
              "community with standing, knowledge and rights. Adivasi and Dalit communities are "
              "often denied this at the outset."},
         ]},

        {"type": "content", "label": "How They Interact", "title": "The three reinforce one another",
         "blocks": [
             {"t": "flow", "steps": [
                 "Not recognised as rights-holders",
                 "so excluded from the decision process",
                 "so the harm is dumped on them",
                 "and their suffering stays invisible"]},
             {"t": "hbox", "color": "red", "html": "Misrecognition feeds exclusion, which feeds "
              "maldistribution. Fixing one without the others rarely holds. A relocation package "
              "(distribution) cannot repair a process that treated people as obstacles."},
         ]},

        {"type": "content", "label": "A Fourth Dimension", "title": "Intergenerational justice",
         "blocks": [
             {"t": "term", "word": "Intergenerational justice",
              "def": "Fairness across time &mdash; not bequeathing exhausted soils, poisoned "
              "aquifers, deforested hills and a destabilised climate to those not yet born."},
             {"t": "quote",
              "text": "We do not inherit the earth from our ancestors; we borrow it from our "
              "children.",
              "attr": "&mdash; a proverb widely invoked in environmental thought"},
         ]},

        {"type": "content", "label": "Applying It", "title": "Use the dimensions as a checklist",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Distribution:</strong> who gains, who loses, and along what social line?",
                 "<strong>Procedure:</strong> were the affected genuinely able to shape the "
                 "decision?",
                 "<strong>Recognition:</strong> are their rights, knowledge and identity "
                 "respected?",
                 "<strong>Future:</strong> what does this leave for the next generation?"]},
         ]},

        {"type": "content", "label": "A Caution", "title": "Compensation is not the same as justice",
         "blocks": [
             {"t": "body", "html": "A cheque can address distribution while leaving procedure and "
              "recognition untouched. People who were never consulted, whose sacred land was "
              "treated as empty, are not made whole by money alone."},
             {"t": "hbox", "color": "amber", "html": "Ask of any &lsquo;rehabilitation package&rsquo;: "
              "does it restore voice and dignity, or does it merely price the loss?"},
         ]},

        # ===================== SECTION 04 =====================
        {"type": "divider", "num": "04", "label": "Section Four",
         "title": "Who Bears the Burden"},

        {"type": "content", "label": "The Indian Axis", "title": "In India, environmental harm runs along caste and tribe",
         "blocks": [
             {"t": "body", "html": "Where the US movement names race, the Indian reality is "
              "structured by <strong>caste, class and tribe</strong>. Dalit and Adivasi "
              "communities are disproportionately exposed to polluted land, hazardous work and "
              "displacement &mdash; a pattern some scholars call <em>environmental casteism</em>."},
             {"t": "hbox", "color": "indigo", "html": "The dirtiest, most dangerous environmental "
              "work in India &mdash; sanitation, tanning, waste, mining &mdash; is overwhelmingly "
              "done by those at the bottom of the caste order."},
         ]},

        {"type": "content", "label": "Illustrative", "title": "Exposure tracks social group",
         "blocks": [
             {"t": "chart", "canvas": "exposureGroupChart",
              "title": "Share living near a polluting site or hazard, by social group (ILLUSTRATIVE)",
              "source": "Illustrative pattern &mdash; not an official statistic",
              "type": "bar",
              "data": {"labels": ["General", "OBC", "Scheduled Caste", "Scheduled Tribe"],
                       "datasets": [{"label": "Relative exposure (illustrative index)",
                                     "data": [20, 30, 48, 55],
                                     "backgroundColor": ["#10B981", "#0EA5E9", "#F59E0B", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:60,title:{display:true,text:'illustrative index'}} } }"}},
             {"t": "hbox", "color": "amber", "html": "The exact numbers here are illustrative. But "
              "the direction &mdash; that marginalised groups live closer to hazards &mdash; is "
              "consistently documented across Indian environmental-justice research."},
         ]},

        {"type": "content", "label": "Sacrifice Zones", "title": "&lsquo;Sacrifice zones&rsquo;",
         "blocks": [
             {"t": "term", "word": "Sacrifice zone",
              "def": "A place &mdash; and the people in it &mdash; treated as expendable for the "
              "sake of industry or growth: saturated with pollution, mining or waste because its "
              "residents are deemed to lack the power to refuse."},
             {"t": "body", "html": "India has its sacrifice zones: the thermal-power and "
              "coal-ash belt of Singrauli; the industrial clusters of Vapi and Ankleshwar; "
              "tanneries along stretches of riverbank. The air and water of the few are spent for "
              "the convenience of the many."},
         ]},

        {"type": "content", "label": "Manual Scavenging", "title": "Manual scavenging: caste and the most degrading work",
         "blocks": [
             {"t": "body", "html": "<strong>Manual scavenging</strong> &mdash; the manual cleaning "
              "of human excreta from dry latrines, sewers and septic tanks &mdash; is banned by "
              "law (the 2013 Act), yet persists. It is done almost entirely by Dalit communities, "
              "and workers still die from toxic gases in sewers and tanks."},
             {"t": "hbox", "color": "red", "html": "This is environmental injustice at its most "
              "naked: a hazard assigned by birth, where caste, sanitation and lethal exposure are "
              "fused into a single occupation."},
         ]},

        {"type": "content", "label": "Waste Pickers", "title": "Waste pickers: the informal backbone of recycling",
         "blocks": [
             {"t": "body", "html": "Millions of <strong>waste pickers</strong> &mdash; largely "
              "Dalit, Muslim, migrant and women &mdash; sort and recover the recyclables that keep "
              "Indian cities from drowning in their own waste. They handle the toxic without "
              "protection and are rarely counted as workers."},
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "The service", "blocks": [
                  {"t": "body", "cls": "sm", "html": "They divert vast tonnage from landfills, "
                   "cut emissions and supply the recycling economy &mdash; an unpaid public "
                   "good."}]}],
              "right": [{"t": "panel", "color": "red", "title": "The cost", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Cuts, infections, respiratory disease, "
                   "stigma &mdash; and displacement when cities privatise waste into machines and "
                   "contracts."}]}]},
         ]},

        {"type": "content", "label": "Gendered Burden", "title": "Women carry the household's environmental load",
         "blocks": [
             {"t": "body", "html": "When the well runs dry or the forest recedes, it is most "
              "often women who walk further for water and fuel, who breathe the smoke of a "
              "biomass <em>chulha</em>, and who manage scarcity in the home."},
             {"t": "hbox", "color": "indigo", "html": "Environmental degradation is not gender-"
              "neutral. The same drought, deforestation or pollution lands hardest on those "
              "already doing the most unpaid care and provisioning work."},
         ]},

        {"type": "content", "label": "Adivasi Lands", "title": "Resources lie under Adivasi homelands",
         "blocks": [
             {"t": "body", "html": "A cruel geography: much of India's coal, bauxite and iron ore "
              "sits beneath the forests of central and eastern India &mdash; the homelands of "
              "<strong>Adivasi (Scheduled Tribe)</strong> communities. Extraction repeatedly "
              "means their displacement."},
             {"t": "hbox", "color": "amber", "html": "Adivasis are a minority of India's "
              "population but a large share of those displaced by mines, dams and industry. The "
              "mineral wealth is theirs by geography and the loss is theirs by power."},
         ]},

        {"type": "content", "label": "Illustrative", "title": "Who lives near the hazard?",
         "blocks": [
             {"t": "chart", "canvas": "proximityChart",
              "title": "Composition of settlements adjacent to polluting sites (ILLUSTRATIVE)",
              "source": "Illustrative pattern &mdash; not an official statistic",
              "type": "doughnut",
              "data": {"labels": ["SC / Dalit", "ST / Adivasi", "OBC", "General"],
                       "datasets": [{"data": [32, 28, 25, 15],
                                     "backgroundColor": ["#F59E0B", "#EF4444", "#0EA5E9", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
             {"t": "hbox", "color": "amber", "html": "Illustrative shares &mdash; but the "
              "well-documented reality is that marginalised groups are over-represented in the "
              "settlements pressed up against pollution, while their share of the benefit is "
              "small."},
         ]},

        {"type": "content", "label": "Intersection", "title": "Burdens stack, they do not simply add",
         "blocks": [
             {"t": "bullets", "items": [
                 "A <strong>poor Adivasi woman</strong> in a mining district faces several "
                 "injustices at once",
                 "Caste, class, gender and indigeneity <strong>compound</strong>, not merely "
                 "coexist",
                 "Policy that addresses only one axis <strong>leaves the rest in place</strong>",
                 "Centring the most-burdened is the surest test of a just intervention"]},
         ]},

        # ===================== SECTION 05 =====================
        {"type": "divider", "num": "05", "label": "Section Five",
         "title": "Climate Justice"},

        {"type": "content", "label": "The Core Claim", "title": "Those who caused least, suffer most",
         "blocks": [
             {"t": "body", "html": "Climate justice extends environmental justice to the planet. "
              "The countries and classes that contributed least to greenhouse gases &mdash; the "
              "poor of the Global South &mdash; face the harshest floods, heatwaves, cyclones and "
              "crop failures."},
             {"t": "hbox", "color": "red", "html": "India is among the most climate-vulnerable "
              "large countries, yet its historical contribution to the problem is small. That gap "
              "between cause and consequence is the heart of climate justice."},
         ]},

        {"type": "content", "label": "CBDR", "title": "Common but differentiated responsibilities",
         "blocks": [
             {"t": "term", "word": "CBDR",
              "def": "Common But Differentiated Responsibilities &mdash; a principle of the UN "
              "Framework Convention on Climate Change (UNFCCC, 1992): all states must act, but "
              "those who emitted more historically, and can do more, must do more."},
             {"t": "hbox", "color": "cyan", "html": "CBDR is the legal expression of climate "
              "fairness: equal duty to act, unequal share of the burden &mdash; weighted by "
              "history and capacity."},
         ]},

        {"type": "content", "label": "Per Capita", "title": "Per-capita emissions: India sits far below the rich world",
         "blocks": [
             {"t": "chart", "canvas": "perCapitaCO2Chart",
              "title": "Per-capita CO&#8322; emissions, tonnes per person per year (approximate)",
              "source": "Pattern per Global Carbon Project / Our World in Data; figures approximate",
              "type": "bar",
              "data": {"labels": ["Qatar", "United States", "China", "World avg", "India", "Nigeria"],
                       "datasets": [{"label": "t CO₂ per capita",
                                     "data": [37, 14.5, 8, 4.7, 2, 0.6],
                                     "backgroundColor": ["#EF4444", "#F59E0B", "#F59E0B", "#6366F1", "#10B981", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,title:{display:true,text:'t CO₂ / person / yr'}} } }"}},
             {"t": "hbox", "color": "green", "html": "India's per-capita emissions are roughly a "
              "third of the world average and a fraction of the US figure &mdash; a well-"
              "established fact. Per-capita framing tells a very different story from totals."},
         ]},

        {"type": "content", "label": "Two Lenses", "title": "Total vs per-capita: both are true",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "amber", "title": "By total", "blocks": [
                  {"t": "body", "cls": "sm", "html": "India is among the largest annual emitters "
                   "in absolute terms &mdash; because it has 1.4 billion people. The total is "
                   "large."}]}],
              "right": [{"t": "panel", "color": "green", "title": "Per person", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Per Indian, emissions are far below the "
                   "global-North average. The average citizen's footprint is small."}]}]},
             {"t": "hbox", "color": "cyan", "html": "Both statements are correct. Which one you "
              "lead with is a justice choice &mdash; it decides who is asked to cut, and by how "
              "much."},
         ]},

        {"type": "content", "label": "History Counts", "title": "Historical vs current emissions",
         "blocks": [
             {"t": "chart", "canvas": "histEmissionsChart",
              "title": "Share of cumulative historical CO&#8322; emissions (approximate, illustrative split)",
              "source": "Illustrative, patterned on cumulative-emissions estimates",
              "type": "doughnut",
              "data": {"labels": ["United States", "EU", "China", "India", "Rest of world"],
                       "datasets": [{"data": [24, 17, 14, 3, 42],
                                     "backgroundColor": ["#EF4444", "#F59E0B", "#6366F1", "#10B981", "#475569"]}]},
              "options": {"__js__": "{ plugins:{legend:{position:'right'}} }"}},
             {"t": "hbox", "color": "amber", "html": "Carbon dioxide lingers for centuries, so "
              "cumulative emissions matter. The industrialised North holds the largest historical "
              "share while India's cumulative share is small relative to its population."},
         ]},

        {"type": "content", "label": "Loss & Damage", "title": "Loss and damage: paying for harm already done",
         "blocks": [
             {"t": "term", "word": "Loss and damage",
              "def": "The unavoidable harm from climate change that adaptation cannot prevent "
              "&mdash; lost lives, lands, crops and cultures &mdash; and the claim that those who "
              "caused it should help bear the cost."},
             {"t": "body", "html": "After decades of demands from vulnerable nations, a "
              "<strong>Loss and Damage Fund</strong> was agreed at the UN climate talks "
              "(COP27, 2022; operationalised at COP28, 2023) &mdash; a hard-won recognition that "
              "some harm is already irreversible."},
         ]},

        {"type": "content", "label": "The Carbon Budget", "title": "A shrinking budget, an unequal claim",
         "blocks": [
             {"t": "body", "html": "Holding warming to safe limits leaves only a finite "
              "<strong>carbon budget</strong> of remaining emissions. The justice question: should "
              "that budget be split by current emissions, by population, or by historical "
              "responsibility?"},
             {"t": "hbox", "color": "indigo", "html": "An <strong>equal per-capita</strong> claim "
              "would grant developing countries far more of the remaining budget than current "
              "shares allow &mdash; which is exactly why the framing is contested."},
         ]},

        {"type": "content", "label": "Adaptation", "title": "Adaptation is a justice issue too",
         "blocks": [
             {"t": "bullets", "items": [
                 "The poor have the <strong>least capacity to adapt</strong> &mdash; no insurance, "
                 "savings or air-conditioning",
                 "Heat, floods and cyclones hit <strong>informal homes and outdoor workers</strong> "
                 "hardest",
                 "Adaptation finance is <strong>scarce and slow</strong> to reach frontline "
                 "communities",
                 "Just adaptation means <strong>resourcing those least responsible</strong> to "
                 "cope"]},
         ]},

        # ===================== SECTION 06 =====================
        {"type": "divider", "num": "06", "label": "Section Six",
         "title": "Land, Forest &amp; the Commons"},

        {"type": "content", "label": "The Commons", "title": "Forests, grazing land and water are shared wealth",
         "blocks": [
             {"t": "term", "word": "The commons",
              "def": "Resources held and used collectively &mdash; village forests, grazing land, "
              "ponds, rivers, fisheries &mdash; on which the poorest most depend for fuel, fodder, "
              "food and water."},
             {"t": "hbox", "color": "green", "html": "When commons are privatised, enclosed or "
              "degraded, it is the landless and forest-dependent who lose a safety net that never "
              "appeared on any balance sheet."},
         ]},

        {"type": "content", "label": "A Historic Wrong", "title": "Colonial forest law made dwellers into trespassers",
         "blocks": [
             {"t": "body", "html": "Colonial-era forest laws declared vast forests state property "
              "and recast the communities who had lived in them for generations as encroachers. "
              "Independence did not immediately undo this; forest-dwellers remained legally "
              "insecure for decades."},
             {"t": "hbox", "color": "amber", "html": "Recognising this &lsquo;historical "
              "injustice&rsquo; is the explicit purpose of India's Forest Rights Act &mdash; the "
              "law names the wrong it seeks to repair."},
         ]},

        {"type": "content", "label": "FRA 2006", "title": "The Forest Rights Act, 2006",
         "blocks": [
             {"t": "body", "html": "The <strong>Scheduled Tribes and Other Traditional Forest "
              "Dwellers (Recognition of Forest Rights) Act, 2006</strong> &mdash; the FRA &mdash; "
              "recognises the rights of Adivasis and other forest-dwellers to live in, use and "
              "<strong>govern</strong> the forests they have long depended on."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "Individual rights", "label": "to cultivate &amp; hold forest land one "
                  "occupies", "color": "cyan"},
                 {"num": "Community rights", "label": "incl. Community Forest Resource rights to "
                  "manage the forest", "color": "green"}]},
         ]},

        {"type": "content", "label": "Gram Sabha", "title": "FRA puts the village assembly in charge",
         "blocks": [
             {"t": "body", "html": "A radical feature of the FRA: the <strong>Gram Sabha</strong> "
              "&mdash; the full village assembly &mdash; is the authority that initiates and "
              "verifies claims. It shifts power over the forest from the forest department toward "
              "the community itself."},
             {"t": "hbox", "color": "indigo", "html": "This is recognition justice written into "
              "statute &mdash; though in practice implementation is uneven, and Community Forest "
              "Resource rights remain under-recognised in many states."},
         ]},

        {"type": "content", "label": "PESA 1996", "title": "PESA, 1996: self-rule in Scheduled Areas",
         "blocks": [
             {"t": "body", "html": "The <strong>Panchayats (Extension to Scheduled Areas) Act, "
              "1996</strong> &mdash; PESA &mdash; extends local self-government to tribal "
              "Scheduled Areas and empowers the Gram Sabha to safeguard community resources, "
              "customs and, crucially, to be consulted before land acquisition and mining."},
             {"t": "hbox", "color": "cyan", "html": "Together, PESA and the FRA give the Gram "
              "Sabha real legal standing over land and forest &mdash; the procedural and "
              "recognition tools that the Niyamgiri verdict would later put to the test."},
         ]},

        {"type": "content", "label": "Displacement", "title": "Development-induced displacement",
         "blocks": [
             {"t": "term", "word": "Development-induced displacement",
              "def": "The forced uprooting of people to make way for dams, mines, highways, "
              "industry or conservation projects &mdash; in the name of a public good they may "
              "never share in."},
             {"t": "body", "html": "Since 1947, tens of millions of Indians have been displaced by "
              "development projects, with Adivasis vastly over-represented. A majority were never "
              "adequately resettled &mdash; displacement without rehabilitation."},
         ]},

        {"type": "content", "label": "Illustrative", "title": "Adivasis are over-represented among the displaced",
         "blocks": [
             {"t": "chart", "canvas": "displacedShareChart",
              "title": "Adivasi share: of population vs of those displaced by projects (ILLUSTRATIVE)",
              "source": "Illustrative, patterned on displacement-studies estimates",
              "type": "bar",
              "data": {"labels": ["Share of India's population", "Share of project-displaced"],
                       "datasets": [{"label": "Adivasi share (%)",
                                     "data": [8.6, 40],
                                     "backgroundColor": ["#0EA5E9", "#EF4444"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,max:50,title:{display:true,text:'%'}} } }"}},
             {"t": "hbox", "color": "red", "html": "Adivasis are about 8.6% of India's "
              "population (Census 2011) yet, by widely cited estimates, a far larger share of "
              "those displaced by dams, mines and industry. The exact displaced-share is "
              "illustrative; the over-representation is well-documented."},
         ]},

        {"type": "content", "label": "R&R", "title": "Resettlement and rehabilitation &mdash; promised, often unmet",
         "blocks": [
             {"t": "body", "html": "The <strong>LARR Act, 2013</strong> (Right to Fair "
              "Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement) "
              "promised consent, social-impact assessment and rehabilitation &mdash; raising the "
              "legal bar for acquiring land."},
             {"t": "hbox", "color": "red", "html": "But cash compensation cannot replace a "
              "commons, a community or a way of life. Rehabilitation that ignores livelihood and "
              "belonging leaves people &lsquo;compensated&rsquo; yet destitute."},
         ]},

        {"type": "content", "label": "The Just Test", "title": "Who decides what counts as &lsquo;public purpose&rsquo;?",
         "blocks": [
             {"t": "bullets", "color": "amber", "items": [
                 "A &lsquo;public purpose&rsquo; for whom &mdash; the city, the company, or the "
                 "displaced?",
                 "Was free, prior and informed <strong>consent</strong> genuinely obtained?",
                 "Does rehabilitation restore <strong>livelihood</strong>, not just housing?",
                 "Are the <strong>commons</strong> and intangible losses counted at all?"]},
         ]},

        # ===================== SECTION 07 =====================
        {"type": "divider", "num": "07", "label": "Section Seven",
         "title": "Pollution &amp; Health"},

        {"type": "content", "label": "The Burden", "title": "Pollution is a leading cause of premature death",
         "blocks": [
             {"t": "body", "html": "Pollution &mdash; of air, water and soil &mdash; is among the "
              "largest environmental causes of disease and premature death in India. And the "
              "burden, as ever, falls hardest on the poor, who cannot move away from it."},
             {"t": "term", "word": "Environmental burden of disease",
              "def": "The share of illness, disability and death attributable to environmental "
              "hazards such as polluted air, unsafe water and toxic exposure &mdash; much of it "
              "preventable."},
         ]},

        {"type": "content", "label": "Air Crisis", "title": "India's air-quality crisis",
         "blocks": [
             {"t": "chart", "canvas": "pm25CitiesChart",
              "title": "Typical annual PM2.5 vs WHO guideline, &micro;g/m&#179; (approximate)",
              "source": "Pattern per WHO / IQAir city data; figures approximate",
              "type": "bar",
              "data": {"labels": ["Delhi", "Patna", "Kolkata", "Mumbai", "Bengaluru", "WHO guideline"],
                       "datasets": [{"label": "PM2.5 (µg/m³)",
                                     "data": [100, 90, 65, 45, 35, 5],
                                     "backgroundColor": ["#EF4444", "#EF4444", "#F59E0B", "#F59E0B", "#F59E0B", "#10B981"]}]},
              "options": {"__js__": "{ plugins:{legend:{display:false}}, scales:{ y:{min:0,title:{display:true,text:'µg/m³ (annual mean)'}} } }"}},
             {"t": "hbox", "color": "red", "html": "Many Indian cities run many times above the "
              "WHO annual PM2.5 guideline of 5&nbsp;&micro;g/m&#179; &mdash; a well-established "
              "fact. The figures here are approximate, but the scale of exceedance is real."},
         ]},

        {"type": "content", "label": "Unequal Air", "title": "Even the air is unequal",
         "blocks": [
             {"t": "body", "html": "Two people in the same city do not breathe the same air. The "
              "poor live closer to traffic, industry and waste-burning; cook with biomass; and "
              "work outdoors. The well-off retreat behind purifiers and air-conditioning."},
             {"t": "hbox", "color": "amber", "html": "Indoor air pollution from solid cooking "
              "fuels &mdash; borne mostly by women and children in poorer homes &mdash; is itself "
              "a major, and deeply unequal, killer."},
         ]},

        {"type": "content", "label": "Water", "title": "Water contamination: fluoride and arsenic",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "cyan", "title": "Fluoride", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Excess fluoride in groundwater across many "
                   "districts causes <em>fluorosis</em> &mdash; mottled teeth, bent bones, "
                   "crippling pain."}]}],
              "right": [{"t": "panel", "color": "indigo", "title": "Arsenic", "blocks": [
                  {"t": "body", "cls": "sm", "html": "Arsenic in groundwater &mdash; notably "
                   "across the Ganga&ndash;Brahmaputra plains &mdash; causes skin lesions and "
                   "cancers over years of exposure."}]}]},
             {"t": "hbox", "color": "red", "html": "These are geogenic contaminants, but the "
              "injustice is social: who has a safe alternative source, and who must keep drinking "
              "what the handpump gives."},
         ]},

        {"type": "content", "label": "E-Waste", "title": "E-waste: dismantling the digital age by hand",
         "blocks": [
             {"t": "body", "html": "India is among the largest generators of <strong>electronic "
              "waste</strong>, and most of it is processed in the informal sector &mdash; burned, "
              "acid-bathed and dismantled by hand in dense urban clusters, releasing lead, "
              "mercury and dioxins."},
             {"t": "hbox", "color": "amber", "html": "The workers, often including children, "
              "absorb the toxics so that the value can be recovered. The convenience of the "
              "connected becomes the poison of the informal recycler."},
         ]},

        {"type": "content", "label": "Industrial Clusters", "title": "Living in the shadow of the plant",
         "blocks": [
             {"t": "body", "html": "Communities ringed by chemical and industrial estates "
              "&mdash; in Gujarat, Tamil Nadu, Andhra Pradesh and beyond &mdash; live with "
              "contaminated groundwater, effluent in fields, and elevated rates of respiratory and "
              "skin disease."},
             {"t": "hbox", "color": "red", "html": "The Sterlite copper smelter in Thoothukudi "
              "(Tuticorin) became a flashpoint: years of complaints about pollution, then a 2018 "
              "protest in which police firing killed multiple residents."},
         ]},

        {"type": "content", "label": "The Through-Line", "title": "Pollution, poverty and powerlessness",
         "blocks": [
             {"t": "flow", "steps": [
                 "Poverty pushes people to cheap, hazardous land",
                 "Polluters site there &mdash; least resistance",
                 "Exposure causes disease &amp; lost earnings",
                 "which deepens the poverty that started it"]},
             {"t": "hbox", "color": "indigo", "html": "Pollution is not just a health problem laid "
              "on top of poverty &mdash; it is a mechanism that <em>produces</em> and entrenches "
              "poverty."},
         ]},

        # ===================== SECTION 08 =====================
        {"type": "divider", "num": "08", "label": "Section Eight",
         "title": "Just Transition"},

        {"type": "content", "label": "The Idea", "title": "Decarbonise &mdash; without abandoning workers",
         "blocks": [
             {"t": "term", "word": "Just transition",
              "def": "Moving an economy off fossil fuels and toward sustainability in a way that "
              "protects the workers and communities who depend on the old economy &mdash; so the "
              "burden of change is shared fairly."},
             {"t": "hbox", "color": "cyan", "html": "The slogan: <strong>leave no one behind.</strong> "
              "A climate solution that throws coal workers into destitution simply trades one "
              "injustice for another."},
         ]},

        {"type": "content", "label": "The Coal Belt", "title": "India's coal economy is a regional lifeline",
         "blocks": [
             {"t": "body", "html": "Coal anchors the economies of states like Jharkhand, "
              "Chhattisgarh, Odisha and West Bengal &mdash; supporting millions of jobs directly "
              "and indirectly, plus the local trade, transport and revenue built around them."},
             {"t": "hbox", "color": "amber", "html": "These are also among India's poorer, more "
              "Adivasi regions. A transition planned without them risks repeating the original "
              "extractive injustice in reverse."},
         ]},

        {"type": "content", "label": "Who Pays", "title": "The transition has its own distribution question",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "green", "title": "If done well", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Retraining and new livelihoods",
                      "Reclaimed land for the community",
                      "Local say in what comes next"]}]}],
              "right": [{"t": "panel", "color": "red", "title": "If done badly", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "Stranded workers, ghost towns",
                      "Abandoned, unhealed mine land",
                      "Decisions taken far away, again"]}]}]},
         ]},

        {"type": "content", "label": "Green Jobs", "title": "Green jobs are not automatic justice",
         "blocks": [
             {"t": "body", "html": "Renewable energy creates jobs &mdash; in manufacturing, "
              "installation and maintenance. But the new jobs may be in different places, demand "
              "different skills, and go to different people than the coal jobs they replace."},
             {"t": "hbox", "color": "indigo", "html": "&lsquo;Green&rsquo; does not guarantee "
              "&lsquo;fair&rsquo;. A solar park can still grab common land, and a green supply "
              "chain can still rest on exploited mining. Justice has to be designed in."},
         ]},

        {"type": "content", "label": "Land for Energy", "title": "Renewables need land &mdash; and land has people",
         "blocks": [
             {"t": "body", "html": "Large solar and wind parks require vast areas, often "
              "classified as &lsquo;wasteland&rsquo; &mdash; a label that erases the pastoralists, "
              "herders and commons-users who actually depend on that land."},
             {"t": "hbox", "color": "amber", "html": "There is no such thing as empty land. "
              "A just transition must apply the same consent and commons-protection standards to "
              "renewables that we demand of mines and dams."},
         ]},

        {"type": "content", "label": "Energy Access", "title": "Justice means energy <em>for</em> the poor too",
         "blocks": [
             {"t": "body", "html": "Climate justice is not only about cutting emissions. Hundreds "
              "of millions still need <strong>more</strong> clean, reliable energy to escape "
              "poverty &mdash; for light, cooking, irrigation and small enterprise."},
             {"t": "hbox", "color": "green", "html": "Decentralised renewables &mdash; rooftop "
              "solar, mini-grids &mdash; can deliver both: lower emissions and energy access, "
              "owned closer to the community."},
         ]},

        {"type": "content", "label": "Designing Fair", "title": "Principles for a just transition",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Plan early</strong>, with affected workers and communities at the table",
                 "<strong>Fund</strong> retraining, social protection and land restoration",
                 "<strong>Diversify</strong> local economies before the mines close, not after",
                 "<strong>Restore</strong> degraded land and water as part of the transition"]},
         ]},

        # ===================== SECTION 09 =====================
        {"type": "divider", "num": "09", "label": "Section Nine",
         "title": "Movements &amp; Resistance"},

        {"type": "content", "label": "People Power", "title": "Most environmental gains were won, not granted",
         "blocks": [
             {"t": "body", "html": "Behind almost every environmental protection in India stands a "
              "movement &mdash; villagers, fishers, forest-dwellers and their allies who refused "
              "to be sacrificed. Understanding EJ means understanding resistance."},
             {"t": "quote",
              "text": "The fight is not against development; it is about whose development, and at "
              "whose cost.",
              "attr": "&mdash; a recurring theme of Indian environmental movements"},
         ]},

        {"type": "content", "label": "Narmada", "title": "Narmada Bachao Andolan",
         "blocks": [
             {"t": "body", "html": "The <strong>Narmada Bachao Andolan</strong> (Save the Narmada "
              "Movement), led from the 1980s by activists including Medha Patkar, challenged the "
              "large dams on the Narmada &mdash; above all the Sardar Sarovar &mdash; over the "
              "displacement of hundreds of thousands, mostly Adivasi and farming families."},
             {"t": "hbox", "color": "cyan", "html": "It reshaped the global debate on big dams and "
              "forced rehabilitation onto the national agenda &mdash; a defining struggle over "
              "development, displacement and rights."},
         ]},

        {"type": "content", "label": "Niyamgiri", "title": "Niyamgiri: the Dongria Kondh say no",
         "blocks": [
             {"t": "body", "html": "When a company sought to mine bauxite from the Niyamgiri hills "
              "in Odisha &mdash; sacred to the <strong>Dongria Kondh</strong> Adivasi community "
              "&mdash; the Supreme Court ruled in 2013 that the Gram Sabhas should decide. Every "
              "village voted <strong>no</strong>."},
             {"t": "hbox", "color": "green", "html": "Niyamgiri became a landmark for recognition "
              "and procedural justice: the law treated the community's relationship to a sacred "
              "mountain, and its right to refuse, as decisive."},
         ]},

        {"type": "content", "label": "Anti-POSCO", "title": "Anti-POSCO: farmers hold the line in Odisha",
         "blocks": [
             {"t": "body", "html": "For years, villagers in Jagatsinghpur, Odisha resisted a "
              "massive proposed <strong>POSCO</strong> steel plant and captive port that would "
              "have taken their betel-vine farms, forests and fishing grounds. The project was "
              "eventually abandoned."},
             {"t": "hbox", "color": "amber", "html": "Their resistance leaned on the Forest Rights "
              "Act and the Gram Sabha &mdash; showing how legal recognition becomes a shield in "
              "the hands of an organised community."},
         ]},

        {"type": "content", "label": "Fisherfolk", "title": "Fisherfolk: defending the coast and the catch",
         "blocks": [
             {"t": "body", "html": "Coastal fishing communities &mdash; among India's poorest "
              "&mdash; resist ports, power plants, reclamation and pollution that destroy "
              "spawning grounds and block access to the sea. From the Kerala coast to Mumbai's "
              "Koli villages, the sea is both home and workplace."},
             {"t": "hbox", "color": "indigo", "html": "Coastal regulation that fails to protect "
              "traditional fishers' access is environmental injustice at the waterline &mdash; "
              "the commons of the sea enclosed for industry and real estate."},
         ]},

        {"type": "content", "label": "Many Fronts", "title": "A movement of movements",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Anti-nuclear:</strong> Koodankulam fisherfolk against a power plant",
                 "<strong>Anti-mining:</strong> communities across the central Indian mineral belt",
                 "<strong>Urban:</strong> citizens against waste dumps, felling and toxic estates",
                 "<strong>River &amp; wetland:</strong> defenders of lakes, rivers and floodplains"]},
         ]},

        {"type": "content", "label": "The Courts", "title": "Public Interest Litigation as a tool",
         "blocks": [
             {"t": "term", "word": "Public Interest Litigation (PIL)",
              "def": "A petition that lets any public-spirited person approach the courts on "
              "behalf of those unable to do so themselves &mdash; widening access to environmental "
              "justice in India."},
             {"t": "body", "html": "PILs have driven major environmental rulings &mdash; from "
              "cleaning the Ganga to relocating polluting industries and mandating CNG for Delhi's "
              "public transport. The courts became an arena where the unheard could be heard."},
         ]},

        {"type": "content", "label": "Costs of Defence", "title": "Defending the environment can be dangerous",
         "blocks": [
             {"t": "body", "html": "Environmental defenders &mdash; especially Adivasi and rural "
              "activists &mdash; face intimidation, criminalisation and violence. The Thoothukudi "
              "firing and attacks on land and forest activists are stark reminders."},
             {"t": "hbox", "color": "red", "html": "Recognising and protecting environmental "
              "defenders is itself a test of justice: a society that punishes those who protect "
              "the commons has its priorities inverted."},
         ]},

        # ===================== SECTION 10 =====================
        {"type": "divider", "num": "10", "label": "Section Ten",
         "title": "Principles &amp; Legal Tools"},

        {"type": "content", "label": "Polluter Pays", "title": "The polluter-pays principle",
         "blocks": [
             {"t": "term", "word": "Polluter-pays principle",
              "def": "Those who cause pollution should bear the cost of preventing, controlling "
              "and remedying it &mdash; rather than passing it to the public or to victims."},
             {"t": "body", "html": "Indian courts have repeatedly affirmed this principle, "
              "ordering polluting industries to fund clean-up and compensate affected communities "
              "&mdash; making the cost of harm sit with its cause."},
         ]},

        {"type": "content", "label": "Precaution", "title": "The precautionary principle",
         "blocks": [
             {"t": "term", "word": "Precautionary principle",
              "def": "Where an activity threatens serious or irreversible harm, lack of full "
              "scientific certainty should not be used to postpone protective measures. Absence of "
              "proof of harm is not proof of safety."},
             {"t": "hbox", "color": "cyan", "html": "It shifts the burden: the developer must show "
              "an activity is safe, rather than the community proving it is dangerous &mdash; often "
              "after the damage is already done."},
         ]},

        {"type": "content", "label": "Public Trust", "title": "The public-trust doctrine",
         "blocks": [
             {"t": "term", "word": "Public-trust doctrine",
              "def": "Natural resources such as air, rivers, forests and seashores are held by the "
              "state in trust for the public &mdash; they cannot be freely handed to private "
              "interests against the common good."},
             {"t": "body", "html": "Indian courts adopted this doctrine to protect rivers, "
              "beaches and forests, treating the government as a trustee accountable to the people "
              "&mdash; not an owner free to sell the commons."},
         ]},

        {"type": "content", "label": "The Constitution", "title": "A right to a healthy environment",
         "blocks": [
             {"t": "body", "html": "Indian courts have read the <strong>right to life</strong> "
              "(Article 21) to include the right to a clean and healthy environment &mdash; "
              "alongside constitutional duties on the state (Article 48A) and on citizens "
              "(Article 51A&#40;g&#41;) to protect nature."},
             {"t": "hbox", "color": "green", "html": "This constitutional anchor is what lets "
              "ordinary people bring environmental claims as fundamental-rights cases &mdash; the "
              "legal soil in which PILs grow."},
         ]},

        {"type": "content", "label": "The NGT", "title": "The National Green Tribunal, 2010",
         "blocks": [
             {"t": "body", "html": "The <strong>National Green Tribunal</strong>, established by "
              "statute in <strong>2010</strong>, is a specialised court for environmental cases. "
              "It combines legal and scientific expertise and is designed to deliver speedier, "
              "more accessible environmental justice."},
             {"t": "stats", "cols": 2, "cards": [
                 {"num": "2010", "label": "NGT Act establishes the Tribunal", "color": "cyan"},
                 {"num": "Polluter-pays", "label": "&amp; precaution are written into its mandate",
                  "color": "green"}]},
         ]},

        {"type": "content", "label": "Assessment", "title": "Environmental Impact Assessment",
         "blocks": [
             {"t": "term", "word": "Environmental Impact Assessment (EIA)",
              "def": "A mandatory study of a project's likely environmental and social effects "
              "before clearance &mdash; meant to include a public hearing for affected "
              "communities."},
             {"t": "hbox", "color": "amber", "html": "On paper the EIA is a tool of procedural "
              "justice. In practice it is often criticised for weak studies, token hearings and "
              "post-facto clearances &mdash; the form of participation drained of its power."},
         ]},

        {"type": "content", "label": "New Frontiers", "title": "Rights of nature",
         "blocks": [
             {"t": "term", "word": "Rights of nature",
              "def": "The emerging legal idea that rivers, forests and ecosystems are themselves "
              "rights-bearing entities &mdash; with legal standing &mdash; rather than mere "
              "property to be used."},
             {"t": "body", "html": "Courts in Uttarakhand once declared the Ganga and Yamuna "
              "&lsquo;living entities&rsquo; (a ruling later stayed), echoing moves in Ecuador and "
              "New Zealand. The frontier question: can a river sue on its own behalf?"},
         ]},

        {"type": "content", "label": "Tools in Hand", "title": "A practitioner's legal toolkit",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>FRA &amp; PESA</strong> &mdash; community rights and Gram Sabha consent",
                 "<strong>RTI</strong> &mdash; prise out the documents that decisions hide",
                 "<strong>EIA hearings</strong> &mdash; the formal moment to object on record",
                 "<strong>NGT &amp; PILs</strong> &mdash; the courts when other doors close"]},
         ]},

        # ===================== SECTION 11 =====================
        {"type": "divider", "num": "11", "label": "Section Eleven",
         "title": "EJ in Practice &amp; Reading"},

        {"type": "content", "label": "Community Monitoring", "title": "Community-led environmental monitoring",
         "blocks": [
             {"t": "body", "html": "Communities need not wait for official data. With low-cost "
              "<strong>air and water monitors</strong>, smartphones and simple protocols, "
              "residents can document pollution themselves &mdash; <em>community science</em> "
              "that makes the invisible visible and credible."},
             {"t": "hbox", "color": "cyan", "html": "Data gathered by the affected, in their own "
              "name, shifts power: it turns &lsquo;we feel sick&rsquo; into evidence that "
              "regulators and courts cannot easily dismiss."},
         ]},

        {"type": "content", "label": "Mapping Injustice", "title": "Make the pattern visible",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Map</strong> polluting sites against caste, income and settlement",
                 "<strong>Overlay</strong> health data to reveal exposure gradients",
                 "<strong>Disaggregate</strong> &mdash; an average hides who is hit hardest",
                 "<strong>Share</strong> findings back with the community, in their language"]},
             {"t": "hbox", "color": "indigo", "html": "What you do not disaggregate, you cannot "
              "see. Environmental injustice becomes undeniable only when the map and the social "
              "data are laid side by side."},
         ]},

        {"type": "content", "label": "A Practitioner's Stance", "title": "How to work justly with the environment",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Ask who bears the harm</strong> of every project &mdash; including your "
                 "own",
                 "<strong>Centre the most-burdened</strong>, not the average beneficiary",
                 "<strong>Treat consent as binding</strong>, not as a box to tick",
                 "<strong>Respect local knowledge</strong> as evidence, not anecdote",
                 "<strong>Give data back</strong> to those it was taken from"]},
         ]},

        {"type": "content", "label": "Common Pitfalls", "title": "Traps to avoid",
         "blocks": [
             {"t": "twocol", "ratio": "half",
              "left": [{"t": "panel", "color": "red", "title": "Watch for", "blocks": [
                  {"t": "bullets", "sm": True, "color": "red", "items": [
                      "&lsquo;Wasteland&rsquo; that is really someone's commons",
                      "Token hearings dressed as consultation",
                      "Cash that erases an uncounted way of life"]}]}],
              "right": [{"t": "panel", "color": "green", "title": "Aim for", "blocks": [
                  {"t": "bullets", "sm": True, "color": "green", "items": [
                      "Free, prior and informed consent",
                      "Restoration of livelihood, not just housing",
                      "Decisions made with, not for"]}]}]},
         ]},

        {"type": "content", "label": "Where to Look", "title": "Data and organisations to know",
         "blocks": [
             {"t": "bullets", "items": [
                 "<strong>Central / State Pollution Control Boards</strong> &mdash; air and water "
                 "monitoring data",
                 "<strong>Our World in Data &amp; the Global Carbon Project</strong> &mdash; "
                 "emissions comparisons",
                 "<strong>The Environmental Justice Atlas (EJAtlas)</strong> &mdash; a global map "
                 "of EJ conflicts",
                 "<strong>India's environmental research &amp; legal groups</strong> &mdash; "
                 "CSE, the NGT's orders, and academic studies"]},
         ]},

        {"type": "content", "label": "Keep Reading", "title": "A short, honest reading list",
         "blocks": [
             {"t": "bullets", "color": "indigo", "items": [
                 "<em>Ecology and Equity</em> &mdash; Madhav Gadgil &amp; Ramachandra Guha",
                 "<em>The Environmentalism of the Poor</em> &mdash; Joan Martinez-Alier",
                 "<em>Environmentalism: A Global History</em> &mdash; Ramachandra Guha",
                 "<em>This Fissured Land</em> &mdash; Gadgil &amp; Guha (India's ecological "
                 "history)",
                 "Reports of the EJAtlas and India's environmental-justice scholars"]},
             {"t": "hbox", "color": "cyan", "html": "Pair this deck with ImpactMojo's "
              "<strong>Climate &amp; Development</strong>, <strong>Land Rights</strong> and "
              "<strong>Adivasi Rights</strong> 101 courses."},
         ]},

        {"type": "content", "label": "The Takeaways", "title": "If you remember five things",
         "blocks": [
             {"t": "bullets", "color": "green", "items": [
                 "<strong>Environmental harm is not shared fairly</strong> &mdash; it tracks "
                 "caste, class and power",
                 "<strong>Justice has three faces</strong> &mdash; distribution, procedure and "
                 "recognition",
                 "<strong>Those who caused least, suffer most</strong> &mdash; the core of climate "
                 "justice",
                 "<strong>Law is a tool, not a guarantee</strong> &mdash; FRA, PESA, NGT, PILs in "
                 "the right hands",
                 "<strong>There is no empty land</strong> &mdash; behind every &lsquo;site&rsquo; "
                 "are people"]},
         ]},

        # ===================== END =====================
        {"type": "end",
         "eyebrow": "Environmental Justice 101 &middot; Complete",
         "headline": "Ask who bears<br>the harm.",
         "byline": "Behind every pipeline, dam, dump and degree of warming are people who did "
                   "least to cause it and stand to lose the most. Carry that question into every "
                   "project. Explore the rest of the ImpactMojo 101 Series, free forever.",
         "ctas": [
             {"label": "More 101 Courses", "href": "https://www.impactmojo.in/101-courses/"},
             {"label": "Explore ImpactMojo", "href": "https://www.impactmojo.in"},
             {"label": "Dataverse", "href": "https://www.impactmojo.in/dataverse.html"}],
         "meta": ["CC BY-NC-ND 4.0", "Free Forever", "ImpactMojo 101 Series"]},
    ],
}
