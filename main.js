// ImpactMojo Main JavaScript - FIXED VERSION (No Infinite Loops)
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
      <!-- Comparison checkbox -->
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
      <!-- Comparison checkbox -->
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
  updateBookmarkViewer();
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
  updateBookmarkViewer();
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
  console.log('🧪 Launching lab: ${labId}');
  showNotification('Lab launching...', 'info');
  
  const lab = window.labs?.find(l => l.id === labId);
  if (lab && lab.url) {
    window.open(lab.url, '_blank');
  } else {
    showNotification('Lab content coming soon!', 'info');
  }
}

// ===== COMPARISON FUNCTIONALITY =====
let selectedForComparison = [];
const MAX_COMPARISON_ITEMS = 4;

function showComparison() {
  showComparisonModal();
}

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

// ===== BOOKMARK VIEWER FUNCTIONALITY =====
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

// ===== MODAL MANAGEMENT =====
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'flex';
    modal.classList.add('active');
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    modal.classList.remove('active');
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

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', function() {
  console.log('🚀 Main JS DOM loaded');
  
  initializeThemeToggle();
  
  // Initialize mobile improvements
  improveMobileTouch();
  window.addEventListener('resize', improveMobileTouch);
  
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
  
  // Initialize bookmark viewer
  setTimeout(() => {
    updateBookmarkViewer();
  }, 1000);
});

console.log('✅ Main JS loaded successfully - NO INFINITE LOOPS!');
// ===== COMPARISON FAB BUTTON UPDATE =====
function updateComparisonUI() {
  // Update all comparison checkboxes
  document.querySelectorAll('.comparison-checkbox').forEach(checkbox => {
    const itemId = checkbox.dataset.itemId;
    const itemType = checkbox.dataset.itemType;
    const itemKey = `${itemType}-${itemId}`;
    checkbox.checked = selectedForComparison.some(item => item.key === itemKey);
  });
  
  // Update FAB button visibility - FIXED
  const compareFab = document.querySelector('.fab-btn.compare');
  if (compareFab) {
    if (selectedForComparison.length > 1) {
      compareFab.style.display = 'flex'; // Changed from 'block' to 'flex'
      compareFab.title = `Compare ${selectedForComparison.length} items`;
    } else {
      compareFab.style.display = 'none';
    }
  }
}

console.log('✅ Comparison FAB button update added!');
// ===== UPCOMING COURSES SECTION - CONSOLIDATED FIX =====

function fixUpcomingSectionFormatting() {
  console.log('🎨 Fixing upcoming courses section formatting...');
  
  // Find upcoming section by ID or class
  let upcomingSection = document.getElementById('upcoming') || 
  document.querySelector('.upcoming-section') ||
  document.querySelector('.upcoming-courses');
  
  // If not found, look for any element containing "development" text
  if (!upcomingSection) {
    const allElements = document.querySelectorAll('section, div, article');
    for (let element of allElements) {
      if (element.textContent && 
        (element.textContent.includes('New courses and labs currently in development') ||
          element.textContent.includes('development') ||
          element.textContent.includes('upcoming'))) {
            upcomingSection = element;
            break;
          }
    }
  }
  
  if (upcomingSection) {
    console.log('✅ Found upcoming section, applying formatting...');
    
    // Apply container styling
    upcomingSection.style.setProperty('padding', '3rem 2rem', 'important');
    upcomingSection.style.setProperty('background', 'var(--surface, #f8fafc)', 'important');
    upcomingSection.style.setProperty('border-radius', '1rem', 'important');
    upcomingSection.style.setProperty('margin', '2rem auto', 'important');
    upcomingSection.style.setProperty('max-width', '1000px', 'important');
    upcomingSection.style.setProperty('border', '1px solid var(--border-color, #e5e7eb)', 'important');
    upcomingSection.style.setProperty('box-shadow', '0 2px 4px rgba(0, 0, 0, 0.05)', 'important');
    upcomingSection.style.setProperty('text-align', 'center', 'important');
    
    // Fix headings inside
    const headings = upcomingSection.querySelectorAll('h1, h2, h3, h4, h5, h6');
    headings.forEach(heading => {
      heading.style.setProperty('font-size', '2.25rem', 'important');
      heading.style.setProperty('font-weight', '700', 'important');
      heading.style.setProperty('line-height', '1.3', 'important');
      heading.style.setProperty('text-align', 'center', 'important');
      heading.style.setProperty('margin', '0 0 1.5rem 0', 'important');
      heading.style.setProperty('padding', '0 1rem', 'important');
      heading.style.setProperty('color', 'var(--text-primary, #1f2937)', 'important');
      heading.style.setProperty('letter-spacing', '-0.025em', 'important');
    });
    
    // Fix paragraphs inside
    const paragraphs = upcomingSection.querySelectorAll('p');
    paragraphs.forEach(p => {
      p.style.setProperty('font-size', '1.125rem', 'important');
      p.style.setProperty('line-height', '1.7', 'important');
      p.style.setProperty('text-align', 'center', 'important');
      p.style.setProperty('margin', '0 auto 2rem auto', 'important');
      p.style.setProperty('padding', '0 1rem', 'important');
      p.style.setProperty('max-width', '700px', 'important');
      p.style.setProperty('color', 'var(--text-secondary, #6b7280)', 'important');
      
      // Special styling for development text
      if (p.textContent && 
        (p.textContent.includes('development') || 
          p.textContent.includes('New courses and labs currently'))) {
            p.style.setProperty('background', 'linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(59, 130, 246, 0.1))', 'important');
            p.style.setProperty('border', '1px solid rgba(99, 102, 241, 0.2)', 'important');
            p.style.setProperty('border-radius', '0.75rem', 'important');
            p.style.setProperty('padding', '1.5rem 2rem', 'important');
            p.style.setProperty('margin', '1rem auto', 'important');
            p.style.setProperty('position', 'relative', 'important');
            
            // Add construction icon
            if (!p.querySelector('.construction-icon')) {
              const icon = document.createElement('span');
              icon.className = 'construction-icon';
              icon.innerHTML = '🚧 ';
              icon.style.cssText = 'font-size: 1.5rem; margin-right: 0.5rem; display: inline-block;';
              p.insertBefore(icon, p.firstChild);
            }
          }
    });
    
    // Handle mobile responsiveness
    function applyMobileStyles() {
      if (window.innerWidth <= 768) {
        upcomingSection.style.setProperty('padding', '2rem 1rem', 'important');
        upcomingSection.style.setProperty('margin', '1rem', 'important');
        
        headings.forEach(heading => {
          heading.style.setProperty('font-size', '1.75rem', 'important');
          heading.style.setProperty('padding', '0 0.5rem', 'important');
        });
        
        paragraphs.forEach(p => {
          p.style.setProperty('font-size', '1rem', 'important');
          p.style.setProperty('padding', '0 0.5rem', 'important');
        });
      }
      
      if (window.innerWidth <= 480) {
        headings.forEach(heading => {
          heading.style.setProperty('font-size', '1.5rem', 'important');
        });
      }
    }
    
    // Apply mobile styles initially
    applyMobileStyles();
    
    // Apply mobile styles on resize
    window.addEventListener('resize', applyMobileStyles);
    
    console.log('✅ Upcoming section formatting applied successfully');
  } else {
    console.log('⚠️ Upcoming section not found');
    
    // Fallback: look for any text containing the specific phrase
    const allTextElements = document.querySelectorAll('*');
    for (let element of allTextElements) {
      if (element.textContent && 
        element.textContent.trim() === 'New courses and labs currently in development') {
          console.log('✅ Found specific development text, applying formatting...');
          
          // Get the parent container
          let container = element.closest('section') || element.closest('div') || element.parentElement;
          
          if (container) {
            container.style.setProperty('padding', '3rem 2rem', 'important');
            container.style.setProperty('background', 'var(--surface, #f8fafc)', 'important');
            container.style.setProperty('border-radius', '1rem', 'important');
            container.style.setProperty('margin', '2rem auto', 'important');
            container.style.setProperty('max-width', '800px', 'important');
            container.style.setProperty('text-align', 'center', 'important');
            container.style.setProperty('border', '1px solid var(--border-color, #e5e7eb)', 'important');
          }
          
          element.style.setProperty('font-size', '1.125rem', 'important');
          element.style.setProperty('line-height', '1.7', 'important');
          element.style.setProperty('color', 'var(--text-secondary, #6b7280)', 'important');
          element.style.setProperty('margin', '1rem auto', 'important');
          
          // Add icon
          if (!element.querySelector('.construction-icon')) {
            const icon = document.createElement('span');
            icon.className = 'construction-icon';
            icon.innerHTML = '🚧 ';
            icon.style.cssText = 'font-size: 1.5rem; margin-right: 0.5rem;';
            element.insertBefore(icon, element.firstChild);
          }
          
          break;
        }
    }
  }
}

// Apply the fix when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  setTimeout(fixUpcomingSectionFormatting, 1500);
});

// Apply the fix when window loads (in case content loads late)
window.addEventListener('load', function() {
  setTimeout(fixUpcomingSectionFormatting, 1000);
});

// Watch for content changes and reapply fix
let upcomingFixObserver = new MutationObserver(function(mutations) {
  let shouldReapply = false;
  
  mutations.forEach(function(mutation) {
    if (mutation.type === 'childList') {
      mutation.addedNodes.forEach(function(node) {
        if (node.nodeType === 1 && // Element node
          (node.textContent?.includes('development') || 
            node.textContent?.includes('upcoming') ||
            node.id?.includes('upcoming') ||
            node.className?.includes('upcoming'))) {
              shouldReapply = true;
            }
      });
    }
  });
  
  if (shouldReapply) {
    console.log('🔄 Content changed, reapplying upcoming section formatting...');
    setTimeout(fixUpcomingSectionFormatting, 500);
  }
});

// Start observing for content changes
upcomingFixObserver.observe(document.body, { 
  childList: true, 
  subtree: true 
});

console.log('🎨 Upcoming courses section formatting fix loaded and ready!');

// ===== END UPCOMING COURSES FIX =====
// ===== CLEAN COMPARISON FUNCTIONALITY =====
if (!window.selectedForComparison) {
  window.selectedForComparison = [];
}
if (!window.MAX_COMPARISON_ITEMS) {
  window.MAX_COMPARISON_ITEMS = 4;
}

function showComparison() {
  if (window.selectedForComparison.length < 2) {
    showNotification('Please select at least 2 items to compare', 'warning');
    return;
  }
  
  updateComparisonContent();
  openModal('comparisonModal');
}

function toggleComparison(itemId, itemType) {
  const itemKey = `${itemType}-${itemId}`;
  const index = window.selectedForComparison.findIndex(item => item.key === itemKey);
  
  if (index === -1) {
    if (window.selectedForComparison.length >= window.MAX_COMPARISON_ITEMS) {
      showNotification(`You can only compare up to ${window.MAX_COMPARISON_ITEMS} items at once`, 'warning');
      return false;
    }
    
    window.selectedForComparison.push({
      key: itemKey,
      id: itemId,
      type: itemType
    });
    
    showNotification(`Added to comparison (${window.selectedForComparison.length}/${window.MAX_COMPARISON_ITEMS})`, 'success');
  } else {
    window.selectedForComparison.splice(index, 1);
    showNotification('Removed from comparison', 'info');
  }
  
  updateComparisonUI();
  return true;
}

function updateComparisonUI() {
  // Update FAB button visibility
  const compareFab = document.querySelector('.fab-btn.compare');
  if (compareFab) {
    compareFab.style.display = window.selectedForComparison.length > 1 ? 'flex' : 'none';
  }
}

function updateComparisonContent() {
  const content = document.getElementById('comparisonContent');
  if (!content) return;
  
  if (window.selectedForComparison.length < 2) {
    content.innerHTML = `
      <div class="comparison-placeholder">
        <i class="fas fa-balance-scale"></i>
        <h3>Select items to compare</h3>
        <p>Use the checkboxes on course and lab cards to select items for comparison.</p>
      </div>
    `;
    return;
  }
  
  content.innerHTML = `
    <div class="comparison-stats">
      <span>Comparing ${window.selectedForComparison.length} items</span>
      <button class="clear-btn" onclick="clearComparison()">
        <i class="fas fa-times"></i> Clear Selection
      </button>
    </div>
    <p>Comparison table will load here when feature is fully implemented.</p>
  `;
}

function clearComparison() {
  window.selectedForComparison = [];
  updateComparisonUI();
  updateComparisonContent();
  showNotification('Comparison cleared', 'info');
}

// ===== MODAL FUNCTIONS =====
window.openModal = function(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'flex';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    console.log(`Opened modal: ${modalId}`);
  }
};

window.closeModal = function(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
    console.log(`Closed modal: ${modalId}`);
  }
};

// ===== INITIALIZATION =====
function initializeCleanFixes() {
  console.log('🚀 Initializing clean fixes...');
  
  // Hide comparison FAB initially
  const compareFab = document.querySelector('.fab-btn.compare');
  if (compareFab) {
    compareFab.style.display = 'none';
  }
  
  // Clean up any duplicate elements
  document.querySelectorAll('.fab-container').forEach((container, index) => {
    if (index > 0) {
      container.remove(); // Remove duplicate FAB containers
    }
  });
  
  console.log('✅ Clean fixes initialized!');
}

// Run initialization
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeCleanFixes);
} else {
  initializeCleanFixes();
}

console.log('🎉 Clean FAB and comparison system loaded!');