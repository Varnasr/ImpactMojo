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
  var NS = "http://www.w3.org/2000/svg";

  function el(name, attrs, text) {
    var n = document.createElementNS(NS, name);
    Object.keys(attrs || {}).forEach(function (k) { n.setAttribute(k, attrs[k]); });
    if (text !== undefined) n.appendChild(document.createTextNode(text));
    return n;
  }

  /* Wrap a label to a pixel width without a measuring pass: SVG has no text
     wrapping, and a per-glyph measure would reflow on every resize. */
  function wrap(text, chars) {
    var words = String(text).split(/\s+/), lines = [], cur = "";
    words.forEach(function (w) {
      if ((cur + " " + w).trim().length > chars && cur) { lines.push(cur); cur = w; }
      else cur = (cur + " " + w).trim();
    });
    if (cur) lines.push(cur);
    return lines;
  }

  /**
   * The conversion chain, drawn.
   *
   * The point the picture has to make is that the three conversion factors are
   * inputs to the second stage rather than decoration around it, and that what
   * fails to convert leaves the chain instead of arriving at the far end. So the
   * factors feed in from below and there is a visible leak between conversion
   * and capability. Where a chain has a real pair of figures, the leak carries
   * them.
   *
   * Two layouts, chosen by width rather than by CSS: at narrow widths a
   * four-across flow would shrink the type past legibility, so the stages stack.
   */
  function drawChain(chain) {
    var host = document.getElementById("chainDiagram");
    if (!host) return;
    var vertical = host.clientWidth < 700;
    host.innerHTML = "";

    var svg = el("svg", {
      class: "cap-svg",
      role: "img",
      "aria-label": "The conversion chain: a resource passes through personal, social and " +
        "environmental conversion factors to become a capability, and then a functioning. " +
        "What does not convert leaves the chain."
    });

    var W = vertical ? 380 : 900;
    var H = vertical ? 660 : 250;
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.setAttribute("preserveAspectRatio", "xMidYMid meet");

    var boxW = vertical ? 250 : 170;
    var boxH = vertical ? 82 : 82;
    var stages = D.stages;

    /* Narrow layout spacing is uneven on purpose: the gap after Conversion
       carries the leak and its figures, so it needs more room than the others.
       Even spacing put the leak label on top of a factor label. */
    var vY = [16, 168, 360, 512];
    function pos(i) {
      return vertical
        ? { x: 20, y: vY[i] }
        : { x: 24 + i * 218, y: 24 };
    }

    /* connectors first, so the boxes sit on top of them */
    for (var i = 0; i < stages.length - 1; i++) {
      var a = pos(i), b = pos(i + 1);
      var line = vertical
        ? el("path", { d: "M" + (a.x + boxW / 2) + " " + (a.y + boxH) + " L" + (a.x + boxW / 2) + " " + b.y })
        : el("path", { d: "M" + (a.x + boxW) + " " + (a.y + boxH / 2) + " L" + b.x + " " + (b.y + boxH / 2) });
      line.setAttribute("class", "cap-flow");
      svg.appendChild(line);
      var mx = vertical ? a.x + boxW / 2 : (a.x + boxW + b.x) / 2;
      var my = vertical ? (a.y + boxH + b.y) / 2 : a.y + boxH / 2;
      var head = el("path", {
        class: "cap-arrow",
        d: vertical
          ? "M" + (mx - 5) + " " + (my - 4) + " L" + mx + " " + (my + 5) + " L" + (mx + 5) + " " + (my - 4) + " Z"
          : "M" + (mx - 4) + " " + (my - 5) + " L" + (mx + 5) + " " + my + " L" + (mx - 4) + " " + (my + 5) + " Z"
      });
      svg.appendChild(head);
    }

    /* The three conversion factors feed the second stage from below.

       Wide layout: a labelled feed line each, under the Conversion box.
       Narrow layout: no side column. It did not fit — ENVIRONMENTAL ran past
       the viewBox edge and the leak label landed on top of it — and it was
       redundant there anyway, because the Conversion box's own body text reads
       "Personal, social, environmental". The colour coding is kept as a legend
       along the foot of the diagram instead. */
    var convo = pos(1);
    var kinds = ["personal", "social", "environmental"];
    if (!vertical) {
      kinds.forEach(function (kind, k) {
        var fx = convo.x + boxW / 2 + (k - 1) * 150;
        var fy = convo.y + boxH + 66;
        svg.appendChild(el("path", {
          class: "cap-feed cf-" + kind,
          d: "M" + fx + " " + fy + " L" + (convo.x + boxW / 2) + " " + (convo.y + boxH)
        }));
        svg.appendChild(el("text", {
          class: "cap-feed-label", x: fx, y: fy + 14, "text-anchor": "middle"
        }, D.FACTOR_LABEL[kind]));
      });
    }

    /* the leak: what the resource promised and the capability delivered */
    var cap = pos(2);
    /* The leak leaves the conversion-to-capability connector, which is where a
       resource stops becoming a freedom, and ends where its figures are printed
       so the number is attached to the path rather than floating near it. */
    var sx = vertical ? cap.x + boxW / 2 : cap.x - 24;
    var sy = vertical ? convo.y + boxH + 18 : cap.y + boxH / 2;
    var ex = vertical ? 300 : cap.x + 46;
    var ey = vertical ? convo.y + boxH + 55 : cap.y + boxH + 62;
    var leak = el("path", {
      class: "cap-leak",
      d: vertical
        /* Both control points sit on the approach side of the end point. With
           the second one past it the curve turned back up and drew a tick at
           the tip that read as a second arrow. */
        ? "M" + sx + " " + sy + " C" + (sx + 50) + " " + sy + " " + (ex - 50) + " " + ey + " " + ex + " " + ey
        : "M" + sx + " " + sy + " C" + sx + " " + (sy + 40) + " " + (ex - 30) + " " + ey + " " + ex + " " + ey
    });
    svg.appendChild(leak);

    /* Only print a pair when both halves are actually quantities. Several chains
       carry a headline like "Legal right" against "2011", which is a real point
       on the page but reads as nonsense on a leak arrow. */
    var hasFigures = chain && chain.headline &&
      /\d/.test(String(chain.headline.stat || "")) &&
      /%|\d/.test(String(chain.headline.contrast || "")) &&
      /%/.test(String(chain.headline.stat) + String(chain.headline.contrast));
    var leakText = hasFigures
      ? chain.headline.stat + " \u2192 " + chain.headline.contrast
      : "what does not convert";
    /* Narrow: the label gets its own line under the curve and is centred, so
       its length cannot push it off the edge whatever the figures are. */
    var lt = el("text", {
      class: "cap-leak-label",
      x: vertical ? W / 2 : ex + 8,
      y: vertical ? ey + 30 : ey + 4,
      "text-anchor": vertical ? "middle" : "start"
    }, leakText);
    svg.appendChild(lt);

    /* the four stages */
    stages.forEach(function (st, i) {
      var p = pos(i);
      var ink = readableOn(st.color);
      var g = el("g", { class: "cap-node" });
      g.appendChild(el("rect", {
        x: p.x, y: p.y, width: boxW, height: boxH, rx: 12,
        fill: st.color, class: "cap-node-box"
      }));
      g.appendChild(el("text", {
        x: p.x + 13, y: p.y + 25, fill: ink, class: "cap-node-n"
      }, String(i + 1)));
      g.appendChild(el("text", {
        x: p.x + 32, y: p.y + 25, fill: ink, class: "cap-node-name"
      }, st.name));

      var body = chain ? chainTextFor(chain, st.id) : st.gloss;
      /* Two lines at most, and the box is tall enough for both: a third line,
         or a tighter box, pushes the descender past the fill. */
      wrap(body, vertical ? 34 : 24).slice(0, 2).forEach(function (ln, k) {
        g.appendChild(el("text", {
          x: p.x + 13, y: p.y + 47 + k * 15, fill: ink, class: "cap-node-sub"
        }, ln));
      });
      svg.appendChild(g);
    });

    host.appendChild(svg);

    /* Narrow-layout legend: keeps the colour coding of the three factors
       without a column that does not fit. Laid out after the SVG is in the
       document so each label can be measured rather than estimated — these are
       letter-spaced uppercase, and a character-count guess put the second
       dash on top of the first word. */
    if (vertical) {
      var lx = 16;
      kinds.forEach(function (kind) {
        var t = el("text", {
          class: "cap-feed-label", x: 0, y: H - 14, "text-anchor": "start"
        }, D.FACTOR_LABEL[kind]);
        svg.appendChild(t);
        var dash = el("path", {
          class: "cap-feed cf-" + kind,
          d: "M" + lx + " " + (H - 18) + " L" + (lx + 14) + " " + (H - 18)
        });
        svg.appendChild(dash);
        t.setAttribute("x", lx + 19);
        lx += 19 + t.getComputedTextLength() + 14;
      });
    }
  }

  /* What each stage says depends on which resource is open. */
  function chainTextFor(chain, stageId) {
    if (stageId === "resource") return chain.name;
    if (stageId === "capability") return chain.capability;
    if (stageId === "functioning") return chain.functioning;
    return "Personal, social, environmental";
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
    drawChain(c);
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
    drawChain(null);
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
  var resizeT = null;
  function onResize() {
    clearTimeout(resizeT);
    resizeT = setTimeout(function () {
      var c = state.chain ? D.chains.filter(function (x) { return x.id === state.chain; })[0] : null;
      drawChain(c || null);
    }, 150);
  }

  function init() {
    drawChain(null);
    window.addEventListener("resize", onResize);
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
