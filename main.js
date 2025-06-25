// ImpactMojo 101 - Main Application Script
// Handles course rendering, filtering, search, and UI interactions

// Global variables
let currentFilter = 'all';
let currentSearch = '';
let bookmarkFilter = false;
let allCourses = [];
let allLabs = [];

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
  console.log('🚀 Initializing ImpactMojo application...');
  
  // Load course data
  if (typeof window.impactMojoAllCourses !== 'undefined') {
    allCourses = window.impactMojoAllCourses;
    console.log(`📚 Loaded ${allCourses.length} courses`);
  }
  
  // Load lab data  
  if (typeof window.labs !== 'undefined') {
    allLabs = window.labs;
    console.log(`🧪 Loaded ${allLabs.length} labs`);
  }
  
  // Initialize features
  initializeSearch();
  initializeFilters();
  initializeNotifications();
  
  // Render initial content
  setTimeout(() => {
    renderCourses();
    renderLabs();
  }, 100);
});

// ===== SEARCH AND FILTER FUNCTIONS =====

// Initialize search functionality
function initializeSearch() {
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    let searchTimeout;
    searchInput.addEventListener('input', function() {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        currentSearch = this.value.toLowerCase().trim();
        renderCourses();
        renderLabs();
      }, 300);
    });
  }
}

// Initialize filter functionality
function initializeFilters() {
  // Category filter
  const categoryFilter = document.getElementById('categoryFilter');
  if (categoryFilter) {
    categoryFilter.addEventListener('change', function() {
      currentFilter = this.value;
      renderCourses();
      renderLabs();
    });
  }
  
  // Difficulty filter
  const difficultyFilter = document.getElementById('difficultyFilter');
  if (difficultyFilter) {
    difficultyFilter.addEventListener('change', function() {
      renderCourses();
      renderLabs();
    });
  }
  
  // Duration filter
  const durationFilter = document.getElementById('durationFilter');
  if (durationFilter) {
    durationFilter.addEventListener('change', function() {
      renderCourses();
      renderLabs();
    });
  }
}

// Apply filters to courses
function applyCourseFilters() {
  const searchTerm = document.getElementById('courseSearch')?.value?.toLowerCase() || '';
  const categoryFilter = document.getElementById('courseCategoryFilter')?.value || 'all';
  const difficultyFilter = document.getElementById('courseDifficultyFilter')?.value || 'all';
  const durationFilter = document.getElementById('courseDurationFilter')?.value || 'all';
  
  const courses = window.impactMojoAllCourses || window.courses || [];
  
  const filteredCourses = courses.filter(course => {
    const matchesSearch = !searchTerm || 
      course.title.toLowerCase().includes(searchTerm) ||
      course.description?.toLowerCase().includes(searchTerm) ||
      course.topics?.some(topic => topic.toLowerCase().includes(searchTerm));
    
    const matchesCategory = categoryFilter === 'all' || course.category === categoryFilter;
    const matchesDifficulty = difficultyFilter === 'all' || course.difficulty === difficultyFilter;
    const matchesDuration = durationFilter === 'all' || course.duration === durationFilter;
    
    return matchesSearch && matchesCategory && matchesDifficulty && matchesDuration;
  });
  
  renderFilteredCourses(filteredCourses);
  updateCourseStats(filteredCourses.length, courses.length);
}

// Apply filters to labs
function applyLabFilters() {
  const searchTerm = document.getElementById('labSearch')?.value?.toLowerCase() || '';
  const categoryFilter = document.getElementById('labCategoryFilter')?.value || 'all';
  const difficultyFilter = document.getElementById('labDifficultyFilter')?.value || 'all';
  
  const labs = window.labs || [];
  
  const filteredLabs = labs.filter(lab => {
    const matchesSearch = !searchTerm || 
      lab.title.toLowerCase().includes(searchTerm) ||
      lab.description?.toLowerCase().includes(searchTerm) ||
      lab.topics?.some(topic => topic.toLowerCase().includes(searchTerm));
    
    const matchesCategory = categoryFilter === 'all' || lab.category === categoryFilter;
    const matchesDifficulty = difficultyFilter === 'all' || lab.difficulty ===