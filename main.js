// ImpactMojo Main JavaScript - Complete Working Version
console.log('🚀 Loading ImpactMojo Main JS...');

// ===== GLOBAL VARIABLES =====
let impactMojoAllCourses = [];
let impactMojoFilteredCourses = [];
let impactMojoSelectedCourses = [];
let impactMojoSelectedLabs = [];
let impactMojoUserBookmarks = JSON.parse(localStorage.getItem('impactMojoBookmarks')) || [];
let impactMojoUserLabBookmarks = JSON.parse(localStorage.getItem('impactMojoLabBookmarks')) || [];

// ===== THEME TOGGLE =====
function toggleTheme() {
  console.log('🎨 Toggling theme...');
  
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  console.log(`Switching from ${currentTheme} to ${newTheme}`);
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  if (themeIcon) {
    themeIcon.className = newTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    console.log(`Icon updated to: ${themeIcon.className}`);
  }
  
  showNotification(`Switched to ${newTheme} mode`, 'success');
}

function initializeThemeToggle() {
  console.log('🎨 Initializing theme toggle');
  
  const savedTheme = localStorage.getItem('theme') || 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  console.log(`Saved theme: ${savedTheme}`);
  
  document.documentElement.setAttribute('data-theme', savedTheme);
  
  if (themeIcon) {
    themeIcon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    console.log(`Initial icon set to: ${themeIcon.className}`);
  }
}

// ===== NOTIFICATION SYSTEM =====
function showNotification(message, type = 'info') {
  const existingNotifications = document.querySelectorAll('.notification');
  existingNotifications.forEach(notification => notification.remove());
  
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.innerHTML = `
    <span>${message}</span>
    <button onclick="this.parentElement.remove()">&times;</button>
  `;
  
  document.body.appendChild(notification);
  
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
    
    updateCourseStats();
    populateCategoryFilter();
    displayCourses();
    
    console.log('✅ Courses initialized successfully');
  } else {
    console.warn('⚠️ Course data not available yet, retrying...');
    setTimeout(initializeCourses, 1000);
  }
}

// ===== POPULAR COURSES =====
function displayPopularCourses() {
  const container = document.getElementById('popularCoursesContainer');
  
  if (!container) {
    console.log('ℹ️ Popular courses container not found');
    return;
  }
  
  if (!impactMojoAllCourses || impactMojoAllCourses.length === 0) {
    container.innerHTML = '<div class="loading" style="text-align: center; padding: 2rem; color: var(--text-secondary);">Loading popular courses...</div>';
    setTimeout(displayPopularCourses, 500);
    return;
  }
  
  let popularItems = impactMojoAllCourses.filter(course => 
    course && (
      course.title?.toLowerCase().includes('gender') ||
      course.title?.toLowerCase().includes('data') ||
      course.title?.toLowerCase().includes('economics') ||
      course.title?.toLowerCase().includes('health')
    )
  ).slice(0, 6);
  
  if (popularItems.length === 0) {
    popularItems = impactMojoAllCourses.slice(0, 6);
  }
  
  container.innerHTML = popularItems.map(course => createCourseCard(course)).join('');
  
  console.log(`✅ Displayed ${popularItems.length} popular courses`);
  
  setTimeout(updateAllBookmarkUI, 100);
}

// ===== SEARCH AND FILTER =====
function searchCourses() {
  const searchTerm = document.getElementById('courseSearch')?.value.toLowerCase() || '';
  const selectedCategory = document.getElementById('categoryFilter')?.value || 'all';
  const selectedDifficulty = document.getElementById('difficultyFilter')?.value || 'all';
  
  impactMojoFilteredCourses = impactMojoAllCourses.filter(course => {
    const matchesSearch = !searchTerm || 
      course.title?.toLowerCase().includes(searchTerm) ||
      course.description?.toLowerCase().includes(searchTerm) ||
      course.category?.toLowerCase().includes(searchTerm);
    
    const matchesCategory = selectedCategory === 'all' || 
      course.category === selectedCategory;
    
    const matchesDifficulty = selectedDifficulty === 'all' || 
      course.difficulty?.toLowerCase() === selectedDifficulty.toLowerCase();
    
    return matchesSearch && matchesCategory && matchesDifficulty;
  });
  
  displayCourses();
  updateCourseStats();
}

function populateCategoryFilter() {
  const categoryFilter = document.getElementById('categoryFilter');
  if (!categoryFilter) return;
  
  const categories = [...new Set(impactMojoAllCourses.map(course => course.category))].filter(Boolean);
  
  categoryFilter.innerHTML = '<option value="all">All Categories</option>';
  categories.forEach(category => {
    const option = document.createElement('option');
    option.value = category;
    option.textContent = category;
    categoryFilter.appendChild(option);
  });
}

function clearAllFilters() {
  const searchInput = document.getElementById('courseSearch');
  const categoryFilter = document.getElementById('categoryFilter');
  const difficultyFilter = document.getElementById('difficultyFilter');
  
  if (searchInput) searchInput.value = '';
  if (categoryFilter) categoryFilter.value = 'all';
  if (difficultyFilter) difficultyFilter.value = 'all';
  
  impactMojoFilteredCourses = [...impactMojoAllCourses];
  
  displayCourses();
  updateCourseStats();
  
  showNotification('All filters cleared', 'info');
}

// ===== DISPLAY FUNCTIONS =====
function displayCourses() {
  const container = document.getElementById('coursesContainer');
  
  if (!container) {
    console.log('ℹ️ Courses container not found, skipping course display');
    return;
  }
  
  if (impactMojoFilteredCourses.length === 0) {
    container.innerHTML = '<div class="no-results"><i class="fas fa-search"></i><h3>No courses found</h3><p>Try adjusting your filters or search terms.</p></div>';
    return;
  }

  container.innerHTML = impactMojoFilteredCourses.map(course => createCourseCard(course)).join('');
  
  console.log(`✅ Displayed ${impactMojoFilteredCourses.length} courses`);
  
  setTimeout(updateAllBookmarkUI, 100);
}

function createCourseCard(course) {
  if (!course) return '';
  
  const category = course.category || 'General';
  const difficulty = course.difficulty || 'Beginner';
  const duration = course.duration || 'Self-paced';
  const rating = course.rating || 4.5;
  const description = course.description || 'No description available';
  const title = course.title || 'Untitled Course';
  const courseId = course.id;
  
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

// ===== LAB FUNCTIONS =====
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
  
  setTimeout(updateAllLabBookmarkUI, 100);
}

function createLabCard(lab) {
  if (!lab) return '';
  
  const category = lab.category || 'Interactive';
  const difficulty = lab.difficulty || 'Beginner';
  const duration = lab.duration || '30 min';
  const description = lab.description || 'Interactive lab experience';
  const title = lab.title || 'Untitled Lab';
  const labId = lab.id;
  const labType = lab.type || 'Simulation';
  
  return `
    <div class="lab-card" data-lab-id="${labId}">
      <div class="lab-card-header">
        <div class="lab-category">
          ${category}
        </div>
        <div class="lab-type-badge">${labType}</div>
        <div class="lab-actions">
          <button class="bookmark-btn" onclick="toggleLabBookmark('${labId}')" aria-label="Bookmark lab">
            <i class="far fa-bookmark"></i>
          </button>
        </div>
      </div>
      
      <div class="lab-content">
        <h3 class="lab-title">${title}</h3>
        <p class="lab-description">${description}</p>
        
        <div class="lab-meta">
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
        <button class="lab-launch-btn" onclick="launchLab('${labId}')">
          <i class="fas fa-flask"></i>
          Launch Lab
        </button>
      </div>
    </div>
  `;
}

// ===== BOOKMARKING =====
function toggleBookmark(courseId) {
  const index = impactMojoUserBookmarks.indexOf(courseId);
  
  if (index === -1) {
    impactMojoUserBookmarks.push(courseId);
    showNotification('Course bookmarked!', 'success');
  } else {
    impactMojoUserBookmarks.splice(index, 1);
    showNotification('Bookmark removed', 'info');
  }
  
  localStorage.setItem('impactMojoBookmarks', JSON.stringify(impactMojoUserBookmarks));
  updateBookmarkUI(courseId);
}

function toggleLabBookmark(labId) {
  const index = impactMojoUserLabBookmarks.indexOf(labId);
  
  if (index === -1) {
    impactMojoUserLabBookmarks.push(labId);
    showNotification('Lab bookmarked!', 'success');
  } else {
    impactMojoUserLabBookmarks.splice(index, 1);
    showNotification('Lab bookmark removed', 'info');
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

// ===== LAUNCHING =====
function launchCourse(courseId) {
  console.log(`🚀 Launching course: ${courseId}`);
  showNotification('Course launching...', 'info');
  
  const course = impactMojoAllCourses.find(c => c.id === courseId);
  if (course && course.url) {
    window.open(course.url, '_blank');
  } else {
    showNotification('Course content coming soon!', 'info');
  }
}

function launchLab(labId) {
  console.log(`🧪 Launching lab: ${labId}`);
  showNotification('Lab launching...', 'info');
  
  const lab = window.labs?.find(l => l.id === labId);
  if (lab && lab.url) {
    window.open(lab.url, '_blank');
  } else {
    showNotification('Lab content coming soon!', 'info');
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

// ===== NAVIGATION CENTERING FIX =====
function centerNavigation() {
  console.log('🎯 Applying navigation centering...');
  
  setTimeout(() => {
    const navContainer = document.querySelector('.navbar .container');
    const navMenu = document.querySelector('.nav-menu');
    const navActions = document.querySelector('.nav-actions');
    
    if (navContainer) {
      navContainer.style.setProperty('justify-content', 'center', 'important');
      navContainer.style.setProperty('gap', '2rem', 'important');
      navContainer.style.setProperty('padding', '1.5rem 1rem', 'important');
    }
    
    if (navMenu) {
      navMenu.style.setProperty('justify-content', 'center', 'important');
      navMenu.style.setProperty('order', '1', 'important');
    }
    
    if (navActions) {
      navActions.style.setProperty('position', 'absolute', 'important');
      navActions.style.setProperty('right', '1rem', 'important');
      navActions.style.setProperty('order', '2', 'important');
    }
    
    console.log('✅ Navigation centering applied');
  }, 500);
}

// ===== KEYBOARD SHORTCUTS =====
document.addEventListener('keydown', function(e) {
  if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
    e.preventDefault();
    const searchInput = document.getElementById('courseSearch');
    if (searchInput) {
      searchInput.focus();
    }
  }
  
  if ((e.ctrlKey || e.metaKey) && e.key === 'd') {
    e.preventDefault();
    toggleTheme();
  }
});

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', function() {
  console.log('🚀 Main JS DOM loaded');
  
  initializeThemeToggle();
  centerNavigation();
  
  const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      if (mutation.type === 'childList' && mutation.target.classList?.contains('nav-links')) {
        console.log('🔄 Navigation updated, reapplying centering...');
        centerNavigation();
      }
    });
  });
  
  const navLinks = document.querySelector('.nav-links');
  if (navLinks) {
    observer.observe(navLinks, { childList: true, subtree: true });
  }
  
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
// ===== ADD THESE MISSING FUNCTIONS AT THE END OF main.js =====

// Missing function that FAB button calls
function showComparison() {
  showComparisonModal();
}

// Comparison functionality
let selectedForComparison = [];
const MAX_COMPARISON_ITEMS = 4;

function showComparisonModal() {
  if (selectedForComparison.length < 2) {
    showNotification('Please select at least 2 items to compare', 'warning');
    return;
  }
  
  updateComparisonContent();
  openModal('comparisonModal');
}

function toggleComparison(itemId, itemType) {
  const itemKey = `${itemType}-${itemId}`;
  const index = selectedForComparison.findIndex(item => item.key === itemKey);
  
  if (index === -1) {
    if (selectedForComparison.length >= MAX_COMPARISON_ITEMS) {
      showNotification(`You can only compare up to ${MAX_COMPARISON_ITEMS} items at once`, 'warning');
      return false;
    }
    
    selectedForComparison.push({
      key: itemKey,
      id: itemId,
      type: itemType
    });
    
    showNotification(`Added to comparison (${selectedForComparison.length}/${MAX_COMPARISON_ITEMS})`, 'success');
  } else {
    selectedForComparison.splice(index, 1);
    showNotification('Removed from comparison', 'info');
  }
  
  updateComparisonUI();
  return true;
}

function updateComparisonUI() {
  // Update all comparison checkboxes
  document.querySelectorAll('.comparison-checkbox').forEach(checkbox => {
    const itemId = checkbox.dataset.itemId;
    const itemType = checkbox.dataset.itemType;
    const itemKey = `${itemType}-${itemId}`;
    checkbox.checked = selectedForComparison.some(item => item.key === itemKey);
  });
  
  // Update FAB button visibility
  const compareFab = document.querySelector('.fab-btn.compare');
  if (compareFab) {
    compareFab.style.display = selectedForComparison.length > 1 ? 'block' : 'none';
  }
}

function updateComparisonContent() {
  const content = document.getElementById('comparisonContent');
  if (!content) return;
  
  if (selectedForComparison.length === 0) {
    content.innerHTML = `
      <div class="comparison-placeholder">
        <i class="fas fa-balance-scale"></i>
        <h3>No items selected for comparison</h3>
        <p>Select courses or labs using the comparison checkboxes to compare them here.</p>
      </div>
    `;
    return;
  }
  
  // Get the actual items
  const items = selectedForComparison.map(selected => {
    if (selected.type === 'course') {
      return { ...impactMojoAllCourses.find(c => c.id === selected.id), type: 'course' };
    } else if (selected.type === 'lab') {
      return { ...(window.labs || []).find(l => l.id === selected.id), type: 'lab' };
    }
  }).filter(item => item && item.id);
  
  content.innerHTML = createBasicComparisonTable(items);
}

function createBasicComparisonTable(items) {
  return `
    <div class="comparison-stats">
      <p>Comparing <strong>${items.length}</strong> items</p>
      <button onclick="clearComparison()" class="clear-btn" style="margin-left: 1rem;">
        <i class="fas fa-trash"></i> Clear All
      </button>
    </div>
    
    <div class="comparison-table-container">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Attribute</th>
            ${items.map(item => `<th>${item.title} (${item.type})</th>`).join('')}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Description</strong></td>
            ${items.map(item => `<td>${item.description || 'No description'}</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Difficulty</strong></td>
            ${items.map(item => `<td><span class="difficulty-badge difficulty-${(item.difficulty || 'beginner').toLowerCase()}">${item.difficulty || 'Beginner'}</span></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Duration</strong></td>
            ${items.map(item => `<td>${item.duration || 'Self-paced'}</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Topics</strong></td>
            ${items.map(item => `<td>${(item.topics || []).join(', ') || 'Not specified'}</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Prerequisites</strong></td>
            ${items.map(item => `<td>${(item.prerequisites || []).join(', ') || 'None'}</td>`).join('')}
          </tr>
          <tr>
            <td><strong>Actions</strong></td>
            ${items.map(item => `
              <td>
                <button onclick="${item.type === 'course' ? 'launchCourse' : 'launchLab'}('${item.id}')" 
                        class="launch-comparison-btn">
                  <i class="fas fa-external-link-alt"></i> Launch
                </button>
              </td>
            `).join('')}
          </tr>
        </tbody>
      </table>
    </div>
  `;
}

function clearComparison() {
  selectedForComparison = [];
  updateComparisonUI();
  updateComparisonContent();
  showNotification('Comparison cleared', 'info');
}

// Bookmark viewer functionality
function showBookmarkModal() {
  if (!document.getElementById('bookmarkViewerModal')) {
    createBookmarkViewerModal();
  }
  
  displayBookmarkedItems();
  openModal('bookmarkViewerModal');
}

function createBookmarkViewerModal() {
  const modal = document.createElement('div');
  modal.id = 'bookmarkViewerModal';
  modal.className = 'modal';
  modal.innerHTML = `
    <div class="modal-content large">
      <span class="close" onclick="closeModal('bookmarkViewerModal')">&times;</span>
      <div class="bookmark-modal-header">
        <h2><i class="fas fa-bookmark"></i> Your Bookmarks</h2>
        <div class="bookmark-modal-actions">
          <button onclick="exportBookmarks('csv')" class="export-btn">
            <i class="fas fa-file-csv"></i> Export CSV
          </button>
          <button onclick="clearAllBookmarks()" class="clear-btn">
            <i class="fas fa-trash"></i> Clear All
          </button>
        </div>
      </div>
      <div id="bookmarkViewerContent">
        <!-- Bookmarked items will be displayed here -->
      </div>
    </div>
  `;
  document.body.appendChild(modal);
}

function displayBookmarkedItems() {
  const content = document.getElementById('bookmarkViewerContent');
  if (!content) return;
  
  const bookmarkedCourses = impactMojoAllCourses.filter(course => 
    impactMojoUserBookmarks.includes(course.id)
  );
  
  const bookmarkedLabs = (window.labs || []).filter(lab => 
    impactMojoUserLabBookmarks.includes(lab.id)
  );
  
  if (bookmarkedCourses.length === 0 && bookmarkedLabs.length === 0) {
    content.innerHTML = `
      <div class="no-bookmarks">
        <i class="fas fa-bookmark"></i>
        <h3>No bookmarks yet</h3>
        <p>Bookmark courses and labs to access them quickly!</p>
      </div>
    `;
    return;
  }
  
  let html = '';
  
  if (bookmarkedCourses.length > 0) {
    html += `
      <div class="bookmark-section">
        <h3><i class="fas fa-graduation-cap"></i> Courses (${bookmarkedCourses.length})</h3>
        <div class="bookmark-grid">
          ${bookmarkedCourses.map(course => createBookmarkCard(course, 'course')).join('')}
        </div>
      </div>
    `;
  }
  
  if (bookmarkedLabs.length > 0) {
    html += `
      <div class="bookmark-section">
        <h3><i class="fas fa-flask"></i> Labs (${bookmarkedLabs.length})</h3>
        <div class="bookmark-grid">
          ${bookmarkedLabs.map(lab => createBookmarkCard(lab, 'lab')).join('')}
        </div>
      </div>
    `;
  }
  
  content.innerHTML = html;
}

function createBookmarkCard(item, type) {
  const isLab = type === 'lab';
  const toggleFunction = isLab ? 'toggleLabBookmark' : 'toggleBookmark';
  const launchFunction = isLab ? 'launchLab' : 'launchCourse';
  
  return `
    <div class="bookmark-item-card">
      <div class="bookmark-item-header">
        <h4>${item.title}</h4>
        <span class="bookmark-type-badge ${type}">${isLab ? 'Lab' : 'Course'}</span>
      </div>
      <p class="bookmark-item-description">${item.description || 'No description'}</p>
      <div class="bookmark-item-meta">
        <span><i class="fas fa-clock"></i> ${item.duration || 'Self-paced'}</span>
        <span><i class="fas fa-signal"></i> ${item.difficulty || 'Beginner'}</span>
        ${!isLab ? `<span><i class="fas fa-star"></i> ${item.rating || '4.5'}/5</span>` : ''}
      </div>
      <div class="bookmark-item-actions">
        <button onclick="${launchFunction}('${item.id}')" class="launch-bookmark-btn">
          <i class="fas fa-external-link-alt"></i> Launch
        </button>
        <button onclick="${toggleFunction}('${item.id}'); displayBookmarkedItems(); updateBookmarkViewer();" 
                class="remove-bookmark-btn">
          <i class="fas fa-trash"></i> Remove
        </button>
      </div>
    </div>
  `;
}

function exportBookmarks(format) {
  const bookmarkedCourses = impactMojoAllCourses.filter(course => 
    impactMojoUserBookmarks.includes(course.id)
  );
  
  const bookmarkedLabs = (window.labs || []).filter(lab => 
    impactMojoUserLabBookmarks.includes(lab.id)
  );
  
  const allBookmarks = [
    ...bookmarkedCourses.map(course => ({ ...course, type: 'course' })),
    ...bookmarkedLabs.map(lab => ({ ...lab, type: 'lab' }))
  ];
  
  if (allBookmarks.length === 0) {
    showNotification('No bookmarks to export', 'warning');
    return;
  }
  
  if (format === 'csv') {
    exportAsCSV(allBookmarks);
  }
}

function exportAsCSV(bookmarks) {
  const headers = ['Title', 'Type', 'Description', 'Difficulty', 'Duration', 'Rating'];
  const csvContent = [
    headers.join(','),
    ...bookmarks.map(item => [
      `"${(item.title || '').replace(/"/g, '""')}"`,
      item.type || '',
      `"${(item.description || '').replace(/"/g, '""')}"`,
      item.difficulty || '',
      item.duration || '',
      item.rating || ''
    ].join(','))
  ].join('\n');
  
  const blob = new Blob([csvContent], { type: 'text/csv' });
  downloadFile(blob, `impactmojo-bookmarks-${new Date().toISOString().split('T')[0]}.csv`);
  showNotification('Bookmarks exported as CSV', 'success');
}

function downloadFile(blob, filename) {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function clearAllBookmarks() {
  if (confirm('Are you sure you want to clear all bookmarks? This action cannot be undone.')) {
    impactMojoUserBookmarks = [];
    impactMojoUserLabBookmarks = [];
    localStorage.setItem('impactMojoBookmarks', JSON.stringify([]));
    localStorage.setItem('impactMojoLabBookmarks', JSON.stringify([]));
    
    updateBookmarkViewer();
    updateAllBookmarkUI();
    updateAllLabBookmarkUI();
    displayBookmarkedItems();
    
    showNotification('All bookmarks cleared', 'info');
  }
}

function updateBookmarkViewer() {
  const bookmarkViewerBtn = document.getElementById('bookmarkViewerBtn');
  const totalBookmarks = impactMojoUserBookmarks.length + impactMojoUserLabBookmarks.length;
  
  if (bookmarkViewerBtn) {
    if (totalBookmarks > 0) {
      bookmarkViewerBtn.style.display = 'block';
      const countSpan = document.getElementById('bookmarkCount');
      if (countSpan) {
        countSpan.textContent = totalBookmarks;
      }
    } else {
      bookmarkViewerBtn.style.display = 'none';
    }
  }
}

function getCategoryColor(category) {
  const colors = {
    'General': '#6366f1',
    'Research & Data Analysis': '#3b82f6',
    'Gender & Justice': '#ec4899',
    'Economics & Development': '#059669',
    'Health & Environment': '#dc2626',
    'Governance & Policy': '#7c3aed',
    'Education & Communication': '#f59e0b',
    'Technology & Ethics': '#10b981'
  };
  return colors[category] || '#6366f1';
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
  setTimeout(() => {
    updateBookmarkViewer();
  }, 1000);
});

// Override existing bookmark functions to update viewer
const originalToggleBookmark = toggleBookmark;
toggleBookmark = function(courseId) {
  originalToggleBookmark(courseId);
  setTimeout(updateBookmarkViewer, 100);
};

const originalToggleLabBookmark = toggleLabBookmark;
toggleLabBookmark = function(labId) {
  originalToggleLabBookmark(labId);
  setTimeout(updateBookmarkViewer, 100);
};

console.log('✅ Missing functions added successfully!');
// ===== UPDATED CARD FUNCTIONS (OVERRIDE EXISTING ONES) =====

// New createCourseCard function with comparison checkboxes
function createCourseCard(course) {
  if (!course) return '';
  
  const category = course.category || 'General';
  const difficulty = course.difficulty || 'Beginner';
  const duration = course.duration || 'Self-paced';
  const rating = course.rating || 4.5;
  const description = course.description || 'No description available';
  const title = course.title || 'Untitled Course';
  const courseId = course.id;
  
  const categoryColor = getCategoryColor(category);
  
  return `
    <div class="course-card" data-course-id="${courseId}" style="border-left: 4px solid ${categoryColor}">
      <!-- Add comparison checkbox -->
      <label class="comparison-checkbox-label" title="Select for comparison">
        <input type="checkbox" 
                class="comparison-checkbox" 
                data-item-id="${courseId}"
                data-item-type="course"
                onchange="toggleComparison('${courseId}', 'course')">
      </label>
      
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

// New createLabCard function with comparison checkboxes
function createLabCard(lab) {
  if (!lab) return '';
  
  const category = lab.category || 'Interactive';
  const difficulty = lab.difficulty || 'Beginner';
  const duration = lab.duration || '30 min';
  const description = lab.description || 'Interactive lab experience';
  const title = lab.title || 'Untitled Lab';
  const labId = lab.id;
  const labType = lab.type || 'Simulation';
  
  return `
    <div class="lab-card" data-lab-id="${labId}">
      <!-- Add comparison checkbox -->
      <label class="comparison-checkbox-label" title="Select for comparison">
        <input type="checkbox" 
                class="comparison-checkbox" 
                data-item-id="${labId}"
                data-item-type="lab"
                onchange="toggleComparison('${labId}', 'lab')">
      </label>
      
      <div class="lab-card-header">
        <div class="lab-category">
          ${category}
        </div>
        <div class="lab-type-badge">${labType}</div>
        <div class="lab-actions">
          <button class="bookmark-btn" onclick="toggleLabBookmark('${labId}')" aria-label="Bookmark lab">
            <i class="far fa-bookmark"></i>
          </button>
        </div>
      </div>
      
      <div class="lab-content">
        <h3 class="lab-title">${title}</h3>
        <p class="lab-description">${description}</p>
        
        <div class="lab-meta">
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
        <button class="lab-launch-btn" onclick="launchLab('${labId}')">
          <i class="fas fa-flask"></i>
          Launch Lab
        </button>
      </div>
    </div>
  `;
}

console.log('✅ Updated card functions loaded!');
/* 
===== COMPLETE IMPACTMOJO JAVASCRIPT FIXES =====
Add this entire block to the END of your main.js file
This includes all fixes for navigation, tooltips, and mobile optimization
*/

// ===== OVERRIDE PROBLEMATIC centerNavigation FUNCTION =====
function centerNavigation() {
  console.log('🎯 Applying fixed navigation layout...');
  
  setTimeout(() => {
    const navContainer = document.querySelector('.navbar .container');
    const navMenu = document.querySelector('.nav-menu');
    const navActions = document.querySelector('.nav-actions');
    const header = document.querySelector('.header');
    
    const isMobile = window.innerWidth <= 768;
    
    if (isMobile) {
      // MOBILE: Prevent overlap by using relative positioning
      console.log('📱 Applying mobile layout...');
      
      if (header) {
        header.style.setProperty('position', 'relative', 'important');
        header.style.setProperty('z-index', '100', 'important');
        header.style.setProperty('margin-bottom', '1rem', 'important');
      }
      
      if (navContainer) {
        navContainer.style.setProperty('position', 'relative', 'important');
        navContainer.style.setProperty('flex-direction', 'column', 'important');
        navContainer.style.setProperty('justify-content', 'center', 'important');
        navContainer.style.setProperty('align-items', 'center', 'important');
        navContainer.style.setProperty('gap', '1.5rem', 'important');
        navContainer.style.setProperty('padding', '1rem', 'important');
        navContainer.style.setProperty('text-align', 'center', 'important');
      }
      
      if (navMenu) {
        navMenu.style.setProperty('position', 'relative', 'important');
        navMenu.style.setProperty('order', '1', 'important');
        navMenu.style.setProperty('width', '100%', 'important');
        navMenu.style.setProperty('justify-content', 'center', 'important');
        navMenu.style.setProperty('flex-direction', 'column', 'important');
        navMenu.style.setProperty('gap', '1rem', 'important');
        navMenu.style.setProperty('transform', 'none', 'important');
        navMenu.style.setProperty('top', 'auto', 'important');
        navMenu.style.setProperty('left', 'auto', 'important');
        navMenu.style.setProperty('right', 'auto', 'important');
      }
      
      if (navActions) {
        navActions.style.setProperty('position', 'relative', 'important');
        navActions.style.setProperty('order', '2', 'important');
        navActions.style.setProperty('width', '100%', 'important');
        navActions.style.setProperty('justify-content', 'center', 'important');
        navActions.style.setProperty('margin-left', '0', 'important');
        navActions.style.setProperty('margin-right', '0', 'important');
        navActions.style.setProperty('transform', 'none', 'important');
        navActions.style.setProperty('top', 'auto', 'important');
        navActions.style.setProperty('left', 'auto', 'important');
        navActions.style.setProperty('right', 'auto', 'important');
        navActions.style.setProperty('float', 'none', 'important');
      }
      
      // Ensure auth buttons container is properly positioned
      const authButtons = document.querySelector('.auth-buttons');
      if (authButtons) {
        authButtons.style.setProperty('position', 'relative', 'important');
        authButtons.style.setProperty('width', '100%', 'important');
        authButtons.style.setProperty('justify-content', 'center', 'important');
        authButtons.style.setProperty('gap', '1rem', 'important');
        authButtons.style.setProperty('transform', 'none', 'important');
        authButtons.style.setProperty('float', 'none', 'important');
      }
      
      // Add spacing to hero section to prevent overlap
      const hero = document.querySelector('.hero');
      if (hero) {
        hero.style.setProperty('margin-top', '1rem', 'important');
        hero.style.setProperty('clear', 'both', 'important');
      }
      
    } else {
      // DESKTOP: Shift left for tooltip space
      console.log('💻 Applying desktop layout...');
      
      if (header) {
        header.style.setProperty('position', 'sticky', 'important');
        header.style.setProperty('top', '0', 'important');
        header.style.setProperty('z-index', '100', 'important');
      }
      
      if (navContainer) {
        navContainer.style.setProperty('flex-direction', 'row', 'important');
        navContainer.style.setProperty('justify-content', 'flex-start', 'important');
        navContainer.style.setProperty('gap', '1.5rem', 'important');
        navContainer.style.setProperty('padding', '1.5rem 1rem 1.5rem 3rem', 'important');
      }
      
      if (navMenu) {
        navMenu.style.setProperty('order', '1', 'important');
        navMenu.style.setProperty('justify-content', 'flex-start', 'important');
        navMenu.style.setProperty('flex', '1', 'important');
        navMenu.style.setProperty('flex-direction', 'row', 'important');
      }
      
      if (navActions) {
        navActions.style.setProperty('position', 'static', 'important');
        navActions.style.setProperty('margin-left', 'auto', 'important');
        navActions.style.setProperty('margin-right', '2rem', 'important');
        navActions.style.setProperty('flex-shrink', '0', 'important');
      }
    }
    
    console.log('✅ Fixed navigation layout applied');
  }, 100);
}

// ===== MOBILE OVERLAP PREVENTION =====
function fixMobileOverlap() {
  if (window.innerWidth <= 768) {
    console.log('📱 Applying mobile overlap fix...');
    
    // Remove any floating or absolute positioned elements
    const problematicElements = document.querySelectorAll('.navbar, .navbar *, .nav-menu, .nav-menu *, .nav-actions, .nav-actions *, .auth-buttons, .auth-buttons *');
    
    problematicElements.forEach(element => {
      element.style.setProperty('position', 'relative', 'important');
      element.style.setProperty('float', 'none', 'important');
      element.style.setProperty('transform', 'none', 'important');
      element.style.setProperty('top', 'auto', 'important');
      element.style.setProperty('left', 'auto', 'important');
      element.style.setProperty('right', 'auto', 'important');
      element.style.setProperty('bottom', 'auto', 'important');
    });
    
    // Ensure proper spacing
    const hero = document.querySelector('.hero');
    if (hero) {
      hero.style.setProperty('clear', 'both', 'important');
      hero.style.setProperty('margin-top', '1rem', 'important');
    }
    
    // Ensure main content has proper spacing
    const mainContent = document.querySelector('main') || document.querySelector('.main-content');
    if (mainContent) {
      mainContent.style.setProperty('clear', 'both', 'important');
      mainContent.style.setProperty('margin-top', '1rem', 'important');
    }
    
    console.log('✅ Mobile overlap fix applied');
  }
}

// ===== RESPONSIVE WINDOW RESIZE HANDLER =====
window.addEventListener('resize', function() {
  clearTimeout(window.navResizeTimeout);
  window.navResizeTimeout = setTimeout(() => {
    centerNavigation();
    fixMobileOverlap();
  }, 250);
});

// ===== FORCE FIXES ON PAGE LOAD =====
window.addEventListener('load', function() {
  setTimeout(() => {
    centerNavigation();
    fixMobileOverlap();
  }, 500);
});

// Apply fixes immediately when script loads
document.addEventListener('DOMContentLoaded', function() {
  setTimeout(() => {
    centerNavigation();
    fixMobileOverlap();
  }, 1000);
});

// ===== TOOLTIP CSS INJECTION =====
const tooltipFixCSS = `
/* Enhanced tooltip positioning */
.auth-btn[title]:hover::after {
  content: attr(title) !important;
  position: absolute !important;
  top: 100% !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  margin-top: 8px !important;
  background: #1f2937 !important;
  color: white !important;
  padding: 0.75rem 1rem !important;
  border-radius: 0.5rem !important;
  font-size: 0.8rem !important;
  width: max-content !important;
  max-width: 280px !important;
  text-align: center !important;
  z-index: 10000 !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
  white-space: normal !important;
  font-family: 'Poppins', sans-serif !important;
  pointer-events: none !important;
}

.auth-btn[title]:hover::before {
  content: '' !important;
  position: absolute !important;
  top: 100% !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  margin-top: 3px !important;
  border: 5px solid transparent !important;
  border-bottom-color: #1f2937 !important;
  z-index: 10000 !important;
  pointer-events: none !important;
}

/* Ensure no clipping */
.header, .navbar, .navbar .container, .nav-actions, .auth-buttons {
  overflow: visible !important;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .auth-btn[title]:hover::after {
    max-width: 220px !important;
    font-size: 0.75rem !important;
  }
}

@media (max-width: 480px) {
  .auth-btn[title]:hover::after,
  .auth-btn[title]:hover::before {
    display: none !important;
  }
}
`;

// Inject tooltip CSS if not already present
if (!document.getElementById('tooltip-fix-styles')) {
  const style = document.createElement('style');
  style.id = 'tooltip-fix-styles';
  style.innerHTML = tooltipFixCSS;
  document.head.appendChild(style);
}

// ===== AUTH BUTTON VISIBILITY ENFORCEMENT =====
function ensureAuthButtonsVisible() {
  const authButtons = document.getElementById('authButtons');
  const userMenu = document.getElementById('userMenu');
  
  if (authButtons) {
    authButtons.style.setProperty('display', 'flex', 'important');
    authButtons.style.setProperty('visibility', 'visible', 'important');
    authButtons.style.setProperty('opacity', '1', 'important');
  }
  
  if (userMenu) {
    userMenu.style.setProperty('display', 'none', 'important');
  }
}

// Apply auth button fixes periodically
setInterval(ensureAuthButtonsVisible, 2000);

// ===== SCROLL BEHAVIOR IMPROVEMENTS =====
function improveScrollBehavior() {
  // Smooth scrolling for navigation links
  const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');
  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href && href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          const offset = 100; // Account for fixed header
          const targetPosition = target.offsetTop - offset;
          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });
        }
      }
    });
  });
}

// Apply scroll improvements
improveScrollBehavior();

// ===== MOBILE TOUCH IMPROVEMENTS =====
function improveMobileTouch() {
  if (window.innerWidth <= 768) {
    // Improve touch targets
    const buttons = document.querySelectorAll('button, .btn, .auth-btn, .cta-btn');
    buttons.forEach(button => {
      if (button.offsetHeight < 44) {
        button.style.setProperty('min-height', '44px', 'important');
        button.style.setProperty('padding', '0.7rem 1rem', 'important');
      }
    });
    
    // Improve form inputs
    const inputs = document.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
      input.style.setProperty('font-size', '16px', 'important');
      if (input.offsetHeight < 44) {
        input.style.setProperty('min-height', '44px', 'important');
      }
    });
  }
}

// Apply mobile touch improvements
improveMobileTouch();
window.addEventListener('resize', improveMobileTouch);

// ===== CONSOLE SUCCESS MESSAGE =====
console.log('✅ All ImpactMojo fixes loaded successfully!');
console.log('🎯 Navigation positioning fixed');
console.log('💬 Tooltip positioning fixed'); 
console.log('📱 Mobile optimization applied');
console.log('🚫 Mobile overlap prevention active');

// ===== END OF COMPLETE JAVASCRIPT FIXES =====