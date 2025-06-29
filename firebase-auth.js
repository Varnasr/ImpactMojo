// Fixed Firebase Auth for ImpactMojo
// RESOLVES: TypeError: window.onAuthStateChanged is not a function

console.log('🔐 Loading ImpactMojo Firebase Auth...');

// ===== WAIT FOR FIREBASE TO BE READY =====
function waitForFirebase() {
  return new Promise((resolve, reject) => {
    let attempts = 0;
    const maxAttempts = 50;
    
    const checkFirebase = () => {
      attempts++;
      
      if (typeof firebase !== 'undefined' && firebase.auth) {
        console.log('✅ Firebase auth ready');
        resolve(firebase.auth());
      } else if (attempts >= maxAttempts) {
        console.error('❌ Firebase failed to load after', maxAttempts, 'attempts');
        reject(new Error('Firebase not available'));
      } else {
        setTimeout(checkFirebase, 100);
      }
    };
    
    checkFirebase();
  });
}

// ===== GLOBAL VARIABLES =====
let currentUser = null;
let userBookmarks = [];
let userNotes = '';
let userProgress = {};

// ===== AUTHENTICATION FUNCTIONS =====

/**
 * Initialize authentication system
 */
async function initializeAuth() {
  try {
    const auth = await waitForFirebase();
    
    // Set up auth state listener
    auth.onAuthStateChanged((user) => {
      console.log('👤 Auth state changed:', user ? `Signed in as ${user.email}` : 'Signed out');
      currentUser = user;
      updateAuthUI(user);
      
      if (user) {
        loadUserData(user.uid);
      } else {
        clearUserData();
      }
    });
    
    console.log('✅ Firebase auth initialized successfully');
    
  } catch (error) {
    console.error('❌ Error initializing auth:', error);
  }
}

/**
 * Update UI based on authentication state
 */
function updateAuthUI(user) {
  const authButtons = document.getElementById('authButtons');
  const userMenu = document.getElementById('userMenu');
  const userName = document.getElementById('userName');
  const userAvatar = document.getElementById('userAvatar');
  
  if (user) {
    // User is signed in
    if (authButtons) authButtons.style.display = 'none';
    if (userMenu) userMenu.style.display = 'flex';
    if (userName) userName.textContent = user.displayName || user.email?.split('@')[0] || 'User';
    if (userAvatar) {
      userAvatar.src = user.photoURL || `https://ui-avatars.com/api/?name=${encodeURIComponent(user.displayName || 'User')}&background=6366f1&color=fff`;
    }
  } else {
    // User is signed out
    if (authButtons) authButtons.style.display = 'flex';
    if (userMenu) userMenu.style.display = 'none';
    if (userName) userName.textContent = 'User';
    if (userAvatar) userAvatar.src = '';
  }
}

/**
 * Sign up with email and password
 */
async function signUp(email, password, displayName) {
  try {
    const auth = await waitForFirebase();
    const { user } = await auth.createUserWithEmailAndPassword(email, password);
    
    // Update display name
    if (displayName) {
      await user.updateProfile({ displayName });
    }
    
    // Create user document
    await createUserDocument(user.uid, {
      email: user.email,
      displayName: displayName || '',
      createdAt: new Date(),
      bookmarks: [],
      progress: {},
      notes: ''
    });
    
    showNotification('Account created successfully!', 'success');
    return user;
    
  } catch (error) {
    console.error('❌ Signup error:', error);
    showNotification(getErrorMessage(error), 'error');
    throw error;
  }
}

/**
 * Sign in with email and password
 */
async function signIn(email, password) {
  try {
    const auth = await waitForFirebase();
    const { user } = await auth.signInWithEmailAndPassword(email, password);
    
    showNotification('Successfully logged in!', 'success');
    return user;
    
  } catch (error) {
    console.error('❌ Signin error:', error);
    showNotification(getErrorMessage(error), 'error');
    throw error;
  }
}

/**
 * Sign in with Google
 */
async function signInWithGoogle() {
  try {
    const auth = await waitForFirebase();
    const provider = new firebase.auth.GoogleAuthProvider();
    const { user } = await auth.signInWithPopup(provider);
    
    // Create/update user document
    await createUserDocument(user.uid, {
      email: user.email,
      displayName: user.displayName || '',
      photoURL: user.photoURL || '',
      lastSignIn: new Date()
    });
    
    showNotification('Successfully logged in with Google!', 'success');
    return user;
    
  } catch (error) {
    console.error('❌ Google signin error:', error);
    showNotification(getErrorMessage(error), 'error');
    throw error;
  }
}

/**
 * Sign out user
 */
async function signOut() {
  try {
    const auth = await waitForFirebase();
    await auth.signOut();
    
    showNotification('Successfully logged out!', 'success');
    
  } catch (error) {
    console.error('❌ Signout error:', error);
    showNotification('Error signing out', 'error');
    throw error;
  }
}

/**
 * Reset password
 */
async function resetPassword(email) {
  try {
    const auth = await waitForFirebase();
    await auth.sendPasswordResetEmail(email);
    
    showNotification('Password reset email sent!', 'success');
    
  } catch (error) {
    console.error('❌ Password reset error:', error);
    showNotification(getErrorMessage(error), 'error');
    throw error;
  }
}

// ===== USER DATA FUNCTIONS =====

/**
 * Create or update user document
 */
async function createUserDocument(uid, userData) {
  try {
    if (!firebase.firestore) {
      console.warn('⚠️ Firestore not available, skipping user document creation');
      return;
    }
    
    const db = firebase.firestore();
    const userRef = db.collection('users').doc(uid);
    
    // Check if user exists
    const userDoc = await userRef.get();
    
    if (!userDoc.exists) {
      // Create new user
      await userRef.set({
        ...userData,
        createdAt: new Date(),
        bookmarks: [],
        progress: {},
        notes: ''
      });
    } else {
      // Update existing user
      await userRef.update({
        ...userData,
        lastSignIn: new Date()
      });
    }
    
    console.log('✅ User document created/updated successfully');
    
  } catch (error) {
    console.error('❌ Error creating user document:', error);
  }
}

/**
 * Load user data from Firestore
 */
async function loadUserData(uid) {
  try {
    if (!firebase.firestore) {
      console.warn('⚠️ Firestore not available, using local storage');
      return;
    }
    
    const db = firebase.firestore();
    const userDoc = await db.collection('users').doc(uid).get();
    
    if (userDoc.exists) {
      const data = userDoc.data();
      userBookmarks = data.bookmarks || [];
      userNotes = data.notes || '';
      userProgress = data.progress || {};
      
      console.log('✅ User data loaded successfully');
    }
    
  } catch (error) {
    console.error('❌ Error loading user data:', error);
  }
}

/**
 * Clear user data on signout
 */
function clearUserData() {
  userBookmarks = [];
  userNotes = '';
  userProgress = {};
}

// ===== BOOKMARK FUNCTIONS =====

/**
 * Add bookmark
 */
async function addBookmark(courseId, courseTitle) {
  if (!currentUser) {
    showNotification('Please log in to bookmark courses', 'error');
    return;
  }
  
  try {
    const bookmark = { id: courseId, title: courseTitle, addedAt: new Date() };
    userBookmarks.push(bookmark);
    
    if (firebase.firestore) {
      const db = firebase.firestore();
      await db.collection('users').doc(currentUser.uid).update({
        bookmarks: userBookmarks
      });
    }
    
    showNotification('Course bookmarked!', 'success');
    
  } catch (error) {
    console.error('❌ Error adding bookmark:', error);
    showNotification('Error adding bookmark', 'error');
  }
}

/**
 * Remove bookmark
 */
async function removeBookmark(courseId) {
  if (!currentUser) return;
  
  try {
    userBookmarks = userBookmarks.filter(b => b.id !== courseId);
    
    if (firebase.firestore) {
      const db = firebase.firestore();
      await db.collection('users').doc(currentUser.uid).update({
        bookmarks: userBookmarks
      });
    }
    
    showNotification('Bookmark removed!', 'success');
    
  } catch (error) {
    console.error('❌ Error removing bookmark:', error);
    showNotification('Error removing bookmark', 'error');
  }
}

// ===== UTILITY FUNCTIONS =====

/**
 * Show notification (placeholder - implement your notification system)
 */
function showNotification(message, type = 'info') {
  console.log(`📢 ${type.toUpperCase()}: ${message}`);
  
  // Simple alert fallback - replace with your notification system
  if (type === 'error') {
    console.error(message);
  }
}

/**
 * Get user-friendly error message
 */
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

// ===== MODAL FUNCTIONS (PLACEHOLDERS) =====

/**
 * Show login modal
 */
function showLoginModal() {
  console.log('🔐 Login modal requested');
  
  // Simple prompt fallback - replace with your modal system
  const email = prompt('Enter your email:');
  if (email) {
    const password = prompt('Enter your password:');
    if (password) {
      signIn(email, password);
    }
  }
}

/**
 * Show signup modal
 */
function showSignupModal() {
  console.log('📝 Signup modal requested');
  
  // Simple prompt fallback - replace with your modal system
  const email = prompt('Enter your email:');
  if (email) {
    const password = prompt('Create a password (min 6 characters):');
    if (password) {
      const displayName = prompt('Enter your display name (optional):');
      signUp(email, password, displayName);
    }
  }
}

// ===== INITIALIZATION =====

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  console.log('📄 DOM loaded, initializing auth...');
  initializeAuth();
});

// Export functions for global use
if (typeof window !== 'undefined') {
  window.ImpactMojoAuth = {
    signUp,
    signIn,
    signInWithGoogle,
    signOut,
    resetPassword,
    addBookmark,
    removeBookmark,
    showLoginModal,
    showSignupModal,
    currentUser: () => currentUser,
    userBookmarks: () => userBookmarks
  };
}

console.log('✅ Firebase auth module loaded successfully');