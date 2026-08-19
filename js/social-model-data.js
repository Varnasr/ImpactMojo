/* =============================================================================
   ImpactMojo — Fundamentals: The Social Model of Disability
   -----------------------------------------------------------------------------
   The distinction between impairment and disability is the Union of the
   Physically Impaired Against Segregation's, from the "Fundamental Principles
   of Disability" (UPIAS, 1976): impairment is a condition of the body;
   disability is the disadvantage imposed on top of it by a society organised
   for people without that condition. Michael Oliver named it the social model
   in "Social Work with Disabled People" (1983) and developed it in "The
   Politics of Disablement" (1990). Vic Finkelstein and Colin Barnes carried
   the argument in Britain; Anita Ghai has made the Indian case, including
   where the model translates badly.

   The claim is narrow and precise, and it is often overstated. It is NOT that
   impairment is unreal, or that pain and illness are socially produced. It is
   that the gap between an impairment and an excluded life is filled by
   arrangements — buildings, timetables, forms, assumptions — and that those
   arrangements were chosen and can be chosen differently.

   ImpactMojo adds the Indian evidence.

   THE SHAPE OF THE PAGE. Each life outcome is drawn as a stack of barriers
   standing between a person and that outcome. The stack is the argument: the
   medical model looks at the figure at the bottom and proposes to change the
   person; the social model looks at the same figure and asks which layer of
   the stack could be removed.

   Barrier weights are 0-100, assigned by the editorial team from the evidence
   attached to each layer. They are comparative and arguable.

   Every figure is from a named source with a year.
   ============================================================================= */

window.SOCIAL_MODEL = (function () {
  "use strict";

  /* The four kinds of barrier, in the order they are stacked. */
  var kinds = [
    { id: "attitudinal", name: "Attitudinal", color: "#B45309",
      gloss: "What people assume before anything is tried.",
      detail: "The barrier that produces the others, because a building is designed by someone who did not expect you in it. It is also the one no statute can require, which is why it usually outlives the legal reform." },
    { id: "environmental", name: "Environmental", color: "#0369A1",
      gloss: "The built world: steps, kerbs, doorways, vehicles, distances.",
      detail: "The most visible barrier and the most tractable, because it is capital works and can be scheduled. It is also the one where India has the clearest legal obligation and the widest gap between obligation and delivery." },
    { id: "institutional", name: "Institutional", color: "#6D28D9",
      gloss: "Rules, eligibility, papers, timetables, and who is allowed to decide.",
      detail: "The barrier that runs through the certificate. An entitlement conditioned on a document converts a right into an administrative process, and the process becomes the disabling thing." },
    { id: "communication", name: "Communication", color: "#15803D",
      gloss: "Format and language: what is written, spoken, signed, or offered only one way.",
      detail: "The least funded of the four and the one that grows as services move online. A form that exists only as an image of text is inaccessible in exactly the way a staircase is." }
  ];

  /* ------------------------------------------------------- the two readings */
  var models = {
    medical: {
      name: "The medical model",
      gloss: "The person is the problem to be solved.",
      detail: "Reads the same outcome figure and proposes treatment, correction, an aid, or a special institution. It is not a caricature: it is how most disability budgets in India are actually allocated, and for some conditions treatment is exactly what a person wants. The objection is not that medicine is wrong but that it is offered instead of access."
    },
    social: {
      name: "The social model",
      gloss: "The arrangements are the problem to be solved.",
      detail: "Reads the same figure and asks which layer of the stack was chosen, by whom, and what it would take to remove. It does not deny the impairment; it denies that the impairment is a sufficient explanation of the outcome."
    }
  };

  /* ---------------------------------------------------------------- domains */
  var domains = [
    {
      id: "building",
      name: "Entering a public building",
      short: "An office, a bank, a hospital, a court",
      outcome: { stat: "43.6%", label: "of persons with disability accessed a public building in a year",
                 second: "63.9%", secondLabel: "of those who did faced difficulties" },
      barriers: [
        { kind: "environmental", weight: 88, text: "Steps at the entrance, no ramp or a ramp too steep to use unaided, doorways too narrow, no accessible toilet, and lifts that stop before the floor the office is on." },
        { kind: "attitudinal", weight: 52, text: "The assumption that someone will be brought, carried or accompanied, which converts an access failure into a favour asked of a stranger." },
        { kind: "institutional", weight: 44, text: "No obligation enforced against any particular official, so the duty to make a building accessible belongs to everyone and to nobody." },
        { kind: "communication", weight: 36, text: "Signage and counter numbers offered only visually, and announcements only aurally." }
      ],
      reading: "The clearest case on the page, because the barrier is physically visible and nobody disputes what it is. Fewer than half of persons with disability entered a public building at all in a year, and two-thirds of those who did found it hard.",
      complication: "The figure counts access, not need. Someone who did not enter a building may not have needed to, or may have stopped needing to after enough attempts — and the survey cannot separate those two.",
      evidence: [
        { stat: "43.6%", detail: "of persons with disability accessed a public building during the last 365 days. Men 48.2%, women 37.3%.", source: "MoSPI, NSS 76th Round, Persons with Disabilities in India, All India", year: "2018" },
        { stat: "63.9%", detail: "of those who did access a public building faced difficulties doing so.", source: "MoSPI, NSS 76th Round, All India", year: "2018" },
        { stat: "ss.44-46", detail: "The Rights of Persons with Disabilities Act requires that no establishment be granted permission to build without adherence to accessibility standards, and set time limits for making existing public buildings accessible.", source: "Rights of Persons with Disabilities Act 2016", year: "2016" },
        { stat: "2017", detail: "In Rajive Raturi v Union of India the Supreme Court issued directions on the accessibility of public places, treating access as a condition of the right to life rather than a welfare measure.", source: "Rajive Raturi v Union of India, Supreme Court of India", year: "2017" }
      ]
    },
    {
      id: "transport",
      name: "Boarding a bus",
      short: "Getting to the thing, before doing the thing",
      outcome: { stat: "58.1%", label: "of persons with disability used public transport in a year",
                 second: "67.1%", secondLabel: "of those who did faced difficulties" },
      barriers: [
        { kind: "environmental", weight: 84, text: "High floors, no kneeling step, no space to secure a wheelchair, bus stops without a level approach, and a gap between platform and train." },
        { kind: "attitudinal", weight: 60, text: "A conductor who will not wait, and passengers for whom the reserved seat is a courtesy rather than a right." },
        { kind: "communication", weight: 55, text: "Route numbers displayed only in print and stops announced only by sound, so the same journey is unusable to a blind passenger and to a deaf one for opposite reasons." },
        { kind: "institutional", weight: 40, text: "A concession that requires a certificate, so the cheaper fare is available only to someone who has completed a separate administrative process." }
      ],
      reading: "Transport is the barrier that multiplies the others: every outcome further down this page is conditional on being able to get there. Two-thirds of those who used public transport at all found it difficult.",
      complication: "58.1% used public transport, which is not the same as 58.1% being able to. The people for whom it is impossible appear in this statistic as people who did not travel.",
      evidence: [
        { stat: "58.1%", detail: "of persons with disability used public transport during the last 365 days. Men 62.6%, women 52.1%.", source: "MoSPI, NSS 76th Round, All India", year: "2018" },
        { stat: "67.1%", detail: "of those who used public transport faced difficulties. The rate barely differs by sex — 66.7% for men, 67.8% for women — which suggests the barrier is in the vehicle rather than in who is boarding it.", source: "MoSPI, NSS 76th Round, All India", year: "2018" },
        { stat: "2015", detail: "The Accessible India Campaign set targets for accessible government buildings, transport and information. It is the clearest statement of the environmental barrier as a schedulable public works problem rather than a private misfortune.", source: "Department of Empowerment of Persons with Disabilities, Accessible India Campaign", year: "2015" }
      ]
    },
    {
      id: "school",
      name: "Finishing school",
      short: "Secondary education, completed",
      outcome: { stat: "14.9%", label: "of rural persons with disability aged 15+ completed secondary or above",
                 second: "8.2%", secondLabel: "for rural women with disability" },
      barriers: [
        { kind: "environmental", weight: 70, text: "The distance to the school and the state of the route, then the building itself: steps, and a toilet that cannot be used, which ends attendance more often than any lesson does." },
        { kind: "attitudinal", weight: 74, text: "The expectation that the child will not benefit, held often enough by the family and the teacher at once, which decides the question before the school is reached." },
        { kind: "communication", weight: 62, text: "Material offered in one format only. A textbook that exists in print and not in braille, audio or sign is not a difficult text; it is an absent one." },
        { kind: "institutional", weight: 58, text: "Placement in a separate stream, examination rules that do not permit a scribe or extra time without a certificate, and a teacher with no training in the accommodation the law already requires." }
      ],
      reading: "The compounding case. Rural women with disability complete secondary education at 8.2%, against 31.0% for urban persons with disability overall — a fourfold difference produced by stacking the same barriers on top of the ones the Wheel of Power describes.",
      complication: "The framework can say the barriers are stacked; it cannot say in what order they bind. Whether the family's expectation or the school's inaccessibility comes first is exactly the question a programme needs answered, and the survey data does not answer it.",
      evidence: [
        { stat: "14.9%", detail: "of rural persons with disability aged 15 and above have completed secondary education or above; 31.0% in urban areas.", source: "MoSPI, NSS 76th Round, All India", year: "2018" },
        { stat: "8.2%", detail: "for rural women with disability, against 19.8% for rural men. The all-India figures are 12.6% for women and 24.3% for men.", source: "MoSPI, NSS 76th Round, All India", year: "2018" },
        { stat: "52.2%", detail: "literacy among persons with disability aged 7 and above — 61.6% for men and 39.6% for women, and 33.3% for rural women.", source: "MoSPI, NSS 76th Round, All India", year: "2018" },
        { stat: "s.16", detail: "The RPwD Act requires educational institutions funded or recognised by government to provide inclusive education, make buildings and materials accessible, and provide reasonable accommodation to individual requirements.", source: "Rights of Persons with Disabilities Act 2016", year: "2016" }
      ]
    },
    {
      id: "work",
      name: "Getting a job",
      short: "Paid work, on the same terms",
      outcome: { stat: "4%", label: "of vacancies in government establishments reserved for persons with benchmark disabilities",
                 second: "5%", secondLabel: "of seats in government-funded higher education" },
      barriers: [
        { kind: "attitudinal", weight: 80, text: "The employer's estimate of what the applicant can do, formed before any task is described, and rarely tested." },
        { kind: "institutional", weight: 68, text: "Reservation that applies to government establishments, in an economy where the overwhelming majority of work is informal — so the strongest provision reaches the smallest share of jobs." },
        { kind: "environmental", weight: 56, text: "The workplace and the journey to it, which decide whether an offer is one a person can accept." },
        { kind: "communication", weight: 48, text: "Recruitment conducted through inaccessible portals and tests, where the assessment measures access to the format rather than capacity for the work." }
      ],
      reading: "The case where the law is strongest and reaches least far. A 4% reservation is a real and enforceable claim on public employment, and public employment is a small fraction of Indian work.",
      complication: "Reservation attaches to “benchmark disability”, defined as not less than forty per cent of a specified condition. That threshold is doing enormous work: it decides who the law sees, and it is a medical judgment placed at the entrance to a social entitlement.",
      evidence: [
        { stat: "4%", detail: "of the total vacancies in the cadre strength of every government establishment are reserved for persons with benchmark disabilities, with one per cent each for four specified categories.", source: "Rights of Persons with Disabilities Act 2016, s.34", year: "2016" },
        { stat: "5%", detail: "of seats in government and government-aided higher education institutions are reserved for persons with benchmark disabilities.", source: "Rights of Persons with Disabilities Act 2016, s.32", year: "2016" },
        { stat: "2021", detail: "In Vikash Kumar v UPSC the Supreme Court held that reasonable accommodation is not confined to persons with benchmark disabilities, and that denying a scribe to a candidate with a disability below the threshold was unlawful — narrowing the gap the threshold creates.", source: "Vikash Kumar v Union Public Service Commission, Supreme Court of India", year: "2021" },
        { stat: "21", detail: "conditions are specified in the Schedule to the RPwD Act, up from seven under the 1995 Act. The list is the mechanism by which the state decides which impairments exist for legal purposes.", source: "Rights of Persons with Disabilities Act 2016, Schedule", year: "2016" }
      ]
    },
    {
      id: "counted",
      name: "Being counted",
      short: "Appearing in the number the policy is written against",
      outcome: { stat: "2.2%", label: "of the Indian population recorded as having a disability",
                 second: "~16%", secondLabel: "the global prevalence estimate" },
      barriers: [
        { kind: "institutional", weight: 86, text: "A definition built on specified conditions and a forty per cent threshold, so the count measures who qualifies rather than who is disabled by their surroundings." },
        { kind: "attitudinal", weight: 70, text: "Non-disclosure within the household, which is not evasion: reporting a disability can affect a daughter's marriage prospects, and the survey has no way to see what it costs to answer honestly." },
        { kind: "communication", weight: 48, text: "Questions asked in terms of conditions rather than functioning, so a person who cannot climb the steps to the office does not recognise themselves in the question." },
        { kind: "environmental", weight: 20, text: "Enumeration that does not reach the households least able to travel to it." }
      ],
      reading: "The barrier that produces every other figure on this page. India records disability at 2.2% against a global estimate nearer 16%, and the gap is not primarily about who exists — it is about what the question asks.",
      complication: "The two figures are not measuring the same thing, and it would be dishonest to present the gap as pure undercounting. The global estimate uses a functioning-based definition that a condition-based count was never going to reproduce. That is the point rather than a caveat: which definition is used decides the size of the population, and therefore the size of the obligation.",
      evidence: [
        { stat: "2.2%", detail: "of the population is recorded as having a disability — rural 2.3%, urban 2.0%.", source: "MoSPI, NSS 76th Round, All India", year: "2018" },
        { stat: "2.4% vs 1.9%", detail: "prevalence among men against women. A lower recorded rate among women in a population where women live longer is difficult to explain by biology, and easier to explain by who gets reported.", source: "MoSPI, NSS 76th Round, All India", year: "2018" },
        { stat: "40%", detail: "“Benchmark disability” means not less than forty per cent of a specified disability where it has not been defined in measurable terms. Most entitlements attach to this threshold rather than to disability as such.", source: "Rights of Persons with Disabilities Act 2016, s.2(r)", year: "2016" }
      ]
    },
    {
      id: "certificate",
      name: "Holding the certificate",
      short: "The document between a right and its exercise",
      outcome: { stat: "UDID", label: "a single national card replacing state-issued certificates",
                 second: "s.58", secondLabel: "the statutory certification process it implements" },
      barriers: [
        { kind: "institutional", weight: 84, text: "Assessment by a medical board that sits in a district hospital on particular days, with an application, a referral and a review — a process whose cost falls hardest on the people least able to travel to it." },
        { kind: "environmental", weight: 58, text: "The journey to the assessment, which is the same journey the certificate is supposed to make easier." },
        { kind: "communication", weight: 44, text: "An online application system that is itself the format barrier this page describes elsewhere." },
        { kind: "attitudinal", weight: 34, text: "The framing of the certificate as a concession granted rather than a right recognised, which shapes how the counter treats the applicant." }
      ],
      reading: "Included because it is where the social model earns its keep in Indian practice. Nearly every entitlement on this page — reservation, concession, pension, scholarship, scribe — runs through a document, and the process of getting the document is itself disabling.",
      complication: "A universal identity card is a real improvement on a dozen state formats, and the criticism here is not of the UDID. It is that any certification process converts a right into an administrative achievement, and that the people furthest from the office are the people the right was written for.",
      evidence: [
        { stat: "s.58", detail: "sets out the procedure for certification: application to a notified authority, assessment, and issue of a certificate of disability valid across India.", source: "Rights of Persons with Disabilities Act 2016", year: "2016" },
        { stat: "s.57", detail: "requires the appropriate government to designate certifying authorities and notify them, which is the step that decides how far a person must travel.", source: "Rights of Persons with Disabilities Act 2016", year: "2016" },
        { stat: "2021", detail: "Vikash Kumar established that reasonable accommodation is owed independently of certification thresholds — the strongest Indian statement that a right should not wait on a document.", source: "Vikash Kumar v UPSC, Supreme Court of India", year: "2021" }
      ]
    }
  ];

  return { kinds: kinds, models: models, domains: domains };
})();
