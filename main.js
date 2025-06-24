// Complete ImpactMojo Main JavaScript File
// All functionality working: theme toggle, login/signup, courses, labs, popular courses

console.log('🚀 Loading ImpactMojo...');

// ===== GLOBAL VARIABLES =====
let allCourses = [];
let filteredCourses = [];
let selectedCourses = [];
let selectedLabs = [];
let userBookmarks = JSON.parse(localStorage.getItem('userBookmarks')) || [];
let userLabBookmarks = JSON.parse(localStorage.getItem('userLabBookmarks')) || [];

// ===== WORKING THEME TOGGLE =====
function toggleTheme() {
  console.log('🎨 Toggling theme...');
  
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  console.log(`Switching from ${currentTheme} to ${newTheme}`);
  
  // Update the theme
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  // Update the icon
  if (themeIcon) {
    themeIcon.className = newTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    console.log(`Icon updated to: ${themeIcon.className}`);
  } else {
    console.error('Theme icon not found!');
  }
  
  // Show notification
  showNotification(`Switched to ${newTheme} mode`, 'success');
}

// Initialize theme on page load
function initializeThemeToggle() {
  console.log('🎨 Initializing theme toggle');
  
  const savedTheme = localStorage.getItem('theme') || 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  console.log(`Saved theme: ${savedTheme}`);
  
  // Set the theme
  document.documentElement.setAttribute('data-theme', savedTheme);
  
  // Set the icon
  if (themeIcon) {
    themeIcon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    console.log(`Initial icon set to: ${themeIcon.className}`);
  } else {
    console.error('Theme icon not found during initialization!');
  }
}

// ===== MODAL FUNCTIONS =====
function showLoginModal() {
  console.log('📝 Opening login modal');
  const modal = document.getElementById('loginModal');
  if (modal) {
    modal.style.display = 'block';
  } else {
    console.error('❌ Login modal not found');
  }
}

function showSignupModal() {
  console.log('📝 Opening signup modal');
  const modal = document.getElementById('signupModal');
  if (modal) {
    modal.style.display = 'block';
  } else {
    console.error('❌ Signup modal not found');
  }
}

function closeModal(modalId) {
  console.log(`📝 Closing modal: ${modalId}`);
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
  }
}

// ===== INITIALIZATION =====
function initializeApp() {
  console.log('📚 Initializing ImpactMojo...');
  
  // Check if data is available
  if (typeof courses === 'undefined') {
    console.error('❌ Courses data not loaded');
    setTimeout(initializeApp, 500); // Try again in 500ms
    return;
  }
  
  if (typeof labs === 'undefined') {
    console.error('❌ Labs data not loaded');
    setTimeout(initializeApp, 500); // Try again in 500ms
    return;
  }
  
  // Set up data
  allCourses = [...courses];
  filteredCourses = [...courses];
  
  // Initialize displays
  displayCourses();
  displayLabs();
  displayPopularCourses();
  updateCourseCount();
  setupEventListeners();
  
  // Initialize theme
  initializeThemeToggle();
  
  console.log('✅ ImpactMojo initialized successfully!');
}

// ===== POPULAR COURSES FUNCTIONALITY =====
function displayPopularCourses() {
  const container = document.getElementById('popularCoursesContainer');
  
  if (!container) {
    console.log('ℹ️ Popular courses container not found');
    return;
  }
  
  // Get popular courses (highest rated)
  const popularCourseIds = ['gender-studies-101', 'dev-econ-101', 'research-ethics-101', 'public-health-101', 'data-literacy-101', 'poverty-inequality-101'];
  const popularCourses = popularCourseIds.map(id => 
    allCourses.find(course => course.id === id)
  ).filter(course => course);
  
  if (popularCourses.length === 0) {
    container.innerHTML = '<div class="no-results">No popular courses found.</div>';
    return;
  }

  container.innerHTML = popularCourses.map(course => createCourseCard(course)).join('');
  
  // Update bookmark UI after displaying
  setTimeout(updateAllBookmarkUI, 100);
}

// ===== COURSE DISPLAY FUNCTIONS =====
function displayCourses() {
  const container = document.getElementById('courseContainer');
  
  if (!container) {
    console.error('❌ Course container not found');
    return;
  }
  
  if (!filteredCourses || filteredCourses.length === 0) {
    container.innerHTML = '<div class="no-results">No courses found.</div>';
    return;
  }

  container.innerHTML = filteredCourses.map(course => createCourseCard(course)).join('');
  
  // Update bookmark UI after displaying
  setTimeout(updateAllBookmarkUI, 100);
}

// ===== FIXED COURSE CARD CREATION WITH CATEGORY COLORS =====
function createCourseCard(course) {
  // Safely handle potentially undefined values
  const rating = course.rating || 4.5;
  const duration = course.duration || '30 min';
  const difficulty = course.difficulty || 'Intermediate';
  const category = course.category || 'General';
  const description = course.description || 'No description available';
  const title = course.title || 'Untitled Course';
  const courseId = course.id || 'unknown';
  
  // Get category color
  const categoryColor = getCategoryColor(category);
  
  return `
    <div class="course-card" data-course-id="${courseId}" style="border-left: 4px solid ${categoryColor}">
      <div class="course-card-header">
        <div class="course-category" style="background-color: ${categoryColor}20; color: ${categoryColor}">
          ${category}
        </div>
        <div class="course-actions">
          <label class="comparison-checkbox">
            <input type="checkbox" onchange="toggleCourseSelection('${courseId}')" aria-label="Select for comparison">
            <span class="checkmark"></span>
          </label>
          <button class="bookmark-btn" onclick="toggleBookmark('${courseId}')" aria-label="Bookmark course">
            <i class="far fa-bookmark"></i>
          </button>
        </div>
      </div>
      
      <div class="course-content">
        <h3 class="course-title">${title}</h3>
        <p class="course-description">${description}</p>
        
        <div class="course-meta">
          <span class="course-rating">
            <i class="fas fa-star"></i>
            ${rating.toFixed(1)}
          </span>
          <span class="course-duration">
            <i class="fas fa-clock"></i>
            ${duration}
          </span>
          <span class="course-difficulty difficulty-${difficulty.toLowerCase()}">
            ${difficulty}
          </span>
        </div>
      </div>
      
      <div class="course-card-footer">
        <button class="launch-btn" onclick="launchCourse('${courseId}')">
          <i class="fas fa-play"></i>
          Launch
        </button>
      </div>
    </div>
  `;
}

// ===== LAB DISPLAY FUNCTIONS =====
function displayLabs() {
  const container = document.getElementById('labsContainer');
  
  if (!container) {
    console.log('ℹ️ Labs container not found, skipping lab display');
    return;
  }
  
  if (!labs || labs.length === 0) {
    container.innerHTML = '<div class="no-results">No labs available.</div>';
    return;
  }

  container.innerHTML = labs.map(lab => createLabCard(lab)).join('');
  
  // Update bookmark UI after displaying
  setTimeout(updateAllLabBookmarkUI, 100);
}

function createLabCard(lab) {
  // Safely handle potentially undefined values
  const rating = lab.rating || 4.5;
  const duration = lab.duration || '20 min';
  const difficulty = lab.difficulty || 'Intermediate';
  const category = lab.category || 'General';
  const description = lab.description || 'No description available';
  const title = lab.title || 'Untitled Lab';
  const labId = lab.id || 'unknown';
  const labType = lab.labType || 'Interactive';
  
  // Get category color
  const categoryColor = getCategoryColor(category);
  
  return `
    <div class="lab-card" data-lab-id="${labId}" style="border-left: 4px solid ${categoryColor}">
      <div class="lab-card-header">
        <div class="lab-category" style="background-color: ${categoryColor}20; color: ${categoryColor}">
          ${category}
        </div>
        <div class="lab-type-badge">${labType}</div>
        <div class="lab-actions">
          <label class="comparison-checkbox">
            <input type="checkbox" onchange="toggleLabSelection('${labId}')" aria-label="Select for comparison">
            <span class="checkmark"></span>
          </label>
          <button class="bookmark-btn" onclick="toggleLabBookmark('${labId}')" aria-label="Bookmark lab">
            <i class="far fa-bookmark"></i>
          </button>
        </div>
      </div>
      
      <div class="lab-content">
        <h3 class="lab-title">${title}</h3>
        <p class="lab-description">${description}</p>
        
        <div class="lab-meta">
          <span class="lab-rating">
            <i class="fas fa-star"></i>
            ${rating.toFixed(1)}
          </span>
          <span class="lab-duration">
            <i class="fas fa-clock"></i>
            ${duration}
          </span>
          <span class="lab-difficulty difficulty-${difficulty.toLowerCase()}">
            ${difficulty}
          </span>
        </div>
      </div>
      
      <div class="lab-card-footer">
        <button class="launch-btn lab-launch" onclick="launchLab('${labId}')">
          <i class="fas fa-flask"></i>
          Launch Lab
        </button>
      </div>
    </div>
  `;
}

// ===== CATEGORY COLOR DISCRIMINATION =====
function getCategoryColor(category) {
  const colors = {
    'Economics & Development': '#6366f1',
    'Research & Data Analysis': '#dc2626',
    'Gender & Social Justice': '#7c3aed',
    'Governance & Policy': '#ea580c',
    'Health & Environment': '#0891b2',
    'Education & Communication': '#be185d',
    'Technology & Ethics': '#4338ca',
    'Community & Fundraising': '#16a34a',
    'General': '#6b7280'
  };
  
  return colors[category] || colors['General'];
}

function updateCourseCount() {
  const countElement = document.getElementById('courseCount');
  if (countElement) {
    countElement.textContent = filteredCourses.length;
  }
}

// ===== INTERACTION FUNCTIONS =====
function launchCourse(courseId) {
  const course = allCourses.find(c => c.id === courseId);
  if (course && course.url) {
    window.open(course.url, '_blank');
    showNotification(`Launching ${course.title}`, 'success');
  } else {
    console.error('Course not found or URL missing:', courseId);
    showNotification('Course not available', 'error');
  }
}

function launchLab(labId) {
  const lab = labs.find(l => l.id === labId);
  if (lab && lab.url) {
    window.open(lab.url, '_blank');
    showNotification(`Launching ${lab.title}`, 'success');
  } else {
    console.error('Lab not found or URL missing:', labId);
    showNotification('Lab not available', 'error');
  }
}

function toggleBookmark(courseId) {
  // Check if user is logged in
  if (typeof window.currentUser === 'undefined' || !window.currentUser) {
    showNotification('Please log in to bookmark courses', 'error');
    showLoginModal();
    return;
  }
  
  const index = userBookmarks.indexOf(courseId);
  if (index > -1) {
    userBookmarks.splice(index, 1);
    showNotification('Course bookmark removed', 'success');
  } else {
    userBookmarks.push(courseId);
    showNotification('Course bookmarked!', 'success');
  }
  
  // Update UI
  updateBookmarkUI(courseId);
  
  // Save to Firebase if available
  if (typeof saveBookmarks === 'function') {
    saveBookmarks();
  } else {
    localStorage.setItem('userBookmarks', JSON.stringify(userBookmarks));
  }
}

function toggleLabBookmark(labId) {
  // Check if user is logged in
  if (typeof window.currentUser === 'undefined' || !window.currentUser) {
    showNotification('Please log in to bookmark labs', 'error');
    showLoginModal();
    return;
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
  
  // Save to Firebase if available
  if (typeof saveLabBookmarks === 'function') {
    saveLabBookmarks();
  } else {
    localStorage.setItem('userLabBookmarks', JSON.stringify(userLabBookmarks));
  }
}

function updateBookmarkUI(courseId) {
  const bookmarkBtn = document.querySelector(`[onclick="toggleBookmark('${courseId}')"]`);
  if (bookmarkBtn) {
    const isBookmarked = userBookmarks.includes(courseId);
    const icon = bookmarkBtn.querySelector('i');
    if (icon) {
      icon.className = isBookmarked ? 'fas fa-bookmark' : 'far fa-bookmark';
    }
    bookmarkBtn.classList.toggle('bookmarked', isBookmarked);
  }
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

function updateAllBookmarkUI() {
  if (typeof courses !== 'undefined') {
    courses.forEach(course => {
      updateBookmarkUI(course.id);
    });
  }
}

function updateAllLabBookmarkUI() {
  if (typeof labs !== 'undefined') {
    labs.forEach(lab => {
      updateLabBookmarkUI(lab.id);
    });
  }
}

// ===== COMPARISON FUNCTIONS =====
function toggleCourseSelection(courseId) {
  const index = selectedCourses.indexOf(courseId);
  if (index > -1) {
    selectedCourses.splice(index, 1);
  } else {
    selectedCourses.push(courseId);
  }
  
  updateComparisonUI();
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

function updateComparisonUI() {
  const compareCount = document.getElementById('compareCount');
  const compareBtn = document.getElementById('compareBtn');
  
  if (compareCount) {
    compareCount.textContent = selectedCourses.length;
  }
  
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

// ===== RESPONSIVE COMPARISON MODALS =====
function showComparison() {
  if (selectedCourses.length < 2) {
    showNotification('Please select at least 2 courses to compare', 'error');
    return;
  }
  
  const selectedData = selectedCourses.map(id => 
    allCourses.find(course => course.id === id)
  ).filter(course => course);
  
  // Create responsive comparison modal
  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.style.display = 'block';
  modal.innerHTML = `
    <div class="modal-content" style="max-width: 90vw; max-height: 80vh; overflow-y: auto;">
      <span class="close" onclick="this.parentElement.parentElement.remove()">&times;</span>
      <h2>Course Comparison</h2>
      <div class="comparison-table">
        ${createResponsiveComparisonTable(selectedData)}
      </div>
    </div>
  `;
  
  document.body.appendChild(modal);
}

function showLabComparison() {
  if (selectedLabs.length < 2) {
    showNotification('Please select at least 2 labs to compare', 'error');
    return;
  }
  
  const selectedData = selectedLabs.map(id => 
    labs.find(lab => lab.id === id)
  ).filter(lab => lab);
  
  // Create responsive lab comparison modal
  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.style.display = 'block';
  modal.innerHTML = `
    <div class="modal-content" style="max-width: 90vw; max-height: 80vh; overflow-y: auto;">
      <span class="close" onclick="this.parentElement.parentElement.remove()">&times;</span>
      <h2>Lab Comparison</h2>
      <div class="comparison-table">
        ${createResponsiveLabComparisonTable(selectedData)}
      </div>
    </div>
  `;
  
  document.body.appendChild(modal);
}

function createResponsiveComparisonTable(courses) {
  let html = '<div style="overflow-x: auto;"><table style="width: 100%; min-width: 600px; border-collapse: collapse;">';
  html += '<tr><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Course</th><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Category</th><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Difficulty</th><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Duration</th><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Rating</th><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Action</th></tr>';
  
  courses.forEach(course => {
    html += `
      <tr>
        <td style="padding: 1rem; border: 1px solid var(--border-color); color: var(--text-primary);">${course.title}</td>
        <td style="padding: 1rem; border: 1px solid var(--border-color); color: var(--text-primary);">${course.category}</td>
        <td style="padding: 1rem; border: 1px solid var(--border-color); color: var(--text-primary);">${course.difficulty}</td>
        <td style="padding: 1rem; border: 1px solid var(--border-color); color: var(--text-primary);">${course.duration}</td>
        <td style="padding: 1rem; border: 1px solid var(--border-color); color: var(--text-primary);">${course.rating}</td>
        <td style="padding: 1rem; border: 1px solid var(--border-color);">
          <button onclick="launchCourse('${course.id}')" class="launch-btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Launch</button>
        </td>
      </tr>
    `;
  });
  
  html += '</table></div>';
  return html;
}

function createResponsiveLabComparisonTable(labs) {
  let html = '<div style="overflow-x: auto;"><table style="width: 100%; min-width: 600px; border-collapse: collapse;">';
  html += '<tr><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Lab</th><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Category</th><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Type</th><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Duration</th><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Rating</th><th style="padding: 1rem; border: 1px solid var(--border-color); background: var(--surface);">Action</th></tr>';
  
  labs.forEach(lab => {
    html += `
      <tr>
        <td style="padding: 1rem; border: 1px solid var(--border-color); color: var(--text-primary);">${lab.title}</td>
        <td style="padding: 1rem; border: 1px solid var(--border-color); color: var(--text-primary);">${lab.category}</td>
        <td style="padding: 1rem; border: 1px solid var(--border-color); color: var(--text-primary);">${lab.labType}</td>
        <td style="padding: 1rem; border: 1px solid var(--border-color); color: var(--text-primary);">${lab.duration}</td>
        <td style="padding: 1rem; border: 1px solid var(--border-color); color: var(--text-primary);">${lab.rating}</td>
        <td style="padding: 1rem; border: 1px solid var(--border-color);">
          <button onclick="launchLab('${lab.id}')" class="launch-btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Launch</button>
        </td>
      </tr>
    `;
  });
  
  html += '</table></div>';
  return html;
}

// ===== FILTERING FUNCTIONS =====
function filterCourses(category = 'All Courses', difficulty = '') {
  let filtered = [...allCourses];
  
  if (category !== 'All Courses') {
    filtered = filtered.filter(course => course.category === category);
  }
  
  if (difficulty) {
    filtered = filtered.filter(course => course.difficulty === difficulty);
  }
  
  filteredCourses = filtered;
  displayCourses();
  updateCourseCount();
}

function searchCourses(query) {
  if (!query) {
    filteredCourses = [...allCourses];
  } else {
    const lowerQuery = query.toLowerCase();
    filteredCourses = allCourses.filter(course => 
      course.title.toLowerCase().includes(lowerQuery) ||
      course.description.toLowerCase().includes(lowerQuery) ||
      course.category.toLowerCase().includes(lowerQuery) ||
      (course.topics && course.topics.some(topic => 
        topic.toLowerCase().includes(lowerQuery)
      ))
    );
  }
  
  displayCourses();
  updateCourseCount();
}

// ===== EVENT LISTENERS =====
function setupEventListeners() {
  // Search functionality
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchCourses(e.target.value);
    });
  }
  
  // Category filters
  const categoryButtons = document.querySelectorAll('[data-category]');
  categoryButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      const category = e.target.dataset.category;
      filterCourses(category);
      
      // Update active state
      categoryButtons.forEach(btn => btn.classList.remove('active'));
      e.target.classList.add('active');
    });
  });
  
  // Difficulty filters
  const difficultyButtons = document.querySelectorAll('[data-difficulty]');
  difficultyButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      const difficulty = e.target.dataset.difficulty;
      const currentCategory = document.querySelector('[data-category].active')?.dataset.category || 'All Courses';
      filterCourses(currentCategory, difficulty);
      
      // Update active state
      difficultyButtons.forEach(btn => btn.classList.remove('active'));
      e.target.classList.add('active');
    });
  });
}

// ===== NOTIFICATION SYSTEM =====
function showNotification(message, type = 'info') {
  // Remove existing notification
  const existing = document.querySelector('.notification');
  if (existing) {
    existing.remove();
  }
  
  // Create notification element
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.innerHTML = `
    <span>${message}</span>
    <button onclick="this.parentElement.remove()" aria-label="Close notification">&times;</button>
  `;
  
  // Add to page
  document.body.appendChild(notification);
  
  // Auto-remove after 5 seconds
  setTimeout(() => {
    if (notification.parentElement) {
      notification.remove();
    }
  }, 5000);
}

// ===== MAKE FUNCTIONS GLOBALLY AVAILABLE =====
window.showLoginModal = showLoginModal;
window.showSignupModal = showSignupModal;
window.closeModal = closeModal;
window.toggleTheme = toggleTheme;
window.toggleBookmark = toggleBookmark;
window.toggleLabBookmark = toggleLabBookmark;
window.launchCourse = launchCourse;
window.launchLab = launchLab;
window.toggleCourseSelection = toggleCourseSelection;
window.toggleLabSelection = toggleLabSelection;
window.showComparison = showComparison;
window.showLabComparison = showLabComparison;
window.showNotification = showNotification;
window.filterCourses = filterCourses;
window.searchCourses = searchCourses;

// ===== INITIALIZATION =====
// Initialize app when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeApp);
} else {
  initializeApp();
}

// Close modal when clicking outside
window.onclick = function(event) {
  const modals = document.querySelectorAll('.modal');
  modals.forEach(modal => {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });
}

console.log('✅ ImpactMojo Main JavaScript loaded successfully!');