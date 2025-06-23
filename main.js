// ImpactMojo 101 - Main Application Logic
// Handles UI interactions, course rendering, filtering, and utilities

// Global variables
let filteredCourses = [...courses];
let currentBookmarkFilter = false;
let comparisonList = [];
let expandedCourse = null;

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
  initializeTheme();
  renderCourses();
  setupModalHandlers();
  setupNavigationHandlers();
  setupFilterHandlers();
});

// Theme Management
function initializeTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  if (savedTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    if (themeIcon) themeIcon.className = 'fas fa-sun';
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
    if (themeIcon) themeIcon.className = 'fas fa-moon';
  }
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const themeIcon = document.getElementById('themeIcon');
  
  if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    if (themeIcon) themeIcon.className = 'fas fa-moon';
  } else {
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
    if (themeIcon) themeIcon.className = 'fas fa-sun';
  }
}

// Course Rendering and Management
function renderCourses() {
  const container = document.getElementById('courseContainer');
  const noResults = document.getElementById('noResults');
  
  if (!container) return;
  
  let coursesToShow = filteredCourses;
  
  // Apply bookmark filter if active
  if (currentBookmarkFilter && typeof userBookmarks !== 'undefined') {
    coursesToShow = filteredCourses.filter(course => userBookmarks.includes(course.id));
  }
  
  if (coursesToShow.length === 0) {
    container.innerHTML = '';
    if (noResults) noResults.classList.remove('hidden');
    return;
  }
  
  if (noResults) noResults.classList.add('hidden');
  
  container.innerHTML = coursesToShow.map(course => `
    <div class="course-card" data-category="${course.category}" data-difficulty="${course.difficulty}" data-duration="${course.duration}">
      <div class="course-header">
        <span class="course-number">${course.number}</span>
        <button class="bookmark-btn" data-course-id="${course.id}" onclick="toggleBookmark('${course.id}')" title="Bookmark this course">
          <i class="far fa-bookmark"></i>
        </button>
      </div>
      
      <h3 class="course-title">${course.title}</h3>
      <p class="course-description">${course.description}</p>
      
      <div class="course-meta">
        <span><i class="fas fa-tag"></i> ${course.category}</span>
        <span><i class="fas fa-clock"></i> ${course.duration}</span>
        <span class="difficulty ${course.difficulty}">${capitalizeFirst(course.difficulty)}</span>
        <span><i class="fas fa-users"></i> ${course.learnerCount.toLocaleString()}</span>
        <span><i class="fas fa-star"></i> ${course.rating}</span>
      </div>
      
      <div class="course-actions">
        <div class="course-actions-left">
          <a href="${course.url}" target="_blank" rel="noopener" class="launch-btn" onclick="trackCourseClick('${course.id}')">
            Launch Course <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
        <div class="course-actions-right">
          <button class="expand-btn" onclick="expandCourse('${course.id}')" title="View details">
            <i class="fas fa-expand"></i> Details
          </button>
          <button class="compare-btn ${comparisonList.includes(course.id) ? 'active' : ''}" onclick="toggleCompare('${course.id}')" title="Add to comparison">
            <i class="fas fa-balance-scale"></i> Compare
          </button>
        </div>
      </div>
      
      <div class="course-expanded-content">
        <div class="course-prerequisites">
          <h5>Prerequisites</h5>
          <ul>
            ${course.prerequisites.map(prereq => `<li>${prereq}</li>`).join('')}
          </ul>
        </div>
        
        <div class="course-outcomes">
          <h5>Learning Outcomes</h5>
          <ul>
            ${course.outcomes.map(outcome => `<li>${outcome}</li>`).join('')}
          </ul>
        </div>
        
        <div class="course-audience">
          <h5>Target Audience</h5>
          <p>${course.audience}</p>
        </div>
      </div>
    </div>
  `).join('');
  
  // Update bookmark UI if user is logged in
  if (typeof updateBookmarkUI === 'function') {
    updateBookmarkUI();
  }
  
  updateCourseCount();
}

// Course Filtering
function filterCourses() {
  const searchTerm = document.getElementById('searchInput')?.value.toLowerCase() || '';
  const category = document.getElementById('categoryFilter')?.value || 'all';
  const difficulty = document.getElementById('difficultyFilter')?.value || 'all';
  const duration = document.getElementById('durationFilter')?.value || 'all';
  
  filteredCourses = courses.filter(course => {
    const matchesSearch = !searchTerm || 
      course.title.toLowerCase().includes(searchTerm) ||
      course.description.toLowerCase().includes(searchTerm) ||
      course.category.toLowerCase().includes(searchTerm) ||
      course.audience.toLowerCase().includes(searchTerm);
    
    const matchesCategory = category === 'all' || course.category === category;
    const matchesDifficulty = difficulty === 'all' || course.difficulty === difficulty;
    
    let matchesDuration = true;
    if (duration !== 'all') {
      const durationText = course.duration.toLowerCase();
      switch (duration) {
        case 'short':
          matchesDuration = durationText.includes('2') || durationText.includes('1');
          break;
        case 'medium':
          matchesDuration = durationText.includes('3') || durationText.includes('4');
          break;
        case 'long':
          matchesDuration = durationText.includes('5') || durationText.includes('6') || durationText.includes('+');
          break;
      }
    }
    
    return matchesSearch && matchesCategory && matchesDifficulty && matchesDuration;
  });
  
  renderCourses();
}

function clearAllFilters() {
  const searchInput = document.getElementById('searchInput');
  const categoryFilter = document.getElementById('categoryFilter');
  const difficultyFilter = document.getElementById('difficultyFilter');
  const durationFilter = document.getElementById('durationFilter');
  
  if (searchInput) searchInput.value = '';
  if (categoryFilter) categoryFilter.value = 'all';
  if (difficultyFilter) difficultyFilter.value = 'all';
  if (durationFilter) durationFilter.value = 'all';
  
  currentBookmarkFilter = false;
  filteredCourses = [...courses];
  renderCourses();
  
  showNotification('All filters cleared', 'info');
}

function filterByPath(pathType) {
  const pathMappings = {
    'data-analysis': ['Data Analysis'],
    'gender-studies': ['Gender Studies'],
    'economics': ['Economics'],
    'justice': ['Justice']
  };
  
  const categories = pathMappings[pathType] || [];
  
  if (categories.length > 0) {
    filteredCourses = courses.filter(course => categories.includes(course.category));
    
    // Update filter UI
    const categoryFilter = document.getElementById('categoryFilter');
    if (categoryFilter && categories.length === 1) {
      categoryFilter.value = categories[0];
    }
    
    renderCourses();
    
    // Scroll to courses section
    const coursesSection = document.getElementById('courses');
    if (coursesSection) {
      coursesSection.scrollIntoView({ behavior: 'smooth' });
    }
    
    showNotification(`Showing ${categories.join(', ')} courses`, 'info');
  }
}

function setBookmarkFilter(active) {
  currentBookmarkFilter = active;
  renderCourses();
}

function updateCourseCount() {
  const visibleCount = document.getElementById('visibleCount');
  const totalCount = document.getElementById('totalCount');
  
  let displayCount = filteredCourses.length;
  
  // Adjust count for bookmark filter
  if (currentBookmarkFilter && typeof userBookmarks !== 'undefined') {
    displayCount = filteredCourses.filter(course => userBookmarks.includes(course.id)).length;
  }
  
  if (visibleCount) visibleCount.textContent = displayCount;
  if (totalCount) totalCount.textContent = courses.length;
}

// Course Interaction Tracking
function trackCourseClick(courseId) {
  // Track course access for analytics
  console.log(`Course accessed: ${courseId}`);
  
  // Update user progress if logged in
  if (typeof updateUserProgress === 'function' && typeof isAuthenticated === 'function' && isAuthenticated()) {
    updateUserProgress(courseId, { lastAccessed: new Date() });
  }
}

// Event Handlers Setup
function setupModalHandlers() {
  // Close modals when clicking outside
  window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    });
  };
  
  // Handle escape key to close modals
  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
      const modals = document.querySelectorAll('.modal');
      modals.forEach(modal => {
        if (modal.style.display === 'block') {
          modal.style.display = 'none';
        }
      });
    }
  });
}

function setupNavigationHandlers() {
  // Smooth scrolling for navigation links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
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
  
  // Handle mobile menu toggle (if needed)
  const mobileMenuToggle = document.getElementById('mobileMenuToggle');
  const navLinks = document.querySelector('.nav-links');
  
  if (mobileMenuToggle && navLinks) {
    mobileMenuToggle.addEventListener('click', function() {
      navLinks.classList.toggle('active');
    });
  }
}

function setupFilterHandlers() {
  // Real-time search
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    let searchTimeout;
    searchInput.addEventListener('input', function() {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(filterCourses, 300); // Debounce search
    });
  }
  
  // Filter change handlers
  const filterSelects = ['categoryFilter', 'difficultyFilter', 'durationFilter'];
  filterSelects.forEach(filterId => {
    const filterElement = document.getElementById(filterId);
    if (filterElement) {
      filterElement.addEventListener('change', filterCourses);
    }
  });
}

// Utility Functions
function showNotification(message, type = 'info') {
  // Remove existing notifications
  const existingNotifications = document.querySelectorAll('.notification');
  existingNotifications.forEach(notification => notification.remove());
  
  // Create new notification
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.textContent = message;
  
  document.body.appendChild(notification);
  
  // Auto-remove after 4 seconds
  setTimeout(() => {
    if (notification.parentNode) {
      notification.remove();
    }
  }, 4000);
  
  // Add click to dismiss
  notification.addEventListener('click', () => {
    notification.remove();
  });
}

function capitalizeFirst(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function formatNumber(num) {
  return num.toLocaleString();
}

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

// Search Functionality Enhancement
function performAdvancedSearch(query) {
  const searchTerms = query.toLowerCase().split(' ').filter(term => term.length > 0);
  
  return courses.filter(course => {
    const searchableText = [
      course.title,
      course.description,
      course.category,
      course.audience,
      ...course.prerequisites,
      ...course.outcomes
    ].join(' ').toLowerCase();
    
    return searchTerms.every(term => searchableText.includes(term));
  });
}

// Course Statistics
function getCourseStatistics() {
  const stats = {
    totalCourses: courses.length,
    categories: {},
    difficulties: {},
    averageRating: 0,
    totalLearners: 0
  };
  
  courses.forEach(course => {
    // Category count
    stats.categories[course.category] = (stats.categories[course.category] || 0) + 1;
    
    // Difficulty count
    stats.difficulties[course.difficulty] = (stats.difficulties[course.difficulty] || 0) + 1;
    
    // Total learners
    stats.totalLearners += course.learnerCount;
  });
  
  // Average rating
  stats.averageRating = courses.reduce((sum, course) => sum + course.rating, 0) / courses.length;
  
  return stats;
}

// Export functions for use in other modules
window.ImpactMojoApp = {
  renderCourses,
  filterCourses,
  clearAllFilters,
  filterByPath,
  setBookmarkFilter,
  showNotification,
  getCourseStatistics,
  performAdvancedSearch
};

// Initialize course count on page load
document.addEventListener('DOMContentLoaded', function() {
  updateCourseCount();
});

// Handle window resize for responsive behavior
window.addEventListener('resize', debounce(() => {
  // Handle any responsive adjustments here
  console.log('Window resized');
}, 250));

// Print functionality
function printCourseList() {
  const printWindow = window.open('', '_blank');
  const courseHTML = filteredCourses.map(course => `
    <div style="margin-bottom: 20px; padding: 15px; border: 1px solid #ddd;">
      <h3>${course.title}</h3>
      <p><strong>Category:</strong> ${course.category}</p>
      <p><strong>Duration:</strong> ${course.duration}</p>
      <p><strong>Difficulty:</strong> ${capitalizeFirst(course.difficulty)}</p>
      <p>${course.description}</p>
      <p><strong>URL:</strong> ${course.url}</p>
    </div>
  `).join('');
  
  printWindow.document.write(`
    <html>
      <head>
        <title>ImpactMojo 101 Course List</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 20px; }
          h1 { color: #2563eb; }
          h3 { color: #333; margin-bottom: 10px; }
          p { margin: 5px 0; }
        </style>
      </head>
      <body>
        <h1>ImpactMojo 101 Knowledge Series</h1>
        <p>Generated on: ${new Date().toLocaleDateString()}</p>
        <p>Total Courses: ${filteredCourses.length}</p>
        <hr>
        ${courseHTML}
      </body>
    </html>
  `);
  printWindow.document.close();
  printWindow.print();
}

// Keyboard shortcuts
document.addEventListener('keydown', function(event) {
  // Ctrl/Cmd + K to focus search
  if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
    event.preventDefault();
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
      searchInput.focus();
    }
  }
  
  // Ctrl/Cmd + Shift + C to clear filters
  if ((event.ctrlKey || event.metaKey) && event.shiftKey && event.key === 'C') {
    event.preventDefault();
    clearAllFilters();
  }
});

// Performance monitoring
console.log(`ImpactMojo 101 loaded with ${courses.length} courses`);
console.log('Available categories:', [...new Set(courses.map(c => c.category))]);
console.log('Course statistics:', getCourseStatistics());

// Course Expansion Functionality
function expandCourse(courseId) {
  const course = courses.find(c => c.id === courseId);
  if (!course) return;
  
  // Close any existing expanded course
  if (expandedCourse) {
    closeExpandedCourse();
  }
  
  const courseCard = document.querySelector(`[data-course-id="${courseId}"]`).closest('.course-card');
  if (courseCard) {
    courseCard.classList.add('expanded');
    expandedCourse = courseId;
    
    // Add close button if not exists
    if (!courseCard.querySelector('.close-expanded')) {
      const closeBtn = document.createElement('button');
      closeBtn.className = 'close-expanded';
      closeBtn.innerHTML = '<i class="fas fa-times"></i>';
      closeBtn.onclick = closeExpandedCourse;
      closeBtn.title = 'Close details';
      courseCard.appendChild(closeBtn);
    }
    
    // Prevent body scroll
    document.body.style.overflow = 'hidden';
  }
}

function closeExpandedCourse() {
  if (expandedCourse) {
    const courseCard = document.querySelector(`[data-course-id="${expandedCourse}"]`).closest('.course-card');
    if (courseCard) {
      courseCard.classList.remove('expanded');
      const closeBtn = courseCard.querySelector('.close-expanded');
      if (closeBtn) {
        closeBtn.remove();
      }
    }
    expandedCourse = null;
    document.body.style.overflow = '';
  }
}

// Course Comparison Functionality
function toggleCompare(courseId) {
  const course = courses.find(c => c.id === courseId);
  if (!course) return;
  
  const index = comparisonList.indexOf(courseId);
  
  if (index > -1) {
    // Remove from comparison
    comparisonList.splice(index, 1);
    showNotification(`${course.title} removed from comparison`, 'info');
  } else {
    // Add to comparison (max 4 courses)
    if (comparisonList.length >= 4) {
      showNotification('Maximum 4 courses can be compared at once', 'warning');
      return;
    }
    comparisonList.push(courseId);
    showNotification(`${course.title} added to comparison`, 'success');
  }
  
  updateComparisonUI();
  updateComparisonPanel();
}

function updateComparisonUI() {
  // Update compare button states
  const compareButtons = document.querySelectorAll('.compare-btn');
  compareButtons.forEach(btn => {
    const courseCard = btn.closest('.course-card');
    const courseId = courseCard.querySelector('.bookmark-btn').dataset.courseId;
    
    if (comparisonList.includes(courseId)) {
      btn.classList.add('active');
      btn.innerHTML = '<i class="fas fa-check"></i> Added';
    } else {
      btn.classList.remove('active');
      btn.innerHTML = '<i class="fas fa-balance-scale"></i> Compare';
    }
  });
}

function updateComparisonPanel() {
  const panel = document.getElementById('comparisonPanel');
  const grid = document.getElementById('comparisonGrid');
  const count = document.getElementById('comparisonCount');
  
  if (!panel || !grid || !count) return;
  
  count.textContent = `${comparisonList.length} course${comparisonList.length !== 1 ? 's' : ''} selected`;
  
  if (comparisonList.length === 0) {
    panel.classList.remove('active');
    grid.innerHTML = '<div class="comparison-empty"><p>Select courses to compare by clicking the "Compare" button on course cards.</p></div>';
    return;
  }
  
  panel.classList.add('active');
  
  const comparisonCourses = comparisonList.map(id => courses.find(c => c.id === id));
  
  grid.innerHTML = comparisonCourses.map(course => `
    <div class="comparison-item">
      <h5>${course.title}</h5>
      <div class="meta">
        <span>${course.category}</span>
        <span>${course.difficulty}</span>
        <span>${course.duration}</span>
        <span>★ ${course.rating}</span>
      </div>
      <div class="description">${course.description}</div>
      <div class="actions">
        <a href="${course.url}" target="_blank" rel="noopener" class="launch-btn" style="font-size: 0.8rem; padding: 0.25rem 0.5rem;">
          Launch <i class="fas fa-external-link-alt"></i>
        </a>
        <button class="remove-comparison" onclick="toggleCompare('${course.id}')" title="Remove from comparison">
          <i class="fas fa-times"></i>
        </button>
      </div>
    </div>
  `).join('');
}

function clearComparison() {
  comparisonList = [];
  updateComparisonUI();
  updateComparisonPanel();
  showNotification('Comparison cleared', 'info');
}

// Close expanded course when clicking outside
document.addEventListener('click', function(event) {
  if (expandedCourse && event.target.closest('.course-card.expanded') === null && !event.target.closest('.close-expanded')) {
    closeExpandedCourse();
  }
});

// Handle escape key
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    if (expandedCourse) {
      closeExpandedCourse();
    }
  }
});