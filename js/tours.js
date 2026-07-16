/**
 * ImpactMojo Product Tours (Intro.js)
 * Provides guided walkthroughs for first-time visitors on major pages.
 * Tours auto-start once per page (tracked via localStorage).
 */

(function () {
  'use strict';

  var STORAGE_PREFIX = 'impactmojo_tour_seen_';

  function hasSeenTour(page) {
    try { return localStorage.getItem(STORAGE_PREFIX + page) === '1'; }
    catch (e) { return true; }
  }

  function markTourSeen(page) {
    try { localStorage.setItem(STORAGE_PREFIX + page, '1'); }
    catch (e) { /* silent */ }
  }

  /**
   * Open the parent dropdown for a step's element so Intro.js can see it.
   * Returns true if a dropdown was opened, false otherwise.
   */
  function ensureDropdownVisible(selector) {
    if (!selector) return false;
    var el = document.querySelector(selector);
    if (!el) return false;

    // If the element is inside a .dropdown-menu, force-open the parent .has-dropdown
    var dropdownMenu = el.closest('.dropdown-menu');
    if (dropdownMenu) {
      var parentLi = dropdownMenu.closest('li.has-dropdown');
      if (parentLi) {
        // `.open` is the nav's own reveal class (releases max-height and the
        // specials-grouped grid layout); `.tour-dropdown-open` adds the tour
        // z-index overrides on top so the menu sits above the Intro.js overlay.
        parentLi.classList.add('tour-dropdown-open', 'open');
        return true;
      }
    }
    return false;
  }

  /** Close all tour-opened dropdowns */
  function closeAllTourDropdowns() {
    document.querySelectorAll('.tour-dropdown-open').forEach(function (el) {
      el.classList.remove('tour-dropdown-open', 'open');
    });
  }

  function startTour(page, steps) {
    if (typeof introJs === 'undefined') return;

    // Add tour-active class for CSS hooks
    document.body.classList.add('introjs-active-tour');

    var filtered = steps.filter(function (s) {
      if (!s.element) return true;
      // Temporarily open dropdown to check if element exists
      ensureDropdownVisible(s.element);
      var exists = !!document.querySelector(s.element);
      closeAllTourDropdowns();
      return exists;
    });

    if (filtered.length < 2) {
      document.body.classList.remove('introjs-active-tour');
      return;
    }

    var tour = introJs.tour();
    tour.setOptions({
      steps: filtered,
      showProgress: true,
      showBullets: false,
      exitOnOverlayClick: true,
      disableInteraction: false,
      scrollToElement: true,
      scrollPadding: 80,
      nextLabel: 'Next →',
      prevLabel: '← Back',
      doneLabel: 'Done ✓',
      skipLabel: '×',
      tooltipClass: 'impactmojo-tour',
      highlightClass: 'impactmojo-highlight'
    });

    // Before each step: open the dropdown if needed
    tour.onbeforechange(function (targetEl) {
      closeAllTourDropdowns();
      if (targetEl) {
        var dropdownMenu = targetEl.closest('.dropdown-menu');
        if (dropdownMenu) {
          var parentLi = dropdownMenu.closest('li.has-dropdown');
          if (parentLi) {
            parentLi.classList.add('tour-dropdown-open', 'open');
          }
        }
      }
    });

    function cleanup() {
      markTourSeen(page);
      closeAllTourDropdowns();
      document.body.classList.remove('introjs-active-tour');
    }

    tour.oncomplete(cleanup);
    tour.onexit(cleanup);

    tour.start();
  }

  // ── Page-specific tour definitions ────────────────────────────────

  var TOURS = {
    index: [
      { intro: '<strong>Welcome to ImpactMojo!</strong><br>A free learning platform for MEAL, development economics, and impact research. Let us show you around.' },
      { element: '#navLinks', intro: '<strong>Navigation Bar</strong><br>Everything is organized under these menus — courses, labs, games, data tools, and more.' },
      { element: '#nav-learn', intro: '<strong>Learn</strong><br>Open this menu for 68 free Courses, hands-on Labs, and learning Games.' },
      { element: '#nav-courses', intro: '<strong>Courses</strong><br>68 free courses (17 flagship + 51 foundational) covering econometrics, gender studies, MEL frameworks, and more.' },
      { element: '#nav-labs', intro: '<strong>Labs</strong><br>Hands-on interactive tools — build a Theory of Change, design MEL frameworks, and more.' },
      { element: '#nav-games', intro: '<strong>Games</strong><br>Learn behavioral economics, game theory, and policy concepts through play.' },
      { element: '#nav-specials', intro: '<strong>Explore</strong><br>The Game Library, reference tools (Dataverse, ImpactLex), Book Companions, Deep Dives, the Research to Action poster series, Dojos, and more.' },
      { element: '#nav-dataverse', intro: '<strong>Dataverse</strong><br>321 curated data tools, APIs, and datasets for development research.' },
      { element: '.theme-selector', intro: '<strong>Theme</strong><br>Switch between light, dark, and system themes.' },
      { element: '#pro-studio', intro: '<strong>Pro Studio</strong><br>Professional-grade tools like VaniScribe AI, Code Convert Pro, and Qual Insights Lab.' }
    ]
    // Tours run on the homepage only. Do not add per-page tours here.
  };

  // ── Detect current page and auto-start tour ───────────────────────

  function detectPage() {
    var path = window.location.pathname.replace(/\.html$/, '').replace(/^\//, '') || 'index';
    if (path === '' || path === 'home') path = 'index';
    return path;
  }

  function init() {
    // Skip auto-start on mobile — tour is too heavy for small screens
    if (window.innerWidth <= 768) return;

    var page = detectPage();
    if (!TOURS[page]) return;
    if (hasSeenTour(page)) return;

    // Delay tour start so page fully renders
    setTimeout(function () { startTour(page, TOURS[page]); }, 1500);
  }

  // Expose manual trigger for "Take a Tour" buttons
  window.ImpactMojoTour = {
    start: function (page) {
      page = page || detectPage();
      if (TOURS[page]) startTour(page, TOURS[page]);
    },
    reset: function (page) {
      page = page || detectPage();
      try { localStorage.removeItem(STORAGE_PREFIX + page); }
      catch (e) { /* silent */ }
    },
    resetAll: function () {
      Object.keys(TOURS).forEach(function (p) {
        try { localStorage.removeItem(STORAGE_PREFIX + p); }
        catch (e) { /* silent */ }
      });
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
