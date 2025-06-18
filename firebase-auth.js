// Firebase configuration for ImpactMojo
const firebaseConfig = {
  apiKey: "AIzaSyDnF0eJsTULzOJUnBskybd44dG5w-f46vE",
  authDomain: "impactmojo.firebaseapp.com",
  projectId: "impactmojo",
  storageBucket: "impactmojo.firebasestorage.app",
  messagingSenderId: "529198336589",
  appId: "1:529198336589:web:1664b5344de5bfb31bea04",
  measurementId: "G-ZHPPXXMRGV"
};

// Initialize Firebase
let app, auth, db;

// Wait for Firebase to be loaded
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM loaded, initializing Firebase...');
  
  // Check if Firebase is loaded
  if (typeof firebase === 'undefined') {
    console.error('Firebase not loaded! Make sure Firebase scripts are included.');
    return;
  }

  try {
    app = firebase.initializeApp(firebaseConfig);
    auth = firebase.auth();
    db = firebase.firestore();
    console.log('Firebase initialized successfully for ImpactMojo project');
    
    // Set up auth state listener
    auth.onAuthStateChanged((user) => {
      console.log('Auth state changed:', user ? 'User logged in' : 'User logged out');
      updateAuthUI(user);
    });
    
  } catch (error) {
    console.error('Firebase initialization error:', error);
  }
});

// Update UI based on auth state
function updateAuthUI(user) {
  const authButtons = document.getElementById('authButtons');
  const userMenu = document.getElementById('userMenu');
  const userName = document.getElementById('userName');
  const userDashboard = document.getElementById('userDashboard');

  if (user) {
    // User is signed in
    if (authButtons) authButtons.style.display = 'none';
    if (userMenu) userMenu.style.display = 'inline-flex';
    if (userName) userName.textContent = user.displayName || user.email.split('@')[0];
    console.log('User logged in:', user.email);
    
    // Show user dashboard if it exists
    if (userDashboard) {
      userDashboard.style.display = 'block';
    }
  } else {
    // User is signed out
    if (authButtons) authButtons.style.display = 'inline-flex';
    if (userMenu) userMenu.style.display = 'none';
    if (userDashboard) userDashboard.style.display = 'none';
    console.log('User logged out');
  }
}

// Login function
window.login = async function(email, password) {
  console.log('Login function called with email:', email);
  
  if (!auth) {
    console.error('Firebase auth not initialized');
    return { success: false, error: 'Authentication system not ready' };
  }

  try {
    console.log('Attempting Firebase signInWithEmailAndPassword...');
    const userCredential = await auth.signInWithEmailAndPassword(email, password);
    const user = userCredential.user;
    console.log('Login successful:', user.email);
    
    return { success: true, user: user };
  } catch (error) {
    console.error('Login error:', error);
    let errorMessage = 'Login failed. Please try again.';
    
    switch (error.code) {
      case 'auth/user-not-found':
        errorMessage = 'No account found with this email address.';
        break;
      case 'auth/wrong-password':
        errorMessage = 'Incorrect password.';
        break;
      case 'auth/invalid-email':
        errorMessage = 'Invalid email address.';
        break;
      case 'auth/user-disabled':
        errorMessage = 'This account has been disabled.';
        break;
      case 'auth/too-many-requests':
        errorMessage = 'Too many failed attempts. Please try again later.';
        break;
      case 'auth/network-request-failed':
        errorMessage = 'Network error. Please check your connection.';
        break;
      case 'auth/invalid-credential':
        errorMessage = 'Invalid email or password.';
        break;
    }
    
    return { success: false, error: errorMessage };
  }
};

// Signup function
window.signup = async function(email, password, name) {
  console.log('Signup function called with email:', email);
  
  if (!auth) {
    console.error('Firebase auth not initialized');
    return { success: false, error: 'Authentication system not ready' };
  }

  try {
    console.log('Attempting Firebase createUserWithEmailAndPassword...');
    const userCredential = await auth.createUserWithEmailAndPassword(email, password);
    const user = userCredential.user;
    
    // Update profile with display name
    if (name) {
      await user.updateProfile({
        displayName: name
      });
    }
    
    console.log('Signup successful:', user.email);
    return { success: true, user: user };
  } catch (error) {
    console.error('Signup error:', error);
    let errorMessage = 'Signup failed. Please try again.';
    
    switch (error.code) {
      case 'auth/email-already-in-use':
        errorMessage = 'An account with this email already exists.';
        break;
      case 'auth/invalid-email':
        errorMessage = 'Invalid email address.';
        break;
      case 'auth/weak-password':
        errorMessage = 'Password should be at least 6 characters.';
        break;
      case 'auth/network-request-failed':
        errorMessage = 'Network error. Please check your connection.';
        break;
    }
    
    return { success: false, error: errorMessage };
  }
};

// Google login function
window.loginWithGoogle = async function() {
  console.log('Google login function called');
  
  if (!auth) {
    console.error('Firebase auth not initialized');
    alert('Authentication system not ready. Please refresh the page and try again.');
    return;
  }

  try {
    const provider = new firebase.auth.GoogleAuthProvider();
    console.log('Opening Google popup...');
    const result = await auth.signInWithPopup(provider);
    const user = result.user;
    console.log('Google login successful:', user.email);
    return { success: true, user: user };
  } catch (error) {
    console.error('Google login error:', error);
    let errorMessage = 'Google login failed. Please try again.';
    
    switch (error.code) {
      case 'auth/popup-closed-by-user':
        errorMessage = 'Login cancelled by user.';
        break;
      case 'auth/popup-blocked':
        errorMessage = 'Popup was blocked by browser. Please allow popups and try again.';
        break;
      case 'auth/network-request-failed':
        errorMessage = 'Network error. Please check your connection.';
        break;
      case 'auth/cancelled-popup-request':
        errorMessage = 'Only one popup request is allowed at a time.';
        break;
      case 'auth/unauthorized-domain':
        errorMessage = 'This domain is not authorized for OAuth operations. Please add your domain to the Firebase Console.';
        break;
    }
    
    alert(errorMessage);
    return { success: false, error: errorMessage };
  }
};

// Logout function
window.logout = async function() {
  console.log('Logout function called');
  
  if (!auth) {
    console.error('Firebase auth not initialized');
    return;
  }

  try {
    await auth.signOut();
    console.log('Logout successful');
  } catch (error) {
    console.error('Logout error:', error);
    alert('Logout failed. Please try again.');
  }
};

// Reset password function
window.resetPassword = async function(email) {
  console.log('Reset password function called for email:', email);
  
  if (!auth) {
    console.error('Firebase auth not initialized');
    alert('Authentication system not ready. Please refresh the page and try again.');
    return;
  }

  try {
    await auth.sendPasswordResetEmail(email);
    alert('Password reset email sent! Check your inbox.');
  } catch (error) {
    console.error('Reset password error:', error);
    let errorMessage = 'Failed to send reset email. Please try again.';
    
    if (error.code === 'auth/user-not-found') {
      errorMessage = 'No account found with this email address.';
    } else if (error.code === 'auth/invalid-email') {
      errorMessage = 'Invalid email address.';
    }
    
    alert(errorMessage);
  }
};

// Bookmark functions with user context
window.toggleBookmark = function(courseTitle, courseUrl) {
  console.log('Toggle bookmark called for:', courseTitle);
  
  // Get current user
  const user = auth ? auth.currentUser : null;
  
  if (user) {
    console.log('User is logged in, bookmarking for user:', user.email);
    // You could save to Firestore here for user-specific bookmarks
    // For now, we'll still use localStorage but could extend this
  }
  
  // Use localStorage for immediate functionality
  let bookmarks = JSON.parse(localStorage.getItem('bookmarkedCourses') || '[]');
  
  if (bookmarks.includes(courseTitle)) {
    bookmarks = bookmarks.filter(title => title !== courseTitle);
    console.log('Removed bookmark:', courseTitle);
  } else {
    bookmarks.push(courseTitle);
    console.log('Added bookmark:', courseTitle);
  }
  
  localStorage.setItem('bookmarkedCourses', JSON.stringify(bookmarks));
  
  // Update the UI to reflect bookmark status
  updateBookmarkDisplay(courseTitle, bookmarks.includes(courseTitle));
};

// Update bookmark display
function updateBookmarkDisplay(courseTitle, isBookmarked) {
  // Find all bookmark buttons for this course and update them
  const bookmarkButtons = document.querySelectorAll(`button[onclick*="${courseTitle}"]`);
  bookmarkButtons.forEach(button => {
    const icon = button.querySelector('i');
    if (isBookmarked) {
      button.classList.add('bookmarked');
      if (icon) icon.className = 'fas fa-bookmark';
    } else {
      button.classList.remove('bookmarked');
      if (icon) icon.className = 'far fa-bookmark';
    }
  });
}

// Initialize bookmarks on page load
function initializeBookmarks() {
  const bookmarks = JSON.parse(localStorage.getItem('bookmarkedCourses') || '[]');
  bookmarks.forEach(courseTitle => {
    updateBookmarkDisplay(courseTitle, true);
  });
}

// Initialize everything when DOM and Firebase are ready
document.addEventListener('DOMContentLoaded', function() {
  console.log('ImpactMojo Firebase auth system ready');
  
  // Initialize bookmarks after a brief delay to ensure course cards are rendered
  setTimeout(initializeBookmarks, 1000);
});