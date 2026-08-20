/**
 * ImpactMojo Admin Gate
 * Version: 1.0.0
 * Date: March 16, 2026
 *
 * Protects admin pages behind ADMIN role + ORGANIZATION tier authentication.
 * Only users with profile.role === 'admin' AND
 * profile.subscription_tier === 'organization' can access admin pages.
 *
 * USAGE:
 *   AdminGate.protect({
 *       loadingEl:  document.getElementById('loadingOverlay'),
 *       onReady:    function(user, profile) { ... },
 *       onDenied:   function() { ... }          // optional
 *   });
 *
 * PREREQUISITES:
 *   <script src="js/config.js"></script>
 *   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
 *   <script src="js/auth.js"></script>
 *   <script src="js/admin-gate.js"></script>
 */

(function () {
  'use strict';

  var AdminGate = {

    _protected: false,

    /**
     * Protect a page behind admin authentication.
     *
     * @param {Object} opts
     * @param {HTMLElement}  opts.loadingEl  - overlay element to hide when ready
     * @param {number}       opts.timeoutMs  - safety timeout (default: 8000)
     * @param {Function}     opts.onReady    - callback(user, profile) when admin access granted
     * @param {Function}     opts.onDenied   - optional callback when access denied
     */
    protect: async function (opts) {
      if (this._protected) return;
      this._protected = true;

      var loadingEl = opts.loadingEl || null;
      var timeoutMs = opts.timeoutMs || 8000;
      var onReady   = opts.onReady || function () {};
      var onDenied  = opts.onDenied || null;
      var resolved  = false;

      function succeed(user, profile) {
        if (resolved) return;
        resolved = true;
        clearTimeout(safetyTimer);
        if (loadingEl) loadingEl.style.display = 'none';
        try { onReady(user, profile); } catch (e) {
          console.error('[AdminGate] onReady error:', e);
        }
      }

      function deny(reason) {
        if (resolved) return;
        resolved = true;
        clearTimeout(safetyTimer);
        if (loadingEl) loadingEl.style.display = 'none';
        console.warn('[AdminGate] Access denied:', reason || 'not admin');
        if (onDenied) {
          onDenied(reason);
        } else {
          // Default: redirect to login
          window.location.href = '/login.html';
        }
      }

      function checkAdmin(user, profile) {
        if (!user) { deny('not logged in'); return; }
        if (!profile) {
          // Profile may still be loading (slow network / token refresh).
          // Retry once with a fresh fetch before denying.
          console.warn('[AdminGate] No profile yet — retrying fetch...');
          ImpactMojoAuth._profileFetchPromise = null;
          ImpactMojoAuth._lastProfileFetchTime = 0;
          ImpactMojoAuth.fetchProfile().then(function () {
            if (resolved) return;
            var p = ImpactMojoAuth.profile;
            if (!p) { deny('no profile after retry'); return; }
            if (p.role !== 'admin') { deny('role is ' + p.role); return; }
            if (p.subscription_tier !== 'organization') {
              deny('tier is ' + (p.subscription_tier || 'none') + ' (organization required)');
              return;
            }
            succeed(user, p);
          }).catch(function () { deny('profile fetch failed'); });
          return;
        }
        if (profile.role !== 'admin') {
          deny('role is ' + profile.role);
          return;
        }
        if (profile.subscription_tier !== 'organization') {
          deny('tier is ' + (profile.subscription_tier || 'none') + ' (organization required)');
          return;
        }
        succeed(user, profile);
      }

      // Safety timeout
      var safetyTimer = setTimeout(async function () {
        if (resolved) return;
        console.warn('[AdminGate] Safety timeout — attempting fallback');
        try {
          var session = await ImpactMojoAuth.getSession();
          if (session && session.user) {
            ImpactMojoAuth.user = session.user;
            if (!ImpactMojoAuth.profile) {
              await ImpactMojoAuth.fetchProfile();
            }
            checkAdmin(ImpactMojoAuth.user, ImpactMojoAuth.profile);
            return;
          }
        } catch (_) {}
        deny('timeout — no session');
      }, timeoutMs);

      // Listen for auth state changes
      window.addEventListener('authStateChanged', async function handler(e) {
        if (resolved) return;
        if (!ImpactMojoAuth.isAuthReady) return;
        if (e.detail && e.detail.isLoggedIn) {
          // Ensure profile is loaded before checking admin role
          if (!ImpactMojoAuth.profile || !ImpactMojoAuth.profile.role) {
            try { await ImpactMojoAuth.fetchProfile(); } catch (_) {}
          }
          checkAdmin(ImpactMojoAuth.user, ImpactMojoAuth.profile);
        }
      });

      // Main flow
      try {
        await ImpactMojoAuth.init();
        await ImpactMojoAuth.waitForAuthReady();
      } catch (e) {
        console.error('[AdminGate] Auth init failed:', e);
      }

      if (resolved) return;
      clearTimeout(safetyTimer);

      if (ImpactMojoAuth.isLoggedIn()) {
        // Re-fetch profile to get latest role
        try { await ImpactMojoAuth.fetchProfile(); } catch (_) {}
        checkAdmin(ImpactMojoAuth.user, ImpactMojoAuth.profile);
      } else {
        // Fallback: check Supabase directly
        try {
          var session = await ImpactMojoAuth.getSession();
          if (session && session.user) {
            ImpactMojoAuth.user = session.user;
            try { await ImpactMojoAuth.fetchProfile(); } catch (_) {}
            checkAdmin(ImpactMojoAuth.user, ImpactMojoAuth.profile);
            return;
          }
        } catch (_) {}
        deny('not logged in');
      }
    },

    /**
     * Quick check if current user is admin (non-blocking, uses cached profile).
     * @returns {boolean}
     */
    isAdmin: function () {
      return !!(
        ImpactMojoAuth.profile &&
        ImpactMojoAuth.profile.role === 'admin' &&
        ImpactMojoAuth.profile.subscription_tier === 'organization'
      );
    }
  };

  window.AdminGate = AdminGate;
})();
