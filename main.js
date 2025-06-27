// ImpactMojo Main JavaScript - CLEAN VERSION (Upcoming Section Fixed)
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
  let backgroundColor, textColor;
  switch(type) {
    case 'success': backgroundColor = '#10b981'; textColor = '#ffffff'; break;
    case 'warning': backgroundColor = '#f59e0b'; textColor = '#ffffff'; break;
    case 'error': backgroundColor = '#ef4444'; textColor = '#ffffff'; break;
    default: backgroundColor = '#3b82f6'; textColor = '#ffffff';
  }
  
  notification.style.cssText = `
    position: fixed !important; top: 20px !important; right: 20px !important;
    background: ${backgroundColor} !important; color: ${textColor} !important;
    padding: 1rem 1.5rem !important; border-radius: 8px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important; z-index: 10000 !important;
    font-weight: 500 !important; font-size: 14px !important; max-width: 300px !important;
  `;
  
  notification.innerHTML = `
    <span style="color: ${textColor} !important;">${message}</span>
    <button onclick="this.parentElement.remove()" style="
      background: rgba(255,255,255,0.2) !important; border: none !important;
      color: ${textColor} !important; padding: 4px 8px !important; 
      border-radius: 4px !important; cursor: pointer !important; margin-left: 8px !important;
    ">✕</button>
  `;
  
  document.body.appendChild(notification);
  setTimeout(() => notification.remove(), 5000);
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

// ===== UPCOMING COURSES - CLEAN NEW IMPLEMENTATION =====
function displayUpcomingCourses() {
  console.log('🚀 Displaying upcoming courses with clean implementation...');
  
  const upcomingData = [
    {
      id: 'upcoming-tech-for-all',
      title: 'Technology for All',
      category: 'Technology & Ethics',
      difficulty: 'Intermediate',
      duration: '6 weeks',
      rating: 0,
      description: 'Exploring how technology can be designed and implemented to serve all communities equitably, with focus on accessibility, digital divides, and inclusive innovation.',
      status: 'Coming Soon',
      expectedDate: 'Fall 2025'
    },
    {
      id: 'upcoming-climate-resilience',
      title: 'Climate Resilience Strategies',
      category: 'Health & Environment', 
      difficulty: 'Advanced',
      duration: '8 weeks',
      rating: 0,
      description: 'Advanced frameworks for building community and institutional resilience against climate change impacts in South Asian contexts.',
      status: 'In Development',
      expectedDate: 'Winter 2025'
    },
    {
      id: 'upcoming-digital-governance',
      title: 'Digital Governance in Practice',
      category: 'Governance & Policy',
      difficulty: 'Intermediate',
      duration: '5 weeks', 
      rating: 0,
      description: 'How digital technologies are transforming governance structures and citizen participation in developing countries.',
      status: 'Coming Soon',
      expectedDate: 'Spring 2026'
    }
  ];
  
  // Find upcoming section container
  let upcomingContainer = document.getElementById('upcomingCoursesContainer') || 
                         document.querySelector('.upcoming-courses-grid') ||
                         document.querySelector('#upcoming .courses-grid');
  
  if (!upcomingContainer) {
    // Create container if it doesn't exist
    const upcomingSection = document.getElementById('upcoming') || document.querySelector('.upcoming-section');
    if (upcomingSection) {
      const existingGrid = upcomingSection.querySelector('.courses-grid');
      if (existingGrid) {
        upcomingContainer = existingGrid;
      } else {
        upcomingContainer = document.createElement('div');
        upcomingContainer.className = 'courses-grid';
        upcomingContainer.id = 'upcomingCoursesContainer';
        upcomingSection.appendChild(upcomingContainer);
      }
    }
  }
  
  if (upcomingContainer) {
    upcomingContainer.innerHTML = upcomingData.map(course => createUpcomingCourseCard(course)).join('');
    console.log('✅ Upcoming courses displayed successfully');
  } else {
    console.log('⚠️ No upcoming courses container found');
  }
}

function createUpcomingCourseCard(course) {
  const category = course.category || 'General';
  const difficulty = course.difficulty || 'Beginner';
  const duration = course.duration || 'Self-paced';
  const description = course.description || 'No description available';
  const title = course.title || 'Untitled Course';
  const courseId = course.id;
  const status = course.status || 'Coming Soon';
  const expectedDate = course.expectedDate || 'TBA';
  
  const categoryColor = getCategoryColor(category);
  
  return `
    <div class="course-card upcoming-course" data-course-id="${courseId}" style="border-left: 4px solid ${categoryColor}; position: relative;">
      <!-- Coming Soon Badge -->
      <div class="upcoming-badge" style="
        position: absolute; top: 1rem; right: 1rem; 
        background: linear-gradient(135deg, #6366f1, #8b5cf6); 
        color: white; padding: 0.25rem 0.75rem; border-radius: 1rem; 
        font-size: 0.75rem; font-weight: 600; z-index: 10;
      ">
        ${status}
      </div>
      
      <div class="course-card-header">
        <div class="course-category" style="background-color: ${categoryColor}20; color: ${categoryColor}">
          ${category}
        </div>
        <div class="course-actions">
          <button class="upcoming-notify-btn" onclick="notifyWhenReady('${courseId}')" aria-label="Notify when ready" style="
            background: transparent; border: 2px solid #6366f1; color: #6366f1; 
            padding: 0.5rem; border-radius: 0.5rem; cursor: pointer;
          ">
            <i class="fas fa-bell"></i>
          </button>
        </div>
      </div>
      
      <div class="course-content">
        <h3 class="course-title">${title}</h3>
        <p class="course-description">${description}</p>
        
        <div class="course-meta">
          <span class="course-duration">
            <i class="fas fa-clock"></i>
            ${duration}
          </span>
          <span class="course-difficulty difficulty-${difficulty.toLowerCase()}">
            ${difficulty}
          </span>
          <span class="expected-date" style="color: #6366f1;">
            <i class="fas fa-calendar"></i>
            ${expectedDate}
          </span>
        </div>
      </div>
      
      <div class="course-card-footer">
        <button class="launch-btn upcoming-disabled" onclick="notifyWhenReady('${courseId}')" style="
          background: #e5e7eb; color: #6b7280; cursor: not-allowed; opacity: 0.7;
        ">
          <i class="fas fa-hourglass-half"></i>
          Coming Soon
        </button>
      </div>
    </div>
  `;
}

function notifyWhenReady(courseId) {
  showNotification('We\'ll notify you when this course is ready!', 'info');
  // Here you could implement actual email notification signup
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
    compareFab.style.display = selectedForComparison.length > 1 ? 'flex' : 'none';
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
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
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
    displayUpcomingCourses(); // Display upcoming courses
  } else {
    console.log('⏳ Waiting for course data...');
    window.addEventListener('dataLoaded', function() {
      console.log('📊 Data loaded event received');
      initializeCourses();
      displayPopularCourses();
      displayLabs();
      displayUpcomingCourses(); // Display upcoming courses
    });
  }
  
  // Initialize bookmark viewer
  setTimeout(() => {
    updateBookmarkViewer();
    displayUpcomingCourses(); // Extra call to ensure upcoming courses load
  }, 1000);
  
  // Extra initialization for upcoming courses
  setTimeout(displayUpcomingCourses, 2000);
});

// Make functions globally available
window.openModal = openModal;
window.closeModal = closeModal;
window.showNotification = showNotification;

console.log('✅ Clean Main JS loaded successfully!');
// ===== IMPACTMOJO RESTORATION JAVASCRIPT - ADD THIS AT THE END =====

// THEME TOGGLE RESTORATION
function toggleTheme() {
  console.log('🎨 Toggling theme...');
  
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  if (themeIcon) {
    themeIcon.className = newTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
  
  showNotification(`Switched to ${newTheme} mode`, 'success');
}

// INITIALIZE THEME ON LOAD
function initializeTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  document.documentElement.setAttribute('data-theme', savedTheme);
  
  if (themeIcon) {
    themeIcon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
}

// COMPARISON FUNCTIONALITY RESTORATION
window.selectedForComparison = window.selectedForComparison || [];
window.MAX_COMPARISON_ITEMS = 4;

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
  const compareFab = document.querySelector('.fab-btn.compare');
  if (compareFab) {
    compareFab.style.display = window.selectedForComparison.length > 1 ? 'flex' : 'none';
  }
  
  // Update checkboxes
  document.querySelectorAll('.comparison-checkbox').forEach(checkbox => {
    const itemId = checkbox.dataset.itemId;
    const itemType = checkbox.dataset.itemType;
    const itemKey = `${itemType}-${itemId}`;
    checkbox.checked = window.selectedForComparison.some(item => item.key === itemKey);
  });
}

function updateComparisonContent() {
  const content = document.getElementById('comparisonContent');
  if (!content) return;
  
  if (window.selectedForComparison.length < 2) {
    content.innerHTML = `
      <div class="comparison-placeholder">
        <i class="fas fa-balance-scale"></i>
        <h3>Select items to compare</h3>
        <p>Use the checkboxes on course and lab cards to select items for comparison. You can compare 2-4 items at once.</p>
      </div>
    `;
    return;
  }
  
  // Get actual course/lab data and generate rich comparison table
  const items = window.selectedForComparison.map(item => {
    if (item.type === 'course') {
      return window.courses?.find(c => c.id === item.id) || 
      impactMojoAllCourses?.find(c => c.id === item.id);
    } else if (item.type === 'lab') {
      return window.labs?.find(l => l.id === item.id);
    }
    return null;
  }).filter(Boolean);
  
  if (items.length === 0) {
    content.innerHTML = '<p>Error loading comparison data.</p>';
    return;
  }
  
  // Generate rich comparison table
  const comparisonHTML = generateRichComparisonTable(items);
  
  content.innerHTML = `
    <div class="comparison-header">
      <div class="comparison-stats">
        <span><i class="fas fa-balance-scale"></i> Comparing ${items.length} item${items.length > 1 ? 's' : ''}</span>
        <button class="btn-secondary" onclick="clearComparison()">
          <i class="fas fa-times"></i> Clear Selection
        </button>
      </div>
    </div>
    ${comparisonHTML}
  `;
}

function generateRichComparisonTable(items) {
  const headers = ['Feature'].concat(items.map(item => item.title || item.name));
  
  const features = [
    'Type',
    'Category', 
    'Difficulty',
    'Duration',
    'Description',
    'Key Topics',
    'Prerequisites',
    'Outcomes'
  ];
  
  let tableHTML = `
    <div class="comparison-table-container">
      <table class="comparison-table">
        <thead>
          <tr>
            ${headers.map(header => `<th>${header}</th>`).join('')}
          </tr>
        </thead>
        <tbody>
  `;
  
  features.forEach(feature => {
    tableHTML += '<tr>';
    tableHTML += `<td><strong>${feature}</strong></td>`;
    
    items.forEach(item => {
      let value = '';
      switch(feature) {
        case 'Type':
          value = item.type || (item.hasOwnProperty('interactive') ? 'Lab' : 'Course');
          break;
        case 'Category':
          value = item.category || 'General';
          break;
        case 'Difficulty':
          value = item.difficulty || 'Intermediate';
          break;
        case 'Duration':
          value = item.duration || item.estimatedTime || 'Varies';
          break;
        case 'Description':
          value = item.description || item.overview || '';
          value = value.length > 150 ? value.substring(0, 150) + '...' : value;
          break;
        case 'Key Topics':
          value = item.topics ? item.topics.join(', ') : 
          item.keyPoints ? item.keyPoints.slice(0, 3).join(', ') : 'N/A';
          break;
        case 'Prerequisites':
          value = item.prerequisites ? item.prerequisites.join(', ') : 'None';
          break;
        case 'Outcomes':
          value = item.learningOutcomes ? item.learningOutcomes.slice(0, 2).join(', ') : 
          item.outcomes ? item.outcomes.slice(0, 2).join(', ') : 'N/A';
          break;
        default:
          value = 'N/A';
      }
      tableHTML += `<td>${value}</td>`;
    });
    
    tableHTML += '</tr>';
  });
  
  tableHTML += `
        </tbody>
      </table>
    </div>
  `;
  
  return tableHTML;
}

function clearComparison() {
  window.selectedForComparison = [];
  updateComparisonUI();
  updateComparisonContent();
  showNotification('Comparison cleared', 'info');
}

// BOOKMARKING FUNCTIONALITY RESTORATION
window.impactMojoUserBookmarks = JSON.parse(localStorage.getItem('impactMojoBookmarks')) || [];
window.impactMojoUserLabBookmarks = JSON.parse(localStorage.getItem('impactMojoLabBookmarks')) || [];

function toggleBookmark(itemId, itemType) {
  const storageKey = itemType === 'course' ? 'impactMojoBookmarks' : 'impactMojoLabBookmarks';
  const bookmarks = JSON.parse(localStorage.getItem(storageKey)) || [];
  
  const index = bookmarks.indexOf(itemId);
  if (index === -1) {
    bookmarks.push(itemId);
    showNotification(`${itemType} bookmarked!`, 'success');
  } else {
    bookmarks.splice(index, 1);
    showNotification(`${itemType} removed from bookmarks`, 'info');
  }
  
  localStorage.setItem(storageKey, JSON.stringify(bookmarks));
  
  if (itemType === 'course') {
    window.impactMojoUserBookmarks = bookmarks;
  } else {
    window.impactMojoUserLabBookmarks = bookmarks;
  }
  
  updateBookmarkUI();
}

function updateBookmarkUI() {
  const totalBookmarks = window.impactMojoUserBookmarks.length + window.impactMojoUserLabBookmarks.length;
  const bookmarkBtn = document.getElementById('bookmarkViewerBtn');
  const bookmarkCount = document.getElementById('bookmarkCount');
  
  if (bookmarkBtn) {
    bookmarkBtn.style.display = totalBookmarks > 0 ? 'flex' : 'none';
  }
  
  if (bookmarkCount) {
    bookmarkCount.textContent = totalBookmarks;
  }
  
  // Update bookmark icons on cards
  document.querySelectorAll('.bookmark-icon').forEach(icon => {
    const itemId = icon.dataset.itemId;
    const itemType = icon.dataset.itemType;
    const bookmarks = itemType === 'course' ? window.impactMojoUserBookmarks : window.impactMojoUserLabBookmarks;
    
    if (bookmarks.includes(itemId)) {
      icon.classList.add('bookmarked');
      icon.innerHTML = '<i class="fas fa-bookmark"></i>';
    } else {
      icon.classList.remove('bookmarked');
      icon.innerHTML = '<i class="far fa-bookmark"></i>';
    }
  });
}

function showBookmarkModal() {
  // Generate bookmarked items display
  const courseBookmarks = window.impactMojoUserBookmarks.map(id => 
    window.courses?.find(c => c.id === id) || impactMojoAllCourses?.find(c => c.id === id)
  ).filter(Boolean);
  
  const labBookmarks = window.impactMojoUserLabBookmarks.map(id => 
    window.labs?.find(l => l.id === id)
  ).filter(Boolean);
  
  let content = '<h3>Your Bookmarked Items</h3>';
  
  if (courseBookmarks.length === 0 && labBookmarks.length === 0) {
    content += '<p>No bookmarks yet. Start exploring courses and labs!</p>';
  } else {
    if (courseBookmarks.length > 0) {
      content += '<h4>Courses</h4><div class="bookmark-grid">';
      courseBookmarks.forEach(course => {
        content += `
          <div class="bookmark-item">
            <h5>${course.title}</h5>
            <p>${course.description.substring(0, 100)}...</p>
            <button onclick="window.open('${course.url}', '_blank')" class="launch-btn">Launch Course</button>
          </div>
        `;
      });
      content += '</div>';
    }
    
    if (labBookmarks.length > 0) {
      content += '<h4>Labs</h4><div class="bookmark-grid">';
      labBookmarks.forEach(lab => {
        content += `
          <div class="bookmark-item">
            <h5>${lab.title}</h5>
            <p>${lab.description.substring(0, 100)}...</p>
            <button onclick="window.open('${lab.url}', '_blank')" class="launch-btn">Launch Lab</button>
          </div>
        `;
      });
      content += '</div>';
    }
  }
  
  const bookmarkModal = document.getElementById('bookmarkModal');
  if (bookmarkModal) {
    bookmarkModal.querySelector('#bookmarkContent').innerHTML = content;
    openModal('bookmarkModal');
  }
}

// MODAL FUNCTIONS RESTORATION
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'flex';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
  }
}

// SEARCH AND FILTERING RESTORATION
function applyCourseFilters() {
  const searchTerm = document.getElementById('courseSearch')?.value.toLowerCase() || '';
  const categoryFilter = document.getElementById('categoryFilter')?.value || '';
  const difficultyFilter = document.getElementById('difficultyFilter')?.value || '';
  
  // Apply filters to course display
  // This would integrate with your existing course rendering logic
  console.log('Applying filters:', { searchTerm, categoryFilter, difficultyFilter });
}

// NOTIFICATION SYSTEM
function showNotification(message, type = 'info') {
  // Remove existing notifications
  document.querySelectorAll('.notification').forEach(notification => notification.remove());
  
  // Create new notification
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.innerHTML = `
    <span>${message}</span>
    <button onclick="this.parentElement.remove()">&times;</button>
  `;
  
  // Add styles
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 10000;
    background: ${type === 'success' ? '#10b981' : type === 'warning' ? '#f59e0b' : type === 'error' ? '#ef4444' : '#3b82f6'};
    color: white;
    padding: 1rem 1.5rem;
    border-radius: 0.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    display: flex;
    align-items: center;
    gap: 1rem;
    font-family: 'Poppins', sans-serif;
    font-size: 0.9rem;
    max-width: 350px;
    animation: slideInRight 0.3s ease;
  `;
  
  notification.querySelector('button').style.cssText = `
    background: none;
    border: none;
    color: white;
    font-size: 1.2rem;
    cursor: pointer;
    padding: 0;
    width: 20px;
    height: 20px;
  `;
  
  document.body.appendChild(notification);
  
  // Auto remove after 5 seconds
  setTimeout(() => {
    if (notification.parentElement) {
      notification.remove();
    }
  }, 5000);
}

// INITIALIZE EVERYTHING ON DOM LOAD
function initializeRestoredFeatures() {
  console.log('🚀 Initializing ImpactMojo restored features...');
  
  // Initialize theme
  initializeTheme();
  
  // Initialize comparison system
  updateComparisonUI();
  
  // Initialize bookmarks
  updateBookmarkUI();
  
  // Fix FAB buttons
  setTimeout(() => {
    const fabBtns = document.querySelectorAll('.fab-btn');
    fabBtns.forEach(btn => {
      if (btn.classList.contains('feedback')) {
        btn.onclick = () => openModal('feedbackModal');
      }
      if (btn.classList.contains('suggest')) {
        btn.onclick = () => openModal('suggestModal');
      }
      if (btn.classList.contains('compare')) {
        btn.onclick = () => showComparison();
      }
      if (btn.classList.contains('bookmark')) {
        btn.onclick = () => showBookmarkModal();
      }
    });
  }, 500);
  
  // Ensure auth buttons are visible
  const authButtons = document.getElementById('authButtons');
  if (authButtons) {
    authButtons.style.display = 'flex';
    authButtons.style.visibility = 'visible';
    authButtons.style.opacity = '1';
  }
  
  console.log('✅ All features restored and initialized!');
}

// AUTO-INITIALIZE
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeRestoredFeatures);
} else {
  initializeRestoredFeatures();
}

// ===== END RESTORATION JAVASCRIPT =====
// ===== TARGETED JAVASCRIPT FIXES - ADD TO END OF MAIN.JS =====

// 1. FIX MODAL OPENING FUNCTIONS
function openModal(modalId) {
  console.log(`Opening modal: ${modalId}`);
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'flex';
    modal.style.alignItems = 'center';
    modal.style.justifyContent = 'center';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    console.log(`Successfully opened: ${modalId}`);
  } else {
    console.error(`Modal not found: ${modalId}`);
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
  }
}

// 2. FIX FAB BUTTON FUNCTIONS WITH CORRECT ORDER
function initializeFABButtons() {
  console.log('🔧 Fixing FAB buttons...');
  
  setTimeout(() => {
    const fabBtns = document.querySelectorAll('.fab-btn');
    
    fabBtns.forEach(btn => {
      // Button 1: Comments/Suggestions (Blue)
      if (btn.classList.contains('feedback')) {
        btn.onclick = () => {
          console.log('💬 Comments/Suggestions clicked');
          openModal('feedbackModal');
        };
        btn.title = "Share comments and suggestions";
        btn.innerHTML = '<i class="fas fa-comment"></i>';
        console.log('✅ Fixed feedback button');
      }
      
      // Button 2: Course/Lab/Resource Requests (Green)
      if (btn.classList.contains('suggest')) {
        btn.onclick = () => {
          console.log('📚 Course/Lab/Resource request clicked');
          openModal('suggestModal');
        };
        btn.title = "Request new course, lab, or resource";
        btn.innerHTML = '<i class="fas fa-lightbulb"></i>';
        console.log('✅ Fixed suggest button');
      }
      
      // Button 3: Comparisons (Orange)
      if (btn.classList.contains('compare')) {
        btn.onclick = () => {
          console.log('⚖️ Comparison clicked');
          if (window.selectedForComparison && window.selectedForComparison.length > 1) {
            openModal('comparisonModal');
            updateComparisonContent();
          } else {
            showNotification('Select at least 2 items to compare', 'warning');
          }
        };
        btn.title = "Compare selected courses and labs";
        btn.innerHTML = '<i class="fas fa-balance-scale"></i>';
        console.log('✅ Fixed compare button');
      }
    });
    
    console.log('✅ All FAB buttons fixed');
  }, 500);
}

// 3. FIX NOTIFICATION SYSTEM
function showNotification(message, type = 'info') {
  // Remove existing notifications
  document.querySelectorAll('.notification').forEach(notification => notification.remove());
  
  // Create new notification
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  
  let backgroundColor;
  switch(type) {
    case 'success': backgroundColor = '#10b981'; break;
    case 'warning': backgroundColor = '#f59e0b'; break;
    case 'error': backgroundColor = '#ef4444'; break;
    default: backgroundColor = '#3b82f6';
  }
  
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 10000;
    background: ${backgroundColor};
    color: white;
    padding: 1rem 1.5rem;
    border-radius: 0.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    display: flex;
    align-items: center;
    gap: 1rem;
    font-family: 'Poppins', sans-serif;
    font-size: 0.9rem;
    font-weight: 500;
    max-width: 350px;
  `;
  
  notification.innerHTML = `
    <span>${message}</span>
    <button onclick="this.parentElement.remove()" style="
      background: rgba(255,255,255,0.2);
      border: none;
      color: white;
      padding: 4px 8px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 0.8rem;
    ">✕</button>
  `;
  
  document.body.appendChild(notification);
  
  // Auto remove after 5 seconds
  setTimeout(() => {
    if (notification.parentElement) {
      notification.remove();
    }
  }, 5000);
}

// 4. FIX BOOKMARKING SYSTEM
window.impactMojoUserBookmarks = JSON.parse(localStorage.getItem('impactMojoBookmarks')) || [];
window.impactMojoUserLabBookmarks = JSON.parse(localStorage.getItem('impactMojoLabBookmarks')) || [];

function toggleBookmark(itemId, itemType) {
  console.log(`Toggling bookmark for ${itemType}: ${itemId}`);
  
  const storageKey = itemType === 'course' ? 'impactMojoBookmarks' : 'impactMojoLabBookmarks';
  const bookmarks = JSON.parse(localStorage.getItem(storageKey)) || [];
  
  const index = bookmarks.indexOf(itemId);
  if (index === -1) {
    bookmarks.push(itemId);
    showNotification(`${itemType.charAt(0).toUpperCase() + itemType.slice(1)} bookmarked!`, 'success');
  } else {
    bookmarks.splice(index, 1);
    showNotification(`${itemType.charAt(0).toUpperCase() + itemType.slice(1)} removed from bookmarks`, 'info');
  }
  
  localStorage.setItem(storageKey, JSON.stringify(bookmarks));
  
  if (itemType === 'course') {
    window.impactMojoUserBookmarks = bookmarks;
  } else {
    window.impactMojoUserLabBookmarks = bookmarks;
  }
  
  updateBookmarkUI();
  return true;
}

function updateBookmarkUI() {
  const totalBookmarks = window.impactMojoUserBookmarks.length + window.impactMojoUserLabBookmarks.length;
  const bookmarkBtn = document.getElementById('bookmarkViewerBtn');
  const bookmarkCount = document.getElementById('bookmarkCount');
  
  if (bookmarkBtn) {
    bookmarkBtn.style.display = totalBookmarks > 0 ? 'flex' : 'none';
  }
  
  if (bookmarkCount) {
    bookmarkCount.textContent = totalBookmarks;
  }
  
  // Update bookmark icons on cards
  document.querySelectorAll('.bookmark-icon').forEach(icon => {
    const itemId = icon.dataset.itemId;
    const itemType = icon.dataset.itemType;
    const bookmarks = itemType === 'course' ? window.impactMojoUserBookmarks : window.impactMojoUserLabBookmarks;
    
    if (bookmarks.includes(itemId)) {
      icon.classList.add('bookmarked');
      icon.innerHTML = '<i class="fas fa-bookmark"></i>';
      icon.style.color = '#f59e0b';
    } else {
      icon.classList.remove('bookmarked');
      icon.innerHTML = '<i class="far fa-bookmark"></i>';
      icon.style.color = '#64748b';
    }
  });
}

function showBookmarkModal() {
  const courseBookmarks = window.impactMojoUserBookmarks.map(id => 
    window.courses?.find(c => c.id === id) || window.impactMojoAllCourses?.find(c => c.id === id)
  ).filter(Boolean);
  
  const labBookmarks = window.impactMojoUserLabBookmarks.map(id => 
    window.labs?.find(l => l.id === id)
  ).filter(Boolean);
  
  let content = '<h3 style="margin-bottom: 2rem; color: var(--text-primary);">Your Bookmarked Items</h3>';
  
  if (courseBookmarks.length === 0 && labBookmarks.length === 0) {
    content += `
      <div style="text-align: center; padding: 2rem; color: var(--text-secondary);">
        <i class="fas fa-bookmark" style="font-size: 3rem; margin-bottom: 1rem; opacity: 0.3;"></i>
        <p>No bookmarks yet. Start exploring courses and labs!</p>
      </div>
    `;
  } else {
    if (courseBookmarks.length > 0) {
      content += '<h4 style="color: var(--primary-color); margin: 1.5rem 0 1rem 0;">📚 Courses</h4>';
      content += '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin-bottom: 2rem;">';
      courseBookmarks.forEach(course => {
        content += `
          <div style="background: var(--surface); border: 1px solid var(--border-color); border-radius: 0.5rem; padding: 1.5rem;">
            <h5 style="margin: 0 0 0.5rem 0; color: var(--text-primary);">${course.title}</h5>
            <p style="margin: 0 0 1rem 0; color: var(--text-secondary); font-size: 0.9rem; line-height: 1.4;">${course.description.substring(0, 120)}...</p>
            <button onclick="window.open('${course.url}', '_blank')" style="
              background: var(--primary-color);
              color: white;
              border: none;
              padding: 0.5rem 1rem;
              border-radius: 0.375rem;
              cursor: pointer;
              font-size: 0.85rem;
              font-weight: 500;
              transition: all 0.3s ease;
            " onmouseover="this.style.background='var(--secondary-color)'" onmouseout="this.style.background='var(--primary-color)'">
              Launch Course <i class="fas fa-external-link-alt"></i>
            </button>
          </div>
        `;
      });
      content += '</div>';
    }
    
    if (labBookmarks.length > 0) {
      content += '<h4 style="color: var(--accent-color); margin: 1.5rem 0 1rem 0;">🧪 Labs</h4>';
      content += '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">';
      labBookmarks.forEach(lab => {
        content += `
          <div style="background: var(--surface); border: 1px solid var(--border-color); border-radius: 0.5rem; padding: 1.5rem;">
            <h5 style="margin: 0 0 0.5rem 0; color: var(--text-primary);">${lab.title}</h5>
            <p style="margin: 0 0 1rem 0; color: var(--text-secondary); font-size: 0.9rem; line-height: 1.4;">${lab.description.substring(0, 120)}...</p>
            <button onclick="window.open('${lab.url}', '_blank')" style="
              background: var(--accent-color);
              color: white;
              border: none;
              padding: 0.5rem 1rem;
              border-radius: 0.375rem;
              cursor: pointer;
              font-size: 0.85rem;
              font-weight: 500;
              transition: all 0.3s ease;
            " onmouseover="this.style.background='#d97706'" onmouseout="this.style.background='var(--accent-color)'">
              Launch Lab <i class="fas fa-external-link-alt"></i>
            </button>
          </div>
        `;
      });
      content += '</div>';
    }
  }
  
  const bookmarkModal = document.getElementById('bookmarkModal');
  if (bookmarkModal) {
    const contentDiv = bookmarkModal.querySelector('#bookmarkContent') || bookmarkModal.querySelector('.modal-content');
    if (contentDiv) {
      contentDiv.innerHTML = content;
    }
    openModal('bookmarkModal');
  }
}

// 5. FIX COMPARISON SYSTEM
window.selectedForComparison = window.selectedForComparison || [];
window.MAX_COMPARISON_ITEMS = 4;

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
  const compareFab = document.querySelector('.fab-btn.compare');
  if (compareFab) {
    compareFab.style.display = window.selectedForComparison.length > 1 ? 'flex' : 'none';
  }
  
  // Update checkboxes
  document.querySelectorAll('.comparison-checkbox').forEach(checkbox => {
    const itemId = checkbox.dataset.itemId;
    const itemType = checkbox.dataset.itemType;
    if (itemId && itemType) {
      const itemKey = `${itemType}-${itemId}`;
      checkbox.checked = window.selectedForComparison.some(item => item.key === itemKey);
    }
  });
}

function updateComparisonContent() {
  const content = document.getElementById('comparisonContent');
  if (!content) return;
  
  if (window.selectedForComparison.length < 2) {
    content.innerHTML = `
      <div style="text-align: center; padding: 3rem; color: var(--text-secondary);">
        <i class="fas fa-balance-scale" style="font-size: 3rem; margin-bottom: 1rem; opacity: 0.3;"></i>
        <h3 style="margin: 0 0 1rem 0; color: var(--text-primary);">Select items to compare</h3>
        <p style="margin: 0;">Use the checkboxes on course and lab cards to select items for comparison. You can compare 2-4 items at once.</p>
      </div>
    `;
    return;
  }
  
  // Get actual course/lab data
  const items = window.selectedForComparison.map(item => {
    if (item.type === 'course') {
      return window.courses?.find(c => c.id === item.id) || 
      window.impactMojoAllCourses?.find(c => c.id === item.id);
    } else if (item.type === 'lab') {
      return window.labs?.find(l => l.id === item.id);
    }
    return null;
  }).filter(Boolean);
  
  if (items.length === 0) {
    content.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Error loading comparison data.</p>';
    return;
  }
  
  // Generate enhanced comparison table
  const comparisonHTML = generateEnhancedComparisonTable(items);
  
  content.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; padding: 1rem; background: var(--surface); border-radius: 0.5rem; border: 1px solid var(--border-color);">
      <span style="font-weight: 600; color: var(--text-primary);">
        <i class="fas fa-balance-scale" style="margin-right: 0.5rem; color: var(--primary-color);"></i>
        Comparing ${items.length} item${items.length > 1 ? 's' : ''}
      </span>
      <button onclick="clearComparison()" style="
        background: var(--error-color);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        cursor: pointer;
        font-size: 0.85rem;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 0.5rem;
      ">
        <i class="fas fa-times"></i> Clear Selection
      </button>
    </div>
    ${comparisonHTML}
  `;
}

function generateEnhancedComparisonTable(items) {
  const headers = ['Feature'].concat(items.map(item => item.title || item.name));
  
  const features = [
    { key: 'type', label: 'Type' },
    { key: 'category', label: 'Category' },
    { key: 'difficulty', label: 'Difficulty' },
    { key: 'duration', label: 'Duration' },
    { key: 'description', label: 'Description' },
    { key: 'topics', label: 'Key Topics' },
    { key: 'prerequisites', label: 'Prerequisites' },
    { key: 'outcomes', label: 'Learning Outcomes' }
  ];
  
  let tableHTML = `
    <div class="comparison-table-container">
      <table class="comparison-table">
        <thead>
          <tr>
            ${headers.map(header => `<th>${header}</th>`).join('')}
          </tr>
        </thead>
        <tbody>
  `;
  
  features.forEach(feature => {
    tableHTML += '<tr>';
    tableHTML += `<td><strong>${feature.label}</strong></td>`;
    
    items.forEach(item => {
      let value = '';
      switch(feature.key) {
        case 'type':
          value = item.type || (item.hasOwnProperty('interactive') ? 'Lab' : 'Course');
          break;
        case 'category':
          value = item.category || 'General';
          break;
        case 'difficulty':
          value = item.difficulty || 'Intermediate';
          break;
        case 'duration':
          value = item.duration || item.estimatedTime || 'Varies';
          break;
        case 'description':
          value = item.description || item.overview || '';
          if (value.length > 200) {
            value = `<div class="description-preview">${value.substring(0, 200)}... <button onclick="this.style.display='none'; this.nextElementSibling.style.display='block';" style="color: var(--primary-color); background: none; border: none; cursor: pointer; text-decoration: underline;">Read more</button></div><div class="description-full" style="display: none;">${value} <button onclick="this.style.display='none'; this.previousElementSibling.style.display='block';" style="color: var(--primary-color); background: none; border: none; cursor: pointer; text-decoration: underline;">Show less</button></div>`;
          }
          break;
        case 'topics':
          if (item.topics && Array.isArray(item.topics)) {
            value = `<ul style="margin: 0; padding-left: 1.2rem;">${item.topics.slice(0, 5).map(topic => `<li>${topic}</li>`).join('')}</ul>`;
          } else if (item.keyPoints && Array.isArray(item.keyPoints)) {
            value = `<ul style="margin: 0; padding-left: 1.2rem;">${item.keyPoints.slice(0, 5).map(point => `<li>${point}</li>`).join('')}</ul>`;
          } else {
            value = 'N/A';
          }
          break;
        case 'prerequisites':
          if (item.prerequisites && Array.isArray(item.prerequisites)) {
            value = item.prerequisites.join(', ');
          } else {
            value = 'None specified';
          }
          break;
        case 'outcomes':
          if (item.learningOutcomes && Array.isArray(item.learningOutcomes)) {
            value = `<ul style="margin: 0; padding-left: 1.2rem;">${item.learningOutcomes.slice(0, 3).map(outcome => `<li>${outcome}</li>`).join('')}</ul>`;
          } else if (item.outcomes && Array.isArray(item.outcomes)) {
            value = `<ul style="margin: 0; padding-left: 1.2rem;">${item.outcomes.slice(0, 3).map(outcome => `<li>${outcome}</li>`).join('')}</ul>`;
          } else {
            value = 'N/A';
          }
          break;
        default:
          value = 'N/A';
      }
      tableHTML += `<td class="comparison-text">${value}</td>`;
    });
    
    tableHTML += '</tr>';
  });
  
  tableHTML += `
        </tbody>
      </table>
    </div>
  `;
  
  return tableHTML;
}

function clearComparison() {
  window.selectedForComparison = [];
  updateComparisonUI();
  updateComparisonContent();
  showNotification('Comparison cleared', 'info');
}

// 6. FIX THEME TOGGLE
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  if (themeIcon) {
    themeIcon.className = newTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
  
  showNotification(`Switched to ${newTheme} mode`, 'success');
}

function initializeTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  document.documentElement.setAttribute('data-theme', savedTheme);
  
  if (themeIcon) {
    themeIcon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
}

// 7. MAIN INITIALIZATION FUNCTION
function initializeAllFeatures() {
  console.log('🚀 Initializing all ImpactMojo features...');
  
  // Initialize theme
  initializeTheme();
  
  // Initialize FAB buttons
  initializeFABButtons();
  
  // Initialize bookmarks
  updateBookmarkUI();
  
  // Initialize comparison system
  updateComparisonUI();
  
  // Ensure auth buttons are visible
  const authButtons = document.getElementById('authButtons');
  if (authButtons) {
    authButtons.style.display = 'flex';
    authButtons.style.visibility = 'visible';
    authButtons.style.opacity = '1';
  }
  
  // Remove duplicate bookmark buttons
  const bookmarkBtns = document.querySelectorAll('.bookmark-viewer-btn');
  if (bookmarkBtns.length > 1) {
    for (let i = 1; i < bookmarkBtns.length; i++) {
      bookmarkBtns[i].remove();
    }
  }
  
  console.log('✅ All features initialized successfully!');
}

// AUTO-INITIALIZE EVERYTHING
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeAllFeatures);
} else {
  initializeAllFeatures();
}

// ===== END TARGETED FIXES =====
// AUTH BUTTONS FUNCTIONS
function showLoginModal() {
  console.log('Opening login modal');
  const modal = document.getElementById('loginModal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
}

function showSignupModal() {
  console.log('Opening signup modal');
  const modal = document.getElementById('signupModal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  }
}
// ===== FIREBASE AUTH BUTTONS FIX - ADD TO END OF main.js =====
// Connect buttons to your existing Firebase auth system

function connectAuthButtons() {
  console.log('🔧 Connecting auth buttons to Firebase...');
  
  // Find and fix Sign In button
  const signInBtn = document.querySelector('.auth-btn:not(.signup)');
  if (signInBtn) {
    // Remove any existing onclick
    signInBtn.onclick = null;
    
    // Connect to your existing Firebase login function
    signInBtn.onclick = function() {
      console.log('🔑 Sign In clicked - opening login modal');
      
      // Try different possible function names for your Firebase auth
      if (typeof showLoginModal === 'function') {
        showLoginModal();
      } else if (typeof openModal === 'function') {
        openModal('loginModal');
      } else if (document.getElementById('loginModal')) {
        // Direct modal opening
        const modal = document.getElementById('loginModal');
        modal.style.display = 'flex';
        modal.style.alignItems = 'center';
        modal.style.justifyContent = 'center';
        document.body.style.overflow = 'hidden';
      } else {
        console.log('⚠️ Login modal not found');
        // Create a simple login modal if none exists
        createSimpleLoginModal();
      }
    };
    console.log('✅ Sign In button connected');
  }
  
  // Find and fix Sign Up button  
  const signUpBtn = document.querySelector('.auth-btn.signup');
  if (signUpBtn) {
    // Remove any existing onclick
    signUpBtn.onclick = null;
    
    // Connect to your existing Firebase signup function
    signUpBtn.onclick = function() {
      console.log('📝 Sign Up clicked - opening signup modal');
      
      // Try different possible function names for your Firebase auth
      if (typeof showSignupModal === 'function') {
        showSignupModal();
      } else if (typeof openModal === 'function') {
        openModal('signupModal');
      } else if (document.getElementById('signupModal')) {
        // Direct modal opening
        const modal = document.getElementById('signupModal');
        modal.style.display = 'flex';
        modal.style.alignItems = 'center';
        modal.style.justifyContent = 'center';
        document.body.style.overflow = 'hidden';
      } else {
        console.log('⚠️ Signup modal not found');
        // Create a simple signup modal if none exists
        createSimpleSignupModal();
      }
    };
    console.log('✅ Sign Up button connected');
  }
}

// Create simple login modal if it doesn't exist
function createSimpleLoginModal() {
  if (document.getElementById('loginModal')) return;
  
  const modal = document.createElement('div');
  modal.id = 'loginModal';
  modal.style.cssText = `
    display: flex; position: fixed; z-index: 10000; left: 0; top: 0; 
    width: 100%; height: 100%; background: rgba(0,0,0,0.7);
    align-items: center; justify-content: center;
  `;
  
  modal.innerHTML = `
    <div style="background: white; padding: 2rem; border-radius: 12px; width: 400px; max-width: 90%; position: relative;">
      <span onclick="closeLoginModal()" style="position: absolute; top: 1rem; right: 1rem; font-size: 1.5rem; cursor: pointer; color: #666;">&times;</span>
      <h2 style="color: #6366f1; margin-bottom: 1.5rem; text-align: center;">
        <i class="fas fa-sign-in-alt"></i> Sign In
      </h2>
      <form style="display: flex; flex-direction: column; gap: 1rem;">
        <input type="email" placeholder="Email" style="padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px;" required>
        <input type="password" placeholder="Password" style="padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px;" required>
        <button type="submit" style="padding: 0.75rem; background: #6366f1; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600;">Sign In</button>
      </form>
      <button onclick="signInWithGoogle()" style="width: 100%; margin-top: 1rem; padding: 0.75rem; background: #ea4335; color: white; border: none; border-radius: 8px; cursor: pointer;">
        <i class="fab fa-google"></i> Sign in with Google
      </button>
      <p style="text-align: center; margin-top: 1rem;">
        Don't have an account? <a href="#" onclick="closeLoginModal(); setTimeout(() => openSignupModal(), 100);" style="color: #6366f1;">Sign Up</a>
      </p>
    </div>
  `;
  
  document.body.appendChild(modal);
}

// Create simple signup modal if it doesn't exist
function createSimpleSignupModal() {
  if (document.getElementById('signupModal')) return;
  
  const modal = document.createElement('div');
  modal.id = 'signupModal';
  modal.style.cssText = `
    display: flex; position: fixed; z-index: 10000; left: 0; top: 0; 
    width: 100%; height: 100%; background: rgba(0,0,0,0.7);
    align-items: center; justify-content: center;
  `;
  
  modal.innerHTML = `
    <div style="background: white; padding: 2rem; border-radius: 12px; width: 400px; max-width: 90%; position: relative;">
      <span onclick="closeSignupModal()" style="position: absolute; top: 1rem; right: 1rem; font-size: 1.5rem; cursor: pointer; color: #666;">&times;</span>
      <h2 style="color: #6366f1; margin-bottom: 1.5rem; text-align: center;">
        <i class="fas fa-user-plus"></i> Sign Up
      </h2>
      <form style="display: flex; flex-direction: column; gap: 1rem;">
        <input type="text" placeholder="Full Name" style="padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px;" required>
        <input type="email" placeholder="Email" style="padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px;" required>
        <input type="password" placeholder="Password" style="padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 8px;" required>
        <button type="submit" style="padding: 0.75rem; background: #6366f1; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600;">Create Account</button>
      </form>
      <button onclick="signInWithGoogle()" style="width: 100%; margin-top: 1rem; padding: 0.75rem; background: #ea4335; color: white; border: none; border-radius: 8px; cursor: pointer;">
        <i class="fab fa-google"></i> Continue with Google
      </button>
      <p style="text-align: center; margin-top: 1rem;">
        Already have an account? <a href="#" onclick="closeSignupModal(); setTimeout(() => openLoginModal(), 100);" style="color: #6366f1;">Sign In</a>
      </p>
    </div>
  `;
  
  document.body.appendChild(modal);
}

// Modal control functions
function closeLoginModal() {
  const modal = document.getElementById('loginModal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  }
}

function closeSignupModal() {
  const modal = document.getElementById('signupModal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  }
}

function openLoginModal() {
  createSimpleLoginModal();
  const modal = document.getElementById('loginModal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
}

function openSignupModal() {
  createSimpleSignupModal();
  const modal = document.getElementById('signupModal');
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
}

// Connect to existing Google sign-in if it exists
if (typeof signInWithGoogle !== 'function') {
  window.signInWithGoogle = function() {
    console.log('🔥 Google sign-in clicked');
    alert('Google sign-in will be implemented with your Firebase config');
  };
}

// Run the connection after page loads
setTimeout(connectAuthButtons, 1000);

// Also run when DOM changes (in case buttons are added later)
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', connectAuthButtons);
} else {
  connectAuthButtons();
}

console.log('🔥 Firebase auth buttons fix loaded!');