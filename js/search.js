/* ============================================================
   ImpactMojo Global Search — Ctrl+K / Cmd+K
   Uses Fuse.js for fuzzy matching across all content
   ============================================================ */
(function () {
  'use strict';

  var FUSE_CDN = 'https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js';
  var INDEX_URL = '/data/search-index.json';

  var fuse = null;
  var searchData = null;
  var modal = null;
  var input = null;
  var resultsList = null;
  var selectedIndex = -1;
  var visible = false;

  var SARGAM_CDN = 'https://cdn.jsdelivr.net/npm/sargam-icons@1.6.7/Icons/Line/';
  function sargamImg(name) {
    return '<img src="' + SARGAM_CDN + name + '.svg" alt="" style="width:18px;height:18px;filter:brightness(0) invert(1);" loading="lazy">';
  }

  var TYPE_META = {
    bct:       { icon: sargamImg('si_Fact_check'),  label: 'BCT Technique', color: '#EC4899' },
    dataverse: { icon: sargamImg('si_Bar_chart'),   label: 'Dataverse',     color: '#6366F1' },
    course:    { icon: sargamImg('si_Book'),         label: 'Course',        color: '#0EA5E9' },
    game:      { icon: sargamImg('si_Activity'),     label: 'Game',          color: '#F59E0B' },
    lab:       { icon: sargamImg('si_Wrench'),          label: 'Studio',           color: '#10B981' },
    page:      { icon: sargamImg('si_Article'),      label: 'Page',          color: '#8B5CF6' },
    'book-summary':  { icon: sargamImg('si_Book'),          label: 'Reading Companion', color: '#D97706' },
    blog:            { icon: sargamImg('si_Article'),       label: 'Blog Post',         color: '#0891B2' },
    'deep-dive':     { icon: sargamImg('si_Library_books'), label: 'Deep Dive',         color: '#7C3AED' },
    product:         { icon: sargamImg('si_Bag'),           label: 'Product',           color: '#DB2777' },
    'practice-pack': { icon: sargamImg('si_Fact_check'),    label: 'Practice Pack',     color: '#059669' },
    tool:            { icon: sargamImg('si_Wrench'),        label: 'Tool',              color: '#2563EB' },
    'data-dive':     { icon: sargamImg('si_Bar_chart'),     label: 'Data Note',         color: '#4F46E5' },
    timeline:        { icon: sargamImg('si_Timer'),         label: 'Timeline',          color: '#B45309' },
    poster:          { icon: sargamImg('si_Image'),         label: 'Poster',            color: '#BE185D' },
    reference:       { icon: sargamImg('si_Library_books'), label: 'Reference',         color: '#0D9488' },
    handout:         { icon: sargamImg('si_File_download'), label: 'Handout',           color: '#65A30D' },
    challenge:       { icon: sargamImg('si_Flag'),          label: 'Challenge',         color: '#DC2626' },
    showcase:        { icon: sargamImg('si_Image'),          label: 'Work Sample',       color: '#7C2D12' },
    special:         { icon: sargamImg('si_Library_books'), label: 'Special',           color: '#9333EA' }
  };

  /* ---- Load Fuse.js ---- */
  function loadFuse(cb) {
    if (window.Fuse) return cb();
    var s = document.createElement('script');
    s.src = FUSE_CDN;
    s.onload = cb;
    s.onerror = function () { console.warn('ImpactMojo Search: Failed to load Fuse.js'); };
    document.head.appendChild(s);
  }

  /* ---- Load search index ---- */
  function loadIndex(cb) {
    if (searchData) return cb(searchData);
    var controller = window.AbortController ? new AbortController() : null;
    var timeoutId = controller ? setTimeout(function () { controller.abort(); }, 10000) : null;
    fetch(INDEX_URL, controller ? { signal: controller.signal } : {})
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (data) { searchData = data; cb(data); })
      .catch(function (e) { console.warn('ImpactMojo Search: Failed to load index', e); })
      .finally(function () { if (timeoutId) clearTimeout(timeoutId); });
  }

  /* ---- Initialize Fuse instance ---- */
  function initFuse() {
    loadFuse(function () {
      loadIndex(function (data) {
        fuse = new window.Fuse(data, {
          keys: [
            { name: 'title', weight: 0.45 },
            { name: 'description', weight: 0.25 },
            { name: 'tags', weight: 0.15 },
            { name: 'category', weight: 0.1 },
            { name: 'id', weight: 0.05 }
          ],
          threshold: 0.35,
          distance: 200,
          includeScore: true,
          minMatchCharLength: 2,
          limit: 20
        });
      });
    });
  }

  /* ---- Build modal HTML ---- */
  function createModal() {
    modal = document.createElement('div');
    modal.id = 'impactmojo-search-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-label', 'Search ImpactMojo');
    modal.innerHTML =
      '<div class="ims-backdrop"></div>' +
      '<div class="ims-dialog">' +
        '<div class="ims-input-row">' +
          '<svg class="ims-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>' +
          '<input id="ims-input" type="text" placeholder="Search courses, tools, techniques..." autocomplete="off" aria-label="Search">' +
          '<kbd class="ims-kbd">ESC</kbd>' +
        '</div>' +
        '<div id="ims-results" class="ims-results"></div>' +
        '<div class="ims-footer">' +
          '<span><kbd>↑</kbd><kbd>↓</kbd> navigate</span>' +
          '<span><kbd>↵</kbd> open</span>' +
          '<span><kbd>esc</kbd> close</span>' +
          '<span class="ims-count" id="ims-count"></span>' +
        '</div>' +
      '</div>';
    document.body.appendChild(modal);

    input = document.getElementById('ims-input');
    resultsList = document.getElementById('ims-results');

    modal.querySelector('.ims-backdrop').addEventListener('click', closeSearch);
    input.addEventListener('input', onInput);
    input.addEventListener('keydown', onKeydown);
  }

  /* ---- Inject CSS ---- */
  function injectStyles() {
    var css = document.createElement('style');
    css.textContent =
      '#impactmojo-search-modal{display:none;position:fixed;inset:0;z-index:99999;font-family:"Amaranth","Inter",system-ui,sans-serif}' +
      '#impactmojo-search-modal.ims-open{display:flex;align-items:flex-start;justify-content:center;padding-top:min(20vh,120px)}' +
      '.ims-backdrop{position:fixed;inset:0;background:rgba(0,0,0,0.5);backdrop-filter:blur(4px)}' +
      '.ims-dialog{position:relative;width:min(640px,90vw);max-height:min(500px,70vh);background:var(--card-bg,#fff);border-radius:16px;box-shadow:0 25px 50px rgba(0,0,0,0.25);display:flex;flex-direction:column;overflow:hidden;border:1px solid var(--border-color,#e2e8f0)}' +
      '.ims-input-row{display:flex;align-items:center;gap:12px;padding:16px 20px;border-bottom:1px solid var(--border-color,#e2e8f0)}' +
      '.ims-search-icon{width:20px;height:20px;flex-shrink:0;color:var(--text-muted,#94a3b8)}' +
      '#ims-input{flex:1;border:none;outline:none;font-size:1rem;background:transparent;color:var(--text-primary,#1e293b);font-family:inherit}' +
      '#ims-input::placeholder{color:var(--text-muted,#94a3b8)}' +
      '.ims-kbd{font-size:0.7rem;padding:2px 6px;border-radius:4px;border:1px solid var(--border-color,#e2e8f0);color:var(--text-secondary,#475569);background:var(--surface-color,#f8fafc);font-family:monospace;flex-shrink:0}' +
      '.ims-results{overflow-y:auto;flex:1;padding:8px}' +
      '.ims-results::-webkit-scrollbar{width:6px}.ims-results::-webkit-scrollbar-thumb{background:#cbd5e1;border-radius:3px}' +
      '.ims-result{display:flex;align-items:flex-start;gap:12px;padding:10px 12px;border-radius:10px;cursor:pointer;text-decoration:none;color:inherit;transition:background 0.15s}' +
      '.ims-result:hover,.ims-result.ims-active{background:var(--surface-color,#f1f5f9)}' +
      '.ims-result-icon{width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0;color:#fff}' +
      '.ims-result-body{flex:1;min-width:0}' +
      '.ims-result-title{font-weight:600;font-size:0.9rem;color:var(--text-primary,#1e293b);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
      '.ims-result-desc{font-size:0.78rem;color:var(--text-muted,#64748b);margin-top:2px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}' +
      '.ims-result-meta{display:flex;gap:8px;margin-top:4px}' +
      '.ims-result-badge{font-size:0.65rem;padding:1px 6px;border-radius:4px;font-weight:600;color:#fff}' +
      '.ims-footer{display:flex;align-items:center;gap:16px;padding:10px 20px;border-top:1px solid var(--border-color,#e2e8f0);font-size:0.75rem;color:var(--text-muted,#94a3b8)}' +
      '.ims-footer kbd{font-size:0.7rem;padding:1px 5px;border-radius:3px;border:1px solid var(--border-color,#e2e8f0);background:var(--surface-color,#f8fafc);font-family:monospace;margin:0 2px}' +
      '.ims-count{margin-left:auto}' +
      '.ims-empty{padding:40px 20px;text-align:center;color:var(--text-muted,#94a3b8)}' +
      '.ims-empty-icon{font-size:2rem;margin-bottom:8px}' +
      '.ims-empty-text{font-size:0.9rem}' +
      '.ims-empty-hint{font-size:0.78rem;margin-top:4px}' +
      /* Navbar search button */
      '.ims-nav-btn{display:inline-flex;align-items:center;gap:6px;padding:6px 14px;border-radius:8px;border:1px solid var(--border-color,#e2e8f0);background:var(--surface-color,#f8fafc);color:var(--text-secondary,#475569);cursor:pointer;font-size:0.82rem;font-family:inherit;transition:all 0.2s;margin-left:8px}' +
      '.ims-nav-btn:hover{border-color:var(--accent-color,#6366F1);color:var(--text-primary,#1e293b);box-shadow:0 2px 8px rgba(99,102,241,0.15)}' +
      '.ims-nav-btn svg{width:15px;height:15px}' +
      '.ims-nav-btn kbd{font-size:0.65rem;padding:1px 5px;border-radius:3px;border:1px solid var(--border-color,#d1d5db);background:var(--card-bg,#fff);font-family:monospace;color:var(--text-secondary,#475569)}' +
      '@media(max-width:768px){.ims-nav-btn kbd{display:none}.ims-nav-btn{padding:6px 10px}}' +
      /* --text-secondary is defined in dark mode but --surface-color is not,
         so the button kept its light fallback background under light text:
         1.42:1. Pin both sides for dark rather than relying on the vars. */
      '[data-theme="dark"] .ims-nav-btn{background:#1e293b;color:#e2e8f0;border-color:#334155}';
    document.head.appendChild(css);
  }

  /* ---- Render results ---- */
  function renderResults(query) {
    if (!fuse || !query || query.length < 2) {
      resultsList.innerHTML =
        '<div class="ims-empty">' +
          '<div class="ims-empty-icon">🔍</div>' +
          '<div class="ims-empty-text">Search ' + (searchData ? searchData.length : 'all') + ' resources across ImpactMojo</div>' +
          '<div class="ims-empty-hint">Courses, BCT techniques, datasets, games, studios, and more</div>' +
        '</div>';
      document.getElementById('ims-count').textContent = '';
      selectedIndex = -1;
      return;
    }

    var results = fuse.search(query, { limit: 15 });
    if (!results.length) {
      resultsList.innerHTML =
        '<div class="ims-empty">' +
          '<div class="ims-empty-icon">🤔</div>' +
          '<div class="ims-empty-text">No results for "' + escapeHTML(query) + '"</div>' +
          '<div class="ims-empty-hint">Try broader terms like "health", "monitoring", or "economics"</div>' +
        '</div>';
      document.getElementById('ims-count').textContent = '';
      selectedIndex = -1;
      return;
    }

    var html = '';
    results.forEach(function (r, i) {
      var item = r.item;
      var meta = TYPE_META[item.type] || { icon: sargamImg('si_Article'), label: item.type, color: '#64748b' };
      html +=
        '<a class="ims-result' + (i === 0 ? ' ims-active' : '') + '" href="' + escapeHTML(item.url) + '" data-idx="' + i + '"' +
        (item.url.indexOf('http') === 0 ? ' target="_blank" rel="noopener noreferrer"' : '') + '>' +
          '<div class="ims-result-icon" style="background:' + meta.color + '">' + meta.icon + '</div>' +
          '<div class="ims-result-body">' +
            '<div class="ims-result-title">' + highlightMatch(item.title, query) + '</div>' +
            '<div class="ims-result-desc">' + escapeHTML(item.description) + '</div>' +
            '<div class="ims-result-meta">' +
              '<span class="ims-result-badge" style="background:' + meta.color + '">' + meta.label + '</span>' +
              (item.category ? '<span class="ims-result-badge" style="background:#64748b">' + escapeHTML(item.category) + '</span>' : '') +
            '</div>' +
          '</div>' +
        '</a>';
    });
    resultsList.innerHTML = html;
    selectedIndex = 0;
    document.getElementById('ims-count').textContent = results.length + ' result' + (results.length !== 1 ? 's' : '');

    resultsList.querySelectorAll('.ims-result').forEach(function (el) {
      el.addEventListener('mouseenter', function () {
        setActive(parseInt(el.dataset.idx));
      });
    });
  }

  function highlightMatch(text, query) {
    var safe = escapeHTML(text);
    var q = escapeHTML(query);
    var regex = new RegExp('(' + q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
    return safe.replace(regex, '<strong style="color:var(--accent-color,#6366F1)">$1</strong>');
  }

  function escapeHTML(str) {
    var map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
    return String(str || '').replace(/[&<>"']/g, function (c) { return map[c]; });
  }

  /* ---- Keyboard navigation ---- */
  function setActive(idx) {
    var items = resultsList.querySelectorAll('.ims-result');
    if (!items.length) return;
    items.forEach(function (el) { el.classList.remove('ims-active'); });
    selectedIndex = Math.max(0, Math.min(idx, items.length - 1));
    items[selectedIndex].classList.add('ims-active');
    items[selectedIndex].scrollIntoView({ block: 'nearest' });
  }

  function onKeydown(e) {
    var items = resultsList.querySelectorAll('.ims-result');
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setActive(selectedIndex + 1);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setActive(selectedIndex - 1);
    } else if (e.key === 'Enter' && items[selectedIndex]) {
      e.preventDefault();
      items[selectedIndex].click();
      closeSearch();
    } else if (e.key === 'Escape') {
      e.preventDefault();
      closeSearch();
    }
  }

  function onInput() {
    renderResults(input.value.trim());
  }

  /* ---- Open / Close ---- */
  function openSearch() {
    if (visible) return;
    if (!modal) createModal();
    if (!fuse) initFuse();
    visible = true;
    modal.classList.add('ims-open');
    input.value = '';
    renderResults('');
    setTimeout(function () { input.focus(); }, 50);
    document.body.style.overflow = 'hidden';
  }

  function closeSearch() {
    if (!visible) return;
    visible = false;
    modal.classList.remove('ims-open');
    document.body.style.overflow = '';
  }

  /* ---- Global keyboard shortcut ---- */
  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      if (visible) closeSearch(); else openSearch();
    }
    if (e.key === '/' && !visible && !isInputFocused()) {
      e.preventDefault();
      openSearch();
    }
  });

  function isInputFocused() {
    var el = document.activeElement;
    return el && (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' || el.isContentEditable);
  }

  /* ---- Inject nav button ---- */
  function injectNavButton() {
    var btn = document.createElement('button');
    btn.className = 'ims-nav-btn';
    btn.setAttribute('aria-label', 'Search (Ctrl+K)');
    btn.innerHTML =
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>' +
      'Search' +
      '<kbd>⌘K</kbd>';
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      openSearch();
    });

    /* Place in nav-buttons area (next to theme selector / auth buttons) for prominence */
    var navButtons = document.querySelector('.nav-buttons');
    if (navButtons) {
      var themeSelector = navButtons.querySelector('.theme-selector');
      if (themeSelector) {
        navButtons.insertBefore(btn, themeSelector);
      } else {
        navButtons.insertBefore(btn, navButtons.firstChild);
      }
      return;
    }

    /* Fallback: append to nav container */
    var nav = document.querySelector('.nav-with-badge') || document.querySelector('.nav-container');
    if (nav) {
      nav.style.display = 'flex';
      nav.style.alignItems = 'center';
      nav.appendChild(btn);
    }
  }

  /* ---- Init ---- */
  injectStyles();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      injectNavButton();
      initFuse();
    });
  } else {
    injectNavButton();
    initFuse();
  }

  window.ImpactMojoSearch = { open: openSearch, close: closeSearch };
})();
