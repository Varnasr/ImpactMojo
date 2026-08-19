/* =============================================================================
   ImpactMojo — Fundamentals: the Power Cube (Gaventa, 2006)
   Nine categories across three dimensions, rendered as buttons, plus a case
   table plotting documented Indian examples on all three at once.
   Depends on /js/cube-data.js.
   ============================================================================= */

window.FCube = (function () {
  "use strict";
  var D = window.CUBE;
  var state = { cat: null };

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

  function find(id) {
    for (var i = 0; i < D.dims.length; i++) {
      var c = D.dims[i].cats.filter(function (x) { return x.id === id; })[0];
      if (c) return { dim: D.dims[i], cat: c };
    }
    return null;
  }

  function build() {
    var box = document.getElementById("cube");
    if (!box) return;
    box.innerHTML = D.dims.map(function (d) {
      return '<div class="dim">' +
        '<div class="dim-h"><span class="dim-n" style="--dc:' + esc(d.color) + '">' + esc(d.name) + '</span>' +
        '<span class="dim-q">' + esc(d.question) + '</span></div>' +
        '<div class="dim-cats">' + d.cats.map(function (c) {
          return '<button type="button" class="cat" data-cat="' + esc(c.id) + '" aria-pressed="false" style="--cc:' + esc(c.color) + ';--ci:' + ink(c.color) + '">' +
                 '<span class="cat-sw"></span>' + esc(c.name) + '</button>';
        }).join("") + '</div></div>';
    }).join("");
    box.querySelectorAll("[data-cat]").forEach(function (b) {
      b.addEventListener("click", function () { select(b.getAttribute("data-cat")); });
    });
  }

  function buildCases() {
    var box = document.getElementById("cases");
    if (!box) return;
    box.innerHTML =
      '<table class="case-tbl"><caption class="sr-only">Indian cases plotted on the three dimensions of the power cube</caption>' +
      '<thead><tr><th scope="col">Case</th><th scope="col">Space</th><th scope="col">Level</th><th scope="col">Form</th><th scope="col">What it shows</th></tr></thead><tbody>' +
      D.cases.map(function (c) {
        return '<tr><th scope="row">' + esc(c.name) + ' <span class="cy">' + esc(c.year) + '</span></th>' +
          ['space', 'level', 'form'].map(function (k) {
            var f = find(c[k]);
            var col = f ? f.cat.color : '#666666';
            return '<td><span class="tag" style="--cc:' + esc(col) + ';color:' + ink(col) + '">' + esc(f ? f.cat.name : c[k]) + '</span></td>';
          }).join("") +
          '<td class="cn">' + esc(c.note) + '</td></tr>';
      }).join("") + '</tbody></table>';
  }

  function select(id, opts) {
    opts = opts || {};
    var f = find(id);
    if (!f) return;
    state.cat = id;
    document.querySelectorAll("#cube .cat").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-cat") === id));
    });
    var c = f.cat, h = [];
    h.push('<div class="panel-axis"><span class="swatch" style="background:' + esc(c.color) + '"></span>' + esc(f.dim.name) + '</div>');
    h.push('<h3>' + esc(c.name) + '</h3>');
    h.push('<blockquote class="arnstein">' + esc(c.gaventa) + '<cite>Gaventa&rsquo;s category, paraphrased from the 2006 paper</cite></blockquote>');
    h.push('<ul class="ev-list">');
    c.evidence.forEach(function (e) {
      h.push('<li class="ev"><div class="fig">' + esc(e.stat) + '</div><div class="txt">' + esc(e.detail) +
             '<span class="src">' + esc(e.source) + ', ' + esc(e.year) + '</span></div></li>');
    });
    h.push('</ul>');
    h.push('<div class="caveat"><b>What this does not settle</b><p>' + esc(c.complication) + '</p></div>');
    h.push('<div class="panel-nav"><button class="btn-ghost" data-nav="next">Next category</button>' +
           '<button class="btn-ghost" data-nav="clear">Clear</button></div>');
    var p = document.getElementById("panel");
    p.innerHTML = h.join("");
    p.querySelectorAll("[data-nav]").forEach(function (b) {
      b.addEventListener("click", function () { nav(b.getAttribute("data-nav")); });
    });
    if (!opts.silent) history.replaceState(null, "", "#" + id);
  }

  function allIds() {
    return D.dims.reduce(function (a, d) { return a.concat(d.cats.map(function (c) { return c.id; })); }, []);
  }

  function nav(dir) {
    if (dir === "clear") {
      state.cat = null;
      document.querySelectorAll("#cube .cat").forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
      renderEmpty();
      history.replaceState(null, "", location.pathname);
      return;
    }
    var ids = allIds(), i = ids.indexOf(state.cat);
    select(ids[(i + 1) % ids.length]);
  }

  function renderEmpty() {
    document.getElementById("panel").innerHTML =
      '<div class="panel-empty"><h3>Pick a category</h3>' +
      '<p>Nine categories across three dimensions. Each opens Gaventa&rsquo;s definition and the Indian evidence for it, with a note on what the evidence does not settle.</p>' +
      '<ol><li><b>Spaces</b> ask where the decision gets made and who set the table.</li>' +
      '<li><b>Levels</b> ask whether that is local, national or global.</li>' +
      '<li><b>Forms</b> ask whether the power is visible, agenda-setting, or working on what people accept as normal.</li></ol>' +
      '<p>Gaventa&rsquo;s argument is that the three have to be read together. A seat in an invited local space is worth little if the decision was taken at another level, in another form.</p></div>';
  }

  function fromHash() {
    var id = (location.hash || "").replace("#", "");
    if (id && find(id)) { select(id, { silent: true }); return true; }
    return false;
  }

  function init() {
    if (!D || !D.dims) return;
    build(); buildCases();
    if (!fromHash()) renderEmpty();
    window.addEventListener("hashchange", fromHash);
  }
  return { init: init, select: select };
})();
