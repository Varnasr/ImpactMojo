// Main Application Logic
// Handles course display, dashboard functionality, theme management, and UI interactions

// Application state
let currentTheme = 'light';
let currentCategory = 'All Courses';
let searchQuery = '';

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
  initializeTheme();
  renderCourses();
  setupEventListeners();
});

// Initialize theme from localStorage or default to light
function initializeTheme() {
  const savedTheme = localStorage.getItem('impactmojo-theme') || 'light';
  setTheme(savedTheme);
}

// Set theme and update UI
function setTheme(theme) {
  currentTheme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('impactmojo-theme', theme);
  
  const themeIcon = document.getElementById('theme-icon');
  if (themeIcon) {
    themeIcon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
}

// Toggle theme
function toggleTheme() {
  setTheme(currentTheme === 'dark' ? 'light' : 'dark');
}

// Setup event listeners
function setupEventListeners() {
  // Add smooth scrolling to navigation links
  document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

// Render courses in the course grid
function renderCourses(coursesToRender = null) {
  const courseGrid = document.getElementById('course-grid');
  if (!courseGrid) return;
  
  const displayCourses = coursesToRender || courses;
  
  if (displayCourses.length === 0) {
    courseGrid.innerHTML = '<p>No courses found matching your criteria.</p>';
    return;
  }
  
  courseGrid.innerHTML = displayCourses.map(course => createCourseCard(course)).join('');
}

// Create course card HTML
function createCourseCard(course) {
  const isCompleted = isCourseCompleted(course.id);
  const isBookmarked = isCourseBookmarked(course.id);
  
  return `
    <div class="course-card" data-course-id="${course.id}">
      <h4>
        ${course.title}
        ${isCompleted ? '<i class="fas fa-check-circle" style="color: #2ecc71; margin-left: 0.5rem;" title="Completed"></i>' : ''}
        ${isBookmarked ? '<i class="fas fa-bookmark" style="color: #f39c12; margin-left: 0.5rem;" title="Bookmarked"></i>' : ''}
      </h4>
      <p>${course.description}</p>
      <div class="course-meta">
        <span class="course-difficulty difficulty-${course.difficulty}">${course.difficulty}</span>
        <span>${course.duration}</span>
      </div>
      <div class="course-actions" style="margin-top: 1rem; display: flex; gap: 0.5rem; justify-content: space-between;">
        <button onclick="openCourse('${course.id}')" class="btn btn-primary" style="flex: 1; padding: 0.5rem;">
          Open Course
        </button>
        ${currentUser ? `
          <button onclick="toggleCourseBookmark('${course.id}')" class="btn" style="padding: 0.5rem; background: ${isBookmarked ? '#f39c12' : 'var(--border-color)'}; color: ${isBookmarked ? 'white' : 'var(--text-primary)'};" title="${isBookmarked ? 'Remove bookmark' : 'Bookmark course'}">
            <i class="fas fa-bookmark"></i>
          </button>
          <button onclick="markCourseCompleted('${course.id}')" class="btn" style="padding: 0.5rem; background: ${isCompleted ? '#2ecc71' : 'var(--border-color)'}; color: ${isCompleted ? 'white' : 'var(--text-primary)'};" title="${isCompleted ? 'Completed' : 'Mark as completed'}">
            <i class="fas fa-check"></i>
          </button>
        ` : ''}
      </div>
    </div>
  `;
}

// Open course in new tab
function openCourse(courseId) {
  const course = getCourseById(courseId);
  if (course) {
    window.open(course.url, '_blank');
  }
}

// Expand/collapse learning path
function expandPath(pathId) {
  const pathCard = document.querySelector(`[onclick="expandPath('${pathId}')"]`);
  const pathCourses = document.getElementById(`${pathId}-courses`);
  const arrow = pathCard.querySelector('.path-arrow');
  
  pathCard.classList.toggle('expanded');
  
  if (pathCard.classList.contains('expanded')) {
    pathCourses.style.display = 'flex';
    arrow.style.transform = 'rotate(180deg)';
  } else {
    pathCourses.style.display = 'none';
    arrow.style.transform = 'rotate(0deg)';
  }
}

// Show user dashboard
function showDashboard() {
  if (!currentUser) {
    showAuthModal('login');
    return;
  }
  
  const modal = document.getElementById('dashboard-modal');
  const container = document.getElementById('dashboard-container');
  
  container.innerHTML = getDashboardHTML();
  modal.style.display = 'block';
  
  // Setup dashboard functionality
  setupDashboardEvents();
}

// Close dashboard
function closeDashboard() {
  const modal = document.getElementById('dashboard-modal');
  modal.style.display = 'none';
}

// Get dashboard HTML
function getDashboardHTML() {
  const progress = getUserProgress();
  const completedCourses = courses.filter(course => isCourseCompleted(course.id));
  const bookmarkedCourses = courses.filter(course => isCourseBookmarked(course.id));
  
  return `
    <div class="dashboard">
      <h2>Your Learning Dashboard</h2>
      
      <!-- Progress Overview -->
      <div class="progress-overview" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 2rem 0;">
        <div class="progress-card" style="background: var(--card-bg); padding: 1.5rem; border-radius: var(--border-radius); border: 1px solid var(--border-color); text-align: center;">
          <h3 style="color: var(--success-color); margin-bottom: 0.5rem;">${progress.completed}</h3>
          <p>Courses Completed</p>
        </div>
        <div class="progress-card" style="background: var(--card-bg); padding: 1.5rem; border-radius: var(--border-radius); border: 1px solid var(--border-color); text-align: center;">
          <h3 style="color: var(--warning-color); margin-bottom: 0.5rem;">${progress.bookmarked}</h3>
          <p>Bookmarked Courses</p>
        </div>
        <div class="progress-card" style="background: var(--card-bg); padding: 1.5rem; border-radius: var(--border-radius); border: 1px solid var(--border-color); text-align: center;">
          <h3 style="color: var(--secondary-color); margin-bottom: 0.5rem;">${Math.round((progress.completed / progress.total) * 100)}%</h3>
          <p>Overall Progress</p>
        </div>
      </div>
      
      <!-- Dashboard Tabs -->
      <div class="dashboard-tabs" style="border-bottom: 1px solid var(--border-color); margin-bottom: 2rem;">
        <button class="tab-button active" onclick="showDashboardTab('overview')" style="padding: 1rem; border: none; background: none; color: var(--text-primary); cursor: pointer; border-bottom: 2px solid var(--secondary-color);">Overview</button>
        <button class="tab-button" onclick="showDashboardTab('completed')" style="padding: 1rem; border: none; background: none; color: var(--text-secondary); cursor: pointer;">Completed (${progress.completed})</button>
        <button class="tab-button" onclick="showDashboardTab('bookmarked')" style="padding: 1rem; border: none; background: none; color: var(--text-secondary); cursor: pointer;">Bookmarked (${progress.bookmarked})</button>
        <button class="tab-button" onclick="showDashboardTab('notes')" style="padding: 1rem; border: none; background: none; color: var(--text-secondary); cursor: pointer;">Notes</button>
      </div>
      
      <!-- Tab Content -->
      <div id="dashboard-content">
        ${getDashboardOverview()}
      </div>
    </div>
  `;
}

// Get dashboard overview content
function getDashboardOverview() {
  const recentCompleted = courses.filter(course => isCourseCompleted(course.id)).slice(0, 3);
  const suggestedCourses = getFeaturedCourses().filter(course => !isCourseCompleted(course.id)).slice(0, 3);
  
  return `
    <div class="dashboard-overview">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        <div>
          <h3 style="margin-bottom: 1rem; color: var(--text-primary);">Recent Completions</h3>
          ${recentCompleted.length > 0 ? recentCompleted.map(course => `
            <div style="padding: 1rem; border: 1px solid var(--border-color); border-radius: var(--border-radius); margin-bottom: 0.5rem;">
              <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">${course.title}</h4>
              <p style="color: var(--text-secondary); font-size: 0.9rem;">${course.description}</p>
            </div>
          `).join('') : '<p style="color: var(--text-secondary);">No completed courses yet. Start learning!</p>'}
        </div>
        
        <div>
          <h3 style="margin-bottom: 1rem; color: var(--text-primary);">Suggested for You</h3>
          ${suggestedCourses.map(course => `
            <div style="padding: 1rem; border: 1px solid var(--border-color); border-radius: var(--border-radius); margin-bottom: 0.5rem; cursor: pointer;" onclick="openCourse('${course.id}')">
              <h4 style="color: var(--text-primary); margin-bottom: 0.5rem;">${course.title}</h4>
              <p style="color: var(--text-secondary); font-size: 0.9rem;">${course.description}</p>
              <span class="course-difficulty difficulty-${course.difficulty}" style="font-size: 0.8rem; margin-top: 0.5rem; display: inline-block;">${course.difficulty}</span>
            </div>
          `).join('')}
        </div>
      </div>
    </div>
  `;
}

// Show specific dashboard tab
function showDashboardTab(tab) {
  // Update tab buttons
  document.querySelectorAll('.tab-button').forEach(btn => {
    btn.style.color = 'var(--text-secondary)';
    btn.style.borderBottom = 'none';
  });
  
  event.target.style.color = 'var(--text-primary)';
  event.target.style.borderBottom = '2px solid var(--secondary-color)';
  
  // Update content
  const content = document.getElementById('dashboard-content');
  
  switch (tab) {
    case 'overview':
      content.innerHTML = getDashboardOverview();
      break;
    case 'completed':
      content.innerHTML = getCompletedCoursesTab();
      break;
    case 'bookmarked':
      content.innerHTML = getBookmarkedCoursesTab();
      break;
    case 'notes':
      content.innerHTML = getNotesTab();
      break;
  }
}

// Get completed courses tab content
function getCompletedCoursesTab() {
  const completedCourses = courses.filter(course => isCourseCompleted(course.id));
  
  if (completedCourses.length === 0) {
    return '<p style="color: var(--text-secondary); text-align: center; padding: 2rem;">No completed courses yet. Start learning to see your progress here!</p>';
  }
  
  return `
    <div class="completed-courses">
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem;">
        ${completedCourses.map(course => `
          <div class="course-card">
            <h4>${course.title} <i class="fas fa-check-circle" style="color: #2ecc71;"></i></h4>
            <p>${course.description}</p>
            <div class="course-meta">
              <span class="course-difficulty difficulty-${course.difficulty}">${course.difficulty}</span>
              <span>${course.duration}</span>
            </div>
            <button onclick="openCourse('${course.id}')" class="btn btn-primary" style="width: 100%; margin-top: 1rem;">Review Course</button>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

// Get bookmarked courses tab content
function getBookmarkedCoursesTab() {
  const bookmarkedCourses = courses.filter(course => isCourseBookmarked(course.id));
  
  if (bookmarkedCourses.length === 0) {
    return '<p style="color: var(--text-secondary); text-align: center; padding: 2rem;">No bookmarked courses yet. Bookmark courses to save them for later!</p>';
  }
  
  return `
    <div class="bookmarked-courses">
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem;">
        ${bookmarkedCourses.map(course => `
          <div class="course-card">
            <h4>${course.title} <i class="fas fa-bookmark" style="color: #f39c12;"></i></h4>
            <p>${course.description}</p>
            <div class="course-meta">
              <span class="course-difficulty difficulty-${course.difficulty}">${course.difficulty}</span>
              <span>${course.duration}</span>
            </div>
            <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
              <button onclick="openCourse('${course.id}')" class="btn btn-primary" style="flex: 1;">Open Course</button>
              <button onclick="toggleCourseBookmark('${course.id}'); showDashboardTab('bookmarked')" class="btn" style="padding: 0.5rem; background: var(--warning-color); color: white;" title="Remove bookmark">
                <i class="fas fa-bookmark"></i>
              </button>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

// Get notes tab content
function getNotesTab() {
  const coursesWithNotes = courses.filter(course => getUserNotes(course.id));
  
  return `
    <div class="notes-tab">
      <div style="margin-bottom: 2rem;">
        <h3 style="color: var(--text-primary); margin-bottom: 1rem;">Your Course Notes</h3>
        <p style="color: var(--text-secondary);">Keep track of your thoughts and insights as you learn.</p>
      </div>
      
      ${coursesWithNotes.length === 0 ? 
        '<p style="color: var(--text-secondary); text-align: center; padding: 2rem;">No notes yet. Start taking notes in your courses!</p>' :
        coursesWithNotes.map(course => `
          <div style="margin-bottom: 2rem; padding: 1.5rem; border: 1px solid var(--border-color); border-radius: var(--border-radius); background: var(--card-bg);">
            <h4 style="color: var(--text-primary); margin-bottom: 1rem;">${course.title}</h4>
            <div style="background: var(--light-bg); padding: 1rem; border-radius: var(--border-radius); margin-bottom: 1rem;">
              <p style="color: var(--text-primary); white-space: pre-wrap;">${getUserNotes(course.id)}</p>
            </div>
            <button onclick="openCourse('${course.id}')" class="btn btn-primary">Open Course</button>
          </div>
        `).join('')
      }
    </div>
  `;
}

// Setup dashboard events
function setupDashboardEvents() {
  // Add any additional dashboard-specific event listeners here
}

// Filter courses by category
function filterCourses(category) {
  currentCategory = category;
  let filteredCourses = getCoursesByCategory(category);
  
  if (searchQuery) {
    filteredCourses = filteredCourses.filter(course => 
      course.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      course.description.toLowerCase().includes(searchQuery.toLowerCase())
    );
  }
  
  renderCourses(filteredCourses);
}

// Search courses
function searchCourses(query) {
  searchQuery = query;
  let filteredCourses = currentCategory === 'All Courses' ? courses : getCoursesByCategory(currentCategory);
  
  if (query) {
    filteredCourses = filteredCourses.filter(course => 
      course.title.toLowerCase().includes(query.toLowerCase()) ||
      course.description.toLowerCase().includes(query.toLowerCase())
    );
  }
  
  renderCourses(filteredCourses);
}

// Get completion percentage for progress bars
function getCompletionPercentage() {
  const progress = getUserProgress();
  return Math.round((progress.completed / progress.total) * 100);
}

// Refresh course display after auth state changes
function refreshCourseDisplay() {
  renderCourses();
}

// Add global event listener for auth state changes
if (typeof window.onAuthStateChanged !== 'undefined') {
  window.onAuthStateChanged(window.auth, (user) => {
    // Refresh course display when auth state changes
    setTimeout(refreshCourseDisplay, 500);
  });
}

// Render labs section
function renderLabs() {
  const labsContainer = document.getElementById('labs-container');
  if (!labsContainer) return;
  
  const liveLabs = getLiveLabs();
  const comingSoonLabs = getComingSoonLabs();
  
  labsContainer.innerHTML = `
    <div class="labs-grid">
      ${[...liveLabs, ...comingSoonLabs].map(lab => createLabCard(lab)).join('')}
    </div>
  `;
}

// Create lab card HTML
function createLabCard(lab) {
  return `
    <div class="lab-card ${lab.status}">
      <h3><i class="${lab.icon}"></i> ${lab.title}</h3>
      <p>${lab.description}</p>
      <div class="lab-status">
        <span class="lab-badge ${lab.status}">${lab.status === 'live' ? 'Live' : 'Coming Soon'}</span>
        ${lab.status === 'live' ? 
          `<a href="${lab.url}" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>` : 
          '<span class="lab-launch-btn disabled">Coming Soon</span>'
        }
      </div>
    </div>
  `;
}

// Open lab in new tab
function openLab(labId) {
  const lab = getLabById(labId);
  if (lab && lab.status === 'live') {
    window.open(lab.url, '_blank');
  }
}

// Initialize labs when page loads
function initializeLabs() {
  renderLabs();
}

// Enhanced course filtering with new categories
function filterByCategory(category) {
  currentCategory = category;
  updateFilterButtons();
  renderCourses(getCoursesByCategory(category));
}

// Update filter button states
function updateFilterButtons() {
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.classList.remove('active');
  });
  document.querySelector(`[data-category="${currentCategory}"]`)?.classList.add('active');
}

// Initialize application with labs
document.addEventListener('DOMContentLoaded', function() {
  initializeTheme();
  renderCourses();
  initializeLabs();
  setupEventListeners();
});

// Enhanced Dashboard with Quiz and Research Library
function getDashboardHTML() {
  const progress = getUserProgress();
  const completedCourses = courses.filter(course => isCourseCompleted(course.id));
  const bookmarkedCourses = courses.filter(course => isCourseBookmarked(course.id));
  
  return `
    <div class="enhanced-dashboard">
      <div class="dashboard-header">
        <h2>Your Learning Dashboard</h2>
        <div class="user-profile-display">
          <div class="user-avatar-large">
            <img id="dashboard-user-photo" style="display: none;" alt="User profile">
            <div id="dashboard-user-initials">U</div>
          </div>
          <div class="user-info">
            <h3 id="dashboard-user-name">Welcome back!</h3>
            <p>Continue your learning journey</p>
          </div>
        </div>
      </div>
      
      <!-- Progress Overview -->
      <div class="progress-overview">
        <div class="progress-card">
          <div class="progress-icon"><i class="fas fa-graduation-cap"></i></div>
          <div class="progress-info">
            <h3>${progress.completed}</h3>
            <p>Courses Completed</p>
          </div>
        </div>
        <div class="progress-card">
          <div class="progress-icon"><i class="fas fa-bookmark"></i></div>
          <div class="progress-info">
            <h3>${progress.bookmarked}</h3>
            <p>Bookmarked</p>
          </div>
        </div>
        <div class="progress-card">
          <div class="progress-icon"><i class="fas fa-chart-line"></i></div>
          <div class="progress-info">
            <h3>${Math.round((progress.completed / progress.total) * 100)}%</h3>
            <p>Overall Progress</p>
          </div>
        </div>
        <div class="progress-card">
          <div class="progress-icon"><i class="fas fa-sticky-note"></i></div>
          <div class="progress-info">
            <h3>${Object.keys(userProfile?.notes || {}).length}</h3>
            <p>Notes Created</p>
          </div>
        </div>
      </div>
      
      <!-- Custom Learning Path Quiz -->
      <div class="learning-path-quiz">
        <h3><i class="fas fa-compass"></i> Find Your Perfect Learning Path</h3>
        <p>Take our quick quiz to get personalized course recommendations.</p>
        <button class="btn btn-primary" onclick="startLearningPathQuiz()">
          <i class="fas fa-play"></i> Start Quiz (2 minutes)
        </button>
      </div>
      
      <!-- Dashboard Tabs -->
      <div class="dashboard-tabs">
        <button class="tab-button active" onclick="showDashboardTab('overview')">Overview</button>
        <button class="tab-button" onclick="showDashboardTab('completed')">Completed (${progress.completed})</button>
        <button class="tab-button" onclick="showDashboardTab('bookmarked')">Bookmarked (${progress.bookmarked})</button>
        <button class="tab-button" onclick="showDashboardTab('research')">Research Library</button>
        <button class="tab-button" onclick="showDashboardTab('notes')">My Notes</button>
      </div>
      
      <!-- Tab Content -->
      <div id="dashboard-content">
        ${getDashboardOverview()}
      </div>
    </div>
  `;
}

// Learning Path Quiz System
function startLearningPathQuiz() {
  const quizHTML = `
    <div class="quiz-container">
      <h3>Learning Path Quiz</h3>
      <div class="quiz-progress">
        <div class="quiz-progress-bar">
          <div class="quiz-progress-fill" style="width: 0%"></div>
        </div>
        <span class="quiz-progress-text">Question 1 of 5</span>
      </div>
      
      <div id="quiz-questions">
        ${getQuizQuestion(1)}
      </div>
      
      <div class="quiz-actions">
        <button class="btn btn-secondary" onclick="closeDashboard()">Cancel</button>
        <button class="btn btn-primary" id="quiz-next-btn" onclick="nextQuizQuestion()" disabled>Next</button>
      </div>
    </div>
  `;
  
  document.getElementById('dashboard-content').innerHTML = quizHTML;
}

let quizAnswers = {};
let currentQuizQuestion = 1;

function getQuizQuestion(questionNum) {
  const questions = {
    1: {
      question: "What best describes your current role?",
      options: [
        { value: "student", text: "Student or researcher" },
        { value: "practitioner", text: "Development practitioner" },
        { value: "academic", text: "Academic or educator" },
        { value: "policy", text: "Policy maker or government" },
        { value: "other", text: "Other" }
      ]
    },
    2: {
      question: "Which area interests you most?",
      options: [
        { value: "data", text: "Data analysis and statistics" },
        { value: "gender", text: "Gender studies and feminism" },
        { value: "economics", text: "Economics and policy" },
        { value: "health", text: "Public health and wellness" },
        { value: "research", text: "Research methods and ethics" }
      ]
    },
    3: {
      question: "What's your experience level with development topics?",
      options: [
        { value: "beginner", text: "Beginner - new to development" },
        { value: "intermediate", text: "Intermediate - some experience" },
        { value: "advanced", text: "Advanced - experienced professional" },
        { value: "expert", text: "Expert - teaching/leading others" }
      ]
    },
    4: {
      question: "How do you prefer to learn?",
      options: [
        { value: "theory", text: "Theory and conceptual frameworks" },
        { value: "practical", text: "Practical applications and case studies" },
        { value: "hands-on", text: "Hands-on exercises and tools" },
        { value: "mixed", text: "Mix of theory and practice" }
      ]
    },
    5: {
      question: "What's your primary goal?",
      options: [
        { value: "skills", text: "Build specific technical skills" },
        { value: "knowledge", text: "Broaden general knowledge" },
        { value: "career", text: "Advance my career" },
        { value: "research", text: "Support my research" },
        { value: "teaching", text: "Improve my teaching" }
      ]
    }
  };
  
  const q = questions[questionNum];
  return `
    <div class="quiz-question">
      <h4>Question ${questionNum}: ${q.question}</h4>
      <div class="quiz-options">
        ${q.options.map(option => `
          <label class="quiz-option">
            <input type="radio" name="q${questionNum}" value="${option.value}" onchange="selectQuizAnswer(${questionNum}, '${option.value}')">
            <span>${option.text}</span>
          </label>
        `).join('')}
      </div>
    </div>
  `;
}

function selectQuizAnswer(questionNum, answer) {
  quizAnswers[questionNum] = answer;
  document.getElementById('quiz-next-btn').disabled = false;
}

function nextQuizQuestion() {
  currentQuizQuestion++;
  const progressPercent = (currentQuizQuestion - 1) / 5 * 100;
  
  if (currentQuizQuestion <= 5) {
    document.querySelector('.quiz-progress-fill').style.width = `${progressPercent}%`;
    document.querySelector('.quiz-progress-text').textContent = `Question ${currentQuizQuestion} of 5`;
    document.getElementById('quiz-questions').innerHTML = getQuizQuestion(currentQuizQuestion);
    document.getElementById('quiz-next-btn').disabled = true;
    
    if (currentQuizQuestion === 5) {
      document.getElementById('quiz-next-btn').textContent = 'Get My Recommendations';
      document.getElementById('quiz-next-btn').onclick = finishQuiz;
    }
  }
}

function finishQuiz() {
  const recommendations = generateQuizRecommendations(quizAnswers);
  const resultsHTML = `
    <div class="quiz-results">
      <h3><i class="fas fa-star"></i> Your Personalized Learning Path</h3>
      <p>Based on your answers, we recommend these courses for you:</p>
      
      <div class="recommended-courses">
        ${recommendations.map(course => `
          <div class="recommended-course">
            <h4>${course.title}</h4>
            <p>${course.description}</p>
            <div class="course-actions">
              <button class="btn btn-primary" onclick="openCourse('${course.id}')">Start Course</button>
              <button class="btn btn-secondary" onclick="toggleCourseBookmark('${course.id}')">
                <i class="fas fa-bookmark"></i> Bookmark
              </button>
            </div>
          </div>
        `).join('')}
      </div>
      
      <div class="quiz-actions">
        <button class="btn btn-secondary" onclick="startLearningPathQuiz()">Retake Quiz</button>
        <button class="btn btn-primary" onclick="showDashboardTab('overview')">Back to Dashboard</button>
      </div>
    </div>
  `;
  
  document.getElementById('dashboard-content').innerHTML = resultsHTML;
}

function generateQuizRecommendations(answers) {
  // Simple recommendation algorithm based on quiz answers
  const recommendations = [];
  
  if (answers[2] === 'data' || answers[4] === 'skills') {
    recommendations.push(getCourseById('data-literacy-101'));
    recommendations.push(getCourseById('data-feminism-101'));
  }
  
  if (answers[2] === 'gender') {
    recommendations.push(getCourseById('gender-studies-101'));
    recommendations.push(getCourseById('womens-economic-empowerment-101'));
  }
  
  if (answers[2] === 'economics') {
    recommendations.push(getCourseById('development-economics-101'));
    recommendations.push(getCourseById('social-safety-nets-101'));
  }
  
  if (answers[2] === 'health') {
    recommendations.push(getCourseById('public-health-101'));
    recommendations.push(getCourseById('mental-health-101'));
  }
  
  if (answers[2] === 'research' || answers[4] === 'research') {
    recommendations.push(getCourseById('research-ethics-101'));
    recommendations.push(getCourseById('qualitative-research-101'));
  }
  
  // Fallback recommendations
  if (recommendations.length === 0) {
    recommendations.push(getCourseById('data-literacy-101'));
    recommendations.push(getCourseById('gender-studies-101'));
    recommendations.push(getCourseById('development-economics-101'));
  }
  
  return recommendations.filter(Boolean).slice(0, 3);
}

// Enhanced Research Library Tab
function getResearchLibraryTab() {
  return `
    <div class="research-library">
      <div class="library-header">
        <h3><i class="fas fa-university"></i> Research Library</h3>
        <p>Access curated research papers, datasets, and academic resources related to your courses.</p>
      </div>
      
      <div class="library-categories">
        <div class="library-category">
          <h4><i class="fas fa-file-alt"></i> Recent Papers</h4>
          <div class="paper-list">
            <div class="paper-item">
              <h5>Gender Gaps in Development: Evidence from South Asia</h5>
              <p>Comprehensive review of gender disparities in education, health, and economic outcomes.</p>
              <div class="paper-meta">
                <span>Journal of Development Economics, 2024</span>
                <a href="#" onclick="openPaper('gender-gaps-2024')">Read Paper</a>
              </div>
            </div>
            <div class="paper-item">
              <h5>Data Feminism in Practice: Lessons from Development NGOs</h5>
              <p>Case studies on implementing feminist data practices in development organizations.</p>
              <div class="paper-meta">
                <span>Development Policy Review, 2024</span>
                <a href="#" onclick="openPaper('data-feminism-practice-2024')">Read Paper</a>
              </div>
            </div>
          </div>
        </div>
        
        <div class="library-category">
          <h4><i class="fas fa-database"></i> Datasets</h4>
          <div class="dataset-list">
            <div class="dataset-item">
              <h5>NFHS-5 State Fact Sheets</h5>
              <p>Complete state-wise data from India's National Family Health Survey 2019-21.</p>
              <div class="dataset-meta">
                <span>Source: Ministry of Health, GOI</span>
                <a href="http://rchiips.org/nfhs/factsheet_NFHS-5.shtml" target="_blank">Access Dataset</a>
              </div>
            </div>
            <div class="dataset-item">
              <h5>World Bank Gender Data Portal</h5>
              <p>Gender-disaggregated indicators across countries and time periods.</p>
              <div class="dataset-meta">
                <span>Source: World Bank</span>
                <a href="https://genderdata.worldbank.org/" target="_blank">Access Dataset</a>
              </div>
            </div>
          </div>
        </div>
        
        <div class="library-category">
          <h4><i class="fas fa-tools"></i> Research Tools</h4>
          <div class="tool-list">
            <div class="tool-item">
              <h5>Survey Design Checklist</h5>
              <p>Comprehensive checklist for designing surveys in development contexts.</p>
              <a href="#" onclick="downloadTool('survey-checklist')">Download Tool</a>
            </div>
            <div class="tool-item">
              <h5>Ethics Review Template</h5>
              <p>Template for conducting ethical review of development research.</p>
              <a href="#" onclick="downloadTool('ethics-template')">Download Tool</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}

// Enhanced Notes Tab with Search
function getNotesTab() {
  const userNotes = getUserAllNotes();
  
  return `
    <div class="notes-tab">
      <div class="notes-header">
        <h3><i class="fas fa-sticky-note"></i> My Academic Notes</h3>
        <div class="notes-search">
          <input type="text" id="notes-search-input" placeholder="Search notes..." class="search-input">
          <button onclick="searchUserNotes()" class="search-btn"><i class="fas fa-search"></i></button>
        </div>
      </div>
      
      <div class="notes-actions">
        <button class="btn btn-primary" onclick="createNewNote()">
          <i class="fas fa-plus"></i> New Note
        </button>
        <button class="btn btn-secondary" onclick="exportNotes()">
          <i class="fas fa-download"></i> Export Notes
        </button>
      </div>
      
      <div id="notes-list">
        ${userNotes.length === 0 ? 
          '<div class="no-notes"><p>No notes yet. Start taking notes in your courses!</p></div>' :
          renderUserNotes(userNotes)
        }
      </div>
    </div>
  `;
}

function getUserAllNotes() {
  if (!userProfile?.notes) return [];
  
  return Object.entries(userProfile.notes).map(([courseId, noteData]) => ({
    courseId,
    courseName: getCourseById(courseId)?.title || 'Unknown Course',
    content: noteData.content || noteData, // Handle both old and new note formats
    timestamp: noteData.timestamp || new Date().toISOString(),
    citations: noteData.citations || []
  })).sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
}

function renderUserNotes(notes) {
  return notes.map(note => `
    <div class="note-item" data-course-id="${note.courseId}">
      <div class="note-header">
        <div class="note-title">${note.courseName}</div>
        <div class="note-date">${new Date(note.timestamp).toLocaleDateString()}</div>
      </div>
      <div class="note-content">${note.content}</div>
      ${note.citations.length > 0 ? `
        <div class="note-citations">
          <h5>Citations:</h5>
          ${note.citations.map(citation => `<div class="citation">${citation}</div>`).join('')}
        </div>
      ` : ''}
      <div class="note-actions">
        <button onclick="editNote('${note.courseId}')" class="btn-small btn-secondary">Edit</button>
        <button onclick="deleteNote('${note.courseId}')" class="btn-small btn-danger">Delete</button>
        <button onclick="openCourse('${note.courseId}')" class="btn-small btn-primary">Open Course</button>
      </div>
    </div>
  `).join('');
}

function searchUserNotes() {
  const query = document.getElementById('notes-search-input').value.toLowerCase();
  const notes = getUserAllNotes();
  
  if (!query) {
    document.getElementById('notes-list').innerHTML = renderUserNotes(notes);
    return;
  }
  
  const filteredNotes = notes.filter(note => 
    note.courseName.toLowerCase().includes(query) ||
    note.content.toLowerCase().includes(query)
  );
  
  document.getElementById('notes-list').innerHTML = 
    filteredNotes.length > 0 ? renderUserNotes(filteredNotes) : 
    '<div class="no-notes"><p>No notes found matching your search.</p></div>';
}

function createNewNote() {
  // Implementation for creating new standalone notes
  showNotification('Feature coming soon: Standalone note creation', 'info');
}

function exportNotes() {
  const notes = getUserAllNotes();
  const exportData = notes.map(note => ({
    course: note.courseName,
    content: note.content,
    date: note.timestamp,
    citations: note.citations
  }));
  
  const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'impactmojo-notes.json';
  a.click();
  URL.revokeObjectURL(url);
  
  showNotification('Notes exported successfully!', 'success');
}

// User Photo Management
function updateUserPhoto(photoURL) {
  const photoElements = [
    document.getElementById('user-photo'),
    document.getElementById('dashboard-user-photo')
  ];
  
  const initialsElements = [
    document.getElementById('user-initials'),
    document.getElementById('dashboard-user-initials')
  ];
  
  if (photoURL) {
    photoElements.forEach(el => {
      if (el) {
        el.src = photoURL;
        el.style.display = 'block';
      }
    });
    initialsElements.forEach(el => {
      if (el) el.style.display = 'none';
    });
  } else {
    photoElements.forEach(el => {
      if (el) el.style.display = 'none';
    });
    initialsElements.forEach(el => {
      if (el) el.style.display = 'flex';
    });
  }
}

function updateUserInitials(name) {
  const initials = name ? name.split(' ').map(word => word[0]).join('').toUpperCase().slice(0, 2) : 'U';
  const initialsElements = [
    document.getElementById('user-initials'),
    document.getElementById('dashboard-user-initials')
  ];
  
  initialsElements.forEach(el => {
    if (el) el.textContent = initials;
  });
}

// Enhanced Dashboard Tab Function
function showDashboardTab(tab) {
  // Update tab buttons
  document.querySelectorAll('.tab-button').forEach(btn => {
    btn.classList.remove('active');
  });
  
  event.target.classList.add('active');
  
  // Update content
  const content = document.getElementById('dashboard-content');
  
  switch (tab) {
    case 'overview':
      content.innerHTML = getDashboardOverview();
      break;
    case 'completed':
      content.innerHTML = getCompletedCoursesTab();
      break;
    case 'bookmarked':
      content.innerHTML = getBookmarkedCoursesTab();
      break;
    case 'research':
      content.innerHTML = getResearchLibraryTab();
      break;
    case 'notes':
      content.innerHTML = getNotesTab();
      break;
  }
}

// Search Notes Function
function searchNotes() {
  const query = document.getElementById('notes-search').value.toLowerCase();
  const noteElements = document.querySelectorAll('.note-item');
  
  noteElements.forEach(noteEl => {
    const content = noteEl.textContent.toLowerCase();
    if (content.includes(query) || query === '') {
      noteEl.style.display = 'block';
    } else {
      noteEl.style.display = 'none';
    }
  });
}

// Enhanced course filtering
function filterByCategory(category) {
  currentCategory = category;
  updateFilterButtons(category);
  renderCourses(getCoursesByCategory(category));
}

function updateFilterButtons(activeCategory) {
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.classList.remove('active');
    if (btn.dataset.category === activeCategory) {
      btn.classList.add('active');
    }
  });
}

// Initialize enhanced application
document.addEventListener('DOMContentLoaded', function() {
  initializeTheme();
  renderCourses();
  initializeLabs();
  setupEventListeners();
  
  // Initialize search functionality
  const notesSearch = document.getElementById('notes-search');
  if (notesSearch) {
    notesSearch.addEventListener('keyup', function(e) {
      if (e.key === 'Enter') {
        searchNotes();
      }
    });
  }
});

// Export enhanced functions for global access
window.toggleTheme = toggleTheme;
window.expandPath = expandPath;
window.showDashboard = showDashboard;
window.closeDashboard = closeDashboard;
window.showDashboardTab = showDashboardTab;
window.openCourse = openCourse;
window.openLab = openLab;
window.filterCourses = filterCourses;
window.filterByCategory = filterByCategory;
window.searchCourses = searchCourses;
window.searchNotes = searchNotes;
window.startLearningPathQuiz = startLearningPathQuiz;
window.selectQuizAnswer = selectQuizAnswer;
window.nextQuizQuestion = nextQuizQuestion;
window.finishQuiz = finishQuiz;