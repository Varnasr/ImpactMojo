// ImpactMojo Complete Course Data
// ALL 33+ courses, 9 labs, and additional resources

const courses = [
  // DATA ANALYSIS TRACK
  {
    id: 'data-feminism-101',
    title: 'Data Feminism 101',
    description: 'Challenges dominant data narratives using feminist theory. Covers intersectionality, visibility, and the politics of knowledge in South Asian development.',
    category: 'Data Analysis',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    tags: ['feminism', 'data', 'intersectionality'],
    url: 'https://101.www.impactmojo.in/DataFeminism',
    featured: true,
    learnerCount: 2847,
    rating: 4.8,
    prerequisites: ['Basic data literacy', 'Interest in gender studies'],
    outcomes: ['Apply feminist lens to data analysis', 'Identify bias in datasets', 'Design inclusive data collection'],
    audience: 'Data scientists, researchers, gender advocates'
  },
  {
    id: 'data-literacy-101',
    title: 'Data Literacy 101',
    description: 'Foundational skills for understanding and working with data in development contexts.',
    category: 'Data Analysis',
    difficulty: 'beginner',
    duration: '3-4 hours',
    tags: ['data', 'literacy', 'fundamentals'],
    url: 'https://101.www.impactmojo.in/DataLiteracy',
    featured: true,
    learnerCount: 1734,
    rating: 4.9,
    prerequisites: ['None - foundational course'],
    outcomes: ['Understand data concepts', 'Read data visualizations', 'Ask good questions of data'],
    audience: 'Beginners, development practitioners, program managers'
  },
  {
    id: 'eda-survey-data',
    title: 'EDA for Survey Data',
    description: 'Exploratory Data Analysis techniques specifically for household and survey datasets.',
    category: 'Data Analysis',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['eda', 'survey', 'analysis'],
    url: 'https://101.www.impactmojo.in/EDAForSurveyData',
    featured: true,
    learnerCount: 2156,
    rating: 4.7,
    prerequisites: ['Data Literacy 101', 'Basic statistics'],
    outcomes: ['Conduct exploratory data analysis', 'Clean survey data', 'Identify patterns and anomalies'],
    audience: 'Researchers, data analysts, program evaluators'
  },
  {
    id: 'bivariate-analysis-101',
    title: 'Bivariate Analysis 101',
    description: 'Master relationships between variables using correlation, regression, and statistical tests. Features real South Asian datasets and development applications.',
    category: 'Data Analysis',
    difficulty: 'intermediate',
    duration: '5-6 hours',
    tags: ['statistics', 'relationships', 'correlation'],
    url: 'https://101.www.impactmojo.in/BivariateAnalysis',
    learnerCount: 1445,
    rating: 4.5,
    prerequisites: ['EDA for Survey Data', 'Statistical foundations'],
    outcomes: ['Analyze variable relationships', 'Interpret correlation coefficients', 'Conduct regression analysis'],
    audience: 'Researchers, data analysts, monitoring & evaluation specialists'
  },
  {
    id: 'multivariate-analysis-101',
    title: 'Multivariate Analysis 101',
    description: 'Advanced statistical techniques for analyzing multiple variables simultaneously.',
    category: 'Data Analysis',
    difficulty: 'advanced',
    duration: '5-6 hours',
    tags: ['statistics', 'multivariate', 'advanced'],
    url: 'https://101.www.impactmojo.in/MultivariateAnalysis',
    learnerCount: 1234,
    rating: 4.6,
    prerequisites: ['Bivariate Analysis 101', 'Statistical software experience'],
    outcomes: ['Conduct multivariate analysis', 'Interpret complex models', 'Control for confounding variables'],
    audience: 'Advanced researchers, data scientists, policy analysts'
  },

  // ECONOMICS TRACK
  {
    id: 'development-economics-101',
    title: 'Development Economics 101',
    description: 'Core principles of development economics with South Asian examples and case studies.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['economics', 'development', 'policy'],
    url: 'https://101.www.impactmojo.in/DevelopmentEconomics',
    learnerCount: 1889,
    rating: 4.4,
    prerequisites: ['Basic economics knowledge'],
    outcomes: ['Understand development theories', 'Analyze economic policies', 'Apply economic frameworks'],
    audience: 'Policy makers, economists, development practitioners'
  },
  {
    id: 'behavioral-economics-101',
    title: 'Behavioral Economics 101',
    description: 'How psychological insights improve program design and policy effectiveness in development contexts.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    tags: ['behavioral economics', 'psychology', 'nudges'],
    url: 'https://101.www.impactmojo.in/BehavioralEconomics',
    learnerCount: 1267,
    rating: 4.3,
    prerequisites: ['Development Economics 101'],
    outcomes: ['Apply behavioral insights', 'Design effective interventions', 'Understand decision-making biases'],
    audience: 'Program designers, policy makers, behavioral researchers'
  },

  // GENDER STUDIES TRACK
  {
    id: 'gender-studies-101',
    title: 'Gender Studies 101',
    description: 'Foundational concepts in gender studies with applications to South Asian development contexts.',
    category: 'Gender Studies',
    difficulty: 'beginner',
    duration: '3-4 hours',
    tags: ['gender', 'feminism', 'intersectionality'],
    url: 'https://101.www.impactmojo.in/GenderStudies',
    featured: true,
    learnerCount: 2341,
    rating: 4.7,
    prerequisites: ['None - foundational course'],
    outcomes: ['Understand gender concepts', 'Apply intersectional analysis', 'Design gender-sensitive programs'],
    audience: 'Development practitioners, social workers, policy makers'
  },
  {
    id: 'care-economy-101',
    title: 'Care Economy 101',
    description: 'Understanding unpaid care work and its implications for economic development and gender equality.',
    category: 'Gender Studies',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['care economy', 'unpaid work', 'gender'],
    url: 'https://101.www.impactmojo.in/CareEconomy',
    learnerCount: 1523,
    rating: 4.6,
    prerequisites: ['Gender Studies 101'],
    outcomes: ['Measure care work', 'Design care-responsive policies', 'Analyze time use data'],
    audience: 'Gender specialists, economists, policy researchers'
  },
  {
    id: 'womens-economic-empowerment-101',
    title: 'Women\'s Economic Empowerment 101',
    description: 'Strategies and frameworks for promoting women\'s economic participation and empowerment.',
    category: 'Gender Studies',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['women empowerment', 'economic participation', 'livelihoods'],
    url: 'https://101.www.impactmojo.in/WomensEconomicEmpowerment',
    learnerCount: 1834,
    rating: 4.5,
    prerequisites: ['Gender Studies 101', 'Development Economics 101'],
    outcomes: ['Design empowerment programs', 'Measure economic outcomes', 'Address structural barriers'],
    audience: 'Program managers, gender specialists, livelihood practitioners'
  },

  // HEALTH TRACK
  {
    id: 'public-health-101',
    title: 'Public Health 101',
    description: 'Foundational concepts in public health with focus on South Asian health systems and challenges.',
    category: 'Health',
    difficulty: 'beginner',
    duration: '3-4 hours',
    tags: ['public health', 'health systems', 'epidemiology'],
    url: 'https://101.www.impactmojo.in/PublicHealth',
    featured: true,
    learnerCount: 1945,
    rating: 4.4,
    prerequisites: ['None - foundational course'],
    outcomes: ['Understand health determinants', 'Analyze health data', 'Design health interventions'],
    audience: 'Health practitioners, public health students, program managers'
  },
  {
    id: 'mental-health-101',
    title: 'Mental Health 101',
    description: 'Understanding mental health challenges and interventions in South Asian contexts.',
    category: 'Health',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    tags: ['mental health', 'psychosocial', 'wellbeing'],
    url: 'https://101.www.impactmojo.in/MentalHealth',
    learnerCount: 1234,
    rating: 4.3,
    prerequisites: ['Public Health 101'],
    outcomes: ['Identify mental health needs', 'Design psychosocial interventions', 'Reduce stigma'],
    audience: 'Health workers, social workers, counselors'
  },
  {
    id: 'nutrition-food-security-101',
    title: 'Nutrition and Food Security 101',
    description: 'Comprehensive overview of nutrition challenges and food security interventions.',
    category: 'Health',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['nutrition', 'food security', 'malnutrition'],
    url: 'https://101.www.impactmojo.in/NutritionFoodSecurity',
    learnerCount: 1567,
    rating: 4.5,
    prerequisites: ['Public Health 101'],
    outcomes: ['Assess nutritional status', 'Design nutrition programs', 'Address food insecurity'],
    audience: 'Nutrition specialists, health practitioners, program managers'
  },
  {
    id: 'srhr-101',
    title: 'Sexual and Reproductive Health and Rights (SRHR) 101',
    description: 'Comprehensive approach to sexual and reproductive health programming and advocacy.',
    category: 'Health',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['SRHR', 'reproductive health', 'rights'],
    url: 'https://101.www.impactmojo.in/SRHR',
    learnerCount: 1123,
    rating: 4.4,
    prerequisites: ['Public Health 101', 'Gender Studies 101'],
    outcomes: ['Design SRHR programs', 'Advocate for reproductive rights', 'Address health inequities'],
    audience: 'Health practitioners, gender specialists, advocates'
  },

  // IDENTITY & JUSTICE TRACK
  {
    id: 'social-safety-nets-101',
    title: 'Social Safety Nets 101',
    description: 'Unpacks India\'s welfare architecture—PDS, NREGA, pensions—through lifecycle needs and exclusion errors.',
    category: 'Identity & Justice',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['social protection', 'welfare', 'policy'],
    url: 'https://101.www.impactmojo.in/SocialSafetyNets',
    featured: true,
    learnerCount: 1923,
    rating: 4.6,
    prerequisites: ['Basic understanding of public policy'],
    outcomes: ['Analyze welfare programs', 'Identify exclusion patterns', 'Design inclusive safety nets'],
    audience: 'Policy researchers, development practitioners, social workers'
  },
  {
    id: 'caste-development-101',
    title: 'Caste and Development 101',
    description: 'Understanding how caste intersects with development outcomes and program design.',
    category: 'Identity & Justice',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['caste', 'social justice', 'intersectionality'],
    url: 'https://101.www.impactmojo.in/CasteDevelopment',
    learnerCount: 1345,
    rating: 4.5,
    prerequisites: ['Social Safety Nets 101'],
    outcomes: ['Analyze caste-based discrimination', 'Design inclusive programs', 'Address structural inequities'],
    audience: 'Social justice advocates, program designers, researchers'
  },
  {
    id: 'disability-inclusion-101',
    title: 'Disability Inclusion 101',
    description: 'Principles and practices for designing disability-inclusive development programs.',
    category: 'Identity & Justice',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    tags: ['disability', 'inclusion', 'accessibility'],
    url: 'https://101.www.impactmojo.in/DisabilityInclusion',
    learnerCount: 987,
    rating: 4.3,
    prerequisites: ['None - standalone course'],
    outcomes: ['Apply universal design principles', 'Conduct accessibility audits', 'Design inclusive programs'],
    audience: 'Program managers, accessibility specialists, advocates'
  },

  // CLIMATE & ENVIRONMENT
  {
    id: 'climate-adaptation-101',
    title: 'Climate Adaptation 101',
    description: 'Strategies for building climate resilience in vulnerable communities.',
    category: 'Climate & Environment',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['climate change', 'adaptation', 'resilience'],
    url: 'https://101.www.impactmojo.in/ClimateAdaptation',
    learnerCount: 1456,
    rating: 4.4,
    prerequisites: ['Basic environmental knowledge'],
    outcomes: ['Assess climate risks', 'Design adaptation strategies', 'Build community resilience'],
    audience: 'Environmental practitioners, climate specialists, community workers'
  },
  {
    id: 'sustainable-livelihoods-101',
    title: 'Sustainable Livelihoods 101',
    description: 'Livelihood frameworks and approaches for sustainable development programming.',
    category: 'Climate & Environment',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['livelihoods', 'sustainability', 'rural development'],
    url: 'https://101.www.impactmojo.in/SustainableLivelihoods',
    learnerCount: 1678,
    rating: 4.5,
    prerequisites: ['Climate Adaptation 101'],
    outcomes: ['Apply livelihood frameworks', 'Design sustainable programs', 'Build resilient livelihoods'],
    audience: 'Rural development practitioners, livelihood specialists, program managers'
  },

  // URBAN & SYSTEMS
  {
    id: 'urban-governance-101',
    title: 'Urban Governance 101',
    description: 'Understanding urban governance challenges and participatory planning approaches.',
    category: 'Urban & Systems',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['urban planning', 'governance', 'participation'],
    url: 'https://101.www.impactmojo.in/UrbanGovernance',
    learnerCount: 1234,
    rating: 4.3,
    prerequisites: ['Basic governance concepts'],
    outcomes: ['Analyze urban challenges', 'Design participatory processes', 'Strengthen urban governance'],
    audience: 'Urban planners, governance specialists, municipal officials'
  },
  {
    id: 'systems-thinking-101',
    title: 'Systems Thinking 101',
    description: 'Systems approaches to understanding and addressing complex development challenges.',
    category: 'Urban & Systems',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    tags: ['systems thinking', 'complexity', 'design'],
    url: 'https://101.www.impactmojo.in/SystemsThinking',
    featured: true,
    learnerCount: 1678,
    rating: 4.5,
    prerequisites: ['None - foundational course'],
    outcomes: ['Apply systems thinking tools', 'Map system relationships', 'Design systems interventions'],
    audience: 'Program managers, policy makers, development practitioners'
  },

  // EDUCATION
  {
    id: 'education-pedagogy-101',
    title: 'Education and Pedagogy 101',
    description: 'Progressive education approaches and pedagogical innovations for equitable learning.',
    category: 'Education',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['education', 'pedagogy', 'learning'],
    url: 'https://101.www.impactmojo.in/EducationPedagogy',
    learnerCount: 1789,
    rating: 4.4,
    prerequisites: ['None - foundational course'],
    outcomes: ['Apply progressive pedagogy', 'Design inclusive curricula', 'Assess learning outcomes'],
    audience: 'Educators, curriculum designers, education researchers'
  },
  {
    id: 'digital-literacy-education-101',
    title: 'Digital Literacy in Education 101',
    description: 'Integrating digital technologies effectively in educational programming.',
    category: 'Education',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    tags: ['digital literacy', 'technology', 'education'],
    url: 'https://101.www.impactmojo.in/DigitalLiteracyEducation',
    learnerCount: 1345,
    rating: 4.2,
    prerequisites: ['Education and Pedagogy 101'],
    outcomes: ['Integrate digital tools', 'Design online learning', 'Build digital competencies'],
    audience: 'Educators, technology specialists, program managers'
  },

  // RESEARCH METHODS
  {
    id: 'research-ethics-101',
    title: 'Research Ethics 101',
    description: 'Ethical principles and practices for conducting research in development contexts.',
    category: 'Research Methods',
    difficulty: 'beginner',
    duration: '2-3 hours',
    tags: ['research ethics', 'consent', 'protection'],
    url: 'https://101.www.impactmojo.in/ResearchEthics',
    learnerCount: 1567,
    rating: 4.6,
    prerequisites: ['None - foundational course'],
    outcomes: ['Apply ethical principles', 'Design consent processes', 'Protect research participants'],
    audience: 'Researchers, graduate students, evaluators'
  },
  {
    id: 'qualitative-research-101',
    title: 'Qualitative Research 101',
    description: 'Methods and approaches for conducting rigorous qualitative research.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '5-6 hours',
    tags: ['qualitative research', 'interviews', 'analysis'],
    url: 'https://101.www.impactmojo.in/QualitativeResearch',
    featured: true,
    learnerCount: 2234,
    rating: 4.7,
    prerequisites: ['Research Ethics 101'],
    outcomes: ['Conduct qualitative interviews', 'Analyze qualitative data', 'Write research findings'],
    audience: 'Researchers, evaluators, graduate students'
  },
  {
    id: 'econometrics-101',
    title: 'Econometrics 101',
    description: 'Statistical methods for causal inference and impact evaluation in development contexts.',
    category: 'Research Methods',
    difficulty: 'advanced',
    duration: '6-8 hours',
    tags: ['econometrics', 'statistics', 'causal inference'],
    url: 'https://101.www.impactmojo.in/Econometrics',
    learnerCount: 1234,
    rating: 4.7,
    prerequisites: ['Multivariate Analysis 101', 'Research design knowledge'],
    outcomes: ['Conduct impact evaluations', 'Apply causal inference methods', 'Interpret econometric results'],
    audience: 'Advanced researchers, economists, impact evaluators'
  },
  {
    id: 'mel-101',
    title: 'Monitoring, Evaluation & Learning (MEL) 101',
    description: 'Frameworks and tools for effective program monitoring and evaluation in development contexts.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '5-6 hours',
    tags: ['MEL', 'evaluation', 'monitoring'],
    url: 'https://101.www.impactmojo.in/MEL',
    featured: true,
    learnerCount: 1678,
    rating: 4.5,
    prerequisites: ['Research Ethics 101'],
    outcomes: ['Design MEL frameworks', 'Conduct evaluations', 'Use data for learning'],
    audience: 'M&E specialists, program managers, donors'
  },
  {
    id: 'visual-ethnography-101',
    title: 'Visual Ethnography and Storytelling 101',
    description: 'Participatory photography, visual documentation ethics, and representation frameworks.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    tags: ['visual ethnography', 'photography', 'storytelling'],
    url: 'https://101.www.impactmojo.in/VisualEthnography',
    learnerCount: 445,
    rating: 4.1,
    prerequisites: ['Qualitative Research 101'],
    outcomes: ['Use visual methods', 'Conduct ethical documentation', 'Create compelling narratives'],
    audience: 'Researchers, documentary makers, communication specialists'
  },

  // TECHNOLOGY
  {
    id: 'digital-development-ethics-101',
    title: 'Digital Development Ethics 101',
    description: 'Ethical frameworks for technology use in development programming.',
    category: 'Technology',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    tags: ['digital ethics', 'technology', 'privacy'],
    url: 'https://101.www.impactmojo.in/DigitalDevelopmentEthics',
    learnerCount: 987,
    rating: 4.3,
    prerequisites: ['Basic technology understanding'],
    outcomes: ['Apply ethical frameworks', 'Design responsible tech', 'Protect digital rights'],
    audience: 'Tech practitioners, program managers, digital rights advocates'
  },
  {
    id: 'data-protection-101',
    title: 'Data Protection and Privacy 101',
    description: 'Understanding data protection laws and implementing privacy-by-design in development programs.',
    category: 'Technology',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    tags: ['data protection', 'privacy', 'GDPR'],
    url: 'https://101.www.impactmojo.in/DataProtection',
    learnerCount: 756,
    rating: 4.2,
    prerequisites: ['Digital Development Ethics 101'],
    outcomes: ['Comply with data laws', 'Implement privacy measures', 'Conduct data audits'],
    audience: 'Data managers, compliance officers, program managers'
  },

  // SPECIALIZED COURSES
  {
    id: 'impact-measurement-101',
    title: 'Impact Measurement 101',
    description: 'Methods and tools for measuring social and economic impact in development programs.',
    category: 'Research Methods',
    difficulty: 'advanced',
    duration: '5-6 hours',
    tags: ['impact', 'measurement', 'evaluation'],
    url: 'https://101.www.impactmojo.in/ImpactMeasurement',
    learnerCount: 1123,
    rating: 4.6,
    prerequisites: ['MEL 101', 'Statistics knowledge'],
    outcomes: ['Design impact measurement systems', 'Collect impact data', 'Report on outcomes'],
    audience: 'Impact specialists, evaluators, donors'
  },
  {
    id: 'participatory-approaches-101',
    title: 'Participatory Approaches 101',
    description: 'Methods for meaningful community participation in development programming.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['participation', 'community', 'engagement'],
    url: 'https://101.www.impactmojo.in/ParticipatoryApproaches',
    learnerCount: 1345,
    rating: 4.4,
    prerequisites: ['Systems Thinking 101'],
    outcomes: ['Facilitate participatory processes', 'Build community ownership', 'Ensure inclusive participation'],
    audience: 'Community workers, facilitators, program managers'
  },
  {
    id: 'financial-inclusion-101',
    title: 'Financial Inclusion 101',
    description: 'Strategies for expanding access to financial services for underserved populations.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    tags: ['financial inclusion', 'microfinance', 'fintech'],
    url: 'https://101.www.impactmojo.in/FinancialInclusion',
    learnerCount: 1456,
    rating: 4.3,
    prerequisites: ['Development Economics 101'],
    outcomes: ['Design financial products', 'Assess financial needs', 'Promote digital payments'],
    audience: 'Financial inclusion specialists, microfinance practitioners, fintech developers'
  }
];

// ImpactMojo Labs - All 9 Labs
const labs = [
  {
    id: 'toc-workbench',
    title: 'TOC Workbench',
    description: 'Create, visualize, and share your intervention logic models.',
    icon: 'fas fa-tools',
    status: 'live',
    url: 'https://toc-workbench.netlify.app/',
    category: 'Planning Tools',
    users: 2341,
    lastUpdated: '2 days ago'
  },
  {
    id: 'risk-mitigation-lab',
    title: 'Risk Mitigation Lab',
    description: 'Identify and plan for potential risks in development projects.',
    icon: 'fas fa-shield-alt',
    status: 'live',
    url: 'https://impactrisk-mitigation.netlify.app/',
    category: 'Risk Management',
    users: 1567,
    lastUpdated: '1 week ago'
  },
  {
    id: 'mel-framework-designer',
    title: 'MEL Framework Designer',
    description: 'Design comprehensive monitoring, evaluation, and learning frameworks.',
    icon: 'fas fa-cogs',
    status: 'live',
    url: 'https://mle-frameworkdesign.netlify.app/',
    category: 'MEL Tools',
    users: 1834,
    lastUpdated: '3 days ago'
  },
  {
    id: 'mel-planning-lab',
    title: 'MEL Planning Lab',
    description: 'Create detailed monitoring and evaluation plans for your projects.',
    icon: 'fas fa-project-diagram',
    status: 'live',
    url: 'https://mle-plan-lab.netlify.app/',
    category: 'MEL Tools',
    users: 1234,
    lastUpdated: '5 days ago'
  },
  {
    id: 'resource-mobilization-lab',
    title: 'Resource Mobilization Lab',
    description: 'Develop strategies for sustainable funding and resource mobilization.',
    icon: 'fas fa-hand-holding-usd',
    status: 'live',
    url: 'https://rm-sustainability4impact.netlify.app/',
    category: 'Fundraising',
    users: 987,
    lastUpdated: '1 week ago'
  },
  {
    id: 'policy-advocacy-lab',
    title: 'Policy & Advocacy Lab',
    description: 'Build effective advocacy strategies and policy recommendations.',
    icon: 'fas fa-gavel',
    status: 'live',
    url: 'https://pol-advocacy4impact.netlify.app/',
    category: 'Advocacy',
    users: 1456,
    lastUpdated: '4 days ago'
  },
  {
    id: 'community-engagement-lab',
    title: 'Community Engagement Lab',
    description: 'Tools and frameworks for meaningful community engagement and participation.',
    icon: 'fas fa-users',
    status: 'live',
    url: 'https://community-engagement-lab.netlify.app/',
    category: 'Community Work',
    users: 1123,
    lastUpdated: '1 week ago'
  },
  {
    id: 'survey-design-lab',
    title: 'Survey Design Lab',
    description: 'Interactive tool for designing surveys and questionnaires for development research.',
    icon: 'fas fa-clipboard-list',
    status: 'live',
    url: 'https://survey-design-lab.netlify.app/',
    category: 'Research Tools',
    users: 2156,
    lastUpdated: '2 days ago'
  },
  {
    id: 'data-visualization-lab',
    title: 'Data Visualization Lab',
    description: 'Create compelling data visualizations and infographics for development data.',
    icon: 'fas fa-chart-pie',
    status: 'live',
    url: 'https://dataviz-lab.netlify.app/',
    category: 'Data Tools',
    users: 1789,
    lastUpdated: '6 days ago'
  }
];

// Learning paths
const learningPaths = {
  'data-analysis': {
    name: 'Data Analysis Track',
    description: 'Master data skills from basics to advanced analysis',
    icon: 'fas fa-chart-bar',
    courses: ['data-literacy-101', 'data-feminism-101', 'eda-survey-data', 'bivariate-analysis-101', 'multivariate-analysis-101'],
    color: '#3498db'
  },
  'gender-studies': {
    name: 'Gender Studies Pathway',
    description: 'Comprehensive understanding of gender in development',
    icon: 'fas fa-venus',
    courses: ['gender-studies-101', 'data-feminism-101', 'care-economy-101', 'womens-economic-empowerment-101'],
    color: '#e74c3c'
  },
  'research-methods': {
    name: 'Research Methods Journey',
    description: 'Complete research toolkit for development work',
    icon: 'fas fa-flask',
    courses: ['research-ethics-101', 'qualitative-research-101', 'econometrics-101', 'mel-101'],
    color: '#8e44ad'
  },
  'health': {
    name: 'Health Systems Track',
    description: 'Public health and health system strengthening',
    icon: 'fas fa-heartbeat',
    courses: ['public-health-101', 'mental-health-101', 'nutrition-food-security-101', 'srhr-101'],
    color: '#27ae60'
  }
};

// Categories for course filtering
const categories = [
  'All Courses',
  'Data Analysis',
  'Economics',
  'Gender Studies',
  'Health',
  'Identity & Justice',
  'Climate & Environment',
  'Urban & Systems',
  'Education',
  'Research Methods',
  'Technology'
];

// Additional resources
const additionalResources = {
  handouts: [
    { title: 'Data Analysis Cheat Sheet', url: 'handouts/data-analysis-cheat-sheet.pdf' },
    { title: 'Gender Mainstreaming Checklist', url: 'handouts/gender-mainstreaming-checklist.pdf' },
    { title: 'MEL Framework Template', url: 'handouts/mel-framework-template.xlsx' }
  ],
  datasets: [
    { title: 'India Development Indicators', url: 'data/india-development-indicators.csv' },
    { title: 'Gender Equality Index Data', url: 'data/gender-equality-index.csv' },
    { title: 'Health System Performance Data', url: 'data/health-system-performance.csv' }
  ],
  tools: [
    { title: 'Logic Model Template', url: 'tools/logic-model-template.pptx' },
    { title: 'Survey Design Checklist', url: 'tools/survey-design-checklist.pdf' },
    { title: 'Stakeholder Mapping Tool', url: 'tools/stakeholder-mapping-tool.xlsx' }
  ]
};

// Utility Functions
function getCourseById(id) {
  return courses.find(course => course.id === id);
}

function getCoursesByCategory(category) {
  if (category === 'All Courses') return courses;
  return courses.filter(course => course.category === category);
}

function getCoursesByDifficulty(difficulty) {
  return courses.filter(course => course.difficulty === difficulty);
}

function getFeaturedCourses() {
  return courses.filter(course => course.featured);
}

function getCoursesByPath(pathId) {
  const path = learningPaths[pathId];
  if (!path) return [];
  return path.courses.map(courseId => getCourseById(courseId)).filter(Boolean);
}

function searchCourses(query) {
  const searchTerm = query.toLowerCase();
  return courses.filter(course => 
    course.title.toLowerCase().includes(searchTerm) ||
    course.description.toLowerCase().includes(searchTerm) ||
    course.tags.some(tag => tag.toLowerCase().includes(searchTerm))
  );
}

function getLabById(id) {
  return labs.find(lab => lab.id === id);
}

function getLabsByStatus(status) {
  return labs.filter(lab => lab.status === status);
}

function getLiveLabs() {
  return getLabsByStatus('live');
}

function getComingSoonLabs() {
  return getLabsByStatus('coming-soon');
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    courses,
    labs,
    additionalResources,
    learningPaths,
    categories,
    getCourseById,
    getCoursesByCategory,
    getCoursesByDifficulty,
    getFeaturedCourses,
    getCoursesByPath,
    searchCourses,
    getLabById,
    getLabsByStatus,
    getLiveLabs,
    getComingSoonLabs
  };
}