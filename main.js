// ImpactMojo 101 - Main Application Logic
console.log('🚀 Loading ImpactMojo Main Application...');

// Global state
let allCourses = [];
let allLabs = [];
let filteredCourses = [];
let filteredLabs = [];
let selectedCourses = [];
let selectedLabs = [];
let bookmarkFilter = false;
let currentTheme = 'light';

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
  console.log('📱 DOM Content Loaded - Initializing app...');
  
  // Initialize theme first
  initializeTheme();
  
  // Wait for course data to be available
  if (typeof courseData !== 'undefined') {
    initializeApp();
  } else {
    // Wait for course-data.js to load
    setTimeout(() => {
      if (typeof courseData !== 'undefined') {
        initializeApp();
      } else {
        console.error('❌ Course data not available');
        showError('Failed to load course data');
      }
    }, 1000);
  }
});

function initializeApp() {
  console.log('🎯 Initializing ImpactMojo application...');
  
  try {
    // Load data
    loadCourseData();
    loadLabData();
    
    // Render content
    renderCourses();
    renderLabs();
    updateStats();
    
    // Setup event listeners
    setupEventListeners();
    
    console.log('✅ ImpactMojo application initialized successfully!');
  } catch (error) {
    console.error('❌ Error initializing app:', error);
    showError('Failed to initialize application');
  }
}

// Theme Management
function initializeTheme() {
  // Get saved theme or default to light
  const savedTheme = localStorage.getItem('impactmojo-theme') || 'light';
  currentTheme = savedTheme;
  
  // Apply theme
  document.documentElement.setAttribute('data-theme', currentTheme);
  
  // Update theme icon
  updateThemeIcon();
  
  console.log(`🎨 Theme initialized: ${currentTheme}`);
}

function toggleTheme() {
  currentTheme = currentTheme === 'light' ? 'dark' : 'light';
  
  // Apply theme
  document.documentElement.setAttribute('data-theme', currentTheme);
  
  // Save theme
  localStorage.setItem('impactmojo-theme', currentTheme);
  
  // Update icon
  updateThemeIcon();
  
  console.log(`🎨 Theme switched to: ${currentTheme}`);
}

function updateThemeIcon() {
  const themeIcon = document.getElementById('themeIcon');
  if (themeIcon) {
    themeIcon.className = currentTheme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
  }
}

// Data Loading
function loadCourseData() {
  if (typeof courseData !== 'undefined' && courseData.courses) {
    allCourses = [...courseData.courses];
    filteredCourses = [...allCourses];
    console.log(`📚 Loaded ${allCourses.length} courses`);
  } else {
    console.warn('⚠️ No course data available');
    allCourses = [];
    filteredCourses = [];
  }
}

function loadLabData() {
  if (typeof courseData !== 'undefined' && courseData.labs) {
    allLabs = [...courseData.labs];
    filteredLabs = [...allLabs];
    console.log(`🧪 Loaded ${allLabs.length} labs`);
  } else {
    console.warn('⚠️ No lab data available');
    allLabs = [];
    filteredLabs = [];
  }
}

// Event Listeners
function setupEventListeners() {
  // Search input
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', debounce(handleSearch, 300));
  }
  
  // Filter dropdowns
  const filters = ['categoryFilter', 'difficultyFilter', 'durationFilter'];
  filters.forEach(filterId => {
    const filter = document.getElementById(filterId);
    if (filter) {
      filter.addEventListener('change', handleFilter);
    }
  });
  
  // Theme toggle
  const themeToggle = document.querySelector('.theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }
  
  // Modal close listeners
  document.addEventListener('click', function(event) {
    if (event.target.classList.contains('modal')) {
      closeModal(event.target.id);
    }
  });
  
  console.log('🎧 Event listeners setup complete');
}

// Search and Filter Functions
function handleSearch() {
  const searchTerm = document.getElementById('searchInput')?.value.toLowerCase() || '';
  filterContent(searchTerm);
}

function handleFilter() {
  const searchTerm = document.getElementById('searchInput')?.value.toLowerCase() || '';
  filterContent(searchTerm);
}

function filterContent(searchTerm = '') {
  const category = document.getElementById('categoryFilter')?.value || 'all';
  const difficulty = document.getElementById('difficultyFilter')?.value || 'all';
  const duration = document.getElementById('durationFilter')?.value || 'all';
  
  // Filter courses
  filteredCourses = allCourses.filter(course => {
    const matchesSearch = !searchTerm || 
      course.title.toLowerCase().includes(searchTerm) ||
      course.description.toLowerCase().includes(searchTerm) ||
      course.category.toLowerCase().includes(searchTerm);
    
    const matchesCategory = category === 'all' || course.category.toLowerCase() === category;
    const matchesDifficulty = difficulty === 'all' || course.difficulty.toLowerCase() === difficulty;
    const matchesDuration = duration === 'all' || checkDurationMatch(course.duration, duration);
    const matchesBookmark = !bookmarkFilter || (typeof userBookmarks !== 'undefined' && userBookmarks.includes(course.id));
    
    return matchesSearch && matchesCategory && matchesDifficulty && matchesDuration && matchesBookmark;
  });
  
  // Filter labs
  filteredLabs = allLabs.filter(lab => {
    const matchesSearch = !searchTerm || 
      lab.title.toLowerCase().includes(searchTerm) ||
      lab.description.toLowerCase().includes(searchTerm) ||
      lab.category.toLowerCase().includes(searchTerm);
    
    return matchesSearch;
  });
  
  renderCourses();
  renderLabs();
  updateStats();
}

function checkDurationMatch(courseDuration, filterDuration) {
  const duration = parseInt(courseDuration);
  switch (filterDuration) {
    case 'short': return duration < 2;
    case 'medium': return duration >= 2 && duration <= 4;
    case 'long': return duration > 4;
    default: return true;
  }
}

function clearAllFilters() {
  // Reset search
  const searchInput = document.getElementById('searchInput');
  if (searchInput) searchInput.value = '';
  
  // Reset filters
  const categoryFilter = document.getElementById('categoryFilter');
  if (categoryFilter) categoryFilter.value = 'all';
  
  const difficultyFilter = document.getElementById('difficultyFilter');
  if (difficultyFilter) difficultyFilter.value = 'all';
  
  const durationFilter = document.getElementById('durationFilter');
  if (durationFilter) durationFilter.value = 'all';
  
  // Reset bookmark filter
  bookmarkFilter = false;
  updateBookmarkToggle();
  
  // Apply filters
  filterContent();
  
  showNotification('All filters cleared', 'success');
}

function toggleBookmarkFilter() {
  if (typeof currentUser === 'undefined' || !currentUser) {
    showNotification('Please log in to view bookmarks', 'error');
    showLoginModal();
    return;
  }
  
  bookmarkFilter = !bookmarkFilter;
  updateBookmarkToggle();
  filterContent();
  
  if (bookmarkFilter) {
    showNotification('Showing bookmarked courses only', 'info');
  } else {
    showNotification('Showing all courses', 'info');
  }
}

function updateBookmarkToggle() {
  const toggleBtn = document.getElementById('bookmarkToggle');
  if (toggleBtn) {
    if (bookmarkFilter) {
      toggleBtn.innerHTML = '<i class="fas fa-times"></i> Show All Courses';
      toggleBtn.classList.add('active');
    } else {
      toggleBtn.innerHTML = '<i class="fas fa-bookmark"></i> Show My Bookmarks';
      toggleBtn.classList.remove('active');
    }
  }
}

// Rendering Functions
function renderCourses() {
  const container = document.getElementById('courseContainer');
  if (!container) {
    console.error('❌ Course container not found');
    return;
  }
  
  if (filteredCourses.length === 0) {
    container.innerHTML = `
      <div class="no-results">
        <i class="fas fa-search"></i>
        <h3>No courses found</h3>
        <p>Try adjusting your search terms or filters to find what you're looking for.</p>
      </div>
    `;
    return;
  }
  
  container.innerHTML = filteredCourses.map(course => createCourseCard(course)).join('');
  console.log(`📚 Rendered ${filteredCourses.length} courses`);
}

function renderLabs() {
  const container = document.getElementById('labsContainer');
  if (!container) {
    console.error('❌ Lab container not found');
    return;
  }
  
  if (filteredLabs.length === 0) {
    container.innerHTML = `
      <div class="no-results">
        <i class="fas fa-flask"></i>
        <h3>No labs found</h3>
        <p>Try adjusting your search terms to find what you're looking for.</p>
      </div>
    `;
    return;
  }
  
  container.innerHTML = filteredLabs.map(lab => createLabCard(lab)).join('');
  console.log(`🧪 Rendered ${filteredLabs.length} labs`);
}

function createCourseCard(course) {
  const isBookmarked = typeof userBookmarks !== 'undefined' && userBookmarks.includes(course.id);
  const bookmarkIcon = isBookmarked ? 'fas fa-bookmark' : 'far fa-bookmark';
  
  return `
    <div class="course-card" data-category="${course.category}" data-difficulty="${course.difficulty}">
      <div class="course-card-header">
        <div class="course-category" style="background-color: ${course.categoryColor}20; color: ${course.categoryColor}">
          ${course.category}
        </div>
        <div class="course-actions">
          <button class="action-btn bookmark-btn ${isBookmarked ? 'bookmarked' : ''}" 
                  onclick="toggleBookmark('${course.id}')" 
                  data-course-id="${course.id}" 
                  title="Bookmark this course">
            <i class="${bookmarkIcon}"></i>
          </button>
          <button class="action-btn share-btn" onclick="shareCourse('${course.id}')" title="Share course">
            <i class="fas fa-share-alt"></i>
          </button>
          <button class="action-btn compare-btn" onclick="addToComparison('${course.id}')" title="Add to comparison">
            <i class="fas fa-balance-scale"></i>
          </button>
        </div>
      </div>
      
      <div class="course-content">
        <h3 class="course-title">${course.title}</h3>
        <p class="course-description">${course.description}</p>
        
        <div class="course-meta">
          <span><i class="fas fa-clock"></i> ${course.duration} hours</span>
          <span><i class="fas fa-signal"></i> ${course.difficulty}</span>
          <span><i class="fas fa-users"></i> ${course.learners || '0'} learners</span>
          <span><i class="fas fa-star"></i> ${course.rating || 'New'}</span>
        </div>
      </div>
      
      <div class="course-card-footer">
        <button class="launch-btn" onclick="launchCourse('${course.id}')">
          <i class="fas fa-play"></i> Launch Course
        </button>
      </div>
    </div>
  `;
}

function createLabCard(lab) {
  return `
    <div class="lab-card" data-category="${lab.category}">
      <div class="lab-card-header">
        <div class="lab-category">
          ${lab.category}
        </div>
        <div class="lab-actions">
          <button class="action-btn" onclick="shareLab('${lab.id}')" title="Share lab">
            <i class="fas fa-share-alt"></i>
          </button>
          <button class="action-btn" onclick="addLabToComparison('${lab.id}')" title="Add to comparison">
            <i class="fas fa-balance-scale"></i>
          </button>
        </div>
      </div>
      
      <div class="lab-content">
        <h3 class="lab-title">${lab.title}</h3>
        <p class="lab-description">${lab.description}</p>
        
        <div class="lab-meta">
          <span><i class="fas fa-clock"></i> ${lab.duration} minutes</span>
          <span><i class="fas fa-code"></i> ${lab.type}</span>
          <span><i class="fas fa-users"></i> ${lab.users || '0'} users</span>
        </div>
      </div>
      
      <div class="lab-card-footer">
        <button class="lab-launch" onclick="launchLab('${lab.id}')">
          <i class="fas fa-play"></i> Launch Lab
        </button>
      </div>
    </div>
  `;
}

function updateStats() {
  // Update course count
  const courseCount = document.getElementById('courseCount');
  if (courseCount) {
    courseCount.textContent = filteredCourses.length;
  }
  
  // Update lab count
  const labCount = document.getElementById('labCount');
  if (labCount) {
    labCount.textContent = filteredLabs.length;
  }
}

// Action Functions
function launchCourse(courseId) {
  const course = allCourses.find(c => c.id === courseId);
  if (course && course.url) {
    window.open(course.url, '_blank');
    
    // Update user progress if logged in
    if (typeof updateUserProgress === 'function' && typeof currentUser !== 'undefined' && currentUser) {
      updateUserProgress(courseId, { lastAccessed: new Date() });
    }
  } else {
    showNotification('Course not available yet', 'error');
  }
}

function launchLab(labId) {
  const lab = allLabs.find(l => l.id === labId);
  if (lab && lab.url) {
    window.open(lab.url, '_blank');
  } else {
    showNotification('Lab not available yet', 'error');
  }
}

function shareCourse(courseId) {
  const course = allCourses.find(c => c.id === courseId);
  if (course) {
    const url = `${window.location.origin}${window.location.pathname}#course-${courseId}`;
    const text = `Check out this course: ${course.title} - ${course.description}`;
    
    if (navigator.share) {
      navigator.share({
        title: course.title,
        text: text,
        url: url
      });
    } else {
      // Fallback: copy to clipboard
      navigator.clipboard.writeText(`${text}\n${url}`).then(() => {
        showNotification('Course link copied to clipboard!', 'success');
      });
    }
  }
}

function shareLab(labId) {
  const lab = allLabs.find(l => l.id === labId);
  if (lab) {
    const url = `${window.location.origin}${window.location.pathname}#lab-${labId}`;
    const text = `Check out this lab: ${lab.title} - ${lab.description}`;
    
    if (navigator.share) {
      navigator.share({
        title: lab.title,
        text: text,
        url: url
      });
    } else {
      // Fallback: copy to clipboard
      navigator.clipboard.writeText(`${text}\n${url}`).then(() => {
        showNotification('Lab link copied to clipboard!', 'success');
      });
    }
  }
}

function addToComparison(courseId) {
  if (!selectedCourses.includes(courseId)) {
    selectedCourses.push(courseId);
    updateComparisonButton();
    showNotification('Course added to comparison', 'success');
  } else {
    showNotification('Course already in comparison', 'info');
  }
}

function addLabToComparison(labId) {
  if (!selectedLabs.includes(labId)) {
    selectedLabs.push(labId);
    updateLabComparisonButton();
    showNotification('Lab added to comparison', 'success');
  } else {
    showNotification('Lab already in comparison', 'info');
  }
}

function updateComparisonButton() {
  const compareBtn = document.getElementById('compareBtn');
  const compareCount = document.getElementById('compareCount');
  
  if (compareBtn && compareCount) {
    compareCount.textContent = selectedCourses.length;
    compareBtn.style.display = selectedCourses.length > 0 ? 'block' : 'none';
  }
}

function updateLabComparisonButton() {
  const compareBtn = document.getElementById('labCompareBtn');
  const compareCount = document.getElementById('labCompareCount');
  
  if (compareBtn && compareCount) {
    compareCount.textContent = selectedLabs.length;
    compareBtn.style.display = selectedLabs.length > 0 ? 'block' : 'none';
  }
}

function showComparison() {
  if (selectedCourses.length === 0) {
    showNotification('Please select courses to compare', 'info');
    return;
  }
  
  const courses = selectedCourses.map(id => allCourses.find(c => c.id === id)).filter(Boolean);
  console.log('Comparing courses:', courses);
  showNotification(`Comparing ${courses.length} courses - Feature coming soon!`, 'info');
}

function showLabComparison() {
  if (selectedLabs.length === 0) {
    showNotification('Please select labs to compare', 'info');
    return;
  }
  
  const labs = selectedLabs.map(id => allLabs.find(l => l.id === id)).filter(Boolean);
  console.log('Comparing labs:', labs);
  showNotification(`Comparing ${labs.length} labs - Feature coming soon!`, 'info');
}

// Modal Functions
function showLoginModal() {
  const modal = document.getElementById('loginModal');
  if (modal) {
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
}

function showSignupModal() {
  const modal = document.getElementById('signupModal');
  if (modal) {
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  }
}

// Notification System
function showNotification(message, type = 'info') {
  // Remove existing notifications
  const existingNotifications = document.querySelectorAll('.notification');
  existingNotifications.forEach(notification => notification.remove());
  
  // Create new notification
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.innerHTML = `
    <span>${message}</span>
    <button onclick="this.parentElement.remove()">&times;</button>
  `;
  
  document.body.appendChild(notification);
  
  // Auto remove after 5 seconds
  setTimeout(() => {
    if (notification.parentElement) {
      notification.remove();
    }
  }, 5000);
}

function showError(message) {
  const containers = ['courseContainer', 'labsContainer'];
  containers.forEach(containerId => {
    const container = document.getElementById(containerId);
    if (container) {
      container.innerHTML = `
        <div class="error">
          <i class="fas fa-exclamation-triangle"></i>
          <h3>Error</h3>
          <p>${message}</p>
        </div>
      `;
    }
  });
}

// Utility Functions
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Make functions globally available
window.toggleTheme = toggleTheme;
window.handleSearch = handleSearch;
window.handleFilter = handleFilter;
window.clearAllFilters = clearAllFilters;
window.toggleBookmarkFilter = toggleBookmarkFilter;
window.launchCourse = launchCourse;
window.launchLab = launchLab;
window.shareCourse = shareCourse;
window.shareLab = shareLab;
window.addToComparison = addToComparison;
window.addLabToComparison = addLabToComparison;
window.showComparison = showComparison;
window.showLabComparison = showLabComparison;
window.showLoginModal = showLoginModal;
window.showSignupModal = showSignupModal;
window.closeModal = closeModal;
window.showNotification = showNotification;

console.log('✅ ImpactMojo Main Application loaded successfully!');