// 🔥 FIREBASE CONFIGURATION 🔥
// Your ImpactMojo Firebase project configuration
const firebaseConfig = {
  apiKey: "AIzaSyDnF0eJsTULzOJUnBskybd44dG5w-f46vE",
  authDomain: "impactmojo.firebaseapp.com",
  projectId: "impactmojo",
  storageBucket: "impactmojo.firebasestorage.app",
  messagingSenderId: "529198336589",
  appId: "1:529198336589:web:1664b5344de5bfb31bea04",
  measurementId: "G-ZHPPXXMRGV"
};

// Import Firebase modules (using Firebase v9 modular SDK)
import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-app.js';
import { 
  getAuth, 
  signInWithEmailAndPassword, 
  createUserWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  sendPasswordResetEmail,
  GoogleAuthProvider,
  signInWithPopup,
  updateProfile
} from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-auth.js';
import { 
  getFirestore, 
  doc, 
  setDoc, 
  getDoc, 
  updateDoc,
  collection,
  addDoc,
  query,
  where,
  getDocs,
  orderBy,
  serverTimestamp
} from 'https://www.gstatic.com/firebasejs/9.22.0/firebase-firestore.js';

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const googleProvider = new GoogleAuthProvider();

// 🎯 AUTHENTICATION STATE MANAGEMENT
let currentUser = null;

// Monitor authentication state changes
onAuthStateChanged(auth, (user) => {
  currentUser = user;
  updateUIForAuthState(user);
  
  if (user) {
    console.log('User signed in:', user.email);
    // Load user data when signed in
    loadUserData(user.uid);
  } else {
    console.log('User signed out');
    // Clear user data when signed out
    clearUserData();
  }
});

// 📝 USER REGISTRATION
async function signUpUser(email, password, displayName) {
  try {
    // Create user account
    const userCredential = await createUserWithEmailAndPassword(auth, email, password);
    const user = userCredential.user;
    
    // Update user profile with display name
    await updateProfile(user, {
      displayName: displayName
    });
    
    // Create user document in Firestore
    await createUserDocument(user.uid, {
      email: user.email,
      displayName: displayName,
      createdAt: serverTimestamp(),
      lastLoginAt: serverTimestamp(),
      totalCoursesAccessed: 0,
      bookmarkedCourses: [],
      completedCourses: [],
      progressData: {},
      membershipTier: 'free',
      preferences: {
        emailNotifications: true,
        courseReminders: true,
        newsletter: true
      }
    });
    
    showNotification('Account created successfully! Welcome to ImpactMojo!', 'success');
    closeModal('signupModal');
    
    return { success: true, user: user };
  } catch (error) {
    console.error('Sign up error:', error);
    showNotification(getErrorMessage(error.code), 'error');
    return { success: false, error: error.message };
  }
}

// 🔐 USER LOGIN
async function signInUser(email, password) {
  try {
    const userCredential = await signInWithEmailAndPassword(auth, email, password);
    const user = userCredential.user;
    
    // Update last login time
    await updateUserDocument(user.uid, {
      lastLoginAt: serverTimestamp()
    });
    
    showNotification(`Welcome back, ${user.displayName || user.email}!`, 'success');
    closeModal('loginModal');
    
    return { success: true, user: user };
  } catch (error) {
    console.error('Sign in error:', error);
    showNotification(getErrorMessage(error.code), 'error');
    return { success: false, error: error.message };
  }
}

// 🌐 GOOGLE SIGN-IN
async function signInWithGoogle() {
  try {
    const result = await signInWithPopup(auth, googleProvider);
    const user = result.user;
    
    // Check if this is a new user
    const userDoc = await getUserDocument(user.uid);
    
    if (!userDoc.exists()) {
      // Create user document for new Google users
      await createUserDocument(user.uid, {
        email: user.email,
        displayName: user.displayName,
        photoURL: user.photoURL,
        createdAt: serverTimestamp(),
        lastLoginAt: serverTimestamp(),
        authProvider: 'google',
        totalCoursesAccessed: 0,
        bookmarkedCourses: [],
        completedCourses: [],
        progressData: {},
        membershipTier: 'free',
        preferences: {
          emailNotifications: true,
          courseReminders: true,
          newsletter: true
        }
      });
      showNotification('Welcome to ImpactMojo! Your account has been created.', 'success');
    } else {
      // Update last login for existing users
      await updateUserDocument(user.uid, {
        lastLoginAt: serverTimestamp()
      });
      showNotification(`Welcome back, ${user.displayName}!`, 'success');
    }
    
    closeModal('loginModal');
    closeModal('signupModal');
    
    return { success: true, user: user };
  } catch (error) {
    console.error('Google sign in error:', error);
    showNotification(getErrorMessage(error.code), 'error');
    return { success: false, error: error.message };
  }
}

// 🚪 USER LOGOUT
async function logoutUser() {
  try {
    await signOut(auth);
    showNotification('Signed out successfully', 'success');
    return { success: true };
  } catch (error) {
    console.error('Sign out error:', error);
    showNotification('Error signing out', 'error');
    return { success: false, error: error.message };
  }
}

// 🔄 PASSWORD RESET
async function resetPassword(email) {
  try {
    await sendPasswordResetEmail(auth, email);
    showNotification('Password reset email sent! Check your inbox.', 'success');
    return { success: true };
  } catch (error) {
    console.error('Password reset error:', error);
    showNotification(getErrorMessage(error.code), 'error');
    return { success: false, error: error.message };
  }
}

// 💾 FIRESTORE USER DOCUMENT FUNCTIONS
async function createUserDocument(userId, userData) {
  try {
    await setDoc(doc(db, 'users', userId), userData);
    return { success: true };
  } catch (error) {
    console.error('Error creating user document:', error);
    return { success: false, error: error.message };
  }
}

async function getUserDocument(userId) {
  try {
    return await getDoc(doc(db, 'users', userId));
  } catch (error) {
    console.error('Error getting user document:', error);
    return null;
  }
}

async function updateUserDocument(userId, updateData) {
  try {
    await updateDoc(doc(db, 'users', userId), updateData);
    return { success: true };
  } catch (error) {
    console.error('Error updating user document:', error);
    return { success: false, error: error.message };
  }
}

// 📚 COURSE PROGRESS FUNCTIONS
async function saveUserProgress(courseId, progressData) {
  if (!currentUser) return { success: false, error: 'User not authenticated' };
  
  try {
    const userRef = doc(db, 'users', currentUser.uid);
    const progressUpdate = {
      [`progressData.${courseId}`]: {
        ...progressData,
        lastUpdated: serverTimestamp()
      }
    };
    
    await updateDoc(userRef, progressUpdate);
    return { success: true };
  } catch (error) {
    console.error('Error saving progress:', error);
    return { success: false, error: error.message };
  }
}

async function saveUserBookmark(courseId, courseTitle) {
  if (!currentUser) return { success: false, error: 'User not authenticated' };
  
  try {
    const userDoc = await getUserDocument(currentUser.uid);
    const userData = userDoc.data();
    const bookmarks = userData.bookmarkedCourses || [];
    
    if (!bookmarks.find(b => b.courseId === courseId)) {
      bookmarks.push({
        courseId: courseId,
        courseTitle: courseTitle,
        bookmarkedAt: serverTimestamp()
      });
      
      await updateUserDocument(currentUser.uid, {
        bookmarkedCourses: bookmarks
      });
    }
    
    return { success: true };
  } catch (error) {
    console.error('Error saving bookmark:', error);
    return { success: false, error: error.message };
  }
}

async function removeUserBookmark(courseId) {
  if (!currentUser) return { success: false, error: 'User not authenticated' };
  
  try {
    const userDoc = await getUserDocument(currentUser.uid);
    const userData = userDoc.data();
    const bookmarks = userData.bookmarkedCourses || [];
    
    const updatedBookmarks = bookmarks.filter(b => b.courseId !== courseId);
    
    await updateUserDocument(currentUser.uid, {
      bookmarkedCourses: updatedBookmarks
    });
    
    return { success: true };
  } catch (error) {
    console.error('Error removing bookmark:', error);
    return { success: false, error: error.message };
  }
}

// 📝 USER NOTES FUNCTIONS
async function saveUserNote(noteText, courseId = null) {
  if (!currentUser) return { success: false, error: 'User not authenticated' };
  
  try {
    const noteData = {
      userId: currentUser.uid,
      noteText: noteText,
      courseId: courseId,
      createdAt: serverTimestamp(),
      updatedAt: serverTimestamp()
    };
    
    const docRef = await addDoc(collection(db, 'userNotes'), noteData);
    return { success: true, noteId: docRef.id };
  } catch (error) {
    console.error('Error saving note:', error);
    return { success: false, error: error.message };
  }
}

async function getUserNotes(courseId = null) {
  if (!currentUser) return { success: false, error: 'User not authenticated' };
  
  try {
    let q;
    if (courseId) {
      q = query(
        collection(db, 'userNotes'),
        where('userId', '==', currentUser.uid),
        where('courseId', '==', courseId),
        orderBy('createdAt', 'desc')
      );
    } else {
      q = query(
        collection(db, 'userNotes'),
        where('userId', '==', currentUser.uid),
        orderBy('createdAt', 'desc')
      );
    }
    
    const querySnapshot = await getDocs(q);
    const notes = [];
    querySnapshot.forEach((doc) => {
      notes.push({ id: doc.id, ...doc.data() });
    });
    
    return { success: true, notes: notes };
  } catch (error) {
    console.error('Error getting notes:', error);
    return { success: false, error: error.message };
  }
}

// 🎨 UI UPDATE FUNCTIONS
function updateUIForAuthState(user) {
  const authButtons = document.getElementById('authButtons');
  const userMenu = document.getElementById('userMenu');
  const userName = document.getElementById('userName');
  const userDashboard = document.getElementById('userDashboard');
  
  if (user) {
    // User is signed in
    if (authButtons) authButtons.style.display = 'none';
    if (userMenu) userMenu.style.display = 'inline-flex';
    if (userName) userName.textContent = user.displayName || user.email.split('@')[0];
    
    // Show member benefits
    showMemberBenefits();
  } else {
    // User is signed out
    if (authButtons) authButtons.style.display = 'inline-flex';
    if (userMenu) userMenu.style.display = 'none';
    if (userDashboard) userDashboard.style.display = 'none';
    
    // Hide member benefits
    hideMemberBenefits();
  }
}

function showMemberBenefits() {
  // Add member-only features visibility
  const memberElements = document.querySelectorAll('.member-only');
  memberElements.forEach(el => el.style.display = 'block');
  
  // Show discount codes
  const discountElements = document.querySelectorAll('.discount-code');
  discountElements.forEach(el => el.style.display = 'inline-block');
}

function hideMemberBenefits() {
  const memberElements = document.querySelectorAll('.member-only');
  memberElements.forEach(el => el.style.display = 'none');
  
  const discountElements = document.querySelectorAll('.discount-code');
  discountElements.forEach(el => el.style.display = 'none');
}

async function loadUserData(userId) {
  try {
    const userDoc = await getUserDocument(userId);
    if (userDoc.exists()) {
      const userData = userDoc.data();
      
      // Update dashboard with user data
      updateDashboard(userData);
      
      // Load user notes
      const notesResult = await getUserNotes();
      if (notesResult.success) {
        displayUserNotes(notesResult.notes);
      }
    }
  } catch (error) {
    console.error('Error loading user data:', error);
  }
}

function clearUserData() {
  // Clear any cached user data
  const userNotes = document.getElementById('userNotes');
  if (userNotes) userNotes.innerHTML = '';
  
  const dashboardStats = document.querySelectorAll('.dashboard-stat');
  dashboardStats.forEach(stat => stat.textContent = '0');
}

function updateDashboard(userData) {
  // Update dashboard statistics
  const coursesAccessedEl = document.getElementById('coursesAccessed');
  const bookmarksCountEl = document.getElementById('bookmarksCount');
  const notesCountEl = document.getElementById('notesCount');
  
  if (coursesAccessedEl) coursesAccessedEl.textContent = userData.totalCoursesAccessed || 0;
  if (bookmarksCountEl) bookmarksCountEl.textContent = userData.bookmarkedCourses?.length || 0;
  
  // Display bookmarked courses
  if (userData.bookmarkedCourses && userData.bookmarkedCourses.length > 0) {
    displayBookmarkedCourses(userData.bookmarkedCourses);
  }
}

function displayUserNotes(notes) {
  const notesContainer = document.getElementById('userNotes');
  if (!notesContainer) return;
  
  if (notes.length === 0) {
    notesContainer.innerHTML = '<p>No notes saved yet. Start taking notes during courses!</p>';
    return;
  }
  
  const notesHTML = notes.map(note => `
    <div class="note-item">
      <div class="note-content">${note.noteText}</div>
      <div class="note-meta">
        ${note.courseId ? `Course: ${note.courseId} • ` : ''}
        ${note.createdAt ? new Date(note.createdAt.toDate()).toLocaleDateString() : ''}
      </div>
    </div>
  `).join('');
  
  notesContainer.innerHTML = notesHTML;
}

function displayBookmarkedCourses(bookmarks) {
  const bookmarksContainer = document.getElementById('bookmarkedCourses');
  if (!bookmarksContainer) return;
  
  const bookmarksHTML = bookmarks.map(bookmark => `
    <div class="bookmark-item">
      <span class="bookmark-title">${bookmark.courseTitle}</span>
      <button onclick="removeBookmark('${bookmark.courseId}')" class="remove-bookmark">
        <i class="fas fa-times"></i>
      </button>
    </div>
  `).join('');
  
  bookmarksContainer.innerHTML = bookmarksHTML;
}

// 📢 NOTIFICATION SYSTEM
function showNotification(message, type = 'info') {
  // Create notification element
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.innerHTML = `
    <span class="notification-message">${message}</span>
    <button class="notification-close" onclick="this.parentElement.remove()">×</button>
  `;
  
  // Add to page
  document.body.appendChild(notification);
  
  // Auto remove after 5 seconds
  setTimeout(() => {
    if (notification.parentElement) {
      notification.remove();
    }
  }, 5000);
}

// 🔧 UTILITY FUNCTIONS
function getErrorMessage(errorCode) {
  const errorMessages = {
    'auth/user-not-found': 'No account found with this email address.',
    'auth/wrong-password': 'Incorrect password. Please try again.',
    'auth/email-already-in-use': 'An account with this email already exists.',
    'auth/weak-password': 'Password should be at least 6 characters long.',
    'auth/invalid-email': 'Please enter a valid email address.',
    'auth/too-many-requests': 'Too many failed attempts. Please try again later.',
    'auth/network-request-failed': 'Network error. Please check your connection.',
    'auth/popup-closed-by-user': 'Sign-in popup was closed. Please try again.',
    'auth/cancelled-popup-request': 'Sign-in was cancelled. Please try again.'
  };
  
  return errorMessages[errorCode] || 'An error occurred. Please try again.';
}

// 🌐 GLOBAL FUNCTIONS (called from HTML)
window.signup = async function(email, password, displayName) {
  return await signUpUser(email, password, displayName);
};

window.login = async function(email, password) {
  return await signInUser(email, password);
};

window.loginWithGoogle = async function() {
  return await signInWithGoogle();
};

window.logout = async function() {
  return await logoutUser();
};

window.resetPassword = async function(email) {
  return await resetPassword(email);
};

window.saveNote = async function(noteText, courseId = null) {
  return await saveUserNote(noteText, courseId);
};

window.toggleBookmark = async function(courseId, courseTitle) {
  if (!currentUser) {
    showNotification('Please sign in to bookmark courses', 'error');
    return;
  }
  
  // Check if already bookmarked
  const userDoc = await getUserDocument(currentUser.uid);
  const userData = userDoc.data();
  const bookmarks = userData.bookmarkedCourses || [];
  
  if (bookmarks.find(b => b.courseId === courseId)) {
    return await removeUserBookmark(courseId);
  } else {
    return await saveUserBookmark(courseId, courseTitle);
  }
};

window.removeBookmark = async function(courseId) {
  return await removeUserBookmark(courseId);
};

window.toggleUserDashboard = function() {
  const dashboard = document.getElementById('userDashboard');
  if (dashboard) {
    dashboard.style.display = dashboard.style.display === 'none' ? 'block' : 'none';
    
    // Scroll to dashboard if showing
    if (dashboard.style.display === 'block') {
      dashboard.scrollIntoView({ behavior: 'smooth' });
    }
  }
};

// Initialize authentication when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  console.log('Firebase Auth initialized for ImpactMojo');
  
  // Add CSS for notifications if not present
  if (!document.getElementById('notificationStyles')) {
    const style = document.createElement('style');
    style.id = 'notificationStyles';
    style.textContent = `
      .notification {
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 10000;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        animation: slideIn 0.3s ease;
      }
      
      .notification-success { background: #27ae60; }
      .notification-error { background: #e74c3c; }
      .notification-info { background: #3498db; }
      .notification-warning { background: #f39c12; }
      
      .notification-close {
        background: none;
        border: none;
        color: white;
        font-size: 1.2rem;
        cursor: pointer;
        padding: 0;
        margin-left: auto;
      }
      
      @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
      }
    `;
    document.head.appendChild(style);
  }
});

console.log('🔥 Firebase Auth configured for ImpactMojo - Ready to use!');