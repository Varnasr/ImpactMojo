/* =============================================================================
   ImpactMojo — Fundamentals: The Sustainable Livelihoods Framework
   -----------------------------------------------------------------------------
   The asset pentagon, drawn as DFID drew it, and drawn eight times over so the
   shapes can be compared. The framework's claim is that the shape matters more
   than the total, so the page shows all eight at once as small multiples and
   the selected one at size. A single large chart would have hidden the point.
   ============================================================================= */

(function () {
  "use strict";

  var D = window.LIVELIHOODS;
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
    return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
  }
  /* Compare both candidate inks against the fill and keep the better one. */
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

  var selected = D.cases[0].id;

  /* Vertex i of a regular pentagon, clockwise from the top, at radius r. */
  function vertex(cx, cy, r, i) {
    var a = -Math.PI / 2 + (i * 2 * Math.PI) / 5;
    return [cx + r * Math.cos(a), cy + r * Math.sin(a)];
  }

  function polygon(cx, cy, R, values) {
    return D.capitals.map(function (cap, i) {
      var p = vertex(cx, cy, R * (values[cap.id] / 100), i);
      return p[0].toFixed(1) + "," + p[1].toFixed(1);
    }).join(" ");
  }

  function ring(cx, cy, R, frac) {
    return D.capitals.map(function (_, i) {
      var p = vertex(cx, cy, R * frac, i);
      return p[0].toFixed(1) + "," + p[1].toFixed(1);
    }).join(" ");
  }

  /* --------------------------------------------------------- one pentagon */
  function pentagon(c, size, withLabels) {
    /* The box is wider than tall when labelled. A square one clipped the left
       and right vertices' names — FINANCIAL and SOCIAL sit at the widest
       points of a pentagon and are the two longest words, so the horizontal
       padding has to carry a whole word on each side while the vertical only
       has to carry a line and a number. */
    var pad = withLabels ? (size < 300 ? 30 : 38) : 6;
    var sidePad = withLabels ? (size < 300 ? 62 : 78) : 0;
    var H = size, W = size + 2 * sidePad;
    var cx = W / 2, cy = size / 2, R = size / 2 - pad;

    var svg = el("svg", {
      class: "lv-pent" + (withLabels ? " is-big" : ""),
      viewBox: "0 0 " + W + " " + H,
      preserveAspectRatio: "xMidYMid meet",
      role: "img",
      "aria-label": c.name + ". " + D.capitals.map(function (cap) {
        return cap.name + " " + c.assets[cap.id];
      }).join(", ") + ", each out of 100."
    });

    [0.25, 0.5, 0.75, 1].forEach(function (f) {
      svg.appendChild(el("polygon", { class: "lv-grid", points: ring(cx, cy, R, f) }));
    });
    D.capitals.forEach(function (_, i) {
      var p = vertex(cx, cy, R, i);
      svg.appendChild(el("line", { class: "lv-spoke", x1: cx, y1: cy, x2: p[0], y2: p[1] }));
    });

    svg.appendChild(el("polygon", { class: "lv-shape", points: polygon(cx, cy, R, c.assets) }));

    D.capitals.forEach(function (cap, i) {
      var v = vertex(cx, cy, R * (c.assets[cap.id] / 100), i);
      svg.appendChild(el("circle", {
        class: "lv-node", cx: v[0], cy: v[1], r: withLabels ? 5 : 3, fill: cap.color
      }));
      if (!withLabels) return;
      var lp = vertex(cx, cy, R + (size < 300 ? 14 : 18), i);
      /* Anchor by which side of the centre the vertex is on, so a label never
         runs back across the chart. */
      var anchor = Math.abs(lp[0] - cx) < 2 ? "middle" : (lp[0] > cx ? "start" : "end");
      /* Nudge the side labels clear of the shape rather than letting them ride
         the vertex, which is what pushed them off the edge. */
      if (anchor === "start") lp[0] += 6;
      if (anchor === "end") lp[0] -= 6;
      svg.appendChild(el("text", {
        class: "lv-axis lv-ax-" + cap.id, x: lp[0], y: lp[1] + 4, "text-anchor": anchor
      }, cap.name));
      svg.appendChild(el("text", {
        class: "lv-val lv-ax-" + cap.id, x: lp[0], y: lp[1] + 21, "text-anchor": anchor
      }, String(c.assets[cap.id])));
    });

    return svg;
  }

  /* ------------------------------------------------------- small multiples */
  function drawGrid() {
    var host = document.getElementById("assetGrid");
    if (!host) return;
    host.innerHTML = "";
    D.cases.forEach(function (c) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "lv-thumb" + (c.id === selected ? " is-on" : "");
      b.setAttribute("data-case", c.id);
      b.setAttribute("aria-pressed", c.id === selected ? "true" : "false");
      b.appendChild(pentagon(c, 120, false));
      var cap = document.createElement("span");
      cap.innerHTML = "<b>" + esc(c.name) + "</b><span>" + esc(c.short) + "</span>";
      b.appendChild(cap);
      b.addEventListener("click", function () { select(c.id); });
      host.appendChild(b);
    });
  }

  function drawBig() {
    var host = document.getElementById("assetPentagon");
    if (!host) return;
    var c = D.cases.filter(function (x) { return x.id === selected; })[0];
    host.innerHTML = "";
    host.appendChild(pentagon(c, host.clientWidth < 420 ? 320 : 400, true));
  }

  /* ----------------------------------------------------------------- panel */
  function drawPanel() {
    var host = document.getElementById("livePanel");
    var c = D.cases.filter(function (x) { return x.id === selected; })[0];
    if (!host || !c) return;
    var h = [];
    h.push('<div class="lv-head"><h3>' + esc(c.name) + "</h3><p>" + esc(c.short) + "</p></div>");

    h.push('<h4>The strategy</h4><p>' + esc(c.strategy) + "</p>");

    h.push('<h4>Vulnerability context</h4><dl class="lv-ctx">');
    D.contexts.forEach(function (x) {
      h.push("<dt>" + esc(x.name) + "</dt><dd>" + esc(c.context[x.id]) + "</dd>");
    });
    h.push("</dl>");

    h.push("<h4>Structures and processes that decide what the assets are worth</h4><p>" +
           esc(c.structures) + "</p>");
    h.push("<h4>How to read the shape</h4><p>" + esc(c.reading) + "</p>");
    h.push('<h4>What this does not settle</h4><p class="lv-comp">' + esc(c.complication) + "</p>");

    if (c.evidence && c.evidence.length) {
      h.push('<h4>The evidence</h4><ul class="lv-ev">');
      c.evidence.forEach(function (e) {
        h.push("<li><b>" + esc(e.stat) + "</b> &mdash; " + esc(e.detail) +
               ' <span class="lv-src">' + esc(e.source) + ", " + esc(e.year) + "</span></li>");
      });
      h.push("</ul>");
    }
    host.innerHTML = h.join("");
  }

  function select(id) {
    selected = id;
    drawGrid();
    drawBig();
    drawPanel();
  }

  function buildKey() {
    var host = document.getElementById("capitalKey");
    if (!host) return;
    host.innerHTML = D.capitals.map(function (cap) {
      return '<div class="lv-key"><span class="lv-key-sw" style="background:' + esc(cap.color) +
             ";color:" + esc(readableOn(cap.color)) + '">' + esc(cap.short) + "</span>" +
             "<b>" + esc(cap.name) + "</b><p>" + esc(cap.gloss) + "</p>" +
             '<p class="lv-key-d">' + esc(cap.detail) + "</p></div>";
    }).join("");
  }

  function init() {
    buildKey();
    select(selected);
    var t;
    window.addEventListener("resize", function () {
      clearTimeout(t);
      t = setTimeout(drawBig, 150);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
