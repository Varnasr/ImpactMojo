// ===== IMPACTMOJO COMPLETE JAVASCRIPT - ALL FEATURES PRESERVED =====

// ===== GLOBAL VARIABLES =====
let currentUser = null;
let userBookmarks = [];
let userLabBookmarks = [];
let userNotes = '';
let selectedForComparison = [];
const MAX_COMPARISON_ITEMS = 4;

// Course data - will be loaded from course-data.js
let impactMojoAllCourses = [];
let impactMojoUserBookmarks = [];
let impactMojoUserLabBookmarks = [];

// ===== THEME MANAGEMENT =====
function initializeTheme() {
  const themeToggle = document.getElementById('themeToggle');
  const savedTheme = localStorage.getItem('theme') || 'light';
  
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
  
  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
  const themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
  }
}

// ===== AUTH STATE MANAGEMENT =====
function updateAuthState() {
  const authButtons = document.getElementById('authButtons');
  const userMenu = document.getElementById('userMenu');
  
  if (currentUser) {
    if (authButtons) authButtons.style.display = 'none';
    if (userMenu) {
      userMenu.style.display = 'flex';
      userMenu.classList.add('active');
      const userNameElement = userMenu.querySelector('.user-name');
      if (userNameElement) {
        userNameElement.textContent = currentUser.displayName || currentUser.email;
      }
      const userAvatar = userMenu.querySelector('.user-avatar');
      if (userAvatar) {
        userAvatar.textContent = (currentUser.displayName || currentUser.email).charAt(0).toUpperCase();
      }
    }
  } else {
    if (authButtons) authButtons.style.display = 'flex';
    if (userMenu) {
      userMenu.style.display = 'none';
      userMenu.classList.remove('active');
    }
  }
}

// ===== USER DROPDOWN MANAGEMENT =====
function toggleUserDropdown() {
  const dropdown = document.getElementById('userDropdown');
  if (dropdown) {
    dropdown.classList.toggle('hidden');
  }
}

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
  const userMenu = document.getElementById('userMenu');
  const dropdown = document.getElementById('userDropdown');
  
  if (userMenu && dropdown && !userMenu.contains(event.target)) {
    dropdown.classList.add('hidden');
  }
});

// ===== COURSE DISPLAY FUNCTIONS =====
function displayCourses() {
  const container = document.getElementById('coursesContainer');
  
  if (!container) {
    console.log('ℹ️ Courses container not found, skipping course display');
    return;
  }
  
  if (!impactMojoAllCourses || impactMojoAllCourses.length === 0) {
    container.innerHTML = '<div class="no-results" style="text-align: center; padding: 2rem; color: var(--text-secondary);">Courses are loading...</div>';
    return;
  }

  container.innerHTML = impactMojoAllCourses.map(course => createCourseCard(course)).join('');
  updateBookmarkUI();
  updateComparisonUI();
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
      
      <!-- Bookmark button -->
      <button class="bookmark-btn" data-course-id="${courseId}" onclick="toggleBookmark('${courseId}')" aria-label="Bookmark course">
        <i class="far fa-bookmark"></i>
      </button>
      
      <div class="course-card-header">
        <div class="course-category" style="background-color: ${categoryColor}20; color: ${categoryColor}">
          ${category}
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

function getCategoryColor(category) {
  const colors = {
    'Data Analysis': '#3b82f6',
    'Development': '#10b981',
    'Research': '#8b5cf6',
    'Economics': '#f59e0b',
    'Policy': '#ef4444',
    'Statistics': '#06b6d4',
    'General': '#6b7280'
  };
  return colors[category] || colors['General'];
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
  updateLabBookmarkUI();
  updateComparisonUI();
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
      
      <!-- Bookmark button -->
      <button class="bookmark-btn" data-lab-id="${labId}" onclick="toggleLabBookmark('${labId}')" aria-label="Bookmark lab">
        <i class="far fa-bookmark"></i>
      </button>
      
      <div class="lab-card-header">
        <div class="lab-category">
          ${category}
        </div>
        <div class="lab-type">
          ${labType}
        </div>
      </div>
      
      <div class="lab-content">
        <h3 class="lab-title">${title}</h3>
        <p class="lab-description">${description}</p>
        
        <div class="course-meta">
          <span class="course-duration">
            <i class="fas fa-clock"></i>
            ${duration}
          </span>
          <span class="course-difficulty difficulty-${difficulty.toLowerCase()}">
            ${difficulty}
          </span>
        </div>
      </div>
      
      <div class="lab-card-footer">
        <button class="launch-btn" onclick="startLab('${labId}')">
          <i class="fas fa-flask"></i>
          Start Lab
        </button>
      </div>
    </div>
  `;
}

// ===== BOOKMARK FUNCTIONALITY =====
async function toggleBookmark(courseId) {
  if (!currentUser) {
    showNotification('Please log in to bookmark courses', 'error');
    showLoginModal();
    return;
  }
  
  try {
    const userRef = window.doc(window.db, 'users', currentUser.uid);
    
    if (impactMojoUserBookmarks.includes(courseId)) {
      // Remove bookmark
      await window.updateDoc(userRef, {
        bookmarks: window.arrayRemove(courseId)
      });
      impactMojoUserBookmarks = impactMojoUserBookmarks.filter(id => id !== courseId);
      showNotification('Bookmark removed', 'success');
    } else {
      // Add bookmark
      await window.updateDoc(userRef, {
        bookmarks: window.arrayUnion(courseId)
      });
      impactMojoUserBookmarks.push(courseId);
      showNotification('Course bookmarked!', 'success');
    }
    
    updateBookmarkUI();
    updateBookmarkCount();
  } catch (error) {
    console.error('Bookmark error:', error);
    showNotification('Error updating bookmark', 'error');
  }
}

async function toggleLabBookmark(labId) {
  if (!currentUser) {
    showNotification('Please log in to bookmark labs', 'error');
    showLoginModal();
    return;
  }
  
  try {
    const userRef = window.doc(window.db, 'users', currentUser.uid);
    
    if (impactMojoUserLabBookmarks.includes(labId)) {
      // Remove bookmark
      await window.updateDoc(userRef, {
        labBookmarks: window.arrayRemove(labId)
      });
      impactMojoUserLabBookmarks = impactMojoUserLabBookmarks.filter(id => id !== labId);
      showNotification('Lab bookmark removed', 'success');
    } else {
      // Add bookmark
      await window.updateDoc(userRef, {
        labBookmarks: window.arrayUnion(labId)
      });
      impactMojoUserLabBookmarks.push(labId);
      showNotification('Lab bookmarked!', 'success');
    }
    
    updateLabBookmarkUI();
    updateBookmarkCount();
  } catch (error) {
    console.error('Lab bookmark error:', error);
    showNotification('Error updating lab bookmark', 'error');
  }
}

function updateBookmarkUI() {
  const bookmarkButtons = document.querySelectorAll('.bookmark-btn[data-course-id]');
  bookmarkButtons.forEach(btn => {
    const courseId = btn.dataset.courseId;
    if (impactMojoUserBookmarks.includes(courseId)) {
      btn.classList.add('bookmarked');
      btn.innerHTML = '<i class="fas fa-bookmark"></i>';
    } else {
      btn.classList.remove('bookmarked');
      btn.innerHTML = '<i class="far fa-bookmark"></i>';
    }
  });
}

function updateLabBookmarkUI() {
  const bookmarkButtons = document.querySelectorAll('.bookmark-btn[data-lab-id]');
  bookmarkButtons.forEach(btn => {
    const labId = btn.dataset.labId;
    if (impactMojoUserLabBookmarks.includes(labId)) {
      btn.classList.add('bookmarked');
      btn.innerHTML = '<i class="fas fa-bookmark"></i>';
    } else {
      btn.classList.remove('bookmarked');
      btn.innerHTML = '<i class="far fa-bookmark"></i>';
    }
  });
}

function updateBookmarkCount() {
  const bookmarkCountElement = document.querySelector('.bookmark-viewer-btn span');
  if (bookmarkCountElement) {
    const totalBookmarks = impactMojoUserBookmarks.length + impactMojoUserLabBookmarks.length;
    bookmarkCountElement.textContent = totalBookmarks;
    bookmarkCountElement.style.display = totalBookmarks > 0 ? 'flex' : 'none';
  }
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
  const launchFunction = isLab ? 'startLab' : 'launchCourse';
  
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
        ${!isLab ? `<span><i class="fas fa-star"></i> ${(item.rating || 4.5).toFixed(1)}</span>` : ''}
      </div>
      <div class="bookmark-item-actions">
        <button onclick="${launchFunction}('${item.id}')" class="launch-bookmark-btn">
          <i class="fas fa-${isLab ? 'flask' : 'play'}"></i> Launch
        </button>
        <button onclick="${toggleFunction}('${item.id}')" class="remove-bookmark-btn">
          <i class="fas fa-trash"></i>
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
  
  if (format === 'csv') {
    const csvContent = generateBookmarkCSV(bookmarkedCourses, bookmarkedLabs);
    downloadFile(csvContent, 'impactmojo-bookmarks.csv', 'text/csv');
    showNotification('Bookmarks exported successfully!', 'success');
  }
}

function generateBookmarkCSV(courses, labs) {
  let csv = 'Type,Title,Description,Category,Difficulty,Duration,Rating\n';
  
  courses.forEach(course => {
    csv += `Course,"${course.title}","${course.description}","${course.category}","${course.difficulty}","${course.duration}","${course.rating}"\n`;
  });
  
  labs.forEach(lab => {
    csv += `Lab,"${lab.title}","${lab.description}","${lab.category}","${lab.difficulty}","${lab.duration}","N/A"\n`;
  });
  
  return csv;
}

function downloadFile(content, filename, mimeType) {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

async function clearAllBookmarks() {
  if (!currentUser) return;
  
  if (!confirm('Are you sure you want to clear all bookmarks? This action cannot be undone.')) {
    return;
  }
  
  try {
    const userRef = window.doc(window.db, 'users', currentUser.uid);
    await window.updateDoc(userRef, {
      bookmarks: [],
      labBookmarks: []
    });
    
    impactMojoUserBookmarks = [];
    impactMojoUserLabBookmarks = [];
    
    updateBookmarkUI();
    updateLabBookmarkUI();
    updateBookmarkCount();
    displayBookmarkedItems();
    
    showNotification('All bookmarks cleared', 'success');
  } catch (error) {
    console.error('Error clearing bookmarks:', error);
    showNotification('Error clearing bookmarks', 'error');
  }
}

// ===== COMPARISON FUNCTIONALITY =====
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
    compareFab.style.display = selectedForComparison.length > 1 ? 'flex' : 'none';
  }
}

function showComparison() {
  showComparisonModal();
}

function showComparisonModal() {
  if (selectedForComparison.length < 2) {
    showNotification('Please select at least 2 items to compare', 'warning');
    return;
  }
  
  if (!document.getElementById('comparisonModal')) {
    createComparisonModal();
  }
  
  updateComparisonContent();
  openModal('comparisonModal');
}

function createComparisonModal() {
  const modal = document.createElement('div');
  modal.id = 'comparisonModal';
  modal.className = 'modal';
  modal.innerHTML = `
    <div class="modal-content large">
      <span class="close" onclick="closeModal('comparisonModal')">&times;</span>
      <div id="comparisonContent">
        <!-- Comparison content will be displayed here -->
      </div>
    </div>
  `;
  document.body.appendChild(modal);
}

function updateComparisonContent() {
  const content = document.getElementById('comparisonContent');
  if (!content) return;
  
  const items = selectedForComparison.map(item => {
    if (item.type === 'course') {
      return impactMojoAllCourses.find(course => course.id === item.id);
    } else {
      return (window.labs || []).find(lab => lab.id === item.id);
    }
  }).filter(Boolean);
  
  if (items.length === 0) {
    content.innerHTML = '<div class="comparison-placeholder"><i class="fas fa-balance-scale"></i><h3>No items to compare</h3></div>';
    return;
  }
  
  content.innerHTML = `
    <div class="comparison-header">
      <h2><i class="fas fa-balance-scale"></i> Comparison</h2>
      <div class="comparison-stats">
        <span>Comparing ${items.length} items</span>
        <button onclick="clearComparison()" class="btn secondary">
          <i class="fas fa-trash"></i> Clear All
        </button>
      </div>
    </div>
    
    <div class="comparison-table-container">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Feature</th>
            ${items.map((item, index) => `
              <th>
                ${item.title}
                <br><small>${selectedForComparison[index].type}</small>
              </th>
            `).join('')}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Description</td>
            ${items.map(item => `<td>${item.description || 'N/A'}</td>`).join('')}
          </tr>
          <tr>
            <td>Category</td>
            ${items.map(item => `<td>${item.category || 'N/A'}</td>`).join('')}
          </tr>
          <tr>
            <td>Difficulty</td>
            ${items.map(item => `<td><span class="difficulty-badge ${(item.difficulty || 'beginner').toLowerCase()}">${item.difficulty || 'Beginner'}</span></td>`).join('')}
          </tr>
          <tr>
            <td>Duration</td>
            ${items.map(item => `<td>${item.duration || 'N/A'}</td>`).join('')}
          </tr>
          <tr>
            <td>Rating</td>
            ${items.map(item => `<td>${item.rating ? item.rating.toFixed(1) + ' ★' : 'N/A'}</td>`).join('')}
          </tr>
          <tr>
            <td>Action</td>
            ${items.map((item, index) => `
              <td>
                <button onclick="${selectedForComparison[index].type === 'course' ? 'launchCourse' : 'startLab'}('${item.id}')" 
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

// ===== SEARCH AND FILTER FUNCTIONALITY =====
function initializeSearch() {
  const searchInput = document.getElementById('searchInput');
  const searchBtn = document.getElementById('searchBtn');
  const categoryFilter = document.getElementById('categoryFilter');
  const difficultyFilter = document.getElementById('difficultyFilter');
  const durationFilter = document.getElementById('durationFilter');
  
  if (searchBtn) {
    searchBtn.addEventListener('click', performSearch);
  }
  
  if (searchInput) {
    searchInput.addEventListener('keypress', function(e) {
      if (e.key === 'Enter') {
        performSearch();
      }
    });
  }
  
  if (categoryFilter) {
    categoryFilter.addEventListener('change', performSearch);
  }
  
  if (difficultyFilter) {
    difficultyFilter.addEventListener('change', performSearch);
  }
  
  if (durationFilter) {
    durationFilter.addEventListener('change', performSearch);
  }
}

function performSearch() {
  const query = document.getElementById('searchInput')?.value.toLowerCase() || '';
  const category = document.getElementById('categoryFilter')?.value || 'all';
  const difficulty = document.getElementById('difficultyFilter')?.value || 'all';
  const duration = document.getElementById('durationFilter')?.value || 'all';
  
  filterAndDisplayContent(query, category, difficulty, duration);
}

function filterAndDisplayContent(query, category, difficulty, duration) {
  // Filter courses
  const filteredCourses = impactMojoAllCourses.filter(course => {
    const matchesQuery = query === '' || 
      course.title.toLowerCase().includes(query) ||
      course.description.toLowerCase().includes(query) ||
      (course.tags && course.tags.some(tag => tag.toLowerCase().includes(query)));
    
    const matchesCategory = category === 'all' || course.category === category;
    const matchesDifficulty = difficulty === 'all' || course.difficulty === difficulty;
    const matchesDuration = duration === 'all' || course.duration === duration;
    
    return matchesQuery && matchesCategory && matchesDifficulty && matchesDuration;
  });
  
  // Filter labs
  const filteredLabs = (window.labs || []).filter(lab => {
    const matchesQuery = query === '' || 
      lab.title.toLowerCase().includes(query) ||
      lab.description.toLowerCase().includes(query);
    
    const matchesCategory = category === 'all' || lab.category === category;
    const matchesDifficulty = difficulty === 'all' || lab.difficulty === difficulty;
    const matchesDuration = duration === 'all' || lab.duration === duration;
    
    return matchesQuery && matchesCategory && matchesDifficulty && matchesDuration;
  });
  
  displayFilteredCourses(filteredCourses);
  displayFilteredLabs(filteredLabs);
  
  // Update result count
  const totalResults = filteredCourses.length + filteredLabs.length;
  updateResultCount(totalResults);
}

function displayFilteredCourses(courses) {
  const container = document.getElementById('coursesContainer');
  if (!container) return;
  
  if (courses.length === 0) {
    container.innerHTML = '<div class="no-results" style="text-align: center; padding: 2rem; color: var(--text-secondary);">No courses found matching your criteria.</div>';
    return;
  }
  
  container.innerHTML = courses.map(course => createCourseCard(course)).join('');
  updateBookmarkUI();
  updateComparisonUI();
}

function displayFilteredLabs(labs) {
  const container = document.getElementById('labsContainer');
  if (!container) return;
  
  if (labs.length === 0) {
    container.innerHTML = '<div class="no-results" style="text-align: center; padding: 2rem; color: var(--text-secondary);">No labs found matching your criteria.</div>';
    return;
  }
  
  container.innerHTML = labs.map(lab => createLabCard(lab)).join('');
  updateLabBookmarkUI();
  updateComparisonUI();
}

function updateResultCount(count) {
  const resultElement = document.getElementById('searchResults');
  if (resultElement) {
    resultElement.textContent = `${count} result${count !== 1 ? 's' : ''} found`;
  }
}

// ===== ACTION HANDLERS =====
function launchCourse(courseId) {
  if (!currentUser) {
    showNotification('Please sign up or log in to access courses.', 'error');
    showLoginModal();
    return;
  }
  
  const course = impactMojoAllCourses.find(c => c.id === courseId);
  if (course) {
    console.log(`Launching course: ${course.title}`);
    showNotification(`Launching: ${course.title}`, 'success');
    // Add actual course launch logic here
    // For example: window.open(course.url, '_blank');
  }
}

function startLab(labId) {
  if (!currentUser) {
    showNotification('Please sign up or log in to access labs.', 'error');
    showLoginModal();
    return;
  }
  
  const lab = (window.labs || []).find(l => l.id === labId);
  if (lab) {
    console.log(`Starting lab: ${lab.title}`);
    showNotification(`Starting: ${lab.title}`, 'success');
    // Add actual lab start logic here
  }
}

function launchLab(labId) {
  startLab(labId); // Alias for compatibility
}

// ===== USER DASHBOARD FUNCTIONS =====
function showDashboard() {
  if (!currentUser) {
    showNotification('Please log in to view dashboard', 'error');
    showLoginModal();
    return;
  }
  
  showNotification('Dashboard feature coming soon! Track your progress and manage your learning path.', 'info');
}

function showBookmarks() {
  if (!currentUser) {
    showNotification('Please log in to view bookmarks', 'error');
    showLoginModal();
    return;
  }
  
  showBookmarkModal();
}

function showProfile() {
  if (!currentUser) {
    showNotification('Please log in to view profile', 'error');
    showLoginModal();
    return;
  }
  
  const profileInfo = `
    Name: ${currentUser.displayName || 'Not provided'}
    Email: ${currentUser.email}
    Joined: ${currentUser.metadata.creationTime ? new Date(currentUser.metadata.creationTime).toLocaleDateString() : 'Unknown'}
  `;
  
  showNotification(`Profile Info:\n${profileInfo}`, 'info');
}

// ===== MODAL MANAGEMENT =====
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add('active');
    modal.style.display = 'flex';
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('active');
    modal.style.display = 'none';
  }
}

function showLoginModal() {
  if (typeof window.showLoginModal === 'function') {
    window.showLoginModal();
  } else {
    showNotification('Please log in to continue', 'info');
  }
}

// ===== NOTIFICATION SYSTEM =====
function showNotification(message, type = 'info') {
  // Remove existing notifications
  const existingNotifications = document.querySelectorAll('.notification');
  existingNotifications.forEach(notification => notification.remove());
  
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.textContent = message;
  
  document.body.appendChild(notification);
  
  // Show notification
  setTimeout(() => {
    notification.classList.add('show');
  }, 100);
  
  // Hide notification after 4 seconds
  setTimeout(() => {
    notification.classList.remove('show');
    setTimeout(() => {
      if (notification.parentNode) {
        notification.parentNode.removeChild(notification);
      }
    }, 300);
  }, 4000);
}

// ===== NAVIGATION HELPERS =====
function scrollToSection(sectionId) {
  const element = document.getElementById(sectionId);
  if (element) {
    element.scrollIntoView({ 
      behavior: 'smooth',
      block: 'start'
    });
  }
}

// ===== LOAD USER DATA FROM FIRESTORE =====
async function loadUserData() {
  if (!currentUser) return;
  
  try {
    const userDoc = await window.getDoc(window.doc(window.db, 'users', currentUser.uid));
    if (userDoc.exists()) {
      const userData = userDoc.data();
      impactMojoUserBookmarks = userData.bookmarks || [];
      impactMojoUserLabBookmarks = userData.labBookmarks || [];
      userNotes = userData.notes || '';
      
      // Update UI to reflect bookmarks
      updateBookmarkUI();
      updateLabBookmarkUI();
      updateBookmarkCount();
    }
  } catch (error) {
    console.error('Error loading user data:', error);
  }
}

// ===== SIMPLE RESPONSIVE HANDLER (NO CONFLICTING POSITIONING) =====
function handleResponsiveNavigation() {
  const isMobile = window.innerWidth <= 768;
  const navMenu = document.querySelector('.nav-menu');
  const navActions = document.querySelector('.nav-actions');
  
  // Simple responsive adjustments without forcing styles
  if (isMobile) {
    if (navMenu) navMenu.classList.add('mobile-nav');
    if (navActions) navActions.classList.add('mobile-actions');
  } else {
    if (navMenu) navMenu.classList.remove('mobile-nav');
    if (navActions) navActions.classList.remove('mobile-actions');
  }
}

// ===== EVENT LISTENERS =====
window.addEventListener('resize', function() {
  clearTimeout(window.resizeTimeout);
  window.resizeTimeout = setTimeout(handleResponsiveNavigation, 150);
});

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', function() {
  console.log('🚀 ImpactMojo initialized');
  
  // Initialize core features
  initializeTheme();
  initializeSearch();
  updateAuthState();
  handleResponsiveNavigation();
  
  // Load content if containers exist
  if (document.getElementById('coursesContainer')) {
    displayCourses();
  }
  
  if (document.getElementById('labsContainer')) {
    displayLabs();
  }
  
  // Initialize bookmark count
  updateBookmarkCount();
  
  console.log('✅ ImpactMojo ready');
});

// ===== GLOBAL FUNCTIONS FOR HTML ONCLICK EVENTS =====
window.scrollToSection = scrollToSection;
window.launchCourse = launchCourse;
window.startLab = startLab;
window.launchLab = launchLab;
window.toggleBookmark = toggleBookmark;
window.toggleLabBookmark = toggleLabBookmark;
window.toggleComparison = toggleComparison;
window.showComparison = showComparison;
window.showBookmarkModal = showBookmarkModal;
window.showDashboard = showDashboard;
window.showBookmarks = showBookmarks;
window.showProfile = showProfile;
window.toggleUserDropdown = toggleUserDropdown;
window.openModal = openModal;
window.closeModal = closeModal;
window.exportBookmarks = exportBookmarks;
window.clearAllBookmarks = clearAllBookmarks;
window.clearComparison = clearComparison;
window.performSearch = performSearch;