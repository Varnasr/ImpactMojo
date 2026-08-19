/* =============================================================================
   ImpactMojo — Fundamentals: Who Counts
   -----------------------------------------------------------------------------
   The Data Room (/explorers.html) covers what India measures. This covers the
   other side: what it does not, why, and what follows from the gap. Unlike the
   rest of the series this framework is ImpactMojo's own, so there is no outside
   author to credit — only the sources for each gap.

   Same rule as the rest of the series: every entry names a source and a year.
   ============================================================================= */

window.WHOCOUNTS = (function () {
  "use strict";

  var KINDS = {
    never:   { label: "Never asked",     note: "No national instrument collects it at all." },
    under:   { label: "Counted, badly",  note: "An official figure exists and is far below what independent estimates find." },
    frozen:  { label: "Frozen",          note: "It was counted once and has not been counted since." }
  };

  var gaps = [
    {
      id: "orientation", name: "Sexual orientation", kind: "never", color: "#7c3aed",
      missing: "No national survey asks who anyone is attracted to, or whether they are in a same-sex relationship.",
      evidence: [
        { stat: "Zero", detail: "The Census, NFHS and PLFS carry no question on sexual orientation. The absence is complete rather than partial.", source: "Review of Census, NFHS-5 and PLFS instruments", year: "2026" },
        { stat: "~25 lakh", detail: "the government's own estimate of LGBT Indians, given to the Supreme Court and derived from 2012 figures. It is the only official number and it rests on nothing that was collected for the purpose.", source: "Union of India submission to the Supreme Court", year: "2018" }
      ],
      cost: "Every claim about health, employment or violence for this population has to be argued from small non-random studies. A ministry can decline a scheme on the ground that the need is not established, and be technically correct.",
      proxy: "None at national scale. Community-led surveys exist and are neither representative nor comparable across states."
    },
    {
      id: "caste", name: "Caste beyond SC and ST", kind: "frozen", color: "#b45309",
      missing: "The Census enumerates Scheduled Castes and Scheduled Tribes. It has not enumerated other castes since 1931.",
      evidence: [
        { stat: "1931", detail: "the last Census to count caste in full. Every OBC entitlement since has been argued from estimates, commission findings and sample surveys rather than an enumeration.", source: "Census of India", year: "1931" },
        { stat: "63%", detail: "OBC and EBC share of Bihar's population in the state's own 2023 survey. No national figure exists to place beside it.", source: "Bihar Caste-based Survey", year: "2023" },
        { stat: "27%", detail: "OBC reservation in central posts and institutions, upheld in 1992, still rests on a population share nobody has measured nationally.", source: "Indra Sawhney v. Union of India", year: "1992" }
      ],
      cost: "Proportionality is the language Indian reservation policy argues in, and for the largest reserved category the denominator is missing. Both sides of every OBC dispute cite estimates.",
      proxy: "NSS and NFHS record a self-reported caste category, which gives shares but not the jati-level detail policy questions turn on."
    },
    {
      id: "disability", name: "Disability", kind: "under", color: "#0369a1",
      missing: "India records disability at a fraction of the rate found everywhere else, and most people it does record hold no certificate.",
      evidence: [
        { stat: "2.2%", detail: "of the population, in both the Census and the NSS 76th Round, measured independently and agreeing with each other.", source: "Census of India; NSS 76th Round", year: "2011, 2018" },
        { stat: "~16%", detail: "global prevalence estimated by the WHO. The gap between the two implies roughly 150 million people India does not record as disabled.", source: "WHO Global Report on Health Equity for Persons with Disabilities", year: "2022" },
        { stat: "28.8%", detail: "of persons with disabilities hold a disability certificate. Reservation, pension, concessions and standing under the RPwD Act all require one.", source: "NSS 76th Round", year: "2018" }
      ],
      cost: "Budgets, quotas and accessibility obligations are all sized against 2.2%. Seven in ten of those counted cannot claim what the count entitles them to.",
      proxy: "NFHS-5 added disability questions, which is why prevalence estimates from it run higher than the Census. The instrument, not the population, is what changed."
    },
    {
      id: "unpaid", name: "Unpaid care and domestic work", kind: "frozen", color: "#be185d",
      missing: "India measured how its households spend time once, in 2019, and does not carry the result into any national account.",
      evidence: [
        { stat: "299 vs 97", detail: "minutes a day of unpaid domestic work by women and by men, from the only full Time Use Survey India has run.", source: "Time Use Survey, NSO", year: "2019" },
        { stat: "Excluded", detail: "None of it enters GDP. The System of National Accounts places unpaid household services outside the production boundary, and India follows that convention.", source: "System of National Accounts", year: "2008" }
      ],
      cost: "The single largest block of work done in India is invisible to the measure that decides whether the economy grew. Policy on childcare, elder care and women's employment argues without it.",
      proxy: "The 2019 survey remains usable and is now several years old. A second round would make it a series rather than a snapshot."
    },
    {
      id: "death", name: "What Indians die of", kind: "under", color: "#7f1d1d",
      missing: "Deaths are registered. The cause is medically certified for a small minority of them.",
      evidence: [
        { stat: "22.3%", detail: "of registered deaths carried a medically certified cause. For roughly four in five deaths, the cause is not recorded in the system health policy is argued from.", source: "Medical Certification of Cause of Death, ORGI", year: "2022" },
        { stat: "100% to <7%", detail: "the range of certification rates across states, from Goa and Manipur at the top to Bihar, Jharkhand and Madhya Pradesh at the bottom.", source: "Medical Certification of Cause of Death, ORGI", year: "2020" }
      ],
      cost: "Disease burden estimates for India are largely modelled rather than counted, and the states with the weakest certification are the ones whose burden most needs to be known.",
      proxy: "The Million Death Study used verbal autopsy on a large sample and remains the main evidence for cause of death outside the certified minority."
    },
    {
      id: "migration", name: "Where people moved", kind: "frozen", color: "#4d7c0f",
      missing: "The only full picture of internal migration is from a Census taken in 2011.",
      evidence: [
        { stat: "45.6 crore", detail: "internal migrants counted, about 37% of the population, in the last Census India completed.", source: "Census of India", year: "2011" },
        { stat: "2021", detail: "The Census due in 2021 was postponed. Nothing has replaced it as a source for district-level migration.", source: "Registrar General of India", year: "2021 onward" }
      ],
      cost: "The 2020 lockdown found the state without a current count of who was where. Entitlements are tied to place of registration, which is precisely what migration breaks.",
      proxy: "PLFS added a migration module in 2020-21, and e-Shram has registered over 30 crore unorganised workers. Neither reproduces the Census's district-to-district detail."
    },
    {
      id: "poverty", name: "How many are poor", kind: "frozen", color: "#166534",
      missing: "India has published no official poverty line, and no official poverty count, for more than a decade.",
      evidence: [
        { stat: "2011-12", detail: "the last consumption survey used for an official poverty estimate. The 2017-18 round was not released.", source: "NSSO; Ministry of Statistics", year: "2011-12, 2019" },
        { stat: "11 years", detail: "between that survey and the Household Consumption Expenditure Survey of 2022-23, which was published without an accompanying official poverty line.", source: "Household Consumption Expenditure Survey", year: "2022-23" }
      ],
      cost: "Every poverty claim about India in the intervening years, in either direction, rests on a researcher's own line rather than the state's.",
      proxy: "The NITI Aayog National MPI counts deprivation across twelve indicators rather than income, which answers a different question and is not a substitute."
    },
    {
      id: "appearance", name: "Skin tone and appearance", kind: "never", color: "#9d174d",
      missing: "No Indian official survey records skin tone, body size, or discrimination based on either.",
      evidence: [
        { stat: "Zero", detail: "national instruments collect it. Evidence on colourism in hiring or marriage comes from audit studies and market data rather than from statistics.", source: "Review of NSO and Census instruments", year: "2026" },
        { stat: "2014", detail: "ASCI guidelines bar advertising that portrays darker skin as a barrier to success, which is a regulator conceding the pattern exists without anyone measuring it.", source: "Advertising Standards Council of India", year: "2014" }
      ],
      cost: "A form of sorting that people describe constantly cannot be entered into any equality argument that requires numbers.",
      proxy: "None. This is the widest gap on the page between what is documented in daily life and what is documented at all."
    }
  ];

  return { gaps: gaps, KINDS: KINDS };
})();
