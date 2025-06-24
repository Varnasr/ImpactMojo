// Complete ImpactMojo Main JavaScript File
// This file handles all the functionality for courses, labs, and user interactions

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
    container.innerHTML = '<div class="no-results">No courses found. Try adjusting your search terms or filters.</div>';
    return;
  }
  
  console.log(`📚 Displaying ${filteredCourses.length} courses`);
  
  // Generate course cards
  const courseCards = filteredCourses.map(course => createCourseCard(course)).join('');
  container.innerHTML = courseCards;
  
  // Update course count
  updateCourseCount();
}

function createCourseCard(course) {
  const isBookmarked = userBookmarks.includes(course.id);
  const isSelected = selectedCourses.includes(course.id);
  
  return `
    <div class="course-card" data-course-id="${course.id}">
      <!-- Course Number Badge (Blue for Theory/Reading) -->
      <div class="course-number" title="Course ${course.number} - Theory & Reading">
        ${course.number}
      </div>
      
      <!-- Course Header -->
      <div class="course-header">
        <div class="course-icon">
          <i class="${course.icon}"></i>
        </div>
        <div class="course-title-section">
          <h3 class="course-title">${course.title}</h3>
          <div class="course-meta">
            <span class="meta-tag category">${course.category}</span>
            <span class="meta-tag difficulty ${course.difficulty}">${course.difficulty}</span>
            <span class="meta-tag duration">${course.duration}</span>
          </div>
        </div>
      </div>
      
      <!-- Course Description -->
      <div class="course-description">
        <p>${course.description}</p>
      </div>
      
      <!-- Course Stats -->
      <div class="course-stats">
        <span><i class="fas fa-star"></i> ${course.rating}/5</span>
        <span><i class="fas fa-users"></i> ${course.learnerCount.toLocaleString()}</span>
      </div>
      
      <!-- Course Actions -->
      <div class="course-actions">
        <div class="course-actions-left">
          <a href="${course.url}" target="_blank" rel="noopener" class="launch-btn">
            <i class="fas fa-book-open"></i> Launch Course
          </a>
        </div>
        <div class="course-actions-right">
          <button class="bookmark-btn ${isBookmarked ? 'bookmarked' : ''}" 
                  onclick="toggleBookmark('${course.id}')" 
                  title="${isBookmarked ? 'Remove bookmark' : 'Bookmark course'}">
            <i class="${isBookmarked ? 'fas' : 'far'} fa-bookmark"></i>
          </button>
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
      
      <!-- Course Details (Hidden by default) -->
      <div class="course-details" id="details-${course.id}" style="display: none;">
        <div class="details-section">
          <h4><i class="fas fa-list-ul"></i> Prerequisites</h4>
          <ul>
            ${course.prerequisites.map(prereq => `<li>${prereq}</li>`).join('')}
          </ul>
        </div>
        
        <div class="details-section">
          <h4><i class="fas fa-target"></i> Learning Outcomes</h4>
          <ul>
            ${course.outcomes.map(outcome => `<li>${outcome}</li>`).join('')}
          </ul>
        </div>
        
        <div class="details-section">
          <h4><i class="fas fa-users"></i> Target Audience</h4>
          <p>${course.audience}</p>
        </div>
      </div>
    </div>
  `;
}

// ===== LAB DISPLAY FUNCTIONS =====
function displayLabs() {
  const container = document.getElementById('labsContainer');
  
  if (!container) {
    console.error('❌ Labs container not found');
    return;
  }
  
  if (!labs || labs.length === 0) {
    console.error('❌ No labs data available');
    container.innerHTML = '<div class="error">Unable to load labs. Please refresh the page.</div>';
    return;
  }
  
  console.log(`🧪 Displaying ${labs.length} labs`);
  
  // Generate lab cards
  const labCards = labs.map(lab => createLabCard(lab)).join('');
  container.innerHTML = labCards;
}

function createLabCard(lab) {
  const isBookmarked = userLabBookmarks.includes(lab.id);
  
  return `
    <div class="lab-card" data-lab-id="${lab.id}">
      <!-- Live Status Indicator (Green with Pulsing Animation) -->
      <div class="lab-status-indicator">
        <div class="live-badge">
          <i class="fas fa-circle"></i> LIVE
        </div>
      </div>
      
      <!-- Lab Header -->
      <div class="lab-header">
        <div class="lab-icon">
          <i class="${lab.icon}"></i>
        </div>
        <div class="lab-title-section">
          <h3 class="lab-title">${lab.title}</h3>
          <div class="lab-meta">
            <span class="lab-category-tag">${lab.category}</span>
          </div>
        </div>
      </div>
      
      <!-- Lab Description -->
      <div class="lab-description">
        <p>${lab.description}</p>
      </div>
      
      <!-- Lab Actions -->
      <div class="lab-actions">
        <div class="lab-actions-left">
          <a href="${lab.url}" target="_blank" rel="noopener" class="lab-launch-btn">
            <i class="fas fa-external-link-alt"></i> Launch Lab
          </a>
        </div>
        <div class="lab-actions-right">
          <button class="lab-bookmark-btn ${isBookmarked ? 'bookmarked' : ''}" 
                  onclick="toggleLabBookmark('${lab.id}')" 
                  title="${isBookmarked ? 'Remove bookmark' : 'Bookmark lab'}">
            <i class="${isBookmarked ? 'fas' : 'far'} fa-bookmark"></i>
          </button>
        </div>
      </div>
    </div>
  `;
}

// ===== COURSE INTERACTION FUNCTIONS =====
function toggleCourseDetails(courseId) {
  const card = document.querySelector(`[data-course-id="${courseId}"]`);
  const detailsElement = document.getElementById(`details-${courseId}`);
  const expandBtn = card ? card.querySelector('.expand-btn i') : null;
  
  if (!card || !detailsElement) return;
  
  if (detailsElement.style.display === 'none' || !detailsElement.style.display) {
    // Expand
    detailsElement.style.display = 'block';
    if (expandBtn) expandBtn.style.transform = 'rotate(180deg)';
  } else {
    // Collapse
    detailsElement.style.display = 'none';
    if (expandBtn) expandBtn.style.transform = 'rotate(0deg)';
  }
}

function toggleBookmark(courseId) {
  const index = userBookmarks.indexOf(courseId);
  
  if (index > -1) {
    userBookmarks.splice(index, 1);
    showNotification('Bookmark removed', 'info');
  } else {
    userBookmarks.push(courseId);
    showNotification('Course bookmarked!', 'success');
  }
  
  // Save to localStorage
  localStorage.setItem('userBookmarks', JSON.stringify(userBookmarks));
  
  // Update UI
  updateBookmarkUI(courseId);
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

function toggleLabBookmark(labId) {
  const index = userLabBookmarks.indexOf(labId);
  
  if (index > -1) {
    userLabBookmarks.splice(index, 1);
    showNotification('Lab bookmark removed', 'info');
  } else {
    userLabBookmarks.push(labId);
    showNotification('Lab bookmarked!', 'success');
  }
  
  // Save to localStorage
  localStorage.setItem('userLabBookmarks', JSON.stringify(userLabBookmarks));
  
  // Update UI
  updateLabBookmarkUI(labId);
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

// ===== SEARCH AND FILTER FUNCTIONS =====
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
  const visibleElement = document.getElementById('visibleCount');
  const totalElement = document.getElementById('totalCount');
  
  if (visibleElement && totalElement) {
    visibleElement.textContent = filteredCourses.length;
    totalElement.textContent = allCourses.length;
  }
}

// ===== COMPARISON FUNCTIONS =====
function showComparison() {
  if (selectedCourses.length < 2) {
    showNotification('Please select at least 2 courses to compare', 'warning');
    return;
  }
  
  const selectedData = selectedCourses.map(id => 
    allCourses.find(course => course.id === id)
  ).filter(course => course);
  
  const comparisonContent = createComparisonTable(selectedData);
  showComparisonModal('Course Comparison', comparisonContent);
}

function createComparisonTable(courses) {
  return `
    <div class="comparison-table-container">
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
            ${courses.map(course => `<td><span class="meta-tag difficulty ${course.difficulty}">${course.difficulty}</span></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Duration</strong></td>
            ${courses.map(course => `<td>${course.duration}</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Rating</strong></td>
            ${courses.map(course => `<td>⭐ ${course.rating}/5</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Learners</strong></td>
            ${courses.map(course => `<td>${course.learnerCount.toLocaleString()}</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Prerequisites</strong></td>
            ${courses.map(course => `<td>${course.prerequisites.join(', ')}</td>`).join('')}
          </tr>
        </tbody>
      </table>
    </div>
  `;
}

function showComparisonModal(title, content) {
  // Remove existing modal if any
  const existingModal = document.getElementById('comparisonModal');
  if (existingModal) {
    existingModal.remove();
  }
  
  const modal = document.createElement('div');
  modal.id = 'comparisonModal';
  modal.className = 'modal';
  modal.style.display = 'block';
  modal.innerHTML = `
    <div class="modal-content comparison-modal">
      <div class="modal-header">
        <h2><i class="fas fa-balance-scale"></i> ${title}</h2>
        <button class="close-modal" onclick="closeComparisonModal()">&times;</button>
      </div>
      <div class="modal-body">
        ${content}
      </div>
      <div class="modal-footer">
        <button onclick="clearAllComparisons()" class="btn-secondary">Clear All</button>
        <button onclick="closeComparisonModal()" class="btn-primary">Close</button>
      </div>
    </div>
  `;
  
  document.body.appendChild(modal);
}

function closeComparisonModal() {
  const modal = document.getElementById('comparisonModal');
  if (modal) {
    modal.remove();
  }
}

function clearAllComparisons() {
  selectedCourses = [];
  updateComparisonUI();
  
  // Uncheck all comparison checkboxes
  document.querySelectorAll('[id^="compare-"]').forEach(checkbox => {
    checkbox.checked = false;
  });
  
  closeComparisonModal();
  showNotification('All comparisons cleared', 'info');
}

// ===== THEME FUNCTIONS =====
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  const themeIcon = document.getElementById('themeIcon');
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  if (themeIcon) {
    themeIcon.className = newTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
}

// ===== UTILITY FUNCTIONS =====
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
  // Search input
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', filterCourses);
  }
  
  // Modal close on outside click
  window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
      event.target.remove();
    }
  };
  
  // Escape key to close modals
  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
      const modal = document.getElementById('comparisonModal');
      if (modal) {
        modal.remove();
      }
    }
  });
}

// ===== FIREBASE AUTH FUNCTIONS (Placeholder) =====
function showLoginModal() {
  // This will be handled by your firebase-auth.js file
  console.log('Login modal triggered');
}

function showSignupModal() {
  // This will be handled by your firebase-auth.js file
  console.log('Signup modal triggered');
}

function signOutUser() {
  // This will be handled by your firebase-auth.js file
  console.log('Sign out triggered');
}

// ===== INITIALIZATION =====
// Load theme from localStorage
const savedTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', savedTheme);
const themeIcon = document.getElementById('themeIcon');
if (themeIcon) {
  themeIcon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
}

// Initialize app when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeApp);
} else {
  initializeApp();
}

// Fallback initialization
setTimeout(() => {
  const courseContainer = document.getElementById('courseContainer');
  const labsContainer = document.getElementById('labsContainer');
  
  if (courseContainer && courseContainer.innerHTML.includes('Loading courses...')) {
    console.log('🔄 Attempting fallback initialization...');
    initializeApp();
  }
}, 2000);

console.log('✅ ImpactMojo main.js loaded');