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
      site: {
        title: "ImpactMojo 101 Knowledge Series - Development Education for South Asia",
        description: "Curated library of full-length knowledge decks exploring justice, equity, and development practice in India and South Asia.",
        keywords: "development education, South Asia, India, social justice, data feminism, development economics",
        author: "Dr. Varna Sri Raman"
      },
      hero: {
        title: "ImpactMojo 101 Knowledge Series",
        description: "ImpactMojo is a curated library of full-length knowledge decks that explore justice, equity, and development practice in India and South Asia. Each one is grounded in theory, applied in context, and ready for real-world use by educators, practitioners, and social researchers."
      },
      interface_text: {
        messages: {
          no_results: "No courses found. Try adjusting your search terms or filters.",
          loading: "Loading courses...",
          error: "Unable to load content. Please refresh the page.",
          welcome_back: "Welcome back!",
          login_success: "Successfully logged in!",
          logout_success: "Successfully logged out!"
        },
        buttons: {
          explore_courses: "Explore Courses",
          try_labs: "Try Labs",
          launch_course: "Launch Course",
          launch_lab: "Launch Lab",
          bookmark: "Bookmark",
          compare: "Compare",
          login: "Log In",
          signup: "Sign Up",
          logout: "Log Out"
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
   * Get interface text with fallback
   */
  getInterfaceText(path, fallback = null) {
    const text = this.get(`interface_text.${path}`);
    return text || fallback;
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
      if (element && hero.title) {
        element.textContent = hero.title;
        break;
      }
    }

    // Update hero description
    const descSelectors = [
      '.hero-description',
      '.hero p',
      'section:first-of-type p'
    ];
    
    for (const selector of descSelectors) {
      const element = document.querySelector(selector);
      if (element && hero.description) {
        element.textContent = hero.description;
        break;
      }
    }
  }

  /**
   * Update learning paths (preserves existing structure)
   */
  updateLearningPaths() {
    if (!this.isLoaded) return;

    const paths = this.content.learning_paths;
    if (!paths || !paths.paths) return;

    // Update section title
    const sectionTitle = document.querySelector('.learning-paths-section h2');
    if (sectionTitle && paths.title) {
      sectionTitle.innerHTML = `<i class="fas fa-route"></i> ${paths.title}`;
    }

    // Update individual path cards (non-destructive)
    paths.paths.forEach((path, index) => {
      const pathCard = document.querySelectorAll('.learning-path-card')[index];
      if (!pathCard) return;

      const titleElement = pathCard.querySelector('h3');
      if (titleElement && path.title) {
        titleElement.textContent = path.title;
      }

      const descElement = pathCard.querySelector('p');
      if (descElement && path.description) {
        descElement.textContent = path.description;
      }

      // Update course tags if provided
      if (path.courses) {
        const tagsContainer = pathCard.querySelector('.path-courses');
        if (tagsContainer) {
          tagsContainer.innerHTML = path.courses.map(course => 
            `<span class="course-tag">${course}</span>`
          ).join('');
        }
      }
    });
  }

  /**
   * Update courses section header
   */
  updateCoursesSection() {
    if (!this.isLoaded) return;

    const courses = this.content.courses_section;
    if (!courses) return;

    const sectionTitle = document.querySelector('.courses-section h2');
    if (sectionTitle && courses.title && courses.icon) {
      sectionTitle.innerHTML = `<i class="${courses.icon}"></i> ${courses.title}`;
    }
  }

  /**
   * Update labs section header
   */
  updateLabsSection() {
    if (!this.isLoaded) return;

    const labs = this.content.labs_section;
    if (!labs) return;

    const sectionTitle = document.querySelector('.labs-section h2');
    if (sectionTitle && labs.title && labs.icon) {
      sectionTitle.innerHTML = `<i class="${labs.icon}"></i> ${labs.title}`;
    }

    const subtitle = document.querySelector('.labs-section .section-header p');
    if (subtitle && labs.subtitle) {
      subtitle.textContent = labs.subtitle;
    }
  }

  /**
   * Update footer content (preserves existing structure)
   */
  updateFooter() {
    if (!this.isLoaded) return;

    const footer = this.content.footer;
    if (!footer || !footer.sections) return;

    footer.sections.forEach((section, index) => {
      const footerSection = document.querySelectorAll('.footer-section')[index];
      if (!footerSection) return;

      const titleElement = footerSection.querySelector('h4');
      if (titleElement && section.title) {
        titleElement.textContent = section.title;
      }

      // Update content safely
      if (section.content) {
        const contentContainer = footerSection.querySelector('p') || 
                               footerSection.querySelector('ul') ||
                               footerSection.querySelector('.contact-info');
        
        if (contentContainer && section.content[0]) {
          if (section.content[0].includes('@') || section.content[0].includes('www.')) {
            // Contact info
            if (contentContainer.classList.contains('contact-info')) {
              contentContainer.innerHTML = section.content.map(item => `<p>${item}</p>`).join('');
            }
          } else if (contentContainer.tagName === 'P') {
            // Regular paragraph
            contentContainer.textContent = section.content[0];
          }
        }
      }
    });
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
      this.updateFooter();
      
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