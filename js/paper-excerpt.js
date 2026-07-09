/**
 * ImpactMojo Paper Excerpt Popups
 * Version 1.0.0 — July 2026
 *
 * Lets a course module surface a real, detailed reading excerpt (open-access /
 * classic / public-domain text) in an accessible modal, without bloating the
 * page flow. Self-contained: injects its own styles + modal DOM and uses event
 * delegation, so it works on module content that course-loader.js injects at
 * runtime.
 *
 * Authoring convention (lives in the module content_html, i.e. the DB):
 *
 *   <button class="excerpt-btn" data-excerpt="ex-causal-m01">
 *     <svg ...></svg> Read the passage — Holland (1986) &rarr;
 *   </button>
 *   <div class="excerpt-source" id="ex-causal-m01" hidden>
 *     <div class="excerpt-kicker">Key reading &middot; Open access</div>
 *     <h3>Paul W. Holland — Statistics and Causal Inference (1986)</h3>
 *     <div class="excerpt-cite">JASA 81(396). <a href="URL" target="_blank" rel="noopener">Source &rarr;</a></div>
 *     <blockquote class="excerpt-quote">"…verbatim open-access passage…"</blockquote>
 *     <p class="excerpt-note"><strong>Why it matters.</strong> Editorial gloss…</p>
 *   </div>
 *
 * The button's data-excerpt must equal the source div's id. Only open-access,
 * Creative-Commons, or public-domain text should be reproduced verbatim.
 */
(function () {
  'use strict';
  if (window.__imExcerptInit) return;
  window.__imExcerptInit = true;

  var lastFocus = null;

  function injectStyles() {
    if (document.getElementById('im-excerpt-styles')) return;
    var css = [
      '.excerpt-source{display:none!important}',
      '.excerpt-btn{display:inline-flex;align-items:center;gap:.5rem;margin:.25rem 0 1rem;',
      'padding:.55rem .95rem;border:1px solid var(--accent-color,#0EA5E9);border-radius:8px;',
      'background:var(--color-accent-light,rgba(14,165,233,.12));color:var(--accent-color,#0EA5E9);',
      'font:600 .9rem/1.2 var(--font-sans,inherit);cursor:pointer;transition:all .15s;text-align:left}',
      '.excerpt-btn:hover{background:var(--accent-color,#0EA5E9);color:#fff}',
      '.excerpt-btn svg{width:16px;height:16px;flex-shrink:0}',
      '.im-excerpt-overlay{position:fixed;inset:0;z-index:10050;display:flex;align-items:center;',
      'justify-content:center;padding:1.25rem;background:rgba(15,23,42,.55);backdrop-filter:blur(4px);',
      'opacity:0;transition:opacity .18s}',
      '.im-excerpt-overlay.open{opacity:1}',
      '.im-excerpt-panel{position:relative;width:100%;max-width:720px;max-height:86vh;overflow-y:auto;',
      'background:var(--card-bg,#fff);color:var(--text-primary,#0F172A);border:1px solid var(--border-color,#E2E8F0);',
      'border-radius:16px;box-shadow:0 24px 60px rgba(0,0,0,.3);padding:2rem 2rem 1.75rem;',
      'transform:translateY(8px) scale(.98);transition:transform .18s;font-family:var(--font-sans,inherit);line-height:1.7}',
      '.im-excerpt-overlay.open .im-excerpt-panel{transform:none}',
      '.im-excerpt-close{position:absolute;top:.85rem;right:.85rem;width:36px;height:36px;border:none;',
      'border-radius:9px;background:var(--hover-bg,#F1F5F9);color:var(--text-secondary,#475569);',
      'font-size:1.35rem;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center}',
      '.im-excerpt-close:hover{background:var(--border-color,#E2E8F0)}',
      '.im-excerpt-panel .excerpt-kicker{font:700 .68rem/1 var(--font-heading,inherit);text-transform:uppercase;',
      'letter-spacing:.08em;color:var(--accent-color,#0EA5E9);margin-bottom:.6rem}',
      '.im-excerpt-panel h3{font-family:var(--font-heading,inherit);font-size:1.3rem;margin:.1rem 2rem .35rem 0;line-height:1.3}',
      '.im-excerpt-panel .excerpt-cite{font-size:.85rem;color:var(--text-secondary,#475569);margin-bottom:1.1rem}',
      '.im-excerpt-panel .excerpt-cite a{color:var(--accent-color,#0EA5E9)}',
      '.im-excerpt-panel .excerpt-quote{border-left:3px solid var(--accent-color,#0EA5E9);margin:0 0 1.1rem;',
      'padding:.4rem 0 .4rem 1.1rem;font-size:1.02rem;color:var(--text-primary,#0F172A)}',
      '.im-excerpt-panel .excerpt-quote p{margin:0 0 .7rem}.im-excerpt-panel .excerpt-quote p:last-child{margin:0}',
      '.im-excerpt-panel .excerpt-note{font-size:.95rem;color:var(--text-secondary,#475569);',
      'background:var(--secondary-bg,#F8FAFC);border-radius:10px;padding:.9rem 1.05rem;margin:.2rem 0 0}',
      '@media (max-width:600px){.im-excerpt-panel{padding:1.5rem 1.25rem}.im-excerpt-panel h3{font-size:1.15rem}}',
      '@media (prefers-reduced-motion:reduce){.im-excerpt-overlay,.im-excerpt-panel{transition:none}}'
    ].join('');
    var s = document.createElement('style');
    s.id = 'im-excerpt-styles';
    s.textContent = css;
    document.head.appendChild(s);
  }

  function ensureModal() {
    var o = document.getElementById('im-excerpt-modal');
    if (o) return o;
    o = document.createElement('div');
    o.id = 'im-excerpt-modal';
    o.className = 'im-excerpt-overlay';
    o.setAttribute('hidden', '');
    o.setAttribute('role', 'dialog');
    o.setAttribute('aria-modal', 'true');
    o.setAttribute('aria-label', 'Reading excerpt');
    o.innerHTML =
      '<div class="im-excerpt-panel" role="document">' +
      '<button class="im-excerpt-close" type="button" aria-label="Close excerpt">&times;</button>' +
      '<div class="im-excerpt-body"></div></div>';
    document.body.appendChild(o);
    o.addEventListener('click', function (e) {
      if (e.target === o || e.target.closest('.im-excerpt-close')) close();
    });
    return o;
  }

  function open(sourceId) {
    var src = document.getElementById(sourceId);
    if (!src) return;
    var modal = ensureModal();
    modal.querySelector('.im-excerpt-body').innerHTML = src.innerHTML;
    lastFocus = document.activeElement;
    modal.removeAttribute('hidden');
    // force reflow so the transition runs
    void modal.offsetWidth;
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    var closeBtn = modal.querySelector('.im-excerpt-close');
    if (closeBtn) closeBtn.focus();
  }

  function close() {
    var modal = document.getElementById('im-excerpt-modal');
    if (!modal || modal.hasAttribute('hidden')) return;
    modal.classList.remove('open');
    document.body.style.overflow = '';
    var done = function () {
      modal.setAttribute('hidden', '');
      modal.removeEventListener('transitionend', done);
    };
    modal.addEventListener('transitionend', done);
    setTimeout(done, 250);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  // Event delegation — works for content injected after load.
  document.addEventListener('click', function (e) {
    var trigger = e.target.closest('[data-excerpt]');
    if (!trigger) return;
    e.preventDefault();
    open(trigger.getAttribute('data-excerpt'));
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });

  function init() { injectStyles(); }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
