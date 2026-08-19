/* =============================================================================
   ImpactMojo — Fundamentals: Who Counts
   Eight gaps in Indian official data, as buttons plus a detail panel.
   Depends on /js/whocounts-data.js.
   ============================================================================= */

window.FWhoCounts = (function () {
  "use strict";
  var D = window.WHOCOUNTS;
  var state = { gap: null };

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  /* Pick the ink that actually contrasts better, rather than guessing a
     luminance cutoff. A fixed threshold picked white on #d97706 (3.19:1);
     comparing the two ratios is self-correcting for any future colour. */
  function ink(hex) {
    function lum(h) {
      h = h.replace("#", "");
      var c = [0, 2, 4].map(function (i) {
        var v = parseInt(h.slice(i, i + 2), 16) / 255;
        return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
      });
      return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
    }
    function ratio(a, b) {
      var x = lum(a), y = lum(b), hi = Math.max(x, y), lo = Math.min(x, y);
      return (hi + 0.05) / (lo + 0.05);
    }
    return ratio("#1a1420", hex) > ratio("#ffffff", hex) ? "#1a1420" : "#ffffff";
  }

  function byId(id) { return D.gaps.filter(function (g) { return g.id === id; })[0]; }

  /* ---------------------------------------------------------------- diagram */
  /* A 3x3 matrix: what is being measured against how the measurement fails.
     The empty cells carry the argument - identity gaps cluster under "never
     asked", and every "how you live" gap is frozen rather than missing. */
  function drawMatrix() {
    var box = document.getElementById("matrix");
    if (!box) return;
    var rows = ["identity", "condition", "outcome"];
    var cols = ["never", "under", "frozen"];
    var h = ['<div class="mx" role="table" aria-label="Gaps in Indian official data, by what is measured and how the measurement fails">'];
    h.push('<div class="mx-row mx-head" role="row"><div class="mx-corner" role="columnheader"><span>what</span><span>how it fails</span></div>');
    cols.forEach(function (c) {
      h.push('<div class="mx-ch" role="columnheader"><b>' + esc(D.KINDS[c].label) + '</b><span>' + esc(D.KINDS[c].note) + '</span></div>');
    });
    h.push('</div>');
    rows.forEach(function (r) {
      h.push('<div class="mx-row" role="row"><div class="mx-rh" role="rowheader"><b>' + esc(D.ABOUT[r].label) + '</b><span>' + esc(D.ABOUT[r].note) + '</span></div>');
      cols.forEach(function (c) {
        var here = D.gaps.filter(function (g) { return g.about === r && g.kind === c; });
        h.push('<div class="mx-cell' + (here.length ? '' : ' is-empty') + '" role="cell">');
        if (!here.length) h.push('<span class="mx-none" aria-label="no gap of this kind">&mdash;</span>');
        here.forEach(function (g) {
          h.push('<button type="button" class="mx-tile" data-gap="' + esc(g.id) + '" aria-pressed="false" style="--gc:' + esc(g.color) + ';--gi:' + ink(g.color) + '">' + esc(g.name) + '</button>');
        });
        h.push('</div>');
      });
      h.push('</div>');
    });
    h.push('</div>');
    box.innerHTML = h.join("");
    box.querySelectorAll("[data-gap]").forEach(function (b) {
      b.addEventListener("click", function () { select(b.getAttribute("data-gap")); });
    });
  }

  function paint() {
    document.querySelectorAll("#matrix .mx-tile, #gaps .gap").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-gap") === state.gap));
    });
    var box = document.getElementById("gapCaption");
    if (!box) return;
    if (!state.gap) {
      box.className = "wheel-caption is-empty";
      box.innerHTML = '<span class="cap-t">Nothing selected yet. Pick a tile in the matrix, or a gap from the list below.</span>';
      return;
    }
    var g = byId(state.gap);
    box.className = "wheel-caption";
    box.innerHTML = '<span class="cap-sw" style="background:' + esc(g.color) + '"></span>' +
      '<span><span class="cap-s">' + esc(D.ABOUT[g.about].label) + ' &middot; ' + esc(D.KINDS[g.kind].label) + '</span>' +
      '<span class="cap-t">' + esc(g.name) + '</span></span>';
  }

  function build() {
    var box = document.getElementById("gaps");
    if (!box) return;
    box.innerHTML = D.gaps.map(function (g) {
      return '<button type="button" class="gap" data-gap="' + esc(g.id) + '" aria-pressed="false" style="--gc:' + esc(g.color) + ';--gi:' + ink(g.color) + '">' +
        '<span class="gap-k">' + esc(D.KINDS[g.kind].label) + '</span>' +
        '<span class="gap-n">' + esc(g.name) + '</span>' +
        '<span class="gap-m">' + esc(g.missing) + '</span></button>';
    }).join("");
    box.querySelectorAll("[data-gap]").forEach(function (b) {
      b.addEventListener("click", function () { select(b.getAttribute("data-gap")); });
    });
  }

  function select(id, opts) {
    opts = opts || {};
    var g = byId(id);
    if (!g) return;
    state.gap = id;
    paint();
    var h = [];
    h.push('<div class="panel-axis"><span class="swatch" style="background:' + esc(g.color) + '"></span>' + esc(D.KINDS[g.kind].label) + '</div>');
    h.push('<h3>' + esc(g.name) + '</h3>');
    h.push('<p class="who"><b>What is missing:</b> ' + esc(g.missing) + '</p>');
    h.push('<ul class="ev-list">');
    g.evidence.forEach(function (e) {
      h.push('<li class="ev"><div class="fig">' + esc(e.stat) + '</div><div class="txt">' + esc(e.detail) +
             '<span class="src">' + esc(e.source) + ', ' + esc(e.year) + '</span></div></li>');
    });
    h.push('</ul>');
    h.push('<div class="caveat"><b>What the gap costs</b><p>' + esc(g.cost) + '</p></div>');
    h.push('<div class="caveat"><b>Closest available proxy</b><p>' + esc(g.proxy) + '</p></div>');
    h.push('<div class="panel-nav"><button class="btn-ghost" data-nav="next">Next gap</button>' +
           '<button class="btn-ghost" data-nav="clear">Clear</button></div>');
    var p = document.getElementById("panel");
    p.innerHTML = h.join("");
    p.querySelectorAll("[data-nav]").forEach(function (b) {
      b.addEventListener("click", function () { nav(b.getAttribute("data-nav")); });
    });
    if (!opts.silent) history.replaceState(null, "", "#" + id);
  }

  function nav(dir) {
    if (dir === "clear") {
      state.gap = null;
      paint();
      renderEmpty();
      history.replaceState(null, "", location.pathname);
      return;
    }
    var ids = D.gaps.map(function (g) { return g.id; });
    select(ids[(ids.indexOf(state.gap) + 1) % ids.length]);
  }

  function renderEmpty() {
    document.getElementById("panel").innerHTML =
      '<div class="panel-empty"><h3>Pick a gap</h3>' +
      '<p>Each opens what is missing, the evidence that it is missing, what the gap costs, and the closest available substitute.</p>' +
      '<ol><li><b>Never asked</b> means no national instrument collects it at all.</li>' +
      '<li><b>Counted, badly</b> means an official figure exists well below what independent estimates find.</li>' +
      '<li><b>Frozen</b> means it was counted once and has not been counted since.</li></ol>' +
      '<p>For what India does measure, and measures well, see <a href="/explorers.html">The Data Room</a>.</p></div>';
  }

  function fromHash() {
    var id = (location.hash || "").replace("#", "");
    if (id && byId(id)) { select(id, { silent: true }); return true; }
    return false;
  }

  function init() {
    if (!D || !D.gaps) return;
    drawMatrix(); build(); paint();
    if (!fromHash()) renderEmpty();
    window.addEventListener("hashchange", fromHash);
  }
  return { init: init, select: select };
})();
