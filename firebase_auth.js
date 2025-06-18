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
let notesTimeout;

// Monitor authentication state changes
onAuthStateChanged(auth, (user) => {
  currentUser = user;
  updateUIForAuthState(user);
  
  if (user) {
    console.log('User signed in:', user.email);
    // Load user data when signed in
    loadUserData(user.uid);
    // Initialize member services
    initializeMemberServices();
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
      },
      // NEW: Member services data
      notes: '',
      skills: {},
      consultationHistory: [],
      assessmentResults: [],
      memberServices: {
        consultationsUsed: 0,
        cvReviewsRequested: 0,
        interviewPrepSessions: 0,
        skillAssessmentsTaken: 0
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
        },
        // NEW: Member services data
        notes: '',
        skills: {},
        consultationHistory: [],
        assessmentResults: [],
        memberServices: {
          consultationsUsed: 0,
          cvReviewsRequested: 0,
          interviewPrepSessions: 0,
          skillAssessmentsTaken: 0
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

// 🔖 ENHANCED BOOKMARK FUNCTIONS
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
      
      showNotification('Course bookmarked!', 'success');
      updateBookmarkedCoursesList();
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
    
    showNotification('Bookmark removed', 'success');
    updateBookmarkedCoursesList();
    
    return { success: true };
  } catch (error) {
    console.error('Error removing bookmark:', error);
    return { success: false, error: error.message };
  }
}

// 📝 ENHANCED NOTES FUNCTIONS WITH AUTO-SAVE
async function saveUserNotes() {
  if (!currentUser) {
    // If not logged in, save to localStorage as fallback
    const notes = document.getElementById('userNotes')?.value || '';
    localStorage.setItem('userNotes', notes);
    return;
  }
  
  try {
    const notes = document.getElementById('userNotes')?.value || '';
    await updateUserDocument(currentUser.uid, {
      notes: notes,
      lastUpdated: serverTimestamp()
    });
    
    // Show success indicator briefly
    showNotification('Notes saved automatically', 'success');
  } catch (error) {
    console.error('Error saving notes:', error);
    showNotification('Failed to save notes', 'error');
  }
}

async function loadUserNotes() {
  if (!currentUser) {
    // Load from localStorage if not logged in
    const savedNotes = localStorage.getItem('userNotes') || '';
    const notesTextarea = document.getElementById('userNotes');
    if (notesTextarea) notesTextarea.value = savedNotes;
    return;
  }
  
  try {
    const userDoc = await getUserDocument(currentUser.uid);
    if (userDoc.exists() && userDoc.data().notes) {
      const notesTextarea = document.getElementById('userNotes');
      if (notesTextarea) notesTextarea.value = userDoc.data().notes;
    }
  } catch (error) {
    console.error('Error loading notes:', error);
  }
}

function setupNotesAutoSave() {
  const notesTextarea = document.getElementById('userNotes');
  if (!notesTextarea) return;
  
  notesTextarea.addEventListener('input', function() {
    clearTimeout(notesTimeout);
    notesTimeout = setTimeout(saveUserNotes, 2000); // Save after 2 seconds of no typing
  });
}

// 🔧 MEMBER SERVICES FUNCTIONS

// Consultation Booking
async function bookConsultation(consultationType, preferredDate, preferredTime, userMessage) {
  if (!currentUser) {
    showNotification('Please log in to book a consultation', 'error');
    return { success: false, error: 'User not authenticated' };
  }

  try {
    const bookingData = {
      userId: currentUser.uid,
      userEmail: currentUser.email,
      userName: currentUser.displayName || 'User',
      consultationType: consultationType,
      preferredDate: preferredDate,
      preferredTime: preferredTime,
      message: userMessage,
      status: 'pending',
      createdAt: serverTimestamp(),
      discountCode: `IMPACT10-${currentUser.uid.substring(0, 8)}`
    };

    // Save to Firestore
    await addDoc(collection(db, 'consultationRequests'), bookingData);
    
    // Update user's consultation count
    const userDoc = await getUserDocument(currentUser.uid);
    const userData = userDoc.data();
    const memberServices = userData.memberServices || {};
    
    await updateUserDocument(currentUser.uid, {
      'memberServices.consultationsUsed': (memberServices.consultationsUsed || 0) + 1
    });
    
    showNotification('Consultation request submitted! You\'ll receive a confirmation email within 24 hours.', 'success');
    
    return { success: true };
  } catch (error) {
    console.error('Error booking consultation:', error);
    showNotification('Error submitting request. Please try again.', 'error');
    return { success: false, error: error.message };
  }
}

// CV Review Request
async function requestCVReview(userMessage, urgency) {
  if (!currentUser) {
    showNotification('Please log in to request CV review', 'error');
    return { success: false, error: 'User not authenticated' };
  }

  try {
    const reviewData = {
      userId: currentUser.uid,
      userEmail: currentUser.email,
      userName: currentUser.displayName || 'User',
      message: userMessage,
      urgency: urgency,
      status: 'pending',
      createdAt: serverTimestamp()
    };

    await addDoc(collection(db, 'cvReviewRequests'), reviewData);
    
    // Update user's CV review count
    const userDoc = await getUserDocument(currentUser.uid);
    const userData = userDoc.data();
    const memberServices = userData.memberServices || {};
    
    await updateUserDocument(currentUser.uid, {
      'memberServices.cvReviewsRequested': (memberServices.cvReviewsRequested || 0) + 1
    });
    
    showNotification('CV review request submitted! You\'ll receive instructions for submitting your CV within 24 hours.', 'success');
    
    return { success: true };
  } catch (error) {
    console.error('Error requesting CV review:', error);
    showNotification('Error submitting request. Please try again.', 'error');
    return { success: false, error: error.message };
  }
}

// Interview Prep Booking
async function bookInterviewPrep(interviewType, companyInfo, timeframe, specificAreas) {
  if (!currentUser) {
    showNotification('Please log in to book interview preparation', 'error');
    return { success: false, error: 'User not authenticated' };
  }

  try {
    const prepData = {
      userId: currentUser.uid,
      userEmail: currentUser.email,
      userName: currentUser.displayName || 'User',
      interviewType: interviewType,
      companyInfo: companyInfo,
      timeframe: timeframe,
      specificAreas: specificAreas,
      status: 'pending',
      createdAt: serverTimestamp()
    };

    await addDoc(collection(db, 'interviewPrepRequests'), prepData);
    
    // Update user's interview prep count
    const userDoc = await getUserDocument(currentUser.uid);
    const userData = userDoc.data();
    const memberServices = userData.memberServices || {};
    
    await updateUserDocument(currentUser.uid, {
      'memberServices.interviewPrepSessions': (memberServices.interviewPrepSessions || 0) + 1
    });
    
    showNotification('Interview prep request submitted! You\'ll be contacted to schedule your session.', 'success');
    
    return { success: true };
  } catch (error) {
    console.error('Error booking interview prep:', error);
    showNotification('Error submitting request. Please try again.', 'error');
    return { success: false, error: error.message };
  }
}

// 🎓 SKILL ASSESSMENT SYSTEM
const skillAssessments = {
  'data-literacy': {
    name: 'Data Literacy Assessment',
    description: 'Test your understanding of data concepts, visualization, and basic analysis',
    questions: [
      {
        question: 'Which measure of central tendency is most appropriate for highly skewed data?',
        options: ['Mean', 'Median', 'Mode', 'Range'],
        correct: 1,
        explanation: 'Median is less affected by extreme values in skewed distributions'
      },
      {
        question: 'What does a correlation coefficient of -0.8 indicate?',
        options: ['Strong positive relationship', 'Weak positive relationship', 'Strong negative relationship', 'No relationship'],
        correct: 2,
        explanation: 'Values close to -1 indicate strong negative correlation'
      },
      {
        question: 'In a survey of 1000 households, what is the margin of error at 95% confidence level?',
        options: ['±1%', '±3.1%', '±5%', '±10%'],
        correct: 1,
        explanation: 'For n=1000, margin of error = 1.96 × √(0.25/1000) ≈ 3.1%'
      }
    ],
    passingScore: 70,
    duration: 15 // minutes
  },
  'gender-analysis': {
    name: 'Gender Analysis Skills',
    description: 'Assess your knowledge of gender frameworks and analysis methods',
    questions: [
      {
        question: 'What is the primary purpose of the Harvard Analytical Framework?',
        options: ['Gender budgeting', 'Roles and responsibilities analysis', 'Violence prevention', 'Legal reform'],
        correct: 1,
        explanation: 'The Harvard Framework focuses on analyzing productive, reproductive, and community roles'
      },
      {
        question: 'Which concept refers to socially constructed roles and behaviors?',
        options: ['Sex', 'Gender', 'Biology', 'Anatomy'],
        correct: 1,
        explanation: 'Gender refers to socially constructed roles, while sex refers to biological differences'
      }
    ],
    passingScore: 75,
    duration: 10
  },
  'policy-analysis': {
    name: 'Policy Analysis Fundamentals',
    description: 'Test your understanding of policy frameworks and analysis methods',
    questions: [
      {
        question: 'What is the first step in policy analysis?',
        options: ['Evaluate options', 'Define the problem', 'Implement solution', 'Monitor outcomes'],
        correct: 1,
        explanation: 'Problem definition is the crucial first step in any policy analysis'
      },
      {
        question: 'What does "evidence-based policy" mean?',
        options: ['Policy based on opinions', 'Policy based on research and data', 'Policy based on tradition', 'Policy based on politics'],
        correct: 1,
        explanation: 'Evidence-based policy uses research, data, and systematic analysis to inform decisions'
      }
    ],
    passingScore: 70,
    duration: 12
  }
};

async function completeSkillAssessment(assessmentId, answers, timeSpent) {
  if (!currentUser) {
    showNotification('Please log in to save assessment results', 'error');
    return { success: false, error: 'User not authenticated' };
  }

  const assessment = skillAssessments[assessmentId];
  
  // Calculate score
  let correctAnswers = 0;
  answers.forEach((answer, index) => {
    if (answer === assessment.questions[index].correct) {
      correctAnswers++;
    }
  });
  
  const score = Math.round((correctAnswers / assessment.questions.length) * 100);
  const passed = score >= assessment.passingScore;
  
  // Save results to Firestore
  try {
    const resultData = {
      userId: currentUser.uid,
      userEmail: currentUser.email,
      assessmentId: assessmentId,
      assessmentName: assessment.name,
      score: score,
      passed: passed,
      correctAnswers: correctAnswers,
      totalQuestions: assessment.questions.length,
      timeSpent: timeSpent,
      completedAt: serverTimestamp()
    };

    await addDoc(collection(db, 'assessmentResults'), resultData);
    
    // If passed, update user's skills
    if (passed) {
      await updateUserSkills(currentUser.uid, assessmentId, score);
    }
    
    // Update assessment count
    const userDoc = await getUserDocument(currentUser.uid);
    const userData = userDoc.data();
    const memberServices = userData.memberServices || {};
    
    await updateUserDocument(currentUser.uid, {
      'memberServices.skillAssessmentsTaken': (memberServices.skillAssessmentsTaken || 0) + 1
    });
    
    showNotification(`Assessment completed! Score: ${score}% ${passed ? '- Certificate earned!' : ''}`, passed ? 'success' : 'warning');
    
    return { success: true, score: score, passed: passed };
  } catch (error) {
    console.error('Error saving assessment results:', error);
    showNotification('Error saving results. Please try again.', 'error');
    return { success: false, error: error.message };
  }
}

async function updateUserSkills(userId, skillId, score) {
  try {
    const userDoc = await getUserDocument(userId);
    const userData = userDoc.data();
    const skills = userData.skills || {};
    
    skills[skillId] = {
      score: score,
      completedAt: serverTimestamp(),
      certified: true
    };
    
    await updateUserDocument(userId, { skills: skills });
  } catch (error) {
    console.error('Error updating user skills:', error);
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
    
    // Update discount code
    updateDiscountCode(user.uid);
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

function updateDiscountCode(userId) {
  const discountCodeElement = document.getElementById('discountCode');
  if (discountCodeElement) {
    discountCodeElement.textContent = `IMPACT10-${userId.substring(0, 8)}`;
  }
}

function initializeMemberServices() {
  // Load user data
  loadUserNotes();
  setupNotesAutoSave();
  
  // Load bookmarks
  updateBookmarkedCoursesList();
  
  // Load certificates
  loadUserCertificates();
}

async function loadUserData(userId) {
  try {
    const userDoc = await getUserDocument(userId);
    if (userDoc.exists()) {
      const userData = userDoc.data();
      
      // Update dashboard with user data
      updateDashboard(userData);
      
      // Display bookmarked courses
      if (userData.bookmarkedCourses && userData.bookmarkedCourses.length > 0) {
        displayBookmarkedCourses(userData.bookmarkedCourses);
      }
    }
  } catch (error) {
    console.error('Error loading user data:', error);
  }
}

function clearUserData() {
  // Clear any cached user data
  const userNotes = document.getElementById('userNotes');
  if (userNotes) userNotes.value = '';
  
  const dashboardStats = document.querySelectorAll('.dashboard-stat');
  dashboardStats.forEach(stat => stat.textContent = '0');
  
  // Clear bookmarked courses list
  const bookmarkedList = document.getElementById('bookmarkedCoursesList');
  if (bookmarkedList) {
    bookmarkedList.innerHTML = '<p style="color: var(--text-secondary); font-style: italic;">No bookmarked courses yet. Bookmark courses to see them here!</p>';
  }
}

function updateDashboard(userData) {
  // Update dashboard statistics
  const coursesAccessedEl = document.getElementById('coursesAccessed');
  const bookmarksCountEl = document.getElementById('bookmarksCount');
  const coursesStartedEl = document.getElementById('coursesStarted');
  const coursesCompletedEl = document.getElementById('coursesCompleted');
  
  if (coursesAccessedEl) coursesAccessedEl.textContent = userData.totalCoursesAccessed || 0;
  if (coursesStartedEl) coursesStartedEl.textContent = userData.totalCoursesAccessed || 0;
  if (coursesCompletedEl) coursesCompletedEl.textContent = userData.completedCourses?.length || 0;
  if (bookmarksCountEl) bookmarksCountEl.textContent = userData.bookmarkedCourses?.length || 0;
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

function updateBookmarkedCoursesList() {
  if (!currentUser) return;
  
  getUserDocument(currentUser.uid).then(userDoc => {
    if (userDoc.exists()) {
      const userData = userDoc.data();
      const bookmarks = userData.bookmarkedCourses || [];
      
      const bookmarkedList = document.getElementById('bookmarkedCoursesList');
      if (!bookmarkedList) return;
      
      if (bookmarks.length === 0) {
        bookmarkedList.innerHTML = '<p style="color: var(--text-secondary); font-style: italic;">No bookmarked courses yet. Bookmark courses to see them here!</p>';
        return;
      }
      
      bookmarkedList.innerHTML = bookmarks.map(bookmark => `
        <div class="bookmarked-course-item">
          <span class="bookmarked-course-title">${bookmark.courseTitle}</span>
          <button class="remove-bookmark" onclick="removeBookmark('${bookmark.courseId}')">
            <i class="fas fa-times"></i>
          </button>
        </div>
      `).join('');
    }
  });
}

function loadUserCertificates() {
  if (!currentUser) return;
  
  const certificatesList = document.getElementById('certificatesList');
  if (!certificatesList) return;
  
  // This would be populated from assessment results in real implementation
  certificatesList.innerHTML = '<p style="color: var(--text-secondary); font-style: italic;">Complete skill assessments to earn certificates!</p>';
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

// NEW: Member Services Global Functions
window.bookConsultation = async function(consultationType, preferredDate, preferredTime, userMessage) {
  return await bookConsultation(consultationType, preferredDate, preferredTime, userMessage);
};

window.requestCVReview = async function(userMessage, urgency) {
  return await requestCVReview(userMessage, urgency);
};

window.bookInterviewPrep = async function(interviewType, companyInfo, timeframe, specificAreas) {
  return await bookInterviewPrep(interviewType, companyInfo, timeframe, specificAreas);
};

window.startSkillAssessment = function(assessmentId) {
  if (!currentUser) {
    showNotification('Please log in to take skill assessments', 'error');
    return;
  }
  
  const assessment = skillAssessments[assessmentId];
  if (!assessment) return;
  
  // For now, show info about the assessment
  showNotification(`Starting ${assessment.name} - ${assessment.questions.length} questions, ${assessment.duration} minutes`, 'info');
  
  // This would open the assessment modal in a full implementation
  // For now, we'll just log the assessment data
  console.log('Assessment data:', assessment);
};

window.completeSkillAssessment = async function(assessmentId, answers, timeSpent) {
  return await completeSkillAssessment(assessmentId, answers, timeSpent);
};

window.copyDiscountCode = function() {
  const discountCode = document.getElementById('discountCode')?.textContent;
  if (discountCode) {
    navigator.clipboard.writeText(discountCode).then(() => {
      showNotification('Discount code copied to clipboard!', 'success');
    });
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
        max-width: 300px;
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
        min-width: 20px;
      }
      
      .notification-message {
        flex: 1;
        font-size: 0.9rem;
      }
      
      @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
      }
    `;
    document.head.appendChild(style);
  }
});

console.log('🔥 Firebase Auth configured for ImpactMojo with Member Features - Ready to use!');