/* =============================================================================
   ImpactMojo — Fundamentals: The Sustainable Livelihoods Framework
   -----------------------------------------------------------------------------
   The framework is DFID's, set out in the Sustainable Livelihoods Guidance
   Sheets (1999). It formalised an argument made by Robert Chambers and Gordon
   Conway in "Sustainable Rural Livelihoods: Practical Concepts for the 21st
   Century" (IDS Discussion Paper 296, 1992), and given its analytical shape by
   Ian Scoones in "Sustainable Rural Livelihoods: A Framework for Analysis"
   (IDS Working Paper 72, 1998).

   Its central move is to stop asking what a household earns and start asking
   what it holds. Five capitals — human, social, natural, physical, financial —
   are drawn as a pentagon whose shape changes from household to household. A
   livelihood is what someone can construct out of that shape, inside a
   vulnerability context they do not control, and through structures and
   processes that decide what each asset is actually worth.

   ImpactMojo adds the Indian evidence.

   THE SHAPE IS THE POINT. Two households with the same income can hold
   completely different pentagons, and will survive completely different shocks.
   The framework's practical use is that it makes the missing corner visible.

   Scores are 0-100, assigned by the editorial team from the evidence attached
   to each case. They are comparative rather than absolute, and they are
   arguable — which is why the evidence sits under each one.

   Every figure is from a named source with a year.
   ============================================================================= */

window.LIVELIHOODS = (function () {
  "use strict";

  /* The five capitals, in the order they are drawn, clockwise from the top. */
  var capitals = [
    { id: "human", name: "Human", color: "#B45309", short: "H",
      gloss: "Labour, skill, health, education — what a household can do with its own bodies.",
      detail: "The one asset almost every household has some of, and the one that is spent by using it. Illness converts human capital into a financial liability faster than any other shock in the Indian data." },
    { id: "social", name: "Social", color: "#6D28D9", short: "S",
      gloss: "Networks, membership, claims on others, and the relationships that produce them.",
      detail: "The most contested of the five. Networks that carry a household through a bad season are the same networks that enforce who may do which work, so social capital is not automatically an asset to everyone inside it." },
    { id: "natural", name: "Natural", color: "#15803D", short: "N",
      gloss: "Land, water, forest, grazing, fish — the resource base a livelihood draws on.",
      detail: "In India this is mostly land, and land is also what makes the other capitals accessible: it is the collateral that opens institutional credit, and the address that opens a scheme." },
    { id: "physical", name: "Physical", color: "#0369A1", short: "P",
      gloss: "Infrastructure and producer goods: road, power, water, tools, transport, storage.",
      detail: "Largely supplied by the state rather than accumulated by the household, which makes it the capital most responsive to policy and the one most unevenly distributed by geography." },
    { id: "financial", name: "Financial", color: "#BE185D", short: "F",
      gloss: "Savings, credit, remittances, pensions, insurance — stocks and inflows of money.",
      detail: "The framework treats credit as an asset. Indian evidence complicates that: for households without land, credit arrives on terms that make it closer to a liability, which the case data below shows directly." }
  ];

  /* Shocks, trends and seasonality — the context a household does not choose. */
  var contexts = [
    { id: "shock", name: "Shocks", gloss: "Sudden and mostly unpredictable: illness, death, flood, drought, crop or livestock loss, eviction, a factory closing." },
    { id: "trend", name: "Trends", gloss: "Slow and directional: groundwater decline, soil loss, mechanisation, price movements, the shrinking of common land." },
    { id: "season", name: "Seasonality", gloss: "Predictable and still punishing: the lean months between harvests, when prices are highest and work is scarcest." }
  ];

  /* ------------------------------------------------------------------ cases */
  var cases = [
    {
      id: "marginal",
      name: "A marginal farmer",
      short: "One hectare or less, rainfed",
      assets: { human: 55, social: 50, natural: 32, physical: 38, financial: 28 },
      strategy: "Farm the plot, and sell labour for the rest of the year. The household is classified as agricultural, and most of its income is not from its own farm.",
      context: { shock: "Crop failure, and illness — the two shocks that convert a marginal holding into a sold one.", trend: "Falling water tables and rising input costs, against output prices that move with a market the household does not enter on good terms.", season: "Income arrives twice a year and expenses arrive monthly." },
      structures: "Whether the plot is recorded in the household's name decides access to institutional credit, crop insurance and most scheme entitlements. A tenant farming the same land holds the natural capital and not the papers.",
      reading: "The defining shape of Indian agriculture: a household whose natural capital is real but too small to carry it, so human capital is sold to fill the gap. That is not a failure of farming — it is the arithmetic of the holding.",
      complication: "The pentagon looks the same for a household one bad season from selling the land and for one steadily accumulating. Assets are a stock, and the framework does not by itself show which direction the stock is moving.",
      evidence: [
        { stat: "70.4%", detail: "of agricultural households possess one hectare or less. 0.37% possess more than ten.", source: "MoSPI, NSS 77th Round, Land and Livestock Holdings, All India", year: "2018-19" },
        { stat: "₹4,063", detail: "The average agricultural household's monthly income from wages, against ₹3,058 from crop production. Wages are the larger share, for the households that agriculture defines.", source: "MoSPI, NSS 77th Round, Situation Assessment Survey, All India, both paid-out and imputed expenditure", year: "2018-19" },
        { stat: "₹8,337", detail: "Total average monthly income per agricultural household — ₹4,063 wages, ₹3,058 crop, ₹641 non-farm business, ₹611 pension and remittance, ₹441 animal farming, ₹134 leasing out land.", source: "MoSPI, NSS 77th Round, Situation Assessment Survey, All India", year: "2018-19" }
      ]
    },
    {
      id: "landless",
      name: "A landless labourer",
      short: "Human capital, sold by the day",
      assets: { human: 52, social: 42, natural: 8, physical: 26, financial: 12 },
      strategy: "Sell labour, locally when there is work and elsewhere when there is not. MGNREGA in the gap, where it functions.",
      context: { shock: "Any illness at all. With no asset to sell, a lost working fortnight is met by borrowing.", trend: "Mechanisation of the operations that used to absorb the most hired labour, particularly harvesting.", season: "The lean season is the whole problem: work disappears exactly when prices rise." },
      structures: "Credit. Without land there is no collateral, and the terms available change completely — which is the sharpest single finding in the Indian asset data.",
      reading: "The pentagon collapses on the natural axis, and the collapse propagates: no land means no collateral, no collateral means no institutional credit, and no institutional credit means borrowing at rates that keep the financial corner permanently small.",
      complication: "Human capital is not evenly sellable. Caste decides which work is available and at what rate, and the framework's five axes have no place to record that. Read this case beside the Wheel of Power.",
      evidence: [
        { stat: "50.3%", detail: "of the amount of loan outstanding to households possessing under 0.01 hectares is owed to professional moneylenders. For households with more than ten hectares it is 5.2%.", source: "MoSPI, NSS 77th Round, distribution of loan outstanding by source, All India", year: "2018-19" },
        { stat: "13.5%", detail: "of the landless households' outstanding credit comes from commercial banks. For the largest holdings it is 55.8%. Land is what buys access to the banking system.", source: "MoSPI, NSS 77th Round, distribution of loan outstanding by source, All India", year: "2018-19" },
        { stat: "One-third", detail: "MGNREGA guarantees up to 100 days per rural household at a statutory wage, with at least a third of beneficiaries to be women. It is the one part of this pentagon the state supplies directly.", source: "MGNREGA 2005, s.3 and Schedule II", year: "2005" }
      ]
    },
    {
      id: "large",
      name: "A large landholder",
      short: "Ten hectares and up, irrigated",
      assets: { human: 62, social: 78, natural: 88, physical: 76, financial: 82 },
      strategy: "Farm at a scale that carries a bad year, and use land as the instrument that opens everything else.",
      context: { shock: "The same weather, absorbed rather than survived.", trend: "The same input prices, paid from a position that can hedge or store.", season: "Storage and credit both convert seasonality from a crisis into a decision about when to sell." },
      structures: "The same structures, working the other way round. Procurement, insurance and institutional credit are all built around recorded land, and this is the household that has it.",
      reading: "Included as the contrast case, because the framework's value is comparative. The pentagon is close to full, and the reason is not that this household works harder — it is that one corner, natural capital, unlocks the other four.",
      complication: "0.37% of agricultural households are in this class. A framework that shows what a full pentagon looks like should also say how rare it is.",
      evidence: [
        { stat: "55.8%", detail: "of outstanding credit to households with more than ten hectares comes from commercial banks, and a further 5.8% from regional rural banks. Institutional sources are the majority of the borrowing.", source: "MoSPI, NSS 77th Round, distribution of loan outstanding by source, All India", year: "2018-19" },
        { stat: "0.37%", detail: "of agricultural households possess more than ten hectares.", source: "MoSPI, NSS 77th Round, Land and Livestock Holdings, All India", year: "2018-19" },
        { stat: "₹2,081", detail: "Monthly wage income of the largest ST agricultural households, against ₹5,400 for those with almost no land. Wage dependence falls as landholding rises — the two capitals substitute for one another.", source: "MoSPI, NSS 77th Round, Situation Assessment Survey, ST households, All India", year: "2018-19" }
      ]
    },
    {
      id: "forest",
      name: "A forest-dwelling household",
      short: "Natural capital, held without title",
      assets: { human: 48, social: 62, natural: 66, physical: 18, financial: 16 },
      strategy: "Collect and sell minor forest produce, cultivate a recorded or unrecorded plot, and take wage work in the season.",
      context: { shock: "Eviction, and the criminalisation of ordinary use.", trend: "Diversion of forest land, and the slow contest over whether the community's claim is recognised at all.", season: "Forest produce is intensely seasonal and its prices are set by traders who are not." },
      structures: "The Forest Rights Act 2006, and whether its individual and community claims have actually been recorded. This case exists to show that natural capital and the legal recognition of it are different assets.",
      reading: "A pentagon with a large natural corner and almost nothing on the physical or financial axes. The gap is not remoteness alone: an asset the state does not recognise cannot be pledged, insured or compensated when it is taken.",
      complication: "Community forest rights are held collectively, and the framework's household pentagon has no clean way to draw an asset that belongs to a village rather than a family. The score here is a compromise and should be read as one.",
      evidence: [
        { stat: "2006", detail: "The Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act recognises individual and community rights over forest land and produce, and records that these rights pre-existed the state's own claim rather than being created by it.", source: "Forest Rights Act 2006, preamble and s.3", year: "2006" },
        { stat: "s.3(1)(c)", detail: "grants the right of ownership, access, use and disposal of minor forest produce traditionally collected — the provision that turns collection from a tolerated activity into a property right.", source: "Forest Rights Act 2006", year: "2006" },
        { stat: "2013", detail: "In the Niyamgiri decision the Supreme Court referred the question of a bauxite mine to the gram sabhas of the affected villages, which then refused consent. It remains the clearest Indian instance of a community's natural capital being treated as a right to decide rather than a resource to compensate.", source: "Orissa Mining Corporation v Ministry of Environment & Forests, Supreme Court of India", year: "2013" }
      ]
    },
    {
      id: "pastoralist",
      name: "A pastoralist household",
      short: "Wealth that walks, on land nobody records",
      assets: { human: 50, social: 70, natural: 44, physical: 20, financial: 34 },
      strategy: "Move herds along established routes between seasons, converting grazing that cannot be owned into milk, wool and animals that can be sold.",
      context: { shock: "Disease in the herd, and a blocked route.", trend: "The steady enclosure of commons and the fencing of migration corridors — a decline in an asset that appears in no land record.", season: "The migration itself is the seasonal strategy, not a response to a bad year." },
      structures: "Whether grazing commons and migration routes have any legal standing. Mostly they do not, which is why this household's natural capital can shrink without anything being recorded as lost.",
      reading: "The case that shows what the framework catches and conventional statistics miss. Livestock is visible, mobile and countable; the grazing that sustains it is a common-pool resource with no title, so a pastoralist can be dispossessed without a single transaction appearing anywhere.",
      complication: "Social capital scores high here because the migration depends on long-standing arrangements with settled villages along the route. Those same arrangements are the first thing to break when land use changes, so this is the least stable high score on the board.",
      evidence: [
        { stat: "s.3(1)(d)", detail: "The Forest Rights Act recognises community rights of use and entitlement including grazing, \u201cboth settled or transhumant\u201d, and traditional seasonal resource access for nomadic and pastoralist communities. It is the clearest statutory acknowledgement that a migration route is an asset.", source: "Forest Rights Act 2006", year: "2006" },
        { stat: "s.3(1)(e)", detail: "extends rights to nomadic and pastoralist communities specifically, alongside primitive tribal groups and pre-agricultural communities \u2014 a category the land record has no other way of reaching.", source: "Forest Rights Act 2006", year: "2006" }
      ]
    },
    {
      id: "fisher",
      name: "A small-scale marine fisher",
      short: "A common-pool resource, and a boat",
      assets: { human: 54, social: 66, natural: 40, physical: 44, financial: 30 },
      strategy: "Fish from a small craft, sell to an agent at the landing, and stay off the water in the ban and the monsoon.",
      context: { shock: "Cyclone, and a season that does not arrive.", trend: "Stock decline, and competition from mechanised vessels working the same water with entirely different capital.", season: "The monsoon ban is both a conservation measure and a guaranteed annual income gap." },
      structures: "Who is allowed to fish where, and who buys the catch. The agent who provides the pre-season advance is usually also the buyer, which is the arrangement that decides the price.",
      reading: "Natural capital that no one owns and everyone draws on, which is exactly the case Ostrom's work is about. The financial corner is small not because credit is unavailable but because the credit available is tied to the sale.",
      complication: "Scoring a common-pool resource on a household pentagon is a compromise, the same one the pastoralist case makes. The asset is real, it is not the household's, and its condition depends on everyone else's use of it.",
      evidence: [
        { stat: "State law", detail: "Marine fishing inside territorial waters is regulated by state Marine Fishing Regulation Acts rather than by a single national statute, so the rules on gear, zone and season \u2014 and therefore what this household\u2019s natural capital is worth \u2014 change at every state boundary.", source: "State Marine Fishing Regulation Acts, from 1978 onward", year: "1978\u2013" },
        { stat: "61 days", detail: "The annual monsoon fishing ban on the east and west coasts is a conservation measure that is also a guaranteed income gap, which is why it appears in this pentagon under seasonality rather than under shocks.", source: "Department of Fisheries, uniform ban period", year: "2015\u2013" }
      ]
    },
    {
      id: "migrant",
      name: "A seasonal migrant worker",
      short: "A livelihood assembled across two places",
      assets: { human: 58, social: 34, natural: 22, physical: 24, financial: 26 },
      strategy: "Leave after the harvest for construction or brick kiln work, return for the season, and hold both ends of the arrangement together.",
      context: { shock: "Injury at a site with no employer on record, and a lockdown.", trend: "Rising dependence on the destination and falling returns at the origin.", season: "The whole strategy is seasonal: the migration is what the lean months are for." },
      structures: "Portability. Almost every entitlement a household holds — ration, school place, health cover, voter registration — is administered at the place of residence, and this household has two.",
      reading: "The pentagon with the distinctive dent: human capital is the highest corner, social capital the lowest, because the networks that would ordinarily buffer a shock are four hundred kilometres from where the shock happens.",
      complication: "The framework was built for a household in one place. A livelihood constructed across two locations has two vulnerability contexts and two sets of structures, and one pentagon cannot hold both.",
      evidence: [
        { stat: "2020", detail: "The One Nation One Ration Card reform made a ration entitlement portable across states, addressing exactly the structural problem this case describes — a household's claims following its residence rather than its person.", source: "Department of Food & Public Distribution, ONORC rollout", year: "2020" },
        { stat: "1979", detail: "The Inter-State Migrant Workmen Act required registration of contractors and licensing of establishments employing migrant labour. Its coverage in practice is the gap this pentagon records.", source: "Inter-State Migrant Workmen (Regulation of Employment and Conditions of Service) Act", year: "1979" }
      ]
    },
    {
      id: "homebased",
      name: "A home-based worker",
      short: "Piece rates, inside the house",
      assets: { human: 46, social: 38, natural: 6, physical: 22, financial: 20 },
      strategy: "Take piece-rate work from a contractor — garments, beedi, agarbatti, assembly — and fit it around unpaid domestic work that does not reduce.",
      context: { shock: "The contractor not returning. There is no employment relationship to enforce.", trend: "Piece rates that fall in real terms while the work stays the same.", season: "Order flow, which is somebody else's market and arrives without notice." },
      structures: "Whether this counts as employment at all. Most statutory protections attach to establishments of ten or more workers, and this workplace is a room.",
      reading: "The flattest pentagon on the board, and the one most invisible to statistics. Work done inside the home is under-recorded as work, so a household can be fully occupied and appear economically inactive.",
      complication: "This is where the livelihoods framework and the gender-needs framework have to be read together. The pentagon shows a household's assets; it cannot show that the human capital in this case is being spent twice, on paid piece work and on the 305 minutes of unpaid work a day that continue alongside it.",
      evidence: [
        { stat: "305 min", detail: "Average daily unpaid work by women, against 56 minutes for men. Home-based paid work is fitted around this, not instead of it.", source: "MoSPI, Time Use Survey 2024, average time per person per day, All India", year: "2024" },
        { stat: "28.0%", detail: "Urban female labour force participation, 15 years and above, against 47.6% rural. Home-based work sits close to the boundary of what the survey counts as participation.", source: "MoSPI, Periodic Labour Force Survey", year: "2023-24" }
      ]
    }
  ];

  return { capitals: capitals, contexts: contexts, cases: cases };
})();
