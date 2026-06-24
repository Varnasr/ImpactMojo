/**
 * ImpactMojo Premium Resource Launcher
 * Version: 3.0.0
 *
 * Opens premium resources through the server-side access gate.
 *
 * FLOW (secure):
 *   1. User clicks a premium tool.
 *   2. We POST the user's Supabase access token to the `mint-resource-token`
 *      Edge Function, which verifies the session, checks the subscription
 *      tier/status server-side (service role), and — only if allowed — mints
 *      a short-lived (5 min) HS256 JWT scoped to that resource.
 *   3. We open the resource URL with `?token=<jwt>`.
 *   4. The resource site's Netlify Edge Function (`auth-gate.ts`) verifies the
 *      JWT against the shared RESOURCE_TOKEN_SECRET and sets a 24h session
 *      cookie. No valid token → it redirects to /login.
 *
 * This means non-logged-in and non-premium users CANNOT open the tools even
 * if they know the URL — the gate rejects them server-side. The token mint is
 * also tier-checked server-side, so the UI lock is defence-in-depth, not the
 * only guard.
 *
 * Depends on: js/config.js (ImpactMojoConfig), js/auth.js (ImpactMojoAuth,
 *             window.supabaseClient).
 */

(function () {
  'use strict';

  // ── Map resource IDs to their deployment URLs ─────────────────────
  // Knowing these URLs grants no access: each site is gated by auth-gate.ts.
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

  // Resources served from this same origin (/premium-tools/*) are gated by
  // the platform auth layer, not the token gate — no minting needed.
  function isLocalResource(url) {
    return url.charAt(0) === '/';
  }

  function mintEndpoint() {
    var base = (window.ImpactMojoConfig && window.ImpactMojoConfig.SUPABASE_URL) || '';
    return base.replace(/\/$/, '') + '/functions/v1/mint-resource-token';
  }

  function anonKey() {
    return (window.ImpactMojoConfig && window.ImpactMojoConfig.SUPABASE_ANON_KEY) || '';
  }

  // Resolve the current Supabase access token, if any.
  function getAccessToken() {
    try {
      if (window.supabaseClient && window.supabaseClient.auth) {
        return window.supabaseClient.auth.getSession().then(function (res) {
          return (res && res.data && res.data.session && res.data.session.access_token) || null;
        }).catch(function () { return null; });
      }
    } catch (e) { /* ignore */ }
    return Promise.resolve(null);
  }

  function appendToken(url, token) {
    var sep = url.indexOf('?') === -1 ? '?' : '&';
    return url + sep + 'token=' + encodeURIComponent(token);
  }

  function goPremium(reason) {
    window.location.href = '/premium.html' + (reason ? ('?reason=' + reason) : '');
  }

  /**
   * Launch a premium resource through the gate.
   * @param {string} resourceId — one of the keys in RESOURCE_URLS
   */
  function launch(resourceId) {
    var baseUrl = RESOURCE_URLS[resourceId];
    if (!baseUrl) {
      console.error('Unknown resource:', resourceId);
      return;
    }

    // Same-origin premium tools: platform auth-gate handles these; open directly
    // (they live behind /premium-tools/ and are covered by the site's own gating).
    if (isLocalResource(baseUrl)) {
      window.open(baseUrl, '_blank');
      return;
    }

    // Open a blank tab synchronously so the browser doesn't block the popup,
    // then navigate it once we have a token (or close it on failure).
    var newTab = window.open('about:blank', '_blank');

    getAccessToken().then(function (accessToken) {
      if (!accessToken) {
        // Not logged in — the gate would reject anyway. Send to premium page.
        if (newTab) newTab.close();
        goPremium('login');
        return;
      }

      return fetch(mintEndpoint(), {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + accessToken,
          'apikey': anonKey(),
        },
        body: JSON.stringify({ resource: resourceId }),
      }).then(function (resp) {
        return resp.json().then(function (data) { return { status: resp.status, data: data }; });
      }).then(function (r) {
        if (r.status === 200 && r.data && r.data.token) {
          var dest = appendToken(baseUrl, r.data.token);
          if (newTab) { newTab.location.href = dest; }
          else { window.open(dest, '_blank'); }
          return;
        }
        // Denied or error — close the tab and route the user appropriately.
        if (newTab) newTab.close();
        if (r.status === 401) {
          goPremium('login');                 // session invalid/expired
        } else if (r.status === 403) {
          // Tier not allowed or subscription inactive
          goPremium(r.data && r.data.code === 'INACTIVE' ? 'inactive' : 'tier');
        } else if (r.status === 429) {
          alert('Too many requests — please wait a moment and try again.');
        } else {
          console.error('mint-resource-token failed:', r.status, r.data);
          goPremium();
        }
      });
    }).catch(function (err) {
      console.error('Resource launch error:', err);
      if (newTab) newTab.close();
      goPremium();
    });
  }

  // ── Public API ────────────────────────────────────────────────────
  window.ImpactMojoResource = {
    launch: launch,
    RESOURCE_URLS: RESOURCE_URLS,
    version: '3.0.0',
  };

  // ── Auto-intercept clicks on links with data-resource-id ──────────
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[data-resource-id]');
    if (!link) return;

    // If premium.js has locked the parent card, let it handle the click.
    var card = link.closest('[data-locked-tier]');
    if (card) return;

    // If the parent gates on a tier but premium.js hasn't initialised yet,
    // defer (avoids a race that could open before the lock is applied).
    var gatedCard = link.closest('[data-required-tier]');
    if (gatedCard && !gatedCard.classList.contains('premium-unlocked')) return;

    e.preventDefault();
    e.stopPropagation();
    launch(link.dataset.resourceId);
  });
})();
