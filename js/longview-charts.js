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
      svg.appendChild(mk('text', { x: mL + 16, y: 18, 'font-size': 11, 'font-weight': 800, fill: o.hlColor, 'font-family': 'Inter, sans-serif' }, hl.label + ' — ' + hl.v + ' t' ));
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

  /* ---------- Render everything ---------- */
  function renderAll() {
    lineChart('c-poverty',
      [{x:1990,y:37.9},{x:2000,y:29.7},{x:2010,y:16.7},{x:2015,y:10.4},{x:2019,y:8.4}],
      { yMax: 44, color: '#0d9488', area: true, valfmt: function(v){return v+'%';}, xfmt: function(x){return "'"+String(x).slice(2);} });

    lineChart('c-u5mr',
      [{x:1990,y:127},{x:1995,y:109.7},{x:2000,y:91.8},{x:2005,y:74.3},{x:2010,y:58.1},{x:2015,y:43.7},{x:2020,y:33},{x:2022,y:29.5}],
      { yMax: 138, color: '#4f46e5', area: true, valfmt: function(v){return Math.round(v);}, labelEvery: 2, xfmt: function(x){return "'"+String(x).slice(2);} });

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
    ethicChart('c-ethic');

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
    { theme:'india', tag:'India & South Asia', title:'Reuters Graphics', who:'Reuters', year:'ongoing', g:['#dd6b20','#e53e3e'], desc:'Award-winning visual investigations, often on South Asia — migrant labour, heat, elections. A reference standard for newsroom dataviz craft.', url:'https://www.reuters.com/graphics/' }
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

  var ORDER = ['c-gender','c-caste','c-co2','c-energy','c-nfhs','c-forest','c-poverty','c-u5mr','c-flfp','c-pipeline','c-climate'];
  var DETAILS = {
    'c-gender': { tag:'Gender', title:'The same gap, four ways',
      takeaway:"Women have caught up with men in college enrolment, and slightly passed them. In paid work and Parliament, they're still far behind.",
      source:"NFHS-5 (literacy), AISHE 2021–22 (college GER), PLFS 2023–24 (labour force), Lok Sabha 2024 (seats).",
      why:"A dumbbell chart puts two values on one line so the gap between them is the first thing you read. Stacking four indicators lets you compare gaps at a glance — and spot the one place the gap reverses.",
      how:"Drawn in plain SVG: a faint connecting line per row, a dot for each sex, values at the ends. No charting library — just the figures and a little geometry.",
      look:"The length of each grey line is the gap. Look at college, where the women's dot sits to the right of the men's." },
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
      look:"How the same warming reads as +0.65, +0.78 or +0.98 depending on the comparison period." }
  };

  return {
    renderAll: renderAll, drawMasters: drawMasters, buildCards: buildCards,
    wireFilters: wireFilters, heroDots: heroDots, reveal: reveal, VIZ: VIZ,
    ORDER: ORDER, DETAILS: DETAILS
  };
})();
