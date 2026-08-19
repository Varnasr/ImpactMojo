/* =============================================================================
   ImpactMojo — Fundamentals: the Capability Approach
   -----------------------------------------------------------------------------
   Renders the conversion chain: resource → conversion → capability →
   functioning. Selecting a chain opens the Indian evidence for it.

   Markup deliberately reuses the class names the other three Fundamentals use
   (.panel, .ev-list, .ev, .fig, .src, .caveat, .panel-nav) so the page inherits
   css/fundamentals.css rather than growing a parallel stylesheet.

   Ink on the stage blocks is chosen by comparing the two candidate contrast
   ratios, never by testing luminance against a fixed cutoff — the mistake that
   put white on twelve unreadable wheel labels and is now guarded by
   scripts/check-diagram-contrast.py.
   ============================================================================= */
(function () {
  "use strict";

  var D = window.CAPABILITIES;
  if (!D) return;

  var state = { chain: null };

  /* --------------------------------------------------------------- contrast */
  function hex2rgb(h) {
    h = h.replace("#", "");
    return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
  }
  function lumOf(hex) {
    var c = hex2rgb(hex).map(function (v) {
      v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  }
  function contrast(a, b) {
    var x = lumOf(a), y = lumOf(b), hi = Math.max(x, y), lo = Math.min(x, y);
    return (hi + 0.05) / (lo + 0.05);
  }
  function readableOn(hex) {
    return contrast("#241a20", hex) > contrast("#ffffff", hex) ? "#241a20" : "#ffffff";
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  /* ------------------------------------------------------------ the diagram */
  /* Four stages left to right on desktop, stacked on narrow screens. The arrow
     between them is the point of the picture: each gap is where a conversion
     factor gets to intervene. */
  function buildChainDiagram() {
    var host = document.getElementById("chainDiagram");
    if (!host) return;
    var h = ['<ol class="cap-chain" aria-label="The conversion chain, in four stages">'];
    D.stages.forEach(function (st, i) {
      var ink = readableOn(st.color);
      h.push(
        '<li class="cap-stage" data-stage="' + esc(st.id) + '">' +
          '<div class="cap-stage-box" style="background:' + esc(st.color) + ';color:' + ink + '">' +
            '<span class="cap-stage-n">' + (i + 1) + '</span>' +
            '<span class="cap-stage-name">' + esc(st.name) + '</span>' +
          '</div>' +
          '<p class="cap-stage-gloss">' + esc(st.gloss) + '</p>' +
          '<p class="cap-stage-detail">' + esc(st.detail) + '</p>' +
        '</li>'
      );
    });
    h.push("</ol>");
    host.innerHTML = h.join("");
  }

  /* --------------------------------------------------------------- pickers */
  function buildPickers() {
    var host = document.getElementById("chainPicker");
    if (!host) return;
    var h = [];
    D.chains.forEach(function (c) {
      h.push('<button type="button" class="chain-btn" data-chain="' + esc(c.id) + '">' +
             '<b>' + esc(c.name) + '</b><span>' + esc(c.short) + '</span></button>');
    });
    host.innerHTML = h.join("");
    host.querySelectorAll("[data-chain]").forEach(function (b) {
      b.addEventListener("click", function () { select(b.getAttribute("data-chain")); });
    });
  }

  function markSelected(id) {
    document.querySelectorAll("#chainPicker [data-chain]").forEach(function (b) {
      var on = b.getAttribute("data-chain") === id;
      b.classList.toggle("is-on", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  /* ----------------------------------------------------------------- panel */
  function renderEmpty() {
    document.getElementById("panel").innerHTML =
      '<div class="panel-empty">' +
        '<h3>Pick a resource</h3>' +
        '<p>Each one is followed along the chain, from what gets provided to what a person can actually do, with the Indian evidence at each step and its source and year.</p>' +
        '<ol>' +
          '<li>A <b>resource</b> is countable, which is why targets are written in it.</li>' +
          '<li>A <b>capability</b> is what someone is able to do with it, and is almost never in the administrative data.</li>' +
          '<li>Every chain carries a <b>&ldquo;what this does not settle&rdquo;</b> note. This is a teaching tool, not a measurement.</li>' +
        '</ol>' +
      '</div>';
  }

  function renderPanel(c) {
    var h = [];
    h.push('<div class="panel-axis"><span class="swatch" style="background:#0369A1"></span>' + esc(c.name) + '</div>');
    h.push('<h3>' + esc(c.short) + '</h3>');

    if (c.headline && c.headline.stat) {
      h.push('<div class="cap-headline">' +
        '<div class="ch-a"><b>' + esc(c.headline.stat) + '</b><span>' + esc(c.headline.label) + '</span></div>' +
        (c.headline.contrast
          ? '<div class="ch-b"><b>' + esc(c.headline.contrast) + '</b><span>' + esc(c.headline.contrastLabel) + '</span></div>'
          : '<div class="ch-b"><span>' + esc(c.headline.contrastLabel) + '</span></div>') +
      '</div>');
    }

    h.push('<dl class="cap-steps">');
    h.push('<dt>Resource</dt><dd>' + esc(c.resource) + '</dd>');
    h.push('<dt>Capability</dt><dd>' + esc(c.capability) + '</dd>');
    h.push('<dt>Functioning</dt><dd>' + esc(c.functioning) + '</dd>');
    h.push("</dl>");

    h.push('<p class="who"><b>What stands in between</b></p>');
    h.push('<ul class="cap-factors">');
    c.factors.forEach(function (f) {
      h.push('<li class="cf cf-' + esc(f.kind) + '"><span class="cf-tag">' +
             esc(D.FACTOR_LABEL[f.kind] || f.kind) + '</span>' + esc(f.text) + '</li>');
    });
    h.push("</ul>");

    h.push('<ul class="ev-list">');
    c.evidence.forEach(function (e) {
      h.push('<li class="ev"><div class="fig">' + esc(e.stat) + '</div>' +
             '<div class="txt">' + esc(e.detail) +
             '<span class="src">' + esc(e.source) + ', ' + esc(e.year) + '</span></div></li>');
    });
    h.push("</ul>");

    h.push('<div class="cap-reading"><b>What the chain shows</b><p>' + esc(c.reading) + '</p></div>');
    h.push('<div class="caveat"><b>What this does not settle</b><p>' + esc(c.complication) + '</p></div>');

    h.push('<div class="panel-nav">' +
      '<button type="button" class="btn-ghost" data-nav="prev">&larr; Previous</button>' +
      '<button type="button" class="btn-ghost" data-nav="next">Next resource &rarr;</button>' +
      '<button type="button" class="btn-ghost" data-nav="clear">Clear</button>' +
      '</div>');

    var panel = document.getElementById("panel");
    panel.innerHTML = h.join("");
    panel.querySelectorAll("[data-nav]").forEach(function (b) {
      b.addEventListener("click", function () { navigate(b.getAttribute("data-nav")); });
    });
  }

  function select(id, opts) {
    opts = opts || {};
    var c = D.chains.filter(function (x) { return x.id === id; })[0];
    if (!c) return;
    state.chain = id;
    markSelected(id);
    renderPanel(c);
    if (!opts.silent) history.replaceState(null, "", "#" + id);
    if (!opts.silent && opts.focus !== false) {
      var p = document.getElementById("panel");
      if (p) p.setAttribute("tabindex", "-1"), p.focus({ preventScroll: true });
    }
  }

  function clearSelection() {
    state.chain = null;
    markSelected(null);
    renderEmpty();
    history.replaceState(null, "", location.pathname);
  }

  function navigate(dir) {
    if (dir === "clear") return clearSelection();
    var ids = D.chains.map(function (c) { return c.id; });
    var i = ids.indexOf(state.chain);
    if (i < 0) return;
    var next = dir === "next" ? (i + 1) % ids.length : (i - 1 + ids.length) % ids.length;
    select(ids[next]);
  }

  /* ------------------------------------------------------- Nussbaum's list */
  function buildNussbaum() {
    var host = document.getElementById("nussbaumList");
    if (!host) return;
    host.innerHTML = D.nussbaum.map(function (c, i) {
      return '<li><b>' + esc(c.n) + '</b><span>' + esc(c.t) + '</span></li>';
    }).join("");
  }

  /* ------------------------------------------------------------------- init */
  function init() {
    buildChainDiagram();
    buildPickers();
    buildNussbaum();
    renderEmpty();

    var hash = (location.hash || "").replace("#", "");
    if (hash && D.chains.some(function (c) { return c.id === hash; })) {
      select(hash, { silent: true, focus: false });
    }

    document.addEventListener("keydown", function (e) {
      if (!state.chain) return;
      if (e.key === "Escape") clearSelection();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
