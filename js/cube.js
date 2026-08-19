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

  /* ---------------------------------------------------------------- diagram */
  /* An isometric cube: three visible faces, each sliced into the three values
     of one dimension. Nine clickable slices, labelled outside the solid with
     leader lines so no text sits on a slanted face. */
  var NS = "http://www.w3.org/2000/svg";
  var CX = 310, CY = 240, S = 125;
  var T  = [CX, CY - S], R = [CX + S, CY - S / 2], BO = [CX, CY],
      L  = [CX - S, CY - S / 2], BL = [CX - S, CY + S / 2],
      BR = [CX + S, CY + S / 2], BOT = [CX, CY + S];

  function lerp(a, b, t) { return [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t]; }
  function pts(a) { return a.map(function (p) { return p[0].toFixed(1) + "," + p[1].toFixed(1); }).join(" "); }
  function el(n, at, txt) {
    var e = document.createElementNS(NS, n);
    for (var k in at) if (at.hasOwnProperty(k)) e.setAttribute(k, at[k]);
    if (txt != null) e.textContent = txt;
    return e;
  }

  /* face: [a,b,c,d]; slices run between edge a-b and edge d-c.
     labelEdge: which side the leader comes off — "ad" or "bc". */
  var FACES = {
    level: { quad: [T, R, BO, L],   labelEdge: "ad", dx: -14, dy: -3, anchor: "end",   title: [150, 96,  "end"] },
    space: { quad: [L, BO, BOT, BL], labelEdge: "ad", dx: -16, dy: 4,  anchor: "end",   title: [150, 340, "end"] },
    form:  { quad: [R, BO, BOT, BR], labelEdge: "ad", dx: 16,  dy: 4,  anchor: "start", title: [470, 340, "start"] }
  };

  function drawCube() {
    var svg = document.getElementById("cubeSvg");
    if (!svg) return;
    svg.setAttribute("viewBox", "0 0 620 470");
    svg.setAttribute("role", "group");
    svg.setAttribute("aria-label", "Power cube: three faces, each sliced into the three values of one dimension. Select a slice to read its evidence.");
    svg.innerHTML = "";

    D.dims.forEach(function (dim) {
      var F = FACES[dim.id];
      if (!F) return;
      var a = F.quad[0], b = F.quad[1], c = F.quad[2], d = F.quad[3];
      var g = el("g", { "data-face": dim.id });

      dim.cats.forEach(function (cat, i) {
        var t0 = i / 3, t1 = (i + 1) / 3;
        var p1 = lerp(a, d, t0), p2 = lerp(b, c, t0), p3 = lerp(b, c, t1), p4 = lerp(a, d, t1);
        g.appendChild(el("polygon", {
          points: pts([p1, p2, p3, p4]), fill: cat.color, class: "slice",
          role: "button", tabindex: "-1", "data-cat": cat.id,
          "aria-label": dim.name + ": " + cat.name
        }));
        /* leader line and label, outside the solid */
        var mid = lerp(lerp(a, d, t0), lerp(a, d, t1), 0.5);
        var lx = mid[0] + F.dx, ly = mid[1] + F.dy;
        g.appendChild(el("line", { x1: mid[0], y1: mid[1], x2: lx, y2: ly, class: "leader" }));
        g.appendChild(el("text", {
          x: lx + (F.anchor === "end" ? -4 : 4), y: ly + 4,
          "text-anchor": F.anchor, class: "slice-label", "data-cat": cat.id
        }, cat.name));
      });

      svg.appendChild(g);
      svg.appendChild(el("text", {
        x: F.title[0], y: F.title[1], "text-anchor": F.title[2], class: "face-title", fill: dim.color
      }, dim.name.toUpperCase()));
    });

    /* the solid's own edges, drawn over the slices */
    [[T, R], [R, BO], [BO, L], [L, T], [L, BL], [BL, BOT], [BOT, BR], [BR, R], [BO, BOT]]
      .forEach(function (e) {
        svg.appendChild(el("line", { x1: e[0][0], y1: e[0][1], x2: e[1][0], y2: e[1][1], class: "cube-edge" }));
      });

    svg.querySelectorAll(".slice").forEach(function (n) {
      n.addEventListener("click", function () { select(n.getAttribute("data-cat")); });
      n.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); select(n.getAttribute("data-cat")); }
      });
    });
    var first = svg.querySelector(".slice");
    if (first) first.setAttribute("tabindex", "0");
  }

  function paintCube() {
    var svg = document.getElementById("cubeSvg");
    if (!svg) return;
    svg.classList.toggle("has-sel", !!state.cat);
    svg.querySelectorAll(".slice").forEach(function (n) {
      n.classList.toggle("is-on", n.getAttribute("data-cat") === state.cat);
    });
    svg.querySelectorAll(".slice-label").forEach(function (n) {
      n.classList.toggle("is-on", n.getAttribute("data-cat") === state.cat);
    });
  }

  function setCaption() {
    var box = document.getElementById("cubeCaption");
    if (!box) return;
    if (!state.cat) {
      box.className = "wheel-caption is-empty";
      box.innerHTML = '<span class="cap-t">Nothing selected yet. Pick a slice of the cube, or use the buttons below.</span>';
      return;
    }
    var f = find(state.cat);
    box.className = "wheel-caption";
    box.innerHTML = '<span class="cap-sw" style="background:' + esc(f.cat.color) + '"></span>' +
      '<span><span class="cap-s">' + esc(f.dim.name) + '</span><span class="cap-t">' + esc(f.cat.name) + '</span></span>';
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
    paintCube(); setCaption();
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
      paintCube(); setCaption();
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
    drawCube(); build(); buildCases(); setCaption();
    if (!fromHash()) renderEmpty();
    window.addEventListener("hashchange", fromHash);
  }
  return { init: init, select: select };
})();
