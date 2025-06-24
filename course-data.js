// Course and Lab Data for ImpactMojo
// All 34 courses with CORRECTED URLs - DUPLICATE REMOVED

// COMPLETE COURSE DATA - ALL COURSES WITH CORRECT URLS
const courses = [
  // DATA ANALYSIS TRACK
  {
    id: 'data-feminism-101',
    number: 1,
    title: 'Data Feminism 101',
    description: 'Challenges dominant data narratives using feminist theory and South Asian contexts.',
    category: 'Data Analysis',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    icon: 'fas fa-venus',
    url: 'https://101.www.impactmojo.in/DataFem',
    learnerCount: 2847,
    rating: 4.8,
    prerequisites: ['Basic data literacy', 'Interest in gender studies'],
    outcomes: ['Apply feminist lens to data analysis', 'Identify bias in datasets', 'Design inclusive data collection'],
    audience: 'Data scientists, researchers, gender advocates'
  },
  {
    id: 'data-literacy-101',
    number: 2,
    title: 'Data Literacy 101',
    description: 'Foundational skills for understanding and working with data in development contexts.',
    category: 'Data Analysis',
    difficulty: 'beginner',
    duration: '3-4 hours',
    icon: 'fas fa-chart-bar',
    url: 'https://101.www.impactmojo.in/data-lit',
    learnerCount: 1734,
    rating: 4.9,
    prerequisites: ['None - foundational course'],
    outcomes: ['Understand data concepts', 'Read data visualizations', 'Ask good questions of data'],
    audience: 'Beginners, development practitioners, program managers'
  },
  // DUPLICATE REMOVED - ONLY ONE DATA LITERACY 101 NOW
  {
    id: 'eda-survey-data',
    number: 3,
    title: 'EDA for Survey Data',
    description: 'Exploratory Data Analysis techniques specifically for household and survey datasets common in development work.',
    category: 'Data Analysis',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-search',
    url: 'https://101.www.impactmojo.in/HH-EDA',
    learnerCount: 1456,
    rating: 4.7,
    prerequisites: ['Data Literacy 101', 'Basic statistics'],
    outcomes: ['Conduct comprehensive EDA', 'Handle survey weights', 'Identify data quality issues'],
    audience: 'Researchers, data analysts, M&E specialists'
  },
  {
    id: 'bivariate-analysis-101',
    number: 4,
    title: 'Bivariate Analysis 101',
    description: 'Understanding relationships between two variables using statistical methods and visualization.',
    category: 'Data Analysis',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-project-diagram',
    url: 'https://101.www.impactmojo.in/bivariateA',
    learnerCount: 1298,
    rating: 4.6,
    prerequisites: ['Data Literacy 101', 'EDA for Survey Data'],
    outcomes: ['Analyze variable relationships', 'Choose appropriate tests', 'Interpret correlation vs causation'],
    audience: 'Data analysts, researchers, program evaluators'
  },
  {
    id: 'multivariate-analysis-101',
    number: 5,
    title: 'Multivariate Analysis 101',
    description: 'Advanced statistical techniques for analyzing multiple variables simultaneously.',
    category: 'Data Analysis',
    difficulty: 'advanced',
    duration: '5-6 hours',
    icon: 'fas fa-cube',
    url: 'https://101.www.impactmojo.in/MultivariateA',
    learnerCount: 987,
    rating: 4.5,
    prerequisites: ['Bivariate Analysis 101', 'Basic econometrics'],
    outcomes: ['Conduct regression analysis', 'Handle multiple variables', 'Control for confounders'],
    audience: 'Advanced researchers, econometricians, impact evaluators'
  },

  // GENDER STUDIES TRACK  
  {
    id: 'gender-studies-101',
    number: 6,
    title: 'Gender Studies 101',
    description: 'Foundational concepts in gender studies with South Asian development applications.',
    category: 'Gender Studies',
    difficulty: 'beginner',
    duration: '3-4 hours',
    icon: 'fas fa-venus-mars',
    url: 'https://101.www.impactmojo.in/Gender',
    learnerCount: 2341,
    rating: 4.7,
    prerequisites: ['None - foundational course'],
    outcomes: ['Understand gender concepts', 'Apply intersectional analysis', 'Design gender-sensitive programs'],
    audience: 'Development practitioners, program managers, researchers'
  },
  {
    id: 'care-economy',
    number: 6,
    title: 'Care Economy',
    description: 'Understanding unpaid care work and its impact on economic development and gender equality.',
    category: 'Gender Studies',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-heart',
    url: 'https://101.www.impactmojo.in/careeconomy',
    learnerCount: 1876,
    rating: 4.6,
    prerequisites: ['Gender Studies 101'],
    outcomes: ['Analyze care work patterns', 'Design care-responsive policies', 'Measure unpaid labor'],
    audience: 'Gender specialists, policy analysts, economists'
  },
  {
    id: 'womens-economic-empowerment',
    number: 7,
    title: 'Women\'s Economic Empowerment',
    description: 'Strategies and interventions for promoting women\'s economic participation and empowerment.',
    category: 'Gender Studies',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-female',
    url: 'https://101.www.impactmojo.in/WEE',
    learnerCount: 1654,
    rating: 4.5,
    prerequisites: ['Gender Studies 101'],
    outcomes: ['Design empowerment programs', 'Understand barriers to participation', 'Measure economic outcomes'],
    audience: 'Program managers, gender specialists, livelihood practitioners'
  },

  // ECONOMICS TRACK
  {
    id: 'development-economics-101',
    number: 8,
    title: 'Development Economics 101',
    description: 'Economic analysis and development theory for practitioners working in South Asia.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-chart-line',
    url: 'https://101.www.impactmojo.in/DevEcon',
    learnerCount: 1923,
    rating: 4.6,
    prerequisites: ['Basic economics knowledge'],
    outcomes: ['Apply economic theories', 'Analyze development challenges', 'Design economic interventions'],
    audience: 'Economists, policy analysts, development practitioners'
  },
  {
    id: 'political-economy-101',
    number: 9,
    title: 'Political Economy 101',
    description: 'Understanding the intersection of politics and economics in development contexts.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-balance-scale',
    url: 'https://101.www.impactmojo.in/polecon',
    learnerCount: 1445,
    rating: 4.4,
    prerequisites: ['Development Economics 101'],
    outcomes: ['Analyze political-economic systems', 'Understand power dynamics', 'Design politically feasible interventions'],
    audience: 'Policy analysts, political scientists, development economists'
  },
  {
    id: 'poverty-inequality-101',
    number: 10,
    title: 'Poverty & Inequality 101',
    description: 'Comprehensive analysis of poverty and inequality measurement and interventions.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-chart-area',
    url: 'https://101.www.impactmojo.in/pov&inq',
    learnerCount: 1789,
    rating: 4.7,
    prerequisites: ['Development Economics 101'],
    outcomes: ['Measure poverty and inequality', 'Design targeting mechanisms', 'Evaluate redistribution policies'],
    audience: 'Policy analysts, program managers, researchers'
  },
  {
    id: 'econometrics-101',
    number: 11,
    title: 'Econometrics 101',
    description: 'Statistical methods for economic analysis and causal inference in development.',
    category: 'Economics',
    difficulty: 'advanced',
    duration: '5-6 hours',
    icon: 'fas fa-calculator',
    url: 'https://101.www.impactmojo.in/econometrics',
    learnerCount: 1234,
    rating: 4.3,
    prerequisites: ['Development Economics 101', 'Multivariate Analysis 101'],
    outcomes: ['Conduct causal analysis', 'Use instrumental variables', 'Design impact evaluations'],
    audience: 'Researchers, impact evaluators, advanced analysts'
  },
  {
    id: 'social-safety-nets-101',
    number: 12,
    title: 'Social Safety Nets 101',
    description: 'Understanding India\'s welfare architecture—PDS, NREGA, pensions—through lifecycle needs and exclusion errors.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-shield-alt',
    url: 'https://101.www.impactmojo.in/safetynets',
    learnerCount: 2156,
    rating: 4.7,
    prerequisites: ['Development Economics 101'],
    outcomes: ['Analyze safety net programs', 'Design targeting mechanisms', 'Evaluate program effectiveness'],
    audience: 'Policy analysts, program managers, social protection specialists'
  },

  // RESEARCH METHODS TRACK
  {
    id: 'research-ethics-101',
    number: 13,
    title: 'Research Ethics 101',
    description: 'Ethical frameworks and practices for conducting research with human subjects.',
    category: 'Research Methods',
    difficulty: 'beginner',
    duration: '3-4 hours',
    icon: 'fas fa-shield-check',
    url: 'https://101.www.impactmojo.in/ResearchEthics',
    learnerCount: 1567,
    rating: 4.8,
    prerequisites: ['None - foundational course'],
    outcomes: ['Apply ethical frameworks', 'Design ethical research', 'Obtain informed consent'],
    audience: 'Researchers, students, practitioners conducting studies'
  },
  {
    id: 'qualitative-research-101',
    number: 14,
    title: 'Qualitative Research 101',
    description: 'Methods and techniques for conducting qualitative research in development contexts.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-comments',
    url: 'https://101.www.impactmojo.in/QualR',
    learnerCount: 1398,
    rating: 4.6,
    prerequisites: ['Research Ethics 101'],
    outcomes: ['Design qualitative studies', 'Conduct interviews and FGDs', 'Analyze qualitative data'],
    audience: 'Researchers, M&E specialists, anthropologists'
  },
  {
    id: 'visual-ethnography-101',
    number: 15,
    title: 'Visual Ethnography 101',
    description: 'Using visual methods in ethnographic research and community engagement.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-camera',
    url: 'https://101.www.impactmojo.in/VEthno',
    learnerCount: 876,
    rating: 4.4,
    prerequisites: ['Qualitative Research 101'],
    outcomes: ['Use visual research methods', 'Engage communities through visuals', 'Analyze visual data'],
    audience: 'Anthropologists, community workers, visual researchers'
  },
  {
    id: 'mel-101',
    number: 16,
    title: 'MEL 101',
    description: 'Comprehensive monitoring, evaluation, and learning frameworks for development programs.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-chart-pie',
    url: 'https://101.www.impactmojo.in/MEAL',
    learnerCount: 2156,
    rating: 4.8,
    prerequisites: ['Research Ethics 101'],
    outcomes: ['Design MEL frameworks', 'Develop indicators', 'Conduct evaluations'],
    audience: 'M&E specialists, program managers, development practitioners'
  },

  // HEALTH TRACK
  {
    id: 'public-health-101',
    number: 17,
    title: 'Public Health 101',
    description: 'Fundamentals of public health systems, epidemiology, and health policy.',
    category: 'Health',
    difficulty: 'beginner',
    duration: '3-4 hours',
    icon: 'fas fa-heartbeat',
    url: 'https://101.www.impactmojo.in/ph',
    learnerCount: 1892,
    rating: 4.5,
    prerequisites: ['None - foundational course'],
    outcomes: ['Understand health systems', 'Analyze health determinants', 'Design health interventions'],
    audience: 'Health workers, program managers, policy analysts'
  },
  {
    id: 'srhr-101',
    number: 18,
    title: 'Sexual & Reproductive Health Rights',
    description: 'Rights-based approaches to sexual and reproductive health programming.',
    category: 'Health',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-venus',
    url: 'https://101.www.impactmojo.in/srhr',
    learnerCount: 1345,
    rating: 4.6,
    prerequisites: ['Public Health 101'],
    outcomes: ['Apply rights-based approaches', 'Design SRHR programs', 'Address stigma and discrimination'],
    audience: 'Health workers, gender specialists, rights advocates'
  },

  // ENVIRONMENT & CLIMATE
  {
    id: 'climate-science-101',
    number: 19,
    title: 'Climate Science 101',
    description: 'Understanding climate change science and its implications for development.',
    category: 'Environment',
    difficulty: 'beginner',
    duration: '3-4 hours',
    icon: 'fas fa-thermometer-half',
    url: 'https://101.www.impactmojo.in/ClimateScience',
    learnerCount: 1234,
    rating: 4.4,
    prerequisites: ['None - foundational course'],
    outcomes: ['Understand climate science', 'Analyze climate impacts', 'Design adaptation strategies'],
    audience: 'Environmental practitioners, planners, policy analysts'
  },
  {
    id: 'environmental-justice-101',
    number: 20,
    title: 'Environmental Justice 101',
    description: 'Intersection of environmental issues and social justice.',
    category: 'Environment',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-leaf',
    url: 'https://101.www.impactmojo.in/env-jus',
    learnerCount: 987,
    rating: 4.3,
    prerequisites: ['Climate Science 101'],
    outcomes: ['Apply justice frameworks', 'Analyze environmental inequities', 'Design just solutions'],
    audience: 'Environmental activists, policy analysts, community workers'
  },

  // EDUCATION
  {
    id: 'education-pedagogy-101',
    number: 21,
    title: 'Education and Pedagogy 101',
    description: 'Educational theory and practice for development contexts.',
    category: 'Education',
    difficulty: 'beginner',
    duration: '3-4 hours',
    icon: 'fas fa-graduation-cap',
    url: 'https://101.www.impactmojo.in/edu',
    learnerCount: 1456,
    rating: 4.5,
    prerequisites: ['None - foundational course'],
    outcomes: ['Apply pedagogical principles', 'Design educational programs', 'Evaluate learning outcomes'],
    audience: 'Educators, program managers, curriculum developers'
  },

  // LIVELIHOODS
  {
    id: 'livelihoods-101',
    number: 22,
    title: 'Livelihoods 101',
    description: 'Sustainable livelihoods approaches and rural development strategies.',
    category: 'Livelihoods',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-seedling',
    url: 'https://101.www.impactmojo.in/Livelihoods',
    learnerCount: 1678,
    rating: 4.6,
    prerequisites: ['None - foundational course'],
    outcomes: ['Apply livelihoods frameworks', 'Design livelihood interventions', 'Measure livelihood outcomes'],
    audience: 'Rural development practitioners, program managers, livelihood specialists'
  },
  {
    id: 'decent-work-101',
    number: 23,
    title: 'Decent Work for All 101',
    description: 'ILO frameworks for promoting decent work and labor rights.',
    category: 'Livelihoods',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-hard-hat',
    url: 'https://101.www.impactmojo.in/DecentWork',
    learnerCount: 1123,
    rating: 4.4,
    prerequisites: ['Livelihoods 101'],
    outcomes: ['Apply decent work principles', 'Design employment programs', 'Monitor labor conditions'],
    audience: 'Labor specialists, program managers, policy analysts'
  },

  // GOVERNANCE & RIGHTS
  {
    id: 'law-constitution-101',
    number: 24,
    title: 'Law & Constitution 101',
    description: 'Understanding legal frameworks and constitutional provisions for development.',
    category: 'Governance',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-gavel',
    url: 'https://101.www.impactmojo.in/Law&Cons',
    learnerCount: 1234,
    rating: 4.3,
    prerequisites: ['None - foundational course'],
    outcomes: ['Understand legal frameworks', 'Apply rights-based approaches', 'Navigate legal systems'],
    audience: 'Legal practitioners, rights advocates, policy analysts'
  },
  {
    id: 'identities-101',
    number: 25,
    title: 'Identities 101',
    description: 'Understanding identity, intersectionality, and social categorization.',
    category: 'Social Theory',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-users',
    url: 'https://101.www.impactmojo.in/identities',
    learnerCount: 976,
    rating: 4.5,
    prerequisites: ['Gender Studies 101'],
    outcomes: ['Analyze identity formation', 'Apply intersectional analysis', 'Design inclusive programs'],
    audience: 'Social researchers, program managers, community workers'
  },

  // COMMUNICATION & ADVOCACY
  {
    id: 'advocacy-communication-101',
    number: 26,
    title: 'Advocacy & Communication 101',
    description: 'Strategic communication and advocacy for social change.',
    category: 'Communication',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-bullhorn',
    url: 'https://101.www.impactmojo.in/adv&comm',
    learnerCount: 1345,
    rating: 4.4,
    prerequisites: ['None - foundational course'],
    outcomes: ['Design advocacy campaigns', 'Develop communication strategies', 'Engage stakeholders'],
    audience: 'Advocates, communication specialists, program managers'
  },
  {
    id: 'post-truth-politics-101',
    number: 27,
    title: 'Post-Truth Politics 101',
    description: 'Understanding misinformation, propaganda, and post-truth politics.',
    category: 'Communication',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-eye',
    url: 'https://101.www.impactmojo.in/post-truth-pol',
    learnerCount: 876,
    rating: 4.2,
    prerequisites: ['Advocacy & Communication 101'],
    outcomes: ['Identify misinformation', 'Develop fact-checking skills', 'Counter false narratives'],
    audience: 'Journalists, advocates, political analysts'
  },

  // COMMUNITY DEVELOPMENT
  {
    id: 'community-development-101',
    number: 28,
    title: 'Community Development 101',
    description: 'Participatory approaches to community-led development.',
    category: 'Community Development',
    difficulty: 'beginner',
    duration: '3-4 hours',
    icon: 'fas fa-hands-helping',
    url: 'https://101.www.impactmojo.in/community-dev',
    learnerCount: 1567,
    rating: 4.6,
    prerequisites: ['None - foundational course'],
    outcomes: ['Apply participatory methods', 'Facilitate community processes', 'Build local capacity'],
    audience: 'Community workers, program managers, grassroots organizers'
  },

  // TECHNOLOGY & ETHICS
  {
    id: 'digital-ethics-101',
    number: 29,
    title: 'Digital Ethics 101',
    description: 'Ethical considerations in digital technology and data use.',
    category: 'Technology',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    icon: 'fas fa-shield-alt',
    url: 'https://101.www.impactmojo.in/DigitalEthics',
    learnerCount: 789,
    rating: 4.1,
    prerequisites: ['Data Literacy 101'],
    outcomes: ['Apply digital ethics frameworks', 'Protect privacy and data', 'Design ethical tech solutions'],
    audience: 'Tech practitioners, data scientists, digital rights advocates'
  },

  // FUNDRAISING & RESOURCE MOBILIZATION
  {
    id: 'fundraising-101',
    number: 30,
    title: 'Fundraising 101',
    description: 'Strategies and techniques for nonprofit fundraising and resource mobilization.',
    category: 'Organizational Development',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-hand-holding-usd',
    url: 'https://101.www.impactmojo.in/fundraising',
    learnerCount: 1234,
    rating: 4.3,
    prerequisites: ['None - foundational course'],
    outcomes: ['Develop fundraising strategies', 'Write grant proposals', 'Build donor relationships'],
    audience: 'Nonprofit leaders, program managers, development officers'
  },

  // DECOLONIAL DEVELOPMENT
  {
    id: 'decolonial-development-101',
    number: 31,
    title: 'Decolonial Development 101',
    description: 'Critical perspectives on development practice and decolonial alternatives.',
    category: 'Critical Theory',
    difficulty: 'advanced',
    duration: '5-6 hours',
    icon: 'fas fa-fist-raised',
    url: 'https://101.www.impactmojo.in/decolonD',
    learnerCount: 654,
    rating: 4.4,
    prerequisites: ['Development Economics 101', 'Political Economy 101'],
    outcomes: ['Apply decolonial frameworks', 'Critique development paradigms', 'Design alternative approaches'],
    audience: 'Critical development scholars, activists, advanced practitioners'
  },

  // Additional courses to complete the 33 courses
  {
    id: 'behaviour-change-101',
    number: 33,
    title: 'Behaviour Change & Communication for Programs',
    description: 'Applying behavioral science and communication strategies in development programs.',
    category: 'Communication',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    icon: 'fas fa-brain',
    url: 'https://101.www.impactmojo.in/BCCP',
    learnerCount: 987,
    rating: 4.2,
    prerequisites: ['Advocacy & Communication 101'],
    outcomes: ['Apply behavioral insights', 'Design behavior change interventions', 'Measure behavior change'],
    audience: 'Program managers, communication specialists, behavioral scientists'
  },
  {
    id: 'gender-data-architecture-101',
    number: 34,
    title: 'Global Development Architecture 101',
    description: 'Understanding global development systems, institutions, and architecture.',
    category: 'Development Systems',
    difficulty: 'advanced',
    duration: '5-6 hours',
    icon: 'fas fa-globe',
    url: 'https://101.www.impactmojo.in/GDArch',
    learnerCount: 543,
    rating: 4.5,
    prerequisites: ['Development Economics 101', 'Political Economy 101'],
    outcomes: ['Understand global development architecture', 'Analyze institutional frameworks', 'Navigate development systems'],
    audience: 'Development practitioners, policy analysts, international development specialists'
  }
];

// UPCOMING COURSES (For reference in upcoming section)
const upcomingCourses = [
  {
    id: 'tall-101',
    title: 'TALL (Technology for ALL) 101',
    description: 'Technology literacy platform covering 10 future technologies: IoT, AI, Robotics, Blockchain, Cryptocurrency, Cybercrime, Digital Transformation, Telehealth, Edutech & Metaworld. Designed for all internet and mobile users in simple, jargon-free language.',
    category: 'Technology',
    difficulty: 'beginner',
    duration: '32 classes (45 min each)',
    icon: 'fas fa-microchip',
    status: 'coming-soon',
    learnerCount: 0,
    rating: 0,
    prerequisites: ['Basic internet/mobile usage', 'English comprehension'],
    outcomes: ['Understand 10 future technologies', 'Apply technology concepts', 'Build digital literacy'],
    audience: 'All internet users, non-engineers, students, professionals seeking tech literacy'
  }
];

// LABS DATA - ALL 9 LABS WITH CORRECTED NETLIFY URLS
const labs = [
  {
    id: 'toc-workbench',
    title: 'TOC Workbench',
    description: 'Create, visualize, and share your intervention logic models.',
    icon: 'fas fa-tools',
    status: 'live',
    url: 'https://toc-workbench.netlify.app/',
    category: 'Planning Tools'
  },
  {
    id: 'risk-mitigation-lab',
    title: 'Risk Mitigation Lab',
    description: 'Identify and plan for potential risks in development projects.',
    icon: 'fas fa-shield-alt',
    status: 'live',
    url: 'https://impactrisk-mitigation.netlify.app/',
    category: 'Risk Management'
  },
  {
    id: 'mel-framework-designer',
    title: 'MEL Framework Designer',
    description: 'Design comprehensive monitoring, evaluation, and learning frameworks.',
    icon: 'fas fa-chart-line',
    status: 'live',
    url: 'https://mel-toolkit.netlify.app/',
    category: 'Monitoring & Evaluation'
  },
  {
    id: 'gender-budget-tracker',
    title: 'Gender Budget Tracker',
    description: 'Track and analyze gender-responsive budgeting and expenditure.',
    icon: 'fas fa-calculator',
    status: 'live',
    url: 'https://gender-budget-tracker.netlify.app/',
    category: 'Gender & Finance'
  },
  {
    id: 'stakeholder-mapper',
    title: 'Stakeholder Mapper',
    description: 'Map and analyze project stakeholders and their relationships.',
    icon: 'fas fa-sitemap',
    status: 'live',
    url: 'https://stakeholder-mapper.netlify.app/',
    category: 'Project Management'
  },
  {
    id: 'impact-calculator',
    title: 'Impact Calculator',
    description: 'Calculate and visualize program impact using standard metrics.',
    icon: 'fas fa-calculator',
    status: 'live',
    url: 'https://impact-calculator.netlify.app/',
    category: 'Impact Measurement'
  },
  {
    id: 'community-feedback-analyzer',
    title: 'Community Feedback Analyzer',
    description: 'Analyze qualitative feedback from community consultations.',
    icon: 'fas fa-comments',
    status: 'live',
    url: 'https://community-feedback-analyzer.netlify.app/',
    category: 'Community Engagement'
  },
  {
    id: 'policy-brief-generator',
    title: 'Policy Brief Generator',
    description: 'Generate structured policy briefs and recommendations.',
    icon: 'fas fa-file-alt',
    status: 'live',
    url: 'https://policy-brief-generator.netlify.app/',
    category: 'Policy Analysis'
  },
  {
    id: 'survey-designer',
    title: 'Survey Designer',
    description: 'Design surveys with best practices for development research.',
    icon: 'fas fa-poll',
    status: 'live',
    url: 'https://survey-designer.netlify.app/',
    category: 'Research Tools'
  }
];

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { courses, upcomingCourses, labs };
}