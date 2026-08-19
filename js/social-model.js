/* =============================================================================
   ImpactMojo — Fundamentals: The Social Model of Disability
   -----------------------------------------------------------------------------
   The barrier stack. A person at the foot, an outcome at the head, and four
   bands between them whose width is how much of the way each one blocks. The
   channel left clear on the right is what gets through.

   Labels sit ON the bands rather than beside them, so every one of them is
   painted on a known fill and its ink can be chosen by contrast ratio. The two
   previous pages in this series put labels on the page ground and both needed
   a theme-aware ink added afterwards; this avoids the problem rather than
   fixing it twice.
   ============================================================================= */

(function () {
  "use strict";

  var D = window.SOCIAL_MODEL;
  if (!D) return;

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
  /* Compare both candidate inks against the fill and take the better one. */
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

  var selected = D.domains[0].id;
  var openBarrier = null;

  function kindOf(id) {
    return D.kinds.filter(function (k) { return k.id === id; })[0];
  }

  /* ------------------------------------------------------------ the stack */
  function drawStack() {
    var host = document.getElementById("barrierStack");
    if (!host) return;
    var d = D.domains.filter(function (x) { return x.id === selected; })[0];
    host.innerHTML = "";

    var narrow = host.clientWidth < 460;
    var W = narrow ? 340 : 520;
    var bandH = narrow ? 52 : 58;
    var gap = 10;
    var headH = narrow ? 74 : 68;
    var footH = narrow ? 54 : 50;
    var H = headH + 4 * (bandH + gap) + footH + 10;
    var padX = 12;
    var innerW = W - padX * 2;

    var svg = el("svg", {
      class: "sm-svg", role: "img",
      viewBox: "0 0 " + W + " " + H,
      preserveAspectRatio: "xMidYMid meet",
      "aria-label": "Barrier stack for " + d.name + ". Four barriers stand between a " +
        "person and the outcome, widest first: " +
        d.barriers.slice().sort(function (a, b) { return b.weight - a.weight; })
          .map(function (b) {
            return kindOf(b.kind).name + " blocking " + b.weight + " per cent of the way";
          }).join(", ") + ". The recorded outcome is " + d.outcome.stat + " " + d.outcome.label + "."
    });

    /* the outcome, at the head */
    svg.appendChild(el("text", {
      class: "sm-out-stat", x: W / 2, y: 30, "text-anchor": "middle"
    }, d.outcome.stat));
    var lines = wrap(d.outcome.label, narrow ? 38 : 52);
    lines.slice(0, 2).forEach(function (ln, i) {
      svg.appendChild(el("text", {
        class: "sm-out-label", x: W / 2, y: 48 + i * 13, "text-anchor": "middle"
      }, ln));
    });

    /* Widest first. The question the stack is built to answer is which layer
       blocks most here, and a descending order answers it before the numbers
       are read. The colour and the name carry the kind, so ordering by weight
       costs nothing in identifying which barrier is which. */
    var bars = d.barriers.slice().sort(function (a, b) { return b.weight - a.weight; });

    bars.forEach(function (b, i) {
      var k = kindOf(b.kind);
      var y = headH + i * (bandH + gap);
      var blockW = Math.max(28, innerW * (b.weight / 100));
      var g = el("g", {
        class: "sm-band" + (openBarrier === b.kind ? " is-on" : ""),
        tabindex: "0", role: "button",
        "aria-pressed": openBarrier === b.kind ? "true" : "false",
        "aria-label": k.name + " barrier, blocking " + b.weight + " per cent. " + b.text
      });

      /* the whole width, faint: the path if nothing blocked it */
      g.appendChild(el("rect", {
        class: "sm-open", x: padX, y: y, width: innerW, height: bandH, rx: 8
      }));
      /* the blocking part */
      g.appendChild(el("rect", {
        class: "sm-block", x: padX, y: y, width: blockW, height: bandH, rx: 8, fill: k.color
      }));

      var ink = readableOn(k.color);
      g.appendChild(el("text", {
        class: "sm-band-name", x: padX + 14, y: y + (narrow ? 22 : 24), fill: ink
      }, k.name));
      g.appendChild(el("text", {
        class: "sm-band-pct", x: padX + 14, y: y + (narrow ? 40 : 43), fill: ink
      }, b.weight + "% of the way"));

      svg.appendChild(g);
    });

    /* the person, at the foot */
    var fy = headH + 4 * (bandH + gap) + 18;
    svg.appendChild(el("text", {
      class: "sm-foot", x: W / 2, y: fy, "text-anchor": "middle"
    }, "a person with an impairment"));
    svg.appendChild(el("text", {
      class: "sm-foot-note", x: W / 2, y: fy + 16, "text-anchor": "middle"
    }, "the medical model stops here"));

    host.appendChild(svg);

    /* wire after append so the nodes exist */
    var groups = svg.querySelectorAll(".sm-band");
    bars.forEach(function (b, i) {
      var g = groups[i];
      if (!g) return;
      g.addEventListener("click", function () { toggle(b.kind); });
      g.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(b.kind); }
      });
    });
  }

  function wrap(text, per) {
    var words = String(text).split(/\s+/), out = [], line = "";
    words.forEach(function (w) {
      if (!line.length) { line = w; return; }
      if ((line + " " + w).length <= per) line += " " + w;
      else { out.push(line); line = w; }
    });
    if (line.length) out.push(line);
    return out;
  }

  function toggle(kind) {
    openBarrier = openBarrier === kind ? null : kind;
    drawStack();
    drawPanel();
  }

  /* ----------------------------------------------------------------- panel */
  function drawPanel() {
    var host = document.getElementById("smPanel");
    var d = D.domains.filter(function (x) { return x.id === selected; })[0];
    if (!host || !d) return;
    var h = [];

    h.push('<div class="sm-head"><h3>' + esc(d.name) + "</h3><p>" + esc(d.short) + "</p></div>");
    h.push('<div class="sm-outcome"><b>' + esc(d.outcome.stat) + "</b> " + esc(d.outcome.label) +
           "<br><b>" + esc(d.outcome.second) + "</b> " + esc(d.outcome.secondLabel) + "</div>");

    if (openBarrier) {
      var b = d.barriers.filter(function (x) { return x.kind === openBarrier; })[0];
      var k = kindOf(openBarrier);
      h.push('<div class="sm-open-barrier" style="border-left-color:' + esc(k.color) + '">');
      h.push('<span class="sm-tag" style="background:' + esc(k.color) + ";color:" +
             esc(readableOn(k.color)) + '">' + esc(k.name) + " &middot; " + b.weight + "%</span>");
      h.push("<p>" + esc(b.text) + "</p></div>");
    }

    h.push("<h4>How to read the stack</h4><p>" + esc(d.reading) + "</p>");
    h.push('<h4>What this does not settle</h4><p class="sm-comp">' + esc(d.complication) + "</p>");

    h.push('<h4>The evidence</h4><ul class="sm-ev">');
    d.evidence.forEach(function (e) {
      h.push("<li><b>" + esc(e.stat) + "</b> &mdash; " + esc(e.detail) +
             ' <span class="sm-src">' + esc(e.source) + ", " + esc(e.year) + "</span></li>");
    });
    h.push("</ul>");
    host.innerHTML = h.join("");
  }

  function select(id) {
    selected = id;
    openBarrier = null;
    document.querySelectorAll("#smPicker [data-domain]").forEach(function (b) {
      var on = b.getAttribute("data-domain") === id;
      b.classList.toggle("is-on", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
    drawStack();
    drawPanel();
  }

  function buildPicker() {
    var host = document.getElementById("smPicker");
    if (!host) return;
    host.innerHTML = D.domains.map(function (d) {
      return '<button type="button" class="sm-btn" data-domain="' + esc(d.id) +
             '" aria-pressed="false"><b>' + esc(d.name) + "</b><span>" +
             esc(d.short) + "</span></button>";
    }).join("");
    host.querySelectorAll("[data-domain]").forEach(function (b) {
      b.addEventListener("click", function () { select(b.getAttribute("data-domain")); });
    });
  }

  function buildKinds() {
    var host = document.getElementById("barrierKinds");
    if (!host) return;
    host.innerHTML = D.kinds.map(function (k) {
      return '<div class="sm-kind"><span class="sm-kind-sw" style="background:' + esc(k.color) +
             '"></span><b>' + esc(k.name) + "</b><p>" + esc(k.gloss) + "</p>" +
             '<p class="sm-kind-d">' + esc(k.detail) + "</p></div>";
    }).join("");
  }

  function buildModels() {
    var host = document.getElementById("twoModels");
    if (!host) return;
    host.innerHTML = ["medical", "social"].map(function (id) {
      var m = D.models[id];
      return '<div class="sm-model sm-' + id + '"><h3>' + esc(m.name) + "</h3><p class=\"sm-model-g\">" +
             esc(m.gloss) + "</p><p>" + esc(m.detail) + "</p></div>";
    }).join("");
  }

  function init() {
    buildKinds();
    buildModels();
    buildPicker();
    select(selected);
    var t;
    window.addEventListener("resize", function () {
      clearTimeout(t);
      t = setTimeout(drawStack, 150);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
