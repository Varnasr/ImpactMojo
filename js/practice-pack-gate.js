/**
 * ImpactMojo Practice Pack Paywall Gate
 * Version: 1.0.0
 *
 * Freemium gate for Practice Packs. The first N modules of every pack stay
 * free (the preview / hook); the remaining modules + the auto-built capstone
 * require access. Access is granted by EITHER:
 *
 *   1. A subscription tier at or above `requiredTier` (default: practitioner),
 *      i.e. the existing platform-wide tier gating, OR
 *   2. A standalone per-pack purchase recorded in the profile's
 *      `resource_grants` array (slug match).
 *
 * This is a CLIENT-SIDE freemium teaser gate, not a hard paywall. It reads the
 * cached Supabase profile written by js/auth.js (`impactmojo_cached_profile`)
 * so it works without loading the full auth stack into every pack. Modules 3-4
 * carry little value without the user's own Module 1-2 inputs (which never
 * leave their browser), so casual bypass is low-risk — the real value is the
 * personalised capstone, the subscription, and the optional expert review.
 *
 * USAGE — add to a pack page, AFTER the pack's inline <script> that defines
 * goTab():
 *
 *   <script>window.IM_PACK = {
 *       slug:        'tor-writing',
 *       title:       'Writing a ToR That Gets You Useful Research',
 *       artefact:    'ToR + costing sheet',
 *       freeModules: 2,            // modules 0..1 free; 2+ gated
 *       price:       '₹299',       // standalone per-pack price
 *       requiredTier:'practitioner'
 *   };</script>
 *   <script src="/js/practice-pack-gate.js"></script>
 */
(function () {
  'use strict';

  var PACK = window.IM_PACK || {};
  var CFG = {
    slug:         PACK.slug || (location.pathname.split('/').filter(Boolean).pop() || 'practice-pack'),
    title:        PACK.title || document.title.split('—')[0].split('|')[0].trim() || 'this Practice Pack',
    artefact:     PACK.artefact || 'capstone artefact',
    freeModules:  typeof PACK.freeModules === 'number' ? PACK.freeModules : 2,
    price:        PACK.price || '₹299',
    requiredTier: PACK.requiredTier || 'practitioner',
    tierPrice:    PACK.tierPrice || '₹399/mo',
    review:       PACK.review || '₹999'
  };

  var TIERS = ['explorer', 'practitioner', 'professional', 'organization'];

  // ── Access check ────────────────────────────────────────────────────
  // Reads the cached profile + session that js/auth.js persists on login.
  function hasSession() {
    try {
      var keys = Object.keys(localStorage);
      for (var i = 0; i < keys.length; i++) {
        var k = keys[i];
        if (k.indexOf('impactmojo-auth') !== -1 ||
            k.indexOf('supabase.auth.token') !== -1 ||
            (k.indexOf('sb-') !== -1 && k.indexOf('-auth-token') !== -1)) {
          var v = JSON.parse(localStorage.getItem(k));
          if (v && (v.access_token || (v.currentSession && v.currentSession.access_token))) return true;
        }
      }
    } catch (e) { /* ignore */ }
    return false;
  }

  function cachedProfile() {
    try { return JSON.parse(localStorage.getItem('impactmojo_cached_profile')) || null; }
    catch (e) { return null; }
  }

  function hasAccess() {
    // Live auth, if the full stack happens to be loaded, wins.
    if (window.ImpactMojoAuth && window.ImpactMojoAuth.profile) {
      return evaluate(window.ImpactMojoAuth.profile);
    }
    if (!hasSession()) return false;
    return evaluate(cachedProfile());
  }

  function evaluate(profile) {
    if (!profile) return false;
    var status = profile.subscription_status;
    // Tier path — block only if subscription is explicitly cancelled/expired.
    if (!(status && status !== 'active' && status !== 'trialing')) {
      var have = TIERS.indexOf(profile.subscription_tier || 'explorer');
      var need = TIERS.indexOf(CFG.requiredTier);
      if (need >= 0 && have >= need) return true;
    }
    // Standalone per-pack grant path.
    var grants = profile.resource_grants;
    if (Array.isArray(grants) && grants.indexOf(CFG.slug) !== -1) return true;
    if (grants && typeof grants === 'object' && grants[CFG.slug]) return true;
    return false;
  }

  // ── Styles (uses the pack's own CSS variables so it themes correctly) ─
  function injectStyles() {
    if (document.getElementById('pp-gate-styles')) return;
    var s = document.createElement('style');
    s.id = 'pp-gate-styles';
    s.textContent = [
      '.pp-lock-pill{display:inline-flex;align-items:center;gap:.25rem;margin-left:.35rem;padding:.05rem .35rem;border-radius:6px;font-size:.6rem;font-weight:700;letter-spacing:.3px;text-transform:uppercase;background:rgba(245,158,11,.18);color:var(--warning,#F59E0B);font-family:var(--font-heading,sans-serif)}',
      '.pp-lock-pill svg{width:10px;height:10px}',
      '.pp-gate-backdrop{position:fixed;inset:0;z-index:9998;background:rgba(15,23,42,.72);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);opacity:0;visibility:hidden;transition:opacity .25s;display:flex;align-items:center;justify-content:center;padding:1rem}',
      '.pp-gate-backdrop.open{opacity:1;visibility:visible}',
      '.pp-gate-modal{background:var(--card-bg,#fff);color:var(--text-primary,#0F172A);border:1px solid var(--border,#E2E8F0);border-radius:16px;max-width:480px;width:100%;max-height:92vh;overflow-y:auto;box-shadow:0 25px 60px rgba(0,0,0,.35);transform:translateY(16px) scale(.98);transition:transform .25s;font-family:var(--font-sans,sans-serif)}',
      '.pp-gate-backdrop.open .pp-gate-modal{transform:none}',
      '.pp-gate-head{padding:1.6rem 1.6rem 1rem;text-align:center;border-bottom:1px solid var(--border,#E2E8F0)}',
      '.pp-gate-badge{display:inline-flex;align-items:center;gap:.35rem;padding:.3rem .8rem;border-radius:20px;background:rgba(14,165,233,.14);color:var(--accent,#0EA5E9);font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-bottom:.8rem;font-family:var(--font-heading,sans-serif)}',
      '.pp-gate-head h3{font-family:var(--font-heading,sans-serif);font-size:1.3rem;margin:0 0 .5rem;color:var(--text-primary,#0F172A)}',
      '.pp-gate-head p{margin:0;color:var(--text-secondary,#475569);font-size:.95rem;line-height:1.65}',
      '.pp-gate-body{padding:1.3rem 1.6rem}',
      '.pp-offer{display:block;text-decoration:none;border:1px solid var(--border,#E2E8F0);border-radius:12px;padding:1rem 1.1rem;margin-bottom:.85rem;transition:all .2s;background:var(--secondary-bg,#F8FAFC)}',
      '.pp-offer:hover{transform:translateY(-2px);border-color:var(--accent,#0EA5E9);text-decoration:none;box-shadow:0 8px 22px rgba(14,165,233,.12)}',
      '.pp-offer.primary{border-color:var(--accent,#0EA5E9);background:linear-gradient(135deg,rgba(14,165,233,.08),rgba(99,102,241,.08))}',
      '.pp-offer-row{display:flex;align-items:baseline;justify-content:space-between;gap:.6rem}',
      '.pp-offer-name{font-family:var(--font-heading,sans-serif);font-weight:700;font-size:1rem;color:var(--text-primary,#0F172A)}',
      '.pp-offer-price{font-family:var(--font-heading,sans-serif);font-weight:800;font-size:1.05rem;color:var(--accent,#0EA5E9);white-space:nowrap}',
      '.pp-offer-desc{margin:.3rem 0 0;font-size:.82rem;color:var(--text-muted,#52627A);line-height:1.5}',
      '.pp-gate-foot{padding:0 1.6rem 1.4rem;text-align:center}',
      '.pp-gate-foot a{color:var(--accent,#0EA5E9);font-size:.85rem;font-weight:600}',
      '.pp-gate-close{position:absolute;top:.9rem;right:.9rem;width:34px;height:34px;border:none;border-radius:50%;background:var(--hover-bg,#F1F5F9);color:var(--text-secondary,#475569);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1.1rem;line-height:1}',
      '.pp-gate-modal{position:relative}'
    ].join('');
    document.head.appendChild(s);
  }

  var LOCK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>';

  // ── Lock the gated tabs visually ─────────────────────────────────────
  function lockTabs() {
    document.querySelectorAll('.module-tab').forEach(function (tab) {
      var idx = parseInt(tab.getAttribute('data-tab'), 10);
      if (isNaN(idx)) {
        // capstone tab has no numeric data-tab on some packs — derive by position
        idx = Array.prototype.indexOf.call(document.querySelectorAll('.module-tab'), tab);
      }
      if (idx >= CFG.freeModules && !tab.querySelector('.pp-lock-pill')) {
        var pill = document.createElement('span');
        pill.className = 'pp-lock-pill';
        pill.innerHTML = LOCK_SVG + 'Premium';
        tab.appendChild(pill);
      }
    });
  }

  // ── The paywall modal ────────────────────────────────────────────────
  function buildModal() {
    var redirect = encodeURIComponent(location.pathname);
    var backdrop = document.createElement('div');
    backdrop.className = 'pp-gate-backdrop';
    backdrop.innerHTML =
      '<div class="pp-gate-modal" role="dialog" aria-modal="true" aria-label="Unlock this Practice Pack">' +
        '<button class="pp-gate-close" aria-label="Close">&times;</button>' +
        '<div class="pp-gate-head">' +
          '<span class="pp-gate-badge">' + LOCK_SVG + 'Free preview complete</span>' +
          '<h3>Keep going — finish the pack</h3>' +
          '<p>You\'ve worked through the first ' + CFG.freeModules + ' modules. The remaining modules and your auto-built <strong>' + esc(CFG.artefact) + '</strong> are part of ImpactMojo Premium.</p>' +
        '</div>' +
        '<div class="pp-gate-body">' +
          '<a class="pp-offer primary" href="/premium.html#detail-practitioner">' +
            '<div class="pp-offer-row"><span class="pp-offer-name">All 18 Practice Packs</span><span class="pp-offer-price">' + esc(CFG.tierPrice) + '</span></div>' +
            '<p class="pp-offer-desc">Practitioner membership — every pack, plus Research Question Builder Pro, ToC Workbench Pro &amp; certificates.</p>' +
          '</a>' +
          '<a class="pp-offer" href="/premium.html?pack=' + encodeURIComponent(CFG.slug) + '#payment">' +
            '<div class="pp-offer-row"><span class="pp-offer-name">Just this pack</span><span class="pp-offer-price">' + esc(CFG.price) + '</span></div>' +
            '<p class="pp-offer-desc">One-time access to <strong>' + esc(CFG.title) + '</strong> — all modules and the capstone builder.</p>' +
          '</a>' +
          '<a class="pp-offer" href="/contact.html?topic=PracticePackReview&pack=' + encodeURIComponent(CFG.slug) + '">' +
            '<div class="pp-offer-row"><span class="pp-offer-name">Add a 1:1 expert review</span><span class="pp-offer-price">' + esc(CFG.review) + '</span></div>' +
            '<p class="pp-offer-desc">Optional — we review your finished ' + esc(CFG.artefact) + ' and send written feedback.</p>' +
          '</a>' +
        '</div>' +
        '<div class="pp-gate-foot"><a href="/login.html?redirect=' + redirect + '">Already a member? Log in &rarr;</a></div>' +
      '</div>';
    document.body.appendChild(backdrop);

    function close() { backdrop.classList.remove('open'); document.body.style.overflow = ''; }
    backdrop.querySelector('.pp-gate-close').addEventListener('click', close);
    backdrop.addEventListener('click', function (e) { if (e.target === backdrop) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    return backdrop;
  }

  function esc(str) {
    return String(str).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  var modalEl = null;
  function showPaywall() {
    if (!modalEl) modalEl = buildModal();
    modalEl.classList.add('open');
    document.body.style.overflow = 'hidden';
    try {
      if (typeof window.gtag === 'function') {
        window.gtag('event', 'practice_pack_paywall', { pack: CFG.slug });
      }
    } catch (e) { /* ignore */ }
  }

  // ── Wrap goTab so every entry point (tabs + nav buttons) is gated ────
  function installGate() {
    var orig = window.goTab;
    if (typeof orig !== 'function') {
      // Fallback: capture-phase interception on tab clicks.
      document.addEventListener('click', function (e) {
        var tab = e.target.closest('.module-tab');
        if (!tab) return;
        var idx = parseInt(tab.getAttribute('data-tab'), 10);
        if (!isNaN(idx) && idx >= CFG.freeModules) {
          e.preventDefault(); e.stopImmediatePropagation(); showPaywall();
        }
      }, true);
      return;
    }
    window.goTab = function (idx) {
      if (typeof idx === 'number' && idx >= CFG.freeModules) { showPaywall(); return; }
      return orig.apply(this, arguments);
    };
  }

  function init() {
    if (hasAccess()) return; // full pack, nothing to do
    injectStyles();
    lockTabs();
    installGate();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
