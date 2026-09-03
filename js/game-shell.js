/**
 * ImpactMojo Game Shell v4
 * Injects shared header, footer, 3-way theme, Indian folk art motifs,
 * ImpactMojo typography, Sargam icon helpers, and visual enhancements.
 * Inspired by DesiLog, FolkLog, and Indian folk art traditions.
 * Typography: Inter (titles), Amaranth (body), JetBrains Mono (code)
 * Usage: <script src="/js/game-shell.js"></script> (at end of <body>)
 */
(function() {
  'use strict';

  // ── Load ImpactMojo Fonts (self-hosted, /assets/fonts/) ────
  if (!document.querySelector('link[href="/css/fonts.css"]')) {
    var fontLink = document.createElement('link');
    fontLink.rel = 'stylesheet';
    fontLink.href = '/css/fonts.css';
    document.head.appendChild(fontLink);
  }

  // ── Sargam Icon helper ─────────────────────────────────────
  // Usage: IMXIcon('Flare') returns an <img> tag string
  var SARGAM_CDN = 'https://cdn.jsdelivr.net/npm/sargam-icons@1.6.7/Icons/';
  window.IMXIcon = function(name, size, style) {
    size = size || 16;
    style = style || 'Line';
    return '<img src="' + SARGAM_CDN + style + '/si_' + name + '.svg" ' +
      'width="' + size + '" height="' + size + '" ' +
      'alt="" class="imx-sargam-icon" aria-hidden="true">';
  };

  // ── Theme System (System / Light / Dark) ──────────────────
  // Canonical key is 'im-theme' (matches handouts + cookie-ui.js + account.js).
  // Also mirror to legacy keys so any page still reading them stays in sync.
  var THEME_KEY = 'im-theme';
  var LEGACY_KEYS = ['imx_theme', 'theme', 'impactmojo-theme'];
  var saved = localStorage.getItem(THEME_KEY);
  if (!saved) {
    // Migrate from legacy keys once
    for (var i = 0; i < LEGACY_KEYS.length; i++) {
      var v = localStorage.getItem(LEGACY_KEYS[i]);
      if (v) { saved = v; localStorage.setItem(THEME_KEY, v); break; }
    }
  }
  // Treat an explicit 'system' value as "no preference" for active-state logic
  if (saved === 'system') saved = null;

  function getSystemPref() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }
  function resolveTheme(pref) {
    if (pref === 'light') return 'light';
    if (pref === 'dark') return 'dark';
    return getSystemPref();
  }
  function applyTheme(pref) {
    var resolved = resolveTheme(pref);
    document.body.classList.toggle('light-mode', resolved === 'light');
    document.documentElement.setAttribute('data-theme', resolved);
    document.querySelectorAll('.imx-theme-btn').forEach(function(btn) {
      btn.classList.toggle('active', btn.getAttribute('data-theme') === (pref || 'system'));
    });
  }
  function setTheme(pref) {
    if (pref === 'system' || !pref) {
      localStorage.removeItem(THEME_KEY);
      LEGACY_KEYS.forEach(function(k) { localStorage.removeItem(k); });
    } else {
      localStorage.setItem(THEME_KEY, pref);
      LEGACY_KEYS.forEach(function(k) { localStorage.setItem(k, pref); });
    }
    applyTheme(pref);
  }
  applyTheme(saved);
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', function() {
      if (!localStorage.getItem(THEME_KEY)) applyTheme(null);
    });
  }

  // ── Header ─────────────────────────────────────────────────
  var header = document.createElement('nav');
  header.id = 'imx-game-header';
  header.innerHTML =
    '<a href="/" class="imx-gh-logo">' +
      '<img src="/assets/images/ImpactMojo%20Logo.png" alt="ImpactMojo" width="32" height="32">' +
      '<span>ImpactMojo</span>' +
    '</a>' +
    '<div class="imx-gh-right">' +
      '<a href="/#games" class="imx-gh-link">All Games</a>' +
      '<div class="imx-gh-theme-group">' +
        '<button class="imx-theme-btn' + (!saved ? ' active' : '') + '" data-theme="system" title="System theme" aria-label="System theme">' +
          '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>' +
        '</button>' +
        '<button class="imx-theme-btn' + (saved === 'light' ? ' active' : '') + '" data-theme="light" title="Light theme" aria-label="Light theme">' +
          '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>' +
        '</button>' +
        '<button class="imx-theme-btn' + (saved === 'dark' ? ' active' : '') + '" data-theme="dark" title="Dark theme" aria-label="Dark theme">' +
          '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>' +
        '</button>' +
      '</div>' +
    '</div>';
  document.body.insertBefore(header, document.body.firstChild);
  document.querySelectorAll('.imx-theme-btn').forEach(function(btn) {
    btn.addEventListener('click', function() { setTheme(btn.getAttribute('data-theme')); });
  });

  // ── Indian Folk Art Decorations ────────────────────────────

  // Warli-inspired village scene (bottom-left) — larger, more visible
  var warli = document.createElement('div');
  warli.className = 'imx-game-motif imx-motif-warli';
  warli.setAttribute('aria-hidden', 'true');
  warli.innerHTML =
    '<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">' +
      // Ground
      '<line x1="0" y1="260" x2="400" y2="260" stroke="currentColor" stroke-width="1.5" opacity="0.4"/>' +
      // Hut 1
      '<polygon points="30,260 30,210 60,175 90,210 90,260" fill="none" stroke="currentColor" stroke-width="2" opacity="0.5"/>' +
      '<line x1="55" y1="260" x2="55" y2="220" stroke="currentColor" stroke-width="1.5" opacity="0.4"/>' +
      '<line x1="65" y1="260" x2="65" y2="220" stroke="currentColor" stroke-width="1.5" opacity="0.4"/>' +
      '<line x1="30" y1="235" x2="90" y2="235" stroke="currentColor" stroke-width="0.8" opacity="0.3"/>' +
      // Hut 2 (smaller, background)
      '<polygon points="100,260 100,225 120,200 140,225 140,260" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.35"/>' +
      '<line x1="117" y1="260" x2="117" y2="235" stroke="currentColor" stroke-width="1" opacity="0.3"/>' +
      '<line x1="123" y1="260" x2="123" y2="235" stroke="currentColor" stroke-width="1" opacity="0.3"/>' +
      // Tree 1 (Warli style - trunk + overlapping circles)
      '<line x1="180" y1="260" x2="180" y2="170" stroke="currentColor" stroke-width="2" opacity="0.45"/>' +
      '<circle cx="180" cy="155" r="25" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.35"/>' +
      '<circle cx="165" cy="168" r="18" fill="none" stroke="currentColor" stroke-width="1" opacity="0.3"/>' +
      '<circle cx="195" cy="165" r="20" fill="none" stroke="currentColor" stroke-width="1" opacity="0.3"/>' +
      '<circle cx="180" cy="140" r="12" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.25"/>' +
      // Tree 2 (smaller)
      '<line x1="155" y1="260" x2="155" y2="210" stroke="currentColor" stroke-width="1.2" opacity="0.3"/>' +
      '<circle cx="155" cy="200" r="14" fill="none" stroke="currentColor" stroke-width="1" opacity="0.25"/>' +
      // Tarpa dance — circle of 5 figures holding hands
      '<g opacity="0.55" transform="translate(270,195)">' +
        // Central tarpa player
        '<polygon points="0,-10 -10,18 10,18" fill="currentColor" opacity="0.5" stroke="currentColor" stroke-width="1.5"/>' +
        '<circle cx="0" cy="-18" r="7" fill="currentColor" opacity="0.5"/>' +
        '<line x1="-14" y1="0" x2="-20" y2="-10" stroke="currentColor" stroke-width="1.5"/>' +
        '<line x1="14" y1="0" x2="20" y2="-10" stroke="currentColor" stroke-width="1.5"/>' +
        '<line x1="-5" y1="18" x2="-10" y2="35" stroke="currentColor" stroke-width="1.5"/>' +
        '<line x1="5" y1="18" x2="10" y2="35" stroke="currentColor" stroke-width="1.5"/>' +
        // Long tarpa horn
        '<path d="M-20,-10 Q-35,-25 -28,-40" fill="none" stroke="currentColor" stroke-width="1.5"/>' +
      '</g>' +
      // Dancer 1
      '<g opacity="0.5" transform="translate(235,200)">' +
        '<polygon points="0,-5 -8,16 8,16" fill="currentColor" opacity="0.4" stroke="currentColor" stroke-width="1.2"/>' +
        '<circle cx="0" cy="-12" r="6" fill="currentColor" opacity="0.4"/>' +
        '<line x1="-12" y1="2" x2="-22" y2="-5" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="12" y1="2" x2="22" y2="8" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="-4" y1="16" x2="-12" y2="32" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="4" y1="16" x2="8" y2="32" stroke="currentColor" stroke-width="1.2"/>' +
      '</g>' +
      // Dancer 2
      '<g opacity="0.5" transform="translate(305,198)">' +
        '<polygon points="0,-5 -8,16 8,16" fill="currentColor" opacity="0.4" stroke="currentColor" stroke-width="1.2"/>' +
        '<circle cx="0" cy="-12" r="6" fill="currentColor" opacity="0.4"/>' +
        '<line x1="-12" y1="4" x2="-22" y2="10" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="12" y1="0" x2="22" y2="-8" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="-4" y1="16" x2="-8" y2="32" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="4" y1="16" x2="12" y2="32" stroke="currentColor" stroke-width="1.2"/>' +
      '</g>' +
      // Dancer 3 (behind)
      '<g opacity="0.4" transform="translate(250,215)">' +
        '<polygon points="0,-4 -6,12 6,12" fill="currentColor" opacity="0.35" stroke="currentColor" stroke-width="1"/>' +
        '<circle cx="0" cy="-10" r="5" fill="currentColor" opacity="0.35"/>' +
        '<line x1="-10" y1="0" x2="-16" y2="6" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="10" y1="2" x2="16" y2="-2" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="-3" y1="12" x2="-6" y2="25" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="3" y1="12" x2="6" y2="25" stroke="currentColor" stroke-width="1"/>' +
      '</g>' +
      // Dancer 4 (behind)
      '<g opacity="0.4" transform="translate(290,218)">' +
        '<polygon points="0,-4 -6,12 6,12" fill="currentColor" opacity="0.35" stroke="currentColor" stroke-width="1"/>' +
        '<circle cx="0" cy="-10" r="5" fill="currentColor" opacity="0.35"/>' +
        '<line x1="-10" y1="2" x2="-15" y2="-4" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="10" y1="0" x2="15" y2="8" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="-3" y1="12" x2="-7" y2="25" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="3" y1="12" x2="7" y2="25" stroke="currentColor" stroke-width="1"/>' +
      '</g>' +
      // Sun with rays (Warli spiral sun)
      '<g opacity="0.45" transform="translate(350,50)">' +
        '<circle cx="0" cy="0" r="20" fill="none" stroke="currentColor" stroke-width="1.5"/>' +
        '<circle cx="0" cy="0" r="12" fill="none" stroke="currentColor" stroke-width="1"/>' +
        '<circle cx="0" cy="0" r="5" fill="currentColor" opacity="0.3"/>' +
        '<line x1="0" y1="-23" x2="0" y2="-32" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="0" y1="23" x2="0" y2="32" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="-23" y1="0" x2="-32" y2="0" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="23" y1="0" x2="32" y2="0" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="-16" y1="-16" x2="-22" y2="-22" stroke="currentColor" stroke-width="0.8"/>' +
        '<line x1="16" y1="-16" x2="22" y2="-22" stroke="currentColor" stroke-width="0.8"/>' +
        '<line x1="-16" y1="16" x2="-22" y2="22" stroke="currentColor" stroke-width="0.8"/>' +
        '<line x1="16" y1="16" x2="22" y2="22" stroke="currentColor" stroke-width="0.8"/>' +
      '</g>' +
      // Ox / bullock (Warli staple)
      '<g opacity="0.4" transform="translate(340,235)">' +
        '<ellipse cx="0" cy="0" rx="18" ry="10" fill="none" stroke="currentColor" stroke-width="1.5"/>' +
        '<circle cx="-15" cy="-10" r="5" fill="none" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="-18" y1="-14" x2="-22" y2="-22" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="-12" y1="-14" x2="-8" y2="-22" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="-10" y1="8" x2="-12" y2="22" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="-4" y1="9" x2="-2" y2="22" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="6" y1="9" x2="4" y2="22" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="12" y1="8" x2="14" y2="22" stroke="currentColor" stroke-width="1.2"/>' +
        '<path d="M16,0 Q28,0 25,5" fill="none" stroke="currentColor" stroke-width="1"/>' +
      '</g>' +
    '</svg>';
  document.body.appendChild(warli);

  // Madhubani-inspired border (top-right) — rich colors, larger motifs
  var madhubani = document.createElement('div');
  madhubani.className = 'imx-game-motif imx-motif-madhubani';
  madhubani.setAttribute('aria-hidden', 'true');
  madhubani.innerHTML =
    '<svg viewBox="0 0 120 500" xmlns="http://www.w3.org/2000/svg">' +
      // Double border strip
      '<rect x="8" y="8" width="104" height="484" fill="none" stroke="#D97706" stroke-width="1.5" opacity="0.3" rx="6"/>' +
      '<rect x="15" y="15" width="90" height="470" fill="none" stroke="#DC2626" stroke-width="1" opacity="0.25" rx="4"/>' +
      // Fish 1 (Madhubani signature — detailed)
      '<g transform="translate(60,60)" opacity="0.5">' +
        '<ellipse cx="0" cy="0" rx="28" ry="14" fill="none" stroke="#D97706" stroke-width="1.8"/>' +
        '<path d="M28,0 L40,-10 L40,10Z" fill="#D97706" opacity="0.3" stroke="#D97706" stroke-width="1"/>' +
        '<circle cx="-12" cy="-3" r="3" fill="#D97706" opacity="0.6"/>' +
        '<circle cx="-12" cy="-3" r="1.2" fill="#1E293B" opacity="0.8"/>' +
        '<path d="M-8,0 Q0,-8 18,0" fill="none" stroke="#D97706" stroke-width="0.6"/>' +
        '<path d="M-8,0 Q0,8 18,0" fill="none" stroke="#D97706" stroke-width="0.6"/>' +
        '<line x1="-5" y1="-6" x2="-5" y2="6" stroke="#D97706" stroke-width="0.5" opacity="0.5"/>' +
        '<line x1="2" y1="-9" x2="2" y2="9" stroke="#D97706" stroke-width="0.5" opacity="0.5"/>' +
        '<line x1="10" y1="-11" x2="10" y2="11" stroke="#D97706" stroke-width="0.5" opacity="0.5"/>' +
        '<line x1="18" y1="-8" x2="18" y2="8" stroke="#D97706" stroke-width="0.5" opacity="0.5"/>' +
      '</g>' +
      // Peacock (Madhubani style — detailed fan tail)
      '<g transform="translate(60,160)" opacity="0.45">' +
        // Body
        '<ellipse cx="0" cy="5" rx="12" ry="16" fill="none" stroke="#059669" stroke-width="1.5"/>' +
        '<ellipse cx="0" cy="5" rx="6" ry="10" fill="#059669" opacity="0.15"/>' +
        // Head and neck
        '<path d="M0,-11 Q0,-25 0,-30" fill="none" stroke="#059669" stroke-width="1.5"/>' +
        '<circle cx="0" cy="-33" r="6" fill="none" stroke="#059669" stroke-width="1.5"/>' +
        '<circle cx="0" cy="-33" r="3" fill="#059669" opacity="0.3"/>' +
        // Crown
        '<line x1="0" y1="-39" x2="0" y2="-45" stroke="#D97706" stroke-width="1"/>' +
        '<line x1="-3" y1="-39" x2="-4" y2="-44" stroke="#D97706" stroke-width="0.8"/>' +
        '<line x1="3" y1="-39" x2="4" y2="-44" stroke="#D97706" stroke-width="0.8"/>' +
        '<circle cx="0" cy="-46" r="1.5" fill="#D97706" opacity="0.6"/>' +
        '<circle cx="-5" cy="-45" r="1.2" fill="#D97706" opacity="0.5"/>' +
        '<circle cx="5" cy="-45" r="1.2" fill="#D97706" opacity="0.5"/>' +
        // Beak and eye
        '<path d="M6,-33 L10,-32 L6,-31" fill="#D97706" opacity="0.6"/>' +
        '<circle cx="-2" cy="-34" r="1" fill="#1E293B" opacity="0.8"/>' +
        // Tail feathers (large fan)
        '<path d="M-12,15 Q-40,-20 -20,-50" fill="none" stroke="#2563EB" stroke-width="1.2"/>' +
        '<path d="M-8,18 Q-30,-10 -10,-45" fill="none" stroke="#7C3AED" stroke-width="1"/>' +
        '<path d="M0,20 Q0,-15 0,-50" fill="none" stroke="#2563EB" stroke-width="1.2"/>' +
        '<path d="M8,18 Q30,-10 10,-45" fill="none" stroke="#7C3AED" stroke-width="1"/>' +
        '<path d="M12,15 Q40,-20 20,-50" fill="none" stroke="#2563EB" stroke-width="1.2"/>' +
        // Eye spots on feathers
        '<circle cx="-25" cy="-35" r="4" fill="none" stroke="#D97706" stroke-width="0.8"/>' +
        '<circle cx="-25" cy="-35" r="1.5" fill="#2563EB" opacity="0.5"/>' +
        '<circle cx="-12" cy="-38" r="3.5" fill="none" stroke="#D97706" stroke-width="0.8"/>' +
        '<circle cx="-12" cy="-38" r="1.3" fill="#7C3AED" opacity="0.5"/>' +
        '<circle cx="0" cy="-42" r="4" fill="none" stroke="#D97706" stroke-width="0.8"/>' +
        '<circle cx="0" cy="-42" r="1.5" fill="#2563EB" opacity="0.5"/>' +
        '<circle cx="12" cy="-38" r="3.5" fill="none" stroke="#D97706" stroke-width="0.8"/>' +
        '<circle cx="12" cy="-38" r="1.3" fill="#7C3AED" opacity="0.5"/>' +
        '<circle cx="25" cy="-35" r="4" fill="none" stroke="#D97706" stroke-width="0.8"/>' +
        '<circle cx="25" cy="-35" r="1.5" fill="#2563EB" opacity="0.5"/>' +
      '</g>' +
      // Lotus (Madhubani style — full bloom)
      '<g transform="translate(60,290)" opacity="0.45">' +
        '<ellipse cx="0" cy="0" rx="8" ry="20" fill="#EC4899" opacity="0.12" stroke="#EC4899" stroke-width="1.2"/>' +
        '<ellipse cx="0" cy="0" rx="8" ry="20" fill="#EC4899" opacity="0.12" stroke="#EC4899" stroke-width="1.2" transform="rotate(36)"/>' +
        '<ellipse cx="0" cy="0" rx="8" ry="20" fill="#EC4899" opacity="0.12" stroke="#EC4899" stroke-width="1.2" transform="rotate(72)"/>' +
        '<ellipse cx="0" cy="0" rx="8" ry="20" fill="#EC4899" opacity="0.12" stroke="#EC4899" stroke-width="1.2" transform="rotate(108)"/>' +
        '<ellipse cx="0" cy="0" rx="8" ry="20" fill="#EC4899" opacity="0.12" stroke="#EC4899" stroke-width="1.2" transform="rotate(144)"/>' +
        '<circle cx="0" cy="0" r="8" fill="none" stroke="#D97706" stroke-width="1.2"/>' +
        '<circle cx="0" cy="0" r="4" fill="#D97706" opacity="0.25"/>' +
        // Inner detail
        '<circle cx="0" cy="0" r="12" fill="none" stroke="#EC4899" stroke-width="0.5" stroke-dasharray="2,2"/>' +
      '</g>' +
      // Geometric rangoli pattern
      '<g transform="translate(60,380)" opacity="0.4">' +
        '<rect x="-18" y="-18" width="36" height="36" fill="none" stroke="#D97706" stroke-width="1.2" transform="rotate(45)"/>' +
        '<rect x="-12" y="-12" width="24" height="24" fill="none" stroke="#DC2626" stroke-width="1" transform="rotate(45)"/>' +
        '<rect x="-6" y="-6" width="12" height="12" fill="none" stroke="#D97706" stroke-width="0.8" transform="rotate(45)"/>' +
        '<circle cx="0" cy="0" r="5" fill="#D97706" opacity="0.2"/>' +
        '<circle cx="0" cy="-18" r="3" fill="#DC2626" opacity="0.3"/>' +
        '<circle cx="0" cy="18" r="3" fill="#DC2626" opacity="0.3"/>' +
        '<circle cx="-18" cy="0" r="3" fill="#DC2626" opacity="0.3"/>' +
        '<circle cx="18" cy="0" r="3" fill="#DC2626" opacity="0.3"/>' +
      '</g>' +
      // Fish 2 (bottom, flipped)
      '<g transform="translate(60,450) scale(-1,1)" opacity="0.45">' +
        '<ellipse cx="0" cy="0" rx="25" ry="12" fill="none" stroke="#059669" stroke-width="1.5"/>' +
        '<path d="M25,0 L36,-9 L36,9Z" fill="#059669" opacity="0.25" stroke="#059669" stroke-width="1"/>' +
        '<circle cx="-10" cy="-2" r="2.5" fill="#059669" opacity="0.5"/>' +
        '<line x1="-2" y1="-5" x2="-2" y2="5" stroke="#059669" stroke-width="0.5" opacity="0.4"/>' +
        '<line x1="5" y1="-8" x2="5" y2="8" stroke="#059669" stroke-width="0.5" opacity="0.4"/>' +
        '<line x1="12" y1="-10" x2="12" y2="10" stroke="#059669" stroke-width="0.5" opacity="0.4"/>' +
      '</g>' +
    '</svg>';
  document.body.appendChild(madhubani);

  // Gond-inspired tree of life (right side, larger)
  var gond = document.createElement('div');
  gond.className = 'imx-game-motif imx-motif-gond';
  gond.setAttribute('aria-hidden', 'true');
  gond.innerHTML =
    '<svg viewBox="0 0 240 300" xmlns="http://www.w3.org/2000/svg">' +
      // Tree trunk with Gond hatching pattern
      '<line x1="120" y1="300" x2="120" y2="110" stroke="currentColor" stroke-width="3" opacity="0.35"/>' +
      '<line x1="114" y1="300" x2="114" y2="120" stroke="currentColor" stroke-width="1" opacity="0.2" stroke-dasharray="3,4"/>' +
      '<line x1="126" y1="300" x2="126" y2="120" stroke="currentColor" stroke-width="1" opacity="0.2" stroke-dasharray="3,4"/>' +
      // Roots
      '<path d="M120,290 Q90,295 70,300" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.25"/>' +
      '<path d="M120,290 Q150,295 170,300" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.25"/>' +
      // Main branches
      '<path d="M120,180 Q70,150 30,130" fill="none" stroke="currentColor" stroke-width="2" opacity="0.3"/>' +
      '<path d="M120,180 Q170,150 210,130" fill="none" stroke="currentColor" stroke-width="2" opacity="0.3"/>' +
      '<path d="M120,150 Q75,120 45,85" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.28"/>' +
      '<path d="M120,150 Q165,120 195,85" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.28"/>' +
      '<path d="M120,120 Q85,90 60,50" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.25"/>' +
      '<path d="M120,120 Q155,90 180,50" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.25"/>' +
      '<path d="M120,110 Q100,75 80,30" fill="none" stroke="currentColor" stroke-width="1" opacity="0.22"/>' +
      '<path d="M120,110 Q140,75 160,30" fill="none" stroke="currentColor" stroke-width="1" opacity="0.22"/>' +
      // Gond concentric circle leaves (large, colorful)
      '<circle cx="30" cy="125" r="16" fill="none" stroke="#059669" stroke-width="1.5" opacity="0.4"/>' +
      '<circle cx="30" cy="125" r="10" fill="none" stroke="#059669" stroke-width="1" opacity="0.3"/>' +
      '<circle cx="30" cy="125" r="5" fill="#059669" opacity="0.2"/>' +
      '<circle cx="210" cy="125" r="16" fill="none" stroke="#D97706" stroke-width="1.5" opacity="0.4"/>' +
      '<circle cx="210" cy="125" r="10" fill="none" stroke="#D97706" stroke-width="1" opacity="0.3"/>' +
      '<circle cx="210" cy="125" r="5" fill="#D97706" opacity="0.2"/>' +
      '<circle cx="45" cy="80" r="14" fill="none" stroke="#EC4899" stroke-width="1.2" opacity="0.35"/>' +
      '<circle cx="45" cy="80" r="7" fill="none" stroke="#EC4899" stroke-width="0.8" opacity="0.25"/>' +
      '<circle cx="45" cy="80" r="3" fill="#EC4899" opacity="0.2"/>' +
      '<circle cx="195" cy="80" r="14" fill="none" stroke="#3B82F6" stroke-width="1.2" opacity="0.35"/>' +
      '<circle cx="195" cy="80" r="7" fill="none" stroke="#3B82F6" stroke-width="0.8" opacity="0.25"/>' +
      '<circle cx="195" cy="80" r="3" fill="#3B82F6" opacity="0.2"/>' +
      '<circle cx="60" cy="45" r="12" fill="none" stroke="#8B5CF6" stroke-width="1" opacity="0.3"/>' +
      '<circle cx="60" cy="45" r="6" fill="none" stroke="#8B5CF6" stroke-width="0.6" opacity="0.2"/>' +
      '<circle cx="60" cy="45" r="2.5" fill="#8B5CF6" opacity="0.2"/>' +
      '<circle cx="180" cy="45" r="12" fill="none" stroke="#10B981" stroke-width="1" opacity="0.3"/>' +
      '<circle cx="180" cy="45" r="6" fill="none" stroke="#10B981" stroke-width="0.6" opacity="0.2"/>' +
      '<circle cx="180" cy="45" r="2.5" fill="#10B981" opacity="0.2"/>' +
      '<circle cx="80" cy="25" r="10" fill="none" stroke="#F59E0B" stroke-width="1" opacity="0.3"/>' +
      '<circle cx="80" cy="25" r="4" fill="#F59E0B" opacity="0.15"/>' +
      '<circle cx="160" cy="25" r="10" fill="none" stroke="#EF4444" stroke-width="1" opacity="0.3"/>' +
      '<circle cx="160" cy="25" r="4" fill="#EF4444" opacity="0.15"/>' +
      // Top crown leaves
      '<circle cx="120" cy="15" r="11" fill="none" stroke="#059669" stroke-width="1" opacity="0.3"/>' +
      '<circle cx="120" cy="15" r="5" fill="#059669" opacity="0.15"/>' +
      // Gond birds (detailed — body with line pattern)
      '<g opacity="0.4" transform="translate(15,55)">' +
        '<path d="M0,0 Q8,-12 16,-8 L22,-12 L20,-6 Q24,-2 20,4 Q8,10 0,0Z" fill="none" stroke="currentColor" stroke-width="1.2"/>' +
        '<circle cx="16" cy="-6" r="1.5" fill="currentColor" opacity="0.6"/>' +
        '<line x1="4" y1="-2" x2="4" y2="4" stroke="currentColor" stroke-width="0.5"/>' +
        '<line x1="8" y1="-4" x2="8" y2="4" stroke="currentColor" stroke-width="0.5"/>' +
        '<line x1="12" y1="-6" x2="12" y2="2" stroke="currentColor" stroke-width="0.5"/>' +
      '</g>' +
      '<g opacity="0.4" transform="translate(200,40) scale(-1,1)">' +
        '<path d="M0,0 Q8,-12 16,-8 L22,-12 L20,-6 Q24,-2 20,4 Q8,10 0,0Z" fill="none" stroke="currentColor" stroke-width="1.2"/>' +
        '<circle cx="16" cy="-6" r="1.5" fill="currentColor" opacity="0.6"/>' +
        '<line x1="4" y1="-2" x2="4" y2="4" stroke="currentColor" stroke-width="0.5"/>' +
        '<line x1="8" y1="-4" x2="8" y2="4" stroke="currentColor" stroke-width="0.5"/>' +
        '<line x1="12" y1="-6" x2="12" y2="2" stroke="currentColor" stroke-width="0.5"/>' +
      '</g>' +
      // Small Gond deer
      '<g opacity="0.35" transform="translate(30,250)">' +
        '<ellipse cx="0" cy="0" rx="14" ry="8" fill="none" stroke="currentColor" stroke-width="1.2"/>' +
        '<line x1="-8" y1="7" x2="-10" y2="18" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="-2" y1="7" x2="-2" y2="18" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="4" y1="7" x2="4" y2="18" stroke="currentColor" stroke-width="1"/>' +
        '<line x1="10" y1="7" x2="12" y2="18" stroke="currentColor" stroke-width="1"/>' +
        '<circle cx="-12" cy="-8" r="4" fill="none" stroke="currentColor" stroke-width="1"/>' +
        '<path d="M-14,-12 Q-18,-22 -12,-20" fill="none" stroke="currentColor" stroke-width="0.8"/>' +
        '<path d="M-10,-12 Q-6,-22 -10,-20" fill="none" stroke="currentColor" stroke-width="0.8"/>' +
      '</g>' +
    '</svg>';
  document.body.appendChild(gond);

  // ── Kolam/Rangoli top border decoration ───────────────────
  var kolam = document.createElement('div');
  kolam.className = 'imx-game-motif imx-motif-kolam';
  kolam.setAttribute('aria-hidden', 'true');
  kolam.innerHTML =
    '<svg viewBox="0 0 1200 40" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">' +
      // Flowing vine pattern
      '<path d="M0,20 Q30,5 60,20 Q90,35 120,20 Q150,5 180,20 Q210,35 240,20 Q270,5 300,20 Q330,35 360,20 Q390,5 420,20 Q450,35 480,20 Q510,5 540,20 Q570,35 600,20 Q630,5 660,20 Q690,35 720,20 Q750,5 780,20 Q810,35 840,20 Q870,5 900,20 Q930,35 960,20 Q990,5 1020,20 Q1050,35 1080,20 Q1110,5 1140,20 Q1170,35 1200,20" fill="none" stroke="#D97706" stroke-width="1.5" opacity="0.5"/>' +
      // Dots at peaks and troughs
      '<g fill="#EC4899" opacity="0.4">' +
        '<circle cx="60" cy="20" r="3"/><circle cx="180" cy="20" r="3"/><circle cx="300" cy="20" r="3"/>' +
        '<circle cx="420" cy="20" r="3"/><circle cx="540" cy="20" r="3"/><circle cx="660" cy="20" r="3"/>' +
        '<circle cx="780" cy="20" r="3"/><circle cx="900" cy="20" r="3"/><circle cx="1020" cy="20" r="3"/><circle cx="1140" cy="20" r="3"/>' +
      '</g>' +
      '<g fill="#059669" opacity="0.35">' +
        '<circle cx="120" cy="20" r="2.5"/><circle cx="240" cy="20" r="2.5"/><circle cx="360" cy="20" r="2.5"/>' +
        '<circle cx="480" cy="20" r="2.5"/><circle cx="600" cy="20" r="2.5"/><circle cx="720" cy="20" r="2.5"/>' +
        '<circle cx="840" cy="20" r="2.5"/><circle cx="960" cy="20" r="2.5"/><circle cx="1080" cy="20" r="2.5"/>' +
      '</g>' +
      // Small paisley/leaf shapes along the vine
      '<g opacity="0.3">' +
        '<path d="M25,12 Q30,5 35,12 Q30,16 25,12Z" fill="#D97706"/>' +
        '<path d="M145,28 Q150,35 155,28 Q150,24 145,28Z" fill="#059669"/>' +
        '<path d="M265,12 Q270,5 275,12 Q270,16 265,12Z" fill="#EC4899"/>' +
        '<path d="M385,28 Q390,35 395,28 Q390,24 385,28Z" fill="#8B5CF6"/>' +
        '<path d="M505,12 Q510,5 515,12 Q510,16 505,12Z" fill="#D97706"/>' +
        '<path d="M625,28 Q630,35 635,28 Q630,24 625,28Z" fill="#059669"/>' +
        '<path d="M745,12 Q750,5 755,12 Q750,16 745,12Z" fill="#EC4899"/>' +
        '<path d="M865,28 Q870,35 875,28 Q870,24 865,28Z" fill="#8B5CF6"/>' +
        '<path d="M985,12 Q990,5 995,12 Q990,16 985,12Z" fill="#D97706"/>' +
        '<path d="M1105,28 Q1110,35 1115,28 Q1110,24 1105,28Z" fill="#059669"/>' +
      '</g>' +
    '</svg>';
  document.body.insertBefore(kolam, header.nextSibling);

  // ── Footer ─────────────────────────────────────────────────
  var footer = document.createElement('footer');
  footer.id = 'imx-game-footer';
  footer.innerHTML =
    '<div class="imx-gf-inner">' +
      '<div class="imx-gf-divider"></div>' +
      '<p>Made with \u2764\uFE0F by <a href="https://www.pinpointventures.in" target="_blank" rel="noopener noreferrer">PinPoint Ventures</a></p>' +
      '<div class="imx-gf-links">' +
        '<a href="/">Home</a>' +
        '<a href="/about">About</a>' +
        '<a href="/privacy-policy">Privacy</a>' +
        '<a href="/terms-of-service">Terms</a>' +
        '<a href="https://github.com/ImpactMojo/ImpactMojo" target="_blank" rel="noopener noreferrer">GitHub</a>' +
      '</div>' +
      '<p class="imx-gf-copy">\u00A9 ' + new Date().getFullYear() + ' ImpactMojo. MIT + CC BY-NC-ND 4.0</p>' +
    '</div>';
  document.body.appendChild(footer);

  // ── Override CSS variables for dark mode contrast ─────────
  // Games define --text-muted:#64748B etc. which are unreadable on dark bg.
  // Override the CSS custom properties directly so var() references pick up readable values.
  var varFix = document.createElement('style');
  varFix.textContent =
    'body:not(.light-mode) { --text-dim: #CBD5E1 !important; --text-muted: #94A3B8 !important; --text: #F1F5F9 !important; --border: #475569 !important; }' +
    'body.light-mode { --bg: #FFFBF5 !important; --card: #FFFFFF !important; --text: #1E293B !important; --text-dim: #78350F !important; --text-muted: #92400E !important; --border: #E7DDD0 !important; }';
  document.head.appendChild(varFix);

  // ── Inject Styles ──────────────────────────────────────────
  var css = document.createElement('style');
  css.textContent =

    /* ═══ TYPOGRAPHY ═════════════════════════════════════════ */
    'body { font-family: "Amaranth", sans-serif !important; }' +
    'h1, h2, h3, h4, h5, h6, .welcome-title, .game-title, .section-title { font-family: "Inter", sans-serif !important; }' +
    'code, pre, kbd, samp, .mono, [class*="mono"] { font-family: "JetBrains Mono", monospace !important; }' +
    '.imx-gh-logo span { font-family: "Inter", sans-serif !important; font-weight: 800 !important; }' +
    '#imx-game-footer { font-family: "Amaranth", sans-serif !important; }' +
    /* Sargam icon inline styling */
    '.imx-sargam-icon { display: inline-block; vertical-align: middle; margin: 0 2px; filter: brightness(0) invert(1); }' +
    'body.light-mode .imx-sargam-icon { filter: brightness(0) invert(0.2); }' +
    '.imx-sargam-accent { filter: invert(67%) sepia(74%) saturate(1200%) hue-rotate(2deg) brightness(104%) contrast(97%); }' +

    /* ═══ DARK MODE CONTRAST FIX ═══════════════════════════ */
    /* Fix dark text on dark backgrounds — comprehensive contrast overrides */
    'body:not(.light-mode) .card, body:not(.light-mode) [class*="card"]:not(.imx-theme-btn) { background: #1E293B !important; color: #F1F5F9 !important; border-color: #475569 !important; }' +
    'body:not(.light-mode) p, body:not(.light-mode) span:not(.imx-gh-logo span), body:not(.light-mode) li, body:not(.light-mode) label, body:not(.light-mode) td, body:not(.light-mode) dd, body:not(.light-mode) dt { color: #E2E8F0 !important; }' +
    'body:not(.light-mode) h1, body:not(.light-mode) h2, body:not(.light-mode) h3, body:not(.light-mode) h4, body:not(.light-mode) h5, body:not(.light-mode) h6 { color: #F8FAFC !important; }' +
    'body:not(.light-mode) small, body:not(.light-mode) .text-muted, body:not(.light-mode) .subtitle, body:not(.light-mode) .desc, body:not(.light-mode) .description { color: #CBD5E1 !important; }' +
    /* Game-specific label/stat classes that use #64748B — force readable */
    'body:not(.light-mode) .label, body:not(.light-mode) .plabel, body:not(.light-mode) .rlabel, body:not(.light-mode) .stat .label, body:not(.light-mode) .stat-label { color: #CBD5E1 !important; }' +
    'body:not(.light-mode) .value, body:not(.light-mode) .rval, body:not(.light-mode) .pval, body:not(.light-mode) .stat .value, body:not(.light-mode) .stat-value { color: #F1F5F9 !important; }' +
    'body:not(.light-mode) .example-item .desc, body:not(.light-mode) .meta, body:not(.light-mode) .caption, body:not(.light-mode) .helper-text, body:not(.light-mode) figcaption { color: #CBD5E1 !important; }' +
    'body:not(.light-mode) .panel, body:not(.light-mode) .box, body:not(.light-mode) .section, body:not(.light-mode) [class*="panel"], body:not(.light-mode) [class*="box"] { background: #1E293B !important; color: #F1F5F9 !important; }' +
    'body:not(.light-mode) th { background: #334155 !important; color: #F1F5F9 !important; }' +
    'body:not(.light-mode) td { border-color: #475569 !important; color: #E2E8F0 !important; }' +
    'body:not(.light-mode) input, body:not(.light-mode) select, body:not(.light-mode) textarea { background: #334155 !important; color: #F1F5F9 !important; border-color: #475569 !important; }' +
    'body:not(.light-mode) button:not(.imx-theme-btn) { color: #F1F5F9 !important; }' +
    'body:not(.light-mode) .hint, body:not(.light-mode) .tip, body:not(.light-mode) blockquote, body:not(.light-mode) .note, body:not(.light-mode) .info, body:not(.light-mode) .insight-card { background: #1E3A5F !important; border-color: #3B82F6 !important; color: #E2E8F0 !important; }' +
    /* Catch-all: any element with inline color: #64748B or similar dark greys */
    'body:not(.light-mode) [style*="color:#64748B"], body:not(.light-mode) [style*="color: #64748B"] { color: #CBD5E1 !important; }' +
    'body:not(.light-mode) [style*="color:#374151"], body:not(.light-mode) [style*="color: #374151"] { color: #CBD5E1 !important; }' +
    'body:not(.light-mode) [style*="color:#4B5563"], body:not(.light-mode) [style*="color: #4B5563"] { color: #CBD5E1 !important; }' +

    /* ═══ LIGHT MODE ═══════════════════════════════════════ */
    'body.light-mode { background: #FFFBF5 !important; color: #1E293B !important; }' +
    'body.light-mode .card, body.light-mode [class*="card"] { background: #FFFFFF !important; border-color: #E7DDD0 !important; color: #1E293B !important; box-shadow: 0 2px 8px rgba(139,90,43,0.08); }' +
    'body.light-mode input, body.light-mode select, body.light-mode textarea { background: #FFF8F0 !important; color: #1E293B !important; border-color: #D4C4B0 !important; }' +
    'body.light-mode button:not(.imx-theme-btn) { color: #1E293B; }' +
    'body.light-mode h1, body.light-mode h2, body.light-mode h3, body.light-mode h4 { color: #1A1207 !important; }' +
    'body.light-mode p, body.light-mode span, body.light-mode li, body.light-mode td, body.light-mode th, body.light-mode label, body.light-mode small { color: #3D2E1C !important; }' +
    'body.light-mode a:not(.imx-gh-logo):not(.imx-gh-link):not(.imx-gf-inner a) { color: #B45309 !important; }' +
    'body.light-mode table { border-color: #E7DDD0 !important; }' +
    'body.light-mode th { background: #FFF3E6 !important; color: #1A1207 !important; }' +
    'body.light-mode td { border-color: #E7DDD0 !important; }' +
    'body.light-mode .label, body.light-mode .plabel, body.light-mode .rlabel, body.light-mode .stat .label, body.light-mode .stat-label { color: #78350F !important; }' +
    'body.light-mode .value, body.light-mode .rval, body.light-mode .pval, body.light-mode .stat .value, body.light-mode .stat-value { color: #1A1207 !important; }' +
    'body.light-mode .desc, body.light-mode .description, body.light-mode .meta, body.light-mode .caption, body.light-mode .helper-text { color: #78350F !important; }' +
    'body.light-mode .panel, body.light-mode .box, body.light-mode [class*="panel"], body.light-mode [class*="box"] { background: #FFFFFF !important; color: #1E293B !important; border-color: #E7DDD0 !important; }' +
    'body.light-mode [class*="stat"] { background: #FFFFFF !important; border-color: #E7DDD0 !important; }' +
    'body.light-mode .progress-bar, body.light-mode [class*="progress"]:not([class*="fill"]) { background: #E7DDD0 !important; }' +
    'body.light-mode .hint, body.light-mode .tip, body.light-mode blockquote, body.light-mode .note, body.light-mode .info, body.light-mode .insight-card { background: #FFF8F0 !important; border-color: #D97706 !important; color: #78350F !important; }' +

    /* ═══ HEADER ═══════════════════════════════════════════ */
    '#imx-game-header {' +
      'position: sticky; top: 0; z-index: 999;' +
      'display: flex; align-items: center; justify-content: space-between;' +
      'padding: 0.5rem 1.25rem;' +
      'background: #0F172A; border-bottom: 1px solid rgba(255,255,255,0.08);' +
    '}' +
    'body.light-mode #imx-game-header { background: #FFFBF5; border-bottom-color: #E7DDD0; }' +
    '.imx-gh-logo { display: flex; align-items: center; gap: 0.5rem; text-decoration: none; color: #F8FAFC; font-weight: 700; font-size: 1rem; }' +
    'body.light-mode .imx-gh-logo { color: #1A1207; }' +
    '.imx-gh-logo img { width: 32px; height: 32px; border-radius: 6px; }' +
    '.imx-gh-right { display: flex; align-items: center; gap: 0.75rem; }' +
    '.imx-gh-link { color: #94A3B8; text-decoration: none; font-size: 0.85rem; font-weight: 500; transition: color 0.2s; }' +
    '.imx-gh-link:hover { color: #F59E0B; }' +
    'body.light-mode .imx-gh-link { color: #78350F; }' +

    /* Theme toggle group */
    '.imx-gh-theme-group { display: flex; gap: 2px; background: rgba(255,255,255,0.08); border-radius: 8px; padding: 2px; }' +
    'body.light-mode .imx-gh-theme-group { background: #E7DDD0; }' +
    '.imx-theme-btn { background: none; border: none; border-radius: 6px; width: 32px; height: 32px; cursor: pointer; color: #94A3B8; display: flex; align-items: center; justify-content: center; transition: all 0.2s; }' +
    '.imx-theme-btn:hover { color: #F1F5F9; background: rgba(255,255,255,0.1); }' +
    '.imx-theme-btn.active { background: rgba(245,158,11,0.2); color: #F59E0B; }' +
    'body.light-mode .imx-theme-btn { color: #92400E; }' +
    'body.light-mode .imx-theme-btn:hover { color: #1A1207; background: rgba(139,90,43,0.1); }' +
    'body.light-mode .imx-theme-btn.active { background: rgba(217,119,6,0.2); color: #B45309; }' +
    '.imx-theme-btn svg { stroke-linecap: round; stroke-linejoin: round; }' +

    /* ═══ DECORATIVE ELEMENTS ═════════════════════════════ */

    /* Indian folk art motifs — high z-index so they float above game content */
    '.imx-game-motif { position: fixed; pointer-events: none; z-index: 9998; opacity: 0.6; }' +
    '.imx-game-motif svg { width: 100%; height: 100%; }' +
    '.imx-motif-warli { bottom: 0; left: 0; width: 420px; height: 320px; color: #F59E0B; }' +
    'body.light-mode .imx-motif-warli { color: #92400E; }' +
    '.imx-motif-madhubani { top: 60px; right: 0; width: 100px; height: 420px; }' +
    '.imx-motif-gond { bottom: 2%; right: 2%; width: 220px; height: 280px; color: #94A3B8; animation: imx-sway 30s ease-in-out infinite; }' +
    'body.light-mode .imx-motif-gond { color: #78350F; }' +
    '.imx-motif-kolam { position: relative !important; z-index: auto !important; opacity: 1 !important; width: 100%; height: 40px; pointer-events: none; }' +
    '.imx-motif-kolam svg { width: 100%; height: 100%; }' +
    '@keyframes imx-sway { 0%,100% { transform: rotate(0deg); } 50% { transform: rotate(1.5deg); } }' +

    /* ═══ FOOTER ═══════════════════════════════════════════ */
    '#imx-game-footer { margin-top: 3rem; padding: 2rem 1.25rem; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; font-size: 0.8rem; color: #94A3B8; }' +
    'body.light-mode #imx-game-footer { border-top-color: #E7DDD0; }' +
    'body.light-mode #imx-game-footer, body.light-mode #imx-game-footer p { color: #92400E !important; }' +
    '.imx-gf-inner { max-width: 700px; margin: 0 auto; }' +
    '.imx-gf-divider { height: 2px; background: linear-gradient(90deg, transparent, #D97706 20%, #DC2626 40%, #EC4899 60%, #8B5CF6 80%, transparent); margin-bottom: 1.5rem; opacity: 0.3; border-radius: 1px; }' +
    'body.light-mode .imx-gf-divider { opacity: 0.5; }' +
    '.imx-gf-inner a { color: #F59E0B; text-decoration: none; }' +
    'body.light-mode .imx-gf-inner a { color: #B45309; }' +
    '.imx-gf-inner a:hover { text-decoration: underline; }' +
    '.imx-gf-links { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem 1rem; margin: 0.75rem 0; }' +
    '.imx-gf-copy { margin-top: 0.5rem; opacity: 0.6; }' +

    /* ═══ GAMIFICATION & VISUAL ENHANCEMENTS ═══════════════ */

    /* Button interactions */
    'button:not(.imx-theme-btn) { transition: all 0.2s ease; }' +
    'button:not(.imx-theme-btn):hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(245,158,11,0.2); }' +
    'button:not(.imx-theme-btn):active { transform: translateY(0) scale(0.97); }' +

    /* Animations */
    '@keyframes imx-celebrate { 0% { transform: scale(0.8) rotate(-3deg); opacity: 0; } 60% { transform: scale(1.08) rotate(1deg); } 100% { transform: scale(1) rotate(0); opacity: 1; } }' +
    '@keyframes imx-glow { 0%,100% { box-shadow: 0 0 8px rgba(245,158,11,0.3); } 50% { box-shadow: 0 0 24px rgba(245,158,11,0.5); } }' +
    '@keyframes imx-confetti { 0% { opacity: 1; transform: translateY(0) rotate(0); } 100% { opacity: 0; transform: translateY(-60px) rotate(360deg); } }' +

    /* Cards — warmer borders, more depth */
    '[class*="card"], .card { transition: all 0.25s ease; border-radius: 12px !important; }' +
    '[class*="card"]:hover, .card:hover { transform: translateY(-3px); box-shadow: 0 8px 30px rgba(0,0,0,0.2); }' +
    'body.light-mode [class*="card"]:hover, body.light-mode .card:hover { box-shadow: 0 8px 30px rgba(139,90,43,0.12); }' +

    /* Choice cards — distinct warm colors */
    '.choice-card:nth-child(1), [class*="option"]:nth-child(1) { border-left: 4px solid #D97706 !important; }' +
    '.choice-card:nth-child(2), [class*="option"]:nth-child(2) { border-left: 4px solid #059669 !important; }' +
    '.choice-card:nth-child(3), [class*="option"]:nth-child(3) { border-left: 4px solid #DC2626 !important; }' +
    '.choice-card:nth-child(4), [class*="option"]:nth-child(4) { border-left: 4px solid #7C3AED !important; }' +

    /* Agent/opponent — indigo accent */
    '.agent-card, [class*="agent"], [class*="opponent"] { border-left: 4px solid #6366F1 !important; }' +

    /* Results — celebration pop */
    '.result, [class*="result"], [class*="outcome"] { animation: imx-celebrate 0.5s ease-out; }' +

    /* Scores — golden emphasis */
    '.score, [class*="score"], [class*="points"], [class*="payoff"] { font-weight: 700; font-size: 1.15em; color: #F59E0B !important; }' +
    'body.light-mode .score, body.light-mode [class*="score"], body.light-mode [class*="points"], body.light-mode [class*="payoff"] { color: #B45309 !important; }' +

    /* Progress bars — warm gradient */
    '.progress-fill, [class*="progress-fill"], [class*="bar-fill"] { background: linear-gradient(90deg, #D97706, #059669) !important; border-radius: 999px; transition: width 0.6s ease; }' +

    /* Welcome/title — folk art inspired gradient */
    '.welcome-title, .game-title { background: linear-gradient(135deg, #D97706, #DC2626, #EC4899, #7C3AED); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }' +
    'body.light-mode .welcome-title, body.light-mode .game-title { background: linear-gradient(135deg, #92400E, #991B1B, #BE185D, #5B21B6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }' +

    /* CTA buttons — warm gradient */
    '.btn-primary, .start-btn, [class*="start"], [class*="play"], [class*="begin"] { background: linear-gradient(135deg, #D97706, #B45309) !important; color: #FFFFFF !important; border: none !important; box-shadow: 0 4px 15px rgba(217,119,6,0.3); }' +
    '.btn-primary:hover, .start-btn:hover, [class*="start"]:hover, [class*="play"]:hover, [class*="begin"]:hover { background: linear-gradient(135deg, #F59E0B, #D97706) !important; box-shadow: 0 6px 20px rgba(245,158,11,0.4); }' +

    /* ═══ MOBILE ═══════════════════════════════════════════ */
    '@media (max-width: 640px) {' +
      '#imx-game-header { padding: 0.4rem 0.75rem; }' +
      '.imx-gh-logo span { font-size: 0.9rem; }' +
      '.imx-gh-link { display: none; }' +
      '.imx-motif-warli { width: 200px; height: 150px; }' +
      '.imx-motif-madhubani { width: 45px; height: 200px; }' +
      '.imx-motif-gond { width: 110px; height: 140px; }' +
      '.imx-theme-btn { width: 28px; height: 28px; }' +
      '.imx-theme-btn svg { width: 14px; height: 14px; }' +
      /* Mobile game layout helpers */
      '.container { padding: 0 0.75rem !important; }' +
      'h1 { font-size: 1.5rem !important; }' +
      'h2 { font-size: 1.2rem !important; }' +
      '.welcome-header h1 { font-size: clamp(1.4rem, 5vw, 2rem) !important; }' +
      /* Ensure game cards stack vertically on mobile */
      '.choice-grid, .options-grid, .grid, [class*="grid"]:not(#imx-game-header) { grid-template-columns: 1fr !important; }' +
      '[class*="flex-row"], [class*="row"]:not(tr) { flex-direction: column !important; }' +
      /* Tables scroll horizontally */
      'table { display: block; overflow-x: auto; -webkit-overflow-scrolling: touch; }' +
      /* Stat cards wrap */
      '.stats, .stat-row, [class*="stats"] { flex-wrap: wrap !important; gap: 0.5rem !important; }' +
      '.stat { min-width: 80px !important; flex: 1 1 45% !important; }' +
    '}' +
    '@media (max-width: 380px) {' +
      '.imx-motif-warli, .imx-motif-madhubani, .imx-motif-gond { display: none; }' +
      '.imx-gh-logo img { width: 24px; height: 24px; }' +
      '.imx-gh-logo span { font-size: 0.8rem; }' +
    '}';
  document.head.appendChild(css);

  // ── JS-based contrast fixer ──────────────────────────────
  // Runs after page load to catch inline styles the CSS can't override
  function fixDarkContrast() {
    if (document.body.classList.contains('light-mode')) return;

    // Map of low-contrast colors → readable replacements
    var fixes = {
      '#64748b': '#CBD5E1', '#64748B': '#CBD5E1',
      '#374151': '#CBD5E1', '#4b5563': '#CBD5E1', '#4B5563': '#CBD5E1',
      '#6b7280': '#CBD5E1', '#6B7280': '#CBD5E1',
      '#475569': '#94A3B8',
      '#334155': '#94A3B8',
      '#1f2937': '#CBD5E1', '#1F2937': '#CBD5E1',
      'rgb(100, 116, 139)': '#CBD5E1',
      'rgb(55, 65, 81)': '#CBD5E1',
      'rgb(75, 85, 99)': '#CBD5E1'
    };

    document.querySelectorAll('[style]').forEach(function(el) {
      if (el.closest('#imx-game-header') || el.closest('#imx-game-footer')) return;
      var s = el.style;
      if (s.color) {
        var c = s.color.toLowerCase();
        Object.keys(fixes).forEach(function(bad) {
          if (c === bad.toLowerCase() || c === bad) {
            s.setProperty('color', fixes[bad], 'important');
          }
        });
      }
    });
  }

  // Run after page fully loads and on theme change
  var origSetTheme = setTheme;
  setTheme = function(pref) {
    origSetTheme(pref);
    setTimeout(fixDarkContrast, 50);
  };

  if (document.readyState === 'complete') {
    fixDarkContrast();
  } else {
    window.addEventListener('load', fixDarkContrast);
  }
  // Also re-run periodically for dynamically added content
  setTimeout(fixDarkContrast, 1000);
  setTimeout(fixDarkContrast, 3000);
})();
