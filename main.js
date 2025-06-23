// ImpactMojo Main JavaScript
// Complete functionality for course display, filtering, authentication, and all interactive features

// Global state variables
let currentUser = null;
let userBookmarks = [];
let userNotes = '';
let filteredCourses = [];
let selectedCourses = [];
let currentView = 'grid';
let currentFilters = {
  search: '',
  category: 'All Courses',
  difficulty: '',
  bookmarks: false
};

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  initializeApp();
});

// Main initialization function
function initializeApp() {
  console.log('Initializing ImpactMojo...');
  
  // Initialize theme
  initializeTheme();
  
  // Load courses and labs
  loadCourses();
  loadLabs();
  
  // Set up event listeners
  setupEventListeners();
  
  // Initialize Firebase auth state listener
  initializeAuth();
  
  console.log('ImpactMojo initialized successfully');
}

// Theme management
function initializeTheme() {
  const savedTheme = localStorage.getItem('impactmojo_theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('impactmojo_theme', newTheme);
  updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
  const themeIcon = document.getElementById('themeIcon');
  if (themeIcon) {
    themeIcon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
}

// Course loading and display
function loadCourses() {
  if (!window.coursesData) {
    console.error('Course data not found. Make sure course-data.js is loaded.');
    return;
  }
  
  filteredCourses = [...window.coursesData];
  displayCourses();
  updateCourseCount();
  console.log(`Loaded ${window.coursesData.length} courses`);
}

function displayCourses() {
  const container = document.getElementById('courseContainer');
  const noResults = document.getElementById('noResults');
  
  if (!container) {
    console.error('Course container not found');
    return;
  }
  
  if (filteredCourses.length === 0) {
    container.innerHTML = '';
    if (noResults) noResults.classList.remove('hidden');
    return;
  }
  
  if (noResults) noResults.classList.add('hidden');
  
  container.innerHTML = filteredCourses.map(course => createCourseCard(course)).join('');
  console.log(`Displayed ${filteredCourses.length} courses`);
}

function createCourseCard(course) {
  const isBookmarked = userBookmarks.includes(course.id);
  const isSelected = selectedCourses.includes(course.id);
  
  return `
    <div class="course-card" data-course-id="${course.id}">
      <div class="course-number">${course.number}</div>
      
      <div class="course-header">
        <div class="course-icon">
          <i class="${course.icon}"></i>
        </div>
        <div class="course-title-section">
          <h3 class="course-title">${course.title}</h3>
          <div class="course-meta">
            <span class="meta-tag category">${course.category}</span>
            <span class="meta-tag difficulty">${course.difficulty}</span>
            <span class="meta-tag duration">${course.duration}</span>
          </div>
        </div>
      </div>
      
      <div class="course-description">
        <p>${course.description}</p>
      </div>
      
      <div class="course-stats">
        <div class="course-stat">
          <i class="fas fa-star"></i>
          <span class="number">${course.rating}</span>
          <span class="label">rating</span>
        </div>
        <div class="course-stat">
          <i class="fas fa-users"></i>
          <span class="number">${course.learnerCount.toLocaleString()}</span>
          <span class="label">learners</span>
        </div>
      </div>
      
      <div class="course-actions">
        <div class="course-actions-left">
          <a href="${course.url}" class="launch-btn" target="_blank" rel="noopener">
            <i class="fas fa-play"></i>
            Launch Course
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
          <button class="expand-btn" onclick="toggleCourseDetails('${course.id}')" 
                  title="Show details">
            <i class="fas fa-chevron-down"></i>
          </button>
        </div>
      </div>
      
      <div class="course-details hidden" id="details-${course.id}">
        <div class="details-section">
          <h4>Prerequisites</h4>
          <ul>
            ${course.prerequisites.map(prereq => `<li>${prereq}</li>`).join('')}
          </ul>
        </div>
        
        <div class="details-section">
          <h4>Learning Outcomes</h4>
          <ul>
            ${course.outcomes.map(outcome => `<li>${outcome}</li>`).join('')}
          </ul>
        </div>
        
        <div class="details-section">
          <h4>Target Audience</h4>
          <p>${course.audience}</p>
        </div>
      </div>
    </div>
  `;
}

// Labs loading and display
function loadLabs() {
  if (!window.labsData) {
    console.error('Labs data not found. Make sure course-data.js is loaded.');
    return;
  }
  
  const container = document.getElementById('labsContainer');
  if (!container) return;
  
  // Labs are already hardcoded in HTML, but we could dynamically generate them here if needed
  console.log(`${window.labsData.length} labs available`);
}

// Course interaction functions
function toggleCourseDetails(courseId) {
  const details = document.getElementById(`details-${courseId}`);
  const expandBtn = document.querySelector(`[onclick="toggleCourseDetails('${courseId}')"] i`);
  
  if (details) {
    details.classList.toggle('hidden');
    if (expandBtn) {
      expandBtn.className = details.classList.contains('hidden') ? 
        'fas fa-chevron-down' : 'fas fa-chevron-up';
    }
  }
}

function toggleBookmark(courseId) {
  if (!currentUser) {
    showNotification('Please log in to bookmark courses', 'warning');
    showLoginModal();
    return;
  }
  
  const index = userBookmarks.indexOf(courseId);
  if (index > -1) {
    userBookmarks.splice(index, 1);
    showNotification('Bookmark removed', 'info');
  } else {
    userBookmarks.push(courseId);
    showNotification('Course bookmarked', 'success');
  }
  
  saveUserData();
  displayCourses(); // Refresh to update bookmark icons
}

function toggleCourseSelection(courseId) {
  const index = selectedCourses.indexOf(courseId);
  if (index > -1) {
    selectedCourses.splice(index, 1);
  } else {
    selectedCourses.push(courseId);
  }
  
  updateCompareButton();
}

function updateCompareButton() {
  const compareBtn = document.querySelector('.fab-btn.compare');
  if (compareBtn) {
    if (selectedCourses.length > 1) {
      compareBtn.style.display = 'flex';
    } else {
      compareBtn.style.display = 'none';
    }
  }
}

// Filtering and search functionality
function searchCourses() {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    currentFilters.search = searchInput.value.toLowerCase();
    applyFilters();
  }
}

function filterCourses() {
  const categoryFilter = document.getElementById('categoryFilter');
  const difficultyFilter = document.getElementById('difficultyFilter');
  
  if (categoryFilter) currentFilters.category = categoryFilter.value;
  if (difficultyFilter) currentFilters.difficulty = difficultyFilter.value;
  
  applyFilters();
}

function applyFilters() {
  if (!window.coursesData) return;
  
  filteredCourses = window.coursesData.filter(course => {
    // Search filter
    const matchesSearch = !currentFilters.search || 
      course.title.toLowerCase().includes(currentFilters.search) ||
      course.description.toLowerCase().includes(currentFilters.search) ||
      course.category.toLowerCase().includes(currentFilters.search) ||
      course.audience.toLowerCase().includes(currentFilters.search);
    
    // Category filter
    const matchesCategory = currentFilters.category === 'All Courses' || 
      course.category === currentFilters.category;
    
    // Difficulty filter
    const matchesDifficulty = !currentFilters.difficulty || 
      course.difficulty === currentFilters.difficulty;
    
    // Bookmark filter
    const matchesBookmark = !currentFilters.bookmarks || 
      userBookmarks.includes(course.id);
    
    return matchesSearch && matchesCategory && matchesDifficulty && matchesBookmark;
  });
  
  displayCourses();
  updateCourseCount();
}

function updateCourseCount() {
  const visibleCount = document.getElementById('visibleCount');
  const totalCount = document.getElementById('totalCount');
  
  if (visibleCount) visibleCount.textContent = filteredCourses.length;
  if (totalCount) totalCount.textContent = window.coursesData ? window.coursesData.length : 0;
}

// Learning path functionality
function applyLearningPath(pathName) {
  const paths = {
    'data-analysis': ['Data Literacy 101', 'EDA for Survey Data', 'Bivariate Analysis', 'Multivariate Analysis'],
    'gender-studies': ['Gender Studies 101', 'Data Feminism 101', 'Care Economy', 'Women\'s Economic Empowerment'],
    'research-methods': ['Research Methods 101', 'Sampling 101', 'Survey Design', 'Impact Measurement'],
    'economics': ['Development Economics 101', 'Behavioral Economics', 'Social Protection', 'Livelihoods 101']
  };
  
  const pathCourses = paths[pathName];
  if (pathCourses) {
    // Filter to show only courses in this learning path
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
      // Create a search pattern that matches any of the path course titles
      const searchPattern = pathCourses.join('|');
      currentFilters.search = '';
      
      filteredCourses = window.coursesData.filter(course => 
        pathCourses.some(pathCourse => 
          course.title.toLowerCase().includes(pathCourse.toLowerCase())
        )
      );
      
      displayCourses();
      updateCourseCount();
      
      // Scroll to courses section
      document.getElementById('courses')?.scrollIntoView({ behavior: 'smooth' });
      
      showNotification(`Showing ${pathName.replace('-', ' ')} courses`, 'info');
    }
  }
}

// View toggle functionality
function toggleView(viewType, event) {
  if (event) {
    // Update button states
    document.querySelectorAll('.view-btn').forEach(btn => {
      btn.classList.remove('active');
      btn.setAttribute('aria-pressed', 'false');
    });
    event.target.closest('.view-btn').classList.add('active');
    event.target.closest('.view-btn').setAttribute('aria-pressed', 'true');
  }
  
  currentView = viewType;
  const container = document.getElementById('courseContainer');
  if (container) {
    container.className = viewType === 'list' ? 'courses-list' : 'courses-grid';
  }
}

// Modal management
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto'; // Restore scrolling
  }
}

// Authentication functions
function initializeAuth() {
  if (typeof window.onAuthStateChanged !== 'undefined' && window.auth) {
    window.onAuthStateChanged(window.auth, handleAuthStateChange);
  }
}

function handleAuthStateChange(user) {
  currentUser = user;
  updateAuthUI();
  
  if (user) {
    loadUserData();
    console.log('User logged in:', user.email);
  } else {
    userBookmarks = [];
    userNotes = '';
    console.log('User logged out');
  }
  
  displayCourses(); // Refresh to update bookmark states
}

function updateAuthUI() {
  const authButtons = document.getElementById('authButtons');
  const userMenu = document.getElementById('userMenu');
  
  if (currentUser) {
    if (authButtons) authButtons.classList.add('hidden');
    if (userMenu) userMenu.classList.remove('hidden');
    
    const userDisplayName = document.getElementById('userDisplayName');
    if (userDisplayName) {
      userDisplayName.textContent = currentUser.displayName || currentUser.email.split('@')[0];
    }
  } else {
    if (authButtons) authButtons.classList.remove('hidden');
    if (userMenu) userMenu.classList.add('hidden');
  }
}

function showLoginModal() {
  openModal('loginModal');
}

function showSignupModal() {
  openModal('signupModal');
}

function showDashboard() {
  loadUserDashboard();
  openModal('dashboardModal');
}

// Authentication form handlers
async function login(event) {
  event.preventDefault();
  
  const email = document.getElementById('loginEmail').value;
  const password = document.getElementById('loginPassword').value;
  
  try {
    await window.signInWithEmailAndPassword(window.auth, email, password);
    closeModal('loginModal');
    showNotification('Successfully logged in!', 'success');
  } catch (error) {
    console.error('Login error:', error);
    showNotification(error.message, 'error');
  }
}

async function signup(event) {
  event.preventDefault();
  
  const name = document.getElementById('signupName').value;
  const email = document.getElementById('signupEmail').value;
  const password = document.getElementById('signupPassword').value;
  
  try {
    const userCredential = await window.createUserWithEmailAndPassword(window.auth, email, password);
    
    // Update user profile with name
    if (name && window.updateProfile) {
      await window.updateProfile(userCredential.user, { displayName: name });
    }
    
    closeModal('signupModal');
    showNotification('Account created successfully!', 'success');
  } catch (error) {
    console.error('Signup error:', error);
    showNotification(error.message, 'error');
  }
}

async function loginWithGoogle() {
  try {
    const provider = new window.GoogleAuthProvider();
    await window.signInWithPopup(window.auth, provider);
    closeModal('loginModal');
    closeModal('signupModal');
    showNotification('Successfully logged in with Google!', 'success');
  } catch (error) {
    console.error('Google login error:', error);
    showNotification(error.message, 'error');
  }
}

async function logout() {
  try {
    await window.signOut(window.auth);
    showNotification('Successfully logged out!', 'info');
  } catch (error) {
    console.error('Logout error:', error);
    showNotification('Error logging out', 'error');
  }
}

async function forgotPassword() {
  const email = prompt('Enter your email address:');
  if (email) {
    try {
      await window.sendPasswordResetEmail(window.auth, email);
      showNotification('Password reset email sent!', 'success');
    } catch (error) {
      console.error('Password reset error:', error);
      showNotification(error.message, 'error');
    }
  }
}

// User data management
async function loadUserData() {
  if (!currentUser || !window.getDoc) return;
  
  try {
    const userDoc = await window.getDoc(window.doc(window.db, 'users', currentUser.uid));
    if (userDoc.exists()) {
      const userData = userDoc.data();
      userBookmarks = userData.bookmarks || [];
      userNotes = userData.notes || '';
    }
  } catch (error) {
    console.error('Error loading user data:', error);
  }
}

async function saveUserData() {
  if (!currentUser || !window.setDoc) return;
  
  try {
    await window.setDoc(window.doc(window.db, 'users', currentUser.uid), {
      bookmarks: userBookmarks,
      notes: userNotes,
      lastUpdated: new Date()
    }, { merge: true });
  } catch (error) {
    console.error('Error saving user data:', error);
  }
}

function loadUserDashboard() {
  // Load bookmarked courses
  const bookmarksList = document.getElementById('userBookmarksList');
  if (bookmarksList && window.coursesData) {
    const bookmarkedCourses = window.coursesData.filter(course => 
      userBookmarks.includes(course.id)
    );
    
    if (bookmarkedCourses.length > 0) {
      bookmarksList.innerHTML = bookmarkedCourses.map(course => `
        <div class="bookmark-item">
          <i class="${course.icon}"></i>
          <span>${course.title}</span>
          <a href="${course.url}" target="_blank" class="launch-btn-small">Launch</a>
        </div>
      `).join('');
    } else {
      bookmarksList.innerHTML = '<p>No bookmarked courses yet.</p>';
    }
  }
  
  // Load user notes
  const notesTextarea = document.getElementById('userNotes');
  if (notesTextarea) {
    notesTextarea.value = userNotes;
  }
}

async function saveNotes() {
  const notesTextarea = document.getElementById('userNotes');
  if (notesTextarea) {
    userNotes = notesTextarea.value;
    await saveUserData();
    showNotification('Notes saved!', 'success');
  }
}

// Event listeners setup
function setupEventListeners() {
  // Search input
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', searchCourses);
  }
  
  // Filter dropdowns
  const categoryFilter = document.getElementById('categoryFilter');
  const difficultyFilter = document.getElementById('difficultyFilter');
  
  if (categoryFilter) categoryFilter.addEventListener('change', filterCourses);
  if (difficultyFilter) difficultyFilter.addEventListener('change', filterCourses);
  
  // Close modals when clicking outside
  window.addEventListener('click', function(event) {
    if (event.target.classList.contains('modal')) {
      event.target.style.display = 'none';
      document.body.style.overflow = 'auto';
    }
  });
  
  // Keyboard shortcuts
  document.addEventListener('keydown', function(event) {
    // Escape key closes modals
    if (event.key === 'Escape') {
      const openModal = document.querySelector('.modal[style*="block"]');
      if (openModal) {
        openModal.style.display = 'none';
        document.body.style.overflow = 'auto';
      }
    }
    
    // Ctrl/Cmd + K for search
    if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
      event.preventDefault();
      const searchInput = document.getElementById('searchInput');
      if (searchInput) {
        searchInput.focus();
      }
    }
  });
}

// Notification system
function showNotification(message, type = 'info') {
  const notification = document.getElementById('notification');
  if (!notification) return;
  
  notification.textContent = message;
  notification.className = `notification ${type}`;
  notification.style.display = 'block';
  
  setTimeout(() => {
    notification.style.display = 'none';
  }, 4000);
}

// Utility functions
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
  }
}

// Make functions globally available
window.toggleTheme = toggleTheme;
window.searchCourses = searchCourses;
window.filterCourses = filterCourses;
window.applyLearningPath = applyLearningPath;
window.toggleView = toggleView;
window.toggleCourseDetails = toggleCourseDetails;
window.toggleBookmark = toggleBookmark;
window.toggleCourseSelection = toggleCourseSelection;
window.openModal = openModal;
window.closeModal = closeModal;
window.showLoginModal = showLoginModal;
window.showSignupModal = showSignupModal;
window.showDashboard = showDashboard;
window.login = login;
window.signup = signup;
window.loginWithGoogle = loginWithGoogle;
window.logout = logout;
window.forgotPassword = forgotPassword;
window.saveNotes = saveNotes;
window.showNotification = showNotification;

console.log('main.js loaded successfully');