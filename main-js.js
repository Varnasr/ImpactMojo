// ImpactMojo Main JavaScript
// Handles course display, filtering, labs, and user interactions

// Global state variables
let currentUser = null;
let filteredCourses = [];
let allCourses = [];
let selectedCourses = [];
let currentView = 'grid';
let currentCategory = 'All Courses';
let currentDifficulty = '';
let userBookmarks = [];

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
  initializeApp();
});

// Initialize application
function initializeApp() {
  // Initialize theme
  initializeTheme();
  
  // Load courses and labs
  loadCourses();
  loadLabs();
  
  // Initialize Firebase auth
  if (typeof window.onAuthStateChanged !== 'undefined') {
    window.onAuthStateChanged(window.auth, handleAuthStateChange);
  }
  
  // Set up event listeners
  setupEventListeners();
  
  // Show courses section by default
  showSection('courses');
}

// Handle authentication state changes
function handleAuthStateChange(user) {
  currentUser = user;
  updateAuthUI();
  if (user) {
    loadUserBookmarks();
  } else {
    userBookmarks = [];
  }
  refreshCourseDisplay();
}

// Load and display courses
function loadCourses() {
  if (typeof courses === 'undefined') {
    console.error('Course data not loaded');
    return;
  }
  
  allCourses = [...courses];
  filteredCourses = [...allCourses];
  displayCourses();
  updateCourseCount();
}

// Display courses in the grid
function displayCourses() {
  const container = document.getElementById('courseContainer');
  const noResults = document.getElementById('noResults');
  
  if (!container) return;
  
  if (filteredCourses.length === 0) {
    container.innerHTML = '';
    if (noResults) noResults.classList.remove('hidden');
    return;
  }
  
  if (noResults) noResults.classList.add('hidden');
  
  container.innerHTML = filteredCourses.map(course => createCourseCard(course)).join('');
}

// Create individual course card HTML
function createCourseCard(course) {
  const isBookmarked = userBookmarks.includes(course.id);
  const isSelected = selectedCourses.includes(course.id);
  
  return `
    <div class="course-card ${currentView === 'list' ? 'list-view' : ''}" data-course-id="${course.id}">
      <div class="course-card-header">
        <div class="course-icon">
          <i class="${getCourseIcon(course.category)}"></i>
        </div>
        <div class="course-meta-info">
          <span class="course-category">${course.category}</span>
          <span class="course-difficulty difficulty-${course.difficulty}">${course.difficulty}</span>
        </div>
      </div>
      
      <div class="course-content">
        <h3>${course.title}</h3>
        <p class="course-description">${course.description}</p>
        
        <div class="course-stats">
          <span><i class="fas fa-clock"></i> ${course.duration || '3-4 hours'}</span>
          <span><i class="fas fa-users"></i> ${course.learnerCount || 0} learners</span>
          <span><i class="fas fa-star"></i> ${course.rating || 4.5}</span>
        </div>
      </div>
      
      <div class="course-actions">
        <div class="course-actions-left">
          <a href="${course.url}" target="_blank" rel="noopener" class="launch-btn">
            <i class="fas fa-external-link-alt"></i> Launch Course
          </a>
          <button class="bookmark-btn ${isBookmarked ? 'bookmarked' : ''}" 
                  onclick="toggleBookmark('${course.id}')" 
                  title="${isBookmarked ? 'Remove bookmark' : 'Bookmark course'}">
            <i class="${isBookmarked ? 'fas' : 'far'} fa-bookmark"></i>
          </button>
        </div>
        <div class="course-actions-right">
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
      
      <div class="course-details" id="details-${course.id}">
        <div class="details-section">
          <h4>Prerequisites</h4>
          <ul>
            ${(course.prerequisites || ['None']).map(prereq => `<li>${prereq}</li>`).join('')}
          </ul>
        </div>
        
        <div class="details-section">
          <h4>Learning Outcomes</h4>
          <ul>
            ${(course.outcomes || ['Comprehensive understanding of the topic']).map(outcome => `<li>${outcome}</li>`).join('')}
          </ul>
        </div>
        
        <div class="details-section">
          <h4>Target Audience</h4>
          <p>${course.audience || 'Development practitioners, researchers, students'}</p>
        </div>
      </div>
    </div>
  `;
}

// Get appropriate icon for course category
function getCourseIcon(category) {
  const icons = {
    'Data Analysis': 'fas fa-chart-bar',
    'Economics': 'fas fa-coins',
    'Gender Studies': 'fas fa-venus',
    'Health': 'fas fa-heartbeat',
    'Identity & Justice': 'fas fa-balance-scale',
    'Climate & Environment': 'fas fa-leaf',
    'Urban & Systems': 'fas fa-city',
    'Education': 'fas fa-graduation-cap',
    'Research Methods': 'fas fa-microscope',
    'Technology': 'fas fa-laptop-code'
  };
  return icons[category] || 'fas fa-book';
}

// Load and display labs
function loadLabs() {
  if (typeof labs === 'undefined') {
    console.error('Lab data not loaded');
    return;
  }
  
  const container = document.getElementById('labsContainer');
  if (!container) return;
  
  container.innerHTML = labs.map(lab => createLabCard(lab)).join('');
}

// Create individual lab card HTML
function createLabCard(lab) {
  const isLive = lab.status === 'live';
  
  return `
    <div class="lab-card ${lab.status}">
      <div class="lab-header">
        <h3><i class="${lab.icon}"></i> ${lab.title}</h3>
        <span class="lab-badge ${lab.status}">
          ${isLive ? '🟢 Live' : '🟡 Coming Soon'}
        </span>
      </div>
      
      <p class="lab-description">${lab.description}</p>
      
      <div class="lab-stats">
        <span><i class="fas fa-users"></i> ${lab.users || 0} users</span>
        <span><i class="fas fa-clock"></i> Updated ${lab.lastUpdated || 'recently'}</span>
      </div>
      
      <div class="lab-actions">
        ${isLive ? 
          `<a href="${lab.url}" target="_blank" rel="noopener" class="lab-launch-btn">
            <i class="fas fa-external-link-alt"></i> Launch Lab
          </a>` : 
          '<span class="lab-launch-btn disabled">Coming Soon</span>'
        }
      </div>
    </div>
  `;
}

// Search functionality
function searchCourses() {
  const searchTerm = document.getElementById('searchInput').value.toLowerCase();
  filterAndDisplayCourses();
}

// Filter courses by category and difficulty
function filterCourses() {
  const categoryFilter = document.getElementById('categoryFilter').value;
  const difficultyFilter = document.getElementById('difficultyFilter').value;
  
  currentCategory = categoryFilter;
  currentDifficulty = difficultyFilter;
  
  filterAndDisplayCourses();
}

// Apply all filters and display results
function filterAndDisplayCourses() {
  const searchTerm = document.getElementById('searchInput')?.value.toLowerCase() || '';
  
  filteredCourses = allCourses.filter(course => {
    // Search filter
    const matchesSearch = !searchTerm || 
      course.title.toLowerCase().includes(searchTerm) ||
      course.description.toLowerCase().includes(searchTerm) ||
      (course.tags && course.tags.some(tag => tag.toLowerCase().includes(searchTerm)));
    
    // Category filter
    const matchesCategory = currentCategory === 'All Courses' || course.category === currentCategory;
    
    // Difficulty filter
    const matchesDifficulty = !currentDifficulty || course.difficulty === currentDifficulty;
    
    return matchesSearch && matchesCategory && matchesDifficulty;
  });
  
  displayCourses();
  updateCourseCount();
}

// Update course count display
function updateCourseCount() {
  const visibleCount = document.getElementById('visibleCount');
  const totalCount = document.getElementById('totalCount');
  
  if (visibleCount) visibleCount.textContent = filteredCourses.length;
  if (totalCount) totalCount.textContent = allCourses.length;
}

// Toggle view between grid and list
function toggleView(view, event) {
  if (event) {
    // Update button states
    document.querySelectorAll('.view-btn').forEach(btn => {
      btn.classList.remove('active');
      btn.setAttribute('aria-pressed', 'false');
    });
    event.target.closest('.view-btn').classList.add('active');
    event.target.closest('.view-btn').setAttribute('aria-pressed', 'true');
  }
  
  currentView = view;
  const container = document.getElementById('courseContainer');
  if (container) {
    container.className = view === 'list' ? 'courses-list' : 'courses-grid';
  }
  
  // Refresh display
  displayCourses();
}

// Toggle course details expansion
function toggleCourseDetails(courseId) {
  const detailsElement = document.getElementById(`details-${courseId}`);
  const card = document.querySelector(`[data-course-id="${courseId}"]`);
  const expandBtn = card.querySelector('.expand-btn i');
  
  if (detailsElement.style.display === 'block') {
    detailsElement.style.display = 'none';
    expandBtn.className = 'fas fa-chevron-down';
    card.classList.remove('expanded');
  } else {
    detailsElement.style.display = 'block';
    expandBtn.className = 'fas fa-chevron-up';
    card.classList.add('expanded');
  }
}

// Toggle course selection for comparison
function toggleCourseSelection(courseId) {
  const index = selectedCourses.indexOf(courseId);
  if (index > -1) {
    selectedCourses.splice(index, 1);
  } else {
    selectedCourses.push(courseId);
  }
  
  updateCompareButton();
}

// Update compare button state
function updateCompareButton() {
  const compareCount = document.getElementById('compareCount');
  const compareBtn = document.getElementById('compareBtn');
  
  if (compareCount) compareCount.textContent = selectedCourses.length;
  if (compareBtn) {
    compareBtn.disabled = selectedCourses.length < 2;
    compareBtn.className = selectedCourses.length >= 2 ? 'compare-btn active' : 'compare-btn';
  }
}

// Bookmark functionality
async function toggleBookmark(courseId) {
  if (!currentUser) {
    openAuthModal('login');
    return;
  }
  
  const isBookmarked = userBookmarks.includes(courseId);
  
  try {
    if (isBookmarked) {
      // Remove bookmark
      userBookmarks = userBookmarks.filter(id => id !== courseId);
      await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), {
        bookmarks: window.arrayRemove(courseId)
      });
    } else {
      // Add bookmark
      userBookmarks.push(courseId);
      await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), {
        bookmarks: window.arrayUnion(courseId)
      });
    }
    
    refreshCourseDisplay();
    showNotification(isBookmarked ? 'Bookmark removed' : 'Course bookmarked!', 'success');
  } catch (error) {
    console.error('Bookmark error:', error);
    showNotification('Error updating bookmark', 'error');
  }
}

// Load user bookmarks from Firebase
async function loadUserBookmarks() {
  if (!currentUser) return;
  
  try {
    const userDoc = await window.getDoc(window.doc(window.db, 'users', currentUser.uid));
    if (userDoc.exists()) {
      const userData = userDoc.data();
      userBookmarks = userData.bookmarks || [];
    }
  } catch (error) {
    console.error('Error loading bookmarks:', error);
  }
}

// Section navigation
function showSection(sectionId) {
  // Hide all sections
  const sections = ['courses', 'labs', 'notes'];
  sections.forEach(section => {
    const element = document.getElementById(section);
    if (element) {
      element.style.display = 'none';
    }
  });
  
  // Show selected section
  const targetSection = document.getElementById(sectionId);
  if (targetSection) {
    targetSection.style.display = 'block';
  }
  
  // Update navigation
  document.querySelectorAll('.nav-link').forEach(link => {
    link.classList.remove('active');
  });
  document.querySelector(`[href="#${sectionId}"]`)?.classList.add('active');
  
  // Scroll to section
  if (targetSection) {
    targetSection.scrollIntoView({ behavior: 'smooth' });
  }
}

// Theme toggle functionality
function initializeTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
  const themeIcon = document.getElementById('themeIcon');
  if (themeIcon) {
    themeIcon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
}

// Mobile menu toggle
function toggleMobileMenu() {
  const navMenu = document.getElementById('navMenu');
  const mobileToggle = document.querySelector('.mobile-toggle');
  
  if (navMenu && mobileToggle) {
    navMenu.classList.toggle('active');
    mobileToggle.classList.toggle('active');
  }
}

// User dropdown toggle
function toggleUserDropdown() {
  const dropdown = document.getElementById('userDropdown');
  if (dropdown) {
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
  }
}

// Authentication UI updates
function updateAuthUI() {
  const loggedOutMenu = document.getElementById('logged-out-menu');
  const loggedInMenu = document.getElementById('logged-in-menu');
  
  if (currentUser) {
    if (loggedOutMenu) loggedOutMenu.style.display = 'none';
    if (loggedInMenu) loggedInMenu.style.display = 'flex';
    
    // Update user display
    const userDisplay = document.getElementById('user-display');
    if (userDisplay) {
      const displayName = currentUser.displayName || currentUser.email.split('@')[0];
      userDisplay.textContent = `Welcome, ${displayName}!`;
    }
    
    // Update user photo/initials
    updateUserPhoto(currentUser.photoURL);
    updateUserInitials(currentUser.displayName || currentUser.email);
  } else {
    if (loggedOutMenu) loggedOutMenu.style.display = 'flex';
    if (loggedInMenu) loggedInMenu.style.display = 'none';
  }
}

// Update user photo
function updateUserPhoto(photoURL) {
  const userPhoto = document.getElementById('user-photo');
  const userInitials = document.getElementById('user-initials');
  
  if (photoURL && userPhoto && userInitials) {
    userPhoto.src = photoURL;
    userPhoto.style.display = 'block';
    userInitials.style.display = 'none';
  } else if (userPhoto && userInitials) {
    userPhoto.style.display = 'none';
    userInitials.style.display = 'flex';
  }
}

// Update user initials
function updateUserInitials(name) {
  const userInitials = document.getElementById('user-initials');
  if (userInitials && name) {
    const initials = name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase();
    userInitials.textContent = initials;
  }
}

// Logout functionality
async function logout() {
  try {
    await window.signOut(window.auth);
    showNotification('Logged out successfully', 'success');
  } catch (error) {
    console.error('Logout error:', error);
    showNotification('Error logging out', 'error');
  }
}

// Refresh course display
function refreshCourseDisplay() {
  setTimeout(() => {
    displayCourses();
  }, 100);
}

// Modal functions (placeholder - implement based on your existing modal system)
function openAuthModal(type) {
  console.log(`Opening ${type} modal`);
  // Implement your authentication modal logic here
}

function closeAuthModal() {
  console.log('Closing auth modal');
  // Implement your modal closing logic here
}

function openDashboard() {
  console.log('Opening dashboard');
  // Implement your dashboard logic here
}

function closeDashboard() {
  console.log('Closing dashboard');
  // Implement your dashboard closing logic here
}

function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) modal.style.display = 'block';
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) modal.style.display = 'none';
}

// Notification system
function showNotification(message, type = 'info') {
  // Create notification element
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.textContent = message;
  
  // Style the notification
  Object.assign(notification.style, {
    position: 'fixed',
    top: '20px',
    right: '20px',
    padding: '1rem 1.5rem',
    borderRadius: '8px',
    color: 'white',
    backgroundColor: type === 'success' ? '#2ecc71' : type === 'error' ? '#e74c3c' : '#3498db',
    zIndex: '10000',
    transform: 'translateX(100%)',
    transition: 'transform 0.3s ease'
  });
  
  document.body.appendChild(notification);
  
  // Animate in
  setTimeout(() => {
    notification.style.transform = 'translateX(0)';
  }, 100);
  
  // Remove after 3 seconds
  setTimeout(() => {
    notification.style.transform = 'translateX(100%)';
    setTimeout(() => {
      if (notification.parentNode) {
        notification.parentNode.removeChild(notification);
      }
    }, 300);
  }, 3000);
}

// Setup event listeners
function setupEventListeners() {
  // Close dropdowns when clicking outside
  document.addEventListener('click', function(event) {
    const userDropdown = document.getElementById('userDropdown');
    const userAvatar = document.querySelector('.user-avatar');
    
    if (userDropdown && !userAvatar?.contains(event.target)) {
      userDropdown.style.display = 'none';
    }
  });
  
  // Handle escape key for modals
  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
      document.querySelectorAll('.modal').forEach(modal => {
        modal.style.display = 'none';
      });
    }
  });
}