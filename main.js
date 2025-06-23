// ImpactMojo 101 - Main Application Logic
// Handles UI interactions, course rendering, filtering, and utilities

// Global variables
let filteredCourses = [...courses];
let currentBookmarkFilter = false;
let comparisonList = [];
let expandedCourse = null;

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
  initializeTheme();
  renderCourses();
  setupModalHandlers();
  setupNavigationHandlers();
  setupFilterHandlers();
});

// Theme Management
function initializeTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  const themeIcon = document.getElementById('themeIcon');
  
  if (savedTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    if (themeIcon) themeIcon.className = 'fas fa-sun';
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
    if (themeIcon) themeIcon.className = 'fas fa-moon';
  }
}
// 🔧 TARGETED FIXES - Add this to the END of your main.js file

console.log('🔧 Loading targeted fixes for modal styling and lab duplicates...');

// ===== FIX 1: Beautiful Course Details Modal =====
function enhanceCourseDetailsModal() {
  // Add beautiful styling for course expansion modal
  const style = document.createElement('style');
  style.id = 'course-details-modal-fix';
  style.textContent = `
    /* Enhanced Course Details Modal */
    .course-card.expanded {
      position: fixed !important;
      top: 50% !important;
      left: 50% !important;
      transform: translate(-50%, -50%) !important;
      width: 90% !important;
      max-width: 800px !important;
      max-height: 85vh !important;
      z-index: 10000 !important;
      background: white !important;
      border-radius: 20px !important;
      box-shadow: 0 25px 80px rgba(0, 0, 0, 0.6) !important;
      overflow-y: auto !important;
      padding: 30px !important;
      border: none !important;
      animation: modalSlideIn 0.4s ease !important;
    }
    
    /* Add backdrop */
    .course-card.expanded::before {
      content: '' !important;
      position: fixed !important;
      top: 0 !important;
      left: 0 !important;
      width: 100vw !important;
      height: 100vh !important;
      background: rgba(0, 0, 0, 0.7) !important;
      z-index: -1 !important;
      backdrop-filter: blur(8px) !important;
    }
    
    /* Enhanced course content in modal */
    .course-card.expanded .course-title {
      color: #2563eb !important;
      font-size: 2rem !important;
      margin-bottom: 20px !important;
      text-align: center !important;
      border-bottom: 3px solid #2563eb !important;
      padding-bottom: 15px !important;
    }
    
    .course-card.expanded .course-description {
      font-size: 1.1rem !important;
      line-height: 1.6 !important;
      color: #374151 !important;
      margin-bottom: 25px !important;
      padding: 20px !important;
      background: #f8fafc !important;
      border-radius: 12px !important;
      border-left: 4px solid #2563eb !important;
    }
    
    .course-card.expanded .course-meta {
      display: grid !important;
      grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)) !important;
      gap: 15px !important;
      margin-bottom: 30px !important;
      padding: 20px !important;
      background: linear-gradient(135deg, #f8fafc, #e2e8f0) !important;
      border-radius: 12px !important;
    }
    
    .course-card.expanded .course-meta span {
      background: white !important;
      padding: 12px 15px !important;
      border-radius: 8px !important;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
      text-align: center !important;
      font-weight: 600 !important;
      color: #374151 !important;
    }
    
    .course-card.expanded .course-expanded-content {
      display: block !important;
      margin-top: 25px !important;
    }
    
    .course-card.expanded .course-expanded-content > div {
      margin-bottom: 25px !important;
      padding: 20px !important;
      background: white !important;
      border-radius: 12px !important;
      border: 2px solid #e5e7eb !important;
      box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
    }
    
    .course-card.expanded .course-expanded-content h5 {
      color: #2563eb !important;
      font-size: 1.3rem !important;
      margin-bottom: 15px !important;
      display: flex !important;
      align-items: center !important;
      gap: 10px !important;
    }
    
    .course-card.expanded .course-prerequisites h5::before {
      content: '📋' !important;
    }
    
    .course-card.expanded .course-outcomes h5::before {
      content: '🎯' !important;
    }
    
    .course-card.expanded .course-audience h5::before {
      content: '👥' !important;
    }
    
    .course-card.expanded .course-expanded-content ul {
      list-style: none !important;
      padding: 0 !important;
      margin: 0 !important;
    }
    
    .course-card.expanded .course-expanded-content li {
      padding: 10px 0 !important;
      border-bottom: 1px solid #f3f4f6 !important;
      position: relative !important;
      padding-left: 25px !important;
      color: #6b7280 !important;
      line-height: 1.5 !important;
    }
    
    .course-card.expanded .course-expanded-content li::before {
      content: '✓' !important;
      position: absolute !important;
      left: 0 !important;
      color: #059669 !important;
      font-weight: bold !important;
    }
    
    .course-card.expanded .course-audience p {
      color: #6b7280 !important;
      line-height: 1.6 !important;
      margin: 0 !important;
    }
    
    /* Enhanced close button */
    .close-expanded {
      position: absolute !important;
      top: 20px !important;
      right: 25px !important;
      background: rgba(239, 68, 68, 0.1) !important;
      border: 2px solid #ef4444 !important;
      color: #ef4444 !important;
      width: 45px !important;
      height: 45px !important;
      border-radius: 50% !important;
      cursor: pointer !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      font-size: 20px !important;
      font-weight: bold !important;
      transition: all 0.3s ease !important;
      z-index: 10001 !important;
    }
    
    .close-expanded:hover {
      background: #ef4444 !important;
      color: white !important;
      transform: scale(1.1) !important;
    }
    
    /* Enhanced action buttons in modal */
    .course-card.expanded .course-actions {
      margin-top: 30px !important;
      display: flex !important;
      gap: 15px !important;
      justify-content: center !important;
      flex-wrap: wrap !important;
    }
    
    .course-card.expanded .launch-btn {
      background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
      color: white !important;
      padding: 15px 30px !important;
      border-radius: 12px !important;
      text-decoration: none !important;
      font-weight: bold !important;
      font-size: 1.1rem !important;
      box-shadow: 0 6px 20px rgba(37, 99, 235, 0.3) !important;
      transition: all 0.3s ease !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 10px !important;
    }
    
    .course-card.expanded .launch-btn:hover {
      transform: translateY(-2px) !important;
      box-shadow: 0 10px 30px rgba(37, 99, 235, 0.4) !important;
    }
  `;
  
  // Remove existing style if it exists
  const existingStyle = document.getElementById('course-details-modal-fix');
  if (existingStyle) {
    existingStyle.remove();
  }
  
  document.head.appendChild(style);
  console.log('✅ Course details modal styling enhanced');
}

// ===== FIX 2: Completely Remove Lab Duplicate Buttons =====
function nuclearLabFix() {
  console.log('🧨 Nuclear lab fix - removing ALL duplicate buttons...');
  
  // Step 1: Remove ALL existing lab action buttons completely
  const allLabActions = document.querySelectorAll(`
    .emergency-lab-actions, 
    .lab-enhanced-actions, 
    .final-lab-actions,
    .lab-bookmark-btn,
    .lab-details-btn,
    .lab-compare-btn
  `);
  
  allLabActions.forEach((element, index) => {
    console.log(`🗑️ Removing lab action element ${index + 1}:`, element.className);
    element.remove();
  });
  
  // Step 2: Clear all markers
  document.querySelectorAll('[data-enhanced], [data-lab-enhanced]').forEach(element => {
    element.removeAttribute('data-enhanced');
    element.removeAttribute('data-lab-enhanced');
  });
  
  // Step 3: Wait and add ONE set of clean buttons
  setTimeout(() => {
    const labCards = document.querySelectorAll('.lab-card');
    console.log(`📦 Nuclear fix: Found ${labCards.length} lab cards`);
    
    labCards.forEach((card, index) => {
      // Triple check - skip if ANY buttons exist
      if (card.querySelector('button[class*="lab-"], .lab-bookmark-btn, .lab-details-btn, .final-lab-actions')) {
        console.log(`⏭️ Lab ${index + 1} already has buttons, skipping...`);
        return;
      }
      
      // Mark as processed
      card.setAttribute('data-lab-enhanced', 'nuclear-fixed');
      
      const labId = `lab-${index + 1}`;
      const title = card.querySelector('h3')?.textContent || `Lab ${index + 1}`;
      
      console.log(`🔧 Nuclear fix enhancing: ${title}`);
      
      // Create ONE clean container
      const actionsContainer = document.createElement('div');
      actionsContainer.className = 'nuclear-lab-actions';
      actionsContainer.style.cssText = `
        margin-top: 15px;
        padding-top: 15px;
        border-top: 2px solid #e2e8f0;
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        background: #f8fafc;
        padding: 15px;
        border-radius: 8px;
        margin: 15px -15px -15px -15px;
      `;
      
      // Bookmark button
      const bookmarkBtn = document.createElement('button');
      bookmarkBtn.innerHTML = '<i class="far fa-bookmark"></i> Bookmark';
      bookmarkBtn.className = 'nuclear-bookmark-btn';
      bookmarkBtn.style.cssText = `
        background: white;
        border: 2px solid #f59e0b;
        color: #f59e0b;
        padding: 10px 15px;
        border-radius: 8px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 600;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      `;
      
      bookmarkBtn.onclick = function() {
        const icon = this.querySelector('i');
        if (icon.classList.contains('far')) {
          icon.className = 'fas fa-bookmark';
          this.style.background = '#f59e0b';
          this.style.color = 'white';
          this.style.borderColor = '#f59e0b';
          showNotification('Lab bookmarked! 🎯', 'success');
        } else {
          icon.className = 'far fa-bookmark';
          this.style.background = 'white';
          this.style.color = '#f59e0b';
          this.style.borderColor = '#f59e0b';
          showNotification('Bookmark removed', 'info');
        }
      };
      
      // Details button
      const detailsBtn = document.createElement('button');
      detailsBtn.innerHTML = '<i class="fas fa-info-circle"></i> Details';
      detailsBtn.className = 'nuclear-details-btn';
      detailsBtn.style.cssText = `
        background: white;
        border: 2px solid #2563eb;
        color: #2563eb;
        padding: 10px 15px;
        border-radius: 8px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 600;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      `;
      
      detailsBtn.onclick = function() {
        this.style.background = '#2563eb';
        this.style.color = 'white';
        
        const description = card.querySelector('p')?.textContent || 'Interactive development tool';
        const launchUrl = card.querySelector('a[href]')?.href || '#';
        
        // Create beautiful details modal
        createLabDetailsModal(title, description, launchUrl);
        
        // Reset button
        setTimeout(() => {
          this.style.background = 'white';
          this.style.color = '#2563eb';
        }, 200);
      };
      
      // Add hover effects
      bookmarkBtn.onmouseover = () => {
        if (!bookmarkBtn.style.background.includes('#f59e0b')) {
          bookmarkBtn.style.background = '#fef3c7';
          bookmarkBtn.style.transform = 'translateY(-1px)';
        }
      };
      bookmarkBtn.onmouseout = () => {
        if (!bookmarkBtn.style.background.includes('#f59e0b')) {
          bookmarkBtn.style.background = 'white';
          bookmarkBtn.style.transform = 'translateY(0)';
        }
      };
      
      detailsBtn.onmouseover = () => {
        if (!detailsBtn.style.background.includes('#2563eb')) {
          detailsBtn.style.background = '#dbeafe';
          detailsBtn.style.transform = 'translateY(-1px)';
        }
      };
      detailsBtn.onmouseout = () => {
        if (!detailsBtn.style.background.includes('#2563eb')) {
          detailsBtn.style.background = 'white';
          detailsBtn.style.transform = 'translateY(0)';
        }
      };
      
      actionsContainer.appendChild(bookmarkBtn);
      actionsContainer.appendChild(detailsBtn);
      card.appendChild(actionsContainer);
      
      console.log(`✅ Nuclear fix completed for: ${title}`);
    });
    
    console.log('🎯 Nuclear lab fix complete - no more duplicates!');
  }, 500);
}

// ===== Beautiful Lab Details Modal =====
function createLabDetailsModal(title, description, url) {
  // Remove existing modal
  const existingModal = document.getElementById('labDetailsModal');
  if (existingModal) existingModal.remove();
  
  const modal = document.createElement('div');
  modal.id = 'labDetailsModal';
  modal.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000;
    backdrop-filter: blur(8px);
    animation: modalFadeIn 0.3s ease;
  `;
  
  const modalContent = document.createElement('div');
  modalContent.style.cssText = `
    background: white;
    border-radius: 20px;
    padding: 40px;
    width: 90%;
    max-width: 600px;
    box-shadow: 0 25px 80px rgba(0, 0, 0, 0.6);
    position: relative;
    animation: modalSlideIn 0.4s ease;
  `;
  
  modalContent.innerHTML = `
    <div style="text-align: center; margin-bottom: 30px;">
      <h2 style="color: #2563eb; margin: 0 0 10px 0; font-size: 2rem; font-weight: bold;">
        📋 ${title}
      </h2>
      <div style="width: 60px; height: 4px; background: linear-gradient(90deg, #2563eb, #3b82f6); margin: 0 auto; border-radius: 2px;"></div>
    </div>
    
    <div style="margin-bottom: 25px; padding: 20px; background: #f8fafc; border-radius: 12px; border-left: 4px solid #2563eb;">
      <h3 style="color: #374151; margin: 0 0 15px 0; font-size: 1.2rem;">📝 Description</h3>
      <p style="margin: 0; color: #6b7280; line-height: 1.6; font-size: 1.1rem;">${description}</p>
    </div>
    
    <div style="margin-bottom: 25px; padding: 20px; background: #f0fdf4; border-radius: 12px; border-left: 4px solid #059669;">
      <h3 style="color: #374151; margin: 0 0 15px 0; font-size: 1.2rem;">✨ Features</h3>
      <ul style="margin: 0; padding: 0 0 0 20px; color: #6b7280; line-height: 1.8;">
        <li>🎯 Interactive tools and simulations</li>
        <li>📊 Real-world case studies and examples</li>
        <li>📥 Downloadable resources and templates</li>
        <li>📖 Step-by-step guidance and tutorials</li>
        <li>🎨 Professional interface design</li>
      </ul>
    </div>
    
    <div style="text-align: center; margin-top: 30px;">
      <a href="${url}" target="_blank" rel="noopener" style="background: linear-gradient(135deg, #2563eb, #1d4ed8); color: white; padding: 15px 30px; border-radius: 12px; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; font-weight: bold; font-size: 1.1rem; box-shadow: 0 6px 20px rgba(37, 99, 235, 0.3); transition: all 0.3s ease; margin-right: 15px;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
        <i class="fas fa-external-link-alt"></i> Launch Lab
      </a>
      <button onclick="document.getElementById('labDetailsModal').remove()" style="background: #f3f4f6; color: #6b7280; padding: 15px 30px; border: none; border-radius: 12px; cursor: pointer; font-weight: bold; font-size: 1.1rem; transition: all 0.3s ease;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='#f3f4f6'">
        Close
      </button>
    </div>
  `;
  
  // Close button
  const closeBtn = document.createElement('button');
  closeBtn.innerHTML = '×';
  closeBtn.style.cssText = `
    position: absolute;
    top: 15px;
    right: 20px;
    background: none;
    border: none;
    font-size: 30px;
    cursor: pointer;
    color: #9ca3af;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: all 0.3s ease;
  `;
  closeBtn.onclick = () => modal.remove();
  closeBtn.onmouseover = () => {
    closeBtn.style.background = '#ef4444';
    closeBtn.style.color = 'white';
  };
  closeBtn.onmouseout = () => {
    closeBtn.style.background = 'none';
    closeBtn.style.color = '#9ca3af';
  };
  
  modalContent.appendChild(closeBtn);
  modal.appendChild(modalContent);
  
  // Close on backdrop click
  modal.onclick = (e) => {
    if (e.target === modal) modal.remove();
  };
  
  document.body.appendChild(modal);
}

// ===== AUTO-INITIALIZE FIXES =====
function initializeFixes() {
  console.log('🔧 Initializing targeted fixes...');
  
  // Fix 1: Enhanced course modal styling
  enhanceCourseDetailsModal();
  
  // Fix 2: Nuclear lab duplicate removal
  setTimeout(nuclearLabFix, 1000);
  
  // Re-apply fixes when content changes
  const observer = new MutationObserver(() => {
    setTimeout(nuclearLabFix, 500);
  });
  
  const labsContainer = document.getElementById('labsContainer');
  if (labsContainer) {
    observer.observe(labsContainer, { childList: true, subtree: true });
  }
  
  console.log('✅ Targeted fixes initialized');
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', initializeFixes);

// Also initialize if DOM already loaded
if (document.readyState !== 'loading') {
  initializeFixes();
}

// Manual fix functions for testing
window.fixCourseModal = enhanceCourseDetailsModal;
window.fixLabDuplicates = nuclearLabFix;

console.log('🎯 TARGETED FIXES LOADED!');
console.log('🔧 Course modal: Enhanced with beautiful styling');
console.log('🧨 Lab duplicates: Nuclear removal system active');
console.log('🧪 Manual fix: run fixLabDuplicates() in console if needed');

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const themeIcon = document.getElementById('themeIcon');
  
  if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    if (themeIcon) themeIcon.className = 'fas fa-moon';
  } else {
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
    if (themeIcon) themeIcon.className = 'fas fa-sun';
  }
}

// Course Rendering and Management
function renderCourses() {
  const container = document.getElementById('courseContainer');
  const noResults = document.getElementById('noResults');
  
  if (!container) return;
  
  let coursesToShow = filteredCourses;
  
  // Apply bookmark filter if active
  if (currentBookmarkFilter && typeof userBookmarks !== 'undefined') {
    coursesToShow = filteredCourses.filter(course => userBookmarks.includes(course.id));
  }
  
  if (coursesToShow.length === 0) {
    container.innerHTML = '';
    if (noResults) noResults.classList.remove('hidden');
    return;
  }
  
  if (noResults) noResults.classList.add('hidden');
  
  container.innerHTML = coursesToShow.map(course => `
    <div class="course-card" data-category="${course.category}" data-difficulty="${course.difficulty}" data-duration="${course.duration}" data-course-id="${course.id}">
      <div class="course-header">
        <span class="course-number">${course.number}</span>
        <button class="bookmark-btn" data-course-id="${course.id}" onclick="toggleBookmark('${course.id}')" title="Bookmark this course">
          <i class="far fa-bookmark"></i>
        </button>
      </div>
      
      <h3 class="course-title">${course.title}</h3>
      <p class="course-description">${course.description}</p>
      
      <div class="course-meta">
        <span><i class="fas fa-tag"></i> ${course.category}</span>
        <span><i class="fas fa-clock"></i> ${course.duration}</span>
        <span class="difficulty ${course.difficulty}">${capitalizeFirst(course.difficulty)}</span>
        <span><i class="fas fa-users"></i> ${course.learnerCount.toLocaleString()}</span>
        <span><i class="fas fa-star"></i> ${course.rating}</span>
      </div>
      
      <div class="course-actions course-actions-enhanced">
        <div class="course-actions-left">
          <a href="${course.url}" target="_blank" rel="noopener" class="launch-btn" onclick="trackCourseClick('${course.id}')">
            Launch Course <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
        <div class="course-actions-right">
          <button class="expand-btn" onclick="expandCourse('${course.id}')" title="View details">
            <i class="fas fa-expand"></i> Details
          </button>
          <button class="course-compare-btn compare-btn ${comparisonList.includes(course.id) ? 'active' : ''}" onclick="toggleCourseComparison('${course.id}')" title="Add to comparison">
            <i class="fas fa-balance-scale"></i> Compare
          </button>
        </div>
      </div>      
      <div class="course-expanded-content">
        <div class="course-prerequisites">
          <h5>Prerequisites</h5>
          <ul>
            ${course.prerequisites.map(prereq => `<li>${prereq}</li>`).join('')}
          </ul>
        </div>
        
        <div class="course-outcomes">
          <h5>Learning Outcomes</h5>
          <ul>
            ${course.outcomes.map(outcome => `<li>${outcome}</li>`).join('')}
          </ul>
        </div>
        
        <div class="course-audience">
          <h5>Target Audience</h5>
          <p>${course.audience}</p>
        </div>
      </div>
    </div>
  `).join('');
  
  // Update bookmark UI if user is logged in
  if (typeof updateBookmarkUI === 'function') {
    updateBookmarkUI();
  }
  
  updateCourseCount();
}

// Course Filtering
function filterCourses() {
  const searchTerm = document.getElementById('searchInput')?.value.toLowerCase() || '';
  const category = document.getElementById('categoryFilter')?.value || 'all';
  const difficulty = document.getElementById('difficultyFilter')?.value || 'all';
  const duration = document.getElementById('durationFilter')?.value || 'all';
  
  filteredCourses = courses.filter(course => {
    const matchesSearch = !searchTerm || 
      course.title.toLowerCase().includes(searchTerm) ||
      course.description.toLowerCase().includes(searchTerm) ||
      course.category.toLowerCase().includes(searchTerm) ||
      course.audience.toLowerCase().includes(searchTerm);
    
    const matchesCategory = category === 'all' || course.category === category;
    const matchesDifficulty = difficulty === 'all' || course.difficulty === difficulty;
    
    let matchesDuration = true;
    if (duration !== 'all') {
      const durationText = course.duration.toLowerCase();
      switch (duration) {
        case 'short':
          matchesDuration = durationText.includes('2') || durationText.includes('1');
          break;
        case 'medium':
          matchesDuration = durationText.includes('3') || durationText.includes('4');
          break;
        case 'long':
          matchesDuration = durationText.includes('5') || durationText.includes('6') || durationText.includes('+');
          break;
      }
    }
    
    return matchesSearch && matchesCategory && matchesDifficulty && matchesDuration;
  });
  
  renderCourses();
}

function clearAllFilters() {
  const searchInput = document.getElementById('searchInput');
  const categoryFilter = document.getElementById('categoryFilter');
  const difficultyFilter = document.getElementById('difficultyFilter');
  const durationFilter = document.getElementById('durationFilter');
  
  if (searchInput) searchInput.value = '';
  if (categoryFilter) categoryFilter.value = 'all';
  if (difficultyFilter) difficultyFilter.value = 'all';
  if (durationFilter) durationFilter.value = 'all';
  
  currentBookmarkFilter = false;
  filteredCourses = [...courses];
  renderCourses();
  
  showNotification('All filters cleared', 'info');
}

function filterByPath(pathType) {
  const pathMappings = {
    'data-analysis': ['Data Analysis'],
    'gender-studies': ['Gender Studies'],
    'economics': ['Economics'],
    'justice': ['Justice']
  };
  
  const categories = pathMappings[pathType] || [];
  
  if (categories.length > 0) {
    filteredCourses = courses.filter(course => categories.includes(course.category));
    
    // Update filter UI
    const categoryFilter = document.getElementById('categoryFilter');
    if (categoryFilter && categories.length === 1) {
      categoryFilter.value = categories[0];
    }
    
    renderCourses();
    
    // Scroll to courses section
    const coursesSection = document.getElementById('courses');
    if (coursesSection) {
      coursesSection.scrollIntoView({ behavior: 'smooth' });
    }
    
    showNotification(`Showing ${categories.join(', ')} courses`, 'info');
  }
}

function setBookmarkFilter(active) {
  currentBookmarkFilter = active;
  renderCourses();
}

function updateCourseCount() {
  const visibleCount = document.getElementById('visibleCount');
  const totalCount = document.getElementById('totalCount');
  
  let displayCount = filteredCourses.length;
  
  // Adjust count for bookmark filter
  if (currentBookmarkFilter && typeof userBookmarks !== 'undefined') {
    displayCount = filteredCourses.filter(course => userBookmarks.includes(course.id)).length;
  }
  
  if (visibleCount) visibleCount.textContent = displayCount;
  if (totalCount) totalCount.textContent = courses.length;
}

// Course Interaction Tracking
function trackCourseClick(courseId) {
  // Track course access for analytics
  console.log(`Course accessed: ${courseId}`);
  
  // Update user progress if logged in
  if (typeof updateUserProgress === 'function' && typeof isAuthenticated === 'function' && isAuthenticated()) {
    updateUserProgress(courseId, { lastAccessed: new Date() });
  }
}

// Event Handlers Setup
function setupModalHandlers() {
  // Close modals when clicking outside
  window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    });
  };
  
  // Handle escape key to close modals
  document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
      const modals = document.querySelectorAll('.modal');
      modals.forEach(modal => {
        if (modal.style.display === 'block') {
          modal.style.display = 'none';
        }
      });
    }
  });
}

function setupNavigationHandlers() {
  // Smooth scrolling for navigation links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
  
  // Handle mobile menu toggle (if needed)
  const mobileMenuToggle = document.getElementById('mobileMenuToggle');
  const navLinks = document.querySelector('.nav-links');
  
  if (mobileMenuToggle && navLinks) {
    mobileMenuToggle.addEventListener('click', function() {
      navLinks.classList.toggle('active');
    });
  }
}

function setupFilterHandlers() {
  // Real-time search
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    let searchTimeout;
    searchInput.addEventListener('input', function() {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(filterCourses, 300); // Debounce search
    });
  }
  
  // Filter change handlers
  const filterSelects = ['categoryFilter', 'difficultyFilter', 'durationFilter'];
  filterSelects.forEach(filterId => {
    const filterElement = document.getElementById(filterId);
    if (filterElement) {
      filterElement.addEventListener('change', filterCourses);
    }
  });
}

// Utility Functions
function showNotification(message, type = 'info') {
  // Remove existing notifications
  const existingNotifications = document.querySelectorAll('.notification');
  existingNotifications.forEach(notification => notification.remove());
  
  // Create new notification
  const notification = document.createElement('div');
  notification.className = `notification ${type}`;
  notification.textContent = message;
  
  document.body.appendChild(notification);
  
  // Auto-remove after 4 seconds
  setTimeout(() => {
    if (notification.parentNode) {
      notification.remove();
    }
  }, 4000);
  
  // Add click to dismiss
  notification.addEventListener('click', () => {
    notification.remove();
  });
}

function capitalizeFirst(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function formatNumber(num) {
  return num.toLocaleString();
}

function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Search Functionality Enhancement
function performAdvancedSearch(query) {
  const searchTerms = query.toLowerCase().split(' ').filter(term => term.length > 0);
  
  return courses.filter(course => {
    const searchableText = [
      course.title,
      course.description,
      course.category,
      course.audience,
      ...course.prerequisites,
      ...course.outcomes
    ].join(' ').toLowerCase();
    
    return searchTerms.every(term => searchableText.includes(term));
  });
}

// Course Statistics
function getCourseStatistics() {
  const stats = {
    totalCourses: courses.length,
    categories: {},
    difficulties: {},
    averageRating: 0,
    totalLearners: 0
  };
  
  courses.forEach(course => {
    // Category count
    stats.categories[course.category] = (stats.categories[course.category] || 0) + 1;
    
    // Difficulty count
    stats.difficulties[course.difficulty] = (stats.difficulties[course.difficulty] || 0) + 1;
    
    // Total learners
    stats.totalLearners += course.learnerCount;
  });
  
  // Average rating
  stats.averageRating = courses.reduce((sum, course) => sum + course.rating, 0) / courses.length;
  
  return stats;
}

// Export functions for use in other modules
window.ImpactMojoApp = {
  renderCourses,
  filterCourses,
  clearAllFilters,
  filterByPath,
  setBookmarkFilter,
  showNotification,
  getCourseStatistics,
  performAdvancedSearch
};

// Initialize course count on page load
document.addEventListener('DOMContentLoaded', function() {
  updateCourseCount();
});

// Handle window resize for responsive behavior
window.addEventListener('resize', debounce(() => {
  // Handle any responsive adjustments here
  console.log('Window resized');
}, 250));

// Print functionality
function printCourseList() {
  const printWindow = window.open('', '_blank');
  const courseHTML = filteredCourses.map(course => `
    <div style="margin-bottom: 20px; padding: 15px; border: 1px solid #ddd;">
      <h3>${course.title}</h3>
      <p><strong>Category:</strong> ${course.category}</p>
      <p><strong>Duration:</strong> ${course.duration}</p>
      <p><strong>Difficulty:</strong> ${capitalizeFirst(course.difficulty)}</p>
      <p>${course.description}</p>
      <p><strong>URL:</strong> ${course.url}</p>
    </div>
  `).join('');
  
  printWindow.document.write(`
    <html>
      <head>
        <title>ImpactMojo 101 Course List</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 20px; }
          h1 { color: #2563eb; }
          h3 { color: #333; margin-bottom: 10px; }
          p { margin: 5px 0; }
        </style>
      </head>
      <body>
        <h1>ImpactMojo 101 Knowledge Series</h1>
        <p>Generated on: ${new Date().toLocaleDateString()}</p>
        <p>Total Courses: ${filteredCourses.length}</p>
        <hr>
        ${courseHTML}
      </body>
    </html>
  `);
  printWindow.document.close();
  printWindow.print();
}

// Keyboard shortcuts
document.addEventListener('keydown', function(event) {
  // Ctrl/Cmd + K to focus search
  if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
    event.preventDefault();
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
      searchInput.focus();
    }
  }
  
  // Ctrl/Cmd + Shift + C to clear filters
  if ((event.ctrlKey || event.metaKey) && event.shiftKey && event.key === 'C') {
    event.preventDefault();
    clearAllFilters();
  }
});

// Performance monitoring
console.log(`ImpactMojo 101 loaded with ${courses.length} courses`);
console.log('Available categories:', [...new Set(courses.map(c => c.category))]);
console.log('Course statistics:', getCourseStatistics());

// Course Expansion Functionality
function expandCourse(courseId) {
  const course = courses.find(c => c.id === courseId);
  if (!course) return;
  
  // Close any existing expanded course
  if (expandedCourse) {
    closeExpandedCourse();
  }
  
  const courseCard = document.querySelector(`[data-course-id="${courseId}"]`).closest('.course-card');
  if (courseCard) {
    courseCard.classList.add('expanded');
    expandedCourse = courseId;
    
    // Add close button if not exists
    if (!courseCard.querySelector('.close-expanded')) {
      const closeBtn = document.createElement('button');
      closeBtn.className = 'close-expanded';
      closeBtn.innerHTML = '<i class="fas fa-times"></i>';
      closeBtn.onclick = closeExpandedCourse;
      closeBtn.title = 'Close details';
      courseCard.appendChild(closeBtn);
    }
    
    // Prevent body scroll
    document.body.style.overflow = 'hidden';
  }
}

function closeExpandedCourse() {
  if (expandedCourse) {
    const courseCard = document.querySelector(`[data-course-id="${expandedCourse}"]`).closest('.course-card');
    if (courseCard) {
      courseCard.classList.remove('expanded');
      const closeBtn = courseCard.querySelector('.close-expanded');
      if (closeBtn) {
        closeBtn.remove();
      }
    }
    expandedCourse = null;
    document.body.style.overflow = '';
  }
}

// Close expanded course when clicking outside
document.addEventListener('click', function(event) {
  if (expandedCourse && event.target.closest('.course-card.expanded') === null && !event.target.closest('.close-expanded')) {
    closeExpandedCourse();
  }
});

// Handle escape key
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    if (expandedCourse) {
      closeExpandedCourse();
    }
  }
});

/* ===== ENHANCED LABS AND COMPARISON FUNCTIONALITY ===== */

// Enhanced Labs and Comparison Functionality
let selectedCourses = [];

// Generate Labs Content - preserving your original 9 labs
function generateLabsContent() {
  const labsContainer = document.getElementById('labsContainer');
  if (!labsContainer) return;
  
  const labsHTML = `
    <div class="labs-grid">
      <!-- TOC Workbench -->
      <div class="lab-card">
        <h3><i class="fas fa-tools"></i> TOC Workbench</h3>
        <p>Create, visualize, and share your intervention logic models.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://toc-workbench.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- MEL Toolkit -->
      <div class="lab-card">
        <h3><i class="fas fa-chart-line"></i> MEL Toolkit</h3>
        <p>Monitoring, evaluation, and learning framework builder.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://mel-toolkit.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Budget Calculator -->
      <div class="lab-card">
        <h3><i class="fas fa-calculator"></i> Development Budget Calculator</h3>
        <p>Project budget planning and cost estimation tool.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://budget-calculator.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Stakeholder Mapping -->
      <div class="lab-card">
        <h3><i class="fas fa-users"></i> Stakeholder Mapping Tool</h3>
        <p>Visualize and analyze stakeholder relationships and influence.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://stakeholder-mapper.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Community Engagement Lab -->
      <div class="lab-card">
        <h3><i class="fas fa-hands-helping"></i> Community Engagement Lab</h3>
        <p>Design participatory processes and community consultation frameworks.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://community-engagement-lab.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Survey Design Lab -->
      <div class="lab-card">
        <h3><i class="fas fa-clipboard-list"></i> Survey Design Lab</h3>
        <p>Interactive tool for designing surveys and questionnaires for development research.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://survey-design-lab.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Data Visualization Lab -->
      <div class="lab-card">
        <h3><i class="fas fa-chart-bar"></i> Data Visualization Lab</h3>
        <p>Create compelling data visualizations and infographics for development data.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://data-viz-lab.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Impact Measurement -->
      <div class="lab-card">
        <h3><i class="fas fa-bullseye"></i> Impact Measurement Lab</h3>
        <p>Design and track impact metrics for development interventions.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://impact-measurement-lab.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
      
      <!-- Policy Analysis Tool -->
      <div class="lab-card">
        <h3><i class="fas fa-gavel"></i> Policy Analysis Tool</h3>
        <p>Framework for analyzing and comparing development policies.</p>
        <div class="lab-status">
          <span class="lab-badge live">Live</span>
          <a href="https://policy-analysis-tool.netlify.app/" target="_blank" rel="noopener" class="lab-launch-btn">
            Launch Lab <i class="fas fa-external-link-alt"></i>
          </a>
        </div>
      </div>
    </div>
  `;
  labsContainer.innerHTML = labsHTML;
}

// Initialize arrays if they don't exist
if (typeof selectedCourses === 'undefined') {
  window.selectedCourses = [];
  console.log('✅ Created selectedCourses array');
}

if (typeof comparisonList === 'undefined') {
  window.comparisonList = [];
  console.log('✅ Created comparisonList array');
}

// Unified Course Comparison Function
window.toggleCourseComparison = function(courseId) {
  console.log('🎯 UNIFIED toggleCourseComparison called:', courseId);
  
  const index = selectedCourses.indexOf(courseId);
  if (index > -1) {
    selectedCourses.splice(index, 1);
    console.log('➖ Removed:', courseId);
  } else {
    if (selectedCourses.length >= 4) {
      alert('Maximum 4 courses can be compared at once');
      return;
    }
    selectedCourses.push(courseId);
    console.log('➕ Added:', courseId);
  }
  
  console.log('📋 Final selectedCourses:', selectedCourses);
  
  // Update everything
  unifiedUpdateComparisonUI();
  unifiedUpdateFAB();
  
  showNotification(index > -1 ? 'Removed from comparison' : 'Added to comparison', 'info');
};

// Unified comparison UI update
window.unifiedUpdateComparisonUI = function() {
  console.log('🔄 Unified UI update...');
  
  // Update ALL compare buttons on course cards
  const allCompareBtns = document.querySelectorAll('.course-compare-btn, .compare-btn');
  console.log(`🔍 Found ${allCompareBtns.length} compare buttons to update`);
  
  allCompareBtns.forEach(btn => {
    const courseCard = btn.closest('[data-course-id]');
    if (!courseCard) return;
    
    const courseId = courseCard.getAttribute('data-course-id');
    const isSelected = selectedCourses.includes(courseId);
    
    // Update button appearance
    if (isSelected) {
      btn.classList.add('selected', 'active');
      btn.innerHTML = '<i class="fas fa-check"></i> Selected';
      btn.style.background = '#059669';
      btn.style.color = 'white';
      btn.style.borderColor = '#059669';
    } else {
      btn.classList.remove('selected', 'active');
      btn.innerHTML = '<i class="fas fa-balance-scale"></i> Compare';
      btn.style.background = '';
      btn.style.color = '';
      btn.style.borderColor = '';
    }
  });
  
  console.log('✅ Comparison UI updated');
};

// Unified FAB button management
window.unifiedUpdateFAB = function() {
  console.log('🔘 Unified FAB update, count:', selectedCourses.length);
  
  // Remove ALL existing floating buttons to prevent duplicates
  const existingFABs = document.querySelectorAll('.unified-fab-btn, .emergency-fab-btn, .fab-btn.compare, .compare-fab, [class*="fab"]');
  existingFABs.forEach(fab => {
    if (fab.textContent.includes('Compare')) {
      console.log('🗑️ Removing duplicate FAB:', fab.className);
      fab.remove();
    }
  });
  
  if (selectedCourses.length === 0) {
    console.log('❌ No courses selected');
    return;
  }
  
  // Create ONE clean floating button
  const unifiedFAB = document.createElement('button');
  unifiedFAB.className = 'unified-fab-btn';
  unifiedFAB.innerHTML = `<i class="fas fa-balance-scale"></i> Compare (${selectedCourses.length})`;
  
  // Clean styling
  unifiedFAB.style.cssText = `
  position: fixed !important;
  bottom: 20px !important;
  right: 20px !important;
  background: #f59e0b !important;
  color: white !important;
  border: none !important;
  padding: 15px 25px !important;
  border-radius: 30px !important;
  cursor: pointer !important;
  font-weight: bold !important;
  font-size: 16px !important;
  box-shadow: 0 6px 20px rgba(245, 158, 11, 0.4) !important;
  z-index: 9999 !important;
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  transition: all 0.3s ease !important;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
  `;
  
  // Click handler
  unifiedFAB.onclick = function(e) {
    e.preventDefault();
    e.stopPropagation();
    console.log('🖱️ UNIFIED FAB CLICKED!');
    unifiedShowComparison();
  };
  
  // Hover effects
  unifiedFAB.onmouseover = () => {
    unifiedFAB.style.transform = 'scale(1.05)';
    unifiedFAB.style.background = '#d97706';
  };
  unifiedFAB.onmouseout = () => {
    unifiedFAB.style.transform = 'scale(1)';
    unifiedFAB.style.background = '#f59e0b';
  };
  
  document.body.appendChild(unifiedFAB);
  console.log('✅ Unified FAB created');
};

// 🔥 RICH UNIFIED COMPARISON MODAL - This is the enhanced version!
window.unifiedShowComparison = function() {
  console.log('🚨 RICH Unified Comparison Modal Starting');
  
  if (selectedCourses.length < 2) {
    alert('Please select at least 2 courses to compare.');
    return;
  }
  
  const coursesToCompare = selectedCourses.map(id => 
    courses.find(c => c.id === id)
  ).filter(Boolean);
  
  if (coursesToCompare.length === 0) {
    alert('Course data not found. Please refresh the page.');
    return;
  }
  
  console.log('📊 Creating RICH comparison for:', coursesToCompare.map(c => c.title));
  
  // Calculate rich analysis data
  const contentDepths = coursesToCompare.map(course => {
    let score = 0;
    
    // Duration scoring (out of 3)
    if (course.duration && (course.duration.includes('5-6') || course.duration.includes('6+'))) score += 3;
    else if (course.duration && course.duration.includes('4-5')) score += 2;
    else score += 1;
    
    // Prerequisites scoring (out of 2) 
    if (course.prerequisites && course.prerequisites.length > 2) score += 2;
    else if (course.prerequisites && course.prerequisites.length > 0 && !course.prerequisites.includes('None - foundational course')) score += 1;
    
    // Learning outcomes complexity (out of 3)
    if (course.outcomes && course.outcomes.length >= 4) score += 3;
    else if (course.outcomes && course.outcomes.length >= 3) score += 2;
    else score += 1;
    
    // Difficulty scoring (out of 2)
    if (course.difficulty === 'advanced') score += 2;
    else if (course.difficulty === 'intermediate') score += 1;
    
    return Math.min(score, 10);
  });
  
  // Analyze content overlaps
  const overlaps = [];
  for (let i = 0; i < coursesToCompare.length; i++) {
    for (let j = i + 1; j < coursesToCompare.length; j++) {
      const course1 = coursesToCompare[i];
      const course2 = coursesToCompare[j];
      
      const categoryMatch = course1.category === course2.category;
      const audienceWords1 = (course1.audience || '').toLowerCase().split(/[,\s]+/);
      const audienceWords2 = (course2.audience || '').toLowerCase().split(/[,\s]+/);
      const audienceOverlap = audienceWords1.filter(word => 
        audienceWords2.includes(word) && word.length > 3
      ).length;
      
      let overlapScore = 0;
      if (categoryMatch) overlapScore += 3;
      overlapScore += Math.min(audienceOverlap, 2);
      
      if (overlapScore > 2) {
        overlaps.push({
          courses: [course1.title, course2.title],
          score: overlapScore,
          details: {
            category: categoryMatch,
            audienceWords: audienceOverlap
          }
        });
      }
    }
  }
  
  // Generate learning path
  const suggestedPath = [...coursesToCompare].sort((a, b) => {
    const difficultyOrder = { 'beginner': 1, 'intermediate': 2, 'advanced': 3 };
    const aDiff = difficultyOrder[a.difficulty] || 2;
    const bDiff = difficultyOrder[b.difficulty] || 2;
    
    if (aDiff !== bDiff) return aDiff - bDiff;
    
    const aFoundational = (a.prerequisites || []).includes('None - foundational course');
    const bFoundational = (b.prerequisites || []).includes('None - foundational course');
    
    if (aFoundational && !bFoundational) return -1;
    if (!aFoundational && bFoundational) return 1;
    
    return 0;
  });
  
  // Create the RICH comparison HTML
  const richComparisonHTML = `
    <div style="padding: 25px; max-height: 85vh; overflow-y: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
      
      <!-- Header -->
      <div style="text-align: center; margin-bottom: 35px; background: linear-gradient(135deg, #2563eb, #3b82f6); color: white; padding: 25px; border-radius: 15px; box-shadow: 0 8px 25px rgba(37, 99, 235, 0.3);">
        <h1 style="margin: 0; font-size: 2.2rem; font-weight: bold; display: flex; align-items: center; justify-content: center; gap: 15px;">
          <i class="fas fa-balance-scale"></i> Advanced Course Comparison
        </h1>
        <p style="margin: 10px 0 0 0; font-size: 1.1rem; opacity: 0.9;">Comprehensive analysis of ${coursesToCompare.length} selected courses</p>
      </div>
  
      <!-- Course Overview Table -->
      <div style="margin-bottom: 35px;">
        <h2 style="color: #2563eb; margin-bottom: 20px; font-size: 1.8rem; display: flex; align-items: center; gap: 12px; font-weight: bold;">
          <i class="fas fa-info-circle"></i> Course Overview
        </h2>
        
        <div style="overflow-x: auto; border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.1);">
          <table style="width: 100%; border-collapse: collapse; background: white; border-radius: 12px; overflow: hidden;">
            <thead>
              <tr style="background: linear-gradient(135deg, #f8fafc, #e2e8f0);">
                <th style="padding: 18px; font-weight: bold; color: #374151; text-align: left; border-bottom: 2px solid #e5e7eb;">Feature</th>
                ${coursesToCompare.map((course, index) => `
                  <th style="padding: 18px; font-weight: bold; color: ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}; min-width: 220px; text-align: left; border-bottom: 2px solid #e5e7eb;">${course.title}</th>
                `).join('')}
              </tr>
            </thead>
            <tbody>
              <tr style="background: #fafbfc;">
                <td style="padding: 15px 18px; font-weight: 600; color: #374151; border-bottom: 1px solid #e5e7eb;">Category</td>
                ${coursesToCompare.map(course => `
                  <td style="padding: 15px 18px; border-bottom: 1px solid #e5e7eb; color: #6b7280;">${course.category}</td>
                `).join('')}
              </tr>
              
              <tr style="background: white;">
                <td style="padding: 15px 18px; font-weight: 600; color: #374151; border-bottom: 1px solid #e5e7eb;">Difficulty</td>
                ${coursesToCompare.map(course => `
                  <td style="padding: 15px 18px; border-bottom: 1px solid #e5e7eb;">
                    <span style="padding: 6px 14px; border-radius: 15px; font-size: 0.85rem; font-weight: bold; color: white; background: ${
                      course.difficulty === 'beginner' ? '#059669' : 
                      course.difficulty === 'intermediate' ? '#d97706' : '#dc2626'
                    }; text-transform: uppercase; letter-spacing: 0.5px;">${course.difficulty}</span>
                  </td>
                `).join('')}
              </tr>
              
              <tr style="background: #fafbfc;">
                <td style="padding: 15px 18px; font-weight: 600; color: #374151; border-bottom: 1px solid #e5e7eb;">Duration</td>
                ${coursesToCompare.map(course => `
                  <td style="padding: 15px 18px; border-bottom: 1px solid #e5e7eb; color: #6b7280;">${course.duration}</td>
                `).join('')}
              </tr>
              
              <tr style="background: white;">
                <td style="padding: 15px 18px; font-weight: 600; color: #374151; border-bottom: 1px solid #e5e7eb;">Content Depth</td>
                ${coursesToCompare.map((course, index) => `
                  <td style="padding: 15px 18px; border-bottom: 1px solid #e5e7eb;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                      <div style="flex: 1; height: 10px; background: #e5e7eb; border-radius: 6px; overflow: hidden;">
                        <div style="width: ${contentDepths[index] * 10}%; height: 100%; background: linear-gradient(90deg, #10b981 0%, #f59e0b 50%, #3b82f6 100%); border-radius: 6px; transition: width 0.8s ease;"></div>
                      </div>
                      <span style="font-weight: bold; color: #2563eb; font-size: 1rem;">${contentDepths[index]}/10</span>
                    </div>
                  </td>
                `).join('')}
              </tr>
              
              <tr style="background: #fafbfc;">
                <td style="padding: 15px 18px; font-weight: 600; color: #374151; border-bottom: 1px solid #e5e7eb;">Rating</td>
                ${coursesToCompare.map(course => `
                  <td style="padding: 15px 18px; border-bottom: 1px solid #e5e7eb;">
                    <span style="color: #f59e0b; font-weight: bold; font-size: 1.1rem;">⭐ ${course.rating}/5</span>
                  </td>
                `).join('')}
              </tr>
              
              <tr style="background: white;">
                <td style="padding: 15px 18px; font-weight: 600; color: #374151;">Learners</td>
                ${coursesToCompare.map(course => `
                  <td style="padding: 15px 18px; color: #6b7280; font-weight: 500;">${course.learnerCount ? course.learnerCount.toLocaleString() : 'N/A'}</td>
                `).join('')}
              </tr>
            </tbody>
          </table>
        </div>
      </div>
  
      <!-- Learning Outcomes Section -->
      ${coursesToCompare.some(c => c.outcomes && c.outcomes.length > 0) ? `
        <div style="margin-bottom: 35px;">
          <h2 style="color: #2563eb; margin-bottom: 20px; font-size: 1.8rem; display: flex; align-items: center; gap: 12px; font-weight: bold;">
            <i class="fas fa-graduation-cap"></i> Learning Outcomes
          </h2>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px;">
            ${coursesToCompare.map((course, index) => `
              <div style="background: white; border: 3px solid ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}; border-radius: 15px; padding: 25px; box-shadow: 0 8px 25px rgba(0,0,0,0.1); position: relative; overflow: hidden;">
                <div style="position: absolute; top: 0; left: 0; right: 0; height: 6px; background: ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'};"></div>
                <h3 style="color: ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}; margin: 0 0 20px 0; font-size: 1.3rem; font-weight: bold;">${course.title}</h3>
                <div style="color: #374151;">
                  <h4 style="margin: 0 0 15px 0; color: #374151; font-size: 1.1rem;">🎯 What you'll learn:</h4>
                  <ul style="margin: 0; padding: 0 0 0 20px; list-style: none;">
                    ${course.outcomes ? course.outcomes.slice(0, 4).map(outcome => `
                      <li style="margin-bottom: 12px; line-height: 1.5; color: #6b7280; position: relative; padding-left: 25px;">
                        <span style="position: absolute; left: 0; top: 0; color: ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}; font-weight: bold;">✓</span>
                        ${outcome}
                      </li>
                    `).join('') : '<li style="color: #9ca3af; font-style: italic;">No specific outcomes listed</li>'}
                  </ul>
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      ` : ''}
  
      <!-- Prerequisites Section -->
      ${coursesToCompare.some(c => c.prerequisites && c.prerequisites.length > 0) ? `
        <div style="margin-bottom: 35px;">
          <h2 style="color: #2563eb; margin-bottom: 20px; font-size: 1.8rem; display: flex; align-items: center; gap: 12px; font-weight: bold;">
            <i class="fas fa-list-check"></i> Prerequisites
          </h2>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 25px;">
            ${coursesToCompare.map((course, index) => `
              <div style="background: white; border: 3px solid ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}; border-radius: 15px; padding: 25px; box-shadow: 0 8px 25px rgba(0,0,0,0.1); position: relative; overflow: hidden;">
                <div style="position: absolute; top: 0; left: 0; right: 0; height: 6px; background: ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'};"></div>
                <h3 style="color: ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}; margin: 0 0 20px 0; font-size: 1.3rem; font-weight: bold;">${course.title}</h3>
                <div style="color: #374151;">
                  <h4 style="margin: 0 0 15px 0; color: #374151; font-size: 1.1rem;">📋 Requirements:</h4>
                  <ul style="margin: 0; padding: 0 0 0 20px; list-style: none;">
                    ${course.prerequisites && course.prerequisites.length > 0 ? 
                      course.prerequisites.map(prereq => `
                        <li style="margin-bottom: 12px; line-height: 1.5; color: #6b7280; position: relative; padding-left: 25px;">
                          <span style="position: absolute; left: 0; top: 0; color: ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}; font-weight: bold;">•</span>
                          ${prereq}
                        </li>
                      `).join('') : 
                      '<li style="color: #9ca3af; font-style: italic;">No specific prerequisites</li>'
                    }
                  </ul>
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      ` : ''}
  
      <!-- Content Overlap Analysis -->
      ${overlaps.length > 0 ? `
        <div style="margin-bottom: 35px;">
          <h2 style="color: #2563eb; margin-bottom: 20px; font-size: 1.8rem; display: flex; align-items: center; gap: 12px; font-weight: bold;">
            <i class="fas fa-intersection"></i> Content Overlap Analysis
          </h2>
          <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 8px 25px rgba(0,0,0,0.1); border: 3px solid #f59e0b;">
            ${overlaps.map(overlap => `
              <div style="margin-bottom: 25px; padding: 20px; background: linear-gradient(135deg, #fef3c7, #fde68a); border-radius: 12px; border-left: 6px solid #f59e0b; box-shadow: 0 4px 15px rgba(245, 158, 11, 0.2);">
                <h3 style="margin: 0 0 15px 0; color: #92400e; font-size: 1.2rem; font-weight: bold;">${overlap.courses.join(' & ')}</h3>
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 15px; flex-wrap: wrap;">
                  <span style="font-weight: bold; color: #92400e; font-size: 1.1rem;">🎯 Overlap Score: ${overlap.score}/5</span>
                  <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                    ${overlap.details.category ? '<span style="background: #059669; color: white; padding: 4px 12px; border-radius: 15px; font-size: 0.85rem; font-weight: bold;">Same Category</span>' : ''}
                    ${overlap.details.audienceWords > 0 ? '<span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 15px; font-size: 0.85rem; font-weight: bold;">Shared Audience</span>' : ''}
                  </div>
                </div>
                <p style="margin: 0; color: #92400e; line-height: 1.6; font-weight: 500;">💡 These courses have significant content overlap and complement each other well in a learning path.</p>
              </div>
            `).join('')}
          </div>
        </div>
      ` : ''}
  
      <!-- Suggested Learning Path -->
      <div style="margin-bottom: 35px;">
        <h2 style="color: #2563eb; margin-bottom: 20px; font-size: 1.8rem; display: flex; align-items: center; gap: 12px; font-weight: bold;">
          <i class="fas fa-route"></i> Suggested Learning Path
        </h2>
        <div style="background: white; border-radius: 15px; padding: 25px; box-shadow: 0 8px 25px rgba(0,0,0,0.1); border: 3px solid #2563eb;">
          <p style="margin: 0 0 25px 0; color: #6b7280; font-size: 1.1rem; line-height: 1.6;">📚 Based on difficulty levels and prerequisites, here's our recommended learning sequence:</p>
          
          <div style="position: relative;">
            ${suggestedPath.map((course, index) => `
              <div style="display: flex; align-items: flex-start; gap: 20px; margin-bottom: ${index < suggestedPath.length - 1 ? '30px' : '0'}; position: relative;">
                <div style="width: 50px; height: 50px; border-radius: 50%; background: ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.4rem; flex-shrink: 0; box-shadow: 0 4px 12px rgba(0,0,0,0.2); z-index: 2; position: relative;">${index + 1}</div>
                
                <div style="flex: 1; background: ${index % 2 === 0 ? '#f8fafc' : 'white'}; padding: 20px; border-radius: 12px; border: 2px solid ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                  <h3 style="margin: 0 0 12px 0; color: #374151; font-size: 1.3rem; font-weight: bold;">${course.title}</h3>
                  <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px; flex-wrap: wrap;">
                    <span style="padding: 4px 12px; border-radius: 12px; font-size: 0.85rem; font-weight: bold; color: white; background: ${
                      course.difficulty === 'beginner' ? '#059669' : 
                      course.difficulty === 'intermediate' ? '#d97706' : '#dc2626'
                    };">${course.difficulty.toUpperCase()}</span>
                    <span style="color: #6b7280; font-weight: 500;">⏱️ ${course.duration || 'Duration not specified'}</span>
                    ${course.prerequisites && course.prerequisites.includes('None - foundational course') ? '<span style="background: #10b981; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">🎯 FOUNDATIONAL</span>' : ''}
                  </div>
                  <p style="margin: 10px 0 0 0; color: #6b7280; line-height: 1.5;">
                    ${index === 0 ? '🚀 <strong>Start here</strong> - ' : `Step ${index + 1} - `}
                    ${course.description ? course.description.substring(0, 120) + '...' : 'Begin your learning journey with this course.'}
                  </p>
                </div>
              </div>
              
              ${index < suggestedPath.length - 1 ? `
                <div style="margin: 10px 0; text-align: center; position: relative;">
                  <div style="color: #9ca3af; font-size: 2rem; background: white; padding: 0 15px; z-index: 1; position: relative;">↓</div>
                  <div style="position: absolute; top: 50%; left: 25px; right: 0; height: 2px; background: linear-gradient(90deg, ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}, ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index + 1] || '#6b7280'}); z-index: 0;"></div>
                </div>
              ` : ''}
            `).join('')}
          </div>
        </div>
      </div>
      
      <!-- Action Buttons -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin-bottom: 25px;">
        ${coursesToCompare.map((course, index) => `
          <a href="${course.url}" target="_blank" rel="noopener" style="background: linear-gradient(135deg, ${['#2563eb', '#059669', '#dc2626', '#7c3aed'][index] || '#6b7280'}, ${['#1d4ed8', '#047857', '#b91c1c', '#6d28d9'][index] || '#4b5563'}); color: white; padding: 18px 25px; border-radius: 12px; text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 10px; font-weight: bold; font-size: 1.1rem; box-shadow: 0 6px 20px rgba(0,0,0,0.2); transition: all 0.3s ease; text-align: center;" onmouseover="this.style.transform='translateY(-3px) scale(1.02)'; this.style.boxShadow='0 12px 30px rgba(0,0,0,0.3)';" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 6px 20px rgba(0,0,0,0.2)';">
            <i class="fas fa-external-link-alt"></i> Launch ${course.title}
          </a>
        `).join('')}
      </div>
      
      <!-- Footer -->
      <div style="text-align: center; padding: 25px; background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 15px; box-shadow: inset 0 2px 10px rgba(0,0,0,0.1);">
        <button onclick="unifiedClearComparison()" style="background: linear-gradient(135deg, #dc2626, #b91c1c); color: white; padding: 15px 35px; border: none; border-radius: 12px; cursor: pointer; font-weight: bold; font-size: 1.1rem; box-shadow: 0 6px 20px rgba(220, 38, 38, 0.3); transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 10px;" onmouseover="this.style.transform='translateY(-2px)'; this.style.background='linear-gradient(135deg, #b91c1c, #991b1b)';" onmouseout="this.style.transform='translateY(0)'; this.style.background='linear-gradient(135deg, #dc2626, #b91c1c)';">
          <i class="fas fa-times"></i> Clear All & Close
        </button>
      </div>
    </div>
  `;
  
  // Create and show the modal
  richCreateModal(richComparisonHTML);
  console.log('✅ RICH comparison modal created successfully');
};

// Rich modal creation function
function richCreateModal(content) {
  // Remove any existing modals
  const existingModals = document.querySelectorAll('#richModal, #unifiedModal, #emergencyModal, [id*="Modal"]');
  existingModals.forEach(modal => {
    if (modal.id.toLowerCase().includes('comparison') || modal.id.toLowerCase().includes('modal')) {
      modal.remove();
    }
  });
  
  const modal = document.createElement('div');
  modal.id = 'richModal';
  modal.style.cssText = `
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    background: rgba(0, 0, 0, 0.8) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    z-index: 10000 !important;
    backdrop-filter: blur(8px) !important;
    animation: modalFadeIn 0.4s ease !important;
  `;
  
  const modalContent = document.createElement('div');
  modalContent.style.cssText = `
    background: white !important;
    border-radius: 20px !important;
    width: 95% !important;
    max-width: 1400px !important;
    max-height: 95vh !important;
    overflow: hidden !important;
    position: relative !important;
    box-shadow: 0 30px 100px rgba(0, 0, 0, 0.6) !important;
    animation: modalSlideIn 0.5s ease !important;
  `;
  
  const closeBtn = document.createElement('button');
  closeBtn.innerHTML = '×';
  closeBtn.style.cssText = `
    position: absolute !important;
    top: 15px !important;
    right: 20px !important;
    background: rgba(255, 255, 255, 0.9) !important;
    border: none !important;
    font-size: 32px !important;
    cursor: pointer !important;
    color: #6b7280 !important;
    z-index: 10001 !important;
    width: 45px !important;
    height: 45px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border-radius: 50% !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    transition: all 0.3s ease !important;
  `;
  
  closeBtn.onclick = () => {
    modal.style.animation = 'modalFadeOut 0.3s ease';
    setTimeout(() => modal.remove(), 300);
  };
  
  closeBtn.onmouseover = () => {
    closeBtn.style.background = '#dc2626';
    closeBtn.style.color = 'white';
    closeBtn.style.transform = 'scale(1.1)';
  };
  
  closeBtn.onmouseout = () => {
    closeBtn.style.background = 'rgba(255, 255, 255, 0.9)';
    closeBtn.style.color = '#6b7280';
    closeBtn.style.transform = 'scale(1)';
  };
  
  modalContent.innerHTML = content;
  modalContent.appendChild(closeBtn);
  modal.appendChild(modalContent);
  
  modal.onclick = (e) => {
    if (e.target === modal) {
      modal.style.animation = 'modalFadeOut 0.3s ease';
      setTimeout(() => modal.remove(), 300);
    }
  };
  
  // Add animations
  if (!document.getElementById('richModalAnimations')) {
    const style = document.createElement('style');
    style.id = 'richModalAnimations';
    style.textContent = `
      @keyframes modalFadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
      }
      @keyframes modalFadeOut {
        from { opacity: 1; }
        to { opacity: 0; }
      }
      @keyframes modalSlideIn {
        from { transform: translateY(50px) scale(0.95); opacity: 0; }
        to { transform: translateY(0) scale(1); opacity: 1; }
      }
    `;
    document.head.appendChild(style);
  }
  
  document.body.appendChild(modal);
  console.log('✅ Rich modal displayed successfully');
}

// Unified clear function
window.unifiedClearComparison = function() {
  selectedCourses.length = 0;
  comparisonList.length = 0;
  
  // Remove modal
  const modal = document.getElementById('richModal');
  if (modal) modal.remove();
  
  // Remove FAB
  const fab = document.querySelector('.unified-fab-btn');
  if (fab) fab.remove();
  
  // Update UI
  unifiedUpdateComparisonUI();
  
  showNotification('Comparison cleared!', 'success');
  console.log('✅ Unified clear complete');
};

// Fixed Lab Enhancement Function
window.fixLabDuplicates = function() {
  console.log('🔧 FINAL lab duplicate fix...');
  
  // First, remove ALL existing lab enhancement buttons
  document.querySelectorAll('.emergency-lab-actions, .lab-enhanced-actions, .final-lab-actions').forEach(actions => {
    actions.remove();
  });
  
  // Clear all enhancement markers
  document.querySelectorAll('[data-enhanced]').forEach(element => {
    element.removeAttribute('data-enhanced');
  });
  
  // Wait and then enhance properly
  setTimeout(() => {
    const labCards = document.querySelectorAll('.lab-card');
    console.log(`📦 Found ${labCards.length} lab cards to enhance`);
    
    labCards.forEach((card, index) => {
      // Skip if already has buttons
      if (card.querySelector('.final-lab-actions')) {
        return;
      }
      
      const labId = `lab-${index + 1}`;
      const title = card.querySelector('h3')?.textContent || `Lab ${index + 1}`;
      
      // Create clean action buttons
      const actionsDiv = document.createElement('div');
      actionsDiv.className = 'final-lab-actions';
      actionsDiv.style.cssText = `
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px solid #e2e8f0;
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
      `;
      
      // Bookmark button
      const bookmarkBtn = document.createElement('button');
      bookmarkBtn.innerHTML = '<i class="far fa-bookmark"></i> Bookmark';
      bookmarkBtn.className = 'lab-bookmark-btn';
      bookmarkBtn.style.cssText = `
        background: none;
        border: 1px solid #f59e0b;
        color: #f59e0b;
        padding: 8px 12px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        transition: all 0.3s ease;
      `;
      
      bookmarkBtn.onclick = function() {
        const icon = this.querySelector('i');
        if (icon.classList.contains('far')) {
          icon.className = 'fas fa-bookmark';
          this.style.background = '#f59e0b';
          this.style.color = 'white';
          showNotification('Lab bookmarked!', 'success');
        } else {
          icon.className = 'far fa-bookmark';
          this.style.background = 'none';
          this.style.color = '#f59e0b';
          showNotification('Bookmark removed', 'info');
        }
      };
      
      // Details button
      const detailsBtn = document.createElement('button');
      detailsBtn.innerHTML = '<i class="fas fa-info-circle"></i> Details';
      detailsBtn.className = 'lab-details-btn';
      detailsBtn.style.cssText = `
        background: none;
        border: 1px solid #2563eb;
        color: #2563eb;
        padding: 8px 12px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        transition: all 0.3s ease;
      `;
      
      detailsBtn.onclick = function() {
        const description = card.querySelector('p')?.textContent || 'Interactive development tool';
        const launchUrl = card.querySelector('a[href]')?.href || '#';
        
        alert(`📋 ${title}\n\n📝 ${description}\n\n🔗 ${launchUrl}\n\n✨ Features:\n• Interactive tools and simulations\n• Real-world case studies\n• Downloadable resources\n• Step-by-step guidance`);
      };
      
      actionsDiv.appendChild(bookmarkBtn);
      actionsDiv.appendChild(detailsBtn);
      card.appendChild(actionsDiv);
      
      console.log(`✅ Enhanced lab: ${title}`);
    });
    
    console.log('✅ Final lab enhancement complete - no more duplicates!');
  }, 1000);
};

// Override functions to prevent conflicts
window.toggleCompare = window.toggleCourseComparison;
window.updateComparisonUI = window.unifiedUpdateComparisonUI;
window.updateFABButton = window.unifiedUpdateFAB;
window.createFloatingButton = window.unifiedUpdateFAB;
window.emergencyShowComparison = window.unifiedShowComparison;
window.showEnhancedComparisonModal = window.unifiedShowComparison;

// Test function
window.testRichComparison = function() {
  console.log('🧪 Testing rich comparison...');
  
  // Add some test courses to selectedCourses if empty
  if (selectedCourses.length === 0) {
    selectedCourses.push('intro-dev-econ', 'rct-design');
    console.log('📝 Added test courses for demo');
  }
  
  console.log('📋 Selected courses:', selectedCourses);
  console.log('🚀 Launching rich comparison...');
  
  unifiedShowComparison();
};

// Initialize enhanced features when DOM loads
document.addEventListener('DOMContentLoaded', function() {
  console.log('🚨 Enhanced initialization started');
  
  generateLabsContent();
  
  // Auto-fix lab duplicates
  setTimeout(fixLabDuplicates, 2000);
  
  // Force update if courses already selected
  if (selectedCourses && selectedCourses.length > 0) {
    unifiedUpdateComparisonUI();
    unifiedUpdateFAB();
  }
});

// If DOM already loaded
if (document.readyState !== 'loading') {
  console.log('🚨 DOM already loaded, initializing...');
  setTimeout(fixLabDuplicates, 2000);
}

console.log('🔥 RICH COMPARISON SYSTEM LOADED!');
console.log('📝 Rich comparison features: ✅ Content depth bars, ✅ Learning paths, ✅ Overlap analysis');
console.log('🧪 Test: run testRichComparison() in console');
console.log('🔧 Fix labs: run fixLabDuplicates() in console');