// Complete ImpactMojo Main JavaScript File
// Fixed version addressing all broken elements

console.log('🚀 Loading ImpactMojo Main JS...');

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

// ===== NOTIFICATION SYSTEM =====
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

// ===== COURSE INITIALIZATION =====
function initializeCourses() {
  console.log('📚 Initializing courses...');
  
  if (window.courses && Array.isArray(window.courses)) {
    allCourses = window.courses;
    filteredCourses = [...allCourses];
    
    console.log(`Loaded ${allCourses.length} courses`);
    
    // Update course stats
    updateCourseStats();
    
    // Populate category filter
    populateCategoryFilter();
    
    // Display courses
    displayCourses();
    
    console.log('✅ Courses initialized successfully');
  } else {
    console.warn('⚠️ Course data not available yet, retrying...');
    setTimeout(initializeCourses, 1000);
  }
}

// ===== POPULAR COURSES FUNCTIONALITY =====
function displayPopularCourses() {
  const container = document.getElementById('popularCoursesContainer');
  
  if (!container) {
    console.log('ℹ️ Popular courses container not found');
    return;
  }
  
  // Wait for courses to be loaded
  if (!allCourses || allCourses.length === 0) {
    container.innerHTML = '<div class="loading" style="text-align: center; padding: 2rem; color: var(--text-secondary);">Loading popular courses...</div>';
    setTimeout(displayPopularCourses, 500);
    return;
  }
  
  // Get popular courses by filtering for specific titles or taking first few
  let popularItems = allCourses.filter(course => 
    course && (
      course.title?.toLowerCase().includes('gender') ||
      course.title?.toLowerCase().includes('development economics') ||
      course.title?.toLowerCase().includes('research ethics') ||
      course.title?.toLowerCase().includes('public health') ||
      course.title?.toLowerCase().includes('data literacy')
    )
  );
  
  // If no matches found, take first 6 courses
  if (popularItems.length === 0) {
    popularItems = allCourses.slice(0, 6);
  } else {
    popularItems = popularItems.slice(0, 6);
  }
  
  // Add some labs if available
  if (window.labs && window.labs.length > 0) {
    popularItems = [...popularItems.slice(0, 4), ...window.labs.slice(0, 2)];
  }

  container.innerHTML = popularItems.map(item => {
    if (item.labType) {
      return createLabCard(item);
    } else {
      return createCourseCard(item);
    }
  }).join('');
  
  console.log(`✅ Displayed ${popularItems.length} popular items`);
  
  // Update bookmark UI after displaying
  setTimeout(() => {
    updateAllBookmarkUI();
    updateAllLabBookmarkUI();
  }, 100);
}

// ===== COURSE DISPLAY FUNCTIONS =====
function displayCourses() {
  const container = document.getElementById('coursesContainer');
  
  if (!container) {
    console.error('❌ Course container not found');
    return;
  }
  
  if (!filteredCourses || filteredCourses.length === 0) {
    container.innerHTML = '<div class="no-results" style="text-align: center; padding: 2rem; color: var(--text-secondary);">No courses found matching your criteria.</div>';
    return;
  }

  container.innerHTML = filteredCourses.map(course => createCourseCard(course)).join('');
  
  console.log(`✅ Displayed ${filteredCourses.length} courses`);
  
  // Update stats
  updateCourseStats();
  
  // Update bookmark UI after displaying
  setTimeout(updateAllBookmarkUI, 100);
}

// ===== COURSE CARD CREATION =====
function createCourseCard(course) {
  if (!course || !course.id) {
    console.warn('Invalid course data:', course);
    return '';
  }
  
  // Safely handle potentially undefined values
  const rating = course.rating || 4.5;
  const duration = course.duration || '30 min';
  const difficulty = course.difficulty || 'Intermediate';
  const category = course.category || 'General';
  const description = course.description || 'No description available';
  const title = course.title || 'Untitled Course';
  const courseId = course.id;
  
  // Get category color
  const categoryColor = getCategoryColor(category);
  
  return `
    <div class="course-card" data-course-id="${courseId}" style="border-left: 4px solid ${categoryColor}">
      <div class="course-card-header">
        <div class="course-category" style="background-color: ${categoryColor}20; color: ${categoryColor}">
          ${category}
        </div>
        <div class="course-actions">
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
          Launch Course
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
  
  if (!window.labs || window.labs.length === 0) {
    container.innerHTML = '<div class="no-results" style="text-align: center; padding: 2rem; color: var(--text-secondary);">Interactive labs will be available soon...</div>';
    return;
  }

  container.innerHTML = window.labs.map(lab => createLabCard(lab)).join('');
  
  console.log(`✅ Displayed ${window.labs.length} labs`);
  
  // Update bookmark UI
  setTimeout(updateAllLabBookmarkUI, 100);
}

function createLabCard(lab) {
  if (!lab || !lab.id) {
    console.warn('Invalid lab data:', lab);
    return '';
  }
  
  const labId = lab.id;
  const title = lab.title || 'Untitled Lab';
  const description = lab.description || 'No description available';
  const category = lab.category || 'Interactive Tool';
  const labType = lab.labType || 'Simulation';
  
  return `
    <div class="lab-card" data-lab-id="${labId}">
      <div class="lab-card-header">
        <div class="lab-category">${category}</div>
        <div class="lab-actions">
          <div class="lab-type-badge">${labType}</div>
          <button class="bookmark-btn" onclick="toggleLabBookmark('${labId}')" aria-label="Bookmark lab">
            <i class="far fa-bookmark"></i>
          </button>
        </div>
      </div>
      
      <div class="lab-content">
        <h3 class="lab-title">${title}</h3>
        <p class="lab-description">${description}</p>
      </div>
      
      <div class="lab-card-footer">
        <button class="lab-launch" onclick="launchLab('${labId}')">
          <i class="fas fa-play"></i>
          Launch Lab
        </button>
      </div>
    </div>
  `;
}

// ===== SEARCH AND FILTER FUNCTIONS =====
function searchCourses() {
  const searchTerm = document.getElementById('courseSearch')?.value.toLowerCase() || '';
  filterCourses(searchTerm);
}

function filterCourses(searchTerm = '') {
  const categoryFilter = document.getElementById('categoryFilter')?.value || '';
  const difficultyFilter = document.getElementById('difficultyFilter')?.value || '';
  const search = searchTerm || document.getElementById('courseSearch')?.value.toLowerCase() || '';
  
  filteredCourses = allCourses.filter(course => {
    const matchesSearch = !search || 
      course.title?.toLowerCase().includes(search) ||
      course.description?.toLowerCase().includes(search) ||
      course.category?.toLowerCase().includes(search);
    
    const matchesCategory = !categoryFilter || course.category === categoryFilter;
    const matchesDifficulty = !difficultyFilter || course.difficulty === difficultyFilter;
    
    return matchesSearch && matchesCategory && matchesDifficulty;
  });
  
  displayCourses();
  console.log(`Filtered to ${filteredCourses.length} courses`);
}

function clearFilters() {
  document.getElementById('courseSearch').value = '';
  document.getElementById('categoryFilter').value = '';
  document.getElementById('difficultyFilter').value = '';
  
  filteredCourses = [...allCourses];
  displayCourses();
  
  showNotification('Filters cleared', 'info');
}

function populateCategoryFilter() {
  const categoryFilter = document.getElementById('categoryFilter');
  if (!categoryFilter || !allCourses) return;
  
  const categories = [...new Set(allCourses.map(course => course.category).filter(Boolean))];
  
  // Clear existing options (except the first one)
  const firstOption = categoryFilter.querySelector('option[value=""]');
  categoryFilter.innerHTML = '';
  if (firstOption) {
    categoryFilter.appendChild(firstOption);
  } else {
    const allOption = document.createElement('option');
    allOption.value = '';
    allOption.textContent = 'All Categories';
    categoryFilter.appendChild(allOption);
  }
  
  categories.forEach(category => {
    const option = document.createElement('option');
    option.value = category;
    option.textContent = category;
    categoryFilter.appendChild(option);
  });
}

// ===== COURSE INTERACTION FUNCTIONS =====
function launchCourse(courseId) {
  const course = allCourses.find(c => c.id === courseId);
  if (!course) {
    showNotification('Course not found', 'error');
    return;
  }
  
  // Track course launch
  console.log(`Launching course: ${course.title}`);
  
  // Update user progress if authenticated
  if (typeof updateUserProgress === 'function' && window.auth?.currentUser) {
    updateUserProgress(courseId, { lastAccessed: new Date() });
  }
  
  // For now, show notification (can be enhanced to open course viewer)
  showNotification(`Opening ${course.title}...`, 'info');
  
  // Could open in new window or modal here
  // window.open(`/courses/${courseId}`, '_blank');
}

function launchLab(labId) {
  const lab = window.labs?.find(l => l.id === labId);
  if (!lab) {
    showNotification('Lab not found', 'error');
    return;
  }
  
  console.log(`Launching lab: ${lab.title}`);
  showNotification(`Opening ${lab.title}...`, 'info');
  
  // Could open lab in new window
  // window.open(`/labs/${labId}`, '_blank');
}

// ===== BOOKMARK FUNCTIONS =====
function toggleBookmark(courseId) {
  if (!window.auth?.currentUser) {
    showNotification('Please log in to bookmark courses', 'warning');
    return;
  }
  
  const isBookmarked = userBookmarks.includes(courseId);
  
  if (isBookmarked) {
    userBookmarks = userBookmarks.filter(id => id !== courseId);
    showNotification('Bookmark removed', 'info');
  } else {
    userBookmarks.push(courseId);
    showNotification('Course bookmarked!', 'success');
  }
  
  // Save to localStorage
  localStorage.setItem('userBookmarks', JSON.stringify(userBookmarks));
  
  // Update UI
  updateBookmarkUI(courseId);
  
  // Save to Firebase if available
  if (typeof saveUserBookmarks === 'function') {
    saveUserBookmarks();
  }
}

function toggleLabBookmark(labId) {
  if (!window.auth?.currentUser) {
    showNotification('Please log in to bookmark labs', 'warning');
    return;
  }
  
  const isBookmarked = userLabBookmarks.includes(labId);
  
  if (isBookmarked) {
    userLabBookmarks = userLabBookmarks.filter(id => id !== labId);
    showNotification('Lab bookmark removed', 'info');
  } else {
    userLabBookmarks.push(labId);
    showNotification('Lab bookmarked!', 'success');
  }
  
  localStorage.setItem('userLabBookmarks', JSON.stringify(userLabBookmarks));
  updateLabBookmarkUI(labId);
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
  if (allCourses && allCourses.length > 0) {
    allCourses.forEach(course => {
      updateBookmarkUI(course.id);
    });
  }
}

function updateAllLabBookmarkUI() {
  if (window.labs && window.labs.length > 0) {
    window.labs.forEach(lab => {
      updateLabBookmarkUI(lab.id);
    });
  }
}

// ===== UTILITY FUNCTIONS =====
function getCategoryColor(category) {
  const categoryColors = {
    'Economics': '#27ae60',
    'Gender': '#9b59b6', 
    'Justice': '#e74c3c',
    'Climate': '#16a085',
    'Data': '#3498db',
    'Development': '#2c3e50',
    'Livelihoods': '#27ae60',
    'Health': '#e74c3c',
    'Education': '#3498db',
    'Systems': '#34495e',
    'Data & Research': '#3498db',
    'Gender & Social Issues': '#9b59b6',
    'Economics & Policy': '#e74c3c',
    'Health & Environment': '#16a085',
    'Education & Communication': '#f39c12',
    'Technology & Ethics': '#2c3e50',
    'Community & Fundraising': '#27ae60',
    'Governance & Policy': '#ea580c',
    'Default': '#6c757d'
  };
  return categoryColors[category] || categoryColors['Default'];
}

function updateCourseStats() {
  const totalElement = document.getElementById('totalCourses');
  const filteredElement = document.getElementById('filteredCourses');
  
  if (totalElement) totalElement.textContent = allCourses.length;
  if (filteredElement) filteredElement.textContent = filteredCourses.length;
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

// ===== LEARNING PATH FUNCTIONS =====
function filterCoursesByPath(pathId) {
  console.log(`Filtering courses by path: ${pathId}`);
  
  // Define learning path mappings
  const pathMappings = {
    'data-analysis': ['data-literacy-101', 'eda-survey-data', 'bivariate-analysis', 'multivariate-analysis'],
    'gender-studies': ['gender-studies-101', 'data-feminism-101', 'care-economy', 'womens-empowerment'],
    'policy-economics': ['dev-econ-101', 'political-economy', 'poverty-inequality-101', 'social-safety-nets'],
    'research-methods': ['research-ethics-101', 'qualitative-research', 'econometrics', 'mel']
  };
  
  const pathCourseIds = pathMappings[pathId] || [];
  
  if (pathCourseIds.length > 0) {
    filteredCourses = allCourses.filter(course => 
      pathCourseIds.includes(course.id)
    );
    displayCourses();
    showNotification(`Showing ${pathId.replace('-', ' ')} learning path`, 'info');
  }
}

// ===== KEYBOARD SHORTCUTS =====
document.addEventListener('keydown', function(e) {
  // Ctrl/Cmd + K for search
  if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
    e.preventDefault();
    const searchInput = document.getElementById('courseSearch');
    if (searchInput) {
      searchInput.focus();
    }
  }
  
  // Ctrl/Cmd + D for dark mode
  if ((e.ctrlKey || e.metaKey) && e.key === 'd') {
    e.preventDefault();
    toggleTheme();
  }
});

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', function() {
  console.log('🚀 Main JS DOM loaded');
  
  // Initialize theme toggle
  initializeThemeToggle();
  
  // Wait for data to be available
  if (window.courses) {
    initializeCourses();
    displayPopularCourses();
    displayLabs();
  } else {
    console.log('⏳ Waiting for course data...');
    window.addEventListener('dataLoaded', function() {
      console.log('📊 Data loaded event received');
      initializeCourses();
      displayPopularCourses();
      displayLabs();
    });
  }
});

console.log('✅ Main JS loaded successfully!');