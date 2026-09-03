/**
 * ImpactMojo Site Chrome — one standard thin top bar + footer for every page.
 * Version 1.0.0 — July 2026
 *
 * Drop-in: add <script src="/js/site-chrome.js" defer></script> to any page.
 * The script (1) removes whatever legacy top bar / footer the page already has,
 * (2) injects the standard thin top bar and standard footer, and (3) wires the
 * theme buttons to the same contract as theme.js (localStorage 'impactmojo-theme'
 * + data-theme on <html>). All future chrome changes happen in this one file.
 *
 * Top bar (left→right): logo + "impactmojo.in/<page>" breadcrumb · [spacer] ·
 *   Language · Premium · About · light/dark toggle · Home.
 * Footer: link columns + licence line.
 *
 * Opt out (homepage only): put data-im-home on <html> or <body>, or set
 *   <meta name="im-chrome" content="off">.
 * Page name: from <meta name="im-page" content="…"> if present, else derived
 *   from <title> (text before the first | or —), else the <h1>, else the path.
 */
(function () {
  'use strict';
  if (window.__imChrome) return;
  window.__imChrome = true;

  var root = document.documentElement;
  var meta = function (n) { var m = document.querySelector('meta[name="' + n + '"]'); return m && m.getAttribute('content'); };

  // ── Opt-out (homepage) ─────────────────────────────────────────────
  var path = location.pathname.replace(/index\.html$/, '');
  var isHome = root.hasAttribute('data-im-home') || (document.body && document.body.hasAttribute('data-im-home'))
    || meta('im-chrome') === 'off' || path === '/' || path === '';
  // Note: on the homepage (isHome) we keep the page's own chrome and skip build(),
  // but the shared WhatsApp share button (below) is still injected on every page.

  // ── Page name for the breadcrumb ───────────────────────────────────
  function pageName() {
    var m = meta('im-page'); if (m) return m;
    var t = (document.title || '').split(/[|—–]/)[0].trim();
    if (t && t.length <= 60) return t;
    var h1 = document.querySelector('h1'); if (h1 && h1.textContent.trim()) return h1.textContent.trim().slice(0, 48);
    var seg = path.split('/').filter(Boolean).pop() || '';
    return seg.replace(/[-_]/g, ' ').replace(/\.html$/, '').replace(/\b\w/g, function (c) { return c.toUpperCase(); }) || 'Page';
  }
  var SITE = ''; // root-relative so links work from any page depth and on any host

  // ── Styles ─────────────────────────────────────────────────────────
  function css() {
    return [
'.im-sc,.im-sc *{box-sizing:border-box}',
'.im-sc{--sc-bg:rgba(255,255,255,.82);--sc-fg:#0F172A;--sc-mut:#64748B;--sc-bd:#E7EBF0;--sc-acc:#0EA5E9;--sc-grad:linear-gradient(135deg,#0EA5E9,#6366F1)}',
'html[data-theme="dark"] .im-sc,html.dark .im-sc{--sc-bg:rgba(11,17,32,.85);--sc-fg:#F1F5F9;--sc-mut:#94A3B8;--sc-bd:#25304A}',
'@media(prefers-color-scheme:dark){html:not([data-theme]) .im-sc{--sc-bg:rgba(11,17,32,.85);--sc-fg:#F1F5F9;--sc-mut:#94A3B8;--sc-bd:#25304A}}',
'.im-sc-bar{position:sticky;top:0;z-index:9999;display:flex;align-items:center;gap:12px;height:46px;padding:0 clamp(12px,3vw,24px);',
 'background:var(--sc-bg);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--sc-bd);',
 "font-family:'Inter',system-ui,-apple-system,sans-serif;font-size:13px;color:var(--sc-fg)}",
'.im-sc-crumb{display:flex;align-items:center;gap:9px;text-decoration:none;color:var(--sc-fg);min-width:0}',
'.im-sc-crumb img{width:22px;height:22px;border-radius:5px;flex:none}',
'.im-sc-site{font-weight:800;letter-spacing:-.2px;background:var(--sc-grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;white-space:nowrap}',
'.im-sc-path{color:var(--sc-mut);font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}',
'.im-sc-path b{color:var(--sc-fg);font-weight:700}',
'.im-sc-spacer{flex:1}',
'.im-sc-right{display:flex;align-items:center;gap:4px}',
'.im-sc-btn{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 11px;border-radius:8px;border:1px solid transparent;',
 'background:transparent;color:var(--sc-fg);font:600 12.5px/1 inherit;text-decoration:none;cursor:pointer;white-space:nowrap;transition:background .15s,border-color .15s}',
'.im-sc-btn:hover{background:color-mix(in srgb,var(--sc-acc) 10%,transparent);border-color:color-mix(in srgb,var(--sc-acc) 30%,transparent);color:var(--sc-acc)}',
'.im-sc-i{width:15px;height:15px;flex:none;filter:brightness(0) saturate(100%);opacity:.78}',
'html[data-theme="dark"] .im-sc .im-sc-i,html.dark .im-sc .im-sc-i{filter:brightness(0) saturate(100%) invert(1);opacity:.85}',
'@media(prefers-color-scheme:dark){html:not([data-theme]) .im-sc .im-sc-i{filter:brightness(0) saturate(100%) invert(1);opacity:.85}}',
'.im-sc-btn:hover .im-sc-i{opacity:1}',
'.im-sc-btn.im-sc-prem{background:linear-gradient(135deg,#F59E0B,#EF4444);color:#fff}',
'.im-sc-btn.im-sc-prem:hover{opacity:.92;color:#fff}',
'.im-sc-prem .im-sc-i,.im-sc-tbtn[aria-pressed="true"] .im-sc-i{filter:brightness(0) invert(1)!important;opacity:1}',
'.im-sc-icon{width:34px;height:32px;padding:0;justify-content:center}',
'.im-sc-theme{display:inline-flex;gap:2px;background:color-mix(in srgb,var(--sc-fg) 6%,transparent);border:1px solid var(--sc-bd);border-radius:9px;padding:3px}',
'.im-sc-tbtn{width:26px;height:24px;border:0;border-radius:6px;background:transparent;cursor:pointer;display:inline-flex;align-items:center;justify-content:center}',
'.im-sc-tbtn[aria-pressed="true"]{background:var(--sc-grad);color:#fff}',
'@media(max-width:720px){.im-sc-label{display:none}.im-sc-btn{padding:0 8px}.im-sc-icon{width:32px}.im-sc-path{display:none}}',
// Phones: the full control row + wordmark overflow a narrow bar, which collapses
// the flex spacer and jams the language globe against the "impactmojo.in" wordmark
// (reads like "impactmojo.<globe>"). Drop the bar wordmark below 600px — the logo
// stays as the brand/home link — so the bar fits and the spacer pushes controls right.
'@media(max-width:600px){.im-sc-bar{gap:8px;padding:0 12px}.im-sc-bar .im-sc-site{display:none}.im-sc-theme{padding:2px}.im-sc-tbtn{width:24px}}',
// footer
'.im-sc-foot{background:var(--sc-bg);border-top:1px solid var(--sc-bd);color:var(--sc-fg);font-family:\'Inter\',system-ui,sans-serif;padding:40px clamp(16px,4vw,32px) 28px;margin-top:48px}',
'html[data-theme="dark"] .im-sc-foot,html.dark .im-sc-foot{--sc-bg:#0B1120}',
'.im-sc-foot-in{max-width:1180px;margin:0 auto;display:flex;flex-wrap:wrap;gap:28px 48px;justify-content:space-between}',
'.im-sc-foot-brand{max-width:280px}',
'.im-sc-foot-brand .im-sc-site{font-size:18px}',
'.im-sc-foot-brand p{margin:8px 0 0;color:var(--sc-mut);font-size:13px;line-height:1.6}',
'.im-sc-foot-col h3{font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:var(--sc-mut);margin:0 0 10px;font-weight:700}',
'.im-sc-foot-col a{display:block;color:var(--sc-fg);text-decoration:none;font-size:13.5px;font-weight:500;padding:4px 0}',
'.im-sc-foot-col a:hover{color:var(--sc-acc)}',
'.im-sc-foot-meta{max-width:1180px;margin:26px auto 0;padding-top:18px;border-top:1px solid var(--sc-bd);color:var(--sc-mut);',
 'font-size:12px;display:flex;flex-wrap:wrap;gap:8px 18px;justify-content:space-between;align-items:center}',
'@media(prefers-reduced-motion:reduce){.im-sc *{transition:none!important}}',
// reconcile app-like pages (course shells): kill dead reserved padding + offset fixed sidebar/progress below the 46px bar
'body.im-sc-on{padding-top:0!important}',
'body.im-sc-on .sidebar{top:46px!important;height:calc(100dvh - 46px)!important}',
'body.im-sc-on .sidebar-overlay{top:46px!important}',
'body.im-sc-on .reading-progress{top:46px!important}'
    ].join('');
  }

  // ── Icons: Sargam (site-standard), recoloured to the bar's fg via CSS filter ──
  var SI = 'https://cdn.jsdelivr.net/npm/sargam-icons@1.6.7/Icons/Line/';
  // alt defaults to "" (decorative — the button carries a visible label or an aria-label
  // on a <button>). Pass an explicit alt for icon-only <a> links: HTMLCS H30.2 requires the
  // sole <img> content of a link to have non-empty alt text (a link's aria-label doesn't count).
  function ic(name, alt) { return '<img class="im-sc-i" src="' + SI + name + '.svg" alt="' + (alt || '') + '" width="15" height="15" loading="lazy" onerror="this.style.display=\'none\'">'; }
  var I = {
    globe: ic('si_Globe_detailed'), star: ic('si_Star'), info: ic('si_Info'), home: ic('si_Home', 'Home'),
    sys: ic('si_Monitor'), sun: ic('si_Sun'), moon: ic('si_Moon'), search: ic('si_Search')
  };
  var LOGO = SITE + '/assets/images/apple-touch-icon.png'; // 7KB vs the 599KB full logo

  // ── Theme (same contract as theme.js) ──────────────────────────────
  function applyTheme(mode) {
    try { localStorage.setItem('impactmojo-theme', mode); } catch (e) {}
    var resolved = mode === 'system'
      ? (window.matchMedia && matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light')
      : mode;
    if (mode === 'system') root.removeAttribute('data-theme'); else root.setAttribute('data-theme', resolved);
    root.classList.toggle('dark', resolved === 'dark');
    syncTheme(mode);
  }
  function currentMode() { try { return localStorage.getItem('impactmojo-theme') || 'system'; } catch (e) { return 'system'; } }
  function syncTheme(mode) {
    var btns = document.querySelectorAll('.im-sc-tbtn');
    for (var i = 0; i < btns.length; i++) btns[i].setAttribute('aria-pressed', btns[i].getAttribute('data-m') === mode ? 'true' : 'false');
  }

  // ── Build ──────────────────────────────────────────────────────────
  function build() {
    // 1. remove legacy chrome (broad: catches the many header/footer patterns across the site)
    var sel = '.im-topbar,#imTopbar,.top-nav,.site-header,header.header,.navbar,.site-nav,.main-nav,'
            + '.nav-container,.masthead,header.mobile-header,.mobile-header,'
            + 'footer,.footer,.foot,.site-footer,.im-footer';
    var kill = [].slice.call(document.querySelectorAll(sel));
    // also any top-level <header>/<nav> that's a direct child of <body> (the site bar)
    [].slice.call(document.body.children).forEach(function (el) {
      var t = el.tagName; if ((t === 'HEADER' || t === 'NAV') && kill.indexOf(el) === -1) kill.push(el);
    });
    for (var i = 0; i < kill.length; i++) { if (kill[i].closest && kill[i].closest('.im-sc')) continue; kill[i].parentNode && kill[i].parentNode.removeChild(kill[i]); }

    // 2. styles
    var st = document.createElement('style'); st.id = 'im-sc-style'; st.textContent = css(); document.head.appendChild(st);
    document.body.classList.add('im-sc-on');

    // 3. top bar
    var bar = document.createElement('div');
    bar.className = 'im-sc im-sc-bar'; bar.setAttribute('role', 'navigation'); bar.setAttribute('aria-label', 'Site');
    bar.innerHTML =
      '<a class="im-sc-crumb" href="/" aria-label="ImpactMojo home">' +
        '<img src="' + LOGO + '" alt="" width="22" height="22" onerror="this.style.display=\'none\'">' +
        '<span class="im-sc-site">impactmojo.in</span>' +
        '<span class="im-sc-path">/&nbsp;<b>' + escapeHtml(pageName()) + '</b></span>' +
      '</a>' +
      '<span class="im-sc-spacer"></span>' +
      '<div class="im-sc-right">' +
        '<button class="im-sc-btn im-sc-search" type="button" aria-label="Search the site">' + I.search + '<span class="im-sc-label">Search</span></button>' +
        '<button class="im-sc-btn im-sc-lang" type="button" aria-label="Language">' + I.globe + '<span class="im-sc-label">Language</span></button>' +
        '<a class="im-sc-btn im-sc-prem" href="' + SITE + '/premium.html" aria-label="Premium">' + I.star + '<span class="im-sc-label">Premium</span></a>' +
        '<a class="im-sc-btn" href="' + SITE + '/about.html" aria-label="About">' + I.info + '<span class="im-sc-label">About</span></a>' +
        '<div class="im-sc-theme" role="group" aria-label="Theme">' +
          '<button class="im-sc-tbtn" data-m="system" title="System" aria-label="System theme">' + I.sys + '</button>' +
          '<button class="im-sc-tbtn" data-m="light" title="Light" aria-label="Light theme">' + I.sun + '</button>' +
          '<button class="im-sc-tbtn" data-m="dark" title="Dark" aria-label="Dark theme">' + I.moon + '</button>' +
        '</div>' +
        '<a class="im-sc-btn im-sc-icon" href="' + SITE + '/" title="Home" aria-label="Home">' + I.home + '</a>' +
      '</div>';
    document.body.insertBefore(bar, document.body.firstChild);

    // 4. footer
    var foot = document.createElement('footer');
    foot.className = 'im-sc im-sc-foot'; foot.setAttribute('role', 'contentinfo');
    foot.innerHTML =
      '<div class="im-sc-foot-in">' +
        '<div class="im-sc-foot-brand"><span class="im-sc-site">impactmojo.in</span>' +
          '<p>Free, open-source development education for South Asia &mdash; flagship courses, 101 decks, labs, games and research tools.</p></div>' +
        '<div class="im-sc-foot-col"><h3>Learn</h3>' +
          '<a href="' + SITE + '/courses/">Flagship Courses</a><a href="' + SITE + '/101-courses/">101 Series</a>' +
          '<a href="' + SITE + '/Labs/">Studios</a><a href="' + SITE + '/teach.html">Teach with ImpactMojo</a>' +
          '<a href="' + SITE + '/teaching-principles.html">Teaching Principles</a>' +
          '<a href="' + SITE + '/catalog.html">Full Catalog</a></div>' +
        '<div class="im-sc-foot-col"><h3>Explore</h3>' +
          '<a href="' + SITE + '/libraries.html"><b>All Libraries</b></a><a href="' + SITE + '/dataverse.html">Dataverse</a>' +
          '<a href="' + SITE + '/BookSummaries/">Reading Companions</a><a href="' + SITE + '/law-guides/">Law Guides</a>' +
          '<a href="' + SITE + '/law-guides/development-law-docket.html">Law Docket</a>' +
          '<a href="' + SITE + '/fundamentals/">Fundamentals</a>' +
          '<a href="' + SITE + '/dojos.html">Dojos &amp; Practice</a>' +
          '<a href="' + SITE + '/blog.html">Blog</a></div>' +
        '<div class="im-sc-foot-col"><h3>ImpactMojo</h3>' +
          '<a href="' + SITE + '/about.html">About</a><a href="' + SITE + '/premium.html">Premium</a>' +
          '<a href="' + SITE + '/community.html">Community</a><a href="https://github.com/ImpactMojo/ImpactMojo">GitHub</a></div>' +
      '</div>' +
      '<div class="im-sc-foot-meta"><span>CC BY-NC-ND 4.0 &middot; Free Forever &middot; &copy; ImpactMojo</span>' +
        '<span>Made for South Asian development practitioners</span></div>';
    document.body.appendChild(foot);

    // 5. wire theme
    syncTheme(currentMode());
    bar.querySelectorAll('.im-sc-tbtn').forEach(function (b) {
      b.addEventListener('click', function () { applyTheme(b.getAttribute('data-m')); });
    });
    if (window.matchMedia) matchMedia('(prefers-color-scheme:dark)').addEventListener('change', function () {
      if (currentMode() === 'system') applyTheme('system');
    });

    // 6. language: reuse translate-sarvam if present, else open a language page
    bar.querySelector('.im-sc-search').addEventListener('click', function () {
      // search.js ships on a minority of pages; lazy-load it on demand
      if (window.ImpactMojoSearch && window.ImpactMojoSearch.open) return window.ImpactMojoSearch.open();
      var s = document.createElement('script');
      s.src = '/js/search.js';
      s.onload = function () {
        if (window.ImpactMojoSearch && window.ImpactMojoSearch.open) window.ImpactMojoSearch.open();
      };
      document.head.appendChild(s);
    });
    bar.querySelector('.im-sc-lang').addEventListener('click', function () {
      if (typeof window.ImpactMojoTranslate === 'function') return window.ImpactMojoTranslate();
      var w = document.querySelector('[data-sarvam-widget],.sarvam-translate,#sarvam-translate,.translate-widget');
      if (w) { w.scrollIntoView({ behavior: 'smooth' }); w.click && w.click(); return; }
      document.dispatchEvent(new CustomEvent('im:open-language'));
    });
  }

  function escapeHtml(s) { return String(s).replace(/[&<>"]/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]; }); }

  // ── Shared WhatsApp "share ImpactMojo" button — every page, homepage included ──
  // Pre-encoded href (no emoji literals in source) matching the site-standard share
  // message. Guarded against duplicates; skipped if the page already has one.
  function injectWhatsApp() {
    if (!document.body || document.getElementById('im-wa-fab')) return;
    var a = document.createElement('a');
    a.id = 'im-wa-fab';
    a.href = 'https://wa.me/?text=%F0%9F%8E%93%20I%27ve%20been%20learning%20with%20ImpactMojo%20%E2%80%94%20a%20free%2C%20open-source%20learning%20platform%20for%20the%20development%20sector%2C%20made%20in%20South%20Asia.%0A%0A%F0%9F%93%9A%2069%20free%20courses%20%E2%80%94%20economics%2C%20gender%2C%20policy%2C%20MEL%20%26%20more%0A%F0%9F%A7%AA%2035%20hands-on%20labs%20%2B%20playable%20economics%20games%0A%F0%9F%93%8A%20A%20321-tool%20data%20library%2C%20book%20companions%20%26%20lexicons%0A%F0%9F%94%93%20No%20paywalls%2C%20no%20sign-up%20walls%20%E2%80%94%20genuinely%20free%2C%20forever%0A%0AIf%20you%20work%20in%20development%20%28or%20want%20to%29%2C%20take%20a%20look%20%F0%9F%91%87%0Ahttps%3A%2F%2Fwww.impactmojo.in';
    a.target = '_blank'; a.rel = 'noopener noreferrer';
    a.setAttribute('aria-label', 'Share ImpactMojo on WhatsApp');
    a.title = 'Share ImpactMojo on WhatsApp';
    // Bottom-RIGHT corner: the bottom-left is the cookie-consent / learning-tools
    // speed-dial stack (see css/cookie.css) — placing the share FAB there covered
    // the cookie button. The language switcher sits higher on the right (bottom:5.5rem),
    // so this lower-right slot is clear on every page and viewport.
    // Stack above the Mojini chat FAB when a page has one (both live bottom-right)
    var waBottom = document.getElementById('mojini-chat-toggle') || document.querySelector('.feedback-fab') ? '92px' : '18px';
    a.style.cssText = 'position:fixed;right:18px;bottom:' + waBottom + ';z-index:9998;width:52px;height:52px;border-radius:50%;background:#25D366;box-shadow:0 6px 20px rgba(37,211,102,.45);display:flex;align-items:center;justify-content:center;text-decoration:none;transition:transform .15s ease';
    a.addEventListener('mouseenter', function () { a.style.transform = 'scale(1.08)'; });
    a.addEventListener('mouseleave', function () { a.style.transform = 'scale(1)'; });
    a.innerHTML = '<svg viewBox="0 0 24 24" width="28" height="28" fill="#fff" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>';
    var wrap = document.createElement('aside');
    wrap.setAttribute('aria-label', 'Share ImpactMojo');
    wrap.appendChild(a);
    document.body.appendChild(wrap);
  }

  // Register the service worker everywhere the chrome loads. js/pwa.js only
  // ships on ~23 pages; without this, most entry points never get offline
  // support or CDN caching. Guarded so pages that DO load pwa.js don't
  // double-register (register() with the same scope is idempotent anyway).
  function registerSW() {
    if (!('serviceWorker' in navigator)) return;
    if (location.protocol !== 'https:' && location.hostname !== 'localhost') return;
    try { navigator.serviceWorker.register('/service-worker.js'); } catch (e) { /* non-fatal */ }
  }

  function boot() { injectWhatsApp(); registerSW(); if (!isHome) build(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
