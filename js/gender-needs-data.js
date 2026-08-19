/* =============================================================================
   ImpactMojo — Fundamentals: Practical and Strategic Gender Needs
   -----------------------------------------------------------------------------
   The distinction is Caroline Moser's, from "Gender Planning in the Third World:
   Meeting Practical and Strategic Gender Needs" (World Development 17(11), 1989)
   and developed in "Gender Planning and Development" (1993). Moser built it on
   Maxine Molyneux's earlier separation of women's practical and strategic
   interests, drawn from the Nicaraguan revolution ("Mobilisation Without
   Emancipation?", Feminist Studies 11(2), 1985). Molyneux is credited on the
   page; the pairing is often attributed to Moser alone.

   Practical gender needs arise from the roles women already occupy. Meeting them
   makes those roles less punishing and does not question them: a closer water
   source, a gas connection, a toilet.

   Strategic gender interests arise from women's subordinate position. Meeting
   them changes the division of labour, of assets, or of authority: a title deed,
   a seat, a law that is enforced.

   Moser's own argument is that the two are not ranked. A programme that meets
   only strategic interests while a woman walks four kilometres for water has not
   understood the day. A programme that only ever meets practical needs leaves
   the arrangement that produced them intact, and often deepens it, because it
   makes the existing division of labour work slightly better.

   ImpactMojo adds the Indian evidence.

   THE PLOT. Each case sits at two coordinates:

     relief  — how much material burden it takes off a woman's day, as observed
               rather than as intended
     shift   — how far it moves the division of labour, assets or authority

   Both are scored 0-100 by the editorial team from the evidence attached to the
   case, and both are arguable. That is the point of showing the evidence under
   each one rather than only the position. Where a case sits high on one axis and
   low on the other, the reading is the interesting part.

   Every figure is from a named source with a year.
   ============================================================================= */

window.GENDER_NEEDS = (function () {
  "use strict";

  var axes = {
    x: { id: "relief", name: "Relief delivered",
         low: "The day is no lighter", high: "Real burden lifted",
         gloss: "How much material burden the intervention actually takes off a woman's day — measured by use and sustained use, not by what was distributed." },
    y: { id: "shift", name: "Position shifted",
         low: "The arrangement is untouched", high: "Division of labour or assets moved",
         gloss: "How far it moves the gendered division of labour, of assets, or of authority. A right that exists on paper and is not exercised scores low here." }
  };

  var quadrants = [
    { id: "practical", name: "Practical only", color: "#0369A1",
      where: "high relief, little shift",
      gloss: "The load is lighter and the arrangement that produced it is intact.",
      detail: "Moser's warning lives in this quadrant. These are not failures — a woman who no longer walks for fuel has got something real. But the work stays hers, and a programme that stops here has made the existing division of labour run more smoothly." },
    { id: "strategic", name: "Strategic only", color: "#6D28D9",
      where: "real shift, little relief",
      gloss: "The position moves on paper, and the day does not.",
      detail: "Rights, seats and titles that exist and are not exercised. The gap is usually not in the law but in what it costs a woman to use it — time she does not have, a registry she cannot reach, a household that will punish the attempt." },
    { id: "both", name: "Both", color: "#15803D",
      where: "high on both",
      gloss: "The burden falls and the arrangement changes with it.",
      detail: "Rare, and worth studying when it happens. What these cases share is that the strategic provision was written into the delivery mechanism rather than bolted on — a wage paid to her account, a quota inside a scheme she already had reason to attend." },
    { id: "neither", name: "Neither yet", color: "#B45309",
      where: "low on both",
      gloss: "Enacted, and not yet reaching most women.",
      detail: "Usually a coverage problem rather than a design one. The provision is sound and applies to a fraction of the women it names, because of who counts as an employee, who has papers, or who lives within reach of the office that administers it." }
  ];

  /* ------------------------------------------------------------------- cases */
  var cases = [
    {
      id: "ujjwala",
      name: "A subsidised LPG connection",
      short: "PMUY — cooking gas in the woman's name",
      relief: 72, shift: 24, quadrant: "practical",
      what: "Pradhan Mantri Ujjwala Yojana, launched 2016. A deposit-free LPG connection issued in the name of an adult woman of a poor household.",
      reading: "The clearest practical-need intervention India has run at scale, and it is deliberately issued in a woman's name, which looks strategic. It is not: the connection recognises that cooking is her job. Nothing about the scheme proposes that it should not be.",
      complication: "Naming the woman as the consumer is not nothing. It puts a formal entitlement, an account and a subsidy transfer in her name, and for many that is the first such document. Whether that converts into anything further is not established either way.",
      evidence: [
        { stat: "305 min", detail: "The average Indian woman spends 305 minutes a day on unpaid activity, against 56 minutes for men. Cooking and fuel collection sit inside that figure, and it is the burden Ujjwala addresses.", source: "MoSPI, Time Use Survey 2024, average time per person per day, All India", year: "2024" },
        { stat: "62 min", detail: "Women spend 62 minutes a day on paid activity, against 251 for men. The two figures together are the division of labour the scheme leaves untouched.", source: "MoSPI, Time Use Survey 2024, average time per person per day, All India", year: "2024" },
        { stat: "Refills", detail: "The scheme's own reported weakness is refill rate rather than connection count: a household with a cylinder it cannot afford to refill returns to biomass for part of the year. Connection counts are published; sustained-use rates are the number that would settle the question.", source: "Ministry of Petroleum & Natural Gas, PMUY scheme reporting", year: "2016–" }
      ]
    },
    {
      id: "toilets",
      name: "A household toilet",
      short: "Swachh Bharat — a latrine within the premises",
      relief: 66, shift: 18, quadrant: "practical",
      what: "Swachh Bharat Mission (Gramin), from 2014. Construction subsidy for an individual household latrine.",
      reading: "Safety and dignity are real gains and they fall disproportionately to women, who bear the cost of open defecation asymmetrically — in risk, in illness, and in the hours it is confined to. The intervention asks nothing of how a household divides its work.",
      complication: "A latrine that exists and is not used delivers none of this, and use is the harder number. The relief score here reflects access rather than verified use, and should be read as an upper bound.",
      evidence: [
        { stat: "Access vs use", detail: "The distance between a toilet built and a toilet used is the same distance the Capability Approach page draws between a resource and a capability. Construction is counted nationally; use is surveyed, and less often.", source: "Department of Drinking Water & Sanitation; NSS 76th Round, latrine use", year: "2018–2019" }
      ]
    },
    {
      id: "water",
      name: "A household water connection",
      short: "Jal Jeevan Mission — water inside the premises",
      relief: 78, shift: 20, quadrant: "practical",
      what: "Jal Jeevan Mission, from 2019. A functional household tap connection.",
      reading: "Fetching water is among the most time-expensive unpaid tasks, and it is close to universally a woman's or a girl's. Bringing the source inside the premises returns hours to her directly, which is why the relief score is the highest on the board.",
      complication: "It also returns those hours to a day that has no claim on them. Time freed from fetching water is not automatically time she controls; the evidence on what replaces it is thin, and this page does not assert it.",
      evidence: [
        { stat: "94.5%", detail: "of rural households have access to an improved drinking water source.", source: "MoSPI, NSS 78th Round, Multiple Indicator Survey", year: "2020-21" },
        { stat: "42.0%", detail: "have a source that is theirs alone, within the premises, and sufficient through the year. The gap between the two figures is the part of the walk that is left.", source: "MoSPI, NSS 78th Round, Multiple Indicator Survey", year: "2020-21" }
      ]
    },
    {
      id: "maternity",
      name: "Paid maternity leave",
      short: "26 weeks, for those the Act reaches",
      relief: 30, shift: 40, quadrant: "neither",
      what: "Maternity Benefit (Amendment) Act 2017, raising paid leave from 12 to 26 weeks and requiring a creche in establishments with 50 or more employees.",
      reading: "Among the most generous statutory entitlements in the world, and it applies to establishments with ten or more employees. Set against an overwhelmingly informal female workforce, the share of women it can reach is small, which is why it sits low on both axes despite being a strong law.",
      complication: "The provision is not the problem; the definition of who is covered is. A law of this quality reaching a larger share of women workers would move sharply up and to the right, and that is a coverage decision rather than a drafting one.",
      evidence: [
        { stat: "10+", detail: "The Act applies to establishments employing ten or more persons. Women working in smaller units, in own-account work, or as casual labour are outside it.", source: "Maternity Benefit Act 1961, s.2, as amended 2017", year: "2017" },
        { stat: "41.7%", detail: "Female labour force participation, 15 years and above, all-India — 47.6% rural and 28.0% urban. Male participation is 78.8%.", source: "MoSPI, Periodic Labour Force Survey", year: "2023-24" }
      ]
    },
    {
      id: "mgnrega",
      name: "A guaranteed wage, at her own rate",
      short: "MGNREGA — equal wage, one-third of days, paid to her account",
      relief: 68, shift: 66, quadrant: "both",
      what: "Mahatma Gandhi National Rural Employment Guarantee Act 2005. Up to 100 days of wage employment per rural household, at a statutory wage that does not differ by sex, with at least one-third of beneficiaries to be women.",
      reading: "The case worth studying. The strategic provisions are not additions to the scheme; they are how the scheme works. The wage is the same for a woman and a man because the Act sets one rate, the work is near the village so attending it does not require permission for travel, and payment goes to an individual account rather than to a household head.",
      complication: "Whether the income remains hers after it arrives is a different question, and the transfer record cannot answer it. Nor does the Act touch the unpaid work that continues alongside the hundred days.",
      evidence: [
        { stat: "One-third", detail: "The Act requires that at least one-third of beneficiaries be women who have registered and requested work. Reported women's share of person-days has run above that floor for most of the scheme's life.", source: "MGNREGA 2005, Schedule II, para 6; Ministry of Rural Development reporting", year: "2005–" },
        { stat: "Equal rate", detail: "The statutory wage is notified per state and does not vary by sex, which makes it one of the few large labour markets in India where a woman's rate is not set below a man's by custom.", source: "MGNREGA 2005, s.6", year: "2005" }
      ]
    },
    {
      id: "panchayat",
      name: "A reserved seat in the panchayat",
      short: "73rd Amendment — one-third of seats, and more in most states",
      relief: 22, shift: 74, quadrant: "strategic",
      what: "Constitution (Seventy-third Amendment) Act 1992, Article 243D. Not less than one-third of seats and of chairperson posts in panchayats reserved for women. Most states have since legislated fifty per cent.",
      reading: "The largest formal transfer of political position to women anywhere, by count of seats. It changes who is in the room and it does not, on its own, change the day of the woman who is in it.",
      complication: "The gap between holding the seat and exercising it is the whole argument. The pattern in which an elected woman's husband conducts the office in practice is documented enough to have a name in several languages, and it is a strategic gain partially reversed at the point of use.",
      evidence: [
        { stat: "One-third", detail: "Article 243D reserves not less than one-third of all seats, and of chairperson posts, for women. Most states now legislate half.", source: "Constitution of India, Article 243D, inserted 1992", year: "1992" },
        { stat: "Above 50%", detail: "In several large states women are more than half of elected panchayat representatives — Andhra Pradesh 55.47%, Assam 54.73%, Bihar 52.02% — above the constitutional floor.", source: "MoSPI Gender Statistics, representation of women in Panchayati Raj Institutions, as on 06.01.2025", year: "2025" },
        { stat: "88.7%", detail: "of women report participating in household decisions, which is the domestic counterpart of the same finding: presence in the decision is more common than control of what is decided over.", source: "NFHS-5, women's participation in household decision-making, All India", year: "2019-21" }
      ]
    },
    {
      id: "succession",
      name: "An equal share in ancestral property",
      short: "Hindu Succession (Amendment) Act 2005 — daughters as coparceners",
      relief: 16, shift: 82, quadrant: "strategic",
      what: "Hindu Succession (Amendment) Act 2005, amending s.6 to make a daughter a coparcener by birth on the same terms as a son. Vineeta Sharma v Rakesh Sharma (2020) settled that the right does not depend on the father being alive on the date of the amendment.",
      reading: "The single largest change to women's property position in independent India, and the one whose gap between right and exercise is widest. Land is the asset that carries credit, standing and the ability to leave.",
      complication: "The right is claimed against one's own family, usually at the moment of a death, and often at the cost of the relationship that a married daughter relies on. That is not a defect in the drafting; it is why a strategic gain can sit unexercised for twenty years.",
      evidence: [
        { stat: "31.7%", detail: "of women own land alone or jointly, against 42.3% of men. The gap has narrowed since the amendment and has not closed.", source: "NFHS-5, ownership of assets, All India", year: "2019-21" },
        { stat: "42.3%", detail: "of women own a house alone or jointly, against 60.1% of men. 'Jointly' is doing considerable work in both figures.", source: "NFHS-5, ownership of assets, All India", year: "2019-21" },
        { stat: "2020", detail: "Vineeta Sharma v Rakesh Sharma held the daughter's coparcenary right to be by birth, unobstructed, and not conditional on the father surviving to 9 September 2005 — resolving a conflict that had run through the High Courts for fifteen years.", source: "Vineeta Sharma v Rakesh Sharma, Supreme Court of India", year: "2020" }
      ]
    },
    {
      id: "dv-act",
      name: "A civil remedy against violence at home",
      short: "PWDVA 2005 — residence orders and protection orders",
      relief: 34, shift: 62, quadrant: "strategic",
      what: "Protection of Women from Domestic Violence Act 2005. A civil statute providing protection orders, residence orders, monetary relief and custody orders, with Protection Officers to assist access.",
      reading: "It named as violence a set of acts the law had not reached, and it gave a woman a right to remain in the shared household rather than choosing between the violence and the street. The residence order is the strategic core: it separates the right to a home from ownership of it.",
      complication: "Access runs through Protection Officers, and their number, training and caseload vary widely by state. A remedy is worth what it costs to reach.",
      evidence: [
        { stat: "33.3%", detail: "of ever-married women aged 15-49 reported emotional, physical or sexual violence by a husband; 30.9% reported physical or sexual violence.", source: "NFHS-4, All India", year: "2015-16" },
        { stat: "Residence", detail: "s.17 gives every woman in a domestic relationship the right to reside in the shared household, whether or not she has any right, title or beneficial interest in it.", source: "Protection of Women from Domestic Violence Act 2005, s.17", year: "2005" }
      ]
    },
    {
      id: "posh",
      name: "A complaints route at work",
      short: "POSH Act 2013 — Internal Committees",
      relief: 28, shift: 48, quadrant: "neither",
      what: "Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act 2013, following the Vishaka guidelines of 1997. Requires an Internal Committee in every workplace with ten or more employees, and a Local Committee for the rest.",
      reading: "It converted a set of judicial guidelines into a statutory duty on the employer. The Local Committee provision was written precisely to cover women outside formal establishments, which is most women who work.",
      complication: "The Local Committees are the part that has not been built out. A statute whose informal-sector arm is thin covers, in practice, the same women the Maternity Benefit Act covers.",
      evidence: [
        { stat: "10+", detail: "Internal Committees are mandatory at ten or more employees. Below that, and for domestic workers and the self-employed, the route is the District Officer's Local Committee.", source: "Sexual Harassment of Women at Workplace Act 2013, ss.4 and 6", year: "2013" },
        { stat: "1997", detail: "Vishaka v State of Rajasthan laid down binding guidelines in the absence of legislation. It took sixteen years for the statute to follow.", source: "Vishaka v State of Rajasthan, Supreme Court of India", year: "1997" }
      ]
    },
    {
      id: "shg",
      name: "A place in a self-help group",
      short: "SHG membership and the loan that follows it",
      relief: 54, shift: 52, quadrant: "both",
      what: "Self-help group federations under NRLM and their predecessors: a savings group of women, linked to a bank, which becomes a borrowing entity and often a delivery channel for other schemes.",
      reading: "Sits near the middle of the board on purpose. The credit is real and modest; the weekly meeting is a standing reason to leave the house that a household finds hard to refuse, and the collective is a body that can be addressed by an administration.",
      complication: "Whether the loan is used by the borrower or by a man in her household is the contested question in the literature, and it is not settled by disbursement figures. The relief score reflects credit access; it does not assert control of the credit."
    },
    {
      id: "creche",
      name: "Childcare during working hours",
      short: "The creche obligation, and what sits behind it",
      relief: 74, shift: 70, quadrant: "both",
      what: "The 2017 creche requirement for establishments with fifty or more employees, and the anganwadi system under ICDS as the near-universal alternative.",
      reading: "The intervention that does most on both axes at once, because childcare is the specific unpaid task that blocks paid work. Removing it lightens the day and opens the labour market in the same act, which is why it scores high on relief and on shift together.",
      complication: "Anganwadis run to a pre-school schedule rather than a working day, so the hours cover a part of the problem. And the fifty-employee threshold puts the statutory version out of reach of most women who work.",
      evidence: [
        { stat: "305 vs 56", detail: "The unpaid-work gap that childcare sits inside: 305 minutes a day for women against 56 for men.", source: "MoSPI, Time Use Survey 2024, All India", year: "2024" },
        { stat: "28.0%", detail: "Urban female labour force participation, against 47.6% rural. Urban work is less compatible with carrying a child to it, and the gap is one of the places that shows.", source: "MoSPI, Periodic Labour Force Survey, 15 years and above", year: "2023-24" }
      ]
    },
    {
      id: "cash",
      name: "A cash transfer to a woman's account",
      short: "Direct transfer, named beneficiary",
      relief: 58, shift: 36, quadrant: "practical",
      what: "The general form of the state-level income transfers to women that have spread across India since 2023, paid monthly into an individual account.",
      reading: "Income relieves the condition and the account is in her name, which is a real change in who the state addresses. It is placed on the practical side because nothing in the design proposes a different division of labour — in several formulations the transfer is explicitly compensation for continuing to do the unpaid work.",
      complication: "This is the case where this page is least confident, and it is deliberately recent enough that the evidence is not in. A transfer that a woman controls and that is large enough to change a bargaining position would belong further up. Whether these are that is an open empirical question, and the entry will move if the evidence says so."
    }
  ];

  return { axes: axes, quadrants: quadrants, cases: cases };
})();
