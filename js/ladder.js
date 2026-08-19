/* =============================================================================
   ImpactMojo — Fundamentals: Ladder of Citizen Participation
   Renders the eight rungs as real <button>s (not SVG), so every target scales
   with the text and stays tappable at any width. Depends on /js/ladder-data.js.
   ============================================================================= */

window.FLadder = (function () {
  "use strict";
  var D = window.LADDER;
  var state = { rung: null };

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function byId(id) { return D.rungs.filter(function (r) { return r.id === id; })[0]; }

  function buildLadder() {
    var box = document.getElementById("ladder");
    if (!box) return;
    var lastBand = null, html = [];
    D.rungs.forEach(function (r) {
      if (r.band !== lastBand) {
        html.push('<div class="band-head"><span class="band-name">' + esc(D.BANDS[r.band].label) +
                  '</span><span class="band-note">' + esc(D.BANDS[r.band].note) + '</span></div>');
        lastBand = r.band;
      }
      html.push(
        '<button type="button" class="rung b-' + r.band + '" data-rung="' + esc(r.id) + '" aria-pressed="false" ' +
          'style="--rc:' + esc(r.color) + '">' +
          '<span class="rung-n">' + r.n + '</span>' +
          '<span class="rung-b"><span class="rung-name">' + esc(r.name) + '</span>' +
          '<span class="rung-say">' + esc(r.india) + '</span></span>' +
        '</button>');
    });
    box.innerHTML = '<div class="ladder-key"><span>&uarr; more power</span><span>less power &darr;</span></div>' + html.join("");
    box.querySelectorAll("[data-rung]").forEach(function (b) {
      b.addEventListener("click", function () { select(b.getAttribute("data-rung")); });
    });
  }

  function select(id, opts) {
    opts = opts || {};
    var r = byId(id);
    if (!r) return;
    state.rung = id;
    document.querySelectorAll("#ladder .rung").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-rung") === id));
    });
    renderPanel(r);
    if (!opts.silent) history.replaceState(null, "", "#" + id);
  }

  function renderPanel(r) {
    var h = [];
    h.push('<div class="panel-axis"><span class="swatch" style="background:' + esc(r.color) + '"></span>Rung ' + r.n + ' &middot; ' + esc(D.BANDS[r.band].label) + '</div>');
    h.push('<h3>' + esc(r.name) + '</h3>');
    h.push('<blockquote class="arnstein">' + esc(r.arnstein) + '<cite>Arnstein, 1969</cite></blockquote>');
    h.push('<p class="who"><b>In Indian practice:</b> ' + esc(r.india) + '</p>');
    h.push('<ul class="ev-list">');
    r.evidence.forEach(function (e) {
      h.push('<li class="ev"><div class="fig">' + esc(e.stat) + '</div><div class="txt">' + esc(e.detail) +
             '<span class="src">' + esc(e.source) + ', ' + esc(e.year) + '</span></div></li>');
    });
    h.push('</ul>');
    h.push('<div class="caveat"><b>What this does not settle</b><p>' + esc(r.complication) + '</p></div>');
    h.push('<div class="panel-nav">' +
      '<button class="btn-ghost" data-nav="up">&uarr; Rung above</button>' +
      '<button class="btn-ghost" data-nav="down">&darr; Rung below</button>' +
      '<button class="btn-ghost" data-nav="clear">Clear</button></div>');
    var p = document.getElementById("panel");
    p.innerHTML = h.join("");
    p.querySelectorAll("[data-nav]").forEach(function (b) {
      b.addEventListener("click", function () { nav(b.getAttribute("data-nav")); });
    });
  }

  function nav(dir) {
    if (dir === "clear") {
      state.rung = null;
      document.querySelectorAll("#ladder .rung").forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
      renderEmpty();
      history.replaceState(null, "", location.pathname);
      return;
    }
    var i = D.rungs.map(function (r) { return r.id; }).indexOf(state.rung);
    if (i < 0) return;
    /* rungs run 8 down to 1 in DOM order, so "up" is the previous index */
    var j = dir === "up" ? Math.max(0, i - 1) : Math.min(D.rungs.length - 1, i + 1);
    select(D.rungs[j].id);
    var btn = document.querySelector('#ladder [data-rung="' + D.rungs[j].id + '"]');
    if (btn) btn.focus();
  }

  function renderEmpty() {
    document.getElementById("panel").innerHTML =
      '<div class="panel-empty"><h3>Pick a rung</h3>' +
      '<p>Each of the eight rungs opens the Indian law, scheme or judgment that puts a real practice on it, with the source and year given, plus a note on what the placement does not settle.</p>' +
      '<ol><li>The top three rungs are <b>citizen power</b>: people decide something.</li>' +
      '<li>The middle three are <b>tokenism</b>: people are heard, and nothing obliges anyone to act.</li>' +
      '<li>The bottom two are <b>non-participation</b>: the exercise substitutes for taking part.</li></ol></div>';
  }

  function fromHash() {
    var id = (location.hash || "").replace("#", "");
    if (id && byId(id)) { select(id, { silent: true }); return true; }
    return false;
  }

  function init() {
    if (!D || !D.rungs) return;
    buildLadder();
    if (!fromHash()) renderEmpty();
    window.addEventListener("hashchange", fromHash);
  }

  return { init: init, select: select };
})();
