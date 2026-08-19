/* =============================================================================
   ImpactMojo — Fundamentals: the Capability Approach
   -----------------------------------------------------------------------------
   The approach is Amartya Sen's, developed across "Equality of What?" (1979),
   "Commodities and Capabilities" (1985) and "Development as Freedom" (1999).
   The list of ten central capabilities is Martha Nussbaum's, from "Women and
   Human Development" (2000) and restated in "Creating Capabilities" (2011).
   Sen has consistently declined to endorse a fixed list; that disagreement is
   recorded on the page rather than smoothed over.

   ImpactMojo adds the Indian evidence.

   The shape of the page is the conversion chain, because that is where the
   argument actually lives: a resource is not a freedom, and the distance
   between them is filled by conversion factors that differ by person, by
   society and by place. Every figure below is from a named source with a year.
   ============================================================================= */

window.CAPABILITIES = (function () {
  "use strict";

  /* The four stages of the chain. Colours match the Fundamentals palette. */
  var stages = [
    { id: "resource",   name: "Resource",    color: "#0369A1",
      gloss: "What is provided, and what gets counted in the budget line.",
      detail: "A school place, a toilet, a cycle, a ration entitlement, a bank account. Resources are countable, which is why targets are written in them." },
    { id: "conversion", name: "Conversion",  color: "#B45309",
      gloss: "What stands between the resource and what a person can do with it.",
      detail: "Sen groups these three ways: personal (body, skill, health), social (norms, caste, public services, law as enforced) and environmental (terrain, distance, infrastructure, climate). Two people handed the same resource do not get the same freedom out of it." },
    { id: "capability", name: "Capability",  color: "#15803D",
      gloss: "What a person is actually able to do or be, whether or not they do it.",
      detail: "The real opportunity set. This is what Sen argues development should be measured in, and it is the stage almost no administrative dataset records." },
    { id: "functioning", name: "Functioning", color: "#6D28D9",
      gloss: "What the person ends up doing or being.",
      detail: "The outcome that surveys observe. A functioning that was chosen and one that was the only option left look identical in the data, which is the reason capability is a separate stage rather than a synonym." }
  ];

  /* -------------------------------------------------------------- the chains */
  var chains = [
    {
      id: "schooling",
      name: "A school place",
      short: "School place → being able to read",
      resource: "A free, compulsory school place for every child aged 6 to 14, guaranteed by the Right to Education Act 2009.",
      capability: "Being able to read, reason and go on learning.",
      functioning: "A child who reads.",
      headline: { stat: "98.1%", label: "enrolled", contrast: "44.8%", contrastLabel: "of Std V children in government schools can read a Std II text" },
      factors: [
        { kind: "personal", text: "Whether the child arrives fed and well enough to attend. Attendance and nutrition move together, which is part of why the midday meal is a schooling intervention as much as a nutrition one." },
        { kind: "social",   text: "Whether a teacher is present and teaching at the child's actual level rather than the syllabus level, and whether a first-generation learner has anyone at home to read with." },
        { kind: "environmental", text: "Distance, and what the walk is like in the monsoon or after dark, which bears differently on girls." }
      ],
      evidence: [
        { stat: "98.1%", detail: "of rural children aged 6 to 14 were enrolled in school in 2024. Enrolment in this age group has been above 95% for close to twenty years, and is above 95% in every single state.", source: "ASER 2024, rural India, 605 districts", year: "2024" },
        { stat: "44.8%", detail: "of Std V children in government schools could read a Std II level text in 2024 — up from 38.5% in 2022, but only just past the 44.2% recorded in 2018. The private-school figure is 59.4%, down from 65.1% in 2018.", source: "ASER 2024", year: "2024" },
        { stat: "23.4%", detail: "of Std III children in government schools could read a Std II level text in 2024. This is the highest the figure has been since ASER began in 2005, which is the honest way to hold both facts at once: the recovery is real and the level is low.", source: "ASER 2024", year: "2024" }
      ],
      reading: "The resource is close to universal and the capability is not. A target written in enrolment was met; a target written in reading would not have been. This single pair is the shortest statement of why Sen argued that counting what people are given tells you less than you think.",
      complication: "The gap is not evidence that schooling fails to convert. Reading levels in government schools rose between 2022 and 2024 across every elementary grade, and the recovery was larger there than in private schools. What the pair shows is that the conversion rate is a policy variable in its own right — not that the resource is worthless."
    },

    {
      id: "sanitation",
      name: "A household toilet",
      short: "Toilet built → not defecating in the open",
      resource: "A subsidised household latrine, built under the Swachh Bharat Mission.",
      capability: "Being able to relieve yourself safely, privately and with dignity.",
      functioning: "A toilet in daily use by everyone in the household.",
      headline: { stat: "100%", label: "of districts declared ODF by 2 Oct 2019", contrast: "19%", contrastLabel: "of households still had no toilet facility in NFHS-5" },
      factors: [
        { kind: "personal", text: "Whether an older household member, or one with a disability, can use the structure that was built." },
        { kind: "social",   text: "Purity and pollution beliefs that make a latrine near the house objectionable, and the caste order that has historically made pit-emptying somebody else's job. A toilet whose pit nobody in the household will empty is a toilet with a life measured in months." },
        { kind: "environmental", text: "Water at the household, and a pit that does not fill or flood. Without water the structure converts into storage." }
      ],
      evidence: [
        { stat: "Oct 2019", detail: "every district in India was declared open-defecation free, five years after the Swachh Bharat Mission began. The declaration was made against toilets constructed.", source: "Swachh Bharat Mission (Gramin), Government of India", year: "2019" },
        { stat: "19%", detail: "of households reported no toilet facility at all in the National Family Health Survey run between 2019 and 2021 — after the ODF declaration. The survey asks households what they have and use, rather than counting what was built.", source: "NFHS-5, India Report", year: "2021" },
        { stat: "Article 21", detail: "the Supreme Court has read sanitation into the right to life, and the National Green Tribunal has repeatedly held municipalities to it. The entitlement is not in doubt; what is in doubt is whether a built structure discharges it.", source: "Constitution of India, as interpreted", year: "1950" }
      ],
      reading: "Two numbers describe the same country in the same years and disagree, because they measure different stages of the chain. One counts the resource. The other asks about the functioning. Neither is wrong, and a programme evaluated on the first can be judged a complete success while the second says otherwise.",
      complication: "The ODF figure is not simply false. Construction at that scale genuinely happened and open defecation genuinely fell a long way. The problem is the choice of measure: declaring a district ODF on the basis of toilets built makes a claim about behaviour using a count of objects, and no amount of construction can settle a question about use."
    },

    {
      id: "cycle",
      name: "A bicycle",
      short: "Cycle given → being able to get to school",
      resource: "A bicycle, given to girls entering Class 9 — Bihar's Mukhyamantri Balika Cycle Yojana, from 2006.",
      capability: "Being able to reach a secondary school that is too far to walk to.",
      functioning: "A girl who stays enrolled through secondary school.",
      headline: { stat: "Sen's own example", label: "", contrast: "", contrastLabel: "a bicycle gives mobility to one person and not to another, from the same object" },
      factors: [
        { kind: "personal", text: "Whether she can ride, and whether a physical impairment makes the object useless to her. This is Sen's original illustration: the bicycle is the same, the freedom it yields is not." },
        { kind: "social",   text: "Whether a girl cycling through the village is acceptable, and whether the household will let her. The object clears the distance; it does not clear the permission." },
        { kind: "environmental", text: "Road surface, distance, and whether the route is one her family judges safe." }
      ],
      evidence: [
        { stat: "2006", detail: "Bihar began giving bicycles to girls entering Class 9. It became one of the most studied schemes in Indian education policy precisely because the resource was so simple and so easy to count.", source: "Government of Bihar, Mukhyamantri Balika Cycle Yojana", year: "2006" },
        { stat: "Distance", detail: "the published evaluation found the effect concentrated among girls living further from a secondary school, which is what a conversion-factor account predicts: the object removes a specific barrier for the people that barrier was binding on, and does little for anyone else.", source: "Muralidharan & Prakash, American Economic Journal: Applied Economics", year: "2017" },
        { stat: "21", detail: "disabilities are recognised under the Rights of Persons with Disabilities Act 2016, up from seven under the 1995 Act. Recognition is the precondition for a personal conversion factor to be visible to a scheme at all.", source: "Rights of Persons with Disabilities Act", year: "2016" }
      ],
      reading: "The cycle scheme is the cleanest natural experiment on this page, and it worked. It is here because it shows the same mechanism running the other way: a resource that removes a real environmental barrier produces a real capability gain, and the gain is largest exactly where the barrier was largest.",
      complication: "A scheme can be well targeted on one conversion factor and blind to another. Distance was addressed; whether a household permits a daughter to cycle was not, and no cycle addresses it. That is not an argument against the cycles — it is the reason a single resource is rarely a sufficient policy."
    },

    {
      id: "income",
      name: "Household income",
      short: "Income → living a long life",
      resource: "Money, the resource that stands in for all the others.",
      capability: "Being able to live a long and healthy life.",
      functioning: "Years actually lived.",
      headline: { stat: "Kerala", label: "leads on life expectancy", contrast: "not", contrastLabel: "on income per head" },
      factors: [
        { kind: "personal", text: "Age, illness and disability all change how much a rupee buys in wellbeing. A household with a chronically ill member converts income into health at a worse rate, and needs more of it to reach the same place." },
        { kind: "social",   text: "What public provision already exists. Where health and schooling are publicly supplied and functioning, private income has less work to do; where they are not, income is the only route and inequality in income becomes inequality in survival." },
        { kind: "environmental", text: "Air, water and heat. Income buys less health where the ambient environment is taking it away faster." }
      ],
      evidence: [
        { stat: "Kerala", detail: "has India's highest life expectancy without having India's highest income per head. Sen's long-standing reading is that public provision in health and schooling converts modest income into long life at a rate that richer states with weaker provision do not achieve.", source: "Drèze & Sen, An Uncertain Glory", year: "2013" },
        { stat: "Self-reported", detail: "Kerala also reports among the highest rates of self-perceived morbidity in India. Sen's explanation is that reported illness measures the ability to recognise and name illness, which schooling and contact with doctors raise — so the healthiest state can look the sickest in a survey that asks people how they feel.", source: "Sen, 'Health: perception versus observation', BMJ", year: "2002" },
        { stat: "HDI", detail: "the Human Development Index was built by Mahbub ul Haq with Sen's involvement precisely to stop income standing alone as the measure of development. Sen's own view of it is notably cool: he called it a crude measure, and defended it as a device for shifting attention rather than as a summary of what matters.", source: "UNDP Human Development Report", year: "1990" }
      ],
      reading: "Income is the resource with the best claim to being general, and it is still only a resource. The Kerala pair is the standard demonstration: the same rupee buys different amounts of life depending on what public provision is already in place around it.",
      complication: "The morbidity finding cuts both ways and is worth handling carefully. It explains why self-reported health data can invert the truth — but it can also be used to wave away any survey result that is politically inconvenient. The check is whether an observational measure, like mortality, agrees with the self-report or contradicts it."
    },

    {
      id: "water",
      name: "A household water connection",
      short: "Water connection → being able to drink safely",
      resource: "An improved drinking water source — a piped supply, a tubewell, a protected well — counted by the source rather than by the household's use of it.",
      capability: "Being able to drink, cook and wash without spending the day fetching water.",
      functioning: "A household that has enough safe water, every day of the year.",
      headline: { stat: "94.5%", label: "of rural households have access to an improved source", contrast: "42.0%", contrastLabel: "have one that is theirs alone, in the premises, and sufficient all year" },
      factors: [
        { kind: "personal", text: "Who in the household does the fetching. Where the source is outside the premises the walk is overwhelmingly women's and girls' time, and it is time taken from school and paid work rather than from leisure." },
        { kind: "social",   text: "Whether the source is shared, and with whom. A well a Dalit household is not free to draw from is an improved source on paper and an inaccessible one in practice." },
        { kind: "environmental", text: "Distance, and seasonality. A source that runs dry for three months a year still counts as an improved source for the whole year." }
      ],
      evidence: [
        { stat: "94.5%", detail: "of rural households had access to an improved source of drinking water. In urban India the figure is 97.4%. This is the number that gets reported as near-universal coverage.", source: "NSS 76th Round, Drinking Water, Sanitation, Hygiene and Housing Condition (MoSPI)", year: "2018" },
        { stat: "56.1%", detail: "of rural households had that improved source located within the household premises — so for roughly two in five, water is somewhere else and someone has to go and get it. Urban: 78.6%.", source: "NSS 76th Round (MoSPI)", year: "2018" },
        { stat: "42.0%", detail: "of rural households had exclusive access to an improved source, in the premises, sufficiently available throughout the year — all three conditions at once. Urban: 50.5%. The gap between this and 94.5% is entirely made of conversion factors.", source: "NSS 76th Round (MoSPI)", year: "2018" }
      ],
      reading: "Three figures from one survey, describing the same households, ranging from 94.5% to 42.0%. None of them is wrong and none is a correction of the others: each adds a condition that has to hold before the source becomes water you can actually rely on. A target written on the first is met at a point where the third is still a minority.",
      complication: "The narrowest measure is not automatically the right one. A shared standpost fifty metres away is a real improvement on an unprotected well, and refusing to count it would erase genuine progress. The argument is not that 42.0% is the true number — it is that which of the three you report is a choice, and it is rarely made explicit."
    },

    {
      id: "internet",
      name: "An internet connection",
      short: "Connection → being able to reach the state online",
      resource: "An internet facility within the household premises — the measure behind India's digital-inclusion numbers.",
      capability: "Being able to file a claim, sit an online class, or hold a video consultation.",
      functioning: "A household that actually transacts online.",
      headline: { stat: "83.3%", label: "of rural households have internet within the premises", contrast: "9.1%", contrastLabel: "of those have a fixed or WiFi connection rather than only a mobile one" },
      factors: [
        { kind: "personal", text: "Whose phone it is. A household counted as connected is often connected through one handset, and who may use it and for how long is a question the survey does not reach." },
        { kind: "social",   text: "Digital literacy, and whether the person who needs the service is the person who can operate it. Filing a grievance is not the same task as receiving a message." },
        { kind: "environmental", text: "Whether the signal holds for the length of a class or a consultation. A mobile connection that drops is adequate for a notification and inadequate for an hour of anything." }
      ],
      evidence: [
        { stat: "83.3%", detail: "of rural households reported an internet facility within the household premises. Urban: 91.6%. This is the figure behind claims of near-universal digital access.", source: "NSS 80th Round, Comprehensive Modular Survey: Telecom (MoSPI)", year: "2025" },
        { stat: "9.1%", detail: "of connected rural households had a fixed or WiFi connection. Urban: 24%. Almost the entire rural internet is mobile — 98.8% of connected rural households use a mobile network.", source: "NSS 80th Round, CMST (MoSPI)", year: "2025" },
        { stat: "Article 21", detail: "the Supreme Court has held that the freedoms of speech and of trade over the internet are constitutionally protected, and that an indefinite shutdown is impermissible. The right is settled; the connection it presumes is mostly a shared handset.", source: "Anuradha Bhasin v. Union of India", year: "2020" }
      ],
      reading: "Being counted as connected and being able to do the thing connection is for are separated here by an order of magnitude. Government services move online against the 83.3%; the 9.1% is closer to the population that can sit through an online hearing or upload a set of documents without the call dropping.",
      complication: "A mobile connection is not a poor substitute for broadband so much as a different thing, and for many purposes — a payment, a message, a status check — it is entirely sufficient. The distinction matters for the tasks that take sustained bandwidth, which happen to include most of what the state has moved online."
    },

    {
      id: "ration",
      name: "A ration entitlement",
      short: "Entitlement → being adequately nourished",
      resource: "Subsidised grain, a legal entitlement for roughly two-thirds of the population under the National Food Security Act 2013.",
      capability: "Being able to be adequately nourished.",
      functioning: "A household that eats enough, of enough different things.",
      headline: { stat: "Legal right", label: "since 2013", contrast: "2011", contrastLabel: "the census the entitlement lists are still drawn from" },
      factors: [
        { kind: "personal", text: "Grain is calories. Whether calories become nutrition depends on absorption, on illness, and on what else is on the plate — which is why a cereal-centred entitlement and a nutrition outcome can move apart." },
        { kind: "social",   text: "Whether your name is on the list, whether the dealer is open, and whether a woman in the household controls what is cooked and for whom. Intra-household distribution is invisible to a scheme that delivers to a household." },
        { kind: "environmental", text: "Distance to the fair price shop, and whether the biometric authentication works where the network does not." },
      ],
      evidence: [
        { stat: "2013", detail: "the National Food Security Act made subsidised grain a legal entitlement rather than a discretionary benefit, covering up to 75% of the rural and 50% of the urban population.", source: "National Food Security Act", year: "2013" },
        { stat: "2011", detail: "coverage is still apportioned using the last completed Census. The 2021 Census was postponed, so the population the Act is applied to is more than a decade out of date, and the shortfall falls on households formed since.", source: "Census of India; NFSA coverage rules", year: "2011" },
        { stat: "Article 21", detail: "the right to food was read into the right to life in the PUCL litigation from 2001, and the Supreme Court's interim orders converted several schemes into entitlements years before Parliament legislated.", source: "PUCL v. Union of India", year: "2001" }
      ],
      reading: "This chain shows a conversion factor that is purely administrative. The entitlement is real, the grain exists, and the binding constraint for a household formed after 2011 is a list. No amount of the resource fixes it, because the failure is not in the resource.",
      complication: "Whether a cereal entitlement should be expected to produce nutrition is genuinely contested. One reading is that the scheme is doing its job and nutrition needs different instruments; another is that a food security law measured in grain has picked the wrong unit. The page does not settle it."
    }
  ];

  /* ------------------------------------------- Nussbaum's ten, for reference */
  var nussbaum = [
    { n: "Life", t: "Being able to live to the end of a human life of normal length." },
    { n: "Bodily health", t: "Good health, adequate nourishment, adequate shelter." },
    { n: "Bodily integrity", t: "Moving freely, secure against assault, choices in reproduction." },
    { n: "Senses, imagination, thought", t: "Being able to use these, informed by an adequate education." },
    { n: "Emotions", t: "Attachments to things and people outside ourselves." },
    { n: "Practical reason", t: "Forming a conception of the good and planning one's life." },
    { n: "Affiliation", t: "Living with others, and being treated as a dignified being whose worth equals others'." },
    { n: "Other species", t: "Living with concern for animals, plants and the world of nature." },
    { n: "Play", t: "Being able to laugh, to play, to enjoy recreational activities." },
    { n: "Control over one's environment", t: "Political participation, and holding property and work on an equal basis." }
  ];

  var FACTOR_LABEL = {
    personal: "Personal",
    social: "Social",
    environmental: "Environmental"
  };

  return {
    stages: stages,
    chains: chains,
    nussbaum: nussbaum,
    FACTOR_LABEL: FACTOR_LABEL
  };
})();
