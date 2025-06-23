// ImpactMojo 101 - Firebase Authentication Module
// Handles all user authentication and data management

let currentUser = null;
let userBookmarks = [];
let userNotes = '';

// Initialize auth state listener when page loads
document.addEventListener('DOMContentLoaded', function() {
  initializeAuth();
});

// Initialize authentication
function initializeAuth() {
  // Check if Firebase is loaded
  if (!window.auth) {
    console.error('Firebase not loaded');
    return;
  }

  // Listen for auth state changes
  window.onAuthStateChanged(window.auth, (user) => {
    if (user) {
      currentUser = user;
      showUserUI();
      loadUserData();
    } else {
      currentUser = null;
      showAuthUI();
    }
  });
}

// Show authentication UI (login/signup buttons)
function showAuthUI() {
  const authButtons = document.getElementById('authButtons');
  const userMenu = document.getElementById('userMenu');
  
  if (authButtons) authButtons.classList.remove('hidden');
  if (userMenu) userMenu.classList.add('hidden');
}

// Show user UI (user menu)
function showUserUI() {
  const authButtons = document.getElementById('authButtons');
  const userMenu = document.getElementById('userMenu');
  const userDisplayName = document.getElementById('userDisplayName');
  
  if (authButtons) authButtons.classList.add('hidden');
  if (userMenu) userMenu.classList.remove('hidden');
  
  if (userDisplayName && currentUser) {
    userDisplayName.textContent = currentUser.displayName || currentUser.email.split('@')[0];
  }
}

// Show login modal
function showLoginModal() {
  const modal = document.getElementById('loginModal');
  if (modal) {
    modal.style.display = 'block';
  }
}

// Show signup modal
function showSignupModal() {
  const modal = document.getElementById('signupModal');
  if (modal) {
    modal.style.display = 'block';
  }
}

// Close modal
function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.style.display = 'none';
  }
}

// Login with email and password
async function login(event) {
  event.preventDefault();
  
  const email = document.getElementById('loginEmail').value;
  const password = document.getElementById('loginPassword').value;
  
  try {
    await window.signInWithEmailAndPassword(window.auth, email, password);
    closeModal('loginModal');
    showNotification('Successfully logged in!', 'success');
    
    // Clear form
    document.getElementById('loginEmail').value = '';
    document.getElementById('loginPassword').value = '';
  } catch (error) {
    console.error('Login error:', error);
    showNotification(getErrorMessage(error), 'error');
  }
}

// Sign up with email and password
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

// Sign in with Google
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

// Logout
async function logout() {
  try {
    await window.signOut(window.auth);
    showNotification('Successfully logged out!', 'success');
    
    // Reset user data
    userBookmarks = [];
    userNotes = '';
    
    // Reset any filtered views
    if (typeof clearAllFilters === 'function') {
      clearAllFilters();
    }
  } catch (error) {
    console.error('Logout error:', error);
    showNotification('Error logging out', 'error');
  }
}

// Show forgot password modal
function showForgotPassword() {
  const email = document.getElementById('loginEmail').value;
  if (!email) {
    showNotification('Please enter your email address first', 'error');
    return;
  }
  
  resetPassword(email);
}

// Reset password
async function resetPassword(email) {
  try {
    await window.sendPasswordResetEmail(window.auth, email);
    showNotification('Password reset email sent!', 'success');
    closeModal('loginModal');
  } catch (error) {
    console.error('Password reset error:', error);
    showNotification(getErrorMessage(error), 'error');
  }
}

// Load user data from Firestore
async function loadUserData() {
  if (!currentUser) return;
  
  try {
    const userDoc = await window.getDoc(window.doc(window.db, 'users', currentUser.uid));
    if (userDoc.exists()) {
      const userData = userDoc.data();
      userBookmarks = userData.bookmarks || [];
      userNotes = userData.notes || '';
      
      // Update UI to reflect bookmarks
      updateBookmarkUI();
    }
  } catch (error) {
    console.error('Error loading user data:', error);
  }
}

// Update bookmark UI
function updateBookmarkUI() {
  const bookmarkButtons = document.querySelectorAll('.bookmark-btn');
  bookmarkButtons.forEach(btn => {
    const courseId = btn.dataset.courseId;
    if (userBookmarks.includes(courseId)) {
      btn.classList.add('bookmarked');
      btn.innerHTML = '<i class="fas fa-bookmark"></i>';
    } else {
      btn.classList.remove('bookmarked');
      btn.innerHTML = '<i class="far fa-bookmark"></i>';
    }
  });
}

// Toggle bookmark
async function toggleBookmark(courseId) {
  if (!currentUser) {
    showNotification('Please log in to bookmark courses', 'error');
    showLoginModal();
    return;
  }
  
  try {
    const userRef = window.doc(window.db, 'users', currentUser.uid);
    
    if (userBookmarks.includes(courseId)) {
      // Remove bookmark
      await window.updateDoc(userRef, {
        bookmarks: window.arrayRemove(courseId)
      });
      userBookmarks = userBookmarks.filter(id => id !== courseId);
      showNotification('Bookmark removed', 'success');
    } else {
      // Add bookmark
      await window.updateDoc(userRef, {
        bookmarks: window.arrayUnion(courseId)
      });
      userBookmarks.push(courseId);
      showNotification('Course bookmarked!', 'success');
    }
    
    updateBookmarkUI();
  } catch (error) {
    console.error('Bookmark error:', error);
    showNotification('Error updating bookmark', 'error');
  }
}

// Toggle user dropdown
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

// Show dashboard
function showDashboard() {
  if (!currentUser) {
    showNotification('Please log in to view dashboard', 'error');
    showLoginModal();
    return;
  }
  
  // Create dashboard functionality
  showNotification('Dashboard feature coming soon! Track your progress and manage your learning path.', 'info');
}

// Show bookmarks
function showBookmarks() {
  if (!currentUser) {
    showNotification('Please log in to view bookmarks', 'error');
    showLoginModal();
    return;
  }
  
  if (userBookmarks.length === 0) {
    showNotification('No bookmarks yet. Start exploring courses!', 'info');
    return;
  }
  
  // Filter courses to show only bookmarked ones
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.value = '';
  }
  
  // Reset other filters
  document.getElementById('categoryFilter').value = 'all';
  document.getElementById('difficultyFilter').value = 'all';
  document.getElementById('durationFilter').value = 'all';
  
  // Set bookmark filter and render
  if (typeof setBookmarkFilter === 'function') {
    setBookmarkFilter(true);
  }
  
  showNotification(`Showing ${userBookmarks.length} bookmarked courses`, 'success');
  
  // Scroll to courses section
  const coursesSection = document.getElementById('courses');
  if (coursesSection) {
    coursesSection.scrollIntoView({ behavior: 'smooth' });
  }
}

// Show profile
function showProfile() {
  if (!currentUser) {
    showNotification('Please log in to view profile', 'error');
    showLoginModal();
    return;
  }
  
  // Create profile modal or page
  const profileInfo = `
    Name: ${currentUser.displayName || 'Not provided'}
    Email: ${currentUser.email}
    Joined: ${currentUser.metadata.creationTime ? new Date(currentUser.metadata.creationTime).toLocaleDateString() : 'Unknown'}
    Bookmarks: ${userBookmarks.length} courses
  `;
  
  showNotification('Profile: ' + profileInfo, 'info');
}

// Save user notes
async function saveUserNotes(notes) {
  if (!currentUser) {
    showNotification('Please log in to save notes', 'error');
    return;
  }
  
  try {
    const userRef = window.doc(window.db, 'users', currentUser.uid);
    await window.updateDoc(userRef, {
      notes: notes
    });
    userNotes = notes;
    showNotification('Notes saved successfully', 'success');
  } catch (error) {
    console.error('Error saving notes:', error);
    showNotification('Error saving notes', 'error');
  }
}

// Update user progress
async function updateUserProgress(courseId, progress) {
  if (!currentUser) return;
  
  try {
    const userRef = window.doc(window.db, 'users', currentUser.uid);
    await window.updateDoc(userRef, {
      [`progress.${courseId}`]: {
        completed: progress.completed || false,
        lastAccessed: new Date(),
        timeSpent: progress.timeSpent || 0
      }
    });
  } catch (error) {
    console.error('Error updating progress:', error);
  }
}

// Get user-friendly error message
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
    case 'auth/popup-closed-by-user':
      return 'Sign-in popup was closed.';
    case 'auth/popup-blocked':
      return 'Popup was blocked. Please allow popups for this site.';
    case 'auth/cancelled-popup-request':
      return 'Sign-in popup was cancelled.';
    case 'auth/network-request-failed':
      return 'Network error. Please check your connection.';
    default:
      return error.message || 'An error occurred. Please try again.';
  }
}

// Utility function to check if user is authenticated
function isAuthenticated() {
  return currentUser !== null;
}

// Get current user data
function getCurrentUserData() {
  return {
    user: currentUser,
    bookmarks: userBookmarks,
    notes: userNotes
  };
}