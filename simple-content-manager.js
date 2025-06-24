// Simple Content Manager for ImpactMojo
// Manages dynamic content updates based on content-config.json

console.log('📝 Loading Simple Content Manager...');

class SimpleContentManager {
  constructor() {
    this.config = null;
    this.isLoaded = false;
  }

  async loadConfig() {
    try {
      const response = await fetch('./content-config.json');
      this.config = await response.json();
      this.isLoaded = true;
      console.log('✅ Content configuration loaded successfully');
      return this.config;
    } catch (error) {
      console.error('❌ Failed to load content configuration:', error);
      // Fallback to default configuration
      this.config = this.getDefaultConfig();
      this.isLoaded = true;
      return this.config;
    }
  }

  getDefaultConfig() {
    return {
      site: {
        title: "ImpactMojo 101 Knowledge Series",
        tagline: "Development Education for South Asia",
        description: "A curated library of full-length knowledge decks and interactive tools/labs exploring justice, equity, and development practice in India and South Asia.",
        email: "info@impactmojo.in"
      },
      branding: {
        showTitleInTopLeft: false,
        showTaglineOnly: true
      }
    };
  }

  // Update site metadata
  updateSiteMetadata() {
    if (!this.isLoaded) return;

    const { site } = this.config;
    
    // Update document title
    if (site.title) {
      document.title = site.title;
    }

    // Update meta description
    const metaDescription = document.querySelector('meta[name="description"]');
    if (metaDescription && site.description) {
      metaDescription.setAttribute('content', site.description);
    }
  }

  // Update hero section content
  updateHeroSection() {
    if (!this.isLoaded || !this.config.hero) return;

    const { hero } = this.config;

    // Update main heading
    const mainHeading = document.querySelector('.hero h1');
    if (mainHeading && hero.title) {
      mainHeading.textContent = hero.title;
    }

    // Update subtitle
    const subtitle = document.querySelector('.hero .subtitle');
    if (subtitle && hero.subtitle) {
      subtitle.textContent = hero.subtitle;
    }

    // Update description
    const description = document.querySelector('.hero .description');
    if (description && hero.description) {
      description.textContent = hero.description;
    }

    // Update CTA buttons
    if (hero.ctaButtons) {
      hero.ctaButtons.forEach((button, index) => {
        const ctaButton = document.querySelector(`.hero .cta-btn:nth-child(${index + 1})`);
        if (ctaButton) {
          ctaButton.textContent = button.text;
          ctaButton.href = button.href;
          
          if (button.primary) {
            ctaButton.style.backgroundColor = button.backgroundColor;
            ctaButton.style.color = button.color;
          }
        }
      });
    }
  }

  // Update branding display
  updateBranding() {
    if (!this.isLoaded || !this.config.branding) return;

    const { branding, site } = this.config;
    const brandElement = document.querySelector('.nav-brand');
    
    if (brandElement) {
      if (branding.showTaglineOnly && !branding.showTitleInTopLeft) {
        const titleElement = brandElement.querySelector('h1');
        const taglineElement = brandElement.querySelector('span');
        
        if (titleElement) titleElement.style.display = 'none';
        if (taglineElement && site.tagline) {
          taglineElement.textContent = site.tagline;
          taglineElement.style.display = 'block';
        }
      }
    }
  }

  // Update section titles and descriptions
  updateSectionContent() {
    if (!this.isLoaded || !this.config.sections) return;

    const { sections } = this.config;

    // Update Latest Additions section
    if (sections.latestAdditions) {
      const section = document.querySelector('#latest-additions');
      if (section) {
        const title = section.querySelector('h2');
        const description = section.querySelector('.section-description');
        
        if (title) title.textContent = sections.latestAdditions.title;
        if (description) description.textContent = sections.latestAdditions.description;
      }
    }

    // Update Learning Paths section
    if (sections.learningPaths) {
      const section = document.querySelector('#learning-paths');
      if (section) {
        const title = section.querySelector('h2');
        const description = section.querySelector('.section-description');
        
        if (title) title.textContent = sections.learningPaths.title;
        if (description) description.textContent = sections.learningPaths.description;
      }
    }

    // Update Popular Courses section
    if (sections.popularCourses) {
      const section = document.querySelector('#popular-courses');
      if (section) {
        const title = section.querySelector('h2');
        const description = section.querySelector('.section-description');
        
        if (title) title.textContent = sections.popularCourses.title;
        if (description) description.textContent = sections.popularCourses.description;
      }
    }

    // Update Upcoming Content section
    if (sections.upcomingContent) {
      const section = document.querySelector('#upcoming');
      if (section) {
        const title = section.querySelector('h2');
        const description = section.querySelector('.section-description');
        
        if (title) title.textContent = sections.upcomingContent.title;
        if (description) description.textContent = sections.upcomingContent.description;
      }
    }
  }

  // Update footer content
  updateFooter() {
    if (!this.isLoaded || !this.config.footer) return;

    const { footer } = this.config;

    // Update contact email
    const contactEmail = document.querySelector('.footer-email a');
    if (contactEmail && footer.contactEmail) {
      contactEmail.href = `mailto:${footer.contactEmail}`;
      contactEmail.textContent = footer.contactEmail;
    }

    // Update copyright text
    const copyright = document.querySelector('.footer-copyright');
    if (copyright && footer.copyrightText) {
      copyright.textContent = footer.copyrightText;
    }
  }

  // Update author section
  updateAuthorSection() {
    if (!this.isLoaded || !this.config.author) return;

    const { author } = this.config;
    const authorSection = document.querySelector('#author');
    
    if (authorSection) {
      // Update author name
      const nameElement = authorSection.querySelector('.author-name');
      if (nameElement && author.name) {
        nameElement.textContent = author.name;
      }

      // Update author title
      const titleElement = authorSection.querySelector('.author-title');
      if (titleElement && author.title) {
        titleElement.textContent = author.title;
      }

      // Update author bio
      const bioElement = authorSection.querySelector('.author-bio');
      if (bioElement && author.bio) {
        bioElement.textContent = author.bio;
      }

      // Update author photo
      const photoElement = authorSection.querySelector('.author-photo img');
      if (photoElement && author.photoUrl) {
        photoElement.src = author.photoUrl;
        photoElement.alt = `Photo of ${author.name}`;
      }
    }
  }

  // Update theme configuration
  updateThemeSettings() {
    if (!this.isLoaded || !this.config.theme) return;

    const { theme } = this.config;

    // Set CSS custom properties for theme colors
    if (theme.colors) {
      const root = document.documentElement;
      
      if (theme.colors.primary) {
        root.style.setProperty('--primary-color', theme.colors.primary);
      }
      if (theme.colors.secondary) {
        root.style.setProperty('--secondary-color', theme.colors.secondary);
      }
      if (theme.colors.accent) {
        root.style.setProperty('--accent-color', theme.colors.accent);
      }
    }

    // Update dark mode toggle icons
    if (theme.darkMode && theme.darkMode.toggleIcon) {
      const toggleButton = document.querySelector('.theme-toggle i');
      if (toggleButton) {
        // Set initial icon based on current theme
        const isDark = document.body.classList.contains('dark-theme');
        toggleButton.className = isDark ? 
          theme.darkMode.toggleIcon.dark : 
          theme.darkMode.toggleIcon.light;
      }
    }
  }

  // Update authentication tooltips
  updateAuthTooltips() {
    if (!this.isLoaded || !this.config.authentication) return;

    const { authentication } = this.config;

    // Update login tooltip
    const loginBtn = document.querySelector('[onclick="showLoginModal()"]');
    if (loginBtn && authentication.loginTooltip) {
      loginBtn.setAttribute('title', authentication.loginTooltip);
    }

    // Update signup tooltip
    const signupBtn = document.querySelector('[onclick="showSignupModal()"]');
    if (signupBtn && authentication.signupTooltip) {
      signupBtn.setAttribute('title', authentication.signupTooltip);
    }
  }

  // Initialize all content updates
  async initialize() {
    await this.loadConfig();
    
    if (this.isLoaded) {
      this.updateSiteMetadata();
      this.updateBranding();
      this.updateHeroSection();
      this.updateSectionContent();
      this.updateFooter();
      this.updateAuthorSection();
      this.updateThemeSettings();
      this.updateAuthTooltips();
      
      console.log('✅ Content Manager initialized successfully');
    } else {
      console.warn('⚠️ Content Manager initialized with default configuration');
    }
  }

  // Get configuration value by path
  getConfig(path) {
    if (!this.isLoaded) return null;
    
    return path.split('.').reduce((obj, key) => obj && obj[key], this.config);
  }

  // Check if feature is enabled
  isFeatureEnabled(feature) {
    return this.getConfig(`features.${feature}`) || false;
  }

  // Get course exclusions
  getExcludedCourses() {
    return this.getConfig('excludedCourses') || [];
  }

  // Update content dynamically
  updateContent(path, value) {
    if (!this.isLoaded) return false;

    const keys = path.split('.');
    const lastKey = keys.pop();
    const target = keys.reduce((obj, key) => obj && obj[key], this.config);
    
    if (target) {
      target[lastKey] = value;
      return true;
    }
    
    return false;
  }
}

// Create global instance
const contentManager = new SimpleContentManager();

// Make available globally
if (typeof window !== 'undefined') {
  window.contentManager = contentManager;
}

// Auto-initialize when DOM is ready
if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      contentManager.initialize();
    });
  } else {
    contentManager.initialize();
  }
}

console.log('✅ Simple Content Manager loaded successfully!');