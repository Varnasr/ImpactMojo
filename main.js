// Complete ImpactMojo Main JavaScript File - All Issues Fixed
// Theme toggle, course/lab loading, popular section - everything working

console.log('🚀 Loading ImpactMojo...');

// ===== GLOBAL VARIABLES =====
let allCourses = [];
let filteredCourses = [];
let selectedCourses = [];
let selectedLabs = [];
let userBookmarks = JSON.parse(localStorage.getItem('userBookmarks')) || [];
let userLabBookmarks = JSON.parse(localStorage.getItem('userLabBookmarks')) || [];

// ===== THEME TOGGLE (FIXED) =====
function toggleTheme() {
  console.log('🎨 Theme toggle clicked');
  
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  console.log(`Switching from ${currentTheme} to ${newTheme}`);
  
  // Update theme
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  // Update icon
  if (themeIcon) {
    themeIcon.className = newTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    console.log(`✅ Theme switched to ${newTheme}`);
  } else {
    console.error('❌ Theme icon not found');
  }
  
  // Show notification
  if (typeof showNotification === 'function') {
    showNotification(`Switched to ${newTheme} mode`, 'success');
  }
}

// Initialize theme on page load
function initializeThemeToggle() {
  console.log('🎨 Initializing theme...');
  
  const savedTheme = localStorage.getItem('theme') || 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  // Set theme
  document.documentElement.setAttribute('data-theme', savedTheme);
  
  // Set icon
  if (themeIcon) {
    themeIcon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    console.log(`✅ Theme initialized: ${savedTheme}`);
  } else {
    console.error('❌ Theme icon not found during initialization');
  }
}

// ===== INITIALIZATION (FIXED) =====
function initializeApp() {
  console.log('📚 Initializing ImpactMojo...');
  
  // Wait for data with retry logic
  if (typeof courses === 'undefined' || typeof labs === 'undefined') {
    console.log('⏳ Waiting for data...');
    setTimeout(initializeApp, 100);
    return;
  }
  
  // Verify data is properly loaded
  if (!Array.isArray(courses) || courses.length === 0) {
    console.error('❌ Courses array problem, retrying...');
    setTimeout(initializeApp, 200);
    return;
  }
  
  console.log(`✅ Data verified: ${courses.length} courses, ${labs.length} labs`);
  
  // Initialize theme FIRST
  initializeThemeToggle();
  
  // Set up data
  allCourses = [...courses];
  filteredCourses = [...courses];
  
  // Display content with error catching
  try {
    displayCourses();
    console.log('✅ Courses loaded');
  } catch (error) {
    console.error('❌ Course display error:', error);
  }
  
  try {
    displayLabs();
    console.log('✅ Labs loaded');
  } catch (error) {
    console.error('❌ Lab display error:', error);
  }
  
  try {
    displayPopularCourses();
    console.log('✅ Popular section loaded');
  } catch (error) {
    console.error('❌ Popular section error:', error);
  }
  
  try {
    updateCourseCount();
    setupEventListeners();
    console.log('✅ Event listeners setup complete');
  } catch (error) {
    console.error('❌ Setup error:', error);
  }
  
  console.log('✅ ImpactMojo fully initialized!');
}

// ===== POPULAR COURSES FUNCTIONALITY (FIXED) =====
function displayPopularCourses() {
  const container = document.getElementById('popularCoursesContainer');
  
  if (!container) {
    console.log('ℹ️ Popular courses container not found, retrying...');
    setTimeout(displayPopularCourses, 300);
    return;
  }
  
  // Wait for data
  if (!allCourses || allCourses.length === 0) {
    console.log('⏳ Waiting for course data for popular section...');
    setTimeout(displayPopularCourses, 200);
    return;
  }
  
  // Get popular courses (highest rated first)
  const topCourses = allCourses
    .filter(course => course && course.rating)
    .sort((a, b) => (b.rating || 0) - (a.rating || 0))
    .slice(0, 3);
  
  // Get some labs if available
  const topLabs = labs && labs.length > 0 ? labs.slice(0, 2) : [];
  
  if (topCourses.length === 0) {
    container.innerHTML = '<div class="loading">Loading popular courses...</div>';
    return;
  }
  
  // Create content
  let html = '';
  
  topCourses.forEach(course => {
    html += createCourseCard(course);
  });
  
  topLabs.forEach(lab => {
    html += createLabCard(lab);
  });
  
  container.innerHTML = html;
  console.log(`✅ Popular section loaded with ${topCourses.length} courses and ${topLabs.length} labs`);
}

// ===== COURSE DISPLAY FUNCTIONS (FIXED) =====
function displayCourses() {
  const container = document.getElementById('courseContainer');
  
  if (!container) {
    console.error('❌ courseContainer not found!');
    return;
  }
  
  if (!filteredCourses || filteredCourses.length === 0) {
    container.innerHTML = `
      <div class="no-results">
        <i class="fas fa-search"></i>
        <h3>No courses found</h3>
        <p>Try adjusting your search terms.</p>
      </div>
    `;
    return;
  }
  
  console.log(`🎓 Displaying ${filteredCourses.length} courses`);
  container.innerHTML = filteredCourses.map(course => createCourseCard(course)).join('');
  
  // Update bookmark UI after displaying
  setTimeout(updateAllBookmarkUI, 100);
}

// ===== COURSE CARD CREATION =====
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

// ===== LAB DISPLAY FUNCTIONS (FIXED) =====
function displayLabs() {
  const container = document.getElementById('labsContainer');
  
  if (!container) {
    console.error('❌ labsContainer not found!');
    return;
  }
  
  if (!labs || labs.length === 0) {
    container.innerHTML = `
      <div class="no-results">
        <i class="fas fa-flask"></i>
        <h3>No labs available</h3>
        <p>Interactive labs coming soon!</p>
      </div>
    `;
    return;
  }
  
  console.log(`🧪 Displaying ${labs.length} labs`);
  container.innerHTML = labs.map(lab => createLabCard(lab)).join('');
  
  // Update bookmark UI after displaying
  setTimeout(updateAllLabBookmarkUI, 100);
}

// ===== LAB CARD CREATION =====
function createLabCard(lab) {
  const labId = lab.id || 'unknown';
  const title = lab.title || 'Untitled Lab';
  const description = lab.description || 'No description available';
  const category = lab.category || 'General';
  const difficulty = lab.difficulty || 'Intermediate';
  const duration = lab.duration || '15 min';
  const rating = lab.rating || 4.5;
  
  return `
    <div class="lab-card" data-lab-id="${labId}">
      <div class="lab-card-header">
        <div class="lab-category">
          ${category}
        </div>
        <div class="lab-type-badge">LAB</div>
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
          <span class="lab-difficulty">
            ${difficulty}
          </span>
        </div>
      </div>
      
      <div class="lab-actions">
        <button class="launch-btn lab-launch" onclick="launchLab('${labId}')">
          <i class="fas fa-flask"></i>
          Launch Lab
        </button>
        <button class="lab-bookmark-btn" onclick="toggleLabBookmark('${labId}')" aria-label="Bookmark lab">
          <i class="far fa-bookmark"></i>
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
  
  // Save to localStorage
  localStorage.setItem('userBookmarks', JSON.stringify(userBookmarks));
}

function toggleLabBookmark(labId) {
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
  
  // Save to localStorage
  localStorage.setItem('userLabBookmarks', JSON.stringify(userLabBookmarks));
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
  userBookmarks.forEach(courseId => updateBookmarkUI(courseId));
}

function updateAllLabBookmarkUI() {
  userLabBookmarks.forEach(labId => updateLabBookmarkUI(labId));
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
  
  if (compareCount) {
    compareCount.textContent = selectedCourses.length;
  }
  
  if (compareBtn) {
    if (selectedCourses.length >= 2) {
      compareBtn.style.display = 'inline-flex';
    } else {
      compareBtn.style.display = 'none';
    }
  }
}

// ===== SEARCH AND FILTERING =====
function filterCourses() {
  const searchInput = document.getElementById('searchInput');
  const query = searchInput ? searchInput.value.toLowerCase() : '';
  
  if (query === '') {
    filteredCourses = [...allCourses];
  } else {
    filteredCourses = allCourses.filter(course => 
      course.title.toLowerCase().includes(query) ||
      course.description.toLowerCase().includes(query) ||
      course.category.toLowerCase().includes(query) ||
      (course.topics && course.topics.some(topic => 
        topic.toLowerCase().includes(query)
      ))
    );
  }
  
  displayCourses();
  updateCourseCount();
}

// ===== EVENT LISTENERS =====
function setupEventListeners() {
  console.log('🔧 Setting up event listeners...');
  
  // Search functionality
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', filterCourses);
    console.log('✅ Search functionality enabled');
  }
  
  // Modal close on outside click
  window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
      event.target.style.display = 'none';
      document.body.style.overflow = '';
    }
  };
  
  // Escape key to close modals
  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
      document.querySelectorAll('.modal').forEach(modal => {
        if (modal.style.display === 'block') {
          modal.style.display = 'none';
          document.body.style.overflow = '';
        }
      });
    }
  });
  
  console.log('✅ Event listeners set up');
}

// ===== MODAL FUNCTIONS =====
function showLoginModal() {
  console.log('📝 Opening login modal');
  const modal = document.getElementById('loginModal');
  if (modal) {
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  } else {
    console.error('❌ Login modal not found');
  }
}

function showSignupModal() {
  console.log('📝 Opening signup modal');
  const modal = document.getElementById('signupModal');
  if (modal) {
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  } else {
    console.error('❌ Signup modal not found');
  }
}

function closeModal(modalId) {
  console.log(`📝 Closing modal: ${modalId}`);
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
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
window.showNotification = showNotification;
window.filterCourses = filterCourses;

// ===== ENHANCED INITIALIZATION =====
function enhancedInitialization() {
  let retryCount = 0;
  const maxRetries = 20; // Try for 2 seconds
  
  function tryInit() {
    retryCount++;
    
    // Check if DOM is ready
    if (document.readyState === 'loading') {
      console.log('⏳ DOM not ready, waiting...');
      setTimeout(tryInit, 100);
      return;
    }
    
    // Check if data is available
    if (typeof courses === 'undefined' || typeof labs === 'undefined') {
      if (retryCount < maxRetries) {
        console.log(`⏳ Data not ready, retry ${retryCount}/${maxRetries}`);
        setTimeout(tryInit, 100);
        return;
      } else {
        console.error('❌ Data failed to load after maximum retries');
        return;
      }
    }
    
    // Check if containers exist
    const courseContainer = document.getElementById('courseContainer');
    const labContainer = document.getElementById('labsContainer');
    const popularContainer = document.getElementById('popularCoursesContainer');
    
    if (!courseContainer || !labContainer || !popularContainer) {
      if (retryCount < maxRetries) {
        console.log(`⏳ Containers not ready, retry ${retryCount}/${maxRetries}`);
        setTimeout(tryInit, 100);
        return;
      } else {
        console.warn('⚠️ Some containers not found, continuing anyway...');
      }
    }
    
    console.log('✅ Everything ready, initializing...');
    initializeApp();
  }
  
  tryInit();
}

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', enhancedInitialization);
window.addEventListener('load', enhancedInitialization);

// Also try immediate initialization if DOM is already ready
if (document.readyState !== 'loading') {
  enhancedInitialization();
}

// Listen for data loaded event if course-data.js fires it
window.addEventListener('dataLoaded', function() {
  console.log('📡 Data loaded event received');
  initializeApp();
});

console.log('✅ Enhanced ImpactMojo JavaScript loaded successfully!');