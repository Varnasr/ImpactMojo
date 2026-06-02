/**
 * ImpactMojo State Manager
 * Version: 1.0.0
 * Date: March 16, 2026
 *
 * Single source of truth for ALL localStorage keys, data formats,
 * and read/write operations.  Every other script MUST go through
 * this module instead of touching localStorage directly.
 *
 * WHY THIS EXISTS:
 *   Scattered localStorage access caused key-name drift (camelCase vs
 *   snake_case), format mismatches (array vs object), and silent data
 *   loss.  Centralising here prevents that entire class of bugs.
 *
 * USAGE:
 *   <script src="js/state-manager.js"></script>   // load first
 *   var bookmarks = IMState.bookmarks.get();
 *   IMState.bookmarks.set([...]);
 *   IMState.bookmarks.clear();
 */

(function () {
  'use strict';

  // =========================================================================
  // KEY REGISTRY — the ONLY place localStorage key strings are defined
  // =========================================================================

  var KEYS = Object.freeze({
    // Core user data (synced to Supabase via auth.js)
    BOOKMARKS:       'impactmojo_bookmarks',
    NOTES:           'impactmojo_notes',
    COMPARE:         'impactmojo_compare',
    STREAK:          'impactmojo_streak',
    ANALYTICS:       'impactmojo_analytics',
    LAST_SYNC:       'impactmojo_last_sync',

    // Course progress (per-course, dynamic suffix)
    COURSE_PROGRESS_PREFIX: 'impactmojo_course_progress_',

    // Assessment progress (per-course, dynamic suffix)
    ASSESSMENT_PREFIX: 'impactmojo_assessment_',

    // Learning pathways
    PATHWAY_STATE:   'impactmojo_pathway_state',

    // Challenges
    CHALLENGE_SUBMISSIONS: 'impactmojo_challenge_submissions',
    CHALLENGE_DRAFTS:      'impactmojo_challenge_drafts',

    // Premium / upgrade
    PREMIUM_DISMISSED: 'impactmojo_premium_dismissed',
    UPGRADE_PROMPTS:   'impactmojo_upgrade_prompts',

    // Onboarding
    TOUR_COMPLETED:  'impactmojo_tour_completed',

    // UI / preferences
    THEME:           'theme',
    LANG:            'impactmojo_lang',
    SITE_VERSION:    'imx_site_version',
    COOKIE_CONSENT:  'cookieConsent',

    // BCT repository (separate namespace)
    BCT_BOOKMARKS:   'impactmojo_bct_bookmarks',
    BCT_NOTES:       'impactmojo_bct_notes',
    BCT_COMPARE:     'impactmojo_bct_compare',

    // Game agent sessions
    GAME_SESSION_PREFIX: 'impactmojo_game_session_',
    GAME_HISTORY:        'impactmojo_game_history',

    // Org dashboard
    COHORTS_PREFIX:  'impactmojo_cohorts_',

    // Quiz tracking
    TRACK_QUIZ:      'impactmojoTrackQuiz',

    // Cached auth profile (persists across page navigations)
    CACHED_PROFILE:  'impactmojo_cached_profile'
  });

  // =========================================================================
  // DEFAULTS — canonical empty values for each data type
  // =========================================================================

  var DEFAULTS = {
    BOOKMARKS:    [],
    NOTES:        [],
    COMPARE:      [],
    STREAK:       { currentStreak: 0, longestStreak: 0, lastVisit: null, totalVisits: 0 },
    ANALYTICS:    {},
    COURSE_PROGRESS: { courseId: '', completed: [], percentage: 0, totalModules: 0, updatedAt: null }
  };

  // =========================================================================
  // SAFE READ / WRITE HELPERS
  // =========================================================================

  function safeGet(key, fallback) {
    try {
      var raw = localStorage.getItem(key);
      if (raw === null) return fallback;
      return JSON.parse(raw);
    } catch (_) {
      return fallback;
    }
  }

  function safeSet(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (e) {
      console.error('[IMState] localStorage write failed for', key, e);
      return false;
    }
  }

  function safeRemove(key) {
    try {
      localStorage.removeItem(key);
    } catch (_) { /* ignore */ }
  }

  function safeGetString(key, fallback) {
    try {
      return localStorage.getItem(key) || fallback;
    } catch (_) {
      return fallback;
    }
  }

  function safeSetString(key, value) {
    try {
      localStorage.setItem(key, value);
      return true;
    } catch (e) {
      console.error('[IMState] localStorage write failed for', key, e);
      return false;
    }
  }

  // =========================================================================
  // PUBLIC API
  // =========================================================================

  var IMState = {

    // Expose key registry (read-only) for migration / debugging
    KEYS: KEYS,
    DEFAULTS: DEFAULTS,

    // ------- Core synced data -------

    bookmarks: {
      get: function () { return safeGet(KEYS.BOOKMARKS, []); },
      set: function (arr) { return safeSet(KEYS.BOOKMARKS, arr); },
      clear: function () { safeRemove(KEYS.BOOKMARKS); }
    },

    notes: {
      get: function () { return safeGet(KEYS.NOTES, []); },
      set: function (arr) { return safeSet(KEYS.NOTES, arr); },
      clear: function () { safeRemove(KEYS.NOTES); }
    },

    compare: {
      get: function () { return safeGet(KEYS.COMPARE, []); },
      set: function (arr) { return safeSet(KEYS.COMPARE, arr); },
      clear: function () { safeRemove(KEYS.COMPARE); }
    },

    streak: {
      get: function () {
        var raw = safeGet(KEYS.STREAK, null);
        if (!raw) return Object.assign({}, DEFAULTS.STREAK);
        // Normalise old field names (current → currentStreak, etc.)
        return {
          currentStreak: raw.currentStreak || raw.current || 0,
          longestStreak: raw.longestStreak || raw.longest || 0,
          lastVisit: raw.lastVisit || raw.lastDate || null,
          totalVisits: raw.totalVisits || 0
        };
      },
      set: function (obj) { return safeSet(KEYS.STREAK, obj); },
      clear: function () { safeRemove(KEYS.STREAK); }
    },

    analytics: {
      get: function () { return safeGet(KEYS.ANALYTICS, {}); },
      set: function (obj) { return safeSet(KEYS.ANALYTICS, obj); },
      clear: function () { safeRemove(KEYS.ANALYTICS); }
    },

    lastSync: {
      get: function () {
        var ts = safeGetString(KEYS.LAST_SYNC, null);
        return ts ? new Date(ts) : null;
      },
      set: function (date) {
        var iso = (date instanceof Date) ? date.toISOString() : new Date().toISOString();
        return safeSetString(KEYS.LAST_SYNC, iso);
      },
      clear: function () { safeRemove(KEYS.LAST_SYNC); }
    },

    // ------- Course progress (per-course) -------

    courseProgress: {
      /** Get progress for a single course */
      getOne: function (courseId) {
        return safeGet(KEYS.COURSE_PROGRESS_PREFIX + courseId, null);
      },
      /** Set progress for a single course */
      setOne: function (courseId, data) {
        return safeSet(KEYS.COURSE_PROGRESS_PREFIX + courseId, data);
      },
      /** Get a flat map { courseId: percentage } for ALL courses */
      getAllPercentages: function () {
        var result = {};
        try {
          for (var i = 0; i < localStorage.length; i++) {
            var key = localStorage.key(i);
            if (key && key.indexOf(KEYS.COURSE_PROGRESS_PREFIX) === 0) {
              var id = key.slice(KEYS.COURSE_PROGRESS_PREFIX.length);
              var data = safeGet(key, {});
              result[id] = data.percentage || 0;
            }
          }
        } catch (_) { /* ignore */ }
        return result;
      },
      /** Remove progress for a single course */
      clearOne: function (courseId) {
        safeRemove(KEYS.COURSE_PROGRESS_PREFIX + courseId);
      }
    },

    // ------- Assessments (per-course) -------

    assessment: {
      get: function (courseId) {
        return safeGet(KEYS.ASSESSMENT_PREFIX + courseId, null);
      },
      set: function (courseId, data) {
        return safeSet(KEYS.ASSESSMENT_PREFIX + courseId, data);
      },
      clear: function (courseId) {
        safeRemove(KEYS.ASSESSMENT_PREFIX + courseId);
      }
    },

    // ------- Learning pathways -------

    pathwayState: {
      get: function () { return safeGet(KEYS.PATHWAY_STATE, {}); },
      set: function (obj) { return safeSet(KEYS.PATHWAY_STATE, obj); },
      clear: function () { safeRemove(KEYS.PATHWAY_STATE); }
    },

    // ------- Game sessions (AI agent games) -------

    gameSession: {
      /** Get active session for a game */
      get: function (gameId) {
        return safeGet(KEYS.GAME_SESSION_PREFIX + gameId, null);
      },
      /** Save session state (round, history, agent decisions) */
      set: function (gameId, data) {
        return safeSet(KEYS.GAME_SESSION_PREFIX + gameId, data);
      },
      /** Clear session for a game */
      clear: function (gameId) {
        safeRemove(KEYS.GAME_SESSION_PREFIX + gameId);
      }
    },

    gameHistory: {
      /** Get completed game history (array of summaries) */
      get: function () { return safeGet(KEYS.GAME_HISTORY, []); },
      /** Add a completed game to history */
      add: function (entry) {
        var hist = safeGet(KEYS.GAME_HISTORY, []);
        hist.push(entry);
        // Keep last 50 games
        if (hist.length > 50) hist = hist.slice(-50);
        return safeSet(KEYS.GAME_HISTORY, hist);
      },
      clear: function () { safeRemove(KEYS.GAME_HISTORY); }
    },

    // ------- Challenges -------

    challengeSubmissions: {
      get: function () { return safeGet(KEYS.CHALLENGE_SUBMISSIONS, {}); },
      set: function (obj) { return safeSet(KEYS.CHALLENGE_SUBMISSIONS, obj); },
      clear: function () { safeRemove(KEYS.CHALLENGE_SUBMISSIONS); }
    },

    challengeDrafts: {
      get: function () { return safeGet(KEYS.CHALLENGE_DRAFTS, {}); },
      set: function (obj) { return safeSet(KEYS.CHALLENGE_DRAFTS, obj); },
      clear: function () { safeRemove(KEYS.CHALLENGE_DRAFTS); }
    },

    // ------- UI / preferences -------

    theme: {
      get: function () { return safeGetString(KEYS.THEME, null); },
      set: function (val) { return safeSetString(KEYS.THEME, val); }
    },

    lang: {
      get: function () { return safeGetString(KEYS.LANG, 'en'); },
      set: function (val) { return safeSetString(KEYS.LANG, val); }
    },

    tourCompleted: {
      get: function () { return safeGetString(KEYS.TOUR_COMPLETED, null) === 'true'; },
      set: function () { return safeSetString(KEYS.TOUR_COMPLETED, 'true'); },
      clear: function () { safeRemove(KEYS.TOUR_COMPLETED); }
    },

    cookieConsent: {
      get: function () { return safeGetString(KEYS.COOKIE_CONSENT, null) === 'true'; },
      set: function () { return safeSetString(KEYS.COOKIE_CONSENT, 'true'); }
    },

    // ------- Premium tracking -------

    upgradePrompts: {
      get: function () { return safeGet(KEYS.UPGRADE_PROMPTS, []); },
      set: function (arr) { return safeSet(KEYS.UPGRADE_PROMPTS, arr); }
    },

    // ------- Cached auth profile -------
    // Persists profile across page navigations so tier is available
    // immediately while a fresh fetchProfile() runs in background.

    cachedProfile: {
      get: function () { return safeGet(KEYS.CACHED_PROFILE, null); },
      set: function (profile) {
        if (!profile) return;
        // Only cache fields needed for instant UI (not sensitive data)
        return safeSet(KEYS.CACHED_PROFILE, {
          id: profile.id,
          display_name: profile.display_name || null,
          full_name: profile.full_name || null,
          email: profile.email || null,
          avatar_url: profile.avatar_url || null,
          subscription_tier: profile.subscription_tier || 'explorer',
          subscription_status: profile.subscription_status || null,
          resource_grants: profile.resource_grants || null,
          organization: profile.organization || null,
          role: profile.role || null,
          cachedAt: new Date().toISOString()
        });
      },
      clear: function () { safeRemove(KEYS.CACHED_PROFILE); }
    },

    // ------- Bulk helpers (used by auth sync) -------

    /**
     * Get all core synced data as a single object.
     * Keys match the Supabase profiles columns.
     */
    getSyncableData: function () {
      return {
        bookmarks:    this.bookmarks.get(),
        notes:        this.notes.get(),
        compare_list: this.compare.get(),
        streak_data:  this.streak.get(),
        progress:     this.analytics.get()
      };
    },

    /**
     * Write core synced data from a single object.
     * Only writes fields that are present (partial update safe).
     */
    setSyncableData: function (data) {
      if (data.bookmarks !== undefined)    this.bookmarks.set(data.bookmarks);
      if (data.notes !== undefined)        this.notes.set(data.notes);
      if (data.compare_list !== undefined) this.compare.set(data.compare_list);
      if (data.streak_data !== undefined)  this.streak.set(data.streak_data);
      if (data.progress !== undefined)     this.analytics.set(data.progress);
    },

    /**
     * Clear ALL core synced data (used by "Clear Local Data" button).
     */
    clearAllSyncedData: function () {
      this.bookmarks.clear();
      this.notes.clear();
      this.compare.clear();
      this.streak.clear();
      this.analytics.clear();
      this.lastSync.clear();
    }
  };

  // Freeze the API surface so other scripts can't overwrite methods
  Object.freeze(IMState.bookmarks);
  Object.freeze(IMState.notes);
  Object.freeze(IMState.compare);
  Object.freeze(IMState.streak);
  Object.freeze(IMState.analytics);
  Object.freeze(IMState.lastSync);
  Object.freeze(IMState.courseProgress);
  Object.freeze(IMState.assessment);
  Object.freeze(IMState.pathwayState);
  Object.freeze(IMState.challengeSubmissions);
  Object.freeze(IMState.challengeDrafts);
  Object.freeze(IMState.gameSession);
  Object.freeze(IMState.gameHistory);
  Object.freeze(IMState.theme);
  Object.freeze(IMState.lang);
  Object.freeze(IMState.tourCompleted);
  Object.freeze(IMState.cookieConsent);
  Object.freeze(IMState.upgradePrompts);
  Object.freeze(IMState.cachedProfile);

  window.IMState = IMState;
})();
