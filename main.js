// ImpactMojo 101 - Complete Application with All Features
// Includes: Course & Lab bookmarking, comparison, sophisticated content analysis, beautiful modals

console.log('🚀 Loading complete ImpactMojo with all features...');

// ===== GLOBAL STATE VARIABLES =====
let allCourses = [...courses];
let filteredCourses = [...courses];
let selectedCourses = [];
let selectedLabs = [];
let currentView = 'grid';
let currentCategory = 'All Courses';
let currentDifficulty = '';

// Firebase auth variables (managed by firebase-auth.js)
// currentUser, userBookmarks, userLabBookmarks

// ===== INITIALIZATION =====

function initializeApp() {
  console.log('📚 Initializing complete ImpactMojo...');
  
  displayCourses();
  displayLabsWithFullFeatures();
  updateCourseCount();
  setupEventListeners();
  addComprehensiveStyles();
  
  console.log('✅ Complete ImpactMojo ready with all features!');
}

// ===== COMPREHENSIVE STYLING =====

function addComprehensiveStyles() {
  const style = document.createElement('style');
  style.textContent = `
    /* ===== BEAUTIFUL COURSE MODAL STYLING ===== */
    .course-card.expanded {
      position: fixed !important;
      top: 50% !important;
      left: 50% !important;
      transform: translate(-50%, -50%) !important;
      width: 90% !important;
      max-width: 700px !important;
      max-height: 80vh !important;
      z-index: 10000 !important;
      background: white !important;
      border-radius: 16px !important;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4) !important;
      overflow-y: auto !important;
      padding: 0 !important;
      animation: modalSlideIn 0.3s ease !important;
    }
    
    /* Beautiful modal backdrop */
    .course-card.expanded::before {
      content: '' !important;
      position: fixed !important;
      top: 0 !important;
      left: 0 !important;
      width: 100vw !important;
      height: 100vh !important;
      background: rgba(0, 0, 0, 0.7) !important;
      z-index: -1 !important;
      backdrop-filter: blur(8px) !important;
    }
    
    /* Compact course header */
    .course-card.expanded .course-header {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
      color: white !important;
      padding: 20px 80px 20px 20px !important;
      border-radius: 16px 16px 0 0 !important;
      position: relative !important;
    }
    
    .course-card.expanded .course-title {
      color: white !important;
      font-size: 1.5rem !important;
      margin: 0 !important;
      font-weight: 600 !important;
    }
    
    /* Compact content sections */
    .course-card.expanded .course-description {
      padding: 16px 20px !important;
      margin: 0 !important;
      font-size: 1rem !important;
      line-height: 1.5 !important;
      background: #f8fafc !important;
      border-bottom: 1px solid #e2e8f0 !important;
    }
    
    .course-card.expanded .course-stats {
      padding: 12px 20px !important;
      background: white !important;
      display: flex !important;
      gap: 24px !important;
      border-bottom: 1px solid #e2e8f0 !important;
    }
    
    .course-card.expanded .course-details {
      padding: 20px !important;
      background: white !important;
    }
    
    .course-card.expanded .details-section {
      margin-bottom: 16px !important;
    }
    
    .course-card.expanded .details-section h4 {
      color: #667eea !important;
      font-size: 1.1rem !important;
      margin-bottom: 8px !important;
      font-weight: 600 !important;
    }
    
    .course-card.expanded .details-section ul {
      margin: 0 !important;
      padding-left: 16px !important;
    }
    
    .course-card.expanded .details-section li {
      margin-bottom: 4px !important;
      line-height: 1.4 !important;
    }
    
    /* Perfect button positioning */
    .course-card.expanded .close-expanded {
      position: absolute !important;
      top: 15px !important;
      right: 15px !important;
      width: 32px !important;
      height: 32px !important;
      background: rgba(255, 255, 255, 0.9) !important;
      color: #667eea !important;
      border: none !important;
      border-radius: 50% !important;
      cursor: pointer !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      font-size: 18px !important;
      z-index: 10001 !important;
      transition: all 0.2s ease !important;
    }
    
    .course-card.expanded .close-expanded:hover {
      background: #dc3545 !important;
      color: white !important;
      transform: scale(1.1) !important;
    }
    
    .course-card.expanded .bookmark-btn {
      position: absolute !important;
      top: 15px !important;
      right: 55px !important;
      width: 32px !important;
      height: 32px !important;
      z-index: 10000 !important;
      background: rgba(255, 255, 255, 0.9) !important;
      border: none !important;
      border-radius: 50% !important;
      color: #ffc107 !important;
    }
    
    .course-card.expanded .bookmark-btn.bookmarked {
      background: #ffc107 !important;
      color: white !important;
    }
    
    @keyframes modalSlideIn {
      from { 
        opacity: 0; 
        transform: translate(-50%, -50%) scale(0.9); 
      }
      to { 
        opacity: 1; 
        transform: translate(-50%, -50%) scale(1); 
      }
    }
    
    /* ===== BEAUTIFUL LAB CARDS - MATCHING COURSE CARD DESIGN ===== */
    #labsContainer {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
      gap: 1.5rem;
      margin-top: 2rem;
    }
    
    .lab-card {
      background: var(--card-bg, white);
      border-radius: var(--border-radius, 12px);
      padding: 1.5rem;
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      transition: all 0.3s ease;
      border: 1px solid var(--border-color, #e2e8f0);
      position: relative;
      overflow: hidden;
      cursor: pointer;
    }
    
    /* Beautiful green border for labs */
    .lab-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, #48bb78, #38a169);
    }
    
    .lab-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    /* Prominent LIVE status indicator - like course number */
    .lab-status-indicator {
      position: absolute;
      top: 1rem;
      right: 1rem;
      z-index: 2;
    }
    
    .live-badge {
      background: linear-gradient(135deg, #48bb78, #38a169);
      color: white;
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      box-shadow: 0 2px 8px rgba(72, 187, 120, 0.3);
      animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
      0% { box-shadow: 0 2px 8px rgba(72, 187, 120, 0.3); }
      50% { box-shadow: 0 4px 16px rgba(72, 187, 120, 0.5); }
      100% { box-shadow: 0 2px 8px rgba(72, 187, 120, 0.3); }
    }
    
    /* Lab header matching course header */
    .lab-header {
      display: flex;
      gap: 1rem;
      align-items: flex-start;
      margin-bottom: 1rem;
      margin-right: 4rem; /* Space for LIVE badge */
    }
    
    .lab-icon {
      font-size: 2rem;
      color: #48bb78;
      flex-shrink: 0;
    }
    
    .lab-title-section {
      flex: 1;
    }
    
    .lab-title {
      color: var(--text-primary, #2d3748);
      font-size: 1.25rem;
      margin: 0 0 0.5rem 0;
      font-weight: 600;
      line-height: 1.3;
    }
    
    /* Lab meta tags matching course meta */
    .lab-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 1rem;
    }
    
    .lab-category-tag {
      background: #e6fffa;
      color: #234e52;
      padding: 0.25rem 0.75rem;
      border-radius: 1rem;
      font-size: 0.8rem;
      font-weight: 500;
    }
    
    .lab-status-tag {
      background: #d4edda;
      color: #155724;
      padding: 0.25rem 0.75rem;
      border-radius: 1rem;
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
    }
    
    /* Lab description matching course description */
    .lab-description {
      color: var(--text-secondary, #4a5568);
      margin-bottom: 1rem;
      line-height: 1.5;
      font-size: 0.95rem;
    }
    
    /* Lab actions matching course actions */
    .lab-actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 1rem;
    }
    
    .lab-actions-left {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    
    .lab-actions-right {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    
    /* Lab launch button matching course launch button */
    .lab-launch-btn {
      background: #48bb78;
      color: white;
      padding: 0.75rem 1.5rem;
      border: none;
      border-radius: 0.5rem;
      text-decoration: none;
      font-weight: 500;
      transition: all 0.3s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.9rem;
    }
    
    .lab-launch-btn:hover {
      background: #38a169;
      text-decoration: none;
      color: white;
      transform: translateY(-1px);
    }
    
    /* Lab bookmark button matching course bookmark */
    .lab-bookmark-btn {
      background: none;
      border: 1px solid var(--border-color, #d1d5db);
      color: var(--text-secondary, #6b7280);
      padding: 0.5rem;
      border-radius: 0.5rem;
      cursor: pointer;
      transition: all 0.3s ease;
      font-size: 1rem;
    }
    
    .lab-bookmark-btn:hover {
      border-color: #fbbf24;
      color: #fbbf24;
    }
    
    .lab-bookmark-btn.bookmarked {
      border-color: #f59e0b;
      color: #f59e0b;
      background: #fef3c7;
    }
    
    /* Lab expand button matching course expand */
    .lab-expand-btn {
      background: none;
      border: 1px solid var(--primary-color, #667eea);
      color: var(--primary-color, #667eea);
      padding: 0.5rem 1rem;
      border-radius: 0.5rem;
      cursor: pointer;
      font-size: 0.9rem;
      transition: all 0.3s ease;
    }
    
    .lab-expand-btn:hover {
      background: var(--primary-color, #667eea);
      color: white;
    }
    
    /* Lab details matching course details */
    .lab-details {
      padding: 1.5rem;
      background: var(--light-bg, #f8fafc);
      border-top: 1px solid var(--border-color, #e2e8f0);
      display: none;
      margin: 1rem -1.5rem -1.5rem -1.5rem;
      border-radius: 0 0 12px 12px;
    }
    
    .lab-card.expanded .lab-details {
      display: block;
    }
    
    /* Lab expanded modal styling */
    .lab-card.expanded {
      position: fixed !important;
      top: 50% !important;
      left: 50% !important;
      transform: translate(-50%, -50%) !important;
      width: 90% !important;
      max-width: 600px !important;
      max-height: 80vh !important;
      z-index: 10000 !important;
      background: white !important;
      border-radius: 16px !important;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4) !important;
      overflow-y: auto !important;
      animation: modalSlideIn 0.3s ease !important;
    }
    
    /* Lab modal backdrop */
    .lab-card.expanded::before {
      content: '' !important;
      position: fixed !important;
      top: 0 !important;
      left: 0 !important;
      width: 100vw !important;
      height: 100vh !important;
      background: rgba(0, 0, 0, 0.7) !important;
      z-index: -1 !important;
      backdrop-filter: blur(8px) !important;
    }
    
    .lab-card.expanded .lab-header {
      background: linear-gradient(135deg, #48bb78, #38a169) !important;
      color: white !important;
      padding: 20px !important;
      border-radius: 16px 16px 0 0 !important;
      margin: -1.5rem -1.5rem 1rem -1.5rem !important;
    }
    
    .lab-card.expanded .lab-title {
      color: white !important;
    }
    
    .lab-card.expanded .lab-icon {
      color: white !important;
    }
    
    /* ===== COMPARISON BUTTONS ===== */
    .compare-btn, .lab-compare-btn {
      display: none;
      align-items: center;
      gap: 8px;
      background: #9f7aea;
      color: white;
      padding: 12px 20px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-weight: 600;
      font-size: 14px;
      transition: all 0.3s ease;
      margin: 0 auto;
    }
    
    .compare-btn.active, .lab-compare-btn.active {
      display: inline-flex;
    }
    
    .compare-btn:hover, .lab-compare-btn:hover {
      background: #805ad5;
      transform: translateY(-1px);
    }
    
    .lab-compare-btn {
      background: #48bb78;
    }
    
    .lab-compare-btn:hover {
      background: #38a169;
    }
    
    /* ===== SOPHISTICATED COMPARISON MODAL ===== */
    .comparison-modal {
      background: white;
      border-radius: 16px;
      padding: 0;
      max-width: 95vw;
      max-height: 90vh;
      overflow-y: auto;
    }
    
    .comparison-header {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 20px 24px;
      border-radius: 16px 16px 0 0;
    }
    
    .comparison-header h2 {
      margin: 0;
      font-size: 1.5rem;
      font-weight: 600;
    }
    
    .comparison-content {
      padding: 24px;
    }
    
    .comparison-overview {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 32px;
    }
    
    .comparison-course-card {
      background: #f8fafc;
      border-radius: 12px;
      padding: 16px;
      border: 2px solid #e2e8f0;
    }
    
    .comparison-course-title {
      color: #667eea;
      font-weight: 600;
      margin-bottom: 8px;
    }
    
    .comparison-quick-stats {
      font-size: 14px;
      color: #6b7280;
    }
    
    .detailed-comparison {
      margin-bottom: 32px;
    }
    
    .comparison-section {
      margin-bottom: 32px;
    }
    
    .comparison-section h3 {
      color: #2d3748;
      font-size: 1.25rem;
      margin-bottom: 16px;
      padding-bottom: 8px;
      border-bottom: 2px solid #e2e8f0;
    }
    
    .comparison-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
      margin-bottom: 24px;
    }
    
    .comparison-table th,
    .comparison-table td {
      padding: 12px;
      text-align: left;
      border: 1px solid #e2e8f0;
      vertical-align: top;
    }
    
    .comparison-table th {
      background: #f8fafc;
      font-weight: 600;
      color: #2d3748;
    }
    
    .content-depth-analysis {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin: 24px 0;
    }
    
    .depth-card {
      background: white;
      border: 2px solid #e2e8f0;
      border-radius: 12px;
      padding: 16px;
    }
    
    .depth-card h4 {
      color: #667eea;
      margin: 0 0 12px 0;
      font-size: 1.1rem;
    }
    
    .depth-indicator {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }
    
    .depth-bar {
      flex: 1;
      height: 8px;
      background: #e2e8f0;
      border-radius: 4px;
      overflow: hidden;
    }
    
    .depth-fill {
      height: 100%;
      background: linear-gradient(90deg, #48bb78, #38a169);
      transition: width 0.3s ease;
    }
    
    .overlap-analysis {
      background: #f0f9ff;
      border: 2px solid #0ea5e9;
      border-radius: 12px;
      padding: 20px;
      margin: 24px 0;
    }
    
    .overlap-analysis h3 {
      color: #0ea5e9;
      margin: 0 0 16px 0;
    }
    
    .overlap-items {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    
    .overlap-tag {
      background: #0ea5e9;
      color: white;
      padding: 4px 8px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 500;
    }
    
    .comparison-actions {
      display: flex;
      gap: 12px;
      justify-content: center;
      padding: 20px 24px;
      background: #f8fafc;
      border-radius: 0 0 16px 16px;
      border-top: 1px solid #e2e8f0;
    }
    
    .btn-primary, .btn-secondary {
      padding: 12px 24px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.3s ease;
    }
    
    .btn-primary {
      background: #667eea;
      color: white;
    }
    
    .btn-primary:hover {
      background: #5a6fd8;
      transform: translateY(-1px);
    }
    
    .btn-secondary {
      background: #e2e8f0;
      color: #2d3748;
    }
    
    .btn-secondary:hover {
      background: #cbd5e0;
    }
  `;
  
  document.head.appendChild(style);
}

// ===== COURSE DISPLAY WITH FULL FEATURES =====

function displayCourses() {
  const container = document.getElementById('courseContainer');
  const noResults = document.getElementById('noResults');
  
  if (!container) return;
  
  if (filteredCourses.length === 0) {
    container.innerHTML = '';
    if (noResults) noResults.classList.remove('hidden');
    return;
  }
  
  if (noResults) noResults.classList.add('hidden');
  
  container.className = currentView === 'grid' ? 'courses-grid' : 'courses-list';
  container.innerHTML = filteredCourses.map(course => createCourseCard(course)).join('');
  
  updateComparisonUI();
}

function createCourseCard(course) {
  const isBookmarked = window.userBookmarks && userBookmarks.includes(course.id);
  const isSelected = selectedCourses.includes(course.id);
  
  return `
    <div class="course-card" data-course-id="${course.id}">
      <div class="course-number">${course.number}</div>
      
      <div class="course-header" onclick="toggleCourseDetails('${course.id}')">
        <div class="course-icon">
          <i class="${course.icon}"></i>
        </div>
        <div class="course-title-section">
          <h4 class="course-title">${course.title}</h4>
          <div class="course-meta">
            <span class="meta-tag">${course.category}</span>
            <span class="meta-tag difficulty ${course.difficulty}">${course.difficulty}</span>
            <span class="meta-tag">${course.duration}</span>
          </div>
        </div>
      </div>
      
      <div class="course-description">${course.description}</div>
      
      <div class="course-stats">
        <div class="course-stat">
          <i class="fas fa-users"></i>
          <span class="number">${course.learnerCount.toLocaleString()}</span> learners
        </div>
        <div class="course-stat">
          <i class="fas fa-star"></i>
          <span class="number">${course.rating}</span> rating
        </div>
      </div>
      
      <div class="course-actions">
        <div class="course-actions-left">
          <a href="${course.url}" target="_blank" rel="noopener" class="launch-btn">
            <i class="fas fa-external-link-alt"></i> Launch Course
          </a>
          <button class="bookmark-btn ${isBookmarked ? 'bookmarked' : ''}" 
                  onclick="toggleBookmark('${course.id}')" 
                  title="${isBookmarked ? 'Remove bookmark' : 'Bookmark course'}">
            <i class="${isBookmarked ? 'fas' : 'far'} fa-bookmark"></i>
          </button>
        </div>
        <div class="course-actions-right">
          <input type="checkbox" id="compare-${course.id}" 
                 ${isSelected ? 'checked' : ''} 
                 onchange="toggleCourseSelection('${course.id}')"
                 aria-label="Select for comparison">
          <label for="compare-${course.id}" class="compare-checkbox">Compare</label>
          <button class="expand-btn" onclick="toggleCourseDetails('${course.id}')" 
                  title="Show details">
            <i class="fas fa-chevron-down"></i>
          </button>
        </div>
      </div>
      
      <div class="course-details" id="details-${course.id}">
        <button class="close-expanded" onclick="closeCourseDetails('${course.id}')" title="Close details">×</button>
        
        <div class="details-section">
          <h4>Prerequisites</h4>
          <ul>
            ${course.prerequisites.map(prereq => `<li>${prereq}</li>`).join('')}
          </ul>
        </div>
        
        <div class="details-section">
          <h4>Learning Outcomes</h4>
          <ul>
            ${course.outcomes.map(outcome => `<li>${outcome}</li>`).join('')}
          </ul>
        </div>
        
        <div class="details-section">
          <h4>Target Audience</h4>
          <p>${course.audience}</p>
        </div>
      </div>
    </div>
  `;
}

function closeCourseDetails(courseId) {
  const detailsElement = document.getElementById(`details-${courseId}`);
  const card = document.querySelector(`[data-course-id="${courseId}"]`);
  const expandBtn = card.querySelector('.expand-btn i');
  
  detailsElement.style.display = 'none';
  expandBtn.className = 'fas fa-chevron-down';
  card.classList.remove('expanded');
}

// ===== LABS WITH FULL FEATURES =====

function displayLabsWithFullFeatures() {
  const container = document.getElementById('labsContainer');
  if (!container) return;
  
  container.innerHTML = labs.map(lab => createLabCardWithFeatures(lab)).join('');
  
  // Add lab comparison button to labs section
  addLabComparisonButton();
}

function createLabCardWithFeatures(lab) {
  const isBookmarked = window.userLabBookmarks && userLabBookmarks.includes(lab.id);
  const isSelected = selectedLabs.includes(lab.id);
  
  return `
    <div class="lab-card" data-lab-id="${lab.id}">
      <!-- Beautiful status indicator like course number -->
      <div class="lab-status-indicator">
        <span class="live-badge">LIVE</span>
      </div>
      
      <div class="lab-header" onclick="toggleLabDetails('${lab.id}')">
        <div class="lab-icon">
          <i class="${lab.icon}"></i>
        </div>
        <div class="lab-title-section">
          <h4 class="lab-title">${lab.title}</h4>
          <div class="lab-meta">
            <span class="meta-tag lab-category-tag">${lab.category}</span>
            <span class="meta-tag lab-status-tag">${lab.status}</span>
          </div>
        </div>
      </div>
      
      <div class="lab-description">${lab.description}</div>
      
      <div class="lab-actions">
        <div class="lab-actions-left">
          <a href="${lab.url}" target="_blank" rel="noopener" class="launch-btn lab-launch-btn">
            <i class="fas fa-external-link-alt"></i> Launch Lab
          </a>
          <button class="bookmark-btn lab-bookmark-btn ${isBookmarked ? 'bookmarked' : ''}" 
                  onclick="toggleLabBookmark('${lab.id}')" 
                  title="${isBookmarked ? 'Remove bookmark' : 'Bookmark lab'}">
            <i class="${isBookmarked ? 'fas' : 'far'} fa-bookmark"></i>
          </button>
        </div>
        <div class="lab-actions-right">
          <input type="checkbox" id="compare-lab-${lab.id}" 
                 ${isSelected ? 'checked' : ''} 
                 onchange="toggleLabSelection('${lab.id}')"
                 aria-label="Select lab for comparison">
          <label for="compare-lab-${lab.id}" class="compare-checkbox">Compare</label>
          <button class="expand-btn lab-expand-btn" onclick="toggleLabDetails('${lab.id}')" 
                  title="Show details">
            <i class="fas fa-chevron-down"></i>
          </button>
        </div>
      </div>
      
      <div class="lab-details" id="lab-details-${lab.id}">
        <div class="details-section">
          <h4>Category</h4>
          <p>${lab.category}</p>
        </div>
        
        <div class="details-section">
          <h4>Tool Features</h4>
          <ul>
            <li>Interactive web-based interface</li>
            <li>Real-time data processing</li>
            <li>Export and sharing capabilities</li>
            <li>Professional-grade outputs</li>
          </ul>
        </div>
        
        <div class="details-section">
          <h4>Best For</h4>
          <p>Development practitioners, researchers, and program managers working in ${lab.category.toLowerCase()}</p>
        </div>
      </div>
    </div>
  `;
}

function toggleLabDetails(labId) {
  const detailsElement = document.getElementById(`lab-details-${labId}`);
  const card = document.querySelector(`[data-lab-id="${labId}"]`);
  const expandBtn = card.querySelector('.lab-expand-btn i');
  
  if (detailsElement.style.display === 'block') {
    detailsElement.style.display = 'none';
    expandBtn.className = 'fas fa-chevron-down';
    card.classList.remove('expanded');
  } else {
    detailsElement.style.display = 'block';
    expandBtn.className = 'fas fa-chevron-up';
    card.classList.add('expanded');
  }
}

function closeLabDetails(labId) {
  const detailsElement = document.getElementById(`lab-details-${labId}`);
  const card = document.querySelector(`[data-lab-id="${labId}"]`);
  const expandBtn = card.querySelector('.lab-expand-btn i');
  
  detailsElement.style.display = 'none';
  expandBtn.className = 'fas fa-chevron-down';
  card.classList.remove('expanded');
}

function addLabComparisonButton() {
  const labsSection = document.querySelector('.labs-section .container');
  if (!labsSection || document.getElementById('labCompareBtn')) return;
  
  const buttonContainer = document.createElement('div');
  buttonContainer.style.textAlign = 'center';
  buttonContainer.style.marginTop = '20px';
  buttonContainer.innerHTML = `
    <button class="lab-compare-btn" id="labCompareBtn" onclick="showLabComparison()">
      <i class="fas fa-balance-scale"></i> Compare Selected Labs (<span id="labCompareCount">0</span>)
    </button>
  `;
  
  labsSection.appendChild(buttonContainer);
}

// ===== LAB FUNCTIONALITY =====

function toggleLabBookmark(labId) {
  if (!window.currentUser) {
    showNotification('Please log in to bookmark labs', 'error');
    openModal('loginModal');
    return;
  }
  
  if (!window.userLabBookmarks) {
    window.userLabBookmarks = [];
  }
  
  const index = userLabBookmarks.indexOf(labId);
  if (index > -1) {
    userLabBookmarks.splice(index, 1);
    showNotification('Lab bookmark removed', 'success');
  } else {
    userLabBookmarks.push(labId);
    showNotification('Lab bookmarked!', 'success');
  }
  
  // Update UI
  updateLabBookmarkUI(labId);
  
  // Save to Firebase (extend firebase-auth.js functionality)
  saveLabBookmarks();
}

function updateLabBookmarkUI(labId) {
  const bookmarkBtn = document.querySelector(`[onclick="toggleLabBookmark('${labId}')"]`);
  if (bookmarkBtn) {
    const isBookmarked = userLabBookmarks.includes(labId);
    const icon = bookmarkBtn.querySelector('i');
    if (icon) {
      icon.className = isBookmarked ? 'fas fa-bookmark' : 'far fa-bookmark';
    }
    bookmarkBtn.classList.toggle('bookmarked', isBookmarked);
  }
}

function toggleLabSelection(labId) {
  const index = selectedLabs.indexOf(labId);
  if (index > -1) {
    selectedLabs.splice(index, 1);
  } else {
    selectedLabs.push(labId);
  }
  
  updateLabComparisonUI();
}

function updateLabComparisonUI() {
  const compareCount = document.getElementById('labCompareCount');
  const compareBtn = document.getElementById('labCompareBtn');
  
  if (compareCount) {
    compareCount.textContent = selectedLabs.length;
  }
  
  if (compareBtn) {
    if (selectedLabs.length >= 2) {
      compareBtn.style.display = 'inline-flex';
      compareBtn.classList.add('active');
    } else {
      compareBtn.style.display = 'none';
      compareBtn.classList.remove('active');
    }
  }
}

// ===== SOPHISTICATED COMPARISON SYSTEM =====

function showComparison() {
  if (selectedCourses.length < 2) {
    alert('Please select at least 2 courses to compare');
    return;
  }
  
  const selectedData = selectedCourses.map(id => 
    allCourses.find(course => course.id === id)
  ).filter(course => course);
  
  const comparisonContent = createSophisticatedComparison(selectedData);
  showComparisonModal('Course Comparison', comparisonContent);
}

function showLabComparison() {
  if (selectedLabs.length < 2) {
    alert('Please select at least 2 labs to compare');
    return;
  }
  
  const selectedData = selectedLabs.map(id => 
    labs.find(lab => lab.id === id)
  ).filter(lab => lab);
  
  const comparisonContent = createLabComparison(selectedData);
  showComparisonModal('Lab Comparison', comparisonContent);
}

function createSophisticatedComparison(courses) {
  const contentDepthAnalysis = analyzeCourseContentDepth(courses);
  const overlapAnalysis = analyzeContentOverlap(courses);
  
  return `
    <div class="comparison-overview">
      ${courses.map((course, index) => `
        <div class="comparison-course-card">
          <div class="comparison-course-title">${course.title}</div>
          <div class="comparison-quick-stats">
            ${course.category} • ${course.difficulty} • ${course.rating}/5
          </div>
        </div>
      `).join('')}
    </div>
    
    <div class="comparison-section">
      <h3>📊 Basic Comparison</h3>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Aspect</th>
            ${courses.map(course => `<th>${course.title}</th>`).join('')}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Category</strong></td>
            ${courses.map(course => `<td>${course.category}</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Difficulty</strong></td>
            ${courses.map(course => `<td><span class="difficulty ${course.difficulty}">${course.difficulty}</span></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Duration</strong></td>
            ${courses.map(course => `<td>${course.duration}</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Rating</strong></td>
            ${courses.map(course => `<td><span class="rating">${course.rating}/5</span></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Learners</strong></td>
            ${courses.map(course => `<td>${course.learnerCount.toLocaleString()}</td>`).join('')}
          </tr>
        </tbody>
      </table>
    </div>
    
    <div class="comparison-section">
      <h3>🎯 Content Depth Analysis</h3>
      <div class="content-depth-analysis">
        ${contentDepthAnalysis.map(analysis => `
          <div class="depth-card">
            <h4>${analysis.title}</h4>
            <div class="depth-indicator">
              <span>Prerequisites:</span>
              <div class="depth-bar">
                <div class="depth-fill" style="width: ${analysis.prerequisiteDepth}%"></div>
              </div>
              <span>${analysis.prerequisiteDepth}%</span>
            </div>
            <div class="depth-indicator">
              <span>Outcomes:</span>
              <div class="depth-bar">
                <div class="depth-fill" style="width: ${analysis.outcomeDepth}%"></div>
              </div>
              <span>${analysis.outcomeDepth}%</span>
            </div>
            <div class="depth-indicator">
              <span>Complexity:</span>
              <div class="depth-bar">
                <div class="depth-fill" style="width: ${analysis.complexityScore}%"></div>
              </div>
              <span>${analysis.complexityScore}%</span>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
    
    <div class="overlap-analysis">
      <h3>🔗 Content Overlap Analysis</h3>
      <p><strong>Common Topics:</strong></p>
      <div class="overlap-items">
        ${overlapAnalysis.commonTopics.map(topic => `
          <span class="overlap-tag">${topic}</span>
        `).join('')}
      </div>
      <p style="margin-top: 16px;"><strong>Learning Path Suggestion:</strong> ${overlapAnalysis.learningPath}</p>
    </div>
    
    <div class="comparison-section">
      <h3>📚 Prerequisites & Outcomes</h3>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Course</th>
            <th>Prerequisites</th>
            <th>Learning Outcomes</th>
          </tr>
        </thead>
        <tbody>
          ${courses.map(course => `
            <tr>
              <td><strong>${course.title}</strong></td>
              <td>
                <ul style="margin: 0; padding-left: 16px;">
                  ${course.prerequisites.map(prereq => `<li>${prereq}</li>`).join('')}
                </ul>
              </td>
              <td>
                <ul style="margin: 0; padding-left: 16px;">
                  ${course.outcomes.map(outcome => `<li>${outcome}</li>`).join('')}
                </ul>
              </td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    </div>
  `;
}

function createLabComparison(labs) {
  return `
    <div class="comparison-overview">
      ${labs.map((lab, index) => `
        <div class="comparison-course-card">
          <div class="comparison-course-title">${lab.title}</div>
          <div class="comparison-quick-stats">
            ${lab.category} • ${lab.status}
          </div>
        </div>
      `).join('')}
    </div>
    
    <div class="comparison-section">
      <h3>🧪 Lab Comparison</h3>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Aspect</th>
            ${labs.map(lab => `<th>${lab.title}</th>`).join('')}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Category</strong></td>
            ${labs.map(lab => `<td>${lab.category}</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Status</strong></td>
            ${labs.map(lab => `<td><span class="lab-status ${lab.status}">${lab.status}</span></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Description</strong></td>
            ${labs.map(lab => `<td>${lab.description}</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Launch</strong></td>
            ${labs.map(lab => `<td><a href="${lab.url}" target="_blank">Open Lab</a></td>`).join('')}
          </tr>
        </tbody>
      </table>
    </div>
  `;
}

function showComparisonModal(title, content) {
  // Remove existing modal if any
  const existingModal = document.getElementById('sophisticatedComparisonModal');
  if (existingModal) {
    existingModal.remove();
  }
  
  const modal = document.createElement('div');
  modal.id = 'sophisticatedComparisonModal';
  modal.className = 'modal';
  modal.style.display = 'block';
  modal.innerHTML = `
    <div class="modal-content comparison-modal">
      <div class="comparison-header">
        <h2><i class="fas fa-balance-scale"></i> ${title}</h2>
      </div>
      <div class="comparison-content">
        ${content}
      </div>
      <div class="comparison-actions">
        <button onclick="clearAllComparisons()" class="btn-secondary">Clear All</button>
        <button onclick="closeSophisticatedModal()" class="btn-primary">Close</button>
      </div>
    </div>
  `;
  
  document.body.appendChild(modal);
}

// ===== CONTENT ANALYSIS FUNCTIONS =====

function analyzeCourseContentDepth(courses) {
  return courses.map(course => {
    const prerequisiteDepth = Math.min(100, (course.prerequisites.length * 25));
    const outcomeDepth = Math.min(100, (course.outcomes.length * 20));
    const difficultyMultiplier = course.difficulty === 'beginner' ? 1 : course.difficulty === 'intermediate' ? 1.5 : 2;
    const complexityScore = Math.min(100, ((prerequisiteDepth + outcomeDepth) / 2) * difficultyMultiplier);
    
    return {
      title: course.title,
      prerequisiteDepth,
      outcomeDepth,
      complexityScore: Math.round(complexityScore)
    };
  });
}

function analyzeContentOverlap(courses) {
  const allTopics = courses.flatMap(course => [
    course.category,
    ...course.prerequisites.flatMap(p => p.split(' ')),
    ...course.outcomes.flatMap(o => o.split(' '))
  ]);
  
  const topicCounts = {};
  allTopics.forEach(topic => {
    const cleanTopic = topic.toLowerCase().replace(/[^a-z]/g, '');
    if (cleanTopic.length > 3) {
      topicCounts[cleanTopic] = (topicCounts[cleanTopic] || 0) + 1;
    }
  });
  
  const commonTopics = Object.entries(topicCounts)
    .filter(([topic, count]) => count >= 2)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8)
    .map(([topic]) => topic);
  
  const learningPath = determineLearningPath(courses);
  
  return {
    commonTopics,
    learningPath
  };
}

function determineLearningPath(courses) {
  const sortedCourses = courses.sort((a, b) => {
    const difficultyOrder = { beginner: 1, intermediate: 2, advanced: 3 };
    return difficultyOrder[a.difficulty] - difficultyOrder[b.difficulty];
  });
  
  return `Start with "${sortedCourses[0].title}" and progress to "${sortedCourses[sortedCourses.length - 1].title}" for optimal learning sequence.`;
}

// ===== UTILITY FUNCTIONS =====

function clearAllComparisons() {
  selectedCourses = [];
  selectedLabs = [];
  updateComparisonUI();
  updateLabComparisonUI();
  
  // Uncheck all checkboxes
  document.querySelectorAll('[id^="compare-"]').forEach(checkbox => {
    checkbox.checked = false;
  });
  
  closeSophisticatedModal();
}

function closeSophisticatedModal() {
  const modal = document.getElementById('sophisticatedComparisonModal');
  if (modal) {
    modal.remove();
  }
}

function saveLabBookmarks() {
  // Extend this to save to Firebase
  if (window.currentUser && typeof window.updateDoc !== 'undefined') {
    // Implementation would save to Firestore
    console.log('Saving lab bookmarks:', userLabBookmarks);
  }
}

// ===== MAINTAIN EXISTING FUNCTIONS =====

function toggleCourseDetails(courseId) {
  const detailsElement = document.getElementById(`details-${courseId}`);
  const card = document.querySelector(`[data-course-id="${courseId}"]`);
  const expandBtn = card.querySelector('.expand-btn i');
  
  if (detailsElement.style.display === 'block') {
    detailsElement.style.display = 'none';
    expandBtn.className = 'fas fa-chevron-down';
    card.classList.remove('expanded');
  } else {
    detailsElement.style.display = 'block';
    expandBtn.className = 'fas fa-chevron-up';
    card.classList.add('expanded');
  }
}

function toggleCourseSelection(courseId) {
  const index = selectedCourses.indexOf(courseId);
  if (index > -1) {
    selectedCourses.splice(index, 1);
  } else {
    selectedCourses.push(courseId);
  }
  updateComparisonUI();
}

function updateComparisonUI() {
  const compareCount = document.getElementById('compareCount');
  const compareBtn = document.getElementById('compareBtn');
  
  if (compareCount) compareCount.textContent = selectedCourses.length;
  if (compareBtn) {
    if (selectedCourses.length >= 2) {
      compareBtn.style.display = 'inline-flex';
      compareBtn.classList.add('active');
    } else {
      compareBtn.style.display = 'none';
      compareBtn.classList.remove('active');
    }
  }
}

function clearComparison() {
  selectedCourses = [];
  updateComparisonUI();
  document.querySelectorAll('[id^="compare-"]:not([id*="lab"])').forEach(checkbox => {
    checkbox.checked = false;
  });
}

function filterCourses() {
  const categoryFilter = document.getElementById('categoryFilter')?.value || '';
  const difficultyFilter = document.getElementById('difficultyFilter')?.value || '';
  const searchQuery = document.getElementById('searchInput')?.value.toLowerCase() || '';
  
  filteredCourses = allCourses.filter(course => {
    const matchesCategory = !categoryFilter || course.category === categoryFilter;
    const matchesDifficulty = !difficultyFilter || course.difficulty === difficultyFilter;
    const matchesSearch = !searchQuery || 
      course.title.toLowerCase().includes(searchQuery) ||
      course.description.toLowerCase().includes(searchQuery) ||
      course.category.toLowerCase().includes(searchQuery);
    
    return matchesCategory && matchesDifficulty && matchesSearch;
  });
  
  displayCourses();
  updateCourseCount();
}

function updateCourseCount() {
  const visibleCount = document.getElementById('visibleCount');
  const totalCount = document.getElementById('totalCount');
  
  if (visibleCount) visibleCount.textContent = filteredCourses.length;
  if (totalCount) totalCount.textContent = allCourses.length;
}

function toggleView(view, event) {
  currentView = view;
  
  document.querySelectorAll('.view-btn').forEach(btn => {
    btn.classList.remove('active');
    btn.setAttribute('aria-pressed', 'false');
  });
  
  if (event && event.target) {
    event.target.classList.add('active');
    event.target.setAttribute('aria-pressed', 'true');
  }
  
  displayCourses();
}

function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.textContent = message;
  
  document.body.appendChild(notification);
  
  setTimeout(() => {
    if (notification.parentNode) {
      notification.parentNode.removeChild(notification);
    }
  }, 3000);
}

function setupEventListeners() {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', filterCourses);
  }
  
  const compareBtn = document.getElementById('compareBtn');
  if (compareBtn) {
    compareBtn.onclick = showComparison;
  }
  
  window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
      event.target.style.display = 'none';
      document.body.style.overflow = '';
    }
  };
  
  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
      document.querySelectorAll('.modal').forEach(modal => {
        if (modal.style.display === 'block') {
          modal.style.display = 'none';
          document.body.style.overflow = '';
        }
      });
      closeSophisticatedModal();
    }
  });
}

function refreshCourseDisplay() {
  displayCourses();
}

// ===== INITIALIZATION =====

document.addEventListener('DOMContentLoaded', function() {
  initializeApp();
});

if (document.readyState !== 'loading') {
  initializeApp();
}

console.log('✅ Complete ImpactMojo loaded with ALL features!');