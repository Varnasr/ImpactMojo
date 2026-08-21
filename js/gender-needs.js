/* =============================================================================
   ImpactMojo — Fundamentals: Practical and Strategic Gender Needs
   -----------------------------------------------------------------------------
   Renders Moser's distinction as a plot rather than a list, because the useful
   thing about it is not the two categories but where a real intervention falls
   between them. Each Indian case sits at (relief, shift); the quadrants are
   drawn under the points and named, so the reading of a position is on the page
   next to the position.
   ============================================================================= */

(function () {
  "use strict";

  var D = window.GENDER_NEEDS;
  if (!D) return;

  /* ------------------------------------------------------------ ink chooser */
  function chan(c) {
    c /= 255;
    return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  }
  function lum(hex) {
    var h = hex.replace("#", "");
    if (h.length === 3) h = h[0] + h[0] + h[1] + h[1] + h[2] + h[2];
    return 0.2126 * chan(parseInt(h.slice(0, 2), 16)) +
           0.7152 * chan(parseInt(h.slice(2, 4), 16)) +
           0.0722 * chan(parseInt(h.slice(4, 6), 16));
  }
  function contrast(a, b) {
    var la = lum(a), lb = lum(b);
    var hi = Math.max(la, lb), lo = Math.min(la, lb);
    return (hi + 0.05) / (lo + 0.05);
  }
  /* Compare the two candidate inks against this fill and take the better one.
     A fixed luminance cutoff is what put white on #d97706 at 3.19:1 on the
     Power Cube and white on every outer ring of the Wheel at 2.3-3.2:1. */
  function readableOn(hex) {
    return contrast("#241a20", hex) > contrast("#ffffff", hex) ? "#241a20" : "#ffffff";
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  var NS = "http://www.w3.org/2000/svg";
  function el(name, attrs, text) {
    var n = document.createElementNS(NS, name);
    Object.keys(attrs || {}).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    if (text !== undefined) n.appendChild(document.createTextNode(text));
    return n;
  }

  /* Wrap to a character budget. SVG has no line box, so every break is ours. */
  function wrap(text, per) {
    var words = String(text).split(/\s+/), lines = [], line = "";
    words.forEach(function (w) {
      if (!line.length) { line = w; return; }
      if ((line + " " + w).length <= per) { line += " " + w; }
      else { lines.push(line); line = w; }
    });
    if (line.length) lines.push(line);
    return lines;
  }

  var selected = D.cases[0].id;

  /* ------------------------------------------------------------- the plot */
  function draw() {
    var host = document.getElementById("needsPlot");
    if (!host) return;
    host.innerHTML = "";

    var narrow = host.clientWidth < 620;
    /* The plot stays square: these are two comparable 0-100 scores, and a
       stretched box would make one axis look like the more decisive one. */
    var S = narrow ? 340 : 520;          // the plotting square
    var padL = narrow ? 54 : 76;         // room for the y-axis label
    var padB = narrow ? 52 : 60;
    var padT = 16, padR = narrow ? 14 : 22;
    var W = S + padL + padR, H = S + padT + padB;

    var svg = el("svg", {
      class: "gn-svg", role: "img",
      viewBox: "0 0 " + W + " " + H,
      preserveAspectRatio: "xMidYMid meet",
      "aria-label": "Twelve Indian interventions plotted by how much material " +
        "relief they deliver and how far they shift the gendered division of " +
        "labour, assets or authority. Four quadrants: practical only, strategic " +
        "only, both, and neither yet."
    });

    function px(v) { return padL + (v / 100) * S; }
    function py(v) { return padT + S - (v / 100) * S; }

    /* quadrant washes, drawn first so everything sits on top of them */
    var qAt = {
      practical:  [50, 100, 0, 50],      // x from, x to, y from, y to (in score)
      both:       [50, 100, 50, 100],
      neither:    [0, 50, 0, 50],
      strategic:  [0, 50, 50, 100]
    };
    D.quadrants.forEach(function (q) {
      var a = qAt[q.id];
      svg.appendChild(el("rect", {
        class: "gn-quad q-" + q.id,
        x: px(a[0]), y: py(a[3]), width: px(a[1]) - px(a[0]), height: py(a[2]) - py(a[3]),
        fill: q.color, "fill-opacity": 0.07
      }));
      /* The quadrant name sits in its own corner, away from the midlines where
         the points cluster. */
      var cx = a[0] === 0 ? px(3) : px(97);
      var anchor = a[0] === 0 ? "start" : "end";
      var cy = a[2] === 0 ? py(4) : py(96) + 12;
      /* The label sits on its own 7% wash over the page, not on the solid
         fill, so the fill colour is far too faint to print in. It gets a
         theme-aware ink from css/fundamentals.css instead: all four failed AA
         in dark and two in light when they inherited q.color. */
      svg.appendChild(el("text", {
        class: "gn-quad-name qn-" + q.id, x: cx, y: cy, "text-anchor": anchor
      }, q.name));
    });

    /* midlines and frame */
    svg.appendChild(el("line", { class: "gn-mid", x1: px(50), y1: py(0), x2: px(50), y2: py(100) }));
    svg.appendChild(el("line", { class: "gn-mid", x1: px(0), y1: py(50), x2: px(100), y2: py(50) }));
    svg.appendChild(el("rect", { class: "gn-frame", x: px(0), y: py(100), width: S, height: S }));

    /* axis labels */
    svg.appendChild(el("text", {
      class: "gn-axis", x: px(50), y: py(0) + (narrow ? 30 : 34), "text-anchor": "middle"
    }, D.axes.x.name + " →"));
    var yl = el("text", {
      class: "gn-axis", x: 0, y: 0, "text-anchor": "middle",
      transform: "translate(" + (narrow ? 15 : 20) + "," + py(50) + ") rotate(-90)"
    }, D.axes.y.name + " →");
    svg.appendChild(yl);

    /* the cases */
    D.cases.forEach(function (c) {
      var g = el("g", {
        class: "gn-pt" + (selected === c.id ? " is-on" : ""),
        tabindex: "0", role: "button",
        "aria-pressed": selected === c.id ? "true" : "false",
        "aria-label": c.name + ". " + c.short
      });
      var q = D.quadrants.filter(function (x) { return x.id === c.quadrant; })[0];
      var r = narrow ? 13 : 16;
      g.appendChild(el("circle", {
        class: "gn-dot", cx: px(c.relief), cy: py(c.shift), r: r, fill: q.color
      }));
      /* The number is the reader's key into the list below, and it is painted
         on the dot, so its ink is chosen against that fill. */
      g.appendChild(el("text", {
        class: "gn-dot-n", x: px(c.relief), y: py(c.shift) + (narrow ? 4 : 5),
        "text-anchor": "middle", fill: readableOn(q.color)
      }, String(D.cases.indexOf(c) + 1)));
      g.addEventListener("click", function () { select(c.id); });
      g.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); select(c.id); }
      });
      svg.appendChild(g);
    });

    host.appendChild(svg);
  }

  /* ----------------------------------------------------------------- panel */
  function select(id) {
    selected = id;
    draw();
    markButtons();
    var c = D.cases.filter(function (x) { return x.id === id; })[0];
    var host = document.getElementById("needsPanel");
    if (!c || !host) return;
    var q = D.quadrants.filter(function (x) { return x.id === c.quadrant; })[0];

    var h = [];
    h.push('<div class="gn-panel-head" style="border-left-color:' + esc(q.color) + '">');
    h.push('<span class="gn-tag" style="background:' + esc(q.color) + ';color:' +
           esc(readableOn(q.color)) + '">' + esc(q.name) + '</span>');
    h.push("<h3>" + esc(c.name) + "</h3>");
    h.push('<p class="gn-coords">Relief <b>' + c.relief + '</b> / 100 &middot; ' +
           'Position shift <b>' + c.shift + '</b> / 100</p>');
    h.push("</div>");
    h.push("<p class=\"gn-what\">" + esc(c.what) + "</p>");
    h.push("<h4>How to read it</h4><p>" + esc(c.reading) + "</p>");
    h.push('<h4>What this does not settle</h4><p class="gn-comp">' + esc(c.complication) + "</p>");

    if (c.evidence && c.evidence.length) {
      h.push("<h4>The evidence</h4><ul class=\"gn-ev\">");
      c.evidence.forEach(function (e) {
        h.push("<li><b>" + esc(e.stat) + "</b> &mdash; " + esc(e.detail) +
               ' <span class="gn-src">' + esc(e.source) + ", " + esc(e.year) + "</span></li>");
      });
      h.push("</ul>");
    } else {
      /* Saying so is better than an empty heading: the series' rule is that a
         claim without a named source and year does not go on the page, and
         these two positions rest on a reading of the literature. */
      h.push('<h4>The evidence</h4><p class="gn-noev">This position is placed ' +
             'from the research literature rather than from a single national ' +
             'statistic, and no figure is offered for it here.</p>');
    }
    host.innerHTML = h.join("");
    host.setAttribute("tabindex", "-1");
  }

  function markButtons() {
    document.querySelectorAll("#needsPicker [data-case]").forEach(function (b) {
      var on = b.getAttribute("data-case") === selected;
      b.classList.toggle("is-on", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  function buildPicker() {
    var host = document.getElementById("needsPicker");
    if (!host) return;
    var h = [];
    D.cases.forEach(function (c, i) {
      var q = D.quadrants.filter(function (x) { return x.id === c.quadrant; })[0];
      h.push('<button type="button" class="gn-btn" data-case="' + esc(c.id) +
             '" aria-pressed="false">' +
             '<span class="gn-btn-n" style="background:' + esc(q.color) + ';color:' +
             esc(readableOn(q.color)) + '">' + (i + 1) + "</span>" +
             "<span><b>" + esc(c.name) + "</b><span>" + esc(c.short) + "</span></span>" +
             "</button>");
    });
    host.innerHTML = h.join("");
    host.querySelectorAll("[data-case]").forEach(function (b) {
      b.addEventListener("click", function () { select(b.getAttribute("data-case")); });
    });
  }

  function buildLegend() {
    var host = document.getElementById("needsLegend");
    if (!host) return;
    host.innerHTML = D.quadrants.map(function (q) {
      return '<div class="gn-leg"><span class="gn-leg-sw" style="background:' +
             esc(q.color) + '"></span><b>' + esc(q.name) + "</b> <i>" +
             esc(q.where) + "</i><p>" + esc(q.gloss) + "</p><p class=\"gn-leg-d\">" +
             esc(q.detail) + "</p></div>";
    }).join("");
  }

  function init() {
    buildPicker();
    buildLegend();
    draw();
    select(selected);   /* siblings do this; without it the panel loads blank */
    var t;
    window.addEventListener("resize", function () {
      clearTimeout(t);
      t = setTimeout(draw, 150);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
