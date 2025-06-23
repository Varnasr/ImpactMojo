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
/* ===== ADD THIS TO YOUR EXISTING main.js FILE ===== */

// Enhanced Labs and Comparison Functionality
let selectedCourses = [];

// Generate Labs Content - preserving your original 9 labs
function generateLabsContent() {
  const labsContainer = document.getElementById('labsContainer');
  if (!labsContainer) return;
  
  const labsHTML = `
    <div class="labs-grid">
      <!-- TOC Workbench -->
      <div class="lab-card">
        <h3><i class="fas fa-tools"></i> TOC Workbench</h3>
        <p>Create, visualize, and share your intervention logic models.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://toc-workbench.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- MEL Toolkit -->
      <div class="lab-card">
        <h3><i class="fas fa-chart-line"></i> MEL Toolkit</h3>
        <p>Monitoring, evaluation, and learning framework builder.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://mel-toolkit.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Budget Calculator -->
      <div class="lab-card">
        <h3><i class="fas fa-calculator"></i> Development Budget Calculator</h3>
        <p>Project budget planning and cost estimation tool.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://budget-calculator.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Stakeholder Mapping -->
      <div class="lab-card">
        <h3><i class="fas fa-users"></i> Stakeholder Mapping Tool</h3>
        <p>Visualize and analyze stakeholder relationships and influence.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://stakeholder-mapper.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Community Engagement Lab -->
      <div class="lab-card">
        <h3><i class="fas fa-hands-helping"></i> Community Engagement Lab</h3>
        <p>Design participatory processes and community consultation frameworks.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://community-engagement-lab.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Survey Design Lab -->
      <div class="lab-card">
        <h3><i class="fas fa-clipboard-list"></i> Survey Design Lab</h3>
        <p>Interactive tool for designing surveys and questionnaires for development research.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://survey-design-lab.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Data Visualization Lab -->
      <div class="lab-card">
        <h3><i class="fas fa-chart-bar"></i> Data Visualization Lab</h3>
        <p>Create compelling data visualizations and infographics for development data.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://data-viz-lab.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Impact Measurement -->
      <div class="lab-card">
        <h3><i class="fas fa-bullseye"></i> Impact Measurement Lab</h3>
        <p>Design and track impact metrics for development interventions.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://impact-measurement-lab.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Policy Analysis Tool -->
      <div class="lab-card">
        <h3><i class="fas fa-gavel"></i> Policy Analysis Tool</h3>
        <p>Framework for analyzing and comparing development policies.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://policy-analysis-tool.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
    </div>
  `;
  labsContainer.innerHTML = labsHTML;
}

// Enhanced Course Comparison Functionality
function toggleCourseComparison(courseId) {
  const index = selectedCourses.indexOf(courseId);
  if (index > -1) {
    selectedCourses.splice(index, 1);
  } else {
    if (selectedCourses.length < 3) {
      selectedCourses.push(courseId);
    } else {
      alert('You can compare up to 3 courses at a time.');
      return;
    }
  }
  updateComparisonUI();
  updateCourseCardStates();
}

function updateComparisonUI() {
  // Update comparison panel
  const comparisonCount = document.getElementById('comparisonCount');
  const comparisonPanel = document.getElementById('comparisonPanel');
  const enhancedBtn = document.querySelector('.enhanced-comparison-btn');
  
  if (comparisonCount) {
    comparisonCount.textContent = `${selectedCourses.length} courses selected`;
  }
  
  if (comparisonPanel) {
    if (selectedCourses.length > 0) {
      comparisonPanel.style.display = 'block';
    } else {
      comparisonPanel.style.display = 'none';
    }
  }
  
  if (enhancedBtn) {
    enhancedBtn.disabled = selectedCourses.length < 2;
  }
  
  // Update FAB button
  updateFABButton();
}

function updateCourseCardStates() {
  // Update all course compare buttons to show selected state
  selectedCourses.forEach(courseId => {
    const btn = document.querySelector(`[data-course-id="${courseId}"] .course-compare-btn`);
    if (btn) {
      btn.classList.add('selected');
      btn.innerHTML = '<i class="fas fa-check"></i> Selected';
    }
  });
  
  // Update unselected buttons
  const allBtns = document.querySelectorAll('.course-compare-btn');
  allBtns.forEach(btn => {
    const courseCard = btn.closest('[data-course-id]');
    if (courseCard) {
      const courseId = courseCard.getAttribute('data-course-id');
      if (!selectedCourses.includes(courseId)) {
        btn.classList.remove('selected');
        btn.innerHTML = '<i class="fas fa-balance-scale"></i> Compare';
      }
    }
  });
}

function updateFABButton() {
  let fabBtn = document.querySelector('.fab-btn.compare');
  
  if (selectedCourses.length > 0) {
    if (!fabBtn) {
      // Create FAB if it doesn't exist
      let fabContainer = document.querySelector('.fab-container');
      if (!fabContainer) {
        fabContainer = document.createElement('div');
        fabContainer.className = 'fab-container';
        document.body.appendChild(fabContainer);
      }
      
      fabBtn = document.createElement('button');
      fabBtn.className = 'fab-btn compare';
      fabBtn.onclick = showEnhancedComparisonModal;
      fabContainer.appendChild(fabBtn);
    }
    
    fabBtn.innerHTML = `<i class="fas fa-balance-scale"></i> Compare (${selectedCourses.length})`;
    fabBtn.classList.remove('hidden');
    fabBtn.style.display = 'flex';
  } else if (fabBtn) {
    fabBtn.classList.add('hidden');
    fabBtn.style.display = 'none';
  }
}

function calculateContentDepth(course) {
  let score = 0;
  
  // Duration scoring (out of 3)
  if (course.duration && (course.duration.includes('5-6') || course.duration.includes('6+'))) score += 3;
  else if (course.duration && course.duration.includes('4-5')) score += 2;
  else score += 1;
  
  // Prerequisites scoring (out of 2)
  if (course.prerequisites && course.prerequisites.length > 2) score += 2;
  else if (course.prerequisites && course.prerequisites.length > 0 && !course.prerequisites.includes('None - foundational course')) score += 1;
  
  // Learning outcomes complexity (out of 3)
  if (course.outcomes && course.outcomes.length >= 4) score += 3;
  else if (course.outcomes && course.outcomes.length >= 3) score += 2;
  else score += 1;
  
  // Difficulty scoring (out of 2)
  if (course.difficulty === 'advanced') score += 2;
  else if (course.difficulty === 'intermediate') score += 1;
  
  return Math.min(score, 10);
}

function analyzeContentOverlap(courses) {
  const overlaps = [];
  
  for (let i = 0; i < courses.length; i++) {
    for (let j = i + 1; j < courses.length; j++) {
      const course1 = courses[i];
      const course2 = courses[j];
      
      // Check category overlap
      const categoryMatch = course1.category === course2.category;
      
      // Check audience overlap
      const audienceWords1 = (course1.audience || '').toLowerCase().split(/[,\s]+/);
      const audienceWords2 = (course2.audience || '').toLowerCase().split(/[,\s]+/);
      const audienceOverlap = audienceWords1.filter(word => 
        audienceWords2.includes(word) && word.length > 3
      ).length;
      
      let overlapScore = 0;
      if (categoryMatch) overlapScore += 3;
      overlapScore += Math.min(audienceOverlap, 2);
      
      if (overlapScore > 2) {
        overlaps.push({
          courses: [course1.title, course2.title],
          score: overlapScore,
          details: {
            category: categoryMatch,
            audienceWords: audienceOverlap
          }
        });
      }
    }
  }
  
  return overlaps;
}

function generateLearningPath(courses) {
  return [...courses].sort((a, b) => {
    const difficultyOrder = { 'beginner': 1, 'intermediate': 2, 'advanced': 3 };
    const aDiff = difficultyOrder[a.difficulty] || 2;
    const bDiff = difficultyOrder[b.difficulty] || 2;
    
    if (aDiff !== bDiff) return aDiff - bDiff;
    
    // If same difficulty, prioritize foundational courses
    const aFoundational = (a.prerequisites || []).includes('None - foundational course');
    const bFoundational = (b.prerequisites || []).includes('None - foundational course');
    
    if (aFoundational && !bFoundational) return -1;
    if (!aFoundational && bFoundational) return 1;
    
    return 0;
  });
}

function showEnhancedComparisonModal() {
  if (selectedCourses.length < 2) {
    alert('Please select at least 2 courses to compare.');
    return;
  }
  
  const modal = document.getElementById('enhancedComparisonModal');
  const comparisonTable = document.getElementById('comparisonTable');
  
  if (!modal || !comparisonTable) {
    alert('Comparison modal not found. Please refresh the page.');
    return;
  }
  
  // Get courses from the global courses array
  const coursesSource = window.courses || courses || [];
  const coursesToCompare = selectedCourses.map(id => 
    coursesSource.find(course => course.id === id)
  ).filter(Boolean);
  
  if (coursesToCompare.length === 0) {
    alert('Course data not found. Please ensure course-data.js is loaded.');
    return;
  }
  
  const contentDepths = coursesToCompare.map(calculateContentDepth);
  const overlaps = analyzeContentOverlap(coursesToCompare);
  const suggestedPath = generateLearningPath(coursesToCompare);
  
  const tableHTML = `
    <div class="comparison-container">
      <!-- Basic Information Comparison -->
      <div class="comparison-section">
        <h4><i class="fas fa-info-circle"></i> Course Overview</h4>
        <div class="comparison-table-grid">
          <div class="comparison-header">
            <div class="feature-column">Feature</div>
            ${coursesToCompare.map(course => `
              <div class="course-column">${course.title}</div>
            `).join('')}
          </div>
          <div class="comparison-row">
            <div class="feature-cell">Difficulty</div>
            ${coursesToCompare.map(course => `
              <div class="course-cell">
                <span class="difficulty ${course.difficulty || 'intermediate'}">${course.difficulty || 'intermediate'}</span>
              </div>
            `).join('')}
          </div>
          <div class="comparison-row">
            <div class="feature-cell">Duration</div>
            ${coursesToCompare.map(course => `
              <div class="course-cell">${course.duration || 'Not specified'}</div>
            `).join('')}
          </div>
          <div class="comparison-row">
            <div class="feature-cell">Category</div>
            ${coursesToCompare.map(course => `
              <div class="course-cell">${course.category || 'General'}</div>
            `).join('')}
          </div>
          <div class="comparison-row">
            <div class="feature-cell">Content Depth</div>
            ${coursesToCompare.map((course, index) => `
              <div class="course-cell">
                <div class="depth-bar-mini" style="width: ${contentDepths[index] * 10}%; background: linear-gradient(90deg, #10b981, #f59e0b, #3b82f6);"></div>
                ${contentDepths[index]}/10
              </div>
            `).join('')}
          </div>
          <div class="comparison-row">
            <div class="feature-cell">Learner Count</div>
            ${coursesToCompare.map(course => `
              <div class="course-cell">${course.learnerCount ? course.learnerCount.toLocaleString() : 'N/A'} learners</div>
            `).join('')}
          </div>
          <div class="comparison-row">
            <div class="feature-cell">Rating</div>
            ${coursesToCompare.map(course => `
              <div class="course-cell">${course.rating ? '★ ' + course.rating : 'Not rated'}</div>
            `).join('')}
          </div>
        </div>
      </div>

      <!-- Prerequisites Analysis -->
      ${coursesToCompare.some(c => c.prerequisites && c.prerequisites.length > 0) ? `
      <div class="comparison-section">
        <h4><i class="fas fa-list-check"></i> Prerequisites Analysis</h4>
        <div class="comparison-table-grid">
          <div class="comparison-header">
            <div class="feature-column">Prerequisites</div>
            ${coursesToCompare.map(course => `
              <div class="course-column">${course.title}</div>
            `).join('')}
          </div>
          <div class="comparison-row">
            <div class="feature-cell">Requirements</div>
            ${coursesToCompare.map(course => `
              <div class="course-cell">
                ${course.prerequisites && course.prerequisites.length > 0 ? 
    course.prerequisites.map(prereq => `<div class="prereq-item">${prereq}</div>`).join('') : 
    'None specified'}
              </div>
            `).join('')}
          </div>
        </div>
      </div>
      ` : ''}

      <!-- Learning Outcomes Comparison -->
      ${coursesToCompare.some(c => c.outcomes && c.outcomes.length > 0) ? `
      <div class="comparison-section">
        <h4><i class="fas fa-graduation-cap"></i> Learning Outcomes</h4>
        <div class="comparison-table-grid">
          <div class="comparison-header">
            <div class="feature-column">What You'll Learn</div>
            ${coursesToCompare.map(course => `
              <div class="course-column">${course.title}</div>
            `).join('')}
          </div>
          <div class="comparison-row">
            <div class="feature-cell">Key Outcomes</div>
            ${coursesToCompare.map(course => `
              <div class="course-cell">
                ${course.outcomes && course.outcomes.length > 0 ? 
    course.outcomes.map(outcome => `<div class="outcome-item">• ${outcome}</div>`).join('') : 
    'Not specified'}
              </div>
            `).join('')}
          </div>
        </div>
      </div>
      ` : ''}

      <!-- Target Audience Comparison -->
      ${coursesToCompare.some(c => c.audience) ? `
      <div class="comparison-section">
        <h4><i class="fas fa-users"></i> Target Audience</h4>
        <div class="comparison-table-grid">
          <div class="comparison-header">
            <div class="feature-column">Best For</div>
            ${coursesToCompare.map(course => `
              <div class="course-column">${course.title}</div>
            `).join('')}
          </div>
          <div class="comparison-row">
            <div class="feature-cell">Audience</div>
            ${coursesToCompare.map(course => `
              <div class="course-cell">${course.audience || 'General audience'}</div>
            `).join('')}
          </div>
        </div>
      </div>
      ` : ''}

      <!-- Content Overlap Analysis -->
      ${overlaps.length > 0 ? `
        <div class="comparison-section">
          <h4><i class="fas fa-intersection"></i> Content Overlap Analysis</h4>
          <div class="overlap-analysis">
            ${overlaps.map(overlap => `
              <div class="overlap-item">
                <strong>${overlap.courses.join(' & ')}</strong>
                <div class="overlap-score">Overlap Score: ${overlap.score}/5</div>
                <div class="overlap-details">
                  ${overlap.details.category ? '<span class="overlap-tag">Same Category</span>' : ''}
                  ${overlap.details.audienceWords > 0 ? `<span class="overlap-tag">Shared Audience (${overlap.details.audienceWords} matches)</span>` : ''}
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      ` : ''}

      <!-- Suggested Learning Path -->
      <div class="comparison-section">
        <h4><i class="fas fa-route"></i> Suggested Learning Path</h4>
        <div class="learning-path">
          ${suggestedPath.map((course, index) => `
            <div class="path-step">
              <div class="step-number">${index + 1}</div>
              <div class="step-content">
                <h5>${course.title}</h5>
                <div class="step-rationale">
                  ${index === 0 ? 'Start here - ' : ''}
                  ${course.difficulty || 'intermediate'} level, ${course.duration || 'duration not specified'}
                  ${course.prerequisites && course.prerequisites.includes('None - foundational course') ? ' (Foundational)' : ''}
                </div>
              </div>
            </div>
            ${index < suggestedPath.length - 1 ? '<div class="path-arrow">↓</div>' : ''}
          `).join('')}
        </div>
      </div>
    </div>
  `;
  
  comparisonTable.innerHTML = tableHTML;
  modal.classList.remove('hidden');
}

function closeEnhancedComparisonModal() {
  const modal = document.getElementById('enhancedComparisonModal');
  if (modal) {
    modal.classList.add('hidden');
  }
}

function clearComparison() {
  selectedCourses = [];
  updateComparisonUI();
  updateCourseCardStates();
  closeEnhancedComparisonModal();
}

function exportComparison() {
  if (selectedCourses.length === 0) {
    alert('No courses selected for comparison.');
    return;
  }
  
  // Simple export functionality - can be enhanced later
  const coursesSource = window.courses || courses || [];
  const coursesToExport = selectedCourses.map(id => 
    coursesSource.find(course => course.id === id)
  ).filter(Boolean);
  
  const exportData = {
    exportDate: new Date().toISOString(),
    courses: coursesToExport.map(course => ({
      title: course.title,
      category: course.category,
      difficulty: course.difficulty,
      duration: course.duration,
      learnerCount: course.learnerCount,
      rating: course.rating
    }))
  };
  
  const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'impactmojo-course-comparison.json';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// Enhanced course rendering to include compare buttons
function enhanceCourseCards() {
  // Wait for courses to be rendered, then add compare buttons
  setTimeout(() => {
    const courseCards = document.querySelectorAll('.course-card');
    courseCards.forEach(card => {
      if (!card.querySelector('.course-compare-btn')) {
        const courseId = card.getAttribute('data-course-id');
        if (courseId) {
          const actionsDiv = card.querySelector('.course-actions');
          if (actionsDiv && !actionsDiv.classList.contains('course-actions-enhanced')) {
            actionsDiv.classList.add('course-actions-enhanced');
            
            const compareBtn = document.createElement('button');
            compareBtn.className = 'course-compare-btn';
            compareBtn.innerHTML = '<i class="fas fa-balance-scale"></i> Compare';
            compareBtn.onclick = (e) => {
              e.preventDefault();
              e.stopPropagation();
              toggleCourseComparison(courseId);
            };
            
            actionsDiv.appendChild(compareBtn);
          }
        }
      }
    });
    
    // Update button states
    updateCourseCardStates();
  }, 100);
}

// Initialize enhanced features when DOM loads
document.addEventListener('DOMContentLoaded', function() {
  generateLabsContent();
  
  // Enhanced course cards after a delay to ensure courses are loaded
  setTimeout(() => {
    enhanceCourseCards();
  }, 500);
  
  // Re-enhance when courses are filtered
  const originalFilterCourses = window.filterCourses;
  if (originalFilterCourses) {
    window.filterCourses = function() {
      originalFilterCourses.apply(this, arguments);
      setTimeout(enhanceCourseCards, 100);
    };
  }
});

// Add event listener for modal clicks
document.addEventListener('click', function(e) {
  if (e.target.classList.contains('modal') && e.target.id === 'enhancedComparisonModal') {
    closeEnhancedComparisonModal();
  }
});

// Make functions globally available
window.generateLabsContent = generateLabsContent;
window.toggleCourseComparison = toggleCourseComparison;
window.showEnhancedComparisonModal = showEnhancedComparisonModal;
window.closeEnhancedComparisonModal = closeEnhancedComparisonModal;
window.clearComparison = clearComparison;
window.exportComparison = exportComparison;