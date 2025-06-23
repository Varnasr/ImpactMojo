// Main Application JavaScript
// Contains all the core functionality for ImpactMojo

// Global variables
let currentFilters = {
  search: '',
  category: 'all',
  difficulty: 'all',
  duration: 'all'
};
let currentView = 'grid';
let currentBookmarkFilter = false;
let savedSearches = JSON.parse(localStorage.getItem('impactmojo_saved_searches')) || [];

// Initialize application when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  initializeApp();
});

// Initialize the application
function initializeApp() {
  initializeTheme();
  renderCourses();
  renderLabs();
  loadSavedSearches();
  updateCourseCount();
  
  // Set up event listeners
  setupEventListeners();
}

// Set up event listeners
function setupEventListeners() {
  // Mobile menu toggle
  const mobileToggle = document.querySelector('.mobile-menu-toggle button');
  if (mobileToggle) {
    mobileToggle.addEventListener('click', toggleMobileMenu);
  }
  
  // Close mobile menu when clicking outside
  document.addEventListener('click', function(event) {
    const navMenu = document.querySelector('.nav-menu');
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    
    if (navMenu && mobileToggle && 
        !navMenu.contains(event.target) && 
        !mobileToggle.contains(event.target)) {
      navMenu.classList.remove('mobile-active');
    }
  });
}

// Theme functionality
function initializeTheme() {
  const savedTheme = localStorage.getItem('impactmojo_theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('impactmojo_theme', newTheme);
  updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
  const themeIcon = document.getElementById('themeIcon');
  if (themeIcon) {
    themeIcon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
}

// Mobile menu functionality
function toggleMobileMenu() {
  const navMenu = document.querySelector('.nav-menu');
  if (navMenu) {
    navMenu.classList.toggle('mobile-active');
  }
}

// Course rendering and filtering
function renderCourses() {
  const container = document.getElementById('courseContainer');
  if (!container || !window.coursesData) return;
  
  const filteredCourses = filterCourses();
  container.innerHTML = '';
  
  if (filteredCourses.length === 0) {
    showNoResults();
    return;
  }
  
  hideNoResults();
  
  filteredCourses.forEach(course => {
    const courseCard = createCourseCard(course);
    container.appendChild(courseCard);
  });
  
  updateCourseCount();
}

function createCourseCard(course) {
  const card = document.createElement('div');
  card.className = 'course-card';
  card.innerHTML = `
    <div class="course-header">
      <div class="course-number">Course ${course.number}</div>
      <h3 class="course-title">${course.title}</h3>
      <div class="course-meta">
        <span class="meta-tag">${course.category}</span>
        <span class="meta-tag">${course.difficulty}</span>
        <span class="meta-tag">${course.duration}</span>
      </div>
    </div>
    
    <div class="course-description">
      ${course.description}
    </div>
    
    <div class="course-stats">
      <div class="course-stat">
        <i class="fas fa-star"></i>
        <span class="number">${course.rating}</span>
      </div>
      <div class="course-stat">
        <i class="fas fa-users"></i>
        <span class="number">${course.learnerCount.toLocaleString()}</span>
        <span>learners</span>
      </div>
    </div>
    
    <div class="course-actions">
      <div class="course-actions-left">
        <a href="${course.url}" class="launch-btn" target="_blank">
          <i class="fas fa-play"></i>
          Launch Course
        </a>
      </div>
      <div class="course-actions-right">
        <button class="bookmark-btn" onclick="toggleBookmark('${course.id}')" data-course-id="${course.id}">
          <i class="far fa-bookmark"></i>
        </button>
        <button class="expand-btn" onclick="toggleCourseDetails('${course.id}')">
          <i class="fas fa-info-circle"></i>
        </button>
      </div>
    </div>
    
    <div class="course-details hidden" id="details-${course.id}">
      <div class="detail-section">
        <h4>Prerequisites</h4>
        <ul>
          ${course.prerequisites.map(prereq => `<li>${prereq}</li>`).join('')}
        </ul>
      </div>
      <div class="detail-section">
        <h4>Learning Outcomes</h4>
        <ul>
          ${course.outcomes.map(outcome => `<li>${outcome}</li>`).join('')}
        </ul>
      </div>
      <div class="detail-section">
        <h4>Target Audience</h4>
        <p>${course.audience}</p>
      </div>
    </div>
  `;
  
  return card;
}

function toggleCourseDetails(courseId) {
  const details = document.getElementById(`details-${courseId}`);
  if (details) {
    details.classList.toggle('hidden');
  }
}

// Filtering functionality
function filterCourses() {
  if (!window.coursesData) return [];
  
  let filtered = window.coursesData;
  
  // Apply bookmark filter
  if (currentBookmarkFilter && userBookmarks) {
    filtered = filtered.filter(course => userBookmarks.includes(course.id));
  }
  
  // Apply search filter
  if (currentFilters.search) {
    const searchTerm = currentFilters.search.toLowerCase();
    filtered = filtered.filter(course => 
      course.title.toLowerCase().includes(searchTerm) ||
      course.description.toLowerCase().includes(searchTerm) ||
      course.category.toLowerCase().includes(searchTerm) ||
      course.audience.toLowerCase().includes(searchTerm)
    );
  }
  
  // Apply category filter
  if (currentFilters.category !== 'all') {
    filtered = filtered.filter(course => course.category === currentFilters.category);
  }
  
  // Apply difficulty filter
  if (currentFilters.difficulty !== 'all') {
    filtered = filtered.filter(course => course.difficulty === currentFilters.difficulty);
  }
  
  // Apply duration filter
  if (currentFilters.duration !== 'all') {
    filtered = filtered.filter(course => {
      const duration = course.duration;
      switch (currentFilters.duration) {
        case 'short':
          return duration.includes('2') || duration.includes('1');
        case 'medium':
          return duration.includes('3') || duration.includes('4');
        case 'long':
          return duration.includes('5') || duration.includes('6') || duration.includes('4+');
        default:
          return true;
      }
    });
  }
  
  return filtered;
}

function searchCourses() {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    currentFilters.search = searchInput.value;
    currentBookmarkFilter = false; // Reset bookmark filter when searching
    renderCourses();
  }
}

function filterCoursesByCategory() {
  const categoryFilter = document.getElementById('categoryFilter');
  if (categoryFilter) {
    currentFilters.category = categoryFilter.value;
    renderCourses();
  }
}

function filterDecks() {
  const levelFilter = document.getElementById('levelFilter');
  const durationFilter = document.getElementById('durationFilter');
  
  if (levelFilter) currentFilters.difficulty = levelFilter.value;
  if (durationFilter) currentFilters.duration = durationFilter.value;
  
  renderCourses();
}

function clearAllFilters() {
  currentFilters = {
    search: '',
    category: 'all',
    difficulty: 'all',
    duration: 'all'
  };
  currentBookmarkFilter = false;
  
  // Reset form inputs
  const searchInput = document.getElementById('searchInput');
  const categoryFilter = document.getElementById('categoryFilter');
  const levelFilter = document.getElementById('levelFilter');
  const durationFilter = document.getElementById('durationFilter');
  
  if (searchInput) searchInput.value = '';
  if (categoryFilter) categoryFilter.value = 'all';
  if (levelFilter) levelFilter.value = 'all';
  if (durationFilter) durationFilter.value = 'all';
  
  renderCourses();
}

function filterByPath(pathType) {
  let categoryFilter = '';
  
  switch (pathType) {
    case 'data-analysis':
      categoryFilter = 'Data Analysis';
      break;
    case 'gender-studies':
      categoryFilter = 'Gender Studies';
      break;
    case 'economics':
      categoryFilter = 'Economics';
      break;
    case 'justice':
      categoryFilter = 'Justice';
      break;
  }
  
  currentFilters.category = categoryFilter;
  const categorySelect = document.getElementById('categoryFilter');
  if (categorySelect) {
    categorySelect.value = categoryFilter;
  }
  
  renderCourses();
  
  // Scroll to courses section
  const coursesSection = document.getElementById('courses');
  if (coursesSection) {
    coursesSection.scrollIntoView({ behavior: 'smooth' });
  }
}

// Advanced search functionality
function toggleAdvancedSearch() {
  const advancedSearch = document.getElementById('advancedSearch');
  if (advancedSearch) {
    advancedSearch.classList.toggle('hidden');
  }
}

function addOperator(operator) {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    const currentValue = searchInput.value;
    const cursorPosition = searchInput.selectionStart;
    const newValue = currentValue.slice(0, cursorPosition) + ' ' + operator + ' ' + currentValue.slice(cursorPosition);
    searchInput.value = newValue;
    searchInput.focus();
  }
}

function saveCurrentSearch() {
  const searchInput = document.getElementById('searchInput');
  if (!searchInput || !searchInput.value.trim()) {
    showNotification('Please enter a search term first', 'error');
    return;
  }
  
  const searchTerm = searchInput.value.trim();
  
  if (!savedSearches.includes(searchTerm)) {
    savedSearches.push(searchTerm);
    localStorage.setItem('impactmojo_saved_searches', JSON.stringify(savedSearches));
    loadSavedSearches();
    showNotification('Search saved!', 'success');
  } else {
    showNotification('Search already saved', 'info');
  }
}

function loadSavedSearches() {
  const container = document.getElementById('savedSearches');
  if (!container) return;
  
  container.innerHTML = '';
  
  savedSearches.forEach(search => {
    const searchItem = document.createElement('span');
    searchItem.className = 'saved-search-item';
    searchItem.textContent = search;
    searchItem.onclick = () => applySavedSearch(search);
    container.appendChild(searchItem);
  });
}

function applySavedSearch(searchTerm) {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.value = searchTerm;
    searchCourses();
  }
}

// View functionality
function setView(viewType) {
  currentView = viewType;
  
  // Update view buttons
  const viewButtons = document.querySelectorAll('.view-btn');
  viewButtons.forEach(btn => {
    btn.classList.remove('active');
    if (btn.dataset.view === viewType) {
      btn.classList.add('active');
    }
  });
  
  // Update courses container class
  const container = document.getElementById('courseContainer');
  if (container) {
    container.className = viewType === 'grid' ? 'courses-grid' : 'courses-list';
  }
}

// Course count functionality
function updateCourseCount() {
  const filteredCourses = filterCourses();
  const visibleCount = document.getElementById('visibleCount');
  const totalCount = document.getElementById('totalCount');
  
  if (visibleCount) visibleCount.textContent = filteredCourses.length;
  if (totalCount) totalCount.textContent = window.coursesData ? window.coursesData.length : 0;
}

// No results functionality
function showNoResults() {
  const noResults = document.getElementById('noResults');
  if (noResults) {
    noResults.classList.remove('hidden');
  }
}

function hideNoResults() {
  const noResults = document.getElementById('noResults');
  if (noResults) {
    noResults.classList.add('hidden');
  }
}

// Labs rendering
function renderLabs() {
  const container = document.getElementById('labsContainer');
  if (!container || !window.labsData) return;
  
  container.innerHTML = '';
  
  window.labsData.forEach(lab => {
    const labCard = createLabCard(lab);
    container.appendChild(labCard);
  });
}

function createLabCard(lab) {
  const card = document.createElement('div');
  card.className = 'lab-card';
  
  const statusColor = getStatusColor(lab.statusClass);
  
  card.innerHTML = `
    <div class="lab-header">
      <h3 class="lab-title">${lab.title}</h3>
      <span class="lab-status" style="background-color: ${statusColor};">${lab.status}</span>
    </div>
    <p class="lab-description">${lab.description}</p>
    <div class="lab-features">
      <ul>
        ${lab.features.map(feature => `<li>${feature}</li>`).join('')}
      </ul>
    </div>
    <a href="${lab.url}" class="lab-launch-btn" ${lab.url === '#' ? 'onclick="return false;" style="opacity: 0.5; cursor: not-allowed;"' : 'target="_blank"'}>
      <i class="fas fa-rocket"></i>
      ${lab.status === 'Coming Soon' || lab.status === 'Research' ? 'Coming Soon' : 'Launch Lab'}
    </a>
  `;
  
  return card;
}

function getStatusColor(statusClass) {
  switch (statusClass) {
    case 'success': return '#2ecc71';
    case 'warning': return '#f39c12';
    case 'info': return '#3498db';
    case 'secondary': return '#95a5a6';
    case 'dark': return '#34495e';
    default: return '#3498db';
  }
}

// Section navigation
function showSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
  }
}

// Utility functions
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

// Add debounced search
const debouncedSearch = debounce(searchCourses, 300);

// Update search input to use debounced search
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', debouncedSearch);
  }
});

// Error handling
window.addEventListener('error', function(event) {
  console.error('Application error:', event.error);
  showNotification('An error occurred. Please refresh the page.', 'error');
});

// Performance monitoring (simple)
if ('performance' in window) {
  window.addEventListener('load', function() {
    setTimeout(() => {
      const perfData = performance.getEntriesByType('navigation')[0];
      console.log('Page load time:', perfData.loadEventEnd - perfData.loadEventStart, 'ms');
    }, 0);
  });
}

// Service worker registration (if available)
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/sw.js')
      .then(function(registration) {
        console.log('SW registered: ', registration);
      })
      .catch(function(registrationError) {
        console.log('SW registration failed: ', registrationError);
      });
  });
}

// Analytics (placeholder)
function trackEvent(category, action, label) {
  // Placeholder for analytics tracking
  console.log('Analytics event:', category, action, label);
  
  // Example Google Analytics 4 event
  if (typeof gtag !== 'undefined') {
    gtag('event', action, {
      'event_category': category,
      'event_label': label
    });
  }
}

// Track course launches
document.addEventListener('click', function(event) {
  if (event.target.classList.contains('launch-btn')) {
    const courseTitle = event.target.closest('.course-card').querySelector('.course-title').textContent;
    trackEvent('Course', 'Launch', courseTitle);
  }
});

// Accessibility improvements
document.addEventListener('keydown', function(event) {
  // Escape key closes modals
  if (event.key === 'Escape') {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
      if (modal.style.display === 'block') {
        modal.style.display = 'none';
      }
    });
  }
  
  // Enter key on course cards launches course
  if (event.key === 'Enter' && event.target.classList.contains('course-card')) {
    const launchBtn = event.target.querySelector('.launch-btn');
    if (launchBtn) {
      launchBtn.click();
    }
  }
});

// Make course cards focusable for keyboard navigation
document.addEventListener('DOMContentLoaded', function() {
  const courseCards = document.querySelectorAll('.course-card');
  courseCards.forEach(card => {
    card.setAttribute('tabindex', '0');
    card.setAttribute('role', 'button');
    card.setAttribute('aria-label', 'Course card. Press Enter to launch course.');
  });
});