// ImpactMojo Main JavaScript - Conflict-Free Version
console.log('🚀 Loading ImpactMojo Main JS...');

// ===== GLOBAL VARIABLES (with unique names to avoid conflicts) =====
let impactMojoAllCourses = [];
let impactMojoFilteredCourses = [];
let impactMojoSelectedCourses = [];
let impactMojoSelectedLabs = [];
let impactMojoUserBookmarks = JSON.parse(localStorage.getItem('impactMojoBookmarks')) || [];
let impactMojoUserLabBookmarks = JSON.parse(localStorage.getItem('impactMojoLabBookmarks')) || [];

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
    impactMojoAllCourses = window.courses;
    impactMojoFilteredCourses = [...impactMojoAllCourses];
    
    console.log(`Loaded ${impactMojoAllCourses.length} courses`);
    
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
  if (!impactMojoAllCourses || impactMojoAllCourses.length === 0) {
    container.innerHTML = '<div class="loading" style="text-align: center; padding: 2rem; color: var(--text-secondary);">Loading popular courses...</div>';
    setTimeout(displayPopularCourses, 500);
    return;
  }
  
  // Get popular courses by filtering for specific titles or taking first few
  let popularItems = impactMojoAllCourses.filter(course => 
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
    popularItems = impactMojoAllCourses.slice(0, 6);
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
  
  if (!impactMojoFilteredCourses || impactMojoFilteredCourses.length === 0) {
    container.innerHTML = '<div class="no-results" style="text-align: center; padding: 2rem; color: var(--text-secondary);">No courses found matching your criteria.</div>';
    return;
  }

  container.innerHTML = impactMojoFilteredCourses.map(course => createCourseCard(course)).join('');
  
  console.log(`✅ Displayed ${impactMojoFilteredCourses.length} courses`);
  
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
  
  impactMojoFilteredCourses = impactMojoAllCourses.filter(course => {
    const matchesSearch = !search || 
      course.title?.toLowerCase().includes(search) ||
      course.description?.toLowerCase().includes(search) ||
      course.category?.toLowerCase().includes(search);
    
    const matchesCategory = !categoryFilter || course.category === categoryFilter;
    const matchesDifficulty = !difficultyFilter || course.difficulty === difficultyFilter;
    
    return matchesSearch && matchesCategory && matchesDifficulty;
  });
  
  displayCourses();
  console.log(`Filtered to ${impactMojoFilteredCourses.length} courses`);
}

function clearFilters() {
  document.getElementById('courseSearch').value = '';
  document.getElementById('categoryFilter').value = '';
  document.getElementById('difficultyFilter').value = '';
  
  impactMojoFilteredCourses = [...impactMojoAllCourses];
  displayCourses();
  
  showNotification('Filters cleared', 'info');
}

function populateCategoryFilter() {
  const categoryFilter = document.getElementById('categoryFilter');
  if (!categoryFilter || !impactMojoAllCourses) return;
  
  const categories = [...new Set(impactMojoAllCourses.map(course => course.category).filter(Boolean))];
  
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
  const course = impactMojoAllCourses.find(c => c.id === courseId);
  if (!course) {
    showNotification('Course not found', 'error');
    return;
  }
  
  console.log(`Launching course: ${course.title}`);
  showNotification(`Opening ${course.title}...`, 'info');
}

function launchLab(labId) {
  const lab = window.labs?.find(l => l.id === labId);
  if (!lab) {
    showNotification('Lab not found', 'error');
    return;
  }
  
  console.log(`Launching lab: ${lab.title}`);
  showNotification(`Opening ${lab.title}...`, 'info');
}

// ===== BOOKMARK FUNCTIONS =====
function toggleBookmark(courseId) {
  const isBookmarked = impactMojoUserBookmarks.includes(courseId);
  
  if (isBookmarked) {
    impactMojoUserBookmarks = impactMojoUserBookmarks.filter(id => id !== courseId);
    showNotification('Bookmark removed', 'info');
  } else {
    impactMojoUserBookmarks.push(courseId);
    showNotification('Course bookmarked!', 'success');
  }
  
  // Save to localStorage
  localStorage.setItem('impactMojoBookmarks', JSON.stringify(impactMojoUserBookmarks));
  
  // Update UI
  updateBookmarkUI(courseId);
}

function toggleLabBookmark(labId) {
  const isBookmarked = impactMojoUserLabBookmarks.includes(labId);
  
  if (isBookmarked) {
    impactMojoUserLabBookmarks = impactMojoUserLabBookmarks.filter(id => id !== labId);
    showNotification('Lab bookmark removed', 'info');
  } else {
    impactMojoUserLabBookmarks.push(labId);
    showNotification('Lab bookmarked!', 'success');
  }
  
  localStorage.setItem('impactMojoLabBookmarks', JSON.stringify(impactMojoUserLabBookmarks));
  updateLabBookmarkUI(labId);
}

function updateBookmarkUI(courseId) {
  const bookmarkBtn = document.querySelector(`[onclick="toggleBookmark('${courseId}')"]`);
  if (bookmarkBtn) {
    const isBookmarked = impactMojoUserBookmarks.includes(courseId);
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
    const isBookmarked = impactMojoUserLabBookmarks.includes(labId);
    const icon = bookmarkBtn.querySelector('i');
    if (icon) {
      icon.className = isBookmarked ? 'fas fa-bookmark' : 'far fa-bookmark';
    }
    bookmarkBtn.classList.toggle('bookmarked', isBookmarked);
  }
}

function updateAllBookmarkUI() {
  if (impactMojoAllCourses && impactMojoAllCourses.length > 0) {
    impactMojoAllCourses.forEach(course => {
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
  
  if (totalElement) totalElement.textContent = impactMojoAllCourses.length;
  if (filteredElement) filteredElement.textContent = impactMojoFilteredCourses.length;
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
// ===== START: Enhanced Filter Functions =====

// Course filtering (enhanced version of your existing function)
function applyCourseFilters() {
  const searchTerm = document.getElementById('courseSearch')?.value.toLowerCase() || '';
  const category = document.getElementById('categoryFilter')?.value || '';
  const difficulty = document.getElementById('difficultyFilter')?.value || '';
  
  let allCourses = window.impactMojoAllCourses || window.courses || [];
  let filteredCourses = [...allCourses];
  
  // Apply search filter
  if (searchTerm) {
    filteredCourses = filteredCourses.filter(course => {
      return (course.title?.toLowerCase().includes(searchTerm)) ||
      (course.description?.toLowerCase().includes(searchTerm)) ||
      (course.category?.toLowerCase().includes(searchTerm));
    });
  }
  
  // Apply category filter
  if (category && category !== '') {
    filteredCourses = filteredCourses.filter(course => course.category === category);
  }
  
  // Apply difficulty filter
  if (difficulty && difficulty !== '') {
    filteredCourses = filteredCourses.filter(course => course.difficulty === difficulty);
  }
  
  // Update global variable
  if (window.impactMojoFilteredCourses !== undefined) {
    window.impactMojoFilteredCourses = filteredCourses;
  }
  
  // Update display
  if (typeof displayCourses === 'function') {
    displayCourses(filteredCourses);
  }
  
  // Update counts
  updateCourseStats(filteredCourses.length, allCourses.length);
  
  console.log(`Course filters applied: ${filteredCourses.length} of ${allCourses.length} courses`);
}

// Lab filtering (NEW function for labs)
function applyLabFilters() {
  const searchTerm = document.getElementById('labSearch')?.value.toLowerCase() || '';
  const category = document.getElementById('labCategoryFilter')?.value || '';
  const type = document.getElementById('labTypeFilter')?.value || '';
  
  let allLabs = window.labs || [];
  let filteredLabs = [...allLabs];
  
  // Apply search filter
  if (searchTerm) {
    filteredLabs = filteredLabs.filter(lab => {
      return (lab.title?.toLowerCase().includes(searchTerm)) ||
      (lab.description?.toLowerCase().includes(searchTerm)) ||
      (lab.category?.toLowerCase().includes(searchTerm)) ||
      (lab.labType?.toLowerCase().includes(searchTerm));
    });
  }
  
  // Apply category filter
  if (category && category !== '') {
    filteredLabs = filteredLabs.filter(lab => lab.category === category);
  }
  
  // Apply type filter
  if (type && type !== '') {
    filteredLabs = filteredLabs.filter(lab => lab.labType === type);
  }
  
  // Update display
  if (typeof displayLabs === 'function') {
    displayLabs(filteredLabs);
  }
  
  // Update counts
  updateLabStats(filteredLabs.length, allLabs.length);
  
  console.log(`Lab filters applied: ${filteredLabs.length} of ${allLabs.length} labs`);
}

// Clear course filters
function clearCourseFilters() {
  const courseSearch = document.getElementById('courseSearch');
  const categoryFilter = document.getElementById('categoryFilter');
  const difficultyFilter = document.getElementById('difficultyFilter');
  
  if (courseSearch) courseSearch.value = '';
  if (categoryFilter) categoryFilter.value = '';
  if (difficultyFilter) difficultyFilter.value = '';
  
  applyCourseFilters();
  
  if (typeof showNotification === 'function') {
    showNotification('Course filters cleared', 'success');
  }
}

// Clear lab filters
function clearLabFilters() {
  const labSearch = document.getElementById('labSearch');
  const labCategoryFilter = document.getElementById('labCategoryFilter');
  const labTypeFilter = document.getElementById('labTypeFilter');
  
  if (labSearch) labSearch.value = '';
  if (labCategoryFilter) labCategoryFilter.value = '';
  if (labTypeFilter) labTypeFilter.value = '';
  
  applyLabFilters();
  
  if (typeof showNotification === 'function') {
    showNotification('Lab filters cleared', 'success');
  }
}

// Update course statistics
function updateCourseStats(filtered, total) {
  const totalElement = document.getElementById('totalCourses');
  const visibleElement = document.getElementById('filteredCourses');
  
  if (totalElement) totalElement.textContent = total;
  if (visibleElement) visibleElement.textContent = filtered;
  
  // Also update the generic elements for backward compatibility
  const genericTotal = document.getElementById('totalCount');
  const genericVisible = document.getElementById('visibleCount');
  if (genericTotal) genericTotal.textContent = total;
  if (genericVisible) genericVisible.textContent = filtered;
}

// Update lab statistics
function updateLabStats(filtered, total) {
  const totalElement = document.getElementById('totalLabs');
  const visibleElement = document.getElementById('filteredLabs');
  
  if (totalElement) totalElement.textContent = total;
  if (visibleElement) visibleElement.textContent = filtered;
}

// Set up real-time search when page loads
document.addEventListener('DOMContentLoaded', function() {
  console.log('🔍 Setting up enhanced filters...');
  
  // Course search with delay
  const courseSearchInput = document.getElementById('courseSearch');
  if (courseSearchInput) {
    let courseSearchTimeout;
    courseSearchInput.addEventListener('input', function() {
      clearTimeout(courseSearchTimeout);
      courseSearchTimeout = setTimeout(applyCourseFilters, 300);
    });
  }
  
  // Lab search with delay
  const labSearchInput = document.getElementById('labSearch');
  if (labSearchInput) {
    let labSearchTimeout;
    labSearchInput.addEventListener('input', function() {
      clearTimeout(labSearchTimeout);
      labSearchTimeout = setTimeout(applyLabFilters, 300);
    });
  }
  
  // Initialize filters
  if (window.impactMojoAllCourses || window.courses) {
    applyCourseFilters();
  }
  
  if (window.labs) {
    applyLabFilters();
  }
});

// ===== END: Enhanced Filter Functions =====
// ===== START: Comparison Feature =====

// Global comparison state
let selectedForComparison = [];
const MAX_COMPARISON_ITEMS = 4;

// Enhanced addToComparison function with better checkbox management
function addToComparison(id, type, item) {
  const existingIndex = selectedForComparison.findIndex(selected => selected.id === id && selected.type === type);
  
  if (existingIndex !== -1) {
    // Remove if already selected
    selectedForComparison.splice(existingIndex, 1);
    updateComparisonCheckbox(id, type, false);
    showNotification('Removed from comparison', 'info');
  } else {
    // Check limit
    if (selectedForComparison.length >= MAX_COMPARISON_ITEMS) {
      showNotification(`Maximum ${MAX_COMPARISON_ITEMS} items can be compared`, 'warning');
      // Uncheck the checkbox since we can't add more
      const checkbox = document.querySelector(`[data-compare-id="${id}"][data-compare-type="${type}"]`);
      if (checkbox) {
        checkbox.checked = false;
        checkbox.closest('.comparison-checkbox-container')?.classList.remove('selected');
      }
      return;
    }
    
    // Add to comparison
    selectedForComparison.push({
      id: id,
      type: type,
      item: item
    });
    updateComparisonCheckbox(id, type, true);
    showNotification('Added to comparison', 'success');
  }
  
  updateComparisonButton();
  updateComparisonCounter();
}

// Enhanced updateComparisonCheckbox function
function updateComparisonCheckbox(id, type, isSelected) {
  const checkbox = document.querySelector(`[data-compare-id="${id}"][data-compare-type="${type}"]`);
  if (checkbox) {
    checkbox.checked = isSelected;
    const container = checkbox.closest('.comparison-checkbox-container');
    if (container) {
      if (isSelected) {
        container.classList.add('selected');
      } else {
        container.classList.remove('selected');
      }
    }
  }
}

// Update comparison button visibility and state
function updateComparisonButton() {
  let compareBtn = document.getElementById('compareSelectedBtn');
  
  if (!compareBtn) {
    // Create comparison button if it doesn't exist
    compareBtn = document.createElement('button');
    compareBtn.id = 'compareSelectedBtn';
    compareBtn.className = 'compare-floating-btn';
    compareBtn.innerHTML = '<i class="fas fa-balance-scale"></i> Compare (<span id="compareCount">0</span>)';
    compareBtn.onclick = openComparisonModal;
    document.body.appendChild(compareBtn);
  }
  
  if (selectedForComparison.length >= 2) {
    compareBtn.style.display = 'block';
    compareBtn.classList.add('visible');
  } else {
    compareBtn.style.display = 'none';
    compareBtn.classList.remove('visible');
  }
}

// Update comparison counter
function updateComparisonCounter() {
  const countSpan = document.getElementById('compareCount');
  if (countSpan) {
    countSpan.textContent = selectedForComparison.length;
  }
}

// Open comparison modal
function openComparisonModal() {
  if (selectedForComparison.length < 2) {
    showNotification('Select at least 2 items to compare', 'warning');
    return;
  }
  
  createComparisonModal();
  populateComparisonModal();
  
  const modal = document.getElementById('comparisonModal');
  if (modal) {
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
}

// Close comparison modal
function closeComparisonModal() {
  const modal = document.getElementById('comparisonModal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  }
}

// Clear all comparisons
function clearAllComparisons() {
  selectedForComparison = [];
  
  document.querySelectorAll('.comparison-checkbox').forEach(checkbox => {
    checkbox.checked = false;
  });
  
  updateComparisonButton();
  updateComparisonCounter();
  closeComparisonModal();
  
  showNotification('Comparison cleared', 'info');
}

// Create comparison modal HTML
function createComparisonModal() {
  const existingModal = document.getElementById('comparisonModal');
  if (existingModal) {
    existingModal.remove();
  }
  
  const modal = document.createElement('div');
  modal.id = 'comparisonModal';
  modal.className = 'comparison-modal';
  
  modal.innerHTML = `
    <div class="comparison-modal-content">
      <div class="comparison-header">
        <h2><i class="fas fa-balance-scale"></i> Compare Items</h2>
        <div class="comparison-actions">
          <button class="btn-secondary" onclick="clearAllComparisons()">
            <i class="fas fa-trash"></i> Clear All
          </button>
          <button class="btn-close" onclick="closeComparisonModal()">
            <i class="fas fa-times"></i>
          </button>
        </div>
      </div>
      <div class="comparison-content" id="comparisonContent"></div>
    </div>
  `;
  
  document.body.appendChild(modal);
  
  modal.addEventListener('click', function(e) {
    if (e.target === modal) {
      closeComparisonModal();
    }
  });
}

// TARGETED FIX: Enhanced content-level comparison
function populateComparisonModal() {
  const content = document.getElementById('comparisonContent');
  if (!content) return;
  
  content.innerHTML = '';
  
  const table = document.createElement('table');
  table.className = 'comparison-table';
  
  // Table Header
  const thead = document.createElement('thead');
  const headerRow = document.createElement('tr');
  
  const featureHeader = document.createElement('th');
  featureHeader.textContent = 'FEATURE';
  featureHeader.className = 'feature-label';
  headerRow.appendChild(featureHeader);
  
  selectedForComparison.forEach(selected => {
    const itemHeader = document.createElement('th');
    itemHeader.className = 'item-header';
    itemHeader.innerHTML = `
      <div class="item-type-badge ${selected.type}">${selected.type.toUpperCase()}</div>
      <h4 class="item-title">${selected.item.title}</h4>
      <button class="remove-from-comparison" onclick="removeFromComparison('${selected.id}', '${selected.type}')" title="Remove">×</button>
    `;
    headerRow.appendChild(itemHeader);
  });
  
  thead.appendChild(headerRow);
  table.appendChild(thead);
  
  // Table Body with Rich Content
  const tbody = document.createElement('tbody');
  
  // Content comparison rows
  const comparisonRows = [
    {
      label: 'Description',
      getValue: (item) => item.description || 'No description available'
    },
    {
      label: 'Topics Covered',
      getValue: (item) => item.topics ? item.topics.join(', ') : 'Not specified'
    },
    {
      label: 'Learning Outcomes',
      getValue: (item) => item.outcomes ? item.outcomes.join('; ') : 'Not specified'
    },
    {
      label: 'Prerequisites',
      getValue: (item) => item.prerequisites ? item.prerequisites.join(', ') : 'None specified'
    },
    {
      label: 'Target Audience',
      getValue: (item) => item.audience || 'General'
    },
    {
      label: 'Learning Path',
      getValue: (item) => item.learningPath || 'Standalone'
    },
    {
      label: 'Category',
      getValue: (item) => item.category || 'General'
    },
    {
      label: 'Difficulty',
      getValue: (item) => item.difficulty || 'Not specified'
    },
    {
      label: 'Duration',
      getValue: (item) => item.duration || 'Not specified'
    },
    {
      label: 'Rating',
      getValue: (item) => item.rating ? `${item.rating}/5.0` : 'Not rated'
    },
    {
      label: 'Related Resources',
      getValue: (item) => item.relatedExtras ? item.relatedExtras.join(', ') : 'None'
    }
  ];
  
  comparisonRows.forEach(row => {
    const tr = document.createElement('tr');
    
    // Feature label cell
    const featureCell = document.createElement('td');
    featureCell.className = 'feature-label';
    featureCell.textContent = row.label;
    tr.appendChild(featureCell);
    
    // Content cells for each selected item
    selectedForComparison.forEach(selected => {
      const contentCell = document.createElement('td');
      contentCell.className = 'comparison-text';
      const value = row.getValue(selected.item);
      
      // Special formatting for longer content
      if (row.label === 'Description' && value.length > 100) {
        contentCell.innerHTML = `
          <div class="description-preview">${value.substring(0, 100)}...</div>
          <button onclick="toggleFullDescription(this)" class="toggle-description">Show Full</button>
          <div class="description-full" style="display: none;">${value}</div>
        `;
      } else if (row.label === 'Topics Covered' || row.label === 'Learning Outcomes') {
        // Format as bullet list for better readability
        const items = value.includes(';') ? value.split(';') : value.split(',');
        if (items.length > 1) {
          contentCell.innerHTML = '<ul style="margin: 0; padding-left: 1rem;">' + 
            items.map(item => `<li>${item.trim()}</li>`).join('') + '</ul>';
        } else {
          contentCell.textContent = value;
        }
      } else {
        contentCell.textContent = value;
      }
      
      tr.appendChild(contentCell);
    });
    
    tbody.appendChild(tr);
  });
  
  // Action row
  const actionRow = document.createElement('tr');
  const actionFeatureCell = document.createElement('td');
  actionFeatureCell.className = 'feature-label';
  actionFeatureCell.textContent = 'ACTIONS';
  actionRow.appendChild(actionFeatureCell);
  
  selectedForComparison.forEach(selected => {
    const actionCell = document.createElement('td');
    actionCell.className = 'actions-cell';
    actionCell.innerHTML = `
      <button class="btn-primary" onclick="window.open('${selected.item.url}', '_blank')">
        <i class="fas fa-external-link-alt"></i> Launch ${selected.type}
      </button>
    `;
    actionRow.appendChild(actionCell);
  });
  
  tbody.appendChild(actionRow);
  table.appendChild(tbody);
  content.appendChild(table);
}

// TARGETED FIX: Toggle description helper function
function toggleFullDescription(button) {
  const preview = button.parentElement.querySelector('.description-preview');
  const full = button.parentElement.querySelector('.description-full');
  
  if (full.style.display === 'none') {
    preview.style.display = 'none';
    full.style.display = 'block';
    button.textContent = 'Show Less';
  } else {
    preview.style.display = 'block';
    full.style.display = 'none';
    button.textContent = 'Show Full';
  }
}

// TARGETED FIX: Enhanced remove function
function removeFromComparison(id, type) {
  selectedForComparison = selectedForComparison.filter(item => 
    !(item.id === id && item.type === type)
  );
  updateComparisonCheckbox(id, type, false);
  
  if (selectedForComparison.length < 2) {
    closeComparisonModal();
    showNotification('Need at least 2 items to compare', 'info');
  } else {
    populateComparisonModal();
  }
  
  updateComparisonButton();
  updateComparisonCounter();
}

// Fixed addComparisonCheckboxesToExistingCards function that preserves bookmarks
function addComparisonCheckboxesToExistingCards() {
  // Add to course cards
  document.querySelectorAll('.course-card').forEach(card => {
    if (card.querySelector('.comparison-checkbox')) return;
    
    const courseId = card.dataset.courseId || card.getAttribute('data-course-id');
    if (!courseId) return;
    
    const checkbox = document.createElement('div');
    checkbox.className = 'comparison-checkbox-container';
    checkbox.innerHTML = `
      <input 
        type="checkbox" 
        class="comparison-checkbox" 
        data-compare-id="${courseId}" 
        data-compare-type="course"
        onchange="handleComparisonCheckbox(this)"
        title="Add to comparison"
      >
    `;
    
    card.style.position = 'relative';
    card.insertBefore(checkbox, card.firstChild);
  });
  
  // Add to lab cards
  document.querySelectorAll('.lab-card').forEach(card => {
    if (card.querySelector('.comparison-checkbox')) return;
    
    const labId = card.dataset.labId || card.getAttribute('data-lab-id');
    if (!labId) return;
    
    const checkbox = document.createElement('div');
    checkbox.className = 'comparison-checkbox-container';
    checkbox.innerHTML = `
      <input 
        type="checkbox" 
        class="comparison-checkbox" 
        data-compare-id="${labId}" 
        data-compare-type="lab"
        onchange="handleComparisonCheckbox(this)"
        title="Add to comparison"
      >
    `;
    
    card.style.position = 'relative';
    card.insertBefore(checkbox, card.firstChild);
  });
}

// Enhanced handleComparisonCheckbox function with visual feedback
function handleComparisonCheckbox(checkbox) {
  const id = checkbox.getAttribute('data-compare-id');
  const type = checkbox.getAttribute('data-compare-type');
  const container = checkbox.closest('.comparison-checkbox-container');
  
  let item;
  if (type === 'course') {
    item = (window.impactMojoAllCourses || window.courses || []).find(course => course.id === id);
  } else {
    item = (window.labs || []).find(lab => lab.id === id);
  }
  
  if (item) {
    addToComparison(id, type, item);
    
    // Add visual feedback
    if (checkbox.checked) {
      container.classList.add('selected');
    } else {
      container.classList.remove('selected');
    }
  }
}

// Initialize comparison feature
document.addEventListener('DOMContentLoaded', function() {
  console.log('🔍 Initializing comparison feature...');
  setTimeout(() => {
    addComparisonCheckboxesToExistingCards();
  }, 1000);
});

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
  if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'C') {
    e.preventDefault();
    if (selectedForComparison.length >= 2) {
      openComparisonModal();
    }
  }
  
  if (e.key === 'Escape') {
    closeComparisonModal();
  }
});

// ===== END: Comparison Feature =====
// TARGETED FIX: Force show auth buttons if no user
document.addEventListener('DOMContentLoaded', function() {
  if (!currentUser) {
    const authButtons = document.getElementById('authButtons');
    if (authButtons) {
      authButtons.classList.remove('hidden');
      authButtons.style.display = 'flex';
    }
  }
});

// TARGETED FIX: Enhanced comparison functionality
function updateComparisonButton() {
  let compareBtn = document.getElementById('compareFab');
  
  // Create the button if it doesn't exist
  if (!compareBtn) {
    compareBtn = document.createElement('button');
    compareBtn.id = 'compareFab';
    compareBtn.className = 'fab-btn compare';
    compareBtn.onclick = showComparison;
    compareBtn.title = 'Compare courses';
    compareBtn.innerHTML = '<i class="fas fa-balance-scale"></i><span id="compareCount" style="position: absolute; top: -8px; right: -8px; background: white; color: var(--accent-color); border-radius: 50%; width: 20px; height: 20px; font-size: 0.7rem; display: flex; align-items: center; justify-content: center; font-weight: bold;">0</span>';
    
    const fabContainer = document.querySelector('.fab-container');
    if (fabContainer) {
      fabContainer.appendChild(compareBtn);
    }
  }
  
  const countSpan = document.getElementById('compareCount');
  if (countSpan) {
    countSpan.textContent = selectedForComparison.length;
  }
  
  // Show/hide based on selection count
  if (selectedForComparison.length >= 2) {
    compareBtn.style.display = 'flex';
    compareBtn.classList.add('visible');
  } else {
    compareBtn.style.display = 'none';
    compareBtn.classList.remove('visible');
  }
}

// TARGETED FIX: Enhanced comparison modal creation
function createComparisonModal() {
  const existingModal = document.getElementById('comparisonModal');
  if (existingModal) {
    existingModal.remove();
  }
  
  const modal = document.createElement('div');
  modal.id = 'comparisonModal';
  modal.className = 'comparison-modal';
  modal.style.display = 'block';
  
  modal.innerHTML = `
    <div class="comparison-modal-content">
      <div class="comparison-header">
        <h2><i class="fas fa-balance-scale"></i> Compare Items</h2>
        <div class="comparison-actions">
          <button class="btn-secondary" onclick="clearAllComparisons()">
            <i class="fas fa-trash"></i> Clear All
          </button>
          <button class="btn-secondary btn-close" onclick="closeComparisonModal()">
            <i class="fas fa-times"></i> Close
          </button>
        </div>
      </div>
      <div class="comparison-content" id="comparisonContent">
        <div class="comparison-preview">
          <h3>Selected Items (${selectedForComparison.length})</h3>
          <p>Comparison functionality restored! Selected items:</p>
          <ul>
            ${selectedForComparison.map(item => `<li>${item.name || item.id || 'Item'}</li>`).join('')}
          </ul>
        </div>
      </div>
    </div>
  `;
  
  document.body.appendChild(modal);
  
  // Close on outside click
  modal.addEventListener('click', function(e) {
    if (e.target === modal) {
      closeComparisonModal();
    }
  });
}

// TARGETED FIX: Enhanced clearAllComparisons function
function clearAllComparisons() {
  selectedForComparison = [];
  
  document.querySelectorAll('.comparison-checkbox').forEach(checkbox => {
    checkbox.checked = false;
  });
  
  updateComparisonButton();
  updateComparisonCounter();
  closeComparisonModal();
  
  if (typeof showNotification === 'function') {
    showNotification('Comparison cleared', 'info');
  }
}
// TARGETED FIX: Bookmark management functions
function updateBookmarkViewerButton() {
  const viewerBtn = document.getElementById('bookmarkViewerBtn');
  const countSpan = document.getElementById('bookmarkCount');
  const totalBookmarks = impactMojoUserBookmarks.length + impactMojoUserLabBookmarks.length;
  
  if (viewerBtn) {
    if (totalBookmarks > 0) {
      viewerBtn.style.display = 'flex';
      countSpan.textContent = totalBookmarks;
    } else {
      viewerBtn.style.display = 'none';
    }
  }
}

function showBookmarkModal() {
  let modal = document.getElementById('bookmarkModal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'bookmarkModal';
    modal.className = 'modal';
    document.body.appendChild(modal);
  }
  
  const bookmarkedCourses = impactMojoAllCourses.filter(course => 
    impactMojoUserBookmarks.includes(course.id)
  );
  const bookmarkedLabs = (window.labs || []).filter(lab => 
    impactMojoUserLabBookmarks.includes(lab.id)
  );
  
  modal.innerHTML = `
    <div class="modal-content">
      <span class="close" onclick="closeModal('bookmarkModal')">&times;</span>
      <h2><i class="fas fa-bookmark"></i> Your Bookmarks</h2>
      <div style="margin-bottom: 1rem;">
        <button onclick="exportBookmarks()" class="modal-btn" style="width: auto; margin-right: 1rem;">
          <i class="fas fa-download"></i> Export List
        </button>
        <button onclick="clearAllBookmarks()" class="modal-btn" style="width: auto; background: var(--accent-color);">
          <i class="fas fa-trash"></i> Clear All
        </button>
      </div>
      ${bookmarkedCourses.length > 0 ? `
        <h3>Courses (${bookmarkedCourses.length})</h3>
        ${bookmarkedCourses.map(course => `
          <div style="padding: 1rem; border: 1px solid var(--border-color); margin-bottom: 0.5rem; border-radius: 0.5rem;">
            <strong>${course.title}</strong><br>
            <small>${course.category} • ${course.duration}</small>
            <button onclick="toggleBookmark('${course.id}')" style="float: right; background: var(--accent-color); color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 0.25rem;">Remove</button>
          </div>
        `).join('')}
      ` : ''}
      ${bookmarkedLabs.length > 0 ? `
        <h3>Labs (${bookmarkedLabs.length})</h3>
        ${bookmarkedLabs.map(lab => `
          <div style="padding: 1rem; border: 1px solid var(--border-color); margin-bottom: 0.5rem; border-radius: 0.5rem;">
            <strong>${lab.title}</strong><br>
            <small>${lab.labType}</small>
            <button onclick="toggleLabBookmark('${lab.id}')" style="float: right; background: var(--accent-color); color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 0.25rem;">Remove</button>
          </div>
        `).join('')}
      ` : ''}
      ${bookmarkedCourses.length === 0 && bookmarkedLabs.length === 0 ? '<p>No bookmarks yet. Start exploring courses and labs!</p>' : ''}
    </div>
  `;
  
  modal.style.display = 'block';
}

function exportBookmarks() {
  const bookmarkedCourses = impactMojoAllCourses.filter(course => 
    impactMojoUserBookmarks.includes(course.id)
  );
  const bookmarkedLabs = (window.labs || []).filter(lab => 
    impactMojoUserLabBookmarks.includes(lab.id)
  );
  
  let exportText = "MY IMPACTMOJO BOOKMARKS\n\n";
  
  if (bookmarkedCourses.length > 0) {
    exportText += "COURSES:\n";
    bookmarkedCourses.forEach(course => {
      exportText += `• ${course.title} (${course.category}, ${course.duration})\n`;
    });
    exportText += "\n";
  }
  
  if (bookmarkedLabs.length > 0) {
    exportText += "LABS:\n";
    bookmarkedLabs.forEach(lab => {
      exportText += `• ${lab.title} (${lab.labType})\n`;
    });
  }
  
  navigator.clipboard.writeText(exportText).then(() => {
    showNotification('Bookmarks copied to clipboard!', 'success');
  });
  
  const blob = new Blob([exportText], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'impactmojo-bookmarks.txt';
  a.click();
  URL.revokeObjectURL(url);
}

function clearAllBookmarks() {
  if (confirm('Clear all bookmarks? This cannot be undone.')) {
    impactMojoUserBookmarks = [];
    impactMojoUserLabBookmarks = [];
    localStorage.setItem('impactMojoBookmarks', JSON.stringify([]));
    localStorage.setItem('impactMojoLabBookmarks', JSON.stringify([]));
    updateBookmarkViewerButton();
    updateAllBookmarkUI();
    updateAllLabBookmarkUI();
    closeModal('bookmarkModal');
    showNotification('All bookmarks cleared', 'info');
  }
}

// TARGETED FIX: Update existing bookmark functions
const originalToggleBookmark = toggleBookmark;
toggleBookmark = function(courseId) {
  originalToggleBookmark.call(this, courseId);
  updateBookmarkViewerButton();
};

const originalToggleLabBookmark = toggleLabBookmark;
toggleLabBookmark = function(labId) {
  originalToggleLabBookmark.call(this, labId);
  updateBookmarkViewerButton();
};