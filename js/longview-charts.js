/* The Long View — shared chart engine. window.LV = { renderAll, drawMasters, buildCards, wireFilters, heroDots, reveal, VIZ } */
window.LV = (function() {
  var NS = "http://www.w3.org/2000/svg";
  function mk(tag, attrs, text) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    return e;
  }
  function clear(el) { while (el && el.firstChild) el.removeChild(el.firstChild); }
  function ink() { return (getComputedStyle(document.documentElement).getPropertyValue('--chart-ink') || '#475569').trim(); }
  function gridc() { return (getComputedStyle(document.documentElement).getPropertyValue('--chart-grid') || '#e8edf4').trim(); }
  function css(name, fallback) { return (getComputedStyle(document.documentElement).getPropertyValue(name) || fallback).trim() || fallback; }
  function reduced() { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; }

  var W = 460, H = 290;
  var COL = { blue: '#4361ee', teal: '#0d9488', amber: '#f59e0b', red: '#e11d48', purple: '#7c3aed', green: '#16a34a', slate: '#64748b' };

  function frame(id) {
    var svg = document.getElementById(id); if (!svg) return null;
    clear(svg); svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H); return svg;
  }
  function animPath(path) {
    if (reduced() || !path.getTotalLength) return;
    var len = path.getTotalLength(); if (!len) return;
    path.style.strokeDasharray = len; path.style.strokeDashoffset = len;
    path.style.transition = 'stroke-dashoffset 1.3s ease';
    requestAnimationFrame(function(){ path.style.strokeDashoffset = 0; });
  }
  function fadeIn(node, delay) {
    if (reduced()) return;
    node.style.opacity = 0; node.style.transition = 'opacity 0.6s ease ' + (delay || 0) + 's';
    requestAnimationFrame(function(){ node.style.opacity = 1; });
  }

  /* ---------- Generic line chart ---------- */
  /* ===== shared design helpers ===== */
  function ensureDefs(svg) { var d = svg.querySelector('defs'); if (!d) { d = mk('defs', {}); svg.insertBefore(d, svg.firstChild); } return d; }
  function vGrad(svg, gid, color, topOp, botOp) {
    var g = mk('linearGradient', { id: gid, x1: '0', y1: '0', x2: '0', y2: '1' });
    g.appendChild(mk('stop', { offset: '0', 'stop-color': color, 'stop-opacity': topOp }));
    g.appendChild(mk('stop', { offset: '1', 'stop-color': color, 'stop-opacity': botOp }));
    ensureDefs(svg).appendChild(g); return 'url(#' + gid + ')';
  }
  function smooth(pts) {
    if (pts.length < 3) return 'M' + pts.map(function(p){ return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' L');
    var d = 'M' + pts[0][0].toFixed(1) + ',' + pts[0][1].toFixed(1);
    for (var i = 0; i < pts.length - 1; i++) {
      var p0 = pts[i-1] || pts[i], p1 = pts[i], p2 = pts[i+1], p3 = pts[i+2] || p2;
      var c1x = p1[0] + (p2[0]-p0[0])/6, c1y = p1[1] + (p2[1]-p0[1])/6;
      var c2x = p2[0] - (p3[0]-p1[0])/6, c2y = p2[1] - (p3[1]-p1[1])/6;
      d += ' C' + c1x.toFixed(1) + ',' + c1y.toFixed(1) + ' ' + c2x.toFixed(1) + ',' + c2y.toFixed(1) + ' ' + p2[0].toFixed(1) + ',' + p2[1].toFixed(1);
    }
    return d;
  }
  function callout(svg, x, y, anchor, lines) {
    var yy = y;
    lines.forEach(function(ln) {
      svg.appendChild(mk('text', { x: x, y: yy, 'text-anchor': anchor, 'font-size': ln.s || 11, 'font-weight': ln.w || 400, fill: ln.c || ink(), 'font-family': ln.f || 'Inter, sans-serif' }, ln.t));
      yy += ln.gap || ((ln.s || 11) + 4);
    });
  }
  function tick(svg, x, y, txt, anchor) {
    svg.appendChild(mk('text', { x: x, y: y, 'text-anchor': anchor || 'middle', 'font-size': 9.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, txt));
  }

  /* ---------- Line / area chart with annotation callout ---------- */
  function lineChart(id, data, o) {
    var svg = frame(id); if (!svg) return;
    var mL = 30, mR = 54, mT = 30, mB = 36;
    var xs = data.map(function(d){ return d.x; });
    var xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs), yMax = o.yMax;
    function X(x){ return mL + (x - xmin) / (xmax - xmin) * (W - mL - mR); }
    function Y(y){ return H - mB - (y / yMax) * (H - mT - mB); }
    var pts = data.map(function(p){ return [X(p.x), Y(p.y)]; });
    svg.appendChild(mk('line', { x1: mL, y1: Y(0), x2: W - mR, y2: Y(0), stroke: gridc(), 'stroke-width': 1 }));
    var lineD = smooth(pts);
    if (o.area) {
      var fill = vGrad(svg, id + '-area', o.color, 0.32, 0.015);
      svg.appendChild(mk('path', { d: lineD + ' L' + X(xmax).toFixed(1) + ',' + Y(0).toFixed(1) + ' L' + X(xmin).toFixed(1) + ',' + Y(0).toFixed(1) + ' Z', fill: fill }));
    }
    var path = mk('path', { d: lineD, fill: 'none', stroke: o.color, 'stroke-width': 3, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' });
    svg.appendChild(path); animPath(path);
    data.forEach(function(p, i){
      var isEnd = (i === 0 || i === data.length - 1);
      if (isEnd || (o.labelEvery && i % o.labelEvery === 0)) tick(svg, X(p.x), H - mB + 16, o.xfmt ? o.xfmt(p.x) : p.x);
      svg.appendChild(mk('circle', { cx: X(p.x), cy: Y(p.y), r: isEnd ? 5 : 3, fill: o.color, stroke: '#fff', 'stroke-width': isEnd ? 1.6 : 0 }));
    });
    var f = data[0], l = data[data.length - 1];
    svg.appendChild(mk('text', { x: X(f.x) + 8, y: Y(f.y) - 11, 'text-anchor': 'start', 'font-size': 15, 'font-weight': 800, fill: o.color, 'font-family': 'Inter, sans-serif' }, o.valfmt(f.y)));
    svg.appendChild(mk('text', { x: X(l.x) - 6, y: Y(l.y) - 11, 'text-anchor': 'end', 'font-size': 15, 'font-weight': 800, fill: o.color, 'font-family': 'Inter, sans-serif' }, o.valfmt(l.y)));
    if (o.callout) callout(svg, o.callout.x, o.callout.y, o.callout.anchor, o.callout.lines);
  }

  /* ---------- Vertical bar chart with reference line ---------- */
  function barChart(id, data, o) {
    var svg = frame(id); if (!svg) return;
    var mL = 18, mR = 66, mT = 30, mB = 42;
    var yMax = o.yMax, n = data.length, gap = 30;
    var bw = (W - mL - mR - gap * (n - 1)) / n;
    function Y(y){ return H - mB - (y / yMax) * (H - mT - mB); }
    svg.appendChild(mk('line', { x1: mL, y1: Y(0), x2: W - mR, y2: Y(0), stroke: ink(), 'stroke-width': 1.4 }));
    data.forEach(function(dd, i){
      var x = mL + i * (bw + gap);
      var fill = vGrad(svg, id + '-b' + i, dd.color, dd.highlight ? 1 : 0.78, dd.highlight ? 0.72 : 0.5);
      var rect = mk('rect', { x: x, y: Y(dd.y), width: bw, height: Y(0) - Y(dd.y), rx: 7, fill: fill });
      svg.appendChild(rect); fadeIn(rect, i * 0.1);
      svg.appendChild(mk('text', { x: x + bw/2, y: Y(dd.y) - 9, 'text-anchor': 'middle', 'font-size': 15, 'font-weight': 800, fill: dd.color, 'font-family': 'Inter, sans-serif' }, o.valfmt(dd.y)));
      svg.appendChild(mk('text', { x: x + bw/2, y: H - mB + 18, 'text-anchor': 'middle', 'font-size': 12, 'font-weight': dd.highlight ? 700 : 400, fill: ink(), 'font-family': 'Amaranth, sans-serif' }, dd.label));
    });
    if (o.refLine) {
      var ry = Y(o.refLine.value);
      svg.appendChild(mk('line', { x1: mL, y1: ry, x2: W - mR + 6, y2: ry, stroke: ink(), 'stroke-width': 1, 'stroke-dasharray': '5,4', opacity: 0.7 }));
      svg.appendChild(mk('text', { x: W - mR + 10, y: ry - 4, 'font-size': 9.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.refLine.label));
    }
    if (o.callout) callout(svg, o.callout.x, o.callout.y, o.callout.anchor, o.callout.lines);
  }

  /* ---------- Horizontal bar chart with reference line ---------- */
  function hbarChart(id, data, o) {
    var svg = frame(id); if (!svg) return;
    var mL = 108, mR = 50, mT = 24, mB = 28;
    var xMax = o.xMax, n = data.length, gap = 18;
    var bh = (H - mT - mB - gap * (n - 1)) / n;
    function Xv(v){ return mL + (v / xMax) * (W - mL - mR); }
    data.forEach(function(dd, i){
      var y = mT + i * (bh + gap);
      svg.appendChild(mk('text', { x: mL - 12, y: y + bh/2 + 4, 'text-anchor': 'end', 'font-size': 12, fill: ink(), 'font-family': 'Amaranth, sans-serif' }, dd.label));
      svg.appendChild(mk('rect', { x: mL, y: y, width: W - mL - mR, height: bh, rx: 7, fill: gridc(), opacity: 0.5 }));
      var bar = mk('rect', { x: mL, y: y, width: Xv(dd.y) - mL, height: bh, rx: 7, fill: dd.color });
      svg.appendChild(bar); fadeIn(bar, i * 0.1);
      svg.appendChild(mk('text', { x: Xv(dd.y) + 8, y: y + bh/2 + 4.5, 'font-size': 14, 'font-weight': 800, fill: dd.vcolor || ink(), 'font-family': 'Inter, sans-serif' }, o.valfmt(dd.y)));
    });
    if (o.refLine) {
      var rx = Xv(o.refLine.value);
      svg.appendChild(mk('line', { x1: rx, y1: mT - 13, x2: rx, y2: H - mB + 3, stroke: ink(), 'stroke-width': 1, 'stroke-dasharray': '5,4', opacity: 0.8 }));
      svg.appendChild(mk('text', { x: rx, y: mT - 17, 'text-anchor': 'middle', 'font-size': 9.5, 'font-weight': 700, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.refLine.label));
    }
  }

  /* ---------- The "honest axis" method panel ---------- */
  function ethicChart(id) {
    var svg = frame(id); if (!svg) return;
    var vals = [52, 55, 58];
    svg.appendChild(mk('text', { x: W/2, y: 20, 'text-anchor': 'middle', 'font-size': 12, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, 'Same three numbers — 52, 55, 58'));
    function panel(ox, pw, yScaleMin, title, color) {
      var top = 44, base = H - 40, n = vals.length, gap = 18, bw = (pw - gap * (n - 1)) / n, range = 60 - yScaleMin;
      function Y(v){ return top + (60 - v) / range * (base - top); }
      svg.appendChild(mk('line', { x1: ox - 6, y1: base, x2: ox + pw + 4, y2: base, stroke: ink(), 'stroke-width': 1.3 }));
      vals.forEach(function(v, i){
        var x = ox + i * (bw + gap);
        var fill = vGrad(svg, id + '-' + ox + '-' + i, color, 0.95, 0.6);
        var r = mk('rect', { x: x, y: Y(v), width: bw, height: base - Y(v), rx: 4, fill: fill });
        svg.appendChild(r); fadeIn(r, i * 0.08);
      });
      svg.appendChild(mk('text', { x: ox - 9, y: base + 3, 'text-anchor': 'end', 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, yScaleMin));
      svg.appendChild(mk('text', { x: ox + pw/2, y: H - 12, 'text-anchor': 'middle', 'font-size': 11, 'font-weight': 700, fill: color, 'font-family': 'Inter, sans-serif' }, title));
    }
    panel(58, 150, 50, 'axis cut at 50 → "a surge!"', COL.red);
    panel(268, 150, 0, 'axis at 0 → the truth', COL.teal);
  }

  /* ---------- India warming (verified IMD anomalies + schematic stripe) ---------- */
  function climateChart(id) {
    var svg = frame(id); if (!svg) return;
    var defs = mk('defs', {});
    var lg = mk('linearGradient', { id: 'warmgrad', x1: '0', y1: '0', x2: '1', y2: '0' });
    [['0','#08306b'],['0.45','#f2f2f2'],['0.7','#fdae61'],['1','#a50026']].forEach(function(s){ lg.appendChild(mk('stop', { offset: s[0], 'stop-color': s[1] })); });
    defs.appendChild(lg); svg.appendChild(defs);
    var bandY = 26, bandH = 44;
    svg.appendChild(mk('rect', { x: 20, y: bandY, width: W - 40, height: bandH, rx: 6, fill: 'url(#warmgrad)' }));
    svg.appendChild(mk('text', { x: 22, y: bandY - 7, 'font-size': 10, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, '1901'));
    svg.appendChild(mk('text', { x: W - 22, y: bandY - 7, 'text-anchor': 'end', 'font-size': 10, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, '2024'));
    svg.appendChild(mk('text', { x: W/2, y: bandY + bandH + 15, 'text-anchor': 'middle', 'font-size': 9.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, 'warming trend — schematic (cool → hot)'));
    svg.appendChild(mk('text', { x: W/2, y: 150, 'text-anchor': 'middle', 'font-size': 44, 'font-weight': 800, fill: COL.red, 'font-family': 'Inter, sans-serif' }, '+0.65°C'));
    svg.appendChild(mk('text', { x: W/2, y: 171, 'text-anchor': 'middle', 'font-size': 12, fill: ink(), 'font-family': 'Amaranth, sans-serif' }, '2024 vs 1991–2020 — warmest year since 1901'));
    var items = [['vs 1981–2010', '+0.78°C'], ['vs 1951–80', '+0.98°C']], cw = (W - 40) / 2;
    items.forEach(function(it, i){
      var cx = 20 + cw * i + cw / 2;
      svg.appendChild(mk('text', { x: cx, y: 212, 'text-anchor': 'middle', 'font-size': 19, 'font-weight': 800, fill: COL.amber, 'font-family': 'Inter, sans-serif' }, it[1]));
      svg.appendChild(mk('text', { x: cx, y: 230, 'text-anchor': 'middle', 'font-size': 10, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, it[0]));
    });
    svg.appendChild(mk('text', { x: W/2, y: 266, 'text-anchor': 'middle', 'font-size': 11, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, '10 of the 15 warmest years have come since 2010'));
  }

  /* ---------- Beeswarm (distribution, one dot per item) ---------- */
  function beeswarm(id, data, o) {
    var svg = frame(id); if (!svg) return;
    var vh = 162; svg.setAttribute('viewBox', '0 0 ' + W + ' ' + vh);
    var mL = 26, mR = 22, axisY = vh - 32, vMax = o.vMax, r = 4.5, step = r * 2.1;
    function X(v){ return mL + (v / vMax) * (W - mL - mR); }
    svg.appendChild(mk('line', { x1: mL, y1: axisY, x2: W - mR, y2: axisY, stroke: ink(), 'stroke-width': 1 }));
    (o.ticks || []).forEach(function(t){ if (X(t) <= W - mR) { svg.appendChild(mk('line', { x1: X(t), y1: axisY, x2: X(t), y2: axisY + 5, stroke: ink(), 'stroke-width': 1 })); tick(svg, X(t), axisY + 16, t); } });
    if (o.ref) {
      svg.appendChild(mk('line', { x1: X(o.ref.v), y1: 34, x2: X(o.ref.v), y2: axisY, stroke: ink(), 'stroke-width': 1, 'stroke-dasharray': '5,4', opacity: 0.5 }));
      svg.appendChild(mk('text', { x: X(o.ref.v) + 4, y: 31, 'font-size': 9.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.ref.label));
    }
    var placed = [];
    data.slice().sort(function(a, b){ return a.v - b.v; }).forEach(function(d){
      var cx = X(d.v), cy = axisY - r - 2, k = 0;
      while (placed.some(function(p){ return Math.abs(p.x - cx) < step && Math.abs(p.y - cy) < step; })) { k++; cy = axisY - r - 2 - k * step; }
      placed.push({ x: cx, y: cy, d: d });
    });
    placed.forEach(function(p){ var d = p.d; svg.appendChild(mk('circle', { cx: p.x, cy: p.y, r: d.hl ? 6.5 : r, fill: d.hl ? o.hlColor : o.dotColor, 'fill-opacity': d.hl ? 1 : 0.8, stroke: d.hl ? '#fff' : 'none', 'stroke-width': d.hl ? 1.6 : 0 })); });
    // isolated outliers labelled inline (e.g. Qatar); the highlighted dot gets a key, so its label never sits on the cluster
    placed.forEach(function(p){ if (p.d.label && !p.d.hl) svg.appendChild(mk('text', { x: p.x, y: p.y - 11, 'text-anchor': 'middle', 'font-size': 10.5, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, p.d.label)); });
    var hl = data.filter(function(d){ return d.hl; })[0];
    if (hl) {
      svg.appendChild(mk('circle', { cx: mL + 5, cy: 14, r: 6, fill: o.hlColor }));
      svg.appendChild(mk('text', { x: mL + 16, y: 18, 'font-size': 11, 'font-weight': 800, fill: o.hlColor, 'font-family': 'Inter, sans-serif' }, hl.label + ' — ' + hl.v + (o.hlUnit !== undefined ? o.hlUnit : ' t') ));
    }
    svg.appendChild(mk('text', { x: (mL + W - mR) / 2, y: vh - 6, 'text-anchor': 'middle', 'font-size': 9.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.axisLabel));
  }

  /* ---------- Funnel (a narrowing pipeline) ---------- */
  function funnel(id, data, o) {
    var svg = frame(id); if (!svg) return;
    var mT = 22, mB = 18, cx = W / 2 + 18, n = data.length, gap = 9, maxW = W - 200;
    var bh = (H - mT - mB - gap * (n - 1)) / n;
    function bw(v){ return (v / o.vMax) * maxW; }
    data.forEach(function(d, i){
      var y = mT + i * (bh + gap), w = bw(d.v);
      if (i < n - 1) {
        var w2 = bw(data[i+1].v), y2 = y + bh + gap;
        svg.appendChild(mk('path', { d: 'M' + (cx - w/2) + ',' + (y + bh) + ' L' + (cx + w/2) + ',' + (y + bh) + ' L' + (cx + w2/2) + ',' + y2 + ' L' + (cx - w2/2) + ',' + y2 + ' Z', fill: o.colors[i], opacity: 0.13 }));
      }
      var fill = vGrad(svg, id + '-f' + i, o.colors[i], 0.95, 0.68);
      var rect = mk('rect', { x: cx - w/2, y: y, width: w, height: bh, rx: 5, fill: fill });
      svg.appendChild(rect); fadeIn(rect, i * 0.1);
      svg.appendChild(mk('text', { x: 16, y: y + bh/2 + 4, 'font-size': 11, fill: ink(), 'font-family': 'Amaranth, sans-serif' }, d.label));
      svg.appendChild(mk('text', { x: cx + w/2 - 9, y: y + bh/2 + 4.5, 'text-anchor': 'end', 'font-size': 13, 'font-weight': 800, fill: '#fff', 'font-family': 'Inter, sans-serif' }, d.v + '%'));
    });
  }

  /* ---------- Radial donut (parts of a whole) ---------- */
  function donut(id, data, o) {
    var svg = frame(id); if (!svg) return;
    var cx = 138, cy = 150, rO = 92, rI = 54, total = data.reduce(function(s, d){ return s + d.v; }, 0);
    function arc(a0, a1) {
      var p0o = polar(cx, cy, rO, a0), p1o = polar(cx, cy, rO, a1), p1i = polar(cx, cy, rI, a1), p0i = polar(cx, cy, rI, a0);
      var lg = (a1 - a0) > 180 ? 1 : 0;
      return 'M' + p0o[0].toFixed(1) + ',' + p0o[1].toFixed(1) + ' A' + rO + ',' + rO + ' 0 ' + lg + ' 1 ' + p1o[0].toFixed(1) + ',' + p1o[1].toFixed(1) +
             ' L' + p1i[0].toFixed(1) + ',' + p1i[1].toFixed(1) + ' A' + rI + ',' + rI + ' 0 ' + lg + ' 0 ' + p0i[0].toFixed(1) + ',' + p0i[1].toFixed(1) + ' Z';
    }
    var ang = 0;
    data.forEach(function(d, i){
      var a1 = ang + d.v / total * 360;
      var p = mk('path', { d: arc(ang, a1), fill: d.color });
      svg.appendChild(p); fadeIn(p, i * 0.08);
      ang = a1;
    });
    // centre stat
    svg.appendChild(mk('text', { x: cx, y: cy - 4, 'text-anchor': 'middle', 'font-size': 28, 'font-weight': 800, fill: ink(), 'font-family': 'Inter, sans-serif' }, o.centerBig));
    svg.appendChild(mk('text', { x: cx, y: cy + 14, 'text-anchor': 'middle', 'font-size': 11, fill: ink(), 'font-family': 'Amaranth, sans-serif' }, o.centerSub));
    // legend
    var lx = 268, ly = 44, lh = (H - 70) / data.length;
    data.forEach(function(d, i){
      var y = ly + i * lh;
      svg.appendChild(mk('rect', { x: lx, y: y - 9, width: 12, height: 12, rx: 3, fill: d.color }));
      svg.appendChild(mk('text', { x: lx + 19, y: y + 1, 'font-size': 11.5, fill: ink(), 'font-family': 'Amaranth, sans-serif' }, d.label));
      svg.appendChild(mk('text', { x: W - 16, y: y + 1, 'text-anchor': 'end', 'font-size': 12, 'font-weight': 800, fill: d.color, 'font-family': 'Inter, sans-serif' }, d.v + '%'));
    });
  }

  /* ---------- Dumbbell (gap between two values) ---------- */
  function dumbbell(id, data, o) {
    var svg = frame(id); if (!svg) return;
    var mL = 134, mR = 26, mT = 44, mB = 30;
    var n = data.length, rowH = (H - mT - mB) / n;
    function X(v){ return mL + (v / 100) * (W - mL - mR); }
    [0, 25, 50, 75, 100].forEach(function(t){
      svg.appendChild(mk('line', { x1: X(t), y1: mT - 6, x2: X(t), y2: H - mB, stroke: gridc(), 'stroke-width': 1 }));
      tick(svg, X(t), H - mB + 15, t + '%');
    });
    // legend
    svg.appendChild(mk('circle', { cx: mL + 2, cy: 22, r: 5, fill: o.fColor }));
    svg.appendChild(mk('text', { x: mL + 12, y: 26, 'font-size': 11, 'font-weight': 700, fill: o.fColor, 'font-family': 'Inter, sans-serif' }, 'Women'));
    svg.appendChild(mk('circle', { cx: mL + 78, cy: 22, r: 5, fill: o.mColor }));
    svg.appendChild(mk('text', { x: mL + 88, y: 26, 'font-size': 11, 'font-weight': 700, fill: o.mColor, 'font-family': 'Inter, sans-serif' }, 'Men'));
    data.forEach(function(d, i){
      var y = mT + i * rowH + rowH / 2;
      svg.appendChild(mk('text', { x: mL - 12, y: y + 4, 'text-anchor': 'end', 'font-size': 11.5, fill: ink(), 'font-family': 'Amaranth, sans-serif' }, d.label));
      var xf = X(d.f), xm = X(d.m), lo = Math.min(xf, xm), hi = Math.max(xf, xm);
      var line = mk('line', { x1: lo, y1: y, x2: hi, y2: y, stroke: ink(), 'stroke-width': 2.4, 'stroke-linecap': 'round', opacity: 0.45 });
      svg.appendChild(line); fadeIn(line, i * 0.08);
      svg.appendChild(mk('circle', { cx: xm, cy: y, r: 5.5, fill: o.mColor }));
      svg.appendChild(mk('circle', { cx: xf, cy: y, r: 5.5, fill: o.fColor }));
      // value labels: put each just outside its dot
      svg.appendChild(mk('text', { x: xf + (xf <= xm ? -9 : 9), y: y + 4, 'text-anchor': xf <= xm ? 'end' : 'start', 'font-size': 11, 'font-weight': 800, fill: o.fColor, 'font-family': 'Inter, sans-serif' }, d.f));
      svg.appendChild(mk('text', { x: xm + (xm < xf ? -9 : 9), y: y + 4, 'text-anchor': xm < xf ? 'end' : 'start', 'font-size': 11, 'font-weight': 800, fill: o.mColor, 'font-family': 'Inter, sans-serif' }, d.m));
    });
  }


  /* ---------- UpSet plot (which sets overlap, and how much) ----------
     A Venn diagram stops being readable at four sets and cannot be drawn
     honestly at six. An UpSet plot replaces the overlapping circles with a
     matrix: every column is one exact combination, the dots below say which
     sets are in it, and the bar above says how many members it has. It is the
     right form here because the question is not "how common is each of these"
     but "how often do they land on the same district". */
  function upset(id, v, o) {
    var svg = frame(id); if (!svg) return;
    var acc = css('--chart-acc' + (o && o.acc === 2 ? 2 : 1), '#be123c');
    var sets = v.sets, cols = v.shown, ns = sets.length, nc = cols.length;

    var mL = 6, setW = 44, labX = mL + setW + 8, matL = 210, matR = 452;
    var barTop = 30, barH = 96, base = barTop + barH;
    var matT = base + 22, rowH = 21, colW = (matR - matL) / nc;
    var vh = matT + ns * rowH + 44;
    svg.setAttribute('viewBox', '0 0 ' + W + ' ' + vh);

    // The <title> is the accessible name. frame() cleared the element, so it
    // has to be put back here or the chart has no name at all.
    svg.appendChild(mk('title', {}, o && o.alt ? o.alt : 'UpSet plot of overlapping groups'));

    var maxN = Math.max.apply(null, cols.map(function(c){ return c.n; }));
    var maxS = Math.max.apply(null, sets.map(function(s){ return s.n; }));
    var idx = {}; sets.forEach(function(s, i){ idx[s.key] = i; });

    /* ----- left: how big each set is on its own ----- */
    // The label lane is fixed and the labels are prose, so a long one used to
    // run straight through its own count ("No clean cooking fu351"). The lane is
    // now wide enough for the longest of them at full size, which is what
    // actually fixes it: measuring alone did not, because the chart draws before
    // Inter has loaded and the fallback face measures narrower, so every label
    // passed the check and then reflowed wider once the real font arrived. The
    // step-down below stays as a backstop for longer labels in future data;
    // getComputedTextLength returns 0 when the node is not laid out (a hidden
    // tab, print), and a character-count estimate would have to assume a font
    // that may not be the one in use, so in that case leave the size alone.
    var lane = (matL - 26) - labX;
    sets.forEach(function(s, i) {
      var y = matT + i * rowH, w = Math.max(2, (s.n / maxS) * setW);
      svg.appendChild(mk('rect', { x: mL + setW - w, y: y + rowH / 2 - 5, width: w, height: 10,
        rx: 3, fill: acc, opacity: 0.30 }));
      var t = mk('text', { x: labX, y: y + rowH / 2 + 4, 'font-size': 10,
        fill: ink(), 'font-family': 'Inter, sans-serif' }, s.label);
      svg.appendChild(t);
      for (var fs = 10; fs > 7.5; fs -= 0.5) {
        var wpx = t.getComputedTextLength ? t.getComputedTextLength() : 0;
        if (!wpx || wpx <= lane) break;
        t.setAttribute('font-size', fs - 0.5);
      }
      svg.appendChild(mk('text', { x: matL - 8, y: y + rowH / 2 + 4, 'text-anchor': 'end',
        'font-size': 9.5, fill: ink(), opacity: 0.75,
        'font-family': 'JetBrains Mono, monospace' }, String(s.n)));
    });

    /* ----- top: how big each exact combination is ----- */
    cols.forEach(function(c, j) {
      var cx = matL + j * colW + colW / 2;
      var h = Math.max(2, (c.n / maxN) * barH), bw = Math.min(15, colW - 7);
      var g = mk('g', {});
      var names = c.sets.map(function(k){ return sets[idx[k]].label; });
      g.appendChild(mk('title', {}, c.n + ' ' + (o && o.unit || 'districts') + ' — ' +
        (names.length ? names.join(' + ') : 'none of these')));
      g.appendChild(mk('rect', { x: cx - bw / 2, y: base - h, width: bw, height: h,
        rx: 4, fill: acc }));
      g.appendChild(mk('text', { x: cx, y: base - h - 5, 'text-anchor': 'middle',
        'font-size': 9.5, 'font-weight': 700, fill: ink(),
        'font-family': 'JetBrains Mono, monospace' }, String(c.n)));
      // a generous, invisible hit area so the hover target is bigger than the mark
      g.appendChild(mk('rect', { x: matL + j * colW, y: barTop, width: colW,
        height: (matT + ns * rowH) - barTop, fill: 'transparent' }));
      svg.appendChild(g); fadeIn(g, j * 0.04);
    });

    svg.appendChild(mk('line', { x1: matL - 4, y1: base, x2: matR, y2: base,
      stroke: gridc(), 'stroke-width': 1 }));

    /* ----- the matrix: filled = in this combination ----- */
    cols.forEach(function(c, j) {
      var cx = matL + j * colW + colW / 2, on = {};
      c.sets.forEach(function(k){ on[idx[k]] = 1; });
      var rows = c.sets.map(function(k){ return idx[k]; }).sort(function(a, b){ return a - b; });
      if (rows.length > 1) {
        svg.appendChild(mk('line', { x1: cx, y1: matT + rows[0] * rowH + rowH / 2,
          x2: cx, y2: matT + rows[rows.length - 1] * rowH + rowH / 2,
          stroke: acc, 'stroke-width': 2 }));
      }
      sets.forEach(function(s, i) {
        svg.appendChild(mk('circle', { cx: cx, cy: matT + i * rowH + rowH / 2, r: 4.5,
          fill: on[i] ? acc : gridc() }));
      });
      // A column with no filled dot is the group that has none of them -- a real
      // and interesting category, but an unlabelled empty column reads as a
      // drawing fault, so it gets named.
      if (!rows.length) {
        svg.appendChild(mk('text', { x: cx, y: matT + ns * rowH + 11, 'text-anchor': 'middle',
          'font-size': 8.5, fill: ink(), opacity: 0.85,
          'font-family': 'Inter, sans-serif' }, 'none'));
      }
    });

    /* ----- what is not drawn ----- */
    if (v.hiddenCombos > 0) {
      svg.appendChild(mk('text', { x: mL, y: vh - 7, 'font-size': 9, fill: ink(),
        opacity: 0.8, 'font-family': 'Inter, sans-serif' },
        'The ' + nc + ' largest of ' + (nc + v.hiddenCombos) + ' combinations. The other ' +
        v.hiddenCombos + ' hold ' + v.hiddenDistricts + ' ' + (o && o.unit || 'districts') + '.'));
    }
    svg.appendChild(mk('text', { x: mL, y: 15, 'font-size': 9.5, fill: ink(), opacity: 0.8,
      'font-family': 'Inter, sans-serif' }, o && o.caption || ''));
  }

  /* ---------- Heatmap (matrix) ---------- */
  function heatmap(id, m, o) {
    var svg = frame(id); if (!svg) return;
    var mL = 150, mT = 40, mR = 16, mB = 16, nc = m.cols.length, nr = m.rows.length;
    var cw = (W - mL - mR) / nc, ch = (H - mT - mB) / nr, gap = 3;
    function shade(v){ if (v == null) return gridc(); var t = Math.max(0, Math.min(1, (v - o.min) / (o.max - o.min)));
      // light -> deep green
      var r = Math.round(237 + (22 - 237) * t), g = Math.round(247 + (138 - 247) * t), b = Math.round(233 + (90 - 233) * t);
      return 'rgb(' + r + ',' + g + ',' + b + ')'; }
    m.cols.forEach(function(c, j){ svg.appendChild(mk('text', { x: mL + j * cw + cw / 2, y: mT - 12, 'text-anchor': 'middle', 'font-size': 10.5, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, c)); });
    m.rows.forEach(function(rw, i){
      svg.appendChild(mk('text', { x: mL - 10, y: mT + i * ch + ch / 2 + 4, 'text-anchor': 'end', 'font-size': 11, fill: ink(), 'font-family': 'Amaranth, sans-serif' }, rw));
      m.cols.forEach(function(c, j){
        var v = m.values[i][j], x = mL + j * cw + gap / 2, y = mT + i * ch + gap / 2;
        var cell = mk('rect', { x: x, y: y, width: cw - gap, height: ch - gap, rx: 5, fill: shade(v) });
        svg.appendChild(cell); fadeIn(cell, (i + j) * 0.05);
        var t = v == null ? 0 : Math.max(0, Math.min(1, (v - o.min) / (o.max - o.min)));
        svg.appendChild(mk('text', { x: x + (cw - gap) / 2, y: y + (ch - gap) / 2 + 4, 'text-anchor': 'middle', 'font-size': 12, 'font-weight': 800, fill: v == null ? ink() : (t > 0.55 ? '#fff' : '#14532d'), 'font-family': 'Inter, sans-serif' }, v == null ? '–' : v + '%'));
      });
    });
  }

  /* ---------- Forest plot (estimate + uncertainty range) ---------- */
  function forest(id, data, o) {
    var svg = frame(id); if (!svg) return;
    var mL = 128, mR = 40, mT = 32, mB = 34, n = data.length, rowH = (H - mT - mB) / n;
    function X(v){ return mL + (v / o.vMax) * (W - mL - mR); }
    (o.ticks || []).forEach(function(t){
      svg.appendChild(mk('line', { x1: X(t), y1: mT - 6, x2: X(t), y2: H - mB, stroke: gridc(), 'stroke-width': 1 }));
      tick(svg, X(t), H - mB + 15, t + '°');
    });
    (o.refs || []).forEach(function(rf){
      svg.appendChild(mk('line', { x1: X(rf.v), y1: mT - 7, x2: X(rf.v), y2: H - mB + 2, stroke: rf.color, 'stroke-width': 1.2, 'stroke-dasharray': '4,3' }));
      svg.appendChild(mk('text', { x: X(rf.v) + (rf.side === 'end' ? -3 : 3), y: mT - 10, 'text-anchor': rf.side || 'middle', 'font-size': 9.5, 'font-weight': 700, fill: rf.color, 'font-family': 'JetBrains Mono, monospace' }, rf.label));
    });
    data.forEach(function(d, i){
      var y = mT + i * rowH + rowH / 2;
      svg.appendChild(mk('text', { x: mL - 12, y: y + 4, 'text-anchor': 'end', 'font-size': 11, fill: ink(), 'font-family': 'Amaranth, sans-serif' }, d.label));
      var wk = mk('line', { x1: X(d.lo), y1: y, x2: X(d.hi), y2: y, stroke: d.color, 'stroke-width': 2.4, 'stroke-linecap': 'round' });
      svg.appendChild(wk); fadeIn(wk, i * 0.08);
      [d.lo, d.hi].forEach(function(v){ svg.appendChild(mk('line', { x1: X(v), y1: y - 4, x2: X(v), y2: y + 4, stroke: d.color, 'stroke-width': 2 })); });
      svg.appendChild(mk('circle', { cx: X(d.est), cy: y, r: 5, fill: d.color, stroke: '#fff', 'stroke-width': 1.4 }));
      svg.appendChild(mk('text', { x: X(d.hi) + 8, y: y + 4, 'font-size': 11.5, 'font-weight': 800, fill: d.color, 'font-family': 'Inter, sans-serif' }, d.est + '°'));
    });
  }

  /* ---------- Small multiples (a grid of mini line charts) ---------- */
  function smallMultiples(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 250; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var s = o.series, cols = o.cols || 4, rows = Math.ceil(s.length / cols);
    var gx = 8, gyTop = 8, padR = 8, padB = 18;
    var pw = (vw - gx - padR) / cols, ph = (vh - gyTop - padB) / rows, yMax = o.yMax;
    s.forEach(function(ser, i){
      var c = i % cols, r = Math.floor(i / cols), ox = gx + c * pw, oy = gyTop + r * ph;
      var plotX = ox + 6, plotY = oy + 20, plotW = pw - 16, plotH = ph - 34;
      var xs = ser.pts.map(function(p){ return p[0]; }), xmin = Math.min.apply(null, xs), xmax = Math.max.apply(null, xs);
      function X(x){ return plotX + (x - xmin) / (xmax - xmin) * plotW; }
      function Y(v){ return plotY + plotH - (v / yMax) * plotH; }
      var col = ser.hl ? o.hlColor : (o.color || '#4f46e5');
      svg.appendChild(mk('line', { x1: plotX, y1: plotY + plotH, x2: plotX + plotW, y2: plotY + plotH, stroke: gridc(), 'stroke-width': 1 }));
      var fill = vGrad(svg, id + '-g' + i, col, 0.22, 0.02);
      var d = ser.pts.map(function(p, j){ return (j ? 'L' : 'M') + X(p[0]).toFixed(1) + ',' + Y(p[1]).toFixed(1); }).join(' ');
      svg.appendChild(mk('path', { d: d + ' L' + X(xmax).toFixed(1) + ',' + (plotY + plotH) + ' L' + X(xmin).toFixed(1) + ',' + (plotY + plotH) + ' Z', fill: fill }));
      svg.appendChild(mk('path', { d: d, fill: 'none', stroke: col, 'stroke-width': 2, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }));
      var last = ser.pts[ser.pts.length - 1], first = ser.pts[0];
      svg.appendChild(mk('circle', { cx: X(last[0]), cy: Y(last[1]), r: 2.6, fill: col }));
      svg.appendChild(mk('text', { x: ox + 6, y: oy + 12, 'font-size': 10.5, 'font-weight': ser.hl ? 800 : 700, fill: ser.hl ? o.hlColor : ink(), 'font-family': 'Inter, sans-serif' }, ser.name));
      svg.appendChild(mk('text', { x: X(first[0]), y: Y(first[1]) - 4, 'font-size': 8.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, Math.round(first[1])));
      svg.appendChild(mk('text', { x: X(last[0]), y: Y(last[1]) - 5, 'text-anchor': 'end', 'font-size': 9, 'font-weight': 700, fill: col, 'font-family': 'JetBrains Mono, monospace' }, Math.round(last[1])));
    });
    svg.appendChild(mk('text', { x: vw - padR, y: vh - 5, 'text-anchor': 'end', 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.axisLabel || '1990 → 2022' ));
  }

  /* ---------- Connected scatterplot (a path through two variables over time) ---------- */
  function connectedScatter(id, o) {
    var svg = frame(id); if (!svg) return; var vh = 300; svg.setAttribute('viewBox', '0 0 ' + W + ' ' + vh);
    var mL = 38, mR = 16, mT = 18, mB = 46;
    function X(f){ return mL + (f / o.xMax) * (W - mL - mR); }
    function Y(l){ return (vh - mB) - (l - o.yMin) / (o.yMax - o.yMin) * (vh - mB - mT); }
    (o.xTicks || []).forEach(function(t){ svg.appendChild(mk('line', { x1: X(t), y1: mT, x2: X(t), y2: vh - mB, stroke: gridc(), 'stroke-width': 1 })); tick(svg, X(t), vh - mB + 15, t); });
    (o.yTicks || []).forEach(function(t){ svg.appendChild(mk('line', { x1: mL, y1: Y(t), x2: W - mR, y2: Y(t), stroke: gridc(), 'stroke-width': 1 })); svg.appendChild(mk('text', { x: mL - 6, y: Y(t) + 3, 'text-anchor': 'end', 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, t)); });
    svg.appendChild(mk('text', { x: (mL + W - mR) / 2, y: vh - 6, 'text-anchor': 'middle', 'font-size': 9.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.xLabel));
    svg.appendChild(mk('text', { x: 12, y: mT + 4, 'font-size': 9.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace', transform: 'rotate(-90 12 ' + (mT + 4) + ')' }, o.yLabel));
    o.series.forEach(function(ser){
      var d = ser.pts.map(function(p, j){ return (j ? 'L' : 'M') + X(p[0]).toFixed(1) + ',' + Y(p[1]).toFixed(1); }).join(' ');
      var path = mk('path', { d: d, fill: 'none', stroke: ser.color, 'stroke-width': 2.4, 'stroke-linejoin': 'round', 'stroke-linecap': 'round', opacity: 0.9 });
      svg.appendChild(path); animPath(path);
      ser.pts.forEach(function(p, j){ var isEnd = j === ser.pts.length - 1; svg.appendChild(mk('circle', { cx: X(p[0]), cy: Y(p[1]), r: isEnd ? 4 : 2.2, fill: isEnd ? ser.color : '#fff', stroke: ser.color, 'stroke-width': 1.4 })); });
      var last = ser.pts[ser.pts.length - 1];
      svg.appendChild(mk('text', { x: X(last[0]) + 6, y: Y(last[1]) + 3, 'font-size': 10.5, 'font-weight': 800, fill: ser.color, 'font-family': 'Inter, sans-serif' }, ser.name));
    });
  }

  /* ---------- Chord diagram (flows between categories) ---------- */
  function chord(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 320; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var cx = vw / 2, cy = vh / 2 + 4, R = 110, rib = R - 14;
    var names = o.names, cols = o.colors, M = o.matrix, n = names.length;
    function P(ang, r){ return [cx + r * Math.cos(ang), cy + r * Math.sin(ang)]; }
    function pair(i, j){ return M[i][j] + M[j][i]; }
    var tot = names.map(function(_, i){ var s = 0; for (var j = 0; j < n; j++) if (j !== i) s += pair(i, j); return s; });
    var grand = tot.reduce(function(a, b){ return a + b; }, 0);
    var gap = 0.045, avail = 2 * Math.PI - n * gap, ang = -Math.PI / 2, arcs = [];
    for (var i = 0; i < n; i++) { var a0 = ang, a1 = a0 + avail * tot[i] / grand; arcs.push([a0, a1]); ang = a1 + gap; }
    var seg = {};
    for (i = 0; i < n; i++) { var p = arcs[i][0]; for (var j = 0; j < n; j++) { if (j === i) continue; var w = (arcs[i][1] - arcs[i][0]) * (tot[i] ? pair(i, j) / tot[i] : 0); seg[i + '-' + j] = [p, p + w]; p += w; } }
    // ribbons (one per unordered pair)
    for (i = 0; i < n; i++) for (j = i + 1; j < n; j++) {
      if (pair(i, j) <= 0) continue;
      var si = seg[i + '-' + j], sj = seg[j + '-' + i];
      var a = P(si[0], rib), b = P(si[1], rib), c = P(sj[0], rib), e = P(sj[1], rib);
      var d = 'M' + a[0].toFixed(1) + ',' + a[1].toFixed(1) +
        ' A' + rib + ',' + rib + ' 0 0 1 ' + b[0].toFixed(1) + ',' + b[1].toFixed(1) +
        ' Q' + cx + ',' + cy + ' ' + c[0].toFixed(1) + ',' + c[1].toFixed(1) +
        ' A' + rib + ',' + rib + ' 0 0 1 ' + e[0].toFixed(1) + ',' + e[1].toFixed(1) +
        ' Q' + cx + ',' + cy + ' ' + a[0].toFixed(1) + ',' + a[1].toFixed(1) + ' Z';
      var rp = mk('path', { d: d, fill: cols[tot[i] >= tot[j] ? i : j], 'fill-opacity': 0.42, stroke: 'none' });
      svg.appendChild(rp); fadeIn(rp, (i + j) * 0.05);
    }
    // arcs + labels
    for (i = 0; i < n; i++) {
      var a0 = arcs[i][0], a1 = arcs[i][1], o1 = P(a0, R), o2 = P(a1, R), i2 = P(a1, rib), i1 = P(a0, rib);
      svg.appendChild(mk('path', { d: 'M' + o1[0].toFixed(1) + ',' + o1[1].toFixed(1) + ' A' + R + ',' + R + ' 0 0 1 ' + o2[0].toFixed(1) + ',' + o2[1].toFixed(1) + ' L' + i2[0].toFixed(1) + ',' + i2[1].toFixed(1) + ' A' + rib + ',' + rib + ' 0 0 0 ' + i1[0].toFixed(1) + ',' + i1[1].toFixed(1) + ' Z', fill: cols[i] }));
      var mid = (a0 + a1) / 2, lp = P(mid, R + 12), anchor = Math.cos(mid) < -0.1 ? 'end' : (Math.cos(mid) > 0.1 ? 'start' : 'middle');
      svg.appendChild(mk('text', { x: lp[0].toFixed(1), y: lp[1].toFixed(1) + 3, 'text-anchor': anchor, 'font-size': 10.5, 'font-weight': 700, fill: cols[i], 'font-family': 'Inter, sans-serif' }, names[i]));
    }
  }

  /* ---------- Sankey (flows source -> target) ---------- */
  function sankey(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 300; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var L = o.left, Rg = o.right, F = o.flows; // F[i][j] left i -> right j
    var mT = 16, mB = 16, colW = 14, lx = 96, rx = vw - 96 - colW, H2 = vh - mT - mB;
    var ltot = L.map(function(_, i){ return Rg.reduce(function(s, _2, j){ return s + F[i][j]; }, 0); });
    var rtot = Rg.map(function(_, j){ return L.reduce(function(s, _2, i){ return s + F[i][j]; }, 0); });
    var grand = ltot.reduce(function(a, b){ return a + b; }, 0);
    var gap = 8;
    function heights(tot){ var avail = H2 - gap * (tot.length - 1); return tot.map(function(t){ return avail * t / grand; }); }
    var lh = heights(ltot), rh = heights(rtot);
    var ly = [], ry = [], y = mT; L.forEach(function(_, i){ ly.push(y); y += lh[i] + gap; }); y = mT; Rg.forEach(function(_, j){ ry.push(y); y += rh[j] + gap; });
    var loff = ly.slice(), roff = ry.slice();
    // ribbons
    for (var i = 0; i < L.length; i++) for (var j = 0; j < Rg.length; j++) {
      var f = F[i][j]; if (f <= 0) continue;
      var t = (H2 - gap * (L.length - 1)) * f / grand;
      var y0a = loff[i], y0b = y0a + t, y1a = roff[j], y1b = y1a + t;
      loff[i] = y0b; roff[j] = y1b;
      var x0 = lx + colW, x1 = rx, xm = (x0 + x1) / 2;
      var d = 'M' + x0 + ',' + y0a.toFixed(1) + ' C' + xm + ',' + y0a.toFixed(1) + ' ' + xm + ',' + y1a.toFixed(1) + ' ' + x1 + ',' + y1a.toFixed(1) +
        ' L' + x1 + ',' + y1b.toFixed(1) + ' C' + xm + ',' + y1b.toFixed(1) + ' ' + xm + ',' + y0b.toFixed(1) + ' ' + x0 + ',' + y0b.toFixed(1) + ' Z';
      var rp = mk('path', { d: d, fill: o.lcolors[i], 'fill-opacity': 0.5 }); svg.appendChild(rp); fadeIn(rp, (i + j) * 0.04);
    }
    // nodes + labels
    L.forEach(function(nm, i){ svg.appendChild(mk('rect', { x: lx, y: ly[i], width: colW, height: Math.max(2, lh[i]), rx: 2, fill: o.lcolors[i] }));
      svg.appendChild(mk('text', { x: lx - 8, y: ly[i] + lh[i] / 2 + 4, 'text-anchor': 'end', 'font-size': 10.5, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, nm)); });
    Rg.forEach(function(nm, j){ svg.appendChild(mk('rect', { x: rx, y: ry[j], width: colW, height: Math.max(2, rh[j]), rx: 2, fill: (o.rcolors && o.rcolors[j]) || o.rcolor || '#64748b' }));
      svg.appendChild(mk('text', { x: rx + colW + 8, y: ry[j] + rh[j] / 2 + 4, 'font-size': 10.5, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, nm)); });
  }

  /* ---------- 3-stage Sankey (sector -> sub-sector -> gas) ---------- */
  function sankey3(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 360; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var SE = o.sectors, GA = o.gases, subs = o.subs; // subs: [{name, si, g:[...]}]
    var nSe = SE.names.length, nG = GA.names.length, nSub = subs.length;
    function sTot(s){ return s.g.reduce(function(a, b){ return a + b; }, 0); }
    var grand = subs.reduce(function(a, s){ return a + sTot(s); }, 0);
    var mT = 14, mB = 14, colW = 12, gap = 6, Hh = vh - mT - mB;
    var maxN = Math.max(nSe, nG, nSub), ppu = (Hh - gap * (maxN - 1)) / grand;
    var x0 = 92, x1 = vw / 2 - colW / 2, x2 = vw - 92 - colW;
    function colY(heights){ var ch = heights.reduce(function(a, b){ return a + b; }, 0) + gap * (heights.length - 1); var sy = mT + (Hh - ch) / 2, ys = []; heights.forEach(function(h){ ys.push(sy); sy += h + gap; }); return ys; }
    // sector totals
    var seTot = SE.names.map(function(_, i){ return subs.filter(function(s){ return s.si === i; }).reduce(function(a, s){ return a + sTot(s); }, 0); });
    var gaTot = GA.names.map(function(_, j){ return subs.reduce(function(a, s){ return a + s.g[j]; }, 0); });
    var seY = colY(seTot.map(function(v){ return v * ppu; }));
    var subH = subs.map(function(s){ return sTot(s) * ppu; }), subY = colY(subH);
    var gaY = colY(gaTot.map(function(v){ return v * ppu; }));
    function ribbon(xa, ya0, ya1, xb, yb0, yb1, col){ var xm = (xa + xb) / 2;
      var d = 'M' + xa + ',' + ya0.toFixed(1) + ' C' + xm + ',' + ya0.toFixed(1) + ' ' + xm + ',' + yb0.toFixed(1) + ' ' + xb + ',' + yb0.toFixed(1) +
        ' L' + xb + ',' + yb1.toFixed(1) + ' C' + xm + ',' + yb1.toFixed(1) + ' ' + xm + ',' + ya1.toFixed(1) + ' ' + xa + ',' + ya1.toFixed(1) + ' Z';
      var p = mk('path', { d: d, fill: col, 'fill-opacity': 0.5 }); svg.appendChild(p); return p; }
    // stage 0 -> 1
    var seOff = seY.slice();
    subs.forEach(function(s, k){ var col = SE.colors[s.si], h = subH[k];
      ribbon(x0 + colW, seOff[s.si], seOff[s.si] + h, x1, subY[k], subY[k] + h, col); seOff[s.si] += h; });
    // stage 1 -> 2
    var subOff = subY.slice(), gaOff = gaY.slice();
    subs.forEach(function(s, k){ var col = SE.colors[s.si];
      for (var j = 0; j < nG; j++) { var v = s.g[j]; if (v <= 0) continue; var t = v * ppu;
        ribbon(x1 + colW, subOff[k], subOff[k] + t, x2, gaOff[j], gaOff[j] + t, col); subOff[k] += t; gaOff[j] += t; } });
    // nodes + labels
    SE.names.forEach(function(nm, i){ svg.appendChild(mk('rect', { x: x0, y: seY[i], width: colW, height: Math.max(2, seTot[i] * ppu), rx: 2, fill: SE.colors[i] }));
      svg.appendChild(mk('text', { x: x0 - 6, y: seY[i] + seTot[i] * ppu / 2 + 3, 'text-anchor': 'end', 'font-size': 10, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, nm)); });
    subs.forEach(function(s, k){ svg.appendChild(mk('rect', { x: x1, y: subY[k], width: colW, height: Math.max(2, subH[k]), rx: 2, fill: SE.colors[s.si] }));
      svg.appendChild(mk('text', { x: x1 + colW + 4, y: subY[k] + subH[k] / 2 + 3, 'font-size': 8, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, s.name)); });
    GA.names.forEach(function(nm, j){ svg.appendChild(mk('rect', { x: x2, y: gaY[j], width: colW, height: Math.max(2, gaTot[j] * ppu), rx: 2, fill: GA.colors[j] }));
      svg.appendChild(mk('text', { x: x2 + colW + 5, y: gaY[j] + gaTot[j] * ppu / 2 + 3, 'font-size': 10, 'font-weight': 700, fill: GA.colors[j], 'font-family': 'Inter, sans-serif' }, nm)); });
  }

  /* ---------- Waffle (small multiples of 10x10 grids) ---------- */
  function waffle(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 268; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var items = o.items, cols = o.cols || 3, rows = Math.ceil(items.length / cols);
    var cw = vw / cols, ch = vh / rows, sq = 6.2, g = 1.7, grid = 10;
    items.forEach(function(it, i){
      var c = i % cols, r = Math.floor(i / cols), ox = c * cw + 16, oy = r * ch + 10;
      var gx0 = ox, gy0 = oy + 20, filled = Math.round(it.pct);
      svg.appendChild(mk('text', { x: gx0, y: oy + 12, 'font-size': 11, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, it.label));
      for (var k = 0; k < 100; k++) {
        var rr = Math.floor(k / grid), cc = k % grid, fromBottom = (grid - 1 - rr) * grid + cc, on = fromBottom < filled;
        svg.appendChild(mk('rect', { x: gx0 + cc * (sq + g), y: gy0 + rr * (sq + g), width: sq, height: sq, rx: 1.2, fill: on ? it.color : gridc() }));
      }
      var gw = grid * (sq + g);
      svg.appendChild(mk('text', { x: gx0 + gw + 6, y: gy0 + gw / 2 + 2, 'font-size': 20, 'font-weight': 800, fill: it.color, 'font-family': 'Inter, sans-serif' }, it.pct));
      svg.appendChild(mk('text', { x: gx0 + gw + 6, y: gy0 + gw / 2 + 16, 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, 'in 100'));
    });
  }

  /* ---------- Stream graph (centred stacked area over time) ---------- */
  function streamGraph(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 300; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var mL = 10, mR = 96, mT = 14, mB = 26, years = o.years, S = o.series, n = years.length;
    var totals = years.map(function(_, t){ return S.reduce(function(s, ser){ return s + ser.vals[t]; }, 0); });
    var maxTot = Math.max.apply(null, totals), Hh = vh - mT - mB, cyc = mT + Hh / 2;
    function X(t){ return mL + t / (n - 1) * (vw - mL - mR); }
    function sY(v){ return v / maxTot * Hh; }
    var tops = [];
    for (var t = 0; t < n; t++) { var off = cyc - sY(totals[t]) / 2; tops.push([]); for (var i = 0; i < S.length; i++) { tops[t][i] = off; off += sY(S[i].vals[t]); } }
    S.forEach(function(ser, i){
      var top = [], bot = [];
      for (var t = 0; t < n; t++) { top.push([X(t), tops[t][i]]); bot.push([X(t), tops[t][i] + sY(ser.vals[t])]); }
      var d = 'M' + top.map(function(p){ return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' L') + ' L' + bot.reverse().map(function(p){ return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' L') + ' Z';
      var rp = mk('path', { d: d, fill: ser.color, 'fill-opacity': 0.88 }); svg.appendChild(rp); fadeIn(rp, i * 0.06);
      var ly = tops[n-1][i] + sY(ser.vals[n-1]) / 2;
      svg.appendChild(mk('text', { x: vw - mR + 6, y: ly + 3, 'font-size': 9.5, 'font-weight': 700, fill: ser.color, 'font-family': 'Inter, sans-serif' }, ser.name));
    });
    years.forEach(function(y, t){ if (t === 0 || t === n - 1 || y === 1990) tick(svg, X(t), vh - 8, y); });
  }

  /* ---------- Population pyramid (two years, later filled + earlier outline) ---------- */
  function pyramid(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 300; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var ages = o.ages, A = o.a, B = o.b, n = ages.length, cx = vw / 2, mT = 36, mB = 22, gapc = 30, gap = 2;
    var totA = 0, totB = 0; for (var i = 0; i < n; i++) { totA += A.m[i] + A.f[i]; totB += B.m[i] + B.f[i]; }
    var bh = (vh - mT - mB) / n, half = cx - gapc - 24, maxPct = 0;
    for (i = 0; i < n; i++) maxPct = Math.max(maxPct, A.m[i] / totA * 100, A.f[i] / totA * 100, B.m[i] / totB * 100, B.f[i] / totB * 100);
    function Wd(p){ return p / maxPct * half; }
    function Yt(i){ return (vh - mB) - (i + 1) * bh; }
    for (i = 0; i < n; i++) {
      var y = Yt(i) + gap / 2, h = bh - gap;
      var wm = Wd(B.m[i] / totB * 100), wf = Wd(B.f[i] / totB * 100);
      var rm = mk('rect', { x: cx - gapc - wm, y: y, width: wm, height: h, fill: B.mcolor, 'fill-opacity': 0.85 }); svg.appendChild(rm); fadeIn(rm, i * 0.02);
      var rf = mk('rect', { x: cx + gapc, y: y, width: wf, height: h, fill: B.fcolor, 'fill-opacity': 0.85 }); svg.appendChild(rf); fadeIn(rf, i * 0.02);
      if (i % 2 === 0 || i === n - 1) svg.appendChild(mk('text', { x: cx, y: y + h / 2 + 3, 'text-anchor': 'middle', 'font-size': 7.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, ages[i]));
    }
    function outline(arr, tot, side){ var pts = []; for (var k = 0; k < n; k++) { var y0 = Yt(k) + gap / 2, y1 = y0 + bh - gap, x = cx + side * gapc + side * Wd(arr[k] / tot * 100); pts.push([x, y0]); pts.push([x, y1]); } return 'M' + pts.map(function(p){ return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' L'); }
    svg.appendChild(mk('path', { d: outline(A.m, totA, -1), fill: 'none', stroke: A.color, 'stroke-width': 1.6, 'stroke-dasharray': '3,2' }));
    svg.appendChild(mk('path', { d: outline(A.f, totA, 1), fill: 'none', stroke: A.color, 'stroke-width': 1.6, 'stroke-dasharray': '3,2' }));
    svg.appendChild(mk('text', { x: cx - gapc - half / 2, y: 18, 'text-anchor': 'middle', 'font-size': 11, 'font-weight': 700, fill: B.mcolor, 'font-family': 'Inter, sans-serif' }, 'Men'));
    svg.appendChild(mk('text', { x: cx + gapc + half / 2, y: 18, 'text-anchor': 'middle', 'font-size': 11, 'font-weight': 700, fill: B.fcolor, 'font-family': 'Inter, sans-serif' }, 'Women'));
    // legend
    svg.appendChild(mk('rect', { x: 14, y: vh - 13, width: 12, height: 8, rx: 1, fill: B.mcolor, 'fill-opacity': 0.85 }));
    svg.appendChild(mk('text', { x: 30, y: vh - 6, 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, B.name));
    svg.appendChild(mk('line', { x1: 100, y1: vh - 9, x2: 116, y2: vh - 9, stroke: A.color, 'stroke-width': 1.6, 'stroke-dasharray': '3,2' }));
    svg.appendChild(mk('text', { x: 120, y: vh - 6, 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, A.name + ' (outline)'));
  }

  /* ---------- Hex cartogram (tile map) ---------- */
  function hexCartogram(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 340; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var cells = o.cells, s = 22;
    function raw(c){ return [c.col * 1.5 * s, c.row * Math.sqrt(3) * s + (c.col % 2) * Math.sqrt(3) * s / 2]; }
    var xs = cells.map(function(c){ return raw(c)[0]; }), ys = cells.map(function(c){ return raw(c)[1]; });
    var minX = Math.min.apply(null, xs), maxX = Math.max.apply(null, xs), minY = Math.min.apply(null, ys), maxY = Math.max.apply(null, ys);
    var ox = (vw - (maxX - minX)) / 2 - minX, oy = (vh - 30 - (maxY - minY)) / 2 - minY + 8;
    function shade(v){ var t = Math.max(0, Math.min(1, (v - o.min) / (o.max - o.min))); var r = Math.round(237 + (22 - 237) * t), g = Math.round(247 + (163 - 247) * t), b = Math.round(233 + (90 - 233) * t); return 'rgb(' + r + ',' + g + ',' + b + ')'; }
    cells.forEach(function(c, i){
      var p = raw(c), cx = p[0] + ox, cy = p[1] + oy, pts = [];
      for (var k = 0; k < 6; k++) { var a = Math.PI / 180 * (60 * k); pts.push((cx + s * 0.92 * Math.cos(a)).toFixed(1) + ',' + (cy + s * 0.92 * Math.sin(a)).toFixed(1)); }
      var t = (c.v - o.min) / (o.max - o.min);
      var hx = mk('polygon', { points: pts.join(' '), fill: shade(c.v), stroke: '#fff', 'stroke-width': 1.4 });
      svg.appendChild(hx); fadeIn(hx, i * 0.015);
      svg.appendChild(mk('text', { x: cx, y: cy + 3.5, 'text-anchor': 'middle', 'font-size': 9.5, 'font-weight': 700, fill: t > 0.55 ? '#fff' : '#14532d', 'font-family': 'Inter, sans-serif' }, c.code));
    });
    // legend
    var lx = 16, ly = vh - 14;
    var defs = mk('defs', {}); var lg = mk('linearGradient', { id: id + '-lg', x1: '0', y1: '0', x2: '1', y2: '0' });
    lg.appendChild(mk('stop', { offset: '0', 'stop-color': shade(o.min) })); lg.appendChild(mk('stop', { offset: '1', 'stop-color': shade(o.max) }));
    defs.appendChild(lg); svg.appendChild(defs);
    svg.appendChild(mk('rect', { x: lx, y: ly, width: 90, height: 9, rx: 2, fill: 'url(#' + id + '-lg)' }));
    svg.appendChild(mk('text', { x: lx, y: ly - 4, 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.min + '%' ));
    svg.appendChild(mk('text', { x: lx + 90, y: ly - 4, 'text-anchor': 'end', 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.max + '%' ));
    svg.appendChild(mk('text', { x: lx + 100, y: ly + 8, 'font-size': 9.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.legend ));
  }

  /* ---------- Sankey through a hub (sources → ₹1 → uses) ---------- */
  function sankeyHub(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 400; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var S = o.sources, U = o.uses, i;
    var tot = S.reduce(function(a, d){ return a + d.v; }, 0);
    var mT = 30, mB = 16, colW = 13, gap = 5, Hh = vh - mT - mB;
    var maxN = Math.max(S.length, U.length);
    var ppu = (Hh - gap * (maxN - 1)) / tot;
    var lx = 104, hx = vw / 2 - colW / 2, rx = vw - 104 - colW;
    function stack(list) {
      var h = list.map(function(d){ return d.v * ppu; });
      var ch = h.reduce(function(a, b){ return a + b; }, 0) + gap * (list.length - 1);
      var sy = mT + (Hh - ch) / 2, ys = [];
      h.forEach(function(hh){ ys.push(sy); sy += hh + gap; });
      return { y: ys, h: h };
    }
    var L = stack(S), R = stack(U);
    var hubH = tot * ppu, hubY = mT + (Hh - hubH) / 2;
    function ribbon(xa, ya0, ya1, xb, yb0, yb1, col, delay) {
      var xm = (xa + xb) / 2;
      var d = 'M' + xa + ',' + ya0.toFixed(1) + ' C' + xm + ',' + ya0.toFixed(1) + ' ' + xm + ',' + yb0.toFixed(1) + ' ' + xb + ',' + yb0.toFixed(1) +
        ' L' + xb + ',' + yb1.toFixed(1) + ' C' + xm + ',' + yb1.toFixed(1) + ' ' + xm + ',' + ya1.toFixed(1) + ' ' + xa + ',' + ya1.toFixed(1) + ' Z';
      var p = mk('path', { d: d, fill: col, 'fill-opacity': 0.5 });
      svg.appendChild(p); fadeIn(p, delay); return p;
    }
    // sources → hub
    var hubOff = hubY;
    S.forEach(function(d, k){ ribbon(lx + colW, L.y[k], L.y[k] + L.h[k], hx, hubOff, hubOff + L.h[k], d.color, k * 0.05); hubOff += L.h[k]; });
    // hub → uses
    hubOff = hubY;
    U.forEach(function(d, k){ var h = R.h[k]; ribbon(hx + colW, hubOff, hubOff + h, rx, R.y[k], R.y[k] + h, d.color, 0.25 + k * 0.05); hubOff += h; });
    // nodes
    S.forEach(function(d, k){ svg.appendChild(mk('rect', { x: lx, y: L.y[k], width: colW, height: Math.max(2, L.h[k]), rx: 2, fill: d.color })); });
    U.forEach(function(d, k){ svg.appendChild(mk('rect', { x: rx, y: R.y[k], width: colW, height: Math.max(2, R.h[k]), rx: 2, fill: d.color })); });
    svg.appendChild(mk('rect', { x: hx, y: hubY, width: colW, height: hubH, rx: 3, fill: ink(), 'fill-opacity': 0.85 }));
    // labels
    S.forEach(function(d, k){
      var cy = L.y[k] + L.h[k] / 2;
      svg.appendChild(mk('text', { x: lx - 7, y: cy + 3, 'text-anchor': 'end', 'font-size': 9.5, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, d.name));
      svg.appendChild(mk('text', { x: lx + colW + 4, y: cy + 3, 'font-size': 8.5, fill: d.color, 'font-family': 'JetBrains Mono, monospace' }, d.v + 'p'));
    });
    U.forEach(function(d, k){
      var cy = R.y[k] + R.h[k] / 2;
      svg.appendChild(mk('text', { x: rx + colW + 7, y: cy + 3, 'font-size': 9.5, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, d.name));
      svg.appendChild(mk('text', { x: rx - 4, y: cy + 3, 'text-anchor': 'end', 'font-size': 8.5, fill: d.color, 'font-family': 'JetBrains Mono, monospace' }, d.v + 'p'));
    });
    svg.appendChild(mk('text', { x: hx + colW / 2, y: hubY - 8, 'text-anchor': 'middle', 'font-size': 15, 'font-weight': 800, fill: ink(), 'font-family': 'Inter, sans-serif' }, o.hub || '₹1'));
    svg.appendChild(mk('text', { x: 16, y: 16, 'font-size': 9.5, 'font-weight': 700, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.leftLabel || 'comes from'));
    svg.appendChild(mk('text', { x: vw - 16, y: 16, 'text-anchor': 'end', 'font-size': 9.5, 'font-weight': 700, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.rightLabel || 'goes to'));
  }

  /* ---------- Seeded PRNG + hex helpers (shared by the map forms) ---------- */
  function rng(seed) {
    var t = seed >>> 0;
    return function() {
      t = (t + 0x6D2B79F5) >>> 0;
      var r = Math.imul(t ^ (t >>> 15), t | 1);
      r ^= r + Math.imul(r ^ (r >>> 7), r | 61);
      return ((r ^ (r >>> 14)) >>> 0) / 4294967296;
    };
  }
  function seedOf(str) { var h = 2166136261; for (var i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
  var SQ3 = Math.sqrt(3);
  function hexAt(col, row, s) { return [col * 1.5 * s, row * SQ3 * s + (col % 2) * SQ3 * s / 2]; }
  function hexPts(cx, cy, r) {
    var pts = [];
    for (var k = 0; k < 6; k++) { var a = Math.PI / 3 * k; pts.push((cx + r * Math.cos(a)).toFixed(1) + ',' + (cy + r * Math.sin(a)).toFixed(1)); }
    return pts.join(' ');
  }
  function inHex(dx, dy, r) {
    var ax = Math.abs(dx), ay = Math.abs(dy);
    return ay <= r * 0.8660254 && (1.7320508 * ax + ay) <= 1.7320508 * r;
  }
  function lerpCol(a, b, t) {
    function hx(c){ return [parseInt(c.slice(1,3),16), parseInt(c.slice(3,5),16), parseInt(c.slice(5,7),16)]; }
    var A = hx(a), B = hx(b), out = [];
    for (var i = 0; i < 3; i++) out.push(Math.round(A[i] + (B[i] - A[i]) * Math.max(0, Math.min(1, t))));
    return 'rgb(' + out.join(',') + ')';
  }

  /* ---------- Dot-density tile map (one dot = one unit, scattered at random) ---------- */
  function dotDensity(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 380; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var cells = o.cells;
    var cols = cells.map(function(c){ return c.col; }), rows = cells.map(function(c){ return c.row; });
    var colSpan = Math.max.apply(null, cols) - Math.min.apply(null, cols);
    var rowSpan = Math.max.apply(null, rows) - Math.min.apply(null, rows);
    // fit the grid to the frame: hexes are 2s wide, √3·s tall, columns 1.5s apart
    var s = Math.min((vw - 24) / (colSpan * 1.5 + 2), (vh - 52) / (rowSpan * 1.732 + 2.6));
    var r = s * 0.88; // a visible gutter, so one state's dot field can't be read as its neighbour's
    var raw = cells.map(function(c){ return hexAt(c.col, c.row, s); });
    var xs = raw.map(function(p){ return p[0]; }), ys = raw.map(function(p){ return p[1]; });
    var minX = Math.min.apply(null, xs), maxX = Math.max.apply(null, xs);
    var minY = Math.min.apply(null, ys), maxY = Math.max.apply(null, ys);
    var ox = (vw - (maxX - minX)) / 2 - minX, oy = (vh - 46 - (maxY - minY)) / 2 - minY;
    var unit = o.unit, dotR = o.dotR || 1.7, k;
    cells.forEach(function(c, i) {
      var cx = raw[i][0] + ox, cy = raw[i][1] + oy;
      svg.appendChild(mk('polygon', { points: hexPts(cx, cy, r), fill: ink(), 'fill-opacity': 0.06, stroke: gridc(), 'stroke-width': 1 }));
    });
    cells.forEach(function(c, i) {
      var cx = raw[i][0] + ox, cy = raw[i][1] + oy;
      var n = Math.round(c.v / unit); if (n <= 0) return;
      var rand = rng(seedOf(c.code + '|' + id)), g = mk('g', {});
      for (var j = 0, guard = 0; j < n && guard < n * 60; guard++) {
        var dx = (rand() * 2 - 1) * r, dy = (rand() * 2 - 1) * r * 0.8660254;
        if (!inHex(dx, dy, r * 0.94)) continue;
        g.appendChild(mk('circle', { cx: (cx + dx).toFixed(1), cy: (cy + dy).toFixed(1), r: dotR, fill: o.color, 'fill-opacity': 0.8 }));
        j++;
      }
      svg.appendChild(g); fadeIn(g, i * 0.012);
    });
    // codes last, with a halo so they stay legible over dense dots
    cells.forEach(function(c, i) {
      var cx = raw[i][0] + ox, cy = raw[i][1] + oy;
      svg.appendChild(mk('text', { x: cx, y: cy + 3, 'text-anchor': 'middle', 'font-size': 9, 'font-weight': 700,
        fill: ink(), 'fill-opacity': 0.75, stroke: 'var(--color-bg-card, #fff)', 'stroke-width': 2.8, 'stroke-opacity': 0.9,
        'paint-order': 'stroke fill', 'font-family': 'JetBrains Mono, monospace' }, c.code));
    });
    // legend — a sample of dots at the same density
    var lx = 16, ly = vh - 18;
    var lr = rng(seedOf('legend|' + id));
    for (k = 0; k < 10; k++) svg.appendChild(mk('circle', { cx: (lx + lr() * 42).toFixed(1), cy: (ly - 6 + lr() * 12).toFixed(1), r: dotR, fill: o.color, 'fill-opacity': 0.8 }));
    svg.appendChild(mk('text', { x: lx + 52, y: ly + 3, 'font-size': 9.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.legend));
  }

  /* ---------- Dorling cartogram (circles sized by value, nudged apart) ---------- */
  function dorling(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 400; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var pad = 14, top = 8, bot = 46;
    // stretch the hand-placed anchors across the whole frame
    var axs = o.nodes.map(function(d){ return d.x; }), ays = o.nodes.map(function(d){ return d.y; });
    var x0 = Math.min.apply(null, axs), x1 = Math.max.apply(null, axs);
    var y0 = Math.min.apply(null, ays), y1 = Math.max.apply(null, ays);
    var nodes = o.nodes.map(function(d) {
      var px = pad + (d.x - x0) / (x1 - x0) * (vw - 2 * pad);
      var py = top + (d.y - y0) / (y1 - y0) * (vh - top - bot);
      return { code: d.code, size: d.size, v: d.v, ax: px, ay: py, x: px, y: py, r: o.k * Math.sqrt(d.size) };
    });
    for (var it = 0; it < 260; it++) {
      for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        a.x += (a.ax - a.x) * 0.045; a.y += (a.ay - a.y) * 0.045;
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j], dx = b.x - a.x, dy = b.y - a.y;
          var d = Math.sqrt(dx * dx + dy * dy) || 0.01, min = a.r + b.r + 1.2;
          if (d < min) {
            var push = (min - d) / d * 0.5, mx = dx * push, my = dy * push;
            var wa = b.r / (a.r + b.r), wb = a.r / (a.r + b.r);
            a.x -= mx * 2 * wa; a.y -= my * 2 * wa; b.x += mx * 2 * wb; b.y += my * 2 * wb;
          }
        }
        a.x = Math.max(a.r + 2, Math.min(vw - a.r - 2, a.x));
        a.y = Math.max(a.r + top - 6, Math.min(vh - bot - a.r + 6, a.y));
      }
    }
    function shade(v) { return lerpCol(o.lowColor, o.highColor, (v - o.min) / (o.max - o.min)); }
    nodes.forEach(function(n, i) {
      var g = mk('g', {});
      g.appendChild(mk('circle', { cx: n.x.toFixed(1), cy: n.y.toFixed(1), r: n.r.toFixed(1), fill: shade(n.v), stroke: '#fff', 'stroke-width': 1.1, 'stroke-opacity': 0.75 }));
      if (n.r >= 7.4) {
        var dark = (n.v - o.min) / (o.max - o.min) > 0.5;
        var fs = Math.max(6.5, Math.min(12, n.r * 0.55));
        g.appendChild(mk('text', { x: n.x.toFixed(1), y: (n.y + fs * 0.34).toFixed(1), 'text-anchor': 'middle', 'font-size': fs.toFixed(1), 'font-weight': 800, fill: dark ? '#fff' : '#7c2d12', 'font-family': 'Inter, sans-serif' }, n.code));
      }
      svg.appendChild(g); fadeIn(g, i * 0.02);
    });
    var lx = 16, lw = 150, ly = vh - 12;
    var lg = mk('linearGradient', { id: id + '-dg', x1: '0', y1: '0', x2: '1', y2: '0' });
    lg.appendChild(mk('stop', { offset: '0', 'stop-color': o.lowColor }));
    lg.appendChild(mk('stop', { offset: '1', 'stop-color': o.highColor }));
    ensureDefs(svg).appendChild(lg);
    svg.appendChild(mk('text', { x: lx, y: ly - 22, 'font-size': 9.5, 'font-weight': 700, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.legend));
    svg.appendChild(mk('rect', { x: lx, y: ly - 16, width: lw, height: 9, rx: 2, fill: 'url(#' + id + '-dg)' }));
    svg.appendChild(mk('text', { x: lx, y: ly, 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.minLabel));
    svg.appendChild(mk('text', { x: lx + lw, y: ly, 'text-anchor': 'end', 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.maxLabel));
  }

  /* ---------- Tilegram (one tile = one unit; states built from tiles) ---------- */
  function tilegram(id, o) {
    var svg = frame(id); if (!svg) return; var vw = 460, vh = 470; svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var tiles = [];
    o.groups.forEach(function(g) {
      g.t.split(' ').forEach(function(cr) {
        var p = cr.split(',');
        tiles.push({ code: g.s, zone: g.z, col: +p[0], row: +p[1] });
      });
    });
    var mapW = 292, s = 15.4;
    var raw = tiles.map(function(t){ return hexAt(t.col, t.row, s); });
    var xs = raw.map(function(p){ return p[0]; }), ys = raw.map(function(p){ return p[1]; });
    var minX = Math.min.apply(null, xs), maxX = Math.max.apply(null, xs);
    var minY = Math.min.apply(null, ys), maxY = Math.max.apply(null, ys);
    var ox = (mapW - (maxX - minX)) / 2 - minX + 6, oy = (vh - 16 - (maxY - minY)) / 2 - minY;
    var zc = o.zones.reduce(function(m, z){ m[z.id] = z.color; return m; }, {});
    var at = {}, cent = {};
    tiles.forEach(function(t){ at[t.col + ',' + t.row] = t.code; });
    // neighbour offsets per hex edge (0:SE 1:S 2:SW 3:NW 4:N 5:NE), odd columns sit half a row lower
    function nb(t, k) {
      var c = t.col, r = t.row, odd = c % 2 ? 1 : 0;
      if (k === 1) return [c, r + 1];
      if (k === 4) return [c, r - 1];
      if (k === 0) return [c + 1, r + odd];
      if (k === 5) return [c + 1, r - 1 + odd];
      if (k === 2) return [c - 1, r + odd];
      return [c - 1, r - 1 + odd];
    }
    tiles.forEach(function(t, i) {
      var cx = raw[i][0] + ox, cy = raw[i][1] + oy;
      var hx = mk('polygon', { points: hexPts(cx, cy, s * 0.98), fill: zc[t.zone], 'fill-opacity': 0.86, stroke: 'var(--color-bg-card, #fff)', 'stroke-width': 1 });
      svg.appendChild(hx); fadeIn(hx, i * 0.006);
      var c = cent[t.code] || (cent[t.code] = { x: 0, y: 0, n: 0, tiles: [] });
      c.x += cx; c.y += cy; c.n++; c.tiles.push([cx, cy]);
    });
    // state outlines: draw only those hex edges whose neighbour is a different state
    tiles.forEach(function(t, i) {
      var cx = raw[i][0] + ox, cy = raw[i][1] + oy, rr = s * 0.98, d = '';
      for (var k = 0; k < 6; k++) {
        var n = nb(t, k); if (at[n[0] + ',' + n[1]] === t.code) continue;
        var a0 = Math.PI / 3 * k, a1 = Math.PI / 3 * (k + 1);
        d += 'M' + (cx + rr * Math.cos(a0)).toFixed(1) + ',' + (cy + rr * Math.sin(a0)).toFixed(1) +
             'L' + (cx + rr * Math.cos(a1)).toFixed(1) + ',' + (cy + rr * Math.sin(a1)).toFixed(1);
      }
      if (d) svg.appendChild(mk('path', { d: d, fill: 'none', stroke: ink(), 'stroke-opacity': 0.5, 'stroke-width': 1.8, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }));
    });
    Object.keys(cent).forEach(function(code) {
      var c = cent[code], mx = c.x / c.n, my = c.y / c.n, best = c.tiles[0], bd = Infinity;
      c.tiles.forEach(function(p){ var d = (p[0] - mx) * (p[0] - mx) + (p[1] - my) * (p[1] - my); if (d < bd) { bd = d; best = p; } });
      svg.appendChild(mk('text', { x: best[0].toFixed(1), y: (best[1] + 3.4).toFixed(1), 'text-anchor': 'middle',
        'font-size': c.n >= 3 ? 10 : 8, 'font-weight': 800, fill: '#fff', 'font-family': 'Inter, sans-serif' }, code));
    });
    // legend: zones, their tile counts and share
    var counts = {};
    tiles.forEach(function(t){ counts[t.zone] = (counts[t.zone] || 0) + 1; });
    var lx = mapW + 22, ly = 44;
    svg.appendChild(mk('text', { x: lx, y: ly - 20, 'font-size': 9.5, 'font-weight': 700, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.legendTitle));
    o.zones.forEach(function(z, i) {
      var y = ly + i * 30;
      svg.appendChild(mk('polygon', { points: hexPts(lx + 8, y, 8), fill: z.color, 'fill-opacity': 0.88 }));
      svg.appendChild(mk('text', { x: lx + 22, y: y - 1, 'font-size': 10, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, z.name));
      svg.appendChild(mk('text', { x: lx + 22, y: y + 11, 'font-size': 9, fill: ink(), 'fill-opacity': 0.7, 'font-family': 'JetBrains Mono, monospace' }, counts[z.id] + ' hexes · ' + Math.round(counts[z.id] / tiles.length * 100) + '%'));
    });
    svg.appendChild(mk('text', { x: lx, y: ly + o.zones.length * 30 + 12, 'font-size': 9, fill: ink(), 'fill-opacity': 0.75, 'font-family': 'JetBrains Mono, monospace' }, tiles.length + ' hexes'));
    svg.appendChild(mk('text', { x: lx, y: ly + o.zones.length * 30 + 25, 'font-size': 9, fill: ink(), 'fill-opacity': 0.75, 'font-family': 'JetBrains Mono, monospace' }, o.unitLabel));
  }

  /* ---------- Framework: Arnstein's ladder ---------- */
  function ladder(id) {
    var svg = frame(id); if (!svg) return;
    var rungs = [
      ['Manipulation', COL.red], ['Therapy', COL.red],
      ['Informing', COL.amber], ['Consultation', COL.amber], ['Placation', COL.amber],
      ['Partnership', COL.green], ['Delegated power', COL.green], ['Citizen control', COL.green]
    ];
    var bands = [['Nonparticipation', COL.red, 0, 2], ['Tokenism', COL.amber, 2, 5], ['Citizen power', COL.green, 5, 8]];
    var mT = 16, mB = 14, x = 150, rw = 250, n = rungs.length;
    var rh = (H - mT - mB - (n - 1) * 6) / n;
    rungs.forEach(function(r, i){
      var idx = n - 1 - i; // draw top rung first
      var y = mT + i * (rh + 6);
      var rect = mk('rect', { x: x, y: y, width: rw, height: rh, rx: 5, fill: rungs[idx][1], opacity: 0.9 });
      svg.appendChild(rect); fadeIn(rect, i * 0.06);
      svg.appendChild(mk('text', { x: x + 12, y: y + rh/2 + 4, 'font-size': 12, 'font-weight': 700, fill: '#fff', 'font-family': 'Inter, sans-serif' }, (idx + 1) + '. ' + rungs[idx][0]));
    });
    bands.forEach(function(b){
      var yTop = mT + (n - 1 - (b[3] - 1)) * (rh + 6);
      var yBot = mT + (n - 1 - b[2]) * (rh + 6) + rh;
      svg.appendChild(mk('line', { x1: x - 10, y1: yTop + 2, x2: x - 10, y2: yBot - 2, stroke: b[1], 'stroke-width': 3 }));
      svg.appendChild(mk('text', { x: x - 18, y: (yTop + yBot)/2 + 4, 'text-anchor': 'end', 'font-size': 11, 'font-weight': 700, fill: b[1], 'font-family': 'Inter, sans-serif' }, b[0]));
    });
    // upward arrow
    svg.appendChild(mk('path', { d: 'M' + (x + rw + 18) + ',' + (H - mB) + ' L' + (x + rw + 18) + ',' + (mT + 10), stroke: ink(), 'stroke-width': 1.5, 'marker-end': 'url(#arrUp)' }));
    var defs = mk('defs', {});
    var marker = mk('marker', { id: 'arrUp', markerWidth: 8, markerHeight: 8, refX: 4, refY: 6, orient: 'auto' });
    marker.appendChild(mk('path', { d: 'M0,6 L4,0 L8,6', fill: 'none', stroke: ink(), 'stroke-width': 1.5 }));
    defs.appendChild(marker); svg.appendChild(defs);
    svg.appendChild(mk('text', { x: x + rw + 30, y: H/2, 'text-anchor': 'middle', 'font-size': 10, fill: ink(), 'font-family': 'JetBrains Mono, monospace', transform: 'rotate(-90 ' + (x + rw + 30) + ' ' + (H/2) + ')' }, 'more power'));
  }

  /* ---------- Framework: results chain ---------- */
  function resultsChain(id) {
    var svg = frame(id); if (!svg) return;
    var steps = [['Inputs', COL.slate], ['Activities', COL.slate], ['Outputs', COL.blue], ['Outcomes', COL.teal], ['Impact', COL.purple]];
    var n = steps.length, bw = 70, by = H/2 - 22, bh = 44, gap = (W - 24 - n * bw) / (n - 1);
    steps.forEach(function(s, i){
      var x = 12 + i * (bw + gap);
      var rect = mk('rect', { x: x, y: by, width: bw, height: bh, rx: 8, fill: s[1], opacity: 0.92 });
      svg.appendChild(rect); fadeIn(rect, i * 0.1);
      svg.appendChild(mk('text', { x: x + bw/2, y: by + bh/2 + 4, 'text-anchor': 'middle', 'font-size': 11.5, 'font-weight': 700, fill: '#fff', 'font-family': 'Inter, sans-serif' }, s[1]===COL.slate? s[0] : s[0]));
      if (i < n - 1) {
        var ax = x + bw, ax2 = x + bw + gap;
        svg.appendChild(mk('path', { d: 'M' + (ax + 3) + ',' + (by + bh/2) + ' L' + (ax2 - 3) + ',' + (by + bh/2), stroke: ink(), 'stroke-width': 1.6, 'marker-end': 'url(#arrR)' }));
      }
    });
    var defs = mk('defs', {});
    var marker = mk('marker', { id: 'arrR', markerWidth: 8, markerHeight: 8, refX: 6, refY: 4, orient: 'auto' });
    marker.appendChild(mk('path', { d: 'M0,0 L8,4 L0,8', fill: ink() }));
    defs.appendChild(marker); svg.appendChild(defs);
    // attribution gap between Outputs (i=2) and Outcomes (i=3)
    var gx = 12 + 2 * (bw + gap) + bw + gap/2;
    svg.appendChild(mk('line', { x1: gx, y1: by - 22, x2: gx, y2: by + bh + 22, stroke: COL.red, 'stroke-width': 1.5, 'stroke-dasharray': '4,4' }));
    svg.appendChild(mk('text', { x: gx, y: by - 28, 'text-anchor': 'middle', 'font-size': 10.5, 'font-weight': 700, fill: COL.red, 'font-family': 'Inter, sans-serif' }, 'the attribution gap'));
    svg.appendChild(mk('text', { x: W/2, y: H - 14, 'text-anchor': 'middle', 'font-size': 10, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, 'what we control  →  what we hope to cause'));
  }

  /* ---------- Framework: poverty trap loop ---------- */
  function trapLoop(id) {
    var svg = frame(id); if (!svg) return;
    var cx = W/2, cy = H/2 + 2, r = 86, nr = 33;
    var nodes = [['Low', 'income', COL.red], ['Low', 'savings', COL.amber], ['Low', 'investment', COL.purple], ['Low', 'productivity', COL.blue]];
    var pts = nodes.map(function(_, i){ var a = (i / nodes.length) * 2 * Math.PI - Math.PI/2; return [cx + r * Math.cos(a), cy + r * Math.sin(a)]; });
    var defs = mk('defs', {});
    var marker = mk('marker', { id: id + '-arr', markerWidth: 10, markerHeight: 10, refX: 7, refY: 5, orient: 'auto' });
    marker.appendChild(mk('path', { d: 'M0,0 L10,5 L0,10 Z', fill: '#e11d48' }));
    defs.appendChild(marker); svg.appendChild(defs);
    for (var i = 0; i < pts.length; i++) {
      var p = pts[i], q = pts[(i+1) % pts.length];
      var a0 = Math.atan2(p[1]-cy, p[0]-cx), a1 = Math.atan2(q[1]-cy, q[0]-cx);
      // start/end on the node rims, arc bowed outward
      var sx = p[0] + Math.cos(a0 + 0.7) * 0, sy = p[1];
      var s = [cx + (r) * Math.cos(a0 + 0.42), cy + (r) * Math.sin(a0 + 0.42)];
      var e = [cx + (r) * Math.cos(a1 - 0.42), cy + (r) * Math.sin(a1 - 0.42)];
      var mcx = (s[0]+e[0])/2, mcy = (s[1]+e[1])/2, ol = Math.hypot(mcx-cx, mcy-cy);
      var ctrl = [mcx + (mcx-cx)/ol * 26, mcy + (mcy-cy)/ol * 26];
      var path = mk('path', { d: 'M' + s[0].toFixed(1) + ',' + s[1].toFixed(1) + ' Q' + ctrl[0].toFixed(1) + ',' + ctrl[1].toFixed(1) + ' ' + e[0].toFixed(1) + ',' + e[1].toFixed(1), fill: 'none', stroke: '#e11d48', 'stroke-width': 2.6, 'stroke-linecap': 'round', 'marker-end': 'url(#' + id + '-arr)' });
      svg.appendChild(path); animPath(path);
    }
    pts.forEach(function(p, i){
      var g = mk('g', {}); fadeIn(g, i * 0.12);
      g.appendChild(mk('circle', { cx: p[0], cy: p[1], r: nr, fill: nodes[i][2] }));
      g.appendChild(mk('text', { x: p[0], y: p[1] - 2, 'text-anchor': 'middle', 'font-size': 10.5, 'font-weight': 600, fill: '#fff', 'font-family': 'Inter, sans-serif' }, nodes[i][0]));
      g.appendChild(mk('text', { x: p[0], y: p[1] + 11, 'text-anchor': 'middle', 'font-size': 10.5, 'font-weight': 800, fill: '#fff', 'font-family': 'Inter, sans-serif' }, nodes[i][1]));
      svg.appendChild(g);
    });
    svg.appendChild(mk('text', { x: cx, y: cy - 2, 'text-anchor': 'middle', 'font-size': 11, 'font-weight': 700, fill: '#e11d48', 'font-family': 'Inter, sans-serif' }, 'self-' ));
    svg.appendChild(mk('text', { x: cx, y: cy + 11, 'text-anchor': 'middle', 'font-size': 11, 'font-weight': 700, fill: '#e11d48', 'font-family': 'Inter, sans-serif' }, 'reinforcing'));
  }

  /* ---------- Framework: intersectionality venn ---------- */
  function venn(id) {
    var svg = frame(id); if (!svg) return;
    var r = 62;
    var circles = [['Gender', COL.red, 230, 106], ['Caste', '#2563eb', 192, 168], ['Class', COL.amber, 268, 168]];
    circles.forEach(function(c, i){
      var circ = mk('circle', { cx: c[2], cy: c[3], r: r, fill: c[1], 'fill-opacity': 0.18, stroke: c[1], 'stroke-width': 2.5 });
      svg.appendChild(circ); fadeIn(circ, i * 0.12);
    });
    svg.appendChild(mk('text', { x: 230, y: 36, 'text-anchor': 'middle', 'font-size': 15, 'font-weight': 800, fill: COL.red, 'font-family': 'Inter, sans-serif' }, 'Gender'));
    svg.appendChild(mk('text', { x: 138, y: 250, 'text-anchor': 'middle', 'font-size': 15, 'font-weight': 800, fill: '#2563eb', 'font-family': 'Inter, sans-serif' }, 'Caste'));
    svg.appendChild(mk('text', { x: 322, y: 250, 'text-anchor': 'middle', 'font-size': 15, 'font-weight': 800, fill: COL.amber, 'font-family': 'Inter, sans-serif' }, 'Class'));
    // central intersection — a clear, readable highlight
    var ccx = 230, ccy = 149;
    svg.appendChild(mk('rect', { x: ccx - 44, y: ccy - 15, width: 88, height: 31, rx: 9, fill: '#ffffff', stroke: '#1f2937', 'stroke-width': 1.3 }));
    svg.appendChild(mk('text', { x: ccx, y: ccy - 1, 'text-anchor': 'middle', 'font-size': 10, 'font-weight': 800, fill: '#1f2937', 'font-family': 'Inter, sans-serif' }, 'compounded'));
    svg.appendChild(mk('text', { x: ccx, y: ccy + 11, 'text-anchor': 'middle', 'font-size': 10, 'font-weight': 800, fill: '#1f2937', 'font-family': 'Inter, sans-serif' }, 'disadvantage'));
  }

  /* ---------- Framework: systems iceberg ---------- */
  function iceberg(id) {
    var svg = frame(id); if (!svg) return;
    var waterY = 100, cx = 230;
    svg.appendChild(mk('rect', { x: 0, y: waterY, width: W, height: H - waterY, fill: '#4361ee', 'fill-opacity': 0.06 }));
    var berg = mk('path', { d: 'M230,36 L272,100 L308,160 L288,212 L250,252 L210,252 L172,212 L152,160 L188,100 Z', fill: '#cfe3f5', stroke: '#7da9d8', 'stroke-width': 1.5 });
    svg.appendChild(berg); fadeIn(berg, 0);
    svg.appendChild(mk('line', { x1: 0, y1: waterY, x2: W, y2: waterY, stroke: '#4361ee', 'stroke-width': 1.4, 'stroke-dasharray': '6,4', opacity: 0.7 }));
    svg.appendChild(mk('text', { x: 8, y: waterY - 7, 'font-size': 9.5, fill: '#4361ee', 'font-family': 'JetBrains Mono, monospace' }, 'sea level'));
    svg.appendChild(mk('text', { x: cx, y: 66, 'text-anchor': 'middle', 'font-size': 13, 'font-weight': 800, fill: '#1d4ed8', 'font-family': 'Inter, sans-serif' }, 'EVENTS'));
    svg.appendChild(mk('text', { x: cx, y: 82, 'text-anchor': 'middle', 'font-size': 9.5, fill: '#1d4ed8', 'font-family': 'JetBrains Mono, monospace' }, 'what we see'));
    [['Patterns', 146], ['Structures', 184], ['Mental models', 218]].forEach(function(l){
      svg.appendChild(mk('text', { x: cx, y: l[1], 'text-anchor': 'middle', 'font-size': 12.5, 'font-weight': 700, fill: '#13335f', 'font-family': 'Inter, sans-serif' }, l[0]));
    });
  }

  /* ---------- Framework: make your own (closing) ---------- */
  function makeYourOwn(id) {
    var svg = frame(id); if (!svg) return;
    var cy = H/2;
    // tiny line
    var d = 'M40,' + (cy+30) + ' L90,' + (cy-10) + ' L140,' + (cy+10) + ' L190,' + (cy-40);
    var p = mk('path', { d: d, fill: 'none', stroke: COL.teal, 'stroke-width': 3, 'stroke-linecap': 'round', 'stroke-linejoin': 'round' });
    svg.appendChild(p); animPath(p);
    // tiny bars
    [[260,40,COL.blue],[300,70,COL.amber],[340,30,COL.purple],[380,60,COL.red]].forEach(function(b, i){
      var rect = mk('rect', { x: b[0], y: cy + 30 - b[1], width: 26, height: b[1], rx: 4, fill: b[2], opacity: 0.9 });
      svg.appendChild(rect); fadeIn(rect, 0.6 + i*0.1);
    });
    svg.appendChild(mk('text', { x: W/2, y: H - 20, 'text-anchor': 'middle', 'font-size': 14, 'font-weight': 800, fill: ink(), 'font-family': 'Inter, sans-serif' }, 'your data, your frame, your turn' ));
  }

  /* ---------- Population-vs-wealth split flow (who owns what) ---------- */
  /* Two bars on one scale — one split by people, one by a resource (wealth/income) —
     with ribbons linking each group across the two, so the disparity becomes a shape. */
  function splitFlow(id, o) {
    var svg = frame(id); if (!svg) return;
    var groups = o.groups, topKey = o.topKey || 'pop', botKey = o.botKey || 'wealth';
    var padL = 56, padR = 14, fullW = W - padL - padR;
    var topY = 50, botY = 178, barH = 32, ribA = topY + barH, ribB = botY, my = (ribA + ribB) / 2;

    function segs(key) { var out = [], acc = 0; groups.forEach(function (g) { var w = g[key] / 100 * fullW; out.push([padL + acc, w]); acc += w; }); return out; }
    var A = segs(topKey), B = segs(botKey);

    // ribbons (behind the bars)
    groups.forEach(function (g, i) {
      var a = A[i], b = B[i];
      var d = 'M' + a[0].toFixed(1) + ',' + ribA + ' C' + a[0].toFixed(1) + ',' + my + ' ' + b[0].toFixed(1) + ',' + my + ' ' + b[0].toFixed(1) + ',' + ribB +
        ' L' + (b[0] + b[1]).toFixed(1) + ',' + ribB + ' C' + (b[0] + b[1]).toFixed(1) + ',' + my + ' ' + (a[0] + a[1]).toFixed(1) + ',' + my + ' ' + (a[0] + a[1]).toFixed(1) + ',' + ribA + ' Z';
      var rib = mk('path', { d: d, fill: g.color, 'fill-opacity': (g.hl ? 0.5 : 0.26) });
      svg.appendChild(rib); fadeIn(rib, 0.15 + i * 0.07);
    });

    // bars + percentage labels
    function bar(xs, key, y) {
      groups.forEach(function (g, i) {
        var s = xs[i];
        var r = mk('rect', { x: s[0].toFixed(1), y: y, width: Math.max(s[1], 0.6).toFixed(1), height: barH, fill: g.color, rx: 1.5 });
        svg.appendChild(r); fadeIn(r, 0.05 + i * 0.05);
        var lbl = (Math.round(g[key] * 10) / 10) + '%', cx = s[0] + s[1] / 2;
        if (s[1] >= 28) {
          svg.appendChild(mk('text', { x: cx.toFixed(1), y: y + barH / 2 + 3.5, 'text-anchor': 'middle', 'font-size': 10.5, 'font-weight': 700, fill: '#fff', 'font-family': 'Inter, sans-serif' }, lbl));
        } else {
          var above = (y === topY), ly = above ? y - 6 : y + barH + 12, ty1 = above ? y - 4 : y + barH, ty2 = above ? y - 1 : y + barH + 3;
          svg.appendChild(mk('line', { x1: cx.toFixed(1), x2: cx.toFixed(1), y1: ty1, y2: ty2, stroke: g.color, 'stroke-width': 1 }));
          svg.appendChild(mk('text', { x: cx.toFixed(1), y: ly, 'text-anchor': 'middle', 'font-size': 10, 'font-weight': 700, fill: g.color, 'font-family': 'Inter, sans-serif' }, lbl));
        }
      });
    }
    bar(A, topKey, topY); bar(B, botKey, botY);

    // row labels in the left gutter
    svg.appendChild(mk('text', { x: padL - 8, y: topY + barH / 2 + 3.5, 'text-anchor': 'end', 'font-size': 11, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, o.topLabel || 'People'));
    svg.appendChild(mk('text', { x: padL - 8, y: botY + barH / 2 + 3.5, 'text-anchor': 'end', 'font-size': 11, 'font-weight': 700, fill: ink(), 'font-family': 'Inter, sans-serif' }, o.botLabel || 'Wealth'));

    // legend (group names) along the bottom
    var ly = H - 14, lx = padL;
    groups.forEach(function (g) {
      svg.appendChild(mk('rect', { x: lx, y: ly - 8, width: 10, height: 10, rx: 2, fill: g.color }));
      svg.appendChild(mk('text', { x: lx + 14, y: ly + 1, 'font-size': 10.5, 'font-weight': g.hl ? 700 : 500, fill: ink(), 'font-family': 'Inter, sans-serif' }, g.label));
      lx += 14 + g.label.length * 5.7 + 16;
    });
  }

  /* ---------- Render everything ---------- */
  /* ---------- Bump chart: rank over time ---------- */
  function bumpChart(id, o) {
    var svg = frame(id); if (!svg) return;
    var mL = 34, mR = 108, mT = 22, mB = 26;
    var years = o.years, n = years.length, rmax = o.rankMax || 6;
    function X(i){ return mL + i * (W - mL - mR) / (n - 1); }
    function Y(r){ return mT + (r - 1) * (H - mT - mB) / (rmax - 1); }
    for (var r = 1; r <= rmax; r++) {
      svg.appendChild(mk('line', { x1: mL, y1: Y(r), x2: W - mR, y2: Y(r), stroke: gridc(), 'stroke-width': 1 }));
      svg.appendChild(mk('text', { x: mL - 8, y: Y(r) + 3.5, 'text-anchor': 'end', 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, r));
    }
    years.forEach(function(yr, i){ tick(svg, X(i), H - mB + 16, yr); });
    o.series.forEach(function(s, si){
      var pts = s.ranks.map(function(rk, i){ return [X(i), Y(rk)]; });
      var d = 'M' + pts.map(function(p){ return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' L');
      var path = mk('path', { d: d, fill: 'none', stroke: s.color, 'stroke-width': 3, 'stroke-linejoin': 'round', 'stroke-linecap': 'round', opacity: 0.92 });
      svg.appendChild(path); animPath(path);
      pts.forEach(function(p){ svg.appendChild(mk('circle', { cx: p[0], cy: p[1], r: 4.5, fill: s.color, stroke: '#fff', 'stroke-width': 1.5 })); });
      var last = pts[n - 1];
      svg.appendChild(mk('text', { x: last[0] + 9, y: last[1] + 3.5, 'text-anchor': 'start', 'font-size': 11, 'font-weight': 700, fill: s.color, 'font-family': 'Inter, sans-serif' }, s.name));
    });
    svg.appendChild(mk('text', { x: mL - 8, y: mT - 8, 'text-anchor': 'end', 'font-size': 8.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, 'rank'));
  }

  /* ---------- Radial (polar) area: a value around a 12-point clock ---------- */
  function radialArea(id, o) {
    var svg = frame(id); if (!svg) return;
    var cx = W / 2, cy = H / 2 + 6, rIn = 14, rOut = 108;
    var vals = o.values, n = vals.length, max = o.max;
    function ang(i){ return -Math.PI / 2 + i * 2 * Math.PI / n; }
    function R(v){ return rIn + (v / max) * (rOut - rIn); }
    (o.rings || []).forEach(function(rv){
      svg.appendChild(mk('circle', { cx: cx, cy: cy, r: R(rv), fill: 'none', stroke: gridc(), 'stroke-width': 1 }));
      svg.appendChild(mk('text', { x: cx + 3, y: cy - R(rv) - 2, 'font-size': 8, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, rv));
    });
    var pts = vals.map(function(v, i){ var a = ang(i); return [cx + R(v) * Math.cos(a), cy + R(v) * Math.sin(a)]; });
    var d = 'M' + pts.map(function(p){ return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' L') + ' Z';
    svg.appendChild(mk('path', { d: d, fill: o.color, 'fill-opacity': 0.26, stroke: o.color, 'stroke-width': 2.5, 'stroke-linejoin': 'round' }));
    vals.forEach(function(v, i){
      var a = ang(i), p = pts[i], hot = o.highlight && o.highlight.indexOf(i) >= 0;
      svg.appendChild(mk('circle', { cx: p[0], cy: p[1], r: hot ? 4 : 2.6, fill: hot ? o.hot : o.color }));
      var lr = rOut + 15, lx = cx + lr * Math.cos(a), ly = cy + lr * Math.sin(a) + 3;
      svg.appendChild(mk('text', { x: lx, y: ly, 'text-anchor': 'middle', 'font-size': 9.5, 'font-weight': hot ? 700 : 400, fill: hot ? o.hot : ink(), 'font-family': 'Inter, sans-serif' }, o.labels[i]));
    });
    if (o.center) {
      svg.appendChild(mk('text', { x: cx, y: cy - 2, 'text-anchor': 'middle', 'font-size': 13, 'font-weight': 800, fill: o.hot, 'font-family': 'Inter, sans-serif' }, o.center.big));
      svg.appendChild(mk('text', { x: cx, y: cy + 11, 'text-anchor': 'middle', 'font-size': 8.5, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.center.small));
    }
  }

  /* ---------- Bubble chart (log-x): wealth vs health, size = population ---------- */
  function bubbleChart(id, o) {
    var svg = frame(id); if (!svg) return;
    var mL = 30, mR = 12, mT = 12, mB = 30;
    var lo = Math.log(o.xMin), hi = Math.log(o.xMax);
    function X(v){ return mL + (Math.log(v) - lo) / (hi - lo) * (W - mL - mR); }
    function Y(v){ return H - mB - (v - o.yMin) / (o.yMax - o.yMin) * (H - mT - mB); }
    var maxPopRoot = Math.sqrt(Math.max.apply(null, o.points.map(function(p){ return p.pop; })));
    function R(pop){ return 5 + Math.sqrt(pop) / maxPopRoot * 30; }
    o.xticks.forEach(function(t){ var x = X(t); svg.appendChild(mk('line', { x1: x, y1: mT, x2: x, y2: H - mB, stroke: gridc(), 'stroke-width': 1 })); tick(svg, x, H - mB + 15, t >= 1000 ? (t / 1000) + 'k' : t); });
    o.yticks.forEach(function(t){ var y = Y(t); svg.appendChild(mk('line', { x1: mL, y1: y, x2: W - mR, y2: y, stroke: gridc(), 'stroke-width': 1 })); svg.appendChild(mk('text', { x: mL - 6, y: y + 3, 'text-anchor': 'end', 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, t)); });
    o.points.slice().sort(function(a, b){ return b.pop - a.pop; }).forEach(function(p, i){
      var cx = X(p.x), cy = Y(p.y), r = R(p.pop);
      var c = mk('circle', { cx: cx, cy: cy, r: r, fill: p.color, 'fill-opacity': 0.6, stroke: p.color, 'stroke-width': 1.4 });
      svg.appendChild(c); fadeIn(c, i * 0.05);
      if (p.label) svg.appendChild(mk('text', { x: cx, y: cy + 3, 'text-anchor': 'middle', 'font-size': 9.5, 'font-weight': 700, fill: '#fff', 'font-family': 'Inter, sans-serif' }, p.label));
      else if (p.note) svg.appendChild(mk('text', { x: cx, y: cy - r - 3, 'text-anchor': 'middle', 'font-size': 9, 'font-weight': 600, fill: ink(), 'font-family': 'Inter, sans-serif' }, p.note));
    });
    // region legend (top-left = high life, low GDP; sparse)
    (o.legend || []).forEach(function(lg, i){
      var lx = mL + 4 + (i % 2) * 92, ly = mT + 8 + Math.floor(i / 2) * 13;
      svg.appendChild(mk('circle', { cx: lx, cy: ly - 3, r: 4, fill: lg.color, 'fill-opacity': 0.75 }));
      svg.appendChild(mk('text', { x: lx + 8, y: ly, 'font-size': 8.5, fill: ink(), 'font-family': 'Inter, sans-serif' }, lg.name));
    });
    svg.appendChild(mk('text', { x: (mL + W - mR) / 2, y: H - 2, 'text-anchor': 'middle', 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace' }, o.xlabel));
    var ymid = mT + (H - mT - mB) / 2;
    svg.appendChild(mk('text', { x: 9, y: ymid, 'text-anchor': 'middle', 'font-size': 9, fill: ink(), 'font-family': 'JetBrains Mono, monospace', transform: 'rotate(-90 9 ' + ymid + ')' }, o.ylabel));
  }

  function renderAll() {
    lineChart('c-poverty',
      [{x:1990,y:37.9},{x:2000,y:29.7},{x:2010,y:16.7},{x:2015,y:10.4},{x:2019,y:8.4}],
      { yMax: 44, color: '#0d9488', area: true, valfmt: function(v){return v+'%';}, xfmt: function(x){return "'"+String(x).slice(2);} });

    lineChart('c-u5mr',
      [{x:1990,y:127},{x:1995,y:109.7},{x:2000,y:91.8},{x:2005,y:74.3},{x:2010,y:58.1},{x:2015,y:43.7},{x:2020,y:33},{x:2022,y:29.5}],
      { yMax: 138, color: '#4f46e5', area: true, valfmt: function(v){return Math.round(v);}, labelEvery: 2, xfmt: function(x){return "'"+String(x).slice(2);} });

    splitFlow('c-wealth',
      { topLabel:'People', botLabel:'Wealth',
        groups:[
          {label:'Bottom 50%', pop:50, wealth:6.4,  color:'#f3a6b0'},
          {label:'Middle 40%', pop:40, wealth:28.6, color:'#e0566a'},
          {label:'Next 9%',    pop:9,  wealth:24.9, color:'#b81d36'},
          {label:'Top 1%',     pop:1,  wealth:40.1, color:'#7d0d23', hl:true}
        ]});

    hbarChart('c-caste',
      [{label:'Sched. Tribes',y:44.4,color:'#7d0d23'},{label:'Sched. Castes',y:29.2,color:'#b81d36'},{label:'OBC',y:24.5,color:'#e0566a'},{label:'Others',y:14.9,color:'#f3a6b0'}],
      { xMax: 50, valfmt: function(v){return v+'%';}, refLine: { value: 24.85, label: 'national 24.8%' } });

    beeswarm('c-co2',
      [{n:'Qatar',v:43.55,label:'Qatar'},{n:'Kuwait',v:24.90},{n:'UAE',v:20.22},{n:'Saudi',v:17.15},
       {n:'Canada',v:14.91},{n:'Russia',v:14.45},{n:'Australia',v:14.21},{n:'USA',v:13.83},
       {n:'S Korea',v:11.04},{n:'China',v:9.24},{n:'Iran',v:9.10},{n:'Poland',v:7.63},
       {n:'Japan',v:7.54},{n:'Germany',v:7.06},{n:'S Africa',v:6.56},{n:'UK',v:4.42},{n:'France',v:4.25},
       {n:'Indonesia',v:2.41},{n:'Brazil',v:2.20},{n:'India',v:2.07,hl:true,label:'India'},
       {n:'Pakistan',v:0.91},{n:'Bangladesh',v:0.71},{n:'Nigeria',v:0.58},{n:'Ethiopia',v:0.14},{n:'DR Congo',v:0.04}],
      { vMax: 46, ticks: [0,10,20,30,40], dotColor: '#94a3b8', hlColor: '#0d9488',
        ref: { v: 4.7, label: 'world avg' }, axisLabel: 'tonnes CO₂ per person, per year (2023)' });

    funnel('c-pipeline',
      [{label:'Primary (1–5)',v:104.8},{label:'Upper primary',v:94.9},{label:'Secondary',v:79.4},{label:'Higher secondary',v:57.6},{label:'Higher education',v:28.5}],
      { vMax: 104.8, colors: ['#0d9488','#22a06b','#eab308','#f97316','#e11d48'] });

    donut('c-energy',
      [{label:'Coal',v:73,color:'#475569'},{label:'Hydro',v:8,color:'#2563eb'},{label:'Solar',v:7,color:'#f59e0b'},
       {label:'Wind',v:5,color:'#0ea5a4'},{label:'Nuclear',v:3,color:'#7c3aed'},{label:'Gas',v:2,color:'#94a3b8'},{label:'Bioenergy',v:2,color:'#16a34a'}],
      { centerBig: '73%', centerSub: 'still fossil' });

    dumbbell('c-gender',
      [{label:'Adult literacy',m:84.7,f:70.3},{label:'College enrolment',m:28.3,f:28.5},
       {label:'In the labour force',m:78.8,f:41.7},{label:'Seats in the Lok Sabha',m:86.6,f:13.4}],
      { mColor: '#1971c2', fColor: '#d6336c' });

    heatmap('c-nfhs',
      { cols: ['NFHS-3 ’05', 'NFHS-4 ’15', 'NFHS-5 ’21'],
        rows: ['Institutional births', 'Full immunisation', 'Woman uses a bank a/c', 'Child not stunted', 'Woman not anaemic'],
        values: [[39,79,89],[44,62,76],[null,53,79],[52,62,64],[45,47,43]] },
      { min: 38, max: 90 });

    if (window.LV_UPSET) {
      upset('c-upset-deprivation', window.LV_UPSET.deprivation,
        { acc: 1, unit: 'districts',
          caption: 'Each column is one exact combination. 706 districts, NFHS-5.',
          alt: 'UpSet plot: how six deprivations overlap across 706 Indian districts. '
             + 'The largest single group is 129 districts carrying five at once — every '
             + 'one except sanitation.' });

      upset('c-upset-backwards', window.LV_UPSET.backwards,
        { acc: 2, unit: 'districts',
          caption: 'Districts that moved the wrong way, NFHS-4 to NFHS-5. 574 districts.',
          alt: 'UpSet plot: which indicators went backwards between the two survey rounds. '
             + 'The largest group is 128 districts where both women\u2019s and '
             + 'children\u2019s anaemia worsened together.' });
    }

    forest('c-forest',
      [{label:'Net zero ~2050', est:1.4, lo:1.0, hi:1.8, color:'#16a34a'},
       {label:'Strong cuts', est:1.8, lo:1.3, hi:2.4, color:'#0d9488'},
       {label:'Middle of the road', est:2.7, lo:2.1, hi:3.5, color:'#eab308'},
       {label:'High emissions', est:3.6, lo:2.8, hi:4.6, color:'#f97316'},
       {label:'Very high emissions', est:4.4, lo:3.3, hi:5.7, color:'#e11d48'}],
      { vMax: 6, ticks: [0,2,4,6], refs: [{v:1.5, label:'1.5°', color:'#16a34a', side:'end'}, {v:2.0, label:'2° Paris', color:'#e11d48', side:'start'}] });

    lineChart('c-flfp',
      [{x:2017.5,y:23.3},{x:2021.5,y:32.8},{x:2022.5,y:37.0},{x:2023.5,y:41.7}],
      { yMax: 50, color: '#7c3aed', area: true, valfmt: function(v){return v.toFixed(1)+'%';},
        xfmt: function(x){var a=Math.floor(x); return "'"+String(a).slice(2)+"–"+String(a+1).slice(2);} });

    climateChart('c-climate');

    lineChart('c-le',
      [{x:1960,y:45.2},{x:1970,y:49.3},{x:1980,y:53.9},{x:1990,y:58.6},{x:2000,y:62.6},{x:2010,y:66.7},{x:2019,y:70.9}],
      { yMax: 78, color: '#0d9488', area: true, valfmt: function(v){return Math.round(v);}, xfmt: function(x){return "'"+String(x).slice(2);} });

    lineChart('c-solar',
      [{x:2014,y:2.6},{x:2016,y:9.0},{x:2018,y:21.7},{x:2020,y:34.6},{x:2022,y:54.0},{x:2024,y:87.2}],
      { yMax: 95, color: '#f59e0b', area: true, valfmt: function(v){return Math.round(v)+' GW';}, xfmt: function(x){return "'"+String(x).slice(2);} });

    lineChart('c-urban',
      [{x:1960,y:17.9},{x:1980,y:23.1},{x:2000,y:27.7},{x:2010,y:30.9},{x:2020,y:34.9},{x:2023,y:36.4}],
      { yMax: 42, color: '#6366f1', area: true, valfmt: function(v){return v.toFixed(1)+'%';}, xfmt: function(x){return "'"+String(x).slice(2);} });

    donut('c-gdp',
      [{label:'Services',v:54,color:'#0d9488'},{label:'Industry',v:27,color:'#475569'},{label:'Agriculture',v:19,color:'#22a06b'}],
      { centerBig: '54%', centerSub: 'services' });

    hbarChart('c-literacy',
      [{label:'Kerala',y:96.2,color:'#0d9488'},{label:'Delhi',y:88.7,color:'#22a06b'},{label:'Maharashtra',y:84.8,color:'#4f46e5'},{label:'Tamil Nadu',y:82.9,color:'#6366f1'},{label:'Rajasthan',y:71.6,color:'#f97316'},{label:'Bihar',y:61.8,color:'#e11d48'}],
      { xMax: 100, valfmt: function(v){return v+'%';}, refLine: { value: 80.2, label: 'national 80%' } });

    beeswarm('c-womenparl',
      [{n:'Rwanda',v:61.3,label:'Rwanda'},{n:'Cuba',v:55.7},{n:'Nicaragua',v:53.9},{n:'Mexico',v:50.4},
       {n:'South Africa',v:44.7},{n:'UK',v:34.6},{n:'USA',v:29.0},{n:'China',v:26.5},
       {n:'Bangladesh',v:20.9},{n:'Japan',v:16.0},{n:'India',v:13.6,hl:true,label:'India'},
       {n:'Sri Lanka',v:5.3},{n:'Nigeria',v:4.4}],
      { vMax: 65, ticks: [0,20,40,60], dotColor: '#94a3b8', hlColor: '#d6336c', hlUnit: '%',
        ref: { v: 26.9, label: 'world avg' }, axisLabel: 'women in the lower house of parliament, 2024 (%)' });

    smallMultiples('c-decline',
      { yMax: 215, cols: 4, color: '#64748b', hlColor: '#0d9488', axisLabel: 'under-5 deaths per 1,000 · 1990 → 2022',
        series: [
          { name:'Nigeria', pts:[[1990,207.6],[2000,177.3],[2010,126.3],[2022,117.5]] },
          { name:'Ethiopia', pts:[[1990,202],[2000,140.1],[2010,82.7],[2022,68.1]] },
          { name:'Rwanda', pts:[[1990,150.7],[2000,184.2],[2010,63.3],[2022,39.7]] },
          { name:'Bangladesh', pts:[[1990,146.5],[2000,85.5],[2010,48.7],[2022,30.7]] },
          { name:'India', hl:true, pts:[[1990,127],[2000,91.8],[2010,58.1],[2022,29.5]] },
          { name:'Indonesia', pts:[[1990,83.2],[2000,51.4],[2010,32.6],[2022,19.1]] },
          { name:'Brazil', pts:[[1990,62.8],[2000,34.4],[2010,18.6],[2022,14.6]] },
          { name:'China', pts:[[1990,53.6],[2000,36.6],[2010,15.7],[2022,6.6]] }
        ] });

    connectedScatter('c-transition',
      { xMax: 7.2, yMin: 30, yMax: 86, xTicks: [1,2,3,4,5,6,7], yTicks: [40,50,60,70,80],
        xLabel: 'babies per woman →', yLabel: 'life expectancy →',
        series: [
          { name:'Nigeria', color:'#f59e0b', pts:[[6.36,37.2],[6.85,46],[6.12,47.1],[4.55,54.1]] },
          { name:'India', color:'#4f46e5', pts:[[5.92,45.6],[4.78,53.6],[3.35,62.7],[1.99,71.7]] },
          { name:'Bangladesh', color:'#0d9488', pts:[[6.74,44],[6.33,52.3],[3.28,62],[2.18,74.3]] },
          { name:'China', color:'#e11d48', pts:[[4.45,33.4],[2.74,64.2],[1.63,72.3],[1.03,78.2]] },
          { name:'S. Korea', color:'#7c3aed', pts:[[5.99,53.8],[2.82,66],[1.48,75.9],[0.78,82.7]] }
        ] });

    chord('c-migration',
      { names: ['Africa','Asia','Europe','Lat. America','N. America','Oceania'],
        colors: ['#f59e0b','#e11d48','#4f46e5','#0d9488','#7c3aed','#64748b'],
        matrix: [
          [0, 5, 11, 0.5, 3, 0.5],
          [4, 0, 23, 0.5, 16, 3],
          [1, 7, 0, 1.5, 6, 1.5],
          [0.2, 0.5, 5, 0, 26, 0.3],
          [0.2, 0.6, 1, 1.5, 0, 0.2],
          [0.1, 0.4, 0.7, 0.1, 0.3, 0]
        ] });

    sankey('c-where',
      { left: ['Asia','Africa','Europe','Lat. America','N. America','Oceania'],
        right: ['Low income','Lower-middle','Upper-middle','High income'],
        lcolors: ['#e11d48','#f59e0b','#4f46e5','#0d9488','#7c3aed','#64748b'],
        flows: [
          [0.5, 2.3, 1.55, 0.43],
          [0.55, 0.75, 0.13, 0.03],
          [0, 0.02, 0.20, 0.52],
          [0, 0.14, 0.46, 0.06],
          [0, 0, 0, 0.38],
          [0, 0.014, 0, 0.032]
        ] });

    sankey('c-ghg',
      { left: ['Energy','Agriculture','Industry','Waste'],
        right: ['CO₂','Methane','Nitrous oxide','F-gases'],
        lcolors: ['#64748b','#16a34a','#7c3aed','#f59e0b'],
        rcolors: ['#64748b','#ea580c','#9333ea','#0891b2'],
        flows: [
          [2160, 50, 34, 0],
          [0, 290, 116, 0],
          [200, 0, 0, 39],
          [0, 60, 11, 0]
        ] });

    sankey3('c-ghg3',
      { sectors: { names: ['Energy','Agriculture','Industry','Waste'], colors: ['#64748b','#16a34a','#7c3aed','#f59e0b'] },
        gases: { names: ['CO₂','Methane','N₂O','F-gases'], colors: ['#64748b','#ea580c','#9333ea','#0891b2'] },
        subs: [
          { name:'Power', si:0, g:[1125,0,5,0] },
          { name:'Industry (fuel)', si:0, g:[558,0,2,0] },
          { name:'Transport', si:0, g:[288,0,2,0] },
          { name:'Buildings', si:0, g:[148,0,2,0] },
          { name:'Fugitive', si:0, g:[14,100,0,0] },
          { name:'Livestock', si:1, g:[0,230,0,0] },
          { name:'Rice', si:1, g:[0,70,0,0] },
          { name:'Soils', si:1, g:[0,0,106,0] },
          { name:'Processes', si:2, g:[200,0,0,39] },
          { name:'Landfill', si:3, g:[0,60,11,0] }
        ] });

    waffle('c-waffle',
      { items: [
        { label:'Electricity', pct:97, color:'#f59e0b' },
        { label:'A toilet', pct:70, color:'#0d9488' },
        { label:'Clean fuel', pct:59, color:'#e11d48' },
        { label:'A bank a/c', pct:78, color:'#4f46e5' },
        { label:'The internet', pct:46, color:'#7c3aed' },
        { label:'Health cover', pct:41, color:'#2563eb' }
      ] });

    streamGraph('c-stream',
      { years: [1960,1970,1980,1990,2000,2010,2023],
        series: [
          { name:'East Asia', color:'#e11d48', vals:[1043,1289,1555,1818,2050,2215,2384] },
          { name:'South Asia', color:'#4f46e5', vals:[508,640,806,1013,1237,1445,1663] },
          { name:'Africa', color:'#f59e0b', vals:[228,294,390,521,681,895,1260] },
          { name:'MENA+', color:'#0d9488', vals:[158,208,279,383,495,625,798] },
          { name:'Europe', color:'#7c3aed', vals:[668,739,795,845,865,891,925] },
          { name:'Lat. America', color:'#0ea5a4', vals:[219,285,360,441,520,588,658] },
          { name:'N. America', color:'#64748b', vals:[199,226,252,277,313,343,377] }
        ] });

    pyramid('c-pyramid',
      { ages: ['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80+'],
        a: { name:'1990', color:'#94a3b8', m:[64,58,51,45,40,36,32,28,21,17,15,13,10,7,5,3,1], f:[60,53,47,42,37,33,29,25,19,16,15,12,10,7,5,3,3] },
        b: { name:'2050', mcolor:'#4361ee', fcolor:'#d6336c', m:[49,51,53,55,56,57,59,62,64,65,62,56,50,42,31,22,23], f:[47,48,51,52,53,53,55,57,58,60,57,54,49,42,33,25,30] } });

    hexCartogram('c-states',
      { min: 50, max: 92, legend: 'female literacy ↑', cells: [
        {code:'JK',col:2,row:0,v:67},{code:'LA',col:3,row:0,v:77},
        {code:'PB',col:2,row:1,v:71},{code:'HP',col:3,row:1,v:76},{code:'UK',col:4,row:1,v:70},{code:'SK',col:6,row:1,v:76},{code:'AR',col:8,row:1,v:59},
        {code:'HR',col:2,row:2,v:66},{code:'DL',col:3,row:2,v:81},{code:'UP',col:4,row:2,v:59},{code:'BR',col:5,row:2,v:53},{code:'ML',col:6,row:2,v:73},{code:'AS',col:7,row:2,v:67},{code:'NL',col:8,row:2,v:76},
        {code:'RJ',col:1,row:3,v:52},{code:'MP',col:3,row:3,v:60},{code:'CG',col:4,row:3,v:60},{code:'JH',col:5,row:3,v:56},{code:'WB',col:6,row:3,v:71},{code:'TR',col:7,row:3,v:83},{code:'MN',col:8,row:3,v:73},{code:'MZ',col:9,row:3,v:89},
        {code:'GJ',col:0,row:4,v:70},{code:'MH',col:2,row:4,v:75},{code:'TS',col:4,row:4,v:58},{code:'OD',col:5,row:4,v:64},
        {code:'GA',col:1,row:5,v:82},{code:'KA',col:2,row:5,v:68},{code:'AP',col:4,row:5,v:60},
        {code:'KL',col:2,row:6,v:92},{code:'TN',col:3,row:6,v:73}
      ] });

    sankeyHub('c-rupee',
      { hub: '₹1', leftLabel: 'comes from', rightLabel: 'goes to',
        sources: [
          { name:'Borrowings',      v:24, color:'#e11d48' },
          { name:'Income tax',      v:22, color:'#4f46e5' },
          { name:'GST & other',     v:18, color:'#0d9488' },
          { name:'Corporation tax', v:17, color:'#6366f1' },
          { name:'Non-tax receipts',v:9,  color:'#0891b2' },
          { name:'Union excise',    v:5,  color:'#f59e0b' },
          { name:'Customs',         v:4,  color:'#7c3aed' },
          { name:'Capital receipts',v:1,  color:'#16a34a' }
        ],
        uses: [
          { name:"States' share",     v:22, color:'#0d9488' },
          { name:'Interest',          v:20, color:'#e11d48' },
          { name:'Central schemes',   v:16, color:'#4f46e5' },
          { name:'FC transfers',      v:8,  color:'#22a06b' },
          { name:'Sponsored schemes', v:8,  color:'#6366f1' },
          { name:'Defence',           v:8,  color:'#64748b' },
          { name:'Subsidies',         v:6,  color:'#f59e0b' },
          { name:'Pensions',          v:4,  color:'#7c3aed' },
          { name:'Other spending',    v:8,  color:'#94a3b8' }
        ] });

    dotDensity('c-poor-dots',
      { unit: 0.1, color: '#e11d48', legend: 'one dot = 10 lakh people in poverty', cells: [
        {code:'JK',col:2,row:0,v:0.18},{code:'LA',col:3,row:0,v:0.01},
        {code:'PB',col:2,row:1,v:0.14},{code:'HP',col:3,row:1,v:0.04},{code:'UK',col:4,row:1,v:0.11},{code:'SK',col:6,row:1,v:0.00},{code:'AR',col:8,row:1,v:0.02},
        {code:'HR',col:2,row:2,v:0.21},{code:'DL',col:3,row:2,v:0.07},{code:'UP',col:4,row:2,v:5.39},{code:'BR',col:5,row:2,v:4.22},{code:'ML',col:6,row:2,v:0.09},{code:'AS',col:7,row:2,v:0.68},{code:'NL',col:8,row:2,v:0.03},
        {code:'RJ',col:1,row:3,v:1.22},{code:'MP',col:3,row:3,v:1.75},{code:'CG',col:4,row:3,v:0.47},{code:'JH',col:5,row:3,v:1.12},{code:'WB',col:6,row:3,v:1.17},{code:'TR',col:7,row:3,v:0.05},{code:'MN',col:8,row:3,v:0.03},{code:'MZ',col:9,row:3,v:0.01},
        {code:'GJ',col:0,row:4,v:0.82},{code:'MH',col:2,row:4,v:0.97},{code:'TS',col:4,row:4,v:0.22},{code:'OD',col:5,row:4,v:0.72},
        {code:'GA',col:1,row:5,v:0.01},{code:'KA',col:2,row:5,v:0.38},{code:'AP',col:4,row:5,v:0.32},
        {code:'KL',col:2,row:6,v:0.02},{code:'TN',col:3,row:6,v:0.17}
      ] });

    dorling('c-seats',
      { k: 9.2, min: 16.7, max: 27.4, lowColor: '#fde68a', highColor: '#9f1239',
        minLabel: '16.7 lakh', maxLabel: '27.4 lakh', legend: 'people per MP →',
        nodes: [
          {code:'JK',x:28,y:3,  size:1.25, v:25.0},{code:'HP',x:34,y:10, size:0.69, v:17.2},
          {code:'PB',x:27,y:12, size:2.77, v:21.3},{code:'UK',x:39,y:14, size:1.01, v:20.2},
          {code:'HR',x:31,y:17, size:2.54, v:25.4},{code:'DL',x:36,y:19, size:1.68, v:24.0},
          {code:'RJ',x:19,y:25, size:6.85, v:27.4},{code:'UP',x:44,y:24, size:19.98,v:25.0},
          {code:'BR',x:61,y:28, size:10.41,v:26.0},{code:'AS',x:74,y:24, size:3.12, v:22.3},
          {code:'WB',x:68,y:37, size:9.13, v:21.7},{code:'JH',x:58,y:36, size:3.30, v:23.6},
          {code:'GJ',x:11,y:39, size:6.04, v:23.2},{code:'MP',x:33,y:36, size:7.26, v:25.0},
          {code:'CG',x:47,y:43, size:2.55, v:23.2},{code:'OD',x:58,y:46, size:4.20, v:20.0},
          {code:'MH',x:24,y:50, size:11.24,v:23.4},{code:'TS',x:36,y:57, size:3.51, v:20.6},
          {code:'AP',x:42,y:65, size:4.94, v:19.8},{code:'KA',x:26,y:66, size:6.11, v:21.8},
          {code:'TN',x:36,y:79, size:7.21, v:18.5},{code:'KL',x:25,y:80, size:3.34, v:16.7}
        ] });

    tilegram('c-tilegram',
      { legendTitle: 'by zone', unitLabel: '1 hex ≈ 1 crore',
        zones: [
          { id:'N',  name:'North',      color:'#4f46e5' },
          { id:'E',  name:'East',       color:'#e11d48' },
          { id:'S',  name:'South',      color:'#16a34a' },
          { id:'W',  name:'West',       color:'#0d9488' },
          { id:'C',  name:'Central',    color:'#f97316' },
          { id:'NE', name:'North-East', color:'#a855f7' }
        ],
        groups: [
          { s:'JK', z:'N',  t:'6,0' },
          { s:'HP', z:'N',  t:'6,1' },
          { s:'PB', z:'N',  t:'5,1 4,2 5,2' },
          { s:'UK', z:'N',  t:'7,1' },
          { s:'HR', z:'N',  t:'6,2 4,3 5,3' },
          { s:'DL', z:'N',  t:'6,3 5,4' },
          { s:'RJ', z:'N',  t:'2,3 3,3 2,4 3,4 4,4 2,5 3,5' },
          { s:'UP', z:'N',  t:'7,2 8,2 9,2 7,3 8,3 9,3 6,4 7,4 8,4 9,4 4,5 5,5 6,5 7,5 8,5 6,6 7,6 8,6 6,7 7,7' },
          { s:'BR', z:'E',  t:'10,3 10,4 11,4 9,5 10,5 9,6 10,6 11,6 8,7 9,7' },
          { s:'AS', z:'NE', t:'11,2 12,2 11,3' },
          { s:'NE', z:'NE', t:'12,3' },
          { s:'GJ', z:'W',  t:'1,6 2,6 1,7 2,7 1,8 2,8' },
          { s:'MP', z:'C',  t:'3,6 4,6 5,6 3,7 4,7 5,7 4,8' },
          { s:'WB', z:'E',  t:'11,5 12,6 10,7 11,7 12,7 10,8 11,8 10,9 11,9' },
          { s:'JH', z:'E',  t:'7,8 8,8 9,8' },
          { s:'CG', z:'C',  t:'5,8 6,8 5,9' },
          { s:'OD', z:'E',  t:'6,9 7,9 8,9 9,9' },
          { s:'MH', z:'W',  t:'3,8 2,9 3,9 4,9 2,10 3,10 4,10 2,11 3,11 4,11 3,12' },
          { s:'TS', z:'S',  t:'5,10 6,10 5,11 6,11' },
          { s:'AP', z:'S',  t:'7,10 8,10 7,11 8,11 7,12' },
          { s:'KA', z:'S',  t:'4,12 5,12 6,12 4,13 5,13 4,14' },
          { s:'TN', z:'S',  t:'6,13 7,13 5,14 6,14 7,14 4,15 5,15' },
          { s:'KL', z:'S',  t:'3,13 3,14 3,15' },
          { s:'UT', z:'W',  t:'2,12' }
        ] });

    ethicChart('c-ethic');

    bumpChart('c-bump',
      { years: [1990, 2010, 2023, 2050], rankMax: 10, series: [
        { name: 'India',      color: COL.teal,   ranks: [2, 2, 1, 1] },
        { name: 'China',      color: COL.blue,   ranks: [1, 1, 2, 2] },
        { name: 'Nigeria',    color: COL.green,  ranks: [10, 7, 6, 3] },
        { name: 'United States', color: COL.red, ranks: [3, 3, 3, 4] },
        { name: 'Pakistan',   color: COL.amber,  ranks: [8, 6, 5, 5] },
        { name: 'Indonesia',  color: COL.purple, ranks: [4, 4, 4, 6] }
      ] });

    radialArea('c-monsoon',
      { labels: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        values: [17, 21, 25, 31, 62, 165, 286, 259, 175, 82, 32, 13],
        max: 300, rings: [100, 200, 300], color: COL.blue, hot: COL.teal,
        highlight: [5, 6, 7, 8],
        center: { big: '~75%', small: 'Jun–Sep' } });

    bubbleChart('c-gapminder',
      { xMin: 2200, xMax: 90000, yMin: 50, yMax: 86,
        xticks: [2500, 5000, 10000, 20000, 50000], yticks: [55, 60, 65, 70, 75, 80, 85],
        xlabel: 'GDP per person (PPP $, log)', ylabel: 'life expectancy (yrs)',
        legend: [ { name: 'South Asia', color: COL.teal }, { name: 'East Asia', color: COL.blue },
                  { name: 'SE Asia', color: COL.purple }, { name: 'Africa', color: COL.amber },
                  { name: 'Americas', color: COL.red }, { name: 'Europe', color: COL.green } ],
        points: [
          { x: 9207,  y: 71.7, pop: 1425, color: COL.teal,   label: 'India' },
          { x: 23032, y: 78.2, pop: 1412, color: COL.blue,   label: 'China' },
          { x: 77861, y: 77.4, pop: 334,  color: COL.red,    note: 'USA' },
          { x: 8305,  y: 54.1, pop: 223,  color: COL.amber,  note: 'Nigeria' },
          { x: 19877, y: 74.9, pop: 210,  color: COL.red },
          { x: 47192, y: 84.0, pop: 125,  color: COL.blue,   note: 'Japan' },
          { x: 69049, y: 80.6, pop: 83,   color: COL.green,  note: 'Germany' },
          { x: 8451,  y: 74.3, pop: 169,  color: COL.teal },
          { x: 14285, y: 70.9, pop: 279,  color: COL.purple, note: 'Indonesia' },
          { x: 2845,  y: 66.9, pop: 125,  color: COL.amber,  note: 'Ethiopia' },
          { x: 14749, y: 65.5, pop: 62,   color: COL.amber },
          { x: 13905, y: 74.5, pop: 100,  color: COL.purple }
        ] });

    ladder('f-ladder');
    resultsChain('f-toc');
    trapLoop('f-trap');
    venn('f-venn');
    iceberg('f-iceberg');
    makeYourOwn('f-make');
  }

  /* ============================================================
     MASTERS' WING — recreated public-domain classics (drawn once)
     ============================================================ */
  function el(name, attrs) { var n = document.createElementNS(NS, name); for (var k in attrs) n.setAttribute(k, attrs[k]); return n; }
  function polar(cx, cy, r, deg) { var a = (deg - 90) * Math.PI / 180; return [cx + r * Math.cos(a), cy + r * Math.sin(a)]; }
  function wedgePath(cx, cy, r, a0, a1) {
    var p0 = polar(cx, cy, r, a0), p1 = polar(cx, cy, r, a1);
    var large = (a1 - a0) > 180 ? 1 : 0;
    return "M" + cx + "," + cy + " L" + p0[0].toFixed(1) + "," + p0[1].toFixed(1) +
           " A" + r + "," + r + " 0 " + large + " 1 " + p1[0].toFixed(1) + "," + p1[1].toFixed(1) + " Z";
  }

  function plateTokens() {
    var dk = document.documentElement.getAttribute('data-theme') === 'dark';
    return { dk: dk, ink: dk ? '#e8ecf8' : '#1a2236', mut: dk ? '#9aa6c8' : '#5b6678', grid: dk ? 'rgba(255,255,255,0.07)' : 'rgba(20,30,60,0.08)', sep: dk ? '#0e1326' : '#cdbfa3' };
  }
  function drawRose() {
    var svg = document.getElementById('viz-rose'); if (!svg) return;
    clear(svg); var T = plateTokens();
    var cx = 200, cy = 165, n = 12, step = 360 / n;
    var disease = [22, 38, 95, 130, 175, 240, 205, 168, 110, 60, 34, 26];
    var wounds  = [3, 5, 8, 12, 16, 22, 18, 14, 10, 7, 5, 4];
    var other   = [4, 6, 9, 11, 13, 15, 14, 12, 9, 6, 5, 4];
    var maxR = 130, maxV = Math.max.apply(null, disease.map(function(d,i){return d+wounds[i]+other[i];}));
    var scale = maxR / Math.sqrt(maxV);
    function ring(values, fill, op) {
      for (var i = 0; i < n; i++) {
        var r = Math.sqrt(values[i]) * scale;
        var path = el('path', { d: wedgePath(cx, cy, r, i*step, (i+1)*step), fill: fill, 'fill-opacity': op, stroke: T.sep, 'stroke-width': 0.6 });
        if (!reduced()) { path.style.opacity = 0; path.style.transition = 'opacity 0.5s ease ' + (i*0.04) + 's'; }
        svg.appendChild(path);
        if (!reduced()) requestAnimationFrame(function(p){ return function(){ p.style.opacity = 1; }; }(path));
      }
    }
    ring(disease.map(function(d,i){return d+wounds[i]+other[i];}), '#3b6fb0', 0.95);
    ring(wounds.map(function(w,i){return w+other[i];}), '#c0392b', 0.95);
    ring(other, T.dk ? '#cbd3e6' : '#2b3450', 0.95);
    svg.appendChild(el('circle', { cx: cx, cy: cy, r: 2, fill: T.ink }));
    var leg = [['#3b6fb0','Preventable disease'], ['#c0392b','Wounds in battle'], [T.dk ? '#cbd3e6' : '#2b3450','Other causes']];
    leg.forEach(function(item, i) {
      svg.appendChild(el('rect', { x: 16, y: 270 + i*15, width: 11, height: 11, rx: 2, fill: item[0] }));
      var t = el('text', { x: 32, y: 279 + i*15, fill: T.mut, 'font-size': 10, 'font-family': 'JetBrains Mono, monospace' }); t.textContent = item[1]; svg.appendChild(t);
    });
  }

  function drawMinard() {
    var svg = document.getElementById('viz-minard'); if (!svg) return;
    clear(svg); var T = plateTokens();
    var advance = [[40,422],[105,400],[165,233],[225,175],[300,127]];
    var retreat = [[300,100],[235,50],[170,28],[110,20],[55,12],[28,4]];
    var midY = 118, k = 0.12;
    function band(pts, fill) {
      var top = "M", bot = "";
      pts.forEach(function(p, i) { var t = Math.max(2, p[1]*k); top += (i?" L":"") + p[0] + "," + (midY - t/2).toFixed(1); });
      for (var i = pts.length - 1; i >= 0; i--) { var t = Math.max(2, pts[i][1]*k); bot += " L" + pts[i][0] + "," + (midY + t/2).toFixed(1); }
      var path = el('path', { d: top + bot + " Z", fill: fill, stroke: T.sep, 'stroke-width': 0.5 });
      if (!reduced()) { path.style.opacity = 0; path.style.transition = 'opacity 0.9s ease'; }
      svg.appendChild(path);
      if (!reduced()) requestAnimationFrame(function(){ path.style.opacity = 1; });
    }
    band(advance, T.dk ? '#d9b38c' : '#b07a30'); band(retreat, T.dk ? '#566' : '#2b3450');
    svg.appendChild(el('circle', { cx: 300, cy: midY, r: 3.5, fill: '#c0392b' }));
    var mono = 'JetBrains Mono, monospace';
    var mt = el('text', { x: 300, y: 84, fill: T.ink, 'font-size': 11, 'font-family': mono, 'text-anchor': 'middle' }); mt.textContent = 'Moscow'; svg.appendChild(mt);
    var st = el('text', { x: 36, y: 72, fill: T.ink, 'font-size': 11, 'font-family': mono }); st.textContent = '422,000 set out'; svg.appendChild(st);
    var et = el('text', { x: 24, y: 170, fill: T.mut, 'font-size': 11, 'font-family': mono }); et.textContent = '≈10,000 returned'; svg.appendChild(et);
    var temps = [[300,206],[235,218],[170,238],[110,256],[55,268],[28,276]];
    var d = "M"; temps.forEach(function(p,i){ d += (i?" L":"") + p[0] + "," + p[1]; });
    var tcol = T.dk ? '#8fb4ff' : '#3b6fb0';
    svg.appendChild(el('path', { d: d, fill: 'none', stroke: tcol, 'stroke-width': 1.6, 'stroke-dasharray': '3,3' }));
    var tlab = el('text', { x: 24, y: 298, fill: tcol, 'font-size': 9.5, 'font-family': mono }); tlab.textContent = 'temperature on the retreat, to −30°'; svg.appendChild(tlab);
  }

  function drawSnow() {
    var svg = document.getElementById('viz-snow'); if (!svg) return;
    clear(svg); var T = plateTokens();
    for (var gx = 40; gx <= 360; gx += 40) svg.appendChild(el('line', { x1: gx, y1: 46, x2: gx, y2: 290, stroke: T.grid, 'stroke-width': 1 }));
    for (var gy = 60; gy <= 280; gy += 40) svg.appendChild(el('line', { x1: 30, y1: gy, x2: 370, y2: gy, stroke: T.grid, 'stroke-width': 1 }));
    var pump = [200, 158], seed = 7;
    function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
    function gauss() { return (rnd() + rnd() + rnd() + rnd() - 2) / 2; }
    for (var i = 0; i < 90; i++) {
      var x = Math.max(34, Math.min(366, pump[0] + gauss() * 70)), y = Math.max(50, Math.min(286, pump[1] + gauss() * 52));
      var dot = el('rect', { x: x.toFixed(1), y: y.toFixed(1), width: 3.6, height: 3.6, fill: T.dk ? '#dfe5f2' : '#1a1f33', stroke: 'none' });
      if (!reduced()) { dot.style.opacity = 0; dot.style.transition = 'opacity 0.4s ease ' + (i*0.012) + 's'; }
      svg.appendChild(dot);
      if (!reduced()) requestAnimationFrame(function(d){ return function(){ d.style.opacity = 1; }; }(dot));
    }
    [[80,84],[330,100],[300,252],[92,246]].forEach(function(p) { svg.appendChild(el('circle', { cx: p[0], cy: p[1], r: 5, fill: 'none', stroke: T.mut, 'stroke-width': 1.5 })); });
    svg.appendChild(el('circle', { cx: pump[0], cy: pump[1], r: 9, fill: 'none', stroke: '#d6336c', 'stroke-width': 2 }));
    svg.appendChild(el('circle', { cx: pump[0], cy: pump[1], r: 4, fill: '#d6336c' }));
    // legend (kept clear of the cluster)
    svg.appendChild(el('circle', { cx: 24, cy: 26, r: 4, fill: '#d6336c' }));
    var lab = el('text', { x: 34, y: 30, fill: T.mut, 'font-size': 10.5, 'font-family': 'JetBrains Mono, monospace' }); lab.textContent = 'the Broad Street pump · each mark is a death'; svg.appendChild(lab);
  }

  function drawDuBois() {
    var svg = document.getElementById('viz-dubois'); if (!svg) return;
    clear(svg);
    var cx = 200, cy = 160, palette = ['#c1272d', '#e8b22a', '#21563f', '#1b1b3a', '#d98e2b', '#7a5230'], segs = 30, base = 6, turns = 3.4, prev = null;
    for (var i = 0; i < segs; i++) {
      var ang = (i / segs) * turns * 360, rad = base + i * 4.6, p = polar(cx, cy, rad, ang);
      if (prev) {
        var seg = el('line', { x1: prev[0].toFixed(1), y1: prev[1].toFixed(1), x2: p[0].toFixed(1), y2: p[1].toFixed(1), stroke: palette[i % palette.length], 'stroke-width': 7, 'stroke-linecap': 'round' });
        if (!reduced()) { seg.style.opacity = 0; seg.style.transition = 'opacity 0.4s ease ' + (i*0.03) + 's'; }
        svg.appendChild(seg);
        if (!reduced()) requestAnimationFrame(function(s){ return function(){ s.style.opacity = 1; }; }(seg));
      }
      prev = p;
    }
    svg.appendChild(el('circle', { cx: cx, cy: cy, r: 5, fill: '#1b1b3a' }));
    var t1 = el('text', { x: 200, y: 296, fill: '#1b1b3a', 'font-size': 12, 'font-family': 'Inter, sans-serif', 'font-weight': 700, 'text-anchor': 'middle', 'letter-spacing': 2 }); t1.textContent = 'VALUE OF PROPERTY OWNED'; svg.appendChild(t1);
    var t2 = el('text', { x: 200, y: 312, fill: '#7a5230', 'font-size': 9.5, 'font-family': 'JetBrains Mono, monospace', 'text-anchor': 'middle' }); t2.textContent = 'in the style of W. E. B. Du Bois, 1900'; svg.appendChild(t2);
  }

  /* ============================================================
     THE GREATS — curated gallery of modern masterworks (links out)
     ============================================================ */
  var VIZ = [
    { theme:'poverty', tag:'Poverty & Inequality', title:'The Wealth & Health of Nations', who:'Hans Rosling · Gapminder', year:'2006', g:['#48bb78','#4facfe'], desc:'The animated bubble chart that made 200 years of global development legible in four minutes. Income vs. life expectancy, every country, every year.', url:'https://www.gapminder.org/tools/' },
    { theme:'poverty', tag:'Poverty & Inequality', title:'Dollar Street', who:'Anna Rosling Rönnlund · Gapminder', year:'2016', g:['#ed8936','#f6ad55'], desc:'Homes photographed across the world, sorted by income. It turns an abstract poverty line into toothbrushes, beds and front doors.', url:'https://www.gapminder.org/dollar-street' },
    { theme:'health', tag:'Public Health', title:'Global Child Mortality', who:'Max Roser · Our World in Data', year:'2013–', g:['#3182ce','#4facfe'], desc:'The single most important — and most hopeful — line in development: the share of children who die before age five, falling across two centuries.', url:'https://ourworldindata.org/child-mortality' },
    { theme:'race', tag:'Race & Equity', title:'The Data Portraits of Black America', who:'W. E. B. Du Bois', year:'1900', g:['#c1272d','#e8b22a'], desc:'The hand-drawn originals behind our recreation — radical, modernist infographics made to confront the 1900 Paris Exposition with the truth of Black life.', url:'https://www.loc.gov/pictures/collection/anedub/' },
    { theme:'justice', tag:'Justice & Rights', title:'U.S. Gun Deaths — Stolen Years', who:'Periscopic', year:'2013', g:['#e53e3e','#fc8181'], desc:'Each life arcs across the screen, then is cut short — the grey arc showing the years that person might have lived. Data as elegy.', url:'https://guns.periscopic.com/' },
    { theme:'migration', tag:'Migration', title:'The Refugee Project', who:'Hyperakt & Ekene Ijeoma', year:'2014', g:['#805ad5','#f093fb'], desc:'Every refugee movement since 1975, mapped and narrated year by year. Migration as a global, historical rhythm rather than a headline.', url:'https://www.therefugeeproject.org/' },
    { theme:'climate', tag:'Climate', title:'The Carbon Map', who:'Duncan Clark & Robin Houston · Kiln', year:'2013', g:['#38a169','#48bb78'], desc:'The world re-drawn by who emits carbon and who suffers for it — two morphing cartograms that hold the central injustice of climate change in one frame.', url:'https://www.carbonmap.org/' },
    { theme:'climate', tag:'Climate', title:'Warming Stripes', who:'Ed Hawkins', year:'2018', g:['#3182ce','#e53e3e'], desc:'No axes, no numbers — just a barcode of blue-to-red years. The most-shared climate graphic ever made, because anyone can read it instantly.', url:'https://showyourstripes.info/' },
    { theme:'health', tag:'Public Health', title:'How the Virus Got Out', who:'The New York Times', year:'2020', g:['#d53f8c','#f093fb'], desc:'A scrollytelling map of the early pandemic — how a local outbreak became a planet-wide event before borders ever closed.', url:'https://www.nytimes.com/interactive/2020/03/22/world/coronavirus-spread.html' },
    { theme:'gender', tag:'Gender', title:'Women’s Pockets, Quantified', who:'Jan Diehm & Amber Thomas · The Pudding', year:'2018', g:['#d53f8c','#f5a8ff'], desc:'They measured the pockets on 80 pairs of jeans. A small, witty, rigorous proof of a structural gender inequity hiding in plain sight.', url:'https://pudding.cool/2018/08/pockets/' },
    { theme:'education', tag:'Education', title:'Segregation Now', who:'ProPublica', year:'2014', g:['#d69e2e','#ed8936'], desc:'How American schools quietly re-segregated, told through one town and decades of enrolment data. Investigative journalism as data narrative.', url:'https://projects.propublica.org/segregation-now/' },
    { theme:'india', tag:'India & South Asia', title:'People’s Archive of Rural India', who:'PARI', year:'2014–', g:['#dd6b20','#f6ad55'], desc:'A living multimedia archive of rural India — maps, faces and livelihoods that national statistics flatten into a single average.', url:'https://ruralindiaonline.org/' },
    { theme:'india', tag:'India & South Asia', title:'IndiaSpend', who:'IndiaSpend', year:'2011–', g:['#3182ce','#667eea'], desc:'India’s pioneering data-journalism newsroom — health, gender, jobs and budgets charted from the public record, story after story.', url:'https://www.indiaspend.com/' },
    { theme:'climate', tag:'Climate', title:'2°C: Beyond the Limit', who:'The Washington Post', year:'2019', g:['#e53e3e','#ed8936'], desc:'A Pulitzer-winning series mapping the places already past 2°C of warming. Global abstraction made local and undeniable.', url:'https://www.washingtonpost.com/graphics/2019/national/climate-environment/climate-change-world/' },
    { theme:'poverty', tag:'Poverty & Inequality', title:'Information is Beautiful', who:'David McCandless', year:'2009–', g:['#667eea','#4facfe'], desc:'The studio that made data visualization mainstream — endlessly studied for how colour, scale and wit turn numbers into something you actually feel.', url:'https://informationisbeautiful.net/' },
    { theme:'india', tag:'India & South Asia', title:'Reuters Graphics', who:'Reuters', year:'ongoing', g:['#dd6b20','#e53e3e'], desc:'Award-winning visual investigations, often on South Asia — migrant labour, heat, elections. A reference standard for newsroom dataviz craft.', url:'https://www.reuters.com/graphics/' },
    { theme:'work', tag:'Work & Technology', title:'Which Jobs Are Most Exposed to AI', who:'The Washington Post · GovAI & Brookings', year:'2026', g:['#0EA5E9','#ed8936'], desc:'Every US occupation as a bubble — AI exposure across, adaptability up, sized by workforce. Search your own job to see whether AI threatens it, and whether you could pivot if it did. The quiet finding: many of the most exposed are also the best placed to move.', url:'https://www.washingtonpost.com/technology/interactive/2026/jobs-most-affected-ai-automation/' },
    { theme:'poverty', tag:'Poverty & Inequality', title:'American Wealth Inequality', who:'PerThirtySix', year:'2025', g:['#e11d48','#f59e0b'], desc:'Horizontal space encodes wealth, stick figures encode people — so the bottom 50% become a dense crowd holding almost nothing while the top 0.1% occupy a vast near-empty hall. The clearest single picture of who owns America, built from Federal Reserve data. The model for our own “Who owns India”.', url:'https://perthirtysix.com/tool/american-wealth-inequality' },
    { theme:'method', tag:'How Numbers Mislead', title:'A Compendium of Statistical Illusions', who:'unspurious', year:'2026–', g:['#475569','#f59e0b'], desc:'Simpson’s paradox, Berkson’s paradox, the base-rate fallacy — twenty-eight ways that arithmetic which is entirely correct walks a careful reader to the wrong conclusion. Nothing here is faked; the error hides in the silent step from number to interpretation. Each entry opens with a figure you can poke until the illusion happens in front of you, and its “Lie With This Chart” tool is the hands-on counterpart to our own note on honest axes.', url:'https://unspurious.com/' }
  ];

  function buildCards() {
    var host = document.getElementById('cards'); if (!host) return;
    VIZ.forEach(function(v) {
      var a = document.createElement('a');
      a.className = 'viz-card'; a.href = v.url; a.target = '_blank'; a.rel = 'noopener'; a.setAttribute('data-theme-cat', v.theme);
      var sw = document.createElement('div'); sw.className = 'swatch'; sw.style.background = 'linear-gradient(135deg, ' + v.g[0] + ', ' + v.g[1] + ')';
      var body = document.createElement('div'); body.className = 'vbody';
      var tag = document.createElement('span'); tag.className = 'theme-tag'; tag.textContent = v.tag;
      var h = document.createElement('h3'); h.textContent = v.title;
      var meta = document.createElement('div'); meta.className = 'meta'; meta.textContent = v.who + ' · ' + v.year;
      var p = document.createElement('p'); p.textContent = v.desc;
      var view = document.createElement('span'); view.className = 'view'; view.textContent = 'View the original →';
      body.appendChild(tag); body.appendChild(h); body.appendChild(meta); body.appendChild(p); body.appendChild(view);
      a.appendChild(sw); a.appendChild(body); host.appendChild(a);
    });
  }

  function wireFilters() {
    var chips = document.querySelectorAll('.filter-chip');
    chips.forEach(function(chip) {
      chip.addEventListener('click', function() {
        chips.forEach(function(c){ c.classList.remove('active'); });
        chip.classList.add('active');
        var f = chip.getAttribute('data-filter');
        document.querySelectorAll('.viz-card').forEach(function(card) {
          card.classList.toggle('hidden', !(f === 'all' || card.getAttribute('data-theme-cat') === f));
        });
      });
    });
  }

  /* ---------- reveal cards + hero dots ---------- */
  function reveal() {
    var cards = document.querySelectorAll('[data-card], [data-plate]');
    if (!('IntersectionObserver' in window)) { cards.forEach(function(c){ c.classList.add('in'); }); return; }
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.15 });
    cards.forEach(function(c){ io.observe(c); });
  }
  function heroDots() {
    var host = document.getElementById('heroDots'); if (!host) return;
    for (var i = 0; i < 24; i++) {
      var s = document.createElement('span');
      var size = (Math.random() * 4 + 1.5).toFixed(1);
      s.style.width = size + 'px'; s.style.height = size + 'px';
      s.style.left = (Math.random() * 100).toFixed(1) + '%';
      s.style.top = (Math.random() * 100).toFixed(1) + '%';
      s.style.animationDelay = (Math.random() * 9).toFixed(1) + 's';
      s.style.opacity = (Math.random() * 0.6 + 0.2).toFixed(2);
      host.appendChild(s);
    }
  }

  function drawMasters(){ drawRose(); drawMinard(); drawSnow(); drawDuBois(); }

  var ORDER = ['c-bump','c-gapminder','c-monsoon','c-gender','c-wealth','c-caste','c-co2','c-energy','c-nfhs','c-upset-deprivation','c-upset-backwards','c-forest','c-decline','c-transition','c-migration','c-where','c-ghg','c-ghg3','c-rupee','c-waffle','c-stream','c-pyramid','c-states','c-poor-dots','c-seats','c-tilegram','c-poverty','c-u5mr','c-flfp','c-pipeline','c-climate','c-le','c-solar','c-urban','c-gdp','c-literacy','c-womenparl'];
  var DETAILS = {
    'c-bump': { tag:'Population', title:'The new giants',
      takeaway:"India passed China to become the world's most populous country in 2023. Look further out and the order keeps shifting — the UN projects Nigeria to climb past the United States by 2050.",
      source:"UN World Population Prospects 2024 — country population rankings for 1990, 2010, 2023 and the 2050 projection.",
      why:"A bump chart is built for ranks that change over time: each line is one country, and what you read is the crossings — who overtakes whom, and when — not the raw millions.",
      how:"Each country's global population rank is plotted at four dates and joined into a line; rank 1 is at the top. Ranks are from the UN's 2024 revision, with 2050 a projection.",
      look:"The India–China cross around 2023, and Nigeria's steep climb from tenth toward third." },
    'c-gapminder': { tag:'Development', title:'The wealth and health of nations',
      takeaway:"Richer countries tend to live longer, but the link bends and breaks: India and Bangladesh reach lives nearly as long as far richer places, while oil-poor Nigeria and Ethiopia sit low on both.",
      source:"World Bank Open Data, 2022 — GDP per capita (PPP, current international $), life expectancy at birth, and total population, pulled from the World Bank API.",
      why:"A bubble chart carries four variables at once — wealth on a log x-axis, health on the y, population as size, region as colour — so a whole world of countries fits in one frame. It's the shape Hans Rosling made famous.",
      how:"Each bubble is a country in 2022, placed by GDP per person (log scale) and life expectancy, sized by population and coloured by region. Drawn in SVG from World Bank figures.",
      look:"How steeply life expectancy rises with the first few thousand dollars, then flattens — and how India sits well above its income on the health axis." },
    'c-monsoon': { tag:'Climate', title:'The shape of the monsoon',
      takeaway:"India's rain is not spread across the year — it arrives in a burst. About three-quarters of it falls in the four monsoon months, June to September.",
      source:"India Meteorological Department — long-period average (normal) monthly rainfall, all-India (mm). Figures approximate.",
      why:"Wrapping the twelve months around a circle makes the year's rhythm a shape you can see: a lopsided blob straining toward the monsoon months, not the flat line a row of bars would suggest.",
      how:"Each month sits at a clock position; the distance from the centre is that month's normal rainfall. The four monsoon months are marked; rings show 100, 200 and 300 mm.",
      look:"How the whole form bulges toward July and August, and how thin the dry winter months are." },
    'c-migration': { tag:'Migration', title:'Migration is a web',
      takeaway:"People move in every direction between world regions — not just South to North. The biggest single cross-region pull is into Northern America.",
      source:"UN DESA, International Migrant Stock 2020 — between-region flows, regional aggregates (approximate, millions). Within-region migration (most of the total) is left out for clarity.",
      why:"A chord diagram is built for flows between a set of places: each region is an arc, each ribbon a flow, sized by how many people moved. It shows the whole web at once, in both directions.",
      how:"Region arcs sized by total cross-region movement, ribbons sized by each pair's flow. Drawn in SVG from the UN DESA regional matrix; figures are rounded aggregates.",
      look:"How thick each ribbon is, and that most regions both send and receive — migration runs both ways." },
    'c-ghg3': { tag:'Climate', title:'India’s emissions, in full',
      takeaway:"Trace each sector to its sub-sectors to the gas: power and industry are the CO₂ engine; livestock and rice make most of the methane; soils make the nitrous oxide.",
      source:"India's Fourth Biennial Update Report to the UNFCCC (BUR4, 2020), excl. land use. Sub-sector and gas split approximate (MtCO₂e).",
      why:"A three-stage Sankey follows emissions across two breakdowns at once — sector, then sub-sector, then gas — so you can see, say, that 'Energy' is really mostly 'Power', and that 'Power' is almost pure CO₂.",
      how:"Three columns of nodes sized by emissions; ribbons keep their thickness end to end, coloured by their origin sector. Built from India's BUR4 totals.",
      look:"Follow the grey Energy band: it fans into Power, Industry, Transport and Buildings, and almost all of it lands in CO₂." },
    'c-ghg': { tag:'Climate', title:'India’s greenhouse gases',
      takeaway:"Energy dominates India's emissions and is almost all CO₂; agriculture is the big source of methane and nitrous oxide.",
      source:"India's Fourth Biennial Update Report to the UNFCCC (BUR4, 2020), excluding land use. Sector-by-gas split approximate.",
      why:"A Sankey is built for tracing where something goes — here, emissions flowing from the sector that produces them to the gas they're made of. You see both breakdowns, and how they connect, in one picture.",
      how:"Left nodes are emitting sectors, right nodes are gases; each ribbon's thickness is that sector's emissions of that gas, in MtCO₂e. Drawn from India's BUR4 totals.",
      look:"How Energy pours almost entirely into CO₂, while Agriculture splits into methane and nitrous oxide." },
    'c-where': { tag:'Population & Income', title:'Where the world lives',
      takeaway:"Most of humanity is in Asia and in the lower- and upper-middle income bands; high income is a small slice, concentrated in a few regions.",
      source:"World Bank — population by region and by income classification, 2023 (cross-tab approximate; marginals from World Bank).",
      why:"A Sankey shows how one split maps onto another — here, region to income band — with band thickness as the number of people. It carries two breakdowns and their overlap in one picture.",
      how:"Left nodes are regions, right nodes income bands; each ribbon's thickness is that region-and-band's population. Region totals and income totals are from the World Bank; the cell split is estimated to fit them.",
      look:"How much of the world flows into 'lower-middle', and how thin the 'high income' band is." },
    'c-rupee': { tag:'Public Finance', title:'Where the rupee comes from, and where it goes',
      takeaway:"Nearly a quarter of every rupee the Union government spends is borrowed — and a fifth of what it spends goes straight back out as interest on past borrowing. Of the rest, the single largest share is not a scheme at all: it is the states' constitutional share of taxes.",
      source:"Union Budget 2025–26, 'Budget at a Glance' — the government's own paise-in-the-rupee breakdown of receipts and expenditure. Figures are whole paise and each side sums to 100.",
      why:"A Sankey drawn through a single hub is the clearest way to read a budget: every source narrows into one rupee, then that rupee fans out into what it pays for. Two lists that would otherwise sit in separate tables become one continuous quantity, and the borrowing-to-interest loop is visible in a way a pie chart can never make it.",
      how:"Left nodes are receipts, right nodes are spending heads, each sized to its paise share; the centre bar is the whole rupee. Ribbon thickness is the paise figure, so both sides balance exactly at 100.",
      look:"Compare the red band on the left (borrowings, 24p) with the red band on the right (interest, 20p) — most of what the government borrows this year services what it borrowed in years past." },
    'c-poor-dots': { tag:'Poverty', title:'Where India’s poor actually live',
      takeaway:"Bihar has India's highest poverty rate, but Uttar Pradesh has India's largest number of poor people — about 5.4 crore, more than the population of South Korea. Rates and counts point at different states, and they call for different policies.",
      source:"NITI Aayog National Multidimensional Poverty Index (2023 report, based on NFHS-5, 2019–21) — state headcount ratios applied to projected 2021 state populations. Numbers are approximate; the dots total about 20.6 crore, close to the national MPI figure.",
      why:"A choropleth colours a whole state by a rate, which quietly hides how many people that rate is about. A dot-density map does the opposite: it draws the count. Each dot is a fixed number of people scattered at random inside the state, so crowding — not colour — carries the quantity, and big numbers look big.",
      how:"One dot per 10 lakh (one million) multidimensionally poor people, placed at random inside each state's tile by a fixed seed so the pattern is the same every time it draws. Tiles are equal-sized, so how dark a tile looks is how many poor people live there.",
      look:"How nearly black Uttar Pradesh and Bihar are, and how empty Kerala, Tamil Nadu and the north-east look — then compare with the rate map, 'The geography of a gap', where the ranking is quite different." },
    'c-seats': { tag:'Democracy & Representation', title:'One person, one vote?',
      takeaway:"Lok Sabha seats were frozen at the 1971 census, so the states that grew fastest are now the least represented. A Rajasthan MP speaks for about 27.4 lakh people; a Kerala MP for 16.7 lakh. On these numbers a vote in Kerala carries roughly 1.6 times the weight of one in Rajasthan — and the gap has widened since 2011.",
      source:"Census of India 2011 (state populations) and the current allocation of Lok Sabha seats, frozen by the 42nd Amendment at the 1971 census and extended to 2026 by the 84th. Population per seat is computed from these two.",
      why:"A Dorling cartogram throws away the map's real shapes and draws each state as a circle sized by its people, nudged apart but kept roughly where it belongs. Land area stops competing with population for your attention — which is the whole point when the subject is how many people sit behind each seat.",
      how:"One circle per state, area proportional to its 2011 population, coloured by population per Lok Sabha seat. Circles start at their approximate geographic position and are pushed apart until none overlap, so the layout is readable without being a real map.",
      look:"That the darkest circles — Rajasthan, Bihar, Haryana, Uttar Pradesh, Madhya Pradesh — are mostly northern, and the palest — Kerala, Tamil Nadu, Andhra Pradesh — are mostly southern. That pattern is what the delimitation debate is about." },
    'c-tilegram': { tag:'Population', title:'India, one hexagon at a time',
      takeaway:"Give every crore of Indians one hexagon and the country's real weight appears: 121 hexagons, of which Uttar Pradesh alone claims 20 — more than the whole south's five states put together would need if you removed Tamil Nadu. The North, Central and East zones hold about three in every four hexagons.",
      source:"Census of India 2011 — population by state, one hexagon per crore (10 million), rounded to the nearest crore. The rounding is why the grid comes to 121, India's 2011 population in crore.",
      why:"A hex cartogram gives every state one tile regardless of size; a tilegram gives each state as many tiles as it has people. So the map itself becomes the bar chart — you can count the population of a region by eye, in units, without reading a single axis. It is the form the NPR and FiveThirtyEight election maps made familiar.",
      how:"Each state is a block of hexagons, one per crore of population, laid out on a grid that keeps states roughly in their real positions and next to their real neighbours. Blocks are coloured by zone and the legend counts the hexes in each.",
      look:"The size of the Uttar Pradesh block against everything around it — and how much of the grid the North and East together take up." },
    'c-waffle': { tag:'Access', title:'If India were 100 people',
      takeaway:"Almost everyone has electricity, but far fewer have clean cooking fuel, the internet, or health cover.",
      source:"NFHS-5 (2019–21) for household amenities; Global Findex 2021 for bank accounts.",
      why:"A waffle turns a percentage into a hundred squares, so 'X in 100' is something you can count, not just read. A grid of them compares several access gaps at once.",
      how:"Each block is a 10×10 grid; coloured squares fill from the bottom up to the share who have that thing.",
      look:"How full each grid is — electricity nearly complete, health cover barely two-fifths." },
    'c-stream': { tag:'Population', title:'The world’s shifting weight',
      takeaway:"Asia is still most populous, but Africa is the fastest-growing band — the world's centre of gravity is moving.",
      source:"World Bank — population by region (SP.POP.TOTL), 1960–2023, via the World Bank API.",
      why:"A stream graph stacks each region's population into a flowing band, so you see the total swelling and each region's changing share at once.",
      how:"Bands stacked around a centred baseline, sized by population each year, from the World Bank regional series.",
      look:"How the Africa band widens fastest while Europe and North America stay nearly flat." },
    'c-decline': { tag:'Child Survival', title:'The great decline',
      takeaway:"Across very different countries, under-five deaths fell sharply over thirty years — even Rwanda, after its 1994 spike.",
      source:"UN Inter-agency Group for Child Mortality Estimation / World Bank (SH.DYN.MORT), 1990–2022.",
      why:"Small multiples — the same little chart repeated for each country, on a shared scale — let you compare many trajectories at once without one busy, tangled chart. Tufte's preferred way to show 'the same thing, everywhere'.",
      how:"One mini line per country, all on the same 0–215 axis, pulled directly from the World Bank API. The 1990 and 2022 values are printed on each.",
      look:"Almost every line falls. Rwanda's rises first (the genocide) then drops fastest; Nigeria starts highest and falls least." },
    'c-states': { tag:'Caste & Equity', title:'The geography of a gap',
      takeaway:"Female literacy is highest in the south and the north-east, lowest across the northern 'BIMARU' belt — Kerala 92%, Rajasthan and Bihar barely half.",
      source:"Census of India 2011 — female literacy rate by state.",
      why:"A hex cartogram gives every state the same-sized tile, so big-but-empty states don't shout and small states aren't lost — you read the pattern, not the area. It keeps rough geography without the distortion of a real map.",
      how:"One hexagon per state, placed on a grid that approximates India's layout, shaded by female literacy on a single green scale.",
      look:"The green south and north-east against the paler northern belt." },
    'c-pyramid': { tag:'Population', title:'From pyramid to barrel',
      takeaway:"In 1990 India was a young country with a wide base of children. By 2050 the bulge moves up: far fewer kids, many more older adults.",
      source:"UN World Population Prospects 2024, via PopulationPyramid.net — India by 5-year age band and sex, 1990 and 2050.",
      why:"A population pyramid shows age and sex at once. Overlaying two years — 2050 filled, 1990 as a dashed outline — makes the shift in shape the story, not two charts you have to compare.",
      how:"Bars are each band's share of that year's population (so the two years are comparable despite different totals); men left, women right; the 1990 outline sits over the 2050 bars.",
      look:"The base narrows and the middle and top swell — a society growing older." },
    'c-transition': { tag:'Population', title:'Everyone walks the same road',
      takeaway:"Countries move from many children and short lives toward few children and long lives — the demographic transition — just at different times.",
      source:"World Bank — total fertility rate (SP.DYN.TFRT.IN) and life expectancy (SP.DYN.LE00.IN), 1960–2022.",
      why:"A connected scatterplot traces each country's path through two variables over time, so you see the shape of change, not just two separate trends. The convergence toward the top-left is the story.",
      how:"Each country is a line through its (fertility, life expectancy) points for 1960, 1980, 2000 and 2022, with the latest year marked.",
      look:"Every path heads up and to the left. Korea and China raced; Nigeria is still early on the same road." },
    'c-gender': { tag:'Gender', title:'The same gap, four ways',
      takeaway:"Women have caught up with men in college enrolment, and slightly passed them. In paid work and Parliament, they're still far behind.",
      source:"NFHS-5 (literacy), AISHE 2021–22 (college GER), PLFS 2023–24 (labour force), Lok Sabha 2024 (seats).",
      why:"A dumbbell chart puts two values on one line so the gap between them is the first thing you read. Stacking four indicators lets you compare gaps at a glance — and spot the one place the gap reverses.",
      how:"Drawn in plain SVG: a faint connecting line per row, a dot for each sex, values at the ends. No charting library — just the figures and a little geometry.",
      look:"The length of each grey line is the gap. Look at college, where the women's dot sits to the right of the men's." },
    'c-wealth': { tag:'Wealth & Inequality', title:'Who owns India',
      takeaway:"The richest 1% of Indians own about 40% of the country's wealth — the most concentrated on record. The bottom half own roughly 6%. That same 1% also take 22.6% of all income.",
      source:"World Inequality Lab — Bharti, Chancel, Piketty & Somanchi, 'Income and Wealth Inequality in India, 1922–2023' (2024). Personal wealth shares, 2022–23.",
      why:"Two bars on one scale — the population split by size, total wealth split among the same groups — turn a statistic into a shape. Ribbons link each group across the two, so you watch the bottom half's wide band of people pinch to a sliver of wealth, and the top 1% do the opposite.",
      how:"The top bar divides the population into four groups; the bottom bar divides total personal wealth among the same four. Segment widths are the exact shares, and each ribbon connects one group across the two bars.",
      look:"How the Top 1% block barely registers in 'People' yet dominates 'Wealth' — and how thin the bottom half's wealth band is." },
    'c-caste': { tag:'Caste & Equity', title:'Poverty is not caste-blind',
      takeaway:"A Scheduled Tribe household is about three times as likely to be poor as an 'Other' household.",
      source:"NFHS-4 (2015–16), multidimensional poverty headcount by social group. National headcount has since fallen to about 15% (NFHS-5).",
      why:"A bar chart is the honest choice for comparing a few categories: length is easy to judge. A single dark-to-light red scale reinforces the ranking without adding a second variable.",
      how:"Horizontal bars from zero, with a dashed line at the national average so each group reads as above or below it.",
      look:"How far each bar sits past the dashed national line. The drop from Scheduled Tribes to 'Others' is the point." },
    'c-co2': { tag:'Climate', title:'Whose carbon?',
      takeaway:"Most countries emit little, and India sits near the bottom. The average person in Qatar emits more than 20 times an Indian.",
      source:"EDGAR (European Commission / JRC), per-capita CO₂ emissions, 2023.",
      why:"A beeswarm shows every country as a dot on one axis, so you see the whole spread — the dense low-emitting cluster and the lonely outliers — instead of a single average.",
      how:"Each country is placed at its value, then nudged up just enough to avoid overlapping its neighbours. India is highlighted; a dashed line marks the world average.",
      look:"How crowded the left side is, and how far Qatar sits alone on the right." },
    'c-energy': { tag:'Energy', title:'How India keeps the lights on',
      takeaway:"About three-quarters of India's electricity still comes from coal; solar and wind together are about 12%.",
      source:"Ember / Central Electricity Authority — share of electricity generation, 2024.",
      why:"For a part-to-whole split, a ring works when one slice dominates and you mainly want the headline share — here, how much is still fossil. The centre carries that number.",
      how:"Each source is an arc sized to its share, with a legend listing the exact percentages.",
      look:"The size of the coal slice against everything else." },
    'c-nfhs': { tag:'Health & Nutrition', title:"Two decades of progress, and one row that won't move",
      takeaway:"Services improved a lot across three surveys. Women's anaemia did not — and by the latest round it is slightly worse.",
      source:"National Family Health Survey rounds 3 (2005–06), 4 (2015–16) and 5 (2019–21).",
      why:"A heatmap is good for a small grid you want to scan in both directions. Every indicator is framed in the positive direction, so one green scale reads honestly: greener is always better.",
      how:"Each cell is coloured by its value on a single green scale, with the number printed in the cell so colour and figure agree.",
      look:"Most rows turn greener from left to right. The bottom row doesn't." },
    'c-upset-deprivation': { tag:'Poverty · Method', title:'Deprivation travels in packs',
      takeaway:"Only 21 of 706 districts clear all six thresholds. The single biggest group \u2014 129 districts \u2014 carries five at once: stunting, anaemia, child marriage, no clean cooking fuel and women under-schooled. The one it does not include is sanitation.",
      source:"NFHS-5 (2019-21) district fact sheets, IIPS/MoHFW. Thresholds: stunting \u226530% and women's anaemia \u226540% are the WHO 'very high' and 'severe public health problem' marks; the other three are stated on the chart.",
      why:"A Venn diagram cannot be drawn honestly for six sets, and six separate bars actively mislead: reading 63%, 90%, 50%, 8%, 75% and 46% invites you to picture six different sets of places. An UpSet plot answers the question those bars cannot \u2014 whether the same district carries several at once. That is what 'multidimensional' poverty means, and it is the only chart form that shows it directly.",
      how:"Every column is one exact combination. The dots below say which deprivations are in it, joined by a line; the bar above says how many districts have that combination and nothing else. The small bars on the left are how common each deprivation is on its own.",
      look:"The tall column five dots deep, and which row its line skips. Sanitation is the one dimension that broke away from the pack." },
    'c-upset-backwards': { tag:'Health & Nutrition', title:'What went backwards',
      takeaway:"Between the two rounds, sanitation went backwards in 20 districts and clean cooking fuel in 13. Women's anaemia went backwards in 353, and children's in 401 \u2014 and in 128 districts the two worsened together, the largest single pattern of reversal.",
      source:"NFHS-4 (2015-16) and NFHS-5 (2019-21) district fact sheets, IIPS/MoHFW. 574 districts have comparable values on all eight indicators.",
      why:"National averages can hide who moved and who did not. Counting the districts that went the wrong way, and then asking which reversals travelled together, separates a broad retreat from a handful of unlucky places \u2014 something a line of national averages cannot do.",
      how:"Same reading as the chart above: a column is one exact combination of indicators that worsened, the dots say which, and the bar says how many districts.",
      look:"How short the infrastructure rows are against the two anaemia rows. Things the state builds improved almost everywhere; things measured in people's blood did not." },
    'c-forest': { tag:'Climate · Evidence', title:'How hot, by 2100?',
      takeaway:"Only the lowest-emission paths stay near the 1.5°C and 2°C limits; the higher ones pass them comfortably.",
      source:"IPCC Sixth Assessment Report (AR6, WG1, 2021): best estimate and 'very likely' range by scenario.",
      why:"A forest plot shows a point estimate and its uncertainty range on the same row, so you compare both the central number and how sure we are. It's the standard way to show estimates with intervals.",
      how:"Each scenario is a row: a dot for the best estimate, a whisker for the very likely range, with the Paris 1.5°C and 2°C lines marked.",
      look:"Where each whisker sits relative to the two dashed Paris lines." },
    'c-poverty': { tag:'Poverty', title:'The great escape',
      takeaway:"The share of people in extreme poverty fell from about 38% to under 9% in one generation.",
      source:"World Bank Poverty & Inequality Platform, via Our World in Data ($2.15/day, 2017 PPP).",
      why:"A line over time is the clearest way to show a trend. The filled area under it gives the fall some weight without adding any new information.",
      how:"A smooth line through the data points, endpoints labelled, axis starting at zero so the drop isn't exaggerated.",
      look:"The steady fall, and the two endpoint numbers." },
    'c-u5mr': { tag:'Child Survival', title:'India’s children, 1990–2022',
      takeaway:"Under-five deaths fell from 127 to about 30 per 1,000 — a child today is roughly four times as likely to reach age five.",
      source:"UN Inter-agency Group for Child Mortality Estimation / World Bank (SH.DYN.MORT).",
      why:"A line over time, the right tool for one number falling across decades. Eight survey years keep the real shape rather than just joining two ends.",
      how:"A smooth line with a marker at each survey year and the first and last values labelled.",
      look:"How steep the early-2000s fall is, and where it flattens." },
    'c-flfp': { tag:'Gender & Work', title:'Women re-enter the workforce',
      takeaway:"After years of decline, women's recorded participation has risen sharply — though much of it is unpaid family work.",
      source:"Periodic Labour Force Survey (PLFS), MoSPI; usual status, women aged 15+.",
      why:"A short line shows the recent turn upward clearly. We plot the official survey rounds rather than smoothing over the gaps between them.",
      how:"A line through four PLFS rounds, area filled, endpoints labelled.",
      look:"The direction — up — and the caveat in the caption about what kind of work it is." },
    'c-pipeline': { tag:'Education', title:'The leaky pipeline',
      takeaway:"The gender gap in enrolment is mostly closed, but only about 1 in 4 young women reaches higher education.",
      source:"UDISE+ 2021–22 (school) and AISHE 2021–22 (higher education); female gross enrolment ratio by level.",
      why:"A funnel shows a quantity shrinking through stages — enrolment falling from primary to higher education — so the drop-off itself is the picture.",
      how:"Centred bars, each narrower than the last, sized to the enrolment ratio at that level.",
      look:"How much narrower each band gets, especially after secondary." },
    'c-climate': { tag:'Climate', title:'India is heating up',
      takeaway:"2024 was India's warmest year since 1901. How big the number looks depends on the baseline you pick.",
      source:"India Meteorological Department gridded data (1901–2024), via Data for India.",
      why:"This one is closer to a single-number readout than a chart — the point is one figure and how the choice of baseline changes it. The colour band is a schematic of the trend, not per-year data.",
      how:"A coloured gradient with the headline anomaly, and the same year shown against three different baselines.",
      look:"How the same warming reads as +0.65, +0.78 or +0.98 depending on the comparison period." },
    'c-le': { tag:'Health', title:'Living longer',
      takeaway:"A child born in India in 1960 could expect to live to about 45. By 2019 that had reached nearly 71 — a full human generation added in six decades.",
      source:"World Bank Open Data — life expectancy at birth, India (SP.DYN.LE00.IN), 1960–2019. The series stops at 2019 to keep the pandemic dip from distorting the trend.",
      why:"A line over time is the clearest way to read a long, steady climb. The filled area gives the gain some weight without adding any new information; the axis starts near the earliest value so the rise is neither exaggerated nor hidden.",
      how:"A smooth line through decadal values, ending in 2019, with each point plotted on a shared vertical scale.",
      look:"The steady, almost straight climb — and how much of it came before 2000." },
    'c-solar': { tag:'Energy', title:'The solar surge',
      takeaway:"India's installed solar capacity has grown more than thirty-fold in a decade — from under 3 GW in 2014 to about 87 GW in 2024.",
      source:"Ministry of New & Renewable Energy (MNRE) — installed grid-connected solar capacity, 2014–2024 (approximate).",
      why:"A line makes an exponential-looking climb legible, and the area beneath it conveys the sheer scale of build-out. Gigawatts on a zero-based axis keep the steepness honest.",
      how:"Installed capacity in gigawatts plotted every two years and joined into a line, area filled beneath.",
      look:"How the curve steepens after 2018 — the build-out is accelerating, not just continuing." },
    'c-urban': { tag:'Population', title:'India goes urban',
      takeaway:"In 1960 fewer than one in five Indians lived in a town or city. By 2023 it was more than one in three, and a majority-urban India is now in sight.",
      source:"World Bank — urban population as a share of total, India (SP.URB.TOTL.IN.ZS), 1960–2023.",
      why:"A share over time is best read as a line: the slope is the pace of urbanisation. A zero-based percentage axis keeps a slow-but-relentless shift from looking either flat or dramatic.",
      how:"Urban share of population plotted at intervals from 1960 to 2023 and joined into a filled line.",
      look:"The unbroken upward slope — India has never de-urbanised, only slowed or sped up." },
    'c-gdp': { tag:'Economy', title:'What India produces',
      takeaway:"Services make up over half of everything India produces, yet agriculture — under a fifth of output — still employs the largest share of workers. That gap is the heart of the jobs debate.",
      source:"MoSPI / National Accounts Statistics — gross value added by broad sector, 2023–24 (approximate shares).",
      why:"For a part-to-whole split with three pieces, a ring reads cleanly and the centre can carry the headline share. It answers one question — how the economy divides — without pretending to more precision than three round numbers.",
      how:"Each sector is an arc sized to its share of gross value added, with the services share called out in the centre.",
      look:"How large the services arc is next to agriculture — and remember that employment splits almost the opposite way." },
    'c-literacy': { tag:'Education', title:'Literacy, state by state',
      takeaway:"The national average hides a wide spread: Kerala is near-universal at 96%, while Bihar sits around 62% — the same country, a generation apart in schooling.",
      source:"NSO Household Social Consumption / Periodic Labour Force Survey estimates, 2022–23 (adult literacy, approximate).",
      why:"A bar chart is the honest choice for comparing a handful of places — length is easy to judge — and a dashed line at the national average lets each state read as above or below it at a glance.",
      how:"Horizontal bars from zero, ordered high to low, with a dashed line marking the national average.",
      look:"The distance between the top and bottom bars, and which side of the national line each state falls on." },
    'c-womenparl': { tag:'Gender & Power', title:'Women in parliament',
      takeaway:"Women hold about 14% of seats in India's Lok Sabha — below the world average of 27%, and a fraction of Rwanda's 61%. The Women's Reservation Act, once in force, would lift it toward a third.",
      source:"Inter-Parliamentary Union (IPU) — women in the lower or single house of parliament, 2024 (%).",
      why:"A beeswarm shows every country as a dot on one axis, so the whole spread is visible — the cluster of low shares and the lonely leaders — rather than a single average. India is highlighted against the pack.",
      how:"Each country is placed at its value and nudged to avoid overlap; India is coloured, with a dashed line at the world average.",
      look:"How far below the world-average line India sits, and how alone Rwanda is on the right." }
  };

  return {
    renderAll: renderAll, drawMasters: drawMasters, buildCards: buildCards,
    wireFilters: wireFilters, heroDots: heroDots, reveal: reveal, VIZ: VIZ,
    ORDER: ORDER, DETAILS: DETAILS
  };
})();
