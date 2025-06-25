// Enhanced Content Manager for ImpactMojo
// Comprehensive content management system for the entire website

console.log('📝 Loading Enhanced Content Manager v2.0...');

class EnhancedContentManager {
  constructor() {
    this.config = null;
    this.isLoaded = false;
    this.configPath = './content-config.json';
  }

  async loadConfig() {
    try {
      const response = await fetch(this.configPath);
      this.config = await response.json();
      this.isLoaded = true;
      console.log('✅ Enhanced content configuration loaded successfully');
      return this.config;
    } catch (error) {
      console.error('❌ Failed to load content configuration:', error);
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
        description: "A curated library of development education courses",
        email: "contact@impactmojo.in",
        upiId: "impactmojo@upi"
      }
    };
  }

  // ===== SITE METADATA & SEO =====
  updateSiteMetadata() {
    if (!this.isLoaded) return;

    const { site, seo } = this.config;
    
    // Update document title
    if (site.title) {
      document.title = site.title;
    }

    // Update meta description
    const metaDescription = document.querySelector('meta[name="description"]');
    if (metaDescription && site.description) {
      metaDescription.setAttribute('content', site.description);
    }

    // Update SEO keywords
    if (seo && seo.keywords) {
      const metaKeywords = document.querySelector('meta[name="keywords"]');
      if (metaKeywords) {
        metaKeywords.setAttribute('content', seo.keywords);
      }
    }

    // Update Open Graph tags
    if (seo) {
      this.updateOpenGraphTags(seo);
    }
  }

  updateOpenGraphTags(seo) {
    const ogTags = {
      'og:title': this.config.site.title,
      'og:description': this.config.site.description,
      'og:image': seo.ogImage,
      'twitter:card': seo.twitterCard
    };

    Object.entries(ogTags).forEach(([property, content]) => {
      if (content) {
        let meta = document.querySelector(`meta[property="${property}"]`) || 
                   document.querySelector(`meta[name="${property}"]`);
        if (meta) {
          meta.setAttribute('content', content);
        }
      }
    });
  }

  // ===== NAVIGATION =====
  updateNavigation() {
    if (!this.isLoaded || !this.config.navigation) return;

    const { navigation } = this.config;
    const navLinks = document.querySelector('.nav-links');
    
    if (navLinks && navigation.links) {
      // Clear existing links
      navLinks.innerHTML = '';
      
      // Add new links from config
      navigation.links.forEach(link => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        
        a.href = link.href;
        a.textContent = link.text;
        
        // Add special styling for "Start Here" button
        if (link.isSpecial) {
          a.classList.add('start-here-link');
        }
        
        // Handle external links
        if (link.external) {
          a.target = '_blank';
          a.rel = 'noopener noreferrer';
        }
        
        li.appendChild(a);
        navLinks.appendChild(li);
      });
    }
  }

  // ===== HERO SECTION =====
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
      const ctaContainer = document.querySelector('.cta-buttons');
      if (ctaContainer) {
        ctaContainer.innerHTML = '';
        
        hero.ctaButtons.forEach(button => {
          if (button.enabled) {
            const a = document.createElement('a');
            a.href = button.href;
            a.textContent = button.text;
            a.className = `cta-btn ${button.type}`;
            ctaContainer.appendChild(a);
          }
        });
      }
    }

    // Update background gradient
    if (hero.backgroundGradient) {
      const heroSection = document.querySelector('.hero');
      if (heroSection) {
        heroSection.style.background = `linear-gradient(135deg, ${hero.backgroundGradient.start}, ${hero.backgroundGradient.end})`;
      }
    }
  }

  // ===== SECTIONS CONTENT =====
  updateSections() {
    if (!this.isLoaded || !this.config.sections) return;

    const { sections } = this.config;

    // Update Latest Additions
    if (sections.latestAdditions) {
      this.updateLatestAdditions(sections.latestAdditions);
    }

    // Update Learning Paths
    if (sections.learningPaths) {
      this.updateLearningPaths(sections.learningPaths);
    }

    // Update Resources Section
    if (sections.resources) {
      this.updateResourcesSection(sections.resources);
    }

    // Update Upcoming Section
    if (sections.upcoming) {
      this.updateUpcomingSection(sections.upcoming);
    }

    // Update section titles and descriptions
    this.updateSectionTitles(sections);
  }

  updateLatestAdditions(latestAdditions) {
    const section = document.querySelector('#latest .latest-additions');
    if (!section) return;

    const title = section.querySelector('h3');
    if (title) {
      title.innerHTML = `<i class="fas fa-star"></i> ${latestAdditions.title}`;
    }

    const list = section.querySelector('ul');
    if (list && latestAdditions.items) {
      list.innerHTML = '';
      
      latestAdditions.items.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `
          <div class="course-info">
            <div class="course-name">${item.name}</div>
            <div class="course-description">${item.description}</div>
          </div>
          <div class="date">${item.date}</div>
        `;
        list.appendChild(li);
      });
    }
  }

  updateLearningPaths(learningPaths) {
    const section = document.querySelector('#learning-paths');
    if (!section) return;

    const title = section.querySelector('h2');
    if (title) {
      title.textContent = learningPaths.title;
    }

    const description = section.querySelector('.section-description');
    if (description) {
      description.textContent = learningPaths.description;
    }

    // Update learning path cards
    const pathsGrid = section.querySelector('.paths-grid');
    if (pathsGrid && learningPaths.paths) {
      pathsGrid.innerHTML = '';
      
      learningPaths.paths.forEach(path => {
        const pathCard = document.createElement('div');
        pathCard.className = 'path-card';
        pathCard.style.borderLeftColor = path.color;
        
        pathCard.innerHTML = `
          <h4 style="color: ${path.color}">${path.title}</h4>
          <p>${path.description}</p>
          <div class="course-tags">
            ${path.courses.map(course => `<span>${course}</span>`).join('')}
          </div>
        `;
        
        pathsGrid.appendChild(pathCard);
      });
    }
  }

  updateResourcesSection(resources) {
    const section = document.querySelector('#resources');
    if (!section) return;

    const title = section.querySelector('h2');
    if (title) {
      title.textContent = resources.title;
    }

    const description = section.querySelector('.section-description');
    if (description) {
      description.textContent = resources.description;
    }

    // Create resources grid if it doesn't exist
    let resourcesGrid = section.querySelector('.resources-grid');
    if (!resourcesGrid) {
      resourcesGrid = document.createElement('div');
      resourcesGrid.className = 'resources-grid';
      section.appendChild(resourcesGrid);
    }

    if (resources.items) {
      resourcesGrid.innerHTML = '';
      
      resources.items.forEach(item => {
        const resourceCard = document.createElement('div');
        resourceCard.className = 'resource-card';
        
        resourceCard.innerHTML = `
          <div class="resource-icon">
            <i class="${item.icon}"></i>
          </div>
          <h4>${item.title}</h4>
          <p>${item.description}</p>
          <a href="${item.url}" ${item.type === 'external' ? 'target="_blank" rel="noopener noreferrer"' : ''} class="resource-link">
            Access ${item.title} <i class="fas fa-external-link-alt"></i>
          </a>
        `;
        
        resourcesGrid.appendChild(resourceCard);
      });
    }
  }

  updateUpcomingSection(upcoming) {
    const section = document.querySelector('#upcoming');
    if (!section) return;

    const title = section.querySelector('h2');
    if (title) {
      title.textContent = upcoming.title;
    }

    const description = section.querySelector('.section-description');
    if (description) {
      description.textContent = upcoming.description;
    }

    // Update upcoming items
    const upcomingGrid = section.querySelector('.upcoming-grid');
    if (upcomingGrid && upcoming.items) {
      // Add items to existing grid
      upcoming.items.forEach(item => {
        const courseCard = document.createElement('div');
        courseCard.className = 'course-card';
        
        courseCard.innerHTML = `
          <div class="course-card-header">
            <div class="course-category" style="background-color: ${item.categoryColor}; color: white;">
              ${item.category}
            </div>
            <div class="upcoming-badge">${item.badge}</div>
          </div>
          <div class="course-content">
            <h3 class="course-title">${item.title}</h3>
            <p class="course-description">${item.description}</p>
          </div>
        `;
        
        upcomingGrid.appendChild(courseCard);
      });
    }
  }

  updateSectionTitles(sections) {
    // Update all section titles and descriptions
    Object.keys(sections).forEach(sectionKey => {
      const section = sections[sectionKey];
      if (section.title || section.description) {
        const sectionElement = document.querySelector(`#${sectionKey.replace(/([A-Z])/g, '-$1').toLowerCase()}`);
        if (sectionElement) {
          const titleElement = sectionElement.querySelector('h2');
          const descElement = sectionElement.querySelector('.section-description');
          
          if (titleElement && section.title) {
            titleElement.textContent = section.title;
          }
          if (descElement && section.description) {
            descElement.textContent = section.description;
          }
        }
      }
    });
  }

  // ===== FOOTER =====
  updateFooter() {
    if (!this.isLoaded || !this.config.footer) return;

    const { footer } = this.config;
    const footerElement = document.querySelector('.footer');
    
    if (!footerElement) return;

    // Clear existing footer content
    footerElement.innerHTML = '';

    // Create footer content container
    const container = document.createElement('div');
    container.className = 'container';

    // Create footer sections
    if (footer.sections) {
      const footerContent = document.createElement('div');
      footerContent.className = 'footer-content';
      
      footer.sections.forEach(section => {
        const sectionDiv = document.createElement('div');
        sectionDiv.className = 'footer-section';
        
        const title = document.createElement('h4');
        title.textContent = section.title;
        sectionDiv.appendChild(title);
        
        section.links.forEach(link => {
          const a = document.createElement('a');
          a.href = link.href;
          a.textContent = link.text;
          
          if (link.external) {
            a.target = '_blank';
            a.rel = 'noopener noreferrer';
          }
          
          const p = document.createElement('p');
          p.appendChild(a);
          sectionDiv.appendChild(p);
        });
        
        footerContent.appendChild(sectionDiv);
      });
      
      container.appendChild(footerContent);
    }

    // Create footer bottom section
    if (footer.bottomSection) {
      const footerBottom = document.createElement('div');
      footerBottom.className = 'footer-bottom';
      
      const copyright = document.createElement('p');
      copyright.textContent = footer.bottomSection.copyrightText;
      footerBottom.appendChild(copyright);
      
      if (footer.bottomSection.licenseInfo && footer.bottomSection.licenseInfo.enabled) {
        const license = document.createElement('p');
        const licenseLink = document.createElement('a');
        licenseLink.href = footer.bottomSection.licenseInfo.url;
        licenseLink.textContent = footer.bottomSection.licenseInfo.text;
        licenseLink.target = '_blank';
        licenseLink.rel = 'noopener noreferrer';
        license.appendChild(licenseLink);
        footerBottom.appendChild(license);
      }
      
      container.appendChild(footerBottom);
    }

    // Add social media links
    if (footer.socialMedia && footer.socialMedia.enabled) {
      const socialDiv = document.createElement('div');
      socialDiv.className = 'footer-social';
      
      footer.socialMedia.links.forEach(social => {
        const a = document.createElement('a');
        a.href = social.url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        a.innerHTML = `<i class="${social.icon}"></i>`;
        socialDiv.appendChild(a);
      });
      
      container.appendChild(socialDiv);
    }

    footerElement.appendChild(container);
  }

  // ===== AUTHOR SECTION =====
  updateAuthorSection() {
    if (!this.isLoaded || !this.config.author) return;

    const { author } = this.config;
    const authorSection = document.querySelector('#author');
    
    if (!authorSection) return;

    // Update author name
    const nameElement = authorSection.querySelector('.author-content h3');
    if (nameElement) {
      nameElement.textContent = author.name;
    }

    // Update author title
    const titleElement = authorSection.querySelector('.author-content .title');
    if (titleElement) {
      titleElement.textContent = author.title;
    }

    // Update author bio
    const bioElement = authorSection.querySelector('.author-content p');
    if (bioElement) {
      bioElement.textContent = author.bio;
    }

    // Update author photo with fallback
    const photoElement = authorSection.querySelector('.author-photo');
    if (photoElement && author.photoUrl) {
      photoElement.src = author.photoUrl;
      photoElement.alt = `Photo of ${author.name}`;
      
      // Add fallback for broken images
      photoElement.onerror = () => {
        photoElement.style.display = 'none';
        const fallback = document.createElement('div');
        fallback.className = 'author-photo-fallback';
        fallback.style.cssText = `
          width: 120px; height: 120px; border-radius: 50%; 
          background: linear-gradient(135deg, #6366f1, #7c3aed);
          display: flex; align-items: center; justify-content: center;
          color: white; font-size: 36px; font-weight: bold;
        `;
        fallback.textContent = author.photoFallback || 'VR';
        photoElement.parentNode.insertBefore(fallback, photoElement);
      };
    }
  }

  // ===== UPI & SUPPORT =====
  updateSupportFeatures() {
    if (!this.isLoaded) return;

    const { support, site } = this.config;

    // Update UPI ID in copy function
    if (site.upiId) {
      window.copyUPIId = () => {
        navigator.clipboard.writeText(site.upiId).then(() => {
          this.showNotification('UPI ID copied to clipboard!', 'success');
        }).catch(() => {
          // Fallback for older browsers
          const textArea = document.createElement('textarea');
          textArea.value = site.upiId;
          document.body.appendChild(textArea);
          textArea.select();
          document.execCommand('copy');
          document.body.removeChild(textArea);
          this.showNotification('UPI ID copied to clipboard!', 'success');
        });
      };
    }

    // Update support section if it exists
    if (support && support.enabled) {
      const supportSection = document.querySelector('#support');
      if (supportSection) {
        this.updateSupportSection(support);
      }
    }
  }

  updateSupportSection(support) {
    const supportSection = document.querySelector('#support');
    if (!supportSection) return;

    const title = supportSection.querySelector('h2');
    if (title) {
      title.textContent = support.title;
    }

    const description = supportSection.querySelector('.section-description');
    if (description) {
      description.textContent = support.description;
    }

    // Add support methods
    if (support.methods) {
      let methodsContainer = supportSection.querySelector('.support-methods');
      if (!methodsContainer) {
        methodsContainer = document.createElement('div');
        methodsContainer.className = 'support-methods';
        supportSection.appendChild(methodsContainer);
      }

      methodsContainer.innerHTML = '';
      
      support.methods.forEach(method => {
        if (method.enabled) {
          const methodDiv = document.createElement('div');
          methodDiv.className = 'support-method';
          
          if (method.type === 'upi') {
            methodDiv.innerHTML = `
              <h4>${method.displayText}</h4>
              <button onclick="copyUPIId()" class="copy-upi-btn">
                <i class="fas fa-copy"></i> ${method.copyText}
              </button>
            `;
          } else {
            methodDiv.innerHTML = `
              <h4>${method.title}</h4>
              <p>${method.description}</p>
            `;
          }
          
          methodsContainer.appendChild(methodDiv);
        }
      });
    }
  }

  // ===== AUTHENTICATION =====
  updateAuthentication() {
    if (!this.isLoaded || !this.config.features?.authentication) return;

    const { authentication } = this.config.features;

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

    // Update modal titles
    if (this.config.content?.modals) {
      const { modals } = this.config.content;
      
      const loginModal = document.querySelector('#loginModal h2');
      if (loginModal && modals.loginTitle) {
        loginModal.textContent = modals.loginTitle;
      }
      
      const signupModal = document.querySelector('#signupModal h2');
      if (signupModal && modals.signupTitle) {
        signupModal.textContent = modals.signupTitle;
      }
    }
  }

  // ===== THEME & STYLING =====
  updateTheme() {
    if (!this.isLoaded || !this.config.theme) return;

    const { theme } = this.config;

    // Update CSS custom properties
    if (theme.colors) {
      const root = document.documentElement;
      
      Object.entries(theme.colors).forEach(([key, value]) => {
        root.style.setProperty(`--${key}-color`, value);
      });
    }

    // Update font families
    if (theme.fonts) {
      const root = document.documentElement;
      
      Object.entries(theme.fonts).forEach(([key, value]) => {
        root.style.setProperty(`--font-${key}`, value);
      });
    }

    // Update dark mode toggle
    if (this.config.features?.darkMode) {
      this.updateDarkModeToggle();
    }
  }

  updateDarkModeToggle() {
    const { darkMode } = this.config.features;
    
    if (darkMode.enabled) {
      const toggleButton = document.querySelector('.theme-toggle i');
      if (toggleButton && darkMode.toggleIcons) {
        // Set up toggle functionality
        window.toggleTheme = () => {
          const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
          const newTheme = isDark ? 'light' : 'dark';
          
          document.documentElement.setAttribute('data-theme', newTheme);
          localStorage.setItem('theme', newTheme);
          
          // Update icon
          toggleButton.className = newTheme === 'dark' ? 
            darkMode.toggleIcons.dark : darkMode.toggleIcons.light;
        };
        
        // Set initial icon
        const currentTheme = localStorage.getItem('theme') || darkMode.defaultMode;
        toggleButton.className = currentTheme === 'dark' ? 
          darkMode.toggleIcons.dark : darkMode.toggleIcons.light;
      }
    }
  }

  // ===== FEATURES CONTROL =====
  updateFeatures() {
    if (!this.isLoaded || !this.config.features) return;

    const { features } = this.config;

    // Control FAB buttons
    if (features.fabButtons !== undefined) {
      const fabContainer = document.querySelector('.fab-container');
      if (fabContainer) {
        fabContainer.style.display = features.fabButtons.enabled ? 'flex' : 'none';
      }
    }

    // Update notification settings
    if (features.notifications) {
      this.notificationDuration = features.notifications.duration || 3000;
    }
  }

  // ===== UTILITY FUNCTIONS =====
  showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.innerHTML = `
      ${message}
      <button onclick="this.parentElement.remove()">×</button>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
      if (notification.parentElement) {
        notification.remove();
      }
    }, this.notificationDuration || 3000);
  }

  // Get configuration value by path
  getConfig(path) {
    if (!this.isLoaded) return null;
    return path.split('.').reduce((obj, key) => obj && obj[key], this.config);
  }

  // Update specific configuration
  updateConfig(path, value) {
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

  // ===== MAIN INITIALIZATION =====
  async initialize() {
    await this.loadConfig();
    
    if (this.isLoaded) {
      console.log('🚀 Initializing enhanced content manager...');
      
      // Update all content
      this.updateSiteMetadata();
      this.updateNavigation();
      this.updateHeroSection();
      this.updateSections();
      this.updateFooter();
      this.updateAuthorSection();
      this.updateSupportFeatures();
      this.updateAuthentication();
      this.updateTheme();
      this.updateFeatures();
      
      console.log('✅ Enhanced Content Manager initialized successfully');
      console.log('📊 Configuration loaded:', this.config);
    } else {
      console.warn('⚠️ Enhanced Content Manager initialized with default configuration');
    }
  }

  // ===== PUBLIC API =====
  reload() {
    return this.initialize();
  }

  getVersion() {
    return this.config?.version || '1.0.0';
  }

  isFeatureEnabled(feature) {
    return this.getConfig(`features.${feature}`) || false;
  }
}

// Create global instance
const contentManager = new EnhancedContentManager();

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

console.log('✅ Enhanced Content Manager v2.0 loaded successfully!');