(function(){
  // Prevent double-install
  if (window.__mojiniFlags?.faqBankV1) return;
  (window.__mojiniFlags || (window.__mojiniFlags = {})).faqBankV1 = true;

  const AGENT_NAME = window.IM_AGENT_NAME || "Mojini";

  // "" "" "" Reuse (or define) minimal KB so we can answer course/lab questions crisply "" "" "" 
  const COURSES = (window.__MOJINI_COURSES__) || [
    { t:'Development Economics 101', u:'/101-courses/dev-economics.html', o:'Poverty, inequality, growth; India/South Asia.'},
    { t:'Law and Constitution 101',   u:'/101-courses/ind-constitution.html', o:'Constitutional principles, rights, institutions.'},
    { t:'Climate Science 101',        u:'/101-courses/climate-essentials.html', o:'Climate systems, evidence, risk; adaptation/resilience.'},
    { t:'Pedagogy and Education 101', u:'/101-courses/edu-pedagogy.html', o:'Learning science + practice in Indian systems.'},
    { t:'Public Health 101',          u:'/101-courses/pub-health-basics.html', o:'Epidemiology, health systems, field implementation.'},
    { t:'Livelihoods 101',            u:'/101-courses/livelihood-basics.html', o:'Labour markets, enterprise, programme design.'},
    { t:'Gender Studies',             u:'/courses/gender/', o:'Frameworks, intersectionality, implications.'},
    { t:"Womens' Economic Empowerment 101", u:'/101-courses/wee-studies.html', o:'Approaches, metrics, programme design.'},
    { t:'Research Ethics 101',        u:'/101-courses/research-ethics.html', o:'Consent, dignity, data protection in research.'},
    { t:'Behaviour Change Communication Programming 101', u:'/101-courses/bcc-comms.html', o:'Designing and testing BCC.'},
    { t:'Advocacy and Communications 101', u:'/101-courses/advocacy-basics.html', o:'Strategy, messaging, coalitions.'},
    { t:'Monitoring, Evaluation, Accountability and Learning 101', u:'/101-courses/mel-basics.html', o:'Indicators, learning loops for implementers.'},
    { t:'Visual Ethnography 101',     u:'/101-courses/visual-eth.html', o:'Photo/video methods; ethical storytelling.'},
    { t:'Political Economy 101',      u:'/101-courses/pol-economy.html', o:'Institutions, incentives, power.'},
    { t:'Poverty and Inequality 101', u:'/101-courses/inequality-basics.html', o:'Measures, drivers, interpretation.'},
    { t:'Data Visualisation 101',     u:'/101-courses/data-lit.html', o:'Clear, ethical charts and dashboards.'},
    { t:'Mixed Methods Research 101', u:'/101-courses/qual-methods.html', o:'Integrating qual + quant rigorously.'},
    { t:'Impact Evaluation Design 101', u:'/101-courses/econometrics-101.html', o:'RCT to quasi-experimental choices.'},
    { t:'Fundraising 101',            u:'/101-courses/fundraising-basics.html', o:'HNI, institutional, grassroots basics.'},
    { t:'Programme Design Principles 101', u:'/101-courses/community-dev.html', o:'Problem framing -> ToC, delivery, risk.'},
    { t:'Environmental Justice 101',  u:'/101-courses/env-justice.html', o:'Justice-centred climate/environment action.'},
    { t:'Digital Governance 101',     u:'/101-courses/digital-ethics.html', o:'Platforms, data governance, service delivery.'},
    { t:'Nutrition, Food Systems & Culture 101', u:'/101-courses/care-economy-101.html', o:'Nutrition security, culture, markets.'},
    { t:'Social Research Ethics & Consent 101', u:'/101-courses/SRHR-basics.html', o:'Operationalising consent and dignity.'},
    { t:'Language & History of Languages 101', u:'/101-courses/post-truth-101.html', o:'Language change, identity, policy.'},
    { t:'Caste 101',                  u:'/101-courses/social-margins.html', o:'Caste, discrimination, remedies.'},
    { t:'Humanitarian vs Development Work 101', u:'/101-courses/decolonize-dev.html', o:'Goals, timelines, accountability.'},
    { t:"Gandhi's Political Thought",      u:'/courses/gandhi/', o:'Swaraj, Satyagraha, Trusteeship, Gram Swaraj; 13 modules + interactive lexicon.'},
    { t:"Understanding Development Economics", u:'/courses/devecon/', o:'Poverty, growth, capabilities; 13 modules + 63-term lexicon.'},
    { t:"Seeing Data: Visualization for Impact", u:'/courses/dataviz/', o:'Tufte principles to dashboards; 13 modules + chart chooser.'},
    { t:"AI for Impact: Data Monitoring & Evaluation", u:'/courses/devai/', o:'ML, NLP, computer vision for development; 13 modules.'},
    { t:"MEL for Development", u:'/courses/mel/', o:'Theory of change to adaptive learning; 13 modules + 65-term lexicon.'},
    { t:"Politics of Aspiration", u:'/courses/poa/', o:'RTI, NREGA, rights architecture; 13 modules + 60-term lexicon.'},
    { t:"Media for Development", u:'/courses/media/', o:'Ethical storytelling, humanitarian comms, participatory media, data journalism; 12 modules + 65-term lexicon.'}
  ];
  const LABS = (window.__MOJINI_LABS__) || [
    { t:'Risk Assessment and Mitigation Lab',  u:'/Labs/risk-mitigation-lab.html' },
    { t:'Resource Mobilisation and Sustainability Lab', u:'/Labs/resource-sustainability-lab.html' },
    { t:'Policy and Advocacy Lab',             u:'/Labs/policy-advocacy-lab.html' },
    { t:'Partnership and Collaboration Lab',   u:'/Labs/impact-partnerships-lab.html' },
    { t:'MLE Framework Workbench',             u:'/Labs/mel-design-lab.html' },
    { t:'MLE Framework Builder Lab',           u:'/Labs/mel-plan-lab.html' },
    { t:'Community Engagement Lab',            u:'/Labs/community-lab.html' },
    { t:'Impact Storytelling Lab',             u:'/Labs/storytelling-lab.html' },
    { t:'Innovation and Design Thinking Lab',  u:'/Labs/design-thinking-lab.html' },
    { t:'Gender Studies Lab',                  u:'/Labs/gender-studies-lab.html' },
    { t:'TOC Lab',                             u:'/Labs/toc-lab.html' }
  ];
  // expose once for other scripts if needed
  window.__MOJINI_COURSES__ = COURSES;
  window.__MOJINI_LABS__ = LABS;

  // "" "" "" Helpers "" "" "" 
  const norm = s => String(s||"").toLowerCase();
  const listCourses = () => COURSES.map(c=>`• ${c.t} — ${c.o}\n  ${c.u}`).join("\n");
  const listLabs = () => LABS.map(l=>`• ${l.t}\n  ${l.u}`).join("\n");
  const byTitle = (arr, text) => {
    const s = norm(text);
    return arr.find(x => s.includes(norm(x.t)) || norm(x.t).includes(s));
  };

  function replyBot(text){
    if (typeof window.addBotMessage === 'function') { window.addBotMessage(text); return; }
    const box = document.getElementById('chatMessages') || document.querySelector('.chat-messages');
    if (!box) return;
    const wrap = document.createElement('div'); wrap.className = 'message bot-message';
    const bub = document.createElement('div'); bub.className = 'bot-bubble'; bub.textContent = text;
    wrap.appendChild(bub); box.appendChild(wrap); box.scrollTop = box.scrollHeight;
  }

  // "" "" "" FAQ BANK (30+) "" "" "" 
  // Each item: {re: /pattern/i, a: "answer" }  (safe, non-inventive wording)
  const FAQ = [
    // Credentials / Certificates / Accreditation
    { re: /(certificate|certification)s?\b/i,
      a: "We don't issue formal certificates. ImpactMojo focuses on **skills and credentials** you can demonstrate via real work and portfolio artefacts." },
    { re: /\bcredential(s)?\b|\bbadge(s)?\b|\bportfolio\b/i,
      a: "Our credentials are skill signals based on doing work — labs, projects, and artefacts you can show. They're designed to be more meaningful than a generic certificate." },
    { re: /\baccredit(ed|ation)|academic credit|university|ugc\b/i,
      a: "ImpactMojo is not an accredited degree program and doesn't offer academic credit. It's a practitioner-focused learning platform." },

    // Premium / Pricing
    { re: /\bpremium\b(?!.*(what|include|benefit|price))/i,
      a: "Premium offers two tiers. **Practitioner** includes RQ Builder Pro, TOC Workbench Pro, certificates, and community access. **Professional** adds Qualitative Research Lab, Statistical Code Converter Pro, VaniScribe AI Transcription (10+ South Asian languages), DevData Practice (36 generators, 840k+ rows), Visualization Cookbook (14 chart types), and the DevEconomics Toolkit (11 Shiny apps). Field Notes from a Dev Economist is free for everyone. Visit the Premium page for details." },
    { re: /\b(what('| i)?s|about).+premium|\bpremium\b.+(include|cover|benefit)/i,
      a: "**Practitioner Tier** includes RQ Builder Pro, TOC Workbench Pro, completion certificates, and community access. **Professional Tier** adds Qual Research Lab, Code Converter Pro, VaniScribe AI Transcription, DevData Practice datasets, Visualization Cookbook, and the DevEconomics Toolkit with 11 interactive Shiny apps. Field Notes from a Dev Economist is free for all tiers. See the Premium page for current pricing." },
    { re: /\b(price|cost|fee|paid|free).+premium|\bpremium.+(price|cost|fee)/i,
      a: "Premium has two tiers: **Practitioner** and **Professional**. Pricing and full details are on the live Premium page. All 15 flagship courses, 101-level courses, labs, and games remain **free** forever." },

    // Courses (catalog, objectives, level, format)
    { re: /\b(list|show|see).+course(s)?\b|^\s*courses?\s*$/i,
      a: () => `Here are our core courses:\n\n${listCourses()}` },
    { re: /(which|what)\s+course(s)?\s+(do you have|are available)/i,
      a: () => `We currently offer:\n\n${listCourses()}` },
    { re: /(objective|about|overview|syllabus).+development economics|dev(\s|-)?econ/i,
      a: () => {
        const c = byTitle(COURSES, "Development Economics 101");
        return c ? `${c.t} — ${c.o}\n${c.u}` : "Development Economics 101 covers poverty, inequality and growth; see the course page for details.";
      }},
    { re: /(objective|about|overview|syllabus).+law/i,
      a: () => { const c = byTitle(COURSES,"Law and Constitution 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+climate/i,
      a: () => { const c = byTitle(COURSES,"Climate Science 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(pedagogy|education)/i,
      a: () => { const c = byTitle(COURSES,"Pedagogy and Education 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(public health|health)/i,
      a: () => { const c = byTitle(COURSES,"Public Health 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+livelihood/i,
      a: () => { const c = byTitle(COURSES,"Livelihoods 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+gender/i,
      a: () => { const c = byTitle(COURSES,"Gender Studies 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(WEE|women)/i,
      a: () => { const c = byTitle(COURSES,"Womens' Economic Empowerment 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(ethics|research ethics)/i,
      a: () => { const c = byTitle(COURSES,"Research Ethics 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(bcc|behaviour|behavior)/i,
      a: () => { const c = byTitle(COURSES,"Behaviour Change Communication Programming 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+advocacy/i,
      a: () => { const c = byTitle(COURSES,"Advocacy and Communications 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(monitoring|evaluation|meal)\b/i,
      a: () => { const c = byTitle(COURSES,"Monitoring, Evaluation, Accountability and Learning 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+ethnograph/i,
      a: () => { const c = byTitle(COURSES,"Visual Ethnography 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(political economy|pol.?econ)/i,
      a: () => { const c = byTitle(COURSES,"Political Economy 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(poverty|inequality)/i,
      a: () => { const c = byTitle(COURSES,"Poverty and Inequality 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(data vis|datavis|visuali[sz]ation)/i,
      a: () => { const c = byTitle(COURSES,"Data Visualisation 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(mixed methods|mmr)/i,
      a: () => { const c = byTitle(COURSES,"Mixed Methods Research 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(impact eval|evaluation design)/i,
      a: () => { const c = byTitle(COURSES,"Impact Evaluation Design 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+fundraising/i,
      a: () => { const c = byTitle(COURSES,"Fundraising 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+programme design/i,
      a: () => { const c = byTitle(COURSES,"Programme Design Principles 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(environmental justice|env\.?justice)/i,
      a: () => { const c = byTitle(COURSES,"Environmental Justice 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(digital gov|governance)/i,
      a: () => { const c = byTitle(COURSES,"Digital Governance 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(nutrition|food)/i,
      a: () => { const c = byTitle(COURSES,"Nutrition, Food Systems & Culture 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(social research ethics|consent)/i,
      a: () => { const c = byTitle(COURSES,"Social Research Ethics & Consent 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(language|history of languages)/i,
      a: () => { const c = byTitle(COURSES,"Language & History of Languages 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+caste/i,
      a: () => { const c = byTitle(COURSES,"Caste 101"); return `${c.t} — ${c.o}\n${c.u}`; } },
    { re: /(objective|about|overview|syllabus).+(humanitarian|development work)/i,
      a: () => { const c = byTitle(COURSES,"Humanitarian vs Development Work 101"); return `${c.t} — ${c.o}\n${c.u}`; } },

    { re: /(beginner|new to this|where to start)/i,
      a: "Start with any **101** course. They're beginner-friendly and focus on practical understanding." },
    { re: /(advanced|deeper|next step)/i,
      a: "For deeper work, explore **labs** and **Premium** deeper-dives." },
    { re: /(duration|time|how long).+course/i,
      a: "Most courses are **self-paced**. Time varies by learner — check each course page for modules and suggested pace." },
    { re: /\blive\b.+(class|session|cohort)/i,
      a: "Most learning is self-paced. When live/cohort options are offered, the course page will say so." },
    { re: /enrol|enroll|join|sign ?up/i,
      a: "Open the course you want and follow the on-page steps. Some items are open access; others may prompt you to sign in." },

    // Labs
    { re: /\b(list|show).+lab(s)?\b|^\s*labs?\s*$/i,
      a: () => `Here are our labs:\n\n${listLabs()}` },
    { re: /\bTOC\b|\btheor(y|ies) of change\b/i,
      a: () => `**TOC Lab** helps you structure a Theory of Change quickly and clearly.\n/Labs/toc-lab.html` },
    { re: /MLE (framework|builder|workbench)/i,
      a: () => `The **MLE Framework Workbench/Builder** help you design monitoring & learning frameworks.\nWorkbench: /Labs/mel-design-lab.html\nBuilder:   /Labs/mel-plan-lab.html` },
    { re: /how (to )?access.+lab|use.+lab/i,
      a: "Labs are web tools. Click a lab link and start; most open directly in your browser." },

    // Resources / Games / Testimonials / Ratings / Founders
    { re: /resource(s)?|reading list|tool(s)?|template(s)?/i,
      a: "Resources include reading lists, tools, data links, and templates referenced across courses and labs." },
    { re: /\bgame(s)?\b|interactive/i,
      a: "Games are short, interactive learning modules that reinforce key ideas in a playful way." },
    { re: /(testimonial|review|what people say)/i,
      a: "Testimonials are showcased on-site when available. You can also leave feedback here and we may feature excerpts." },
    { re: /rating(s)?|stars?/i,
      a: "Ratings vary by context. Where available, they appear with the relevant course or lab — Mojini avoids quoting numbers out of context." },
    { re: /founder|who.*(behind|lead)/i,
      a: "ImpactMojo is led by **Dr. Varna Sri Raman**. (Additional leadership may be featured on the site.)" },

    // Access, language, privacy, support
    { re: /\bmobile|phone|tablet|responsive\b/i,
      a: "ImpactMojo works on modern browsers across desktop and mobile. For the best experience, keep your browser up to date." },
    { re: /\blanguage(s)?\b|hindi|translation/i,
      a: "Content is primarily in **English**. Additional language options may be added over time." },
    { re: /privacy|data|gdpr/i,
      a: "We respect your privacy. Feedback is used to improve ImpactMojo. Please refer to the site's Privacy/Terms pages for details." },
    { re: /(support|help|contact|reach|email)/i,
      a: "For support, use this chat's **Report Bug** or **Feature Request** options. We'll follow up using the info you provide." },
    { re: /(suggest|request).+course/i,
      a: "Use the **Suggest Course** shortcut here in chat to propose a new course or topic." },

    // Services: Dojos, Workshops, Coaching
    { re: /\bdojo(s)?\b/i,
      a: "**Dojos** are practice-based skill sessions: 90-minute cohort workshops that build practitioner skills through doing. Topics include pre-mortems, stakeholder mapping, cost-effectiveness analysis, and 32+ other techniques. ₹1,500 per session in Delhi, Bangalore, or online. Check the **Dojos** page under Services." },
    { re: /\bworkshop(s)?\b/i,
      a: "We offer **Workshops** like the Three-Day MEAL Intensive and Theory of Change Design Sprint. For organizations, we provide custom training on any ImpactMojo topic. Check the **Workshops** page under Services." },
    { re: /\bcoaching\b/i,
      a: "**Coaching** includes one-on-one sessions with Dr. Varna (career counseling, research design) and Vandana (social media strategy). Check the **Coaching** page under Services to book a session." },
    { re: /(service|what do you offer|training|consulting)/i,
      a: "ImpactMojo offers **Courses** (self-paced learning), **Labs** (hands-on tools), **Coaching** (1:1 sessions), **Workshops** (group training), and **Dojos** (practice-based skill sessions). Explore the Services menu!" },

    // Org / team use
    { re: /(organization|organisation|team|ngo|gov|company)/i,
      a: "ImpactMojo is designed for practitioners and teams. Courses build foundations; labs help teams design, test, and improve programs." },

    // WhatsApp PLC
    { re: /whatsapp|plc|community|peer.*learn/i,
      a: "Join our **WhatsApp Professional Learning Community**! Connect with practitioners, researchers, and changemakers across South Asia. Share resources, discuss fieldwork challenges, and grow together. Look for the green WhatsApp section on the homepage." },

    // Flagship count
    { re: /how many.*course|flagship|all.*course/i,
      a: () => "We have **15 flagship courses** (Gandhi, DevEcon, DataViz, AI for Impact, MEL, Politics of Aspiration, Media for Development, Constitution & Law, Social-Emotional Learning, Livelihoods, Gender, Public Choice, Public Policy, Causal Inference, and Power BI) plus **47 foundational courses**. Each flagship includes 12-13 modules, interactive lexicons, AI companions, and coach callouts.\n\n" + listCourses() },

    // PoA specific
    { re: /poa|politics.*aspiration|nrega|rti|nfsa|forest.*right/i,
      a: () => { const c = byTitle(COURSES,"Politics of Aspiration"); return "**" + c.t + "**: 13 modules covering NREGA, RTI, NFSA, and Forest Rights Act. 60-term interactive lexicon.\n" + c.u; } },

    // Media specific
    { re: /media.*dev|development.*media|journalism|humanitarian.*comm/i,
      a: () => { const c = byTitle(COURSES,"Media for Development"); return "**" + c.t + "**: 12 modules covering ethics, P. Sainath, Khabar Lahariya, Video Volunteers, data journalism. 65-term lexicon.\n" + c.u; } },

    // ImpactLex
    { re: /impactlex|glossary|dictionary|terminology|acronym/i,
      a: "**ImpactLex** is our searchable glossary with 500+ development terms, acronyms, formulas, and case studies. Features 'Finance Word of the Day'. Visit: https://on-web.link/ImpactLex" },

    // FieldCases Library
    { re: /fieldcases|case.?stud|evidence.*library|cited.*research|country.*studies|dev.*case/i,
      a: "**FieldCases** is our free, searchable library of 200 cited development case studies from 117 countries. Covers financial inclusion, health, education, governance, and more across 10 topics and 7 regions. Every claim is grounded in published research. Browse it at: https://varnasr.github.io/dev-case-studies/" },

    // Development Discourses
    { re: /dev.*discourse|discourse|open.?access.*paper|research.*paper|grey.*lit|academic.*library|curated.*library|research.*library/i,
      a: "**Development Discourses** is a curated open-access library of 500+ research papers, books, and grey literature on development, social impact, and public policy. Searchable by topic, type, author, and keyword. Covers MEL, gender justice, climate resilience, data governance, public health, livelihoods, and more. Prioritizes open-access resources so you can read, cite, and share without paywalls. Explore it at: https://on-web.link/DevDiscourses" },

    // DevData Practice
    { re: /devdata|dataset|data.*practice|realistic.*data|household.*survey|rct.*data/i,
      a: "**DevData Practice** is our premium resource with 36 realistic dataset generators producing 840k+ rows of development economics data. Covers household surveys, RCTs, health, education, agriculture, gender, climate, WASH, humanitarian, IRT psychometrics, and more. Includes practice exercises. Visit: https://impactmojo-devdata-pro.netlify.app/" },
    // Constitution & Law
    { re: /constitution|law.*course|pil|article.*21|fundamental.*right|basic.*structure|rights.*based/i,
      a: "**Constitution & Law for Development Practice** is our flagship course on rights, institutions and justice in South Asia. 13 modules covering the Indian Constitution, fundamental rights, PIL, Article 21, reservations, rights-based legislation, criminal justice, environmental law, digital rights, and comparative constitutional systems. Visit: /courses/law/" },
    // Social-Emotional Learning
    { re: /sel|social.*emotional|practitioner.*wellbeing|facilitation.*skill|conflict.*resolution|reflective.*practice/i,
      a: "**Social-Emotional Learning for Practitioners** is our flagship course on practitioner wellbeing, burnout prevention, empathy, resilience, facilitation skills, conflict resolution, and reflective practice. 13 modules with 55+ term interactive lexicon. Visit: /courses/sel/" },
    // VaniScribe
    { re: /vaniscribe|transcri|field.*interview|fgd.*transcri|kii.*transcri|south.*asian.*language|sarvam|diarization/i,
      a: "**VaniScribe** is our premium AI transcription tool for development researchers. Transcribe field interviews, FGDs, and KIIs in Hindi, Tamil, Bengali, and 10+ South Asian languages using Sarvam AI. Features speaker diarization, auto-timestamping, and export to structured formats for qualitative analysis. Visit: /premium.html" },
    // Visualization Cookbook
    { re: /viz.*cookbook|visualization.*cookbook|chart.*recipe|chart.*type|python.*chart|data.*viz.*code/i,
      a: "The **Visualization Cookbook** is a premium resource with 14 chart types and production-ready Python code. Question-driven: pick the story your data tells (comparison, distribution, relationship, composition, time series, spatial) and get the right chart with code. Part of DevData Practice. Visit: https://impactmojo-devdata-pro.netlify.app/charts.html" },
    { re: /deveconomics.*toolkit|shiny.*app|rct.*power|did.*simulator|rdd.*explorer|synthetic.*control|gini.*tool|mpi.*explorer|logframe|wdi.*dashboard|poverty.*line.*analysis|cost.*benefit.*tool/i,
      a: "**DevEconomics Toolkit** is our premium collection of 11 interactive Shiny apps for development economics. Includes RCT power calculator, DiD simulator, RDD explorer, synthetic control visualizer, Gini and Lorenz curve tool, MPI explorer, poverty line analysis, Theory of Change visualizer, cost-benefit analysis tool, LogFrame builder, and WDI dashboard. Visit: https://impactmojo-devecon-toolkit.netlify.app/" }
  ];

  // Dynamic course objective matcher (covers "What's the objective of X?"  without listing all regexes)
  function tryCourseObjective(text){
    const s = norm(text);
    if (!/(objective|about|overview|syllabus|what is)/i.test(text)) return null;
    // Find best matching course title token
    let best = null, bestScore = 0;
    COURSES.forEach(c => {
      const title = norm(c.t);
      let score = 0;
      title.split(/\s+/).forEach(tok => { if (tok && s.includes(tok)) score++; });
      if (score > bestScore) { bestScore = score; best = c; }
    });
    if (best && bestScore >= 2) return `${best.t} — ${best.o}\n${best.u}`;
    return null;
  }

  // Main answerer: bank -> dynamic course objective -> (optional) existing mojiniAnswer -> fallback null
  function answerFromFAQ(userText){
    const text = String(userText||"");
    // 1) Hardcoded bank
    for (const item of FAQ) {
      if (item.re.test(text)) {
        const out = (typeof item.a === "function") ? item.a(text) : item.a;
        return out;
      }
    }
    // 2) Dynamic course objective
    const dyn = tryCourseObjective(text);
    if (dyn) return dyn;

    // 3) If an earlier global answerer exists, let it try next (keeps compatibility)
    if (typeof window.mojiniAnswer === "function") {
      const maybe = window.mojiniAnswer(text);
      if (maybe) return maybe;
    }
    return null;
  }

  // Expose so other blocks (wrappers) can use it too
  window.mojiniAnswer = answerFromFAQ;

  // Handle KB chips: answer first and stop propagation so we don't double-reply
  window.addEventListener("immojo:user", function(e){
    const q = e?.detail?.text || "";
    if (!q) return;
    const a = answerFromFAQ(q);
    if (a) {
      replyBot(a);
      // avoid duplicate responses from other listeners
      if (e.stopImmediatePropagation) e.stopImmediatePropagation();
    }
  }, true); // capture first

  // Wrap current sendMessage again (without breaking the existing fallback chain)
  const __prevSend = window.sendMessage;
  window.sendMessage = function(){
    const inp = document.getElementById("chatInput");
    const text = (inp?.value || "").trim();
    if (!text) return;
    const a = answerFromFAQ(text);
    if (a) {
      if (typeof window.addUserMessage === "function") window.addUserMessage(text);
      replyBot(a);
      if (inp) inp.value = "";
      return;
    }
    // Not matched -> pass through to whatever was there before
    if (typeof __prevSend === "function") return __prevSend.apply(this, arguments);
  };
})();
