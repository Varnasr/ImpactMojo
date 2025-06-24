/**
 * Simple Content Manager - Works alongside existing main.js
 * Only handles text content updates, preserves all existing functionality
 */

class SimpleContentManager {
  constructor() {
    this.content = null;
    this.isLoaded = false;
  }

  /**
   * Load content configuration from JSON file
   */
  async loadContent() {
    try {
      const response = await fetch('./content-config.json');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      this.content = await response.json();
      this.isLoaded = true;
      console.log('✅ Content configuration loaded successfully');
      return this.content;
    } catch (error) {
      console.warn('⚠️ Could not load content configuration, using defaults:', error);
      // Use defaults if config file not found
      this.useDefaults();
      return null;
    }
  }

  /**
   * Use default content if config file not available
   */
  useDefaults() {
    this.content = {
      hero: {
        title: "ImpactMojo 101 Knowledge Series",
        description: "ImpactMojo is a curated library of full-length knowledge decks that explore justice, equity, and development practice in India and South Asia. Each one is grounded in theory, applied in context, and ready for real-world use by educators, practitioners, and social researchers."
      },
      interface_text: {
        messages: {
          no_results: "No courses found. Try adjusting your search terms or filters."
        }
      }
    };
    this.isLoaded = true;
  }

  /**
   * Get content by path (e.g., 'hero.title')
   */
  get(path) {
    if (!this.isLoaded || !this.content) {
      return null;
    }

    const keys = path.split('.');
    let current = this.content;
    
    for (const key of keys) {
      if (current && typeof current === 'object' && key in current) {
        current = current[key];
      } else {
        return null;
      }
    }
    
    return current;
  }

  /**
   * Update page title and meta tags (non-destructive)
   */
  updatePageMeta() {
    if (!this.isLoaded) return;

    const site = this.content.site;
    if (!site) return;
    
    // Only update if not already set
    if (document.title === '' || document.title.includes('Document')) {
      document.title = site.title;
    }
    
    // Update meta tags safely
    this.safeUpdateMeta('description', site.description);
    this.safeUpdateMeta('keywords', site.keywords);
    this.safeUpdateMeta('author', site.author);
  }

  /**
   * Safely update meta tags without breaking existing ones
   */
  safeUpdateMeta(name, content) {
    if (!content) return;
    
    let meta = document.querySelector(`meta[name="${name}"]`);
    if (!meta) {
      meta = document.createElement('meta');
      meta.name = name;
      document.head.appendChild(meta);
    }
    
    // Only update if empty or default
    if (!meta.content || meta.content.includes('Generated') || meta.content.length < 10) {
      meta.content = content;
    }
  }

  /**
   * Update hero section text (preserves existing if content not available)
   */
  updateHeroSection() {
    if (!this.isLoaded) return;

    const hero = this.content.hero;
    if (!hero) return;

    // Update hero title
    const titleSelectors = [
      '.hero-title',
      '.hero h1', 
      'section:first-of-type h1',
      'header + main h1'
    ];
    
    for (const selector of titleSelectors) {
      const element = document.querySelector(selector);
      if (element && this.shouldUpdateElement(element)) {
        element.textContent = hero.title;
        break;
      }
    }

    // Update hero description
    const descSelectors = [
      '.hero-description',
      '.hero p',
      'section:first-of-type p',
      'header + main p'
    ];
    
    for (const selector of descSelectors) {
      const element = document.querySelector(selector);
      if (element && this.shouldUpdateElement(element)) {
        element.textContent = hero.description;
        break;
      }
    }
  }

  /**
   * Check if element should be updated (not empty, not user-customized)
   */
  shouldUpdateElement(element) {
    const text = element.textContent.trim();
    return text === '' || 
           text.includes('ImpactMojo') || 
           text.includes('knowledge deck') ||
           text.length < 10;
  }

  /**
   * Update learning paths section
   */
  updateLearningPaths() {
    if (!this.isLoaded) return;

    const pathsData = this.content.learning_paths;
    if (!pathsData) return;

    // Update section title
    const titleElement = document.querySelector('#learning-paths h3, .learning-paths h3');
    if (titleElement && this.shouldUpdateElement(titleElement)) {
      titleElement.innerHTML = `<i class="${pathsData.icon}"></i> ${pathsData.title}`;
    }

    // Update subtitle if it exists
    const subtitleElement = document.querySelector('#learning-paths .section-subtitle, .learning-paths .section-subtitle');
    if (subtitleElement && pathsData.subtitle) {
      subtitleElement.textContent = pathsData.subtitle;
    }
  }

  /**
   * Update courses section headers
   */
  updateCoursesSection() {
    if (!this.isLoaded) return;

    const coursesData = this.content.courses_section;
    if (!coursesData) return;

    // Update section title
    const titleElement = document.querySelector('#courses h3, .courses-section h3');
    if (titleElement && this.shouldUpdateElement(titleElement)) {
      titleElement.innerHTML = `<i class="${coursesData.icon}"></i> ${coursesData.title}`;
    }

    // Update subtitle
    const subtitleElement = document.querySelector('#courses h3 + p, .courses-section h3 + p');
    if (subtitleElement && this.shouldUpdateElement(subtitleElement)) {
      subtitleElement.textContent = coursesData.subtitle;
    }

    // Update search placeholder
    const searchInput = document.querySelector('#searchInput');
    if (searchInput && (!searchInput.placeholder || searchInput.placeholder === '')) {
      searchInput.placeholder = this.get('interface_text.labels.search_placeholder') || 'Search courses...';
    }
  }

  /**
   * Update labs section
   */
  updateLabsSection() {
    if (!this.isLoaded) return;

    const labsData = this.content.labs_section;
    if (!labsData) return;

    const titleElement = document.querySelector('#labs h3, .labs-section h3');
    if (titleElement && this.shouldUpdateElement(titleElement)) {
      titleElement.innerHTML = `<i class="${labsData.icon}"></i> ${labsData.title}`;
    }

    const subtitleElement = document.querySelector('#labs h3 + p, .labs-section h3 + p');
    if (subtitleElement && this.shouldUpdateElement(subtitleElement)) {
      subtitleElement.textContent = labsData.subtitle;
    }
  }

  /**
   * Get interface text (fallback to key if not found)
   */
  getInterfaceText(path, fallback = null) {
    const text = this.get(`interface_text.${path}`);
    return text || fallback || path.split('.').pop();
  }

  /**
   * Format dynamic messages
   */
  formatMessage(messageKey, replacements = {}) {
    if (!this.isLoaded) return messageKey;
    
    let message = this.get(`interface_text.messages.${messageKey}`) || messageKey;
    
    // Replace placeholders like {count} with actual values
    Object.keys(replacements).forEach(key => {
      message = message.replace(`{${key}}`, replacements[key]);
    });
    
    return message;
  }

  /**
   * Initialize all content updates (non-destructive)
   */
  async initialize() {
    try {
      await this.loadContent();
      
      // Update content in a safe, non-destructive way
      this.updatePageMeta();
      this.updateHeroSection();
      this.updateLearningPaths();
      this.updateCoursesSection();
      this.updateLabsSection();
      
      // Dispatch event for existing code to hook into
      window.dispatchEvent(new CustomEvent('contentManagerReady', { 
        detail: { 
          content: this.content,
          getText: (path, fallback) => this.getInterfaceText(path, fallback),
          formatMessage: (key, replacements) => this.formatMessage(key, replacements)
        }
      }));
      
      console.log('✅ Content manager initialized (preserving existing functionality)');
      
    } catch (error) {
      console.warn('⚠️ Content manager initialization failed, website will work normally:', error);
    }
  }
}

// Create global instance
const simpleContentManager = new SimpleContentManager();

// Auto-initialize when DOM is ready (doesn't interfere with existing code)
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    // Add small delay to let existing scripts run first
    setTimeout(() => {
      simpleContentManager.initialize();
    }, 100);
  });
} else {
  setTimeout(() => {
    simpleContentManager.initialize();
  }, 100);
}

// Export for use in existing scripts (backwards compatible)
window.contentManager = simpleContentManager;

// Helper function for existing code to use
window.getContentText = function(path, fallback = null) {
  return simpleContentManager.getInterfaceText(path, fallback);
};

window.formatContentMessage = function(messageKey, replacements = {}) {
  return simpleContentManager.formatMessage(messageKey, replacements);
};