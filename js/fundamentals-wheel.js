/* =============================================================================
   ImpactMojo — Fundamentals: clickable Indian Wheel of Power & Powerlessness
   Renders the wheel as SVG, wires selection / keyboard / deep links / marking,
   and builds an accessible text index of the same data.

   Depends on /js/fundamentals-data.js (window.FUNDAMENTALS).
   ============================================================================= */

window.FWheel = (function () {
  "use strict";

  var D = window.FUNDAMENTALS;
  var NS = "http://www.w3.org/2000/svg";

  var CX = 380, CY = 380;
  var R = { hub: 62, r1: 150, r2: 238, r3: 320, label: 336 };
  var RING_R = { power: [R.hub, R.r1], middle: [R.r1, R.r2], margin: [R.r2, R.r3] };
  var N = 12, SPAN = 360 / N;

  var state = { axis: null, ring: null, marking: false, marks: {} };
  var MARK_KEY = "im-fundamentals-marks";

  /* ---------------------------------------------------------------- colours */
  function hex2rgb(h) {
    h = h.replace("#", "");
    return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
  }
  function rgb2hex(c) {
    return "#" + c.map(function (v) {
      var s = Math.max(0, Math.min(255, Math.round(v))).toString(16);
      return s.length === 1 ? "0" + s : s;
    }).join("");
  }
  function mix(hexA, hexB, t) {
    var a = hex2rgb(hexA), b = hex2rgb(hexB);
    return rgb2hex([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t]);
  }
  function ringFill(base, ring) {
    if (ring === "power") return mix(base, "#000000", 0.30);
    if (ring === "middle") return base;
    return mix(base, "#ffffff", 0.42);
  }
  function readableOn(hex) {
    var c = hex2rgb(hex).map(function (v) {
      v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    var L = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
    return L > 0.42 ? "#241a20" : "#ffffff";
  }

  /* -------------------------------------------------------------- geometry */
  function pt(cx, cy, r, deg) {
    var a = (deg - 90) * Math.PI / 180;
    return [cx + r * Math.cos(a), cy + r * Math.sin(a)];
  }
  function annulusPath(a0, a1, rIn, rOut) {
    var p1 = pt(CX, CY, rOut, a0), p2 = pt(CX, CY, rOut, a1),
        p3 = pt(CX, CY, rIn, a1), p4 = pt(CX, CY, rIn, a0);
    var large = (a1 - a0) > 180 ? 1 : 0;
    return [
      "M", p1[0].toFixed(2), p1[1].toFixed(2),
      "A", rOut, rOut, 0, large, 1, p2[0].toFixed(2), p2[1].toFixed(2),
      "L", p3[0].toFixed(2), p3[1].toFixed(2),
      "A", rIn, rIn, 0, large, 0, p4[0].toFixed(2), p4[1].toFixed(2),
      "Z"
    ].join(" ");
  }
  /* Arc for text on a path. Reversed (anticlockwise) on the lower half so the
     label never renders upside down. */
  function textArc(a0, a1, r) {
    var mid = (a0 + a1) / 2, flip = mid > 90 && mid < 270;
    var s = flip ? a1 : a0, e = flip ? a0 : a1;
    var rr = flip ? r - 9 : r;
    var p1 = pt(CX, CY, rr, s), p2 = pt(CX, CY, rr, e);
    return ["M", p1[0].toFixed(2), p1[1].toFixed(2),
            "A", rr, rr, 0, 0, flip ? 0 : 1, p2[0].toFixed(2), p2[1].toFixed(2)].join(" ");
  }

  function el(name, attrs, text) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) if (attrs.hasOwnProperty(k)) n.setAttribute(k, attrs[k]);
    if (text != null) n.textContent = text;
    return n;
  }

  /* ----------------------------------------------------------------- build */
  function buildWheel() {
    var svg = document.getElementById("wheel");
    if (!svg) return;
    svg.setAttribute("viewBox", "0 0 760 760");
    svg.setAttribute("role", "group");
    svg.setAttribute("aria-label",
      "Interactive wheel: twelve axes of power, each with three bands from centre (closer to power) to rim (pushed to the margin). Select a band to read the evidence.");

    var defs = el("defs", {});
    svg.appendChild(defs);

    D.axes.forEach(function (axis, i) {
      var a0 = i * SPAN, a1 = a0 + SPAN;
      var g = el("g", { "data-axis": axis.id });

      D.RING_ORDER.forEach(function (ring) {
        var rr = RING_R[ring];
        var fill = ringFill(axis.color, ring);
        var wrap = el("g", { class: "segw", "data-axis": axis.id, "data-ring": ring });
        var path = el("path", {
          d: annulusPath(a0 + 0.35, a1 - 0.35, rr[0], rr[1]),
          fill: fill,
          class: "seg",
          role: "button",
          tabindex: "-1",
          "data-axis": axis.id,
          "data-ring": ring,
          "aria-label": axis.name + " — " + D.RING_LABEL[ring] + ": " + axis.rings[ring].short
        });
        wrap.appendChild(path);

        /* short label curved along the middle of the band */
        var rMid = (rr[0] + rr[1]) / 2;
        var id = "arc-" + axis.id + "-" + ring;
        defs.appendChild(el("path", { id: id, d: textArc(a0, a1, rMid) }));
        var t = el("text", {
          class: "seg-label r-" + ring,
          fill: readableOn(fill),
          "pointer-events": "none"
        });
        var tp = el("textPath", {
          href: "#" + id, startOffset: "50%", "text-anchor": "middle",
          "dominant-baseline": "middle"
        }, axis.rings[ring].short);
        tp.setAttributeNS("http://www.w3.org/1999/xlink", "xlink:href", "#" + id);
        t.appendChild(tp);
        wrap.appendChild(t);
        g.appendChild(wrap);
      });

      /* axis name around the rim */
      var lid = "arc-label-" + axis.id;
      defs.appendChild(el("path", { id: lid, d: textArc(a0, a1, R.label) }));
      var lt = el("text", { class: "axis-label" });
      var ltp = el("textPath", { href: "#" + lid, startOffset: "50%", "text-anchor": "middle" }, axis.name);
      ltp.setAttributeNS("http://www.w3.org/1999/xlink", "xlink:href", "#" + lid);
      lt.appendChild(ltp);
      g.appendChild(lt);

      svg.appendChild(g);
    });

    /* hub */
    svg.appendChild(el("circle", { cx: CX, cy: CY, r: R.hub, class: "hub" }));
    svg.appendChild(el("text", { x: CX, y: CY + 5, class: "hub-label" }, "POWER"));

  }

  /* ------------------------------------------------------------- selection */
  function segNode(axisId, ring) {
    return document.querySelector('#wheel .seg[data-axis="' + axisId + '"][data-ring="' + ring + '"]');
  }

  function select(axisId, ring, opts) {
    opts = opts || {};
    var axis = D.axes.filter(function (a) { return a.id === axisId; })[0];
    if (!axis || !axis.rings[ring]) return;
    state.axis = axisId; state.ring = ring;

    document.querySelectorAll("#wheel .seg, #wheel .segw").forEach(function (s) { s.classList.remove("is-active"); });
    var node = segNode(axisId, ring);
    if (node) {
      /* Raising the group re-inserts it in the DOM, which drops focus — so
         remember whether we had it and hand it back afterwards, otherwise the
         next arrow key never reaches the wheel's keydown handler. */
      var hadFocus = document.activeElement === node ||
                     (document.activeElement && document.activeElement.classList &&
                      document.activeElement.classList.contains("seg"));
      node.classList.add("is-active");
      node.parentNode.classList.add("is-active");
      node.parentNode.parentNode.appendChild(node.parentNode);  /* raise above neighbours */
      document.querySelectorAll("#wheel .seg").forEach(function (s) { s.setAttribute("tabindex", "-1"); });
      node.setAttribute("tabindex", "0");
      if (opts.focus || hadFocus) node.focus();
    }
    document.getElementById("wheelFrame").classList.add("wheel-dim");
    syncPickers();
    setCaption(axis, ring);
    renderPanel(axis, ring);
    if (!opts.silent) history.replaceState(null, "", "#" + axisId + "/" + ring);
  }

  function clearSelection() {
    state.axis = state.ring = null;
    document.querySelectorAll("#wheel .seg, #wheel .segw").forEach(function (s) { s.classList.remove("is-active"); });
    document.getElementById("wheelFrame").classList.remove("wheel-dim");
    syncPickers();
    setCaption(null, null);
    renderEmpty();
    history.replaceState(null, "", location.pathname);
  }

  /* ----------------------------------------------------------------- panel */
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function renderEmpty() {
    document.getElementById("panel").innerHTML =
      '<div class="panel-empty">' +
        '<h3>Pick a band on the wheel</h3>' +
        '<p>Each of the 36 bands opens the Indian evidence behind where it sits: the survey, the statute or the judgment, with the source and year given.</p>' +
        '<ol>' +
          '<li>The <b>hub</b> is power. The further out a group sits, the less of it that group holds.</li>' +
          '<li>Each wedge is one <b>axis</b>: caste, gender, language and nine others.</li>' +
          '<li>Each band carries a <b>“what this does not settle”</b> note. The wheel is a teaching tool, not a measurement.</li>' +
        '</ol>' +
      '</div>';
  }

  function renderPanel(axis, ring) {
    var band = axis.rings[ring];
    var h = [];
    h.push('<div class="panel-axis"><span class="swatch" style="background:' + esc(axis.color) + '"></span>' + esc(axis.name) + '</div>');
    h.push('<h3>' + esc(band.short) + '</h3>');
    h.push('<span class="ring-pos r-' + ring + '">' + esc(D.RING_LABEL[ring]) + '</span>');
    h.push('<p class="axis-q">' + esc(axis.question) + '</p>');
    h.push('<p class="who"><b>Who is in this band:</b> ' + esc(band.groups) + '</p>');

    h.push('<ul class="ev-list">');
    band.evidence.forEach(function (e) {
      var src = esc(e.source) + ', ' + esc(e.year);
      if (e.url) {
        /* only send people off-site in a new tab; our own explorers open in place */
        var ext = /^https?:/i.test(e.url) ? ' target="_blank" rel="noopener"' : '';
        src = '<a href="' + esc(e.url) + '"' + ext + '>' + src + '</a>';
      }
      h.push('<li class="ev"><div class="fig">' + esc(e.stat) + '</div>' +
             '<div class="txt">' + esc(e.detail) + '<span class="src">' + src + '</span></div></li>');
    });
    h.push('</ul>');

    h.push('<div class="caveat"><b>What this does not settle</b><p>' + esc(axis.complication) + '</p></div>');

    if (axis.links && axis.links.length) {
      h.push('<div class="panel-links">');
      axis.links.forEach(function (l) {
        h.push('<a href="' + esc(l.href) + '">' + esc(l.label) + '</a>');
      });
      h.push('</div>');
    }

    h.push('<div class="panel-nav">' +
      '<button class="btn-ghost" data-nav="out">Further out &rarr;</button>' +
      '<button class="btn-ghost" data-nav="in">&larr; Closer in</button>' +
      '<button class="btn-ghost" data-nav="next">Next axis</button>' +
      '<button class="btn-ghost" data-nav="clear">Clear</button>' +
      '</div>');

    var panel = document.getElementById("panel");
    panel.innerHTML = h.join("");
    panel.querySelectorAll("[data-nav]").forEach(function (b) {
      b.addEventListener("click", function () { navigate(b.getAttribute("data-nav")); });
    });
  }

  function navigate(dir) {
    if (dir === "clear") return clearSelection();
    var ai = D.axes.map(function (a) { return a.id; }).indexOf(state.axis);
    var ri = D.RING_ORDER.indexOf(state.ring);
    if (ai < 0) return;
    if (dir === "out") ri = Math.min(2, ri + 1);
    if (dir === "in") ri = Math.max(0, ri - 1);
    if (dir === "next") ai = (ai + 1) % D.axes.length;
    if (dir === "prev") ai = (ai - 1 + D.axes.length) % D.axes.length;
    select(D.axes[ai].id, D.RING_ORDER[ri], { focus: true });
  }

  /* -------------------------------------------------------- mark-your-place */
  function loadMarks() {
    try { state.marks = JSON.parse(localStorage.getItem(MARK_KEY) || "{}") || {}; }
    catch (e) { state.marks = {}; }
  }
  function saveMarks() {
    try { localStorage.setItem(MARK_KEY, JSON.stringify(state.marks)); } catch (e) {}
  }
  function toggleMark(axisId, ring) {
    if (state.marks[axisId] === ring) delete state.marks[axisId];
    else state.marks[axisId] = ring;
    saveMarks(); paintMarks(); renderMarks();
  }
  function paintMarks() {
    document.querySelectorAll("#wheel .seg").forEach(function (s) {
      var on = state.marks[s.getAttribute("data-axis")] === s.getAttribute("data-ring");
      s.classList.toggle("is-marked", on);
    });
  }
  function renderMarks() {
    var box = document.getElementById("marks");
    if (!box) return;
    var ids = Object.keys(state.marks);
    if (!ids.length) { box.hidden = true; return; }
    box.hidden = false;
    var rows = D.axes.filter(function (a) { return state.marks[a.id]; }).map(function (a) {
      var r = state.marks[a.id];
      return '<li><span>' + esc(a.name) + '</span><span>' + esc(a.rings[r].short) +
             ' &middot; ' + esc(D.RING_LABEL[r]) + '</span></li>';
    });
    box.innerHTML =
      '<h4>Where you marked yourself &mdash; ' + ids.length + ' of 12 axes</h4>' +
      '<p>Kept in this browser only and sent nowhere. Nothing is scored or totalled: a wheel is not a ranking of who has it worst.</p>' +
      '<ul>' + rows.join("") + '</ul>' +
      '<button class="btn-ghost" id="clearMarks">Clear my marks</button>';
    document.getElementById("clearMarks").addEventListener("click", function () {
      state.marks = {}; saveMarks(); paintMarks(); renderMarks();
    });
  }

  /* Labels are sized per ring by the arc that ring has, but the longest string
     in a ring can still overrun its 30-degree slice and spill onto the page
     background. Measure each one against its own arc and shrink only those
     that overflow, so a future label change cannot reintroduce it. */
  function fitLabels() {
    document.querySelectorAll("#wheel .seg-label").forEach(function (t) {
      var tp = t.querySelector("textPath");
      if (!tp) return;
      var href = tp.getAttribute("href") || tp.getAttributeNS("http://www.w3.org/1999/xlink", "href");
      var arc = href && document.querySelector("#wheel " + href);
      if (!arc || !arc.getTotalLength) return;
      var avail = arc.getTotalLength() * 0.92;
      var size = parseFloat(getComputedStyle(t).fontSize) || 9;
      for (var i = 0; i < 12; i++) {
        var len = 0;
        try { len = t.getComputedTextLength(); } catch (e) { return; }
        if (!len || len <= avail || size <= 6.5) break;
        size = Math.max(6.5, size * Math.max(0.86, avail / len));
        t.setAttribute("font-size", size.toFixed(2));
      }
    });
  }

  /* ------------------------------------------------------------- caption */
  /* Below 760px the segment labels would render at about 4px, so they are
     hidden and this carries the selection at real text size instead. It is
     useful at every width, which is why it is not itself behind a query. */
  function setCaption(axis, ring) {
    var box = document.getElementById("wheelCaption");
    if (!box) return;
    if (!axis) {
      box.className = "wheel-caption is-empty";
      box.innerHTML = '<span class="cap-t">Nothing selected yet. Pick a band on the wheel, or use the buttons below.</span>';
      return;
    }
    box.className = "wheel-caption";
    box.innerHTML = '<span class="cap-sw" style="background:' + esc(axis.color) + '"></span>' +
      '<span><span class="cap-s">' + esc(axis.name) + ' &middot; ' + esc(D.RING_LABEL[ring]) + '</span>' +
      '<span class="cap-t">' + esc(axis.rings[ring].short) + '</span></span>';
  }

  /* --------------------------------------------------------------- pickers */
  /* On a 390px phone the inner segments are ~30px across and their labels
     render at ~3px, so the wheel cannot be the only control. These chips
     select the same 36 bands with 44px targets at any width. */
  function buildPickers() {
    var ax = document.getElementById("axisChips");
    var rg = document.getElementById("ringChips");
    if (!ax || !rg) return;

    ax.innerHTML = D.axes.map(function (a) {
      return '<button type="button" class="chip" data-axis="' + esc(a.id) + '" aria-pressed="false">' +
             '<span class="sw" style="background:' + esc(a.color) + '"></span>' + esc(a.name) + '</button>';
    }).join("");

    rg.innerHTML = D.RING_ORDER.map(function (r) {
      return '<button type="button" class="chip" data-ring="' + r + '" aria-pressed="false">' +
             esc(D.RING_LABEL[r]) + '</button>';
    }).join("");

    ax.querySelectorAll("[data-axis]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        select(btn.getAttribute("data-axis"), state.ring || "margin");
      });
    });
    rg.querySelectorAll("[data-ring]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        select(state.axis || D.axes[0].id, btn.getAttribute("data-ring"));
      });
    });
  }

  function syncPickers() {
    document.querySelectorAll("#axisChips [data-axis]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-axis") === state.axis));
    });
    document.querySelectorAll("#ringChips [data-ring]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-ring") === state.ring));
    });
  }

  /* ----------------------------------------------------------- text index */
  function buildIndex() {
    var box = document.getElementById("axisIndex");
    if (!box) return;
    var h = D.axes.map(function (axis) {
      var rings = D.RING_ORDER.map(function (ring) {
        var b = axis.rings[ring];
        var ev = b.evidence.map(function (e) {
          return '<li><b>' + esc(e.stat) + '</b> — ' + esc(e.detail) +
                 ' <i>(' + esc(e.source) + ', ' + esc(e.year) + ')</i></li>';
        }).join("");
        return '<div class="ax-ring"><h4>' + esc(D.RING_LABEL[ring]) + ' — ' + esc(b.short) + '</h4>' +
               '<p>' + esc(b.groups) + '</p><ul>' + ev + '</ul></div>';
      }).join("");
      return '<details class="ax" id="ax-' + esc(axis.id) + '">' +
        '<summary><span class="swatch" style="background:' + esc(axis.color) + '"></span>' +
          '<h3>' + esc(axis.name) + '</h3> <span class="q">' + esc(axis.question) + '</span></summary>' +
        '<div class="ax-body"><p>' + esc(axis.intro) + '</p>' + rings +
          '<div class="caveat"><b>What this does not settle</b><p>' + esc(axis.complication) + '</p></div>' +
        '</div></details>';
    }).join("");
    box.innerHTML = h;
  }

  /* --------------------------------------------------------------- wiring */
  function onSegActivate(node) {
    var a = node.getAttribute("data-axis"), r = node.getAttribute("data-ring");
    if (state.marking) toggleMark(a, r);
    select(a, r);
  }

  function wire() {
    var svg = document.getElementById("wheel");

    svg.addEventListener("click", function (e) {
      var t = e.target.closest ? e.target.closest(".seg") : null;
      if (t) onSegActivate(t);
    });

    svg.addEventListener("keydown", function (e) {
      var t = e.target;
      if (!t || !t.classList || !t.classList.contains("seg")) return;
      if (e.key === "Enter" || e.key === " " || e.key === "Spacebar") {
        e.preventDefault(); onSegActivate(t); return;
      }
      var map = { ArrowRight: "next", ArrowLeft: "prev", ArrowUp: "in", ArrowDown: "out" };
      if (map[e.key]) {
        e.preventDefault();
        if (!state.axis) select(t.getAttribute("data-axis"), t.getAttribute("data-ring"), { focus: true });
        else navigate(map[e.key]);
      }
      if (e.key === "Escape") { e.preventDefault(); clearSelection(); }
    });

    /* one tab stop into the wheel */
    var first = document.querySelector("#wheel .seg");
    if (first) first.setAttribute("tabindex", "0");

    var mk = document.getElementById("markToggle");
    if (mk) mk.addEventListener("click", function () {
      state.marking = !state.marking;
      mk.setAttribute("aria-pressed", String(state.marking));
      mk.textContent = state.marking ? "Marking on — click a band" : "Mark where you sit";
    });

    var rst = document.getElementById("resetView");
    if (rst) rst.addEventListener("click", clearSelection);

    window.addEventListener("hashchange", fromHash);
  }

  function fromHash() {
    var m = (location.hash || "").replace("#", "").split("/");
    if (m.length === 2 && D.axes.some(function (a) { return a.id === m[0]; }) && D.RING_ORDER.indexOf(m[1]) > -1) {
      select(m[0], m[1], { silent: true });
      /* a shared link should land on the wheel, not the top of the page */
      var sec = document.getElementById("wheel-section");
      if (sec) sec.scrollIntoView({ behavior: "auto", block: "start" });
      return true;
    }
    return false;
  }

  function init() {
    if (!D || !D.axes) return;
    buildWheel();
    fitLabels();
    buildPickers();
    setCaption(null, null);
    buildIndex();
    loadMarks();
    paintMarks();
    renderMarks();
    wire();
    if (!fromHash()) renderEmpty();
  }

  return { init: init, select: select };
})();
