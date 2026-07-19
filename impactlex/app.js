/**
 * ImpactLex app logic.
 *
 * Data flow:
 *   1. Load seed-snapshot.json immediately → render anything.
 *   2. If window.IMPACTLEX_CONFIG.instantDbAppId is set, subscribe to live terms
 *      collection and re-render when it arrives. (Progressive enhancement.)
 *
 * Features:
 *   - Fuzzy search (term, acronym, aliases, definition)
 *   - Category + course filters
 *   - Term-of-the-day (deterministic by date)
 *   - Bookmarks (localStorage; cloud sync when logged in)
 *   - Deep-link via ?term=<slug>
 *   - Submit-a-term form (writes to `contributions` collection)
 */

(() => {
  'use strict';

  const CONFIG = window.IMPACTLEX_CONFIG || {};
  const $ = (id) => document.getElementById(id);

  // ─── State ──────────────────────────────────────────────────────────────
  const state = {
    terms: [],
    caseStudies: [],
    formulae: [],
    filter: { category: 'all', course: 'all', query: '' },
    bookmarks: new Set(JSON.parse(localStorage.getItem('impactlex:bookmarks') || '[]')),
    liveSource: 'snapshot', // 'snapshot' | 'instantdb'
  };

  // ─── Theme ──────────────────────────────────────────────────────────────
  const THEME_KEY = 'im-theme';
  function initTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const theme = saved || (prefersDark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
  }
  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem(THEME_KEY, next);
  }
  initTheme();

  // ─── Data loading ───────────────────────────────────────────────────────
  async function loadSnapshot() {
    try {
      const res = await fetch(CONFIG.snapshotUrl);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      state.terms = (data.terms || []).filter((t) => t.status !== 'rejected');
      state.caseStudies = data.caseStudies || [];
      state.formulae = data.formulae || [];
      updateStats();
      render();
    } catch (err) {
      showStatus(`Could not load glossary: ${err.message}`, 'offline');
    }
  }

  async function connectInstantDB() {
    if (!CONFIG.instantDbAppId) return;
    try {
      // Lazy-load the SDK only when configured. Kept as an ES module import.
      const { init, tx, i } = await import('https://esm.sh/@instantdb/core@0.14.22');
      const db = init({ appId: CONFIG.instantDbAppId });
      window.__impactlexDb = db;
      db.subscribeQuery({ terms: {}, caseStudies: {}, formulae: {} }, (resp) => {
        if (resp.error) { console.warn('InstantDB error:', resp.error); return; }
        const d = resp.data;
        // InstantDB uses UUIDs as entity ids; the app routes on slugs. Normalize.
        const useSlug = (row) => ({ ...row, uuid: row.id, id: row.slug || row.id });
        // Show everything that isn't explicitly rejected. Seed/draft/published all visible.
        // (Drafts only appear in /impactlex/review.html for editors.)
        if (d.terms?.length) state.terms = d.terms.filter((t) => t.status !== 'rejected').map(useSlug);
        if (d.caseStudies?.length) state.caseStudies = d.caseStudies.map(useSlug);
        if (d.formulae?.length) state.formulae = d.formulae.map(useSlug);
        state.liveSource = 'instantdb';
        updateStats();
        render();
        // No user-facing status on success; backend choice is implementation detail.
      });
    } catch (err) {
      console.warn('InstantDB connection failed, staying on snapshot:', err);
    }
  }

  // ─── Search ─────────────────────────────────────────────────────────────
  function matches(term, query) {
    if (!query) return true;
    const q = query.toLowerCase();
    const hay = [
      term.term,
      term.acronym,
      ...(term.aliases || []),
      term.definition,
      term.example,
      term.category,
      ...(term.courses || []),
    ].filter(Boolean).join(' ').toLowerCase();
    return hay.includes(q);
  }

  function visibleTerms() {
    return state.terms.filter((t) => {
      if (state.filter.category !== 'all' && t.category !== state.filter.category) return false;
      if (state.filter.course !== 'all' && !(t.courses || []).includes(state.filter.course)) return false;
      if (!matches(t, state.filter.query)) return false;
      return true;
    });
  }

  // ─── Rendering ──────────────────────────────────────────────────────────
  function updateStats() {
    $('stat-terms').textContent = state.terms.length;
    $('stat-formulae').textContent = state.formulae.length;
    $('stat-cases').textContent = state.caseStudies.length;
    // course count derived from the data, not hardcoded in the hero markup
    var courseEl = $('stat-courses');
    if (courseEl) {
      var courses = new Set();
      state.terms.forEach(function (t) {
        (t.courses || (t.course ? [t.course] : [])).forEach(function (c) { courses.add(c); });
      });
      if (courses.size) courseEl.textContent = courses.size;
    }
  }

  function renderFilters() {
    const catCounts = {};
    const courseCounts = {};
    for (const t of state.terms) {
      catCounts[t.category] = (catCounts[t.category] || 0) + 1;
      for (const c of (t.courses || [])) courseCounts[c] = (courseCounts[c] || 0) + 1;
    }
    const catOrder = ['all', 'concept', 'acronym', 'framework', 'method', 'formula', 'institution'];
    const catLabel = { all: 'All', concept: 'Concepts', acronym: 'Acronyms', framework: 'Frameworks', method: 'Methods', formula: 'Formulae', institution: 'Institutions' };
    $('category-filters').innerHTML = catOrder
      .filter((c) => c === 'all' || catCounts[c])
      .map((c) => {
        const active = state.filter.category === c ? ' active' : '';
        const count = c === 'all' ? state.terms.length : (catCounts[c] || 0);
        return `<button class="filter-chip${active}" data-filter-type="category" data-filter-value="${c}">${catLabel[c]}<span class="count">${count}</span></button>`;
      }).join('');

    const courses = Object.keys(courseCounts).sort();
    if (!courses.length) {
      $('course-filters').innerHTML = '';
    } else {
      const courseLabel = { SEL: 'SEL', dataviz: 'DataViz', devai: 'DevAI', devecon: 'DevEcon', gandhi: 'Gandhi', gender: 'Gender', law: 'Law', mel: 'MEL', poa: 'PoA', pubpol: 'PubPol' };
      const activeAll = state.filter.course === 'all' ? ' active' : '';
      const chips = [`<button class="filter-chip${activeAll}" data-filter-type="course" data-filter-value="all">All courses</button>`]
        .concat(courses.map((c) => {
          const active = state.filter.course === c ? ' active' : '';
          return `<button class="filter-chip${active}" data-filter-type="course" data-filter-value="${c}">${courseLabel[c] || c}<span class="count">${courseCounts[c]}</span></button>`;
        }));
      $('course-filters').innerHTML = chips.join('');
    }
  }

  function renderResults() {
    const terms = visibleTerms();
    const meta = $('results-meta');
    const grid = $('terms-grid');
    const empty = $('empty-state');

    meta.textContent = terms.length === state.terms.length
      ? `Showing all ${terms.length} terms`
      : `${terms.length} of ${state.terms.length} terms`;

    if (!terms.length) {
      grid.innerHTML = '';
      empty.hidden = false;
      return;
    }
    empty.hidden = true;

    const slice = terms.slice(0, 120);
    grid.innerHTML = slice.map((t) => termCard(t)).join('');
    if (terms.length > slice.length) {
      grid.insertAdjacentHTML('beforeend', `<div class="results-meta" style="grid-column: 1 / -1; text-align: center;">+${terms.length - slice.length} more — refine your search to narrow down.</div>`);
    }
  }

  function termCard(t) {
    const courseBadges = (t.courses || []).slice(0, 3)
      .map((c) => `<span class="course-badge">${c}</span>`).join('');
    const bookmarked = state.bookmarks.has(t.id) ? ' active' : '';
    const acronym = t.acronym ? `<span class="term-card-acronym">${escapeHtml(t.acronym)}</span>` : '';
    return `
      <button class="term-card" data-term-id="${t.id}" type="button">
        <div class="term-card-header">
          <span class="term-card-title">${escapeHtml(t.term)}</span>
          ${acronym}
        </div>
        <span class="term-card-category">${t.category}</span>
        <p class="term-card-def">${escapeHtml(t.definition || '')}</p>
        <div class="term-card-courses">${courseBadges}</div>
        <span class="bookmark-btn${bookmarked}" data-bookmark-id="${t.id}" aria-label="Bookmark">
          <svg viewBox="0 0 24 24"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
        </span>
      </button>
    `;
  }

  function renderFeatured() {
    if (!state.terms.length) return;
    const today = new Date();
    const seed = today.getFullYear() * 1000 + (today.getMonth() + 1) * 32 + today.getDate();
    const idx = seed % state.terms.length;
    const t = state.terms[idx];
    $('featured-term').textContent = t.term + (t.acronym ? ` (${t.acronym})` : '');
    $('featured-def').textContent = t.definition;
    $('featured').hidden = false;
    $('featured').setAttribute('data-term-id', t.id);
  }

  function render() {
    renderFilters();
    renderResults();
    renderFeatured();
    openFromHash();
  }

  // ─── Modal ──────────────────────────────────────────────────────────────
  function openTerm(id) {
    const t = state.terms.find((x) => x.id === id);
    if (!t) return;
    $('modal-title').textContent = t.term;
    $('modal-acronym').textContent = t.acronym || '';
    $('modal-meta').innerHTML = `
      <span class="term-card-category">${t.category}</span>
      ${(t.courses || []).map((c) => `<span class="course-badge">${c}</span>`).join('')}
    `;
    $('modal-definition').textContent = t.definition || '';
    const exSec = $('modal-example-section');
    if (t.example) { $('modal-example').textContent = t.example; exSec.hidden = false; } else { exSec.hidden = true; }

    const fSec = $('modal-formula-section');
    if (t.formula) {
      $('modal-formula-expr').textContent = t.formula.expression || t.formula.formula || '';
      $('modal-formula-exp').textContent = t.formula.explanation || t.formula.description || '';
      fSec.hidden = false;
    } else fSec.hidden = true;

    const cSec = $('modal-case-section');
    if (t.caseStudy) {
      $('modal-case').innerHTML = `
        <h4>${escapeHtml(t.caseStudy.title || '')}</h4>
        <div class="meta">${escapeHtml([t.caseStudy.region, t.caseStudy.year].filter(Boolean).join(' · '))}</div>
        <p>${escapeHtml(t.caseStudy.summary || '')}</p>
        ${t.caseStudy.keyFinding ? `<div class="key-finding"><strong>Key finding:</strong> ${escapeHtml(t.caseStudy.keyFinding)}</div>` : ''}
      `;
      cSec.hidden = false;
    } else cSec.hidden = true;

    const rSec = $('modal-related-section');
    const related = t.related || [];
    if (related.length) {
      $('modal-related').innerHTML = related.map((rel) => {
        const match = state.terms.find((x) =>
          x.term.toLowerCase() === String(rel).toLowerCase() ||
          x.id === slugify(rel)
        );
        const targetId = match ? match.id : slugify(rel);
        return `<button class="related-pill" data-related-id="${targetId}" type="button">${escapeHtml(rel)}</button>`;
      }).join('');
      rSec.hidden = false;
    } else rSec.hidden = true;

    const sSec = $('modal-sources-section');
    if (t.sources && t.sources.length) {
      $('modal-sources').textContent = t.sources.join(' · ');
      sSec.hidden = false;
    } else sSec.hidden = true;

    const bm = $('modal-bookmark');
    bm.classList.toggle('btn-primary', state.bookmarks.has(t.id));
    bm.querySelector('span').textContent = state.bookmarks.has(t.id) ? 'Bookmarked' : 'Bookmark';
    bm.dataset.termId = t.id;

    $('term-modal').classList.add('open');
    history.replaceState({}, '', `?term=${encodeURIComponent(t.id)}`);
    document.body.style.overflow = 'hidden';
    if (window.gtag) window.gtag('event', 'view_term', { term_id: t.id });
  }

  function closeModal() {
    $('term-modal').classList.remove('open');
    $('submit-modal').classList.remove('open');
    document.body.style.overflow = '';
    history.replaceState({}, '', window.location.pathname);
  }

  // ─── Bookmarks ──────────────────────────────────────────────────────────
  function toggleBookmark(id) {
    if (state.bookmarks.has(id)) state.bookmarks.delete(id);
    else state.bookmarks.add(id);
    localStorage.setItem('impactlex:bookmarks', JSON.stringify([...state.bookmarks]));
    // Update card badges + modal button without full re-render.
    document.querySelectorAll(`[data-bookmark-id="${id}"]`).forEach((el) => el.classList.toggle('active'));
    const modalBm = $('modal-bookmark');
    if (modalBm.dataset.termId === id) {
      modalBm.classList.toggle('btn-primary', state.bookmarks.has(id));
      modalBm.querySelector('span').textContent = state.bookmarks.has(id) ? 'Bookmarked' : 'Bookmark';
    }
    if (window.gtag) window.gtag('event', 'bookmark_term', { term_id: id, action: state.bookmarks.has(id) ? 'add' : 'remove' });
  }

  // ─── Submission ─────────────────────────────────────────────────────────
  async function submitContribution(payload) {
    // Offline queue: if InstantDB not connected, store in localStorage.
    const queueKey = 'impactlex:contributions-queue';
    const queue = JSON.parse(localStorage.getItem(queueKey) || '[]');
    const entry = {
      id: `c-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
      ...payload,
      status: 'pending',
      createdAt: new Date().toISOString(),
    };
    queue.push(entry);
    localStorage.setItem(queueKey, JSON.stringify(queue));

    if (window.__impactlexDb) {
      try {
        const { tx } = await import('https://esm.sh/@instantdb/core@0.14.22');
        await window.__impactlexDb.transact([tx.contributions[entry.id].update(entry)]);
        return { ok: true, queued: false };
      } catch (err) {
        console.warn('Contribution push failed, kept in local queue:', err);
        return { ok: true, queued: true };
      }
    }
    return { ok: true, queued: true };
  }

  // ─── Utilities ──────────────────────────────────────────────────────────
  function slugify(s) {
    return String(s).toLowerCase()
      .replace(/\([^)]*\)/g, '')
      .replace(/[^a-z0-9\s-]/g, '')
      .trim().replace(/\s+/g, '-').replace(/-+/g, '-');
  }
  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
  function showStatus(text, kind) {
    const b = $('status-banner');
    b.hidden = false;
    b.className = 'status-banner' + (kind ? ' ' + kind : '');
    $('status-text').textContent = text;
    if (!kind) setTimeout(() => { b.hidden = true; }, 3500);
  }
  function openFromHash() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('term');
    if (id) openTerm(id);
  }

  // ─── Event wiring ───────────────────────────────────────────────────────
  function wire() {
    $('theme-toggle').addEventListener('click', toggleTheme);
    $('modal-close').addEventListener('click', closeModal);
    $('submit-close').addEventListener('click', closeModal);
    $('submit-cancel').addEventListener('click', closeModal);
    document.querySelectorAll('.modal-overlay').forEach((o) => {
      o.addEventListener('click', (e) => { if (e.target === o) closeModal(); });
    });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });

    // Search
    const searchInput = $('search-input');
    const searchClear = $('search-clear');
    let searchTimer;
    searchInput.addEventListener('input', (e) => {
      const v = e.target.value;
      searchClear.classList.toggle('visible', v.length > 0);
      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => {
        state.filter.query = v;
        renderResults();
        if (window.gtag && v.length >= 3) window.gtag('event', 'search', { search_term: v });
      }, 120);
    });
    searchClear.addEventListener('click', () => {
      searchInput.value = '';
      state.filter.query = '';
      searchClear.classList.remove('visible');
      renderResults();
      searchInput.focus();
    });

    // Filters (event delegation)
    document.addEventListener('click', (e) => {
      const chip = e.target.closest('.filter-chip');
      if (chip) {
        const type = chip.dataset.filterType;
        const value = chip.dataset.filterValue;
        state.filter[type] = value;
        renderFilters();
        renderResults();
        return;
      }
      const card = e.target.closest('[data-term-id]');
      if (card) {
        // Bookmark toggle takes precedence over card click.
        const bm = e.target.closest('[data-bookmark-id]');
        if (bm) { e.stopPropagation(); toggleBookmark(bm.dataset.bookmarkId); return; }
        openTerm(card.dataset.termId);
        return;
      }
      const rel = e.target.closest('[data-related-id]');
      if (rel) {
        openTerm(rel.dataset.relatedId);
        return;
      }
    });

    // Modal actions
    $('modal-bookmark').addEventListener('click', (e) => {
      const id = e.currentTarget.dataset.termId;
      if (id) toggleBookmark(id);
    });
    $('modal-share').addEventListener('click', async (e) => {
      const url = window.location.href;
      try {
        await navigator.clipboard.writeText(url);
        const span = e.currentTarget.querySelector('span');
        const prev = span.textContent;
        span.textContent = 'Copied!';
        setTimeout(() => { span.textContent = prev; }, 1500);
      } catch {}
    });
    $('modal-suggest-edit').addEventListener('click', () => {
      const id = $('modal-bookmark').dataset.termId;
      const t = state.terms.find((x) => x.id === id);
      if (!t) return;
      $('submit-term').value = t.term;
      $('submit-category').value = t.category;
      $('submit-definition').value = t.definition;
      $('submit-example').value = t.example || '';
      closeModal();
      $('submit-modal').classList.add('open');
      document.body.style.overflow = 'hidden';
    });

    // Submit form
    $('suggest-link').addEventListener('click', (e) => { e.preventDefault(); $('submit-modal').classList.add('open'); document.body.style.overflow = 'hidden'; });
    $('footer-suggest').addEventListener('click', (e) => { e.preventDefault(); $('submit-modal').classList.add('open'); document.body.style.overflow = 'hidden'; });

    $('submit-form').addEventListener('submit', async (e) => {
      e.preventDefault();
      const payload = {
        term: $('submit-term').value.trim(),
        category: $('submit-category').value,
        definition: $('submit-definition').value.trim(),
        example: $('submit-example').value.trim(),
        email: $('submit-email').value.trim(),
      };
      const result = await submitContribution(payload);
      if (result.ok) {
        const msg = result.queued
          ? 'Thanks! Saved locally — will sync when contributions backend is live.'
          : 'Thanks! Your submission is in the moderation queue.';
        showStatus(msg, '');
        closeModal();
        e.target.reset();
        if (window.gtag) window.gtag('event', 'submit_contribution', { queued: result.queued });
      }
    });

    // Admin link visibility
    const email = localStorage.getItem('impactlex:user-email');
    if (email && (CONFIG.adminEmails || []).includes(email)) {
      $('nav-review').hidden = false;
    }
  }

  // ─── Init ───────────────────────────────────────────────────────────────
  async function init() {
    wire();
    await loadSnapshot();
    connectInstantDB(); // fire-and-forget; progressively enhances
  }

  document.addEventListener('DOMContentLoaded', init);
})();
