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

  // NOTE: content counts below are scanned by scripts/check-counts.py —
  // keep the "<number> <type>" phrasing when editing.
  var TOURS = {
    index: [
      { intro: '<strong>Welcome to ImpactMojo!</strong><br>Development know-how for South Asia — 70 courses, 135 games and 36 studios, all free, built by practitioners. Here’s a quick lay of the land.' },
      { element: '#nav-learn', intro: '<strong>Learn</strong><br>The heart of the platform: 70 courses (19 flagship + 51 foundational), interactive studios, and practice packs.' },
      { element: '#nav-flagships', intro: '<strong>Flagship courses</strong><br>Semester-depth courses with progress tracking, self-assessments, and free certificates — MEL, development economics, gender studies, causal inference, and more.' },
      { element: '#nav-labs', intro: '<strong>Studios</strong><br>36 studios where you build real artefacts — a Theory of Change, a LogFrame, a sampling plan, a survey instrument.' },
      { element: '#nav-specials', intro: '<strong>Explore</strong><br>The 135-game library, 163 reading companions, 22 deep dives, citation-backed timelines, and daily practice dojos.' },
      { element: '#nav-libraries', intro: '<strong>Libraries &amp; data</strong><br>Reference collections: the Dataverse of data tools, the ImpactLex glossary, NudgeKit behaviour-change techniques, and Indian policy documents.' },
      { element: '.ims-nav-btn', intro: '<strong>Search everything</strong><br>Press <kbd>Ctrl</kbd>+<kbd>K</kbd> anywhere to search across every course, studio, game and companion.' },
      { element: '#quiz', intro: '<strong>Not sure where to start?</strong><br>Six quick questions give you a personal starting path — and the homepage remembers it.' },
      { element: '.theme-selector', intro: '<strong>Theme</strong><br>Light, dark, or follow your device.' },
      { element: '#pro-studio', intro: '<strong>Pro Studio</strong><br>Professional tools for subscribers — and everything you’ve seen so far stays free, forever.' }
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
