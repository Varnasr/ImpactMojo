/**
 * ImpactMojo Dynamic Course Content Loader
 * Version 1.0.0 — March 2026
 *
 * Fetches course module content from Supabase edge function instead of
 * rendering static HTML. This prevents forks from redistributing course
 * material — the HTML shells contain only structure, not content.
 *
 * How it works:
 *   1. Detects course ID from URL (/courses/gandhi/ → "gandhi")
 *   2. Calls serve-course-content edge function
 *   3. Injects content_html + quiz_html into each module's placeholder
 *   4. For locked modules (unauthenticated), shows a sign-up prompt
 *
 * Usage: include BEFORE course-progress.js on course pages:
 *   <script src="../../js/config.js"></script>
 *   <script src="../../js/course-loader.js"></script>
 *   <script src="../../js/course-progress.js"></script>
 */

(function () {
  'use strict';

  // ── Config ──────────────────────────────────────────────────────
  var cfg = window.ImpactMojoConfig;
  if (!cfg || !cfg.SUPABASE_URL) return;

  var EDGE_FN_URL = cfg.SUPABASE_URL + '/functions/v1/serve-course-content';

  // ── Detect course ID ────────────────────────────────────────────
  // Map URL slugs to DB course_ids (handles case mismatches)
  var COURSE_ID_MAP = { 'sel': 'SEL' };

  function detectCourseId() {
    var match = window.location.pathname.match(/\/courses\/([^/]+)/);
    if (!match) return null;
    var slug = match[1];
    return COURSE_ID_MAP[slug] || slug;
  }

  var courseId = detectCourseId();
  if (!courseId) return;

  // ── Get auth token if user is logged in ─────────────────────────
  // Prefers the token from Supabase's in-memory session (which may have
  // been refreshed) over the raw localStorage value (which may be stale).
  function getAccessToken() {
    try {
      // Prefer the live client session (token may have been refreshed)
      if (window.supabaseClient) {
        // getSession() is async; we'll handle that in loadContent()
        // For sync fallback, read localStorage
      }
      // Check custom storage key used by auth.js
      var customSession = localStorage.getItem('impactmojo-auth');
      if (customSession) {
        var parsed = JSON.parse(customSession);
        if (parsed && parsed.access_token) return parsed.access_token;
      }
    } catch (e) { /* ignore */ }
    return null;
  }

  // Async version that gets the freshest token
  async function getFreshAccessToken() {
    try {
      if (window.supabaseClient) {
        var result = await window.supabaseClient.auth.getSession();
        if (result?.data?.session?.access_token) {
          return result.data.session.access_token;
        }
      }
    } catch (e) { /* fall through to sync method */ }
    return getAccessToken();
  }

  // ── Loading skeleton ────────────────────────────────────────────
  function showLoading() {
    var placeholders = document.querySelectorAll('.module-content-placeholder');
    for (var i = 0; i < placeholders.length; i++) {
      placeholders[i].innerHTML =
        '<div class="content-loading" style="padding:2rem;text-align:center;">' +
        '<div style="width:40px;height:40px;border:3px solid var(--border-color,#e2e8f0);border-top-color:var(--color-primary,#4F46E5);border-radius:50%;animation:spin 0.8s linear infinite;margin:0 auto 1rem;"></div>' +
        '<p style="color:var(--text-muted,#94A3B8);font-size:0.9rem;">Loading course content...</p>' +
        '</div>';
    }
  }

  // ── Locked module overlay ───────────────────────────────────────
  function renderLockedModule(placeholder, mod) {
    placeholder.innerHTML =
      '<div class="module-locked" style="padding:3rem 2rem;text-align:center;background:var(--bg-secondary,#f8fafc);border-radius:12px;border:1px dashed var(--border-color,#e2e8f0);">' +
      '<div style="margin-bottom:1rem;"><img src="https://cdn.jsdelivr.net/npm/sargam-icons@1.6.7/Icons/Line/si_Lock.svg" alt="Locked" style="width:48px;height:48px;opacity:0.6;filter:brightness(0) saturate(100%) invert(48%) sepia(95%) saturate(1012%) hue-rotate(178deg) brightness(97%) contrast(97%);"></div>' +
      '<h3 style="font-family:var(--font-display,Inter,sans-serif);margin-bottom:0.5rem;color:var(--text-primary,#1e293b);">Sign in to continue</h3>' +
      '<p style="color:var(--text-secondary,#475569);max-width:400px;margin:0 auto 1.5rem;">Create a free ImpactMojo account to access all course modules, track your progress, and earn certificates.</p>' +
      '<a href="/login.html" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.75rem 1.5rem;background:var(--color-primary,#4F46E5);color:#fff;border-radius:8px;font-weight:600;text-decoration:none;transition:transform 0.2s;">Sign up free →</a>' +
      '</div>';
  }

  // ── Error state ─────────────────────────────────────────────────
  function showError() {
    var placeholders = document.querySelectorAll('.module-content-placeholder');
    for (var i = 0; i < placeholders.length; i++) {
      placeholders[i].innerHTML =
        '<div style="padding:2rem;text-align:center;color:var(--text-muted,#94A3B8);">' +
        '<p>Unable to load course content. Please refresh the page.</p>' +
        '<button onclick="window.location.reload()" style="margin-top:1rem;padding:0.5rem 1rem;background:var(--color-primary,#4F46E5);color:#fff;border:none;border-radius:6px;cursor:pointer;">Retry</button>' +
        '</div>';
    }
  }

  // ── Inject content into module placeholders ─────────────────────
  function injectContent(modules) {
    for (var i = 0; i < modules.length; i++) {
      var mod = modules[i];
      var placeholder = document.getElementById('module' + mod.module_number + '-content');

      if (!placeholder) continue;

      if (mod.locked) {
        renderLockedModule(placeholder, mod);
        continue;
      }

      // Inject the actual HTML content
      var html = '';
      if (mod.content_html) html += mod.content_html;
      if (mod.quiz_html) html += mod.quiz_html;
      placeholder.innerHTML = html;
    }

    // Re-initialize quiz handlers (course-progress.js will pick these up)
    if (window.ImpactMojoCourseProgress && window.ImpactMojoCourseProgress.reinit) {
      window.ImpactMojoCourseProgress.reinit();
    }

    // Dispatch event so other scripts know content is ready
    document.dispatchEvent(new CustomEvent('courseContentLoaded', {
      detail: { courseId: courseId }
    }));
  }

  // ── Fetch content from edge function ────────────────────────────
  async function loadContent() {
    showLoading();

    // Wait for auth to be ready so we have a fresh (refreshed) token
    if (typeof window.ImpactMojoAuth !== 'undefined' && typeof window.ImpactMojoAuth.waitForAuthReady === 'function') {
      try { await window.ImpactMojoAuth.waitForAuthReady(); } catch (_) {}
    }

    // Force a session refresh to get a non-expired access token.
    // The edge function calls getUser() to verify — expired tokens are rejected,
    // and modules 2+ get locked. Always refresh to ensure a valid token.
    var token = null;
    try {
      if (window.supabaseClient) {
        var refreshResult = await window.supabaseClient.auth.refreshSession();
        if (refreshResult?.data?.session?.access_token) {
          token = refreshResult.data.session.access_token;
          console.log('[CourseLoader] Using refreshed token');
        } else {
          // Refresh failed — try cached session as fallback
          var sessionResult = await window.supabaseClient.auth.getSession();
          if (sessionResult?.data?.session?.access_token) {
            token = sessionResult.data.session.access_token;
            console.log('[CourseLoader] Using cached session token (refresh failed)');
          }
        }
      }
    } catch (e) {
      console.warn('[CourseLoader] Session refresh failed:', e);
    }

    // Fallback to localStorage
    if (!token) token = getAccessToken();

    console.log('[CourseLoader] Fetching with token:', token ? 'yes (' + token.substring(0, 20) + '...)' : 'anon');

    var headers = {
      'Content-Type': 'application/json',
      'apikey': cfg.SUPABASE_ANON_KEY,
      'Authorization': 'Bearer ' + (token || cfg.SUPABASE_ANON_KEY),
    };

    // Headers that drop the (possibly stale) user token and use the anon key.
    // The edge function rejects an expired/invalid JWT with a 401 for the WHOLE
    // request — it does NOT fall back to serving public content — so without
    // this a returning user with a stale session would see no content at all.
    var anonHeaders = {
      'Content-Type': 'application/json',
      'apikey': cfg.SUPABASE_ANON_KEY,
      'Authorization': 'Bearer ' + cfg.SUPABASE_ANON_KEY,
    };

    // Fetch with a per-attempt timeout and one automatic retry, so a hung
    // edge-function request can no longer leave the page spinning forever.
    var MAX_ATTEMPTS = 2;
    var TIMEOUT_MS = 12000;

    function attempt(n, anonOnly) {
      var controller = new AbortController();
      var timer = setTimeout(function () { controller.abort(); }, TIMEOUT_MS);

      fetch(EDGE_FN_URL, {
        method: 'POST',
        headers: anonOnly ? anonHeaders : headers,
        body: JSON.stringify({ course_id: courseId }),
        signal: controller.signal,
      })
        .then(function (res) {
          clearTimeout(timer);
          // A stale/expired user token makes the function 401 the entire
          // request. Retry once as anonymous so public modules still load
          // (re-logging in restores access to the gated modules).
          if (res.status === 401 && !anonOnly && token) {
            console.warn('[CourseLoader] 401 with user token — retrying anonymously');
            attempt(n, true);
            return null;
          }
          if (!res.ok) throw new Error('HTTP ' + res.status);
          return res.json();
        })
        .then(function (data) {
          if (!data) return; // handed off to the anonymous retry above
          if (data.modules && data.modules.length > 0) {
            injectContent(data.modules);
          } else {
            throw new Error('empty payload');
          }
        })
        .catch(function (err) {
          clearTimeout(timer);
          if (n < MAX_ATTEMPTS) {
            console.warn('[CourseLoader] attempt ' + n + ' failed (' + err.message + '), retrying…');
            setTimeout(function () { attempt(n + 1, anonOnly); }, 1500 * n);
          } else {
            console.error('[CourseLoader] Failed to load content:', err);
            showError();
          }
        });
    }

    attempt(1, false);
  }

  // ── CSS for spinner animation ───────────────────────────────────
  var style = document.createElement('style');
  style.textContent = '@keyframes spin { to { transform: rotate(360deg); } }';
  document.head.appendChild(style);

  // ── Run on DOM ready ────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadContent);
  } else {
    loadContent();
  }
})();
