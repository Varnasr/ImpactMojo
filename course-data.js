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
    path: 'data-analysis',
    tags: ['feminism', 'data', 'intersectionality'],
    url: 'https://101.www.impactmojo.in/DataFeminism',
    featured: true,
    learnerCount: 2847,
    rating: 4.8
  },
  {
    id: 'data-literacy-101',
    title: 'Data Literacy 101',
    description: 'Foundational skills for understanding and working with data in development contexts.',
    category: 'Data Analysis',
    difficulty: 'beginner',
    duration: '3-4 hours',
    path: 'data-analysis',
    tags: ['data', 'literacy', 'fundamentals'],
    url: 'data_literacy_101.html',
    featured: true,
    learnerCount: 1734,
    rating: 4.9
  },
  {
    id: 'eda-survey-data',
    title: 'EDA for Survey Data',
    description: 'Exploratory Data Analysis techniques specifically for household and survey datasets.',
    category: 'Data Analysis',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    path: 'data-analysis',
    tags: ['eda', 'survey', 'analysis'],
    url: 'eda_survey_handout_1.html',
    featured: true,
    learnerCount: 2156,
    rating: 4.7
  },
  {
    id: 'bivariate-analysis-101',
    title: 'Bivariate Analysis 101',
    description: 'Master relationships between variables using correlation, regression, and statistical tests. Features real South Asian datasets and development applications.',
    category: 'Data Analysis',
    difficulty: 'intermediate',
    duration: '5-6 hours',
    path: 'data-analysis',
    tags: ['statistics', 'relationships', 'correlation'],
    url: 'https://101.www.impactmojo.in/BivariateAnalysis',
    learnerCount: 1445,
    rating: 4.5
  },
  {
    id: 'multivariate-analysis-101',
    title: 'Multivariate Analysis 101',
    description: 'Advanced statistical techniques for analyzing multiple variables simultaneously.',
    category: 'Data Analysis',
    difficulty: 'advanced',
    duration: '5-6 hours',
    path: 'data-analysis',
    tags: ['statistics', 'multivariate', 'advanced'],
    url: 'https://101.www.impactmojo.in/MultivariateAnalysis',
    learnerCount: 1234,
    rating: 4.6
  },

  // ECONOMICS TRACK
  {
    id: 'development-economics-101',
    title: 'Development Economics 101',
    description: 'Core principles of development economics with South Asian examples.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '5-6 hours',
    path: 'economics',
    tags: ['economics', 'development', 'theory'],
    url: 'development_economics_problem_sets.html',
    featured: true,
    learnerCount: 1923,
    rating: 4.6
  },
  {
    id: 'social-safety-nets-101',
    title: 'Social Safety Nets 101',
    description: 'Unpacks India\'s welfare architecture—PDS, NREGA, pensions—through lifecycle needs and exclusion errors, with discussion on Aadhaar and last-mile barriers.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    path: 'economics',
    tags: ['welfare', 'policy', 'safety nets'],
    url: 'https://101.www.impactmojo.in/SocialSafetyNets',
    featured: true,
    learnerCount: 2156,
    rating: 4.7
  },
  {
    id: 'political-economy-101',
    title: 'Political Economy 101',
    description: 'Explores incentives, institutions, and power in policymaking, featuring comparative case studies and Indian governance contexts.',
    category: 'Economics',
    difficulty: 'advanced',
    duration: '4+ hours',
    path: 'economics',
    tags: ['political economy', 'institutions', 'governance'],
    url: 'https://101.www.impactmojo.in/PoliticalEconomy',
    learnerCount: 698,
    rating: 4.2
  },
  {
    id: 'poverty-inequality-101',
    title: 'Poverty & Inequality 101',
    description: 'Comprehensive analysis of poverty measurement, inequality trends, and policy responses in South Asian contexts.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    path: 'economics',
    tags: ['poverty', 'inequality', 'measurement'],
    url: 'https://101.www.impactmojo.in/PovertyInequality',
    learnerCount: 1567,
    rating: 4.4
  },
  {
    id: 'livelihoods-101',
    title: 'Livelihoods 101',
    description: 'Introduction to sustainable livelihoods approaches, rural economy dynamics, and livelihood diversification strategies.',
    category: 'Economics',
    difficulty: 'beginner',
    duration: '4-5 hours',
    path: 'economics',
    tags: ['livelihoods', 'sustainability', 'rural'],
    url: 'livelihood_assessment_toolkit.html',
    featured: true,
    learnerCount: 1876,
    rating: 4.5
  },
  {
    id: 'decent-work-101',
    title: 'Decent Work for All 101',
    description: 'ILO frameworks, labour rights, and employment quality in South Asian labour markets.',
    category: 'Economics',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    path: 'economics',
    tags: ['labour', 'employment', 'rights'],
    url: 'https://101.www.impactmojo.in/DecentWork',
    learnerCount: 1345,
    rating: 4.3
  },

  // GENDER STUDIES TRACK
  {
    id: 'gender-studies-101',
    title: 'Gender Studies 101',
    description: 'Foundational concepts in gender studies applied to development practice. Covers intersectionality, power dynamics, and gender-sensitive programming.',
    category: 'Gender Studies',
    difficulty: 'beginner',
    duration: '4-5 hours',
    path: 'gender-studies',
    tags: ['gender', 'development', 'social justice'],
    url: 'gender_studies_101.html',
    featured: true,
    learnerCount: 3789,
    rating: 4.6
  },
  {
    id: 'care-economy-101',
    title: 'Care Economy and Time Use 101',
    description: 'Analyzes unpaid care work, time-use surveys, care infrastructure, and feminist economics, rooted in Indian labour statistics and policy debates.',
    category: 'Gender Studies',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    path: 'gender-studies',
    tags: ['care work', 'time use', 'feminist economics'],
    url: 'https://101.www.impactmojo.in/CareEconomy',
    learnerCount: 934,
    rating: 4.4
  },
  {
    id: 'womens-economic-empowerment-101',
    title: "Women's Economic Empowerment 101",
    description: 'Strategies and frameworks for promoting women\'s economic participation and addressing barriers to economic inclusion.',
    category: 'Gender Studies',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    path: 'gender-studies',
    tags: ['empowerment', 'economics', 'women'],
    url: 'womens_economic_empowerment.html',
    learnerCount: 2456,
    rating: 4.8
  },

  // HEALTH TRACK
  {
    id: 'public-health-101',
    title: 'Public Health 101',
    description: 'Introduction to public health concepts, health systems, and major health challenges in South Asia including infectious diseases and NCDs.',
    category: 'Health',
    difficulty: 'beginner',
    duration: '5-6 hours',
    path: 'health',
    tags: ['public health', 'health systems', 'policy'],
    url: 'public_health_assessment_framework.html',
    featured: true,
    learnerCount: 3456,
    rating: 4.5
  },
  {
    id: 'mental-health-101',
    title: 'Mental Health and Well-being 101',
    description: 'Explores mental health challenges, stigma, and community-based approaches to mental wellness in South Asian contexts.',
    category: 'Health',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    path: 'health',
    tags: ['mental health', 'community', 'wellness'],
    url: 'https://101.www.impactmojo.in/MentalHealth',
    learnerCount: 1678,
    rating: 4.8
  },
  {
    id: 'nutrition-food-security-101',
    title: 'Nutrition and Food Security 101',
    description: 'Comprehensive analysis of malnutrition, food systems, and nutrition-sensitive programming approaches.',
    category: 'Health',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    path: 'health',
    tags: ['nutrition', 'food security', 'malnutrition'],
    url: 'https://101.www.impactmojo.in/Nutrition',
    learnerCount: 2123,
    rating: 4.6
  },
  {
    id: 'srhr-101',
    title: 'Sexual & Reproductive Health Rights 101',
    description: 'Comprehensive overview of SRHR frameworks, policy landscape, and implementation challenges in South Asian contexts.',
    category: 'Health',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    path: 'health',
    tags: ['SRHR', 'rights', 'reproductive health'],
    url: 'srhr.html',
    learnerCount: 823,
    rating: 4.3
  },

  // IDENTITY & JUSTICE TRACK
  {
    id: 'marginalized-identities-101',
    title: 'Marginalized Identities 101',
    description: 'Explores caste, tribe, gender, religion, disability, and intersectionality through rights, representation, and discrimination data in South Asia.',
    category: 'Identity & Justice',
    difficulty: 'intermediate',
    duration: '4+ hours',
    path: 'identity',
    tags: ['caste', 'identity', 'discrimination'],
    url: 'https://101.www.impactmojo.in/MarginalizedIdentities',
    learnerCount: 1056,
    rating: 4.5
  },
  {
    id: 'caste-class-identity-101',
    title: 'Caste, Class and Identity 101',
    description: 'Critical examination of social stratification in South Asia. Covers caste dynamics, class mobility, and intersections with development outcomes.',
    category: 'Identity & Justice',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    path: 'identity',
    tags: ['caste', 'class', 'stratification'],
    url: 'https://101.www.impactmojo.in/CasteClass',
    learnerCount: 2134,
    rating: 4.5
  },
  {
    id: 'religion-development-101',
    title: 'Religion and Development 101',
    description: 'Explores the complex relationships between religious identity, social capital, and development outcomes in pluralistic South Asian societies.',
    category: 'Identity & Justice',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    path: 'identity',
    tags: ['religion', 'social capital', 'pluralism'],
    url: 'https://101.www.impactmojo.in/Religion',
    learnerCount: 1567,
    rating: 4.4
  },

  // CLIMATE & ENVIRONMENT TRACK
  {
    id: 'climate-change-development-101',
    title: 'Climate Change and Development 101',
    description: 'Comprehensive coverage of climate impacts on development, adaptation strategies, and mitigation approaches relevant to South Asian contexts.',
    category: 'Climate & Environment',
    difficulty: 'intermediate',
    duration: '5-6 hours',
    path: 'climate',
    tags: ['climate change', 'adaptation', 'mitigation'],
    url: 'https://101.www.impactmojo.in/Climate',
    learnerCount: 2234,
    rating: 4.7
  },
  {
    id: 'environmental-justice-101',
    title: 'Environmental Justice 101',
    description: 'Explores air, water, land, and environmental decision-making through equity and procedural justice lenses in the Indian regulatory context.',
    category: 'Climate & Environment',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    path: 'climate',
    tags: ['environmental justice', 'equity', 'regulation'],
    url: 'https://101.www.impactmojo.in/EnvironmentalJustice',
    learnerCount: 789,
    rating: 4.2
  },

  // URBAN & SYSTEMS TRACK
  {
    id: 'urbanization-cities-101',
    title: 'Urbanization and Cities 101',
    description: 'Analysis of rapid urbanization in South Asia, urban governance challenges, and sustainable city planning approaches.',
    category: 'Urban & Systems',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    path: 'systems',
    tags: ['urbanization', 'governance', 'planning'],
    url: 'https://101.www.impactmojo.in/Cities',
    learnerCount: 1889,
    rating: 4.6
  },

  // EDUCATION TRACK
  {
    id: 'education-pedagogy-101',
    title: 'Education and Pedagogy 101',
    description: 'Explores educational challenges, pedagogy innovations, and evidence-based approaches to improving learning outcomes in South Asia.',
    category: 'Education',
    difficulty: 'beginner',
    duration: '4-5 hours',
    path: 'education',
    tags: ['education', 'pedagogy', 'learning'],
    url: 'education_pedagogy_101.html',
    featured: true,
    learnerCount: 2789,
    rating: 4.7
  },
  {
    id: 'digital-education-tech-101',
    title: 'Digital Education Technologies 101',
    description: 'Examination of technology-enabled learning, digital divide issues, and effective integration of tech in educational programming.',
    category: 'Education',
    difficulty: 'intermediate',
    duration: '4-5 hours',
    path: 'education',
    tags: ['edtech', 'digital divide', 'technology'],
    url: 'https://101.www.impactmojo.in/EdTech',
    learnerCount: 1567,
    rating: 4.5
  },

  // RESEARCH METHODS TRACK
  {
    id: 'research-ethics-101',
    title: 'Research Ethics 101',
    description: 'Ethical considerations in development research and practice, covering consent, harm minimization, and community engagement.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    path: 'research',
    tags: ['ethics', 'research', 'methodology'],
    url: 'research_ethics.html',
    learnerCount: 1456,
    rating: 4.4
  },
  {
    id: 'qualitative-research-101',
    title: 'Qualitative Research Methods 101',
    description: 'Comprehensive guide to qualitative research in development contexts, including interviews, focus groups, and ethnography.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '5-6 hours',
    path: 'research',
    tags: ['qualitative', 'interviews', 'ethnography'],
    url: 'qualitative_research.html',
    learnerCount: 1789,
    rating: 4.6
  },
  {
    id: 'econometrics-101',
    title: 'Econometrics 101',
    description: 'Statistical methods for economic analysis and causal inference in development research.',
    category: 'Research Methods',
    difficulty: 'advanced',
    duration: '6-8 hours',
    path: 'research',
    tags: ['econometrics', 'statistics', 'causal inference'],
    url: 'econometrics.html',
    learnerCount: 1234,
    rating: 4.7
  },
  {
    id: 'mel-101',
    title: 'Monitoring, Evaluation & Learning (MEL) 101',
    description: 'Frameworks and tools for effective program monitoring and evaluation in development contexts.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '5-6 hours',
    path: 'research',
    tags: ['MEL', 'evaluation', 'monitoring'],
    url: 'mel.html',
    learnerCount: 1678,
    rating: 4.5
  },
  {
    id: 'visual-ethnography-101',
    title: 'Visual Ethnography and Storytelling 101',
    description: 'Introduces participatory photography, visual documentation ethics, field aesthetics, and representation frameworks for South Asian contexts.',
    category: 'Research Methods',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    path: 'research',
    tags: ['visual ethnography', 'photography', 'storytelling'],
    url: 'https://101.www.impactmojo.in/VisualEthnography',
    learnerCount: 445,
    rating: 4.1
  },

  // TECHNOLOGY & INNOVATION
  {
    id: 'digital-development-ethics-101',
    title: 'Digital Development Ethics 101',
    description: 'Ethical frameworks for technology use in development programming, covering privacy, consent, and digital rights.',
    category: 'Technology',
    difficulty: 'intermediate',
    duration: '3-4 hours',
    path: 'technology',
    tags: ['digital ethics', 'technology', 'privacy'],
    url: 'digital_development_ethics.html',
    learnerCount: 987,
    rating: 4.3
  },

  // ADDITIONAL SPECIALIZED COURSES
  {
    id: 'impact-measurement-101',
    title: 'Impact Measurement 101',
    description: 'Methods and tools for measuring social and economic impact in development programs.',
    category: 'Research Methods',
    difficulty: 'advanced',
    duration: '5-6 hours',
    path: 'research',
    tags: ['impact', 'measurement', 'evaluation'],
    url: 'impact_measurement.html',
    learnerCount: 1123,
    rating: 4.6
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
    icon: 'fas fa-cogs',
    status: 'live',
    url: 'https://mel-framework.netlify.app/',
    category: 'MEL Tools'
  },
  {
    id: 'budget-simulator',
    title: 'Budget Simulator',
    description: 'Model and test different budget scenarios for development projects.',
    icon: 'fas fa-calculator',
    status: 'coming-soon',
    url: '#',
    category: 'Financial Planning'
  },
  {
    id: 'stakeholder-mapper',
    title: 'Stakeholder Mapping Tool',
    description: 'Visualize and analyze stakeholder relationships and influence.',
    icon: 'fas fa-sitemap',
    status: 'coming-soon',
    url: '#',
    category: 'Analysis Tools'
  },
  {
    id: 'data-viz-builder',
    title: 'Data Visualization Builder',
    description: 'Create interactive charts and dashboards from development data.',
    icon: 'fas fa-chart-pie',
    status: 'coming-soon',
    url: '#',
    category: 'Data Tools'
  },
  {
    id: 'survey-designer',
    title: 'Survey Design Assistant',
    description: 'Build and validate survey instruments for development research.',
    icon: 'fas fa-clipboard-list',
    status: 'coming-soon',
    url: '#',
    category: 'Research Tools'
  },
  {
    id: 'policy-simulator',
    title: 'Policy Impact Simulator',
    description: 'Model potential impacts of policy interventions.',
    icon: 'fas fa-balance-scale',
    status: 'coming-soon',
    url: '#',
    category: 'Policy Tools'
  },
  {
    id: 'community-feedback',
    title: 'Community Feedback Portal',
    description: 'Collect and analyze community feedback on development programs.',
    icon: 'fas fa-comments',
    status: 'coming-soon',
    url: '#',
    category: 'Community Tools'
  }
];

// Additional Resources (Extras)
const additionalResources = {
  handouts: {
    title: 'Educational Handouts',
    description: 'Over 20 ready-to-use workshop modules covering Digital Development Ethics, Statistical Analysis, and South Asian Applications. Each designed for 75-90 minute classroom sessions.',
    url: 'https://github.com/Varnasr/ImpactMojo/tree/main/extras/handouts',
    relatedCourses: ['education-pedagogy-101', 'digital-development-ethics-101', 'data-literacy-101']
  },
  research: {
    title: 'Research Design Resources',
    description: 'Practical tools for conducting rigorous development research, including design standards checklists and specialized papers like "Understanding Attributable Risk".',
    url: 'https://github.com/Varnasr/ImpactMojo/tree/main/extras/research-design',
    relatedCourses: ['research-ethics-101', 'qualitative-research-101', 'mel-101', 'econometrics-101']
  },
  health: {
    title: 'Public Health Materials',
    description: 'Complete course on public health fundamentals developed by the CDC, providing evidence-based frameworks for health program design and evaluation.',
    url: 'https://github.com/Varnasr/ImpactMojo/tree/main/extras/public-health',
    relatedCourses: ['public-health-101', 'srhr-101']
  },
  data: {
    title: 'Data Analysis Toolkit',
    description: 'Comprehensive technical resources including analysis scripts, Excel templates, Python code samples, and qualitative data analysis tools.',
    url: 'https://github.com/Varnasr/ImpactMojo/tree/main/extras/data-analysis',
    relatedCourses: ['data-literacy-101', 'eda-survey-data', 'bivariate-analysis-101', 'multivariate-analysis-101', 'econometrics-101']
  }
};

// Learning paths configuration
const learningPaths = {
  'data-analysis': {
    name: 'Data Analysis Track',
    description: 'Master data skills from basics to advanced analysis',
    icon: 'fas fa-chart-bar',
    courses: ['data-literacy-101', 'eda-survey-data', 'bivariate-analysis-101', 'multivariate-analysis-101', 'data-feminism-101'],
    color: '#3498db'
  },
  'gender-studies': {
    name: 'Gender Studies Pathway',
    description: 'Comprehensive understanding of gender in development',
    icon: 'fas fa-venus-mars',
    courses: ['gender-studies-101', 'data-feminism-101', 'care-economy-101', 'womens-economic-empowerment-101'],
    color: '#8e44ad'
  },
  'economics': {
    name: 'Development Economics',
    description: 'Economic theory and practice for development professionals',
    icon: 'fas fa-coins',
    courses: ['development-economics-101', 'social-safety-nets-101', 'political-economy-101', 'livelihoods-101'],
    color: '#2c3e50'
  },
  'research': {
    name: 'Research Methods Journey',
    description: 'Complete research toolkit for development work',
    icon: 'fas fa-flask',
    courses: ['research-ethics-101', 'qualitative-research-101', 'econometrics-101', 'mel-101'],
    color: '#e74c3c'
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