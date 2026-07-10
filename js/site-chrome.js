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
  if (isHome) return;

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
'.im-sc-foot-col h4{font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:var(--sc-mut);margin:0 0 10px;font-weight:700}',
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
  var SI = 'https://cdn.jsdelivr.net/npm/sargam-icons@1.6.6/Icons/Line/';
  // alt defaults to "" (decorative — the button carries a visible label or an aria-label
  // on a <button>). Pass an explicit alt for icon-only <a> links: HTMLCS H30.2 requires the
  // sole <img> content of a link to have non-empty alt text (a link's aria-label doesn't count).
  function ic(name, alt) { return '<img class="im-sc-i" src="' + SI + name + '.svg" alt="' + (alt || '') + '" width="15" height="15" loading="lazy" onerror="this.style.display=\'none\'">'; }
  var I = {
    globe: ic('si_Globe_detailed'), star: ic('si_Star'), info: ic('si_Info'), home: ic('si_Home', 'Home'),
    sys: ic('si_Monitor'), sun: ic('si_Sun'), moon: ic('si_Moon')
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
        '<button class="im-sc-btn im-sc-lang" type="button" aria-label="Language">' + I.globe + '<span class="im-sc-label">Language</span></button>' +
        '<a class="im-sc-btn im-sc-prem" href="' + SITE + '/premium.html">' + I.star + '<span class="im-sc-label">Premium</span></a>' +
        '<a class="im-sc-btn" href="' + SITE + '/about.html">' + I.info + '<span class="im-sc-label">About</span></a>' +
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
        '<div class="im-sc-foot-col"><h4>Learn</h4>' +
          '<a href="' + SITE + '/courses/">Flagship Courses</a><a href="' + SITE + '/101-courses/">101 Series</a>' +
          '<a href="' + SITE + '/Labs/">Labs</a><a href="' + SITE + '/catalog.html">Full Catalog</a></div>' +
        '<div class="im-sc-foot-col"><h4>Explore</h4>' +
          '<a href="' + SITE + '/dataverse.html">Dataverse</a><a href="' + SITE + '/dojos.html">Dojos &amp; Practice</a>' +
          '<a href="' + SITE + '/BookSummaries/">Reading Companions</a><a href="' + SITE + '/blog.html">Blog</a></div>' +
        '<div class="im-sc-foot-col"><h4>ImpactMojo</h4>' +
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
    bar.querySelector('.im-sc-lang').addEventListener('click', function () {
      if (typeof window.ImpactMojoTranslate === 'function') return window.ImpactMojoTranslate();
      var w = document.querySelector('[data-sarvam-widget],.sarvam-translate,#sarvam-translate,.translate-widget');
      if (w) { w.scrollIntoView({ behavior: 'smooth' }); w.click && w.click(); return; }
      document.dispatchEvent(new CustomEvent('im:open-language'));
    });
  }

  function escapeHtml(s) { return String(s).replace(/[&<>"]/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]; }); }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();
})();
