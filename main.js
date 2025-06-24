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

// Firebase auth variables (managed by Firebase script in HTML)
let currentUser = null;
let userNotes = '';

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
  displayPopularCourses();
  updateCourseCount();
  setupEventListeners();
  initializeTheme();
  setupFirebaseAuth();
  
  console.log('✅ ImpactMojo initialized successfully!');
}

// ===== FIREBASE AUTH SETUP =====
function setupFirebaseAuth() {
  if (typeof window.auth === 'undefined') {
    console.warn('Firebase not yet loaded, retrying...');
    setTimeout(setupFirebaseAuth, 1000);
    return;
  }

  // Authentication state observer
  window.onAuthStateChanged(window.auth, async (user) => {
    currentUser = user;
    
    if (user) {
      // User is signed in
      console.log('User signed in:', user.email);
      
      // Update UI
      document.getElementById('authButtons').style.display = 'none';
      document.getElementById('userMenu').style.display = 'block';
      document.getElementById('userDisplayName').textContent = user.displayName || user.email.split('@')[0];
      document.getElementById('userEmail').textContent = user.email;
      
      // Load user data
      await loadUserData(user.uid);
      
      showNotification('Welcome back!', 'success');
    } else {
      // User is signed out
      console.log('User signed out');
      
      // Update UI
      document.getElementById('authButtons').style.display = 'flex';
      document.getElementById('userMenu').style.display = 'none';
      
      // Clear user data
      userBookmarks = [];
      userLabBookmarks = [];
      userNotes = '';
    }
  });
}

// Load user data from Firestore
async function loadUserData(userId) {
  try {
    const userDoc = await window.getDoc(window.doc(window.db, 'users', userId));
    if (userDoc.exists()) {
      const userData = userDoc.data();
      userBookmarks = userData.bookmarks || [];
      userLabBookmarks = userData.labBookmarks || [];
      userNotes = userData.notes || '';
      
      // Update UI to reflect loaded bookmarks
      updateAllBookmarkStates();
      updateAllLabBookmarkStates();
    }
  } catch (error) {
    console.error('Error loading user data:', error);
  }
}

// ===== THEME FUNCTIONS - Fix Issue 3: Dark/light toggle with sun/moon icons =====
function initializeTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
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

// ===== AUTHENTICATION FUNCTIONS - Fix Issue 4: Login/signup functionality =====
function showLoginModal() {
  const modal = document.getElementById('loginModal');
  if (modal) {
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
}

function showSignupModal() {
  const modal = document.getElementById('signupModal');
  if (modal) {
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

async function login(event) {
  event.preventDefault();
  
  const email = document.getElementById('loginEmail').value;
  const password = document.getElementById('loginPassword').value;
  
  try {
    await window.signInWithEmailAndPassword(window.auth, email, password);
    closeModal('loginModal');
    document.getElementById('loginEmail').value = '';
    document.getElementById('loginPassword').value = '';
  } catch (error) {
    console.error('Login error:', error);
    showNotification(getErrorMessage(error), 'error');
  }
}

async function signup(event) {
  event.preventDefault();
  
  const name = document.getElementById('signupName').value;
  const email = document.getElementById('signupEmail').value;
  const password = document.getElementById('signupPassword').value;
  
  try {
    const userCredential = await window.createUserWithEmailAndPassword(window.auth, email, password);
    const user = userCredential.user;
    
    // Create user document in Firestore
    await window.setDoc(window.doc(window.db, 'users', user.uid), {
      displayName: name,
      email: email,
      createdAt: new Date(),
      bookmarks: [],
      labBookmarks: [],
      notes: '',
      progress: {}
    });
    
    closeModal('signupModal');
    showNotification('Account created successfully!', 'success');
    
    // Clear form
    document.getElementById('signupName').value = '';
    document.getElementById('signupEmail').value = '';
    document.getElementById('signupPassword').value = '';
  } catch (error) {
    console.error('Signup error:', error);
    showNotification(getErrorMessage(error), 'error');
  }
}

async function signInWithGoogle() {
  try {
    const result = await window.signInWithPopup(window.auth, window.provider);
    const user = result.user;
    
    // Check if user document exists, create if not
    const userDoc = await window.getDoc(window.doc(window.db, 'users', user.uid));
    if (!userDoc.exists()) {
      await window.setDoc(window.doc(window.db, 'users', user.uid), {
        displayName: user.displayName,
        email: user.email,
        createdAt: new Date(),
        bookmarks: [],
        labBookmarks: [],
        notes: '',
        progress: {}
      });
    }
    
    closeModal('loginModal');
    closeModal('signupModal');
    showNotification('Successfully signed in with Google!', 'success');
  } catch (error) {
    console.error('Google sign-in error:', error);
    showNotification(getErrorMessage(error), 'error');
  }
}

async function logout() {
  try {
    await window.signOut(window.auth);
    showNotification('Successfully logged out!', 'success');
  } catch (error) {
    console.error('Logout error:', error);
    showNotification('Error logging out', 'error');
  }
}

function getErrorMessage(error) {
  switch (error.code) {
    case 'auth/user-not-found':
      return 'No account found with this email address.';
    case 'auth/wrong-password':
      return 'Incorrect password.';
    case 'auth/email-already-in-use':
      return 'An account already exists with this email address.';
    case 'auth/weak-password':
      return 'Password should be at least 6 characters.';
    case 'auth/invalid-email':
      return 'Please enter a valid email address.';
    case 'auth/too-many-requests':
      return 'Too many failed attempts. Please try again later.';
    default:
      return error.message || 'An error occurred. Please try again.';
  }
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
  
  container.innerHTML = filteredCourses.map(course => createCourseCard(course)).join('');
  
  // Update bookmark states
  updateAllBookmarkStates();
}

function displayPopularCourses() {
  const container = document.getElementById('popularContainer');
  
  if (!container) {
    return;
  }
  
  // Get top 6 most popular courses by learner count
  const popularCourses = [...courses]
    .sort((a, b) => b.learnerCount - a.learnerCount)
    .slice(0, 6);
  
  container.innerHTML = popularCourses.map(course => createCourseCard(course)).join('');
}

function createCourseCard(course) {
  const isBookmarked = userBookmarks.includes(course.id);
  const isSelected = selectedCourses.includes(course.id);
  
  return `
    <div class="course-card" data-course-id="${course.id}" data-category="${course.category}">
      <div class="course-header">
        <div class="course-icon">
          <i class="${course.icon}"></i>
        </div>
        <div class="course-number">#${course.number || courses.indexOf(course) + 1}</div>
      </div>
      
      <div class="course-content">
        <h3 class="course-title">${course.title}</h3>
        <p class="course-description">${course.description}</p>
        
        <div class="course-meta">
          <span class="course-category">${course.category}</span>
          <span class="course-difficulty ${course.difficulty}">${course.difficulty}</span>
          <span class="course-duration">${course.duration}</span>
        </div>
        
        <div class="course-stats">
          <div class="stat">
            <i class="fas fa-users"></i>
            <span>${course.learnerCount.toLocaleString()} learners</span>
          </div>
          <div class="stat">
            <i class="fas fa-star"></i>
            <span>${course.rating}/5</span>
          </div>
        </div>
      </div>
      
      <div class="course-actions">
        <a href="${course.url}" target="_blank" rel="noopener" class="launch-btn">
          Launch
        </a>
        
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
    container.innerHTML = '<div class="error">Unable to load labs.</div>';
    return;
  }
  
  container.innerHTML = labs.map(lab => createLabCard(lab)).join('');
  
  // Update lab bookmark states
  updateAllLabBookmarkStates();
}

function createLabCard(lab) {
  const isBookmarked = userLabBookmarks.includes(lab.id);
  const isSelected = selectedLabs.includes(lab.id);
  
  return `
    <div class="lab-card" data-lab-id="${lab.id}">
      <div class="lab-header">
        <div class="lab-icon">
          <i class="${lab.icon}"></i>
        </div>
        <div class="lab-status ${lab.status}">
          ${lab.status === 'live' ? 'LIVE' : 'COMING SOON'}
        </div>
      </div>
      
      <div class="lab-content">
        <h3 class="lab-title">${lab.title}</h3>
        <p class="lab-description">${lab.description}</p>
        <div class="lab-category">${lab.category}</div>
      </div>
      
      <div class="lab-actions">
        <a href="${lab.url}" target="_blank" rel="noopener" class="lab-launch-btn ${lab.status !== 'live' ? 'disabled' : ''}">
          ${lab.status === 'live' ? 'Launch' : 'Coming Soon'}
        </a>
        
        <div class="lab-actions-right">
          <button class="lab-bookmark-btn ${isBookmarked ? 'bookmarked' : ''}" 
                  onclick="toggleLabBookmark('${lab.id}')" 
                  title="${isBookmarked ? 'Remove bookmark' : 'Bookmark lab'}">
            <i class="${isBookmarked ? 'fas' : 'far'} fa-bookmark"></i>
          </button>
          <input type="checkbox" id="lab-compare-${lab.id}" 
                 ${isSelected ? 'checked' : ''} 
                 onchange="toggleLabSelection('${lab.id}')"
                 aria-label="Select lab for comparison">
          <label for="lab-compare-${lab.id}" class="compare-checkbox">Compare</label>
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
  
  // If user is logged in, save to Firestore
  if (currentUser) {
    saveUserBookmarks();
  }
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
  
  // If user is logged in, save to Firestore
  if (currentUser) {
    saveUserLabBookmarks();
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

function updateAllBookmarkStates() {
  userBookmarks.forEach(courseId => {
    updateBookmarkUI(courseId);
  });
}

function updateAllLabBookmarkStates() {
  userLabBookmarks.forEach(labId => {
    updateLabBookmarkUI(labId);
  });
}

// ===== FIREBASE SAVE FUNCTIONS =====
async function saveUserBookmarks() {
  if (!currentUser) return;
  
  try {
    const userRef = window.doc(window.db, 'users', currentUser.uid);
    await window.updateDoc(userRef, {
      bookmarks: userBookmarks
    });
  } catch (error) {
    console.error('Error saving bookmarks:', error);
  }
}

async function saveUserLabBookmarks() {
  if (!currentUser) return;
  
  try {
    const userRef = window.doc(window.db, 'users', currentUser.uid);
    await window.updateDoc(userRef, {
      labBookmarks: userLabBookmarks
    });
  } catch (error) {
    console.error('Error saving lab bookmarks:', error);
  }
}

// ===== COURSE SELECTION AND COMPARISON =====
function toggleCourseSelection(courseId) {
  const index = selectedCourses.indexOf(courseId);
  
  if (index > -1) {
    selectedCourses.splice(index, 1);
  } else {
    selectedCourses.push(courseId);
  }
  
  updateComparisonUI();
}

function toggleLabSelection(labId) {
  const index = selectedLabs.indexOf(labId);
  
  if (index > -1) {
    selectedLabs.splice(index, 1);
  } else {
    selectedLabs.push(labId);
  }
  
  updateLabComparisonUI();
}

function updateComparisonUI() {
  const compareBtn = document.getElementById('compareBtn');
  const compareCount = document.getElementById('compareCount');
  
  if (compareBtn && compareCount) {
    compareCount.textContent = selectedCourses.length;
    compareBtn.disabled = selectedCourses.length < 2;
  }
}

function updateLabComparisonUI() {
  // Lab comparison UI can be added if needed
  console.log(`${selectedLabs.length} labs selected for comparison`);
  
  // If you want to add a lab comparison button, implement it here
  if (selectedLabs.length >= 2) {
    showLabComparison();
  }
}

// ===== COMPARISON MODALS - Fix Issue 9 & 14 =====
function showComparison() {
  if (selectedCourses.length < 2) {
    showNotification('Please select at least 2 courses to compare', 'warning');
    return;
  }
  
  const modal = document.getElementById('comparisonModal');
  const content = document.getElementById('comparisonContent');
  
  if (!modal || !content) return;
  
  // Get selected course data
  const coursesToCompare = courses.filter(course => selectedCourses.includes(course.id));
  
  // Generate comparison content
  content.innerHTML = createCourseComparison(coursesToCompare);
  
  modal.style.display = 'block';
  document.body.style.overflow = 'hidden';
}

// Fix Issue 14: Lab comparison functionality
function showLabComparison() {
  if (selectedLabs.length < 2) {
    showNotification('Please select at least 2 labs to compare', 'warning');
    return;
  }
  
  const modal = document.getElementById('labComparisonModal');
  const content = document.getElementById('labComparisonContent');
  
  if (!modal || !content) return;
  
  // Get selected lab data
  const labsToCompare = labs.filter(lab => selectedLabs.includes(lab.id));
  
  // Generate comparison content
  content.innerHTML = createLabComparison(labsToCompare);
  
  modal.style.display = 'block';
  document.body.style.overflow = 'hidden';
}

function createCourseComparison(courses) {
  const contentDepthAnalysis = analyzeContentDepth(courses);
  const overlapAnalysis = analyzeContentOverlap(courses);
  
  return `
    <div class="comparison-overview">
      ${courses.map((course, index) => `
        <div class="comparison-course-card">
          <div class="comparison-course-title">${course.title}</div>
          <div class="comparison-quick-stats">
            ${course.category} • ${course.difficulty} • ${course.rating}/5
          </div>
        </div>
      `).join('')}
    </div>
    
    <div class="comparison-section">
      <h3>📊 Basic Comparison</h3>
      <div style="overflow-x: auto;">
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
              ${courses.map(course => `<td><span class="difficulty ${course.difficulty}">${course.difficulty}</span></td>`).join('')}
            </tr>
            <tr>
              <td><strong>Duration</strong></td>
              ${courses.map(course => `<td>${course.duration}</td>`).join('')}
            </tr>
            <tr>
              <td><strong>Rating</strong></td>
              ${courses.map(course => `<td><span class="rating">${course.rating}/5</span></td>`).join('')}
            </tr>
            <tr>
              <td><strong>Learners</strong></td>
              ${courses.map(course => `<td>${course.learnerCount.toLocaleString()}</td>`).join('')}
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <div class="comparison-section">
      <h3>🎯 Content Depth Analysis</h3>
      <div class="content-depth-analysis">
        ${contentDepthAnalysis.map(analysis => `
          <div class="depth-card">
            <h4>${analysis.title}</h4>
            <div class="depth-indicator">
              <span>Prerequisites:</span>
              <div class="depth-bar">
                <div class="depth-fill" style="width: ${analysis.prerequisiteDepth}%"></div>
              </div>
              <span>${analysis.prerequisiteDepth}%</span>
            </div>
            <div class="depth-indicator">
              <span>Outcomes:</span>
              <div class="depth-bar">
                <div class="depth-fill" style="width: ${analysis.outcomeDepth}%"></div>
              </div>
              <span>${analysis.outcomeDepth}%</span>
            </div>
            <div class="depth-indicator">
              <span>Complexity:</span>
              <div class="depth-bar">
                <div class="depth-fill" style="width: ${analysis.complexityScore}%"></div>
              </div>
              <span>${analysis.complexityScore}%</span>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
    
    <div class="overlap-analysis">
      <h3>🔗 Content Overlap Analysis</h3>
      <p><strong>Common Topics:</strong></p>
      <div class="overlap-items">
        ${overlapAnalysis.commonTopics.map(topic => `
          <span class="overlap-tag">${topic}</span>
        `).join('')}
      </div>
      <p style="margin-top: 16px;"><strong>Learning Path Suggestion:</strong> ${overlapAnalysis.learningPath}</p>
    </div>
  `;
}

function createLabComparison(labs) {
  return `
    <div class="comparison-overview">
      ${labs.map((lab, index) => `
        <div class="comparison-course-card">
          <div class="comparison-course-title">${lab.title}</div>
          <div class="comparison-quick-stats">
            ${lab.category} • ${lab.status}
          </div>
        </div>
      `).join('')}
    </div>
    
    <div class="comparison-section">
      <h3>🧪 Lab Comparison</h3>
      <div style="overflow-x: auto;">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>Aspect</th>
              ${labs.map(lab => `<th>${lab.title}</th>`).join('')}
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Category</strong></td>
              ${labs.map(lab => `<td>${lab.category}</td>`).join('')}
            </tr>
            <tr>
              <td><strong>Status</strong></td>
              ${labs.map(lab => `<td><span class="lab-status ${lab.status}">${lab.status}</span></td>`).join('')}
            </tr>
            <tr>
              <td><strong>Description</strong></td>
              ${labs.map(lab => `<td>${lab.description}</td>`).join('')}
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <div class="comparison-section">
      <h3>🔧 Feature Analysis</h3>
      <div class="content-depth-analysis">
        ${labs.map(lab => `
          <div class="depth-card">
            <h4>${lab.title}</h4>
            <p><strong>Purpose:</strong> ${lab.description}</p>
            <p><strong>Category:</strong> ${lab.category}</p>
            <p><strong>Status:</strong> ${lab.status}</p>
            <div style="margin-top: 1rem;">
              <a href="${lab.url}" target="_blank" class="btn btn-primary" ${lab.status !== 'live' ? 'style="pointer-events: none; opacity: 0.5;"' : ''}>
                ${lab.status === 'live' ? 'Launch Lab' : 'Coming Soon'}
              </a>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

// ===== SEARCH AND FILTER FUNCTIONS =====
function filterCourses() {
  const searchTerm = document.getElementById('searchInput')?.value.toLowerCase() || '';
  const categoryFilter = document.getElementById('categoryFilter')?.value || '';
  const difficultyFilter = document.getElementById('difficultyFilter')?.value || '';
  const sortBy = document.getElementById('sortBy')?.value || 'popularity';
  
  // Filter courses
  filteredCourses = allCourses.filter(course => {
    const matchesSearch = !searchTerm || 
      course.title.toLowerCase().includes(searchTerm) ||
      course.description.toLowerCase().includes(searchTerm) ||
      course.category.toLowerCase().includes(searchTerm);
    
    const matchesCategory = !categoryFilter || course.category === categoryFilter;
    const matchesDifficulty = !difficultyFilter || course.difficulty === difficultyFilter;
    
    return matchesSearch && matchesCategory && matchesDifficulty;
  });
  
  // Sort courses
  switch (sortBy) {
    case 'title':
      filteredCourses.sort((a, b) => a.title.localeCompare(b.title));
      break;
    case 'rating':
      filteredCourses.sort((a, b) => b.rating - a.rating);
      break;
    case 'recent':
      filteredCourses.sort((a, b) => (b.number || 0) - (a.number || 0));
      break;
    case 'popularity':
    default:
      filteredCourses.sort((a, b) => b.learnerCount - a.learnerCount);
      break;
  }
  
  displayCourses();
  updateCourseCount();
}

function updateCourseCount() {
  const countElement = document.getElementById('courseCount');
  if (countElement) {
    const total = allCourses.length;
    const filtered = filteredCourses.length;
    
    if (filtered === total) {
      countElement.textContent = `${total} courses available`;
    } else {
      countElement.textContent = `${filtered} of ${total} courses`;
    }
  }
}

// ===== ANALYSIS FUNCTIONS =====
function analyzeContentDepth(courses) {
  return courses.map(course => {
    const prerequisiteDepth = Math.min(100, course.prerequisites.length * 20);
    const outcomeDepth = Math.min(100, course.outcomes.length * 15);
    const difficultyMultiplier = course.difficulty === 'beginner' ? 1 : course.difficulty === 'intermediate' ? 1.5 : 2;
    const complexityScore = Math.min(100, ((prerequisiteDepth + outcomeDepth) / 2) * difficultyMultiplier);
    
    return {
      title: course.title,
      prerequisiteDepth,
      outcomeDepth,
      complexityScore: Math.round(complexityScore)
    };
  });
}

function analyzeContentOverlap(courses) {
  const allTopics = courses.flatMap(course => [
    course.category,
    ...course.prerequisites.flatMap(p => p.split(' ')),
    ...course.outcomes.flatMap(o => o.split(' '))
  ]);
  
  const topicCounts = {};
  allTopics.forEach(topic => {
    const cleanTopic = topic.toLowerCase().replace(/[^a-z]/g, '');
    if (cleanTopic.length > 3) {
      topicCounts[cleanTopic] = (topicCounts[cleanTopic] || 0) + 1;
    }
  });
  
  const commonTopics = Object.entries(topicCounts)
    .filter(([topic, count]) => count >= 2)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8)
    .map(([topic]) => topic);
  
  const learningPath = determineLearningPath(courses);
  
  return {
    commonTopics,
    learningPath
  };
}

function determineLearningPath(courses) {
  const sortedCourses = courses.sort((a, b) => {
    const difficultyOrder = { beginner: 1, intermediate: 2, advanced: 3 };
    return difficultyOrder[a.difficulty] - difficultyOrder[b.difficulty];
  });
  
  return `Start with "${sortedCourses[0].title}" and progress to "${sortedCourses[sortedCourses.length - 1].title}" for optimal learning sequence.`;
}

// ===== DASHBOARD FUNCTIONS =====
function showDashboard() {
  const modal = document.getElementById('dashboardModal');
  const content = document.getElementById('dashboardContent');
  
  if (!modal || !content) return;
  
  content.innerHTML = `
    <div class="dashboard-stats">
      <div class="stat-card">
        <h3>Bookmarked Courses</h3>
        <p class="stat-number">${userBookmarks.length}</p>
      </div>
      <div class="stat-card">
        <h3>Bookmarked Labs</h3>
        <p class="stat-number">${userLabBookmarks.length}</p>
      </div>
    </div>
    <div class="dashboard-section">
      <h3>Your Notes</h3>
      <textarea id="userNotesTextarea" placeholder="Add your notes here..." rows="4" style="width: 100%; padding: 1rem; border: 1px solid var(--border-color); border-radius: 0.5rem;">${userNotes}</textarea>
      <button onclick="saveNotes()" class="btn btn-primary" style="margin-top: 1rem;">Save Notes</button>
    </div>
  `;
  
  modal.style.display = 'block';
  document.body.style.overflow = 'hidden';
}

function showBookmarks() {
  // Filter courses by bookmarked IDs
  const bookmarkedCourses = courses.filter(course => userBookmarks.includes(course.id));
  const bookmarkedLabs = labs.filter(lab => userLabBookmarks.includes(lab.id));
  
  showNotification(`You have ${bookmarkedCourses.length} bookmarked courses and ${bookmarkedLabs.length} bookmarked labs`, 'info');
}

function showProfile() {
  if (!currentUser) return;
  
  const profileInfo = `Email: ${currentUser.email}\nMember since: ${currentUser.metadata?.creationTime ? new Date(currentUser.metadata.creationTime).toLocaleDateString() : 'Unknown'}\nBookmarks: ${userBookmarks.length} courses, ${userLabBookmarks.length} labs`;
  
  showNotification('Profile: ' + profileInfo, 'info');
}

async function saveNotes() {
  if (!currentUser) {
    showNotification('Please log in to save notes', 'error');
    return;
  }
  
  const notes = document.getElementById('userNotesTextarea')?.value || '';
  
  try {
    const userRef = window.doc(window.db, 'users', currentUser.uid);
    await window.updateDoc(userRef, { notes: notes });
    userNotes = notes;
    showNotification('Notes saved successfully', 'success');
  } catch (error) {
    console.error('Error saving notes:', error);
    showNotification('Error saving notes', 'error');
  }
}

// ===== UTILITY FUNCTIONS =====
function showNotification(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.textContent = message;
  
  const container = document.getElementById('notificationContainer') || document.body;
  container.appendChild(notification);
  
  setTimeout(() => {
    if (notification.parentNode) {
      notification.parentNode.removeChild(notification);
    }
  }, 5000);
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
      event.target.style.display = 'none';
      document.body.style.overflow = '';
    }
  };
  
  // Escape key to close modals
  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
      const modals = document.querySelectorAll('.modal[style*="block"]');
      modals.forEach(modal => {
        modal.style.display = 'none';
        document.body.style.overflow = '';
      });
    }
  });
}

// ===== INITIALIZATION =====
// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  initializeApp();
});

// Also initialize if DOM is already loaded
if (document.readyState !== 'loading') {
  initializeApp();
}

console.log('✅ ImpactMojo Main JavaScript loaded successfully!');