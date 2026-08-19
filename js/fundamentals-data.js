/* =============================================================================
   ImpactMojo — Fundamentals: the Indian Wheel of Power & Powerlessness
   -----------------------------------------------------------------------------
   Dataset for /fundamentals/wheel.html

   The wheel itself is NOT ImpactMojo's. It is the Indian Wheel of Power &
   Powerlessness, built in 2022-23 by The Listeners Collective (Bengaluru) —
   Disha Paul, Ayush Biswas, Trupti M. and Ganga Nair, with contributors —
   adapting Sylvia Duckworth's Wheel of Power/Privilege, itself made for the
   Canadian Council for Refugees. See the credits section of the page.

   What ImpactMojo adds here is the evidence layer: for each of the 36 segments,
   the Indian statistics, laws and judgments that bear on where that group sits,
   plus an honest note on what the evidence does NOT settle.

   Every `evidence` entry must carry a named source and a year. If we could not
   source it, it is not in here — and where an axis has thin official data, the
   `complication` field says so rather than inventing precision.
   ============================================================================= */

window.FUNDAMENTALS = (function () {
  "use strict";

  var RING_LABEL = {
    power:  "Closer to power",
    middle: "In between",
    margin: "Pushed to the margin"
  };

  var axes = [

  /* ---------------------------------------------------------------- 1. CASTE */
  {
    id: "caste",
    name: "Caste",
    color: "#b45309",
    question: "The jati you were born into, and who you are expected to marry.",
    intro: "Caste is assigned at birth, and it is enumerated in law for some groups and not others. It also has more Indian data behind it than any other axis here, which is why this wedge carries the most numbers.",
    complication: "Caste is not a single ladder. The OBC band holds dominant landowning castes and very poor artisanal ones together. A Dalit household in Kerala and one in Bihar live in different worlds. Adivasi disadvantage also works differently, through land alienation and distance from services rather than ritual rank, which is part of why ST outcomes are worse than SC outcomes on most indicators.",
    rings: {
      power: {
        groups: "Savarna castes — Brahmin, Kshatriya, Vaishya and the regionally dominant castes; the Census 'Others' category",
        short: "Upper caste",
        evidence: [
          { stat: "~1 in 3", detail: "of Indians outside the SC, ST and OBC categories are in the richest national wealth quintile.", source: "NFHS-5", year: "2019-21" },
          { stat: "~90%", detail: "of India's billionaire wealth is held by forward castes, who are roughly a fifth of the population.", source: "World Inequality Lab (Bharti, Chancel, Piketty, Somanchi)", year: "2024", url: "https://wid.world/news-article/inequality-in-india-the-billionaire-raj-is-now-more-unequal-than-the-british-colonial-raj/" },
          { stat: "14.9%", detail: "multidimensional poverty headcount for 'Others', the lowest of the four social groups.", source: "NITI Aayog National MPI, baseline round (NFHS-4)", year: "2015-16" },
          { stat: "Lowest", detail: "under-five mortality of the four social groups; OBC child mortality runs about 23% above the general category.", source: "NFHS-5", year: "2019-21" }
        ]
      },
      middle: {
        groups: "Other Backward Classes (OBC), including the Extremely Backward Classes",
        short: "OBC",
        evidence: [
          { stat: "24.5%", detail: "multidimensional poverty headcount, between SC at 29.2% and 'Others' at 14.9%.", source: "NITI Aayog National MPI, baseline round (NFHS-4)", year: "2015-16" },
          { stat: "+23%", detail: "under-five mortality among OBCs relative to the general category, at every childhood age.", source: "NFHS-5", year: "2019-21" },
          { stat: "27%", detail: "reservation in central government posts and institutions since the Mandal recommendations were upheld in Indra Sawhney, with a 'creamy layer' income bar.", source: "Indra Sawhney v. Union of India", year: "1992" },
          { stat: "1931", detail: "the last Census to enumerate caste beyond SC and ST. Bihar's own 2023 survey put OBC and EBC together at about 63% of the state. No national statistic can confirm that.", source: "Bihar Caste-based Survey", year: "2023" }
        ]
      },
      margin: {
        groups: "Scheduled Castes (Dalits) and Scheduled Tribes (Adivasis)",
        short: "SC / ST — Dalit, Adivasi",
        evidence: [
          { stat: "25%", detail: "of India: SC are 16.6% of the population and ST 8.6%.", source: "Census of India", year: "2011" },
          { stat: "44.4% / 29.2%", detail: "multidimensional poverty headcount for ST and SC, against 14.9% for 'Others'.", source: "NITI Aayog National MPI, baseline round (NFHS-4)", year: "2015-16" },
          { stat: "46% / 26%", detail: "of ST and SC members are in the poorest national wealth quintile.", source: "NFHS-5", year: "2019-21" },
          { stat: "50", detail: "under-five deaths per 1,000 live births among Scheduled Tribes, against a national 41.9.", source: "NFHS-5", year: "2019-21" },
          { stat: "57,582", detail: "cases registered as crimes against Scheduled Castes in a single year, a rate of 28.6 per lakh SC population. Uttar Pradesh recorded the most.", source: "NCRB, Crime in India", year: "2022" },
          { stat: "~27%", detail: "of surveyed households admitted that someone in the household practises untouchability.", source: "India Human Development Survey-II", year: "2011-12" },
          { stat: "21.2 / 25.9", detail: "higher-education gross enrolment ratio for ST and SC students, against 28.4 for all India.", source: "AISHE, Ministry of Education", year: "2021-22", url: "/aishe.html" }
        ]
      }
    },
    links: [
      { label: "AISHE Explorer — higher education by social category", href: "/aishe.html" },
      { label: "NFHS Explorer — health outcomes by group", href: "/nfhs.html" }
    ]
  },

  /* --------------------------------------------------------------- 2. GENDER */
  {
    id: "gender",
    name: "Gender",
    color: "#be185d",
    question: "Whether the gender you were assigned matches the one you live in.",
    intro: "India measures gender more thoroughly than anything else on this wheel, and still counts only two. The labour, health and time-use surveys all report male and female alone.",
    complication: "The middle band is not uniform, and the difference is not one of degree. Gopal Guru's argument that Dalit women talk differently is that their position is not a cis woman's position with caste added to it. Concentric rings cannot show two axes acting together.",
    rings: {
      power: {
        groups: "Cis men",
        short: "Cis men",
        evidence: [
          { stat: "78.8%", detail: "male labour force participation (15+, usual status), against 41.7% for women.", source: "PLFS Annual Report", year: "2023-24", url: "/plfs.html" },
          { stat: "97 min", detail: "a day spent by men on unpaid domestic work, against 299 minutes by women.", source: "Time Use Survey, NSO", year: "2019" },
          { stat: "86%", detail: "of the 18th Lok Sabha: 469 of 543 members are men.", source: "Election Commission of India", year: "2024", url: "/eci.html" },
          { stat: "<14%", detail: "of operational agricultural holdings are operated by women, in a country where most women workers are in agriculture.", source: "Agriculture Census", year: "2015-16" }
        ]
      },
      middle: {
        groups: "Cis women",
        short: "Cis women",
        evidence: [
          { stat: "41.7%", detail: "female labour force participation, up from 23.3% in 2017-18 and still barely half the male rate.", source: "PLFS Annual Report", year: "2023-24", url: "/plfs.html" },
          { stat: "299 min", detail: "a day on unpaid domestic work, over three times what men do. None of it enters the national accounts.", source: "Time Use Survey, NSO", year: "2019" },
          { stat: "929", detail: "girls born per 1,000 boys in the five years before the survey. No natural process produces a ratio that low.", source: "NFHS-5", year: "2019-21" },
          { stat: "~30%", detail: "of ever-married women aged 18-49 report physical or sexual violence by a spouse; a small minority of them ever seek help.", source: "NFHS-5", year: "2019-21" },
          { stat: "33%", detail: "of legislative seats reserved for women by the Nari Shakti Vandan Adhiniyam, but only after the next delimitation and Census.", source: "Constitution (106th Amendment) Act", year: "2023" }
        ]
      },
      margin: {
        groups: "Transgender, non-binary and intersex people",
        short: "Trans & intersex",
        evidence: [
          { stat: "4.88 lakh", detail: "transgender persons counted in the only Census that has ever asked. Researchers treat the figure as a severe undercount.", source: "Census of India", year: "2011" },
          { stat: "56.1%", detail: "literacy among the counted transgender population, against 74% nationally.", source: "Census of India", year: "2011" },
          { stat: "~96%", detail: "of transgender respondents reported being denied jobs; about 92% reported exclusion from economic activity altogether.", source: "Kerala Development Society study for the NHRC", year: "2017" },
          { stat: "2014", detail: "NALSA v. Union of India recognised the right to a self-identified gender. The 2019 Act still routes legal recognition through a District Magistrate's certificate.", source: "Supreme Court of India; Transgender Persons (Protection of Rights) Act", year: "2014, 2019" },
          { stat: "No count", detail: "of intersex people exists in any Indian official statistic; only Tamil Nadu has banned non-consensual infant sex-assignment surgery.", source: "Madras High Court, Arunkumar v. Inspector General of Registration", year: "2019" }
        ]
      }
    },
    links: [
      { label: "PLFS Workforce Explorer — the female participation gap", href: "/plfs" },
      { label: "Gender Studies Lab", href: "/Labs/gender-studies-lab.html" },
      { label: "Data Feminism Lab", href: "/Labs/data-feminism-lab.html" }
    ]
  },

  /* --------------------------------------------------- 3. SEXUAL ORIENTATION */
  {
    id: "sexuality",
    name: "Sexual orientation",
    color: "#7c3aed",
    question: "Who you are allowed to desire, and whether the law recognises the family you make.",
    intro: "The Indian state collects no data on sexual orientation. The Census, NFHS and PLFS do not ask, so every figure in this wedge describes the law rather than the population.",
    complication: "The outer band is not further out because it is more criminalised. It is not criminalised at all. Asexual, aromantic and pansexual people are at the margin because no law names them, no survey counts them and no institution has a category for them. That works differently from what gay and lesbian people face, and one radial scale cannot separate the two.",
    rings: {
      power: {
        groups: "Heterosexual people",
        short: "Straight",
        evidence: [
          { stat: "Every", detail: "Indian marriage statute presumes a man and a woman: the Hindu Marriage Act, the Special Marriage Act and the personal laws alike. Succession, insurance nomination, tenancy, hospital consent and adoption all follow from that presumption.", source: "Supriyo v. Union of India", year: "2023" },
          { stat: "Default", detail: "status in every official form that asks about marital status, and in the household definitions that structure NFHS, PLFS and the Census.", source: "NSO survey instruments", year: "2023-24" }
        ]
      },
      middle: {
        groups: "Gay, lesbian and bisexual people",
        short: "Gay / lesbian / bi",
        evidence: [
          { stat: "2018", detail: "Navtej Singh Johar read down Section 377. Consensual same-sex conduct between adults is no longer a crime.", source: "Supreme Court of India", year: "2018" },
          { stat: "2023", detail: "Supriyo v. Union of India declined to recognise same-sex marriage or civil unions, leaving the question to Parliament and a Cabinet Secretary-led committee.", source: "Supreme Court of India", year: "2023" },
          { stat: "None", detail: "of India's employment or housing law prohibits discrimination on grounds of sexual orientation. The Equality Bill drafts that would have done so were never introduced.", source: "Statutory review", year: "2026" },
          { stat: "~25 lakh", detail: "the government's own estimate of LGBT Indians, submitted to the Supreme Court. It was derived from 2012 figures and is almost certainly a fraction of the real number.", source: "Union of India submission", year: "2018" }
        ]
      },
      margin: {
        groups: "Asexual, aromantic, pansexual and questioning people",
        short: "Ace, aro, pan",
        evidence: [
          { stat: "Zero", detail: "official Indian statistics exist on asexual, aromantic or pansexual people. No national survey has ever asked.", source: "Review of Census, NFHS, PLFS instruments", year: "2026" },
          { stat: "2022", detail: "the National Medical Commission directed that so-called conversion therapy is professional misconduct, following the Madras High Court's directions in S. Sushma.", source: "NMC; Madras High Court", year: "2021, 2022" },
          { stat: "Compulsory", detail: "marriage remains the main enforcement mechanism: with 23.3% of women married before 18 and near-universal marriage by 30, opting out is not a recognised life course.", source: "NFHS-5", year: "2019-21" }
        ]
      }
    },
    links: [
      { label: "Ethics in Research Lab — consent and invisible populations", href: "/Labs/ethics-research-lab.html" }
    ]
  },

  /* ------------------------------------------------------------- 4. RELIGION */
  {
    id: "religion",
    name: "Religion",
    color: "#0f766e",
    question: "Whose festivals are public holidays, and whose personal law is the default.",
    intro: "Religion is the axis where a national average is least useful. A Christian in Mizoram or a Muslim in Lakshadweep lives in the majority.",
    complication: "Religion and caste are not independent here. The sharpest religious disability in Indian law, the exclusion of Dalit Christians and Dalit Muslims from SC status, is a caste rule enforced through religion. Jain and Parsi communities are small in number but sit near the top of most socioeconomic indicators, so minority and marginalised are not the same category.",
    rings: {
      power: {
        groups: "Hindus — in practice, upper-caste Hindus",
        short: "Hindu",
        evidence: [
          { stat: "79.8%", detail: "of the population, and the reference point from which 'minority' is defined in law.", source: "Census of India", year: "2011" },
          { stat: "73.3%", detail: "Hindu literacy, against a national rate of 73.0%. This is the community that sets the average.", source: "Census of India", year: "2011" },
          { stat: "Structural", detail: "advantage in the public calendar, in the personal law that governs the largest number of Indians, and in the Article 25 explanation that folds Sikhs, Jains and Buddhists into 'Hindu' for legal purposes.", source: "Constitution of India, Art. 25", year: "1950" }
        ]
      },
      middle: {
        groups: "Sikhs, Jains, Buddhists, Parsis and Jews",
        short: "Sikh, Jain, Buddhist",
        evidence: [
          { stat: "94.9%", detail: "Jain literacy, the highest of any religious community in India, against a national 73.0%.", source: "Census of India", year: "2011" },
          { stat: "81.3% / 75.4%", detail: "Buddhist and Sikh literacy, both above the national average.", source: "Census of India", year: "2011" },
          { stat: "Included", detail: "Sikh and Buddhist converts of Dalit origin retain Scheduled Caste status under the 1950 Presidential Order as amended. Christians and Muslims of the same origin do not.", source: "Constitution (Scheduled Castes) Order, para 3", year: "1950, amended 1956 and 1990" }
        ]
      },
      margin: {
        groups: "Muslims, Christians and followers of Indigenous faiths",
        short: "Muslim, Christian, Sarna",
        evidence: [
          { stat: "14.2% vs 4.4%", detail: "Muslims as a share of the population, against their share of the 18th Lok Sabha, where they hold 24 of 543 seats. The governing alliance returned none.", source: "Census 2011; Election Commission of India", year: "2011, 2024" },
          { stat: "3% / 4%", detail: "of IAS and IPS officers were Muslim when the Sachar Committee counted, against 13.4% of the population at the time.", source: "Sachar Committee Report", year: "2006" },
          { stat: "68.5%", detail: "Muslim literacy, the lowest of India's major religious communities and 4.5 points below the national rate.", source: "Census of India", year: "2011" },
          { stat: "Excluded", detail: "Dalit Christians and Dalit Muslims are barred from SC reservation by para 3 of the 1950 Order. The Ranganath Misra Commission recommended removing the religious bar; it has not been removed.", source: "Ranganath Misra Commission", year: "2007" },
          { stat: "No code", detail: "Indigenous faiths such as Sarna and Donyi-Polo have no Census code of their own. They are absorbed into 'other religions', about 0.7% of the count. Jharkhand's Assembly asked for a Sarna code in 2020 and has not been given one.", source: "Census of India; Jharkhand Assembly resolution", year: "2011, 2020" }
        ]
      }
    },
    links: [
      { label: "Inequality Basics — 101 course", href: "/101-courses/inequality-basics.html" }
    ]
  },

  /* ------------------------------------------------------ 5. ECONOMIC POSITION */
  {
    id: "economic",
    name: "Economic position",
    color: "#166534",
    question: "What you own, and whether you inherited it.",
    intro: "Income poverty and multidimensional poverty have both fallen a long way. Wealth concentration has risen to its highest level since 1961. This ring has to hold both facts.",
    complication: "This ring mixes assets with income. A salaried graduate with no property and a landless farmer with no wages are in different positions, and neither clearly ranks above the other. Economic position is also the one axis people move along within a lifetime, so it behaves differently from caste or disability even where the gaps look similar.",
    rings: {
      power: {
        groups: "The owning class — inherited property, land and capital income",
        short: "Owning class",
        evidence: [
          { stat: "40.1%", detail: "of national wealth is held by the top 1%, the highest concentration recorded since 1961.", source: "World Inequality Lab", year: "2022-23", url: "https://wid.world/news-article/inequality-in-india-the-billionaire-raj-is-now-more-unequal-than-the-british-colonial-raj/" },
          { stat: "22.6%", detail: "of national income goes to the top 1%, the highest share since the series begins in 1922.", source: "World Inequality Lab", year: "2022-23" },
          { stat: "162", detail: "billionaires in 2022, from one in 1991. The authors call the result a 'Billionaire Raj' more unequal than the British Raj.", source: "World Inequality Lab", year: "2024" },
          { stat: "Nil", detail: "inheritance tax. Estate duty was abolished in 1985 and wealth tax in 2016, so transmitted advantage is untaxed at transfer.", source: "Finance Acts", year: "1985, 2016" }
        ]
      },
      middle: {
        groups: "Salaried middle and upper-middle households",
        short: "Middle income",
        evidence: [
          { stat: "15%", detail: "of national income goes to the bottom half of the population.", source: "World Inequality Lab", year: "2022-23" },
          { stat: "~22%", detail: "of workers hold regular salaried jobs at all. About 58% are self-employed and about 20% are casual labour.", source: "PLFS Annual Report", year: "2023-24", url: "/plfs.html" },
          { stat: "Most", detail: "regular wage workers in the non-agricultural sector have no written contract and no eligibility for paid leave or social security.", source: "PLFS Annual Report", year: "2023-24" }
        ]
      },
      margin: {
        groups: "Below the poverty line, unemployed, in debt, homeless",
        short: "BPL, in debt, homeless",
        evidence: [
          { stat: "80.7 crore", detail: "people are entitled to free foodgrain under the National Food Security Act. That is the state's own estimate of how many cannot reliably buy food.", source: "Dept. of Food & Public Distribution", year: "2024" },
          { stat: "17.7 lakh", detail: "homeless persons counted in the last Census. Researchers and municipal surveys consistently find the figure too low.", source: "Census of India", year: "2011" },
          { stat: "~26%", detail: "of all recorded suicides in India are of daily-wage earners, the largest occupational category in the data.", source: "NCRB, Accidental Deaths & Suicides in India", year: "2022" },
          { stat: "46% / 26%", detail: "of Scheduled Tribe and Scheduled Caste members are in the poorest wealth quintile. Economic position is not independent of caste.", source: "NFHS-5", year: "2019-21" }
        ]
      }
    },
    links: [
      { label: "Inequality Basics — 101 course", href: "/101-courses/inequality-basics.html" },
      { label: "Budget & Fiscal Lab", href: "/Labs/budget-fiscal-lab.html" },
      { label: "The Long View — inequality charts", href: "/the-long-view.html" }
    ]
  },

  /* ------------------------------------------------------------ 6. EDUCATION */
  {
    id: "education",
    name: "Education",
    color: "#1d4ed8",
    question: "How long you were in school, in which language, and at whose institution.",
    intro: "Schooling has expanded much faster than learning. What opens a door is rarely a degree on its own, but a degree from a particular institution in a particular language.",
    complication: "Two things are stacked into one ring: years of schooling, and the language and standing of the institution. A first-generation graduate from a state university and a second-generation graduate from an English-medium institution sit in the same band by years and nowhere near each other in the job market.",
    rings: {
      power: {
        groups: "College graduates, elite and foreign-educated",
        short: "Graduate",
        evidence: [
          { stat: "28.4", detail: "gross enrolment ratio in higher education. Fewer than three in ten 18 to 23 year olds are enrolled anywhere.", source: "AISHE, Ministry of Education", year: "2021-22", url: "/aishe.html" },
          { stat: "10.6%", detail: "of Indians report English at any level. Higher education, the higher judiciary and the corporate labour market run on it.", source: "Census of India", year: "2011" }
        ]
      },
      middle: {
        groups: "First-generation learners; school-completed",
        short: "Finished school",
        evidence: [
          { stat: "23.4%", detail: "of Class 3 children in rural government schools can read a Class 2 text. That is above pre-pandemic levels and still under a quarter.", source: "ASER (Pratham)", year: "2024", url: "/aser.html" },
          { stat: "Expansion", detail: "GER rose from 23.7 to 28.4 in seven years, with the sharpest gains among ST and SC women.", source: "AISHE, Ministry of Education", year: "2014-15 to 2021-22" }
        ]
      },
      margin: {
        groups: "No formal education; interrupted schooling",
        short: "No formal schooling",
        evidence: [
          { stat: "73.0%", detail: "literacy at the last Census: 80.9% for men and 64.6% for women, a 16-point gap.", source: "Census of India", year: "2011" },
          { stat: "21.2 / 25.9", detail: "higher-education GER for ST and SC students, against 28.4 for all India. The education ring reproduces the caste ring.", source: "AISHE, Ministry of Education", year: "2021-22" },
          { stat: "1.01 crore", detail: "children aged 5-14 recorded as working rather than schooling at the last Census.", source: "Census of India", year: "2011" }
        ]
      }
    },
    links: [
      { label: "ASER Explorer — learning outcomes", href: "/aser.html" },
      { label: "UDISE+ Explorer — school system data", href: "/udise.html" },
      { label: "AISHE Explorer — higher education", href: "/aishe.html" }
    ]
  },

  /* ------------------------------------------------------ 7. BODY & APPEARANCE */
  {
    id: "body",
    name: "Body & appearance",
    color: "#9d174d",
    question: "How closely your body matches what gets treated as normal.",
    intro: "This axis has the least official data behind it. No Indian survey collects skin tone, body size or appearance-based discrimination, so its placement rests on market evidence, case law and qualitative research.",
    complication: "Almost nothing here is measured. There is no official Indian statistic on colourism in hiring, on size discrimination, or on how appearance affects marriage and work. The wheel is more confident about this axis than the available evidence allows, so treat the band as a gap in the research rather than a settled position.",
    rings: {
      power: {
        groups: "Fair skin; conventionally gendered bodies",
        short: "Fair skin",
        evidence: [
          { stat: "45 years", detail: "of 'Fair & Lovely' before Hindustan Unilever renamed it 'Glow & Lovely'. The category it sits in remains among the largest in Indian personal care.", source: "Hindustan Unilever announcement", year: "2020" },
          { stat: "2014", detail: "ASCI guidelines bar advertising that portrays darker skin as inferior or as a barrier to success, which had been the industry norm.", source: "Advertising Standards Council of India", year: "2014" }
        ]
      },
      middle: {
        groups: "Average build; conventional attractiveness",
        short: "Average build",
        evidence: [
          { stat: "24.0% / 22.9%", detail: "of women and men aged 15 to 49 are overweight or obese, up from 20.6% and 18.9% five years earlier.", source: "NFHS-5", year: "2019-21" },
          { stat: "Both ends", detail: "the same survey finds 18.7% of women and 16.2% of men underweight. India carries the double burden, and the middle band is statistically the smaller part of the population.", source: "NFHS-5", year: "2019-21" }
        ]
      },
      margin: {
        groups: "Dark skin, visible difference, disabled or gender-nonconforming bodies",
        short: "Dark skin, disabled",
        evidence: [
          { stat: "~150", detail: "acid attack cases recorded a year. Laxmi v. Union of India forced regulation of over-the-counter acid sale; enforcement remains partial.", source: "NCRB; Supreme Court of India", year: "2013, 2022" },
          { stat: "Not measured", detail: "no Indian official survey collects skin tone, body size or appearance-based discrimination. The evidence is matrimonial-market and audit-study research, not statistics.", source: "Review of NSO and Census instruments", year: "2026" }
        ]
      }
    },
    links: [
      { label: "Data Feminism Lab — what gets counted", href: "/Labs/data-feminism-lab.html" }
    ]
  },

  /* --------------------------------------------- 8. NEURODIVERSITY & ABILITY */
  {
    id: "ability",
    name: "Neurodiversity & ability",
    color: "#0369a1",
    question: "Whether the environment was built for your body and mind, and whether the state has certified that it wasn't.",
    intro: "India records disability at about 2.2% of its population. The global estimate is nearer 16%. The gap between the two is roughly 150 million people.",
    complication: "The middle band, mild disability and chronic illness without a diagnosis or a certificate, is where most people actually are, and it is defined by a missing document rather than by the condition. Without a certificate there is no reservation, no pension, no rail concession and no standing under the RPwD Act. What moves a person between these bands is certification, not impairment.",
    rings: {
      power: {
        groups: "Able-bodied and neurotypical people",
        short: "Able-bodied",
        evidence: [
          { stat: "Built for", detail: "the default in transport, buildings, examination formats and workplace design. The RPwD Act's accessibility obligations carry deadlines that have repeatedly been extended.", source: "Rights of Persons with Disabilities Act", year: "2016" }
        ]
      },
      middle: {
        groups: "Mild disability, chronic illness, undiagnosed or uncertified",
        short: "Mild / uncertified",
        evidence: [
          { stat: "28.8%", detail: "of persons with disabilities hold a disability certificate: 32.4% of men and 24.1% of women. Seven in ten are outside every entitlement that requires one.", source: "NSS 76th Round, Persons with Disabilities in India", year: "2018" },
          { stat: "21", detail: "conditions recognised under the RPwD Act, up from 7. Learning disabilities, autism and mental illness entered the schedule only in 2016, so the diagnosed population is young and thin.", source: "Rights of Persons with Disabilities Act", year: "2016" }
        ]
      },
      margin: {
        groups: "Severe and multiple disability; significant neurodivergence",
        short: "Severe / multiple",
        evidence: [
          { stat: "2.68 crore", detail: "persons with disabilities counted, or 2.21% of the population. The NSS 76th Round independently finds 2.2%.", source: "Census of India; NSS 76th Round", year: "2011, 2018" },
          { stat: "~16%", detail: "global disability prevalence estimated by the WHO. India's measured 2.2% implies an undercount on the order of 150 million people.", source: "WHO Global Report on Health Equity for Persons with Disabilities", year: "2022" },
          { stat: "36%", detail: "of persons with disabilities were recorded as workers at the last Census, against a general work participation rate of about 40%.", source: "Census of India", year: "2011" },
          { stat: "54.5%", detail: "literacy among persons with disabilities, against 73.0% nationally.", source: "Census of India", year: "2011" },
          { stat: "4%", detail: "reservation in government posts under the RPwD Act. It is filled well below quota, with backlog vacancies carried year on year.", source: "Rights of Persons with Disabilities Act", year: "2016" }
        ]
      }
    },
    links: [
      { label: "Disability-Inclusive MEL Lab", href: "/Labs/disability-inclusive-mel-lab.html" }
    ]
  },

  /* ------------------------------------------------------------- 9. LANGUAGE */
  {
    id: "language",
    name: "Language",
    color: "#a16207",
    question: "Which language you speak, and whether the state and the employer speak it back.",
    intro: "The Census recognised 1,369 mother tongues and grouped them into 121 languages. The Constitution schedules 22. The higher judiciary works in one.",
    complication: "Most Indians speak two or three languages, so asking which language you speak is the wrong question. What this ring measures is which of your languages carries weight with the state and the employer. A Santali speaker who also has Hindi and English is not at the margin, and the wheel has no way to show that.",
    rings: {
      power: {
        groups: "English plus the state language (and Hindi across the Hindi belt)",
        short: "English",
        evidence: [
          { stat: "10.6%", detail: "of Indians report English as a first, second or third language. That minority staffs the higher judiciary, higher education and formal-sector hiring.", source: "Census of India", year: "2011" },
          { stat: "Article 348", detail: "proceedings in the Supreme Court and every High Court are in English unless the President permits otherwise.", source: "Constitution of India", year: "1950" }
        ]
      },
      middle: {
        groups: "Monolingual speakers of a Scheduled language",
        short: "Scheduled language",
        evidence: [
          { stat: "22", detail: "languages in the Eighth Schedule. Inclusion brings textbooks, public broadcasting, recruitment-exam options and official patronage.", source: "Constitution of India, Eighth Schedule", year: "1950 onward" },
          { stat: "43.6%", detail: "of Indians return Hindi as their mother tongue. The category absorbs dozens of distinct tongues, including Bhojpuri with over 5 crore speakers.", source: "Census of India", year: "2011" }
        ]
      },
      margin: {
        groups: "Speakers of non-scheduled and Indigenous languages",
        short: "Indigenous languages",
        evidence: [
          { stat: "10,000", detail: "the speaker threshold below which a mother tongue is not separately listed at all. 19,569 raw returns were rationalised to 1,369, then grouped into 121 languages.", source: "Census of India", year: "2011" },
          { stat: "~197", detail: "Indian languages are listed as endangered in UNESCO's Atlas, more than in any other country.", source: "UNESCO Atlas of the World's Languages in Danger", year: "2010" },
          { stat: "~50 / 400+", detail: "languages lost in five decades, and more than 400 assessed as at risk within the next fifty.", source: "People's Linguistic Survey of India", year: "2013" },
          { stat: "NEP 2020", detail: "commits to mother-tongue instruction to at least Grade 5, but teaching materials exist in a small fraction of the languages children actually arrive speaking.", source: "National Education Policy", year: "2020" }
        ]
      }
    },
    links: [
      { label: "Sarvam AI translation — ImpactMojo in 11 Indian languages", href: "/about.html" }
    ]
  },

  /* ------------------------------------------------------------------ 10. AGE */
  {
    id: "age",
    name: "Age",
    color: "#c2410c",
    question: "How old you are, and what that is worth in work and in care.",
    intro: "India is young, and the wheel reflects the country as it is now. The 60-plus share doubles by 2050, so this ring will read differently within a generation.",
    complication: "Everyone crosses this axis. The people at the centre reach the rim if they live long enough, which makes age unlike caste or disability even where the outcome gaps look similar. It also runs in both directions: children and the very old are both dependent, but only one group is treated as an investment.",
    rings: {
      power: {
        groups: "Young adults in the labour market",
        short: "Young adult",
        evidence: [
          { stat: "~28", detail: "India's median age. Roughly two-thirds of the population is between 15 and 59.", source: "UN World Population Prospects; MoSPI", year: "2022-24" }
        ]
      },
      middle: {
        groups: "Middle-aged adults",
        short: "Middle-aged",
        evidence: [
          { stat: "Peak", detail: "earning and caregiving years at once. This group carries both child and elder dependency in a system with almost no public care infrastructure.", source: "Time Use Survey, NSO", year: "2019" }
        ]
      },
      margin: {
        groups: "Children and vulnerable elders",
        short: "Children & elders",
        evidence: [
          { stat: "35.5%", detail: "of children under five are stunted, 32.1% underweight and 19.3% wasted. All three improved on the previous round and remain among the highest burdens in the world.", source: "NFHS-5", year: "2019-21", url: "/nfhs.html" },
          { stat: "1.01 crore", detail: "children aged 5-14 recorded as working.", source: "Census of India", year: "2011" },
          { stat: "10.5% to 20.8%", detail: "the 60-plus share of the population between 2022 and 2050, rising from 14.9 crore to 34.7 crore people.", source: "UNFPA & IIPS, India Ageing Report", year: "2023" },
          { stat: "40%+", detail: "of India's elderly are in the poorest wealth quintile, and about 18.7% live with no income of their own.", source: "UNFPA & IIPS, India Ageing Report", year: "2023" },
          { stat: "+279%", detail: "projected growth in the 80-plus population by 2050, predominantly widowed and highly dependent very old women.", source: "UNFPA & IIPS, India Ageing Report", year: "2023" }
        ]
      }
    },
    links: [
      { label: "NFHS Explorer — child nutrition", href: "/nfhs.html" }
    ]
  },

  /* --------------------------------------------- 11. GEOGRAPHY & CITIZENSHIP */
  {
    id: "geography",
    name: "Geography & citizenship",
    color: "#4d7c0f",
    question: "Where you live, where you moved from, and whether the state treats you as belonging.",
    intro: "This axis holds two separate things: distance from infrastructure, and distance from unquestioned citizenship. India's borderlands carry both.",
    complication: "Metropolitan means power for infrastructure and the reverse for cost and security. A migrant construction worker in Mumbai is metropolitan and marginal at the same time; a landowning farmer in a district town is rural and secure. One ring per axis cannot hold that, and local context matters more here than anywhere else on the wheel.",
    rings: {
      power: {
        groups: "Metropolitan residents; locals; unquestioned citizens",
        short: "Metro",
        evidence: [
          { stat: "Concentration", detail: "of tertiary hospitals, universities, courts and formal employment in a small number of urban agglomerations. That is what access means on this axis.", source: "AISHE; NFHS-5", year: "2019-22" }
        ]
      },
      middle: {
        groups: "Rural residents and inter-state migrants",
        short: "Rural, migrant",
        evidence: [
          { stat: "45.6 crore", detail: "internal migrants, or 37% of the population. Most moved for marriage, then for work.", source: "Census of India", year: "2011" },
          { stat: "30 crore+", detail: "unorganised workers registered on e-Shram. Entitlements largely remain tied to the state of registration, so movement costs benefits.", source: "Ministry of Labour & Employment", year: "2024" },
          { stat: "Rural gaps", detail: "persist across NFHS indicators. Institutional delivery, stunting, anaemia and access to improved sanitation all track the rural-urban line.", source: "NFHS-5", year: "2019-21" }
        ]
      },
      margin: {
        groups: "Kashmir, the North-East, the islands, and non-citizens",
        short: "Kashmir, NE, islands",
        evidence: [
          { stat: "116", detail: "internet shutdowns in a single year, the sixth consecutive year India led the world. Manipur alone accounted for 47 orders, covering the state for 212 days.", source: "Access Now, #KeepItOn", year: "2023", url: "https://www.accessnow.org/press-release/india-keepiton-internet-shutdowns-2023-en/" },
          { stat: "2019", detail: "Article 370 was read down and Jammu & Kashmir was reorganised from a state into two Union Territories, the only such downgrade in Indian history.", source: "Jammu & Kashmir Reorganisation Act", year: "2019" },
          { stat: "19 lakh", detail: "people left out of the final Assam National Register of Citizens, facing Foreigners Tribunals to establish citizenship they had assumed.", source: "Office of the State Coordinator, NRC Assam", year: "2019" },
          { stat: "AFSPA", detail: "remains in force in parts of the North-East and Jammu & Kashmir, granting armed forces powers that do not apply elsewhere in the country.", source: "Armed Forces (Special Powers) Act", year: "1958, in force" }
        ]
      }
    },
    links: [
      { label: "Cities Explorer", href: "/cities.html" },
      { label: "IHDS Explorer — rural-urban outcomes", href: "/ihds.html" }
    ]
  },

  /* -------------------------------------------------- 12. RELATIONSHIP STATUS */
  {
    id: "relationship",
    name: "Relationship status",
    color: "#6d28d9",
    question: "Whether you are married, and whether your family and the law approve of the match.",
    intro: "Marriage in India is rarely a private arrangement. It is how caste is reproduced, how property moves between generations, and how legal standing is acquired.",
    complication: "The wheel puts married at the centre and child marriage in the middle band. But marriage confers power only when it is chosen, and 23.3% of Indian women aged 20 to 24 were married before they turned 18.",
    rings: {
      power: {
        groups: "Married — within caste and religion, with family approval",
        short: "Married",
        evidence: [
          { stat: "~95%", detail: "of Indian marriages are within caste. The 5% that are not are the exception the system is built to prevent.", source: "India Human Development Survey-II", year: "2011-12" },
          { stat: "Gateway", detail: "succession, insurance nomination, tenancy, hospital consent, adoption and most housing rentals run through recognised marriage.", source: "Supriyo v. Union of India", year: "2023" }
        ]
      },
      middle: {
        groups: "Dating, engaged, or married under compulsion",
        short: "Dating, engaged",
        evidence: [
          { stat: "23.3%", detail: "of women aged 20 to 24 were married before 18, down from 26.8% in the previous round and still nearly one in four.", source: "NFHS-5", year: "2019-21" },
          { stat: "Under-recorded", detail: "so-called honour killings appear in NCRB data in the low tens each year, a figure researchers and state commissions treat as a fraction of the real count.", source: "NCRB, Crime in India", year: "2022" },
          { stat: "Protected", detail: "inter-faith and inter-caste couples face registration objections under state 'conversion' laws enacted since 2018 in several states, despite Shafin Jahan and Lata Singh affirming the right to choose.", source: "Supreme Court of India", year: "2006, 2018" }
        ]
      },
      margin: {
        groups: "Single, divorced, separated, widowed, or in unrecognised relationships",
        short: "Single, divorced, widowed",
        evidence: [
          { stat: "7.14 crore", detail: "single women in India, whether widowed, divorced, separated or never married. That is a 39% rise in a decade, from 5.12 crore.", source: "Census of India", year: "2011" },
          { stat: "68%", detail: "growth in single women aged 25 to 29 between the two Censuses, the sharpest rise of any age band.", source: "Census of India", year: "2001-2011" },
          { stat: "2005 / 2020", detail: "the Hindu Succession (Amendment) Act gave daughters coparcenary rights, and Vineeta Sharma confirmed they apply regardless of when the father died. Widows' property claims remain contested in practice.", source: "Parliament; Supreme Court of India", year: "2005, 2020" },
          { stat: "None", detail: "live-in and same-sex partners have no automatic succession, insurance-nominee or next-of-kin standing after Supriyo declined to recognise non-marital unions.", source: "Supriyo v. Union of India", year: "2023" }
        ]
      }
    },
    links: [
      { label: "Gender Studies Lab", href: "/Labs/gender-studies-lab.html" }
    ]
  }

  ];

  return { axes: axes, RING_LABEL: RING_LABEL, RING_ORDER: ["power", "middle", "margin"] };
})();
