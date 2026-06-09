/**
 * ImpactMojo Premium Resource Launcher
 * Version: 2.1.0
 *
 * Opens premium resources directly for authenticated users.
 * No JWT minting — resource sites are access-gated at the platform level
 * (via premium.js tier checks), not at the resource site level.
 *
 * Usage:
 *   <button onclick="ImpactMojoResource.launch('vaniscribe')">Open VaniScribe</button>
 *
 * Depends on: js/auth.js (provides `ImpactMojoAuth`)
 */

(function () {
  'use strict';

  // ── Map resource IDs to their deployment URLs ─────────────────────
  var RESOURCE_URLS = {
    // Practitioner tier
    'rq-builder':         '/premium-tools/rq-builder.html',
    // Professional tier
    'advisory-board-pro': '/premium-tools/advisory-board-pro.html',
    'vaniscribe':         'https://vaniscribe.netlify.app/',
    'devdata-practice':   'https://impactmojo-devdata-pro.netlify.app/',
    'viz-cookbook':        'https://impactmojo-devdata-pro.netlify.app/charts.html',
    'devecon-toolkit':    'https://impactmojo-devecon-toolkit.netlify.app/',
    'field-notes-pro':    'https://impactmojo-field-notes-pro.netlify.app/',
    'qual-insights-lab':  '/premium-tools/qual-insights-lab.html',
    'code-converter-pro': '/premium-tools/code-converter-pro.html',
    // Workshop Pro templates
    'toc-workshop-pro':   'https://impactmojo-workshop-pro.netlify.app/toc-pro.html',
    'logframe-pro':       'https://impactmojo-workshop-pro.netlify.app/logframe-pro.html',
    'chart-selector-pro': 'https://impactmojo-workshop-pro.netlify.app/chart-selector-pro.html',
    'stakeholder-pro':    'https://impactmojo-workshop-pro.netlify.app/stakeholder-pro.html',
    'empathy-pro':        'https://impactmojo-workshop-pro.netlify.app/empathy-pro.html',
    'policy-canvas-pro':  'https://impactmojo-workshop-pro.netlify.app/policy-canvas-pro.html',
    'ai-canvas-pro':      'https://impactmojo-workshop-pro.netlify.app/ai-canvas-pro.html',
  };

  // Check if there is a Supabase session in localStorage (fallback for
  // transient SIGNED_OUT states during token refresh)
  function hasSupabaseSession() {
    try {
      var keys = Object.keys(localStorage);
      for (var i = 0; i < keys.length; i++) {
        if (keys[i].indexOf('impactmojo-auth') !== -1 ||
            keys[i].indexOf('supabase.auth.token') !== -1 ||
            (keys[i].indexOf('sb-') !== -1 && keys[i].indexOf('-auth-token') !== -1)) {
          var val = JSON.parse(localStorage.getItem(keys[i]));
          if (val && (val.access_token || (val.currentSession && val.currentSession.access_token))) {
            return true;
          }
        }
      }
    } catch (e) { /* ignore */ }
    return false;
  }

  /**
   * Launch a premium resource.
   * Waits for auth to initialise before checking login state.
   * Falls back to Supabase session check to prevent redirect loops
   * caused by transient auth states during token refresh.
   * @param {string} resourceId  — one of the keys in RESOURCE_URLS
   */
  function launch(resourceId) {
    // 1. Resolve the resource URL
    var baseUrl = RESOURCE_URLS[resourceId];
    if (!baseUrl) {
      console.error('Unknown resource:', resourceId);
      return;
    }

    // 2. Auth may still be initialising — wait for it
    if (typeof ImpactMojoAuth === 'undefined') {
      // Fallback: if Supabase has a session, open the resource directly
      if (hasSupabaseSession()) {
        window.open(baseUrl, '_blank');
        return;
      }
      // No session at all — send to premium page (not login) so user
      // understands this is a premium feature, not just an auth issue
      window.location.href = '/premium.html';
      return;
    }

    // Open a blank tab synchronously (must be in the click handler
    // or browsers will block the popup)
    var newTab = window.open('about:blank', '_blank');

    ImpactMojoAuth.waitForAuthReady().then(function () {
      if (!ImpactMojoAuth.isLoggedIn()) {
        // Double-check: Supabase may still have a valid session even if
        // ImpactMojoAuth missed it during a token refresh race
        if (hasSupabaseSession()) {
          if (newTab) {
            newTab.location.href = baseUrl;
          } else {
            window.open(baseUrl, '_blank');
          }
          return;
        }
        // Not logged in — send to premium page instead of login to avoid
        // redirect loops and to communicate this is a premium feature
        if (newTab) newTab.close();
        window.location.href = '/premium.html';
        return;
      }
      // 3. Navigate the already-open tab to the resource
      if (newTab) {
        newTab.location.href = baseUrl;
      } else {
        window.open(baseUrl, '_blank');
      }
    });
  }

  // ── Public API ────────────────────────────────────────────────────
  window.ImpactMojoResource = {
    launch: launch,
    RESOURCE_URLS: RESOURCE_URLS,
    version: '2.1.0',
  };

  // ── Auto-intercept clicks on links with data-resource-id ─────────
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[data-resource-id]');
    if (!link) return;

    // If premium.js has locked the parent card, let it handle the click
    var card = link.closest('[data-locked-tier]');
    if (card) return;

    // If the parent requires a premium tier but premium.js hasn't finished
    // initializing yet (no data-locked-tier set), defer the click to avoid
    // a race condition that redirects unauthenticated users to login
    var gatedCard = link.closest('[data-required-tier]');
    if (gatedCard && !gatedCard.classList.contains('premium-unlocked')) return;

    e.preventDefault();
    e.stopPropagation();

    // If premium.js has already verified the user's tier and unlocked the
    // card, open the resource directly — no need for a second auth check
    // which can fail due to auth timing issues and redirect to login
    if (gatedCard && gatedCard.classList.contains('premium-unlocked')) {
      var directUrl = RESOURCE_URLS[link.dataset.resourceId];
      if (directUrl) {
        window.open(directUrl, '_blank');
        return;
      }
    }

    launch(link.dataset.resourceId);
  });
})();
