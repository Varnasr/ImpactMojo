// ===== CLEAN FIREBASE ERROR HANDLING =====
// Add this to the very TOP of main.js (before any other code)

console.log('🚀 Loading ImpactMojo Main JS with Firebase...');

// Initialize Firebase state tracking
window.firebaseAvailable = false;
window.userAuthenticated = false;

// Check if Firebase is properly loaded
function initializeFirebase() {
  try {
    if (typeof firebase !== 'undefined' && firebase.apps && firebase.auth) {
      console.log('✅ Firebase available, initializing auth...');
      window.firebaseAvailable = true;
      
      // Your existing Firebase initialization code goes here
      // firebase.auth().onAuthStateChanged(user => { ... });
      
    } else {
      console.log('⚠️ Firebase not available, running in standalone mode');
      window.firebaseAvailable = false;
      // Show auth buttons but disable their functionality
      showAuthUIFallback();
    }
  } catch (error) {
    console.log('⚠️ Firebase initialization failed, running in standalone mode:', error.message);
    window.firebaseAvailable = false;
    showAuthUIFallback();
  }
}

// Fallback auth UI for when Firebase isn't available
function showAuthUIFallback() {
  console.log('🔧 Setting up fallback auth UI...');
  
  // Show auth buttons but make them informational
  const authButtons = document.querySelectorAll('.auth-btn');
  authButtons.forEach(btn => {
    btn.style.opacity = '0.7';
    btn.onclick = function() {
      alert('Authentication temporarily unavailable. Core features still work!');
    };
  });
  
  console.log('✅ Fallback auth UI ready');
}

// Safe Firebase function wrapper
function withFirebase(callback, fallback = null) {
  if (window.firebaseAvailable) {
    return callback();
  } else {
    console.log('🔄 Firebase not available, using fallback');
    return fallback ? fallback() : null;
  }
}

// Initialize Firebase (safely)
initializeFirebase();

// Continue with your existing main.js code below...
// Just wrap any Firebase-dependent code with withFirebase()
// ===== COMPLETE IMPACTMOJO MAIN.JS WITH FIREBASE =====
// Initialize global variables immediately
window.userBookmarks = window.userBookmarks || [];
window.selectedForComparison = window.selectedForComparison || [];

console.log('🚀 Loading ImpactMojo Main JS with Firebase...');

// ===== FIREBASE CONFIGURATION =====
const firebaseConfig = {
  apiKey: "AIzaSyDnF0eJsTULzOJUnBskybd44dG5w-f46vE",
  authDomain: "impactmojo.firebaseapp.com",
  projectId: "impactmojo",
  storageBucket: "impactmojo.firebasestorage.app",
  messagingSenderId: "529198336589",
  appId: "1:529198336589:web:1664b5344de5bfb31bea04",
  measurementId: "G-ZHPPXXMRGV"
};

// Initialize Firebase (if not already initialized)
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}

// Firebase Auth reference
const auth = firebase.auth();
const provider = new firebase.auth.GoogleAuthProvider();

// ===== GLOBAL VARIABLES =====
let impactMojoAllCourses = [];
let impactMojoFilteredCourses = [];
let impactMojoSelectedCourses = [];
let impactMojoSelectedLabs = [];
let impactMojoUserBookmarks = JSON.parse(localStorage.getItem('impactMojoBookmarks')) || [];
let impactMojoUserLabBookmarks = JSON.parse(localStorage.getItem('impactMojoLabBookmarks')) || [];

// ===== CORE FUNCTIONS (SINGLE DEFINITIONS ONLY) =====

// NOTIFICATION SYSTEM
function showNotification(message, type = 'info') {
  document.querySelectorAll('.notification').forEach(notification => notification.remove());
  
  const notification = document.createElement('div');
  const colors = {
    success: '#10b981',
    warning: '#f59e0b', 
    error: '#ef4444',
    info: '#3b82f6'
  };
  
  notification.style.cssText = `
    position: fixed; top: 20px; right: 20px; z-index: 10001;
    background: ${colors[type]}; color: white; padding: 1rem 1.5rem;
    border-radius: 0.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    font-size: 0.9rem; max-width: 350px; font-family: 'Poppins', sans-serif;
    display: flex; align-items: center; gap: 0.5rem;
  `;
  
  notification.innerHTML = `
    <span>${message}</span>
    <button onclick="this.parentElement.remove()" style="
      background: rgba(255,255,255,0.2); border: none; color: white;
      padding: 4px 8px; border-radius: 4px; cursor: pointer; margin-left: 8px;
      font-size: 0.8rem;
    ">✕</button>
  `;
  
  document.body.appendChild(notification);
  setTimeout(() => notification.remove(), 5000);
}

// MODAL FUNCTIONS
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'flex';
    modal.style.alignItems = 'center';
    modal.style.justifyContent = 'center';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    console.log(`✅ Opened modal: ${modalId}`);
  } else {
    console.warn(`⚠️ Modal not found: ${modalId}`);
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
    console.log(`❌ Closed modal: ${modalId}`);
  }
}

// ENHANCED THEME TOGGLE WITH PROPER NAVBAR INTEGRATION
function toggleTheme() {
  console.log('🎨 Toggling theme...');
  
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  // Apply theme to document
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  // Update theme icon
  if (themeIcon) {
    themeIcon.className = newTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    console.log(`🎨 Theme icon updated: ${themeIcon.className}`);
  }
  
  // Update navbar theme classes
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    navbar.classList.toggle('dark-theme', newTheme === 'dark');
  }
  
  // Update auth buttons theme
  const authButtons = document.querySelectorAll('.auth-btn');
  authButtons.forEach(btn => {
    btn.classList.toggle('dark-theme', newTheme === 'dark');
  });
  
  showNotification(`Switched to ${newTheme} mode`, 'success');
  console.log(`✅ Theme switched to: ${newTheme}`);
}

function initializeThemeToggle() {
  console.log('🎨 Initializing theme system...');
  
  const savedTheme = localStorage.getItem('theme') || 'light';
  const themeIcon = document.getElementById('themeIcon');
  const themeToggleBtn = document.getElementById('themeToggle');
  
  // Apply saved theme
  document.documentElement.setAttribute('data-theme', savedTheme);
  
  // Update theme icon
  if (themeIcon) {
    themeIcon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
  
  // Connect theme toggle button
  if (themeToggleBtn) {
    themeToggleBtn.onclick = toggleTheme;
    console.log('🎨 Theme toggle button connected');
  }
  
  // Apply theme to navbar
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    navbar.classList.toggle('dark-theme', savedTheme === 'dark');
  }
  
  console.log(`✅ Theme initialized: ${savedTheme}`);
}

// FIREBASE AUTH FUNCTIONS
function signInWithGoogle() {
  console.log('🔥 Google sign-in initiated...');
  
  auth.signInWithPopup(provider)
    .then((result) => {
      const user = result.user;
      console.log('✅ Google sign-in successful:', user.displayName);
      showNotification(`Welcome, ${user.displayName}!`, 'success');
      updateAuthUI(user);
      closeModal('loginModal');
      closeModal('signupModal');
    })
    .catch((error) => {
      console.error('❌ Google sign-in failed:', error);
      showNotification('Google sign-in failed. Please try again.', 'error');
    });
}

function login(event) {
  event.preventDefault();
  console.log('🔑 Email login initiated...');
  
  const email = document.getElementById('loginEmail').value;
  const password = document.getElementById('loginPassword').value;
  
  if (!email || !password) {
    showNotification('Please fill in all fields', 'warning');
    return;
  }
  
  auth.signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      const user = userCredential.user;
      console.log('✅ Email login successful:', user.email);
      showNotification(`Welcome back, ${user.email}!`, 'success');
      updateAuthUI(user);
      closeModal('loginModal');
    })
    .catch((error) => {
      console.error('❌ Email login failed:', error);
      let errorMessage = 'Login failed. Please check your credentials.';
      if (error.code === 'auth/user-not-found') {
        errorMessage = 'No account found with this email.';
      } else if (error.code === 'auth/wrong-password') {
        errorMessage = 'Incorrect password.';
      } else if (error.code === 'auth/invalid-email') {
        errorMessage = 'Invalid email address.';
      }
      showNotification(errorMessage, 'error');
    });
}

function signup(event) {
  event.preventDefault();
  console.log('📝 Email signup initiated...');
  
  const name = document.getElementById('signupName').value;
  const email = document.getElementById('signupEmail').value;
  const password = document.getElementById('signupPassword').value;
  
  if (!name || !email || !password) {
    showNotification('Please fill in all fields', 'warning');
    return;
  }
  
  if (password.length < 6) {
    showNotification('Password must be at least 6 characters', 'warning');
    return;
  }
  
  auth.createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      const user = userCredential.user;
      
      // Update user profile with name
      return user.updateProfile({
        displayName: name
      }).then(() => {
        console.log('✅ Email signup successful:', user.email);
        showNotification(`Welcome to ImpactMojo, ${name}!`, 'success');
        updateAuthUI(user);
        closeModal('signupModal');
      });
    })
    .catch((error) => {
      console.error('❌ Email signup failed:', error);
      let errorMessage = 'Signup failed. Please try again.';
      if (error.code === 'auth/email-already-in-use') {
        errorMessage = 'An account with this email already exists.';
      } else if (error.code === 'auth/invalid-email') {
        errorMessage = 'Invalid email address.';
      } else if (error.code === 'auth/weak-password') {
        errorMessage = 'Password is too weak.';
      }
      showNotification(errorMessage, 'error');
    });
}

function logout() {
  console.log('🚪 Logout initiated...');
  
  auth.signOut()
    .then(() => {
      console.log('✅ Logout successful');
      showNotification('You have been logged out', 'info');
      updateAuthUI(null);
    })
    .catch((error) => {
      console.error('❌ Logout failed:', error);
      showNotification('Logout failed', 'error');
    });
}

function updateAuthUI(user) {
  const authButtons = document.getElementById('authButtons');
  const userProfile = document.getElementById('userProfile');
  
  if (user) {
    // User is signed in
    if (authButtons) {
      authButtons.style.display = 'none';
    }
    
    // Create or update user profile display
    if (!userProfile) {
      const profileDiv = document.createElement('div');
      profileDiv.id = 'userProfile';
      profileDiv.style.cssText = `
        display: flex; align-items: center; gap: 1rem;
        background: rgba(255,255,255,0.1); padding: 0.5rem 1rem;
        border-radius: 2rem; backdrop-filter: blur(10px);
      `;
      
      const avatar = user.photoURL ? 
        `<img src="${user.photoURL}" alt="Profile" style="width:32px;height:32px;border-radius:50%;">` :
        `<div style="width:32px;height:32px;border-radius:50%;background:#6366f1;display:flex;align-items:center;justify-content:center;color:white;font-weight:600;">${(user.displayName || user.email)[0].toUpperCase()}</div>`;
      
      profileDiv.innerHTML = `
        ${avatar}
        <span style="color: var(--text-primary); font-weight: 500;">${user.displayName || user.email}</span>
        <button onclick="logout()" style="
          background: rgba(239,68,68,0.1); border: 2px solid #ef4444;
          color: #ef4444; padding: 0.25rem 0.75rem; border-radius: 1rem;
          cursor: pointer; font-size: 0.75rem; font-weight: 500;
        ">Logout</button>
      `;
      
      // Insert profile where auth buttons were
      const navbar = document.querySelector('.navbar');
      if (navbar) {
        navbar.appendChild(profileDiv);
      }
    }
  } else {
    // User is signed out
    if (authButtons) {
      authButtons.style.display = 'flex';
    }
    
    if (userProfile) {
      userProfile.remove();
    }
  }
}

// AUTH MODAL FUNCTIONS
function showLoginModal() {
  createAuthModalsIfNeeded();
  openModal('loginModal');
}

function showSignupModal() {
  createAuthModalsIfNeeded();
  openModal('signupModal');
}

// CREATE AUTH MODALS IF THEY DON'T EXIST
function createAuthModalsIfNeeded() {
  if (!document.getElementById('loginModal')) {
    const loginModal = document.createElement('div');
    loginModal.id = 'loginModal';
    loginModal.className = 'modal';
    loginModal.style.cssText = 'display:none;position:fixed;z-index:10000;left:0;top:0;width:100%;height:100%;background:rgba(0,0,0,0.5);align-items:center;justify-content:center;';
    loginModal.innerHTML = `
      <div class="modal-content" style="background:var(--surface);padding:2rem;border-radius:0.75rem;max-width:400px;width:90%;position:relative;border:1px solid var(--border-color);">
        <span class="close" onclick="closeModal('loginModal')" style="position:absolute;top:1rem;right:1rem;font-size:2rem;cursor:pointer;color:var(--text-secondary);">&times;</span>
        <h2 style="margin-top:0;color:var(--text-primary);">Sign In to ImpactMojo</h2>
        <form onsubmit="login(event)" style="margin:1rem 0;">
          <div style="margin-bottom:1rem;">
            <label style="color:var(--text-primary);font-weight:500;">Email:</label>
            <input type="email" id="loginEmail" required style="width:100%;padding:0.75rem;border:2px solid var(--border-color);border-radius:0.5rem;box-sizing:border-box;background:var(--surface);color:var(--text-primary);margin-top:0.25rem;">
          </div>
          <div style="margin-bottom:1rem;">
            <label style="color:var(--text-primary);font-weight:500;">Password:</label>
            <input type="password" id="loginPassword" required style="width:100%;padding:0.75rem;border:2px solid var(--border-color);border-radius:0.5rem;box-sizing:border-box;background:var(--surface);color:var(--text-primary);margin-top:0.25rem;">
          </div>
          <button type="submit" style="width:100%;background:#6366f1;color:white;border:none;padding:0.75rem;border-radius:0.5rem;cursor:pointer;font-size:1rem;font-weight:600;">Sign In</button>
        </form>
        <div style="text-align:center;margin:1rem 0;"><span style="color:var(--text-secondary);">or</span></div>
        <button onclick="signInWithGoogle()" style="width:100%;background:#db4437;color:white;border:none;padding:0.75rem;border-radius:0.5rem;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;gap:0.5rem;">
          <i class="fab fa-google"></i> Continue with Google
        </button>
        <div style="text-align:center;margin-top:1rem;color:var(--text-secondary);">
          Don't have an account? 
          <a href="#" onclick="closeModal('loginModal'); showSignupModal()" style="color:#6366f1;text-decoration:none;">Sign Up</a>
        </div>
      </div>
    `;
    document.body.appendChild(loginModal);
  }
  
  if (!document.getElementById('signupModal')) {
    const signupModal = document.createElement('div');
    signupModal.id = 'signupModal';
    signupModal.className = 'modal';
    signupModal.style.cssText = 'display:none;position:fixed;z-index:10000;left:0;top:0;width:100%;height:100%;background:rgba(0,0,0,0.5);align-items:center;justify-content:center;';
    signupModal.innerHTML = `
      <div class="modal-content" style="background:var(--surface);padding:2rem;border-radius:0.75rem;max-width:400px;width:90%;position:relative;border:1px solid var(--border-color);">
        <span class="close" onclick="closeModal('signupModal')" style="position:absolute;top:1rem;right:1rem;font-size:2rem;cursor:pointer;color:var(--text-secondary);">&times;</span>
        <h2 style="margin-top:0;color:var(--text-primary);">Join ImpactMojo</h2>
        <form onsubmit="signup(event)" style="margin:1rem 0;">
          <div style="margin-bottom:1rem;">
            <label style="color:var(--text-primary);font-weight:500;">Full Name:</label>
            <input type="text" id="signupName" required style="width:100%;padding:0.75rem;border:2px solid var(--border-color);border-radius:0.5rem;box-sizing:border-box;background:var(--surface);color:var(--text-primary);margin-top:0.25rem;">
          </div>
          <div style="margin-bottom:1rem;">
            <label style="color:var(--text-primary);font-weight:500;">Email:</label>
            <input type="email" id="signupEmail" required style="width:100%;padding:0.75rem;border:2px solid var(--border-color);border-radius:0.5rem;box-sizing:border-box;background:var(--surface);color:var(--text-primary);margin-top:0.25rem;">
          </div>
          <div style="margin-bottom:1rem;">
            <label style="color:var(--text-primary);font-weight:500;">Password:</label>
            <input type="password" id="signupPassword" required minlength="6" style="width:100%;padding:0.75rem;border:2px solid var(--border-color);border-radius:0.5rem;box-sizing:border-box;background:var(--surface);color:var(--text-primary);margin-top:0.25rem;">
          </div>
          <button type="submit" style="width:100%;background:#6366f1;color:white;border:none;padding:0.75rem;border-radius:0.5rem;cursor:pointer;font-size:1rem;font-weight:600;">Create Account</button>
        </form>
        <div style="text-align:center;margin:1rem 0;"><span style="color:var(--text-secondary);">or</span></div>
        <button onclick="signInWithGoogle()" style="width:100%;background:#db4437;color:white;border:none;padding:0.75rem;border-radius:0.5rem;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;gap:0.5rem;">
          <i class="fab fa-google"></i> Continue with Google
        </button>
        <div style="text-align:center;margin-top:1rem;color:var(--text-secondary);">
          Already have an account? 
          <a href="#" onclick="closeModal('signupModal'); showLoginModal()" style="color:#6366f1;text-decoration:none;">Sign In</a>
        </div>
      </div>
    `;
    document.body.appendChild(signupModal);
  }
}

// NAVBAR FIXES
function fixNavbar() {
  console.log('🔧 Fixing navbar...');
  
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    // Ensure navbar has proper overflow and positioning
    navbar.style.cssText += `
      overflow: visible !important;
      position: relative !important;
      z-index: 1000 !important;
    `;
    
    // Fix auth buttons container
    const authButtons = document.getElementById('authButtons');
    if (authButtons) {
      authButtons.style.cssText += `
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        align-items: center !important;
        gap: 1rem !important;
      `;
      
      // Ensure auth buttons are properly styled
      const authBtns = authButtons.querySelectorAll('.auth-btn');
      authBtns.forEach(btn => {
        btn.style.cssText += `
          background: rgba(255,255,255,0.1) !important;
          border: 2px solid rgba(255,255,255,0.2) !important;
          color: var(--text-primary) !important;
          padding: 0.5rem 1rem !important;
          border-radius: 2rem !important;
          cursor: pointer !important;
          font-weight: 500 !important;
          transition: all 0.3s ease !important;
          backdrop-filter: blur(10px) !important;
        `;
      });
    }
    
    // Remove duplicate bookmark buttons
    const bookmarkButtons = navbar.querySelectorAll('.bookmark-viewer-btn');
    if (bookmarkButtons.length > 1) {
      for (let i = 1; i < bookmarkButtons.length; i++) {
        bookmarkButtons[i].remove();
      }
    }
    
    console.log('✅ Navbar fixed');
  }
}

// CONNECT AUTH BUTTONS
function connectAuthButtons() {
  console.log('🔗 Connecting auth buttons...');
  
  // Wait for DOM elements
  setTimeout(() => {
    const signInBtn = document.querySelector('.auth-btn:not(.signup)');
    const signUpBtn = document.querySelector('.auth-btn.signup');
    
    if (signInBtn) {
      signInBtn.onclick = showLoginModal;
      console.log('✅ Sign In button connected');
    } else {
      console.warn('⚠️ Sign In button not found');
    }
    
    if (signUpBtn) {
      signUpBtn.onclick = showSignupModal;
      console.log('✅ Sign Up button connected');
    } else {
      console.warn('⚠️ Sign Up button not found');
    }
  }, 500);
}

// BOOKMARKING SYSTEM
function toggleBookmark(itemId, itemType) {
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
    impactMojoUserBookmarks = bookmarks;
  } else {
    impactMojoUserLabBookmarks = bookmarks;
  }
  
  updateBookmarkUI();
  updateBookmarkViewer();
}

function updateBookmarkUI() {
  // Update bookmark button icons
  document.querySelectorAll('[onclick*="toggleBookmark"]').forEach(btn => {
    const onclick = btn.getAttribute('onclick');
    const matches = onclick.match(/toggleBookmark\('([^']+)',\s*'([^']+)'/);
    if (matches) {
      const itemId = matches[1];
      const itemType = matches[2];
      const bookmarks = itemType === 'course' ? impactMojoUserBookmarks : impactMojoUserLabBookmarks;
      const icon = btn.querySelector('i');
      if (icon) {
        icon.className = bookmarks.includes(itemId) ? 'fas fa-bookmark' : 'far fa-bookmark';
        btn.style.color = bookmarks.includes(itemId) ? '#f59e0b' : '#64748b';
      }
    }
  });
}

function updateBookmarkViewer() {
  const totalBookmarks = impactMojoUserBookmarks.length + impactMojoUserLabBookmarks.length;
  const bookmarkBtn = document.getElementById('bookmarkViewerBtn');
  const bookmarkCount = document.getElementById('bookmarkCount');
  
  if (bookmarkBtn) {
    bookmarkBtn.style.display = totalBookmarks > 0 ? 'flex' : 'none';
  }
  
  if (bookmarkCount) {
    bookmarkCount.textContent = totalBookmarks;
  }
}

// COMPARISON SYSTEM
function toggleComparison(itemId, itemType) {
  if (!window.selectedForComparison) {
    window.selectedForComparison = [];
  }
  
  const itemKey = `${itemType}-${itemId}`;
  const index = window.selectedForComparison.findIndex(item => item.key === itemKey);
  
  if (index === -1) {
    if (window.selectedForComparison.length >= 4) {
      showNotification('You can only compare up to 4 items at once', 'warning');
      return false;
    }
    
    window.selectedForComparison.push({
      key: itemKey,
      id: itemId,
      type: itemType
    });
    
    showNotification(`Added to comparison (${window.selectedForComparison.length}/4)`, 'success');
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

function showComparison() {
  if (!window.selectedForComparison || window.selectedForComparison.length < 2) {
    showNotification('Please select at least 2 items to compare', 'warning');
    return;
  }
  
  createComparisonModalIfNeeded();
  updateComparisonContent();
  openModal('comparisonModal');
}

function createComparisonModalIfNeeded() {
  if (!document.getElementById('comparisonModal')) {
    const modal = document.createElement('div');
    modal.id = 'comparisonModal';
    modal.className = 'modal';
    modal.style.cssText = 'display:none;position:fixed;z-index:10000;left:0;top:0;width:100%;height:100%;background:rgba(0,0,0,0.5);align-items:center;justify-content:center;';
    modal.innerHTML = `
      <div class="modal-content" style="background:var(--surface);padding:2rem;border-radius:0.75rem;max-width:95%;max-height:90%;overflow-y:auto;position:relative;border:1px solid var(--border-color);">
        <span class="close" onclick="closeModal('comparisonModal')" style="position:absolute;top:1rem;right:1rem;font-size:2rem;cursor:pointer;color:var(--text-secondary);">&times;</span>
        <h2 style="margin-top:0;color:var(--text-primary);">
          <i class="fas fa-balance-scale" style="margin-right:0.5rem;color:#6366f1;"></i>
          Course & Lab Comparison
        </h2>
        <div id="comparisonContent">
          <!-- Comparison content will be generated here -->
        </div>
      </div>
    `;
    document.body.appendChild(modal);
  }
}

function updateComparisonContent() {
  const content = document.getElementById('comparisonContent');
  if (!content) return;
  
  if (!window.selectedForComparison || window.selectedForComparison.length < 2) {
    content.innerHTML = `
      <div style="text-align:center;padding:3rem;color:var(--text-secondary);">
        <i class="fas fa-balance-scale" style="font-size:4rem;opacity:0.3;margin-bottom:1rem;"></i>
        <h3 style="color:var(--text-primary);margin:0 0 1rem 0;">Select items to compare</h3>
        <p style="margin:0;">Use the checkboxes on course and lab cards to select items for comparison. You can compare 2-4 items at once.</p>
      </div>
    `;
    return;
  }
  
  // Get item data for comparison
  const items = window.selectedForComparison.map(item => {
    if (item.type === 'course') {
      return window.courses?.find(c => c.id === item.id) || impactMojoAllCourses?.find(c => c.id === item.id);
    } else if (item.type === 'lab') {
      return window.labs?.find(l => l.id === item.id);
    }
    return null;
  }).filter(Boolean);
  
  if (items.length === 0) {
    content.innerHTML = '<p style="text-align:center;color:var(--text-secondary);">Error loading comparison data.</p>';
    return;
  }
  
  // Create enhanced comparison table
  let tableHTML = `
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2rem;padding:1rem;background:var(--surface);border-radius:0.5rem;border:1px solid var(--border-color);">
      <span style="font-weight:600;color:var(--text-primary);">
        <i class="fas fa-chart-line" style="margin-right:0.5rem;color:#10b981;"></i>
        Comparing ${items.length} item${items.length > 1 ? 's' : ''}
      </span>
      <button onclick="clearComparison()" style="background:#ef4444;color:white;border:none;padding:0.5rem 1rem;border-radius:0.375rem;cursor:pointer;font-size:0.85rem;font-weight:500;display:flex;align-items:center;gap:0.5rem;">
        <i class="fas fa-times"></i> Clear All
      </button>
    </div>
    <div style="overflow-x:auto;border-radius:0.5rem;border:1px solid var(--border-color);">
      <table style="width:100%;border-collapse:collapse;">
        <thead>
          <tr style="background:var(--primary-color);color:white;">
            <th style="padding:1rem;text-align:left;font-weight:600;min-width:120px;">Feature</th>
  `;
  
  items.forEach(item => {
    tableHTML += `<th style="padding:1rem;text-align:left;font-weight:600;min-width:200px;">${item.title || 'Untitled'}</th>`;
  });
  
  tableHTML += '</tr></thead><tbody>';
  
  // Enhanced comparison aspects
  const aspects = [
    { key: 'type', label: 'Type', icon: 'fas fa-tag' },
    { key: 'category', label: 'Category', icon: 'fas fa-folder' },
    { key: 'difficulty', label: 'Difficulty', icon: 'fas fa-signal' },
    { key: 'duration', label: 'Duration', icon: 'fas fa-clock' },
    { key: 'description', label: 'Description', icon: 'fas fa-file-text' },
    { key: 'rating', label: 'Rating', icon: 'fas fa-star' },
    { key: 'topics', label: 'Key Topics', icon: 'fas fa-list' },
    { key: 'outcomes', label: 'Learning Outcomes', icon: 'fas fa-graduation-cap' }
  ];
  
  aspects.forEach((aspect, index) => {
    const bgColor = index % 2 === 0 ? 'var(--surface)' : 'rgba(99, 102, 241, 0.05)';
    tableHTML += `<tr style="background:${bgColor};"><td style="padding:1rem;font-weight:600;color:var(--text-primary);border-bottom:1px solid var(--border-color);">
      <i class="${aspect.icon}" style="margin-right:0.5rem;color:#6366f1;"></i>${aspect.label}
    </td>`;
    
    items.forEach(item => {
      let value = 'N/A';
      
      switch(aspect.key) {
        case 'type':
          value = window.selectedForComparison.find(s => s.id === item.id)?.type || 'Unknown';
          value = `<span style="background:#6366f1;color:white;padding:0.25rem 0.75rem;border-radius:1rem;font-size:0.75rem;font-weight:600;">${value.toUpperCase()}</span>`;
          break;
        case 'category':
          value = item.category || 'General';
          break;
        case 'difficulty':
          const difficultyColors = { 'Beginner': '#10b981', 'Intermediate': '#f59e0b', 'Advanced': '#ef4444' };
          const diffColor = difficultyColors[item.difficulty] || '#6b7280';
          value = item.difficulty ? `<span style="background:${diffColor};color:white;padding:0.25rem 0.75rem;border-radius:1rem;font-size:0.75rem;font-weight:600;">${item.difficulty}</span>` : 'N/A';
          break;
        case 'duration':
          value = item.duration || item.estimatedTime || 'Varies';
          break;
        case 'description':
          value = item.description || item.overview || 'No description available';
          if (value.length > 120) {
            value = `<div style="max-height:4rem;overflow:hidden;line-height:1.4;">${value.substring(0, 120)}... <button onclick="this.previousSibling.style.maxHeight='none';this.style.display='none';" style="color:#6366f1;background:none;border:none;cursor:pointer;text-decoration:underline;font-size:0.8rem;">Read more</button></div>`;
          }
          break;
        case 'rating':
          const rating = item.rating || 0;
          value = rating > 0 ? `<div style="display:flex;align-items:center;gap:0.25rem;"><span style="color:#f59e0b;">${'★'.repeat(Math.floor(rating))}</span><span>${rating.toFixed(1)}</span></div>` : 'No rating';
          break;
        case 'topics':
          if (item.topics && Array.isArray(item.topics)) {
            value = `<ul style="margin:0;padding-left:1rem;line-height:1.6;">${item.topics.slice(0, 4).map(topic => `<li style="font-size:0.85rem;">${topic}</li>`).join('')}${item.topics.length > 4 ? `<li style="font-size:0.75rem;color:var(--text-secondary);">+${item.topics.length - 4} more</li>` : ''}</ul>`;
          } else if (item.keyPoints && Array.isArray(item.keyPoints)) {
            value = `<ul style="margin:0;padding-left:1rem;line-height:1.6;">${item.keyPoints.slice(0, 4).map(point => `<li style="font-size:0.85rem;">${point}</li>`).join('')}</ul>`;
          }
          break;
        case 'outcomes':
          if (item.learningOutcomes && Array.isArray(item.learningOutcomes)) {
            value = `<ul style="margin:0;padding-left:1rem;line-height:1.6;">${item.learningOutcomes.slice(0, 3).map(outcome => `<li style="font-size:0.85rem;">${outcome}</li>`).join('')}</ul>`;
          } else if (item.outcomes && Array.isArray(item.outcomes)) {
            value = `<ul style="margin:0;padding-left:1rem;line-height:1.6;">${item.outcomes.slice(0, 3).map(outcome => `<li style="font-size:0.85rem;">${outcome}</li>`).join('')}</ul>`;
          }
          break;
        default:
          value = item[aspect.key] || 'N/A';
      }
      
      tableHTML += `<td style="padding:1rem;color:var(--text-primary);border-bottom:1px solid var(--border-color);vertical-align:top;">${value}</td>`;
    });
    tableHTML += '</tr>';
  });
  
  tableHTML += '</tbody></table></div>';
  
  // Add action buttons
  tableHTML += `
    <div style="margin-top:2rem;display:flex;gap:1rem;flex-wrap:wrap;">
      ${items.map(item => {
        const itemType = window.selectedForComparison.find(s => s.id === item.id)?.type;
        const launchFunction = itemType === 'course' ? 'launchCourse' : 'launchLab';
        return `
          <button onclick="${launchFunction}('${item.id}')" style="
            background:linear-gradient(135deg,#6366f1,#8b5cf6);color:white;border:none;
            padding:0.75rem 1.5rem;border-radius:0.5rem;cursor:pointer;font-weight:600;
            display:flex;align-items:center;gap:0.5rem;transition:all 0.3s ease;
          " onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
            <i class="fas fa-external-link-alt"></i> Launch ${item.title}
          </button>
        `;
      }).join('')}
    </div>
  `;
  
  content.innerHTML = tableHTML;
}

function clearComparison() {
  window.selectedForComparison = [];
  updateComparisonUI();
  updateComparisonContent();
  showNotification('Comparison cleared', 'info');
}

// FAB BUTTONS CREATION
function createFABButtons() {
  console.log('🎯 Creating FAB buttons...');
  
  // Remove existing FAB container if it exists
  const existingFab = document.querySelector('.fab-container');
  if (existingFab) {
    existingFab.remove();
  }
  
  const fabContainer = document.createElement('div');
  fabContainer.className = 'fab-container';
  fabContainer.style.cssText = `
    position: fixed; bottom: 2rem; right: 2rem; z-index: 1000;
    display: flex; flex-direction: column; gap: 1rem;
  `;
  
  // Button 1: Feedback/Comments (Blue)
  const feedbackBtn = document.createElement('button');
  feedbackBtn.className = 'fab-btn feedback';
  feedbackBtn.style.cssText = `
    width: 56px; height: 56px; border-radius: 50%; border: none;
    background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: white; font-size: 1.25rem;
    cursor: pointer; box-shadow: 0 4px 12px rgba(59,130,246,0.4);
    display: flex; align-items: center; justify-content: center;
    transition: all 0.3s ease;
  `;
  feedbackBtn.innerHTML = '<i class="fas fa-comment"></i>';
  feedbackBtn.title = 'Share feedback and suggestions';
  feedbackBtn.onmouseover = () => { feedbackBtn.style.transform = 'scale(1.1)'; };
  feedbackBtn.onmouseout = () => { feedbackBtn.style.transform = 'scale(1)'; };
  feedbackBtn.onclick = () => {
    createFeedbackModal();
    openModal('feedbackModal');
  };
  
  // Button 2: Course/Lab Request (Green)
  const suggestBtn = document.createElement('button');
  suggestBtn.className = 'fab-btn suggest';
  suggestBtn.style.cssText = `
    width: 56px; height: 56px; border-radius: 50%; border: none;
    background: linear-gradient(135deg, #10b981, #047857); color: white; font-size: 1.25rem;
    cursor: pointer; box-shadow: 0 4px 12px rgba(16,185,129,0.4);
    display: flex; align-items: center; justify-content: center;
    transition: all 0.3s ease;
  `;
  suggestBtn.innerHTML = '<i class="fas fa-lightbulb"></i>';
  suggestBtn.title = 'Request new course, lab, or resource';
  suggestBtn.onmouseover = () => { suggestBtn.style.transform = 'scale(1.1)'; };
  suggestBtn.onmouseout = () => { suggestBtn.style.transform = 'scale(1)'; };
  suggestBtn.onclick = () => {
    createSuggestModal();
    openModal('suggestModal');
  };
  
  // Button 3: Comparison (Orange)
  const compareBtn = document.createElement('button');
  compareBtn.className = 'fab-btn compare';
  compareBtn.style.cssText = `
    width: 56px; height: 56px; border-radius: 50%; border: none;
    background: linear-gradient(135deg, #f59e0b, #d97706); color: white; font-size: 1.25rem;
    cursor: pointer; box-shadow: 0 4px 12px rgba(245,158,11,0.4);
    display: none; align-items: center; justify-content: center;
    transition: all 0.3s ease;
  `;
  compareBtn.innerHTML = '<i class="fas fa-balance-scale"></i>';
  compareBtn.title = 'Compare selected courses and labs';
  compareBtn.onmouseover = () => { compareBtn.style.transform = 'scale(1.1)'; };
  compareBtn.onmouseout = () => { compareBtn.style.transform = 'scale(1)'; };
  compareBtn.onclick = showComparison;
  
  fabContainer.appendChild(feedbackBtn);
  fabContainer.appendChild(suggestBtn);
  fabContainer.appendChild(compareBtn);
  
  document.body.appendChild(fabContainer);
  
  console.log('✅ FAB buttons created');
}

// CREATE FEEDBACK AND SUGGEST MODALS
function createFeedbackModal() {
  if (document.getElementById('feedbackModal')) return;
  
  const modal = document.createElement('div');
  modal.id = 'feedbackModal';
  modal.className = 'modal';
  modal.style.cssText = 'display:none;position:fixed;z-index:10000;left:0;top:0;width:100%;height:100%;background:rgba(0,0,0,0.5);align-items:center;justify-content:center;';
  modal.innerHTML = `
    <div class="modal-content" style="background:var(--surface);padding:2rem;border-radius:0.75rem;max-width:500px;width:90%;position:relative;border:1px solid var(--border-color);">
      <span class="close" onclick="closeModal('feedbackModal')" style="position:absolute;top:1rem;right:1rem;font-size:2rem;cursor:pointer;color:var(--text-secondary);">&times;</span>
      <h2 style="margin-top:0;color:var(--text-primary);">
        <i class="fas fa-comment" style="margin-right:0.5rem;color:#3b82f6;"></i>
        Share Your Feedback
      </h2>
      <p style="color:var(--text-secondary);margin-bottom:1.5rem;">Help us improve ImpactMojo! Your feedback is valuable to us.</p>
      <form style="display:flex;flex-direction:column;gap:1rem;">
        <div>
          <label style="color:var(--text-primary);font-weight:500;display:block;margin-bottom:0.5rem;">Feedback Type:</label>
          <select style="width:100%;padding:0.75rem;border:2px solid var(--border-color);border-radius:0.5rem;background:var(--surface);color:var(--text-primary);">
            <option>General Feedback</option>
            <option>Bug Report</option>
            <option>Feature Request</option>
            <option>Content Suggestion</option>
            <option>User Experience</option>
          </select>
        </div>
        <div>
          <label style="color:var(--text-primary);font-weight:500;display:block;margin-bottom:0.5rem;">Your Message:</label>
          <textarea rows="4" placeholder="Tell us what you think..." style="width:100%;padding:0.75rem;border:2px solid var(--border-color);border-radius:0.5rem;background:var(--surface);color:var(--text-primary);resize:vertical;"></textarea>
        </div>
        <button type="submit" onclick="submitFeedback(event)" style="background:#3b82f6;color:white;border:none;padding:0.75rem;border-radius:0.5rem;cursor:pointer;font-weight:600;">
          <i class="fas fa-paper-plane" style="margin-right:0.5rem;"></i>
          Send Feedback
        </button>
      </form>
    </div>
  `;
  document.body.appendChild(modal);
}

function createSuggestModal() {
  if (document.getElementById('suggestModal')) return;
  
  const modal = document.createElement('div');
  modal.id = 'suggestModal';
  modal.className = 'modal';
  modal.style.cssText = 'display:none;position:fixed;z-index:10000;left:0;top:0;width:100%;height:100%;background:rgba(0,0,0,0.5);align-items:center;justify-content:center;';
  modal.innerHTML = `
    <div class="modal-content" style="background:var(--surface);padding:2rem;border-radius:0.75rem;max-width:500px;width:90%;position:relative;border:1px solid var(--border-color);">
      <span class="close" onclick="closeModal('suggestModal')" style="position:absolute;top:1rem;right:1rem;font-size:2rem;cursor:pointer;color:var(--text-secondary);">&times;</span>
      <h2 style="margin-top:0;color:var(--text-primary);">
        <i class="fas fa-lightbulb" style="margin-right:0.5rem;color:#10b981;"></i>
        Request Content
      </h2>
      <p style="color:var(--text-secondary);margin-bottom:1.5rem;">Suggest new courses, labs, or resources you'd like to see on ImpactMojo.</p>
      <form style="display:flex;flex-direction:column;gap:1rem;">
        <div>
          <label style="color:var(--text-primary);font-weight:500;display:block;margin-bottom:0.5rem;">Content Type:</label>
          <select style="width:100%;padding:0.75rem;border:2px solid var(--border-color);border-radius:0.5rem;background:var(--surface);color:var(--text-primary);">
            <option>Course</option>
            <option>Interactive Lab</option>
            <option>Resource Library</option>
            <option>Research Paper</option>
            <option>Case Study</option>
          </select>
        </div>
        <div>
          <label style="color:var(--text-primary);font-weight:500;display:block;margin-bottom:0.5rem;">Topic/Title:</label>
          <input type="text" placeholder="e.g., Climate Change Economics" style="width:100%;padding:0.75rem;border:2px solid var(--border-color);border-radius:0.5rem;background:var(--surface);color:var(--text-primary);">
        </div>
        <div>
          <label style="color:var(--text-primary);font-weight:500;display:block;margin-bottom:0.5rem;">Description:</label>
          <textarea rows="3" placeholder="Describe what you'd like to learn or see covered..." style="width:100%;padding:0.75rem;border:2px solid var(--border-color);border-radius:0.5rem;background:var(--surface);color:var(--text-primary);resize:vertical;"></textarea>
        </div>
        <button type="submit" onclick="submitSuggestion(event)" style="background:#10b981;color:white;border:none;padding:0.75rem;border-radius:0.5rem;cursor:pointer;font-weight:600;">
          <i class="fas fa-plus" style="margin-right:0.5rem;"></i>
          Submit Request
        </button>
      </form>
    </div>
  `;
  document.body.appendChild(modal);
}

function submitFeedback(event) {
  event.preventDefault();
  showNotification('Thank you for your feedback! We\'ll review it carefully.', 'success');
  closeModal('feedbackModal');
}

function submitSuggestion(event) {
  event.preventDefault();
  showNotification('Thank you for your suggestion! We\'ll consider it for future content.', 'success');
  closeModal('suggestModal');
}

// ADD INTERACTIVE ELEMENTS TO CARDS
function addInteractiveElements() {
  console.log('🔗 Adding interactive elements to cards...');
  
  // Add bookmark buttons and comparison checkboxes to course/lab cards
  document.querySelectorAll('.course-card, .lab-card').forEach(card => {
    if (!card.querySelector('.bookmark-btn')) {
      const courseId = card.dataset.courseId || card.querySelector('[data-course-id]')?.dataset.courseId;
      const labId = card.dataset.labId || card.querySelector('[data-lab-id]')?.dataset.labId;
      
      if (courseId || labId) {
        const itemId = courseId || labId;
        const itemType = courseId ? 'course' : 'lab';
        
        // Add bookmark button
        const bookmarkBtn = document.createElement('button');
        bookmarkBtn.className = 'bookmark-btn';
        bookmarkBtn.style.cssText = `
          position: absolute; top: 0.5rem; right: 0.5rem; z-index: 10;
          background: rgba(255,255,255,0.95); border: 2px solid #f59e0b;
          border-radius: 50%; width: 40px; height: 40px;
          display: flex; align-items: center; justify-content: center;
          cursor: pointer; color: #f59e0b; transition: all 0.3s ease;
          backdrop-filter: blur(10px);
        `;
        bookmarkBtn.innerHTML = '<i class="far fa-bookmark"></i>';
        bookmarkBtn.title = `Bookmark this ${itemType}`;
        bookmarkBtn.onmouseover = () => { bookmarkBtn.style.transform = 'scale(1.1)'; };
        bookmarkBtn.onmouseout = () => { bookmarkBtn.style.transform = 'scale(1)'; };
        bookmarkBtn.onclick = () => toggleBookmark(itemId, itemType);
        
        // Add comparison checkbox
        const comparisonLabel = document.createElement('label');
        comparisonLabel.style.cssText = `
          position: absolute; top: 0.5rem; left: 0.5rem; z-index: 10;
          background: rgba(255,255,255,0.95); border: 2px solid #6366f1;
          border-radius: 6px; padding: 0.4rem; cursor: pointer;
          transition: all 0.3s ease; backdrop-filter: blur(10px);
        `;
        comparisonLabel.title = 'Select for comparison';
        
        const comparisonCheckbox = document.createElement('input');
        comparisonCheckbox.type = 'checkbox';
        comparisonCheckbox.className = 'comparison-checkbox';
        comparisonCheckbox.dataset.itemId = itemId;
        comparisonCheckbox.dataset.itemType = itemType;
        comparisonCheckbox.style.cssText = 'width: 16px; height: 16px; cursor: pointer; margin: 0; accent-color: #6366f1;';
        comparisonCheckbox.onchange = () => toggleComparison(itemId, itemType);
        
        comparisonLabel.appendChild(comparisonCheckbox);
        
        // Make card relative positioned
        card.style.position = 'relative';
        card.appendChild(bookmarkBtn);
        card.appendChild(comparisonLabel);
      }
    }
  });
  
  console.log('✅ Interactive elements added to cards');
}

// COURSE FUNCTIONS
function initializeCourses() {
  console.log('📚 Initializing courses...');
  
  if (window.courses && Array.isArray(window.courses)) {
    impactMojoAllCourses = window.courses;
    impactMojoFilteredCourses = [...impactMojoAllCourses];
    
    updateCourseStats();
    populateCategoryFilter();
    displayCourses();
    
    console.log('✅ Courses initialized successfully');
  } else {
    console.warn('⚠️ Course data not available yet, retrying...');
    setTimeout(initializeCourses, 1000);
  }
}

function displayCourses() {
  const container = document.getElementById('coursesContainer');
  
  if (!container) {
    console.log('ℹ️ Courses container not found');
    return;
  }
  
  if (impactMojoFilteredCourses.length === 0) {
    container.innerHTML = '<div class="no-results"><h3>No courses found</h3><p>Try adjusting your filters.</p></div>';
    return;
  }

  container.innerHTML = impactMojoFilteredCourses.map(course => createCourseCard(course)).join('');
  console.log(`✅ Displayed ${impactMojoFilteredCourses.length} courses`);
  
  // Add interactive elements after rendering
  setTimeout(addInteractiveElements, 100);
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
    <div class="course-card" data-course-id="${courseId}" style="border-left: 4px solid ${categoryColor}; position: relative;">
      <div class="course-card-header">
        <div class="course-category" style="background-color: ${categoryColor}20; color: ${categoryColor};">
          ${category}
        </div>
      </div>
      
      <div class="course-content">
        <h3 class="course-title">${title}</h3>
        <p class="course-description">${description}</p>
        
        <div class="course-meta">
          <span class="course-rating">
            <i class="fas fa-star" style="color: #f59e0b;"></i>
            ${rating.toFixed(1)}
          </span>
          <span class="course-duration">
            <i class="fas fa-clock"></i>
            ${duration}
          </span>
          <span class="course-difficulty difficulty-${difficulty.toLowerCase()}" style="background: ${getCategoryColor(difficulty)}; color: white; padding: 0.25rem 0.5rem; border-radius: 1rem; font-size: 0.75rem;">
            ${difficulty}
          </span>
        </div>
      </div>
      
      <div class="course-card-footer">
        <button class="launch-btn" onclick="launchCourse('${courseId}')" style="background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; cursor: pointer; font-weight: 600; display: flex; align-items: center; gap: 0.5rem; transition: all 0.3s ease;">
          <i class="fas fa-play"></i>
          Launch Course
        </button>
      </div>
    </div>
  `;
}

function displayPopularCourses() {
  const container = document.getElementById('popularCoursesContainer');
  
  if (!container) {
    console.log('ℹ️ Popular courses container not found');
    return;
  }
  
  if (!impactMojoAllCourses || impactMojoAllCourses.length === 0) {
    container.innerHTML = '<div class="loading">Loading popular courses...</div>';
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
  
  // Add interactive elements after rendering
  setTimeout(addInteractiveElements, 100);
}

function displayUpcomingCourses() {
  console.log('🚀 Displaying upcoming courses...');
  
  // Remove any duplicate upcoming sections first
  const duplicateContainers = document.querySelectorAll('.upcoming-courses-grid');
  if (duplicateContainers.length > 1) {
    for (let i = 0; i < duplicateContainers.length - 1; i++) {
      duplicateContainers[i].remove();
    }
    console.log(`🧹 Removed ${duplicateContainers.length - 1} duplicate upcoming containers`);
  }
  
  const upcomingData = [
    {
      id: 'upcoming-tech-for-all',
      title: 'Technology for All',
      category: 'Technology & Ethics',
      difficulty: 'Intermediate',
      duration: '6 weeks',
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
      description: 'How digital technologies are transforming governance structures and citizen participation in developing countries.',
      status: 'Coming Soon',
      expectedDate: 'Spring 2026'
    }
  ];
  
  let upcomingContainer = document.getElementById('upcomingCoursesContainer') || 
                         document.querySelector('.upcoming-courses-grid') ||
                         document.querySelector('#upcoming .courses-grid');
  
  if (upcomingContainer) {
    upcomingContainer.innerHTML = upcomingData.map(course => createUpcomingCourseCard(course)).join('');
    console.log('✅ Upcoming courses displayed successfully');
  } else {
    console.warn('⚠️ No upcoming courses container found');
  }
}

function createUpcomingCourseCard(course) {
  const categoryColor = getCategoryColor(course.category);
  
  return `
    <div class="course-card upcoming-course" data-course-id="${course.id}" style="border-left: 4px solid ${categoryColor}; position: relative; opacity: 0.9;">
      <div class="upcoming-badge" style="
        position: absolute; top: 1rem; right: 1rem; 
        background: linear-gradient(135deg, #6366f1, #8b5cf6); 
        color: white; padding: 0.25rem 0.75rem; border-radius: 1rem; 
        font-size: 0.75rem; font-weight: 600; z-index: 10;
        box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
      ">
        ${course.status}
      </div>
      
      <div class="course-card-header">
        <div class="course-category" style="background-color: ${categoryColor}20; color: ${categoryColor};">
          ${course.category}
        </div>
      </div>
      
      <div class="course-content">
        <h3 class="course-title">${course.title}</h3>
        <p class="course-description">${course.description}</p>
        
        <div class="course-meta">
          <span class="course-duration">
            <i class="fas fa-clock"></i>
            ${course.duration}
          </span>
          <span class="course-difficulty difficulty-${course.difficulty.toLowerCase()}" style="background: ${getCategoryColor(course.difficulty)}; color: white; padding: 0.25rem 0.5rem; border-radius: 1rem; font-size: 0.75rem;">
            ${course.difficulty}
          </span>
          <span class="expected-date" style="color: #6366f1; font-weight: 500;">
            <i class="fas fa-calendar"></i>
            ${course.expectedDate}
          </span>
        </div>
      </div>
      
      <div class="course-card-footer">
        <button class="launch-btn upcoming-disabled" onclick="notifyWhenReady('${course.id}')" style="
          background: #e5e7eb; color: #6b7280; cursor: not-allowed; opacity: 0.7;
          border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; font-weight: 600;
          display: flex; align-items: center; gap: 0.5rem; width: 100%; justify-content: center;
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
}

function displayLabs() {
  const container = document.getElementById('labsContainer');
  
  if (!container) {
    console.log('ℹ️ Labs container not found');
    return;
  }
  
  if (!window.labs || window.labs.length === 0) {
    container.innerHTML = '<div class="no-results" style="text-align: center; padding: 2rem; color: var(--text-secondary);">Interactive labs will be available soon...</div>';
    return;
  }

  container.innerHTML = window.labs.map(lab => createLabCard(lab)).join('');
  console.log(`✅ Displayed ${window.labs.length} labs`);
  
  // Add interactive elements after rendering
  setTimeout(addInteractiveElements, 100);
}

function createLabCard(lab) {
  if (!lab) return '';
  
  return `
    <div class="lab-card" data-lab-id="${lab.id}" style="position: relative;">
      <div class="lab-card-header">
        <div class="lab-category" style="background-color: rgba(245, 158, 11, 0.2); color: #f59e0b;">
          ${lab.category || 'Interactive'}
        </div>
        <div class="lab-type-badge" style="background: #10b981; color: white; padding: 0.25rem 0.5rem; border-radius: 1rem; font-size: 0.75rem;">
          ${lab.type || 'Simulation'}
        </div>
      </div>
      
      <div class="lab-content">
        <h3 class="lab-title">${lab.title || 'Untitled Lab'}</h3>
        <p class="lab-description">${lab.description || 'Interactive lab experience'}</p>
        
        <div class="lab-meta">
          <span class="lab-duration">
            <i class="fas fa-clock"></i>
            ${lab.duration || '30 min'}
          </span>
          <span class="lab-difficulty difficulty-${(lab.difficulty || 'beginner').toLowerCase()}" style="background: ${getCategoryColor(lab.difficulty || 'Beginner')}; color: white; padding: 0.25rem 0.5rem; border-radius: 1rem; font-size: 0.75rem;">
            ${lab.difficulty || 'Beginner'}
          </span>
        </div>
      </div>
      
      <div class="lab-card-footer">
        <button class="lab-launch-btn" onclick="launchLab('${lab.id}')" style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; cursor: pointer; font-weight: 600; display: flex; align-items: center; gap: 0.5rem; transition: all 0.3s ease;">
          <i class="fas fa-flask"></i>
          Launch Lab
        </button>
      </div>
    </div>
  `;
}

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

// SEARCH AND FILTER
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

function updateCourseStats() {
  const totalElement = document.getElementById('totalCourses');
  const filteredElement = document.getElementById('filteredCourses');
  
  if (totalElement) totalElement.textContent = impactMojoAllCourses.length;
  if (filteredElement) filteredElement.textContent = impactMojoFilteredCourses.length;
}

// UTILITY FUNCTIONS
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
    'Beginner': '#10b981',
    'Intermediate': '#f59e0b',
    'Advanced': '#ef4444',
    'Default': '#6c757d'
  };
  return categoryColors[category] || categoryColors['Default'];
}

// KEYBOARD SHORTCUTS
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
  
  if (e.key === 'Escape') {
    // Close any open modals
    document.querySelectorAll('.modal.active').forEach(modal => {
      closeModal(modal.id);
    });
  }
});

// FIREBASE AUTH STATE LISTENER
auth.onAuthStateChanged((user) => {
  console.log('👤 Auth state changed:', user ? `Signed in as ${user.email}` : 'Signed out');
  updateAuthUI(user);
});

// MAIN INITIALIZATION
function initializeEverything() {
  console.log('🚀 Initializing all ImpactMojo features...');
  
  // Initialize theme first
  initializeThemeToggle();
  
  // Fix navbar
  fixNavbar();
  
  // Create FAB buttons
  createFABButtons();
  
  // Connect auth buttons
  connectAuthButtons();
  
  // Initialize courses if available
  if (window.courses) {
    initializeCourses();
    displayPopularCourses();
    displayLabs();
    displayUpcomingCourses();
  } else {
    window.addEventListener('dataLoaded', function() {
      initializeCourses();
      displayPopularCourses();
      displayLabs();
      displayUpcomingCourses();
    });
  }
  
  // Add interactive elements to existing cards
  setTimeout(() => {
    addInteractiveElements();
    updateBookmarkUI();
    updateComparisonUI();
  }, 1000);
  
  console.log('✅ All features initialized successfully!');
  showNotification('ImpactMojo features ready!', 'success');
}

// AUTO-INITIALIZE
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeEverything);
} else {
  setTimeout(initializeEverything, 100);
}

// Make functions globally available
window.openModal = openModal;
window.closeModal = closeModal;
window.showNotification = showNotification;
window.toggleBookmark = toggleBookmark;
window.toggleComparison = toggleComparison;
window.showComparison = showComparison;
window.showLoginModal = showLoginModal;
window.showSignupModal = showSignupModal;
window.toggleTheme = toggleTheme;
window.login = login;
window.signup = signup;
window.signInWithGoogle = signInWithGoogle;
window.logout = logout;

console.log('✅ Complete ImpactMojo Main JS with Firebase loaded successfully!');
// ADD THIS CODE TO THE END OF YOUR EXISTING main.js
// This ensures courses/labs display even if Firebase fails

console.log('🔧 Adding course/lab display fallback...');

// Force initialize courses and labs after data loads
function forceInitializeCourses() {
  console.log('🚀 Force initializing courses and labs...');
  
  // Check if data is available
  if (window.courses && window.courses.length > 0) {
    console.log(`📚 Found ${window.courses.length} courses, displaying...`);
    
    // Display popular courses
    const popularContainer = document.getElementById('popularCoursesContainer');
    if (popularContainer) {
      const popularCourses = window.courses.slice(0, 6); // First 6 courses
      popularContainer.innerHTML = popularCourses.map(course => createSimpleCourseCard(course)).join('');
      console.log('✅ Popular courses displayed');
    }
    
    // Display all courses
    const coursesContainer = document.getElementById('coursesContainer');
    if (coursesContainer) {
      coursesContainer.innerHTML = window.courses.map(course => createSimpleCourseCard(course)).join('');
      console.log('✅ All courses displayed');
    }
    
    // Update stats
    const totalElement = document.getElementById('totalCourses');
    const filteredElement = document.getElementById('filteredCourses');
    if (totalElement) totalElement.textContent = window.courses.length;
    if (filteredElement) filteredElement.textContent = window.courses.length;
  }
  
  // Display labs
  if (window.labs && window.labs.length > 0) {
    console.log(`🧪 Found ${window.labs.length} labs, displaying...`);
    
    const labsContainer = document.getElementById('labsContainer');
    if (labsContainer) {
      labsContainer.innerHTML = window.labs.map(lab => createSimpleLabCard(lab)).join('');
      console.log('✅ Labs displayed');
    }
  }
}

// Simple course card creator (backup version)
function createSimpleCourseCard(course) {
  if (!course) return '';
  
  return `
    <div class="course-card" style="background: white; border: 1px solid #e5e7eb; border-radius: 0.5rem; padding: 1.5rem; margin-bottom: 1rem;">
      <div style="background: rgba(99, 102, 241, 0.1); color: #6366f1; padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.8rem; display: inline-block; margin-bottom: 1rem;">
        ${course.category || 'Course'}
      </div>
      <h3 style="font-size: 1.3rem; margin-bottom: 0.5rem; color: #1f2937; font-weight: 600;">
        ${course.title || 'Untitled Course'}
      </h3>
      <p style="color: #6b7280; margin-bottom: 1rem; line-height: 1.5;">
        ${course.description || 'No description available'}
      </p>
      <div style="display: flex; gap: 1rem; margin-bottom: 1rem; font-size: 0.9rem; color: #6b7280;">
        <span><i class="fas fa-star"></i> ${course.rating || 4.5}</span>
        <span><i class="fas fa-clock"></i> ${course.duration || 'Self-paced'}</span>
        <span><i class="fas fa-signal"></i> ${course.difficulty || 'Beginner'}</span>
      </div>
      <button onclick="window.open('${course.url}', '_blank')" style="background: #6366f1; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; cursor: pointer; font-weight: 600;">
        <i class="fas fa-play"></i> Launch Course
      </button>
    </div>
  `;
}

// Simple lab card creator (backup version)
function createSimpleLabCard(lab) {
  if (!lab) return '';
  
  return `
    <div class="lab-card" style="background: white; border: 1px solid #e5e7eb; border-radius: 0.5rem; padding: 1.5rem; margin-bottom: 1rem;">
      <div style="background: rgba(245, 158, 11, 0.1); color: #f59e0b; padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.8rem; display: inline-block; margin-bottom: 1rem;">
        ${lab.category || 'Lab'}
      </div>
      <h3 style="font-size: 1.3rem; margin-bottom: 0.5rem; color: #1f2937; font-weight: 600;">
        ${lab.title || 'Untitled Lab'}
      </h3>
      <p style="color: #6b7280; margin-bottom: 1rem; line-height: 1.5;">
        ${lab.description || 'Interactive lab experience'}
      </p>
      <div style="display: flex; gap: 1rem; margin-bottom: 1rem; font-size: 0.9rem; color: #6b7280;">
        <span><i class="fas fa-star"></i> ${lab.rating || 4.5}</span>
        <span><i class="fas fa-clock"></i> ${lab.duration || '20 min'}</span>
        <span><i class="fas fa-signal"></i> ${lab.difficulty || 'Beginner'}</span>
      </div>
      <button onclick="window.open('${lab.url}', '_blank')" style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; cursor: pointer; font-weight: 600;">
        <i class="fas fa-flask"></i> Launch Lab
      </button>
    </div>
  `;
}

// Try to initialize immediately
setTimeout(forceInitializeCourses, 1000);

// Also try when data loads
window.addEventListener('dataLoaded', forceInitializeCourses);

// Also try when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    setTimeout(forceInitializeCourses, 500);
  });
} else {
  setTimeout(forceInitializeCourses, 500);
}

console.log('✅ Course/lab display fallback added');