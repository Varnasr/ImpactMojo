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
      
      <div class="course-actions course-actions-enhanced">
  <div class="course-actions-left">
    <a href="${course.url}" target="_blank" rel="noopener" class="launch-btn" onclick="trackCourseClick('${course.id}')">
      Launch Course <i class="fas fa-external-link-alt"></i>
    </a>
  </div>
  <div class="course-actions-right">
    <button class="expand-btn" onclick="expandCourse('${course.id}')" title="View details">
      <i class="fas fa-expand"></i> Details
    </button>
    <button class="course-compare-btn compare-btn ${comparisonList.includes(course.id) ? 'active' : ''}" onclick="toggleCourseComparison('${course.id}')" title="Add to comparison">
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
// 🔥 DIRECT FIXES - ADD THIS TO THE END OF YOUR main.js FILE

// Fix 1: Ensure the comparison modal works
function showEnhancedComparisonModal() {
  console.log('🔥 Modal called with selected courses:', selectedCourses);
  
  // Create modal if it doesn't exist
  let modal = document.getElementById('enhancedComparisonModal');
  if (!modal) {
    console.log('❌ Modal not found, creating it...');
    createEnhancedModal();
    modal = document.getElementById('enhancedComparisonModal');
  }
  
  if (selectedCourses.length < 2) {
    alert('Please select at least 2 courses to compare.');
    return;
  }
  
  // Get the courses data
  const coursesToCompare = selectedCourses.map(id => 
    courses.find(course => course.id === id)
  ).filter(Boolean);
  
  if (coursesToCompare.length === 0) {
    alert('Course data not found. Please refresh the page.');
    return;
  }
  
  console.log('📊 Comparing courses:', coursesToCompare.map(c => c.title));
  
  // Generate comparison content
  const comparisonTable = document.getElementById('comparisonTable');
  if (comparisonTable) {
    comparisonTable.innerHTML = generateSimpleComparison(coursesToCompare);
  }
  
  // Show modal
  modal.classList.remove('hidden');
  modal.style.display = 'block';
}

// Fix 2: Create the modal if it doesn't exist
function createEnhancedModal() {
  const modalHTML = `
    <div id="enhancedComparisonModal" class="modal enhanced-modal hidden">
      <div class="modal-content comparison-modal-content">
        <div class="modal-header">
          <h2><i class="fas fa-balance-scale"></i> Course Comparison</h2>
          <button class="close-modal" onclick="closeEnhancedComparisonModal()">
            <i class="fas fa-times"></i>
          </button>
        </div>
        <div class="modal-body">
          <div id="comparisonTable">
            <!-- Dynamic comparison content will be inserted here -->
          </div>
        </div>
        <div class="modal-footer">
          <button class="clear-comparison-btn" onclick="clearComparison()">
            <i class="fas fa-times"></i> Clear All
          </button>
        </div>
      </div>
    </div>
  `;
  
  document.body.insertAdjacentHTML('beforeend', modalHTML);
  console.log('✅ Enhanced modal created');
}

// Fix 3: Generate simple comparison content
function generateSimpleComparison(coursesToCompare) {
  return `
    <div class="comparison-container">
      <div class="comparison-section">
        <h4><i class="fas fa-info-circle"></i> Course Overview</h4>
        <div class="simple-comparison-grid">
          ${coursesToCompare.map(course => `
            <div class="course-comparison-card">
              <h5>${course.title}</h5>
              <div class="course-details">
                <p><strong>Category:</strong> ${course.category}</p>
                <p><strong>Difficulty:</strong> <span class="difficulty ${course.difficulty}">${course.difficulty}</span></p>
                <p><strong>Duration:</strong> ${course.duration}</p>
                <p><strong>Rating:</strong> ⭐ ${course.rating}</p>
                <p><strong>Learners:</strong> ${course.learnerCount?.toLocaleString() || 'N/A'}</p>
              </div>
              <div class="course-description">
                <p><strong>Description:</strong></p>
                <p>${course.description}</p>
              </div>
              ${course.outcomes ? `
                <div class="course-outcomes">
                  <p><strong>What you'll learn:</strong></p>
<ul>
${course.outcomes.slice(0, 3).map(outcome => `<li>${outcome}</li>`).join('')}
</ul>
</div>
` : ''}
              <div class="course-actions">
                <a href="${course.url}" target="_blank" rel="noopener" class="launch-btn-modal">
                  <i class="fas fa-external-link-alt"></i> Launch Course
                </a>
              </div>
            </div>
          `).join('')}
</div>
</div>
</div>
`;
}

// Fix 4: Ensure clearComparison works
function clearComparison() {
  selectedCourses = [];
  comparisonList = []; // Clear both arrays
  updateComparisonUI();
  updateCourseCardStates();
  closeEnhancedComparisonModal();
  showNotification('Comparison cleared', 'info');
}

// Fix 5: Close modal function
function closeEnhancedComparisonModal() {
  const modal = document.getElementById('enhancedComparisonModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.style.display = 'none';
  }
}

// Fix 6: Enhanced Lab Cards - with debugging
function enhanceLabCards() {
  console.log('🔧 Enhancing lab cards...');
  
  // Look for lab cards in the labs container
  const labsContainer = document.getElementById('labsContainer');
  if (!labsContainer) {
    console.log('❌ Labs container not found');
    return;
  }
  
  const labCards = labsContainer.querySelectorAll('.lab-card');
  console.log(`📦 Found ${labCards.length} lab cards`);
  
  if (labCards.length === 0) {
    console.log('❌ No lab cards found');
    return;
  }
  
  labCards.forEach((card, index) => {
    // Add unique ID if not present
    if (!card.getAttribute('data-lab-id')) {
      card.setAttribute('data-lab-id', `lab-${index + 1}`);
    }
    
    const labId = card.getAttribute('data-lab-id');
    const labTitle = card.querySelector('h3') ? card.querySelector('h3').textContent : `Lab ${index + 1}`;
    
    console.log(`🔧 Enhancing lab: ${labTitle} (ID: ${labId})`);
    
    // Check if already enhanced
    if (card.querySelector('.lab-enhanced-actions')) {
      console.log(`⏭️ Lab ${labId} already enhanced`);
      return;
    }
    
    // Create enhanced actions
    const enhancedActions = document.createElement('div');
    enhancedActions.className = 'lab-enhanced-actions';
    enhancedActions.innerHTML = `
<div class="lab-actions-row">
<button class="lab-bookmark-btn" data-lab-id="${labId}" onclick="toggleLabBookmark('${labId}')" title="Bookmark this lab">
<i class="far fa-bookmark"></i> Bookmark
</button>
<button class="lab-compare-btn" onclick="alert('Lab comparison feature coming soon!')" title="Compare labs">
<i class="fas fa-balance-scale"></i> Compare
</button>
<button class="lab-details-btn" onclick="showLabDetails('${labId}')" title="View details">
<i class="fas fa-info-circle"></i> Details
</button>
</div>
`;
    
    // Insert at the end of the card
    card.appendChild(enhancedActions);
    console.log(`✅ Enhanced lab: ${labTitle}`);
  });
  
  console.log('✅ Lab enhancement complete');
}

// Fix 7: Lab bookmark functionality
function toggleLabBookmark(labId) {
  console.log('🔖 Bookmarking lab:', labId);
  const btn = document.querySelector(`[data-lab-id="${labId}"] .lab-bookmark-btn`);
  if (btn) {
    const icon = btn.querySelector('i');
    if (icon.classList.contains('far')) {
      icon.className = 'fas fa-bookmark';
      btn.style.color = '#f59e0b';
      showNotification('Lab bookmarked!', 'success');
    } else {
      icon.className = 'far fa-bookmark';
      btn.style.color = '';
      showNotification('Bookmark removed', 'info');
    }
  }
}

// Fix 8: Lab details functionality
function showLabDetails(labId) {
  const labCard = document.querySelector(`[data-lab-id="${labId}"]`);
  if (!labCard) {
    console.log('❌ Lab card not found:', labId);
    return;
  }
  
  const title = labCard.querySelector('h3')?.textContent || 'Lab Details';
  const description = labCard.querySelector('p')?.textContent || 'No description available';
  const launchLink = labCard.querySelector('.lab-launch-btn')?.href || '#';
  
  // Simple alert for now - can be enhanced later
  const details = `
📋 ${title}

📝 Description:
${description}

🔗 Link: ${launchLink}

✨ Features:
• Interactive tools and simulations
• Real-world case studies  
  • Downloadable resources
  • Step-by-step guidance
  `;
  
  alert(details);
}

// Fix 9: Initialize everything properly
function initializeEnhancements() {
  console.log('🚀 Initializing enhancements...');
  
  // Add styles for lab enhancements
  addLabStyles();
  
  // Add modal styles
  addModalStyles();
  
  // Try to enhance lab cards multiple times to catch different loading states
  setTimeout(() => enhanceLabCards(), 500);
  setTimeout(() => enhanceLabCards(), 1500);
  setTimeout(() => enhanceLabCards(), 3000);
  
  console.log('✅ Enhancement initialization complete');
}

// Fix 10: Add required styles
function addLabStyles() {
  if (document.getElementById('lab-enhancement-styles')) return;
  
  const styles = document.createElement('style');
  styles.id = 'lab-enhancement-styles';
  styles.textContent = `
  .lab-enhanced-actions {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border-color);
  }
  
  .lab-actions-row {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    align-items: center;
  }
  
  .lab-bookmark-btn,
  .lab-compare-btn,
  .lab-details-btn {
    background: none;
    border: 1px solid var(--primary-color);
    color: var(--primary-color);
    padding: 0.5rem 0.75rem;
    border-radius: 0.5rem;
    cursor: pointer;
    font-size: 0.85rem;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.25rem;
  }
  
  .lab-bookmark-btn:hover,
  .lab-details-btn:hover {
    background: var(--primary-color);
    color: white;
  }
  
  .lab-compare-btn {
    border-color: var(--accent-color);
    color: var(--accent-color);
  }
  
  .lab-compare-btn:hover {
    background: var(--accent-color);
    color: white;
  }
  `;
  document.head.appendChild(styles);
}

// Fix 11: Add modal styles
function addModalStyles() {
  if (document.getElementById('enhanced-modal-styles')) return;
  
  const styles = document.createElement('style');
  styles.id = 'enhanced-modal-styles';
  styles.textContent = `
  .enhanced-modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    z-index: 1000;
    backdrop-filter: blur(4px);
  }
  
  .comparison-modal-content {
    background: var(--background);
    margin: 5% auto;
    padding: 0;
    border-radius: 1rem;
    width: 90%;
    max-width: 900px;
    max-height: 80vh;
    position: relative;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    border: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
  }
  
  .modal-header {
    padding: 1.5rem;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--surface);
    border-radius: 1rem 1rem 0 0;
  }
  
  .modal-header h2 {
    margin: 0;
    color: var(--text-primary);
    font-size: 1.5rem;
  }
  
  .close-modal {
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: var(--text-secondary);
    padding: 0.5rem;
    border-radius: 50%;
    transition: all 0.3s ease;
  }
  
  .close-modal:hover {
    background: var(--error-color);
    color: white;
  }
  
  .modal-body {
    flex: 1;
    padding: 1.5rem;
    overflow-y: auto;
    background: var(--background);
  }
  
  .modal-footer {
    padding: 1rem 1.5rem;
    border-top: 1px solid var(--border-color);
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
    background: var(--surface);
    border-radius: 0 0 1rem 1rem;
  }
  
  .clear-comparison-btn {
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 0.5rem;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;
    background: var(--error-color);
    color: white;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  
  .clear-comparison-btn:hover {
    background: #b91c1c;
  }
  
  .simple-comparison-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
  }
  
  .course-comparison-card {
    background: var(--surface);
    padding: 1.5rem;
    border-radius: 0.5rem;
    border: 1px solid var(--border-color);
  }
  
  .course-comparison-card h5 {
    color: var(--primary-color);
    margin-bottom: 1rem;
    font-size: 1.2rem;
  }
  
  .course-details p {
    margin-bottom: 0.5rem;
    color: var(--text-primary);
  }
  
  .course-description {
    margin: 1rem 0;
    padding-top: 1rem;
    border-top: 1px solid var(--border-color);
  }
  
  .course-outcomes ul {
    margin: 0.5rem 0;
    padding-left: 1.5rem;
  }
  
  .course-outcomes li {
    margin-bottom: 0.25rem;
    color: var(--text-secondary);
  }
  
  .course-actions {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border-color);
  }
  
  .launch-btn-modal {
    background: var(--primary-color);
    color: white;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 600;
    transition: all 0.3s ease;
  }
  
  .launch-btn-modal:hover {
    background: var(--secondary-color);
  }
  
  .difficulty {
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: capitalize;
  }
  
  .difficulty.beginner {
    background: var(--success-color);
    color: white;
  }
  
  .difficulty.intermediate {
    background: var(--warning-color);
    color: white;
  }
  
  .difficulty.advanced {
    background: var(--error-color);
    color: white;
  }
  `;
  document.head.appendChild(styles);
}

// Fix 12: Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  console.log('🔥 DOM ready, initializing fixes...');
  initializeEnhancements();
});

// Also try to initialize immediately in case DOM is already loaded
if (document.readyState !== 'loading') {
  console.log('🔥 DOM already loaded, initializing fixes...');
  initializeEnhancements();
}

// Fix 13: Debug selectedCourses array
console.log('🔍 Current selectedCourses:', selectedCourses);
console.log('🔍 Current comparisonList:', comparisonList);

// Override the FAB update to ensure it works
function updateFABButton() {
  let fabBtn = document.querySelector('.fab-btn.compare');
  
  console.log('🔄 Updating FAB button, selectedCourses:', selectedCourses);
  
  if (selectedCourses.length > 0) {
    if (!fabBtn) {
      // Create FAB if it doesn't exist
      let fabContainer = document.querySelector('.fab-container');
      if (!fabContainer) {
        fabContainer = document.createElement('div');
        fabContainer.className = 'fab-container';
        fabContainer.style.cssText = `
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 998;
  `;
        document.body.appendChild(fabContainer);
      }
      
      fabBtn = document.createElement('button');
      fabBtn.className = 'fab-btn compare';
      fabBtn.onclick = () => {
        console.log('🖱️ FAB button clicked!');
        showEnhancedComparisonModal();
      };
      fabBtn.style.cssText = `
  padding: 1rem 1.5rem;
  border-radius: 2rem;
  border: none;
  background: var(--accent-color);
  color: white;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  `;
      fabContainer.appendChild(fabBtn);
    }
    
    fabBtn.innerHTML = `<i class="fas fa-balance-scale"></i> Compare (${selectedCourses.length})`;
    fabBtn.style.display = 'flex';
  } else if (fabBtn) {
    fabBtn.style.display = 'none';
  }
}
// 🔥 EMERGENCY DEBUG & FIX - Replace the entire bottom section of your main.js

// Step 1: Check what's happening
console.log('🔍 DEBUG: Starting emergency fixes...');
console.log('🔍 DEBUG: selectedCourses exists?', typeof selectedCourses);
console.log('🔍 DEBUG: comparisonList exists?', typeof comparisonList);

// Step 2: Initialize arrays if they don't exist
if (typeof selectedCourses === 'undefined') {
  window.selectedCourses = [];
  console.log('✅ Created selectedCourses array');
}

if (typeof comparisonList === 'undefined') {
  window.comparisonList = [];
  console.log('✅ Created comparisonList array');
}

// Step 3: Override the toggleCourseComparison function completely
window.toggleCourseComparison = function(courseId) {
  console.log('🖱️ toggleCourseComparison called with:', courseId);
  
  const index = selectedCourses.indexOf(courseId);
  if (index > -1) {
    selectedCourses.splice(index, 1);
    console.log('➖ Removed course from comparison:', courseId);
  } else {
    if (selectedCourses.length >= 4) {
      alert('Maximum 4 courses can be compared at once');
      return;
    }
    selectedCourses.push(courseId);
    console.log('➕ Added course to comparison:', courseId);
  }
  
  console.log('📋 Current selectedCourses:', selectedCourses);
  
  // Update UI
  updateComparisonUI();
  updateCourseCardStates();
  createFloatingButton();
  
  // Show notification
  const message = index > -1 ? 'Removed from comparison' : 'Added to comparison';
  showNotification(message, 'info');
};

// Step 4: Create floating button function
window.createFloatingButton = function() {
  console.log('🔘 Creating floating button, count:', selectedCourses.length);
  
  // Remove existing button
  const existingBtn = document.querySelector('.emergency-fab-btn');
  if (existingBtn) {
    existingBtn.remove();
  }
  
  if (selectedCourses.length === 0) {
    console.log('❌ No courses selected, hiding button');
    return;
  }
  
  // Create new button
  const fabBtn = document.createElement('button');
  fabBtn.className = 'emergency-fab-btn';
  fabBtn.innerHTML = `<i class="fas fa-balance-scale"></i> Compare (${selectedCourses.length})`;
  fabBtn.style.cssText = `
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #f59e0b;
  color: white;
  border: none;
  padding: 15px 20px;
  border-radius: 25px;
  cursor: pointer;
  font-weight: bold;
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
  z-index: 999;
  display: flex;
  align-items: center;
  gap: 10px;
  transition: all 0.3s ease;
  `;
  
  // Add click handler
  fabBtn.onclick = function() {
    console.log('🖱️ Emergency FAB clicked!');
    emergencyShowComparison();
  };
  
  // Add hover effect
  fabBtn.onmouseover = function() {
    this.style.transform = 'scale(1.1)';
    this.style.background = '#d97706';
  };
  
  fabBtn.onmouseout = function() {
    this.style.transform = 'scale(1)';
    this.style.background = '#f59e0b';
  };
  
  document.body.appendChild(fabBtn);
  console.log('✅ Emergency FAB button created and added');
};

// Step 5: Emergency comparison modal
window.emergencyShowComparison = function() {
  console.log('🚨 Emergency comparison modal called');
  console.log('📋 Comparing courses:', selectedCourses);
  
  if (selectedCourses.length < 2) {
    alert('Please select at least 2 courses to compare.');
    return;
  }
  
  // Get course data
  const coursesToCompare = selectedCourses.map(id => {
    const course = courses.find(c => c.id === id);
    console.log(`🔍 Found course ${id}:`, course ? course.title : 'NOT FOUND');
    return course;
  }).filter(Boolean);
  
  if (coursesToCompare.length === 0) {
    alert('Course data not found. Please refresh the page.');
    return;
  }
  
  // Create simple comparison content
  let comparisonHTML = `
  <div style="max-height: 70vh; overflow-y: auto;">
  <h3 style="margin-bottom: 20px; color: #2563eb;">📊 Course Comparison</h3>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
  `;
  
  coursesToCompare.forEach(course => {
    comparisonHTML += `
  <div style="background: #f8fafc; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0;">
  <h4 style="color: #2563eb; margin-bottom: 15px;">${course.title}</h4>
  <div style="margin-bottom: 10px;">
  <strong>Category:</strong> ${course.category}
  </div>
  <div style="margin-bottom: 10px;">
  <strong>Difficulty:</strong> 
  <span style="padding: 2px 8px; border-radius: 12px; font-size: 12px; color: white; background: ${
            course.difficulty === 'beginner' ? '#059669' : 
            course.difficulty === 'intermediate' ? '#d97706' : '#dc2626'
          };">${course.difficulty}</span>
  </div>
  <div style="margin-bottom: 10px;">
  <strong>Duration:</strong> ${course.duration}
  </div>
  <div style="margin-bottom: 10px;">
  <strong>Rating:</strong> ⭐ ${course.rating}
  </div>
  <div style="margin-bottom: 15px;">
  <strong>Learners:</strong> ${course.learnerCount ? course.learnerCount.toLocaleString() : 'N/A'}
  </div>
  <div style="margin-bottom: 15px; border-top: 1px solid #e2e8f0; padding-top: 15px;">
  <strong>Description:</strong><br>
  <div style="margin-top: 5px; color: #64748b; line-height: 1.5;">${course.description}</div>
  </div>
  <a href="${course.url}" target="_blank" rel="noopener" style="background: #2563eb; color: white; padding: 10px 15px; border-radius: 5px; text-decoration: none; display: inline-flex; align-items: center; gap: 5px; font-weight: 600;">
  <i class="fas fa-external-link-alt"></i> Launch Course
  </a>
  </div>
  `;
  });
  
  comparisonHTML += `
  </div>
  <div style="margin-top: 20px; text-align: center;">
  <button onclick="emergencyClearComparison()" style="background: #dc2626; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-weight: 600;">
  <i class="fas fa-times"></i> Clear Comparison
  </button>
  </div>
  </div>
  `;
  
  // Create and show modal
  createEmergencyModal(comparisonHTML);
};

// Step 6: Create emergency modal
function createEmergencyModal(content) {
  // Remove existing modal
  const existingModal = document.getElementById('emergencyModal');
  if (existingModal) {
    existingModal.remove();
  }
  
  // Create modal
  const modal = document.createElement('div');
  modal.id = 'emergencyModal';
  modal.style.cssText = `
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
  `;
  
  const modalContent = document.createElement('div');
  modalContent.style.cssText = `
  background: white;
  padding: 30px;
  border-radius: 15px;
  width: 90%;
  max-width: 1000px;
  max-height: 80vh;
  overflow-y: auto;
  position: relative;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  `;
  
  // Add close button
  const closeBtn = document.createElement('button');
  closeBtn.innerHTML = '&times;';
  closeBtn.style.cssText = `
  position: absolute;
  top: 15px;
  right: 20px;
  background: none;
  border: none;
  font-size: 30px;
  cursor: pointer;
  color: #64748b;
  `;
  closeBtn.onclick = () => modal.remove();
  
  modalContent.innerHTML = content;
  modalContent.appendChild(closeBtn);
  modal.appendChild(modalContent);
  
  // Close on background click
  modal.onclick = (e) => {
    if (e.target === modal) {
      modal.remove();
    }
  };
  
  document.body.appendChild(modal);
  console.log('✅ Emergency modal created and shown');
}

// Step 7: Clear comparison function
window.emergencyClearComparison = function() {
  selectedCourses.length = 0;
  comparisonList.length = 0;
  
  // Remove FAB button
  const fabBtn = document.querySelector('.emergency-fab-btn');
  if (fabBtn) {
    fabBtn.remove();
  }
  
  // Remove modal
  const modal = document.getElementById('emergencyModal');
  if (modal) {
    modal.remove();
  }
  
  // Update course card states
  updateCourseCardStates();
  
  showNotification('Comparison cleared', 'info');
  console.log('✅ Comparison cleared');
};

// Step 8: Enhance lab cards with simple approach
window.enhanceLabCardsEmergency = function() {
  console.log('🔧 Emergency lab enhancement starting...');
  
  // Wait for labs to load
  setTimeout(() => {
    const labCards = document.querySelectorAll('.lab-card');
    console.log(`📦 Found ${labCards.length} lab cards`);
    
    if (labCards.length === 0) {
      console.log('❌ No lab cards found, trying again...');
      // Try again with different selectors
      const alternativeLabCards = document.querySelectorAll('[class*="lab"]');
      console.log(`📦 Found ${alternativeLabCards.length} elements with "lab" in class`);
    }
    
    labCards.forEach((card, index) => {
      if (card.querySelector('.emergency-lab-actions')) {
        return; // Already enhanced
      }
      
      const labId = `lab-${index + 1}`;
      const title = card.querySelector('h3')?.textContent || `Lab ${index + 1}`;
      
      console.log(`🔧 Enhancing lab: ${title}`);
      
      // Create action buttons
      const actionsDiv = document.createElement('div');
      actionsDiv.className = 'emergency-lab-actions';
      actionsDiv.style.cssText = `
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px solid #e2e8f0;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  `;
      
      // Bookmark button
      const bookmarkBtn = document.createElement('button');
      bookmarkBtn.innerHTML = '<i class="far fa-bookmark"></i> Bookmark';
      bookmarkBtn.style.cssText = `
  background: none;
  border: 1px solid #f59e0b;
  color: #f59e0b;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s ease;
  `;
      bookmarkBtn.onclick = function() {
        const icon = this.querySelector('i');
        if (icon.classList.contains('far')) {
          icon.className = 'fas fa-bookmark';
          this.style.background = '#f59e0b';
          this.style.color = 'white';
          showNotification('Lab bookmarked!', 'success');
        } else {
          icon.className = 'far fa-bookmark';
          this.style.background = 'none';
          this.style.color = '#f59e0b';
          showNotification('Bookmark removed', 'info');
        }
      };
      
      // Details button
      const detailsBtn = document.createElement('button');
      detailsBtn.innerHTML = '<i class="fas fa-info-circle"></i> Details';
      detailsBtn.style.cssText = `
  background: none;
  border: 1px solid #2563eb;
  color: #2563eb;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s ease;
  `;
      detailsBtn.onclick = function() {
        const description = card.querySelector('p')?.textContent || 'No description available';
        const launchUrl = card.querySelector('a[href]')?.href || '#';
        
        alert(`📋 ${title}\n\n📝 ${description}\n\n🔗 ${launchUrl}\n\n✨ Features:\n• Interactive tools\n• Real-world examples\n• Downloadable resources`);
      };
      
      actionsDiv.appendChild(bookmarkBtn);
      actionsDiv.appendChild(detailsBtn);
      card.appendChild(actionsDiv);
      
      console.log(`✅ Enhanced lab: ${title}`);
    });
    
    console.log('✅ Emergency lab enhancement complete');
  }, 1000);
};

// Step 9: Initialize everything
document.addEventListener('DOMContentLoaded', function() {
  console.log('🚨 Emergency initialization started');
  
  // Initialize lab enhancements
  enhanceLabCardsEmergency();
  
  // Try again after delay in case content loads dynamically
  setTimeout(enhanceLabCardsEmergency, 3000);
  setTimeout(enhanceLabCardsEmergency, 5000);
});

// Step 10: Test everything
console.log('🔥 Emergency fixes loaded!');
console.log('🧪 Testing selectedCourses:', selectedCourses);
console.log('🧪 Testing functions available:', {
  toggleCourseComparison: typeof toggleCourseComparison,
  createFloatingButton: typeof createFloatingButton,
  emergencyShowComparison: typeof emergencyShowComparison
});

// Force creation of floating button if courses are already selected
if (selectedCourses && selectedCourses.length > 0) {
  console.log('🔄 Courses already selected, creating button...');
  createFloatingButton();
}
// 🔧 CONFLICT FIX - Add this to the END of your main.js file (after the emergency fixes)

console.log('🔧 Starting conflict resolution...');

// Step 1: Debug what's happening when compare is clicked
window.debugCompareClick = function(courseId) {
  console.log('🖱️ Compare clicked for course:', courseId);
  console.log('📋 Before - selectedCourses:', [...selectedCourses]);
  console.log('📋 Before - comparisonList:', [...comparisonList]);
  
  // Call the emergency function
  toggleCourseComparison(courseId);
  
  console.log('📋 After - selectedCourses:', [...selectedCourses]);
  console.log('📋 After - comparisonList:', [...comparisonList]);
};

// Step 2: Override ALL compare functions to use our emergency one
window.toggleCompare = window.toggleCourseComparison;

// Step 3: Fix the floating button issue
window.createFloatingButton = function() {
  console.log('🔘 Creating floating button, selectedCourses count:', selectedCourses.length);
  
  // Remove ALL existing floating buttons
  const existingBtns = document.querySelectorAll('.emergency-fab-btn, .fab-btn.compare, .compare-fab');
  existingBtns.forEach(btn => {
    console.log('🗑️ Removing existing button:', btn.className);
    btn.remove();
  });
  
  if (selectedCourses.length === 0) {
    console.log('❌ No courses selected, no button needed');
    return;
  }
  
  console.log('✅ Creating new floating button...');
  
  // Create ONE floating button
  const fabBtn = document.createElement('button');
  fabBtn.className = 'emergency-fab-btn';
  fabBtn.innerHTML = `<i class="fas fa-balance-scale"></i> Compare Selected (${selectedCourses.length})`;
  
  // Position and style
  fabBtn.style.cssText = `
  position: fixed !important;
  bottom: 20px !important;
  right: 20px !important;
  background: #f59e0b !important;
  color: white !important;
  border: none !important;
  padding: 15px 25px !important;
  border-radius: 30px !important;
  cursor: pointer !important;
  font-weight: bold !important;
  font-size: 16px !important;
  box-shadow: 0 6px 20px rgba(0,0,0,0.4) !important;
  z-index: 9999 !important;
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  transition: all 0.3s ease !important;
  font-family: inherit !important;
  `;
  
  // Click handler with debugging
  fabBtn.onclick = function(e) {
    e.preventDefault();
    e.stopPropagation();
    console.log('🖱️ FLOATING BUTTON CLICKED!');
    console.log('📋 Current selectedCourses:', selectedCourses);
    
    if (selectedCourses.length < 2) {
      alert('Please select at least 2 courses to compare.');
      return;
    }
    
    emergencyShowComparison();
  };
  
  // Hover effects
  fabBtn.onmouseover = function() {
    this.style.transform = 'scale(1.05)';
    this.style.background = '#d97706';
    this.style.boxShadow = '0 8px 25px rgba(0,0,0,0.5)';
  };
  
  fabBtn.onmouseout = function() {
    this.style.transform = 'scale(1)';
    this.style.background = '#f59e0b';
    this.style.boxShadow = '0 6px 20px rgba(0,0,0,0.4)';
  };
  
  document.body.appendChild(fabBtn);
  console.log('✅ Floating button created and positioned');
  
  // Test if button is visible
  const rect = fabBtn.getBoundingClientRect();
  console.log('📍 Button position:', rect);
};

// Step 4: Fix the updateCourseCardStates function
window.updateCourseCardStates = function() {
  console.log('🔄 Updating course card states...');
  
  // Update selected course buttons
  selectedCourses.forEach(courseId => {
    const compareBtn = document.querySelector(`[data-course-id="${courseId}"] .course-compare-btn, [data-course-id="${courseId}"] .compare-btn`);
    if (compareBtn) {
      compareBtn.classList.add('selected', 'active');
      compareBtn.innerHTML = '<i class="fas fa-check"></i> Selected';
      compareBtn.style.background = '#059669';
      compareBtn.style.color = 'white';
      compareBtn.style.borderColor = '#059669';
      console.log('✅ Updated button for course:', courseId);
    }
  });
  
  // Reset unselected course buttons
  const allCompareBtns = document.querySelectorAll('.course-compare-btn, .compare-btn');
  allCompareBtns.forEach(btn => {
    const courseCard = btn.closest('[data-course-id]');
    if (courseCard) {
      const courseId = courseCard.getAttribute('data-course-id');
      if (!selectedCourses.includes(courseId)) {
        btn.classList.remove('selected', 'active');
        btn.innerHTML = '<i class="fas fa-balance-scale"></i> Compare';
        btn.style.background = '';
        btn.style.color = '';
        btn.style.borderColor = '';
      }
    }
  });
  
  console.log('🔄 Card states updated');
};

// Step 5: Enhanced emergencyShowComparison with better debugging
window.emergencyShowComparison = function() {
  console.log('🚨 EMERGENCY COMPARISON MODAL STARTING');
  console.log('📋 Selected courses to compare:', selectedCourses);
  
  if (selectedCourses.length < 2) {
    alert('Please select at least 2 courses to compare.');
    return;
  }
  
  // Get course data with detailed logging
  const coursesToCompare = [];
  selectedCourses.forEach(id => {
    const course = courses.find(c => c.id === id);
    if (course) {
      coursesToCompare.push(course);
      console.log(`✅ Found course: ${course.title}`);
    } else {
      console.log(`❌ Course not found: ${id}`);
    }
  });
  
  if (coursesToCompare.length === 0) {
    alert('Course data not found. Please refresh the page.');
    return;
  }
  
  console.log('📊 Creating comparison for:', coursesToCompare.map(c => c.title));
  
  // Enhanced comparison content
  let comparisonHTML = `
  <div style="max-height: 75vh; overflow-y: auto; padding: 10px;">
  <div style="text-align: center; margin-bottom: 25px;">
  <h2 style="color: #2563eb; margin: 0; font-size: 28px;">
  <i class="fas fa-balance-scale"></i> Course Comparison
  </h2>
  <p style="color: #64748b; margin: 10px 0 0 0;">Compare ${coursesToCompare.length} selected courses</p>
  </div>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 25px;">
  `;
  
  coursesToCompare.forEach((course, index) => {
    comparisonHTML += `
  <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); padding: 25px; border-radius: 15px; border: 2px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
  <div style="background: ${index === 0 ? '#2563eb' : index === 1 ? '#059669' : '#dc2626'}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
  <h3 style="margin: 0; font-size: 20px; font-weight: bold;">${course.title}</h3>
  </div>
  
  <div style="space-y: 12px;">
  <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #e2e8f0;">
  <strong style="color: #374151;">Category:</strong> 
  <span style="color: #6b7280;">${course.category}</span>
  </div>
  
  <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #e2e8f0;">
  <strong style="color: #374151;">Difficulty:</strong> 
  <span style="padding: 4px 12px; border-radius: 15px; font-size: 13px; font-weight: bold; color: white; background: ${
              course.difficulty === 'beginner' ? '#059669' : 
              course.difficulty === 'intermediate' ? '#d97706' : '#dc2626'
            };">${course.difficulty.toUpperCase()}</span>
  </div>
  
  <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #e2e8f0;">
  <strong style="color: #374151;">Duration:</strong> 
  <span style="color: #6b7280;">${course.duration}</span>
  </div>
  
  <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #e2e8f0;">
  <strong style="color: #374151;">Rating:</strong> 
  <span style="color: #f59e0b; font-weight: bold;">⭐ ${course.rating}/5</span>
  </div>
  
  <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #e2e8f0;">
  <strong style="color: #374151;">Learners:</strong> 
  <span style="color: #6b7280;">${course.learnerCount ? course.learnerCount.toLocaleString() : 'N/A'}</span>
  </div>
  </div>
  
  <div style="margin: 20px 0; padding: 15px; background: white; border-radius: 8px; border-left: 4px solid ${index === 0 ? '#2563eb' : index === 1 ? '#059669' : '#dc2626'};">
  <strong style="color: #374151; display: block; margin-bottom: 8px;">Description:</strong>
  <p style="margin: 0; color: #6b7280; line-height: 1.6; font-size: 14px;">${course.description}</p>
  </div>
  
  <div style="text-align: center; margin-top: 20px;">
  <a href="${course.url}" target="_blank" rel="noopener" style="background: linear-gradient(135deg, #2563eb, #1d4ed8); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; font-weight: bold; box-shadow: 0 3px 10px rgba(37, 99, 235, 0.3); transition: all 0.3s ease;">
  <i class="fas fa-external-link-alt"></i> Launch Course
  </a>
  </div>
  </div>
  `;
  });
  
  comparisonHTML += `
  </div>
  <div style="margin-top: 30px; text-align: center; padding: 20px; background: #f8fafc; border-radius: 10px;">
  <button onclick="emergencyClearComparison()" style="background: #dc2626; color: white; padding: 12px 30px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 16px; box-shadow: 0 3px 10px rgba(220, 38, 38, 0.3); transition: all 0.3s ease;">
  <i class="fas fa-times"></i> Clear All & Close
  </button>
  </div>
  </div>
  `;
  
  // Create and show enhanced modal
  createEnhancedEmergencyModal(comparisonHTML);
  console.log('✅ Enhanced comparison modal created');
};

// Step 6: Enhanced modal creation
function createEnhancedEmergencyModal(content) {
  // Remove existing modal
  const existingModal = document.getElementById('emergencyModal');
  if (existingModal) {
    existingModal.remove();
  }
  
  // Create modal backdrop
  const modal = document.createElement('div');
  modal.id = 'emergencyModal';
  modal.style.cssText = `
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
  background: rgba(0, 0, 0, 0.7) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  z-index: 10000 !important;
  backdrop-filter: blur(5px) !important;
  animation: fadeIn 0.3s ease !important;
  `;
  
  // Create modal content
  const modalContent = document.createElement('div');
  modalContent.style.cssText = `
  background: white !important;
  padding: 0 !important;
  border-radius: 20px !important;
  width: 95% !important;
  max-width: 1200px !important;
  max-height: 90vh !important;
  overflow: hidden !important;
  position: relative !important;
  box-shadow: 0 25px 80px rgba(0, 0, 0, 0.4) !important;
  animation: slideUp 0.3s ease !important;
  `;
  
  // Add close button
  const closeBtn = document.createElement('button');
  closeBtn.innerHTML = '&times;';
  closeBtn.style.cssText = `
  position: absolute !important;
  top: 20px !important;
  right: 25px !important;
  background: none !important;
  border: none !important;
  font-size: 35px !important;
  cursor: pointer !important;
  color: #64748b !important;
  z-index: 10001 !important;
  border-radius: 50% !important;
  width: 45px !important;
  height: 45px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: all 0.3s ease !important;
  `;
  closeBtn.onclick = () => {
    modal.style.animation = 'fadeOut 0.3s ease';
    setTimeout(() => modal.remove(), 300);
  };
  closeBtn.onmouseover = () => {
    closeBtn.style.background = '#dc2626';
    closeBtn.style.color = 'white';
  };
  closeBtn.onmouseout = () => {
    closeBtn.style.background = 'none';
    closeBtn.style.color = '#64748b';
  };
  
  modalContent.innerHTML = content;
  modalContent.appendChild(closeBtn);
  modal.appendChild(modalContent);
  
  // Close on backdrop click
  modal.onclick = (e) => {
    if (e.target === modal) {
      modal.style.animation = 'fadeOut 0.3s ease';
      setTimeout(() => modal.remove(), 300);
    }
  };
  
  // Add animations
  const style = document.createElement('style');
  style.textContent = `
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  @keyframes fadeOut {
    from { opacity: 1; }
    to { opacity: 0; }
  }
  @keyframes slideUp {
    from { transform: translateY(30px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }
  `;
  document.head.appendChild(style);
  
  document.body.appendChild(modal);
  console.log('✅ Enhanced emergency modal displayed');
}

// Step 7: Initialize conflict resolution
console.log('🔧 Conflict resolution loaded!');
console.log('🎯 All functions ready for testing');

// Step 8: Force update if courses already selected
if (selectedCourses && selectedCourses.length > 0) {
  console.log('🔄 Updating existing selection...');
  createFloatingButton();
  updateCourseCardStates();
}
// 🧹 FINAL CLEANUP - Add this to the END of your main.js file

console.log('🧹 Starting final cleanup...');

// Step 1: Remove all existing compare functions and replace with ONE unified function
window.toggleCourseComparison = function(courseId) {
  console.log('🎯 UNIFIED toggleCourseComparison called:', courseId);
  
  const index = selectedCourses.indexOf(courseId);
  if (index > -1) {
    selectedCourses.splice(index, 1);
    console.log('➖ Removed:', courseId);
  } else {
    if (selectedCourses.length >= 4) {
      alert('Maximum 4 courses can be compared at once');
      return;
    }
    selectedCourses.push(courseId);
    console.log('➕ Added:', courseId);
  }
  
  console.log('📋 Final selectedCourses:', selectedCourses);
  
  // Update everything
  unifiedUpdateComparisonUI();
  unifiedUpdateFAB();
  
  showNotification(index > -1 ? 'Removed from comparison' : 'Added to comparison', 'info');
};

// Step 2: Unified comparison UI update
window.unifiedUpdateComparisonUI = function() {
  console.log('🔄 Unified UI update...');
  
  // Update ALL compare buttons on course cards
  const allCompareBtns = document.querySelectorAll('.course-compare-btn, .compare-btn');
  console.log(`🔍 Found ${allCompareBtns.length} compare buttons to update`);
  
  allCompareBtns.forEach(btn => {
    const courseCard = btn.closest('[data-course-id]');
    if (!courseCard) return;
    
    const courseId = courseCard.getAttribute('data-course-id');
    const isSelected = selectedCourses.includes(courseId);
    
    // Update button appearance
    if (isSelected) {
      btn.classList.add('selected', 'active');
      btn.innerHTML = '<i class="fas fa-check"></i> Selected';
      btn.style.background = '#059669';
      btn.style.color = 'white';
      btn.style.borderColor = '#059669';
    } else {
      btn.classList.remove('selected', 'active');
      btn.innerHTML = '<i class="fas fa-balance-scale"></i> Compare';
      btn.style.background = '';
      btn.style.color = '';
      btn.style.borderColor = '';
    }
  });
  
  console.log('✅ Comparison UI updated');
};

// Step 3: Unified FAB button management
window.unifiedUpdateFAB = function() {
  console.log('🔘 Unified FAB update, count:', selectedCourses.length);
  
  // Remove ALL existing floating buttons to prevent duplicates
  const existingFABs = document.querySelectorAll('.emergency-fab-btn, .fab-btn.compare, .compare-fab, [class*="fab"]');
  existingFABs.forEach(fab => {
    if (fab.textContent.includes('Compare')) {
      console.log('🗑️ Removing duplicate FAB:', fab.className);
      fab.remove();
    }
  });
  
  if (selectedCourses.length === 0) {
    console.log('❌ No courses selected');
    return;
  }
  
  // Create ONE clean floating button
  const unifiedFAB = document.createElement('button');
  unifiedFAB.className = 'unified-fab-btn';
  unifiedFAB.innerHTML = `<i class="fas fa-balance-scale"></i> Compare (${selectedCourses.length})`;
  
  // Clean styling
  unifiedFAB.style.cssText = `
  position: fixed !important;
  bottom: 20px !important;
  right: 20px !important;
  background: #f59e0b !important;
  color: white !important;
  border: none !important;
  padding: 15px 25px !important;
  border-radius: 30px !important;
  cursor: pointer !important;
  font-weight: bold !important;
  font-size: 16px !important;
  box-shadow: 0 6px 20px rgba(245, 158, 11, 0.4) !important;
  z-index: 9999 !important;
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  transition: all 0.3s ease !important;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
  `;
  
  // Click handler
  unifiedFAB.onclick = function(e) {
    e.preventDefault();
    e.stopPropagation();
    console.log('🖱️ UNIFIED FAB CLICKED!');
    unifiedShowComparison();
  };
  
  // Hover effects
  unifiedFAB.onmouseover = () => {
    unifiedFAB.style.transform = 'scale(1.05)';
    unifiedFAB.style.background = '#d97706';
  };
  unifiedFAB.onmouseout = () => {
    unifiedFAB.style.transform = 'scale(1)';
    unifiedFAB.style.background = '#f59e0b';
  };
  
  document.body.appendChild(unifiedFAB);
  console.log('✅ Unified FAB created');
};

// Step 4: Unified comparison modal
window.unifiedShowComparison = function() {
  console.log('🚨 Unified comparison modal');
  
  if (selectedCourses.length < 2) {
    alert('Please select at least 2 courses to compare.');
    return;
  }
  
  const coursesToCompare = selectedCourses.map(id => 
    courses.find(c => c.id === id)
  ).filter(Boolean);
  
  if (coursesToCompare.length === 0) {
    alert('Course data not found. Please refresh the page.');
    return;
  }
  
  // Create clean comparison HTML
  const comparisonHTML = `
  <div style="padding: 20px; max-height: 75vh; overflow-y: auto;">
  <div style="text-align: center; margin-bottom: 30px;">
  <h2 style="color: #2563eb; margin: 0; font-size: 2rem; font-weight: bold;">
  📊 Course Comparison
  </h2>
  <p style="color: #64748b; margin: 10px 0;">Comparing ${coursesToCompare.length} selected courses</p>
  </div>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 25px;">
  ${coursesToCompare.map((course, index) => `
          <div style="background: white; border: 2px solid #e5e7eb; border-radius: 15px; padding: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
            <div style="background: ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
              <h3 style="margin: 0; font-size: 1.25rem; font-weight: bold;">${course.title}</h3>
            </div>
            
            <div style="space-y: 15px;">
              <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f3f4f6;">
                <span style="font-weight: 600; color: #374151;">Category:</span>
                <span style="color: #6b7280;">${course.category}</span>
              </div>
              
              <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f3f4f6;">
                <span style="font-weight: 600; color: #374151;">Difficulty:</span>
                <span style="padding: 4px 12px; border-radius: 12px; font-size: 0.8rem; font-weight: bold; color: white; background: ${
    course.difficulty === 'beginner' ? '#059669' : 
    course.difficulty === 'intermediate' ? '#d97706' : '#dc2626'
    };">${course.difficulty.toUpperCase()}</span>
              </div>
              
              <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f3f4f6;">
                <span style="font-weight: 600; color: #374151;">Duration:</span>
                <span style="color: #6b7280;">${course.duration}</span>
              </div>
              
              <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f3f4f6;">
                <span style="font-weight: 600; color: #374151;">Rating:</span>
                <span style="color: #f59e0b; font-weight: bold;">⭐ ${course.rating}/5</span>
              </div>
              
              <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f3f4f6;">
                <span style="font-weight: 600; color: #374151;">Learners:</span>
                <span style="color: #6b7280;">${course.learnerCount ? course.learnerCount.toLocaleString() : 'N/A'}</span>
              </div>
            </div>
            
            <div style="margin: 20px 0; padding: 15px; background: #f8fafc; border-radius: 8px; border-left: 4px solid ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'};">
              <strong style="color: #374151; display: block; margin-bottom: 8px;">Description:</strong>
              <p style="margin: 0; color: #6b7280; line-height: 1.5;">${course.description}</p>
            </div>
            
            <div style="text-align: center;">
              <a href="${course.url}" target="_blank" rel="noopener" style="background: linear-gradient(135deg, #2563eb, #1d4ed8); color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; font-weight: bold; box-shadow: 0 3px 10px rgba(37, 99, 235, 0.3);">
                <i class="fas fa-external-link-alt"></i> Launch Course
              </a>
            </div>
          </div>
        `).join('')}
  </div>
  
  <div style="margin-top: 30px; text-align: center; padding: 20px; background: #f8fafc; border-radius: 10px;">
  <button onclick="unifiedClearComparison()" style="background: #dc2626; color: white; padding: 12px 30px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 16px; box-shadow: 0 3px 10px rgba(220, 38, 38, 0.3);">
  <i class="fas fa-times"></i> Clear All & Close
  </button>
  </div>
  </div>
  `;
  
  unifiedCreateModal(comparisonHTML);
};

// Step 5: Unified modal creation
function unifiedCreateModal(content) {
  // Remove any existing modals
  const existingModals = document.querySelectorAll('#unifiedModal, #emergencyModal, [id*="Modal"]');
  existingModals.forEach(modal => {
    if (modal.id.includes('comparison') || modal.id.includes('emergency') || modal.id.includes('unified')) {
      modal.remove();
    }
  });
  
  const modal = document.createElement('div');
  modal.id = 'unifiedModal';
  modal.style.cssText = `
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
  background: rgba(0, 0, 0, 0.75) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  z-index: 10000 !important;
  backdrop-filter: blur(4px) !important;
  `;
  
  const modalContent = document.createElement('div');
  modalContent.style.cssText = `
  background: white !important;
  border-radius: 20px !important;
  width: 95% !important;
  max-width: 1200px !important;
  max-height: 90vh !important;
  overflow: hidden !important;
  position: relative !important;
  box-shadow: 0 25px 80px rgba(0, 0, 0, 0.5) !important;
  `;
  
  const closeBtn = document.createElement('button');
  closeBtn.innerHTML = '×';
  closeBtn.style.cssText = `
  position: absolute !important;
  top: 15px !important;
  right: 20px !important;
  background: none !important;
  border: none !important;
  font-size: 30px !important;
  cursor: pointer !important;
  color: #9ca3af !important;
  z-index: 10001 !important;
  width: 40px !important;
  height: 40px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 50% !important;
  `;
  closeBtn.onclick = () => modal.remove();
  closeBtn.onmouseover = () => {
    closeBtn.style.background = '#dc2626';
    closeBtn.style.color = 'white';
  };
  closeBtn.onmouseout = () => {
    closeBtn.style.background = 'none';
    closeBtn.style.color = '#9ca3af';
  };
  
  modalContent.innerHTML = content;
  modalContent.appendChild(closeBtn);
  modal.appendChild(modalContent);
  
  modal.onclick = (e) => {
    if (e.target === modal) modal.remove();
  };
  
  document.body.appendChild(modal);
  console.log('✅ Unified modal created');
}

// Step 6: Unified clear function
window.unifiedClearComparison = function() {
  selectedCourses.length = 0;
  
  // Remove modal
  const modal = document.getElementById('unifiedModal');
  if (modal) modal.remove();
  
  // Remove FAB
  const fab = document.querySelector('.unified-fab-btn');
  if (fab) fab.remove();
  
  // Update UI
  unifiedUpdateComparisonUI();
  
  showNotification('Comparison cleared!', 'success');
  console.log('✅ Unified clear complete');
};

// Step 7: Override ALL existing functions to prevent conflicts
window.toggleCompare = window.toggleCourseComparison;
window.updateComparisonUI = window.unifiedUpdateComparisonUI;
window.updateFABButton = window.unifiedUpdateFAB;
window.createFloatingButton = window.unifiedUpdateFAB;
window.emergencyShowComparison = window.unifiedShowComparison;
window.showEnhancedComparisonModal = window.unifiedShowComparison;

// Step 8: Clean initialization
console.log('🧹 Final cleanup complete!');
console.log('🎯 Unified comparison system ready');

// Force update if needed
if (selectedCourses && selectedCourses.length > 0) {
  unifiedUpdateComparisonUI();
  unifiedUpdateFAB();
}