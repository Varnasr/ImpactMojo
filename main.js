// Complete ImpactMojo Main JavaScript File
// Fixed version that handles undefined values properly

console.log('🚀 Loading ImpactMojo...');

// ===== GLOBAL VARIABLES =====
let allCourses = [];
let filteredCourses = [];
let selectedCourses = [];
let selectedLabs = [];
let userBookmarks = JSON.parse(localStorage.getItem('userBookmarks')) || [];
let userLabBookmarks = JSON.parse(localStorage.getItem('userLabBookmarks')) || [];

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
  updateCourseCount();
  setupEventListeners();
  
  console.log('✅ ImpactMojo initialized successfully!');
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

// ===== FIXED COURSE CARD CREATION =====
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

// ===== UTILITY FUNCTIONS =====
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
  } else {
    console.error('Course not found or URL missing:', courseId);
  }
}

function launchLab(labId) {
  const lab = labs.find(l => l.id === labId);
  if (lab && lab.url) {
    window.open(lab.url, '_blank');
  } else {
    console.error('Lab not found or URL missing:', labId);
  }
}

function toggleBookmark(courseId) {
  // Check if user is logged in
  if (typeof window.currentUser === 'undefined' || !window.currentUser) {
    alert('Please log in to bookmark courses');
    if (typeof showLoginModal === 'function') {
      showLoginModal();
    }
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
    alert('Please log in to bookmark labs');
    if (typeof showLoginModal === 'function') {
      showLoginModal();
    }
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

// ===== THEME TOGGLE =====
function toggleTheme() {
  const body = document.body;
  const themeIcon = document.getElementById('themeIcon');
  
  body.classList.toggle('dark-theme');
  
  if (themeIcon) {
    themeIcon.className = body.classList.contains('dark-theme') ? 
      'fas fa-sun' : 'fas fa-moon';
  }
  
  // Save theme preference
  localStorage.setItem('theme', body.classList.contains('dark-theme') ? 'dark' : 'light');
}

// ===== NOTIFICATION SYSTEM =====
function showNotification(message, type = 'info') {
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

// ===== INITIALIZATION =====
// Initialize app when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeApp);
} else {
  initializeApp();
}

// Apply saved theme
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
  document.body.classList.add('dark-theme');
  const themeIcon = document.getElementById('themeIcon');
  if (themeIcon) {
    themeIcon.className = 'fas fa-sun';
  }
}

console.log('✅ ImpactMojo Main JavaScript loaded successfully!');