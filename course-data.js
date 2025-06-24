// ImpactMojo 101 Knowledge Series - Complete Course and Lab Data
// All 34 courses + 9 labs with proper categorization and functionality

console.log('📚 Loading course and lab data...');

// ===== COURSE DATA =====
const courses = [
  // ECONOMICS & DEVELOPMENT
  {
    id: 'dev-econ-101',
    title: 'Development Economics 101',
    category: 'Economics & Development',
    difficulty: 'Intermediate',
    duration: '45 min',
    rating: 4.8,
    description: 'Comprehensive introduction to development economics theory and practice in South Asian contexts.',
    url: 'https://101.www.impactmojo.in/DevEcon',
    topics: ['Economic Growth', 'Poverty Reduction', 'Development Theory', 'Market Failures'],
    learningPath: 'Development Foundations'
  },
  {
    id: 'political-economy-101',
    title: 'Political Economy 101',
    category: 'Economics & Development',
    difficulty: 'Advanced',
    duration: '50 min',
    rating: 4.7,
    description: 'Understanding the intersection of politics and economics in development contexts.',
    url: 'https://101.www.impactmojo.in/polecon',
    topics: ['Institutional Economics', 'State and Markets', 'Power Dynamics', 'Governance'],
    learningPath: 'Development Foundations'
  },
  {
    id: 'poverty-inequality-101',
    title: 'Poverty and Inequality 101',
    category: 'Economics & Development',
    difficulty: 'Intermediate',
    duration: '40 min',
    rating: 4.6,
    description: 'Deep dive into poverty measurement, inequality analysis, and intervention strategies.',
    url: 'https://101.www.impactmojo.in/pov&inq',
    topics: ['Poverty Measurement', 'Inequality Indices', 'Social Mobility', 'Policy Interventions'],
    learningPath: 'Development Foundations'
  },
  {
    id: 'livelihoods-101',
    title: 'Livelihoods 101',
    category: 'Economics & Development',
    difficulty: 'Intermediate',
    duration: '35 min',
    rating: 4.5,
    description: 'Sustainable livelihoods framework and rural development strategies.',
    url: 'https://101.www.impactmojo.in/Livelihoods',
    topics: ['Livelihoods Framework', 'Rural Development', 'Asset Building', 'Vulnerability Analysis'],
    learningPath: 'Development Foundations'
  },
  {
    id: 'care-economy-101',
    title: 'Care Economy 101',
    category: 'Economics & Development',
    difficulty: 'Intermediate',
    duration: '40 min',
    rating: 4.7,
    description: 'Understanding unpaid care work and its role in economic development.',
    url: 'https://101.www.impactmojo.in/careeconomy',
    topics: ['Unpaid Care Work', 'Time Use Surveys', 'Care Infrastructure', 'Gender Economics'],
    learningPath: 'Gender Studies Pathway'
  },
  {
    id: 'decent-work-101',
    title: 'Decent Work 101',
    category: 'Economics & Development',
    difficulty: 'Intermediate',
    duration: '35 min',
    rating: 4.4,
    description: 'ILO decent work agenda and employment quality in developing contexts.',
    url: 'https://101.www.impactmojo.in/DecentWork',
    topics: ['Decent Work Agenda', 'Employment Quality', 'Labour Rights', 'Social Protection'],
    learningPath: 'Development Foundations'
  },
  {
    id: 'social-welfare-101',
    title: 'Social Welfare and Safety Nets 101',
    category: 'Economics & Development',
    difficulty: 'Intermediate',
    duration: '45 min',
    rating: 4.6,
    description: 'Design and evaluation of social protection programs in developing countries.',
    url: 'https://101.www.impactmojo.in/safetynets',
    topics: ['Social Protection', 'Cash Transfers', 'Safety Nets', 'Welfare Economics'],
    learningPath: 'Development Foundations'
  },

  // RESEARCH & DATA ANALYSIS
  {
    id: 'econometrics-101',
    title: 'Econometrics 101',
    category: 'Research & Data Analysis',
    difficulty: 'Advanced',
    duration: '60 min',
    rating: 4.8,
    description: 'Statistical methods for economic analysis and causal inference.',
    url: 'https://101.www.impactmojo.in/econometrics',
    topics: ['Regression Analysis', 'Causal Inference', 'Panel Data', 'Instrumental Variables'],
    learningPath: 'Data Analysis Track'
  },
  {
    id: 'qualitative-research-101',
    title: 'Qualitative Research Methods 101',
    category: 'Research & Data Analysis',
    difficulty: 'Intermediate',
    duration: '50 min',
    rating: 4.7,
    description: 'Comprehensive guide to qualitative research in development contexts.',
    url: 'https://101.www.impactmojo.in/QualR',
    topics: ['Interview Methods', 'Ethnography', 'Content Analysis', 'Mixed Methods'],
    learningPath: 'Research Methods'
  },
  {
    id: 'research-ethics-101',
    title: 'Research Ethics 101',
    category: 'Research & Data Analysis',
    difficulty: 'Beginner',
    duration: '30 min',
    rating: 4.9,
    description: 'Ethical considerations in development research and practice.',
    url: 'https://101.www.impactmojo.in/ResearchEthics',
    topics: ['Informed Consent', 'Research Ethics', 'Vulnerable Populations', 'Data Protection'],
    learningPath: 'Research Methods'
  },
  {
    id: 'data-literacy-101',
    title: 'Data Literacy 101',
    category: 'Research & Data Analysis',
    difficulty: 'Beginner',
    duration: '35 min',
    rating: 4.5,
    description: 'Foundational data skills for development practitioners.',
    url: 'https://101.www.impactmojo.in/data-lit',
    topics: ['Data Collection', 'Data Quality', 'Basic Statistics', 'Data Visualization'],
    learningPath: 'Data Analysis Track'
  },
  {
    id: 'hh-eda-101',
    title: 'Exploratory Data Analysis for Household Surveys 101',
    category: 'Research & Data Analysis',
    difficulty: 'Intermediate',
    duration: '45 min',
    rating: 4.6,
    description: 'Statistical exploration of household survey data in development research.',
    url: 'https://101.www.impactmojo.in/HH-EDA',
    topics: ['Survey Data', 'Descriptive Statistics', 'Data Exploration', 'Household Analysis'],
    learningPath: 'Data Analysis Track'
  },
  {
    id: 'bivariate-analysis-101',
    title: 'Bivariate Analysis 101',
    category: 'Research & Data Analysis',
    difficulty: 'Intermediate',
    duration: '40 min',
    rating: 4.5,
    description: 'Two-variable statistical analysis methods for development data.',
    url: 'https://101.www.impactmojo.in/bivariateA',
    topics: ['Correlation Analysis', 'Chi-square Tests', 'T-tests', 'Cross-tabulation'],
    learningPath: 'Data Analysis Track'
  },
  {
    id: 'multivariate-analysis-101',
    title: 'Multivariate Analysis 101',
    category: 'Research & Data Analysis',
    difficulty: 'Advanced',
    duration: '55 min',
    rating: 4.7,
    description: 'Advanced statistical methods for complex development data analysis.',
    url: 'https://101.www.impactmojo.in/MultivariateA',
    topics: ['Multiple Regression', 'Factor Analysis', 'Cluster Analysis', 'Discriminant Analysis'],
    learningPath: 'Data Analysis Track'
  },
  {
    id: 'visual-ethnography-101',
    title: 'Visual Ethnography 101',
    category: 'Research & Data Analysis',
    difficulty: 'Intermediate',
    duration: '40 min',
    rating: 4.4,
    description: 'Using visual methods in ethnographic research for development.',
    url: 'https://101.www.impactmojo.in/VEthno',
    topics: ['Photo-elicitation', 'Video Ethnography', 'Participatory Visual Methods', 'Visual Analysis'],
    learningPath: 'Research Methods'
  },
  {
    id: 'data-feminism-101',
    title: 'Data Feminism 101',
    category: 'Research & Data Analysis',
    difficulty: 'Intermediate',
    duration: '45 min',
    rating: 4.8,
    description: 'Feminist approaches to data science and research methodology.',
    url: 'https://101.www.impactmojo.in/DataFem',
    topics: ['Feminist Data Science', 'Intersectionality', 'Power in Data', 'Inclusive Methods'],
    learningPath: 'Gender Studies Pathway'
  },

  // GENDER & SOCIAL JUSTICE
  {
    id: 'gender-studies-101',
    title: 'Gender Studies 101',
    category: 'Gender & Social Justice',
    difficulty: 'Beginner',
    duration: '40 min',
    rating: 4.9,
    description: 'Foundational concepts in gender theory and development practice.',
    url: 'https://101.www.impactmojo.in/Gender',
    topics: ['Gender Theory', 'Intersectionality', 'Patriarchy', 'Gender Analysis'],
    learningPath: 'Gender Studies Pathway'
  },
  {
    id: 'womens-empowerment-101',
    title: 'Women\'s Economic Empowerment 101',
    category: 'Gender & Social Justice',
    difficulty: 'Intermediate',
    duration: '45 min',
    rating: 4.7,
    description: 'Strategies for promoting women\'s economic participation and empowerment.',
    url: 'https://101.www.impactmojo.in/WEE',
    topics: ['Economic Empowerment', 'Financial Inclusion', 'Entrepreneurship', 'Labor Force Participation'],
    learningPath: 'Gender Studies Pathway'
  },
  {
    id: 'marginalized-identities-101',
    title: 'Marginalized Identities 101',
    category: 'Gender & Social Justice',
    difficulty: 'Intermediate',
    duration: '40 min',
    rating: 4.6,
    description: 'Understanding intersectional identities and marginalization in development.',
    url: 'https://101.www.impactmojo.in/identities',
    topics: ['Intersectionality', 'Caste', 'Sexuality', 'Disability', 'Social Exclusion'],
    learningPath: 'Social Justice'
  },
  {
    id: 'srhr-101',
    title: 'Sexual and Reproductive Health Rights 101',
    category: 'Gender & Social Justice',
    difficulty: 'Intermediate',
    duration: '45 min',
    rating: 4.8,
    description: 'Rights-based approach to sexual and reproductive health in development.',
    url: 'https://101.www.impactmojo.in/srhr',
    topics: ['Reproductive Rights', 'Sexual Health', 'Maternal Health', 'Family Planning'],
    learningPath: 'Public Health Track'
  },

  // GOVERNANCE & POLICY
  {
    id: 'law-constitution-101',
    title: 'Law and Constitution 101',
    category: 'Governance & Policy',
    difficulty: 'Intermediate',
    duration: '50 min',
    rating: 4.5,
    description: 'Constitutional law and legal frameworks for development in India.',
    url: 'https://101.www.impactmojo.in/Law&Cons',
    topics: ['Constitutional Law', 'Fundamental Rights', 'Directive Principles', 'Legal Framework'],
    learningPath: 'Governance'
  },
  {
    id: 'meal-101',
    title: 'Monitoring, Evaluation, Accountability and Learning 101',
    category: 'Governance & Policy',
    difficulty: 'Intermediate',
    duration: '50 min',
    rating: 4.7,
    description: 'MEAL frameworks for development programs and policy evaluation.',
    url: 'https://101.www.impactmojo.in/MEAL',
    topics: ['Theory of Change', 'Impact Evaluation', 'Accountability', 'Learning Systems'],
    learningPath: 'Program Management'
  },
  {
    id: 'global-dev-arch-101',
    title: 'Global Development Architecture 101',
    category: 'Governance & Policy',
    difficulty: 'Advanced',
    duration: '55 min',
    rating: 4.6,
    description: 'Understanding global development institutions and aid architecture.',
    url: 'https://101.www.impactmojo.in/GDArch',
    topics: ['Development Finance', 'Multilateral Organizations', 'Aid Effectiveness', 'Global Governance'],
    learningPath: 'Development Foundations'
  },
  {
    id: 'decolonising-dev-101',
    title: 'Decolonising Development 101',
    category: 'Governance & Policy',
    difficulty: 'Advanced',
    duration: '50 min',
    rating: 4.9,
    description: 'Critical perspectives on development practice and decolonial approaches.',
    url: 'https://101.www.impactmojo.in/decolonD',
    topics: ['Decolonial Theory', 'Post-development', 'Indigenous Knowledge', 'Power Relations'],
    learningPath: 'Critical Development'
  },
  {
    id: 'post-truth-politics-101',
    title: 'Post-Truth Politics 101',
    category: 'Governance & Policy',
    difficulty: 'Intermediate',
    duration: '40 min',
    rating: 4.4,
    description: 'Understanding misinformation and post-truth dynamics in policy contexts.',
    url: 'https://101.www.impactmojo.in/post-truth-pol',
    topics: ['Misinformation', 'Media Literacy', 'Democratic Governance', 'Information Warfare'],
    learningPath: 'Digital Society'
  },

  // HEALTH & ENVIRONMENT
  {
    id: 'public-health-101',
    title: 'Public Health 101',
    category: 'Health & Environment',
    difficulty: 'Beginner',
    duration: '40 min',
    rating: 4.8,
    description: 'Fundamentals of public health approaches in developing country contexts.',
    url: 'https://101.www.impactmojo.in/ph',
    topics: ['Epidemiology', 'Health Systems', 'Disease Prevention', 'Health Promotion'],
    learningPath: 'Public Health Track'
  },
  {
    id: 'climate-science-101',
    title: 'Climate Science 101',
    category: 'Health & Environment',
    difficulty: 'Intermediate',
    duration: '45 min',
    rating: 4.7,
    description: 'Climate change science and its implications for development.',
    url: 'https://101.www.impactmojo.in/ClimateScience',
    topics: ['Climate Dynamics', 'Global Warming', 'Climate Impacts', 'Adaptation'],
    learningPath: 'Environment & Climate'
  },
  {
    id: 'environmental-justice-101',
    title: 'Environmental Justice 101',
    category: 'Health & Environment',
    difficulty: 'Intermediate',
    duration: '40 min',
    rating: 4.6,
    description: 'Environmental inequalities and justice frameworks in development.',
    url: 'https://101.www.impactmojo.in/env-jus',
    topics: ['Environmental Racism', 'Climate Justice', 'Resource Conflicts', 'Environmental Rights'],
    learningPath: 'Environment & Climate'
  },

  // EDUCATION & COMMUNICATION
  {
    id: 'pedagogy-education-101',
    title: 'Pedagogy and Education 101',
    category: 'Education & Communication',
    difficulty: 'Beginner',
    duration: '35 min',
    rating: 4.5,
    description: 'Educational theory and practice for development contexts.',
    url: 'https://101.www.impactmojo.in/edu',
    topics: ['Learning Theory', 'Inclusive Education', 'Adult Learning', 'Educational Development'],
    learningPath: 'Education'
  },
  {
    id: 'bccp-101',
    title: 'Behaviour Change Communication Programming 101',
    category: 'Education & Communication',
    difficulty: 'Intermediate',
    duration: '45 min',
    rating: 4.6,
    description: 'Designing effective behavior change interventions in development programs.',
    url: 'https://101.www.impactmojo.in/BCCP',
    topics: ['Behavior Change Models', 'Communication Strategy', 'Social Marketing', 'Program Design'],
    learningPath: 'Program Management'
  },
  {
    id: 'advocacy-comm-101',
    title: 'Advocacy and Communications 101',
    category: 'Education & Communication',
    difficulty: 'Intermediate',
    duration: '40 min',
    rating: 4.4,
    description: 'Strategic communication and advocacy for development organizations.',
    url: 'https://101.www.impactmojo.in/adv&comm',
    topics: ['Advocacy Strategy', 'Stakeholder Engagement', 'Media Relations', 'Campaign Planning'],
    learningPath: 'Program Management'
  },

  // TECHNOLOGY & ETHICS
  {
    id: 'digital-ethics-101',
    title: 'Digital Ethics 101',
    category: 'Technology & Ethics',
    difficulty: 'Intermediate',
    duration: '40 min',
    rating: 4.7,
    description: 'Ethical considerations in digital development and technology use.',
    url: 'https://101.www.impactmojo.in/DigitalEthics',
    topics: ['Data Privacy', 'Algorithmic Bias', 'Digital Rights', 'Technology Ethics'],
    learningPath: 'Digital Society'
  },

  // COMMUNITY & FUNDRAISING
  {
    id: 'community-dev-101',
    title: 'Community Development 101',
    category: 'Community & Fundraising',
    difficulty: 'Beginner',
    duration: '35 min',
    rating: 4.5,
    description: 'Participatory approaches to community-driven development.',
    url: 'https://101.www.impactmojo.in/community-dev',
    topics: ['Community Mobilization', 'Participatory Development', 'Social Capital', 'Local Governance'],
    learningPath: 'Development Foundations'
  },
  {
    id: 'fundraising-101',
    title: 'Fundraising 101',
    category: 'Community & Fundraising',
    difficulty: 'Beginner',
    duration: '30 min',
    rating: 4.3,
    description: 'Fundraising strategies for development organizations and social enterprises.',
    url: 'https://101.www.impactmojo.in/fundraising',
    topics: ['Grant Writing', 'Donor Relations', 'Fundraising Strategy', 'Resource Mobilization'],
    learningPath: 'Organizational Management'
  }
];

// ===== LAB DATA =====
const labs = [
  {
    id: 'poverty-calc-lab',
    title: 'Poverty Calculator Lab',
    category: 'Economics & Development',
    difficulty: 'Intermediate',
    duration: '20 min',
    rating: 4.7,
    description: 'Interactive tool to calculate poverty headcount ratio, poverty gap, and squared poverty gap.',
    url: 'https://labs.impactmojo.in/poverty-calculator',
    topics: ['Poverty Measurement', 'FGT Indices', 'Poverty Line', 'Welfare Analysis'],
    learningPath: 'Data Analysis Track',
    labType: 'Calculator',
    relatedCourses: ['poverty-inequality-101', 'dev-econ-101']
  },
  {
    id: 'inequality-viz-lab',
    title: 'Inequality Visualization Lab',
    category: 'Economics & Development', 
    difficulty: 'Beginner',
    duration: '15 min',
    rating: 4.6,
    description: 'Interactive visualizations of income inequality using Lorenz curves and Gini coefficients.',
    url: 'https://labs.impactmojo.in/inequality-viz',
    topics: ['Lorenz Curve', 'Gini Coefficient', 'Income Distribution', 'Inequality Measures'],
    learningPath: 'Data Analysis Track',
    labType: 'Visualization',
    relatedCourses: ['poverty-inequality-101', 'econometrics-101']
  },
  {
    id: 'survey-design-lab',
    title: 'Survey Design Lab',
    category: 'Research & Data Analysis',
    difficulty: 'Intermediate',
    duration: '25 min',
    rating: 4.8,
    description: 'Step-by-step tool for designing effective household surveys for development research.',
    url: 'https://labs.impactmojo.in/survey-design',
    topics: ['Questionnaire Design', 'Sampling Methods', 'Survey Methodology', 'Data Collection'],
    learningPath: 'Research Methods',
    labType: 'Design Tool',
    relatedCourses: ['qualitative-research-101', 'research-ethics-101', 'hh-eda-101']
  },
  {
    id: 'power-analysis-lab',
    title: 'Statistical Power Analysis Lab',
    category: 'Research & Data Analysis',
    difficulty: 'Advanced',
    duration: '30 min',
    rating: 4.5,
    description: 'Calculate sample sizes and statistical power for impact evaluations and experiments.',
    url: 'https://labs.impactmojo.in/power-analysis',
    topics: ['Statistical Power', 'Sample Size', 'Effect Size', 'Type I/II Errors'],
    learningPath: 'Data Analysis Track',
    labType: 'Calculator',
    relatedCourses: ['econometrics-101', 'research-ethics-101', 'meal-101']
  },
  {
    id: 'gender-budget-lab',
    title: 'Gender Budget Analysis Lab',
    category: 'Gender & Social Justice',
    difficulty: 'Intermediate',
    duration: '25 min',
    rating: 4.7,
    description: 'Tools for analyzing government budgets through a gender lens.',
    url: 'https://labs.impactmojo.in/gender-budget',
    topics: ['Gender Budgeting', 'Public Finance', 'Budget Analysis', 'Gender Mainstreaming'],
    learningPath: 'Gender Studies Pathway',
    labType: 'Analysis Tool',
    relatedCourses: ['gender-studies-101', 'womens-empowerment-101', 'law-constitution-101']
  },
  {
    id: 'theory-change-lab',
    title: 'Theory of Change Builder Lab',
    category: 'Governance & Policy',
    difficulty: 'Beginner',
    duration: '20 min',
    rating: 4.9,
    description: 'Interactive tool to build and visualize theory of change for development programs.',
    url: 'https://labs.impactmojo.in/theory-change',
    topics: ['Theory of Change', 'Logic Models', 'Program Design', 'Results Framework'],
    learningPath: 'Program Management',
    labType: 'Design Tool',
    relatedCourses: ['meal-101', 'bccp-101', 'community-dev-101']
  },
  {
    id: 'climate-impact-lab',
    title: 'Climate Impact Calculator Lab',
    category: 'Health & Environment',
    difficulty: 'Intermediate',
    duration: '20 min',
    rating: 4.6,
    description: 'Calculate and visualize climate change impacts on agriculture and livelihoods.',
    url: 'https://labs.impactmojo.in/climate-impact',
    topics: ['Climate Modeling', 'Agricultural Impact', 'Vulnerability Assessment', 'Adaptation Planning'],
    learningPath: 'Environment & Climate',
    labType: 'Calculator',
    relatedCourses: ['climate-science-101', 'environmental-justice-101', 'livelihoods-101']
  },
  {
    id: 'data-viz-lab',
    title: 'Development Data Visualization Lab',
    category: 'Research & Data Analysis',
    difficulty: 'Beginner',
    duration: '15 min',
    rating: 4.4,
    description: 'Create effective charts and graphs for development data storytelling.',
    url: 'https://labs.impactmojo.in/data-viz',
    topics: ['Data Visualization', 'Charts', 'Infographics', 'Data Storytelling'],
    learningPath: 'Data Analysis Track',
    labType: 'Visualization',
    relatedCourses: ['data-literacy-101', 'advocacy-comm-101', 'hh-eda-101']
  },
  {
    id: 'ethics-scenarios-lab',
    title: 'Research Ethics Scenarios Lab',
    category: 'Research & Data Analysis',
    difficulty: 'Beginner',
    duration: '18 min',
    rating: 4.8,
    description: 'Interactive scenarios to practice ethical decision-making in development research.',
    url: 'https://labs.impactmojo.in/ethics-scenarios',
    topics: ['Research Ethics', 'Case Studies', 'Ethical Dilemmas', 'Decision Making'],
    learningPath: 'Research Methods',
    labType: 'Simulation',
    relatedCourses: ['research-ethics-101', 'digital-ethics-101', 'qualitative-research-101']
  }
];

// ===== LEARNING PATHS CONFIGURATION =====
const learningPaths = [
  {
    id: 'development-foundations',
    title: 'Development Foundations',
    description: 'Core concepts in international development theory and practice',
    color: '#6366f1',
    courses: ['dev-econ-101', 'political-economy-101', 'poverty-inequality-101', 'global-dev-arch-101'],
    estimatedDuration: '3-4 weeks'
  },
  {
    id: 'data-analysis-track',
    title: 'Data Analysis Track',
    description: 'Master data skills from basics to advanced analysis',
    color: '#059669',
    courses: ['data-literacy-101', 'hh-eda-101', 'bivariate-analysis-101', 'multivariate-analysis-101', 'econometrics-101'],
    estimatedDuration: '6-8 weeks'
  },
  {
    id: 'gender-studies-pathway',
    title: 'Gender Studies Pathway',
    description: 'Comprehensive understanding of gender in development',
    color: '#dc2626',
    courses: ['gender-studies-101', 'data-feminism-101', 'care-economy-101', 'womens-empowerment-101'],
    estimatedDuration: '4-5 weeks'
  },
  {
    id: 'public-health-track',
    title: 'Public Health Track',
    description: 'Health systems and public health approaches in development',
    color: '#7c3aed',
    courses: ['public-health-101', 'srhr-101', 'environmental-justice-101', 'bccp-101'],
    estimatedDuration: '4-6 weeks'
  }
];

// ===== CATEGORY CONFIGURATIONS =====
const courseCategories = [
  { name: 'All Courses', count: courses.length, color: '#6366f1' },
  { name: 'Economics & Development', count: courses.filter(c => c.category === 'Economics & Development').length, color: '#059669' },
  { name: 'Research & Data Analysis', count: courses.filter(c => c.category === 'Research & Data Analysis').length, color: '#dc2626' },
  { name: 'Gender & Social Justice', count: courses.filter(c => c.category === 'Gender & Social Justice').length, color: '#7c3aed' },
  { name: 'Governance & Policy', count: courses.filter(c => c.category === 'Governance & Policy').length, color: '#ea580c' },
  { name: 'Health & Environment', count: courses.filter(c => c.category === 'Health & Environment').length, color: '#0891b2' },
  { name: 'Education & Communication', count: courses.filter(c => c.category === 'Education & Communication').length, color: '#be185d' },
  { name: 'Technology & Ethics', count: courses.filter(c => c.category === 'Technology & Ethics').length, color: '#4338ca' },
  { name: 'Community & Fundraising', count: courses.filter(c => c.category === 'Community & Fundraising').length, color: '#16a34a' }
];

// ===== POPULAR AND FEATURED COURSES =====
const popularCourses = [
  'gender-studies-101',
  'dev-econ-101', 
  'research-ethics-101',
  'public-health-101',
  'data-literacy-101',
  'poverty-inequality-101'
];

const featuredCourses = [
  'decolonising-dev-101',
  'data-feminism-101',
  'environmental-justice-101',
  'digital-ethics-101'
];

// ===== UPCOMING COURSES =====
const upcomingCourses = [
  {
    id: 'tall-methodology',
    title: 'TALL Methodology for Development Programs',
    category: 'Governance & Policy',
    difficulty: 'Advanced',
    expectedLaunch: 'August 2025',
    description: 'Thinking and Acting Like a Learner (TALL) methodology for adaptive programming.',
    topics: ['Adaptive Management', 'Learning Systems', 'Program Adaptation', 'Complexity'],
    preRegister: true
  },
  {
    id: 'basic-english-dev',
    title: 'Basic English for Development Practitioners',
    category: 'Education & Communication',
    difficulty: 'Beginner',
    expectedLaunch: 'September 2025',
    description: 'Essential English communication skills for development professionals.',
    topics: ['Professional Writing', 'Presentation Skills', 'Report Writing', 'Communication'],
    preRegister: true
  }
];

// ===== EXPORT CONFIGURATION =====
console.log(`✅ Loaded ${courses.length} courses and ${labs.length} labs successfully!`);

// Make data available globally and ensure they're accessible
try {
  if (typeof window !== 'undefined') {
    window.courses = courses;
    window.labs = labs;
    window.learningPaths = learningPaths;
    window.courseCategories = courseCategories;
    window.popularCourses = popularCourses;
    window.featuredCourses = featuredCourses;
    window.upcomingCourses = upcomingCourses;
    
    // Trigger data loaded event
    window.dispatchEvent(new CustomEvent('dataLoaded', { 
      detail: { courses, labs } 
    }));
    
    console.log('✅ Course data successfully attached to window object');
  }
} catch (error) {
  console.error('❌ Error making data globally available:', error);
}