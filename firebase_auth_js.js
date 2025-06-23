// Firebase Authentication Functions
// Handles user authentication, registration, and user management

// Authentication state management
let currentUser = null;
let userProfile = null;

// Initialize authentication state listener
function initializeAuth() {
  if (typeof window.onAuthStateChanged === 'undefined') {
    console.error('Firebase not loaded properly');
    return;
  }

  window.onAuthStateChanged(window.auth, (user) => {
    currentUser = user;
    updateAuthUI(user);
    if (user) {
      loadUserProfile(user.uid);
    } else {
      userProfile = null;
    }
  });
}

// Update UI based on authentication state
function updateAuthUI(user) {
  const loggedOutMenu = document.getElementById('logged-out-menu');
  const loggedInMenu = document.getElementById('logged-in-menu');
  const userDisplay = document.getElementById('user-display');

  if (user) {
    loggedOutMenu.style.display = 'none';
    loggedInMenu.style.display = 'flex';
    
    const displayName = user.displayName || user.email.split('@')[0];
    userDisplay.textContent = `Welcome, ${displayName}!`;
    
    // Update user photo and initials
    updateUserPhoto(user.photoURL);
    updateUserInitials(displayName);
    
    // Update dashboard user info
    const dashboardUserName = document.getElementById('dashboard-user-name');
    if (dashboardUserName) {
      dashboardUserName.textContent = `Welcome back, ${displayName}!`;
    }
  } else {
    loggedOutMenu.style.display = 'flex';
    loggedInMenu.style.display = 'none';
    
    // Reset user photo/initials
    updateUserPhoto(null);
    updateUserInitials('User');
  }
}

// Enhanced user profile creation
async function createUserProfile(uid, profileData) {
  try {
    const enhancedProfileData = {
      ...profileData,
      preferences: {
        theme: 'light',
        notifications: true,
        emailUpdates: false
      },
      learningPath: null,
      quizResults: {},
      noteSettings: {
        autoSave: true,
        showCitations: true,
        exportFormat: 'json'
      },
      lastLogin: new Date().toISOString(),
      ...profileData
    };
    
    await window.setDoc(window.doc(window.db, 'users', uid), enhancedProfileData);
  } catch (error) {
    console.error('Error creating user profile:', error);
    throw error;
  }
}

// Enhanced save user notes with academic formatting
async function saveUserNotes(courseId, notes, citations = []) {
  if (!currentUser) return;
  
  try {
    const noteData = {
      content: notes,
      timestamp: new Date().toISOString(),
      citations: citations,
      courseId: courseId,
      wordCount: notes.split(' ').length
    };
    
    await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), {
      [`notes.${courseId}`]: noteData
    });
    
    if (userProfile) {
      if (!userProfile.notes) userProfile.notes = {};
      userProfile.notes[courseId] = noteData;
    }
    
    showNotification('Notes saved with citations!', 'success');
  } catch (error) {
    console.error('Error saving notes:', error);
    throw error;
  }
}

// Save quiz results
async function saveQuizResults(quizType, results) {
  if (!currentUser) return;
  
  try {
    await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), {
      [`quizResults.${quizType}`]: {
        results: results,
        timestamp: new Date().toISOString(),
        recommendations: generateQuizRecommendations(results)
      }
    });
    
    if (userProfile) {
      if (!userProfile.quizResults) userProfile.quizResults = {};
      userProfile.quizResults[quizType] = {
        results: results,
        timestamp: new Date().toISOString(),
        recommendations: generateQuizRecommendations(results)
      };
    }
  } catch (error) {
    console.error('Error saving quiz results:', error);
  }
}

// Update user preferences
async function updateUserPreferences(preferences) {
  if (!currentUser) return;
  
  try {
    await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), {
      preferences: { ...userProfile?.preferences, ...preferences }
    });
    
    if (userProfile) {
      userProfile.preferences = { ...userProfile.preferences, ...preferences };
    }
  } catch (error) {
    console.error('Error updating preferences:', error);
  }
}

// Track course view
async function trackCourseView(courseId) {
  if (!currentUser) return;
  
  try {
    const viewData = {
      courseId: courseId,
      timestamp: new Date().toISOString()
    };
    
    // Add to recently viewed (keep last 10)
    const recentlyViewed = userProfile?.recentlyViewed || [];
    const updatedRecentlyViewed = [viewData, ...recentlyViewed.filter(item => item.courseId !== courseId)].slice(0, 10);
    
    await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), {
      recentlyViewed: updatedRecentlyViewed
    });
    
    if (userProfile) {
      userProfile.recentlyViewed = updatedRecentlyViewed;
    }
  } catch (error) {
    console.error('Error tracking course view:', error);
  }
}

// Enhanced signup form with additional fields
function getSignupForm() {
  return `
    <div class="auth-form">
      <h2>Create Your ImpactMojo Account</h2>
      <div class="signup-benefits">
        <p><i class="fas fa-check"></i> Track progress across all courses</p>
        <p><i class="fas fa-check"></i> Save notes with academic citations</p>
        <p><i class="fas fa-check"></i> Get personalized learning paths</p>
        <p><i class="fas fa-check"></i> Access research library</p>
      </div>
      <form id="signup-form" onsubmit="handleSignup(event)">
        <div class="form-group">
          <label for="signup-name">Full Name</label>
          <input type="text" id="signup-name" required>
        </div>
        <div class="form-group">
          <label for="signup-email">Email</label>
          <input type="email" id="signup-email" required>
        </div>
        <div class="form-group">
          <label for="signup-organization">Organization (Optional)</label>
          <input type="text" id="signup-organization" placeholder="University, NGO, Government, etc.">
        </div>
        <div class="form-group">
          <label for="signup-role">Role (Optional)</label>
          <select id="signup-role">
            <option value="">Select your role</option>
            <option value="student">Student</option>
            <option value="researcher">Researcher</option>
            <option value="practitioner">Development Practitioner</option>
            <option value="academic">Academic/Educator</option>
            <option value="policy">Policy Maker</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div class="form-group">
          <label for="signup-password">Password</label>
          <input type="password" id="signup-password" minlength="6" required>
        </div>
        <div class="form-group">
          <label for="signup-confirm">Confirm Password</label>
          <input type="password" id="signup-confirm" required>
        </div>
        <div class="form-group">
          <label class="checkbox-label">
            <input type="checkbox" id="signup-updates">
            <span>I'd like to receive updates about new courses (optional)</span>
          </label>
        </div>
        <button type="submit" class="btn btn-primary">Create Account</button>
        <button type="button" class="btn btn-google" onclick="handleGoogleSignIn()">
          <i class="fab fa-google"></i> Sign up with Google
        </button>
      </form>
      <div class="form-switch">
        Already have an account? <a href="#" onclick="showAuthModal('login')">Log in</a>
      </div>
    </div>
  `;
}

// Enhanced signup handler
async function handleSignup(event) {
  event.preventDefault();
  
  const name = document.getElementById('signup-name').value;
  const email = document.getElementById('signup-email').value;
  const organization = document.getElementById('signup-organization').value;
  const role = document.getElementById('signup-role').value;
  const password = document.getElementById('signup-password').value;
  const confirmPassword = document.getElementById('signup-confirm').value;
  const emailUpdates = document.getElementById('signup-updates').checked;
  
  if (password !== confirmPassword) {
    showNotification('Passwords do not match', 'error');
    return;
  }
  
  showLoading(true);
  
  try {
    const userCredential = await window.createUserWithEmailAndPassword(window.auth, email, password);
    const user = userCredential.user;
    
    // Create enhanced user profile
    await createUserProfile(user.uid, {
      name: name,
      email: email,
      organization: organization,
      role: role,
      createdAt: new Date().toISOString(),
      completedCourses: [],
      bookmarkedCourses: [],
      notes: {},
      recentlyViewed: [],
      preferences: {
        theme: 'light',
        notifications: true,
        emailUpdates: emailUpdates
      }
    });
    
    closeAuthModal();
    showNotification('Account created successfully! Welcome to ImpactMojo!', 'success');
  } catch (error) {
    console.error('Signup error:', error);
    showNotification(getAuthErrorMessage(error), 'error');
  } finally {
    showLoading(false);
  }
}

// Global functions for enhanced features
window.saveUserNotes = saveUserNotes;
window.saveQuizResults = saveQuizResults;
window.updateUserPreferences = updateUserPreferences;
window.trackCourseView = trackCourseView;

// Show authentication modal
function showAuthModal(mode = 'login') {
  const modal = document.getElementById('auth-modal');
  const container = document.getElementById('auth-form-container');
  
  if (mode === 'login') {
    container.innerHTML = getLoginForm();
  } else {
    container.innerHTML = getSignupForm();
  }
  
  modal.style.display = 'block';
}

// Close authentication modal
function closeAuthModal() {
  const modal = document.getElementById('auth-modal');
  modal.style.display = 'none';
}

// Get login form HTML
function getLoginForm() {
  return `
    <div class="auth-form">
      <h2>Log In to ImpactMojo</h2>
      <form id="login-form" onsubmit="handleLogin(event)">
        <div class="form-group">
          <label for="login-email">Email</label>
          <input type="email" id="login-email" required>
        </div>
        <div class="form-group">
          <label for="login-password">Password</label>
          <input type="password" id="login-password" required>
        </div>
        <button type="submit" class="btn btn-primary">Log In</button>
        <button type="button" class="btn btn-google" onclick="handleGoogleSignIn()">
          <i class="fab fa-google"></i> Sign in with Google
        </button>
      </form>
      <div class="form-switch">
        Don't have an account? <a href="#" onclick="showAuthModal('signup')">Sign up</a>
      </div>
      <div class="form-switch">
        <a href="#" onclick="handleForgotPassword()">Forgot password?</a>
      </div>
    </div>
  `;
}

// Get signup form HTML
function getSignupForm() {
  return `
    <div class="auth-form">
      <h2>Create Your Account</h2>
      <form id="signup-form" onsubmit="handleSignup(event)">
        <div class="form-group">
          <label for="signup-name">Full Name</label>
          <input type="text" id="signup-name" required>
        </div>
        <div class="form-group">
          <label for="signup-email">Email</label>
          <input type="email" id="signup-email" required>
        </div>
        <div class="form-group">
          <label for="signup-password">Password</label>
          <input type="password" id="signup-password" minlength="6" required>
        </div>
        <div class="form-group">
          <label for="signup-confirm">Confirm Password</label>
          <input type="password" id="signup-confirm" required>
        </div>
        <button type="submit" class="btn btn-primary">Create Account</button>
        <button type="button" class="btn btn-google" onclick="handleGoogleSignIn()">
          <i class="fab fa-google"></i> Sign up with Google
        </button>
      </form>
      <div class="form-switch">
        Already have an account? <a href="#" onclick="showAuthModal('login')">Log in</a>
      </div>
    </div>
  `;
}

// Handle login form submission
async function handleLogin(event) {
  event.preventDefault();
  
  const email = document.getElementById('login-email').value;
  const password = document.getElementById('login-password').value;
  
  showLoading(true);
  
  try {
    await window.signInWithEmailAndPassword(window.auth, email, password);
    closeAuthModal();
    showNotification('Successfully logged in!', 'success');
  } catch (error) {
    console.error('Login error:', error);
    showNotification(getAuthErrorMessage(error), 'error');
  } finally {
    showLoading(false);
  }
}

// Handle signup form submission
async function handleSignup(event) {
  event.preventDefault();
  
  const name = document.getElementById('signup-name').value;
  const email = document.getElementById('signup-email').value;
  const password = document.getElementById('signup-password').value;
  const confirmPassword = document.getElementById('signup-confirm').value;
  
  if (password !== confirmPassword) {
    showNotification('Passwords do not match', 'error');
    return;
  }
  
  showLoading(true);
  
  try {
    const userCredential = await window.createUserWithEmailAndPassword(window.auth, email, password);
    const user = userCredential.user;
    
    // Create user profile in Firestore
    await createUserProfile(user.uid, {
      name: name,
      email: email,
      createdAt: new Date().toISOString(),
      completedCourses: [],
      bookmarkedCourses: [],
      notes: {},
      preferences: {
        theme: 'light',
        notifications: true
      }
    });
    
    closeAuthModal();
    showNotification('Account created successfully!', 'success');
  } catch (error) {
    console.error('Signup error:', error);
    showNotification(getAuthErrorMessage(error), 'error');
  } finally {
    showLoading(false);
  }
}

// Handle Google Sign-In
async function handleGoogleSignIn() {
  showLoading(true);
  
  try {
    const result = await window.signInWithPopup(window.auth, window.provider);
    const user = result.user;
    
    // Check if this is a new user
    const userDoc = await window.getDoc(window.doc(window.db, 'users', user.uid));
    
    if (!userDoc.exists()) {
      // Create profile for new Google user
      await createUserProfile(user.uid, {
        name: user.displayName,
        email: user.email,
        createdAt: new Date().toISOString(),
        completedCourses: [],
        bookmarkedCourses: [],
        notes: {},
        preferences: {
          theme: 'light',
          notifications: true
        }
      });
    }
    
    closeAuthModal();
    showNotification('Successfully signed in with Google!', 'success');
  } catch (error) {
    console.error('Google sign-in error:', error);
    showNotification(getAuthErrorMessage(error), 'error');
  } finally {
    showLoading(false);
  }
}

// Handle logout
async function handleLogout() {
  try {
    await window.signOut(window.auth);
    showNotification('Successfully logged out', 'success');
    closeDashboard(); // Close dashboard if open
  } catch (error) {
    console.error('Logout error:', error);
    showNotification('Error logging out', 'error');
  }
}

// Handle forgot password
async function handleForgotPassword() {
  const email = prompt('Enter your email address:');
  if (!email) return;
  
  try {
    await window.sendPasswordResetEmail(window.auth, email);
    showNotification('Password reset email sent!', 'success');
    closeAuthModal();
  } catch (error) {
    console.error('Password reset error:', error);
    showNotification(getAuthErrorMessage(error), 'error');
  }
}

// Create user profile in Firestore
async function createUserProfile(uid, profileData) {
  try {
    await window.setDoc(window.doc(window.db, 'users', uid), profileData);
  } catch (error) {
    console.error('Error creating user profile:', error);
    throw error;
  }
}

// Load user profile from Firestore
async function loadUserProfile(uid) {
  try {
    const userDoc = await window.getDoc(window.doc(window.db, 'users', uid));
    if (userDoc.exists()) {
      userProfile = userDoc.data();
    }
  } catch (error) {
    console.error('Error loading user profile:', error);
  }
}

// Update user profile
async function updateUserProfile(updates) {
  if (!currentUser) return;
  
  try {
    await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), updates);
    userProfile = { ...userProfile, ...updates };
  } catch (error) {
    console.error('Error updating user profile:', error);
    throw error;
  }
}

// Mark course as completed
async function markCourseCompleted(courseId) {
  if (!currentUser || !userProfile) return;
  
  if (!userProfile.completedCourses.includes(courseId)) {
    try {
      await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), {
        completedCourses: window.arrayUnion(courseId)
      });
      userProfile.completedCourses.push(courseId);
      showNotification('Course marked as completed!', 'success');
    } catch (error) {
      console.error('Error marking course as completed:', error);
      showNotification('Error updating progress', 'error');
    }
  }
}

// Toggle course bookmark
async function toggleCourseBookmark(courseId) {
  if (!currentUser || !userProfile) return;
  
  try {
    const isBookmarked = userProfile.bookmarkedCourses.includes(courseId);
    
    if (isBookmarked) {
      await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), {
        bookmarkedCourses: window.arrayRemove(courseId)
      });
      userProfile.bookmarkedCourses = userProfile.bookmarkedCourses.filter(id => id !== courseId);
      showNotification('Bookmark removed', 'info');
    } else {
      await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), {
        bookmarkedCourses: window.arrayUnion(courseId)
      });
      userProfile.bookmarkedCourses.push(courseId);
      showNotification('Course bookmarked!', 'success');
    }
  } catch (error) {
    console.error('Error toggling bookmark:', error);
    showNotification('Error updating bookmark', 'error');
  }
}

// Save user notes for a course
async function saveUserNotes(courseId, notes) {
  if (!currentUser) return;
  
  try {
    await window.updateDoc(window.doc(window.db, 'users', currentUser.uid), {
      [`notes.${courseId}`]: notes
    });
    if (userProfile) {
      userProfile.notes[courseId] = notes;
    }
  } catch (error) {
    console.error('Error saving notes:', error);
    throw error;
  }
}

// Get user notes for a course
function getUserNotes(courseId) {
  return userProfile?.notes?.[courseId] || '';
}

// Check if course is completed
function isCourseCompleted(courseId) {
  return userProfile?.completedCourses?.includes(courseId) || false;
}

// Check if course is bookmarked
function isCourseBookmarked(courseId) {
  return userProfile?.bookmarkedCourses?.includes(courseId) || false;
}

// Get user progress statistics
function getUserProgress() {
  if (!userProfile) return { completed: 0, bookmarked: 0, total: courses.length };
  
  return {
    completed: userProfile.completedCourses?.length || 0,
    bookmarked: userProfile.bookmarkedCourses?.length || 0,
    total: courses.length
  };
}

// Convert Firebase auth errors to user-friendly messages
function getAuthErrorMessage(error) {
  switch (error.code) {
    case 'auth/user-not-found':
      return 'No account found with this email address.';
    case 'auth/wrong-password':
      return 'Incorrect password.';
    case 'auth/email-already-in-use':
      return 'An account with this email already exists.';
    case 'auth/weak-password':
      return 'Password should be at least 6 characters.';
    case 'auth/invalid-email':
      return 'Please enter a valid email address.';
    case 'auth/too-many-requests':
      return 'Too many failed attempts. Please try again later.';
    case 'auth/popup-closed-by-user':
      return 'Sign-in popup was closed.';
    default:
      return 'An error occurred. Please try again.';
  }
}

// Show loading overlay
function showLoading(show) {
  const loading = document.getElementById('loading');
  if (loading) {
    loading.style.display = show ? 'flex' : 'none';
  }
}

// Show notification
function showNotification(message, type = 'info') {
  // Create notification element if it doesn't exist
  let notification = document.getElementById('notification');
  if (!notification) {
    notification = document.createElement('div');
    notification.id = 'notification';
    notification.style.cssText = `
      position: fixed;
      top: 20px;
      right: 20px;
      padding: 1rem 1.5rem;
      border-radius: 8px;
      color: white;
      font-weight: 500;
      z-index: 10000;
      transition: all 0.3s ease;
      transform: translateX(400px);
    `;
    document.body.appendChild(notification);
  }
  
  // Set notification style based on type
  const colors = {
    success: '#2ecc71',
    error: '#e74c3c',
    warning: '#f39c12',
    info: '#3498db'
  };
  
  notification.style.backgroundColor = colors[type] || colors.info;
  notification.textContent = message;
  notification.style.transform = 'translateX(0)';
  
  // Auto-hide after 3 seconds
  setTimeout(() => {
    notification.style.transform = 'translateX(400px)';
  }, 3000);
}

// Initialize authentication when page loads
document.addEventListener('DOMContentLoaded', () => {
  // Wait a bit for Firebase to load
  setTimeout(initializeAuth, 500);
});

// Close modal when clicking outside
window.onclick = function(event) {
  const authModal = document.getElementById('auth-modal');
  const dashboardModal = document.getElementById('dashboard-modal');
  
  if (event.target === authModal) {
    closeAuthModal();
  }
  if (event.target === dashboardModal) {
    closeDashboard();
  }
}